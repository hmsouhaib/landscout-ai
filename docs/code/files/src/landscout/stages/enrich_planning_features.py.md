# `src/landscout/stages/enrich_planning_features.py`

## File identity

- Repository path: `src/landscout/stages/enrich_planning_features.py`
- File type: Python source
- Primary responsibility: Normalizes GPU planning feature catalogs and constructs validated factual parcel-feature relations.
- Layer / domain: `stage` / `planning`
- Public or internal role: Contains an explicit module/package export surface; helpers prefixed with `_` remain internal unless re-exported elsewhere.
- Source SHA256: `01a56b482a3c956d1f8a7069b94c69518758ea3937c3d98ef8ae5d74615d6148`

## 1. Purpose

Normalizes GPU planning feature catalogs and constructs validated factual parcel-feature relations.

## 2. Position in LandScout architecture

This file is a `stage` artifact in the `planning` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from __future__ import annotations` — required by the implementation paths and symbols documented below.
- `import json` — required by the implementation paths and symbols documented below.
- `from dataclasses import dataclass, replace` — required by the implementation paths and symbols documented below.
- `from datetime import date, datetime` — required by the implementation paths and symbols documented below.
- `from hashlib import sha256` — required by the implementation paths and symbols documented below.
- `from math import isfinite` — required by the implementation paths and symbols documented below.
- `from numbers import Integral, Real` — required by the implementation paths and symbols documented below.
- `from typing import Literal, NamedTuple` — required by the implementation paths and symbols documented below.

### Third-party

- `import geopandas as gpd` — required by the implementation paths and symbols documented below.
- `import numpy as np` — required by the implementation paths and symbols documented below.
- `import pandas as pd` — required by the implementation paths and symbols documented below.
- `from pyproj import CRS` — required by the implementation paths and symbols documented below.
- `from shapely import ( # type: ignore[import-untyped] area as shapely_area, )` — required by the implementation paths and symbols documented below.
- `from shapely import ( contains, covers, force_2d, get_coordinate_dimension, get_parts, intersection, union_all, )` — required by the implementation paths and symbols documented below.
- `from shapely import ( length as shapely_length, )` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout.common.frame_integrity import deterministic_frame_schema_signature` — required by the implementation paths and symbols documented below.
- `from landscout.common.planning_feature_contract import ( validate_intrinsic_planning_feature_relations, )` — required by the implementation paths and symbols documented below.
- `from landscout.common.planning_feature_schema import ( NORMALIZED_FEATURE_COLUMNS, NORMALIZED_FEATURE_DTYPES, NORMALIZED_RELATION_DTYPES, RELATION_COLUMNS, RELATION_COUNT_COLUMNS, RELATION_FLOAT_COLUMNS, RELATION_STRING_COLUMNS, normalized_feature_dtypes, validate_canonical_frame_schema, )` — required by the implementation paths and symbols documented below.
- `from landscout.common.planning_overlay import technical_overlay_tolerance` — required by the implementation paths and symbols documented below.
- `from landscout.sources.gpu_fr import ( GpuInspectedLayer, GpuPlanningDocument, GpuSpatialInspectionError, GpuValidatedSpatialLayerSource, revalidate_gpu_spatial_layer_sources, )` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `CALCULATION_CRS` | `"EPSG:2154"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `PARCEL_REQUIRED_COLUMNS` | `frozenset({"parcel_id", "geometry"})` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `SOURCE_IDENTITY_KINDS` | `frozenset({"CNIG_ATTRIBUTE", "ARCHIVE_SCOPED_OGR_FID"})` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `SURFACE_TYPES` | `frozenset({"Polygon", "MultiPolygon"})` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `LINE_TYPES` | `frozenset({"LineString", "MultiLineString"})` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `POINT_TYPES` | `frozenset({"Point", "MultiPoint"})` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `LAYER_SPECS` | `{ "prescription_surface": _LayerSpec( "prescription_surface", "PRESCRIPTION", "SURFACE", "LIB_IDPSC", "TYPEPSC", "STYPEPSC", SURFACE_TYPES, ), "prescription_line": _LayerSpec( "prescription_line", "PRESCRIPTION", "LINE", "LIB_IDPSC", "TYPEPSC", "STYPEPSC", LINE_TYPES, ), "prescription_point": _LayerSpec( "prescription_point", "PRESCRIPTION", "POINT", "LIB_IDPSC", "TYPEPSC", "STYPEPSC", POINT_TYPES, ), "information_surface": _LayerSpec( "information_surface", "INFORMATION", "SURFACE", "LIB_IDINFO", "TYPEINF", "STYPEINF", SURFACE_TYPES, ), "information_line": _LayerSpec( "information_line", "INFORMATION", "LINE", "LIB_IDINFO", "TYPEINF", "STYPEINF", LINE_TYPES, ), "information_point": _LayerSpec( "information_point", "INFORMATION", "POINT", "LIB_IDINFO", "TYPEINF", "STYPEINF", POINT_TYPES, ), }` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `COMMON_SOURCE_FIELDS` | `{ "label_raw": "LIBELLE", "text_raw": "TXT", "regulation_filename_raw": "NOMFIC", "regulation_url_raw": "URLFIC", "source_document_reference_raw": "IDURBA", "source_validity_date_raw": "DATVALID", }` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `OPTIONAL_SOURCE_FIELDS` | `frozenset( { "LIBELLE", "TXT", "NOMFIC", "URLFIC", "DATVALID", } )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_CATALOG_GEOMETRY_TYPES` | `{ "SURFACE": SURFACE_TYPES, "LINE": LINE_TYPES, "POINT": POINT_TYPES, }` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_CATALOG_REQUIRED_EXACT_STRING_COLUMNS` | `( "planning_feature_id", "source_feature_id", "source_identity_kind", "source_identity_field", "logical_layer", "feature_family", "geometry_kind", "type_code_raw", "subtype_code_raw", "source_document_reference_raw", "source_provider", "source_portal", "source_commune_code", "source_document_id", "source_document_type", "source_archive_name", "source_archive_sha256", "source_layer", "source_crs", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_CATALOG_OPTIONAL_EXACT_STRING_COLUMNS` | `( "label_raw", "text_raw", "regulation_filename_raw", "regulation_url_raw", "source_validity_date_raw", "source_standard_model", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `PARCEL_OUTPUT_COLUMNS` | `frozenset( { "planning_surface_relation_count", "planning_surface_area_overlap_count", "planning_surface_touch_count", "planning_surface_intersection_area_sum_m2", "planning_surface_covered_union_area_m2", "planning_surface_covered_pct", "prescription_surface_relation_count", "prescription_surface_covered_union_area_m2", "prescription_surface_covered_pct", "information_surface_relation_count", "information_surface_covered_union_area_m2", "information_surface_covered_pct", "planning_line_relation_count", "planning_line_length_overlap_count", "planning_line_touch_count", "planning_line_intersection_length_sum_m", "planning_point_relation_count", "planning_point_inside_count", "planning_point_boundary_count", "planning_feature_document_id", "planning_feature_archive_sha256", } )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `PARCEL_COUNT_COLUMNS` | `frozenset( { "planning_surface_relation_count", "planning_surface_area_overlap_count", "planning_surface_touch_count", "prescription_surface_relation_count", "information_surface_relation_count", "planning_line_relation_count", "planning_line_length_overlap_count", "planning_line_touch_count", "planning_point_relation_count", "planning_point_inside_count", "planning_point_boundary_count", } )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_RELATION_CATALOG_FIELDS` | `( "source_feature_id", "source_identity_kind", "source_identity_field", "logical_layer", "feature_family", "geometry_kind", "type_code_raw", "subtype_code_raw", "label_raw", "text_raw", "source_document_id", "source_archive_sha256", "source_layer", "source_validity_date_raw", "regulation_filename_raw", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

### `_LayerSpec`

**Purpose:** Groups the `LayerSpec` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `NamedTuple`.

**Model form and mutability:** class inheriting from `NamedTuple`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `logical_layer` | `str` | `required` | `str` state used by `src/landscout/stages/enrich_planning_features.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `feature_family` | `FeatureFamily` | `required` | `FeatureFamily` state used by `src/landscout/stages/enrich_planning_features.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `geometry_kind` | `GeometryKind` | `required` | `GeometryKind` state used by `src/landscout/stages/enrich_planning_features.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `identity_field` | `str` | `required` | `str` state used by `src/landscout/stages/enrich_planning_features.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `type_field` | `str` | `required` | `str` state used by `src/landscout/stages/enrich_planning_features.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `subtype_field` | `str` | `required` | `str` state used by `src/landscout/stages/enrich_planning_features.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `allowed_geometry_types` | `frozenset[str]` | `required` | `frozenset[str]` state used by `src/landscout/stages/enrich_planning_features.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `PlanningFeaturesError`

**Purpose:** Raised when factual GPU feature measurement cannot be completed safely.

**Inheritance:** `ValueError`.

**Model form and mutability:** class inheriting from `ValueError`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

### `ParcelPlanningFeaturesResult`

**Purpose:** Normalized feature catalogs, parcel enrichment, and factual relations.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `parcels` | `gpd.GeoDataFrame` | `required` | Tabular/spatial evidence carried with the schema, dtype, index, geometry, and preservation contract documented in this module. |
| `surface_features` | `gpd.GeoDataFrame` | `required` | Tabular/spatial evidence carried with the schema, dtype, index, geometry, and preservation contract documented in this module. |
| `line_features` | `gpd.GeoDataFrame` | `required` | Tabular/spatial evidence carried with the schema, dtype, index, geometry, and preservation contract documented in this module. |
| `point_features` | `gpd.GeoDataFrame` | `required` | Tabular/spatial evidence carried with the schema, dtype, index, geometry, and preservation contract documented in this module. |
| `relations` | `pd.DataFrame` | `required` | Tabular/spatial evidence carried with the schema, dtype, index, geometry, and preservation contract documented in this module. |

**Validators and methods:**

- None.

### `PlanningFeatureInputValidation`

**Purpose:** Immutable source-completeness evidence for normalized planning facts.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `gpu_related_source_files_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `expected_relations_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `related_source_layer_count` | `int` | `required` | Strict count; Boolean coercion is rejected where the model/validator requires an exact integer. |
| `related_source_file_count` | `int` | `required` | Strict count; Boolean coercion is rejected where the model/validator requires an exact integer. |
| `expected_relation_count` | `int` | `required` | Strict count; Boolean coercion is rejected where the model/validator requires an exact integer. |

**Validators and methods:**

- None.

### `_PlanningContext`

**Purpose:** Groups the `PlanningContext` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `provider` | `str` | `required` | `str` state used by `src/landscout/stages/enrich_planning_features.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `portal` | `str` | `required` | `str` state used by `src/landscout/stages/enrich_planning_features.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `commune_code` | `str` | `required` | Exact configured or source code whose vocabulary/format is enforced by the owning validator. |
| `document_id` | `str` | `required` | Exact portable identity used to join lineage or evidence across frames and result envelopes. |
| `document_type` | `str` | `required` | Categorical source, feature, or relation type constrained by the owning model or validator. |
| `archive_name` | `str` | `required` | `str` state used by `src/landscout/stages/enrich_planning_features.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `archive_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `standard_model` | `str | None` | `required` | `str | None` state used by `src/landscout/stages/enrich_planning_features.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

## 6. Functions and methods

### `_strict_string`

**Signature**

```python
def _strict_string(value: object, label: str) -> str:
```

**Purpose**

Implements strict string according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `value`.

**Algorithm**

1. Checks `not isinstance(value, str) or not value or value != value.strip()`. When true: Raises `PlanningFeaturesError(f'{label} must be a non-empty exact string')`.
2. Returns `value`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(value, str) or not value or value != value.strip()` is true.

**Exceptions**

- Explicitly raises: `PlanningFeaturesError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningFeaturesError`, `isinstance`, `value.strip`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `_normalize_layer`
- `src/landscout/stages/enrich_planning_features.py` — `_planning_context`
- `src/landscout/stages/enrich_planning_features.py` — `_standard_model`
- `src/landscout/stages/enrich_planning_features.py` — `_validate_catalog_identity`
- `src/landscout/stages/enrich_planning_features.py` — `_validate_exact_strings`
- `src/landscout/stages/enrich_planning_features.py` — `_validate_optional_exact_strings`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

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

- Declared return type: `int`. Observed return expression(s): `int(value)`.

**Algorithm**

1. Checks `isinstance(value, bool) or not isinstance(value, Integral)`. When true: Raises `PlanningFeaturesError(f'{label} must be an integer count')`.
2. Checks `value < 0`. When true: Raises `PlanningFeaturesError(f'{label} must be non-negative')`.
3. Returns `int(value)`.

**Validation and invariants**

- Rejects or diverts the path when `isinstance(value, bool) or not isinstance(value, Integral)` is true.
- Rejects or diverts the path when `value < 0` is true.

**Exceptions**

- Explicitly raises: `PlanningFeaturesError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningFeaturesError`, `int`, `isinstance`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `_integer_values`
- `src/landscout/stages/enrich_planning_features.py` — `_validate_layer_summary`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_ids`

**Signature**

```python
def _validate_ids(values: pd.Series, label: str) -> None:
```

**Purpose**

Validates and rejects malformed ids according to the exact implementation and guards in this file.

**Inputs**

- `values` (`pd.Series`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Calls `_validate_exact_strings(values, label)` for its validation or side effect.
2. Checks `values.duplicated().any()`. When true: Raises `PlanningFeaturesError(f'{label} values must be unique')`.

**Validation and invariants**

- Rejects or diverts the path when `values.duplicated().any()` is true.

**Exceptions**

- Explicitly raises: `PlanningFeaturesError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningFeaturesError`, `_validate_exact_strings`, `values.duplicated`, `values.duplicated().any`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `_combine_catalogs`
- `src/landscout/stages/enrich_planning_features.py` — `_source_feature_ids`
- `src/landscout/stages/enrich_planning_features.py` — `_validate_catalog_identity`
- `src/landscout/stages/enrich_planning_features.py` — `_validate_parcels`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_exact_strings`

**Signature**

```python
def _validate_exact_strings(values: pd.Series, label: str) -> None:
```

**Purpose**

Validates and rejects malformed exact strings according to the exact implementation and guards in this file.

**Inputs**

- `values` (`pd.Series`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `values.isna().any()`. When true: Raises `PlanningFeaturesError(f'{label} values must not be null')`.
2. Iterates `value` over `values.tolist()`. For each value: Calls `_strict_string(value, label)` for its validation or side effect.

**Validation and invariants**

- Rejects or diverts the path when `values.isna().any()` is true.

**Exceptions**

- Explicitly raises: `PlanningFeaturesError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningFeaturesError`, `_strict_string`, `values.isna`, `values.isna().any`, `values.tolist`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `_validate_catalog_identity`
- `src/landscout/stages/enrich_planning_features.py` — `_validate_ids`
- `src/landscout/stages/enrich_planning_features.py` — `_validate_normalized_planning_feature_inputs`
- `src/landscout/stages/enrich_planning_features.py` — `_validate_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_optional_exact_strings`

**Signature**

```python
def _validate_optional_exact_strings(values: pd.Series, label: str) -> None:
```

**Purpose**

Validates and rejects malformed optional exact strings according to the exact implementation and guards in this file.

**Inputs**

- `values` (`pd.Series`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Iterates `value` over `values.tolist()`. For each value: Checks `pd.isna(value)`. When true: Executes `continue` control flow. Calls `_strict_string(value, label)` for its validation or side effect.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_strict_string`, `pd.isna`, `values.tolist`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `_validate_catalog_identity`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_crs`

**Signature**

```python
def _crs(value: object, label: str) -> CRS:
```

**Purpose**

Implements crs according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `CRS`. Observed return expression(s): `CRS.from_user_input(value)`.

**Algorithm**

1. Checks `value is None`. When true: Raises `PlanningFeaturesError(f'{label} CRS is required')`.
2. Runs guarded operation: Returns `CRS.from_user_input(value)`. Handles `Exception`.

**Validation and invariants**

- Rejects or diverts the path when `value is None` is true.

**Exceptions**

- Explicitly raises: `PlanningFeaturesError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `CRS.from_user_input`, `PlanningFeaturesError`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `_compare_normalized_catalog`
- `src/landscout/stages/enrich_planning_features.py` — `_compare_rebuilt_parcel_output`
- `src/landscout/stages/enrich_planning_features.py` — `_project_geometry`
- `src/landscout/stages/enrich_planning_features.py` — `_validate_layer_summary`
- `src/landscout/stages/enrich_planning_features.py` — `_validate_parcels`

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

1. Checks `'geometry' not in frame.columns`. When true: Raises `PlanningFeaturesError(f'{label} geometry column is required')`.
2. Runs guarded operation: Computes `active` from `frame.active_geometry_name`. Handles `AttributeError`.
3. Checks `active != 'geometry'`. When true: Raises `PlanningFeaturesError(f'{label} geometry must be active')`.

**Validation and invariants**

- Rejects or diverts the path when `'geometry' not in frame.columns` is true.
- Rejects or diverts the path when `active != 'geometry'` is true.

**Exceptions**

- Explicitly raises: `PlanningFeaturesError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningFeaturesError`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `_normalize_layer`
- `src/landscout/stages/enrich_planning_features.py` — `_validate_catalog_contract`
- `src/landscout/stages/enrich_planning_features.py` — `_validate_parcels`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_geometries`

**Signature**

```python
def _validate_geometries(
    frame: gpd.GeoDataFrame,
    allowed: frozenset[str],
    label: str,
) -> None:
```

**Purpose**

Validates and rejects malformed geometries according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `allowed` (`frozenset[str]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `geometry` from `frame.geometry`.
2. Checks `geometry.isna().any()`. When true: Raises `PlanningFeaturesError(f'{label} geometry must not be null')`.
3. Checks `geometry.is_empty.any()`. When true: Raises `PlanningFeaturesError(f'{label} geometry must not be empty')`.
4. Checks `not geometry.is_valid.all()`. When true: Raises `PlanningFeaturesError(f'{label} geometry must be valid')`.
5. Computes `found` from `set(geometry.geom_type)`.
6. Checks `not found.issubset(allowed)`. When true: Raises `PlanningFeaturesError(f'{label} has unsupported geometry types: ' + ', '.join(sorted(found - allowed)))`.

**Validation and invariants**

- Rejects or diverts the path when `geometry.isna().any()` is true.
- Rejects or diverts the path when `geometry.is_empty.any()` is true.
- Rejects or diverts the path when `not geometry.is_valid.all()` is true.
- Rejects or diverts the path when `not found.issubset(allowed)` is true.

**Exceptions**

- Explicitly raises: `PlanningFeaturesError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `', '.join`, `PlanningFeaturesError`, `found.issubset`, `geometry.is_empty.any`, `geometry.is_valid.all`, `geometry.isna`, `geometry.isna().any`, `set`, `sorted`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `_normalize_layer`
- `src/landscout/stages/enrich_planning_features.py` — `_validate_catalog_contract`
- `src/landscout/stages/enrich_planning_features.py` — `_validate_parcels`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_two_dimensional_geometry`

**Signature**

```python
def _validate_two_dimensional_geometry(
    frame: gpd.GeoDataFrame,
    label: str,
) -> None:
```

**Purpose**

Validates and rejects malformed two dimensional geometry according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Runs guarded operation: Computes `dimensions` from `np.asarray(get_coordinate_dimension(frame.geometry.array), dtype='int64')`. Checks `(dimensions != 2).any()`. When true: Raises `PlanningFeaturesError(f'{label} geometry must be canonical 2D')`. Handles `PlanningFeaturesError`, `Exception`.

**Validation and invariants**

- Rejects or diverts the path when `(dimensions != 2).any()` is true.

**Exceptions**

- Explicitly raises: `PlanningFeaturesError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `(dimensions != 2).any`, `PlanningFeaturesError`, `get_coordinate_dimension`, `np.asarray`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `_validate_catalog_contract`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_parcels`

**Signature**

```python
def _validate_parcels(
    parcels: gpd.GeoDataFrame,
    *,
    allow_output_columns: bool = False,
) -> CRS:
```

**Purpose**

Validates and rejects malformed parcels according to the exact implementation and guards in this file.

**Inputs**

- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `allow_output_columns` (`bool`; optional/default `False`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `CRS`. Observed return expression(s): `source_crs`.

**Algorithm**

1. Checks `not isinstance(parcels, gpd.GeoDataFrame)`. When true: Raises `PlanningFeaturesError('Parcels must be a GeoDataFrame')`.
2. Checks `parcels.columns.duplicated().any()`. When true: Raises `PlanningFeaturesError('Parcels contain duplicate columns')`.
3. Computes `missing` from `sorted(PARCEL_REQUIRED_COLUMNS - set(parcels.columns))`.
4. Checks `missing`. When true: Raises `PlanningFeaturesError('Parcels are missing required columns: ' + ', '.join(missing))`.
5. Computes `collisions` from `sorted(PARCEL_OUTPUT_COLUMNS & set(parcels.columns))`.
6. Checks `collisions and (not allow_output_columns)`. When true: Raises `PlanningFeaturesError('Parcels already contain planning-feature output columns: ' + ', '.join(collisions))`.
7. Calls `_active_geometry(parcels, 'Parcel')` for its validation or side effect.
8. Computes `source_crs` from `_crs(parcels.crs, 'Parcel')`.
9. Calls `_validate_ids(parcels['parcel_id'], 'parcel_id')` for its validation or side effect.
10. Calls `_validate_geometries(parcels, SURFACE_TYPES, 'Parcel')` for its validation or side effect.
11. Returns `source_crs`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(parcels, gpd.GeoDataFrame)` is true.
- Rejects or diverts the path when `parcels.columns.duplicated().any()` is true.
- Rejects or diverts the path when `missing` is true.
- Rejects or diverts the path when `collisions and (not allow_output_columns)` is true.

**Exceptions**

- Explicitly raises: `PlanningFeaturesError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `', '.join`, `PlanningFeaturesError`, `_active_geometry`, `_crs`, `_validate_geometries`, `_validate_ids`, `isinstance`, `parcels.columns.duplicated`, `parcels.columns.duplicated().any`, `set`, `sorted`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `_validate_normalized_planning_feature_inputs`
- `src/landscout/stages/enrich_planning_features.py` — `intersect_parcels_with_gpu_planning_features`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_standard_model`

**Signature**

```python
def _standard_model(document: GpuPlanningDocument) -> str | None:
```

**Purpose**

Implements standard model according to the exact implementation and guards in this file.

**Inputs**

- `document` (`GpuPlanningDocument`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str | None`. Observed return expression(s): `values[0] if values else None`.

**Algorithm**

1. Defines `values` with annotation `list[str]` from `[]`.
2. Computes `model` from `document.extraction.archive.document.standard_model`.
3. Checks `model is not None`. When true: Calls `values.append(_strict_string(model, 'GPU standard model'))` for its validation or side effect.
4. Iterates `value` over `document.extraction.standard_models`. For each value: Computes `validated` from `_strict_string(value, 'GPU extracted standard model')`. Checks `validated not in values`. When true: Calls `values.append(validated)` for its validation or side effect.
5. Checks `len(values) > 1`. When true: Raises `PlanningFeaturesError('GPU standard-model lineage is ambiguous')`.
6. Returns `values[0] if values else None`.

**Validation and invariants**

- Rejects or diverts the path when `len(values) > 1` is true.

**Exceptions**

- Explicitly raises: `PlanningFeaturesError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningFeaturesError`, `_strict_string`, `len`, `values.append`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `_planning_context`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_planning_context`

**Signature**

```python
def _planning_context(document: GpuPlanningDocument) -> _PlanningContext:
```

**Purpose**

Implements planning context according to the exact implementation and guards in this file.

**Inputs**

- `document` (`GpuPlanningDocument`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `_PlanningContext`. Observed return expression(s): `_PlanningContext(provider=_strict_string(metadata.provider, 'GPU provider'), portal=_strict_string(metadata.portal, 'GPU portal'), commune_code=_strict_string(metadata.commune_code, 'GPU commune code'), document_id=_strict_string(metadata.document_id, 'GPU document ID'), document_type=_strict_string(metadata.document_type, 'GPU document type'), archive_name=_strict_string(metadata.archive_name, '…`.

**Algorithm**

1. Checks `not isinstance(document, GpuPlanningDocument)`. When true: Raises `PlanningFeaturesError('planning_document must be a GpuPlanningDocument')`.
2. Computes `archive` from `document.extraction.archive`.
3. Computes `metadata` from `archive.document`.
4. Computes `sha` from `_strict_string(archive.sha256, 'GPU archive SHA256')`.
5. Checks `len(sha) != 64 or any((c not in '0123456789abcdefABCDEF' for c in sha))`. When true: Raises `PlanningFeaturesError('GPU archive SHA256 must contain 64 hex chars')`.
6. Returns `_PlanningContext(provider=_strict_string(metadata.provider, 'GPU provider'), portal=_strict_string(metadata.portal, 'GPU portal'), commune_code=_strict_string(metadata.commune_code, 'GPU commune code'), document_id=_strict_string(metadata.document_id, 'GPU document ID'), document_type=_strict_string(metadata.document_type, 'GPU document type'), archive_name…`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(document, GpuPlanningDocument)` is true.
- Rejects or diverts the path when `len(sha) != 64 or any((c not in '0123456789abcdefABCDEF' for c in sha))` is true.

**Exceptions**

- Explicitly raises: `PlanningFeaturesError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningFeaturesError`, `_PlanningContext`, `_standard_model`, `_strict_string`, `any`, `isinstance`, `len`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `_normalized_catalogs`
- `src/landscout/stages/enrich_planning_features.py` — `_validate_normalized_planning_feature_inputs`
- `src/landscout/stages/enrich_planning_features.py` — `intersect_parcels_with_gpu_planning_features`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_summary_geometry_types`

**Signature**

```python
def _summary_geometry_types(frame: gpd.GeoDataFrame) -> tuple[tuple[str, int], ...]:
```

**Purpose**

Implements summary geometry types according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[tuple[str, int], ...]`. Observed return expression(s): `tuple(((str(key), int(value)) for key, value in counts.items()))`.

**Algorithm**

1. Computes `counts` from `frame.geometry.geom_type.value_counts().sort_index()`.
2. Returns `tuple(((str(key), int(value)) for key, value in counts.items()))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `counts.items`, `frame.geometry.geom_type.value_counts`, `frame.geometry.geom_type.value_counts().sort_index`, `int`, `str`, `tuple`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `_validate_layer_summary`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_layer_summary`

**Signature**

```python
def _validate_layer_summary(
    layer: GpuInspectedLayer,
    context: _PlanningContext,
) -> None:
```

**Purpose**

Validates and rejects malformed layer summary according to the exact implementation and guards in this file.

**Inputs**

- `layer` (`GpuInspectedLayer`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `context` (`_PlanningContext`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `frame` from `layer.data`.
2. Computes `summary` from `layer.summary`.
3. Computes `actual_crs` from `_crs(frame.crs, f'{layer.logical_name} source')`.
4. Computes `summary_crs` from `_crs(summary.crs, f'{layer.logical_name} summary')`.
5. Computes `expected_nulls` from `tuple(((str(column), int(frame[column].isna().sum())) for column in frame.columns))`.
6. Computes `expected_dtypes` from `tuple(((str(column), str(dtype)) for column, dtype in frame.dtypes.items()))`.
7. Computes `geometry` from `frame.geometry`.
8. Computes `non_null` from `geometry.notna()`.
9. Computes `non_empty` from `non_null & ~geometry.is_empty`.
10. Calls `_strict_nonnegative_integer(summary.feature_count, 'summary feature_count')` for its validation or side effect.
11. Calls `_strict_nonnegative_integer(summary.null_geometry_count, 'summary null_geometry_count')` for its validation or side effect.
12. Calls `_strict_nonnegative_integer(summary.empty_geometry_count, 'summary empty_geometry_count')` for its validation or side effect.
13. Calls `_strict_nonnegative_integer(summary.invalid_geometry_count, 'summary invalid_geometry_count')` for its validation or side effect.
14. Iterates `(column, value)` over `summary.null_counts`. For each value: Calls `_strict_nonnegative_integer(value, f'summary {column} null count')` for its validation or side effect.
15. Iterates `(geometry_type, value)` over `summary.geometry_types`. For each value: Calls `_strict_nonnegative_integer(value, f'summary {geometry_type} count')` for its validation or side effect.
16. Checks `summary.source_document_id != context.document_id or summary.source_archive_sha256 != context.archive_sha256 or summary.source_layer != layer.reference.source_layer or (summary.feature_count != len(frame)) or (not actual_crs.equals(summary_crs)) or (summary.columns != tuple((str(column) for column in frame.columns))) or (summary.dtypes != expected_dtypes) o…`. When true: Raises `PlanningFeaturesError(f'{layer.logical_name} source summary is inconsistent with loaded data')`.

**Validation and invariants**

- Rejects or diverts the path when `summary.source_document_id != context.document_id or summary.source_archive_sha256 != context.archive_sha256 or summary.source_layer != layer.reference.source_layer or (summary.feature_count != len(frame)) or (not actual_crs.equals(summary_crs)) or (summary.columns != tuple((str(column) for column in frame.columns))) or (summary.dtypes != expected_dtypes) or (summary.null_counts != expected_nulls…` is true.

**Exceptions**

- Explicitly raises: `PlanningFeaturesError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `(non_empty & ~geometry.is_valid).sum`, `(non_null & geometry.is_empty).sum`, `(~non_null).sum`, `PlanningFeaturesError`, `_crs`, `_strict_nonnegative_integer`, `_summary_geometry_types`, `actual_crs.equals`, `frame.dtypes.items`, `frame[column].isna`, `frame[column].isna().sum`, `geometry.notna`, `int`, `len`, `str`, `tuple`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `_normalize_layer`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_project_geometry`

**Signature**

```python
def _project_geometry(frame: gpd.GeoDataFrame, label: str) -> gpd.GeoSeries:
```

**Purpose**

Implements project geometry according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoSeries`. Observed return expression(s): `gpd.GeoSeries(force_2d(projected.array), crs=target)`.

**Algorithm**

1. Computes `source` from `_crs(frame.crs, label)`.
2. Computes `target` from `CRS.from_epsg(2154)`.
3. Runs guarded operation: Computes `projected` from `frame.geometry.copy() if source.equals(target) else frame.to_crs(target).geometry`. Returns `gpd.GeoSeries(force_2d(projected.array), crs=target)`. Handles `Exception`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `PlanningFeaturesError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `frame.geometry.copy`, `frame.to_crs`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `CRS.from_epsg`, `PlanningFeaturesError`, `_crs`, `force_2d`, `frame.geometry.copy`, `frame.to_crs`, `gpd.GeoSeries`, `source.equals`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `_metric_parcels`
- `src/landscout/stages/enrich_planning_features.py` — `_normalize_layer`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_source_feature_ids`

**Signature**

```python
def _source_feature_ids(
    layer: GpuInspectedLayer,
    spec: _LayerSpec,
    validated_source: GpuValidatedSpatialLayerSource,
) -> tuple[pd.Series, SourceIdentityKind, str]:
```

**Purpose**

Implements source feature ids according to the exact implementation and guards in this file.

**Inputs**

- `layer` (`GpuInspectedLayer`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `spec` (`_LayerSpec`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `validated_source` (`GpuValidatedSpatialLayerSource`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[pd.Series, SourceIdentityKind, str]`. Observed return expression(s): `(result, 'CNIG_ATTRIBUTE', spec.identity_field)`; `(values, 'ARCHIVE_SCOPED_OGR_FID', 'OGR_FID')`; `(pd.Series(dtype='object'), 'ARCHIVE_SCOPED_OGR_FID', 'OGR_FID')`.

**Algorithm**

1. Checks `spec.identity_field in layer.data.columns`. When true: Computes `result` from `layer.data[spec.identity_field].reset_index(drop=True).copy()`. Calls `_validate_ids(result, spec.identity_field)` for its validation or side effect. Returns `(result, 'CNIG_ATTRIBUTE', spec.identity_field)`.
2. Checks `spec.logical_layer == 'prescription_surface'`. When true: Checks `layer.data.empty`. When true: Returns `(pd.Series(dtype='object'), 'ARCHIVE_SCOPED_OGR_FID', 'OGR_FID')`. Checks `len(validated_source.ogr_fids) != len(layer.data)`. When true: Raises `PlanningFeaturesError(f'{layer.logical_name} verified source FIDs are unavailable')`. Computes `values` from `pd.Series([f'OGR_FID:{value}' for value in validated_source.ogr_fids], dtype='object')`. Executes 2 additional source-ordered statement(s).
3. Raises `PlanningFeaturesError(f'{spec.logical_layer} is missing required identity field {spec.identity_field}')`.

**Validation and invariants**

- Rejects or diverts the path when `spec.logical_layer == 'prescription_surface'` is true.
- Rejects or diverts the path when `len(validated_source.ogr_fids) != len(layer.data)` is true.

**Exceptions**

- Explicitly raises: `PlanningFeaturesError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `layer.data[spec.identity_field].reset_index(drop=True).copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `PlanningFeaturesError`, `_validate_ids`, `layer.data[spec.identity_field].reset_index`, `layer.data[spec.identity_field].reset_index(drop=True).copy`, `len`, `pd.Series`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `_normalize_layer`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_optional_values`

**Signature**

```python
def _optional_values(frame: gpd.GeoDataFrame, source_field: str) -> np.ndarray:
```

**Purpose**

Implements optional values according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `source_field` (`str`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `np.ndarray`. Observed return expression(s): `frame[source_field].to_numpy(copy=True)`; `np.full(len(frame), None, dtype='object')`.

**Algorithm**

1. Checks `source_field not in frame.columns`. When true: Returns `np.full(len(frame), None, dtype='object')`.
2. Returns `frame[source_field].to_numpy(copy=True)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `frame[source_field].to_numpy`, `len`, `np.full`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `_normalize_layer`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_normalize_layer`

**Signature**

```python
def _normalize_layer(
    layer: GpuInspectedLayer,
    spec: _LayerSpec,
    context: _PlanningContext,
    validated_source: GpuValidatedSpatialLayerSource,
) -> gpd.GeoDataFrame:
```

**Purpose**

Normalizes layer according to the exact implementation and guards in this file.

**Inputs**

- `layer` (`GpuInspectedLayer`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `spec` (`_LayerSpec`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `context` (`_PlanningContext`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `validated_source` (`GpuValidatedSpatialLayerSource`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `projected`.

**Algorithm**

1. Computes `frame` from `layer.data`.
2. Checks `not isinstance(frame, gpd.GeoDataFrame)`. When true: Raises `PlanningFeaturesError(f'{spec.logical_layer} must be a GeoDataFrame')`.
3. Calls `_active_geometry(frame, spec.logical_layer)` for its validation or side effect.
4. Computes `required` from `{spec.type_field, spec.subtype_field, 'IDURBA', 'geometry'}`.
5. Computes `missing` from `sorted(required - set(frame.columns))`.
6. Checks `missing`. When true: Raises `PlanningFeaturesError(f'{spec.logical_layer} is missing required source fields: ' + ', '.join(missing))`.
7. Iterates `field` over `(spec.type_field, spec.subtype_field, 'IDURBA')`. For each value: Checks `frame[field].isna().any()`. When true: Raises `PlanningFeaturesError(f'{spec.logical_layer} {field} must not be null')`. Iterates `value` over `frame[field].tolist()`. For each value: Calls `_strict_string(value, f'{spec.logical_layer} {field}')` for its validation or side effect.
8. Calls `_validate_geometries(frame, spec.allowed_geometry_types, spec.logical_layer)` for its validation or side effect.
9. Calls `_validate_layer_summary(layer, context)` for its validation or side effect.
10. Computes `expected_reference` from `context.archive_name[:-4] if context.archive_name.casefold().endswith('.zip') else context.archive_name`.
11. Checks `not frame['IDURBA'].eq(expected_reference).all()`. When true: Raises `PlanningFeaturesError(f'{spec.logical_layer} IDURBA does not match planning archive identity')`.
12. Computes `(source_ids, identity_kind, identity_field)` from `_source_feature_ids(layer, spec, validated_source)`.
13. Computes `planning_ids` from `source_ids.map(lambda value: f'GPU:{context.document_id}:{spec.logical_layer}:{value}')`.
14. Computes `geometry` from `_project_geometry(frame, spec.logical_layer)`.
15. Computes `projected` from `gpd.GeoDataFrame({'planning_feature_id': planning_ids.to_numpy(copy=True), 'source_feature_id': source_ids.to_numpy(copy=True), 'source_identity_kind': np.repeat(identity_kind, len(frame)), 'source_identity_field': np.repeat(identity_field, len(frame)), 'logical_layer': np.repeat(spec.logical_layer, len(frame)), 'feat…`.
16. Calls `_validate_geometries(projected, spec.allowed_geometry_types, spec.logical_layer)` for its validation or side effect.
17. Checks `spec.geometry_kind == 'SURFACE'`. When true: Runs guarded operation: Computes `values` from `projected.geometry.area.to_numpy(dtype='float64')`. Handles `Exception`. Checks `not np.isfinite(values).all() or (values <= 0).any()`. When true: Raises `PlanningFeaturesError(f'{spec.logical_layer} areas must be positive')`. Computes `projected['feature_area_m2']` from `values`. Otherwise: Checks `spec.geometry_kind == 'LINE'`. When true: Runs guarded operation: Computes `values` from `projected.geometry.length.to_numpy(dtype='float64')`. Handles `Exception`. Checks `not np.isfinite(values).all() or (values <= 0).any()`. When true: Raises `PlanningFeaturesError(f'{spec.logical_layer} lengths must be positive')`. Computes `projected['feature_length_m']` from `values`. Otherwise: Runs guarded operation: Computes `projected['point_member_count']` from `[len(get_parts(value)) for value in projected.geometry.array]`. Handles `Exception`.
18. Returns `projected`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(frame, gpd.GeoDataFrame)` is true.
- Rejects or diverts the path when `missing` is true.
- Rejects or diverts the path when `not frame['IDURBA'].eq(expected_reference).all()` is true.
- Rejects or diverts the path when `spec.geometry_kind == 'SURFACE'` is true.
- Rejects or diverts the path when `frame[field].isna().any()` is true.
- Rejects or diverts the path when `not np.isfinite(values).all() or (values <= 0).any()` is true.
- Rejects or diverts the path when `spec.geometry_kind == 'LINE'` is true.

**Exceptions**

- Explicitly raises: `PlanningFeaturesError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `gpd.GeoDataFrame({'planning_feature_id': planning_ids.to_numpy(copy=True), 'source_feature_id': source_ids.to_numpy(copy=True), 'source_identity_kind': np.repeat(identity_kind, len(frame)), 'source_identity_field': np.repeat(identity_field, len(frame)), 'logical_layer': np.repeat(spec.logical_layer, len(frame)), 'feature_family': np.repeat(spec.feature_family, len(frame)), 'geometry_kind': np.repeat(spec.geometry_kind, len(frame)), 'type_code_raw': frame[spec.type_field].to_numpy(copy=True), 'subtype_code_raw': frame[spec.subtype_field].to_numpy(copy=True), **{normalized: _optional_values(frame, source) for normalized, source in COMMON_SOURCE_FIELDS.items()}, 'source_provider': np.repeat(context.provider, len(frame)), 'source_portal': np.repeat(context.portal, len(frame)), 'source_commune_code': np.repeat(context.commune_code, len(frame)), 'source_document_id': np.repeat(context.document_id, len(frame)), 'source_document_type': np.repeat(context.document_type, len(frame)), 'source_archive_name': np.repeat(context.archive_name, len(frame)), 'source_archive_sha256': np.repeat(context.archive_sha256, len(frame)), 'source_layer': np.repeat(layer.reference.source_layer, len(frame)), 'source_standard_model': np.full(len(frame), context.standard_model, dtype='object'), 'source_crs': np.repeat(layer.summary.crs, len(frame))}, geometry=geometry.to_numpy(copy=True), crs=CALCULATION_CRS).reset_index`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `', '.join`, `(values <= 0).any`, `COMMON_SOURCE_FIELDS.items`, `PlanningFeaturesError`, `_active_geometry`, `_optional_values`, `_project_geometry`, `_source_feature_ids`, `_strict_string`, `_validate_geometries`, `_validate_layer_summary`, `context.archive_name.casefold`, `context.archive_name.casefold().endswith`, `frame['IDURBA'].eq`, `frame['IDURBA'].eq(expected_reference).all`, `frame[field].isna`, `frame[field].isna().any`, `frame[field].tolist`, `frame[spec.subtype_field].to_numpy`, `frame[spec.type_field].to_numpy`, `geometry.to_numpy`, `get_parts`, `gpd.GeoDataFrame`, `gpd.GeoDataFrame({'planning_feature_id': planning_ids.to_numpy(copy=True), 'source_feature_id': source_ids.to_numpy(copy=True), 'source_identity_kind': np.repeat(identity_kind, len(frame)), 'source_identity_field': np.repeat(identity_field, len(frame)), 'logical_layer': np.repeat(spec.logical_layer, len(frame)), 'feature_family': np.repeat(spec.feature_family, len(frame)), 'geometry_kind': np.repeat(spec.geometry_kind, len(frame)), 'type_code_raw': frame[spec.type_field].to_numpy(copy=True), 'subtype_code_raw': frame[spec.subtype_field].to_numpy(copy=True), **{normalized: _optional_values(frame, source) for normalized, source in COMMON_SOURCE_FIELDS.items()}, 'source_provider': np.repeat(context.provider, len(frame)), 'source_portal': np.repeat(context.portal, len(frame)), 'source_commune_code': np.repeat(context.commune_code, len(frame)), 'source_document_id': np.repeat(context.document_id, len(frame)), 'source_document_type': np.repeat(context.document_type, len(frame)), 'source_archive_name': np.repeat(context.archive_name, len(frame)), 'source_archive_sha256': np.repeat(context.archive_sha256, len(frame)), 'source_layer': np.repeat(layer.reference.source_layer, len(frame)), 'source_standard_model': np.full(len(frame), context.standard_model, dtype='object'), 'source_crs': np.repeat(layer.summary.crs, len(frame))}, geometry=geometry.to_numpy(copy=True), crs=CALCULATION_CRS).reset_index`, `isinstance`, `len`, `np.full`, `np.isfinite`, `np.isfinite(values).all`, `np.repeat`, `planning_ids.to_numpy`, `projected.geometry.area.to_numpy`, `projected.geometry.length.to_numpy`, `set`, `sorted`, `source_ids.map`, `source_ids.to_numpy`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `_normalized_catalogs`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_canonical_catalog_dtypes`

**Signature**

```python
def _canonical_catalog_dtypes(
    catalog: gpd.GeoDataFrame,
    kind: GeometryKind,
) -> gpd.GeoDataFrame:
```

**Purpose**

Implements canonical catalog dtypes according to the exact implementation and guards in this file.

**Inputs**

- `catalog` (`gpd.GeoDataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `kind` (`GeometryKind`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `catalog`.

**Algorithm**

1. Iterates `(column, dtype)` over `zip(NORMALIZED_FEATURE_COLUMNS[kind], normalized_feature_dtypes(kind, catalog), strict=True)`. For each value: Checks `column == 'geometry'`. When true: Executes `continue` control flow. Computes `catalog[column]` from `pd.Series(catalog[column].tolist(), index=catalog.index, dtype=dtype)`.
2. Computes `catalog.index` from `pd.RangeIndex(len(catalog))`.
3. Returns `catalog`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `catalog[column].tolist`, `len`, `normalized_feature_dtypes`, `pd.RangeIndex`, `pd.Series`, `zip`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `_combine_catalogs`
- `src/landscout/stages/enrich_planning_features.py` — `_empty_catalog`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_empty_catalog`

**Signature**

```python
def _empty_catalog(kind: GeometryKind) -> gpd.GeoDataFrame:
```

**Purpose**

Implements empty catalog according to the exact implementation and guards in this file.

**Inputs**

- `kind` (`GeometryKind`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `_canonical_catalog_dtypes(output, kind)`.

**Algorithm**

1. Defines `data` with annotation `dict[str, object]` from `{}`.
2. Iterates `(column, dtype)` over `zip(NORMALIZED_FEATURE_COLUMNS[kind], NORMALIZED_FEATURE_DTYPES[kind], strict=True)`. For each value: Computes `data[column]` from `gpd.GeoSeries([], crs=CALCULATION_CRS) if column == 'geometry' else pd.Series(dtype=dtype)`.
3. Computes `output` from `gpd.GeoDataFrame(data, geometry='geometry', crs=CALCULATION_CRS)`.
4. Returns `_canonical_catalog_dtypes(output, kind)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_canonical_catalog_dtypes`, `gpd.GeoDataFrame`, `gpd.GeoSeries`, `pd.Series`, `zip`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `_combine_catalogs`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_combine_catalogs`

**Signature**

```python
def _combine_catalogs(
    frames: list[gpd.GeoDataFrame], kind: GeometryKind
) -> gpd.GeoDataFrame:
```

**Purpose**

Implements combine catalogs according to the exact implementation and guards in this file.

**Inputs**

- `frames` (`list[gpd.GeoDataFrame]`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `kind` (`GeometryKind`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `_canonical_catalog_dtypes(combined, kind)`; `_empty_catalog(kind)`.

**Algorithm**

1. Checks `not frames`. When true: Returns `_empty_catalog(kind)`.
2. Computes `combined` from `gpd.GeoDataFrame(pd.concat(frames, ignore_index=True), geometry='geometry', crs=CALCULATION_CRS)`.
3. Calls `_validate_ids(combined['planning_feature_id'], 'planning_feature_id')` for its validation or side effect.
4. Returns `_canonical_catalog_dtypes(combined, kind)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_canonical_catalog_dtypes`, `_empty_catalog`, `_validate_ids`, `gpd.GeoDataFrame`, `pd.concat`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `_normalized_catalogs.combined`
- `src/landscout/stages/enrich_planning_features.py` — `_normalized_catalogs`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_normalized_catalogs`

**Signature**

```python
def _normalized_catalogs(
    planning_document: GpuPlanningDocument,
) -> tuple[
    gpd.GeoDataFrame,
    gpd.GeoDataFrame,
    gpd.GeoDataFrame,
    tuple[GpuValidatedSpatialLayerSource, ...],
]:
```

**Purpose**

Rebuild canonical catalogs from the inspected GPU related layers only.

**Inputs**

- `planning_document` (`GpuPlanningDocument`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[gpd.GeoDataFrame, gpd.GeoDataFrame, gpd.GeoDataFrame, tuple[GpuValidatedSpatialLayerSource, ...]]`. Observed return expression(s): `(combined('SURFACE'), combined('LINE'), combined('POINT'), validated_sources)`; `_combine_catalogs([normalized[logical] for logical, spec in LAYER_SPECS.items() if spec.geometry_kind == kind and logical in normalized], kind)`.

**Algorithm**

1. Computes `context` from `_planning_context(planning_document)`.
2. Computes `spatial_inventory` from `tuple(planning_document.all_spatial_layers)`.
3. Computes `inspected_layers` from `(planning_document.zoning, *planning_document.related_layers)`.
4. Iterates `layer` over `inspected_layers`. For each value: Checks `sum((reference == layer.reference for reference in spatial_inventory)) != 1`. When true: Raises `PlanningFeaturesError(f'{layer.logical_name} inspected reference must occur exactly once in the GPU spatial-layer inventory')`.
5. Defines `layer_map` with annotation `dict[str, GpuInspectedLayer]` from `{}`.
6. Iterates `inspected_layer` over `planning_document.related_layers`. For each value: Computes `logical` from `str(inspected_layer.logical_name)`. Checks `logical not in LAYER_SPECS`. When true: Raises `PlanningFeaturesError(f'Unsupported related layer: {logical}')`. Checks `logical in layer_map`. When true: Raises `PlanningFeaturesError(f'Duplicate related layer: {logical}')`. Executes 1 additional source-ordered statement(s).
7. Runs guarded operation: Computes `validated_sources` from `revalidate_gpu_spatial_layer_sources(planning_document, tuple((layer_map[logical] for logical in LAYER_SPECS if logical in layer_map)))`. Handles `GpuSpatialInspectionError`.
8. Defines `source_by_logical` with annotation `dict[str, GpuValidatedSpatialLayerSource]` from `{source.logical_name: source for source in validated_sources}`.
9. Defines `normalized` with annotation `dict[str, gpd.GeoDataFrame]` from `{}`.
10. Iterates `(logical, layer)` over `layer_map.items()`. For each value: Computes `source` from `source_by_logical[logical]`. Computes `fresh_layer` from `replace(layer, data=source.data)`. Computes `normalized[logical]` from `_normalize_layer(fresh_layer, LAYER_SPECS[logical], context, source)`.
11. Defines the local helper `combined`; its behavior is documented with the parent function's nested helpers.
12. Returns `(combined('SURFACE'), combined('LINE'), combined('POINT'), validated_sources)`.

**Meaningful nested/local helpers**

- `combined` — `def combined(kind: GeometryKind) -> gpd.GeoDataFrame:`. It executes 1 top-level statement(s), uses `LAYER_SPECS.items`, `_combine_catalogs`, and has no explicit raises. Trivial test callbacks are intentionally grouped here with their parent.

**Validation and invariants**

- Rejects or diverts the path when `sum((reference == layer.reference for reference in spatial_inventory)) != 1` is true.
- Rejects or diverts the path when `logical not in LAYER_SPECS` is true.
- Rejects or diverts the path when `logical in layer_map` is true.

**Exceptions**

- Explicitly raises: `PlanningFeaturesError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `LAYER_SPECS.items`, `PlanningFeaturesError`, `_combine_catalogs`, `_normalize_layer`, `_planning_context`, `combined`, `layer_map.items`, `replace`, `revalidate_gpu_spatial_layer_sources`, `str`, `sum`, `tuple`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `_validate_normalized_planning_feature_inputs`
- `src/landscout/stages/enrich_planning_features.py` — `intersect_parcels_with_gpu_planning_features`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_normalized_catalogs.combined`

**Signature**

```python
def combined(kind: GeometryKind) -> gpd.GeoDataFrame:
```

**Purpose**

Implements combined according to the exact implementation and guards in this file.

**Inputs**

- `kind` (`GeometryKind`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `_combine_catalogs([normalized[logical] for logical, spec in LAYER_SPECS.items() if spec.geometry_kind == kind and logical in normalized], kind)`.

**Algorithm**

1. Returns `_combine_catalogs([normalized[logical] for logical, spec in LAYER_SPECS.items() if spec.geometry_kind == kind and logical in normalized], kind)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `LAYER_SPECS.items`, `_combine_catalogs`.

**Known repository callers**

No direct repository caller found.

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

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `result`.

**Algorithm**

1. Computes `geometry` from `_project_geometry(parcels, 'Parcel')`.
2. Computes `result` from `gpd.GeoDataFrame({'_parcel_position': np.arange(len(parcels), dtype='int64'), 'parcel_id': parcels['parcel_id'].to_numpy(copy=True)}, geometry=geometry.to_numpy(copy=True), crs=CALCULATION_CRS)`.
3. Runs guarded operation: Computes `areas` from `result.geometry.area.to_numpy(dtype='float64')`. Handles `Exception`.
4. Checks `not np.isfinite(areas).all() or (areas <= 0).any()`. When true: Raises `PlanningFeaturesError('Parcel metric areas must be finite and positive')`.
5. Computes `result['_parcel_area_m2']` from `areas`.
6. Returns `result`.

**Validation and invariants**

- Rejects or diverts the path when `not np.isfinite(areas).all() or (areas <= 0).any()` is true.

**Exceptions**

- Explicitly raises: `PlanningFeaturesError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `(areas <= 0).any`, `PlanningFeaturesError`, `_project_geometry`, `geometry.to_numpy`, `gpd.GeoDataFrame`, `len`, `np.arange`, `np.isfinite`, `np.isfinite(areas).all`, `parcels['parcel_id'].to_numpy`, `result.geometry.area.to_numpy`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `_validate_normalized_planning_feature_inputs`
- `src/landscout/stages/enrich_planning_features.py` — `_validate_parcel_summaries`
- `src/landscout/stages/enrich_planning_features.py` — `intersect_parcels_with_gpu_planning_features`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_relation_base`

**Signature**

```python
def _relation_base(
    metric: gpd.GeoDataFrame,
    catalog: gpd.GeoDataFrame,
) -> tuple[pd.DataFrame, np.ndarray, np.ndarray]:
```

**Purpose**

Implements relation base according to the exact implementation and guards in this file.

**Inputs**

- `metric` (`gpd.GeoDataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `catalog` (`gpd.GeoDataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[pd.DataFrame, np.ndarray, np.ndarray]`. Observed return expression(s): `(base, parcel_positions, feature_positions)`; `(pd.DataFrame(), np.array([], dtype='int64'), np.array([], dtype='int64'))`.

**Algorithm**

1. Checks `catalog.empty or metric.empty`. When true: Returns `(pd.DataFrame(), np.array([], dtype='int64'), np.array([], dtype='int64'))`.
2. Runs guarded operation: Computes `candidates` from `gpd.sjoin(metric[['_parcel_position', 'parcel_id', 'geometry']], gpd.GeoDataFrame({'_feature_position': np.arange(len(catalog), dtype='int64')}, geometry=catalog.geometry.to_numpy(copy=True), crs=CALCULATION_CRS), how='inner', predicate='intersects')`. Handles `Exception`.
3. Checks `candidates.empty`. When true: Returns `(pd.DataFrame(), np.array([], dtype='int64'), np.array([], dtype='int64'))`.
4. Computes `parcel_positions` from `candidates['_parcel_position'].to_numpy(dtype='int64')`.
5. Computes `feature_positions` from `candidates['_feature_position'].to_numpy(dtype='int64')`.
6. Computes `selected` from `catalog.iloc[feature_positions]`.
7. Computes `base` from `pd.DataFrame({'_parcel_position': parcel_positions, '_feature_position': feature_positions, 'parcel_id': metric['parcel_id'].to_numpy()[parcel_positions], **{column: selected[column].to_numpy(copy=True) for column in ('planning_feature_id', 'source_feature_id', 'source_identity_kind', 'source_identity_field', 'logical…`.
8. Returns `(base, parcel_positions, feature_positions)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `PlanningFeaturesError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningFeaturesError`, `candidates['_feature_position'].to_numpy`, `candidates['_parcel_position'].to_numpy`, `catalog.geometry.to_numpy`, `gpd.GeoDataFrame`, `gpd.sjoin`, `len`, `metric['_parcel_area_m2'].to_numpy`, `metric['parcel_id'].to_numpy`, `np.arange`, `np.array`, `pd.DataFrame`, `selected['regulation_filename_raw'].to_numpy`, `selected['source_archive_sha256'].to_numpy`, `selected['source_document_id'].to_numpy`, `selected['source_layer'].to_numpy`, `selected['source_validity_date_raw'].to_numpy`, `selected[column].to_numpy`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `_line_relations`
- `src/landscout/stages/enrich_planning_features.py` — `_point_relations`
- `src/landscout/stages/enrich_planning_features.py` — `_surface_relations`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_surface_relations`

**Signature**

```python
def _surface_relations(
    metric: gpd.GeoDataFrame,
    catalog: gpd.GeoDataFrame,
) -> pd.DataFrame:
```

**Purpose**

Implements surface relations according to the exact implementation and guards in this file.

**Inputs**

- `metric` (`gpd.GeoDataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `catalog` (`gpd.GeoDataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.DataFrame`. Observed return expression(s): `base`.

**Algorithm**

1. Computes `(base, parcel_positions, feature_positions)` from `_relation_base(metric, catalog)`.
2. Checks `base.empty`. When true: Returns `base`.
3. Runs guarded operation: Computes `geometries` from `intersection(metric.geometry.iloc[parcel_positions].array, catalog.geometry.iloc[feature_positions].array)`. Computes `areas` from `np.asarray(shapely_area(geometries), dtype='float64')`. Handles `Exception`.
4. Computes `feature_areas` from `catalog['feature_area_m2'].to_numpy(dtype='float64')[feature_positions]`.
5. Computes `base['_intersection_geometry']` from `list(geometries)`.
6. Computes `base['relation_type']` from `np.where(areas > 0, 'AREA_OVERLAP', 'TOUCH_ONLY')`.
7. Computes `base['feature_area_m2']` from `feature_areas`.
8. Computes `base['source_line_length_m']` from `np.nan`.
9. Computes `base['intersection_area_m2']` from `areas`.
10. Computes `base['intersection_length_m']` from `np.nan`.
11. Computes `base['parcel_share_pct']` from `100.0 * areas / base['parcel_metric_area_m2']`.
12. Computes `base['feature_share_pct']` from `100.0 * areas / feature_areas`.
13. Iterates `column` over `RELATION_COUNT_COLUMNS`. For each value: Computes `base[column]` from `pd.array([pd.NA] * len(base), dtype='Int64')`.
14. Returns `base`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `PlanningFeaturesError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningFeaturesError`, `_relation_base`, `catalog['feature_area_m2'].to_numpy`, `intersection`, `len`, `list`, `np.asarray`, `np.where`, `pd.array`, `shapely_area`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `_build_relation_tables`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_line_relations`

**Signature**

```python
def _line_relations(
    metric: gpd.GeoDataFrame,
    catalog: gpd.GeoDataFrame,
) -> pd.DataFrame:
```

**Purpose**

Implements line relations according to the exact implementation and guards in this file.

**Inputs**

- `metric` (`gpd.GeoDataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `catalog` (`gpd.GeoDataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.DataFrame`. Observed return expression(s): `base`.

**Algorithm**

1. Computes `(base, parcel_positions, feature_positions)` from `_relation_base(metric, catalog)`.
2. Checks `base.empty`. When true: Returns `base`.
3. Runs guarded operation: Computes `geometries` from `intersection(metric.geometry.iloc[parcel_positions].array, catalog.geometry.iloc[feature_positions].array)`. Computes `lengths` from `np.asarray(shapely_length(geometries), dtype='float64')`. Handles `Exception`.
4. Computes `source_lengths` from `catalog['feature_length_m'].to_numpy(dtype='float64')[feature_positions]`.
5. Computes `base['relation_type']` from `np.where(lengths > 0, 'LENGTH_OVERLAP', 'TOUCH_ONLY')`.
6. Computes `base['feature_area_m2']` from `np.nan`.
7. Computes `base['source_line_length_m']` from `source_lengths`.
8. Computes `base['intersection_area_m2']` from `np.nan`.
9. Computes `base['intersection_length_m']` from `lengths`.
10. Computes `base['parcel_share_pct']` from `np.nan`.
11. Computes `base['feature_share_pct']` from `np.nan`.
12. Iterates `column` over `RELATION_COUNT_COLUMNS`. For each value: Computes `base[column]` from `pd.array([pd.NA] * len(base), dtype='Int64')`.
13. Returns `base`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `PlanningFeaturesError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningFeaturesError`, `_relation_base`, `catalog['feature_length_m'].to_numpy`, `intersection`, `len`, `np.asarray`, `np.where`, `pd.array`, `shapely_length`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `_build_relation_tables`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_point_relations`

**Signature**

```python
def _point_relations(
    metric: gpd.GeoDataFrame,
    catalog: gpd.GeoDataFrame,
) -> pd.DataFrame:
```

**Purpose**

Implements point relations according to the exact implementation and guards in this file.

**Inputs**

- `metric` (`gpd.GeoDataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `catalog` (`gpd.GeoDataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.DataFrame`. Observed return expression(s): `base`.

**Algorithm**

1. Computes `(base, parcel_positions, feature_positions)` from `_relation_base(metric, catalog)`.
2. Checks `base.empty`. When true: Returns `base`.
3. Runs guarded operation: Computes `(members, relation_positions)` from `get_parts(catalog.geometry.iloc[feature_positions].array, return_index=True)`. Computes `relation_positions` from `np.asarray(relation_positions, dtype='int64')`. Computes `member_parcels` from `metric.geometry.iloc[parcel_positions[relation_positions]].array`. Computes `inside_mask` from `np.asarray(contains(member_parcels, members), dtype='bool')`. Executes 1 additional source-ordered statement(s). Handles `Exception`.
4. Computes `member_counts` from `np.bincount(relation_positions, minlength=len(base))`.
5. Computes `inside_counts` from `np.bincount(relation_positions, weights=inside_mask, minlength=len(base)).astype('int64')`.
6. Computes `covered_counts` from `np.bincount(relation_positions, weights=covered_mask, minlength=len(base)).astype('int64')`.
7. Computes `boundary_counts` from `covered_counts - inside_counts`.
8. Checks `(inside_counts + boundary_counts <= 0).any()`. When true: Raises `PlanningFeaturesError('Point candidate has no covered source member')`.
9. Computes `base['relation_type']` from `np.where(inside_counts > 0, 'INSIDE', 'BOUNDARY_TOUCH')`.
10. Iterates `column` over `RELATION_FLOAT_COLUMNS - {'parcel_metric_area_m2'}`. For each value: Computes `base[column]` from `np.nan`.
11. Computes `base['point_member_count']` from `pd.array(member_counts, dtype='Int64')`.
12. Computes `base['point_members_inside_count']` from `pd.array(inside_counts, dtype='Int64')`.
13. Computes `base['point_members_boundary_count']` from `pd.array(boundary_counts, dtype='Int64')`.
14. Returns `base`.

**Validation and invariants**

- Rejects or diverts the path when `(inside_counts + boundary_counts <= 0).any()` is true.

**Exceptions**

- Explicitly raises: `PlanningFeaturesError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `(inside_counts + boundary_counts <= 0).any`, `PlanningFeaturesError`, `_relation_base`, `contains`, `covers`, `get_parts`, `len`, `np.asarray`, `np.bincount`, `np.bincount(relation_positions, weights=covered_mask, minlength=len(base)).astype`, `np.bincount(relation_positions, weights=inside_mask, minlength=len(base)).astype`, `np.where`, `pd.array`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `_build_relation_tables`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_empty_relations`

**Signature**

```python
def _empty_relations() -> pd.DataFrame:
```

**Purpose**

Implements empty relations according to the exact implementation and guards in this file.

**Inputs**

- No parameters.

**Returns**

- Declared return type: `pd.DataFrame`. Observed return expression(s): `output`.

**Algorithm**

1. Computes `output` from `pd.DataFrame({column: pd.Series(dtype='float64' if column in RELATION_FLOAT_COLUMNS else 'Int64' if column in RELATION_COUNT_COLUMNS else 'str') for column in RELATION_COLUMNS})`.
2. Computes `output.index` from `pd.RangeIndex(0)`.
3. Returns `output`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `pd.DataFrame`, `pd.RangeIndex`, `pd.Series`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `_build_relation_tables`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_build_relation_tables`

**Signature**

```python
def _build_relation_tables(
    metric: gpd.GeoDataFrame,
    surfaces: gpd.GeoDataFrame,
    lines: gpd.GeoDataFrame,
    points: gpd.GeoDataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
```

**Purpose**

Builds relation tables according to the exact implementation and guards in this file.

**Inputs**

- `metric` (`gpd.GeoDataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `surfaces` (`gpd.GeoDataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `lines` (`gpd.GeoDataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `points` (`gpd.GeoDataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]`. Observed return expression(s): `(surface_work, line_work, point_work, relations)`; `(surface_work, line_work, point_work, _empty_relations())`.

**Algorithm**

1. Computes `surface_work` from `_surface_relations(metric, surfaces)`.
2. Computes `line_work` from `_line_relations(metric, lines)`.
3. Computes `point_work` from `_point_relations(metric, points)`.
4. Computes `work_frames` from `[frame for frame in (surface_work, line_work, point_work) if not frame.empty]`.
5. Checks `not work_frames`. When true: Returns `(surface_work, line_work, point_work, _empty_relations())`.
6. Computes `combined` from `pd.concat(work_frames, ignore_index=True)`.
7. Computes `combined` from `combined.sort_values(['_parcel_position', 'planning_feature_id'], kind='stable').reset_index(drop=True)`.
8. Computes `relations` from `combined.loc[:, RELATION_COLUMNS].copy()`.
9. Iterates `column` over `RELATION_STRING_COLUMNS`. For each value: Computes `relations[column]` from `relations[column].astype('str')`.
10. Iterates `column` over `RELATION_COUNT_COLUMNS`. For each value: Computes `relations[column]` from `pd.array(relations[column], dtype='Int64')`.
11. Computes `relations.index` from `pd.RangeIndex(len(relations))`.
12. Returns `(surface_work, line_work, point_work, relations)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `combined.loc[:, RELATION_COLUMNS].copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `_empty_relations`, `_line_relations`, `_point_relations`, `_surface_relations`, `combined.loc[:, RELATION_COLUMNS].copy`, `combined.sort_values`, `combined.sort_values(['_parcel_position', 'planning_feature_id'], kind='stable').reset_index`, `len`, `pd.RangeIndex`, `pd.array`, `pd.concat`, `relations[column].astype`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `_validate_normalized_planning_feature_inputs`
- `src/landscout/stages/enrich_planning_features.py` — `intersect_parcels_with_gpu_planning_features`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_canonical_integrity_value`

**Signature**

```python
def _canonical_integrity_value(value: object) -> object:
```

**Purpose**

Implements canonical integrity value according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `object`. Observed return expression(s): `value.isoformat()`; `_canonical_integrity_value(value.item())`; `None`; `value`; `int(value)`; `number`.

**Algorithm**

1. Checks `isinstance(value, (datetime, date, pd.Timestamp))`. When true: Returns `value.isoformat()`.
2. Checks `isinstance(value, np.generic)`. When true: Returns `_canonical_integrity_value(value.item())`.
3. Checks `value is None or value is pd.NA`. When true: Returns `None`.
4. Runs guarded operation: Computes `missing` from `pd.isna(value)`. Handles `(TypeError, ValueError)`.
5. Checks `isinstance(missing, (bool, np.bool_)) and bool(missing)`. When true: Returns `None`.
6. Checks `isinstance(value, bool)`. When true: Returns `value`.
7. Checks `isinstance(value, Integral)`. When true: Returns `int(value)`.
8. Checks `isinstance(value, Real)`. When true: Computes `number` from `float(value)`. Checks `not isfinite(number)`. When true: Raises `PlanningFeaturesError('Integrity payload contains non-finite numeric data')`. Returns `number`.
9. Checks `isinstance(value, str)`. When true: Returns `value`.
10. Raises `PlanningFeaturesError(f'Integrity payload contains unsupported value {type(value).__name__}')`.

**Validation and invariants**

- Rejects or diverts the path when `isinstance(value, Real)` is true.
- Rejects or diverts the path when `not isfinite(number)` is true.

**Exceptions**

- Explicitly raises: `PlanningFeaturesError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningFeaturesError`, `_canonical_integrity_value`, `bool`, `float`, `int`, `isfinite`, `isinstance`, `pd.isna`, `type`, `value.isoformat`, `value.item`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `_expected_relations_content_sha256`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_canonical_integrity_sha256`

**Signature**

```python
def _canonical_integrity_sha256(payload: object) -> str:
```

**Purpose**

Implements canonical integrity sha256 according to the exact implementation and guards in this file.

**Inputs**

- `payload` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `sha256(encoded).hexdigest()`.

**Algorithm**

1. Runs guarded operation: Computes `encoded` from `json.dumps(payload, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(',', ':')).encode('utf-8')`. Handles `Exception`.
2. Returns `sha256(encoded).hexdigest()`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `PlanningFeaturesError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningFeaturesError`, `json.dumps`, `json.dumps(payload, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(',', ':')).encode`, `sha256`, `sha256(encoded).hexdigest`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `_expected_relations_content_sha256`
- `src/landscout/stages/enrich_planning_features.py` — `_gpu_related_source_files_sha256`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_gpu_related_source_files_sha256`

**Signature**

```python
def _gpu_related_source_files_sha256(
    planning_document: GpuPlanningDocument,
    sources: tuple[GpuValidatedSpatialLayerSource, ...],
) -> str:
```

**Purpose**

Implements gpu related source files sha256 according to the exact implementation and guards in this file.

**Inputs**

- `planning_document` (`GpuPlanningDocument`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `sources` (`tuple[GpuValidatedSpatialLayerSource, ...]`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `_canonical_integrity_sha256({'domain': 'landscout.planning_features.verified_gpu_sources.v1', 'source_archive_sha256': planning_document.extraction.archive.sha256, 'layers': [{'logical_layer': source.logical_name, 'driver': source.driver, 'source_layer': source.source_layer, 'dataset_relative_path': source.dataset_relative_path, 'source_feature_count': source.feature_count, 'source_crs': source.s…`.

**Algorithm**

1. Returns `_canonical_integrity_sha256({'domain': 'landscout.planning_features.verified_gpu_sources.v1', 'source_archive_sha256': planning_document.extraction.archive.sha256, 'layers': [{'logical_layer': source.logical_name, 'driver': source.driver, 'source_layer': source.source_layer, 'dataset_relative_path': source.dataset_relative_path, 'source_feature_count': sour…`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_canonical_integrity_sha256`, `list`, `sorted`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `_validate_normalized_planning_feature_inputs`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_expected_relations_content_sha256`

**Signature**

```python
def _expected_relations_content_sha256(relations: pd.DataFrame) -> str:
```

**Purpose**

Implements expected relations content sha256 according to the exact implementation and guards in this file.

**Inputs**

- `relations` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `_canonical_integrity_sha256({'domain': 'landscout.planning_features.expected_relations.v2', 'schema': deterministic_frame_schema_signature(relations), 'index': [_canonical_integrity_value(value) for value in relations.index.tolist()], 'rows': [[_canonical_integrity_value(value) for value in row] for row in relations.itertuples(index=False, name=None)]})`.

**Algorithm**

1. Returns `_canonical_integrity_sha256({'domain': 'landscout.planning_features.expected_relations.v2', 'schema': deterministic_frame_schema_signature(relations), 'index': [_canonical_integrity_value(value) for value in relations.index.tolist()], 'rows': [[_canonical_integrity_value(value) for value in row] for row in relations.itertuples(index=False, name=None)]})`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_canonical_integrity_sha256`, `_canonical_integrity_value`, `deterministic_frame_schema_signature`, `relations.index.tolist`, `relations.itertuples`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `_validate_normalized_planning_feature_inputs`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_technical_tolerance`

**Signature**

```python
def _technical_tolerance(parcel_area: float) -> float:
```

**Purpose**

Implements technical tolerance according to the exact implementation and guards in this file.

**Inputs**

- `parcel_area` (`float`; required) — area quantity, normally square metres where the name ends in `_m2`. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `float`. Observed return expression(s): `technical_overlay_tolerance(parcel_area)`.

**Algorithm**

1. Returns `technical_overlay_tolerance(parcel_area)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `technical_overlay_tolerance`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `_surface_union_summary`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_surface_union_summary`

**Signature**

```python
def _surface_union_summary(
    positive: pd.DataFrame,
    parcel_areas: np.ndarray,
    count: int,
) -> np.ndarray:
```

**Purpose**

Implements surface union summary according to the exact implementation and guards in this file.

**Inputs**

- `positive` (`pd.DataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `parcel_areas` (`np.ndarray`; required) — area quantity, normally square metres where the name ends in `_m2`. Nullability and accepted values are exactly those enforced by the guards listed below.
- `count` (`int`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `np.ndarray`. Observed return expression(s): `output`.

**Algorithm**

1. Computes `output` from `np.zeros(count, dtype='float64')`.
2. Checks `positive.empty`. When true: Returns `output`.
3. Iterates `(position_value, group)` over `positive.groupby('_parcel_position', sort=False)`. For each value: Computes `position` from `int(position_value)`. Runs guarded operation: Computes `value` from `float(shapely_area(union_all(group['_intersection_geometry'].to_numpy())))`. Handles `Exception`. Checks `not isfinite(value) or value < 0`. When true: Raises `PlanningFeaturesError('Surface covered-union area is invalid')`. Executes 3 additional source-ordered statement(s).
4. Returns `output`.

**Validation and invariants**

- Rejects or diverts the path when `not isfinite(value) or value < 0` is true.
- Rejects or diverts the path when `value > area` is true.
- Rejects or diverts the path when `value - area > _technical_tolerance(area)` is true.

**Exceptions**

- Explicitly raises: `PlanningFeaturesError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningFeaturesError`, `_technical_tolerance`, `float`, `group['_intersection_geometry'].to_numpy`, `int`, `isfinite`, `np.zeros`, `positive.groupby`, `shapely_area`, `union_all`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `_attach_parcel_summaries`
- `src/landscout/stages/enrich_planning_features.py` — `_validate_parcel_summaries`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_attach_parcel_summaries`

**Signature**

```python
def _attach_parcel_summaries(
    parcels: gpd.GeoDataFrame,
    metric: gpd.GeoDataFrame,
    surface_work: pd.DataFrame,
    line_work: pd.DataFrame,
    point_work: pd.DataFrame,
    context: _PlanningContext,
) -> gpd.GeoDataFrame:
```

**Purpose**

Implements attach parcel summaries according to the exact implementation and guards in this file.

**Inputs**

- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `metric` (`gpd.GeoDataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `surface_work` (`pd.DataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `line_work` (`pd.DataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `point_work` (`pd.DataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `context` (`_PlanningContext`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `output`; `result`.

**Algorithm**

1. Computes `count` from `len(parcels)`.
2. Computes `areas` from `metric['_parcel_area_m2'].to_numpy(dtype='float64')`.
3. Computes `output` from `parcels.copy(deep=True)`.
4. Defines the local helper `relation_counts`; its behavior is documented with the parent function's nested helpers.
5. Computes `surface_positive` from `surface_work.loc[surface_work['relation_type'] == 'AREA_OVERLAP'] if not surface_work.empty else surface_work`.
6. Computes `surface_union` from `_surface_union_summary(surface_positive, areas, count)`.
7. Computes `output['planning_surface_relation_count']` from `relation_counts(surface_work)`.
8. Computes `output['planning_surface_area_overlap_count']` from `relation_counts(surface_work, surface_work['relation_type'].eq('AREA_OVERLAP') if not surface_work.empty else None)`.
9. Computes `output['planning_surface_touch_count']` from `relation_counts(surface_work, surface_work['relation_type'].eq('TOUCH_ONLY') if not surface_work.empty else None)`.
10. Computes `raw_sum` from `np.zeros(count, dtype='float64')`.
11. Checks `not surface_positive.empty`. When true: Computes `sums` from `surface_positive.groupby('_parcel_position', sort=False)['intersection_area_m2'].sum()`. Computes `raw_sum[sums.index.to_numpy(dtype='int64')]` from `sums.to_numpy(dtype='float64')`.
12. Computes `output['planning_surface_intersection_area_sum_m2']` from `raw_sum`.
13. Computes `output['planning_surface_covered_union_area_m2']` from `surface_union`.
14. Computes `output['planning_surface_covered_pct']` from `np.where(surface_union == areas, 100.0, 100.0 * surface_union / areas)`.
15. Iterates `(family, prefix)` over `(('PRESCRIPTION', 'prescription'), ('INFORMATION', 'information'))`. For each value: Computes `family_work` from `surface_work.loc[surface_work['feature_family'] == family] if not surface_work.empty else surface_work`. Computes `family_positive` from `family_work.loc[family_work['relation_type'] == 'AREA_OVERLAP'] if not family_work.empty else family_work`. Computes `union` from `_surface_union_summary(family_positive, areas, count)`. Executes 3 additional source-ordered statement(s).
16. Computes `output['planning_line_relation_count']` from `relation_counts(line_work)`.
17. Computes `output['planning_line_length_overlap_count']` from `relation_counts(line_work, line_work['relation_type'].eq('LENGTH_OVERLAP') if not line_work.empty else None)`.
18. Computes `output['planning_line_touch_count']` from `relation_counts(line_work, line_work['relation_type'].eq('TOUCH_ONLY') if not line_work.empty else None)`.
19. Computes `line_sum` from `np.zeros(count, dtype='float64')`.
20. Checks `not line_work.empty`. When true: Computes `values` from `line_work.groupby('_parcel_position', sort=False)['intersection_length_m'].sum()`. Computes `line_sum[values.index.to_numpy(dtype='int64')]` from `values.to_numpy(dtype='float64')`.
21. Computes `output['planning_line_intersection_length_sum_m']` from `line_sum`.
22. Computes `output['planning_point_relation_count']` from `relation_counts(point_work)`.
23. Iterates `(source, target)` over `(('point_members_inside_count', 'planning_point_inside_count'), ('point_members_boundary_count', 'planning_point_boundary_count'))`. For each value: Computes `values` from `np.zeros(count, dtype='int64')`. Checks `not point_work.empty`. When true: Computes `grouped` from `point_work.groupby('_parcel_position', sort=False)[source].sum()`. Computes `values[grouped.index.to_numpy(dtype='int64')]` from `grouped.to_numpy(dtype='int64')`. Computes `output[target]` from `values`.
24. Computes `output['planning_feature_document_id']` from `context.document_id`.
25. Computes `output['planning_feature_archive_sha256']` from `context.archive_sha256`.
26. Returns `output`.

**Meaningful nested/local helpers**

- `relation_counts` — `def relation_counts(         frame: pd.DataFrame, mask: pd.Series | None = None     ) -> np.ndarray:`. It executes 4 top-level statement(s), uses `counts.index.to_numpy`, `counts.to_numpy`, `np.zeros`, `selected.groupby`, `selected.groupby('_parcel_position', sort=False).size`, and has no explicit raises. Trivial test callbacks are intentionally grouped here with their parent.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `parcels.copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `_surface_union_summary`, `counts.index.to_numpy`, `counts.to_numpy`, `grouped.index.to_numpy`, `grouped.to_numpy`, `len`, `line_work.groupby`, `line_work.groupby('_parcel_position', sort=False)['intersection_length_m'].sum`, `line_work['relation_type'].eq`, `metric['_parcel_area_m2'].to_numpy`, `np.where`, `np.zeros`, `parcels.copy`, `point_work.groupby`, `point_work.groupby('_parcel_position', sort=False)[source].sum`, `relation_counts`, `selected.groupby`, `selected.groupby('_parcel_position', sort=False).size`, `sums.index.to_numpy`, `sums.to_numpy`, `surface_positive.groupby`, `surface_positive.groupby('_parcel_position', sort=False)['intersection_area_m2'].sum`, `surface_work['relation_type'].eq`, `values.index.to_numpy`, `values.to_numpy`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `_validate_normalized_planning_feature_inputs`
- `src/landscout/stages/enrich_planning_features.py` — `intersect_parcels_with_gpu_planning_features`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_attach_parcel_summaries.relation_counts`

**Signature**

```python
def relation_counts(
        frame: pd.DataFrame, mask: pd.Series | None = None
    ) -> np.ndarray:
```

**Purpose**

Implements relation counts according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `mask` (`pd.Series | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `np.ndarray`. Observed return expression(s): `result`.

**Algorithm**

1. Computes `result` from `np.zeros(count, dtype='int64')`.
2. Computes `selected` from `frame if mask is None else frame.loc[mask]`.
3. Checks `not selected.empty`. When true: Computes `counts` from `selected.groupby('_parcel_position', sort=False).size()`. Computes `result[counts.index.to_numpy(dtype='int64')]` from `counts.to_numpy(dtype='int64')`.
4. Returns `result`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `counts.index.to_numpy`, `counts.to_numpy`, `np.zeros`, `selected.groupby`, `selected.groupby('_parcel_position', sort=False).size`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_numeric_values`

**Signature**

```python
def _numeric_values(
    frame: pd.DataFrame,
    columns: set[str] | frozenset[str] | tuple[str, ...],
    label: str,
    *,
    allow_null: bool,
) -> None:
```

**Purpose**

Implements numeric values according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `columns` (`set[str] | frozenset[str] | tuple[str, ...]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `allow_null` (`bool`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Iterates `column` over `columns`. For each value: Iterates `value` over `frame[column].tolist()`. For each value: Checks `pd.isna(value)`. When true: Checks `allow_null`. When true: Executes `continue` control flow. Raises `PlanningFeaturesError(f'{label} {column} must not be null')`. Checks `isinstance(value, bool) or not isinstance(value, Real)`. When true: Raises `PlanningFeaturesError(f'{label} {column} must be numeric')`. Runs guarded operation: Computes `number` from `float(value)`. Handles `(TypeError, ValueError, OverflowError)`. Executes 1 additional source-ordered statement(s).

**Validation and invariants**

- Rejects or diverts the path when `pd.isna(value)` is true.
- Rejects or diverts the path when `isinstance(value, bool) or not isinstance(value, Real)` is true.
- Rejects or diverts the path when `not isfinite(number) or number < 0` is true.

**Exceptions**

- Explicitly raises: `PlanningFeaturesError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningFeaturesError`, `float`, `frame[column].tolist`, `isfinite`, `isinstance`, `pd.isna`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `_validate_catalog_contract`
- `src/landscout/stages/enrich_planning_features.py` — `_validate_parcel_summaries`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_integer_values`

**Signature**

```python
def _integer_values(
    frame: pd.DataFrame,
    columns: set[str] | frozenset[str] | tuple[str, ...],
    label: str,
    *,
    allow_null: bool,
) -> None:
```

**Purpose**

Implements integer values according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `columns` (`set[str] | frozenset[str] | tuple[str, ...]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `allow_null` (`bool`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Iterates `column` over `columns`. For each value: Iterates `value` over `frame[column].tolist()`. For each value: Checks `pd.isna(value)`. When true: Checks `allow_null`. When true: Executes `continue` control flow. Raises `PlanningFeaturesError(f'{label} {column} must not be null')`. Calls `_strict_nonnegative_integer(value, f'{label} {column}')` for its validation or side effect.

**Validation and invariants**

- Rejects or diverts the path when `pd.isna(value)` is true.

**Exceptions**

- Explicitly raises: `PlanningFeaturesError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningFeaturesError`, `_strict_nonnegative_integer`, `frame[column].tolist`, `pd.isna`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `_validate_catalog_contract`
- `src/landscout/stages/enrich_planning_features.py` — `_validate_parcel_summaries`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_null_safe_equal`

**Signature**

```python
def _null_safe_equal(left: object, right: object) -> bool:
```

**Purpose**

Implements null safe equal according to the exact implementation and guards in this file.

**Inputs**

- `left` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `right` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bool`. Observed return expression(s): `False`; `left_null and right_null`; `bool(left == right)`.

**Algorithm**

1. Runs guarded operation: Computes `left_missing` from `pd.isna(left)`. Computes `right_missing` from `pd.isna(right)`. Handles `(TypeError, ValueError)`.
2. Checks `not isinstance(left_missing, (bool, np.bool_)) or not isinstance(right_missing, (bool, np.bool_))`. When true: Returns `False`.
3. Computes `left_null` from `bool(left_missing)`.
4. Computes `right_null` from `bool(right_missing)`.
5. Checks `left_null or right_null`. When true: Returns `left_null and right_null`.
6. Runs guarded operation: Returns `bool(left == right)`. Handles `(TypeError, ValueError)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `bool`, `isinstance`, `pd.isna`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `_compare_rebuilt_relations`
- `src/landscout/stages/enrich_planning_features.py` — `_validate_relation_catalog_consistency`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_require_close`

**Signature**

```python
def _require_close(actual: object, expected: float, label: str) -> None:
```

**Purpose**

Implements require close according to the exact implementation and guards in this file.

**Inputs**

- `actual` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `expected` (`float`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `isinstance(actual, bool) or not isinstance(actual, Real)`. When true: Raises `PlanningFeaturesError(f'{label} must be numeric')`.
2. Runs guarded operation: Computes `number` from `float(actual)`. Handles `(TypeError, ValueError, OverflowError)`.
3. Checks `not isfinite(number)`. When true: Raises `PlanningFeaturesError(f'{label} must be finite')`.
4. Computes `reference` from `max(abs(number), abs(expected))`.
5. Checks `abs(number - expected) > technical_overlay_tolerance(reference)`. When true: Raises `PlanningFeaturesError(f'{label} is inconsistent')`.

**Validation and invariants**

- Rejects or diverts the path when `isinstance(actual, bool) or not isinstance(actual, Real)` is true.
- Rejects or diverts the path when `not isfinite(number)` is true.
- Rejects or diverts the path when `abs(number - expected) > technical_overlay_tolerance(reference)` is true.

**Exceptions**

- Explicitly raises: `PlanningFeaturesError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningFeaturesError`, `abs`, `float`, `isfinite`, `isinstance`, `max`, `technical_overlay_tolerance`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `_compare_rebuilt_parcel_output`
- `src/landscout/stages/enrich_planning_features.py` — `_compare_rebuilt_relations`
- `src/landscout/stages/enrich_planning_features.py` — `_validate_catalog_contract`
- `src/landscout/stages/enrich_planning_features.py` — `_validate_normalized_planning_feature_inputs`
- `src/landscout/stages/enrich_planning_features.py` — `_validate_parcel_summaries`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_catalog_identity`

**Signature**

```python
def _validate_catalog_identity(catalog: gpd.GeoDataFrame) -> None:
```

**Purpose**

Validates and rejects malformed catalog identity according to the exact implementation and guards in this file.

**Inputs**

- `catalog` (`gpd.GeoDataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Iterates `column` over `_CATALOG_REQUIRED_EXACT_STRING_COLUMNS`. For each value: Calls `_validate_exact_strings(catalog[column], f"Feature catalog {column.replace('_', ' ')}")` for its validation or side effect.
2. Iterates `column` over `_CATALOG_OPTIONAL_EXACT_STRING_COLUMNS`. For each value: Calls `_validate_optional_exact_strings(catalog[column], f"Feature catalog {column.replace('_', ' ')}")` for its validation or side effect.
3. Calls `_validate_ids(catalog['planning_feature_id'], 'planning_feature_id')` for its validation or side effect.
4. Iterates `(logical_layer, group)` over `catalog.groupby('logical_layer', sort=False)`. For each value: Calls `_validate_ids(group['source_feature_id'], f'{logical_layer} source_feature_id')` for its validation or side effect.
5. Iterates `(_, row)` over `catalog.iterrows()`. For each value: Computes `logical` from `_strict_string(row['logical_layer'], 'logical_layer')`. Checks `logical not in LAYER_SPECS`. When true: Raises `PlanningFeaturesError('Feature catalog logical layer is invalid')`. Computes `spec` from `LAYER_SPECS[logical]`. Executes 8 additional source-ordered statement(s).

**Validation and invariants**

- Rejects or diverts the path when `logical not in LAYER_SPECS` is true.
- Rejects or diverts the path when `row['feature_family'] != spec.feature_family` is true.
- Rejects or diverts the path when `row['geometry_kind'] != spec.geometry_kind` is true.
- Rejects or diverts the path when `row['planning_feature_id'] != expected_planning_id` is true.
- Rejects or diverts the path when `kind not in SOURCE_IDENTITY_KINDS` is true.
- Rejects or diverts the path when `kind == 'CNIG_ATTRIBUTE'` is true.
- Rejects or diverts the path when `field != spec.identity_field` is true.
- Rejects or diverts the path when `logical != 'prescription_surface' or field != 'OGR_FID' or (not str(row['source_feature_id']).startswith('OGR_FID:'))` is true.

**Exceptions**

- Explicitly raises: `PlanningFeaturesError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `column.replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `PlanningFeaturesError`, `_strict_string`, `_validate_exact_strings`, `_validate_ids`, `_validate_optional_exact_strings`, `catalog.groupby`, `catalog.iterrows`, `column.replace`, `str`, `str(row['source_feature_id']).startswith`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `_validate_catalog_contract`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_catalog_contract`

**Signature**

```python
def _validate_catalog_contract(
    catalog: object,
    geometry_kind: GeometryKind,
) -> gpd.GeoDataFrame:
```

**Purpose**

Validates and rejects malformed catalog contract according to the exact implementation and guards in this file.

**Inputs**

- `catalog` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `geometry_kind` (`GeometryKind`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `catalog`.

**Algorithm**

1. Computes `label` from `f'{geometry_kind} feature catalog'`.
2. Checks `not isinstance(catalog, gpd.GeoDataFrame)`. When true: Raises `PlanningFeaturesError(f'{label} must be a GeoDataFrame')`.
3. Runs guarded operation: Calls `validate_canonical_frame_schema(catalog, columns=NORMALIZED_FEATURE_COLUMNS[geometry_kind], dtypes=normalized_feature_dtypes(geometry_kind, catalog), label=label, geospatial=True, index_class='RangeIndex')` for its validation or side effect. Handles `(TypeError, ValueError)`.
4. Calls `_active_geometry(catalog, label)` for its validation or side effect.
5. Calls `_validate_catalog_identity(catalog)` for its validation or side effect.
6. Checks `not catalog.empty and (not catalog['geometry_kind'].eq(geometry_kind).all())`. When true: Raises `PlanningFeaturesError(f'{label} geometry kind is invalid')`.
7. Calls `_validate_geometries(catalog, _CATALOG_GEOMETRY_TYPES[geometry_kind], label)` for its validation or side effect.
8. Calls `_validate_two_dimensional_geometry(catalog, label)` for its validation or side effect.
9. Checks `geometry_kind == 'SURFACE'`. When true: Calls `_numeric_values(catalog, ('feature_area_m2',), 'Surface feature', allow_null=False)` for its validation or side effect. Checks `(catalog['feature_area_m2'] <= 0).any()`. When true: Raises `PlanningFeaturesError('Surface feature areas must be positive')`. Runs guarded operation: Computes `measured` from `catalog.geometry.area.to_numpy(dtype='float64')`. Handles `Exception`. Executes 1 additional source-ordered statement(s). Otherwise: Checks `geometry_kind == 'LINE'`. When true: Calls `_numeric_values(catalog, ('feature_length_m',), 'Line feature', allow_null=False)` for its validation or side effect. Checks `(catalog['feature_length_m'] <= 0).any()`. When true: Raises `PlanningFeaturesError('Line feature lengths must be positive')`. Runs guarded operation: Computes `measured` from `catalog.geometry.length.to_numpy(dtype='float64')`. Handles `Exception`. Executes 1 additional source-ordered statement(s). Otherwise: Calls `_integer_values(catalog, ('point_member_count',), 'Point feature', allow_null=False)` for its validation or side effect. Checks `(catalog['point_member_count'] < 1).any()`. When true: Raises `PlanningFeaturesError('Point features must contain a member')`. Executes 2 additional source-ordered statement(s).
10. Returns `catalog`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(catalog, gpd.GeoDataFrame)` is true.
- Rejects or diverts the path when `not catalog.empty and (not catalog['geometry_kind'].eq(geometry_kind).all())` is true.
- Rejects or diverts the path when `geometry_kind == 'SURFACE'` is true.
- Rejects or diverts the path when `(catalog['feature_area_m2'] <= 0).any()` is true.
- Rejects or diverts the path when `geometry_kind == 'LINE'` is true.
- Rejects or diverts the path when `(catalog['feature_length_m'] <= 0).any()` is true.
- Rejects or diverts the path when `(catalog['point_member_count'] < 1).any()` is true.
- Rejects or diverts the path when `catalog['point_member_count'].tolist() != member_counts` is true.

**Exceptions**

- Explicitly raises: `PlanningFeaturesError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `(catalog['feature_area_m2'] <= 0).any`, `(catalog['feature_length_m'] <= 0).any`, `(catalog['point_member_count'] < 1).any`, `PlanningFeaturesError`, `_active_geometry`, `_integer_values`, `_numeric_values`, `_require_close`, `_validate_catalog_identity`, `_validate_geometries`, `_validate_two_dimensional_geometry`, `catalog.geometry.area.to_numpy`, `catalog.geometry.length.to_numpy`, `catalog['feature_area_m2'].tolist`, `catalog['feature_length_m'].tolist`, `catalog['geometry_kind'].eq`, `catalog['geometry_kind'].eq(geometry_kind).all`, `catalog['point_member_count'].tolist`, `float`, `get_parts`, `isinstance`, `len`, `normalized_feature_dtypes`, `str`, `validate_canonical_frame_schema`, `zip`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `_validate_normalized_planning_feature_inputs`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_compare_normalized_catalog`

**Signature**

```python
def _compare_normalized_catalog(
    supplied: gpd.GeoDataFrame,
    expected: gpd.GeoDataFrame,
    label: str,
) -> None:
```

**Purpose**

Compares normalized catalog according to the exact implementation and guards in this file.

**Inputs**

- `supplied` (`gpd.GeoDataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `expected` (`gpd.GeoDataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `deterministic_frame_schema_signature(supplied) != deterministic_frame_schema_signature(expected)`. When true: Raises `PlanningFeaturesError(f'{label} schema differs from normalized GPU source')`.
2. Runs guarded operation: Computes `supplied_crs` from `_crs(supplied.crs, label)`. Computes `expected_crs` from `_crs(expected.crs, f'expected {label}')`. Computes `geometry_equal` from `np.array_equal(supplied.geometry.to_wkb(), expected.geometry.to_wkb())`. Computes `attributes_equal` from `supplied.drop(columns='geometry').equals(expected.drop(columns='geometry'))`. Handles `PlanningFeaturesError`, `Exception`.
3. Checks `not supplied_crs.equals(expected_crs) or not geometry_equal or (not attributes_equal)`. When true: Raises `PlanningFeaturesError(f'{label} differs from normalized GPU source')`.

**Validation and invariants**

- Rejects or diverts the path when `deterministic_frame_schema_signature(supplied) != deterministic_frame_schema_signature(expected)` is true.
- Rejects or diverts the path when `not supplied_crs.equals(expected_crs) or not geometry_equal or (not attributes_equal)` is true.

**Exceptions**

- Explicitly raises: `PlanningFeaturesError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningFeaturesError`, `_crs`, `deterministic_frame_schema_signature`, `expected.drop`, `expected.geometry.to_wkb`, `np.array_equal`, `supplied.drop`, `supplied.drop(columns='geometry').equals`, `supplied.geometry.to_wkb`, `supplied_crs.equals`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `_validate_normalized_planning_feature_inputs`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_relation_catalog_consistency`

**Signature**

```python
def _validate_relation_catalog_consistency(
    relations: pd.DataFrame,
    catalogs: tuple[gpd.GeoDataFrame, gpd.GeoDataFrame, gpd.GeoDataFrame],
) -> None:
```

**Purpose**

Validates and rejects malformed relation catalog consistency according to the exact implementation and guards in this file.

**Inputs**

- `relations` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `catalogs` (`tuple[gpd.GeoDataFrame, gpd.GeoDataFrame, gpd.GeoDataFrame]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `feature_rows` from `pd.concat([catalog.drop(columns='geometry') for catalog in catalogs], ignore_index=True)`.
2. Checks `feature_rows['planning_feature_id'].duplicated().any()`. When true: Raises `PlanningFeaturesError('planning_feature_id values must be globally unique')`.
3. Computes `indexed` from `feature_rows.set_index('planning_feature_id', drop=False)`.
4. Iterates `(_, relation)` over `relations.iterrows()`. For each value: Computes `identifier` from `relation['planning_feature_id']`. Checks `identifier not in indexed.index`. When true: Raises `PlanningFeaturesError('Planning relation references an unknown feature')`. Computes `feature` from `indexed.loc[identifier]`. Executes 5 additional source-ordered statement(s).

**Validation and invariants**

- Rejects or diverts the path when `feature_rows['planning_feature_id'].duplicated().any()` is true.
- Rejects or diverts the path when `identifier not in indexed.index` is true.
- Rejects or diverts the path when `metric_column is None or catalog_column is None or (not _null_safe_equal(relation[metric_column], feature[catalog_column]))` is true.
- Rejects or diverts the path when `not _null_safe_equal(relation[column], feature[column])` is true.

**Exceptions**

- Explicitly raises: `PlanningFeaturesError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningFeaturesError`, `_null_safe_equal`, `catalog.drop`, `feature_rows.set_index`, `feature_rows['planning_feature_id'].duplicated`, `feature_rows['planning_feature_id'].duplicated().any`, `pd.concat`, `relations.iterrows`, `{'SURFACE': 'feature_area_m2', 'LINE': 'feature_length_m', 'POINT': 'point_member_count'}.get`, `{'SURFACE': 'feature_area_m2', 'LINE': 'source_line_length_m', 'POINT': 'point_member_count'}.get`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `_validate_normalized_planning_feature_inputs`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_relation_semantics`

**Signature**

```python
def _validate_relation_semantics(relations: pd.DataFrame) -> None:
```

**Purpose**

Validates and rejects malformed relation semantics according to the exact implementation and guards in this file.

**Inputs**

- `relations` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Runs guarded operation: Calls `validate_intrinsic_planning_feature_relations(relations)` for its validation or side effect. Handles `(TypeError, ValueError)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `PlanningFeaturesError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningFeaturesError`, `str`, `validate_intrinsic_planning_feature_relations`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `_validate_normalized_planning_feature_inputs`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_compare_rebuilt_relations`

**Signature**

```python
def _compare_rebuilt_relations(
    supplied: pd.DataFrame,
    expected: pd.DataFrame,
) -> None:
```

**Purpose**

Compares rebuilt relations according to the exact implementation and guards in this file.

**Inputs**

- `supplied` (`pd.DataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `expected` (`pd.DataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `deterministic_frame_schema_signature(supplied) != deterministic_frame_schema_signature(expected)`. When true: Raises `PlanningFeaturesError('Planning relation schema differs from the spatial reconstruction')`.
2. Checks `not supplied.index.equals(expected.index)`. When true: Raises `PlanningFeaturesError('Planning relation index or row order differs from the spatial reconstruction')`.
3. Checks `len(supplied) != len(expected)`. When true: Raises `PlanningFeaturesError('Planning relation count differs from the spatial reconstruction')`.
4. Iterates `column` over `RELATION_COLUMNS`. For each value: Computes `actual_values` from `supplied[column].tolist()`. Computes `expected_values` from `expected[column].tolist()`. Iterates `(position, (actual, rebuilt))` over `enumerate(zip(actual_values, expected_values, strict=True))`. For each value: Computes `label` from `f'Planning relation {column} at row {position}'`. Checks `column in RELATION_FLOAT_COLUMNS`. When true: Computes `actual_missing` from `bool(pd.isna(actual))`. Computes `expected_missing` from `bool(pd.isna(rebuilt))`. Checks `actual_missing or expected_missing`. When true: Checks `actual_missing != expected_missing`. When true: Raises `PlanningFeaturesError(f'{label} null pattern differs from spatial reconstruction')`. Executes `continue` control flow. Executes 1 additional source-ordered statement(s). Otherwise: Checks `not _null_safe_equal(actual, rebuilt)`. When true: Raises `PlanningFeaturesError(f'{label} differs from the spatial reconstruction')`.

**Validation and invariants**

- Rejects or diverts the path when `deterministic_frame_schema_signature(supplied) != deterministic_frame_schema_signature(expected)` is true.
- Rejects or diverts the path when `not supplied.index.equals(expected.index)` is true.
- Rejects or diverts the path when `len(supplied) != len(expected)` is true.
- Rejects or diverts the path when `column in RELATION_FLOAT_COLUMNS` is true.
- Rejects or diverts the path when `actual_missing or expected_missing` is true.
- Rejects or diverts the path when `not _null_safe_equal(actual, rebuilt)` is true.
- Rejects or diverts the path when `actual_missing != expected_missing` is true.

**Exceptions**

- Explicitly raises: `PlanningFeaturesError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningFeaturesError`, `_null_safe_equal`, `_require_close`, `bool`, `deterministic_frame_schema_signature`, `enumerate`, `expected[column].tolist`, `float`, `len`, `pd.isna`, `supplied.index.equals`, `supplied[column].tolist`, `zip`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `_validate_normalized_planning_feature_inputs`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_compare_rebuilt_parcel_output`

**Signature**

```python
def _compare_rebuilt_parcel_output(
    supplied: gpd.GeoDataFrame,
    expected: gpd.GeoDataFrame,
) -> None:
```

**Purpose**

Compares rebuilt parcel output according to the exact implementation and guards in this file.

**Inputs**

- `supplied` (`gpd.GeoDataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `expected` (`gpd.GeoDataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `deterministic_frame_schema_signature(supplied) != deterministic_frame_schema_signature(expected)`. When true: Raises `PlanningFeaturesError('Planning-feature parcel output schema differs from reconstruction')`.
2. Checks `not supplied.index.equals(expected.index)`. When true: Raises `PlanningFeaturesError('Planning-feature parcel output index differs from reconstruction')`.
3. Checks `not _crs(supplied.crs, 'Parcel output').equals(_crs(expected.crs, 'Expected parcel output')) or not np.array_equal(supplied.geometry.to_wkb(), expected.geometry.to_wkb())`. When true: Raises `PlanningFeaturesError('Planning-feature parcel geometry or CRS differs from reconstruction')`.
4. Computes `summary_float_columns` from `PARCEL_OUTPUT_COLUMNS - PARCEL_COUNT_COLUMNS - {'planning_feature_document_id', 'planning_feature_archive_sha256'}`.
5. Iterates `column` over `supplied.columns`. For each value: Checks `column == 'geometry'`. When true: Executes `continue` control flow. Checks `column in summary_float_columns`. When true: Iterates `(position, (actual, rebuilt))` over `enumerate(zip(supplied[column].tolist(), expected[column].tolist(), strict=True))`. For each value: Calls `_require_close(actual, float(rebuilt), f'Parcel summary {column} at row {position}')` for its validation or side effect. Otherwise: Checks `not supplied[column].equals(expected[column])`. When true: Raises `PlanningFeaturesError(f'Planning-feature parcel column {column} differs from reconstruction')`.

**Validation and invariants**

- Rejects or diverts the path when `deterministic_frame_schema_signature(supplied) != deterministic_frame_schema_signature(expected)` is true.
- Rejects or diverts the path when `not supplied.index.equals(expected.index)` is true.
- Rejects or diverts the path when `not _crs(supplied.crs, 'Parcel output').equals(_crs(expected.crs, 'Expected parcel output')) or not np.array_equal(supplied.geometry.to_wkb(), expected.geometry.to_wkb())` is true.
- Rejects or diverts the path when `not supplied[column].equals(expected[column])` is true.

**Exceptions**

- Explicitly raises: `PlanningFeaturesError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningFeaturesError`, `_crs`, `_crs(supplied.crs, 'Parcel output').equals`, `_require_close`, `deterministic_frame_schema_signature`, `enumerate`, `expected.geometry.to_wkb`, `expected[column].tolist`, `float`, `np.array_equal`, `supplied.geometry.to_wkb`, `supplied.index.equals`, `supplied[column].equals`, `supplied[column].tolist`, `zip`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `_validate_normalized_planning_feature_inputs`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_normalized_planning_feature_inputs`

**Signature**

```python
def _validate_normalized_planning_feature_inputs(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
) -> PlanningFeatureInputValidation:
```

**Purpose**

Validate exact STEP 7D.3.1 facts against their document and parcels.

**Inputs**

- `planning_document` (`GpuPlanningDocument`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `surface_features` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `line_features` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `point_features` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `relations` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `PlanningFeatureInputValidation`. Observed return expression(s): `PlanningFeatureInputValidation(gpu_related_source_files_sha256=_gpu_related_source_files_sha256(planning_document, validated_sources), expected_relations_content_sha256=_expected_relations_content_sha256(expected_relations), related_source_layer_count=len(validated_sources), related_source_file_count=len(unique_files), expected_relation_count=len(expected_relations))`.

**Algorithm**

1. Computes `present_outputs` from `PARCEL_OUTPUT_COLUMNS & set(parcels.columns)`.
2. Checks `present_outputs and present_outputs != PARCEL_OUTPUT_COLUMNS`. When true: Computes `missing` from `sorted(PARCEL_OUTPUT_COLUMNS - present_outputs)`. Raises `PlanningFeaturesError('Parcel planning-feature summaries are incomplete: ' + ', '.join(missing))`.
3. Calls `_validate_parcels(parcels, allow_output_columns=True)` for its validation or side effect.
4. Computes `source_parcels` from `parcels.drop(columns=list(PARCEL_OUTPUT_COLUMNS)) if present_outputs else parcels`.
5. Calls `_validate_parcels(source_parcels)` for its validation or side effect.
6. Computes `metric_parcels` from `_metric_parcels(source_parcels)`.
7. Computes `(surfaces, lines, points, validated_sources)` from `_normalized_catalogs(planning_document)`.
8. Computes `expected_catalogs` from `(surfaces, lines, points)`.
9. Computes `catalogs` from `(_validate_catalog_contract(surface_features, 'SURFACE'), _validate_catalog_contract(line_features, 'LINE'), _validate_catalog_contract(point_features, 'POINT'))`.
10. Iterates `(supplied, expected, label)` over `zip(catalogs, expected_catalogs, ('SURFACE feature catalog', 'LINE feature catalog', 'POINT feature catalog'), strict=True)`. For each value: Calls `_compare_normalized_catalog(supplied, expected, label)` for its validation or side effect.
11. Computes `all_feature_ids` from `[identifier for catalog in catalogs for identifier in catalog['planning_feature_id'].tolist()]`.
12. Checks `len(all_feature_ids) != len(set(all_feature_ids))`. When true: Raises `PlanningFeaturesError('planning_feature_id values must be globally unique')`.
13. Checks `not isinstance(relations, pd.DataFrame) or isinstance(relations, gpd.GeoDataFrame)`. When true: Raises `PlanningFeaturesError('Planning relations must be a DataFrame')`.
14. Runs guarded operation: Calls `validate_canonical_frame_schema(relations, columns=RELATION_COLUMNS, dtypes=NORMALIZED_RELATION_DTYPES, label='Planning relations', geospatial=False, index_class='RangeIndex')` for its validation or side effect. Handles `(TypeError, ValueError)`.
15. Calls `_validate_exact_strings(relations['parcel_id'], 'planning relation parcel_id')` for its validation or side effect.
16. Calls `_validate_exact_strings(relations['planning_feature_id'], 'planning relation planning_feature_id')` for its validation or side effect.
17. Checks `relations.duplicated(['parcel_id', 'planning_feature_id']).any()`. When true: Raises `PlanningFeaturesError('Parcel/planning-feature relations must be unique')`.
18. Checks `not set(relations['planning_feature_id']).issubset(set(all_feature_ids))`. When true: Raises `PlanningFeaturesError('Planning relation references an unknown feature')`.
19. Computes `parcel_areas` from `dict(zip(metric_parcels['parcel_id'].tolist(), metric_parcels['_parcel_area_m2'].tolist(), strict=True))`.
20. Iterates `(parcel_id, actual_area)` over `relations[['parcel_id', 'parcel_metric_area_m2']].itertuples(index=False, name=None)`. For each value: Checks `parcel_id not in parcel_areas`. When true: Raises `PlanningFeaturesError('Planning relation references an unknown source parcel')`. Calls `_require_close(actual_area, float(parcel_areas[parcel_id]), 'Relation parcel metric area')` for its validation or side effect.
21. Calls `_validate_relation_semantics(relations)` for its validation or side effect.
22. Calls `_validate_relation_catalog_consistency(relations, catalogs)` for its validation or side effect.
23. Computes `(surface_work, line_work, point_work, expected_relations)` from `_build_relation_tables(metric_parcels, *expected_catalogs)`.
24. Calls `_compare_rebuilt_relations(relations, expected_relations)` for its validation or side effect.
25. Checks `present_outputs`. When true: Computes `context` from `_planning_context(planning_document)`. Computes `expected_output` from `_attach_parcel_summaries(source_parcels, metric_parcels, surface_work, line_work, point_work, context)`. Calls `_compare_rebuilt_parcel_output(parcels, expected_output)` for its validation or side effect. Executes 3 additional source-ordered statement(s).
26. Computes `unique_files` from `{item.relative_path for source in validated_sources for item in source.files}`.
27. Returns `PlanningFeatureInputValidation(gpu_related_source_files_sha256=_gpu_related_source_files_sha256(planning_document, validated_sources), expected_relations_content_sha256=_expected_relations_content_sha256(expected_relations), related_source_layer_count=len(validated_sources), related_source_file_count=len(unique_files), expected_relation_count=len(expected_r…`.

**Validation and invariants**

- Rejects or diverts the path when `present_outputs and present_outputs != PARCEL_OUTPUT_COLUMNS` is true.
- Rejects or diverts the path when `len(all_feature_ids) != len(set(all_feature_ids))` is true.
- Rejects or diverts the path when `not isinstance(relations, pd.DataFrame) or isinstance(relations, gpd.GeoDataFrame)` is true.
- Rejects or diverts the path when `relations.duplicated(['parcel_id', 'planning_feature_id']).any()` is true.
- Rejects or diverts the path when `not set(relations['planning_feature_id']).issubset(set(all_feature_ids))` is true.
- Rejects or diverts the path when `present_outputs` is true.
- Rejects or diverts the path when `parcel_id not in parcel_areas` is true.
- Rejects or diverts the path when `not parcels['planning_feature_document_id'].eq(context.document_id).all()` is true.
- Rejects or diverts the path when `not parcels['planning_feature_archive_sha256'].eq(context.archive_sha256).all()` is true.

**Exceptions**

- Explicitly raises: `PlanningFeaturesError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `', '.join`, `PlanningFeatureInputValidation`, `PlanningFeaturesError`, `_attach_parcel_summaries`, `_build_relation_tables`, `_compare_normalized_catalog`, `_compare_rebuilt_parcel_output`, `_compare_rebuilt_relations`, `_expected_relations_content_sha256`, `_gpu_related_source_files_sha256`, `_metric_parcels`, `_normalized_catalogs`, `_planning_context`, `_require_close`, `_validate_catalog_contract`, `_validate_exact_strings`, `_validate_parcel_summaries`, `_validate_parcels`, `_validate_relation_catalog_consistency`, `_validate_relation_semantics`, `catalog['planning_feature_id'].tolist`, `dict`, `float`, `isinstance`, `len`, `list`, `metric_parcels['_parcel_area_m2'].tolist`, `metric_parcels['parcel_id'].tolist`, `parcels.drop`, `parcels['planning_feature_archive_sha256'].eq`, `parcels['planning_feature_archive_sha256'].eq(context.archive_sha256).all`, `parcels['planning_feature_document_id'].eq`, `parcels['planning_feature_document_id'].eq(context.document_id).all`, `relations.duplicated`, `relations.duplicated(['parcel_id', 'planning_feature_id']).any`, `relations[['parcel_id', 'parcel_metric_area_m2']].itertuples`, `set`, `set(relations['planning_feature_id']).issubset`, `sorted`, `str`, `validate_canonical_frame_schema`, `zip`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `validate_normalized_planning_feature_inputs`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `validate_normalized_planning_feature_inputs`

**Signature**

```python
def validate_normalized_planning_feature_inputs(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
) -> PlanningFeatureInputValidation:
```

**Purpose**

Validate exact STEP 7D.3.1 facts against their document and parcels.

**Inputs**

- `planning_document` (`GpuPlanningDocument`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `surface_features` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `line_features` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `point_features` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `relations` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `PlanningFeatureInputValidation`. Observed return expression(s): `_validate_normalized_planning_feature_inputs(planning_document, parcels, surface_features, line_features, point_features, relations)`.

**Algorithm**

1. Runs guarded operation: Returns `_validate_normalized_planning_feature_inputs(planning_document, parcels, surface_features, line_features, point_features, relations)`. Handles `PlanningFeaturesError`, `Exception`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `PlanningFeaturesError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningFeaturesError`, `_validate_normalized_planning_feature_inputs`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `_validate_result`
- `src/landscout/stages/resolve_planning_feature_codes.py` — `_build_result`
- `src/landscout/stages/resolve_planning_feature_codes.py` — `resolve_planning_feature_codes`
- `tests/unit/test_enrich_planning_features.py` — `_validate_source_complete`
- `tests/unit/test_enrich_planning_features.py` — `test_public_normalized_input_contract_rejects_stripped_catalog`
- `tests/unit/test_enrich_planning_features.py` — `test_public_normalized_input_contract_validates_step_7d_3_1_result`
- `tests/unit/test_enrich_planning_features.py` — `test_public_source_validation_hashes_survive_parquet_readback`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_relation_index_class_change`

**Tests**

- `tests/unit/test_enrich_planning_features.py::test_public_normalized_input_contract_rejects_stripped_catalog`
- `tests/unit/test_enrich_planning_features.py::test_public_normalized_input_contract_validates_step_7d_3_1_result`
- `tests/unit/test_enrich_planning_features.py::test_public_source_validation_hashes_survive_parquet_readback`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_relation_index_class_change`

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_parcel_summaries`

**Signature**

```python
def _validate_parcel_summaries(
    source: gpd.GeoDataFrame,
    output: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    surface_work: pd.DataFrame | None,
) -> None:
```

**Purpose**

Validates and rejects malformed parcel summaries according to the exact implementation and guards in this file.

**Inputs**

- `source` (`gpd.GeoDataFrame`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `output` (`gpd.GeoDataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `relations` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `surface_work` (`pd.DataFrame | None`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `metric` from `_metric_parcels(source)`.
2. Computes `metric_areas` from `dict(zip(metric['parcel_id'].tolist(), metric['_parcel_area_m2'].tolist(), strict=True))`.
3. Calls `_integer_values(output, PARCEL_COUNT_COLUMNS, 'Parcel summary', allow_null=False)` for its validation or side effect.
4. Computes `float_columns` from `tuple(PARCEL_OUTPUT_COLUMNS - PARCEL_COUNT_COLUMNS - {'planning_feature_document_id', 'planning_feature_archive_sha256'})`.
5. Calls `_numeric_values(output, float_columns, 'Parcel summary', allow_null=False)` for its validation or side effect.
6. Iterates `(_, parcel)` over `output.iterrows()`. For each value: Computes `parcel_id` from `parcel['parcel_id']`. Computes `rows` from `relations.loc[relations['parcel_id'] == parcel_id]`. Computes `surfaces` from `rows.loc[rows['geometry_kind'] == 'SURFACE']`. Executes 14 additional source-ordered statement(s).
7. Checks `surface_work is not None`. When true: Computes `areas` from `metric['_parcel_area_m2'].to_numpy(dtype='float64')`. Computes `positive` from `surface_work.loc[surface_work['relation_type'] == 'AREA_OVERLAP'] if not surface_work.empty else surface_work`. Computes `expected_total` from `_surface_union_summary(positive, areas, len(output))`. Executes 1 additional source-ordered statement(s).

**Validation and invariants**

- Rejects or diverts the path when `planning_union - raw_sum > technical_overlay_tolerance(raw_sum)` is true.
- Rejects or diverts the path when `planning_union - parcel_area > technical_overlay_tolerance(parcel_area)` is true.
- Rejects or diverts the path when `parcel[column] != expected` is true.
- Rejects or diverts the path when `union - planning_union > technical_overlay_tolerance(planning_union)` is true.
- Rejects or diverts the path when `abs(pct - expected_pct) > pct_tolerance` is true.

**Exceptions**

- Explicitly raises: `PlanningFeaturesError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningFeaturesError`, `_integer_values`, `_metric_parcels`, `_numeric_values`, `_require_close`, `_surface_union_summary`, `abs`, `dict`, `exact_counts.items`, `float`, `int`, `len`, `lines['intersection_length_m'].sum`, `lines['relation_type'].eq`, `lines['relation_type'].eq('LENGTH_OVERLAP').sum`, `lines['relation_type'].eq('TOUCH_ONLY').sum`, `metric['_parcel_area_m2'].to_numpy`, `metric['_parcel_area_m2'].tolist`, `metric['parcel_id'].tolist`, `output.iterrows`, `output[column].tolist`, `points['point_members_boundary_count'].sum`, `points['point_members_inside_count'].sum`, `positive_surfaces['intersection_area_m2'].sum`, `surfaces['feature_family'].eq`, `surfaces['feature_family'].eq('INFORMATION').sum`, `surfaces['feature_family'].eq('PRESCRIPTION').sum`, `surfaces['relation_type'].eq`, `surfaces['relation_type'].eq('TOUCH_ONLY').sum`, `technical_overlay_tolerance`, `tuple`, `zip`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `_validate_normalized_planning_feature_inputs`
- `src/landscout/stages/enrich_planning_features.py` — `_validate_result`

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
    source: gpd.GeoDataFrame,
    result: ParcelPlanningFeaturesResult,
    surface_work: pd.DataFrame | None = None,
    *,
    planning_document: GpuPlanningDocument,
    source_inputs_already_rebuilt: bool = False,
) -> None:
```

**Purpose**

Validates and rejects malformed result according to the exact implementation and guards in this file.

**Inputs**

- `source` (`gpd.GeoDataFrame`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `result` (`ParcelPlanningFeaturesResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `surface_work` (`pd.DataFrame | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `planning_document` (`GpuPlanningDocument`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `source_inputs_already_rebuilt` (`bool`; optional/default `False`) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `output` from `result.parcels`.
2. Computes `missing_output` from `sorted(PARCEL_OUTPUT_COLUMNS - set(output.columns))`.
3. Checks `missing_output`. When true: Raises `PlanningFeaturesError('Planning-feature parcel output is missing columns: ' + ', '.join(missing_output))`.
4. Checks `len(output) != len(source)`. When true: Raises `PlanningFeaturesError('Planning-feature parcel count changed')`.
5. Checks `output['parcel_id'].tolist() != source['parcel_id'].tolist()`. When true: Raises `PlanningFeaturesError('Planning-feature parcel IDs or order changed')`.
6. Checks `not output.index.equals(source.index)`. When true: Raises `PlanningFeaturesError('Planning-feature parcel index changed')`.
7. Checks `output.crs != source.crs or not np.array_equal(output.geometry.to_wkb(), source.geometry.to_wkb())`. When true: Raises `PlanningFeaturesError('Planning-feature parcel geometry or CRS changed')`.
8. Iterates `column` over `source.columns`. For each value: Checks `column == 'geometry'`. When true: Executes `continue` control flow. Checks `not output[column].equals(source[column])`. When true: Raises `PlanningFeaturesError(f'Existing parcel column changed: {column}')`.
9. Computes `catalogs` from `(result.surface_features, result.line_features, result.point_features)`.
10. Checks `not source_inputs_already_rebuilt`. When true: Calls `validate_normalized_planning_feature_inputs(planning_document, source, *catalogs, result.relations)` for its validation or side effect.
11. Computes `all_feature_ids` from `[identifier for catalog in catalogs for identifier in catalog['planning_feature_id'].tolist()]`.
12. Computes `known_features` from `set(all_feature_ids)`.
13. Computes `relations` from `result.relations`.
14. Checks `not set(relations['parcel_id']).issubset(set(output['parcel_id']))`. When true: Raises `PlanningFeaturesError('Planning relation references an unknown parcel')`.
15. Checks `not set(relations['planning_feature_id']).issubset(known_features)`. When true: Raises `PlanningFeaturesError('Planning relation references an unknown feature')`.
16. Calls `_validate_parcel_summaries(source, output, relations, surface_work)` for its validation or side effect.
17. Iterates `column` over `('planning_feature_document_id', 'planning_feature_archive_sha256')`. For each value: Calls `_validate_exact_strings(output[column], column)` for its validation or side effect.
18. Computes `nonempty_catalogs` from `[catalog for catalog in catalogs if not catalog.empty]`.
19. Checks `nonempty_catalogs`. When true: Computes `expected_document_ids` from `{value for catalog in nonempty_catalogs for value in catalog['source_document_id'].tolist()}`. Computes `expected_archive_hashes` from `{value for catalog in nonempty_catalogs for value in catalog['source_archive_sha256'].tolist()}`. Checks `len(expected_document_ids) != 1 or len(expected_archive_hashes) != 1 or set(output['planning_feature_document_id']) != expected_document_ids or (set(output['planning_feature_archive_sha256']) != expected_archive_hashes)`. When true: Raises `PlanningFeaturesError('Parcel planning-feature lineage is inconsistent with catalogs')`.

**Validation and invariants**

- Rejects or diverts the path when `missing_output` is true.
- Rejects or diverts the path when `len(output) != len(source)` is true.
- Rejects or diverts the path when `output['parcel_id'].tolist() != source['parcel_id'].tolist()` is true.
- Rejects or diverts the path when `not output.index.equals(source.index)` is true.
- Rejects or diverts the path when `output.crs != source.crs or not np.array_equal(output.geometry.to_wkb(), source.geometry.to_wkb())` is true.
- Rejects or diverts the path when `not set(relations['parcel_id']).issubset(set(output['parcel_id']))` is true.
- Rejects or diverts the path when `not set(relations['planning_feature_id']).issubset(known_features)` is true.
- Rejects or diverts the path when `nonempty_catalogs` is true.
- Rejects or diverts the path when `not output[column].equals(source[column])` is true.
- Rejects or diverts the path when `len(expected_document_ids) != 1 or len(expected_archive_hashes) != 1 or set(output['planning_feature_document_id']) != expected_document_ids or (set(output['planning_feature_archive_sha256']) != expected_archive_hashes)` is true.

**Exceptions**

- Explicitly raises: `PlanningFeaturesError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `', '.join`, `PlanningFeaturesError`, `_validate_exact_strings`, `_validate_parcel_summaries`, `catalog['planning_feature_id'].tolist`, `catalog['source_archive_sha256'].tolist`, `catalog['source_document_id'].tolist`, `len`, `np.array_equal`, `output.geometry.to_wkb`, `output.index.equals`, `output['parcel_id'].tolist`, `output[column].equals`, `set`, `set(relations['parcel_id']).issubset`, `set(relations['planning_feature_id']).issubset`, `sorted`, `source.geometry.to_wkb`, `source['parcel_id'].tolist`, `validate_normalized_planning_feature_inputs`.

**Known repository callers**

- `src/landscout/stages/enrich_planning_features.py` — `intersect_parcels_with_gpu_planning_features`
- `tests/unit/test_enrich_planning_features.py` — `test_corrupted_parcel_summary_is_rejected`
- `tests/unit/test_enrich_planning_features.py` — `test_corrupted_relation_semantics_are_rejected`
- `tests/unit/test_enrich_planning_features.py` — `test_corrupted_surface_union_contract_is_rejected`
- `tests/unit/test_enrich_planning_features.py` — `test_feature_ids_are_globally_unique_across_catalogs`
- `tests/unit/test_enrich_planning_features.py` — `test_point_member_relation_semantics_are_exact`
- `tests/unit/test_enrich_planning_features.py` — `test_relation_must_match_feature_catalog`
- `tests/unit/test_enrich_planning_features.py` — `test_strict_parcel_summary_integer_counts_are_enforced`
- `tests/unit/test_enrich_planning_features.py` — `test_strict_relation_integer_counts_are_enforced`

**Tests**

- `tests/unit/test_enrich_planning_features.py::test_corrupted_parcel_summary_is_rejected`
- `tests/unit/test_enrich_planning_features.py::test_corrupted_relation_semantics_are_rejected`
- `tests/unit/test_enrich_planning_features.py::test_corrupted_surface_union_contract_is_rejected`
- `tests/unit/test_enrich_planning_features.py::test_feature_ids_are_globally_unique_across_catalogs`
- `tests/unit/test_enrich_planning_features.py::test_point_member_relation_semantics_are_exact`
- `tests/unit/test_enrich_planning_features.py::test_relation_must_match_feature_catalog`
- `tests/unit/test_enrich_planning_features.py::test_strict_parcel_summary_integer_counts_are_enforced`
- `tests/unit/test_enrich_planning_features.py::test_strict_relation_integer_counts_are_enforced`

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `intersect_parcels_with_gpu_planning_features`

**Signature**

```python
def intersect_parcels_with_gpu_planning_features(
    parcels: gpd.GeoDataFrame,
    planning_document: GpuPlanningDocument,
) -> ParcelPlanningFeaturesResult:
```

**Purpose**

Measure factual GPU prescription/information relations to full parcels. All metric work is planar XY in EPSG:2154. Raw codes are preserved without interpretation, and every pre-existing parcel field and geometry is copied.

**Inputs**

- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `planning_document` (`GpuPlanningDocument`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `ParcelPlanningFeaturesResult`. Observed return expression(s): `result`.

**Algorithm**

1. Calls `_validate_parcels(parcels)` for its validation or side effect.
2. Computes `context` from `_planning_context(planning_document)`.
3. Computes `(surfaces, lines, points, _)` from `_normalized_catalogs(planning_document)`.
4. Computes `metric` from `_metric_parcels(parcels)`.
5. Computes `(surface_work, line_work, point_work, relations)` from `_build_relation_tables(metric, surfaces, lines, points)`.
6. Computes `parcel_output` from `_attach_parcel_summaries(parcels, metric, surface_work, line_work, point_work, context)`.
7. Computes `result` from `ParcelPlanningFeaturesResult(parcels=parcel_output, surface_features=surfaces, line_features=lines, point_features=points, relations=relations)`.
8. Calls `_validate_result(parcels, result, surface_work, planning_document=planning_document, source_inputs_already_rebuilt=True)` for its validation or side effect.
9. Returns `result`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ParcelPlanningFeaturesResult`, `_attach_parcel_summaries`, `_build_relation_tables`, `_metric_parcels`, `_normalized_catalogs`, `_planning_context`, `_validate_parcels`, `_validate_result`.

**Known repository callers**

- `tests/unit/test_enrich_planning_features.py` — `_contract_result`
- `tests/unit/test_enrich_planning_features.py` — `_run`
- `tests/unit/test_enrich_planning_features.py` — `_shapefile_ogr_fid_source_complete_contract`
- `tests/unit/test_enrich_planning_features.py` — `_shapefile_source_complete_contract`
- `tests/unit/test_enrich_planning_features.py` — `_source_complete_contract`
- `tests/unit/test_enrich_planning_features.py` — `_two_parcel_source_complete_contract`
- `tests/unit/test_enrich_planning_features.py` — `test_inputs_and_all_existing_parcel_fields_are_preserved`
- `tests/unit/test_enrich_planning_features.py` — `test_mutated_source_summary_is_rejected`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_accepts_epsg4326_parcels`
- `tests/unit/test_enrich_planning_features.py` — `test_source_complete_contract_rejects_reordered_physical_gpkg_rows`
- `tests/unit/test_enrich_planning_features.py` — `test_source_document_reference_allows_one_archive_zip_suffix`
- `tests/unit/test_enrich_planning_features.py` — `test_source_summary_counts_are_strict_integers`
- `tests/unit/test_resolve_planning_feature_codes.py` — `_integration_inputs`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_valid_empty_optional_catalogs_preserve_schema_and_crs`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_valid_multi_geometries_are_accepted`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_valid_relation_types_are_retained`

**Tests**

- `tests/unit/test_enrich_planning_features.py::test_inputs_and_all_existing_parcel_fields_are_preserved`
- `tests/unit/test_enrich_planning_features.py::test_mutated_source_summary_is_rejected`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_accepts_epsg4326_parcels`
- `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_reordered_physical_gpkg_rows`
- `tests/unit/test_enrich_planning_features.py::test_source_document_reference_allows_one_archive_zip_suffix`
- `tests/unit/test_enrich_planning_features.py::test_source_summary_counts_are_strict_integers`
- `tests/unit/test_resolve_planning_feature_codes.py::test_valid_empty_optional_catalogs_preserve_schema_and_crs`
- `tests/unit/test_resolve_planning_feature_codes.py::test_valid_multi_geometries_are_accepted`
- `tests/unit/test_resolve_planning_feature_codes.py::test_valid_relation_types_are_retained`

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `ARCHIVE_SCOPED_OGR_FID` | Logical dtype: mapping/domain key (not asserted as a DataFrame column). Nullability: not applicable as a column. | exact lookup/domain label used by an implementation mapping; it is intentionally not presented as a contractual frame column. Consumers and exact calculations are the functions that reference this column above. |
| `CNIG_ATTRIBUTE` | Logical dtype: mapping/domain key (not asserted as a DataFrame column). Nullability: not applicable as a column. | exact lookup/domain label used by an implementation mapping; it is intentionally not presented as a contractual frame column. Consumers and exact calculations are the functions that reference this column above. |
| `IDURBA` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `INFORMATION` | Logical dtype: mapping/domain key (not asserted as a DataFrame column). Nullability: not applicable as a column. | exact lookup/domain label used by an implementation mapping; it is intentionally not presented as a contractual frame column. Consumers and exact calculations are the functions that reference this column above. |
| `LINE` | Logical dtype: mapping/domain key (not asserted as a DataFrame column). Nullability: not applicable as a column. | exact lookup/domain label used by an implementation mapping; it is intentionally not presented as a contractual frame column. Consumers and exact calculations are the functions that reference this column above. |
| `POINT` | Logical dtype: mapping/domain key (not asserted as a DataFrame column). Nullability: not applicable as a column. | exact lookup/domain label used by an implementation mapping; it is intentionally not presented as a contractual frame column. Consumers and exact calculations are the functions that reference this column above. |
| `PRESCRIPTION` | Logical dtype: mapping/domain key (not asserted as a DataFrame column). Nullability: not applicable as a column. | exact lookup/domain label used by an implementation mapping; it is intentionally not presented as a contractual frame column. Consumers and exact calculations are the functions that reference this column above. |
| `SURFACE` | Logical dtype: mapping/domain key (not asserted as a DataFrame column). Nullability: not applicable as a column. | exact lookup/domain label used by an implementation mapping; it is intentionally not presented as a contractual frame column. Consumers and exact calculations are the functions that reference this column above. |
| `_feature_position` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `_intersection_geometry` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `_parcel_area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `_parcel_position` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `columns` | Logical dtype: mapping/domain key (not asserted as a DataFrame column). Nullability: not applicable as a column. | exact lookup/domain label used by an implementation mapping; it is intentionally not presented as a contractual frame column. Consumers and exact calculations are the functions that reference this column above. |
| `drop` | Logical dtype: mapping/domain key (not asserted as a DataFrame column). Nullability: not applicable as a column. | exact lookup/domain label used by an implementation mapping; it is intentionally not presented as a contractual frame column. Consumers and exact calculations are the functions that reference this column above. |
| `feature_area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `feature_family` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `feature_length_m` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | linear distance/length in metres; proxy meaning is limited by the introducing stage. Consumers and exact calculations are the functions that reference this column above. |
| `feature_share_pct` | Logical dtype: float64. Nullability: determined by the owning schema/dtype map and explicit null guards. | percentage derived from the exact numerator/denominator named by its stage. Consumers and exact calculations are the functions that reference this column above. |
| `geometry` | Logical dtype: GeoPandas active geometry dtype. Nullability: nullable only where the source-stage geometry-status contract explicitly preserves nulls. | source or preserved spatial geometry; never itself a suitability or legal conclusion. Consumers and exact calculations are the functions that reference this column above. |
| `geometry_kind` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `intersection_area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `intersection_length_m` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | linear distance/length in metres; proxy meaning is limited by the introducing stage. Consumers and exact calculations are the functions that reference this column above. |
| `kind` | Logical dtype: mapping/domain key (not asserted as a DataFrame column). Nullability: not applicable as a column. | exact lookup/domain label used by an implementation mapping; it is intentionally not presented as a contractual frame column. Consumers and exact calculations are the functions that reference this column above. |
| `label_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `logical_layer` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `parcel_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `parcel_metric_area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `parcel_share_pct` | Logical dtype: float64. Nullability: determined by the owning schema/dtype map and explicit null guards. | percentage derived from the exact numerator/denominator named by its stage. Consumers and exact calculations are the functions that reference this column above. |
| `planning_feature_archive_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `planning_feature_document_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `planning_feature_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `planning_line_intersection_length_sum_m` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | linear distance/length in metres; proxy meaning is limited by the introducing stage. Consumers and exact calculations are the functions that reference this column above. |
| `planning_line_length_overlap_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `planning_line_relation_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `planning_line_touch_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `planning_point_relation_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `planning_surface_area_overlap_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `planning_surface_covered_pct` | Logical dtype: float64. Nullability: determined by the owning schema/dtype map and explicit null guards. | percentage derived from the exact numerator/denominator named by its stage. Consumers and exact calculations are the functions that reference this column above. |
| `planning_surface_covered_union_area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `planning_surface_intersection_area_sum_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `planning_surface_relation_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `planning_surface_touch_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `point_member_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `point_members_boundary_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `point_members_inside_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `regulation_filename_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `regulation_url_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `relation_type` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `source_archive_name` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_archive_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `source_commune_code` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_crs` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_document_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `source_document_reference_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `source_document_type` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `source_feature_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `source_identity_field` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_identity_kind` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `source_layer` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_line_length_m` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | linear distance/length in metres; proxy meaning is limited by the introducing stage. Consumers and exact calculations are the functions that reference this column above. |
| `source_portal` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_provider` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_standard_model` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_validity_date_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `subtype_code_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `text_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `type_code_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |

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

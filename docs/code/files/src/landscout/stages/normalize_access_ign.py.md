# `src/landscout/stages/normalize_access_ign.py`

## File identity

- Repository path: `src/landscout/stages/normalize_access_ign.py`
- File type: Python source
- Primary responsibility: Source-completely normalizes IGN road segments and raw access attributes without interpreting suitability.
- Layer / domain: `stage` / `road`
- Public or internal role: Contains an explicit module/package export surface; helpers prefixed with `_` remain internal unless re-exported elsewhere.
- Source SHA256: `7f5132849965a01ce4e6826044f2e879dd3a4c7614ae8f5cc8e2d0fed080cfa3`

## 1. Purpose

Source-completely normalizes IGN road segments and raw access attributes without interpreting suitability.

## 2. Position in LandScout architecture

This file is a `stage` artifact in the `road` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from __future__ import annotations` — required by the implementation paths and symbols documented below.
- `import re` — required by the implementation paths and symbols documented below.
- `import unicodedata` — required by the implementation paths and symbols documented below.
- `from dataclasses import dataclass` — required by the implementation paths and symbols documented below.
- `from datetime import date, datetime` — required by the implementation paths and symbols documented below.

### Third-party

- `import geopandas as gpd` — required by the implementation paths and symbols documented below.
- `import pandas as pd` — required by the implementation paths and symbols documented below.
- `from pydantic import HttpUrl, TypeAdapter, ValidationError` — required by the implementation paths and symbols documented below.
- `from pyproj import CRS` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout.sources.ign_bdtopo_fr import ( DepartmentCode, EditionString, IgnBdTopoDownload, IgnBdTopoExtraction, IgnBdTopoLayerSummary, IgnBdTopoRoadData, IgnBdTopoSourceConfig, _revalidate_ign_bdtopo_road_data, _validate_layer_summary_contract, )` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `_SOURCE_PROVIDER` | `"IGN"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_SOURCE_PRODUCT` | `"BD_TOPO"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_SPATIAL_ROLE` | `"PROXY_GEOMETRY"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_ROAD_FEATURE_TYPE` | `"ROAD_SEGMENT"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_OUTPUT_COLUMNS` | `( "road_feature_id", "road_feature_type", "source_provider", "source_product", "source_layer", "source_feature_id", "source_department_code", "source_edition", "source_product_version", "source_download_timestamp", "source_archive_sha256", "source_url", "nature_raw", "importance_raw", "fictitious_raw", "position_relative_to_ground_raw", "asset_status_raw", "lane_count_raw", "carriageway_width_raw", "private_raw", "traffic_direction_raw", "urban_raw", "mean_light_vehicle_speed_raw", "light_vehicle_access_raw", "closure_period_raw", "restriction_nature_raw", "restriction_height_raw", "restriction_total_weight_raw", "restriction_axle_weight_raw", "restriction_width_raw", "restriction_length_raw", "dangerous_goods_forbidden_raw", "administrative_classification_raw", "manager_raw", "source_name_raw", "source_identifiers_raw", "source_created_at", "source_modified_at", "source_confirmed_at", "planimetric_acquisition_method", "planimetric_precision_raw", "spatial_role", "geometry_status", "geometry", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_RAW_FIELD_MAPPING` | `( ("nature", "nature_raw"), ("importance", "importance_raw"), ("fictif", "fictitious_raw"), ("position_par_rapport_au_sol", "position_relative_to_ground_raw"), ("etat_de_l_objet", "asset_status_raw"), ("nombre_de_voies", "lane_count_raw"), ("largeur_de_chaussee", "carriageway_width_raw"), ("prive", "private_raw"), ("sens_de_circulation", "traffic_direction_raw"), ("urbain", "urban_raw"), ("vitesse_moyenne_vl", "mean_light_vehicle_speed_raw"), ("acces_vehicule_leger", "light_vehicle_access_raw"), ("periode_de_fermeture", "closure_period_raw"), ("nature_de_la_restriction", "restriction_nature_raw"), ("restriction_de_hauteur", "restriction_height_raw"), ("restriction_de_poids_total", "restriction_total_weight_raw"), ("restriction_de_poids_par_essieu", "restriction_axle_weight_raw"), ("restriction_de_largeur", "restriction_width_raw"), ("restriction_de_longueur", "restriction_length_raw"), ("matieres_dangereuses_interdites", "dangerous_goods_forbidden_raw"), ("cpx_classement_administratif", "administrative_classification_raw"), ("cpx_gestionnaire", "manager_raw"), ("sources", "source_name_raw"), ("identifiants_sources", "source_identifiers_raw"), ("date_creation", "source_created_at"), ("date_modification", "source_modified_at"), ("date_de_confirmation", "source_confirmed_at"), ("methode_d_acquisition_planimetrique", "planimetric_acquisition_method"), ("precision_planimetrique", "planimetric_precision_raw"), )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_REQUIRED_SOURCE_FIELDS` | `frozenset( {"cleabs", "geometry", *(source for source, _ in _RAW_FIELD_MAPPING)} )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_ROAD_GEOMETRY_TYPES` | `frozenset({"LineString", "MultiLineString"})` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_DEPARTMENT_CODE_VALIDATOR` | `TypeAdapter(DepartmentCode)` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_EDITION_VALIDATOR` | `TypeAdapter(EditionString)` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_HTTP_URL_VALIDATOR` | `TypeAdapter(HttpUrl)` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_SHA256_PATTERN` | `re.compile(r"^[0-9a-f]{64}$")` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_IGN_PROVIDER_IDENTITIES` | `frozenset( { "ign", "institut national de l information geographique et forestiere", "institut national de l information geographique et forestiere ign", } )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

### `IgnRoadNormalizationError`

**Purpose:** Raised when factual IGN road data cannot be normalized safely.

**Inheritance:** `ValueError`.

**Model form and mutability:** class inheriting from `ValueError`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

### `_IgnRoadSourceContext`

**Purpose:** Groups the `IgnRoadSourceContext` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `source_layer` | `str` | `required` | Source lineage or source-bound object whose exact identity is checked before downstream use. |
| `department_code` | `str` | `required` | Exact configured or source code whose vocabulary/format is enforced by the owning validator. |
| `edition` | `str` | `required` | `str` state used by `src/landscout/stages/normalize_access_ign.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `product_version` | `str | None` | `required` | `str | None` state used by `src/landscout/stages/normalize_access_ign.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `download_timestamp` | `str` | `required` | Offset-aware source/download timestamp string preserved as lineage and validated by the owning model. |
| `archive_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `source_url` | `str` | `required` | Exact source or evidence URL; host/path/HTTPS restrictions are enforced by configuration or source validators. |

**Validators and methods:**

- None.

### `NormalizedIgnRoadData`

**Purpose:** Stable factual IGN road catalog with no access-policy interpretation.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `road_segments` | `gpd.GeoDataFrame` | `required` | `gpd.GeoDataFrame` state used by `src/landscout/stages/normalize_access_ign.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

## 6. Functions and methods

### `_validated_lambert93`

**Signature**

```python
def _validated_lambert93(crs_value: object, label: str) -> CRS:
```

**Purpose**

Validates and returns canonical lambert93 according to the exact implementation and guards in this file.

**Inputs**

- `crs_value` (`object`; required) — coordinate reference system identity. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `CRS`. Observed return expression(s): `source_crs`.

**Algorithm**

1. Checks `crs_value is None`. When true: Raises `IgnRoadNormalizationError(f'{label} CRS is required')`.
2. Runs guarded operation: Computes `source_crs` from `CRS.from_user_input(crs_value)`. Handles `Exception`.
3. Computes `expected_crs` from `CRS.from_epsg(2154)`.
4. Checks `not source_crs.is_projected or not source_crs.equals(expected_crs)`. When true: Raises `IgnRoadNormalizationError(f'{label} must use EPSG:2154')`.
5. Returns `source_crs`.

**Validation and invariants**

- Rejects or diverts the path when `crs_value is None` is true.
- Rejects or diverts the path when `not source_crs.is_projected or not source_crs.equals(expected_crs)` is true.

**Exceptions**

- Explicitly raises: `IgnRoadNormalizationError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `CRS.from_epsg`, `CRS.from_user_input`, `IgnRoadNormalizationError`, `source_crs.equals`.

**Known repository callers**

- `src/landscout/stages/normalize_access_ign.py` — `_validate_layer_summary`
- `src/landscout/stages/normalize_access_ign.py` — `_validate_source_bundle`
- `src/landscout/stages/normalize_access_ign.py` — `_validate_source_frame`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_required_exact_string`

**Signature**

```python
def _required_exact_string(value: object, label: str) -> str:
```

**Purpose**

Implements required exact string according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `value`.

**Algorithm**

1. Checks `not isinstance(value, str) or not value.strip()`. When true: Raises `IgnRoadNormalizationError(f'IGN road {label} must be a string')`.
2. Checks `value != value.strip()`. When true: Raises `IgnRoadNormalizationError(f'IGN road {label} must not contain edge whitespace')`.
3. Returns `value`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(value, str) or not value.strip()` is true.
- Rejects or diverts the path when `value != value.strip()` is true.

**Exceptions**

- Explicitly raises: `IgnRoadNormalizationError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `IgnRoadNormalizationError`, `isinstance`, `value.strip`.

**Known repository callers**

- `src/landscout/stages/normalize_access_ign.py` — `_validate_layer_summary`
- `src/landscout/stages/normalize_access_ign.py` — `_validate_source_context`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_validate_source_context`

**Signature**

```python
def _validate_source_context(context: _IgnRoadSourceContext) -> None:
```

**Purpose**

Validates and rejects malformed source context according to the exact implementation and guards in this file.

**Inputs**

- `context` (`_IgnRoadSourceContext`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Calls `_required_exact_string(context.source_layer, 'source_layer')` for its validation or side effect.
2. Computes `department_code` from `_required_exact_string(context.department_code, 'department_code')`.
3. Computes `edition` from `_required_exact_string(context.edition, 'edition')`.
4. Computes `timestamp_raw` from `_required_exact_string(context.download_timestamp, 'download_timestamp')`.
5. Computes `archive_sha256` from `_required_exact_string(context.archive_sha256, 'archive_sha256')`.
6. Computes `source_url` from `_required_exact_string(context.source_url, 'source_url')`.
7. Runs guarded operation: Computes `validated_department` from `_DEPARTMENT_CODE_VALIDATOR.validate_python(department_code)`. Handles `ValidationError`.
8. Checks `validated_department != department_code`. When true: Raises `IgnRoadNormalizationError('IGN road department_code must not be rewritten')`.
9. Runs guarded operation: Computes `validated_edition` from `_EDITION_VALIDATOR.validate_python(edition)`. Calls `date.fromisoformat(validated_edition)` for its validation or side effect. Handles `(ValidationError, ValueError)`.
10. Checks `validated_edition != edition`. When true: Raises `IgnRoadNormalizationError('IGN road edition must not be rewritten')`.
11. Runs guarded operation: Computes `timestamp` from `datetime.fromisoformat(timestamp_raw)`. Handles `ValueError`.
12. Checks `timestamp.tzinfo is None or timestamp.utcoffset() is None`. When true: Raises `IgnRoadNormalizationError('IGN road download_timestamp must be timezone-aware')`.
13. Checks `_SHA256_PATTERN.fullmatch(archive_sha256) is None`. When true: Raises `IgnRoadNormalizationError('IGN road archive_sha256 must contain 64 hexadecimal characters')`.
14. Runs guarded operation: Calls `_HTTP_URL_VALIDATOR.validate_python(source_url)` for its validation or side effect. Handles `ValidationError`.
15. Checks `context.product_version is not None`. When true: Calls `_required_exact_string(context.product_version, 'product_version')` for its validation or side effect.

**Validation and invariants**

- Rejects or diverts the path when `validated_department != department_code` is true.
- Rejects or diverts the path when `validated_edition != edition` is true.
- Rejects or diverts the path when `timestamp.tzinfo is None or timestamp.utcoffset() is None` is true.
- Rejects or diverts the path when `_SHA256_PATTERN.fullmatch(archive_sha256) is None` is true.

**Exceptions**

- Explicitly raises: `IgnRoadNormalizationError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `IgnRoadNormalizationError`, `_DEPARTMENT_CODE_VALIDATOR.validate_python`, `_EDITION_VALIDATOR.validate_python`, `_HTTP_URL_VALIDATOR.validate_python`, `_SHA256_PATTERN.fullmatch`, `_required_exact_string`, `date.fromisoformat`, `datetime.fromisoformat`, `timestamp.utcoffset`.

**Known repository callers**

- `src/landscout/stages/normalize_access_ign.py` — `_normalize_road_frame`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

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

- Declared return type: `str`. Observed return expression(s): `' '.join(re.findall('[a-z0-9]+', without_accents))`.

**Algorithm**

1. Checks `not isinstance(value, str) or not value.strip()`. When true: Raises `IgnRoadNormalizationError(f'IGN archive {label} must be a string')`.
2. Computes `decomposed` from `unicodedata.normalize('NFKD', value.casefold())`.
3. Computes `without_accents` from `''.join((character for character in decomposed if not unicodedata.combining(character)))`.
4. Returns `' '.join(re.findall('[a-z0-9]+', without_accents))`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(value, str) or not value.strip()` is true.

**Exceptions**

- Explicitly raises: `IgnRoadNormalizationError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `' '.join`, `''.join`, `IgnRoadNormalizationError`, `isinstance`, `re.findall`, `unicodedata.combining`, `unicodedata.normalize`, `value.casefold`, `value.strip`.

**Known repository callers**

- `src/landscout/stages/normalize_access_ign.py` — `_validate_source_bundle`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_geometry_summary`

**Signature**

```python
def _geometry_summary(
    frame: gpd.GeoDataFrame,
) -> tuple[int, int, int, tuple[str, ...]]:
```

**Purpose**

Implements geometry summary according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[int, int, int, tuple[str, ...]]`. Observed return expression(s): `(int(null_mask.sum()), int(empty_mask.sum()), int(invalid_mask.sum()), geometry_types)`.

**Algorithm**

1. Computes `geometry` from `frame.geometry`.
2. Computes `null_mask` from `geometry.isna()`.
3. Computes `empty_mask` from `~null_mask & geometry.is_empty`.
4. Computes `invalid_mask` from `~null_mask & ~geometry.is_empty & ~geometry.is_valid`.
5. Computes `geometry_types` from `tuple(sorted((str(value) for value in geometry[~null_mask].geom_type.dropna().unique())))`.
6. Returns `(int(null_mask.sum()), int(empty_mask.sum()), int(invalid_mask.sum()), geometry_types)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `empty_mask.sum`, `geometry.isna`, `geometry[~null_mask].geom_type.dropna`, `geometry[~null_mask].geom_type.dropna().unique`, `int`, `invalid_mask.sum`, `null_mask.sum`, `sorted`, `str`, `tuple`.

**Known repository callers**

- `src/landscout/stages/normalize_access_ign.py` — `_validate_layer_summary`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_validate_layer_summary`

**Signature**

```python
def _validate_layer_summary(
    frame: gpd.GeoDataFrame,
    summary: IgnBdTopoLayerSummary,
    all_layer_names: tuple[str, ...],
) -> None:
```

**Purpose**

Validates and rejects malformed layer summary according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `summary` (`IgnBdTopoLayerSummary`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `all_layer_names` (`tuple[str, ...]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Runs guarded operation: Calls `_validate_layer_summary_contract(summary)` for its validation or side effect. Handles `Exception`.
2. Checks `summary.logical_name != 'road_segments'`. When true: Raises `IgnRoadNormalizationError('IGN road summary has the wrong logical name')`.
3. Computes `source_layer` from `_required_exact_string(summary.source_layer_name, 'summary physical layer')`.
4. Checks `source_layer not in all_layer_names`. When true: Raises `IgnRoadNormalizationError('IGN road summary physical layer is absent from the extraction layer inventory')`.
5. Checks `summary.feature_count != len(frame)`. When true: Raises `IgnRoadNormalizationError('IGN road summary row count does not match the source frame')`.
6. Computes `observed_columns` from `tuple((str(column) for column in frame.columns))`.
7. Computes `observed_dtypes` from `tuple(((str(column), str(dtype)) for column, dtype in frame.dtypes.items()))`.
8. Checks `summary.columns != observed_columns or summary.dtypes != observed_dtypes`. When true: Raises `IgnRoadNormalizationError('IGN road summary schema columns or dtypes do not match the source frame')`.
9. Checks `frame.active_geometry_name != 'geometry'`. When true: Raises `IgnRoadNormalizationError('IGN road source requires an active geometry column')`.
10. Computes `frame_crs` from `_validated_lambert93(frame.crs, 'IGN road source')`.
11. Computes `summary_crs` from `_validated_lambert93(summary.crs, 'IGN road summary')`.
12. Checks `not frame_crs.equals(summary_crs)`. When true: Raises `IgnRoadNormalizationError('IGN road summary CRS does not match the source frame')`.
13. Computes `expected_geometry` from `(summary.null_geometry_count, summary.empty_geometry_count, summary.invalid_geometry_count, summary.geometry_types)`.
14. Checks `_geometry_summary(frame) != expected_geometry`. When true: Raises `IgnRoadNormalizationError('IGN road geometry summary does not match the source frame')`.

**Validation and invariants**

- Rejects or diverts the path when `summary.logical_name != 'road_segments'` is true.
- Rejects or diverts the path when `source_layer not in all_layer_names` is true.
- Rejects or diverts the path when `summary.feature_count != len(frame)` is true.
- Rejects or diverts the path when `summary.columns != observed_columns or summary.dtypes != observed_dtypes` is true.
- Rejects or diverts the path when `frame.active_geometry_name != 'geometry'` is true.
- Rejects or diverts the path when `not frame_crs.equals(summary_crs)` is true.
- Rejects or diverts the path when `_geometry_summary(frame) != expected_geometry` is true.

**Exceptions**

- Explicitly raises: `IgnRoadNormalizationError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `IgnRoadNormalizationError`, `_geometry_summary`, `_required_exact_string`, `_validate_layer_summary_contract`, `_validated_lambert93`, `frame.dtypes.items`, `frame_crs.equals`, `len`, `str`, `tuple`.

**Known repository callers**

- `src/landscout/stages/normalize_access_ign.py` — `_validate_source_bundle`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_validate_source_bundle`

**Signature**

```python
def _validate_source_bundle(source: IgnBdTopoRoadData) -> _IgnRoadSourceContext:
```

**Purpose**

Validates and rejects malformed source bundle according to the exact implementation and guards in this file.

**Inputs**

- `source` (`IgnBdTopoRoadData`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `_IgnRoadSourceContext`. Observed return expression(s): `_IgnRoadSourceContext(source_layer=source.road_segments_summary.source_layer_name, department_code=archive.department_code, edition=archive.edition, product_version=archive.product_version, download_timestamp=archive.download_timestamp, archive_sha256=archive.sha256, source_url=archive.source_url)`.

**Algorithm**

1. Checks `type(source.extraction) is not IgnBdTopoExtraction`. When true: Raises `IgnRoadNormalizationError('IGN road extraction type is invalid')`.
2. Checks `type(source.extraction.archive) is not IgnBdTopoDownload`. When true: Raises `IgnRoadNormalizationError('IGN road archive type is invalid')`.
3. Checks `type(source.road_segments_summary) is not IgnBdTopoLayerSummary`. When true: Raises `IgnRoadNormalizationError('IGN road summary type is invalid')`.
4. Computes `archive` from `source.extraction.archive`.
5. Computes `provider` from `_normalized_identity(archive.provider, 'provider')`.
6. Computes `product` from `_normalized_identity(archive.product, 'product')`.
7. Checks `provider not in _IGN_PROVIDER_IDENTITIES`. When true: Raises `IgnRoadNormalizationError('IGN archive provider is incompatible with the IGN road normalizer')`.
8. Checks `product.replace(' ', '') != 'bdtopo'`. When true: Raises `IgnRoadNormalizationError('IGN archive product is incompatible with the BD TOPO road normalizer')`.
9. Calls `_validated_lambert93(archive.projection, 'IGN archive projection')` for its validation or side effect.
10. Computes `roles` from `(archive.spatial_role, source.extraction.spatial_role, source.road_segments_summary.spatial_role)`.
11. Checks `any((role != _SPATIAL_ROLE for role in roles))`. When true: Raises `IgnRoadNormalizationError('IGN road source spatial roles must all be PROXY_GEOMETRY')`.
12. Computes `layer_names` from `source.extraction.all_layer_names`.
13. Checks `type(layer_names) is not tuple or not layer_names or any((not isinstance(name, str) or not name or name != name.strip() for name in layer_names)) or (len(set(layer_names)) != len(layer_names))`. When true: Raises `IgnRoadNormalizationError('IGN road layer inventory must be a unique non-empty tuple')`.
14. Computes `selected_layers` from `(source.extraction.electric_lines_layer, source.extraction.transformation_posts_layer)`.
15. Checks `any((layer not in layer_names for layer in selected_layers))`. When true: Raises `IgnRoadNormalizationError('IGN road extraction selected layer is absent from the layer inventory')`.
16. Checks `selected_layers[0] == selected_layers[1]`. When true: Raises `IgnRoadNormalizationError('IGN electricity roles must use distinct layers, not the same layer')`.
17. Computes `road_layer` from `source.road_segments_summary.source_layer_name`.
18. Checks `road_layer in selected_layers`. When true: Raises `IgnRoadNormalizationError('IGN road and electricity roles must use distinct layers, not the same layer')`.
19. Checks `not isinstance(source.road_segments, gpd.GeoDataFrame)`. When true: Raises `IgnRoadNormalizationError('IGN road_segments must be a GeoDataFrame with an active geometry column')`.
20. Calls `_validate_source_frame(source.road_segments)` for its validation or side effect.
21. Calls `_validate_layer_summary(source.road_segments, source.road_segments_summary, source.extraction.all_layer_names)` for its validation or side effect.
22. Returns `_IgnRoadSourceContext(source_layer=source.road_segments_summary.source_layer_name, department_code=archive.department_code, edition=archive.edition, product_version=archive.product_version, download_timestamp=archive.download_timestamp, archive_sha256=archive.sha256, source_url=archive.source_url)`.

**Validation and invariants**

- Rejects or diverts the path when `type(source.extraction) is not IgnBdTopoExtraction` is true.
- Rejects or diverts the path when `type(source.extraction.archive) is not IgnBdTopoDownload` is true.
- Rejects or diverts the path when `type(source.road_segments_summary) is not IgnBdTopoLayerSummary` is true.
- Rejects or diverts the path when `provider not in _IGN_PROVIDER_IDENTITIES` is true.
- Rejects or diverts the path when `product.replace(' ', '') != 'bdtopo'` is true.
- Rejects or diverts the path when `any((role != _SPATIAL_ROLE for role in roles))` is true.
- Rejects or diverts the path when `type(layer_names) is not tuple or not layer_names or any((not isinstance(name, str) or not name or name != name.strip() for name in layer_names)) or (len(set(layer_names)) != len(layer_names))` is true.
- Rejects or diverts the path when `any((layer not in layer_names for layer in selected_layers))` is true.
- Rejects or diverts the path when `selected_layers[0] == selected_layers[1]` is true.
- Rejects or diverts the path when `road_layer in selected_layers` is true.
- Rejects or diverts the path when `not isinstance(source.road_segments, gpd.GeoDataFrame)` is true.

**Exceptions**

- Explicitly raises: `IgnRoadNormalizationError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `product.replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `IgnRoadNormalizationError`, `_IgnRoadSourceContext`, `_normalized_identity`, `_validate_layer_summary`, `_validate_source_frame`, `_validated_lambert93`, `any`, `isinstance`, `len`, `name.strip`, `product.replace`, `set`, `type`.

**Known repository callers**

- `src/landscout/stages/normalize_access_ign.py` — `_normalize_ign_roads`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_validate_identifiers`

**Signature**

```python
def _validate_identifiers(frame: gpd.GeoDataFrame) -> None:
```

**Purpose**

Validates and rejects malformed identifiers according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `identifiers` from `frame['cleabs']`.
2. Checks `identifiers.isna().any()`. When true: Raises `IgnRoadNormalizationError('IGN road cleabs values must not be null')`.
3. Computes `values` from `identifiers.tolist()`.
4. Checks `any((not isinstance(identifier, str) for identifier in values))`. When true: Raises `IgnRoadNormalizationError('IGN road cleabs values must be strings')`.
5. Checks `any((not identifier.strip() for identifier in values))`. When true: Raises `IgnRoadNormalizationError('IGN road cleabs values must not be empty')`.
6. Checks `any((identifier != identifier.strip() for identifier in values))`. When true: Raises `IgnRoadNormalizationError('IGN road cleabs values must not contain edge whitespace')`.
7. Checks `any((':' in identifier for identifier in values))`. When true: Raises `IgnRoadNormalizationError("IGN road cleabs values must not contain ':'")`.
8. Checks `any((unicodedata.category(character) == 'Cc' for identifier in values for character in identifier))`. When true: Raises `IgnRoadNormalizationError('IGN road cleabs values must not contain control characters')`.
9. Checks `identifiers.duplicated().any()`. When true: Raises `IgnRoadNormalizationError('IGN road cleabs values must be unique')`.

**Validation and invariants**

- Rejects or diverts the path when `identifiers.isna().any()` is true.
- Rejects or diverts the path when `any((not isinstance(identifier, str) for identifier in values))` is true.
- Rejects or diverts the path when `any((not identifier.strip() for identifier in values))` is true.
- Rejects or diverts the path when `any((identifier != identifier.strip() for identifier in values))` is true.
- Rejects or diverts the path when `any((':' in identifier for identifier in values))` is true.
- Rejects or diverts the path when `any((unicodedata.category(character) == 'Cc' for identifier in values for character in identifier))` is true.
- Rejects or diverts the path when `identifiers.duplicated().any()` is true.

**Exceptions**

- Explicitly raises: `IgnRoadNormalizationError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `IgnRoadNormalizationError`, `any`, `identifier.strip`, `identifiers.duplicated`, `identifiers.duplicated().any`, `identifiers.isna`, `identifiers.isna().any`, `identifiers.tolist`, `isinstance`, `unicodedata.category`.

**Known repository callers**

- `src/landscout/stages/normalize_access_ign.py` — `_validate_source_frame`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_validate_source_frame`

**Signature**

```python
def _validate_source_frame(frame: gpd.GeoDataFrame) -> None:
```

**Purpose**

Validates and rejects malformed source frame according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `frame.columns.duplicated().any()`. When true: Raises `IgnRoadNormalizationError('IGN road source columns must not contain duplicates')`.
2. Computes `missing` from `_REQUIRED_SOURCE_FIELDS - set(frame.columns)`.
3. Checks `missing`. When true: Computes `formatted` from `', '.join(sorted(missing))`. Raises `IgnRoadNormalizationError(f'Missing required IGN road source columns: {formatted}')`.
4. Checks `frame.active_geometry_name != 'geometry'`. When true: Raises `IgnRoadNormalizationError('IGN road source requires an active geometry column')`.
5. Calls `_validated_lambert93(frame.crs, 'IGN road source')` for its validation or side effect.
6. Calls `_validate_identifiers(frame)` for its validation or side effect.

**Validation and invariants**

- Rejects or diverts the path when `frame.columns.duplicated().any()` is true.
- Rejects or diverts the path when `missing` is true.
- Rejects or diverts the path when `frame.active_geometry_name != 'geometry'` is true.

**Exceptions**

- Explicitly raises: `IgnRoadNormalizationError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `', '.join`, `IgnRoadNormalizationError`, `_validate_identifiers`, `_validated_lambert93`, `frame.columns.duplicated`, `frame.columns.duplicated().any`, `set`, `sorted`.

**Known repository callers**

- `src/landscout/stages/normalize_access_ign.py` — `_normalize_road_frame`
- `src/landscout/stages/normalize_access_ign.py` — `_validate_source_bundle`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_geometry_status`

**Signature**

```python
def _geometry_status(geometry: gpd.GeoSeries) -> pd.Series:
```

**Purpose**

Implements geometry status according to the exact implementation and guards in this file.

**Inputs**

- `geometry` (`gpd.GeoSeries`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.Series`. Observed return expression(s): `status`.

**Algorithm**

1. Computes `status` from `pd.Series('VALID', index=geometry.index, dtype='object')`.
2. Computes `null_mask` from `geometry.isna()`.
3. Computes `empty_mask` from `~null_mask & geometry.is_empty`.
4. Computes `invalid_mask` from `~null_mask & ~geometry.is_empty & ~geometry.is_valid`.
5. Computes `status.loc[null_mask]` from `'NULL'`.
6. Computes `status.loc[empty_mask]` from `'EMPTY'`.
7. Computes `status.loc[invalid_mask]` from `'INVALID'`.
8. Returns `status`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `geometry.isna`, `pd.Series`.

**Known repository callers**

- `src/landscout/stages/normalize_access_ign.py` — `_normalize_road_frame`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_normalize_road_frame`

**Signature**

```python
def _normalize_road_frame(
    frame: gpd.GeoDataFrame,
    context: _IgnRoadSourceContext,
) -> gpd.GeoDataFrame:
```

**Purpose**

Normalizes road frame according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `context` (`_IgnRoadSourceContext`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `normalized`.

**Algorithm**

1. Calls `_validate_source_context(context)` for its validation or side effect.
2. Calls `_validate_source_frame(frame)` for its validation or side effect.
3. Computes `working` from `frame.reset_index(drop=True).copy()`.
4. Computes `status` from `_geometry_status(working.geometry)`.
5. Computes `valid_types` from `working.loc[status == 'VALID', 'geometry'].geom_type`.
6. Computes `unsupported` from `sorted(set(valid_types.dropna()) - _ROAD_GEOMETRY_TYPES)`.
7. Checks `unsupported`. When true: Raises `IgnRoadNormalizationError('IGN road source has unsupported VALID geometry types: ' + ', '.join(unsupported))`.
8. Computes `source_ids` from `working['cleabs'].copy()`.
9. Computes `output` from `pd.DataFrame(index=working.index.copy())`.
10. Computes `output['road_feature_id']` from `source_ids.map(lambda identifier: f'IGN_BDTOPO:{_ROAD_FEATURE_TYPE}:{identifier}')`.
11. Computes `output['road_feature_type']` from `_ROAD_FEATURE_TYPE`.
12. Computes `output['source_provider']` from `_SOURCE_PROVIDER`.
13. Computes `output['source_product']` from `_SOURCE_PRODUCT`.
14. Computes `output['source_layer']` from `context.source_layer`.
15. Computes `output['source_feature_id']` from `source_ids`.
16. Computes `output['source_department_code']` from `context.department_code`.
17. Computes `output['source_edition']` from `context.edition`.
18. Computes `output['source_product_version']` from `context.product_version`.
19. Computes `output['source_download_timestamp']` from `context.download_timestamp`.
20. Computes `output['source_archive_sha256']` from `context.archive_sha256`.
21. Computes `output['source_url']` from `context.source_url`.
22. Iterates `(source_column, output_column)` over `_RAW_FIELD_MAPPING`. For each value: Computes `output[output_column]` from `working[source_column].copy()`.
23. Computes `output['spatial_role']` from `_SPATIAL_ROLE`.
24. Computes `output['geometry_status']` from `status`.
25. Computes `output['geometry']` from `working.geometry.copy()`.
26. Computes `normalized` from `gpd.GeoDataFrame(output.loc[:, list(_OUTPUT_COLUMNS)], geometry='geometry', crs=working.crs)`.
27. Checks `len(normalized) != len(frame)`. When true: Raises `IgnRoadNormalizationError('IGN road normalization changed the row count')`.
28. Checks `not isinstance(normalized.index, pd.RangeIndex)`. When true: Raises `IgnRoadNormalizationError('IGN normalized road output must use a RangeIndex')`.
29. Checks `normalized['road_feature_id'].isna().any() or normalized['road_feature_id'].duplicated().any()`. When true: Raises `IgnRoadNormalizationError('Normalized IGN road_feature_id values must be non-null and unique')`.
30. Returns `normalized`.

**Validation and invariants**

- Rejects or diverts the path when `unsupported` is true.
- Rejects or diverts the path when `len(normalized) != len(frame)` is true.
- Rejects or diverts the path when `not isinstance(normalized.index, pd.RangeIndex)` is true.
- Rejects or diverts the path when `normalized['road_feature_id'].isna().any() or normalized['road_feature_id'].duplicated().any()` is true.

**Exceptions**

- Explicitly raises: `IgnRoadNormalizationError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `frame.reset_index(drop=True).copy`, `working.geometry.copy`, `working.index.copy`, `working['cleabs'].copy`, `working[source_column].copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `', '.join`, `IgnRoadNormalizationError`, `_geometry_status`, `_validate_source_context`, `_validate_source_frame`, `frame.reset_index`, `frame.reset_index(drop=True).copy`, `gpd.GeoDataFrame`, `isinstance`, `len`, `list`, `normalized['road_feature_id'].duplicated`, `normalized['road_feature_id'].duplicated().any`, `normalized['road_feature_id'].isna`, `normalized['road_feature_id'].isna().any`, `pd.DataFrame`, `set`, `sorted`, `source_ids.map`, `valid_types.dropna`, `working.geometry.copy`, `working.index.copy`, `working['cleabs'].copy`, `working[source_column].copy`.

**Known repository callers**

- `src/landscout/stages/normalize_access_ign.py` — `_normalize_ign_roads`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_normalize_ign_roads`

**Signature**

```python
def _normalize_ign_roads(
    source: IgnBdTopoRoadData,
    config: IgnBdTopoSourceConfig,
) -> NormalizedIgnRoadData:
```

**Purpose**

Normalizes ign roads according to the exact implementation and guards in this file.

**Inputs**

- `source` (`IgnBdTopoRoadData`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `config` (`IgnBdTopoSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `NormalizedIgnRoadData`. Observed return expression(s): `NormalizedIgnRoadData(road_segments=_normalize_road_frame(source.road_segments, context))`.

**Algorithm**

1. Computes `context` from `_validate_source_bundle(source)`.
2. Calls `_revalidate_ign_bdtopo_road_data(source, config)` for its validation or side effect.
3. Returns `NormalizedIgnRoadData(road_segments=_normalize_road_frame(source.road_segments, context))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `NormalizedIgnRoadData`, `_normalize_road_frame`, `_revalidate_ign_bdtopo_road_data`, `_validate_source_bundle`.

**Known repository callers**

- `src/landscout/stages/normalize_access_ign.py` — `normalize_ign_roads`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `normalize_ign_roads`

**Signature**

```python
def normalize_ign_roads(
    source: IgnBdTopoRoadData,
    config: IgnBdTopoSourceConfig,
) -> NormalizedIgnRoadData:
```

**Purpose**

Validate and project one already-loaded IGN road source without interpretation.

**Inputs**

- `source` (`IgnBdTopoRoadData`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `config` (`IgnBdTopoSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `NormalizedIgnRoadData`. Observed return expression(s): `_normalize_ign_roads(source, config)`.

**Algorithm**

1. Runs guarded operation: Checks `type(source) is not IgnBdTopoRoadData`. When true: Raises `TypeError('source must be an IgnBdTopoRoadData')`. Checks `type(config) is not IgnBdTopoSourceConfig`. When true: Raises `TypeError('config must be an IgnBdTopoSourceConfig')`. Returns `_normalize_ign_roads(source, config)`. Handles `IgnRoadNormalizationError`, `Exception`.

**Validation and invariants**

- Rejects or diverts the path when `type(source) is not IgnBdTopoRoadData` is true.
- Rejects or diverts the path when `type(config) is not IgnBdTopoSourceConfig` is true.

**Exceptions**

- Explicitly raises: `IgnRoadNormalizationError`, `TypeError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `IgnRoadNormalizationError`, `TypeError`, `_normalize_ign_roads`, `type`.

**Known repository callers**

- `src/landscout/stages/apply_road_vehicle_proxy_policy.py` — `_apply_ign_road_vehicle_proxy_policy`
- `tests/unit/test_normalize_access_ign.py` — `test_duplicate_cleabs_is_rejected`
- `tests/unit/test_normalize_access_ign.py` — `test_every_raw_field_preserves_source_values_nulls_and_dtype`
- `tests/unit/test_normalize_access_ign.py` — `test_forged_ordered_summary_schema_is_rejected`
- `tests/unit/test_normalize_access_ign.py` — `test_high_level_rejects_coordinated_road_frame_and_summary_forgery`
- `tests/unit/test_normalize_access_ign.py` — `test_malformed_public_input_has_controlled_error`
- `tests/unit/test_normalize_access_ign.py` — `test_missing_required_source_field_is_rejected`
- `tests/unit/test_normalize_access_ign.py` — `test_normalization_does_not_mutate_input`
- `tests/unit/test_normalize_access_ign.py` — `test_null_empty_and_invalid_geometry_are_preserved_with_status`
- `tests/unit/test_normalize_access_ign.py` — `test_null_or_empty_cleabs_is_rejected`
- `tests/unit/test_normalize_access_ign.py` — `test_raw_access_and_restriction_values_are_copied_without_interpretation`
- `tests/unit/test_normalize_access_ign.py` — `test_road_archive_sha256_requires_canonical_lowercase`
- `tests/unit/test_normalize_access_ign.py` — `test_road_normalization_reproduces_configured_logical_layer`
- `tests/unit/test_normalize_access_ign.py` — `test_road_source_rejects_duplicate_layer_inventory`
- `tests/unit/test_normalize_access_ign.py` — `test_road_source_rejects_physical_role_collision`
- `tests/unit/test_normalize_access_ign.py` — `test_road_summary_requires_strict_structural_types`
- `tests/unit/test_normalize_access_ign.py` — `test_row_count_order_geometry_and_range_index_are_preserved`
- `tests/unit/test_normalize_access_ign.py` — `test_summary_crs_mismatch_is_rejected`
- `tests/unit/test_normalize_access_ign.py` — `test_summary_geometry_facts_mismatch_is_rejected`
- `tests/unit/test_normalize_access_ign.py` — `test_summary_layer_and_logical_name_must_be_exact`
- `tests/unit/test_normalize_access_ign.py` — `test_summary_layer_must_exist_in_extraction_inventory`
- `tests/unit/test_normalize_access_ign.py` — `test_summary_row_count_mismatch_is_rejected`
- `tests/unit/test_normalize_access_ign.py` — `test_unsafe_cleabs_is_rejected`
- `tests/unit/test_normalize_access_ign.py` — `test_valid_linestring_normalization_has_exact_schema_identity_and_lineage`
- `tests/unit/test_normalize_access_ign.py` — `test_valid_multilinestring_is_preserved`
- `tests/unit/test_normalize_access_ign.py` — `test_valid_unsupported_geometry_type_is_rejected`
- `tests/unit/test_normalize_access_ign.py` — `test_wrong_archive_identity_is_rejected`
- `tests/unit/test_normalize_access_ign.py` — `test_wrong_or_missing_road_crs_is_rejected`
- `tests/unit/test_normalize_access_ign.py` — `test_wrong_source_spatial_role_is_rejected`
- `tests/unit/test_normalize_access_ign.py` — `test_z_coordinates_are_preserved_exactly`

**Tests**

- `tests/unit/test_normalize_access_ign.py::test_duplicate_cleabs_is_rejected`
- `tests/unit/test_normalize_access_ign.py::test_every_raw_field_preserves_source_values_nulls_and_dtype`
- `tests/unit/test_normalize_access_ign.py::test_forged_ordered_summary_schema_is_rejected`
- `tests/unit/test_normalize_access_ign.py::test_high_level_rejects_coordinated_road_frame_and_summary_forgery`
- `tests/unit/test_normalize_access_ign.py::test_malformed_public_input_has_controlled_error`
- `tests/unit/test_normalize_access_ign.py::test_missing_required_source_field_is_rejected`
- `tests/unit/test_normalize_access_ign.py::test_normalization_does_not_mutate_input`
- `tests/unit/test_normalize_access_ign.py::test_null_empty_and_invalid_geometry_are_preserved_with_status`
- `tests/unit/test_normalize_access_ign.py::test_null_or_empty_cleabs_is_rejected`
- `tests/unit/test_normalize_access_ign.py::test_raw_access_and_restriction_values_are_copied_without_interpretation`
- `tests/unit/test_normalize_access_ign.py::test_road_archive_sha256_requires_canonical_lowercase`
- `tests/unit/test_normalize_access_ign.py::test_road_normalization_reproduces_configured_logical_layer`
- `tests/unit/test_normalize_access_ign.py::test_road_source_rejects_duplicate_layer_inventory`
- `tests/unit/test_normalize_access_ign.py::test_road_source_rejects_physical_role_collision`
- `tests/unit/test_normalize_access_ign.py::test_road_summary_requires_strict_structural_types`
- `tests/unit/test_normalize_access_ign.py::test_row_count_order_geometry_and_range_index_are_preserved`
- `tests/unit/test_normalize_access_ign.py::test_summary_crs_mismatch_is_rejected`
- `tests/unit/test_normalize_access_ign.py::test_summary_geometry_facts_mismatch_is_rejected`
- `tests/unit/test_normalize_access_ign.py::test_summary_layer_and_logical_name_must_be_exact`
- `tests/unit/test_normalize_access_ign.py::test_summary_layer_must_exist_in_extraction_inventory`
- `tests/unit/test_normalize_access_ign.py::test_summary_row_count_mismatch_is_rejected`
- `tests/unit/test_normalize_access_ign.py::test_unsafe_cleabs_is_rejected`
- `tests/unit/test_normalize_access_ign.py::test_valid_linestring_normalization_has_exact_schema_identity_and_lineage`
- `tests/unit/test_normalize_access_ign.py::test_valid_multilinestring_is_preserved`
- `tests/unit/test_normalize_access_ign.py::test_valid_unsupported_geometry_type_is_rejected`
- `tests/unit/test_normalize_access_ign.py::test_wrong_archive_identity_is_rejected`
- `tests/unit/test_normalize_access_ign.py::test_wrong_or_missing_road_crs_is_rejected`
- `tests/unit/test_normalize_access_ign.py::test_wrong_source_spatial_role_is_rejected`
- `tests/unit/test_normalize_access_ign.py::test_z_coordinates_are_preserved_exactly`

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `administrative_classification_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `asset_status_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `carriageway_width_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `cleabs` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `closure_period_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `dangerous_goods_forbidden_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `fictitious_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `geometry` | Logical dtype: GeoPandas active geometry dtype. Nullability: nullable only where the source-stage geometry-status contract explicitly preserves nulls. | source or preserved spatial geometry; never itself a suitability or legal conclusion. Consumers and exact calculations are the functions that reference this column above. |
| `geometry_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `importance_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `lane_count_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `light_vehicle_access_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `manager_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `mean_light_vehicle_speed_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `nature_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `planimetric_acquisition_method` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `planimetric_precision_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `position_relative_to_ground_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `private_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `restriction_axle_weight_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `restriction_height_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `restriction_length_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `restriction_nature_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `restriction_total_weight_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `restriction_width_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `road_feature_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `road_feature_type` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `source_archive_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `source_confirmed_at` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_created_at` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_department_code` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_download_timestamp` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_edition` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_feature_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `source_identifiers_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `source_layer` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_modified_at` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_name_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `source_product` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_product_version` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_provider` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_url` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `spatial_role` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `traffic_direction_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `urban_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |

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

This file contributes to LandScout's `road` evidence flow as described by its purpose and public symbols. It preserves the distinction among fact, proxy evidence, policy interpretation, diagnostic status, and parcel precheck.

## 15. Explicit non-goals

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

## 16. Tests

Direct name-resolved tests appear under each symbol. Higher-level tests may exercise private helpers through a public source-complete function; companion documents for all test files describe their fixtures, actions, assertions, and boundaries.

## 17. Change impact

Changing this file requires reviewing its static callers, package exports, directly mapped tests, relevant schema/hash/version constants, source locks, persisted artifact contracts, and the corresponding pipeline/cross-cutting documents. Any byte change makes the SHA256 above stale and requires regenerating this companion.

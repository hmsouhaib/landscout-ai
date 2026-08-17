# `src/landscout/stages/filter_parcels.py`

## File identity

- Repository path: `src/landscout/stages/filter_parcels.py`
- File type: Python source
- Primary responsibility: Applies configured factual parcel-area bounds and records explicit keep/reject facts without ranking.
- Layer / domain: `stage` / `cadastre`
- Public or internal role: Module symbols without a package re-export are internal unless imported directly by repository code.
- Source SHA256: `aa2071fc0df4ae843ded9df394df0b9d2f151d84eb5ac6edee1a41c3d6e2f439`

## 1. Purpose

Applies configured factual parcel-area bounds and records explicit keep/reject facts without ranking.

## 2. Position in LandScout architecture

This file is a `stage` artifact in the `cadastre` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from math import isfinite` — required by the implementation paths and symbols documented below.
- `from numbers import Real` — required by the implementation paths and symbols documented below.

### Third-party

- `import geopandas as gpd` — required by the implementation paths and symbols documented below.
- `from pyproj import CRS` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout.common.cadastre_contract import validate_cadastre_geometry_statuses` — required by the implementation paths and symbols documented below.
- `from landscout.config import ParcelConfig, ShapeScreeningConfig` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `AREA_REQUIRED_COLUMNS` | `frozenset( {"parcel_id", "geometry_status", "area_m2", "geometry"} )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `SHAPE_REQUIRED_COLUMNS` | `frozenset( {"parcel_id", "shape_status", "width_m", "length_width_ratio", "geometry"} )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `ALLOWED_SHAPE_STATUSES` | `frozenset({"VALID", "ERROR"})` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

### `ParcelFilterError`

**Purpose:** Raised when normalized parcels cannot be partitioned safely.

**Inheritance:** `ValueError`.

**Model form and mutability:** class inheriting from `ValueError`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

## 6. Functions and methods

### `_validate_spatial_frame`

**Signature**

```python
def _validate_spatial_frame(parcels: object, label: str) -> gpd.GeoDataFrame:
```

**Purpose**

Validates and rejects malformed spatial frame according to the exact implementation and guards in this file.

**Inputs**

- `parcels` (`object`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `parcels`.

**Algorithm**

1. Checks `not isinstance(parcels, gpd.GeoDataFrame)`. When true: Raises `ParcelFilterError(f'{label} input must be a GeoDataFrame')`.
2. Checks `parcels.columns.duplicated().any()`. When true: Raises `ParcelFilterError(f'{label} input columns must be unique')`.
3. Runs guarded operation: Computes `geometry_name` from `parcels.active_geometry_name`. Handles `(AttributeError, ValueError)`.
4. Checks `geometry_name is None or geometry_name not in parcels.columns`. When true: Raises `ParcelFilterError(f'{label} input requires an active geometry column')`.
5. Checks `parcels.crs is None`. When true: Raises `ParcelFilterError(f'{label} input must have a known CRS')`.
6. Runs guarded operation: Calls `CRS.from_user_input(parcels.crs)` for its validation or side effect. Handles `Exception`.
7. Returns `parcels`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(parcels, gpd.GeoDataFrame)` is true.
- Rejects or diverts the path when `parcels.columns.duplicated().any()` is true.
- Rejects or diverts the path when `geometry_name is None or geometry_name not in parcels.columns` is true.
- Rejects or diverts the path when `parcels.crs is None` is true.

**Exceptions**

- Explicitly raises: `ParcelFilterError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `CRS.from_user_input`, `ParcelFilterError`, `isinstance`, `parcels.columns.duplicated`, `parcels.columns.duplicated().any`.

**Known repository callers**

- `src/landscout/stages/filter_parcels.py` — `_validate_shape_filter_input`
- `src/landscout/stages/filter_parcels.py` — `filter_parcels_by_area`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `cadastre` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

### `_missing_columns`

**Signature**

```python
def _missing_columns(
    parcels: object,
    required: frozenset[str],
    label: str,
) -> frozenset[str]:
```

**Purpose**

Implements missing columns according to the exact implementation and guards in this file.

**Inputs**

- `parcels` (`object`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `required` (`frozenset[str]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `frozenset[str]`. Observed return expression(s): `required - set(parcels.columns)`.

**Algorithm**

1. Runs guarded operation: Returns `required - set(parcels.columns)`. Handles `Exception`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `ParcelFilterError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ParcelFilterError`, `set`.

**Known repository callers**

- `src/landscout/stages/filter_parcels.py` — `_validate_shape_filter_input`
- `src/landscout/stages/filter_parcels.py` — `filter_parcels_by_area`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `cadastre` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

### `_validate_exact_parcel_ids`

**Signature**

```python
def _validate_exact_parcel_ids(parcels: gpd.GeoDataFrame) -> None:
```

**Purpose**

Validates and rejects malformed exact parcel ids according to the exact implementation and guards in this file.

**Inputs**

- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `identifiers` from `parcels['parcel_id']`.
2. Checks `identifiers.isna().any()`. When true: Raises `ParcelFilterError('parcel_id values must not be null')`.
3. Checks `any((not isinstance(identifier, str) or not identifier or identifier != identifier.strip() for identifier in identifiers))`. When true: Raises `ParcelFilterError('parcel_id values must be exact non-empty strings')`.
4. Checks `identifiers.duplicated().any()`. When true: Raises `ParcelFilterError('parcel_id values must be unique')`.

**Validation and invariants**

- Rejects or diverts the path when `identifiers.isna().any()` is true.
- Rejects or diverts the path when `any((not isinstance(identifier, str) or not identifier or identifier != identifier.strip() for identifier in identifiers))` is true.
- Rejects or diverts the path when `identifiers.duplicated().any()` is true.

**Exceptions**

- Explicitly raises: `ParcelFilterError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ParcelFilterError`, `any`, `identifier.strip`, `identifiers.duplicated`, `identifiers.duplicated().any`, `identifiers.isna`, `identifiers.isna().any`, `isinstance`.

**Known repository callers**

- `src/landscout/stages/filter_parcels.py` — `_validate_shape_filter_input`
- `src/landscout/stages/filter_parcels.py` — `filter_parcels_by_area`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `cadastre` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

### `_is_strict_finite_number`

**Signature**

```python
def _is_strict_finite_number(value: object) -> bool:
```

**Purpose**

Returns whether `strict finite number` satisfies the exact predicates and branches listed below.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bool`. Observed return expression(s): `isinstance(value, Real) and (not isinstance(value, bool)) and isfinite(float(value))`.

**Algorithm**

1. Returns `isinstance(value, Real) and (not isinstance(value, bool)) and isfinite(float(value))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `float`, `isfinite`, `isinstance`.

**Known repository callers**

- `src/landscout/stages/filter_parcels.py` — `_validate_shape_filter_input`
- `src/landscout/stages/filter_parcels.py` — `filter_parcels_by_area`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `cadastre` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

### `filter_parcels_by_area`

**Signature**

```python
def filter_parcels_by_area(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> tuple[gpd.GeoDataFrame, gpd.GeoDataFrame]:
```

**Purpose**

Filters parcels by area according to the exact implementation and guards in this file.

**Inputs**

- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `area_config` (`ParcelConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[gpd.GeoDataFrame, gpd.GeoDataFrame]`. Observed return expression(s): `(candidates, rejected)`.

**Algorithm**

1. Computes `missing_columns` from `_missing_columns(parcels, AREA_REQUIRED_COLUMNS, 'Area-filter')`.
2. Checks `missing_columns`. When true: Computes `formatted` from `', '.join(sorted(missing_columns))`. Raises `ParcelFilterError(f'Missing required normalized columns: {formatted}')`.
3. Computes `parcels` from `_validate_spatial_frame(parcels, 'Area-filter')`.
4. Calls `_validate_exact_parcel_ids(parcels)` for its validation or side effect.
5. Runs guarded operation: Calls `validate_cadastre_geometry_statuses(parcels['geometry_status'].tolist())` for its validation or side effect. Handles `ValueError`.
6. Computes `valid_geometry` from `parcels['geometry_status'] == 'VALID'`.
7. Checks `any((not _is_strict_finite_number(value) or float(value) <= 0 for value in parcels.loc[valid_geometry, 'area_m2']))`. When true: Raises `ParcelFilterError('area_m2 must be a strict positive finite numeric value when geometry_status is VALID')`.
8. Computes `known_area` from `parcels['area_m2'].notna()`.
9. Computes `within_area_range` from `parcels['area_m2'].between(area_config.min_area_m2, area_config.max_area_m2, inclusive='both')`.
10. Computes `candidate_mask` from `valid_geometry & known_area & within_area_range`.
11. Computes `candidates` from `parcels.loc[candidate_mask].copy()`.
12. Computes `rejected` from `parcels.loc[~candidate_mask].copy()`.
13. Computes `rejected['rejection_reason']` from `'AREA_UNKNOWN'`.
14. Computes `rejected_valid_geometry` from `rejected['geometry_status'] == 'VALID'`.
15. Computes `rejected_known_area` from `rejected['area_m2'].notna()`.
16. Computes `rejected.loc[~rejected_valid_geometry, 'rejection_reason']` from `'INVALID_GEOMETRY'`.
17. Computes `rejected.loc[rejected_valid_geometry & rejected_known_area & (rejected['area_m2'] < area_config.min_area_m2), 'rejection_reason']` from `'AREA_BELOW_MIN'`.
18. Computes `rejected.loc[rejected_valid_geometry & rejected_known_area & (rejected['area_m2'] > area_config.max_area_m2), 'rejection_reason']` from `'AREA_ABOVE_MAX'`.
19. Checks `len(parcels) != len(candidates) + len(rejected)`. When true: Raises `ParcelFilterError('Parcel partition did not preserve every input row')`.
20. Computes `input_ids` from `set(parcels['parcel_id'])`.
21. Computes `candidate_ids` from `set(candidates['parcel_id'])`.
22. Computes `rejected_ids` from `set(rejected['parcel_id'])`.
23. Checks `candidates['parcel_id'].duplicated().any() or rejected['parcel_id'].duplicated().any()`. When true: Raises `ParcelFilterError('Parcel partition contains duplicate parcel IDs')`.
24. Checks `candidate_ids & rejected_ids`. When true: Raises `ParcelFilterError('Candidate and rejected parcel IDs overlap')`.
25. Checks `candidate_ids | rejected_ids != input_ids`. When true: Raises `ParcelFilterError('Parcel partition did not preserve exact parcel IDs')`.
26. Returns `(candidates, rejected)`.

**Validation and invariants**

- Rejects or diverts the path when `missing_columns` is true.
- Rejects or diverts the path when `any((not _is_strict_finite_number(value) or float(value) <= 0 for value in parcels.loc[valid_geometry, 'area_m2']))` is true.
- Rejects or diverts the path when `len(parcels) != len(candidates) + len(rejected)` is true.
- Rejects or diverts the path when `candidates['parcel_id'].duplicated().any() or rejected['parcel_id'].duplicated().any()` is true.
- Rejects or diverts the path when `candidate_ids & rejected_ids` is true.
- Rejects or diverts the path when `candidate_ids | rejected_ids != input_ids` is true.

**Exceptions**

- Explicitly raises: `ParcelFilterError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `parcels.loc[candidate_mask].copy`, `parcels.loc[~candidate_mask].copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `', '.join`, `ParcelFilterError`, `_is_strict_finite_number`, `_missing_columns`, `_validate_exact_parcel_ids`, `_validate_spatial_frame`, `any`, `candidates['parcel_id'].duplicated`, `candidates['parcel_id'].duplicated().any`, `float`, `len`, `parcels.loc[candidate_mask].copy`, `parcels.loc[~candidate_mask].copy`, `parcels['area_m2'].between`, `parcels['area_m2'].notna`, `parcels['geometry_status'].tolist`, `rejected['area_m2'].notna`, `rejected['parcel_id'].duplicated`, `rejected['parcel_id'].duplicated().any`, `set`, `sorted`, `str`, `validate_cadastre_geometry_statuses`.

**Known repository callers**

- `tests/unit/test_filter_parcels.py` — `test_area_filter_rejects_duplicate_columns`
- `tests/unit/test_filter_parcels.py` — `test_area_filter_rejects_malformed_spatial_envelope`
- `tests/unit/test_filter_parcels.py` — `test_area_filter_rejects_noncanonical_geometry_status`
- `tests/unit/test_filter_parcels.py` — `test_area_filter_rejects_plain_dataframe`
- `tests/unit/test_filter_parcels.py` — `test_area_filter_requires_exact_non_empty_parcel_ids`
- `tests/unit/test_filter_parcels.py` — `test_candidate_and_rejected_ids_do_not_overlap`
- `tests/unit/test_filter_parcels.py` — `test_duplicate_parcel_id_fails`
- `tests/unit/test_filter_parcels.py` — `test_exact_parcel_ids_are_preserved`
- `tests/unit/test_filter_parcels.py` — `test_maximum_boundary_is_included`
- `tests/unit/test_filter_parcels.py` — `test_minimum_boundary_is_included`
- `tests/unit/test_filter_parcels.py` — `test_missing_parcel_id_fails`
- `tests/unit/test_filter_parcels.py` — `test_no_parcel_disappears`
- `tests/unit/test_filter_parcels.py` — `test_null_parcel_id_fails`
- `tests/unit/test_filter_parcels.py` — `test_rejected_parcel_has_expected_reason`
- `tests/unit/test_filter_parcels.py` — `test_thresholds_come_from_config`
- `tests/unit/test_filter_parcels.py` — `test_valid_geometry_requires_strict_positive_finite_area`

**Tests**

- `tests/unit/test_filter_parcels.py::test_area_filter_rejects_duplicate_columns`
- `tests/unit/test_filter_parcels.py::test_area_filter_rejects_malformed_spatial_envelope`
- `tests/unit/test_filter_parcels.py::test_area_filter_rejects_noncanonical_geometry_status`
- `tests/unit/test_filter_parcels.py::test_area_filter_rejects_plain_dataframe`
- `tests/unit/test_filter_parcels.py::test_area_filter_requires_exact_non_empty_parcel_ids`
- `tests/unit/test_filter_parcels.py::test_candidate_and_rejected_ids_do_not_overlap`
- `tests/unit/test_filter_parcels.py::test_duplicate_parcel_id_fails`
- `tests/unit/test_filter_parcels.py::test_exact_parcel_ids_are_preserved`
- `tests/unit/test_filter_parcels.py::test_maximum_boundary_is_included`
- `tests/unit/test_filter_parcels.py::test_minimum_boundary_is_included`
- `tests/unit/test_filter_parcels.py::test_missing_parcel_id_fails`
- `tests/unit/test_filter_parcels.py::test_no_parcel_disappears`
- `tests/unit/test_filter_parcels.py::test_null_parcel_id_fails`
- `tests/unit/test_filter_parcels.py::test_rejected_parcel_has_expected_reason`
- `tests/unit/test_filter_parcels.py::test_thresholds_come_from_config`
- `tests/unit/test_filter_parcels.py::test_valid_geometry_requires_strict_positive_finite_area`

**Business interpretation**

This symbol contributes to the `cadastre` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

### `_validate_shape_filter_input`

**Signature**

```python
def _validate_shape_filter_input(parcels: gpd.GeoDataFrame) -> None:
```

**Purpose**

Validates and rejects malformed shape filter input according to the exact implementation and guards in this file.

**Inputs**

- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `missing_columns` from `_missing_columns(parcels, SHAPE_REQUIRED_COLUMNS, 'Shape-filter')`.
2. Checks `missing_columns`. When true: Computes `formatted` from `', '.join(sorted(missing_columns))`. Raises `ParcelFilterError(f'Missing required shape columns: {formatted}')`.
3. Computes `parcels` from `_validate_spatial_frame(parcels, 'Shape-filter')`.
4. Calls `_validate_exact_parcel_ids(parcels)` for its validation or side effect.
5. Computes `statuses` from `parcels['shape_status']`.
6. Computes `unexpected_statuses` from `set(statuses.dropna().unique()) - ALLOWED_SHAPE_STATUSES`.
7. Checks `statuses.isna().any() or unexpected_statuses`. When true: Computes `formatted` from `', '.join(sorted((str(value) for value in unexpected_statuses)))`. Computes `detail` from `formatted or 'null'`. Raises `ParcelFilterError(f'Unexpected shape_status value(s): {detail}')`.
8. Computes `valid_rows` from `statuses == 'VALID'`.
9. Checks `parcels.loc[valid_rows, ['width_m', 'length_width_ratio']].isna().any().any()`. When true: Raises `ParcelFilterError('VALID shape rows must have complete width_m and length_width_ratio metrics')`.
10. Iterates `column` over `('width_m', 'length_width_ratio')`. For each value: Checks `any((not _is_strict_finite_number(value) for value in parcels.loc[valid_rows, column]))`. When true: Raises `ParcelFilterError(f'{column} must be numeric and finite when shape_status is VALID')`.
11. Computes `valid_width` from `parcels.loc[valid_rows, 'width_m']`.
12. Checks `any((float(value) <= 0 for value in valid_width))`. When true: Raises `ParcelFilterError('width_m must be greater than zero when shape_status is VALID')`.
13. Computes `valid_ratio` from `parcels.loc[valid_rows, 'length_width_ratio']`.
14. Checks `any((float(value) < 1 for value in valid_ratio))`. When true: Raises `ParcelFilterError('length_width_ratio must be at least one when shape_status is VALID')`.

**Validation and invariants**

- Rejects or diverts the path when `missing_columns` is true.
- Rejects or diverts the path when `statuses.isna().any() or unexpected_statuses` is true.
- Rejects or diverts the path when `parcels.loc[valid_rows, ['width_m', 'length_width_ratio']].isna().any().any()` is true.
- Rejects or diverts the path when `any((float(value) <= 0 for value in valid_width))` is true.
- Rejects or diverts the path when `any((float(value) < 1 for value in valid_ratio))` is true.
- Rejects or diverts the path when `any((not _is_strict_finite_number(value) for value in parcels.loc[valid_rows, column]))` is true.

**Exceptions**

- Explicitly raises: `ParcelFilterError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `', '.join`, `ParcelFilterError`, `_is_strict_finite_number`, `_missing_columns`, `_validate_exact_parcel_ids`, `_validate_spatial_frame`, `any`, `float`, `parcels.loc[valid_rows, ['width_m', 'length_width_ratio']].isna`, `parcels.loc[valid_rows, ['width_m', 'length_width_ratio']].isna().any`, `parcels.loc[valid_rows, ['width_m', 'length_width_ratio']].isna().any().any`, `set`, `sorted`, `statuses.dropna`, `statuses.dropna().unique`, `statuses.isna`, `statuses.isna().any`, `str`.

**Known repository callers**

- `src/landscout/stages/filter_parcels.py` — `filter_parcels_by_shape`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `cadastre` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

### `_validate_shape_partition`

**Signature**

```python
def _validate_shape_partition(
    parcels: gpd.GeoDataFrame,
    retained: gpd.GeoDataFrame,
    rejected: gpd.GeoDataFrame,
) -> None:
```

**Purpose**

Validates and rejects malformed shape partition according to the exact implementation and guards in this file.

**Inputs**

- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `retained` (`gpd.GeoDataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `rejected` (`gpd.GeoDataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `len(parcels) != len(retained) + len(rejected)`. When true: Raises `ParcelFilterError('Shape partition did not preserve every input row')`.
2. Checks `retained['parcel_id'].duplicated().any() or rejected['parcel_id'].duplicated().any()`. When true: Raises `ParcelFilterError('Shape partition contains duplicate parcel IDs')`.
3. Computes `input_ids` from `set(parcels['parcel_id'])`.
4. Computes `retained_ids` from `set(retained['parcel_id'])`.
5. Computes `rejected_ids` from `set(rejected['parcel_id'])`.
6. Checks `retained_ids & rejected_ids`. When true: Raises `ParcelFilterError('Retained and rejected parcel IDs overlap')`.
7. Checks `retained_ids | rejected_ids != input_ids`. When true: Raises `ParcelFilterError('Shape partition did not preserve exact parcel IDs')`.

**Validation and invariants**

- Rejects or diverts the path when `len(parcels) != len(retained) + len(rejected)` is true.
- Rejects or diverts the path when `retained['parcel_id'].duplicated().any() or rejected['parcel_id'].duplicated().any()` is true.
- Rejects or diverts the path when `retained_ids & rejected_ids` is true.
- Rejects or diverts the path when `retained_ids | rejected_ids != input_ids` is true.

**Exceptions**

- Explicitly raises: `ParcelFilterError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ParcelFilterError`, `len`, `rejected['parcel_id'].duplicated`, `rejected['parcel_id'].duplicated().any`, `retained['parcel_id'].duplicated`, `retained['parcel_id'].duplicated().any`, `set`.

**Known repository callers**

- `src/landscout/stages/filter_parcels.py` — `filter_parcels_by_shape`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `cadastre` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

### `filter_parcels_by_shape`

**Signature**

```python
def filter_parcels_by_shape(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> tuple[gpd.GeoDataFrame, gpd.GeoDataFrame]:
```

**Purpose**

Partition shape-enriched parcels using an explicit screening policy.

**Inputs**

- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `shape_config` (`ShapeScreeningConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[gpd.GeoDataFrame, gpd.GeoDataFrame]`. Observed return expression(s): `(retained, rejected)`.

**Algorithm**

1. Calls `_validate_shape_filter_input(parcels)` for its validation or side effect.
2. Checks `not shape_config.enabled`. When true: Computes `retained` from `parcels.copy()`. Computes `rejected` from `parcels.iloc[0:0].copy()`. Calls `_validate_shape_partition(parcels, retained, rejected)` for its validation or side effect. Executes 1 additional source-ordered statement(s).
3. Computes `min_width_m` from `shape_config.min_width_m`.
4. Computes `max_ratio` from `shape_config.max_length_width_ratio`.
5. Computes `calibration` from `shape_config.calibration`.
6. Checks `min_width_m is None or max_ratio is None or calibration is None`. When true: Raises `ParcelFilterError('Enabled shape screening policy is incomplete')`.
7. Computes `valid_shape` from `parcels['shape_status'] == 'VALID'`.
8. Computes `screening_width` from `parcels['width_m'].where(valid_shape)`.
9. Computes `screening_ratio` from `parcels['length_width_ratio'].where(valid_shape)`.
10. Computes `known_width` from `screening_width.notna()`.
11. Computes `known_ratio` from `screening_ratio.notna()`.
12. Computes `retained_mask` from `valid_shape & known_width & known_ratio & (screening_width >= min_width_m) & (screening_ratio <= max_ratio)`.
13. Computes `retained` from `parcels.loc[retained_mask].copy()`.
14. Computes `rejected` from `parcels.loc[~retained_mask].copy()`.
15. Computes `rejected['shape_rejection_reason']` from `'RATIO_ABOVE_MAX'`.
16. Computes `rejected_valid` from `rejected['shape_status'] == 'VALID'`.
17. Computes `rejected_width` from `rejected['width_m'].where(rejected_valid)`.
18. Computes `rejected.loc[rejected_valid & (rejected_width < min_width_m), 'shape_rejection_reason']` from `'WIDTH_BELOW_MIN'`.
19. Computes `rejected.loc[~rejected_valid, 'shape_rejection_reason']` from `'SHAPE_ERROR'`.
20. Iterates `output` over `(retained, rejected)`. For each value: Computes `output['shape_policy_version']` from `calibration.policy_version`. Computes `output['shape_policy_min_width_m']` from `min_width_m`. Computes `output['shape_policy_max_ratio']` from `max_ratio`.
21. Calls `_validate_shape_partition(parcels, retained, rejected)` for its validation or side effect.
22. Returns `(retained, rejected)`.

**Validation and invariants**

- Rejects or diverts the path when `min_width_m is None or max_ratio is None or calibration is None` is true.

**Exceptions**

- Explicitly raises: `ParcelFilterError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `parcels.copy`, `parcels.iloc[0:0].copy`, `parcels.loc[retained_mask].copy`, `parcels.loc[~retained_mask].copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `ParcelFilterError`, `_validate_shape_filter_input`, `_validate_shape_partition`, `parcels.copy`, `parcels.iloc[0:0].copy`, `parcels.loc[retained_mask].copy`, `parcels.loc[~retained_mask].copy`, `parcels['length_width_ratio'].where`, `parcels['width_m'].where`, `rejected['width_m'].where`, `screening_ratio.notna`, `screening_width.notna`.

**Known repository callers**

- `tests/unit/test_filter_shape.py` — `test_different_configs_change_results_for_same_parcels`
- `tests/unit/test_filter_shape.py` — `test_disabled_policy_is_an_exact_passthrough`
- `tests/unit/test_filter_shape.py` — `test_duplicate_parcel_id_fails`
- `tests/unit/test_filter_shape.py` — `test_enabled_outputs_record_active_policy_metadata`
- `tests/unit/test_filter_shape.py` — `test_enabled_partition_preserves_exact_ids_and_crs`
- `tests/unit/test_filter_shape.py` — `test_exact_width_and_ratio_boundaries_are_retained`
- `tests/unit/test_filter_shape.py` — `test_filter_does_not_mutate_input`
- `tests/unit/test_filter_shape.py` — `test_missing_required_column_fails`
- `tests/unit/test_filter_shape.py` — `test_negative_ratio_cannot_pass_permissive_thresholds`
- `tests/unit/test_filter_shape.py` — `test_non_finite_known_metric_on_valid_row_fails`
- `tests/unit/test_filter_shape.py` — `test_null_parcel_id_fails`
- `tests/unit/test_filter_shape.py` — `test_rejected_parcel_has_expected_primary_reason`
- `tests/unit/test_filter_shape.py` — `test_rejection_reason_precedence_is_deterministic`
- `tests/unit/test_filter_shape.py` — `test_shape_error_precedence_does_not_inspect_metrics`
- `tests/unit/test_filter_shape.py` — `test_shape_filter_rejects_duplicate_columns`
- `tests/unit/test_filter_shape.py` — `test_shape_filter_rejects_plain_dataframe`
- `tests/unit/test_filter_shape.py` — `test_shape_filter_rejects_unreadable_crs`
- `tests/unit/test_filter_shape.py` — `test_unexpected_or_null_shape_status_fails`
- `tests/unit/test_filter_shape.py` — `test_unknown_crs_fails`
- `tests/unit/test_filter_shape.py` — `test_valid_shape_rejects_every_incomplete_metric_form`
- `tests/unit/test_filter_shape.py` — `test_valid_shape_requires_complete_metrics_even_when_screening_disabled`
- `tests/unit/test_filter_shape.py` — `test_valid_shape_requires_ratio_at_least_one`
- `tests/unit/test_filter_shape.py` — `test_valid_shape_requires_strict_positive_width`

**Tests**

- `tests/unit/test_filter_shape.py::test_different_configs_change_results_for_same_parcels`
- `tests/unit/test_filter_shape.py::test_disabled_policy_is_an_exact_passthrough`
- `tests/unit/test_filter_shape.py::test_duplicate_parcel_id_fails`
- `tests/unit/test_filter_shape.py::test_enabled_outputs_record_active_policy_metadata`
- `tests/unit/test_filter_shape.py::test_enabled_partition_preserves_exact_ids_and_crs`
- `tests/unit/test_filter_shape.py::test_exact_width_and_ratio_boundaries_are_retained`
- `tests/unit/test_filter_shape.py::test_filter_does_not_mutate_input`
- `tests/unit/test_filter_shape.py::test_missing_required_column_fails`
- `tests/unit/test_filter_shape.py::test_negative_ratio_cannot_pass_permissive_thresholds`
- `tests/unit/test_filter_shape.py::test_non_finite_known_metric_on_valid_row_fails`
- `tests/unit/test_filter_shape.py::test_null_parcel_id_fails`
- `tests/unit/test_filter_shape.py::test_rejected_parcel_has_expected_primary_reason`
- `tests/unit/test_filter_shape.py::test_rejection_reason_precedence_is_deterministic`
- `tests/unit/test_filter_shape.py::test_shape_error_precedence_does_not_inspect_metrics`
- `tests/unit/test_filter_shape.py::test_shape_filter_rejects_duplicate_columns`
- `tests/unit/test_filter_shape.py::test_shape_filter_rejects_plain_dataframe`
- `tests/unit/test_filter_shape.py::test_shape_filter_rejects_unreadable_crs`
- `tests/unit/test_filter_shape.py::test_unexpected_or_null_shape_status_fails`
- `tests/unit/test_filter_shape.py::test_unknown_crs_fails`
- `tests/unit/test_filter_shape.py::test_valid_shape_rejects_every_incomplete_metric_form`
- `tests/unit/test_filter_shape.py::test_valid_shape_requires_complete_metrics_even_when_screening_disabled`
- `tests/unit/test_filter_shape.py::test_valid_shape_requires_ratio_at_least_one`
- `tests/unit/test_filter_shape.py::test_valid_shape_requires_strict_positive_width`

**Business interpretation**

This symbol contributes to the `cadastre` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `geometry_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `length_width_ratio` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `parcel_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `rejection_reason` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `shape_policy_max_ratio` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `shape_policy_min_width_m` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | linear distance/length in metres; proxy meaning is limited by the introducing stage. Consumers and exact calculations are the functions that reference this column above. |
| `shape_policy_version` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `shape_rejection_reason` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `shape_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `width_m` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | linear distance/length in metres; proxy meaning is limited by the introducing stage. Consumers and exact calculations are the functions that reference this column above. |

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

This file contributes to LandScout's `cadastre` evidence flow as described by its purpose and public symbols. It preserves the distinction among fact, proxy evidence, policy interpretation, diagnostic status, and parcel precheck.

## 15. Explicit non-goals

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

## 16. Tests

Direct name-resolved tests appear under each symbol. Higher-level tests may exercise private helpers through a public source-complete function; companion documents for all test files describe their fixtures, actions, assertions, and boundaries.

## 17. Change impact

Changing this file requires reviewing its static callers, package exports, directly mapped tests, relevant schema/hash/version constants, source locks, persisted artifact contracts, and the corresponding pipeline/cross-cutting documents. Any byte change makes the SHA256 above stale and requires regenerating this companion.

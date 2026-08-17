# `src/landscout/stages/filter_parcels.py`

## File identity

- Repository path: `src/landscout/stages/filter_parcels.py`
- File type: Python source
- Layer: processing/policy stage
- Domain: cadastre
- Responsibility: Applies configured factual parcel-area bounds and records explicit keep/reject facts without ranking.
- Source SHA256: `aa2071fc0df4ae843ded9df394df0b9d2f151d84eb5ac6edee1a41c3d6e2f439`

## 1. Purpose

Applies configured factual parcel-area bounds and records explicit keep/reject facts without ranking.

## 2. Position in LandScout architecture

This file belongs to the **processing/policy stage** layer and the **cadastre** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from math import isfinite`
- `from numbers import Real`

### Third-party packages

- `import geopandas as gpd`
- `from pyproj import CRS`

### Internal LandScout imports

- `from landscout.common.cadastre_contract import validate_cadastre_geometry_statuses`
- `from landscout.config import ParcelConfig, ShapeScreeningConfig`

## 4. Contract taxonomy

### A. Python constants

#### `AREA_REQUIRED_COLUMNS`

```python
AREA_REQUIRED_COLUMNS = frozenset(
    {"parcel_id", "geometry_status", "area_m2", "geometry"}
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/stages/filter_parcels.py::filter_parcels_by_area` (value argument/reference).

#### `SHAPE_REQUIRED_COLUMNS`

```python
SHAPE_REQUIRED_COLUMNS = frozenset(
    {"parcel_id", "shape_status", "width_m", "length_width_ratio", "geometry"}
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/stages/filter_parcels.py::_validate_shape_filter_input` (value argument/reference).

#### `ALLOWED_SHAPE_STATUSES`

```python
ALLOWED_SHAPE_STATUSES = frozenset({"VALID", "ERROR"})
```

Hash identity, algorithm, or canonical-content field used by the named integrity contract.


### B. Type aliases and closed domains

No module-level Literal/Annotated/TypeAlias declaration is present.

### C. Meaningful dunder contracts

No meaningful module-level dunder contract is declared.

### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

### `ParcelFilterError`

**Purpose:** Raised when normalized parcels cannot be partitioned safely.

**Kind:** controlled exception.

**Inheritance:** `ValueError`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.filter_parcels import (
    ParcelFilterError,
    filter_parcels_by_area,
    filter_parcels_by_shape,
)`.
- direct call or construction: `src/landscout/stages/filter_parcels.py::_validate_spatial_frame` via `ParcelFilterError`.
- direct call or construction: `src/landscout/stages/filter_parcels.py::_missing_columns` via `ParcelFilterError`.
- direct call or construction: `src/landscout/stages/filter_parcels.py::_validate_exact_parcel_ids` via `ParcelFilterError`.
- direct call or construction: `src/landscout/stages/filter_parcels.py::filter_parcels_by_area` via `ParcelFilterError`.
- direct call or construction: `src/landscout/stages/filter_parcels.py::_validate_shape_filter_input` via `ParcelFilterError`.
- direct call or construction: `src/landscout/stages/filter_parcels.py::_validate_shape_partition` via `ParcelFilterError`.
- direct call or construction: `src/landscout/stages/filter_parcels.py::filter_parcels_by_shape` via `ParcelFilterError`.
- callback/function object: `tests/unit/test_filter_parcels.py::test_missing_parcel_id_fails` via `pytest.raises(ParcelFilterError, match='parcel_id')`.
- callback/function object: `tests/unit/test_filter_parcels.py::test_null_parcel_id_fails` via `pytest.raises(ParcelFilterError, match='null')`.
- callback/function object: `tests/unit/test_filter_parcels.py::test_duplicate_parcel_id_fails` via `pytest.raises(ParcelFilterError, match='unique')`.
- callback/function object: `tests/unit/test_filter_parcels.py::test_valid_geometry_requires_strict_positive_finite_area` via `pytest.raises(ParcelFilterError, match='strict positive finite numeric')`.
- callback/function object: `tests/unit/test_filter_parcels.py::test_area_filter_requires_exact_non_empty_parcel_ids` via `pytest.raises(ParcelFilterError, match='exact non-empty strings')`.
- callback/function object: `tests/unit/test_filter_parcels.py::test_area_filter_rejects_plain_dataframe` via `pytest.raises(ParcelFilterError, match='GeoDataFrame')`.
- callback/function object: `tests/unit/test_filter_parcels.py::test_area_filter_rejects_duplicate_columns` via `pytest.raises(ParcelFilterError, match='columns.*unique')`.
- callback/function object: `tests/unit/test_filter_parcels.py::test_area_filter_rejects_malformed_spatial_envelope` via `pytest.raises(ParcelFilterError, match='geometry|CRS')`.
- callback/function object: `tests/unit/test_filter_parcels.py::test_area_filter_rejects_noncanonical_geometry_status` via `pytest.raises(ParcelFilterError, match='geometry_status')`.
- import/re-export: `tests/unit/test_filter_parcels.py::<module>` via `from landscout.stages.filter_parcels import ParcelFilterError, filter_parcels_by_area`.
- callback/function object: `tests/unit/test_filter_shape.py::test_missing_required_column_fails` via `pytest.raises(ParcelFilterError, match='Missing required shape columns')`.
- callback/function object: `tests/unit/test_filter_shape.py::test_null_parcel_id_fails` via `pytest.raises(ParcelFilterError, match='must not be null')`.
- callback/function object: `tests/unit/test_filter_shape.py::test_duplicate_parcel_id_fails` via `pytest.raises(ParcelFilterError, match='must be unique')`.
- callback/function object: `tests/unit/test_filter_shape.py::test_unknown_crs_fails` via `pytest.raises(ParcelFilterError, match='known CRS')`.
- callback/function object: `tests/unit/test_filter_shape.py::test_unexpected_or_null_shape_status_fails` via `pytest.raises(ParcelFilterError, match='Unexpected shape_status')`.
- callback/function object: `tests/unit/test_filter_shape.py::test_non_finite_known_metric_on_valid_row_fails` via `pytest.raises(ParcelFilterError, match='numeric and finite')`.
- callback/function object: `tests/unit/test_filter_shape.py::test_valid_shape_requires_strict_positive_width` via `pytest.raises(ParcelFilterError, match='width_m must be (numeric and finite|greater than zero)')`.
- callback/function object: `tests/unit/test_filter_shape.py::test_valid_shape_requires_ratio_at_least_one` via `pytest.raises(ParcelFilterError, match='length_width_ratio must be (numeric and finite|at least one)')`.
- callback/function object: `tests/unit/test_filter_shape.py::test_negative_ratio_cannot_pass_permissive_thresholds` via `pytest.raises(ParcelFilterError, match='length_width_ratio must be at least one')`.
- callback/function object: `tests/unit/test_filter_shape.py::test_valid_shape_requires_complete_metrics_even_when_screening_disabled` via `pytest.raises(ParcelFilterError, match='complete|must not be null')`.
- callback/function object: `tests/unit/test_filter_shape.py::test_valid_shape_rejects_every_incomplete_metric_form` via `pytest.raises(ParcelFilterError, match='complete')`.
- callback/function object: `tests/unit/test_filter_shape.py::test_shape_filter_rejects_plain_dataframe` via `pytest.raises(ParcelFilterError, match='GeoDataFrame')`.
- callback/function object: `tests/unit/test_filter_shape.py::test_shape_filter_rejects_duplicate_columns` via `pytest.raises(ParcelFilterError, match='columns.*unique')`.
- callback/function object: `tests/unit/test_filter_shape.py::test_shape_filter_rejects_unreadable_crs` via `pytest.raises(ParcelFilterError, match='CRS')`.
- import/re-export: `tests/unit/test_filter_shape.py::<module>` via `from landscout.stages.filter_parcels import (
    ParcelFilterError,
    filter_parcels_by_shape,
)`.

**Exact class source**

```python
class ParcelFilterError(ValueError):
    """Raised when normalized parcels cannot be partitioned safely."""
```


## 6. Functions and methods

### `_validate_spatial_frame`

**Exact signature**

```python
def _validate_spatial_frame(parcels: object, label: str) -> gpd.GeoDataFrame:
```

**Purpose**

Rejects malformed or inconsistent spatial frame; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
parcels
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(parcels, gpd.GeoDataFrame)`.
- Guard with a raise path: `parcels.columns.duplicated().any()`.
- Guard with a raise path: `geometry_name is None or geometry_name not in parcels.columns`.
- Guard with a raise path: `parcels.crs is None`.
- Explicit raise expressions: `ParcelFilterError(f'{label} input CRS must be readable')`, `ParcelFilterError(f'{label} input columns must be unique')`, `ParcelFilterError(f'{label} input geometry is invalid')`, `ParcelFilterError(f'{label} input must be a GeoDataFrame')`, `ParcelFilterError(f'{label} input must have a known CRS')`, `ParcelFilterError(f'{label} input requires an active geometry column')`.

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

- direct call or construction: `src/landscout/stages/filter_parcels.py::filter_parcels_by_area` via `_validate_spatial_frame`.
- direct call or construction: `src/landscout/stages/filter_parcels.py::_validate_shape_filter_input` via `_validate_spatial_frame`.

**Complete source-ordered implementation**

```python
def _validate_spatial_frame(parcels: object, label: str) -> gpd.GeoDataFrame:
    if not isinstance(parcels, gpd.GeoDataFrame):
        raise ParcelFilterError(f"{label} input must be a GeoDataFrame")
    if parcels.columns.duplicated().any():
        raise ParcelFilterError(f"{label} input columns must be unique")
    try:
        geometry_name = parcels.active_geometry_name
    except (AttributeError, ValueError) as error:
        raise ParcelFilterError(f"{label} input geometry is invalid") from error
    if geometry_name is None or geometry_name not in parcels.columns:
        raise ParcelFilterError(f"{label} input requires an active geometry column")
    if parcels.crs is None:
        raise ParcelFilterError(f"{label} input must have a known CRS")
    try:
        CRS.from_user_input(parcels.crs)
    except Exception as error:
        raise ParcelFilterError(f"{label} input CRS must be readable") from error
    return parcels
```

**Business boundary**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

### `_missing_columns`

**Exact signature**

```python
def _missing_columns(
    parcels: object,
    required: frozenset[str],
    label: str,
) -> frozenset[str]:
```

**Purpose**

Private `cadastre` helper for missing columns; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `frozenset[str]`.
- Every observed return expression is reproduced without truncation:
```python
required - set(parcels.columns)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `ParcelFilterError(f'{label} input must be a GeoDataFrame')`.

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

- direct call or construction: `src/landscout/stages/filter_parcels.py::filter_parcels_by_area` via `_missing_columns`.
- direct call or construction: `src/landscout/stages/filter_parcels.py::_validate_shape_filter_input` via `_missing_columns`.

**Complete source-ordered implementation**

```python
def _missing_columns(
    parcels: object,
    required: frozenset[str],
    label: str,
) -> frozenset[str]:
    try:
        return required - set(parcels.columns)  # type: ignore[attr-defined]
    except Exception as error:
        raise ParcelFilterError(f"{label} input must be a GeoDataFrame") from error
```

**Business boundary**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

### `_validate_exact_parcel_ids`

**Exact signature**

```python
def _validate_exact_parcel_ids(parcels: gpd.GeoDataFrame) -> None:
```

**Purpose**

Rejects malformed or inconsistent exact parcel ids; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `identifiers.isna().any()`.
- Guard with a raise path: `any((not isinstance(identifier, str) or not identifier or identifier != identifier.strip() for identifier in identifiers))`.
- Guard with a raise path: `identifiers.duplicated().any()`.
- Explicit raise expressions: `ParcelFilterError('parcel_id values must be exact non-empty strings')`, `ParcelFilterError('parcel_id values must be unique')`, `ParcelFilterError('parcel_id values must not be null')`.

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

- direct call or construction: `src/landscout/stages/filter_parcels.py::filter_parcels_by_area` via `_validate_exact_parcel_ids`.
- direct call or construction: `src/landscout/stages/filter_parcels.py::_validate_shape_filter_input` via `_validate_exact_parcel_ids`.

**Complete source-ordered implementation**

```python
def _validate_exact_parcel_ids(parcels: gpd.GeoDataFrame) -> None:
    identifiers = parcels["parcel_id"]
    if identifiers.isna().any():
        raise ParcelFilterError("parcel_id values must not be null")
    if any(
        not isinstance(identifier, str)
        or not identifier
        or identifier != identifier.strip()
        for identifier in identifiers
    ):
        raise ParcelFilterError("parcel_id values must be exact non-empty strings")
    if identifiers.duplicated().any():
        raise ParcelFilterError("parcel_id values must be unique")
```

**Business boundary**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

### `_is_strict_finite_number`

**Exact signature**

```python
def _is_strict_finite_number(value: object) -> bool:
```

**Purpose**

Tests whether strict finite number; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `bool`.
- Every observed return expression is reproduced without truncation:
```python
isinstance(value, Real) and (not isinstance(value, bool)) and isfinite(float(value))
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

- direct call or construction: `src/landscout/stages/filter_parcels.py::filter_parcels_by_area` via `_is_strict_finite_number`.
- direct call or construction: `src/landscout/stages/filter_parcels.py::_validate_shape_filter_input` via `_is_strict_finite_number`.

**Complete source-ordered implementation**

```python
def _is_strict_finite_number(value: object) -> bool:
    return (
        isinstance(value, Real)
        and not isinstance(value, bool)
        and isfinite(float(value))
    )
```

**Business boundary**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

### `filter_parcels_by_area`

**Exact signature**

```python
def filter_parcels_by_area(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> tuple[gpd.GeoDataFrame, gpd.GeoDataFrame]:
```

**Purpose**

Partitions normalized parcels into candidates and rejected rows using configured inclusive area thresholds and explicit area rejection reasons.

**Return contract**

- Declared return annotation: `tuple[gpd.GeoDataFrame, gpd.GeoDataFrame]`.
- Every observed return expression is reproduced without truncation:
```python
(candidates, rejected)
```

**Validation and exceptions**

- Guard with a raise path: `missing_columns`.
- Guard with a raise path: `any((not _is_strict_finite_number(value) or float(value) <= 0 for value in parcels.loc[valid_geometry, 'area_m2']))`.
- Guard with a raise path: `len(parcels) != len(candidates) + len(rejected)`.
- Guard with a raise path: `candidates['parcel_id'].duplicated().any() or rejected['parcel_id'].duplicated().any()`.
- Guard with a raise path: `candidate_ids & rejected_ids`.
- Guard with a raise path: `candidate_ids | rejected_ids != input_ids`.
- Explicit raise expressions: `ParcelFilterError('Candidate and rejected parcel IDs overlap')`, `ParcelFilterError('Parcel partition contains duplicate parcel IDs')`, `ParcelFilterError('Parcel partition did not preserve every input row')`, `ParcelFilterError('Parcel partition did not preserve exact parcel IDs')`, `ParcelFilterError('area_m2 must be a strict positive finite numeric value when geometry_status is VALID')`, `ParcelFilterError(f'Missing required normalized columns: {formatted}')`, `ParcelFilterError(str(error))`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `parcels['area_m2'].between`, `parcels['area_m2'].notna`, `parcels['geometry_status'].tolist`, `rejected['area_m2'].notna`, `validate_cadastre_geometry_statuses`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: `rejected.loc[rejected_valid_geometry & rejected_known_area & (rejected['area_m2'] < area_config.min_area_m2), 'rejection_reason']`, `rejected.loc[rejected_valid_geometry & rejected_known_area & (rejected['area_m2'] > area_config.max_area_m2), 'rejection_reason']`, `rejected.loc[~rejected_valid_geometry, 'rejection_reason']`, `rejected['rejection_reason']`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.filter_parcels import (
    ParcelFilterError,
    filter_parcels_by_area,
    filter_parcels_by_shape,
)`.
- direct call or construction: `tests/unit/test_filter_parcels.py::test_minimum_boundary_is_included` via `filter_parcels_by_area`.
- direct call or construction: `tests/unit/test_filter_parcels.py::test_maximum_boundary_is_included` via `filter_parcels_by_area`.
- direct call or construction: `tests/unit/test_filter_parcels.py::test_rejected_parcel_has_expected_reason` via `filter_parcels_by_area`.
- direct call or construction: `tests/unit/test_filter_parcels.py::test_no_parcel_disappears` via `filter_parcels_by_area`.
- direct call or construction: `tests/unit/test_filter_parcels.py::test_thresholds_come_from_config` via `filter_parcels_by_area`.
- direct call or construction: `tests/unit/test_filter_parcels.py::test_missing_parcel_id_fails` via `filter_parcels_by_area`.
- direct call or construction: `tests/unit/test_filter_parcels.py::test_null_parcel_id_fails` via `filter_parcels_by_area`.
- direct call or construction: `tests/unit/test_filter_parcels.py::test_duplicate_parcel_id_fails` via `filter_parcels_by_area`.
- direct call or construction: `tests/unit/test_filter_parcels.py::test_candidate_and_rejected_ids_do_not_overlap` via `filter_parcels_by_area`.
- direct call or construction: `tests/unit/test_filter_parcels.py::test_exact_parcel_ids_are_preserved` via `filter_parcels_by_area`.
- direct call or construction: `tests/unit/test_filter_parcels.py::test_valid_geometry_requires_strict_positive_finite_area` via `filter_parcels_by_area`.
- direct call or construction: `tests/unit/test_filter_parcels.py::test_area_filter_requires_exact_non_empty_parcel_ids` via `filter_parcels_by_area`.
- direct call or construction: `tests/unit/test_filter_parcels.py::test_area_filter_rejects_plain_dataframe` via `filter_parcels_by_area`.
- direct call or construction: `tests/unit/test_filter_parcels.py::test_area_filter_rejects_duplicate_columns` via `filter_parcels_by_area`.
- direct call or construction: `tests/unit/test_filter_parcels.py::test_area_filter_rejects_malformed_spatial_envelope` via `filter_parcels_by_area`.
- direct call or construction: `tests/unit/test_filter_parcels.py::test_area_filter_rejects_noncanonical_geometry_status` via `filter_parcels_by_area`.
- import/re-export: `tests/unit/test_filter_parcels.py::<module>` via `from landscout.stages.filter_parcels import ParcelFilterError, filter_parcels_by_area`.

**Complete source-ordered implementation**

```python
def filter_parcels_by_area(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> tuple[gpd.GeoDataFrame, gpd.GeoDataFrame]:
    missing_columns = _missing_columns(parcels, AREA_REQUIRED_COLUMNS, "Area-filter")
    if missing_columns:
        formatted = ", ".join(sorted(missing_columns))
        raise ParcelFilterError(f"Missing required normalized columns: {formatted}")
    parcels = _validate_spatial_frame(parcels, "Area-filter")
    _validate_exact_parcel_ids(parcels)
    try:
        validate_cadastre_geometry_statuses(parcels["geometry_status"].tolist())
    except ValueError as error:
        raise ParcelFilterError(str(error)) from error

    valid_geometry = parcels["geometry_status"] == "VALID"
    if any(
        not _is_strict_finite_number(value) or float(value) <= 0
        for value in parcels.loc[valid_geometry, "area_m2"]
    ):
        raise ParcelFilterError(
            "area_m2 must be a strict positive finite numeric value when "
            "geometry_status is VALID"
        )

    known_area = parcels["area_m2"].notna()
    within_area_range = parcels["area_m2"].between(
        area_config.min_area_m2, area_config.max_area_m2, inclusive="both"
    )
    candidate_mask = valid_geometry & known_area & within_area_range

    candidates = parcels.loc[candidate_mask].copy()
    rejected = parcels.loc[~candidate_mask].copy()
    rejected["rejection_reason"] = "AREA_UNKNOWN"

    rejected_valid_geometry = rejected["geometry_status"] == "VALID"
    rejected_known_area = rejected["area_m2"].notna()
    rejected.loc[~rejected_valid_geometry, "rejection_reason"] = "INVALID_GEOMETRY"
    rejected.loc[
        rejected_valid_geometry
        & rejected_known_area
        & (rejected["area_m2"] < area_config.min_area_m2),
        "rejection_reason",
    ] = "AREA_BELOW_MIN"
    rejected.loc[
        rejected_valid_geometry
        & rejected_known_area
        & (rejected["area_m2"] > area_config.max_area_m2),
        "rejection_reason",
    ] = "AREA_ABOVE_MAX"

    if len(parcels) != len(candidates) + len(rejected):
        raise ParcelFilterError("Parcel partition did not preserve every input row")
    input_ids = set(parcels["parcel_id"])
    candidate_ids = set(candidates["parcel_id"])
    rejected_ids = set(rejected["parcel_id"])
    if candidates["parcel_id"].duplicated().any() or rejected[
        "parcel_id"
    ].duplicated().any():
        raise ParcelFilterError("Parcel partition contains duplicate parcel IDs")
    if candidate_ids & rejected_ids:
        raise ParcelFilterError("Candidate and rejected parcel IDs overlap")
    if candidate_ids | rejected_ids != input_ids:
        raise ParcelFilterError("Parcel partition did not preserve exact parcel IDs")
    return candidates, rejected
```

**Business boundary**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

### `_validate_shape_filter_input`

**Exact signature**

```python
def _validate_shape_filter_input(parcels: gpd.GeoDataFrame) -> None:
```

**Purpose**

Rejects malformed or inconsistent shape filter input; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `missing_columns`.
- Guard with a raise path: `statuses.isna().any() or unexpected_statuses`.
- Guard with a raise path: `parcels.loc[valid_rows, ['width_m', 'length_width_ratio']].isna().any().any()`.
- Guard with a raise path: `any((float(value) <= 0 for value in valid_width))`.
- Guard with a raise path: `any((float(value) < 1 for value in valid_ratio))`.
- Guard with a raise path: `any((not _is_strict_finite_number(value) for value in parcels.loc[valid_rows, column]))`.
- Explicit raise expressions: `ParcelFilterError('VALID shape rows must have complete width_m and length_width_ratio metrics')`, `ParcelFilterError('length_width_ratio must be at least one when shape_status is VALID')`, `ParcelFilterError('width_m must be greater than zero when shape_status is VALID')`, `ParcelFilterError(f'Missing required shape columns: {formatted}')`, `ParcelFilterError(f'Unexpected shape_status value(s): {detail}')`, `ParcelFilterError(f'{column} must be numeric and finite when shape_status is VALID')`.

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

- direct call or construction: `src/landscout/stages/filter_parcels.py::filter_parcels_by_shape` via `_validate_shape_filter_input`.

**Complete source-ordered implementation**

```python
def _validate_shape_filter_input(parcels: gpd.GeoDataFrame) -> None:
    missing_columns = _missing_columns(parcels, SHAPE_REQUIRED_COLUMNS, "Shape-filter")
    if missing_columns:
        formatted = ", ".join(sorted(missing_columns))
        raise ParcelFilterError(f"Missing required shape columns: {formatted}")
    parcels = _validate_spatial_frame(parcels, "Shape-filter")
    _validate_exact_parcel_ids(parcels)

    statuses = parcels["shape_status"]
    unexpected_statuses = set(statuses.dropna().unique()) - ALLOWED_SHAPE_STATUSES
    if statuses.isna().any() or unexpected_statuses:
        formatted = ", ".join(sorted(str(value) for value in unexpected_statuses))
        detail = formatted or "null"
        raise ParcelFilterError(f"Unexpected shape_status value(s): {detail}")

    valid_rows = statuses == "VALID"
    if parcels.loc[valid_rows, ["width_m", "length_width_ratio"]].isna().any().any():
        raise ParcelFilterError(
            "VALID shape rows must have complete width_m and length_width_ratio metrics"
        )
    for column in ("width_m", "length_width_ratio"):
        if any(
            not _is_strict_finite_number(value)
            for value in parcels.loc[valid_rows, column]
        ):
            raise ParcelFilterError(
                f"{column} must be numeric and finite when shape_status is VALID"
            )
    valid_width = parcels.loc[valid_rows, "width_m"]
    if any(float(value) <= 0 for value in valid_width):
        raise ParcelFilterError(
            "width_m must be greater than zero when shape_status is VALID"
        )
    valid_ratio = parcels.loc[valid_rows, "length_width_ratio"]
    if any(float(value) < 1 for value in valid_ratio):
        raise ParcelFilterError(
            "length_width_ratio must be at least one when shape_status is VALID"
        )
```

**Business boundary**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

### `_validate_shape_partition`

**Exact signature**

```python
def _validate_shape_partition(
    parcels: gpd.GeoDataFrame,
    retained: gpd.GeoDataFrame,
    rejected: gpd.GeoDataFrame,
) -> None:
```

**Purpose**

Rejects malformed or inconsistent shape partition; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `len(parcels) != len(retained) + len(rejected)`.
- Guard with a raise path: `retained['parcel_id'].duplicated().any() or rejected['parcel_id'].duplicated().any()`.
- Guard with a raise path: `retained_ids & rejected_ids`.
- Guard with a raise path: `retained_ids | rejected_ids != input_ids`.
- Explicit raise expressions: `ParcelFilterError('Retained and rejected parcel IDs overlap')`, `ParcelFilterError('Shape partition contains duplicate parcel IDs')`, `ParcelFilterError('Shape partition did not preserve every input row')`, `ParcelFilterError('Shape partition did not preserve exact parcel IDs')`.

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

- direct call or construction: `src/landscout/stages/filter_parcels.py::filter_parcels_by_shape` via `_validate_shape_partition`.

**Complete source-ordered implementation**

```python
def _validate_shape_partition(
    parcels: gpd.GeoDataFrame,
    retained: gpd.GeoDataFrame,
    rejected: gpd.GeoDataFrame,
) -> None:
    if len(parcels) != len(retained) + len(rejected):
        raise ParcelFilterError("Shape partition did not preserve every input row")
    if retained["parcel_id"].duplicated().any() or rejected[
        "parcel_id"
    ].duplicated().any():
        raise ParcelFilterError("Shape partition contains duplicate parcel IDs")

    input_ids = set(parcels["parcel_id"])
    retained_ids = set(retained["parcel_id"])
    rejected_ids = set(rejected["parcel_id"])
    if retained_ids & rejected_ids:
        raise ParcelFilterError("Retained and rejected parcel IDs overlap")
    if retained_ids | rejected_ids != input_ids:
        raise ParcelFilterError("Shape partition did not preserve exact parcel IDs")
```

**Business boundary**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

### `filter_parcels_by_shape`

**Exact signature**

```python
def filter_parcels_by_shape(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> tuple[gpd.GeoDataFrame, gpd.GeoDataFrame]:
```

**Purpose**

Partition shape-enriched parcels using an explicit screening policy.

**Return contract**

- Declared return annotation: `tuple[gpd.GeoDataFrame, gpd.GeoDataFrame]`.
- Every observed return expression is reproduced without truncation:
```python
(retained, rejected)

(retained, rejected)
```

**Validation and exceptions**

- Guard with a raise path: `min_width_m is None or max_ratio is None or calibration is None`.
- Explicit raise expressions: `ParcelFilterError('Enabled shape screening policy is incomplete')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `_validate_shape_filter_input`, `_validate_shape_partition`.
- Environment/process effects: none directly visible.
- In-memory mutation: `output['shape_policy_max_ratio']`, `output['shape_policy_min_width_m']`, `output['shape_policy_version']`, `rejected.loc[rejected_valid & (rejected_width < min_width_m), 'shape_rejection_reason']`, `rejected.loc[~rejected_valid, 'shape_rejection_reason']`, `rejected['shape_rejection_reason']`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.filter_parcels import (
    ParcelFilterError,
    filter_parcels_by_area,
    filter_parcels_by_shape,
)`.
- direct call or construction: `tests/unit/test_filter_shape.py::test_exact_width_and_ratio_boundaries_are_retained` via `filter_parcels_by_shape`.
- direct call or construction: `tests/unit/test_filter_shape.py::test_rejected_parcel_has_expected_primary_reason` via `filter_parcels_by_shape`.
- direct call or construction: `tests/unit/test_filter_shape.py::test_rejection_reason_precedence_is_deterministic` via `filter_parcels_by_shape`.
- direct call or construction: `tests/unit/test_filter_shape.py::test_shape_error_precedence_does_not_inspect_metrics` via `filter_parcels_by_shape`.
- direct call or construction: `tests/unit/test_filter_shape.py::test_enabled_outputs_record_active_policy_metadata` via `filter_parcels_by_shape`.
- direct call or construction: `tests/unit/test_filter_shape.py::test_enabled_partition_preserves_exact_ids_and_crs` via `filter_parcels_by_shape`.
- direct call or construction: `tests/unit/test_filter_shape.py::test_filter_does_not_mutate_input` via `filter_parcels_by_shape`.
- direct call or construction: `tests/unit/test_filter_shape.py::test_missing_required_column_fails` via `filter_parcels_by_shape`.
- direct call or construction: `tests/unit/test_filter_shape.py::test_null_parcel_id_fails` via `filter_parcels_by_shape`.
- direct call or construction: `tests/unit/test_filter_shape.py::test_duplicate_parcel_id_fails` via `filter_parcels_by_shape`.
- direct call or construction: `tests/unit/test_filter_shape.py::test_unknown_crs_fails` via `filter_parcels_by_shape`.
- direct call or construction: `tests/unit/test_filter_shape.py::test_unexpected_or_null_shape_status_fails` via `filter_parcels_by_shape`.
- direct call or construction: `tests/unit/test_filter_shape.py::test_non_finite_known_metric_on_valid_row_fails` via `filter_parcels_by_shape`.
- direct call or construction: `tests/unit/test_filter_shape.py::test_valid_shape_requires_strict_positive_width` via `filter_parcels_by_shape`.
- direct call or construction: `tests/unit/test_filter_shape.py::test_valid_shape_requires_ratio_at_least_one` via `filter_parcels_by_shape`.
- direct call or construction: `tests/unit/test_filter_shape.py::test_negative_ratio_cannot_pass_permissive_thresholds` via `filter_parcels_by_shape`.
- direct call or construction: `tests/unit/test_filter_shape.py::test_disabled_policy_is_an_exact_passthrough` via `filter_parcels_by_shape`.
- direct call or construction: `tests/unit/test_filter_shape.py::test_different_configs_change_results_for_same_parcels` via `filter_parcels_by_shape`.
- direct call or construction: `tests/unit/test_filter_shape.py::test_valid_shape_requires_complete_metrics_even_when_screening_disabled` via `filter_parcels_by_shape`.
- direct call or construction: `tests/unit/test_filter_shape.py::test_valid_shape_rejects_every_incomplete_metric_form` via `filter_parcels_by_shape`.
- direct call or construction: `tests/unit/test_filter_shape.py::test_shape_filter_rejects_plain_dataframe` via `filter_parcels_by_shape`.
- direct call or construction: `tests/unit/test_filter_shape.py::test_shape_filter_rejects_duplicate_columns` via `filter_parcels_by_shape`.
- direct call or construction: `tests/unit/test_filter_shape.py::test_shape_filter_rejects_unreadable_crs` via `filter_parcels_by_shape`.
- import/re-export: `tests/unit/test_filter_shape.py::<module>` via `from landscout.stages.filter_parcels import (
    ParcelFilterError,
    filter_parcels_by_shape,
)`.

**Complete source-ordered implementation**

```python
def filter_parcels_by_shape(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> tuple[gpd.GeoDataFrame, gpd.GeoDataFrame]:
    """Partition shape-enriched parcels using an explicit screening policy."""
    _validate_shape_filter_input(parcels)

    if not shape_config.enabled:
        retained = parcels.copy()
        rejected = parcels.iloc[0:0].copy()
        _validate_shape_partition(parcels, retained, rejected)
        return retained, rejected

    min_width_m = shape_config.min_width_m
    max_ratio = shape_config.max_length_width_ratio
    calibration = shape_config.calibration
    if min_width_m is None or max_ratio is None or calibration is None:
        raise ParcelFilterError("Enabled shape screening policy is incomplete")

    valid_shape = parcels["shape_status"] == "VALID"
    screening_width = parcels["width_m"].where(valid_shape)
    screening_ratio = parcels["length_width_ratio"].where(valid_shape)
    known_width = screening_width.notna()
    known_ratio = screening_ratio.notna()
    retained_mask = (
        valid_shape
        & known_width
        & known_ratio
        & (screening_width >= min_width_m)
        & (screening_ratio <= max_ratio)
    )

    retained = parcels.loc[retained_mask].copy()
    rejected = parcels.loc[~retained_mask].copy()

    rejected["shape_rejection_reason"] = "RATIO_ABOVE_MAX"
    rejected_valid = rejected["shape_status"] == "VALID"
    rejected_width = rejected["width_m"].where(rejected_valid)
    rejected.loc[
        rejected_valid
        & (rejected_width < min_width_m),
        "shape_rejection_reason",
    ] = "WIDTH_BELOW_MIN"
    rejected.loc[~rejected_valid, "shape_rejection_reason"] = "SHAPE_ERROR"

    for output in (retained, rejected):
        output["shape_policy_version"] = calibration.policy_version
        output["shape_policy_min_width_m"] = min_width_m
        output["shape_policy_max_ratio"] = max_ratio

    _validate_shape_partition(parcels, retained, rejected)
    return retained, rejected
```

**Business boundary**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.


## 7. Data contracts

### Frame-preservation and semantic notes

- Area filtering copies all input columns to both partitions, preserving each subset's input order and original index labels. Candidates add no column; rejected rows append `rejection_reason` with the closed values `AREA_UNKNOWN`, `INVALID_GEOMETRY`, `AREA_BELOW_MIN`, or `AREA_ABOVE_MAX`.
- With shape screening enabled, both outputs preserve all input columns/order/index and append `shape_policy_version`, `shape_policy_min_width_m`, and `shape_policy_max_ratio`; rejected rows additionally append `shape_rejection_reason` with the closed values `RATIO_ABOVE_MAX`, `WIDTH_BELOW_MIN`, or `SHAPE_ERROR`.
- Configured width and ratio values are policy metadata, not measurements. When shape screening is disabled, retained is an unchanged copy of all rows and rejected is an empty same-schema copy; no shape policy/rejection columns are added on that branch.

### `AREA_REJECTED_APPEND_COLUMNS` — source-reviewed frame contract

Only the rejected area partition appends this column; candidates preserve the exact input schema.

| Position | Exact column | Dtype | Nullability/domain | Classification | Source/calculation/business meaning |
|---:|---|---|---|---|---|
| 1 | `rejection_reason` | non-null string values | never null on rejected rows | policy-derived screening result | Exactly AREA_UNKNOWN, INVALID_GEOMETRY, AREA_BELOW_MIN, or AREA_ABOVE_MAX; it is not a score or rank. |

### `ENABLED_SHAPE_POLICY_APPEND_COLUMNS` — source-reviewed frame contract

Appended to both retained and rejected partitions only when shape screening is enabled.

| Position | Exact column | Dtype | Nullability/domain | Classification | Source/calculation/business meaning |
|---:|---|---|---|---|---|
| 1 | `shape_policy_version` | string | non-null on enabled branch | policy lineage | Configured calibration policy version. |
| 2 | `shape_policy_min_width_m` | numeric | non-null on enabled branch | policy configuration | Configured width threshold in metres, not measured width. |
| 3 | `shape_policy_max_ratio` | numeric | non-null on enabled branch | policy configuration | Configured maximum dimensionless length/width ratio. |

### `ENABLED_SHAPE_REJECTED_EXTRA_COLUMN` — source-reviewed frame contract

Appended only to rejected rows on the enabled branch.

| Position | Exact column | Dtype | Nullability/domain | Classification | Source/calculation/business meaning |
|---:|---|---|---|---|---|
| 1 | `shape_rejection_reason` | non-null string values | never null on enabled rejected rows | policy-derived screening result | Exactly RATIO_ABOVE_MAX, WIDTH_BELOW_MIN, or SHAPE_ERROR; it is not a score or rank. |

### `AREA_REQUIRED_COLUMNS` — required input frame fields (unordered when stored as a set)

```python
AREA_REQUIRED_COLUMNS = frozenset(
    {"parcel_id", "geometry_status", "area_m2", "geometry"}
)
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `area_m2` | float64 when builder initializes NaN/numeric metric; otherwise exact source numeric dtype shown by implementation | null only on the explicit no-measurement/invalid path | geometry metric | Square-metre geometry measurement; not a policy threshold unless the field belongs to configuration. |
| 2 | `geometry` | GeoPandas geometry dtype | nullable only where the owning geometry-status contract permits it | source/geometry fact | Active geometry; never an authorization or suitability result. |
| 3 | `geometry_status` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | derived factual classification | Stores one value from its separately documented closed domain; domain values are not columns. |
| 4 | `parcel_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |

### `SHAPE_REQUIRED_COLUMNS` — required input frame fields (unordered when stored as a set)

```python
SHAPE_REQUIRED_COLUMNS = frozenset(
    {"parcel_id", "shape_status", "width_m", "length_width_ratio", "geometry"}
)
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `geometry` | GeoPandas geometry dtype | nullable only where the owning geometry-status contract permits it | source/geometry fact | Active geometry; never an authorization or suitability result. |
| 2 | `length_width_ratio` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 3 | `parcel_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 4 | `shape_status` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 5 | `width_m` | builder/source numeric dtype shown by the implementation; no cast is inferred from the name | null on explicit no-match/unknown paths | derived fact or proxy metric | Numeric evidence in the unit encoded by the suffix; it does not establish legal/capacity suitability. |


No enum/status/Literal value is classified as a column unless it is separately present in a canonical schema declaration. Mapping keys, JSON keys, dataclass fields, and configuration leaves remain distinct categories.

## 8. Interfaces

This module does not define `__all__`; no package-export guarantee is inferred from its absence. Symbols can still be imported directly or re-exported by a separate package initializer, as shown by the reference lists.

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

The module contributes to the cadastre flow through the exact facts, proxy evidence, policy results, diagnostics, or prechecks identified above.

## 15. Explicit non-goals

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

## 16. Tests

Test consumers and framework invocation are included in per-symbol interfaces. Test modules distinguish fixture injection from parameterized values and reproduce setup/action/assertion source.

## 17. Change impact

Any source-byte change invalidates the SHA above. Review exact exports, aliases, canonical frame schemas/dtypes, configured source/policy identities, callers, framework hooks, artifacts, and all linked tests before updating this companion.

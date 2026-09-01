# `src/landscout/stages/filter_parcels.py`

## File identity

- Repository path: `src/landscout/stages/filter_parcels.py`
- File type: Python source
- Layer: pipeline stage
- Domain: factual transformation, evidence, or policy boundary
- Responsibility: Applies configured factual parcel-area bounds and records explicit keep/reject facts without ranking.
- Source SHA256: `53487ea689f4b650c17a3e692d5b3bf0fb80b57aefaf0621b66883ed40e45713`

## 1. STEP 7F.1A.4 contract delta

- Revalidates parcel configuration and canonical parcel facts before applying configured factual area bounds.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Applies configured factual parcel-area bounds and records explicit keep/reject facts without ranking.

The file belongs to the **pipeline stage** layer and **factual transformation, evidence, or policy boundary** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from math import isfinite`
- `from numbers import Real`

### Third-party packages

- `import geopandas as gpd`
- `from pydantic import ValidationError`
- `from pyproj import CRS`

### Internal LandScout imports

- `from landscout.common.cadastre_contract import validate_normalized_cadastre_parcels`
- `from landscout.config import ParcelConfig, ShapeScreeningConfig`

## 4. Contract taxonomy

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `AREA_REQUIRED_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
AREA_REQUIRED_COLUMNS = frozenset(
    {"parcel_id", "geometry_status", "area_m2", "geometry"}
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `SHAPE_REQUIRED_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
SHAPE_REQUIRED_COLUMNS = frozenset(
    {"parcel_id", "shape_status", "width_m", "length_width_ratio", "geometry"}
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `ALLOWED_SHAPE_STATUSES`

- Category: module constant or closed domain.
- Exact declaration:

```python
ALLOWED_SHAPE_STATUSES = frozenset({"VALID", "ERROR"})
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

### `ParcelFilterError`

**Source purpose:** Raised when normalized parcels cannot be partitioned safely.

- Exact decorators: none.
- Exact bases: `ValueError`.

**Fields and model attributes**

No direct class/model/dataclass or `self` field assignment is declared.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.filter_parcels import (
    ParcelFilterError,
    filter_parcels_by_area,
    filter_parcels_by_shape,
)`
- constructor call: `landscout.stages.filter_parcels::_validate_spatial_frame` via `ParcelFilterError`
- value/type reference: `landscout.stages.filter_parcels::_validate_spatial_frame` via `ParcelFilterError`
- constructor call: `landscout.stages.filter_parcels::_missing_columns` via `ParcelFilterError`
- value/type reference: `landscout.stages.filter_parcels::_missing_columns` via `ParcelFilterError`
- constructor call: `landscout.stages.filter_parcels::_validate_exact_parcel_ids` via `ParcelFilterError`
- value/type reference: `landscout.stages.filter_parcels::_validate_exact_parcel_ids` via `ParcelFilterError`
- constructor call: `landscout.stages.filter_parcels::filter_parcels_by_area` via `ParcelFilterError`
- value/type reference: `landscout.stages.filter_parcels::filter_parcels_by_area` via `ParcelFilterError`
- constructor call: `landscout.stages.filter_parcels::_validate_shape_filter_input` via `ParcelFilterError`
- value/type reference: `landscout.stages.filter_parcels::_validate_shape_filter_input` via `ParcelFilterError`
- constructor call: `landscout.stages.filter_parcels::_validate_shape_partition` via `ParcelFilterError`
- value/type reference: `landscout.stages.filter_parcels::_validate_shape_partition` via `ParcelFilterError`
- constructor call: `landscout.stages.filter_parcels::filter_parcels_by_shape` via `ParcelFilterError`
- value/type reference: `landscout.stages.filter_parcels::filter_parcels_by_shape` via `ParcelFilterError`
- import: `tests.unit.test_filter_parcels::<module>` via `from landscout.stages.filter_parcels import ParcelFilterError, filter_parcels_by_area`
- value/type reference: `tests.unit.test_filter_parcels::test_area_filter_revalidates_mutated_config_before_frame_work` via `ParcelFilterError`
- value/type reference: `tests.unit.test_filter_parcels::test_missing_parcel_id_fails` via `ParcelFilterError`
- value/type reference: `tests.unit.test_filter_parcels::test_null_parcel_id_fails` via `ParcelFilterError`
- value/type reference: `tests.unit.test_filter_parcels::test_duplicate_parcel_id_fails` via `ParcelFilterError`
- value/type reference: `tests.unit.test_filter_parcels::test_valid_geometry_requires_strict_positive_finite_area` via `ParcelFilterError`
- value/type reference: `tests.unit.test_filter_parcels::test_valid_geometry_with_forged_positive_area_is_rejected` via `ParcelFilterError`
- value/type reference: `tests.unit.test_filter_parcels::test_invalid_geometry_with_recorded_area_is_rejected` via `ParcelFilterError`
- value/type reference: `tests.unit.test_filter_parcels::test_parcel_id_must_match_its_canonical_source_identity_fields` via `ParcelFilterError`
- value/type reference: `tests.unit.test_filter_parcels::test_area_filter_requires_exact_non_empty_parcel_ids` via `ParcelFilterError`
- value/type reference: `tests.unit.test_filter_parcels::test_area_filter_rejects_plain_dataframe` via `ParcelFilterError`
- value/type reference: `tests.unit.test_filter_parcels::test_area_filter_rejects_duplicate_columns` via `ParcelFilterError`
- value/type reference: `tests.unit.test_filter_parcels::test_area_filter_rejects_malformed_spatial_envelope` via `ParcelFilterError`
- value/type reference: `tests.unit.test_filter_parcels::test_area_filter_rejects_noncanonical_geometry_status` via `ParcelFilterError`
- import: `tests.unit.test_filter_shape::<module>` via `from landscout.stages.filter_parcels import (
    ParcelFilterError,
    filter_parcels_by_shape,
)`
- value/type reference: `tests.unit.test_filter_shape::test_shape_filter_revalidates_mutated_config_before_frame_work` via `ParcelFilterError`
- value/type reference: `tests.unit.test_filter_shape::test_missing_required_column_fails` via `ParcelFilterError`
- value/type reference: `tests.unit.test_filter_shape::test_null_parcel_id_fails` via `ParcelFilterError`
- value/type reference: `tests.unit.test_filter_shape::test_duplicate_parcel_id_fails` via `ParcelFilterError`
- value/type reference: `tests.unit.test_filter_shape::test_unknown_crs_fails` via `ParcelFilterError`
- value/type reference: `tests.unit.test_filter_shape::test_unexpected_or_null_shape_status_fails` via `ParcelFilterError`
- value/type reference: `tests.unit.test_filter_shape::test_non_finite_known_metric_on_valid_row_fails` via `ParcelFilterError`
- value/type reference: `tests.unit.test_filter_shape::test_valid_shape_requires_strict_positive_width` via `ParcelFilterError`
- value/type reference: `tests.unit.test_filter_shape::test_valid_shape_requires_ratio_at_least_one` via `ParcelFilterError`
- value/type reference: `tests.unit.test_filter_shape::test_negative_ratio_cannot_pass_permissive_thresholds` via `ParcelFilterError`
- value/type reference: `tests.unit.test_filter_shape::test_valid_shape_requires_complete_metrics_even_when_screening_disabled` via `ParcelFilterError`
- value/type reference: `tests.unit.test_filter_shape::test_valid_shape_rejects_every_incomplete_metric_form` via `ParcelFilterError`
- value/type reference: `tests.unit.test_filter_shape::test_shape_filter_rejects_plain_dataframe` via `ParcelFilterError`
- value/type reference: `tests.unit.test_filter_shape::test_shape_filter_rejects_duplicate_columns` via `ParcelFilterError`
- value/type reference: `tests.unit.test_filter_shape::test_shape_filter_rejects_unreadable_crs` via `ParcelFilterError`

**Exact class source**

```python
class ParcelFilterError(ValueError):
    """Raised when normalized parcels cannot be partitioned safely."""
```


## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `_validate_spatial_frame`

**Purpose:** Implements `validate spatial frame` within the file role: Applies configured factual parcel-area bounds and records explicit keep/reject facts without ranking.

**Exact signature**

```python
def _validate_spatial_frame(parcels: object, label: str) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `object` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `parcels`
- Explicit raise paths:
  - `ParcelFilterError(f"{label} input must be a GeoDataFrame")` under lexical guard `not isinstance(parcels, gpd.GeoDataFrame)`.
  - `ParcelFilterError(f"{label} input columns must be unique")` under lexical guard `parcels.columns.duplicated().any()`.
  - `ParcelFilterError(f"{label} input geometry is invalid")`.
  - `ParcelFilterError(f"{label} input requires an active geometry column")` under lexical guard `geometry_name is None or geometry_name not in parcels.columns`.
  - `ParcelFilterError(f"{label} input must have a known CRS")` under lexical guard `parcels.crs is None`.
  - `ParcelFilterError(f"{label} input CRS must be readable")`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.filter_parcels::filter_parcels_by_area` via `_validate_spatial_frame`
- value/type reference: `landscout.stages.filter_parcels::filter_parcels_by_area` via `_validate_spatial_frame`
- direct call: `landscout.stages.filter_parcels::_validate_shape_filter_input` via `_validate_spatial_frame`
- value/type reference: `landscout.stages.filter_parcels::_validate_shape_filter_input` via `_validate_spatial_frame`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `ParcelFilterError` | `landscout.stages.filter_parcels.ParcelFilterError` |
| `parcels.columns.duplicated().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels.columns.duplicated` | `unresolved local/third-party receiver; no ownership inferred` |
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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_missing_columns`

**Purpose:** Implements `missing columns` within the file role: Applies configured factual parcel-area bounds and records explicit keep/reject facts without ranking.

**Exact signature**

```python
def _missing_columns(
    parcels: object,
    required: frozenset[str],
    label: str,
) -> frozenset[str]:
```

- Exact decorators: none.
- Declared return annotation: `frozenset[str]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `object` | `required` |
| `required` | positional-or-keyword | `frozenset[str]` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `required - set(parcels.columns)`
- Explicit raise paths:
  - `ParcelFilterError(f"{label} input must be a GeoDataFrame")`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.filter_parcels::filter_parcels_by_area` via `_missing_columns`
- value/type reference: `landscout.stages.filter_parcels::filter_parcels_by_area` via `_missing_columns`
- direct call: `landscout.stages.filter_parcels::_validate_shape_filter_input` via `_missing_columns`
- value/type reference: `landscout.stages.filter_parcels::_validate_shape_filter_input` via `_missing_columns`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `ParcelFilterError` | `landscout.stages.filter_parcels.ParcelFilterError` |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_exact_parcel_ids`

**Purpose:** Implements `validate exact parcel ids` within the file role: Applies configured factual parcel-area bounds and records explicit keep/reject facts without ranking.

**Exact signature**

```python
def _validate_exact_parcel_ids(parcels: gpd.GeoDataFrame) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `ParcelFilterError("parcel_id values must not be null")` under lexical guard `identifiers.isna().any()`.
  - `ParcelFilterError("parcel_id values must be exact non-empty strings")` under lexical guard `any(<br>        not isinstance(identifier, str)<br>        or not identifier<br>        or identifier != identifier.strip()<br>        for identifier in identifiers<br>    )`.
  - `ParcelFilterError("parcel_id values must be unique")` under lexical guard `identifiers.duplicated().any()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.filter_parcels::filter_parcels_by_area` via `_validate_exact_parcel_ids`
- value/type reference: `landscout.stages.filter_parcels::filter_parcels_by_area` via `_validate_exact_parcel_ids`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `identifiers.isna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `identifiers.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `ParcelFilterError` | `landscout.stages.filter_parcels.ParcelFilterError` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `identifier.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `identifiers.duplicated().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `identifiers.duplicated` | `unresolved local/third-party receiver; no ownership inferred` |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_is_strict_finite_number`

**Purpose:** Implements `is strict finite number` within the file role: Applies configured factual parcel-area bounds and records explicit keep/reject facts without ranking.

**Exact signature**

```python
def _is_strict_finite_number(value: object) -> bool:
```

- Exact decorators: none.
- Declared return annotation: `bool`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `isinstance(value, Real)<br>        and not isinstance(value, bool)<br>        and isfinite(float(value))`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.filter_parcels::_validate_shape_filter_input` via `_is_strict_finite_number`
- value/type reference: `landscout.stages.filter_parcels::_validate_shape_filter_input` via `_is_strict_finite_number`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `isfinite` | `math.isfinite` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _is_strict_finite_number(value: object) -> bool:
    return (
        isinstance(value, Real)
        and not isinstance(value, bool)
        and isfinite(float(value))
    )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `filter_parcels_by_area`

**Purpose:** Implements `filter parcels by area` within the file role: Applies configured factual parcel-area bounds and records explicit keep/reject facts without ranking.

**Exact signature**

```python
def filter_parcels_by_area(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> tuple[gpd.GeoDataFrame, gpd.GeoDataFrame]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[gpd.GeoDataFrame, gpd.GeoDataFrame]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `area_config` | positional-or-keyword | `ParcelConfig` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `candidates, rejected`
- Explicit raise paths:
  - `TypeError("Area filter config type is invalid")` under lexical guard `type(area_config) is not ParcelConfig`.
  - `ParcelFilterError("Area filter config is invalid")`.
  - `ParcelFilterError(<br>            "Area-filter input collides with generated rejection_reason"<br>        )` under lexical guard `"rejection_reason" in getattr(parcels, "columns", ())`.
  - `ParcelFilterError(f"Missing required normalized columns: {formatted}")` under lexical guard `missing_columns`.
  - `ParcelFilterError(str(error))`.
  - `ParcelFilterError("Parcel partition did not preserve every input row")` under lexical guard `len(parcels) != len(candidates) + len(rejected)`.
  - `ParcelFilterError("Parcel partition contains duplicate parcel IDs")` under lexical guard `candidates["parcel_id"].duplicated().any()<br>        or rejected["parcel_id"].duplicated().any()`.
  - `ParcelFilterError("Candidate and rejected parcel IDs overlap")` under lexical guard `candidate_ids & rejected_ids`.
  - `ParcelFilterError("Parcel partition did not preserve exact parcel IDs")` under lexical guard `candidate_ids \| rejected_ids != input_ids`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.stages::<module>` via `from landscout.stages.filter_parcels import (
    ParcelFilterError,
    filter_parcels_by_area,
    filter_parcels_by_shape,
)`
- import: `tests.unit.test_filter_parcels::<module>` via `from landscout.stages.filter_parcels import ParcelFilterError, filter_parcels_by_area`
- direct call: `tests.unit.test_filter_parcels::test_minimum_boundary_is_included` via `filter_parcels_by_area`
- value/type reference: `tests.unit.test_filter_parcels::test_minimum_boundary_is_included` via `filter_parcels_by_area`
- direct call: `tests.unit.test_filter_parcels::test_maximum_boundary_is_included` via `filter_parcels_by_area`
- value/type reference: `tests.unit.test_filter_parcels::test_maximum_boundary_is_included` via `filter_parcels_by_area`
- direct call: `tests.unit.test_filter_parcels::test_rejected_parcel_has_expected_reason` via `filter_parcels_by_area`
- value/type reference: `tests.unit.test_filter_parcels::test_rejected_parcel_has_expected_reason` via `filter_parcels_by_area`
- direct call: `tests.unit.test_filter_parcels::test_no_parcel_disappears` via `filter_parcels_by_area`
- value/type reference: `tests.unit.test_filter_parcels::test_no_parcel_disappears` via `filter_parcels_by_area`
- direct call: `tests.unit.test_filter_parcels::test_thresholds_come_from_config` via `filter_parcels_by_area`
- value/type reference: `tests.unit.test_filter_parcels::test_thresholds_come_from_config` via `filter_parcels_by_area`
- direct call: `tests.unit.test_filter_parcels::test_area_filter_revalidates_mutated_config_before_frame_work` via `filter_parcels_by_area`
- value/type reference: `tests.unit.test_filter_parcels::test_area_filter_revalidates_mutated_config_before_frame_work` via `filter_parcels_by_area`
- direct call: `tests.unit.test_filter_parcels::test_missing_parcel_id_fails` via `filter_parcels_by_area`
- value/type reference: `tests.unit.test_filter_parcels::test_missing_parcel_id_fails` via `filter_parcels_by_area`
- direct call: `tests.unit.test_filter_parcels::test_null_parcel_id_fails` via `filter_parcels_by_area`
- value/type reference: `tests.unit.test_filter_parcels::test_null_parcel_id_fails` via `filter_parcels_by_area`
- direct call: `tests.unit.test_filter_parcels::test_duplicate_parcel_id_fails` via `filter_parcels_by_area`
- value/type reference: `tests.unit.test_filter_parcels::test_duplicate_parcel_id_fails` via `filter_parcels_by_area`
- direct call: `tests.unit.test_filter_parcels::test_candidate_and_rejected_ids_do_not_overlap` via `filter_parcels_by_area`
- value/type reference: `tests.unit.test_filter_parcels::test_candidate_and_rejected_ids_do_not_overlap` via `filter_parcels_by_area`
- direct call: `tests.unit.test_filter_parcels::test_exact_parcel_ids_are_preserved` via `filter_parcels_by_area`
- value/type reference: `tests.unit.test_filter_parcels::test_exact_parcel_ids_are_preserved` via `filter_parcels_by_area`
- direct call: `tests.unit.test_filter_parcels::test_valid_geometry_requires_strict_positive_finite_area` via `filter_parcels_by_area`
- value/type reference: `tests.unit.test_filter_parcels::test_valid_geometry_requires_strict_positive_finite_area` via `filter_parcels_by_area`
- direct call: `tests.unit.test_filter_parcels::test_valid_geometry_with_forged_positive_area_is_rejected` via `filter_parcels_by_area`
- value/type reference: `tests.unit.test_filter_parcels::test_valid_geometry_with_forged_positive_area_is_rejected` via `filter_parcels_by_area`
- direct call: `tests.unit.test_filter_parcels::test_invalid_geometry_with_recorded_area_is_rejected` via `filter_parcels_by_area`
- value/type reference: `tests.unit.test_filter_parcels::test_invalid_geometry_with_recorded_area_is_rejected` via `filter_parcels_by_area`
- direct call: `tests.unit.test_filter_parcels::test_parcel_id_must_match_its_canonical_source_identity_fields` via `filter_parcels_by_area`
- value/type reference: `tests.unit.test_filter_parcels::test_parcel_id_must_match_its_canonical_source_identity_fields` via `filter_parcels_by_area`
- direct call: `tests.unit.test_filter_parcels::test_area_filter_requires_exact_non_empty_parcel_ids` via `filter_parcels_by_area`
- value/type reference: `tests.unit.test_filter_parcels::test_area_filter_requires_exact_non_empty_parcel_ids` via `filter_parcels_by_area`
- direct call: `tests.unit.test_filter_parcels::test_area_filter_rejects_plain_dataframe` via `filter_parcels_by_area`
- value/type reference: `tests.unit.test_filter_parcels::test_area_filter_rejects_plain_dataframe` via `filter_parcels_by_area`
- direct call: `tests.unit.test_filter_parcels::test_area_filter_rejects_duplicate_columns` via `filter_parcels_by_area`
- value/type reference: `tests.unit.test_filter_parcels::test_area_filter_rejects_duplicate_columns` via `filter_parcels_by_area`
- direct call: `tests.unit.test_filter_parcels::test_area_filter_rejects_malformed_spatial_envelope` via `filter_parcels_by_area`
- value/type reference: `tests.unit.test_filter_parcels::test_area_filter_rejects_malformed_spatial_envelope` via `filter_parcels_by_area`
- direct call: `tests.unit.test_filter_parcels::test_area_filter_rejects_noncanonical_geometry_status` via `filter_parcels_by_area`
- value/type reference: `tests.unit.test_filter_parcels::test_area_filter_rejects_noncanonical_geometry_status` via `filter_parcels_by_area`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `TypeError` | `unresolved local/third-party receiver; no ownership inferred` |
| `ParcelConfig.model_validate` | `landscout.config.ParcelConfig.model_validate` |
| `area_config.model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `ParcelFilterError` | `landscout.stages.filter_parcels.ParcelFilterError` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `_missing_columns` | `landscout.stages.filter_parcels._missing_columns` |
| `", ".join` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validate_spatial_frame` | `landscout.stages.filter_parcels._validate_spatial_frame` |
| `_validate_exact_parcel_ids` | `landscout.stages.filter_parcels._validate_exact_parcel_ids` |
| `validate_normalized_cadastre_parcels` | `landscout.common.cadastre_contract.validate_normalized_cadastre_parcels` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels["area_m2"].notna` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels["area_m2"].between` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels.loc[candidate_mask].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels.loc[~candidate_mask].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `rejected["area_m2"].notna` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `candidates["parcel_id"].duplicated().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `candidates["parcel_id"].duplicated` | `unresolved local/third-party receiver; no ownership inferred` |
| `rejected["parcel_id"].duplicated().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `rejected["parcel_id"].duplicated` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `rejected["rejection_reason"] = "AREA_UNKNOWN"`<br>`rejected.loc[~rejected_valid_geometry, "rejection_reason"] = "INVALID_GEOMETRY"`<br>`rejected.loc[<br>        rejected_valid_geometry<br>        & rejected_known_area<br>        & (rejected["area_m2"] < validated_config.min_area_m2),<br>        "rejection_reason",<br>    ] = "AREA_BELOW_MIN"`<br>`rejected.loc[<br>        rejected_valid_geometry<br>        & rejected_known_area<br>        & (rejected["area_m2"] > validated_config.max_area_m2),<br>        "rejection_reason",<br>    ] = "AREA_ABOVE_MAX"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def filter_parcels_by_area(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> tuple[gpd.GeoDataFrame, gpd.GeoDataFrame]:
    try:
        if type(area_config) is not ParcelConfig:
            raise TypeError("Area filter config type is invalid")
        validated_config = ParcelConfig.model_validate(
            area_config.model_dump(mode="python")
        )
    except (AttributeError, TypeError, ValidationError, ValueError) as error:
        raise ParcelFilterError("Area filter config is invalid") from error
    if "rejection_reason" in getattr(parcels, "columns", ()):
        raise ParcelFilterError(
            "Area-filter input collides with generated rejection_reason"
        )
    missing_columns = _missing_columns(parcels, AREA_REQUIRED_COLUMNS, "Area-filter")
    if missing_columns:
        formatted = ", ".join(sorted(missing_columns))
        raise ParcelFilterError(f"Missing required normalized columns: {formatted}")
    parcels = _validate_spatial_frame(parcels, "Area-filter")
    _validate_exact_parcel_ids(parcels)
    try:
        validate_normalized_cadastre_parcels(parcels)
    except ValueError as error:
        raise ParcelFilterError(str(error)) from error

    valid_geometry = parcels["geometry_status"] == "VALID"

    known_area = parcels["area_m2"].notna()
    within_area_range = parcels["area_m2"].between(
        validated_config.min_area_m2,
        validated_config.max_area_m2,
        inclusive="both",
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
        & (rejected["area_m2"] < validated_config.min_area_m2),
        "rejection_reason",
    ] = "AREA_BELOW_MIN"
    rejected.loc[
        rejected_valid_geometry
        & rejected_known_area
        & (rejected["area_m2"] > validated_config.max_area_m2),
        "rejection_reason",
    ] = "AREA_ABOVE_MAX"

    if len(parcels) != len(candidates) + len(rejected):
        raise ParcelFilterError("Parcel partition did not preserve every input row")
    input_ids = set(parcels["parcel_id"])
    candidate_ids = set(candidates["parcel_id"])
    rejected_ids = set(rejected["parcel_id"])
    if (
        candidates["parcel_id"].duplicated().any()
        or rejected["parcel_id"].duplicated().any()
    ):
        raise ParcelFilterError("Parcel partition contains duplicate parcel IDs")
    if candidate_ids & rejected_ids:
        raise ParcelFilterError("Candidate and rejected parcel IDs overlap")
    if candidate_ids | rejected_ids != input_ids:
        raise ParcelFilterError("Parcel partition did not preserve exact parcel IDs")
    return candidates, rejected
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_shape_filter_input`

**Purpose:** Implements `validate shape filter input` within the file role: Applies configured factual parcel-area bounds and records explicit keep/reject facts without ranking.

**Exact signature**

```python
def _validate_shape_filter_input(parcels: gpd.GeoDataFrame) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `ParcelFilterError(f"Missing required shape columns: {formatted}")` under lexical guard `missing_columns`.
  - `ParcelFilterError(str(error))`.
  - `ParcelFilterError(f"Unexpected shape_status value(s): {detail}")` under lexical guard `statuses.isna().any() or unexpected_statuses`.
  - `ParcelFilterError(<br>            "VALID shape rows must have complete width_m and length_width_ratio metrics"<br>        )` under lexical guard `parcels.loc[valid_rows, ["width_m", "length_width_ratio"]].isna().any().any()`.
  - `ParcelFilterError(<br>                f"{column} must be numeric and finite when shape_status is VALID"<br>            )` under lexical guard `any(<br>            not _is_strict_finite_number(value)<br>            for value in parcels.loc[valid_rows, column]<br>        )`.
  - `ParcelFilterError(<br>            "width_m must be greater than zero when shape_status is VALID"<br>        )` under lexical guard `any(float(value) <= 0 for value in valid_width)`.
  - `ParcelFilterError(<br>            "length_width_ratio must be at least one when shape_status is VALID"<br>        )` under lexical guard `any(float(value) < 1 for value in valid_ratio)`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.filter_parcels::filter_parcels_by_shape` via `_validate_shape_filter_input`
- value/type reference: `landscout.stages.filter_parcels::filter_parcels_by_shape` via `_validate_shape_filter_input`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_missing_columns` | `landscout.stages.filter_parcels._missing_columns` |
| `", ".join` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `ParcelFilterError` | `landscout.stages.filter_parcels.ParcelFilterError` |
| `_validate_spatial_frame` | `landscout.stages.filter_parcels._validate_spatial_frame` |
| `validate_normalized_cadastre_parcels` | `landscout.common.cadastre_contract.validate_normalized_cadastre_parcels` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `statuses.dropna().unique` | `unresolved local/third-party receiver; no ownership inferred` |
| `statuses.dropna` | `unresolved local/third-party receiver; no ownership inferred` |
| `statuses.isna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `statuses.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels.loc[valid_rows, ["width_m", "length_width_ratio"]].isna().any().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels.loc[valid_rows, ["width_m", "length_width_ratio"]].isna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels.loc[valid_rows, ["width_m", "length_width_ratio"]].isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `_is_strict_finite_number` | `landscout.stages.filter_parcels._is_strict_finite_number` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _validate_shape_filter_input(parcels: gpd.GeoDataFrame) -> None:
    missing_columns = _missing_columns(parcels, SHAPE_REQUIRED_COLUMNS, "Shape-filter")
    if missing_columns:
        formatted = ", ".join(sorted(missing_columns))
        raise ParcelFilterError(f"Missing required shape columns: {formatted}")
    parcels = _validate_spatial_frame(parcels, "Shape-filter")
    try:
        validate_normalized_cadastre_parcels(parcels)
    except ValueError as error:
        raise ParcelFilterError(str(error)) from error

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_shape_partition`

**Purpose:** Implements `validate shape partition` within the file role: Applies configured factual parcel-area bounds and records explicit keep/reject facts without ranking.

**Exact signature**

```python
def _validate_shape_partition(
    parcels: gpd.GeoDataFrame,
    retained: gpd.GeoDataFrame,
    rejected: gpd.GeoDataFrame,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `retained` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `rejected` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `ParcelFilterError("Shape partition did not preserve every input row")` under lexical guard `len(parcels) != len(retained) + len(rejected)`.
  - `ParcelFilterError("Shape partition contains duplicate parcel IDs")` under lexical guard `retained["parcel_id"].duplicated().any()<br>        or rejected["parcel_id"].duplicated().any()`.
  - `ParcelFilterError("Retained and rejected parcel IDs overlap")` under lexical guard `retained_ids & rejected_ids`.
  - `ParcelFilterError("Shape partition did not preserve exact parcel IDs")` under lexical guard `retained_ids \| rejected_ids != input_ids`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.filter_parcels::filter_parcels_by_shape` via `_validate_shape_partition`
- value/type reference: `landscout.stages.filter_parcels::filter_parcels_by_shape` via `_validate_shape_partition`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `ParcelFilterError` | `landscout.stages.filter_parcels.ParcelFilterError` |
| `retained["parcel_id"].duplicated().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `retained["parcel_id"].duplicated` | `unresolved local/third-party receiver; no ownership inferred` |
| `rejected["parcel_id"].duplicated().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `rejected["parcel_id"].duplicated` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _validate_shape_partition(
    parcels: gpd.GeoDataFrame,
    retained: gpd.GeoDataFrame,
    rejected: gpd.GeoDataFrame,
) -> None:
    if len(parcels) != len(retained) + len(rejected):
        raise ParcelFilterError("Shape partition did not preserve every input row")
    if (
        retained["parcel_id"].duplicated().any()
        or rejected["parcel_id"].duplicated().any()
    ):
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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `filter_parcels_by_shape`

**Purpose:** Partition shape-enriched parcels using an explicit screening policy.

**Exact signature**

```python
def filter_parcels_by_shape(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> tuple[gpd.GeoDataFrame, gpd.GeoDataFrame]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[gpd.GeoDataFrame, gpd.GeoDataFrame]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `shape_config` | positional-or-keyword | `ShapeScreeningConfig` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `retained, rejected`
- Explicit raise paths:
  - `TypeError("Shape filter config type is invalid")` under lexical guard `type(shape_config) is not ShapeScreeningConfig`.
  - `ParcelFilterError("Shape filter config is invalid")`.
  - `ParcelFilterError(<br>            "Shape-filter input collides with generated columns: "<br>            + ", ".join(sorted(collisions))<br>        )` under lexical guard `collisions`.
  - `ParcelFilterError("Enabled shape screening policy is incomplete")` under lexical guard `min_width_m is None or max_ratio is None or calibration is None`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.stages::<module>` via `from landscout.stages.filter_parcels import (
    ParcelFilterError,
    filter_parcels_by_area,
    filter_parcels_by_shape,
)`
- import: `tests.unit.test_filter_shape::<module>` via `from landscout.stages.filter_parcels import (
    ParcelFilterError,
    filter_parcels_by_shape,
)`
- direct call: `tests.unit.test_filter_shape::test_exact_width_and_ratio_boundaries_are_retained` via `filter_parcels_by_shape`
- value/type reference: `tests.unit.test_filter_shape::test_exact_width_and_ratio_boundaries_are_retained` via `filter_parcels_by_shape`
- direct call: `tests.unit.test_filter_shape::test_shape_filter_revalidates_mutated_config_before_frame_work` via `filter_parcels_by_shape`
- value/type reference: `tests.unit.test_filter_shape::test_shape_filter_revalidates_mutated_config_before_frame_work` via `filter_parcels_by_shape`
- direct call: `tests.unit.test_filter_shape::test_rejected_parcel_has_expected_primary_reason` via `filter_parcels_by_shape`
- value/type reference: `tests.unit.test_filter_shape::test_rejected_parcel_has_expected_primary_reason` via `filter_parcels_by_shape`
- direct call: `tests.unit.test_filter_shape::test_rejection_reason_precedence_is_deterministic` via `filter_parcels_by_shape`
- value/type reference: `tests.unit.test_filter_shape::test_rejection_reason_precedence_is_deterministic` via `filter_parcels_by_shape`
- direct call: `tests.unit.test_filter_shape::test_shape_error_precedence_does_not_inspect_metrics` via `filter_parcels_by_shape`
- value/type reference: `tests.unit.test_filter_shape::test_shape_error_precedence_does_not_inspect_metrics` via `filter_parcels_by_shape`
- direct call: `tests.unit.test_filter_shape::test_enabled_outputs_record_active_policy_metadata` via `filter_parcels_by_shape`
- value/type reference: `tests.unit.test_filter_shape::test_enabled_outputs_record_active_policy_metadata` via `filter_parcels_by_shape`
- direct call: `tests.unit.test_filter_shape::test_enabled_partition_preserves_exact_ids_and_crs` via `filter_parcels_by_shape`
- value/type reference: `tests.unit.test_filter_shape::test_enabled_partition_preserves_exact_ids_and_crs` via `filter_parcels_by_shape`
- direct call: `tests.unit.test_filter_shape::test_filter_does_not_mutate_input` via `filter_parcels_by_shape`
- value/type reference: `tests.unit.test_filter_shape::test_filter_does_not_mutate_input` via `filter_parcels_by_shape`
- direct call: `tests.unit.test_filter_shape::test_missing_required_column_fails` via `filter_parcels_by_shape`
- value/type reference: `tests.unit.test_filter_shape::test_missing_required_column_fails` via `filter_parcels_by_shape`
- direct call: `tests.unit.test_filter_shape::test_null_parcel_id_fails` via `filter_parcels_by_shape`
- value/type reference: `tests.unit.test_filter_shape::test_null_parcel_id_fails` via `filter_parcels_by_shape`
- direct call: `tests.unit.test_filter_shape::test_duplicate_parcel_id_fails` via `filter_parcels_by_shape`
- value/type reference: `tests.unit.test_filter_shape::test_duplicate_parcel_id_fails` via `filter_parcels_by_shape`
- direct call: `tests.unit.test_filter_shape::test_unknown_crs_fails` via `filter_parcels_by_shape`
- value/type reference: `tests.unit.test_filter_shape::test_unknown_crs_fails` via `filter_parcels_by_shape`
- direct call: `tests.unit.test_filter_shape::test_unexpected_or_null_shape_status_fails` via `filter_parcels_by_shape`
- value/type reference: `tests.unit.test_filter_shape::test_unexpected_or_null_shape_status_fails` via `filter_parcels_by_shape`
- direct call: `tests.unit.test_filter_shape::test_non_finite_known_metric_on_valid_row_fails` via `filter_parcels_by_shape`
- value/type reference: `tests.unit.test_filter_shape::test_non_finite_known_metric_on_valid_row_fails` via `filter_parcels_by_shape`
- direct call: `tests.unit.test_filter_shape::test_valid_shape_requires_strict_positive_width` via `filter_parcels_by_shape`
- value/type reference: `tests.unit.test_filter_shape::test_valid_shape_requires_strict_positive_width` via `filter_parcels_by_shape`
- direct call: `tests.unit.test_filter_shape::test_valid_shape_requires_ratio_at_least_one` via `filter_parcels_by_shape`
- value/type reference: `tests.unit.test_filter_shape::test_valid_shape_requires_ratio_at_least_one` via `filter_parcels_by_shape`
- direct call: `tests.unit.test_filter_shape::test_negative_ratio_cannot_pass_permissive_thresholds` via `filter_parcels_by_shape`
- value/type reference: `tests.unit.test_filter_shape::test_negative_ratio_cannot_pass_permissive_thresholds` via `filter_parcels_by_shape`
- direct call: `tests.unit.test_filter_shape::test_disabled_policy_is_an_exact_passthrough` via `filter_parcels_by_shape`
- value/type reference: `tests.unit.test_filter_shape::test_disabled_policy_is_an_exact_passthrough` via `filter_parcels_by_shape`
- direct call: `tests.unit.test_filter_shape::test_different_configs_change_results_for_same_parcels` via `filter_parcels_by_shape`
- value/type reference: `tests.unit.test_filter_shape::test_different_configs_change_results_for_same_parcels` via `filter_parcels_by_shape`
- direct call: `tests.unit.test_filter_shape::test_valid_shape_requires_complete_metrics_even_when_screening_disabled` via `filter_parcels_by_shape`
- value/type reference: `tests.unit.test_filter_shape::test_valid_shape_requires_complete_metrics_even_when_screening_disabled` via `filter_parcels_by_shape`
- direct call: `tests.unit.test_filter_shape::test_valid_shape_rejects_every_incomplete_metric_form` via `filter_parcels_by_shape`
- value/type reference: `tests.unit.test_filter_shape::test_valid_shape_rejects_every_incomplete_metric_form` via `filter_parcels_by_shape`
- direct call: `tests.unit.test_filter_shape::test_shape_filter_rejects_plain_dataframe` via `filter_parcels_by_shape`
- value/type reference: `tests.unit.test_filter_shape::test_shape_filter_rejects_plain_dataframe` via `filter_parcels_by_shape`
- direct call: `tests.unit.test_filter_shape::test_shape_filter_rejects_duplicate_columns` via `filter_parcels_by_shape`
- value/type reference: `tests.unit.test_filter_shape::test_shape_filter_rejects_duplicate_columns` via `filter_parcels_by_shape`
- direct call: `tests.unit.test_filter_shape::test_shape_filter_rejects_unreadable_crs` via `filter_parcels_by_shape`
- value/type reference: `tests.unit.test_filter_shape::test_shape_filter_rejects_unreadable_crs` via `filter_parcels_by_shape`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `TypeError` | `unresolved local/third-party receiver; no ownership inferred` |
| `ShapeScreeningConfig.model_validate` | `landscout.config.ShapeScreeningConfig.model_validate` |
| `shape_config.model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `ParcelFilterError` | `landscout.stages.filter_parcels.ParcelFilterError` |
| `_validate_shape_filter_input` | `landscout.stages.filter_parcels._validate_shape_filter_input` |
| `parcels.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels.iloc[0:0].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validate_shape_partition` | `landscout.stages.filter_parcels._validate_shape_partition` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `", ".join` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels["width_m"].where` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels["length_width_ratio"].where` | `unresolved local/third-party receiver; no ownership inferred` |
| `screening_width.notna` | `unresolved local/third-party receiver; no ownership inferred` |
| `screening_ratio.notna` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels.loc[retained_mask].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels.loc[~retained_mask].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `rejected["width_m"].where` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `rejected["shape_rejection_reason"] = "RATIO_ABOVE_MAX"`<br>`rejected.loc[<br>        rejected_valid & (rejected_width < min_width_m),<br>        "shape_rejection_reason",<br>    ] = "WIDTH_BELOW_MIN"`<br>`rejected.loc[~rejected_valid, "shape_rejection_reason"] = "SHAPE_ERROR"`<br>`output["shape_policy_version"] = calibration.policy_version`<br>`output["shape_policy_min_width_m"] = min_width_m`<br>`output["shape_policy_max_ratio"] = max_ratio` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def filter_parcels_by_shape(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> tuple[gpd.GeoDataFrame, gpd.GeoDataFrame]:
    """Partition shape-enriched parcels using an explicit screening policy."""
    try:
        if type(shape_config) is not ShapeScreeningConfig:
            raise TypeError("Shape filter config type is invalid")
        validated_config = ShapeScreeningConfig.model_validate(
            shape_config.model_dump(mode="python")
        )
    except (AttributeError, TypeError, ValidationError, ValueError) as error:
        raise ParcelFilterError("Shape filter config is invalid") from error
    _validate_shape_filter_input(parcels)

    if not validated_config.enabled:
        retained = parcels.copy()
        rejected = parcels.iloc[0:0].copy()
        _validate_shape_partition(parcels, retained, rejected)
        return retained, rejected

    generated_columns = {
        "shape_rejection_reason",
        "shape_policy_version",
        "shape_policy_min_width_m",
        "shape_policy_max_ratio",
    }
    collisions = generated_columns & set(parcels.columns)
    if collisions:
        raise ParcelFilterError(
            "Shape-filter input collides with generated columns: "
            + ", ".join(sorted(collisions))
        )

    min_width_m = validated_config.min_width_m
    max_ratio = validated_config.max_length_width_ratio
    calibration = validated_config.calibration
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
        rejected_valid & (rejected_width < min_width_m),
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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.


## 7. Validation and data-contract summary

- Canonical schema/mapping declarations inventoried above: `AREA_REQUIRED_COLUMNS`, `SHAPE_REQUIRED_COLUMNS`.
- Exact value/null/index/CRS/geometry/hash behavior is claimed only where the reproduced validators and operations enforce it.

## 8. Public exports and package ownership

This module declares no `__all__`; no package-level public guarantee is inferred from direct importability alone.

## 9. Trust, provenance, side effects, and business boundary

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.
- Configured identity, textual lineage, byte identity, physical source reconstruction, local envelope validation, and source-complete validation remain distinct trust levels. This companion attributes only the levels implemented in the exact source.
- Filesystem, network, hashing, CRS/geometry, process, mutation, and expected-exception evidence is listed per callable; an empty category is not silently promoted to an effect.

## 10. Change impact

A source-byte change invalidates the SHA above and requires re-auditing imports/re-exports, constants/aliases/schemas, model fields/immutability, qualified callers, side effects, controlled errors, tests, source/artifact locks, and the exact full snapshot.

## 11. Exact complete current file content

The following UTF-8 snapshot is the complete current repository file, not an excerpt. Its raw-byte SHA256 is the value in **File identity**.

```python
from math import isfinite
from numbers import Real

import geopandas as gpd  # type: ignore[import-untyped]
from pydantic import ValidationError
from pyproj import CRS

from landscout.common.cadastre_contract import validate_normalized_cadastre_parcels
from landscout.config import ParcelConfig, ShapeScreeningConfig

AREA_REQUIRED_COLUMNS = frozenset(
    {"parcel_id", "geometry_status", "area_m2", "geometry"}
)
SHAPE_REQUIRED_COLUMNS = frozenset(
    {"parcel_id", "shape_status", "width_m", "length_width_ratio", "geometry"}
)
ALLOWED_SHAPE_STATUSES = frozenset({"VALID", "ERROR"})


class ParcelFilterError(ValueError):
    """Raised when normalized parcels cannot be partitioned safely."""


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


def _missing_columns(
    parcels: object,
    required: frozenset[str],
    label: str,
) -> frozenset[str]:
    try:
        return required - set(parcels.columns)  # type: ignore[attr-defined]
    except Exception as error:
        raise ParcelFilterError(f"{label} input must be a GeoDataFrame") from error


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


def _is_strict_finite_number(value: object) -> bool:
    return (
        isinstance(value, Real)
        and not isinstance(value, bool)
        and isfinite(float(value))
    )


def filter_parcels_by_area(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> tuple[gpd.GeoDataFrame, gpd.GeoDataFrame]:
    try:
        if type(area_config) is not ParcelConfig:
            raise TypeError("Area filter config type is invalid")
        validated_config = ParcelConfig.model_validate(
            area_config.model_dump(mode="python")
        )
    except (AttributeError, TypeError, ValidationError, ValueError) as error:
        raise ParcelFilterError("Area filter config is invalid") from error
    if "rejection_reason" in getattr(parcels, "columns", ()):
        raise ParcelFilterError(
            "Area-filter input collides with generated rejection_reason"
        )
    missing_columns = _missing_columns(parcels, AREA_REQUIRED_COLUMNS, "Area-filter")
    if missing_columns:
        formatted = ", ".join(sorted(missing_columns))
        raise ParcelFilterError(f"Missing required normalized columns: {formatted}")
    parcels = _validate_spatial_frame(parcels, "Area-filter")
    _validate_exact_parcel_ids(parcels)
    try:
        validate_normalized_cadastre_parcels(parcels)
    except ValueError as error:
        raise ParcelFilterError(str(error)) from error

    valid_geometry = parcels["geometry_status"] == "VALID"

    known_area = parcels["area_m2"].notna()
    within_area_range = parcels["area_m2"].between(
        validated_config.min_area_m2,
        validated_config.max_area_m2,
        inclusive="both",
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
        & (rejected["area_m2"] < validated_config.min_area_m2),
        "rejection_reason",
    ] = "AREA_BELOW_MIN"
    rejected.loc[
        rejected_valid_geometry
        & rejected_known_area
        & (rejected["area_m2"] > validated_config.max_area_m2),
        "rejection_reason",
    ] = "AREA_ABOVE_MAX"

    if len(parcels) != len(candidates) + len(rejected):
        raise ParcelFilterError("Parcel partition did not preserve every input row")
    input_ids = set(parcels["parcel_id"])
    candidate_ids = set(candidates["parcel_id"])
    rejected_ids = set(rejected["parcel_id"])
    if (
        candidates["parcel_id"].duplicated().any()
        or rejected["parcel_id"].duplicated().any()
    ):
        raise ParcelFilterError("Parcel partition contains duplicate parcel IDs")
    if candidate_ids & rejected_ids:
        raise ParcelFilterError("Candidate and rejected parcel IDs overlap")
    if candidate_ids | rejected_ids != input_ids:
        raise ParcelFilterError("Parcel partition did not preserve exact parcel IDs")
    return candidates, rejected


def _validate_shape_filter_input(parcels: gpd.GeoDataFrame) -> None:
    missing_columns = _missing_columns(parcels, SHAPE_REQUIRED_COLUMNS, "Shape-filter")
    if missing_columns:
        formatted = ", ".join(sorted(missing_columns))
        raise ParcelFilterError(f"Missing required shape columns: {formatted}")
    parcels = _validate_spatial_frame(parcels, "Shape-filter")
    try:
        validate_normalized_cadastre_parcels(parcels)
    except ValueError as error:
        raise ParcelFilterError(str(error)) from error

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


def _validate_shape_partition(
    parcels: gpd.GeoDataFrame,
    retained: gpd.GeoDataFrame,
    rejected: gpd.GeoDataFrame,
) -> None:
    if len(parcels) != len(retained) + len(rejected):
        raise ParcelFilterError("Shape partition did not preserve every input row")
    if (
        retained["parcel_id"].duplicated().any()
        or rejected["parcel_id"].duplicated().any()
    ):
        raise ParcelFilterError("Shape partition contains duplicate parcel IDs")

    input_ids = set(parcels["parcel_id"])
    retained_ids = set(retained["parcel_id"])
    rejected_ids = set(rejected["parcel_id"])
    if retained_ids & rejected_ids:
        raise ParcelFilterError("Retained and rejected parcel IDs overlap")
    if retained_ids | rejected_ids != input_ids:
        raise ParcelFilterError("Shape partition did not preserve exact parcel IDs")


def filter_parcels_by_shape(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> tuple[gpd.GeoDataFrame, gpd.GeoDataFrame]:
    """Partition shape-enriched parcels using an explicit screening policy."""
    try:
        if type(shape_config) is not ShapeScreeningConfig:
            raise TypeError("Shape filter config type is invalid")
        validated_config = ShapeScreeningConfig.model_validate(
            shape_config.model_dump(mode="python")
        )
    except (AttributeError, TypeError, ValidationError, ValueError) as error:
        raise ParcelFilterError("Shape filter config is invalid") from error
    _validate_shape_filter_input(parcels)

    if not validated_config.enabled:
        retained = parcels.copy()
        rejected = parcels.iloc[0:0].copy()
        _validate_shape_partition(parcels, retained, rejected)
        return retained, rejected

    generated_columns = {
        "shape_rejection_reason",
        "shape_policy_version",
        "shape_policy_min_width_m",
        "shape_policy_max_ratio",
    }
    collisions = generated_columns & set(parcels.columns)
    if collisions:
        raise ParcelFilterError(
            "Shape-filter input collides with generated columns: "
            + ", ".join(sorted(collisions))
        )

    min_width_m = validated_config.min_width_m
    max_ratio = validated_config.max_length_width_ratio
    calibration = validated_config.calibration
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
        rejected_valid & (rejected_width < min_width_m),
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

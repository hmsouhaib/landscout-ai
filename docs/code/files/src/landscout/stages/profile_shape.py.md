# `src/landscout/stages/profile_shape.py`

## File identity

- Repository path: `src/landscout/stages/profile_shape.py`
- File type: Python source
- Layer: pipeline stage
- Domain: factual transformation, evidence, or policy boundary
- Responsibility: Profiles shape metrics and scenario evidence without making parcel suitability decisions.
- Source SHA256: `bafac8d1b9c67c338bdf2937d1717bd7f64c1723668a6dfb325fb41d532deeb8`

## 1. STEP 7F.1A.4 contract delta

- Revalidates shape configuration and canonical parcel facts before producing scenario diagnostics.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Profiles shape metrics and scenario evidence without making parcel suitability decisions.

The file belongs to the **pipeline stage** layer and **factual transformation, evidence, or policy boundary** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from dataclasses import dataclass`
- `from math import isclose, isfinite`
- `from numbers import Real`

### Third-party packages

- `import geopandas as gpd`
- `from pyproj import CRS`

### Internal LandScout imports

- `from landscout.common.cadastre_contract import validate_normalized_cadastre_parcels`

## 4. Contract taxonomy

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `PROFILE_METRICS`

- Category: module constant or closed domain.
- Exact declaration:

```python
PROFILE_METRICS = (
    "area_m2",
    "length_m",
    "width_m",
    "length_width_ratio",
    "compactness",
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `area_m2`
  - `length_m`
  - `width_m`
  - `length_width_ratio`
  - `compactness`

### `REPRESENTATIVE_FIELDS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
REPRESENTATIVE_FIELDS = (
    "parcel_id",
    "area_m2",
    "length_m",
    "width_m",
    "length_width_ratio",
    "compactness",
    "centroid_lat",
    "centroid_lon",
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `parcel_id`
  - `area_m2`
  - `length_m`
  - `width_m`
  - `length_width_ratio`
  - `compactness`
  - `centroid_lat`
  - `centroid_lon`

### `REQUIRED_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
REQUIRED_COLUMNS = frozenset({"parcel_id", "shape_status", *REPRESENTATIVE_FIELDS})
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `PERCENTILES`

- Category: module constant or closed domain.
- Exact declaration:

```python
PERCENTILES = {
    "min": 0.0,
    "p01": 0.01,
    "p05": 0.05,
    "p10": 0.10,
    "p25": 0.25,
    "p50": 0.50,
    "p75": 0.75,
    "p90": 0.90,
    "p95": 0.95,
    "p99": 0.99,
    "max": 1.0,
}
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact mapping keys:
  - `min`
  - `p01`
  - `p05`
  - `p10`
  - `p25`
  - `p50`
  - `p75`
  - `p90`
  - `p95`
  - `p99`
  - `max`


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

### `ShapeProfileError`

**Source purpose:** Raised when shape candidates cannot be profiled safely.

- Exact decorators: none.
- Exact bases: `ValueError`.

**Fields and model attributes**

No direct class/model/dataclass or `self` field assignment is declared.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.profile_shape import (
    ShapeDistributionProfile,
    ShapeProfileError,
    profile_shape_distribution,
)`
- constructor call: `landscout.stages.profile_shape::profile_shape_distribution` via `ShapeProfileError`
- value/type reference: `landscout.stages.profile_shape::profile_shape_distribution` via `ShapeProfileError`
- import: `tests.unit.test_profile_shape::<module>` via `from landscout.stages.profile_shape import (
    ShapeProfileError,
    profile_shape_distribution,
)`
- value/type reference: `tests.unit.test_profile_shape::test_missing_metric_fails` via `ShapeProfileError`
- value/type reference: `tests.unit.test_profile_shape::test_null_parcel_id_fails` via `ShapeProfileError`
- value/type reference: `tests.unit.test_profile_shape::test_duplicate_parcel_id_fails` via `ShapeProfileError`
- value/type reference: `tests.unit.test_profile_shape::test_missing_crs_fails` via `ShapeProfileError`
- value/type reference: `tests.unit.test_profile_shape::test_null_metric_on_valid_shape_fails` via `ShapeProfileError`
- value/type reference: `tests.unit.test_profile_shape::test_unexpected_shape_status_fails` via `ShapeProfileError`
- value/type reference: `tests.unit.test_profile_shape::test_non_finite_metric_on_valid_row_fails` via `ShapeProfileError`
- value/type reference: `tests.unit.test_profile_shape::test_zero_valid_rows_fails_clearly` via `ShapeProfileError`
- value/type reference: `tests.unit.test_profile_shape::test_valid_shape_metrics_require_physical_domains` via `ShapeProfileError`
- value/type reference: `tests.unit.test_profile_shape::test_valid_shape_length_must_not_be_less_than_width` via `ShapeProfileError`
- value/type reference: `tests.unit.test_profile_shape::test_valid_shape_ratio_must_match_length_divided_by_width` via `ShapeProfileError`
- value/type reference: `tests.unit.test_profile_shape::test_valid_shape_metrics_reject_bool_and_numeric_strings` via `ShapeProfileError`

**Exact class source**

```python
class ShapeProfileError(ValueError):
    """Raised when shape candidates cannot be profiled safely."""
```

### `DiagnosticScenario`

**Source purpose:** Defines `DiagnosticScenario`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `retained_count` | `int` | `required` | `retained_count: int` |
| `retained_percentage` | `float` | `required` | `retained_percentage: float` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- constructor call: `landscout.stages.profile_shape::profile_shape_distribution` via `DiagnosticScenario`
- value/type reference: `landscout.stages.profile_shape::profile_shape_distribution` via `DiagnosticScenario`

**Exact class source**

```python
class DiagnosticScenario:
    retained_count: int
    retained_percentage: float
```

### `ShapeDistributionProfile`

**Source purpose:** Defines `ShapeDistributionProfile`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `input_count` | `int` | `required` | `input_count: int` |
| `valid_count` | `int` | `required` | `valid_count: int` |
| `error_count` | `int` | `required` | `error_count: int` |
| `distributions` | `dict[str, dict[str, float]]` | `required` | `distributions: dict[str, dict[str, float]]` |
| `width_buckets` | `dict[str, int]` | `required` | `width_buckets: dict[str, int]` |
| `ratio_buckets` | `dict[str, int]` | `required` | `ratio_buckets: dict[str, int]` |
| `compactness_buckets` | `dict[str, int]` | `required` | `compactness_buckets: dict[str, int]` |
| `scenarios` | `dict[str, DiagnosticScenario]` | `required` | `scenarios: dict[str, DiagnosticScenario]` |
| `median_parcels` | `list[dict[str, object]]` | `required` | `median_parcels: list[dict[str, object]]` |
| `extreme_parcels` | `list[dict[str, object]]` | `required` | `extreme_parcels: list[dict[str, object]]` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.profile_shape import (
    ShapeDistributionProfile,
    ShapeProfileError,
    profile_shape_distribution,
)`
- constructor call: `landscout.stages.profile_shape::profile_shape_distribution` via `ShapeDistributionProfile`
- value/type reference: `landscout.stages.profile_shape::profile_shape_distribution` via `ShapeDistributionProfile`

**Exact class source**

```python
class ShapeDistributionProfile:
    input_count: int
    valid_count: int
    error_count: int
    distributions: dict[str, dict[str, float]]
    width_buckets: dict[str, int]
    ratio_buckets: dict[str, int]
    compactness_buckets: dict[str, int]
    scenarios: dict[str, DiagnosticScenario]
    median_parcels: list[dict[str, object]]
    extreme_parcels: list[dict[str, object]]
```


## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `_records`

**Purpose:** Implements `records` within the file role: Profiles shape metrics and scenario evidence without making parcel suitability decisions.

**Exact signature**

```python
def _records(frame: gpd.GeoDataFrame) -> list[dict[str, object]]:
```

- Exact decorators: none.
- Declared return annotation: `list[dict[str, object]]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `frame[list(REPRESENTATIVE_FIELDS)].to_dict(orient="records")`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.profile_shape::profile_shape_distribution` via `_records`
- value/type reference: `landscout.stages.profile_shape::profile_shape_distribution` via `_records`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `frame[list(REPRESENTATIVE_FIELDS)].to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _records(frame: gpd.GeoDataFrame) -> list[dict[str, object]]:
    return frame[list(REPRESENTATIVE_FIELDS)].to_dict(orient="records")
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `profile_shape_distribution`

**Purpose:** Implements `profile shape distribution` within the file role: Profiles shape metrics and scenario evidence without making parcel suitability decisions.

**Exact signature**

```python
def profile_shape_distribution(
    parcels: gpd.GeoDataFrame,
) -> ShapeDistributionProfile:
```

- Exact decorators: none.
- Declared return annotation: `ShapeDistributionProfile`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `ShapeDistributionProfile(<br>        input_count=input_count,<br>        valid_count=valid_count,<br>        error_count=error_count,<br>        distributions=distributions,<br>        width_buckets=width_buckets,<br>        ratio_buckets=ratio_buckets,<br>        compactness_buckets=compactness_buckets,<br>        scenarios=scenarios,<br>        median_parcels=_records(median_frame),<br>        extreme_parcels=_records(extreme_frame),<br>    )`
- Explicit raise paths:
  - `ShapeProfileError(str(error))`.
  - `ShapeProfileError(f"Missing required shape columns: {formatted}")` under lexical guard `missing_columns`.
  - `ShapeProfileError("Shape candidate CRS is required")` under lexical guard `parcels.crs is None`.
  - `ShapeProfileError("Shape candidate CRS must be readable")`.
  - `ShapeProfileError("parcel_id values must not be null")` under lexical guard `identifiers.isna().any()`.
  - `ShapeProfileError("parcel_id values must be exact non-empty strings")` under lexical guard `any(<br>        not isinstance(identifier, str)<br>        or not identifier<br>        or identifier != identifier.strip()<br>        for identifier in identifiers<br>    )`.
  - `ShapeProfileError("parcel_id values must be unique")` under lexical guard `identifiers.duplicated().any()`.
  - `ShapeProfileError(f"Unexpected shape_status values: {formatted}")` under lexical guard `parcels["shape_status"].isna().any() or not statuses <= {"VALID", "ERROR"}`.
  - `ShapeProfileError("Shape status counts do not match input count")` under lexical guard `input_count != valid_count + error_count`.
  - `ShapeProfileError("At least one VALID shape row is required")` under lexical guard `valid_count == 0`.
  - `ShapeProfileError("VALID shape rows must have complete shape metrics")` under lexical guard `parcels.loc[valid_shapes, required_valid_metrics].isna().any().any()`.
  - `ShapeProfileError(<br>                f"VALID shape metric must be numeric and finite: {column}"<br>            )` under lexical guard `not values_are_finite`.
  - `ShapeProfileError(message)` under lexical guard `not bool(condition.all())`.
  - `ShapeProfileError("length_m must be at least width_m")` under lexical guard `not bool((valid["length_m"] >= valid["width_m"]).all())`.
  - `ShapeProfileError(<br>                "length_width_ratio must equal length_m / width_m within tolerance"<br>            )` under lexical guard `not isclose(<br>            float(row.length_width_ratio),<br>            expected_ratio,<br>            rel_tol=1e-9,<br>            abs_tol=1e-9,<br>        )`.
  - `ShapeProfileError("Width buckets do not cover every VALID row")` under lexical guard `sum(width_buckets.values()) != valid_count`.
  - `ShapeProfileError("Ratio buckets do not cover every VALID row")` under lexical guard `sum(ratio_buckets.values()) != valid_count`.
  - `ShapeProfileError("Compactness buckets do not cover every VALID row")` under lexical guard `sum(compactness_buckets.values()) != valid_count`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.stages::<module>` via `from landscout.stages.profile_shape import (
    ShapeDistributionProfile,
    ShapeProfileError,
    profile_shape_distribution,
)`
- import: `tests.unit.test_profile_shape::<module>` via `from landscout.stages.profile_shape import (
    ShapeProfileError,
    profile_shape_distribution,
)`
- direct call: `tests.unit.test_profile_shape::test_percentile_calculation` via `profile_shape_distribution`
- value/type reference: `tests.unit.test_profile_shape::test_percentile_calculation` via `profile_shape_distribution`
- direct call: `tests.unit.test_profile_shape::test_bucket_counts_sum_to_input_count` via `profile_shape_distribution`
- value/type reference: `tests.unit.test_profile_shape::test_bucket_counts_sum_to_input_count` via `profile_shape_distribution`
- direct call: `tests.unit.test_profile_shape::test_existing_all_valid_behavior_is_unchanged` via `profile_shape_distribution`
- value/type reference: `tests.unit.test_profile_shape::test_existing_all_valid_behavior_is_unchanged` via `profile_shape_distribution`
- direct call: `tests.unit.test_profile_shape::test_diagnostic_scenario_counts` via `profile_shape_distribution`
- value/type reference: `tests.unit.test_profile_shape::test_diagnostic_scenario_counts` via `profile_shape_distribution`
- direct call: `tests.unit.test_profile_shape::test_input_is_not_mutated` via `profile_shape_distribution`
- value/type reference: `tests.unit.test_profile_shape::test_input_is_not_mutated` via `profile_shape_distribution`
- direct call: `tests.unit.test_profile_shape::test_missing_metric_fails` via `profile_shape_distribution`
- value/type reference: `tests.unit.test_profile_shape::test_missing_metric_fails` via `profile_shape_distribution`
- direct call: `tests.unit.test_profile_shape::test_null_parcel_id_fails` via `profile_shape_distribution`
- value/type reference: `tests.unit.test_profile_shape::test_null_parcel_id_fails` via `profile_shape_distribution`
- direct call: `tests.unit.test_profile_shape::test_duplicate_parcel_id_fails` via `profile_shape_distribution`
- value/type reference: `tests.unit.test_profile_shape::test_duplicate_parcel_id_fails` via `profile_shape_distribution`
- direct call: `tests.unit.test_profile_shape::test_missing_crs_fails` via `profile_shape_distribution`
- value/type reference: `tests.unit.test_profile_shape::test_missing_crs_fails` via `profile_shape_distribution`
- direct call: `tests.unit.test_profile_shape::test_null_metric_on_valid_shape_fails` via `profile_shape_distribution`
- value/type reference: `tests.unit.test_profile_shape::test_null_metric_on_valid_shape_fails` via `profile_shape_distribution`
- direct call: `tests.unit.test_profile_shape::test_mixed_valid_and_error_rows_are_counted` via `profile_shape_distribution`
- value/type reference: `tests.unit.test_profile_shape::test_mixed_valid_and_error_rows_are_counted` via `profile_shape_distribution`
- direct call: `tests.unit.test_profile_shape::test_error_rows_are_excluded_from_percentiles` via `profile_shape_distribution`
- value/type reference: `tests.unit.test_profile_shape::test_error_rows_are_excluded_from_percentiles` via `profile_shape_distribution`
- direct call: `tests.unit.test_profile_shape::test_error_rows_are_excluded_from_buckets` via `profile_shape_distribution`
- value/type reference: `tests.unit.test_profile_shape::test_error_rows_are_excluded_from_buckets` via `profile_shape_distribution`
- direct call: `tests.unit.test_profile_shape::test_scenario_percentages_use_valid_count` via `profile_shape_distribution`
- value/type reference: `tests.unit.test_profile_shape::test_scenario_percentages_use_valid_count` via `profile_shape_distribution`
- direct call: `tests.unit.test_profile_shape::test_unexpected_shape_status_fails` via `profile_shape_distribution`
- value/type reference: `tests.unit.test_profile_shape::test_unexpected_shape_status_fails` via `profile_shape_distribution`
- direct call: `tests.unit.test_profile_shape::test_non_finite_metric_on_valid_row_fails` via `profile_shape_distribution`
- value/type reference: `tests.unit.test_profile_shape::test_non_finite_metric_on_valid_row_fails` via `profile_shape_distribution`
- direct call: `tests.unit.test_profile_shape::test_zero_valid_rows_fails_clearly` via `profile_shape_distribution`
- value/type reference: `tests.unit.test_profile_shape::test_zero_valid_rows_fails_clearly` via `profile_shape_distribution`
- direct call: `tests.unit.test_profile_shape::test_valid_shape_metrics_require_physical_domains` via `profile_shape_distribution`
- value/type reference: `tests.unit.test_profile_shape::test_valid_shape_metrics_require_physical_domains` via `profile_shape_distribution`
- direct call: `tests.unit.test_profile_shape::test_valid_shape_length_must_not_be_less_than_width` via `profile_shape_distribution`
- value/type reference: `tests.unit.test_profile_shape::test_valid_shape_length_must_not_be_less_than_width` via `profile_shape_distribution`
- direct call: `tests.unit.test_profile_shape::test_valid_shape_ratio_must_match_length_divided_by_width` via `profile_shape_distribution`
- value/type reference: `tests.unit.test_profile_shape::test_valid_shape_ratio_must_match_length_divided_by_width` via `profile_shape_distribution`
- direct call: `tests.unit.test_profile_shape::test_valid_shape_metrics_reject_bool_and_numeric_strings` via `profile_shape_distribution`
- value/type reference: `tests.unit.test_profile_shape::test_valid_shape_metrics_reject_bool_and_numeric_strings` via `profile_shape_distribution`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `validate_normalized_cadastre_parcels` | `landscout.common.cadastre_contract.validate_normalized_cadastre_parcels` |
| `ShapeProfileError` | `landscout.stages.profile_shape.ShapeProfileError` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `", ".join` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `CRS.from_user_input` | `pyproj.CRS.from_user_input` |
| `identifiers.isna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `identifiers.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `identifier.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `identifiers.duplicated().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `identifiers.duplicated` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels["shape_status"].dropna().unique` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels["shape_status"].dropna` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels["shape_status"].isna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels["shape_status"].isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `int` | `unresolved local/third-party receiver; no ownership inferred` |
| `valid_shapes.sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `error_shapes.sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels.loc[valid_shapes, required_valid_metrics].isna().any().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels.loc[valid_shapes, required_valid_metrics].isna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels.loc[valid_shapes, required_valid_metrics].isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `all` | `unresolved local/third-party receiver; no ownership inferred` |
| `isfinite` | `math.isfinite` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |
| `valid["centroid_lat"].between` | `unresolved local/third-party receiver; no ownership inferred` |
| `valid["centroid_lon"].between` | `unresolved local/third-party receiver; no ownership inferred` |
| `bool` | `unresolved local/third-party receiver; no ownership inferred` |
| `condition.all` | `unresolved local/third-party receiver; no ownership inferred` |
| `(valid["length_m"] >= valid["width_m"]).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `valid.itertuples` | `unresolved local/third-party receiver; no ownership inferred` |
| `isclose` | `math.isclose` |
| `parcels.loc[valid_shapes].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `working[metric].quantile` | `unresolved local/third-party receiver; no ownership inferred` |
| `PERCENTILES.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `(width < 5).sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `((width >= 5) & (width < 10)).sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `((width >= 10) & (width < 15)).sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `((width >= 15) & (width < 20)).sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `((width >= 20) & (width < 25)).sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `((width >= 25) & (width < 30)).sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `((width >= 30) & (width < 40)).sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `((width >= 40) & (width < 50)).sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `(width >= 50).sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `(ratio <= 2).sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `((ratio > 2) & (ratio <= 3)).sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `((ratio > 3) & (ratio <= 4)).sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `((ratio > 4) & (ratio <= 5)).sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `((ratio > 5) & (ratio <= 7)).sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `((ratio > 7) & (ratio <= 10)).sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `((ratio > 10) & (ratio <= 15)).sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `((ratio > 15) & (ratio <= 25)).sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `(ratio > 25).sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `(compactness < 0.05).sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `((compactness >= 0.05) & (compactness < 0.10)).sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `((compactness >= 0.10) & (compactness < 0.20)).sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `((compactness >= 0.20) & (compactness < 0.30)).sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `((compactness >= 0.30) & (compactness < 0.40)).sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `((compactness >= 0.40) & (compactness < 0.50)).sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `((compactness >= 0.50) & (compactness < 0.60)).sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `((compactness >= 0.60) & (compactness < 0.70)).sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `(compactness >= 0.70).sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `width_buckets.values` | `unresolved local/third-party receiver; no ownership inferred` |
| `ratio_buckets.values` | `unresolved local/third-party receiver; no ownership inferred` |
| `compactness_buckets.values` | `unresolved local/third-party receiver; no ownership inferred` |
| `DiagnosticScenario` | `landscout.stages.profile_shape.DiagnosticScenario` |
| `mask.sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `scenario_masks.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `working[metric].median` | `unresolved local/third-party receiver; no ownership inferred` |
| `(working[metric] - median).abs` | `unresolved local/third-party receiver; no ownership inferred` |
| `working.nsmallest` | `unresolved local/third-party receiver; no ownership inferred` |
| `working["length_width_ratio"].rank` | `unresolved local/third-party receiver; no ownership inferred` |
| `(-working["width_m"]).rank` | `unresolved local/third-party receiver; no ownership inferred` |
| `(-working["compactness"]).rank` | `unresolved local/third-party receiver; no ownership inferred` |
| `working["parcel_id"].isin` | `unresolved local/third-party receiver; no ownership inferred` |
| `extreme_pool.nlargest` | `unresolved local/third-party receiver; no ownership inferred` |
| `ShapeDistributionProfile` | `landscout.stages.profile_shape.ShapeDistributionProfile` |
| `_records` | `landscout.stages.profile_shape._records` |

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
| In-memory mutation | `working["_median_score"] = 0.0`<br>`working["_median_score"] += (working[metric] - median).abs() / scale`<br>`working["_extreme_score"] = (<br>        working["length_width_ratio"].rank(pct=True)<br>        + (-working["width_m"]).rank(pct=True)<br>        + (-working["compactness"]).rank(pct=True)<br>    )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def profile_shape_distribution(
    parcels: gpd.GeoDataFrame,
) -> ShapeDistributionProfile:
    try:
        validate_normalized_cadastre_parcels(parcels)
    except ValueError as error:
        raise ShapeProfileError(str(error)) from error
    missing_columns = REQUIRED_COLUMNS - set(parcels.columns)
    if missing_columns:
        formatted = ", ".join(sorted(missing_columns))
        raise ShapeProfileError(f"Missing required shape columns: {formatted}")
    if parcels.crs is None:
        raise ShapeProfileError("Shape candidate CRS is required")
    try:
        CRS.from_user_input(parcels.crs)
    except Exception as error:
        raise ShapeProfileError("Shape candidate CRS must be readable") from error
    identifiers = parcels["parcel_id"]
    if identifiers.isna().any():
        raise ShapeProfileError("parcel_id values must not be null")
    if any(
        not isinstance(identifier, str)
        or not identifier
        or identifier != identifier.strip()
        for identifier in identifiers
    ):
        raise ShapeProfileError("parcel_id values must be exact non-empty strings")
    if identifiers.duplicated().any():
        raise ShapeProfileError("parcel_id values must be unique")

    statuses = set(parcels["shape_status"].dropna().unique())
    if parcels["shape_status"].isna().any() or not statuses <= {"VALID", "ERROR"}:
        unexpected = sorted(str(status) for status in statuses - {"VALID", "ERROR"})
        formatted = ", ".join(unexpected) if unexpected else "null"
        raise ShapeProfileError(f"Unexpected shape_status values: {formatted}")

    valid_shapes = parcels["shape_status"] == "VALID"
    error_shapes = parcels["shape_status"] == "ERROR"
    input_count = len(parcels)
    valid_count = int(valid_shapes.sum())
    error_count = int(error_shapes.sum())
    if input_count != valid_count + error_count:
        raise ShapeProfileError("Shape status counts do not match input count")
    if valid_count == 0:
        raise ShapeProfileError("At least one VALID shape row is required")

    required_valid_metrics = [
        *PROFILE_METRICS,
        "centroid_lat",
        "centroid_lon",
    ]
    if parcels.loc[valid_shapes, required_valid_metrics].isna().any().any():
        raise ShapeProfileError("VALID shape rows must have complete shape metrics")
    for column in required_valid_metrics:
        values_are_finite = all(
            isinstance(value, Real)
            and not isinstance(value, bool)
            and isfinite(float(value))
            for value in parcels.loc[valid_shapes, column]
        )
        if not values_are_finite:
            raise ShapeProfileError(
                f"VALID shape metric must be numeric and finite: {column}"
            )

    valid = parcels.loc[valid_shapes]
    domain_contracts = (
        ("area_m2", valid["area_m2"] > 0, "area_m2 must be greater than zero"),
        ("length_m", valid["length_m"] > 0, "length_m must be greater than zero"),
        ("width_m", valid["width_m"] > 0, "width_m must be greater than zero"),
        (
            "length_width_ratio",
            valid["length_width_ratio"] >= 1,
            "length_width_ratio must be at least one",
        ),
        (
            "compactness",
            (valid["compactness"] > 0) & (valid["compactness"] <= 1),
            "compactness must be greater than zero and at most one",
        ),
        (
            "centroid_lat",
            valid["centroid_lat"].between(-90, 90, inclusive="both"),
            "centroid_lat must be between -90 and 90",
        ),
        (
            "centroid_lon",
            valid["centroid_lon"].between(-180, 180, inclusive="both"),
            "centroid_lon must be between -180 and 180",
        ),
    )
    for _, condition, message in domain_contracts:
        if not bool(condition.all()):
            raise ShapeProfileError(message)
    if not bool((valid["length_m"] >= valid["width_m"]).all()):
        raise ShapeProfileError("length_m must be at least width_m")
    for row in valid.itertuples(index=False):
        expected_ratio = float(row.length_m) / float(row.width_m)
        if not isclose(
            float(row.length_width_ratio),
            expected_ratio,
            rel_tol=1e-9,
            abs_tol=1e-9,
        ):
            raise ShapeProfileError(
                "length_width_ratio must equal length_m / width_m within tolerance"
            )

    working = parcels.loc[valid_shapes].copy()
    distributions = {
        metric: {
            label: float(working[metric].quantile(quantile))
            for label, quantile in PERCENTILES.items()
        }
        for metric in PROFILE_METRICS
    }

    width = working["width_m"]
    width_buckets = {
        "width < 5 m": int((width < 5).sum()),
        "5–10 m": int(((width >= 5) & (width < 10)).sum()),
        "10–15 m": int(((width >= 10) & (width < 15)).sum()),
        "15–20 m": int(((width >= 15) & (width < 20)).sum()),
        "20–25 m": int(((width >= 20) & (width < 25)).sum()),
        "25–30 m": int(((width >= 25) & (width < 30)).sum()),
        "30–40 m": int(((width >= 30) & (width < 40)).sum()),
        "40–50 m": int(((width >= 40) & (width < 50)).sum()),
        "width >= 50 m": int((width >= 50).sum()),
    }

    ratio = working["length_width_ratio"]
    ratio_buckets = {
        "ratio <= 2": int((ratio <= 2).sum()),
        "2–3": int(((ratio > 2) & (ratio <= 3)).sum()),
        "3–4": int(((ratio > 3) & (ratio <= 4)).sum()),
        "4–5": int(((ratio > 4) & (ratio <= 5)).sum()),
        "5–7": int(((ratio > 5) & (ratio <= 7)).sum()),
        "7–10": int(((ratio > 7) & (ratio <= 10)).sum()),
        "10–15": int(((ratio > 10) & (ratio <= 15)).sum()),
        "15–25": int(((ratio > 15) & (ratio <= 25)).sum()),
        "ratio > 25": int((ratio > 25).sum()),
    }

    compactness = working["compactness"]
    compactness_buckets = {
        "compactness < 0.05": int((compactness < 0.05).sum()),
        "0.05–0.10": int(((compactness >= 0.05) & (compactness < 0.10)).sum()),
        "0.10–0.20": int(((compactness >= 0.10) & (compactness < 0.20)).sum()),
        "0.20–0.30": int(((compactness >= 0.20) & (compactness < 0.30)).sum()),
        "0.30–0.40": int(((compactness >= 0.30) & (compactness < 0.40)).sum()),
        "0.40–0.50": int(((compactness >= 0.40) & (compactness < 0.50)).sum()),
        "0.50–0.60": int(((compactness >= 0.50) & (compactness < 0.60)).sum()),
        "0.60–0.70": int(((compactness >= 0.60) & (compactness < 0.70)).sum()),
        "compactness >= 0.70": int((compactness >= 0.70).sum()),
    }
    if sum(width_buckets.values()) != valid_count:
        raise ShapeProfileError("Width buckets do not cover every VALID row")
    if sum(ratio_buckets.values()) != valid_count:
        raise ShapeProfileError("Ratio buckets do not cover every VALID row")
    if sum(compactness_buckets.values()) != valid_count:
        raise ShapeProfileError("Compactness buckets do not cover every VALID row")

    scenario_masks = {
        "A": width >= 10,
        "B": width >= 15,
        "C": width >= 20,
        "D": (width >= 15) & (ratio <= 10),
        "E": (width >= 20) & (ratio <= 7),
        "F": (width >= 20) & (ratio <= 5) & (compactness >= 0.20),
    }
    scenarios = {
        name: DiagnosticScenario(
            retained_count=int(mask.sum()),
            retained_percentage=float(mask.sum() / valid_count * 100),
        )
        for name, mask in scenario_masks.items()
    }

    working["_median_score"] = 0.0
    for metric in PROFILE_METRICS:
        median = working[metric].median()
        scale = working[metric].quantile(0.75) - working[metric].quantile(0.25)
        if scale == 0:
            scale = 1.0
        working["_median_score"] += (working[metric] - median).abs() / scale
    median_frame = working.nsmallest(5, "_median_score")

    working["_extreme_score"] = (
        working["length_width_ratio"].rank(pct=True)
        + (-working["width_m"]).rank(pct=True)
        + (-working["compactness"]).rank(pct=True)
    )
    extreme_pool = working.loc[~working["parcel_id"].isin(median_frame["parcel_id"])]
    extreme_frame = extreme_pool.nlargest(5, "_extreme_score")

    return ShapeDistributionProfile(
        input_count=input_count,
        valid_count=valid_count,
        error_count=error_count,
        distributions=distributions,
        width_buckets=width_buckets,
        ratio_buckets=ratio_buckets,
        compactness_buckets=compactness_buckets,
        scenarios=scenarios,
        median_parcels=_records(median_frame),
        extreme_parcels=_records(extreme_frame),
    )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.


## 7. Validation and data-contract summary

- Canonical schema/mapping declarations inventoried above: `REPRESENTATIVE_FIELDS`, `REQUIRED_COLUMNS`.
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
from dataclasses import dataclass
from math import isclose, isfinite
from numbers import Real

import geopandas as gpd  # type: ignore[import-untyped]
from pyproj import CRS  # type: ignore[import-untyped]

from landscout.common.cadastre_contract import validate_normalized_cadastre_parcels

PROFILE_METRICS = (
    "area_m2",
    "length_m",
    "width_m",
    "length_width_ratio",
    "compactness",
)
REPRESENTATIVE_FIELDS = (
    "parcel_id",
    "area_m2",
    "length_m",
    "width_m",
    "length_width_ratio",
    "compactness",
    "centroid_lat",
    "centroid_lon",
)
REQUIRED_COLUMNS = frozenset({"parcel_id", "shape_status", *REPRESENTATIVE_FIELDS})
PERCENTILES = {
    "min": 0.0,
    "p01": 0.01,
    "p05": 0.05,
    "p10": 0.10,
    "p25": 0.25,
    "p50": 0.50,
    "p75": 0.75,
    "p90": 0.90,
    "p95": 0.95,
    "p99": 0.99,
    "max": 1.0,
}


class ShapeProfileError(ValueError):
    """Raised when shape candidates cannot be profiled safely."""


@dataclass(frozen=True)
class DiagnosticScenario:
    retained_count: int
    retained_percentage: float


@dataclass(frozen=True)
class ShapeDistributionProfile:
    input_count: int
    valid_count: int
    error_count: int
    distributions: dict[str, dict[str, float]]
    width_buckets: dict[str, int]
    ratio_buckets: dict[str, int]
    compactness_buckets: dict[str, int]
    scenarios: dict[str, DiagnosticScenario]
    median_parcels: list[dict[str, object]]
    extreme_parcels: list[dict[str, object]]


def _records(frame: gpd.GeoDataFrame) -> list[dict[str, object]]:
    return frame[list(REPRESENTATIVE_FIELDS)].to_dict(orient="records")


def profile_shape_distribution(
    parcels: gpd.GeoDataFrame,
) -> ShapeDistributionProfile:
    try:
        validate_normalized_cadastre_parcels(parcels)
    except ValueError as error:
        raise ShapeProfileError(str(error)) from error
    missing_columns = REQUIRED_COLUMNS - set(parcels.columns)
    if missing_columns:
        formatted = ", ".join(sorted(missing_columns))
        raise ShapeProfileError(f"Missing required shape columns: {formatted}")
    if parcels.crs is None:
        raise ShapeProfileError("Shape candidate CRS is required")
    try:
        CRS.from_user_input(parcels.crs)
    except Exception as error:
        raise ShapeProfileError("Shape candidate CRS must be readable") from error
    identifiers = parcels["parcel_id"]
    if identifiers.isna().any():
        raise ShapeProfileError("parcel_id values must not be null")
    if any(
        not isinstance(identifier, str)
        or not identifier
        or identifier != identifier.strip()
        for identifier in identifiers
    ):
        raise ShapeProfileError("parcel_id values must be exact non-empty strings")
    if identifiers.duplicated().any():
        raise ShapeProfileError("parcel_id values must be unique")

    statuses = set(parcels["shape_status"].dropna().unique())
    if parcels["shape_status"].isna().any() or not statuses <= {"VALID", "ERROR"}:
        unexpected = sorted(str(status) for status in statuses - {"VALID", "ERROR"})
        formatted = ", ".join(unexpected) if unexpected else "null"
        raise ShapeProfileError(f"Unexpected shape_status values: {formatted}")

    valid_shapes = parcels["shape_status"] == "VALID"
    error_shapes = parcels["shape_status"] == "ERROR"
    input_count = len(parcels)
    valid_count = int(valid_shapes.sum())
    error_count = int(error_shapes.sum())
    if input_count != valid_count + error_count:
        raise ShapeProfileError("Shape status counts do not match input count")
    if valid_count == 0:
        raise ShapeProfileError("At least one VALID shape row is required")

    required_valid_metrics = [
        *PROFILE_METRICS,
        "centroid_lat",
        "centroid_lon",
    ]
    if parcels.loc[valid_shapes, required_valid_metrics].isna().any().any():
        raise ShapeProfileError("VALID shape rows must have complete shape metrics")
    for column in required_valid_metrics:
        values_are_finite = all(
            isinstance(value, Real)
            and not isinstance(value, bool)
            and isfinite(float(value))
            for value in parcels.loc[valid_shapes, column]
        )
        if not values_are_finite:
            raise ShapeProfileError(
                f"VALID shape metric must be numeric and finite: {column}"
            )

    valid = parcels.loc[valid_shapes]
    domain_contracts = (
        ("area_m2", valid["area_m2"] > 0, "area_m2 must be greater than zero"),
        ("length_m", valid["length_m"] > 0, "length_m must be greater than zero"),
        ("width_m", valid["width_m"] > 0, "width_m must be greater than zero"),
        (
            "length_width_ratio",
            valid["length_width_ratio"] >= 1,
            "length_width_ratio must be at least one",
        ),
        (
            "compactness",
            (valid["compactness"] > 0) & (valid["compactness"] <= 1),
            "compactness must be greater than zero and at most one",
        ),
        (
            "centroid_lat",
            valid["centroid_lat"].between(-90, 90, inclusive="both"),
            "centroid_lat must be between -90 and 90",
        ),
        (
            "centroid_lon",
            valid["centroid_lon"].between(-180, 180, inclusive="both"),
            "centroid_lon must be between -180 and 180",
        ),
    )
    for _, condition, message in domain_contracts:
        if not bool(condition.all()):
            raise ShapeProfileError(message)
    if not bool((valid["length_m"] >= valid["width_m"]).all()):
        raise ShapeProfileError("length_m must be at least width_m")
    for row in valid.itertuples(index=False):
        expected_ratio = float(row.length_m) / float(row.width_m)
        if not isclose(
            float(row.length_width_ratio),
            expected_ratio,
            rel_tol=1e-9,
            abs_tol=1e-9,
        ):
            raise ShapeProfileError(
                "length_width_ratio must equal length_m / width_m within tolerance"
            )

    working = parcels.loc[valid_shapes].copy()
    distributions = {
        metric: {
            label: float(working[metric].quantile(quantile))
            for label, quantile in PERCENTILES.items()
        }
        for metric in PROFILE_METRICS
    }

    width = working["width_m"]
    width_buckets = {
        "width < 5 m": int((width < 5).sum()),
        "5–10 m": int(((width >= 5) & (width < 10)).sum()),
        "10–15 m": int(((width >= 10) & (width < 15)).sum()),
        "15–20 m": int(((width >= 15) & (width < 20)).sum()),
        "20–25 m": int(((width >= 20) & (width < 25)).sum()),
        "25–30 m": int(((width >= 25) & (width < 30)).sum()),
        "30–40 m": int(((width >= 30) & (width < 40)).sum()),
        "40–50 m": int(((width >= 40) & (width < 50)).sum()),
        "width >= 50 m": int((width >= 50).sum()),
    }

    ratio = working["length_width_ratio"]
    ratio_buckets = {
        "ratio <= 2": int((ratio <= 2).sum()),
        "2–3": int(((ratio > 2) & (ratio <= 3)).sum()),
        "3–4": int(((ratio > 3) & (ratio <= 4)).sum()),
        "4–5": int(((ratio > 4) & (ratio <= 5)).sum()),
        "5–7": int(((ratio > 5) & (ratio <= 7)).sum()),
        "7–10": int(((ratio > 7) & (ratio <= 10)).sum()),
        "10–15": int(((ratio > 10) & (ratio <= 15)).sum()),
        "15–25": int(((ratio > 15) & (ratio <= 25)).sum()),
        "ratio > 25": int((ratio > 25).sum()),
    }

    compactness = working["compactness"]
    compactness_buckets = {
        "compactness < 0.05": int((compactness < 0.05).sum()),
        "0.05–0.10": int(((compactness >= 0.05) & (compactness < 0.10)).sum()),
        "0.10–0.20": int(((compactness >= 0.10) & (compactness < 0.20)).sum()),
        "0.20–0.30": int(((compactness >= 0.20) & (compactness < 0.30)).sum()),
        "0.30–0.40": int(((compactness >= 0.30) & (compactness < 0.40)).sum()),
        "0.40–0.50": int(((compactness >= 0.40) & (compactness < 0.50)).sum()),
        "0.50–0.60": int(((compactness >= 0.50) & (compactness < 0.60)).sum()),
        "0.60–0.70": int(((compactness >= 0.60) & (compactness < 0.70)).sum()),
        "compactness >= 0.70": int((compactness >= 0.70).sum()),
    }
    if sum(width_buckets.values()) != valid_count:
        raise ShapeProfileError("Width buckets do not cover every VALID row")
    if sum(ratio_buckets.values()) != valid_count:
        raise ShapeProfileError("Ratio buckets do not cover every VALID row")
    if sum(compactness_buckets.values()) != valid_count:
        raise ShapeProfileError("Compactness buckets do not cover every VALID row")

    scenario_masks = {
        "A": width >= 10,
        "B": width >= 15,
        "C": width >= 20,
        "D": (width >= 15) & (ratio <= 10),
        "E": (width >= 20) & (ratio <= 7),
        "F": (width >= 20) & (ratio <= 5) & (compactness >= 0.20),
    }
    scenarios = {
        name: DiagnosticScenario(
            retained_count=int(mask.sum()),
            retained_percentage=float(mask.sum() / valid_count * 100),
        )
        for name, mask in scenario_masks.items()
    }

    working["_median_score"] = 0.0
    for metric in PROFILE_METRICS:
        median = working[metric].median()
        scale = working[metric].quantile(0.75) - working[metric].quantile(0.25)
        if scale == 0:
            scale = 1.0
        working["_median_score"] += (working[metric] - median).abs() / scale
    median_frame = working.nsmallest(5, "_median_score")

    working["_extreme_score"] = (
        working["length_width_ratio"].rank(pct=True)
        + (-working["width_m"]).rank(pct=True)
        + (-working["compactness"]).rank(pct=True)
    )
    extreme_pool = working.loc[~working["parcel_id"].isin(median_frame["parcel_id"])]
    extreme_frame = extreme_pool.nlargest(5, "_extreme_score")

    return ShapeDistributionProfile(
        input_count=input_count,
        valid_count=valid_count,
        error_count=error_count,
        distributions=distributions,
        width_buckets=width_buckets,
        ratio_buckets=ratio_buckets,
        compactness_buckets=compactness_buckets,
        scenarios=scenarios,
        median_parcels=_records(median_frame),
        extreme_parcels=_records(extreme_frame),
    )
```

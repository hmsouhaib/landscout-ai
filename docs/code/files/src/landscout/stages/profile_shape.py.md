# `src/landscout/stages/profile_shape.py`

## File identity

- Repository path: `src/landscout/stages/profile_shape.py`
- File type: Python source
- Layer: diagnostic/profile stage
- Domain: cadastre
- Responsibility: Profiles shape metrics and scenario evidence without making parcel suitability decisions.
- Source SHA256: `1a5e1de1f7584e49abedf963282e4cc3b7c7ab3a724333bea75cdaa6f90a24c8`

## 1. Purpose

Profiles shape metrics and scenario evidence without making parcel suitability decisions.

## 2. Position in LandScout architecture

This file belongs to the **diagnostic/profile stage** layer and the **cadastre** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from dataclasses import dataclass`
- `from math import isclose, isfinite`
- `from numbers import Real`

### Third-party packages

- `import geopandas as gpd`
- `from pyproj import CRS`

### Internal LandScout imports

- `None.`

## 4. Contract taxonomy

### A. Python constants

#### `PROFILE_METRICS`

```python
PROFILE_METRICS = (
    "area_m2",
    "length_m",
    "width_m",
    "length_width_ratio",
    "compactness",
)
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_profile_shape.py::<module>` (import), `src/landscout/stages/profile_shape.py::profile_shape_distribution` (value reference), `tests/unit/test_profile_shape.py::_with_error_row` (value reference).

#### `REPRESENTATIVE_FIELDS`

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

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `src/landscout/stages/profile_shape.py::<module>` (value reference), `src/landscout/stages/profile_shape.py::_records` (value reference).

#### `REQUIRED_COLUMNS`

```python
REQUIRED_COLUMNS = frozenset({"parcel_id", "shape_status", *REPRESENTATIVE_FIELDS})
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/stages/profile_shape.py::profile_shape_distribution` (value reference).

#### `PERCENTILES`

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

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `src/landscout/stages/profile_shape.py::profile_shape_distribution` (value reference).


### B. Type aliases and closed domains

No module-level Literal/Annotated/TypeAlias declaration is present.

### C. Meaningful dunder contracts

No meaningful module-level dunder contract is declared.

### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

### `ShapeProfileError`

**Purpose:** Raised when shape candidates cannot be profiled safely.

**Kind:** controlled exception.

**Inheritance:** `ValueError`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.profile_shape import (
    ShapeDistributionProfile,
    ShapeProfileError,
    profile_shape_distribution,
)`.
- import: `tests/unit/test_profile_shape.py::<module>` via `from landscout.stages.profile_shape import (
    PROFILE_METRICS,
    ShapeProfileError,
    profile_shape_distribution,
)`.
- constructor call: `src/landscout/stages/profile_shape.py::profile_shape_distribution` via `ShapeProfileError`.
- expected exception type: `tests/unit/test_profile_shape.py::test_missing_metric_fails` via `pytest.raises(ShapeProfileError, match='width_m')`.
- expected exception type: `tests/unit/test_profile_shape.py::test_null_parcel_id_fails` via `pytest.raises(ShapeProfileError, match='null')`.
- expected exception type: `tests/unit/test_profile_shape.py::test_duplicate_parcel_id_fails` via `pytest.raises(ShapeProfileError, match='unique')`.
- expected exception type: `tests/unit/test_profile_shape.py::test_missing_crs_fails` via `pytest.raises(ShapeProfileError, match='CRS')`.
- expected exception type: `tests/unit/test_profile_shape.py::test_null_metric_on_valid_shape_fails` via `pytest.raises(ShapeProfileError, match='complete')`.
- expected exception type: `tests/unit/test_profile_shape.py::test_unexpected_shape_status_fails` via `pytest.raises(ShapeProfileError, match='Unexpected')`.
- expected exception type: `tests/unit/test_profile_shape.py::test_non_finite_metric_on_valid_row_fails` via `pytest.raises(ShapeProfileError, match='finite')`.
- expected exception type: `tests/unit/test_profile_shape.py::test_zero_valid_rows_fails_clearly` via `pytest.raises(ShapeProfileError, match='At least one VALID')`.
- expected exception type: `tests/unit/test_profile_shape.py::test_valid_shape_metrics_require_physical_domains` via `pytest.raises(ShapeProfileError, match=message)`.
- expected exception type: `tests/unit/test_profile_shape.py::test_valid_shape_length_must_not_be_less_than_width` via `pytest.raises(ShapeProfileError, match='length_m must be at least width_m')`.
- expected exception type: `tests/unit/test_profile_shape.py::test_valid_shape_ratio_must_match_length_divided_by_width` via `pytest.raises(ShapeProfileError, match='must equal length_m / width_m')`.
- expected exception type: `tests/unit/test_profile_shape.py::test_valid_shape_metrics_reject_bool_and_numeric_strings` via `pytest.raises(ShapeProfileError, match='numeric and finite')`.

**Exact class source**

```python
class ShapeProfileError(ValueError):
    """Raised when shape candidates cannot be profiled safely."""
```

### `DiagnosticScenario`

**Purpose:** Immutable result/value envelope carrying `retained_count`, `retained_percentage`.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `retained_count` | `retained_count: int` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |
| `retained_percentage` | `retained_percentage: float` | Percentage of profiled parcels retained by this diagnostic threshold scenario. |

**Interface consumers**

- type annotation: `src/landscout/stages/profile_shape.py::ShapeDistributionProfile` via `DiagnosticScenario`.
- constructor call: `src/landscout/stages/profile_shape.py::profile_shape_distribution` via `DiagnosticScenario`.

**Exact class source**

```python
class DiagnosticScenario:
    retained_count: int
    retained_percentage: float
```

### `ShapeDistributionProfile`

**Purpose:** Immutable result/value envelope carrying `input_count`, `valid_count`, `error_count`, `distributions`, `width_buckets`, `ratio_buckets`, `compactness_buckets`, `scenarios`, `median_parcels`, `extreme_parcels`.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `input_count` | `input_count: int` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |
| `valid_count` | `valid_count: int` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |
| `error_count` | `error_count: int` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |
| `distributions` | `distributions: dict[str, dict[str, float]]` | Structured `distributions` collection owned by `ShapeDistributionProfile`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |
| `width_buckets` | `width_buckets: dict[str, int]` | Structured `width buckets` collection owned by `ShapeDistributionProfile`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |
| `ratio_buckets` | `ratio_buckets: dict[str, int]` | Structured `ratio buckets` collection owned by `ShapeDistributionProfile`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |
| `compactness_buckets` | `compactness_buckets: dict[str, int]` | Structured `compactness buckets` collection owned by `ShapeDistributionProfile`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |
| `scenarios` | `scenarios: dict[str, DiagnosticScenario]` | Structured `scenarios` collection owned by `ShapeDistributionProfile`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |
| `median_parcels` | `median_parcels: list[dict[str, object]]` | Structured `median parcels` collection owned by `ShapeDistributionProfile`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |
| `extreme_parcels` | `extreme_parcels: list[dict[str, object]]` | Structured `extreme parcels` collection owned by `ShapeDistributionProfile`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |

**Interface consumers**

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.profile_shape import (
    ShapeDistributionProfile,
    ShapeProfileError,
    profile_shape_distribution,
)`.
- type annotation: `src/landscout/stages/profile_shape.py::profile_shape_distribution` via `ShapeDistributionProfile`.
- constructor call: `src/landscout/stages/profile_shape.py::profile_shape_distribution` via `ShapeDistributionProfile`.

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


## 6. Functions and methods

### `_records`

**Exact signature**

```python
def _records(frame: gpd.GeoDataFrame) -> list[dict[str, object]]:
```

**Purpose**

Private `cadastre` helper for records; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `list[dict[str, object]]`.
- Every observed return expression is reproduced without truncation:
```python
frame[list(REPRESENTATIVE_FIELDS)].to_dict(orient='records')
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/profile_shape.py::profile_shape_distribution` via `_records`.

**Complete source-ordered implementation**

```python
def _records(frame: gpd.GeoDataFrame) -> list[dict[str, object]]:
    return frame[list(REPRESENTATIVE_FIELDS)].to_dict(orient="records")
```

**Business boundary**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

### `profile_shape_distribution`

**Exact signature**

```python
def profile_shape_distribution(
    parcels: gpd.GeoDataFrame,
) -> ShapeDistributionProfile:
```

**Purpose**

Computes non-decisional summary statistics for shape distribution; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `ShapeDistributionProfile`.
- Every observed return expression is reproduced without truncation:
```python
ShapeDistributionProfile(input_count=input_count, valid_count=valid_count, error_count=error_count, distributions=distributions, width_buckets=width_buckets, ratio_buckets=ratio_buckets, compactness_buckets=compactness_buckets, scenarios=scenarios, median_parcels=_records(median_frame), extreme_parcels=_records(extreme_frame))
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(parcels, gpd.GeoDataFrame)`.
- Guard with a raise path: `parcels.columns.duplicated().any()`.
- Guard with a raise path: `missing_columns`.
- Guard with a raise path: `parcels.crs is None`.
- Guard with a raise path: `identifiers.isna().any()`.
- Guard with a raise path: `any((not isinstance(identifier, str) or not identifier or identifier != identifier.strip() for identifier in identifiers))`.
- Guard with a raise path: `identifiers.duplicated().any()`.
- Guard with a raise path: `parcels['shape_status'].isna().any() or not statuses <= {'VALID', 'ERROR'}`.
- Guard with a raise path: `input_count != valid_count + error_count`.
- Guard with a raise path: `valid_count == 0`.
- Guard with a raise path: `parcels.loc[valid_shapes, required_valid_metrics].isna().any().any()`.
- Guard with a raise path: `not bool((valid['length_m'] >= valid['width_m']).all())`.
- Guard with a raise path: `sum(width_buckets.values()) != valid_count`.
- Guard with a raise path: `sum(ratio_buckets.values()) != valid_count`.
- Guard with a raise path: `sum(compactness_buckets.values()) != valid_count`.
- Guard with a raise path: `not values_are_finite`.
- Guard with a raise path: `not bool(condition.all())`.
- Guard with a raise path: `not isclose(float(row.length_width_ratio), expected_ratio, rel_tol=1e-09, abs_tol=1e-09)`.
- Explicit raise expressions: `ShapeProfileError('At least one VALID shape row is required')`, `ShapeProfileError('Compactness buckets do not cover every VALID row')`, `ShapeProfileError('Ratio buckets do not cover every VALID row')`, `ShapeProfileError('Shape candidate CRS is required')`, `ShapeProfileError('Shape candidate CRS must be readable')`, `ShapeProfileError('Shape candidate columns must be unique')`, `ShapeProfileError('Shape candidates must be a GeoDataFrame')`, `ShapeProfileError('Shape status counts do not match input count')`, `ShapeProfileError('VALID shape rows must have complete shape metrics')`, `ShapeProfileError('Width buckets do not cover every VALID row')`, `ShapeProfileError('length_m must be at least width_m')`, `ShapeProfileError('length_width_ratio must equal length_m / width_m within tolerance')`, `ShapeProfileError('parcel_id values must be exact non-empty strings')`, `ShapeProfileError('parcel_id values must be unique')`, `ShapeProfileError('parcel_id values must not be null')`, `ShapeProfileError(f'Missing required shape columns: {formatted}')`, `ShapeProfileError(f'Unexpected shape_status values: {formatted}')`, `ShapeProfileError(f'VALID shape metric must be numeric and finite: {column}')`, `ShapeProfileError(message)`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `working['_extreme_score']`, `working['_median_score']`.
- Input mutation: none.

**Repository interfaces and consumers**

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.profile_shape import (
    ShapeDistributionProfile,
    ShapeProfileError,
    profile_shape_distribution,
)`.
- import: `tests/unit/test_profile_shape.py::<module>` via `from landscout.stages.profile_shape import (
    PROFILE_METRICS,
    ShapeProfileError,
    profile_shape_distribution,
)`.
- direct call: `tests/unit/test_profile_shape.py::test_percentile_calculation` via `profile_shape_distribution`.
- direct call: `tests/unit/test_profile_shape.py::test_bucket_counts_sum_to_input_count` via `profile_shape_distribution`.
- direct call: `tests/unit/test_profile_shape.py::test_existing_all_valid_behavior_is_unchanged` via `profile_shape_distribution`.
- direct call: `tests/unit/test_profile_shape.py::test_diagnostic_scenario_counts` via `profile_shape_distribution`.
- direct call: `tests/unit/test_profile_shape.py::test_input_is_not_mutated` via `profile_shape_distribution`.
- direct call: `tests/unit/test_profile_shape.py::test_missing_metric_fails` via `profile_shape_distribution`.
- direct call: `tests/unit/test_profile_shape.py::test_null_parcel_id_fails` via `profile_shape_distribution`.
- direct call: `tests/unit/test_profile_shape.py::test_duplicate_parcel_id_fails` via `profile_shape_distribution`.
- direct call: `tests/unit/test_profile_shape.py::test_missing_crs_fails` via `profile_shape_distribution`.
- direct call: `tests/unit/test_profile_shape.py::test_null_metric_on_valid_shape_fails` via `profile_shape_distribution`.
- direct call: `tests/unit/test_profile_shape.py::test_mixed_valid_and_error_rows_are_counted` via `profile_shape_distribution`.
- direct call: `tests/unit/test_profile_shape.py::test_error_rows_are_excluded_from_percentiles` via `profile_shape_distribution`.
- direct call: `tests/unit/test_profile_shape.py::test_error_rows_are_excluded_from_buckets` via `profile_shape_distribution`.
- direct call: `tests/unit/test_profile_shape.py::test_scenario_percentages_use_valid_count` via `profile_shape_distribution`.
- direct call: `tests/unit/test_profile_shape.py::test_unexpected_shape_status_fails` via `profile_shape_distribution`.
- direct call: `tests/unit/test_profile_shape.py::test_non_finite_metric_on_valid_row_fails` via `profile_shape_distribution`.
- direct call: `tests/unit/test_profile_shape.py::test_zero_valid_rows_fails_clearly` via `profile_shape_distribution`.
- direct call: `tests/unit/test_profile_shape.py::test_valid_shape_metrics_require_physical_domains` via `profile_shape_distribution`.
- direct call: `tests/unit/test_profile_shape.py::test_valid_shape_length_must_not_be_less_than_width` via `profile_shape_distribution`.
- direct call: `tests/unit/test_profile_shape.py::test_valid_shape_ratio_must_match_length_divided_by_width` via `profile_shape_distribution`.
- direct call: `tests/unit/test_profile_shape.py::test_valid_shape_metrics_reject_bool_and_numeric_strings` via `profile_shape_distribution`.

**Complete source-ordered implementation**

```python
def profile_shape_distribution(
    parcels: gpd.GeoDataFrame,
) -> ShapeDistributionProfile:
    if not isinstance(parcels, gpd.GeoDataFrame):
        raise ShapeProfileError("Shape candidates must be a GeoDataFrame")
    if parcels.columns.duplicated().any():
        raise ShapeProfileError("Shape candidate columns must be unique")
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
    extreme_pool = working.loc[
        ~working["parcel_id"].isin(median_frame["parcel_id"])
    ]
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

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.


## 7. Data contracts

### `REQUIRED_COLUMNS` — required input frame fields (unordered when stored as a set)

```python
REQUIRED_COLUMNS = frozenset({"parcel_id", "shape_status", *REPRESENTATIVE_FIELDS})
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `area_m2` | float64 when builder initializes NaN/numeric metric; otherwise exact source numeric dtype shown by implementation | null only on the explicit no-measurement/invalid path | geometry metric | Square-metre geometry measurement; not a policy threshold unless the field belongs to configuration. |
| 2 | `centroid_lat` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 3 | `centroid_lon` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 4 | `compactness` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 5 | `length_m` | builder/source numeric dtype shown by the implementation; no cast is inferred from the name | null on explicit no-match/unknown paths | derived fact or proxy metric | Numeric evidence in the unit encoded by the suffix; it does not establish legal/capacity suitability. |
| 6 | `length_width_ratio` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 7 | `parcel_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 8 | `shape_status` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 9 | `width_m` | builder/source numeric dtype shown by the implementation; no cast is inferred from the name | null on explicit no-match/unknown paths | derived fact or proxy metric | Numeric evidence in the unit encoded by the suffix; it does not establish legal/capacity suitability. |


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

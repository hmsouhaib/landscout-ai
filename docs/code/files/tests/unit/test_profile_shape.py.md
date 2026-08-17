# `tests/unit/test_profile_shape.py`

## File identity

- Repository path: `tests/unit/test_profile_shape.py`
- File type: Python test
- Layer: unit/regression test
- Domain: test
- Responsibility: Provides complete unit and regression coverage for the `profile_shape` contracts exercised in this file.
- Source SHA256: `c571ddbee0b9ae0676cd75a637e01c08c8f3b8562f75d4a7e104e9ec891b9086`

## 1. Purpose

Provides complete unit and regression coverage for the `profile_shape` contracts exercised in this file.

## 2. Position in LandScout architecture

This file belongs to the **unit/regression test** layer and the **test** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `None.`

### Third-party packages

- `import geopandas as gpd`
- `import pandas as pd`
- `import pytest`
- `from shapely.geometry import Point`

### Internal LandScout imports

- `from landscout.stages.profile_shape import (
    PROFILE_METRICS,
    ShapeProfileError,
    profile_shape_distribution,
)`

## 4. Contract taxonomy

### A. Python constants

No meaningful module constant is declared.

### B. Type aliases and closed domains

No module-level Literal/Annotated/TypeAlias declaration is present.

### C. Meaningful dunder contracts

No meaningful module-level dunder contract is declared.

### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

No class/model/dataclass is declared.

## 6. Functions and methods

### `_with_error_row`

**Exact signature**

```python
def _with_error_row(parcels: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
```

**Purpose**

Private `test` helper for with error row; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
mixed
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
- In-memory mutation: `mixed.loc[9, 'shape_status']`, `mixed.loc[9, column]`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_profile_shape.py::test_mixed_valid_and_error_rows_are_counted` via `_with_error_row`.
- direct call or construction: `tests/unit/test_profile_shape.py::test_error_rows_are_excluded_from_percentiles` via `_with_error_row`.
- direct call or construction: `tests/unit/test_profile_shape.py::test_error_rows_are_excluded_from_buckets` via `_with_error_row`.
- direct call or construction: `tests/unit/test_profile_shape.py::test_scenario_percentages_use_valid_count` via `_with_error_row`.

**Complete source-ordered implementation**

```python
def _with_error_row(parcels: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    mixed = parcels.copy()
    mixed.loc[9, "shape_status"] = "ERROR"
    for column in (*PROFILE_METRICS, "centroid_lat", "centroid_lon"):
        mixed.loc[9, column] = None
    return mixed
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `parcels` — pytest fixture

- Scope: `function` (decorator `pytest.fixture`).
- Returned/yielded object expression(s): `gpd.GeoDataFrame({'parcel_id': [f'parcel-{index}' for index in range(count)], 'shape_status': ['VALID'] * count, 'area_m2': [100.0 * (index + 1) for index in range(count)], 'length_m': [4.0, 17.5, 42.0, 76.5, 132.0, 216.0, 420.0, 900.0, 1650.0, 300.0], 'width_m': [4.0, 7.0, 12.0, 17.0, 22.0, 27.0, 35.0, 45.0, 55.0, 60.0], 'length_width_ratio': [1.0, 2.5, 3.5, 4.5, 6.0, 8.0, 12.0, 20.0, 30.0, 5.0], 'compactness': [0.02, 0.07, 0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85], 'centroid_lat': [43.0 + index / 100 for index in range(count)], 'centroid_lon': [2.0 + index / 100 for index in range(count)]}, geometry=[Point(2.0 + index / 100, 43.0) for index in range(count)], crs='EPSG:4326')`.
- Tests requesting it by parameter injection: `_with_error_row`, `test_percentile_calculation`, `test_bucket_counts_sum_to_input_count`, `test_existing_all_valid_behavior_is_unchanged`, `test_diagnostic_scenario_counts`, `test_input_is_not_mutated`, `test_missing_metric_fails`, `test_null_parcel_id_fails`, `test_duplicate_parcel_id_fails`, `test_missing_crs_fails`, `test_null_metric_on_valid_shape_fails`, `test_mixed_valid_and_error_rows_are_counted`, `test_error_rows_are_excluded_from_percentiles`, `test_error_rows_are_excluded_from_buckets`, `test_scenario_percentages_use_valid_count`, `test_unexpected_shape_status_fails`, `test_non_finite_metric_on_valid_row_fails`, `test_zero_valid_rows_fails_clearly`, `test_valid_shape_metrics_require_physical_domains`, `test_valid_shape_length_must_not_be_less_than_width`, `test_valid_shape_ratio_must_match_length_divided_by_width`, `test_valid_shape_metrics_reject_bool_and_numeric_strings`.

**Complete fixture implementation**

```python
def parcels() -> gpd.GeoDataFrame:
    count = 10
    return gpd.GeoDataFrame(
        {
            "parcel_id": [f"parcel-{index}" for index in range(count)],
            "shape_status": ["VALID"] * count,
            "area_m2": [100.0 * (index + 1) for index in range(count)],
            "length_m": [4.0, 17.5, 42.0, 76.5, 132.0, 216.0, 420.0, 900.0, 1650.0, 300.0],
            "width_m": [4.0, 7.0, 12.0, 17.0, 22.0, 27.0, 35.0, 45.0, 55.0, 60.0],
            "length_width_ratio": [1.0, 2.5, 3.5, 4.5, 6.0, 8.0, 12.0, 20.0, 30.0, 5.0],
            "compactness": [0.02, 0.07, 0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85],
            "centroid_lat": [43.0 + index / 100 for index in range(count)],
            "centroid_lon": [2.0 + index / 100 for index in range(count)],
        },
        geometry=[Point(2.0 + index / 100, 43.0) for index in range(count)],
        crs="EPSG:4326",
    )
```

### `test_percentile_calculation`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
area = profile.distributions["area_m2"]
```

**Action**

```python
profile = profile_shape_distribution(parcels)
```

**Expected result**

```python
assert area["min"] == pytest.approx(100.0)
assert area["p50"] == pytest.approx(550.0)
assert area["max"] == pytest.approx(1000.0)
assert set(area) == {
        "min",
        "p01",
        "p05",
        "p10",
        "p25",
        "p50",
        "p75",
        "p90",
        "p95",
        "p99",
        "max",
    }
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_percentile_calculation(parcels: gpd.GeoDataFrame) -> None:
    profile = profile_shape_distribution(parcels)

    area = profile.distributions["area_m2"]
    assert area["min"] == pytest.approx(100.0)
    assert area["p50"] == pytest.approx(550.0)
    assert area["max"] == pytest.approx(1000.0)
    assert set(area) == {
        "min",
        "p01",
        "p05",
        "p10",
        "p25",
        "p50",
        "p75",
        "p90",
        "p95",
        "p99",
        "max",
    }
```

### `test_bucket_counts_sum_to_input_count`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
profile = profile_shape_distribution(parcels)
```

**Expected result**

```python
assert sum(profile.width_buckets.values()) == len(parcels)
assert sum(profile.ratio_buckets.values()) == len(parcels)
assert sum(profile.compactness_buckets.values()) == len(parcels)
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_bucket_counts_sum_to_input_count(parcels: gpd.GeoDataFrame) -> None:
    profile = profile_shape_distribution(parcels)

    assert sum(profile.width_buckets.values()) == len(parcels)
    assert sum(profile.ratio_buckets.values()) == len(parcels)
    assert sum(profile.compactness_buckets.values()) == len(parcels)
```

### `test_existing_all_valid_behavior_is_unchanged`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
profile = profile_shape_distribution(parcels)
```

**Expected result**

```python
assert profile.input_count == 10
assert profile.valid_count == 10
assert profile.error_count == 0
assert profile.distributions["area_m2"]["max"] == pytest.approx(1000.0)
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_existing_all_valid_behavior_is_unchanged(parcels: gpd.GeoDataFrame) -> None:
    profile = profile_shape_distribution(parcels)

    assert profile.input_count == 10
    assert profile.valid_count == 10
    assert profile.error_count == 0
    assert profile.distributions["area_m2"]["max"] == pytest.approx(1000.0)
```

### `test_diagnostic_scenario_counts`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
profile = profile_shape_distribution(parcels)
```

**Expected result**

```python
assert profile.scenarios["A"].retained_count == 8
assert profile.scenarios["B"].retained_count == 7
assert profile.scenarios["C"].retained_count == 6
assert profile.scenarios["D"].retained_count == 4
assert profile.scenarios["E"].retained_count == 2
assert profile.scenarios["F"].retained_count == 1
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_diagnostic_scenario_counts(parcels: gpd.GeoDataFrame) -> None:
    profile = profile_shape_distribution(parcels)

    assert profile.scenarios["A"].retained_count == 8
    assert profile.scenarios["B"].retained_count == 7
    assert profile.scenarios["C"].retained_count == 6
    assert profile.scenarios["D"].retained_count == 4
    assert profile.scenarios["E"].retained_count == 2
    assert profile.scenarios["F"].retained_count == 1
```

### `test_input_is_not_mutated`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
original = parcels.copy(deep=True)
pd.testing.assert_frame_equal(parcels, original)
```

**Action**

```python
profile_shape_distribution(parcels)
```

**Expected result**

```python
# Completion without an exception is the asserted outcome.
```

**Regression protected**

Pins the exact framework interaction and outcome reproduced in the complete test source.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_input_is_not_mutated(parcels: gpd.GeoDataFrame) -> None:
    original = parcels.copy(deep=True)

    profile_shape_distribution(parcels)

    pd.testing.assert_frame_equal(parcels, original)
```

### `test_missing_metric_fails`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
without_width = parcels.drop(columns=["width_m"])
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ShapeProfileError, match="width_m"):
        profile_shape_distribution(without_width)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_missing_metric_fails(parcels: gpd.GeoDataFrame) -> None:
    without_width = parcels.drop(columns=["width_m"])

    with pytest.raises(ShapeProfileError, match="width_m"):
        profile_shape_distribution(without_width)
```

### `test_null_parcel_id_fails`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
with_null = parcels.copy()
with_null.loc[0, "parcel_id"] = None
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ShapeProfileError, match="null"):
        profile_shape_distribution(with_null)
```

**Regression protected**

Pins true-null handling and prevents textual or malformed null-like values from changing the contract.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_null_parcel_id_fails(parcels: gpd.GeoDataFrame) -> None:
    with_null = parcels.copy()
    with_null.loc[0, "parcel_id"] = None

    with pytest.raises(ShapeProfileError, match="null"):
        profile_shape_distribution(with_null)
```

### `test_duplicate_parcel_id_fails`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
with_duplicate = parcels.copy()
with_duplicate.loc[1, "parcel_id"] = with_duplicate.loc[0, "parcel_id"]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ShapeProfileError, match="unique"):
        profile_shape_distribution(with_duplicate)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_duplicate_parcel_id_fails(parcels: gpd.GeoDataFrame) -> None:
    with_duplicate = parcels.copy()
    with_duplicate.loc[1, "parcel_id"] = with_duplicate.loc[0, "parcel_id"]

    with pytest.raises(ShapeProfileError, match="unique"):
        profile_shape_distribution(with_duplicate)
```

### `test_missing_crs_fails`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
without_crs = parcels.set_crs(None, allow_override=True)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ShapeProfileError, match="CRS"):
        profile_shape_distribution(without_crs)
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_missing_crs_fails(parcels: gpd.GeoDataFrame) -> None:
    without_crs = parcels.set_crs(None, allow_override=True)

    with pytest.raises(ShapeProfileError, match="CRS"):
        profile_shape_distribution(without_crs)
```

### `test_null_metric_on_valid_shape_fails`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
with_null_metric = parcels.copy()
with_null_metric.loc[0, "compactness"] = None
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ShapeProfileError, match="complete"):
        profile_shape_distribution(with_null_metric)
```

**Regression protected**

Pins true-null handling and prevents textual or malformed null-like values from changing the contract.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_null_metric_on_valid_shape_fails(parcels: gpd.GeoDataFrame) -> None:
    with_null_metric = parcels.copy()
    with_null_metric.loc[0, "compactness"] = None

    with pytest.raises(ShapeProfileError, match="complete"):
        profile_shape_distribution(with_null_metric)
```

### `test_mixed_valid_and_error_rows_are_counted`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
profile = profile_shape_distribution(_with_error_row(parcels))
```

**Expected result**

```python
assert profile.input_count == 10
assert profile.valid_count == 9
assert profile.error_count == 1
assert profile.input_count == profile.valid_count + profile.error_count
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_mixed_valid_and_error_rows_are_counted(parcels: gpd.GeoDataFrame) -> None:
    profile = profile_shape_distribution(_with_error_row(parcels))

    assert profile.input_count == 10
    assert profile.valid_count == 9
    assert profile.error_count == 1
    assert profile.input_count == profile.valid_count + profile.error_count
```

### `test_error_rows_are_excluded_from_percentiles`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
profile = profile_shape_distribution(_with_error_row(parcels))
```

**Expected result**

```python
assert profile.distributions["area_m2"]["max"] == pytest.approx(900.0)
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_error_rows_are_excluded_from_percentiles(parcels: gpd.GeoDataFrame) -> None:
    profile = profile_shape_distribution(_with_error_row(parcels))

    assert profile.distributions["area_m2"]["max"] == pytest.approx(900.0)
```

### `test_error_rows_are_excluded_from_buckets`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
profile = profile_shape_distribution(_with_error_row(parcels))
```

**Expected result**

```python
assert sum(profile.width_buckets.values()) == profile.valid_count == 9
assert sum(profile.ratio_buckets.values()) == profile.valid_count
assert sum(profile.compactness_buckets.values()) == profile.valid_count
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_error_rows_are_excluded_from_buckets(parcels: gpd.GeoDataFrame) -> None:
    profile = profile_shape_distribution(_with_error_row(parcels))

    assert sum(profile.width_buckets.values()) == profile.valid_count == 9
    assert sum(profile.ratio_buckets.values()) == profile.valid_count
    assert sum(profile.compactness_buckets.values()) == profile.valid_count
```

### `test_scenario_percentages_use_valid_count`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
profile = profile_shape_distribution(_with_error_row(parcels))
```

**Expected result**

```python
assert profile.scenarios["A"].retained_count == 7
assert profile.scenarios["A"].retained_percentage == pytest.approx(7 / 9 * 100)
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_scenario_percentages_use_valid_count(parcels: gpd.GeoDataFrame) -> None:
    profile = profile_shape_distribution(_with_error_row(parcels))

    assert profile.scenarios["A"].retained_count == 7
    assert profile.scenarios["A"].retained_percentage == pytest.approx(7 / 9 * 100)
```

### `test_unexpected_shape_status_fails`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
unexpected = parcels.copy()
unexpected.loc[0, "shape_status"] = "UNKNOWN"
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ShapeProfileError, match="Unexpected"):
        profile_shape_distribution(unexpected)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_unexpected_shape_status_fails(parcels: gpd.GeoDataFrame) -> None:
    unexpected = parcels.copy()
    unexpected.loc[0, "shape_status"] = "UNKNOWN"

    with pytest.raises(ShapeProfileError, match="Unexpected"):
        profile_shape_distribution(unexpected)
```

### `test_non_finite_metric_on_valid_row_fails`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
non_finite = parcels.copy()
non_finite.loc[0, "length_m"] = float("inf")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ShapeProfileError, match="finite"):
        profile_shape_distribution(non_finite)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_non_finite_metric_on_valid_row_fails(parcels: gpd.GeoDataFrame) -> None:
    non_finite = parcels.copy()
    non_finite.loc[0, "length_m"] = float("inf")

    with pytest.raises(ShapeProfileError, match="finite"):
        profile_shape_distribution(non_finite)
```

### `test_zero_valid_rows_fails_clearly`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
errors_only = parcels.copy()
errors_only["shape_status"] = "ERROR"
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ShapeProfileError, match="At least one VALID"):
        profile_shape_distribution(errors_only)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_zero_valid_rows_fails_clearly(parcels: gpd.GeoDataFrame) -> None:
    errors_only = parcels.copy()
    errors_only["shape_status"] = "ERROR"

    with pytest.raises(ShapeProfileError, match="At least one VALID"):
        profile_shape_distribution(errors_only)
```

### `test_valid_shape_metrics_require_physical_domains`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `column`, `message`, `value`.

**Setup**

```python
invalid = parcels.copy()
invalid.loc[0, column] = value
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ShapeProfileError, match=message):
        profile_shape_distribution(invalid)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_valid_shape_metrics_require_physical_domains(
    parcels: gpd.GeoDataFrame,
    column: str,
    value: float,
    message: str,
) -> None:
    invalid = parcels.copy()
    invalid.loc[0, column] = value

    with pytest.raises(ShapeProfileError, match=message):
        profile_shape_distribution(invalid)
```

### `test_valid_shape_length_must_not_be_less_than_width`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
invalid = parcels.copy()
invalid.loc[0, "length_m"] = 3
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ShapeProfileError, match="length_m must be at least width_m"):
        profile_shape_distribution(invalid)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_valid_shape_length_must_not_be_less_than_width(
    parcels: gpd.GeoDataFrame,
) -> None:
    invalid = parcels.copy()
    invalid.loc[0, "length_m"] = 3

    with pytest.raises(ShapeProfileError, match="length_m must be at least width_m"):
        profile_shape_distribution(invalid)
```

### `test_valid_shape_ratio_must_match_length_divided_by_width`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
invalid = parcels.copy()
invalid.loc[0, "length_width_ratio"] = 2
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ShapeProfileError, match="must equal length_m / width_m"):
        profile_shape_distribution(invalid)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_valid_shape_ratio_must_match_length_divided_by_width(
    parcels: gpd.GeoDataFrame,
) -> None:
    invalid = parcels.copy()
    invalid.loc[0, "length_width_ratio"] = 2

    with pytest.raises(ShapeProfileError, match="must equal length_m / width_m"):
        profile_shape_distribution(invalid)
```

### `test_valid_shape_metrics_reject_bool_and_numeric_strings`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `value`.

**Setup**

```python
invalid = parcels.copy()
invalid["area_m2"] = invalid["area_m2"].astype(object)
invalid.loc[0, "area_m2"] = value
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ShapeProfileError, match="numeric and finite"):
        profile_shape_distribution(invalid)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_valid_shape_metrics_reject_bool_and_numeric_strings(
    parcels: gpd.GeoDataFrame,
    value: object,
) -> None:
    invalid = parcels.copy()
    invalid["area_m2"] = invalid["area_m2"].astype(object)
    invalid.loc[0, "area_m2"] = value

    with pytest.raises(ShapeProfileError, match="numeric and finite"):
        profile_shape_distribution(invalid)
```


## 7. Data contracts

No module-level canonical frame schema, mapping, or dtype declaration is present. Any frame interaction is recoverable from the complete function implementations below; no string literal is promoted to a column merely because it appears in code.

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

The module contributes to the test flow through the exact facts, proxy evidence, policy results, diagnostics, or prechecks identified above.

## 15. Explicit non-goals

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

## 16. Tests

Test consumers and framework invocation are included in per-symbol interfaces. Test modules distinguish fixture injection from parameterized values and reproduce setup/action/assertion source.

## 17. Change impact

Any source-byte change invalidates the SHA above. Review exact exports, aliases, canonical frame schemas/dtypes, configured source/policy identities, callers, framework hooks, artifacts, and all linked tests before updating this companion.

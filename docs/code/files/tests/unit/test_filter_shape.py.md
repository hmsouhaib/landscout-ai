# `tests/unit/test_filter_shape.py`

## File identity

- Repository path: `tests/unit/test_filter_shape.py`
- File type: Python test
- Layer: unit/regression test
- Domain: test
- Responsibility: Provides complete unit and regression coverage for the `filter_shape` contracts exercised in this file.
- Source SHA256: `92d7ea6f3b6c3ae3c5edf33cfbab1db9ca6699840bafeba28fd1667bdbf9d81b`

## 1. Purpose

Provides complete unit and regression coverage for the `filter_shape` contracts exercised in this file.

## 2. Position in LandScout architecture

This file belongs to the **unit/regression test** layer and the **test** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `None.`

### Third-party packages

- `import geopandas as gpd`
- `import pandas as pd`
- `import pytest`
- `from geopandas.testing import assert_geodataframe_equal`
- `from shapely.geometry import Polygon`

### Internal LandScout imports

- `from landscout.config import ShapeCalibrationConfig, ShapeScreeningConfig`
- `from landscout.stages.filter_parcels import (
    ParcelFilterError,
    filter_parcels_by_shape,
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

### `_shape_config`

**Exact signature**

```python
def _shape_config(
    *,
    min_width_m: float = 15,
    max_length_width_ratio: float = 10,
    policy_version: str = "test_policy_v1",
) -> ShapeScreeningConfig:
```

**Purpose**

Private `test` helper for shape config; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `ShapeScreeningConfig`.
- Every observed return expression is reproduced without truncation:
```python
ShapeScreeningConfig(enabled=True, min_width_m=min_width_m, max_length_width_ratio=max_length_width_ratio, calibration=ShapeCalibrationConfig(policy_version=policy_version, method='unit_test', calibration_scope='test fixture', sample_size=10, calibrated_at='2026-08-11', target_retention_pct=90, observed_retention_pct=90))
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `ShapeCalibrationConfig`, `ShapeScreeningConfig`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_filter_shape.py::shape_config` via `_shape_config`.
- direct call or construction: `tests/unit/test_filter_shape.py::test_different_configs_change_results_for_same_parcels` via `_shape_config`.

**Complete source-ordered implementation**

```python
def _shape_config(
    *,
    min_width_m: float = 15,
    max_length_width_ratio: float = 10,
    policy_version: str = "test_policy_v1",
) -> ShapeScreeningConfig:
    return ShapeScreeningConfig(
        enabled=True,
        min_width_m=min_width_m,
        max_length_width_ratio=max_length_width_ratio,
        calibration=ShapeCalibrationConfig(
            policy_version=policy_version,
            method="unit_test",
            calibration_scope="test fixture",
            sample_size=10,
            calibrated_at="2026-08-11",
            target_retention_pct=90,
            observed_retention_pct=90,
        ),
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `shape_config` — pytest fixture

- Scope: `function` (decorator `pytest.fixture`).
- Returned/yielded object expression(s): `_shape_config()`.
- Tests requesting it by parameter injection: `test_exact_width_and_ratio_boundaries_are_retained`, `test_rejected_parcel_has_expected_primary_reason`, `test_rejection_reason_precedence_is_deterministic`, `test_shape_error_precedence_does_not_inspect_metrics`, `test_enabled_outputs_record_active_policy_metadata`, `test_enabled_partition_preserves_exact_ids_and_crs`, `test_filter_does_not_mutate_input`, `test_missing_required_column_fails`, `test_null_parcel_id_fails`, `test_duplicate_parcel_id_fails`, `test_unknown_crs_fails`, `test_unexpected_or_null_shape_status_fails`, `test_non_finite_known_metric_on_valid_row_fails`, `test_valid_shape_requires_strict_positive_width`, `test_valid_shape_requires_ratio_at_least_one`, `test_negative_ratio_cannot_pass_permissive_thresholds`, `test_valid_shape_rejects_every_incomplete_metric_form`, `test_shape_filter_rejects_plain_dataframe`, `test_shape_filter_rejects_duplicate_columns`, `test_shape_filter_rejects_unreadable_crs`.

**Complete fixture implementation**

```python
def shape_config() -> ShapeScreeningConfig:
    return _shape_config()
```

### `parcels` — pytest fixture

- Scope: `function` (decorator `pytest.fixture`).
- Returned/yielded object expression(s): `gpd.GeoDataFrame({'parcel_id': ['at-boundaries', 'passing', 'width-below', 'ratio-above', 'shape-error', 'width-unknown', 'ratio-unknown', 'both-unknown', 'ratio-unknown-width-below', 'both-thresholds-fail'], 'shape_status': ['VALID', 'VALID', 'VALID', 'VALID', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'VALID'], 'width_m': [15.0, 20.0, 14.9, 16.0, None, None, 20.0, None, 14.0, 14.0], 'length_width_ratio': [10.0, 5.0, 8.0, 10.1, None, 2.0, None, None, None, 11.0], 'compactness': [0.5] * 10}, geometry=[geometry] * 10, crs='EPSG:4326')`.
- Tests requesting it by parameter injection: `test_exact_width_and_ratio_boundaries_are_retained`, `test_rejected_parcel_has_expected_primary_reason`, `test_rejection_reason_precedence_is_deterministic`, `test_shape_error_precedence_does_not_inspect_metrics`, `test_enabled_outputs_record_active_policy_metadata`, `test_enabled_partition_preserves_exact_ids_and_crs`, `test_filter_does_not_mutate_input`, `test_missing_required_column_fails`, `test_null_parcel_id_fails`, `test_duplicate_parcel_id_fails`, `test_unknown_crs_fails`, `test_unexpected_or_null_shape_status_fails`, `test_non_finite_known_metric_on_valid_row_fails`, `test_valid_shape_requires_strict_positive_width`, `test_valid_shape_requires_ratio_at_least_one`, `test_negative_ratio_cannot_pass_permissive_thresholds`, `test_disabled_policy_is_an_exact_passthrough`, `test_different_configs_change_results_for_same_parcels`, `test_valid_shape_requires_complete_metrics_even_when_screening_disabled`, `test_valid_shape_rejects_every_incomplete_metric_form`, `test_shape_filter_rejects_plain_dataframe`, `test_shape_filter_rejects_duplicate_columns`, `test_shape_filter_rejects_unreadable_crs`.

**Complete fixture implementation**

```python
def parcels() -> gpd.GeoDataFrame:
    geometry = Polygon(
        [(2.0, 43.0), (2.01, 43.0), (2.01, 43.01), (2.0, 43.0)]
    )
    return gpd.GeoDataFrame(
        {
            "parcel_id": [
                "at-boundaries",
                "passing",
                "width-below",
                "ratio-above",
                "shape-error",
                "width-unknown",
                "ratio-unknown",
                "both-unknown",
                "ratio-unknown-width-below",
                "both-thresholds-fail",
            ],
            "shape_status": [
                "VALID",
                "VALID",
                "VALID",
                "VALID",
                "ERROR",
                "ERROR",
                "ERROR",
                "ERROR",
                "ERROR",
                "VALID",
            ],
            "width_m": [15.0, 20.0, 14.9, 16.0, None, None, 20.0, None, 14.0, 14.0],
            "length_width_ratio": [
                10.0,
                5.0,
                8.0,
                10.1,
                None,
                2.0,
                None,
                None,
                None,
                11.0,
            ],
            "compactness": [0.5] * 10,
        },
        geometry=[geometry] * 10,
        crs="EPSG:4326",
    )
```

### `test_exact_width_and_ratio_boundaries_are_retained`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`), `shape_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
retained, _ = filter_parcels_by_shape(parcels, shape_config)
```

**Expected result**

```python
assert "at-boundaries" in set(retained["parcel_id"])
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_exact_width_and_ratio_boundaries_are_retained(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
    retained, _ = filter_parcels_by_shape(parcels, shape_config)

    assert "at-boundaries" in set(retained["parcel_id"])
```

### `test_rejected_parcel_has_expected_primary_reason`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`), `shape_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `expected_reason`, `parcel_id`.

**Setup**

```python
row = rejected.loc[rejected["parcel_id"] == parcel_id].iloc[0]
```

**Action**

```python
_, rejected = filter_parcels_by_shape(parcels, shape_config)
```

**Expected result**

```python
assert row["shape_rejection_reason"] == expected_reason
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_rejected_parcel_has_expected_primary_reason(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
    parcel_id: str,
    expected_reason: str,
) -> None:
    _, rejected = filter_parcels_by_shape(parcels, shape_config)

    row = rejected.loc[rejected["parcel_id"] == parcel_id].iloc[0]
    assert row["shape_rejection_reason"] == expected_reason
```

### `test_rejection_reason_precedence_is_deterministic`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`), `shape_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `expected_reason`, `parcel_id`.

**Setup**

```python
reason = rejected.set_index("parcel_id").loc[parcel_id, "shape_rejection_reason"]
```

**Action**

```python
_, rejected = filter_parcels_by_shape(parcels, shape_config)
```

**Expected result**

```python
assert reason == expected_reason
```

**Regression protected**

Pins the configured policy-rule ordering so a lower-priority observation cannot replace the controlling evidence.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_rejection_reason_precedence_is_deterministic(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
    parcel_id: str,
    expected_reason: str,
) -> None:
    _, rejected = filter_parcels_by_shape(parcels, shape_config)

    reason = rejected.set_index("parcel_id").loc[parcel_id, "shape_rejection_reason"]
    assert reason == expected_reason
```

### `test_shape_error_precedence_does_not_inspect_metrics`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`), `shape_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
with_error_payload = parcels.copy()
with_error_payload["width_m"] = with_error_payload["width_m"].astype(object)
with_error_payload["length_width_ratio"] = with_error_payload[
        "length_width_ratio"
    ].astype(object)
error_row = with_error_payload["parcel_id"] == "shape-error"
with_error_payload.loc[error_row, "width_m"] = "unavailable"
with_error_payload.loc[error_row, "length_width_ratio"] = "unavailable"
reason = rejected.set_index("parcel_id").loc[
        "shape-error", "shape_rejection_reason"
    ]
```

**Action**

```python
_, rejected = filter_parcels_by_shape(with_error_payload, shape_config)
```

**Expected result**

```python
assert reason == "SHAPE_ERROR"
```

**Regression protected**

Pins the configured policy-rule ordering so a lower-priority observation cannot replace the controlling evidence.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_shape_error_precedence_does_not_inspect_metrics(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
    with_error_payload = parcels.copy()
    with_error_payload["width_m"] = with_error_payload["width_m"].astype(object)
    with_error_payload["length_width_ratio"] = with_error_payload[
        "length_width_ratio"
    ].astype(object)
    error_row = with_error_payload["parcel_id"] == "shape-error"
    with_error_payload.loc[error_row, "width_m"] = "unavailable"
    with_error_payload.loc[error_row, "length_width_ratio"] = "unavailable"

    _, rejected = filter_parcels_by_shape(with_error_payload, shape_config)

    reason = rejected.set_index("parcel_id").loc[
        "shape-error", "shape_rejection_reason"
    ]
    assert reason == "SHAPE_ERROR"
```

### `test_enabled_outputs_record_active_policy_metadata`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`), `shape_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
for output in (retained, rejected):
        assert set(output["shape_policy_version"]) == {"test_policy_v1"}
        assert set(output["shape_policy_min_width_m"]) == {15.0}
        assert set(output["shape_policy_max_ratio"]) == {10.0}
```

**Action**

```python
retained, rejected = filter_parcels_by_shape(parcels, shape_config)
```

**Expected result**

```python
assert "shape_rejection_reason" not in retained.columns
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_enabled_outputs_record_active_policy_metadata(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
    retained, rejected = filter_parcels_by_shape(parcels, shape_config)

    for output in (retained, rejected):
        assert set(output["shape_policy_version"]) == {"test_policy_v1"}
        assert set(output["shape_policy_min_width_m"]) == {15.0}
        assert set(output["shape_policy_max_ratio"]) == {10.0}
    assert "shape_rejection_reason" not in retained.columns
```

### `test_enabled_partition_preserves_exact_ids_and_crs`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`), `shape_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
retained_ids = set(retained["parcel_id"])
rejected_ids = set(rejected["parcel_id"])
```

**Action**

```python
retained, rejected = filter_parcels_by_shape(parcels, shape_config)
```

**Expected result**

```python
assert len(parcels) == len(retained) + len(rejected)
assert retained_ids.isdisjoint(rejected_ids)
assert retained_ids | rejected_ids == set(parcels["parcel_id"])
assert not retained["parcel_id"].duplicated().any()
assert not rejected["parcel_id"].duplicated().any()
assert retained.crs == parcels.crs
assert rejected.crs == parcels.crs
assert "compactness" in retained.columns
assert "compactness" in rejected.columns
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_enabled_partition_preserves_exact_ids_and_crs(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
    retained, rejected = filter_parcels_by_shape(parcels, shape_config)

    retained_ids = set(retained["parcel_id"])
    rejected_ids = set(rejected["parcel_id"])
    assert len(parcels) == len(retained) + len(rejected)
    assert retained_ids.isdisjoint(rejected_ids)
    assert retained_ids | rejected_ids == set(parcels["parcel_id"])
    assert not retained["parcel_id"].duplicated().any()
    assert not rejected["parcel_id"].duplicated().any()
    assert retained.crs == parcels.crs
    assert rejected.crs == parcels.crs
    assert "compactness" in retained.columns
    assert "compactness" in rejected.columns
```

### `test_filter_does_not_mutate_input`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`), `shape_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
original = parcels.copy(deep=True)
assert_geodataframe_equal(parcels, original)
```

**Action**

```python
filter_parcels_by_shape(parcels, shape_config)
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
def test_filter_does_not_mutate_input(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
    original = parcels.copy(deep=True)

    filter_parcels_by_shape(parcels, shape_config)

    assert_geodataframe_equal(parcels, original)
```

### `test_missing_required_column_fails`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`), `shape_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `column`.

**Setup**

```python
missing_column = parcels.drop(columns=[column])
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ParcelFilterError, match="Missing required shape columns"):
        filter_parcels_by_shape(missing_column, shape_config)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_missing_required_column_fails(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
    column: str,
) -> None:
    missing_column = parcels.drop(columns=[column])

    with pytest.raises(ParcelFilterError, match="Missing required shape columns"):
        filter_parcels_by_shape(missing_column, shape_config)
```

### `test_null_parcel_id_fails`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`), `shape_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
invalid = parcels.copy()
invalid.loc[0, "parcel_id"] = None
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ParcelFilterError, match="must not be null"):
        filter_parcels_by_shape(invalid, shape_config)
```

**Regression protected**

Pins true-null handling and prevents textual or malformed null-like values from changing the contract.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_null_parcel_id_fails(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
    invalid = parcels.copy()
    invalid.loc[0, "parcel_id"] = None

    with pytest.raises(ParcelFilterError, match="must not be null"):
        filter_parcels_by_shape(invalid, shape_config)
```

### `test_duplicate_parcel_id_fails`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`), `shape_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
invalid = parcels.copy()
invalid.loc[1, "parcel_id"] = invalid.loc[0, "parcel_id"]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ParcelFilterError, match="must be unique"):
        filter_parcels_by_shape(invalid, shape_config)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_duplicate_parcel_id_fails(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
    invalid = parcels.copy()
    invalid.loc[1, "parcel_id"] = invalid.loc[0, "parcel_id"]

    with pytest.raises(ParcelFilterError, match="must be unique"):
        filter_parcels_by_shape(invalid, shape_config)
```

### `test_unknown_crs_fails`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`), `shape_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
invalid = parcels.set_crs(None, allow_override=True)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ParcelFilterError, match="known CRS"):
        filter_parcels_by_shape(invalid, shape_config)
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_unknown_crs_fails(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
    invalid = parcels.set_crs(None, allow_override=True)

    with pytest.raises(ParcelFilterError, match="known CRS"):
        filter_parcels_by_shape(invalid, shape_config)
```

### `test_unexpected_or_null_shape_status_fails`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`), `shape_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `status`.

**Setup**

```python
invalid = parcels.copy()
invalid.loc[0, "shape_status"] = status
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ParcelFilterError, match="Unexpected shape_status"):
        filter_parcels_by_shape(invalid, shape_config)
```

**Regression protected**

Pins true-null handling and prevents textual or malformed null-like values from changing the contract.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_unexpected_or_null_shape_status_fails(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
    status: str | None,
) -> None:
    invalid = parcels.copy()
    invalid.loc[0, "shape_status"] = status

    with pytest.raises(ParcelFilterError, match="Unexpected shape_status"):
        filter_parcels_by_shape(invalid, shape_config)
```

### `test_non_finite_known_metric_on_valid_row_fails`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`), `shape_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `column`.

**Setup**

```python
invalid = parcels.copy()
invalid.loc[0, column] = float("inf")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ParcelFilterError, match="numeric and finite"):
        filter_parcels_by_shape(invalid, shape_config)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_non_finite_known_metric_on_valid_row_fails(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
    column: str,
) -> None:
    invalid = parcels.copy()
    invalid.loc[0, column] = float("inf")

    with pytest.raises(ParcelFilterError, match="numeric and finite"):
        filter_parcels_by_shape(invalid, shape_config)
```

### `test_valid_shape_requires_strict_positive_width`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`), `shape_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `width`.

**Setup**

```python
invalid = parcels.copy()
invalid["width_m"] = invalid["width_m"].astype(object)
invalid.loc[0, "width_m"] = width
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(
        ParcelFilterError,
        match="width_m must be (numeric and finite|greater than zero)",
    ):
        filter_parcels_by_shape(invalid, shape_config)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_valid_shape_requires_strict_positive_width(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
    width: object,
) -> None:
    invalid = parcels.copy()
    invalid["width_m"] = invalid["width_m"].astype(object)
    invalid.loc[0, "width_m"] = width

    with pytest.raises(
        ParcelFilterError,
        match="width_m must be (numeric and finite|greater than zero)",
    ):
        filter_parcels_by_shape(invalid, shape_config)
```

### `test_valid_shape_requires_ratio_at_least_one`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`), `shape_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `ratio`.

**Setup**

```python
invalid = parcels.copy()
invalid["length_width_ratio"] = invalid["length_width_ratio"].astype(object)
invalid.loc[0, "length_width_ratio"] = ratio
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(
        ParcelFilterError,
        match="length_width_ratio must be (numeric and finite|at least one)",
    ):
        filter_parcels_by_shape(invalid, shape_config)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_valid_shape_requires_ratio_at_least_one(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
    ratio: object,
) -> None:
    invalid = parcels.copy()
    invalid["length_width_ratio"] = invalid["length_width_ratio"].astype(object)
    invalid.loc[0, "length_width_ratio"] = ratio

    with pytest.raises(
        ParcelFilterError,
        match="length_width_ratio must be (numeric and finite|at least one)",
    ):
        filter_parcels_by_shape(invalid, shape_config)
```

### `test_negative_ratio_cannot_pass_permissive_thresholds`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`), `shape_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
invalid = parcels.copy()
invalid.loc[0, "width_m"] = 20
invalid.loc[0, "length_width_ratio"] = -1
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ParcelFilterError, match="length_width_ratio must be at least one"):
        filter_parcels_by_shape(invalid, shape_config)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_negative_ratio_cannot_pass_permissive_thresholds(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
) -> None:
    invalid = parcels.copy()
    invalid.loc[0, "width_m"] = 20
    invalid.loc[0, "length_width_ratio"] = -1

    with pytest.raises(ParcelFilterError, match="length_width_ratio must be at least one"):
        filter_parcels_by_shape(invalid, shape_config)
```

### `test_disabled_policy_is_an_exact_passthrough`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
assert_geodataframe_equal(retained, parcels)
assert_geodataframe_equal(rejected, parcels.iloc[0:0])
for column in (
        "shape_rejection_reason",
        "shape_policy_version",
        "shape_policy_min_width_m",
        "shape_policy_max_ratio",
    ):
        assert column not in retained.columns
        assert column not in rejected.columns
```

**Action**

```python
disabled = ShapeScreeningConfig(enabled=False)
retained, rejected = filter_parcels_by_shape(parcels, disabled)
```

**Expected result**

```python
# Completion without an exception is the asserted outcome.
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_disabled_policy_is_an_exact_passthrough(parcels: gpd.GeoDataFrame) -> None:
    disabled = ShapeScreeningConfig(enabled=False)

    retained, rejected = filter_parcels_by_shape(parcels, disabled)

    assert_geodataframe_equal(retained, parcels)
    assert_geodataframe_equal(rejected, parcels.iloc[0:0])
    for column in (
        "shape_rejection_reason",
        "shape_policy_version",
        "shape_policy_min_width_m",
        "shape_policy_max_ratio",
    ):
        assert column not in retained.columns
        assert column not in rejected.columns
```

### `test_different_configs_change_results_for_same_parcels`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
permissive = _shape_config(
        min_width_m=10,
        max_length_width_ratio=12,
        policy_version="permissive",
    )
restrictive = _shape_config(
        min_width_m=18,
        max_length_width_ratio=6,
        policy_version="restrictive",
    )
```

**Action**

```python
permissive_retained, _ = filter_parcels_by_shape(parcels, permissive)
restrictive_retained, _ = filter_parcels_by_shape(parcels, restrictive)
```

**Expected result**

```python
assert set(permissive_retained["parcel_id"]) == {
        "at-boundaries",
        "passing",
        "width-below",
        "ratio-above",
        "both-thresholds-fail",
    }
assert set(restrictive_retained["parcel_id"]) == {"passing"}
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_different_configs_change_results_for_same_parcels(
    parcels: gpd.GeoDataFrame,
) -> None:
    permissive = _shape_config(
        min_width_m=10,
        max_length_width_ratio=12,
        policy_version="permissive",
    )
    restrictive = _shape_config(
        min_width_m=18,
        max_length_width_ratio=6,
        policy_version="restrictive",
    )

    permissive_retained, _ = filter_parcels_by_shape(parcels, permissive)
    restrictive_retained, _ = filter_parcels_by_shape(parcels, restrictive)

    assert set(permissive_retained["parcel_id"]) == {
        "at-boundaries",
        "passing",
        "width-below",
        "ratio-above",
        "both-thresholds-fail",
    }
    assert set(restrictive_retained["parcel_id"]) == {"passing"}
```

### `test_valid_shape_requires_complete_metrics_even_when_screening_disabled`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `column`.

**Setup**

```python
invalid = parcels.copy()
invalid.loc[0, column] = None
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ParcelFilterError, match="complete|must not be null"):
        filter_parcels_by_shape(invalid, ShapeScreeningConfig(enabled=False))
```

**Regression protected**

Pins true-null handling and prevents textual or malformed null-like values from changing the contract.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_valid_shape_requires_complete_metrics_even_when_screening_disabled(
    parcels: gpd.GeoDataFrame,
    column: str,
) -> None:
    invalid = parcels.copy()
    invalid.loc[0, column] = None

    with pytest.raises(ParcelFilterError, match="complete|must not be null"):
        filter_parcels_by_shape(invalid, ShapeScreeningConfig(enabled=False))
```

### `test_valid_shape_rejects_every_incomplete_metric_form`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`), `shape_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `ratio`, `width`.

**Setup**

```python
invalid = parcels.copy()
invalid.loc[0, "width_m"] = width
invalid.loc[0, "length_width_ratio"] = ratio
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ParcelFilterError, match="complete"):
        filter_parcels_by_shape(invalid, shape_config)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_valid_shape_rejects_every_incomplete_metric_form(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
    width: float | None,
    ratio: float | None,
) -> None:
    invalid = parcels.copy()
    invalid.loc[0, "width_m"] = width
    invalid.loc[0, "length_width_ratio"] = ratio

    with pytest.raises(ParcelFilterError, match="complete"):
        filter_parcels_by_shape(invalid, shape_config)
```

### `test_shape_filter_rejects_plain_dataframe`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`), `shape_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ParcelFilterError, match="GeoDataFrame"):
        filter_parcels_by_shape(
            pd.DataFrame(parcels),  # type: ignore[arg-type]
            shape_config,
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_shape_filter_rejects_plain_dataframe(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
    with pytest.raises(ParcelFilterError, match="GeoDataFrame"):
        filter_parcels_by_shape(
            pd.DataFrame(parcels),  # type: ignore[arg-type]
            shape_config,
        )
```

### `test_shape_filter_rejects_duplicate_columns`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`), `shape_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
duplicate = gpd.GeoDataFrame(
        pd.concat([parcels, parcels[["parcel_id"]]], axis=1),
        geometry="geometry",
        crs=parcels.crs,
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ParcelFilterError, match="columns.*unique"):
        filter_parcels_by_shape(duplicate, shape_config)
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_shape_filter_rejects_duplicate_columns(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
    duplicate = gpd.GeoDataFrame(
        pd.concat([parcels, parcels[["parcel_id"]]], axis=1),
        geometry="geometry",
        crs=parcels.crs,
    )

    with pytest.raises(ParcelFilterError, match="columns.*unique"):
        filter_parcels_by_shape(duplicate, shape_config)
```

### `test_shape_filter_rejects_unreadable_crs`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`), `shape_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
invalid = parcels.copy()
invalid.geometry.array._crs = "not-a-crs"
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ParcelFilterError, match="CRS"):
        filter_parcels_by_shape(invalid, shape_config)
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_shape_filter_rejects_unreadable_crs(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
    invalid = parcels.copy()
    invalid.geometry.array._crs = "not-a-crs"

    with pytest.raises(ParcelFilterError, match="CRS"):
        filter_parcels_by_shape(invalid, shape_config)
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

# `tests/unit/test_filter_parcels.py`

## File identity

- Repository path: `tests/unit/test_filter_parcels.py`
- File type: Python test
- Layer: unit/regression test
- Domain: test
- Responsibility: Provides complete unit and regression coverage for the `filter_parcels` contracts exercised in this file.
- Source SHA256: `d2b7a4bd8e16d349973ac8c21c1609dada89ae0604c6723f72b997660c2eaf1a`

## 1. Purpose

Provides complete unit and regression coverage for the `filter_parcels` contracts exercised in this file.

## 2. Position in LandScout architecture

This file belongs to the **unit/regression test** layer and the **test** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `None.`

### Third-party packages

- `import geopandas as gpd`
- `import pandas as pd`
- `import pytest`
- `from shapely.geometry import Polygon`

### Internal LandScout imports

- `from landscout.config import ParcelConfig`
- `from landscout.stages.filter_parcels import ParcelFilterError, filter_parcels_by_area`

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

### `area_config` — pytest fixture

- Scope: `function` (decorator `pytest.fixture`).
- Returned/yielded object expression(s): `ParcelConfig(min_area_m2=2000, max_area_m2=15000)`.
- Tests requesting it by parameter injection: `test_minimum_boundary_is_included`, `test_maximum_boundary_is_included`, `test_rejected_parcel_has_expected_reason`, `test_no_parcel_disappears`, `test_missing_parcel_id_fails`, `test_null_parcel_id_fails`, `test_duplicate_parcel_id_fails`, `test_candidate_and_rejected_ids_do_not_overlap`, `test_exact_parcel_ids_are_preserved`, `test_valid_geometry_requires_strict_positive_finite_area`, `test_area_filter_requires_exact_non_empty_parcel_ids`, `test_area_filter_rejects_plain_dataframe`, `test_area_filter_rejects_duplicate_columns`, `test_area_filter_rejects_malformed_spatial_envelope`, `test_area_filter_rejects_noncanonical_geometry_status`.

**Complete fixture implementation**

```python
def area_config() -> ParcelConfig:
    return ParcelConfig(min_area_m2=2000, max_area_m2=15000)
```

### `parcels` — pytest fixture

- Scope: `function` (decorator `pytest.fixture`).
- Returned/yielded object expression(s): `gpd.GeoDataFrame({'parcel_id': ['at-minimum', 'at-maximum', 'below-minimum', 'above-maximum', 'invalid-geometry', 'unknown-area'], 'geometry_status': ['VALID', 'VALID', 'VALID', 'VALID', 'INVALID', 'INVALID'], 'area_m2': [2000.0, 15000.0, 1999.0, 15001.0, 5000.0, None], 'commune_code': ['31395'] * 6}, geometry=[geometry] * 6, crs='EPSG:4326')`.
- Tests requesting it by parameter injection: `test_minimum_boundary_is_included`, `test_maximum_boundary_is_included`, `test_rejected_parcel_has_expected_reason`, `test_no_parcel_disappears`, `test_thresholds_come_from_config`, `test_missing_parcel_id_fails`, `test_null_parcel_id_fails`, `test_duplicate_parcel_id_fails`, `test_candidate_and_rejected_ids_do_not_overlap`, `test_exact_parcel_ids_are_preserved`, `test_valid_geometry_requires_strict_positive_finite_area`, `test_area_filter_requires_exact_non_empty_parcel_ids`, `test_area_filter_rejects_plain_dataframe`, `test_area_filter_rejects_duplicate_columns`, `test_area_filter_rejects_malformed_spatial_envelope`, `test_area_filter_rejects_noncanonical_geometry_status`.

**Complete fixture implementation**

```python
def parcels() -> gpd.GeoDataFrame:
    geometry = Polygon([(2.0, 43.0), (2.1, 43.0), (2.1, 43.1), (2.0, 43.0)])
    return gpd.GeoDataFrame(
        {
            "parcel_id": [
                "at-minimum",
                "at-maximum",
                "below-minimum",
                "above-maximum",
                "invalid-geometry",
                "unknown-area",
            ],
            "geometry_status": [
                "VALID",
                "VALID",
                "VALID",
                "VALID",
                "INVALID",
                "INVALID",
            ],
            "area_m2": [2000.0, 15000.0, 1999.0, 15001.0, 5000.0, None],
            "commune_code": ["31395"] * 6,
        },
        geometry=[geometry] * 6,
        crs="EPSG:4326",
    )
```

### `test_minimum_boundary_is_included`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`), `area_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
candidates, _ = filter_parcels_by_area(parcels, area_config)
```

**Expected result**

```python
assert "at-minimum" in set(candidates["parcel_id"])
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_minimum_boundary_is_included(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
    candidates, _ = filter_parcels_by_area(parcels, area_config)

    assert "at-minimum" in set(candidates["parcel_id"])
```

### `test_maximum_boundary_is_included`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`), `area_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
candidates, _ = filter_parcels_by_area(parcels, area_config)
```

**Expected result**

```python
assert "at-maximum" in set(candidates["parcel_id"])
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_maximum_boundary_is_included(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
    candidates, _ = filter_parcels_by_area(parcels, area_config)

    assert "at-maximum" in set(candidates["parcel_id"])
```

### `test_rejected_parcel_has_expected_reason`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`), `area_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `expected_reason`, `parcel_id`.

**Setup**

```python
row = rejected.loc[rejected["parcel_id"] == parcel_id].iloc[0]
```

**Action**

```python
_, rejected = filter_parcels_by_area(parcels, area_config)
```

**Expected result**

```python
assert row["rejection_reason"] == expected_reason
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_rejected_parcel_has_expected_reason(
    parcels: gpd.GeoDataFrame,
    area_config: ParcelConfig,
    parcel_id: str,
    expected_reason: str,
) -> None:
    _, rejected = filter_parcels_by_area(parcels, area_config)

    row = rejected.loc[rejected["parcel_id"] == parcel_id].iloc[0]
    assert row["rejection_reason"] == expected_reason
```

### `test_no_parcel_disappears`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`), `area_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
candidates, rejected = filter_parcels_by_area(parcels, area_config)
```

**Expected result**

```python
assert len(parcels) == len(candidates) + len(rejected)
assert set(parcels["parcel_id"]) == set(candidates["parcel_id"]) | set(
        rejected["parcel_id"]
    )
assert candidates.crs == parcels.crs
assert rejected.crs == parcels.crs
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_no_parcel_disappears(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
    candidates, rejected = filter_parcels_by_area(parcels, area_config)

    assert len(parcels) == len(candidates) + len(rejected)
    assert set(parcels["parcel_id"]) == set(candidates["parcel_id"]) | set(
        rejected["parcel_id"]
    )
    assert candidates.crs == parcels.crs
    assert rejected.crs == parcels.crs
```

### `test_thresholds_come_from_config`

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
custom_config = ParcelConfig(min_area_m2=1999, max_area_m2=2000)
candidates, _ = filter_parcels_by_area(parcels, custom_config)
```

**Expected result**

```python
assert set(candidates["parcel_id"]) == {"below-minimum", "at-minimum"}
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_thresholds_come_from_config(parcels: gpd.GeoDataFrame) -> None:
    custom_config = ParcelConfig(min_area_m2=1999, max_area_m2=2000)

    candidates, _ = filter_parcels_by_area(parcels, custom_config)

    assert set(candidates["parcel_id"]) == {"below-minimum", "at-minimum"}
```

### `test_missing_parcel_id_fails`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`), `area_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
without_id = parcels.drop(columns=["parcel_id"])
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ParcelFilterError, match="parcel_id"):
        filter_parcels_by_area(without_id, area_config)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_missing_parcel_id_fails(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
    without_id = parcels.drop(columns=["parcel_id"])

    with pytest.raises(ParcelFilterError, match="parcel_id"):
        filter_parcels_by_area(without_id, area_config)
```

### `test_null_parcel_id_fails`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`), `area_config` (local fixture, scope `function`).
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
with pytest.raises(ParcelFilterError, match="null"):
        filter_parcels_by_area(with_null, area_config)
```

**Regression protected**

Pins true-null handling and prevents textual or malformed null-like values from changing the contract.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_null_parcel_id_fails(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
    with_null = parcels.copy()
    with_null.loc[0, "parcel_id"] = None

    with pytest.raises(ParcelFilterError, match="null"):
        filter_parcels_by_area(with_null, area_config)
```

### `test_duplicate_parcel_id_fails`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`), `area_config` (local fixture, scope `function`).
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
with pytest.raises(ParcelFilterError, match="unique"):
        filter_parcels_by_area(with_duplicate, area_config)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_duplicate_parcel_id_fails(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
    with_duplicate = parcels.copy()
    with_duplicate.loc[1, "parcel_id"] = with_duplicate.loc[0, "parcel_id"]

    with pytest.raises(ParcelFilterError, match="unique"):
        filter_parcels_by_area(with_duplicate, area_config)
```

### `test_candidate_and_rejected_ids_do_not_overlap`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`), `area_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
candidates, rejected = filter_parcels_by_area(parcels, area_config)
```

**Expected result**

```python
assert set(candidates["parcel_id"]).isdisjoint(set(rejected["parcel_id"]))
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_candidate_and_rejected_ids_do_not_overlap(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
    candidates, rejected = filter_parcels_by_area(parcels, area_config)

    assert set(candidates["parcel_id"]).isdisjoint(set(rejected["parcel_id"]))
```

### `test_exact_parcel_ids_are_preserved`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`), `area_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
output_ids = list(candidates["parcel_id"]) + list(rejected["parcel_id"])
```

**Action**

```python
candidates, rejected = filter_parcels_by_area(parcels, area_config)
```

**Expected result**

```python
assert len(output_ids) == len(set(output_ids))
assert set(output_ids) == set(parcels["parcel_id"])
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_exact_parcel_ids_are_preserved(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
    candidates, rejected = filter_parcels_by_area(parcels, area_config)

    output_ids = list(candidates["parcel_id"]) + list(rejected["parcel_id"])
    assert len(output_ids) == len(set(output_ids))
    assert set(output_ids) == set(parcels["parcel_id"])
```

### `test_valid_geometry_requires_strict_positive_finite_area`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`), `area_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `area`.

**Setup**

```python
invalid = parcels.copy()
invalid["area_m2"] = invalid["area_m2"].astype(object)
invalid.loc[0, "area_m2"] = area
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ParcelFilterError, match="strict positive finite numeric"):
        filter_parcels_by_area(invalid, area_config)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_valid_geometry_requires_strict_positive_finite_area(
    parcels: gpd.GeoDataFrame,
    area_config: ParcelConfig,
    area: object,
) -> None:
    invalid = parcels.copy()
    invalid["area_m2"] = invalid["area_m2"].astype(object)
    invalid.loc[0, "area_m2"] = area

    with pytest.raises(ParcelFilterError, match="strict positive finite numeric"):
        filter_parcels_by_area(invalid, area_config)
```

### `test_area_filter_requires_exact_non_empty_parcel_ids`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`), `area_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `parcel_id`.

**Setup**

```python
invalid = parcels.copy()
invalid["parcel_id"] = invalid["parcel_id"].astype(object)
invalid.loc[0, "parcel_id"] = parcel_id
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ParcelFilterError, match="exact non-empty strings"):
        filter_parcels_by_area(invalid, area_config)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_area_filter_requires_exact_non_empty_parcel_ids(
    parcels: gpd.GeoDataFrame,
    area_config: ParcelConfig,
    parcel_id: object,
) -> None:
    invalid = parcels.copy()
    invalid["parcel_id"] = invalid["parcel_id"].astype(object)
    invalid.loc[0, "parcel_id"] = parcel_id

    with pytest.raises(ParcelFilterError, match="exact non-empty strings"):
        filter_parcels_by_area(invalid, area_config)
```

### `test_area_filter_rejects_plain_dataframe`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`), `area_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
plain = pd.DataFrame(parcels)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ParcelFilterError, match="GeoDataFrame"):
        filter_parcels_by_area(plain, area_config)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_area_filter_rejects_plain_dataframe(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
    plain = pd.DataFrame(parcels)

    with pytest.raises(ParcelFilterError, match="GeoDataFrame"):
        filter_parcels_by_area(plain, area_config)
```

### `test_area_filter_rejects_duplicate_columns`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`), `area_config` (local fixture, scope `function`).
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
        filter_parcels_by_area(duplicate, area_config)
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_area_filter_rejects_duplicate_columns(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
    duplicate = gpd.GeoDataFrame(
        pd.concat([parcels, parcels[["parcel_id"]]], axis=1),
        geometry="geometry",
        crs=parcels.crs,
    )

    with pytest.raises(ParcelFilterError, match="columns.*unique"):
        filter_parcels_by_area(duplicate, area_config)
```

### `test_area_filter_rejects_malformed_spatial_envelope`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`), `area_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `mode`.

**Setup**

```python
invalid = parcels.copy()
if mode == "missing_geometry":
        invalid = invalid.drop(columns="geometry")
    elif mode == "missing_crs":
        invalid = invalid.set_crs(None, allow_override=True)
    else:
        invalid.geometry.array._crs = "not-a-crs"
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ParcelFilterError, match="geometry|CRS"):
        filter_parcels_by_area(invalid, area_config)
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_area_filter_rejects_malformed_spatial_envelope(
    parcels: gpd.GeoDataFrame,
    area_config: ParcelConfig,
    mode: str,
) -> None:
    invalid = parcels.copy()
    if mode == "missing_geometry":
        invalid = invalid.drop(columns="geometry")
    elif mode == "missing_crs":
        invalid = invalid.set_crs(None, allow_override=True)
    else:
        invalid.geometry.array._crs = "not-a-crs"

    with pytest.raises(ParcelFilterError, match="geometry|CRS"):
        filter_parcels_by_area(invalid, area_config)
```

### `test_area_filter_rejects_noncanonical_geometry_status`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `parcels` (local fixture, scope `function`), `area_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `geometry_status`.

**Setup**

```python
invalid = parcels.copy()
invalid["geometry_status"] = invalid["geometry_status"].astype(object)
invalid.loc[0, "geometry_status"] = geometry_status
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ParcelFilterError, match="geometry_status"):
        filter_parcels_by_area(invalid, area_config)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_area_filter_rejects_noncanonical_geometry_status(
    parcels: gpd.GeoDataFrame,
    area_config: ParcelConfig,
    geometry_status: object,
) -> None:
    invalid = parcels.copy()
    invalid["geometry_status"] = invalid["geometry_status"].astype(object)
    invalid.loc[0, "geometry_status"] = geometry_status

    with pytest.raises(ParcelFilterError, match="geometry_status"):
        filter_parcels_by_area(invalid, area_config)
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

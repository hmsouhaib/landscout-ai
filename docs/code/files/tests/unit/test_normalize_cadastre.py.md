# `tests/unit/test_normalize_cadastre.py`

## File identity

- Repository path: `tests/unit/test_normalize_cadastre.py`
- File type: Python test
- Layer: unit/regression test
- Domain: test
- Responsibility: Provides complete unit and regression coverage for the `normalize_cadastre` contracts exercised in this file.
- Source SHA256: `2ee56ea4fa80743a6834d5fc1449e92e5509b2e39071cc2035a80b11e50b3f86`

## 1. Purpose

Provides complete unit and regression coverage for the `normalize_cadastre` contracts exercised in this file.

## 2. Position in LandScout architecture

This file belongs to the **unit/regression test** layer and the **test** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from copy import deepcopy`

### Third-party packages

- `import geopandas as gpd`
- `import pandas as pd`
- `import pytest`
- `from geopandas.testing import assert_geodataframe_equal`
- `from shapely.geometry import LineString, MultiPolygon, Point, Polygon`

### Internal LandScout imports

- `from landscout.stages.normalize_cadastre import (
    CadastreNormalizationError,
    normalize_cadastre_parcels,
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

### `_source_parcels`

**Exact signature**

```python
def _source_parcels(
    geometries: list[object],
    ids: list[object] | None = None,
    crs: str | None = "EPSG:4326",
) -> gpd.GeoDataFrame:
```

**Purpose**

Private `test` helper for source parcels; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
gpd.GeoDataFrame({'id': parcel_ids, 'commune': ['31395'] * count, 'prefixe': ['000'] * count, 'section': ['A'] * count, 'numero': [str(index + 1) for index in range(count)], 'contenance': [1000.0] * count, 'arpente': [False] * count, 'created': ['2020-01-01'] * count, 'updated': ['2024-01-01'] * count}, geometry=geometries, crs=crs)
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

- direct call or construction: `tests/unit/test_normalize_cadastre.py::test_field_normalization` via `_source_parcels`.
- direct call or construction: `tests/unit/test_normalize_cadastre.py::test_lambert93_area_calculation` via `_source_parcels`.
- direct call or construction: `tests/unit/test_normalize_cadastre.py::test_output_geometry_stays_in_wgs84` via `_source_parcels`.
- direct call or construction: `tests/unit/test_normalize_cadastre.py::test_invalid_geometry_is_preserved_with_null_area` via `_source_parcels`.
- direct call or construction: `tests/unit/test_normalize_cadastre.py::test_missing_crs_fails` via `_source_parcels`.
- direct call or construction: `tests/unit/test_normalize_cadastre.py::test_duplicate_parcel_id_fails` via `_source_parcels`.
- direct call or construction: `tests/unit/test_normalize_cadastre.py::test_duplicate_columns_are_rejected` via `_source_parcels`.
- direct call or construction: `tests/unit/test_normalize_cadastre.py::test_projected_source_crs_is_rejected` via `_source_parcels`.
- direct call or construction: `tests/unit/test_normalize_cadastre.py::test_parcel_id_must_be_an_exact_nonempty_string` via `_source_parcels`.
- direct call or construction: `tests/unit/test_normalize_cadastre.py::test_non_polygonal_geometry_is_rejected` via `_source_parcels`.
- direct call or construction: `tests/unit/test_normalize_cadastre.py::test_valid_multipolygon_is_accepted` via `_source_parcels`.
- direct call or construction: `tests/unit/test_normalize_cadastre.py::test_null_and_empty_geometry_are_preserved_as_invalid` via `_source_parcels`.
- direct call or construction: `tests/unit/test_normalize_cadastre.py::test_normalization_does_not_mutate_input` via `_source_parcels`.
- direct call or construction: `tests/unit/test_normalize_cadastre.py::test_every_cadastral_identity_field_requires_an_exact_nonempty_string` via `_source_parcels`.
- direct call or construction: `tests/unit/test_normalize_cadastre.py::test_commune_requires_canonical_french_insee_identity` via `_source_parcels`.
- direct call or construction: `tests/unit/test_normalize_cadastre.py::test_commune_accepts_canonical_french_insee_identity` via `_source_parcels`.

**Complete source-ordered implementation**

```python
def _source_parcels(
    geometries: list[object],
    ids: list[object] | None = None,
    crs: str | None = "EPSG:4326",
) -> gpd.GeoDataFrame:
    parcel_ids = ids or [f"parcel-{index}" for index in range(len(geometries))]
    count = len(geometries)
    return gpd.GeoDataFrame(
        {
            "id": parcel_ids,
            "commune": ["31395"] * count,
            "prefixe": ["000"] * count,
            "section": ["A"] * count,
            "numero": [str(index + 1) for index in range(count)],
            "contenance": [1000.0] * count,
            "arpente": [False] * count,
            "created": ["2020-01-01"] * count,
            "updated": ["2024-01-01"] * count,
        },
        geometry=geometries,
        crs=crs,
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `valid_polygon` — pytest fixture

- Scope: `function` (decorator `pytest.fixture`).
- Returned/yielded object expression(s): `Polygon([(2.35, 43.45), (2.36, 43.45), (2.36, 43.46), (2.35, 43.45)])`.
- Tests requesting it by parameter injection: `test_field_normalization`, `test_lambert93_area_calculation`, `test_output_geometry_stays_in_wgs84`, `test_missing_crs_fails`, `test_duplicate_parcel_id_fails`, `test_duplicate_columns_are_rejected`, `test_projected_source_crs_is_rejected`, `test_parcel_id_must_be_an_exact_nonempty_string`, `test_valid_multipolygon_is_accepted`, `test_normalization_does_not_mutate_input`, `test_every_cadastral_identity_field_requires_an_exact_nonempty_string`, `test_commune_requires_canonical_french_insee_identity`, `test_commune_accepts_canonical_french_insee_identity`.

**Complete fixture implementation**

```python
def valid_polygon() -> Polygon:
    return Polygon(
        [(2.35, 43.45), (2.36, 43.45), (2.36, 43.46), (2.35, 43.45)]
    )
```

### `test_field_normalization`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `valid_polygon` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
normalized = normalize_cadastre_parcels(_source_parcels([valid_polygon]))
```

**Expected result**

```python
assert list(normalized.columns) == [
        "parcel_id",
        "commune_code",
        "section_prefix",
        "section",
        "parcel_number",
        "source_contenance",
        "source_arpente",
        "source_created_at",
        "source_updated_at",
        "geometry_status",
        "area_m2",
        "geometry",
    ]
assert normalized.iloc[0]["parcel_id"] == "parcel-0"
assert normalized.iloc[0]["commune_code"] == "31395"
assert normalized.iloc[0]["geometry_status"] == "VALID"
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_field_normalization(valid_polygon: Polygon) -> None:
    normalized = normalize_cadastre_parcels(_source_parcels([valid_polygon]))

    assert list(normalized.columns) == [
        "parcel_id",
        "commune_code",
        "section_prefix",
        "section",
        "parcel_number",
        "source_contenance",
        "source_arpente",
        "source_created_at",
        "source_updated_at",
        "geometry_status",
        "area_m2",
        "geometry",
    ]
    assert normalized.iloc[0]["parcel_id"] == "parcel-0"
    assert normalized.iloc[0]["commune_code"] == "31395"
    assert normalized.iloc[0]["geometry_status"] == "VALID"
```

### `test_lambert93_area_calculation`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `valid_polygon` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
source = _source_parcels([valid_polygon])
expected_area = source.to_crs("EPSG:2154").geometry.area.iloc[0]
```

**Action**

```python
normalized = normalize_cadastre_parcels(source)
```

**Expected result**

```python
assert normalized.iloc[0]["area_m2"] == pytest.approx(expected_area)
assert normalized.iloc[0]["area_m2"] > 0
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_lambert93_area_calculation(valid_polygon: Polygon) -> None:
    source = _source_parcels([valid_polygon])
    expected_area = source.to_crs("EPSG:2154").geometry.area.iloc[0]

    normalized = normalize_cadastre_parcels(source)

    assert normalized.iloc[0]["area_m2"] == pytest.approx(expected_area)
    assert normalized.iloc[0]["area_m2"] > 0
```

### `test_output_geometry_stays_in_wgs84`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `valid_polygon` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
source = _source_parcels([valid_polygon])
```

**Action**

```python
normalized = normalize_cadastre_parcels(source)
```

**Expected result**

```python
assert normalized.crs is not None
assert normalized.crs.to_epsg() == 4326
assert normalized.geometry.iloc[0].equals_exact(valid_polygon, tolerance=0)
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_output_geometry_stays_in_wgs84(valid_polygon: Polygon) -> None:
    source = _source_parcels([valid_polygon])

    normalized = normalize_cadastre_parcels(source)

    assert normalized.crs is not None
    assert normalized.crs.to_epsg() == 4326
    assert normalized.geometry.iloc[0].equals_exact(valid_polygon, tolerance=0)
```

### `test_invalid_geometry_is_preserved_with_null_area`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
bow_tie = Polygon(
        [(2.35, 43.45), (2.36, 43.46), (2.35, 43.46), (2.36, 43.45)]
    )
```

**Action**

```python
normalized = normalize_cadastre_parcels(_source_parcels([bow_tie]))
```

**Expected result**

```python
assert not bow_tie.is_valid
assert normalized.iloc[0]["geometry_status"] == "INVALID"
assert normalized["area_m2"].isna().iloc[0]
assert normalized.geometry.iloc[0].equals_exact(bow_tie, tolerance=0)
```

**Regression protected**

Pins true-null handling and prevents textual or malformed null-like values from changing the contract.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_invalid_geometry_is_preserved_with_null_area() -> None:
    bow_tie = Polygon(
        [(2.35, 43.45), (2.36, 43.46), (2.35, 43.46), (2.36, 43.45)]
    )
    assert not bow_tie.is_valid

    normalized = normalize_cadastre_parcels(_source_parcels([bow_tie]))

    assert normalized.iloc[0]["geometry_status"] == "INVALID"
    assert normalized["area_m2"].isna().iloc[0]
    assert normalized.geometry.iloc[0].equals_exact(bow_tie, tolerance=0)
```

### `test_missing_crs_fails`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `valid_polygon` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
source = _source_parcels([valid_polygon], crs=None)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(CadastreNormalizationError, match="CRS"):
        normalize_cadastre_parcels(source)
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_missing_crs_fails(valid_polygon: Polygon) -> None:
    source = _source_parcels([valid_polygon], crs=None)

    with pytest.raises(CadastreNormalizationError, match="CRS"):
        normalize_cadastre_parcels(source)
```

### `test_duplicate_parcel_id_fails`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `valid_polygon` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
source = _source_parcels(
        [valid_polygon, valid_polygon], ids=["duplicate", "duplicate"]
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(CadastreNormalizationError, match="unique"):
        normalize_cadastre_parcels(source)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_duplicate_parcel_id_fails(valid_polygon: Polygon) -> None:
    source = _source_parcels(
        [valid_polygon, valid_polygon], ids=["duplicate", "duplicate"]
    )

    with pytest.raises(CadastreNormalizationError, match="unique"):
        normalize_cadastre_parcels(source)
```

### `test_non_geodataframe_is_rejected_safely`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
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
with pytest.raises(CadastreNormalizationError, match="GeoDataFrame"):
        normalize_cadastre_parcels(pd.DataFrame({"id": ["parcel"]}))
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_non_geodataframe_is_rejected_safely() -> None:
    with pytest.raises(CadastreNormalizationError, match="GeoDataFrame"):
        normalize_cadastre_parcels(pd.DataFrame({"id": ["parcel"]}))
```

### `test_duplicate_columns_are_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `valid_polygon` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
source = _source_parcels([valid_polygon])
duplicate = gpd.GeoDataFrame(
        pd.concat([source, source[["id"]]], axis=1),
        geometry="geometry",
        crs=source.crs,
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(CadastreNormalizationError, match="columns.*unique"):
        normalize_cadastre_parcels(duplicate)
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_duplicate_columns_are_rejected(valid_polygon: Polygon) -> None:
    source = _source_parcels([valid_polygon])
    duplicate = gpd.GeoDataFrame(
        pd.concat([source, source[["id"]]], axis=1),
        geometry="geometry",
        crs=source.crs,
    )

    with pytest.raises(CadastreNormalizationError, match="columns.*unique"):
        normalize_cadastre_parcels(duplicate)
```

### `test_projected_source_crs_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `valid_polygon` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
source = _source_parcels([valid_polygon]).to_crs("EPSG:2154")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(CadastreNormalizationError, match="4326"):
        normalize_cadastre_parcels(source)
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_projected_source_crs_is_rejected(valid_polygon: Polygon) -> None:
    source = _source_parcels([valid_polygon]).to_crs("EPSG:2154")

    with pytest.raises(CadastreNormalizationError, match="4326"):
        normalize_cadastre_parcels(source)
```

### `test_parcel_id_must_be_an_exact_nonempty_string`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `valid_polygon` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `identifier`.

**Setup**

```python
source = _source_parcels([valid_polygon], ids=[identifier])
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(CadastreNormalizationError, match="parcel_id"):
        normalize_cadastre_parcels(source)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_parcel_id_must_be_an_exact_nonempty_string(
    valid_polygon: Polygon,
    identifier: object,
) -> None:
    source = _source_parcels([valid_polygon], ids=[identifier])

    with pytest.raises(CadastreNormalizationError, match="parcel_id"):
        normalize_cadastre_parcels(source)
```

### `test_non_polygonal_geometry_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `geometry`.

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
with pytest.raises(CadastreNormalizationError, match="Polygon"):
        normalize_cadastre_parcels(_source_parcels([geometry]))
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_non_polygonal_geometry_is_rejected(geometry: object) -> None:
    with pytest.raises(CadastreNormalizationError, match="Polygon"):
        normalize_cadastre_parcels(_source_parcels([geometry]))
```

### `test_valid_multipolygon_is_accepted`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `valid_polygon` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
normalized = normalize_cadastre_parcels(
        _source_parcels([MultiPolygon([valid_polygon])])
    )
```

**Expected result**

```python
assert normalized.loc[0, "geometry_status"] == "VALID"
assert normalized.loc[0, "area_m2"] > 0
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_valid_multipolygon_is_accepted(valid_polygon: Polygon) -> None:
    normalized = normalize_cadastre_parcels(
        _source_parcels([MultiPolygon([valid_polygon])])
    )

    assert normalized.loc[0, "geometry_status"] == "VALID"
    assert normalized.loc[0, "area_m2"] > 0
```

### `test_null_and_empty_geometry_are_preserved_as_invalid`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `geometry`.

**Setup**

```python
if geometry is None:
        assert normalized.geometry.isna().iloc[0]
    else:
        assert normalized.geometry.is_empty.iloc[0]
```

**Action**

```python
normalized = normalize_cadastre_parcels(_source_parcels([geometry]))
```

**Expected result**

```python
assert normalized.loc[0, "geometry_status"] == "INVALID"
assert pd.isna(normalized.loc[0, "area_m2"])
```

**Regression protected**

Pins true-null handling and prevents textual or malformed null-like values from changing the contract.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_null_and_empty_geometry_are_preserved_as_invalid(geometry: object) -> None:
    normalized = normalize_cadastre_parcels(_source_parcels([geometry]))

    assert normalized.loc[0, "geometry_status"] == "INVALID"
    assert pd.isna(normalized.loc[0, "area_m2"])
    if geometry is None:
        assert normalized.geometry.isna().iloc[0]
    else:
        assert normalized.geometry.is_empty.iloc[0]
```

### `test_normalization_does_not_mutate_input`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `valid_polygon` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
source = _source_parcels([valid_polygon])
before = deepcopy(source)
assert_geodataframe_equal(source, before)
```

**Action**

```python
normalize_cadastre_parcels(source)
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
def test_normalization_does_not_mutate_input(valid_polygon: Polygon) -> None:
    source = _source_parcels([valid_polygon])
    before = deepcopy(source)

    normalize_cadastre_parcels(source)

    assert_geodataframe_equal(source, before)
```

### `test_every_cadastral_identity_field_requires_an_exact_nonempty_string`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `valid_polygon` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `column`, `value`.

**Setup**

```python
source = _source_parcels([valid_polygon])
source[column] = source[column].astype(object)
source.loc[0, column] = value
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(CadastreNormalizationError, match=column):
        normalize_cadastre_parcels(source)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_every_cadastral_identity_field_requires_an_exact_nonempty_string(
    valid_polygon: Polygon,
    column: str,
    value: object,
) -> None:
    source = _source_parcels([valid_polygon])
    source[column] = source[column].astype(object)
    source.loc[0, column] = value

    with pytest.raises(CadastreNormalizationError, match=column):
        normalize_cadastre_parcels(source)
```

### `test_commune_requires_canonical_french_insee_identity`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `valid_polygon` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `commune`.

**Setup**

```python
source = _source_parcels([valid_polygon])
source.loc[0, "commune"] = commune
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(CadastreNormalizationError, match="commune"):
        normalize_cadastre_parcels(source)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_commune_requires_canonical_french_insee_identity(
    valid_polygon: Polygon,
    commune: str,
) -> None:
    source = _source_parcels([valid_polygon])
    source.loc[0, "commune"] = commune

    with pytest.raises(CadastreNormalizationError, match="commune"):
        normalize_cadastre_parcels(source)
```

### `test_commune_accepts_canonical_french_insee_identity`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `valid_polygon` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `commune`.

**Setup**

```python
source = _source_parcels([valid_polygon])
source.loc[0, "commune"] = commune
```

**Action**

```python
result = normalize_cadastre_parcels(source)
```

**Expected result**

```python
assert result.loc[0, "commune_code"] == commune
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_commune_accepts_canonical_french_insee_identity(
    valid_polygon: Polygon,
    commune: str,
) -> None:
    source = _source_parcels([valid_polygon])
    source.loc[0, "commune"] = commune

    result = normalize_cadastre_parcels(source)

    assert result.loc[0, "commune_code"] == commune
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

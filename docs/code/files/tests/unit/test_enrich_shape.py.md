# `tests/unit/test_enrich_shape.py`

## File identity

- Repository path: `tests/unit/test_enrich_shape.py`
- File type: Python test
- Layer: unit/regression test
- Domain: test
- Responsibility: Provides complete unit and regression coverage for the `enrich_shape` contracts exercised in this file.
- Source SHA256: `ad4f6b2997ac30b29a5aaa182b882cc7aac0a50abf55b4d97126934b187af21b`

## 1. Purpose

Provides complete unit and regression coverage for the `enrich_shape` contracts exercised in this file.

## 2. Position in LandScout architecture

This file belongs to the **unit/regression test** layer and the **test** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `None.`

### Third-party packages

- `import geopandas as gpd`
- `import pytest`
- `from shapely.affinity import rotate`
- `from shapely.geometry import Point, Polygon`
- `from shapely.geometry.base import BaseGeometry`

### Internal LandScout imports

- `from landscout.geo import LAMBERT93, parcel_shape_metrics_m`
- `from landscout.stages.enrich_shape import (
    DERIVED_METRIC_COLUMNS,
    ShapeEnrichmentError,
    enrich_parcel_shapes,
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

### `_candidate_frame`

**Exact signature**

```python
def _candidate_frame(geometries: list[BaseGeometry]) -> gpd.GeoDataFrame:
```

**Purpose**

Private `test` helper for candidate frame; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
gpd.GeoDataFrame({'parcel_id': [f'parcel-{index}' for index in range(len(geometries))], 'geometry_status': ['VALID'] * len(geometries), 'area_m2': list(projected.area)}, geometry=wgs84, crs='EPSG:4326')
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `projected.to_crs`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_enrich_shape.py::test_square_metrics` via `_candidate_frame`.
- direct call or construction: `tests/unit/test_enrich_shape.py::test_rectangle_metrics` via `_candidate_frame`.
- direct call or construction: `tests/unit/test_enrich_shape.py::test_rotated_rectangle_metrics` via `_candidate_frame`.
- direct call or construction: `tests/unit/test_enrich_shape.py::test_elongated_parcel` via `_candidate_frame`.
- direct call or construction: `tests/unit/test_enrich_shape.py::test_centroid_coordinates` via `_candidate_frame`.
- direct call or construction: `tests/unit/test_enrich_shape.py::test_output_geometry_remains_wgs84` via `_candidate_frame`.
- direct call or construction: `tests/unit/test_enrich_shape.py::test_missing_crs_fails` via `_candidate_frame`.
- direct call or construction: `tests/unit/test_enrich_shape.py::test_missing_parcel_id_fails` via `_candidate_frame`.
- direct call or construction: `tests/unit/test_enrich_shape.py::test_null_parcel_id_fails` via `_candidate_frame`.
- direct call or construction: `tests/unit/test_enrich_shape.py::test_duplicate_parcel_id_fails` via `_candidate_frame`.
- direct call or construction: `tests/unit/test_enrich_shape.py::test_enrichment_requires_exact_non_empty_parcel_ids` via `_candidate_frame`.
- direct call or construction: `tests/unit/test_enrich_shape.py::test_valid_candidate_area_requires_strict_positive_finite_number` via `_candidate_frame`.
- direct call or construction: `tests/unit/test_enrich_shape.py::test_failed_geometry_does_not_remove_other_rows` via `_candidate_frame`.
- direct call or construction: `tests/unit/test_enrich_shape.py::test_exact_parcel_ids_are_preserved` via `_candidate_frame`.
- direct call or construction: `tests/unit/test_enrich_shape.py::test_enrichment_matches_centralized_shape_metrics` via `_candidate_frame`.
- direct call or construction: `tests/unit/test_enrich_shape.py::test_shape_enrichment_rejects_noncanonical_geometry_status` via `_candidate_frame`.

**Complete source-ordered implementation**

```python
def _candidate_frame(geometries: list[BaseGeometry]) -> gpd.GeoDataFrame:
    projected = gpd.GeoSeries(geometries, crs="EPSG:2154")
    wgs84 = projected.to_crs("EPSG:4326")
    return gpd.GeoDataFrame(
        {
            "parcel_id": [f"parcel-{index}" for index in range(len(geometries))],
            "geometry_status": ["VALID"] * len(geometries),
            "area_m2": list(projected.area),
        },
        geometry=wgs84,
        crs="EPSG:4326",
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `square` — pytest fixture

- Scope: `function` (decorator `pytest.fixture`).
- Returned/yielded object expression(s): `Polygon([(600000, 6200000), (600010, 6200000), (600010, 6200010), (600000, 6200010)])`.
- Tests requesting it by parameter injection: `test_square_metrics`, `test_centroid_coordinates`, `test_output_geometry_remains_wgs84`, `test_missing_crs_fails`, `test_missing_parcel_id_fails`, `test_null_parcel_id_fails`, `test_duplicate_parcel_id_fails`, `test_enrichment_requires_exact_non_empty_parcel_ids`, `test_valid_candidate_area_requires_strict_positive_finite_number`, `test_failed_geometry_does_not_remove_other_rows`, `test_exact_parcel_ids_are_preserved`, `test_enrichment_matches_centralized_shape_metrics`, `test_shape_enrichment_rejects_noncanonical_geometry_status`.

**Complete fixture implementation**

```python
def square() -> Polygon:
    return Polygon(
        [(600000, 6200000), (600010, 6200000), (600010, 6200010), (600000, 6200010)]
    )
```

### `test_square_metrics`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `square` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
row = enriched.iloc[0]
```

**Action**

```python
enriched = enrich_parcel_shapes(_candidate_frame([square]))
```

**Expected result**

```python
assert row["shape_status"] == "VALID"
assert row["length_m"] == pytest.approx(10.0, abs=0.01)
assert row["width_m"] == pytest.approx(10.0, abs=0.01)
assert row["length_width_ratio"] == pytest.approx(1.0, abs=0.001)
assert row["compactness"] == pytest.approx(0.785398)
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_square_metrics(square: Polygon) -> None:
    enriched = enrich_parcel_shapes(_candidate_frame([square]))
    row = enriched.iloc[0]

    assert row["shape_status"] == "VALID"
    assert row["length_m"] == pytest.approx(10.0, abs=0.01)
    assert row["width_m"] == pytest.approx(10.0, abs=0.01)
    assert row["length_width_ratio"] == pytest.approx(1.0, abs=0.001)
    assert row["compactness"] == pytest.approx(0.785398)
```

### `test_rectangle_metrics`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
rectangle = Polygon(
        [(600000, 6200000), (600020, 6200000), (600020, 6200010), (600000, 6200010)]
    )
```

**Action**

```python
row = enrich_parcel_shapes(_candidate_frame([rectangle])).iloc[0]
```

**Expected result**

```python
assert row["length_m"] == pytest.approx(20.0, abs=0.01)
assert row["width_m"] == pytest.approx(10.0, abs=0.01)
assert row["length_width_ratio"] == pytest.approx(2.0, abs=0.001)
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_rectangle_metrics() -> None:
    rectangle = Polygon(
        [(600000, 6200000), (600020, 6200000), (600020, 6200010), (600000, 6200010)]
    )
    row = enrich_parcel_shapes(_candidate_frame([rectangle])).iloc[0]

    assert row["length_m"] == pytest.approx(20.0, abs=0.01)
    assert row["width_m"] == pytest.approx(10.0, abs=0.01)
    assert row["length_width_ratio"] == pytest.approx(2.0, abs=0.001)
```

### `test_rotated_rectangle_metrics`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
rectangle = Polygon(
        [(600000, 6200000), (600030, 6200000), (600030, 6200010), (600000, 6200010)]
    )
rotated = rotate(rectangle, 37)
```

**Action**

```python
row = enrich_parcel_shapes(_candidate_frame([rotated])).iloc[0]
```

**Expected result**

```python
assert row["length_m"] == pytest.approx(30.0, abs=0.01)
assert row["width_m"] == pytest.approx(10.0, abs=0.01)
assert row["length_width_ratio"] == pytest.approx(3.0, abs=0.001)
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_rotated_rectangle_metrics() -> None:
    rectangle = Polygon(
        [(600000, 6200000), (600030, 6200000), (600030, 6200010), (600000, 6200010)]
    )
    rotated = rotate(rectangle, 37)
    row = enrich_parcel_shapes(_candidate_frame([rotated])).iloc[0]

    assert row["length_m"] == pytest.approx(30.0, abs=0.01)
    assert row["width_m"] == pytest.approx(10.0, abs=0.01)
    assert row["length_width_ratio"] == pytest.approx(3.0, abs=0.001)
```

### `test_elongated_parcel`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
elongated = Polygon(
        [(600000, 6200000), (600100, 6200000), (600100, 6200002), (600000, 6200002)]
    )
```

**Action**

```python
row = enrich_parcel_shapes(_candidate_frame([elongated])).iloc[0]
```

**Expected result**

```python
assert row["length_width_ratio"] == pytest.approx(50.0, abs=0.01)
assert row["length_m"] >= row["width_m"]
assert 0 <= row["compactness"] <= 1
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_elongated_parcel() -> None:
    elongated = Polygon(
        [(600000, 6200000), (600100, 6200000), (600100, 6200002), (600000, 6200002)]
    )
    row = enrich_parcel_shapes(_candidate_frame([elongated])).iloc[0]

    assert row["length_width_ratio"] == pytest.approx(50.0, abs=0.01)
    assert row["length_m"] >= row["width_m"]
    assert 0 <= row["compactness"] <= 1
```

### `test_centroid_coordinates`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `square` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
expected = gpd.GeoSeries([square.centroid], crs="EPSG:2154").to_crs("EPSG:4326").iloc[0]
```

**Action**

```python
row = enrich_parcel_shapes(_candidate_frame([square])).iloc[0]
```

**Expected result**

```python
assert row["centroid_lat"] == pytest.approx(expected.y)
assert row["centroid_lon"] == pytest.approx(expected.x)
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_centroid_coordinates(square: Polygon) -> None:
    expected = gpd.GeoSeries([square.centroid], crs="EPSG:2154").to_crs("EPSG:4326").iloc[0]

    row = enrich_parcel_shapes(_candidate_frame([square])).iloc[0]

    assert row["centroid_lat"] == pytest.approx(expected.y)
    assert row["centroid_lon"] == pytest.approx(expected.x)
```

### `test_output_geometry_remains_wgs84`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `square` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
source = _candidate_frame([square])
```

**Action**

```python
enriched = enrich_parcel_shapes(source)
```

**Expected result**

```python
assert enriched.crs is not None
assert enriched.crs.to_epsg() == 4326
assert enriched.geometry.iloc[0].equals_exact(source.geometry.iloc[0], tolerance=0)
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_output_geometry_remains_wgs84(square: Polygon) -> None:
    source = _candidate_frame([square])

    enriched = enrich_parcel_shapes(source)

    assert enriched.crs is not None
    assert enriched.crs.to_epsg() == 4326
    assert enriched.geometry.iloc[0].equals_exact(source.geometry.iloc[0], tolerance=0)
```

### `test_missing_crs_fails`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `square` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
source = _candidate_frame([square]).set_crs(None, allow_override=True)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ShapeEnrichmentError, match="CRS"):
        enrich_parcel_shapes(source)
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_missing_crs_fails(square: Polygon) -> None:
    source = _candidate_frame([square]).set_crs(None, allow_override=True)

    with pytest.raises(ShapeEnrichmentError, match="CRS"):
        enrich_parcel_shapes(source)
```

### `test_missing_parcel_id_fails`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `square` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
source = _candidate_frame([square]).drop(columns=["parcel_id"])
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ShapeEnrichmentError, match="parcel_id"):
        enrich_parcel_shapes(source)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_missing_parcel_id_fails(square: Polygon) -> None:
    source = _candidate_frame([square]).drop(columns=["parcel_id"])

    with pytest.raises(ShapeEnrichmentError, match="parcel_id"):
        enrich_parcel_shapes(source)
```

### `test_null_parcel_id_fails`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `square` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
source = _candidate_frame([square])
source.loc[0, "parcel_id"] = None
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ShapeEnrichmentError, match="null"):
        enrich_parcel_shapes(source)
```

**Regression protected**

Pins true-null handling and prevents textual or malformed null-like values from changing the contract.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_null_parcel_id_fails(square: Polygon) -> None:
    source = _candidate_frame([square])
    source.loc[0, "parcel_id"] = None

    with pytest.raises(ShapeEnrichmentError, match="null"):
        enrich_parcel_shapes(source)
```

### `test_duplicate_parcel_id_fails`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `square` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
source = _candidate_frame([square, square])
source.loc[1, "parcel_id"] = source.loc[0, "parcel_id"]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ShapeEnrichmentError, match="unique"):
        enrich_parcel_shapes(source)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_duplicate_parcel_id_fails(square: Polygon) -> None:
    source = _candidate_frame([square, square])
    source.loc[1, "parcel_id"] = source.loc[0, "parcel_id"]

    with pytest.raises(ShapeEnrichmentError, match="unique"):
        enrich_parcel_shapes(source)
```

### `test_enrichment_requires_exact_non_empty_parcel_ids`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `square` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `parcel_id`.

**Setup**

```python
source = _candidate_frame([square])
source["parcel_id"] = source["parcel_id"].astype(object)
source.loc[0, "parcel_id"] = parcel_id
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ShapeEnrichmentError, match="exact non-empty strings"):
        enrich_parcel_shapes(source)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_enrichment_requires_exact_non_empty_parcel_ids(
    square: Polygon,
    parcel_id: object,
) -> None:
    source = _candidate_frame([square])
    source["parcel_id"] = source["parcel_id"].astype(object)
    source.loc[0, "parcel_id"] = parcel_id

    with pytest.raises(ShapeEnrichmentError, match="exact non-empty strings"):
        enrich_parcel_shapes(source)
```

### `test_valid_candidate_area_requires_strict_positive_finite_number`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `square` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `area`.

**Setup**

```python
source = _candidate_frame([square])
source["area_m2"] = source["area_m2"].astype(object)
source.loc[0, "area_m2"] = area
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ShapeEnrichmentError, match="strict positive finite numeric"):
        enrich_parcel_shapes(source)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_valid_candidate_area_requires_strict_positive_finite_number(
    square: Polygon,
    area: object,
) -> None:
    source = _candidate_frame([square])
    source["area_m2"] = source["area_m2"].astype(object)
    source.loc[0, "area_m2"] = area

    with pytest.raises(ShapeEnrichmentError, match="strict positive finite numeric"):
        enrich_parcel_shapes(source)
```

### `test_failed_geometry_does_not_remove_other_rows`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `square` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
source = _candidate_frame([square, Point(600000, 6200000)])
source.loc[1, "geometry_status"] = "INVALID"
```

**Action**

```python
enriched = enrich_parcel_shapes(source)
```

**Expected result**

```python
assert list(enriched["shape_status"]) == ["VALID", "ERROR"]
assert enriched.loc[1, list(DERIVED_METRIC_COLUMNS)].isna().all()
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_failed_geometry_does_not_remove_other_rows(square: Polygon) -> None:
    source = _candidate_frame([square, Point(600000, 6200000)])
    source.loc[1, "geometry_status"] = "INVALID"

    enriched = enrich_parcel_shapes(source)

    assert list(enriched["shape_status"]) == ["VALID", "ERROR"]
    assert enriched.loc[1, list(DERIVED_METRIC_COLUMNS)].isna().all()
```

### `test_exact_parcel_ids_are_preserved`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `square` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
source = _candidate_frame([square, Point(600000, 6200000)])
source.loc[1, "geometry_status"] = "INVALID"
```

**Action**

```python
enriched = enrich_parcel_shapes(source)
```

**Expected result**

```python
assert len(enriched) == len(source)
assert set(enriched["parcel_id"]) == set(source["parcel_id"])
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_exact_parcel_ids_are_preserved(square: Polygon) -> None:
    source = _candidate_frame([square, Point(600000, 6200000)])
    source.loc[1, "geometry_status"] = "INVALID"

    enriched = enrich_parcel_shapes(source)

    assert len(enriched) == len(source)
    assert set(enriched["parcel_id"]) == set(source["parcel_id"])
```

### `test_enrichment_matches_centralized_shape_metrics`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `square` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
source = _candidate_frame([square])
expected_geometry = source.to_crs(LAMBERT93).geometry.iloc[0]
```

**Action**

```python
expected = parcel_shape_metrics_m(expected_geometry, LAMBERT93)
row = enrich_parcel_shapes(source).iloc[0]
```

**Expected result**

```python
assert row["length_m"] == pytest.approx(expected.length_m)
assert row["width_m"] == pytest.approx(expected.width_m)
assert row["length_width_ratio"] == pytest.approx(expected.length_width_ratio)
assert row["compactness"] == pytest.approx(expected.compactness)
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_enrichment_matches_centralized_shape_metrics(square: Polygon) -> None:
    source = _candidate_frame([square])
    expected_geometry = source.to_crs(LAMBERT93).geometry.iloc[0]
    expected = parcel_shape_metrics_m(expected_geometry, LAMBERT93)

    row = enrich_parcel_shapes(source).iloc[0]

    assert row["length_m"] == pytest.approx(expected.length_m)
    assert row["width_m"] == pytest.approx(expected.width_m)
    assert row["length_width_ratio"] == pytest.approx(expected.length_width_ratio)
    assert row["compactness"] == pytest.approx(expected.compactness)
```

### `test_shape_enrichment_rejects_noncanonical_geometry_status`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `square` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `geometry_status`.

**Setup**

```python
invalid = _candidate_frame([square])
invalid["geometry_status"] = invalid["geometry_status"].astype(object)
invalid.loc[0, "geometry_status"] = geometry_status
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ShapeEnrichmentError, match="geometry_status"):
        enrich_parcel_shapes(invalid)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_shape_enrichment_rejects_noncanonical_geometry_status(
    square: Polygon,
    geometry_status: object,
) -> None:
    invalid = _candidate_frame([square])
    invalid["geometry_status"] = invalid["geometry_status"].astype(object)
    invalid.loc[0, "geometry_status"] = geometry_status

    with pytest.raises(ShapeEnrichmentError, match="geometry_status"):
        enrich_parcel_shapes(invalid)
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

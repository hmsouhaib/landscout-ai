# `tests/unit/test_crs.py`

## File identity

- Repository path: `tests/unit/test_crs.py`
- File type: Python test
- Primary responsibility: Provides complete unit and regression coverage for the `crs` contracts exercised in this file.
- Layer / domain: `unit/regression test` / `test`
- Public or internal role: Internal test support; not a production API.
- Source SHA256: `5853d271a807675e0d775bea4ab0279d36428b337e5edb3c9ce2cf95d8a866be`

## 1. Purpose

Provides complete unit and regression coverage for the `crs` contracts exercised in this file.

## 2. Position in LandScout architecture

This file is a `unit/regression test` artifact in the `test` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- None.

### Third-party

- `import pytest` — required by the implementation paths and symbols documented below.
- `from shapely.geometry import Polygon` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout.geo import LAMBERT93, WGS84, MetricCrsError, centroid_to_latlon` — required by the implementation paths and symbols documented below.
- `from landscout.geo.geometry import reproject_to_lambert93` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

No module-level meaningful constant is defined. Literal domains enforced inside functions are documented with those functions.

## 5. Classes / models / dataclasses

No class, model, or dataclass is declared in this file.

## 6. Functions and methods

### `test_crs_constants`

**Signature**

```python
def test_crs_constants() -> None:
```

**Purpose**

Protects the `crs constants` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 0 explicit setup/context statement(s).

**Action**

- Calls `LAMBERT93.to_epsg`, `WGS84.to_epsg`.

**Expected result**

- Direct assertions: `assert WGS84.to_epsg() == 4326`; `assert LAMBERT93.to_epsg() == 2154`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `crs constants` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LAMBERT93.to_epsg`, `WGS84.to_epsg`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_reproject_to_lambert93_and_back_to_latlon`

**Signature**

```python
def test_reproject_to_lambert93_and_back_to_latlon() -> None:
```

**Purpose**

Protects the `reproject to lambert93 and back to latlon` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `polygon` from `Polygon([(2.0, 48.0), (2.01, 48.0), (2.01, 48.01), (2.0, 48.01)])`.
- Computes `projected` from `reproject_to_lambert93(polygon, WGS84)`.
- Computes `(latitude, longitude)` from `centroid_to_latlon(projected, LAMBERT93)`.

**Action**

- Calls `Polygon`, `centroid_to_latlon`, `reproject_to_lambert93`.

**Expected result**

- Direct assertions: `assert latitude == pytest.approx(48.005, abs=0.001)`; `assert longitude == pytest.approx(2.005, abs=0.001)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `reproject to lambert93 and back to latlon` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Polygon`, `centroid_to_latlon`, `pytest.approx`, `reproject_to_lambert93`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_reprojection_rejects_malformed_crs_with_controlled_error`

**Signature**

```python
def test_reprojection_rejects_malformed_crs_with_controlled_error(
    crs: object,
) -> None:
```

**Purpose**

Protects the `reprojection rejects malformed crs with controlled error` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `crs`.
- Contains 2 explicit setup/context statement(s).
- Computes `polygon` from `Polygon([(2, 48), (2.01, 48), (2.01, 48.01), (2, 48.01)])`.
- Enters managed context(s) `pytest.raises(MetricCrsError)` and executes: Calls `reproject_to_lambert93(polygon, crs)` for its validation or side effect.

**Action**

- Calls `Polygon`, `object`, `reproject_to_lambert93`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(MetricCrsError): reproject_to_lambert93(polygon, crs)`.

**Regression protected**

- Protects the exact `reprojection rejects malformed crs with controlled error` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Polygon`, `object`, `pytest.mark.parametrize`, `pytest.raises`, `reproject_to_lambert93`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

## 7. Data contracts

No DataFrame/GeoDataFrame column is referenced directly. Object and scalar contracts are documented through classes, parameters, returns, constants, and validators.

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

This file contributes to LandScout's `test` evidence flow as described by its purpose and public symbols. It preserves the distinction among fact, proxy evidence, policy interpretation, diagnostic status, and parcel precheck.

## 15. Explicit non-goals

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

## 16. Tests

Direct name-resolved tests appear under each symbol. Higher-level tests may exercise private helpers through a public source-complete function; companion documents for all test files describe their fixtures, actions, assertions, and boundaries.

## 17. Change impact

Changing this file requires reviewing its static callers, package exports, directly mapped tests, relevant schema/hash/version constants, source locks, persisted artifact contracts, and the corresponding pipeline/cross-cutting documents. Any byte change makes the SHA256 above stale and requires regenerating this companion.

# `tests/unit/test_crs.py`

## File identity

- Repository path: `tests/unit/test_crs.py`
- File type: Python test
- Layer: unit/regression test
- Domain: test
- Responsibility: Provides complete unit and regression coverage for the `crs` contracts exercised in this file.
- Source SHA256: `5853d271a807675e0d775bea4ab0279d36428b337e5edb3c9ce2cf95d8a866be`

## 1. Purpose

Provides complete unit and regression coverage for the `crs` contracts exercised in this file.

## 2. Position in LandScout architecture

This file belongs to the **unit/regression test** layer and the **test** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `None.`

### Third-party packages

- `import pytest`
- `from shapely.geometry import Polygon`

### Internal LandScout imports

- `from landscout.geo import LAMBERT93, WGS84, MetricCrsError, centroid_to_latlon`
- `from landscout.geo.geometry import reproject_to_lambert93`

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

### `test_crs_constants`

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
assert WGS84.to_epsg() == 4326
assert LAMBERT93.to_epsg() == 2154
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_crs_constants() -> None:
    assert WGS84.to_epsg() == 4326
    assert LAMBERT93.to_epsg() == 2154
```

### `test_reproject_to_lambert93_and_back_to_latlon`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
polygon = Polygon(
        [(2.0, 48.0), (2.01, 48.0), (2.01, 48.01), (2.0, 48.01)]
    )
```

**Action**

```python
projected = reproject_to_lambert93(polygon, WGS84)
latitude, longitude = centroid_to_latlon(projected, LAMBERT93)
```

**Expected result**

```python
assert latitude == pytest.approx(48.005, abs=0.001)
assert longitude == pytest.approx(2.005, abs=0.001)
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_reproject_to_lambert93_and_back_to_latlon() -> None:
    polygon = Polygon(
        [(2.0, 48.0), (2.01, 48.0), (2.01, 48.01), (2.0, 48.01)]
    )

    projected = reproject_to_lambert93(polygon, WGS84)
    latitude, longitude = centroid_to_latlon(projected, LAMBERT93)

    assert latitude == pytest.approx(48.005, abs=0.001)
    assert longitude == pytest.approx(2.005, abs=0.001)
```

### `test_reprojection_rejects_malformed_crs_with_controlled_error`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `crs`.

**Setup**

```python
polygon = Polygon([(2, 48), (2.01, 48), (2.01, 48.01), (2, 48.01)])
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(MetricCrsError):
        reproject_to_lambert93(polygon, crs)
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_reprojection_rejects_malformed_crs_with_controlled_error(
    crs: object,
) -> None:
    polygon = Polygon([(2, 48), (2.01, 48), (2.01, 48.01), (2, 48.01)])

    with pytest.raises(MetricCrsError):
        reproject_to_lambert93(polygon, crs)
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

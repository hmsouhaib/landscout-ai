# `tests/unit/test_enrich_shape.py`

## File identity

- Repository path: `tests/unit/test_enrich_shape.py`
- File type: Python source
- Layer: unit/regression test
- Domain: isolated contract test evidence
- Responsibility: Provides complete unit and regression coverage for the `enrich_shape` contracts exercised in this file.
- Source SHA256: `4803e1c4fce5eb152b1005842702fb77b5e13de2be61a882e7d8128d0fb28901`

## 1. STEP 7F.1A.4 contract delta

- Refreshes permanent STEP 7F.1A.4 regression coverage for enrich shape; the exact fixtures, mutations, calls, controlled failures, and assertions are inventoried below.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Provides complete unit and regression coverage for the `enrich_shape` contracts exercised in this file.

The file belongs to the **unit/regression test** layer and **isolated contract test evidence** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- None.

### Third-party packages

- `import geopandas as gpd`
- `import pytest`
- `from shapely.affinity import rotate`
- `from shapely.geometry import Polygon`
- `from shapely.geometry.base import BaseGeometry`

### Internal LandScout imports

- `from landscout.geo import LAMBERT93, parcel_shape_metrics_m`
- `from landscout.stages.enrich_shape import (
    DERIVED_METRIC_COLUMNS,
    ShapeEnrichmentError,
    enrich_parcel_shapes,
)`

## 4. Contract taxonomy

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

No module-level constant, alias, schema, mapping, or meaningful dunder assignment is declared.

### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

No top-level class/model/dataclass is declared.

## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `_candidate_frame`

**Purpose:** Implements `candidate frame` within the file role: Provides complete unit and regression coverage for the `enrich_shape` contracts exercised in this file.

**Exact signature**

```python
def _candidate_frame(geometries: list[BaseGeometry]) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `geometries` | positional-or-keyword | `list[BaseGeometry]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `gpd.GeoDataFrame(<br>        {<br>            "parcel_id": [<br>                f"313950000A{index + 1:04d}" for index in range(len(geometries))<br>            ],<br>            "commune_code": ["31395"] * len(geometries),<br>            "section_prefix": ["000"] * len(geometries),<br>            "section": ["A"] * len(geometries),<br>            "parcel_number": [str(index + 1) for index in range(len(geometries))],<br>            "source_contenance": [None] * len(geometries),<br>            "source_arpente": [None] * len(geometries),<br>            "source_created_at": [None] * len(geometries),<br>            "source_updated_at": [None] * len(geometries),<br>            "geometry_status": [<br>                "VALID"<br>                if geometry.geom_type in {"Polygon", "MultiPolygon"}<br>                and not geometry.is_empty<br>                and geometry.is_valid<br>                else "INVALID"<br>                for geometry in geometries<br>            ],<br>            "area_m2": [<br>                float(area)<br>                if geometry.geom_type in {"Polygon", "MultiPolygon"}<br>                and not geometry.is_empty<br>                and geometry.is_valid<br>                else None<br>                for geometry, area in zip(<br>                    geometries,<br>                    wgs84.to_crs("EPSG:2154").area,<br>                    strict=True,<br>                )<br>            ],<br>        },<br>        geometry=wgs84,<br>        crs="EPSG:4326",<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_enrich_shape::test_square_metrics` via `_candidate_frame`
- value/type reference: `tests.unit.test_enrich_shape::test_square_metrics` via `_candidate_frame`
- direct call: `tests.unit.test_enrich_shape::test_rectangle_metrics` via `_candidate_frame`
- value/type reference: `tests.unit.test_enrich_shape::test_rectangle_metrics` via `_candidate_frame`
- direct call: `tests.unit.test_enrich_shape::test_rotated_rectangle_metrics` via `_candidate_frame`
- value/type reference: `tests.unit.test_enrich_shape::test_rotated_rectangle_metrics` via `_candidate_frame`
- direct call: `tests.unit.test_enrich_shape::test_elongated_parcel` via `_candidate_frame`
- value/type reference: `tests.unit.test_enrich_shape::test_elongated_parcel` via `_candidate_frame`
- direct call: `tests.unit.test_enrich_shape::test_centroid_coordinates` via `_candidate_frame`
- value/type reference: `tests.unit.test_enrich_shape::test_centroid_coordinates` via `_candidate_frame`
- direct call: `tests.unit.test_enrich_shape::test_output_geometry_remains_wgs84` via `_candidate_frame`
- value/type reference: `tests.unit.test_enrich_shape::test_output_geometry_remains_wgs84` via `_candidate_frame`
- direct call: `tests.unit.test_enrich_shape::test_missing_crs_fails` via `_candidate_frame`
- value/type reference: `tests.unit.test_enrich_shape::test_missing_crs_fails` via `_candidate_frame`
- direct call: `tests.unit.test_enrich_shape::test_missing_parcel_id_fails` via `_candidate_frame`
- value/type reference: `tests.unit.test_enrich_shape::test_missing_parcel_id_fails` via `_candidate_frame`
- direct call: `tests.unit.test_enrich_shape::test_null_parcel_id_fails` via `_candidate_frame`
- value/type reference: `tests.unit.test_enrich_shape::test_null_parcel_id_fails` via `_candidate_frame`
- direct call: `tests.unit.test_enrich_shape::test_duplicate_parcel_id_fails` via `_candidate_frame`
- value/type reference: `tests.unit.test_enrich_shape::test_duplicate_parcel_id_fails` via `_candidate_frame`
- direct call: `tests.unit.test_enrich_shape::test_enrichment_requires_exact_non_empty_parcel_ids` via `_candidate_frame`
- value/type reference: `tests.unit.test_enrich_shape::test_enrichment_requires_exact_non_empty_parcel_ids` via `_candidate_frame`
- direct call: `tests.unit.test_enrich_shape::test_valid_candidate_area_requires_strict_positive_finite_number` via `_candidate_frame`
- value/type reference: `tests.unit.test_enrich_shape::test_valid_candidate_area_requires_strict_positive_finite_number` via `_candidate_frame`
- direct call: `tests.unit.test_enrich_shape::test_failed_geometry_does_not_remove_other_rows` via `_candidate_frame`
- value/type reference: `tests.unit.test_enrich_shape::test_failed_geometry_does_not_remove_other_rows` via `_candidate_frame`
- direct call: `tests.unit.test_enrich_shape::test_exact_parcel_ids_are_preserved` via `_candidate_frame`
- value/type reference: `tests.unit.test_enrich_shape::test_exact_parcel_ids_are_preserved` via `_candidate_frame`
- direct call: `tests.unit.test_enrich_shape::test_enrichment_matches_centralized_shape_metrics` via `_candidate_frame`
- value/type reference: `tests.unit.test_enrich_shape::test_enrichment_matches_centralized_shape_metrics` via `_candidate_frame`
- direct call: `tests.unit.test_enrich_shape::test_shape_enrichment_rejects_noncanonical_geometry_status` via `_candidate_frame`
- value/type reference: `tests.unit.test_enrich_shape::test_shape_enrichment_rejects_noncanonical_geometry_status` via `_candidate_frame`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `gpd.GeoSeries` | `geopandas.GeoSeries` |
| `projected.to_crs` | `unresolved local/third-party receiver; no ownership inferred` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `range` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |
| `zip` | `unresolved local/third-party receiver; no ownership inferred` |
| `wgs84.to_crs` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `projected.to_crs`<br>`wgs84.to_crs` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _candidate_frame(geometries: list[BaseGeometry]) -> gpd.GeoDataFrame:
    projected = gpd.GeoSeries(geometries, crs="EPSG:2154")
    wgs84 = projected.to_crs("EPSG:4326")
    return gpd.GeoDataFrame(
        {
            "parcel_id": [
                f"313950000A{index + 1:04d}" for index in range(len(geometries))
            ],
            "commune_code": ["31395"] * len(geometries),
            "section_prefix": ["000"] * len(geometries),
            "section": ["A"] * len(geometries),
            "parcel_number": [str(index + 1) for index in range(len(geometries))],
            "source_contenance": [None] * len(geometries),
            "source_arpente": [None] * len(geometries),
            "source_created_at": [None] * len(geometries),
            "source_updated_at": [None] * len(geometries),
            "geometry_status": [
                "VALID"
                if geometry.geom_type in {"Polygon", "MultiPolygon"}
                and not geometry.is_empty
                and geometry.is_valid
                else "INVALID"
                for geometry in geometries
            ],
            "area_m2": [
                float(area)
                if geometry.geom_type in {"Polygon", "MultiPolygon"}
                and not geometry.is_empty
                and geometry.is_valid
                else None
                for geometry, area in zip(
                    geometries,
                    wgs84.to_crs("EPSG:2154").area,
                    strict=True,
                )
            ],
        },
        geometry=wgs84,
        crs="EPSG:4326",
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `square`

**Purpose:** Implements `square` within the file role: Provides complete unit and regression coverage for the `enrich_shape` contracts exercised in this file.

**Exact signature**

```python
def square() -> Polygon:
```

- Exact decorators: `pytest.fixture`.
- Declared return annotation: `Polygon`.

**Inputs**

- No parameters.

**Return and exception contract**

- Exact observed return expressions:
  - `Polygon(<br>        [(600000, 6200000), (600010, 6200000), (600010, 6200010), (600000, 6200010)]<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- value/type reference: `tests.unit.test_enrich_shape::test_square_metrics` via `square`
- value/type reference: `tests.unit.test_enrich_shape::test_centroid_coordinates` via `square`
- value/type reference: `tests.unit.test_enrich_shape::test_output_geometry_remains_wgs84` via `square`
- value/type reference: `tests.unit.test_enrich_shape::test_missing_crs_fails` via `square`
- value/type reference: `tests.unit.test_enrich_shape::test_missing_parcel_id_fails` via `square`
- value/type reference: `tests.unit.test_enrich_shape::test_null_parcel_id_fails` via `square`
- value/type reference: `tests.unit.test_enrich_shape::test_duplicate_parcel_id_fails` via `square`
- value/type reference: `tests.unit.test_enrich_shape::test_enrichment_requires_exact_non_empty_parcel_ids` via `square`
- value/type reference: `tests.unit.test_enrich_shape::test_valid_candidate_area_requires_strict_positive_finite_number` via `square`
- value/type reference: `tests.unit.test_enrich_shape::test_failed_geometry_does_not_remove_other_rows` via `square`
- value/type reference: `tests.unit.test_enrich_shape::test_exact_parcel_ids_are_preserved` via `square`
- value/type reference: `tests.unit.test_enrich_shape::test_enrichment_matches_centralized_shape_metrics` via `square`
- value/type reference: `tests.unit.test_enrich_shape::test_shape_enrichment_rejects_noncanonical_geometry_status` via `square`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `Polygon` | `shapely.geometry.Polygon` |

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
def square() -> Polygon:
    return Polygon(
        [(600000, 6200000), (600010, 6200000), (600010, 6200010), (600000, 6200010)]
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_square_metrics`

**Purpose:** Regression invariant: square metrics. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_square_metrics(square: Polygon) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `square` | positional-or-keyword | `Polygon` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert row["shape_status"] == "VALID"`
  - `assert row["length_m"] == pytest.approx(10.0, abs=0.01)`
  - `assert row["width_m"] == pytest.approx(10.0, abs=0.01)`
  - `assert row["length_width_ratio"] == pytest.approx(1.0, abs=0.001)`
  - `assert row["compactness"] == pytest.approx(0.785398)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `enrich_parcel_shapes` | `landscout.stages.enrich_shape.enrich_parcel_shapes` |
| `_candidate_frame` | `tests.unit.test_enrich_shape._candidate_frame` |
| `pytest.approx` | `pytest.approx` |

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
def test_square_metrics(square: Polygon) -> None:
    enriched = enrich_parcel_shapes(_candidate_frame([square]))
    row = enriched.iloc[0]

    assert row["shape_status"] == "VALID"
    assert row["length_m"] == pytest.approx(10.0, abs=0.01)
    assert row["width_m"] == pytest.approx(10.0, abs=0.01)
    assert row["length_width_ratio"] == pytest.approx(1.0, abs=0.001)
    assert row["compactness"] == pytest.approx(0.785398)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_rectangle_metrics`

**Purpose:** Regression invariant: rectangle metrics. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_rectangle_metrics() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert row["length_m"] == pytest.approx(20.0, abs=0.01)`
  - `assert row["width_m"] == pytest.approx(10.0, abs=0.01)`
  - `assert row["length_width_ratio"] == pytest.approx(2.0, abs=0.001)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `Polygon` | `shapely.geometry.Polygon` |
| `enrich_parcel_shapes` | `landscout.stages.enrich_shape.enrich_parcel_shapes` |
| `_candidate_frame` | `tests.unit.test_enrich_shape._candidate_frame` |
| `pytest.approx` | `pytest.approx` |

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
def test_rectangle_metrics() -> None:
    rectangle = Polygon(
        [(600000, 6200000), (600020, 6200000), (600020, 6200010), (600000, 6200010)]
    )
    row = enrich_parcel_shapes(_candidate_frame([rectangle])).iloc[0]

    assert row["length_m"] == pytest.approx(20.0, abs=0.01)
    assert row["width_m"] == pytest.approx(10.0, abs=0.01)
    assert row["length_width_ratio"] == pytest.approx(2.0, abs=0.001)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_rotated_rectangle_metrics`

**Purpose:** Regression invariant: rotated rectangle metrics. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_rotated_rectangle_metrics() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert row["length_m"] == pytest.approx(30.0, abs=0.01)`
  - `assert row["width_m"] == pytest.approx(10.0, abs=0.01)`
  - `assert row["length_width_ratio"] == pytest.approx(3.0, abs=0.001)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `Polygon` | `shapely.geometry.Polygon` |
| `rotate` | `shapely.affinity.rotate` |
| `enrich_parcel_shapes` | `landscout.stages.enrich_shape.enrich_parcel_shapes` |
| `_candidate_frame` | `tests.unit.test_enrich_shape._candidate_frame` |
| `pytest.approx` | `pytest.approx` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_elongated_parcel`

**Purpose:** Regression invariant: elongated parcel. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_elongated_parcel() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert row["length_width_ratio"] == pytest.approx(50.0, abs=0.01)`
  - `assert row["length_m"] >= row["width_m"]`
  - `assert 0 <= row["compactness"] <= 1`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `Polygon` | `shapely.geometry.Polygon` |
| `enrich_parcel_shapes` | `landscout.stages.enrich_shape.enrich_parcel_shapes` |
| `_candidate_frame` | `tests.unit.test_enrich_shape._candidate_frame` |
| `pytest.approx` | `pytest.approx` |

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
def test_elongated_parcel() -> None:
    elongated = Polygon(
        [(600000, 6200000), (600100, 6200000), (600100, 6200002), (600000, 6200002)]
    )
    row = enrich_parcel_shapes(_candidate_frame([elongated])).iloc[0]

    assert row["length_width_ratio"] == pytest.approx(50.0, abs=0.01)
    assert row["length_m"] >= row["width_m"]
    assert 0 <= row["compactness"] <= 1
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_centroid_coordinates`

**Purpose:** Regression invariant: centroid coordinates. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_centroid_coordinates(square: Polygon) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `square` | positional-or-keyword | `Polygon` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert row["centroid_lat"] == pytest.approx(expected.y)`
  - `assert row["centroid_lon"] == pytest.approx(expected.x)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `gpd.GeoSeries([square.centroid], crs="EPSG:2154").to_crs` | `unresolved local/third-party receiver; no ownership inferred` |
| `gpd.GeoSeries` | `geopandas.GeoSeries` |
| `enrich_parcel_shapes` | `landscout.stages.enrich_shape.enrich_parcel_shapes` |
| `_candidate_frame` | `tests.unit.test_enrich_shape._candidate_frame` |
| `pytest.approx` | `pytest.approx` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `gpd.GeoSeries([square.centroid], crs="EPSG:2154").to_crs` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_centroid_coordinates(square: Polygon) -> None:
    expected = (
        gpd.GeoSeries([square.centroid], crs="EPSG:2154").to_crs("EPSG:4326").iloc[0]
    )

    row = enrich_parcel_shapes(_candidate_frame([square])).iloc[0]

    assert row["centroid_lat"] == pytest.approx(expected.y)
    assert row["centroid_lon"] == pytest.approx(expected.x)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_output_geometry_remains_wgs84`

**Purpose:** Regression invariant: output geometry remains wgs84. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_output_geometry_remains_wgs84(square: Polygon) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `square` | positional-or-keyword | `Polygon` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert enriched.crs is not None`
  - `assert enriched.crs.to_epsg() == 4326`
  - `assert enriched.geometry.iloc[0].equals_exact(source.geometry.iloc[0], tolerance=0)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_candidate_frame` | `tests.unit.test_enrich_shape._candidate_frame` |
| `enrich_parcel_shapes` | `landscout.stages.enrich_shape.enrich_parcel_shapes` |
| `enriched.crs.to_epsg` | `unresolved local/third-party receiver; no ownership inferred` |
| `enriched.geometry.iloc[0].equals_exact` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `enriched.geometry.iloc[0].equals_exact` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_output_geometry_remains_wgs84(square: Polygon) -> None:
    source = _candidate_frame([square])

    enriched = enrich_parcel_shapes(source)

    assert enriched.crs is not None
    assert enriched.crs.to_epsg() == 4326
    assert enriched.geometry.iloc[0].equals_exact(source.geometry.iloc[0], tolerance=0)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_missing_crs_fails`

**Purpose:** Regression invariant: missing crs fails. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_missing_crs_fails(square: Polygon) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `square` | positional-or-keyword | `Polygon` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ShapeEnrichmentError, match="CRS")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_candidate_frame([square]).set_crs` | `unresolved local/third-party receiver; no ownership inferred` |
| `_candidate_frame` | `tests.unit.test_enrich_shape._candidate_frame` |
| `pytest.raises` | `pytest.raises` |
| `enrich_parcel_shapes` | `landscout.stages.enrich_shape.enrich_parcel_shapes` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `_candidate_frame([square]).set_crs` |
| External process/environment | None directly present. |
| In-memory mutation | `_candidate_frame([square]).set_crs(None, allow_override=True)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_missing_crs_fails(square: Polygon) -> None:
    source = _candidate_frame([square]).set_crs(None, allow_override=True)

    with pytest.raises(ShapeEnrichmentError, match="CRS"):
        enrich_parcel_shapes(source)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_missing_parcel_id_fails`

**Purpose:** Regression invariant: missing parcel id fails. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_missing_parcel_id_fails(square: Polygon) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `square` | positional-or-keyword | `Polygon` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ShapeEnrichmentError, match="parcel_id")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_candidate_frame([square]).drop` | `unresolved local/third-party receiver; no ownership inferred` |
| `_candidate_frame` | `tests.unit.test_enrich_shape._candidate_frame` |
| `pytest.raises` | `pytest.raises` |
| `enrich_parcel_shapes` | `landscout.stages.enrich_shape.enrich_parcel_shapes` |

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
| In-memory mutation | `_candidate_frame([square]).drop(columns=["parcel_id"])` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_missing_parcel_id_fails(square: Polygon) -> None:
    source = _candidate_frame([square]).drop(columns=["parcel_id"])

    with pytest.raises(ShapeEnrichmentError, match="parcel_id"):
        enrich_parcel_shapes(source)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_null_parcel_id_fails`

**Purpose:** Regression invariant: null parcel id fails. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_null_parcel_id_fails(square: Polygon) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `square` | positional-or-keyword | `Polygon` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ShapeEnrichmentError, match="null")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_candidate_frame` | `tests.unit.test_enrich_shape._candidate_frame` |
| `pytest.raises` | `pytest.raises` |
| `enrich_parcel_shapes` | `landscout.stages.enrich_shape.enrich_parcel_shapes` |

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
| In-memory mutation | `source.loc[0, "parcel_id"] = None` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_null_parcel_id_fails(square: Polygon) -> None:
    source = _candidate_frame([square])
    source.loc[0, "parcel_id"] = None

    with pytest.raises(ShapeEnrichmentError, match="null"):
        enrich_parcel_shapes(source)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_duplicate_parcel_id_fails`

**Purpose:** Regression invariant: duplicate parcel id fails. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_duplicate_parcel_id_fails(square: Polygon) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `square` | positional-or-keyword | `Polygon` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ShapeEnrichmentError, match="unique")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_candidate_frame` | `tests.unit.test_enrich_shape._candidate_frame` |
| `pytest.raises` | `pytest.raises` |
| `enrich_parcel_shapes` | `landscout.stages.enrich_shape.enrich_parcel_shapes` |

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
| In-memory mutation | `source.loc[1, "parcel_id"] = source.loc[0, "parcel_id"]` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_duplicate_parcel_id_fails(square: Polygon) -> None:
    source = _candidate_frame([square, square])
    source.loc[1, "parcel_id"] = source.loc[0, "parcel_id"]

    with pytest.raises(ShapeEnrichmentError, match="unique"):
        enrich_parcel_shapes(source)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_enrichment_requires_exact_non_empty_parcel_ids`

**Purpose:** Regression invariant: enrichment requires exact non empty parcel ids. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_enrichment_requires_exact_non_empty_parcel_ids(
    square: Polygon,
    parcel_id: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("parcel_id", [1, "", " parcel", "parcel "])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `square` | positional-or-keyword | `Polygon` | `required` |
| `parcel_id` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ShapeEnrichmentError, match="exact non-empty strings")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_candidate_frame` | `tests.unit.test_enrich_shape._candidate_frame` |
| `source["parcel_id"].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `enrich_parcel_shapes` | `landscout.stages.enrich_shape.enrich_parcel_shapes` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

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
| In-memory mutation | `source["parcel_id"] = source["parcel_id"].astype(object)`<br>`source.loc[0, "parcel_id"] = parcel_id` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_valid_candidate_area_requires_strict_positive_finite_number`

**Purpose:** Regression invariant: valid candidate area requires strict positive finite number. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_valid_candidate_area_requires_strict_positive_finite_number(
    square: Polygon,
    area: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("area", [-1, 0, float("inf"), float("nan"), "100", True])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `square` | positional-or-keyword | `Polygon` | `required` |
| `area` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ShapeEnrichmentError, match="strict positive finite numeric")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_candidate_frame` | `tests.unit.test_enrich_shape._candidate_frame` |
| `source["area_m2"].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `enrich_parcel_shapes` | `landscout.stages.enrich_shape.enrich_parcel_shapes` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
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
| In-memory mutation | `source["area_m2"] = source["area_m2"].astype(object)`<br>`source.loc[0, "area_m2"] = area` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_failed_geometry_does_not_remove_other_rows`

**Purpose:** Regression invariant: failed geometry does not remove other rows. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_failed_geometry_does_not_remove_other_rows(square: Polygon) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `square` | positional-or-keyword | `Polygon` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert list(enriched["shape_status"]) == ["VALID", "ERROR"]`
  - `assert enriched.loc[1, list(DERIVED_METRIC_COLUMNS)].isna().all()`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_candidate_frame` | `tests.unit.test_enrich_shape._candidate_frame` |
| `Polygon` | `shapely.geometry.Polygon` |
| `enrich_parcel_shapes` | `landscout.stages.enrich_shape.enrich_parcel_shapes` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `enriched.loc[1, list(DERIVED_METRIC_COLUMNS)].isna().all` | `unresolved local/third-party receiver; no ownership inferred` |
| `enriched.loc[1, list(DERIVED_METRIC_COLUMNS)].isna` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_failed_geometry_does_not_remove_other_rows(square: Polygon) -> None:
    source = _candidate_frame([square, Polygon()])

    enriched = enrich_parcel_shapes(source)

    assert list(enriched["shape_status"]) == ["VALID", "ERROR"]
    assert enriched.loc[1, list(DERIVED_METRIC_COLUMNS)].isna().all()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_exact_parcel_ids_are_preserved`

**Purpose:** Regression invariant: exact parcel ids are preserved. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_exact_parcel_ids_are_preserved(square: Polygon) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `square` | positional-or-keyword | `Polygon` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert len(enriched) == len(source)`
  - `assert set(enriched["parcel_id"]) == set(source["parcel_id"])`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_candidate_frame` | `tests.unit.test_enrich_shape._candidate_frame` |
| `Polygon` | `shapely.geometry.Polygon` |
| `enrich_parcel_shapes` | `landscout.stages.enrich_shape.enrich_parcel_shapes` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
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
def test_exact_parcel_ids_are_preserved(square: Polygon) -> None:
    source = _candidate_frame([square, Polygon()])

    enriched = enrich_parcel_shapes(source)

    assert len(enriched) == len(source)
    assert set(enriched["parcel_id"]) == set(source["parcel_id"])
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_enrichment_matches_centralized_shape_metrics`

**Purpose:** Regression invariant: enrichment matches centralized shape metrics. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_enrichment_matches_centralized_shape_metrics(square: Polygon) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `square` | positional-or-keyword | `Polygon` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert row["length_m"] == pytest.approx(expected.length_m)`
  - `assert row["width_m"] == pytest.approx(expected.width_m)`
  - `assert row["length_width_ratio"] == pytest.approx(expected.length_width_ratio)`
  - `assert row["compactness"] == pytest.approx(expected.compactness)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_candidate_frame` | `tests.unit.test_enrich_shape._candidate_frame` |
| `source.to_crs` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcel_shape_metrics_m` | `landscout.geo.parcel_shape_metrics_m` |
| `enrich_parcel_shapes` | `landscout.stages.enrich_shape.enrich_parcel_shapes` |
| `pytest.approx` | `pytest.approx` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `source.to_crs` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_shape_enrichment_rejects_noncanonical_geometry_status`

**Purpose:** Regression invariant: shape enrichment rejects noncanonical geometry status. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_shape_enrichment_rejects_noncanonical_geometry_status(
    square: Polygon,
    geometry_status: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "geometry_status",
    [None, "UNKNOWN", "ERROR", "BANANA", "valid", 0, 1, True, False],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `square` | positional-or-keyword | `Polygon` | `required` |
| `geometry_status` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ShapeEnrichmentError, match="geometry_status")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_candidate_frame` | `tests.unit.test_enrich_shape._candidate_frame` |
| `invalid["geometry_status"].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `enrich_parcel_shapes` | `landscout.stages.enrich_shape.enrich_parcel_shapes` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `invalid["geometry_status"].astype` |
| External process/environment | None directly present. |
| In-memory mutation | `invalid["geometry_status"] = invalid["geometry_status"].astype(object)`<br>`invalid.loc[0, "geometry_status"] = geometry_status` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.


## 7. Test-specific regression contract

- Test functions: **16**.
- Pytest fixtures (decorator-proven): **1**.

### Fixtures

- `square` — decorators: `pytest.fixture`.

### Per-test regression index

| Test | Parametrization | Expected exception contexts | Assertion count | Exact regression purpose |
|---|---|---|---:|---|
| `test_square_metrics` | none | none | 5 | Proves square metrics using the exact source reproduced in section 7. |
| `test_rectangle_metrics` | none | none | 3 | Proves rectangle metrics using the exact source reproduced in section 7. |
| `test_rotated_rectangle_metrics` | none | none | 3 | Proves rotated rectangle metrics using the exact source reproduced in section 7. |
| `test_elongated_parcel` | none | none | 3 | Proves elongated parcel using the exact source reproduced in section 7. |
| `test_centroid_coordinates` | none | none | 2 | Proves centroid coordinates using the exact source reproduced in section 7. |
| `test_output_geometry_remains_wgs84` | none | none | 3 | Proves output geometry remains wgs84 using the exact source reproduced in section 7. |
| `test_missing_crs_fails` | none | pytest.raises(ShapeEnrichmentError, match="CRS") | 0 | Proves missing crs fails using the exact source reproduced in section 7. |
| `test_missing_parcel_id_fails` | none | pytest.raises(ShapeEnrichmentError, match="parcel_id") | 0 | Proves missing parcel id fails using the exact source reproduced in section 7. |
| `test_null_parcel_id_fails` | none | pytest.raises(ShapeEnrichmentError, match="null") | 0 | Proves null parcel id fails using the exact source reproduced in section 7. |
| `test_duplicate_parcel_id_fails` | none | pytest.raises(ShapeEnrichmentError, match="unique") | 0 | Proves duplicate parcel id fails using the exact source reproduced in section 7. |
| `test_enrichment_requires_exact_non_empty_parcel_ids` | pytest.mark.parametrize("parcel_id", [1, "", " parcel", "parcel "]) | pytest.raises(ShapeEnrichmentError, match="exact non-empty strings") | 0 | Proves enrichment requires exact non empty parcel ids using the exact source reproduced in section 7. |
| `test_valid_candidate_area_requires_strict_positive_finite_number` | pytest.mark.parametrize("area", [-1, 0, float("inf"), float("nan"), "100", True]) | pytest.raises(ShapeEnrichmentError, match="strict positive finite numeric") | 0 | Proves valid candidate area requires strict positive finite number using the exact source reproduced in section 7. |
| `test_failed_geometry_does_not_remove_other_rows` | none | none | 2 | Proves failed geometry does not remove other rows using the exact source reproduced in section 7. |
| `test_exact_parcel_ids_are_preserved` | none | none | 2 | Proves exact parcel ids are preserved using the exact source reproduced in section 7. |
| `test_enrichment_matches_centralized_shape_metrics` | none | none | 4 | Proves enrichment matches centralized shape metrics using the exact source reproduced in section 7. |
| `test_shape_enrichment_rejects_noncanonical_geometry_status` | pytest.mark.parametrize(<br>    "geometry_status",<br>    [None, "UNKNOWN", "ERROR", "BANANA", "valid", 0, 1, True, False],<br>) | pytest.raises(ShapeEnrichmentError, match="geometry_status") | 0 | Proves shape enrichment rejects noncanonical geometry status using the exact source reproduced in section 7. |

## 8. Public exports and package ownership

This module declares no `__all__`; no package-level public guarantee is inferred from direct importability alone.

## 9. Trust, provenance, side effects, and business boundary

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.
- Configured identity, textual lineage, byte identity, physical source reconstruction, local envelope validation, and source-complete validation remain distinct trust levels. This companion attributes only the levels implemented in the exact source.
- Filesystem, network, hashing, CRS/geometry, process, mutation, and expected-exception evidence is listed per callable; an empty category is not silently promoted to an effect.

## 10. Change impact

A source-byte change invalidates the SHA above and requires re-auditing imports/re-exports, constants/aliases/schemas, model fields/immutability, qualified callers, side effects, controlled errors, tests, source/artifact locks, and the exact full snapshot.

## 11. Exact complete current file content

The following UTF-8 snapshot is the complete current repository file, not an excerpt. Its raw-byte SHA256 is the value in **File identity**.

```python
import geopandas as gpd
import pytest
from shapely.affinity import rotate
from shapely.geometry import Polygon
from shapely.geometry.base import BaseGeometry

from landscout.geo import LAMBERT93, parcel_shape_metrics_m
from landscout.stages.enrich_shape import (
    DERIVED_METRIC_COLUMNS,
    ShapeEnrichmentError,
    enrich_parcel_shapes,
)


def _candidate_frame(geometries: list[BaseGeometry]) -> gpd.GeoDataFrame:
    projected = gpd.GeoSeries(geometries, crs="EPSG:2154")
    wgs84 = projected.to_crs("EPSG:4326")
    return gpd.GeoDataFrame(
        {
            "parcel_id": [
                f"313950000A{index + 1:04d}" for index in range(len(geometries))
            ],
            "commune_code": ["31395"] * len(geometries),
            "section_prefix": ["000"] * len(geometries),
            "section": ["A"] * len(geometries),
            "parcel_number": [str(index + 1) for index in range(len(geometries))],
            "source_contenance": [None] * len(geometries),
            "source_arpente": [None] * len(geometries),
            "source_created_at": [None] * len(geometries),
            "source_updated_at": [None] * len(geometries),
            "geometry_status": [
                "VALID"
                if geometry.geom_type in {"Polygon", "MultiPolygon"}
                and not geometry.is_empty
                and geometry.is_valid
                else "INVALID"
                for geometry in geometries
            ],
            "area_m2": [
                float(area)
                if geometry.geom_type in {"Polygon", "MultiPolygon"}
                and not geometry.is_empty
                and geometry.is_valid
                else None
                for geometry, area in zip(
                    geometries,
                    wgs84.to_crs("EPSG:2154").area,
                    strict=True,
                )
            ],
        },
        geometry=wgs84,
        crs="EPSG:4326",
    )


@pytest.fixture
def square() -> Polygon:
    return Polygon(
        [(600000, 6200000), (600010, 6200000), (600010, 6200010), (600000, 6200010)]
    )


def test_square_metrics(square: Polygon) -> None:
    enriched = enrich_parcel_shapes(_candidate_frame([square]))
    row = enriched.iloc[0]

    assert row["shape_status"] == "VALID"
    assert row["length_m"] == pytest.approx(10.0, abs=0.01)
    assert row["width_m"] == pytest.approx(10.0, abs=0.01)
    assert row["length_width_ratio"] == pytest.approx(1.0, abs=0.001)
    assert row["compactness"] == pytest.approx(0.785398)


def test_rectangle_metrics() -> None:
    rectangle = Polygon(
        [(600000, 6200000), (600020, 6200000), (600020, 6200010), (600000, 6200010)]
    )
    row = enrich_parcel_shapes(_candidate_frame([rectangle])).iloc[0]

    assert row["length_m"] == pytest.approx(20.0, abs=0.01)
    assert row["width_m"] == pytest.approx(10.0, abs=0.01)
    assert row["length_width_ratio"] == pytest.approx(2.0, abs=0.001)


def test_rotated_rectangle_metrics() -> None:
    rectangle = Polygon(
        [(600000, 6200000), (600030, 6200000), (600030, 6200010), (600000, 6200010)]
    )
    rotated = rotate(rectangle, 37)
    row = enrich_parcel_shapes(_candidate_frame([rotated])).iloc[0]

    assert row["length_m"] == pytest.approx(30.0, abs=0.01)
    assert row["width_m"] == pytest.approx(10.0, abs=0.01)
    assert row["length_width_ratio"] == pytest.approx(3.0, abs=0.001)


def test_elongated_parcel() -> None:
    elongated = Polygon(
        [(600000, 6200000), (600100, 6200000), (600100, 6200002), (600000, 6200002)]
    )
    row = enrich_parcel_shapes(_candidate_frame([elongated])).iloc[0]

    assert row["length_width_ratio"] == pytest.approx(50.0, abs=0.01)
    assert row["length_m"] >= row["width_m"]
    assert 0 <= row["compactness"] <= 1


def test_centroid_coordinates(square: Polygon) -> None:
    expected = (
        gpd.GeoSeries([square.centroid], crs="EPSG:2154").to_crs("EPSG:4326").iloc[0]
    )

    row = enrich_parcel_shapes(_candidate_frame([square])).iloc[0]

    assert row["centroid_lat"] == pytest.approx(expected.y)
    assert row["centroid_lon"] == pytest.approx(expected.x)


def test_output_geometry_remains_wgs84(square: Polygon) -> None:
    source = _candidate_frame([square])

    enriched = enrich_parcel_shapes(source)

    assert enriched.crs is not None
    assert enriched.crs.to_epsg() == 4326
    assert enriched.geometry.iloc[0].equals_exact(source.geometry.iloc[0], tolerance=0)


def test_missing_crs_fails(square: Polygon) -> None:
    source = _candidate_frame([square]).set_crs(None, allow_override=True)

    with pytest.raises(ShapeEnrichmentError, match="CRS"):
        enrich_parcel_shapes(source)


def test_missing_parcel_id_fails(square: Polygon) -> None:
    source = _candidate_frame([square]).drop(columns=["parcel_id"])

    with pytest.raises(ShapeEnrichmentError, match="parcel_id"):
        enrich_parcel_shapes(source)


def test_null_parcel_id_fails(square: Polygon) -> None:
    source = _candidate_frame([square])
    source.loc[0, "parcel_id"] = None

    with pytest.raises(ShapeEnrichmentError, match="null"):
        enrich_parcel_shapes(source)


def test_duplicate_parcel_id_fails(square: Polygon) -> None:
    source = _candidate_frame([square, square])
    source.loc[1, "parcel_id"] = source.loc[0, "parcel_id"]

    with pytest.raises(ShapeEnrichmentError, match="unique"):
        enrich_parcel_shapes(source)


@pytest.mark.parametrize("parcel_id", [1, "", " parcel", "parcel "])
def test_enrichment_requires_exact_non_empty_parcel_ids(
    square: Polygon,
    parcel_id: object,
) -> None:
    source = _candidate_frame([square])
    source["parcel_id"] = source["parcel_id"].astype(object)
    source.loc[0, "parcel_id"] = parcel_id

    with pytest.raises(ShapeEnrichmentError, match="exact non-empty strings"):
        enrich_parcel_shapes(source)


@pytest.mark.parametrize("area", [-1, 0, float("inf"), float("nan"), "100", True])
def test_valid_candidate_area_requires_strict_positive_finite_number(
    square: Polygon,
    area: object,
) -> None:
    source = _candidate_frame([square])
    source["area_m2"] = source["area_m2"].astype(object)
    source.loc[0, "area_m2"] = area

    with pytest.raises(ShapeEnrichmentError, match="strict positive finite numeric"):
        enrich_parcel_shapes(source)


def test_failed_geometry_does_not_remove_other_rows(square: Polygon) -> None:
    source = _candidate_frame([square, Polygon()])

    enriched = enrich_parcel_shapes(source)

    assert list(enriched["shape_status"]) == ["VALID", "ERROR"]
    assert enriched.loc[1, list(DERIVED_METRIC_COLUMNS)].isna().all()


def test_exact_parcel_ids_are_preserved(square: Polygon) -> None:
    source = _candidate_frame([square, Polygon()])

    enriched = enrich_parcel_shapes(source)

    assert len(enriched) == len(source)
    assert set(enriched["parcel_id"]) == set(source["parcel_id"])


def test_enrichment_matches_centralized_shape_metrics(square: Polygon) -> None:
    source = _candidate_frame([square])
    expected_geometry = source.to_crs(LAMBERT93).geometry.iloc[0]
    expected = parcel_shape_metrics_m(expected_geometry, LAMBERT93)

    row = enrich_parcel_shapes(source).iloc[0]

    assert row["length_m"] == pytest.approx(expected.length_m)
    assert row["width_m"] == pytest.approx(expected.width_m)
    assert row["length_width_ratio"] == pytest.approx(expected.length_width_ratio)
    assert row["compactness"] == pytest.approx(expected.compactness)


@pytest.mark.parametrize(
    "geometry_status",
    [None, "UNKNOWN", "ERROR", "BANANA", "valid", 0, 1, True, False],
)
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

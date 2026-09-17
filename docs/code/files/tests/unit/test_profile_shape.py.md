# `tests/unit/test_profile_shape.py`

## File identity

- Repository path: `tests/unit/test_profile_shape.py`
- File type: Python source
- Layer: unit/regression test
- Domain: isolated contract test evidence
- Responsibility: Exercises shape-profile summaries on ten synthetic local rows: selected area quantiles, three bucket totals, six scenario counts, VALID/ERROR denominators, input preservation and metric/ID/CRS/status domain guards; no physical-source or geometry-derived shape-metric equivalence is established.
- Source SHA256: `b7ab56caf8bf6abb5cac08f9c36f5420dccac713137c6bb95eb0c6dc70530239`

## 1. STEP 7F.1A.4 contract delta

- Refreshes permanent STEP 7F.1A.4 regression coverage for profile shape; the exact fixtures, mutations, calls, controlled failures, and assertions are inventoried below.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Exercises shape-profile summaries on ten synthetic local rows: selected area quantiles, three bucket totals, six scenario counts, VALID/ERROR denominators, input preservation and metric/ID/CRS/status domain guards; no physical-source or geometry-derived shape-metric equivalence is established.

The file belongs to the **unit/regression test** layer and **isolated contract test evidence** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- None.

### Third-party packages

- `import geopandas as gpd`
- `import pandas as pd`
- `import pytest`
- `from numpy import sqrt`
- `from shapely.geometry import Polygon`

### Internal LandScout imports

- `from landscout.stages.profile_shape import (
    ShapeProfileError,
    profile_shape_distribution,
)`

## 4. Contract taxonomy

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

No module-level constant, alias, schema, mapping, or meaningful dunder assignment is declared.

### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

No top-level class/model/dataclass is declared.

## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `_with_error_row`

**Purpose:** Copy the ten-row fixture, mark row 9 ERROR and null its six shape metrics while retaining valid geometry/area; return the mixed local frame.

**Exact signature**

```python
def _with_error_row(parcels: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `mixed`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_profile_shape::test_mixed_valid_and_error_rows_are_counted` via `_with_error_row`
- value/type reference: `tests.unit.test_profile_shape::test_mixed_valid_and_error_rows_are_counted` via `_with_error_row`
- direct call: `tests.unit.test_profile_shape::test_error_rows_are_excluded_from_percentiles` via `_with_error_row`
- value/type reference: `tests.unit.test_profile_shape::test_error_rows_are_excluded_from_percentiles` via `_with_error_row`
- direct call: `tests.unit.test_profile_shape::test_error_rows_are_excluded_from_buckets` via `_with_error_row`
- value/type reference: `tests.unit.test_profile_shape::test_error_rows_are_excluded_from_buckets` via `_with_error_row`
- direct call: `tests.unit.test_profile_shape::test_scenario_percentages_use_valid_count` via `_with_error_row`
- value/type reference: `tests.unit.test_profile_shape::test_scenario_percentages_use_valid_count` via `_with_error_row`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `parcels.copy` | `geopandas.GeoDataFrame.copy` (the injected fixture value) |

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
| In-memory mutation | `mixed.loc[9, "shape_status"] = "ERROR"`<br>`mixed.loc[9, column] = None` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _with_error_row(parcels: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    mixed = parcels.copy()
    mixed.loc[9, "shape_status"] = "ERROR"
    for column in (
        "length_m",
        "width_m",
        "length_width_ratio",
        "compactness",
        "centroid_lat",
        "centroid_lon",
    ):
        mixed.loc[9, column] = None
    return mixed
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `parcels`

**Purpose:** Create ten synthetic WGS84 square parcels with independently remeasured EPSG:2154 areas 100..1000, but supply separate internally consistent diagnostic shape metrics. Those metrics are not derived from the fixture squares; this is local profile validation, not source-bound metric recomputation.

**Exact signature**

```python
def parcels() -> gpd.GeoDataFrame:
```

- Exact decorators: `pytest.fixture`.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

- No parameters.

**Return and exception contract**

- Exact observed return expressions:
  - `gpd.GeoDataFrame(<br>        {<br>            "parcel_id": [f"313950000A{index + 1:04d}" for index in range(count)],<br>            "commune_code": ["31395"] * count,<br>            "section_prefix": ["000"] * count,<br>            "section": ["A"] * count,<br>            "parcel_number": [str(index + 1) for index in range(count)],<br>            "source_contenance": [None] * count,<br>            "source_arpente": [None] * count,<br>            "source_created_at": [None] * count,<br>            "source_updated_at": [None] * count,<br>            "geometry_status": ["VALID"] * count,<br>            "area_m2": measured_areas,<br>            "geometry": geometry,<br>            "shape_status": ["VALID"] * count,<br>            "length_m": [<br>                4.0,<br>                17.5,<br>                42.0,<br>                76.5,<br>                132.0,<br>                216.0,<br>                420.0,<br>                900.0,<br>                1650.0,<br>                300.0,<br>            ],<br>            "width_m": [4.0, 7.0, 12.0, 17.0, 22.0, 27.0, 35.0, 45.0, 55.0, 60.0],<br>            "length_width_ratio": [1.0, 2.5, 3.5, 4.5, 6.0, 8.0, 12.0, 20.0, 30.0, 5.0],<br>            "compactness": [0.02, 0.07, 0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85],<br>            "centroid_lat": [43.0 + index / 100 for index in range(count)],<br>            "centroid_lon": [2.0 + index / 100 for index in range(count)],<br>        },<br>        geometry="geometry",<br>        crs="EPSG:4326",<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- value/type reference: `tests.unit.test_profile_shape::_with_error_row` via `parcels`
- value/type reference: `tests.unit.test_profile_shape::test_percentile_calculation` via `parcels`
- value/type reference: `tests.unit.test_profile_shape::test_bucket_counts_sum_to_input_count` via `parcels`
- value/type reference: `tests.unit.test_profile_shape::test_existing_all_valid_behavior_is_unchanged` via `parcels`
- value/type reference: `tests.unit.test_profile_shape::test_diagnostic_scenario_counts` via `parcels`
- value/type reference: `tests.unit.test_profile_shape::test_input_is_not_mutated` via `parcels`
- value/type reference: `tests.unit.test_profile_shape::test_missing_metric_fails` via `parcels`
- value/type reference: `tests.unit.test_profile_shape::test_null_parcel_id_fails` via `parcels`
- value/type reference: `tests.unit.test_profile_shape::test_duplicate_parcel_id_fails` via `parcels`
- value/type reference: `tests.unit.test_profile_shape::test_missing_crs_fails` via `parcels`
- value/type reference: `tests.unit.test_profile_shape::test_null_metric_on_valid_shape_fails` via `parcels`
- value/type reference: `tests.unit.test_profile_shape::test_mixed_valid_and_error_rows_are_counted` via `parcels`
- value/type reference: `tests.unit.test_profile_shape::test_error_rows_are_excluded_from_percentiles` via `parcels`
- value/type reference: `tests.unit.test_profile_shape::test_error_rows_are_excluded_from_buckets` via `parcels`
- value/type reference: `tests.unit.test_profile_shape::test_scenario_percentages_use_valid_count` via `parcels`
- value/type reference: `tests.unit.test_profile_shape::test_unexpected_shape_status_fails` via `parcels`
- value/type reference: `tests.unit.test_profile_shape::test_non_finite_metric_on_valid_row_fails` via `parcels`
- value/type reference: `tests.unit.test_profile_shape::test_zero_valid_rows_fails_clearly` via `parcels`
- value/type reference: `tests.unit.test_profile_shape::test_valid_shape_metrics_require_physical_domains` via `parcels`
- value/type reference: `tests.unit.test_profile_shape::test_valid_shape_length_must_not_be_less_than_width` via `parcels`
- value/type reference: `tests.unit.test_profile_shape::test_valid_shape_ratio_must_match_length_divided_by_width` via `parcels`
- value/type reference: `tests.unit.test_profile_shape::test_valid_shape_metrics_reject_bool_and_numeric_strings` via `parcels`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `range` | `unresolved local/third-party receiver; no ownership inferred` |
| `gpd.GeoSeries` | `geopandas.GeoSeries` |
| `Polygon` | `shapely.geometry.Polygon` |
| `sqrt` | `numpy.sqrt` |
| `enumerate` | `unresolved local/third-party receiver; no ownership inferred` |
| `projected.to_crs` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry.to_crs("EPSG:2154").area.tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry.to_crs` | `unresolved local/third-party receiver; no ownership inferred` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `projected.to_crs`<br>`geometry.to_crs("EPSG:2154").area.tolist`<br>`geometry.to_crs` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def parcels() -> gpd.GeoDataFrame:
    count = 10
    target_areas = [100.0 * (index + 1) for index in range(count)]
    projected = gpd.GeoSeries(
        [
            Polygon(
                [
                    (600000 + index * 100, 6200000),
                    (600000 + index * 100 + sqrt(area), 6200000),
                    (600000 + index * 100 + sqrt(area), 6200000 + sqrt(area)),
                    (600000 + index * 100, 6200000 + sqrt(area)),
                ]
            )
            for index, area in enumerate(target_areas)
        ],
        crs="EPSG:2154",
    )
    geometry = projected.to_crs("EPSG:4326")
    measured_areas = geometry.to_crs("EPSG:2154").area.tolist()
    return gpd.GeoDataFrame(
        {
            "parcel_id": [f"313950000A{index + 1:04d}" for index in range(count)],
            "commune_code": ["31395"] * count,
            "section_prefix": ["000"] * count,
            "section": ["A"] * count,
            "parcel_number": [str(index + 1) for index in range(count)],
            "source_contenance": [None] * count,
            "source_arpente": [None] * count,
            "source_created_at": [None] * count,
            "source_updated_at": [None] * count,
            "geometry_status": ["VALID"] * count,
            "area_m2": measured_areas,
            "geometry": geometry,
            "shape_status": ["VALID"] * count,
            "length_m": [
                4.0,
                17.5,
                42.0,
                76.5,
                132.0,
                216.0,
                420.0,
                900.0,
                1650.0,
                300.0,
            ],
            "width_m": [4.0, 7.0, 12.0, 17.0, 22.0, 27.0, 35.0, 45.0, 55.0, 60.0],
            "length_width_ratio": [1.0, 2.5, 3.5, 4.5, 6.0, 8.0, 12.0, 20.0, 30.0, 5.0],
            "compactness": [0.02, 0.07, 0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85],
            "centroid_lat": [43.0 + index / 100 for index in range(count)],
            "centroid_lon": [2.0 + index / 100 for index in range(count)],
        },
        geometry="geometry",
        crs="EPSG:4326",
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_percentile_calculation`

**Purpose:** Assert area minimum 100, median 550 and maximum 1000 plus the exact eleven distribution keys; other quantile values are not individually asserted.

**Exact signature**

```python
def test_percentile_calculation(parcels: gpd.GeoDataFrame) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert area["min"] == pytest.approx(100.0)`
  - `assert area["p50"] == pytest.approx(550.0)`
  - `assert area["max"] == pytest.approx(1000.0)`
  - `assert set(area) == {<br>        "min",<br>        "p01",<br>        "p05",<br>        "p10",<br>        "p25",<br>        "p50",<br>        "p75",<br>        "p90",<br>        "p95",<br>        "p99",<br>        "max",<br>    }`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `profile_shape_distribution` | `landscout.stages.profile_shape.profile_shape_distribution` |
| `pytest.approx` | `pytest.approx` |
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_bucket_counts_sum_to_input_count`

**Purpose:** Require each of the width, ratio and compactness bucket totals to equal all ten valid rows.

**Exact signature**

```python
def test_bucket_counts_sum_to_input_count(parcels: gpd.GeoDataFrame) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert sum(profile.width_buckets.values()) == len(parcels)`
  - `assert sum(profile.ratio_buckets.values()) == len(parcels)`
  - `assert sum(profile.compactness_buckets.values()) == len(parcels)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `profile_shape_distribution` | `landscout.stages.profile_shape.profile_shape_distribution` |
| `sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `profile.width_buckets.values` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `profile.ratio_buckets.values` | `unresolved local/third-party receiver; no ownership inferred` |
| `profile.compactness_buckets.values` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_bucket_counts_sum_to_input_count(parcels: gpd.GeoDataFrame) -> None:
    profile = profile_shape_distribution(parcels)

    assert sum(profile.width_buckets.values()) == len(parcels)
    assert sum(profile.ratio_buckets.values()) == len(parcels)
    assert sum(profile.compactness_buckets.values()) == len(parcels)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_existing_all_valid_behavior_is_unchanged`

**Purpose:** Assert input=valid=10, error=0 and area maximum 1000 for the baseline all-VALID fixture.

**Exact signature**

```python
def test_existing_all_valid_behavior_is_unchanged(parcels: gpd.GeoDataFrame) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert profile.input_count == 10`
  - `assert profile.valid_count == 10`
  - `assert profile.error_count == 0`
  - `assert profile.distributions["area_m2"]["max"] == pytest.approx(1000.0)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `profile_shape_distribution` | `landscout.stages.profile_shape.profile_shape_distribution` |
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
def test_existing_all_valid_behavior_is_unchanged(parcels: gpd.GeoDataFrame) -> None:
    profile = profile_shape_distribution(parcels)

    assert profile.input_count == 10
    assert profile.valid_count == 10
    assert profile.error_count == 0
    assert profile.distributions["area_m2"]["max"] == pytest.approx(1000.0)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_diagnostic_scenario_counts`

**Purpose:** Assert diagnostic scenarios A..F retain 8, 7, 6, 4, 2 and 1 fixture rows respectively; these are summary scenarios, not new screening policy.

**Exact signature**

```python
def test_diagnostic_scenario_counts(parcels: gpd.GeoDataFrame) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert profile.scenarios["A"].retained_count == 8`
  - `assert profile.scenarios["B"].retained_count == 7`
  - `assert profile.scenarios["C"].retained_count == 6`
  - `assert profile.scenarios["D"].retained_count == 4`
  - `assert profile.scenarios["E"].retained_count == 2`
  - `assert profile.scenarios["F"].retained_count == 1`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `profile_shape_distribution` | `landscout.stages.profile_shape.profile_shape_distribution` |

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
def test_diagnostic_scenario_counts(parcels: gpd.GeoDataFrame) -> None:
    profile = profile_shape_distribution(parcels)

    assert profile.scenarios["A"].retained_count == 8
    assert profile.scenarios["B"].retained_count == 7
    assert profile.scenarios["C"].retained_count == 6
    assert profile.scenarios["D"].retained_count == 4
    assert profile.scenarios["E"].retained_count == 2
    assert profile.scenarios["F"].retained_count == 1
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_input_is_not_mutated`

**Purpose:** Compare the input to a deep copy with pandas.testing.assert_frame_equal after profiling; the helper assertion is not counted as an assert statement in the generated index.

**Exact signature**

```python
def test_input_is_not_mutated(parcels: gpd.GeoDataFrame) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `parcels.copy` | `geopandas.GeoDataFrame.copy` (the injected fixture value) |
| `profile_shape_distribution` | `landscout.stages.profile_shape.profile_shape_distribution` |
| `pd.testing.assert_frame_equal` | `pandas.testing.assert_frame_equal` |

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
def test_input_is_not_mutated(parcels: gpd.GeoDataFrame) -> None:
    original = parcels.copy(deep=True)

    profile_shape_distribution(parcels)

    pd.testing.assert_frame_equal(parcels, original)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_missing_metric_fails`

**Purpose:** Drop width_m into a new local frame and require a width_m error.

**Exact signature**

```python
def test_missing_metric_fails(parcels: gpd.GeoDataFrame) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ShapeProfileError, match="width_m")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `parcels.drop` | `geopandas.GeoDataFrame.drop` (the injected fixture value) |
| `pytest.raises` | `pytest.raises` |
| `profile_shape_distribution` | `landscout.stages.profile_shape.profile_shape_distribution` |

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
| In-memory mutation | None on existing frames; non-inplace `drop` returns a new frame. |
| Direct parameter mutation | None; `drop` is not inplace. |

**Complete source-ordered implementation**

```python
def test_missing_metric_fails(parcels: gpd.GeoDataFrame) -> None:
    without_width = parcels.drop(columns=["width_m"])

    with pytest.raises(ShapeProfileError, match="width_m"):
        profile_shape_distribution(without_width)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_null_parcel_id_fails`

**Purpose:** Replace one copied ID with None and require a null-ID error.

**Exact signature**

```python
def test_null_parcel_id_fails(parcels: gpd.GeoDataFrame) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ShapeProfileError, match="null")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `parcels.copy` | `geopandas.GeoDataFrame.copy` (the injected fixture value) |
| `pytest.raises` | `pytest.raises` |
| `profile_shape_distribution` | `landscout.stages.profile_shape.profile_shape_distribution` |

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
| In-memory mutation | `with_null.loc[0, "parcel_id"] = None` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_null_parcel_id_fails(parcels: gpd.GeoDataFrame) -> None:
    with_null = parcels.copy()
    with_null.loc[0, "parcel_id"] = None

    with pytest.raises(ShapeProfileError, match="null"):
        profile_shape_distribution(with_null)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_duplicate_parcel_id_fails`

**Purpose:** Duplicate one ID in a copied frame and require the unique-ID guard.

**Exact signature**

```python
def test_duplicate_parcel_id_fails(parcels: gpd.GeoDataFrame) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ShapeProfileError, match="unique")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `parcels.copy` | `geopandas.GeoDataFrame.copy` (the injected fixture value) |
| `pytest.raises` | `pytest.raises` |
| `profile_shape_distribution` | `landscout.stages.profile_shape.profile_shape_distribution` |

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
| In-memory mutation | `with_duplicate.loc[1, "parcel_id"] = with_duplicate.loc[0, "parcel_id"]` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_duplicate_parcel_id_fails(parcels: gpd.GeoDataFrame) -> None:
    with_duplicate = parcels.copy()
    with_duplicate.loc[1, "parcel_id"] = with_duplicate.loc[0, "parcel_id"]

    with pytest.raises(ShapeProfileError, match="unique"):
        profile_shape_distribution(with_duplicate)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_missing_crs_fails`

**Purpose:** Use non-inplace set_crs(None, allow_override=True) and require a CRS error; the original fixture is not mutated.

**Exact signature**

```python
def test_missing_crs_fails(parcels: gpd.GeoDataFrame) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ShapeProfileError, match="CRS")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `parcels.set_crs` | `geopandas.GeoDataFrame.set_crs` (the injected fixture value) |
| `pytest.raises` | `pytest.raises` |
| `profile_shape_distribution` | `landscout.stages.profile_shape.profile_shape_distribution` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `parcels.set_crs` |
| External process/environment | None directly present. |
| In-memory mutation | None on existing frames; `set_crs` returns a new frame. |
| Direct parameter mutation | None; `set_crs` is not inplace. |

**Complete source-ordered implementation**

```python
def test_missing_crs_fails(parcels: gpd.GeoDataFrame) -> None:
    without_crs = parcels.set_crs(None, allow_override=True)

    with pytest.raises(ShapeProfileError, match="CRS"):
        profile_shape_distribution(without_crs)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_null_metric_on_valid_shape_fails`

**Purpose:** Null compactness on a VALID row and require complete metrics.

**Exact signature**

```python
def test_null_metric_on_valid_shape_fails(parcels: gpd.GeoDataFrame) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ShapeProfileError, match="complete")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `parcels.copy` | `geopandas.GeoDataFrame.copy` (the injected fixture value) |
| `pytest.raises` | `pytest.raises` |
| `profile_shape_distribution` | `landscout.stages.profile_shape.profile_shape_distribution` |

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
| In-memory mutation | `with_null_metric.loc[0, "compactness"] = None` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_null_metric_on_valid_shape_fails(parcels: gpd.GeoDataFrame) -> None:
    with_null_metric = parcels.copy()
    with_null_metric.loc[0, "compactness"] = None

    with pytest.raises(ShapeProfileError, match="complete"):
        profile_shape_distribution(with_null_metric)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_mixed_valid_and_error_rows_are_counted`

**Purpose:** Mark the final row ERROR through the helper and assert input 10, valid 9, error 1 and count closure.

**Exact signature**

```python
def test_mixed_valid_and_error_rows_are_counted(parcels: gpd.GeoDataFrame) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert profile.input_count == 10`
  - `assert profile.valid_count == 9`
  - `assert profile.error_count == 1`
  - `assert profile.input_count == profile.valid_count + profile.error_count`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `profile_shape_distribution` | `landscout.stages.profile_shape.profile_shape_distribution` |
| `_with_error_row` | `tests.unit.test_profile_shape._with_error_row` |

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
def test_mixed_valid_and_error_rows_are_counted(parcels: gpd.GeoDataFrame) -> None:
    profile = profile_shape_distribution(_with_error_row(parcels))

    assert profile.input_count == 10
    assert profile.valid_count == 9
    assert profile.error_count == 1
    assert profile.input_count == profile.valid_count + profile.error_count
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_error_rows_are_excluded_from_percentiles`

**Purpose:** Mark the final 1000-square-metre row ERROR and assert the reported area maximum becomes 900.

**Exact signature**

```python
def test_error_rows_are_excluded_from_percentiles(parcels: gpd.GeoDataFrame) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert profile.distributions["area_m2"]["max"] == pytest.approx(900.0)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `profile_shape_distribution` | `landscout.stages.profile_shape.profile_shape_distribution` |
| `_with_error_row` | `tests.unit.test_profile_shape._with_error_row` |
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
def test_error_rows_are_excluded_from_percentiles(parcels: gpd.GeoDataFrame) -> None:
    profile = profile_shape_distribution(_with_error_row(parcels))

    assert profile.distributions["area_m2"]["max"] == pytest.approx(900.0)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_error_rows_are_excluded_from_buckets`

**Purpose:** Assert all three bucket totals use the nine valid rows, excluding the single ERROR row.

**Exact signature**

```python
def test_error_rows_are_excluded_from_buckets(parcels: gpd.GeoDataFrame) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert sum(profile.width_buckets.values()) == profile.valid_count == 9`
  - `assert sum(profile.ratio_buckets.values()) == profile.valid_count`
  - `assert sum(profile.compactness_buckets.values()) == profile.valid_count`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `profile_shape_distribution` | `landscout.stages.profile_shape.profile_shape_distribution` |
| `_with_error_row` | `tests.unit.test_profile_shape._with_error_row` |
| `sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `profile.width_buckets.values` | `unresolved local/third-party receiver; no ownership inferred` |
| `profile.ratio_buckets.values` | `unresolved local/third-party receiver; no ownership inferred` |
| `profile.compactness_buckets.values` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_error_rows_are_excluded_from_buckets(parcels: gpd.GeoDataFrame) -> None:
    profile = profile_shape_distribution(_with_error_row(parcels))

    assert sum(profile.width_buckets.values()) == profile.valid_count == 9
    assert sum(profile.ratio_buckets.values()) == profile.valid_count
    assert sum(profile.compactness_buckets.values()) == profile.valid_count
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_scenario_percentages_use_valid_count`

**Purpose:** Assert scenario A retains seven rows and percentage equals 7/9*100, using valid rather than total count.

**Exact signature**

```python
def test_scenario_percentages_use_valid_count(parcels: gpd.GeoDataFrame) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert profile.scenarios["A"].retained_count == 7`
  - `assert profile.scenarios["A"].retained_percentage == pytest.approx(7 / 9 * 100)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `profile_shape_distribution` | `landscout.stages.profile_shape.profile_shape_distribution` |
| `_with_error_row` | `tests.unit.test_profile_shape._with_error_row` |
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
def test_scenario_percentages_use_valid_count(parcels: gpd.GeoDataFrame) -> None:
    profile = profile_shape_distribution(_with_error_row(parcels))

    assert profile.scenarios["A"].retained_count == 7
    assert profile.scenarios["A"].retained_percentage == pytest.approx(7 / 9 * 100)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unexpected_shape_status_fails`

**Purpose:** Replace one shape_status with UNKNOWN and require the unexpected-status error.

**Exact signature**

```python
def test_unexpected_shape_status_fails(parcels: gpd.GeoDataFrame) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ShapeProfileError, match="Unexpected")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `parcels.copy` | `geopandas.GeoDataFrame.copy` (the injected fixture value) |
| `pytest.raises` | `pytest.raises` |
| `profile_shape_distribution` | `landscout.stages.profile_shape.profile_shape_distribution` |

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
| In-memory mutation | `unexpected.loc[0, "shape_status"] = "UNKNOWN"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_unexpected_shape_status_fails(parcels: gpd.GeoDataFrame) -> None:
    unexpected = parcels.copy()
    unexpected.loc[0, "shape_status"] = "UNKNOWN"

    with pytest.raises(ShapeProfileError, match="Unexpected"):
        profile_shape_distribution(unexpected)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_non_finite_metric_on_valid_row_fails`

**Purpose:** Replace a VALID row's length with positive infinity and require a finite-metric error.

**Exact signature**

```python
def test_non_finite_metric_on_valid_row_fails(parcels: gpd.GeoDataFrame) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ShapeProfileError, match="finite")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `parcels.copy` | `geopandas.GeoDataFrame.copy` (the injected fixture value) |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `profile_shape_distribution` | `landscout.stages.profile_shape.profile_shape_distribution` |

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
| In-memory mutation | `non_finite.loc[0, "length_m"] = float("inf")` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_non_finite_metric_on_valid_row_fails(parcels: gpd.GeoDataFrame) -> None:
    non_finite = parcels.copy()
    non_finite.loc[0, "length_m"] = float("inf")

    with pytest.raises(ShapeProfileError, match="finite"):
        profile_shape_distribution(non_finite)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_zero_valid_rows_fails_clearly`

**Purpose:** Mark every row ERROR and require at least one VALID row; retained nonnull shape metrics are not independently cleared in this fixture.

**Exact signature**

```python
def test_zero_valid_rows_fails_clearly(parcels: gpd.GeoDataFrame) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ShapeProfileError, match="At least one VALID")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `parcels.copy` | `geopandas.GeoDataFrame.copy` (the injected fixture value) |
| `pytest.raises` | `pytest.raises` |
| `profile_shape_distribution` | `landscout.stages.profile_shape.profile_shape_distribution` |

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
| In-memory mutation | `errors_only["shape_status"] = "ERROR"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_zero_valid_rows_fails_clearly(parcels: gpd.GeoDataFrame) -> None:
    errors_only = parcels.copy()
    errors_only["shape_status"] = "ERROR"

    with pytest.raises(ShapeProfileError, match="At least one VALID"):
        profile_shape_distribution(errors_only)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_valid_shape_metrics_require_physical_domains`

**Purpose:** Reject eight area/length/width/ratio/compactness/latitude/longitude domain violations with their specified error messages.

**Exact signature**

```python
def test_valid_shape_metrics_require_physical_domains(
    parcels: gpd.GeoDataFrame,
    column: str,
    value: float,
    message: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("column", "value", "message"),
    [
        ("area_m2", 0, "area_m2 must be greater than zero"),
        ("length_m", 0, "length_m must be greater than zero"),
        ("width_m", -1, "width_m must be greater than zero"),
        ("length_width_ratio", 0.99, "length_width_ratio must be at least one"),
        ("compactness", 0, "compactness must be greater than zero and at most one"),
        ("compactness", 1.01, "compactness must be greater than zero and at most one"),
        ("centroid_lat", 90.1, "centroid_lat must be between -90 and 90"),
        ("centroid_lon", 180.1, "centroid_lon must be between -180 and 180"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `column` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `float` | `required` |
| `message` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ShapeProfileError, match=message)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `parcels.copy` | `geopandas.GeoDataFrame.copy` (the injected fixture value) |
| `pytest.raises` | `pytest.raises` |
| `profile_shape_distribution` | `landscout.stages.profile_shape.profile_shape_distribution` |
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
| In-memory mutation | `invalid.loc[0, column] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_valid_shape_length_must_not_be_less_than_width`

**Purpose:** Set length 3 while width remains 4 and require length at least width.

**Exact signature**

```python
def test_valid_shape_length_must_not_be_less_than_width(
    parcels: gpd.GeoDataFrame,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ShapeProfileError, match="length_m must be at least width_m")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `parcels.copy` | `geopandas.GeoDataFrame.copy` (the injected fixture value) |
| `pytest.raises` | `pytest.raises` |
| `profile_shape_distribution` | `landscout.stages.profile_shape.profile_shape_distribution` |

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
| In-memory mutation | `invalid.loc[0, "length_m"] = 3` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_valid_shape_length_must_not_be_less_than_width(
    parcels: gpd.GeoDataFrame,
) -> None:
    invalid = parcels.copy()
    invalid.loc[0, "length_m"] = 3

    with pytest.raises(ShapeProfileError, match="length_m must be at least width_m"):
        profile_shape_distribution(invalid)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_valid_shape_ratio_must_match_length_divided_by_width`

**Purpose:** Set ratio 2 for the 4-by-4 metric row and require consistency with length/width.

**Exact signature**

```python
def test_valid_shape_ratio_must_match_length_divided_by_width(
    parcels: gpd.GeoDataFrame,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ShapeProfileError, match="must equal length_m / width_m")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `parcels.copy` | `geopandas.GeoDataFrame.copy` (the injected fixture value) |
| `pytest.raises` | `pytest.raises` |
| `profile_shape_distribution` | `landscout.stages.profile_shape.profile_shape_distribution` |

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
| In-memory mutation | `invalid.loc[0, "length_width_ratio"] = 2` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_valid_shape_ratio_must_match_length_divided_by_width(
    parcels: gpd.GeoDataFrame,
) -> None:
    invalid = parcels.copy()
    invalid.loc[0, "length_width_ratio"] = 2

    with pytest.raises(ShapeProfileError, match="must equal length_m / width_m"):
        profile_shape_distribution(invalid)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_valid_shape_metrics_reject_bool_and_numeric_strings`

**Purpose:** Reject True and numeric text in area_m2 after casting it to object; this parametrization targets area, not every metric column.

**Exact signature**

```python
def test_valid_shape_metrics_reject_bool_and_numeric_strings(
    parcels: gpd.GeoDataFrame,
    value: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("value", [True, "100"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ShapeProfileError, match="numeric and finite")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `parcels.copy` | `geopandas.GeoDataFrame.copy` (the injected fixture value) |
| `invalid["area_m2"].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `profile_shape_distribution` | `landscout.stages.profile_shape.profile_shape_distribution` |
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
| In-memory mutation | `invalid["area_m2"] = invalid["area_m2"].astype(object)`<br>`invalid.loc[0, "area_m2"] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.


## 7. Test-specific regression contract

Exercises shape-profile summaries on ten synthetic local rows: selected area quantiles, three bucket totals, six scenario counts, VALID/ERROR denominators, input preservation and metric/ID/CRS/status domain guards; no physical-source or geometry-derived shape-metric equivalence is established.

The 21 test definitions expand statically to 29 cases; no test run is claimed for this documentation audit. No test here asserts the exact representative/extreme ID ordering.

- Test functions: **21**.
- Pytest fixtures (decorator-proven): **1**.

### Fixtures

- `parcels` — decorators: `pytest.fixture`.

### Per-test regression index

| Test | Parametrization | Expected exception contexts | Assertion count | Exact regression purpose |
|---|---|---|---:|---|
| `test_percentile_calculation` | none | none | 4 | Assert area minimum 100, median 550 and maximum 1000 plus the exact eleven distribution keys; other quantile values are not individually asserted. |
| `test_bucket_counts_sum_to_input_count` | none | none | 3 | Require each of the width, ratio and compactness bucket totals to equal all ten valid rows. |
| `test_existing_all_valid_behavior_is_unchanged` | none | none | 4 | Assert input=valid=10, error=0 and area maximum 1000 for the baseline all-VALID fixture. |
| `test_diagnostic_scenario_counts` | none | none | 6 | Assert diagnostic scenarios A..F retain 8, 7, 6, 4, 2 and 1 fixture rows respectively; these are summary scenarios, not new screening policy. |
| `test_input_is_not_mutated` | none | none | 0 | Compare the input to a deep copy with pandas.testing.assert_frame_equal after profiling; the helper assertion is not counted as an assert statement in the generated index. |
| `test_missing_metric_fails` | none | pytest.raises(ShapeProfileError, match="width_m") | 0 | Drop width_m into a new local frame and require a width_m error. |
| `test_null_parcel_id_fails` | none | pytest.raises(ShapeProfileError, match="null") | 0 | Replace one copied ID with None and require a null-ID error. |
| `test_duplicate_parcel_id_fails` | none | pytest.raises(ShapeProfileError, match="unique") | 0 | Duplicate one ID in a copied frame and require the unique-ID guard. |
| `test_missing_crs_fails` | none | pytest.raises(ShapeProfileError, match="CRS") | 0 | Use non-inplace set_crs(None, allow_override=True) and require a CRS error; the original fixture is not mutated. |
| `test_null_metric_on_valid_shape_fails` | none | pytest.raises(ShapeProfileError, match="complete") | 0 | Null compactness on a VALID row and require complete metrics. |
| `test_mixed_valid_and_error_rows_are_counted` | none | none | 4 | Mark the final row ERROR through the helper and assert input 10, valid 9, error 1 and count closure. |
| `test_error_rows_are_excluded_from_percentiles` | none | none | 1 | Mark the final 1000-square-metre row ERROR and assert the reported area maximum becomes 900. |
| `test_error_rows_are_excluded_from_buckets` | none | none | 3 | Assert all three bucket totals use the nine valid rows, excluding the single ERROR row. |
| `test_scenario_percentages_use_valid_count` | none | none | 2 | Assert scenario A retains seven rows and percentage equals 7/9*100, using valid rather than total count. |
| `test_unexpected_shape_status_fails` | none | pytest.raises(ShapeProfileError, match="Unexpected") | 0 | Replace one shape_status with UNKNOWN and require the unexpected-status error. |
| `test_non_finite_metric_on_valid_row_fails` | none | pytest.raises(ShapeProfileError, match="finite") | 0 | Replace a VALID row's length with positive infinity and require a finite-metric error. |
| `test_zero_valid_rows_fails_clearly` | none | pytest.raises(ShapeProfileError, match="At least one VALID") | 0 | Mark every row ERROR and require at least one VALID row; retained nonnull shape metrics are not independently cleared in this fixture. |
| `test_valid_shape_metrics_require_physical_domains` | pytest.mark.parametrize(<br>    ("column", "value", "message"),<br>    [<br>        ("area_m2", 0, "area_m2 must be greater than zero"),<br>        ("length_m", 0, "length_m must be greater than zero"),<br>        ("width_m", -1, "width_m must be greater than zero"),<br>        ("length_width_ratio", 0.99, "length_width_ratio must be at least one"),<br>        ("compactness", 0, "compactness must be greater than zero and at most one"),<br>        ("compactness", 1.01, "compactness must be greater than zero and at most one"),<br>        ("centroid_lat", 90.1, "centroid_lat must be between -90 and 90"),<br>        ("centroid_lon", 180.1, "centroid_lon must be between -180 and 180"),<br>    ],<br>) | pytest.raises(ShapeProfileError, match=message) | 0 | Reject eight area/length/width/ratio/compactness/latitude/longitude domain violations with their specified error messages. |
| `test_valid_shape_length_must_not_be_less_than_width` | none | pytest.raises(ShapeProfileError, match="length_m must be at least width_m") | 0 | Set length 3 while width remains 4 and require length at least width. |
| `test_valid_shape_ratio_must_match_length_divided_by_width` | none | pytest.raises(ShapeProfileError, match="must equal length_m / width_m") | 0 | Set ratio 2 for the 4-by-4 metric row and require consistency with length/width. |
| `test_valid_shape_metrics_reject_bool_and_numeric_strings` | pytest.mark.parametrize("value", [True, "100"]) | pytest.raises(ShapeProfileError, match="numeric and finite") | 0 | Reject True and numeric text in area_m2 after casting it to object; this parametrization targets area, not every metric column. |

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
import pandas as pd
import pytest
from numpy import sqrt
from shapely.geometry import Polygon

from landscout.stages.profile_shape import (
    ShapeProfileError,
    profile_shape_distribution,
)


def _with_error_row(parcels: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    mixed = parcels.copy()
    mixed.loc[9, "shape_status"] = "ERROR"
    for column in (
        "length_m",
        "width_m",
        "length_width_ratio",
        "compactness",
        "centroid_lat",
        "centroid_lon",
    ):
        mixed.loc[9, column] = None
    return mixed


@pytest.fixture
def parcels() -> gpd.GeoDataFrame:
    count = 10
    target_areas = [100.0 * (index + 1) for index in range(count)]
    projected = gpd.GeoSeries(
        [
            Polygon(
                [
                    (600000 + index * 100, 6200000),
                    (600000 + index * 100 + sqrt(area), 6200000),
                    (600000 + index * 100 + sqrt(area), 6200000 + sqrt(area)),
                    (600000 + index * 100, 6200000 + sqrt(area)),
                ]
            )
            for index, area in enumerate(target_areas)
        ],
        crs="EPSG:2154",
    )
    geometry = projected.to_crs("EPSG:4326")
    measured_areas = geometry.to_crs("EPSG:2154").area.tolist()
    return gpd.GeoDataFrame(
        {
            "parcel_id": [f"313950000A{index + 1:04d}" for index in range(count)],
            "commune_code": ["31395"] * count,
            "section_prefix": ["000"] * count,
            "section": ["A"] * count,
            "parcel_number": [str(index + 1) for index in range(count)],
            "source_contenance": [None] * count,
            "source_arpente": [None] * count,
            "source_created_at": [None] * count,
            "source_updated_at": [None] * count,
            "geometry_status": ["VALID"] * count,
            "area_m2": measured_areas,
            "geometry": geometry,
            "shape_status": ["VALID"] * count,
            "length_m": [
                4.0,
                17.5,
                42.0,
                76.5,
                132.0,
                216.0,
                420.0,
                900.0,
                1650.0,
                300.0,
            ],
            "width_m": [4.0, 7.0, 12.0, 17.0, 22.0, 27.0, 35.0, 45.0, 55.0, 60.0],
            "length_width_ratio": [1.0, 2.5, 3.5, 4.5, 6.0, 8.0, 12.0, 20.0, 30.0, 5.0],
            "compactness": [0.02, 0.07, 0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85],
            "centroid_lat": [43.0 + index / 100 for index in range(count)],
            "centroid_lon": [2.0 + index / 100 for index in range(count)],
        },
        geometry="geometry",
        crs="EPSG:4326",
    )


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


def test_bucket_counts_sum_to_input_count(parcels: gpd.GeoDataFrame) -> None:
    profile = profile_shape_distribution(parcels)

    assert sum(profile.width_buckets.values()) == len(parcels)
    assert sum(profile.ratio_buckets.values()) == len(parcels)
    assert sum(profile.compactness_buckets.values()) == len(parcels)


def test_existing_all_valid_behavior_is_unchanged(parcels: gpd.GeoDataFrame) -> None:
    profile = profile_shape_distribution(parcels)

    assert profile.input_count == 10
    assert profile.valid_count == 10
    assert profile.error_count == 0
    assert profile.distributions["area_m2"]["max"] == pytest.approx(1000.0)


def test_diagnostic_scenario_counts(parcels: gpd.GeoDataFrame) -> None:
    profile = profile_shape_distribution(parcels)

    assert profile.scenarios["A"].retained_count == 8
    assert profile.scenarios["B"].retained_count == 7
    assert profile.scenarios["C"].retained_count == 6
    assert profile.scenarios["D"].retained_count == 4
    assert profile.scenarios["E"].retained_count == 2
    assert profile.scenarios["F"].retained_count == 1


def test_input_is_not_mutated(parcels: gpd.GeoDataFrame) -> None:
    original = parcels.copy(deep=True)

    profile_shape_distribution(parcels)

    pd.testing.assert_frame_equal(parcels, original)


def test_missing_metric_fails(parcels: gpd.GeoDataFrame) -> None:
    without_width = parcels.drop(columns=["width_m"])

    with pytest.raises(ShapeProfileError, match="width_m"):
        profile_shape_distribution(without_width)


def test_null_parcel_id_fails(parcels: gpd.GeoDataFrame) -> None:
    with_null = parcels.copy()
    with_null.loc[0, "parcel_id"] = None

    with pytest.raises(ShapeProfileError, match="null"):
        profile_shape_distribution(with_null)


def test_duplicate_parcel_id_fails(parcels: gpd.GeoDataFrame) -> None:
    with_duplicate = parcels.copy()
    with_duplicate.loc[1, "parcel_id"] = with_duplicate.loc[0, "parcel_id"]

    with pytest.raises(ShapeProfileError, match="unique"):
        profile_shape_distribution(with_duplicate)


def test_missing_crs_fails(parcels: gpd.GeoDataFrame) -> None:
    without_crs = parcels.set_crs(None, allow_override=True)

    with pytest.raises(ShapeProfileError, match="CRS"):
        profile_shape_distribution(without_crs)


def test_null_metric_on_valid_shape_fails(parcels: gpd.GeoDataFrame) -> None:
    with_null_metric = parcels.copy()
    with_null_metric.loc[0, "compactness"] = None

    with pytest.raises(ShapeProfileError, match="complete"):
        profile_shape_distribution(with_null_metric)


def test_mixed_valid_and_error_rows_are_counted(parcels: gpd.GeoDataFrame) -> None:
    profile = profile_shape_distribution(_with_error_row(parcels))

    assert profile.input_count == 10
    assert profile.valid_count == 9
    assert profile.error_count == 1
    assert profile.input_count == profile.valid_count + profile.error_count


def test_error_rows_are_excluded_from_percentiles(parcels: gpd.GeoDataFrame) -> None:
    profile = profile_shape_distribution(_with_error_row(parcels))

    assert profile.distributions["area_m2"]["max"] == pytest.approx(900.0)


def test_error_rows_are_excluded_from_buckets(parcels: gpd.GeoDataFrame) -> None:
    profile = profile_shape_distribution(_with_error_row(parcels))

    assert sum(profile.width_buckets.values()) == profile.valid_count == 9
    assert sum(profile.ratio_buckets.values()) == profile.valid_count
    assert sum(profile.compactness_buckets.values()) == profile.valid_count


def test_scenario_percentages_use_valid_count(parcels: gpd.GeoDataFrame) -> None:
    profile = profile_shape_distribution(_with_error_row(parcels))

    assert profile.scenarios["A"].retained_count == 7
    assert profile.scenarios["A"].retained_percentage == pytest.approx(7 / 9 * 100)


def test_unexpected_shape_status_fails(parcels: gpd.GeoDataFrame) -> None:
    unexpected = parcels.copy()
    unexpected.loc[0, "shape_status"] = "UNKNOWN"

    with pytest.raises(ShapeProfileError, match="Unexpected"):
        profile_shape_distribution(unexpected)


def test_non_finite_metric_on_valid_row_fails(parcels: gpd.GeoDataFrame) -> None:
    non_finite = parcels.copy()
    non_finite.loc[0, "length_m"] = float("inf")

    with pytest.raises(ShapeProfileError, match="finite"):
        profile_shape_distribution(non_finite)


def test_zero_valid_rows_fails_clearly(parcels: gpd.GeoDataFrame) -> None:
    errors_only = parcels.copy()
    errors_only["shape_status"] = "ERROR"

    with pytest.raises(ShapeProfileError, match="At least one VALID"):
        profile_shape_distribution(errors_only)


@pytest.mark.parametrize(
    ("column", "value", "message"),
    [
        ("area_m2", 0, "area_m2 must be greater than zero"),
        ("length_m", 0, "length_m must be greater than zero"),
        ("width_m", -1, "width_m must be greater than zero"),
        ("length_width_ratio", 0.99, "length_width_ratio must be at least one"),
        ("compactness", 0, "compactness must be greater than zero and at most one"),
        ("compactness", 1.01, "compactness must be greater than zero and at most one"),
        ("centroid_lat", 90.1, "centroid_lat must be between -90 and 90"),
        ("centroid_lon", 180.1, "centroid_lon must be between -180 and 180"),
    ],
)
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


def test_valid_shape_length_must_not_be_less_than_width(
    parcels: gpd.GeoDataFrame,
) -> None:
    invalid = parcels.copy()
    invalid.loc[0, "length_m"] = 3

    with pytest.raises(ShapeProfileError, match="length_m must be at least width_m"):
        profile_shape_distribution(invalid)


def test_valid_shape_ratio_must_match_length_divided_by_width(
    parcels: gpd.GeoDataFrame,
) -> None:
    invalid = parcels.copy()
    invalid.loc[0, "length_width_ratio"] = 2

    with pytest.raises(ShapeProfileError, match="must equal length_m / width_m"):
        profile_shape_distribution(invalid)


@pytest.mark.parametrize("value", [True, "100"])
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

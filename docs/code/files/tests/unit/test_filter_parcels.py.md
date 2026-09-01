# `tests/unit/test_filter_parcels.py`

## File identity

- Repository path: `tests/unit/test_filter_parcels.py`
- File type: Python source
- Layer: unit/regression test
- Domain: isolated contract test evidence
- Responsibility: Provides complete unit and regression coverage for the `filter_parcels` contracts exercised in this file.
- Source SHA256: `3122ccfd47fbaf6ac079ab733ddb5235b5053d25c4cba5017fe9cf30b3392a89`

## 1. STEP 7F.1A.4 contract delta

- Refreshes permanent STEP 7F.1A.4 regression coverage for filter parcels; the exact fixtures, mutations, calls, controlled failures, and assertions are inventoried below.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Provides complete unit and regression coverage for the `filter_parcels` contracts exercised in this file.

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

- `from landscout.config import ParcelConfig`
- `from landscout.stages.filter_parcels import ParcelFilterError, filter_parcels_by_area`

## 4. Contract taxonomy

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `PARCEL_IDS`

- Category: module constant or closed domain.
- Exact declaration:

```python
PARCEL_IDS = {
    name: f"313950000A{index:04d}"
    for index, name in enumerate(
        (
            "at-minimum",
            "at-maximum",
            "below-minimum",
            "above-maximum",
            "invalid-geometry",
            "unknown-area",
        ),
        start=1,
    )
}
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

No top-level class/model/dataclass is declared.

## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `area_config`

**Purpose:** Implements `area config` within the file role: Provides complete unit and regression coverage for the `filter_parcels` contracts exercised in this file.

**Exact signature**

```python
def area_config() -> ParcelConfig:
```

- Exact decorators: `pytest.fixture`.
- Declared return annotation: `ParcelConfig`.

**Inputs**

- No parameters.

**Return and exception contract**

- Exact observed return expressions:
  - `ParcelConfig(min_area_m2=2000, max_area_m2=15000)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- value/type reference: `tests.unit.test_filter_parcels::test_minimum_boundary_is_included` via `area_config`
- value/type reference: `tests.unit.test_filter_parcels::test_maximum_boundary_is_included` via `area_config`
- value/type reference: `tests.unit.test_filter_parcels::test_rejected_parcel_has_expected_reason` via `area_config`
- value/type reference: `tests.unit.test_filter_parcels::test_no_parcel_disappears` via `area_config`
- value/type reference: `tests.unit.test_filter_parcels::test_area_filter_revalidates_mutated_config_before_frame_work` via `area_config`
- value/type reference: `tests.unit.test_filter_parcels::test_missing_parcel_id_fails` via `area_config`
- value/type reference: `tests.unit.test_filter_parcels::test_null_parcel_id_fails` via `area_config`
- value/type reference: `tests.unit.test_filter_parcels::test_duplicate_parcel_id_fails` via `area_config`
- value/type reference: `tests.unit.test_filter_parcels::test_candidate_and_rejected_ids_do_not_overlap` via `area_config`
- value/type reference: `tests.unit.test_filter_parcels::test_exact_parcel_ids_are_preserved` via `area_config`
- value/type reference: `tests.unit.test_filter_parcels::test_valid_geometry_requires_strict_positive_finite_area` via `area_config`
- value/type reference: `tests.unit.test_filter_parcels::test_valid_geometry_with_forged_positive_area_is_rejected` via `area_config`
- value/type reference: `tests.unit.test_filter_parcels::test_invalid_geometry_with_recorded_area_is_rejected` via `area_config`
- value/type reference: `tests.unit.test_filter_parcels::test_parcel_id_must_match_its_canonical_source_identity_fields` via `area_config`
- value/type reference: `tests.unit.test_filter_parcels::test_area_filter_requires_exact_non_empty_parcel_ids` via `area_config`
- value/type reference: `tests.unit.test_filter_parcels::test_area_filter_rejects_plain_dataframe` via `area_config`
- value/type reference: `tests.unit.test_filter_parcels::test_area_filter_rejects_duplicate_columns` via `area_config`
- value/type reference: `tests.unit.test_filter_parcels::test_area_filter_rejects_malformed_spatial_envelope` via `area_config`
- value/type reference: `tests.unit.test_filter_parcels::test_area_filter_rejects_noncanonical_geometry_status` via `area_config`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `ParcelConfig` | `landscout.config.ParcelConfig` |

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
def area_config() -> ParcelConfig:
    return ParcelConfig(min_area_m2=2000, max_area_m2=15000)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `parcels`

**Purpose:** Implements `parcels` within the file role: Provides complete unit and regression coverage for the `filter_parcels` contracts exercised in this file.

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
  - `gpd.GeoDataFrame(<br>        {<br>            "parcel_id": list(PARCEL_IDS.values()),<br>            "commune_code": ["31395"] * 6,<br>            "section_prefix": ["000"] * 6,<br>            "section": ["A"] * 6,<br>            "parcel_number": [str(index) for index in range(1, 7)],<br>            "source_contenance": [None] * 6,<br>            "source_arpente": [None] * 6,<br>            "source_created_at": [None] * 6,<br>            "source_updated_at": [None] * 6,<br>            "geometry_status": [<br>                "VALID",<br>                "VALID",<br>                "VALID",<br>                "VALID",<br>                "INVALID",<br>                "INVALID",<br>            ],<br>            "area_m2": [*areas, None, None],<br>        },<br>        geometry=geometries,<br>        crs="EPSG:4326",<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- value/type reference: `tests.unit.test_filter_parcels::test_minimum_boundary_is_included` via `parcels`
- value/type reference: `tests.unit.test_filter_parcels::test_maximum_boundary_is_included` via `parcels`
- value/type reference: `tests.unit.test_filter_parcels::test_rejected_parcel_has_expected_reason` via `parcels`
- value/type reference: `tests.unit.test_filter_parcels::test_no_parcel_disappears` via `parcels`
- value/type reference: `tests.unit.test_filter_parcels::test_thresholds_come_from_config` via `parcels`
- value/type reference: `tests.unit.test_filter_parcels::test_area_filter_revalidates_mutated_config_before_frame_work` via `parcels`
- value/type reference: `tests.unit.test_filter_parcels::test_missing_parcel_id_fails` via `parcels`
- value/type reference: `tests.unit.test_filter_parcels::test_null_parcel_id_fails` via `parcels`
- value/type reference: `tests.unit.test_filter_parcels::test_duplicate_parcel_id_fails` via `parcels`
- value/type reference: `tests.unit.test_filter_parcels::test_candidate_and_rejected_ids_do_not_overlap` via `parcels`
- value/type reference: `tests.unit.test_filter_parcels::test_exact_parcel_ids_are_preserved` via `parcels`
- value/type reference: `tests.unit.test_filter_parcels::test_valid_geometry_requires_strict_positive_finite_area` via `parcels`
- value/type reference: `tests.unit.test_filter_parcels::test_valid_geometry_with_forged_positive_area_is_rejected` via `parcels`
- value/type reference: `tests.unit.test_filter_parcels::test_invalid_geometry_with_recorded_area_is_rejected` via `parcels`
- value/type reference: `tests.unit.test_filter_parcels::test_parcel_id_must_match_its_canonical_source_identity_fields` via `parcels`
- value/type reference: `tests.unit.test_filter_parcels::test_area_filter_requires_exact_non_empty_parcel_ids` via `parcels`
- value/type reference: `tests.unit.test_filter_parcels::test_area_filter_rejects_plain_dataframe` via `parcels`
- value/type reference: `tests.unit.test_filter_parcels::test_area_filter_rejects_duplicate_columns` via `parcels`
- value/type reference: `tests.unit.test_filter_parcels::test_area_filter_rejects_malformed_spatial_envelope` via `parcels`
- value/type reference: `tests.unit.test_filter_parcels::test_area_filter_rejects_noncanonical_geometry_status` via `parcels`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `gpd.GeoSeries(<br>        [<br>            Polygon(<br>                [<br>                    (600000 + index * 1000, 6200000),<br>                    (600000 + index * 1000 + sqrt(area), 6200000),<br>                    (600000 + index * 1000 + sqrt(area), 6200000 + sqrt(area)),<br>                    (600000 + index * 1000, 6200000 + sqrt(area)),<br>                ]<br>            )<br>            for index, area in enumerate(areas)<br>        ],<br>        crs="EPSG:2154",<br>    ).to_crs` | `unresolved local/third-party receiver; no ownership inferred` |
| `gpd.GeoSeries` | `geopandas.GeoSeries` |
| `Polygon` | `shapely.geometry.Polygon` |
| `sqrt` | `numpy.sqrt` |
| `enumerate` | `unresolved local/third-party receiver; no ownership inferred` |
| `projected.tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `PARCEL_IDS.values` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `range` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `gpd.GeoSeries(<br>        [<br>            Polygon(<br>                [<br>                    (600000 + index * 1000, 6200000),<br>                    (600000 + index * 1000 + sqrt(area), 6200000),<br>                    (600000 + index * 1000 + sqrt(area), 6200000 + sqrt(area)),<br>                    (600000 + index * 1000, 6200000 + sqrt(area)),<br>                ]<br>            )<br>            for index, area in enumerate(areas)<br>        ],<br>        crs="EPSG:2154",<br>    ).to_crs` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def parcels() -> gpd.GeoDataFrame:
    areas = [2000.0, 15000.0, 1999.0, 15001.0]
    projected = gpd.GeoSeries(
        [
            Polygon(
                [
                    (600000 + index * 1000, 6200000),
                    (600000 + index * 1000 + sqrt(area), 6200000),
                    (600000 + index * 1000 + sqrt(area), 6200000 + sqrt(area)),
                    (600000 + index * 1000, 6200000 + sqrt(area)),
                ]
            )
            for index, area in enumerate(areas)
        ],
        crs="EPSG:2154",
    ).to_crs("EPSG:4326")
    geometries = [*projected.tolist(), None, Polygon()]
    return gpd.GeoDataFrame(
        {
            "parcel_id": list(PARCEL_IDS.values()),
            "commune_code": ["31395"] * 6,
            "section_prefix": ["000"] * 6,
            "section": ["A"] * 6,
            "parcel_number": [str(index) for index in range(1, 7)],
            "source_contenance": [None] * 6,
            "source_arpente": [None] * 6,
            "source_created_at": [None] * 6,
            "source_updated_at": [None] * 6,
            "geometry_status": [
                "VALID",
                "VALID",
                "VALID",
                "VALID",
                "INVALID",
                "INVALID",
            ],
            "area_m2": [*areas, None, None],
        },
        geometry=geometries,
        crs="EPSG:4326",
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_minimum_boundary_is_included`

**Purpose:** Regression invariant: minimum boundary is included. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_minimum_boundary_is_included(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `area_config` | positional-or-keyword | `ParcelConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert PARCEL_IDS["at-minimum"] in set(candidates["parcel_id"])`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `filter_parcels_by_area` | `landscout.stages.filter_parcels.filter_parcels_by_area` |
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
def test_minimum_boundary_is_included(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
    candidates, _ = filter_parcels_by_area(parcels, area_config)

    assert PARCEL_IDS["at-minimum"] in set(candidates["parcel_id"])
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_maximum_boundary_is_included`

**Purpose:** Regression invariant: maximum boundary is included. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_maximum_boundary_is_included(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `area_config` | positional-or-keyword | `ParcelConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert PARCEL_IDS["at-maximum"] in set(candidates["parcel_id"])`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `filter_parcels_by_area` | `landscout.stages.filter_parcels.filter_parcels_by_area` |
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
def test_maximum_boundary_is_included(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
    candidates, _ = filter_parcels_by_area(parcels, area_config)

    assert PARCEL_IDS["at-maximum"] in set(candidates["parcel_id"])
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_rejected_parcel_has_expected_reason`

**Purpose:** Regression invariant: rejected parcel has expected reason. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_rejected_parcel_has_expected_reason(
    parcels: gpd.GeoDataFrame,
    area_config: ParcelConfig,
    parcel_id: str,
    expected_reason: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("parcel_id", "expected_reason"),
    [
        ("below-minimum", "AREA_BELOW_MIN"),
        ("above-maximum", "AREA_ABOVE_MAX"),
        ("invalid-geometry", "INVALID_GEOMETRY"),
        ("unknown-area", "INVALID_GEOMETRY"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `area_config` | positional-or-keyword | `ParcelConfig` | `required` |
| `parcel_id` | positional-or-keyword | `str` | `required` |
| `expected_reason` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert row["rejection_reason"] == expected_reason`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `filter_parcels_by_area` | `landscout.stages.filter_parcels.filter_parcels_by_area` |
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
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_rejected_parcel_has_expected_reason(
    parcels: gpd.GeoDataFrame,
    area_config: ParcelConfig,
    parcel_id: str,
    expected_reason: str,
) -> None:
    _, rejected = filter_parcels_by_area(parcels, area_config)

    row = rejected.loc[rejected["parcel_id"] == PARCEL_IDS[parcel_id]].iloc[0]
    assert row["rejection_reason"] == expected_reason
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_no_parcel_disappears`

**Purpose:** Regression invariant: no parcel disappears. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_no_parcel_disappears(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `area_config` | positional-or-keyword | `ParcelConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert len(parcels) == len(candidates) + len(rejected)`
  - `assert set(parcels["parcel_id"]) == set(candidates["parcel_id"]) \| set(<br>        rejected["parcel_id"]<br>    )`
  - `assert candidates.crs == parcels.crs`
  - `assert rejected.crs == parcels.crs`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `filter_parcels_by_area` | `landscout.stages.filter_parcels.filter_parcels_by_area` |
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_thresholds_come_from_config`

**Purpose:** Regression invariant: thresholds come from config. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_thresholds_come_from_config(parcels: gpd.GeoDataFrame) -> None:
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
  - `assert set(candidates["parcel_id"]) == {<br>        PARCEL_IDS["below-minimum"],<br>        PARCEL_IDS["at-minimum"],<br>    }`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `ParcelConfig` | `landscout.config.ParcelConfig` |
| `filter_parcels_by_area` | `landscout.stages.filter_parcels.filter_parcels_by_area` |
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
def test_thresholds_come_from_config(parcels: gpd.GeoDataFrame) -> None:
    custom_config = ParcelConfig(min_area_m2=1999, max_area_m2=2000)

    candidates, _ = filter_parcels_by_area(parcels, custom_config)

    assert set(candidates["parcel_id"]) == {
        PARCEL_IDS["below-minimum"],
        PARCEL_IDS["at-minimum"],
    }
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_area_filter_revalidates_mutated_config_before_frame_work`

**Purpose:** Regression invariant: area filter revalidates mutated config before frame work. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_area_filter_revalidates_mutated_config_before_frame_work(
    parcels: gpd.GeoDataFrame,
    area_config: ParcelConfig,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `area_config` | positional-or-keyword | `ParcelConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ParcelFilterError, match="config")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `area_config.model_copy` | `tests.unit.test_filter_parcels.area_config.model_copy` |
| `parcels.assign` | `tests.unit.test_filter_parcels.parcels.assign` |
| `pytest.raises` | `pytest.raises` |
| `filter_parcels_by_area` | `landscout.stages.filter_parcels.filter_parcels_by_area` |

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
def test_area_filter_revalidates_mutated_config_before_frame_work(
    parcels: gpd.GeoDataFrame,
    area_config: ParcelConfig,
) -> None:
    tampered = area_config.model_copy(update={"min_area_m2": -1.0})
    colliding = parcels.assign(rejection_reason="existing")

    with pytest.raises(ParcelFilterError, match="config"):
        filter_parcels_by_area(colliding, tampered)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_missing_parcel_id_fails`

**Purpose:** Regression invariant: missing parcel id fails. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_missing_parcel_id_fails(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `area_config` | positional-or-keyword | `ParcelConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ParcelFilterError, match="parcel_id")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `parcels.drop` | `tests.unit.test_filter_parcels.parcels.drop` |
| `pytest.raises` | `pytest.raises` |
| `filter_parcels_by_area` | `landscout.stages.filter_parcels.filter_parcels_by_area` |

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
| In-memory mutation | `parcels.drop(columns=["parcel_id"])` |
| Direct parameter mutation | `parcels.drop(columns=["parcel_id"])` |

**Complete source-ordered implementation**

```python
def test_missing_parcel_id_fails(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
    without_id = parcels.drop(columns=["parcel_id"])

    with pytest.raises(ParcelFilterError, match="parcel_id"):
        filter_parcels_by_area(without_id, area_config)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_null_parcel_id_fails`

**Purpose:** Regression invariant: null parcel id fails. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_null_parcel_id_fails(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `area_config` | positional-or-keyword | `ParcelConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ParcelFilterError, match="null")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `parcels.copy` | `tests.unit.test_filter_parcels.parcels.copy` |
| `pytest.raises` | `pytest.raises` |
| `filter_parcels_by_area` | `landscout.stages.filter_parcels.filter_parcels_by_area` |

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
def test_null_parcel_id_fails(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
    with_null = parcels.copy()
    with_null.loc[0, "parcel_id"] = None

    with pytest.raises(ParcelFilterError, match="null"):
        filter_parcels_by_area(with_null, area_config)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_duplicate_parcel_id_fails`

**Purpose:** Regression invariant: duplicate parcel id fails. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_duplicate_parcel_id_fails(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `area_config` | positional-or-keyword | `ParcelConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ParcelFilterError, match="unique")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `parcels.copy` | `tests.unit.test_filter_parcels.parcels.copy` |
| `pytest.raises` | `pytest.raises` |
| `filter_parcels_by_area` | `landscout.stages.filter_parcels.filter_parcels_by_area` |

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
def test_duplicate_parcel_id_fails(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
    with_duplicate = parcels.copy()
    with_duplicate.loc[1, "parcel_id"] = with_duplicate.loc[0, "parcel_id"]

    with pytest.raises(ParcelFilterError, match="unique"):
        filter_parcels_by_area(with_duplicate, area_config)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_candidate_and_rejected_ids_do_not_overlap`

**Purpose:** Regression invariant: candidate and rejected ids do not overlap. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_candidate_and_rejected_ids_do_not_overlap(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `area_config` | positional-or-keyword | `ParcelConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert set(candidates["parcel_id"]).isdisjoint(set(rejected["parcel_id"]))`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `filter_parcels_by_area` | `landscout.stages.filter_parcels.filter_parcels_by_area` |
| `set(candidates["parcel_id"]).isdisjoint` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `set(candidates["parcel_id"]).isdisjoint` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_candidate_and_rejected_ids_do_not_overlap(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
    candidates, rejected = filter_parcels_by_area(parcels, area_config)

    assert set(candidates["parcel_id"]).isdisjoint(set(rejected["parcel_id"]))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_exact_parcel_ids_are_preserved`

**Purpose:** Regression invariant: exact parcel ids are preserved. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_exact_parcel_ids_are_preserved(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `area_config` | positional-or-keyword | `ParcelConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert len(output_ids) == len(set(output_ids))`
  - `assert set(output_ids) == set(parcels["parcel_id"])`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `filter_parcels_by_area` | `landscout.stages.filter_parcels.filter_parcels_by_area` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
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
def test_exact_parcel_ids_are_preserved(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
    candidates, rejected = filter_parcels_by_area(parcels, area_config)

    output_ids = list(candidates["parcel_id"]) + list(rejected["parcel_id"])
    assert len(output_ids) == len(set(output_ids))
    assert set(output_ids) == set(parcels["parcel_id"])
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_valid_geometry_requires_strict_positive_finite_area`

**Purpose:** Regression invariant: valid geometry requires strict positive finite area. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_valid_geometry_requires_strict_positive_finite_area(
    parcels: gpd.GeoDataFrame,
    area_config: ParcelConfig,
    area: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("area", [-1, 0, float("inf"), float("nan"), "5000", True])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `area_config` | positional-or-keyword | `ParcelConfig` | `required` |
| `area` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ParcelFilterError, match="strict positive finite numeric")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `parcels.copy` | `tests.unit.test_filter_parcels.parcels.copy` |
| `invalid["area_m2"].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `filter_parcels_by_area` | `landscout.stages.filter_parcels.filter_parcels_by_area` |
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
| In-memory mutation | `invalid["area_m2"] = invalid["area_m2"].astype(object)`<br>`invalid.loc[0, "area_m2"] = area` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_valid_geometry_with_forged_positive_area_is_rejected`

**Purpose:** Regression invariant: valid geometry with forged positive area is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_valid_geometry_with_forged_positive_area_is_rejected(
    parcels: gpd.GeoDataFrame,
    area_config: ParcelConfig,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `area_config` | positional-or-keyword | `ParcelConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ParcelFilterError, match="measured EPSG:2154")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `parcels.copy` | `tests.unit.test_filter_parcels.parcels.copy` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `filter_parcels_by_area` | `landscout.stages.filter_parcels.filter_parcels_by_area` |

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
| In-memory mutation | `invalid.loc[0, "area_m2"] = float(invalid.loc[0, "area_m2"]) + 1.0` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_valid_geometry_with_forged_positive_area_is_rejected(
    parcels: gpd.GeoDataFrame,
    area_config: ParcelConfig,
) -> None:
    invalid = parcels.copy()
    invalid.loc[0, "area_m2"] = float(invalid.loc[0, "area_m2"]) + 1.0

    with pytest.raises(ParcelFilterError, match="measured EPSG:2154"):
        filter_parcels_by_area(invalid, area_config)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_invalid_geometry_with_recorded_area_is_rejected`

**Purpose:** Regression invariant: invalid geometry with recorded area is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_invalid_geometry_with_recorded_area_is_rejected(
    parcels: gpd.GeoDataFrame,
    area_config: ParcelConfig,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `area_config` | positional-or-keyword | `ParcelConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ParcelFilterError, match="INVALID.*area_m2.*null")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `parcels.copy` | `tests.unit.test_filter_parcels.parcels.copy` |
| `pytest.raises` | `pytest.raises` |
| `filter_parcels_by_area` | `landscout.stages.filter_parcels.filter_parcels_by_area` |

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
| In-memory mutation | `invalid.loc[4, "area_m2"] = 100.0` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_invalid_geometry_with_recorded_area_is_rejected(
    parcels: gpd.GeoDataFrame,
    area_config: ParcelConfig,
) -> None:
    invalid = parcels.copy()
    invalid.loc[4, "area_m2"] = 100.0

    with pytest.raises(ParcelFilterError, match="INVALID.*area_m2.*null"):
        filter_parcels_by_area(invalid, area_config)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_parcel_id_must_match_its_canonical_source_identity_fields`

**Purpose:** Regression invariant: parcel id must match its canonical source identity fields. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_parcel_id_must_match_its_canonical_source_identity_fields(
    parcels: gpd.GeoDataFrame,
    area_config: ParcelConfig,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `area_config` | positional-or-keyword | `ParcelConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ParcelFilterError, match="must equal commune")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `parcels.copy` | `tests.unit.test_filter_parcels.parcels.copy` |
| `pytest.raises` | `pytest.raises` |
| `filter_parcels_by_area` | `landscout.stages.filter_parcels.filter_parcels_by_area` |

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
| In-memory mutation | `invalid.loc[0, "parcel_id"] = "313950000A9999"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_parcel_id_must_match_its_canonical_source_identity_fields(
    parcels: gpd.GeoDataFrame,
    area_config: ParcelConfig,
) -> None:
    invalid = parcels.copy()
    invalid.loc[0, "parcel_id"] = "313950000A9999"

    with pytest.raises(ParcelFilterError, match="must equal commune"):
        filter_parcels_by_area(invalid, area_config)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_area_filter_requires_exact_non_empty_parcel_ids`

**Purpose:** Regression invariant: area filter requires exact non empty parcel ids. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_area_filter_requires_exact_non_empty_parcel_ids(
    parcels: gpd.GeoDataFrame,
    area_config: ParcelConfig,
    parcel_id: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("parcel_id", [1, "", " parcel", "parcel "])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `area_config` | positional-or-keyword | `ParcelConfig` | `required` |
| `parcel_id` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ParcelFilterError, match="exact non-empty strings")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `parcels.copy` | `tests.unit.test_filter_parcels.parcels.copy` |
| `invalid["parcel_id"].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `filter_parcels_by_area` | `landscout.stages.filter_parcels.filter_parcels_by_area` |
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
| In-memory mutation | `invalid["parcel_id"] = invalid["parcel_id"].astype(object)`<br>`invalid.loc[0, "parcel_id"] = parcel_id` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_area_filter_rejects_plain_dataframe`

**Purpose:** Regression invariant: area filter rejects plain dataframe. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_area_filter_rejects_plain_dataframe(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `area_config` | positional-or-keyword | `ParcelConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ParcelFilterError, match="GeoDataFrame")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pd.DataFrame` | `pandas.DataFrame` |
| `pytest.raises` | `pytest.raises` |
| `filter_parcels_by_area` | `landscout.stages.filter_parcels.filter_parcels_by_area` |

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
def test_area_filter_rejects_plain_dataframe(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
    plain = pd.DataFrame(parcels)

    with pytest.raises(ParcelFilterError, match="GeoDataFrame"):
        filter_parcels_by_area(plain, area_config)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_area_filter_rejects_duplicate_columns`

**Purpose:** Regression invariant: area filter rejects duplicate columns. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_area_filter_rejects_duplicate_columns(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `area_config` | positional-or-keyword | `ParcelConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ParcelFilterError, match="columns.*unique")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `pd.concat` | `pandas.concat` |
| `pytest.raises` | `pytest.raises` |
| `filter_parcels_by_area` | `landscout.stages.filter_parcels.filter_parcels_by_area` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_area_filter_rejects_malformed_spatial_envelope`

**Purpose:** Regression invariant: area filter rejects malformed spatial envelope. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_area_filter_rejects_malformed_spatial_envelope(
    parcels: gpd.GeoDataFrame,
    area_config: ParcelConfig,
    mode: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("mode", ["missing_geometry", "missing_crs", "unreadable_crs"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `area_config` | positional-or-keyword | `ParcelConfig` | `required` |
| `mode` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ParcelFilterError, match="geometry\|CRS")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `parcels.copy` | `tests.unit.test_filter_parcels.parcels.copy` |
| `invalid.drop` | `unresolved local/third-party receiver; no ownership inferred` |
| `invalid.set_crs` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `filter_parcels_by_area` | `landscout.stages.filter_parcels.filter_parcels_by_area` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `invalid.set_crs` |
| External process/environment | None directly present. |
| In-memory mutation | `invalid.drop(columns="geometry")`<br>`invalid.set_crs(None, allow_override=True)`<br>`invalid.geometry.array._crs = "not-a-crs"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_area_filter_rejects_noncanonical_geometry_status`

**Purpose:** Regression invariant: area filter rejects noncanonical geometry status. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_area_filter_rejects_noncanonical_geometry_status(
    parcels: gpd.GeoDataFrame,
    area_config: ParcelConfig,
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
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `area_config` | positional-or-keyword | `ParcelConfig` | `required` |
| `geometry_status` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ParcelFilterError, match="geometry_status")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `parcels.copy` | `tests.unit.test_filter_parcels.parcels.copy` |
| `invalid["geometry_status"].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `filter_parcels_by_area` | `landscout.stages.filter_parcels.filter_parcels_by_area` |
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.


## 7. Test-specific regression contract

- Test functions: **20**.
- Pytest fixtures (decorator-proven): **2**.

### Fixtures

- `area_config` — decorators: `pytest.fixture`.
- `parcels` — decorators: `pytest.fixture`.

### Per-test regression index

| Test | Parametrization | Expected exception contexts | Assertion count | Exact regression purpose |
|---|---|---|---:|---|
| `test_minimum_boundary_is_included` | none | none | 1 | Proves minimum boundary is included using the exact source reproduced in section 7. |
| `test_maximum_boundary_is_included` | none | none | 1 | Proves maximum boundary is included using the exact source reproduced in section 7. |
| `test_rejected_parcel_has_expected_reason` | pytest.mark.parametrize(<br>    ("parcel_id", "expected_reason"),<br>    [<br>        ("below-minimum", "AREA_BELOW_MIN"),<br>        ("above-maximum", "AREA_ABOVE_MAX"),<br>        ("invalid-geometry", "INVALID_GEOMETRY"),<br>        ("unknown-area", "INVALID_GEOMETRY"),<br>    ],<br>) | none | 1 | Proves rejected parcel has expected reason using the exact source reproduced in section 7. |
| `test_no_parcel_disappears` | none | none | 4 | Proves no parcel disappears using the exact source reproduced in section 7. |
| `test_thresholds_come_from_config` | none | none | 1 | Proves thresholds come from config using the exact source reproduced in section 7. |
| `test_area_filter_revalidates_mutated_config_before_frame_work` | none | pytest.raises(ParcelFilterError, match="config") | 0 | Proves area filter revalidates mutated config before frame work using the exact source reproduced in section 7. |
| `test_missing_parcel_id_fails` | none | pytest.raises(ParcelFilterError, match="parcel_id") | 0 | Proves missing parcel id fails using the exact source reproduced in section 7. |
| `test_null_parcel_id_fails` | none | pytest.raises(ParcelFilterError, match="null") | 0 | Proves null parcel id fails using the exact source reproduced in section 7. |
| `test_duplicate_parcel_id_fails` | none | pytest.raises(ParcelFilterError, match="unique") | 0 | Proves duplicate parcel id fails using the exact source reproduced in section 7. |
| `test_candidate_and_rejected_ids_do_not_overlap` | none | none | 1 | Proves candidate and rejected ids do not overlap using the exact source reproduced in section 7. |
| `test_exact_parcel_ids_are_preserved` | none | none | 2 | Proves exact parcel ids are preserved using the exact source reproduced in section 7. |
| `test_valid_geometry_requires_strict_positive_finite_area` | pytest.mark.parametrize("area", [-1, 0, float("inf"), float("nan"), "5000", True]) | pytest.raises(ParcelFilterError, match="strict positive finite numeric") | 0 | Proves valid geometry requires strict positive finite area using the exact source reproduced in section 7. |
| `test_valid_geometry_with_forged_positive_area_is_rejected` | none | pytest.raises(ParcelFilterError, match="measured EPSG:2154") | 0 | Proves valid geometry with forged positive area is rejected using the exact source reproduced in section 7. |
| `test_invalid_geometry_with_recorded_area_is_rejected` | none | pytest.raises(ParcelFilterError, match="INVALID.*area_m2.*null") | 0 | Proves invalid geometry with recorded area is rejected using the exact source reproduced in section 7. |
| `test_parcel_id_must_match_its_canonical_source_identity_fields` | none | pytest.raises(ParcelFilterError, match="must equal commune") | 0 | Proves parcel id must match its canonical source identity fields using the exact source reproduced in section 7. |
| `test_area_filter_requires_exact_non_empty_parcel_ids` | pytest.mark.parametrize("parcel_id", [1, "", " parcel", "parcel "]) | pytest.raises(ParcelFilterError, match="exact non-empty strings") | 0 | Proves area filter requires exact non empty parcel ids using the exact source reproduced in section 7. |
| `test_area_filter_rejects_plain_dataframe` | none | pytest.raises(ParcelFilterError, match="GeoDataFrame") | 0 | Proves area filter rejects plain dataframe using the exact source reproduced in section 7. |
| `test_area_filter_rejects_duplicate_columns` | none | pytest.raises(ParcelFilterError, match="columns.*unique") | 0 | Proves area filter rejects duplicate columns using the exact source reproduced in section 7. |
| `test_area_filter_rejects_malformed_spatial_envelope` | pytest.mark.parametrize("mode", ["missing_geometry", "missing_crs", "unreadable_crs"]) | pytest.raises(ParcelFilterError, match="geometry\|CRS") | 0 | Proves area filter rejects malformed spatial envelope using the exact source reproduced in section 7. |
| `test_area_filter_rejects_noncanonical_geometry_status` | pytest.mark.parametrize(<br>    "geometry_status",<br>    [None, "UNKNOWN", "ERROR", "BANANA", "valid", 0, 1, True, False],<br>) | pytest.raises(ParcelFilterError, match="geometry_status") | 0 | Proves area filter rejects noncanonical geometry status using the exact source reproduced in section 7. |

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

from landscout.config import ParcelConfig
from landscout.stages.filter_parcels import ParcelFilterError, filter_parcels_by_area

PARCEL_IDS = {
    name: f"313950000A{index:04d}"
    for index, name in enumerate(
        (
            "at-minimum",
            "at-maximum",
            "below-minimum",
            "above-maximum",
            "invalid-geometry",
            "unknown-area",
        ),
        start=1,
    )
}


@pytest.fixture
def area_config() -> ParcelConfig:
    return ParcelConfig(min_area_m2=2000, max_area_m2=15000)


@pytest.fixture
def parcels() -> gpd.GeoDataFrame:
    areas = [2000.0, 15000.0, 1999.0, 15001.0]
    projected = gpd.GeoSeries(
        [
            Polygon(
                [
                    (600000 + index * 1000, 6200000),
                    (600000 + index * 1000 + sqrt(area), 6200000),
                    (600000 + index * 1000 + sqrt(area), 6200000 + sqrt(area)),
                    (600000 + index * 1000, 6200000 + sqrt(area)),
                ]
            )
            for index, area in enumerate(areas)
        ],
        crs="EPSG:2154",
    ).to_crs("EPSG:4326")
    geometries = [*projected.tolist(), None, Polygon()]
    return gpd.GeoDataFrame(
        {
            "parcel_id": list(PARCEL_IDS.values()),
            "commune_code": ["31395"] * 6,
            "section_prefix": ["000"] * 6,
            "section": ["A"] * 6,
            "parcel_number": [str(index) for index in range(1, 7)],
            "source_contenance": [None] * 6,
            "source_arpente": [None] * 6,
            "source_created_at": [None] * 6,
            "source_updated_at": [None] * 6,
            "geometry_status": [
                "VALID",
                "VALID",
                "VALID",
                "VALID",
                "INVALID",
                "INVALID",
            ],
            "area_m2": [*areas, None, None],
        },
        geometry=geometries,
        crs="EPSG:4326",
    )


def test_minimum_boundary_is_included(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
    candidates, _ = filter_parcels_by_area(parcels, area_config)

    assert PARCEL_IDS["at-minimum"] in set(candidates["parcel_id"])


def test_maximum_boundary_is_included(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
    candidates, _ = filter_parcels_by_area(parcels, area_config)

    assert PARCEL_IDS["at-maximum"] in set(candidates["parcel_id"])


@pytest.mark.parametrize(
    ("parcel_id", "expected_reason"),
    [
        ("below-minimum", "AREA_BELOW_MIN"),
        ("above-maximum", "AREA_ABOVE_MAX"),
        ("invalid-geometry", "INVALID_GEOMETRY"),
        ("unknown-area", "INVALID_GEOMETRY"),
    ],
)
def test_rejected_parcel_has_expected_reason(
    parcels: gpd.GeoDataFrame,
    area_config: ParcelConfig,
    parcel_id: str,
    expected_reason: str,
) -> None:
    _, rejected = filter_parcels_by_area(parcels, area_config)

    row = rejected.loc[rejected["parcel_id"] == PARCEL_IDS[parcel_id]].iloc[0]
    assert row["rejection_reason"] == expected_reason


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


def test_thresholds_come_from_config(parcels: gpd.GeoDataFrame) -> None:
    custom_config = ParcelConfig(min_area_m2=1999, max_area_m2=2000)

    candidates, _ = filter_parcels_by_area(parcels, custom_config)

    assert set(candidates["parcel_id"]) == {
        PARCEL_IDS["below-minimum"],
        PARCEL_IDS["at-minimum"],
    }


def test_area_filter_revalidates_mutated_config_before_frame_work(
    parcels: gpd.GeoDataFrame,
    area_config: ParcelConfig,
) -> None:
    tampered = area_config.model_copy(update={"min_area_m2": -1.0})
    colliding = parcels.assign(rejection_reason="existing")

    with pytest.raises(ParcelFilterError, match="config"):
        filter_parcels_by_area(colliding, tampered)


def test_missing_parcel_id_fails(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
    without_id = parcels.drop(columns=["parcel_id"])

    with pytest.raises(ParcelFilterError, match="parcel_id"):
        filter_parcels_by_area(without_id, area_config)


def test_null_parcel_id_fails(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
    with_null = parcels.copy()
    with_null.loc[0, "parcel_id"] = None

    with pytest.raises(ParcelFilterError, match="null"):
        filter_parcels_by_area(with_null, area_config)


def test_duplicate_parcel_id_fails(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
    with_duplicate = parcels.copy()
    with_duplicate.loc[1, "parcel_id"] = with_duplicate.loc[0, "parcel_id"]

    with pytest.raises(ParcelFilterError, match="unique"):
        filter_parcels_by_area(with_duplicate, area_config)


def test_candidate_and_rejected_ids_do_not_overlap(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
    candidates, rejected = filter_parcels_by_area(parcels, area_config)

    assert set(candidates["parcel_id"]).isdisjoint(set(rejected["parcel_id"]))


def test_exact_parcel_ids_are_preserved(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
    candidates, rejected = filter_parcels_by_area(parcels, area_config)

    output_ids = list(candidates["parcel_id"]) + list(rejected["parcel_id"])
    assert len(output_ids) == len(set(output_ids))
    assert set(output_ids) == set(parcels["parcel_id"])


@pytest.mark.parametrize("area", [-1, 0, float("inf"), float("nan"), "5000", True])
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


def test_valid_geometry_with_forged_positive_area_is_rejected(
    parcels: gpd.GeoDataFrame,
    area_config: ParcelConfig,
) -> None:
    invalid = parcels.copy()
    invalid.loc[0, "area_m2"] = float(invalid.loc[0, "area_m2"]) + 1.0

    with pytest.raises(ParcelFilterError, match="measured EPSG:2154"):
        filter_parcels_by_area(invalid, area_config)


def test_invalid_geometry_with_recorded_area_is_rejected(
    parcels: gpd.GeoDataFrame,
    area_config: ParcelConfig,
) -> None:
    invalid = parcels.copy()
    invalid.loc[4, "area_m2"] = 100.0

    with pytest.raises(ParcelFilterError, match="INVALID.*area_m2.*null"):
        filter_parcels_by_area(invalid, area_config)


def test_parcel_id_must_match_its_canonical_source_identity_fields(
    parcels: gpd.GeoDataFrame,
    area_config: ParcelConfig,
) -> None:
    invalid = parcels.copy()
    invalid.loc[0, "parcel_id"] = "313950000A9999"

    with pytest.raises(ParcelFilterError, match="must equal commune"):
        filter_parcels_by_area(invalid, area_config)


@pytest.mark.parametrize("parcel_id", [1, "", " parcel", "parcel "])
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


def test_area_filter_rejects_plain_dataframe(
    parcels: gpd.GeoDataFrame, area_config: ParcelConfig
) -> None:
    plain = pd.DataFrame(parcels)

    with pytest.raises(ParcelFilterError, match="GeoDataFrame"):
        filter_parcels_by_area(plain, area_config)  # type: ignore[arg-type]


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


@pytest.mark.parametrize("mode", ["missing_geometry", "missing_crs", "unreadable_crs"])
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


@pytest.mark.parametrize(
    "geometry_status",
    [None, "UNKNOWN", "ERROR", "BANANA", "valid", 0, 1, True, False],
)
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

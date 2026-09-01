# `tests/unit/test_normalize_cadastre.py`

## File identity

- Repository path: `tests/unit/test_normalize_cadastre.py`
- File type: Python source
- Layer: unit/regression test
- Domain: isolated contract test evidence
- Responsibility: Provides complete unit and regression coverage for the `normalize_cadastre` contracts exercised in this file.
- Source SHA256: `db89effb40b328e03a5101d60378cceef8c6e368e93e85870eaecab4e5e3868e`

## 1. STEP 7F.1A.4 contract delta

- Refreshes permanent STEP 7F.1A.4 regression coverage for normalize cadastre; the exact fixtures, mutations, calls, controlled failures, and assertions are inventoried below.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Provides complete unit and regression coverage for the `normalize_cadastre` contracts exercised in this file.

The file belongs to the **unit/regression test** layer and **isolated contract test evidence** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from copy import deepcopy`
- `from pathlib import Path`

### Third-party packages

- `import geopandas as gpd`
- `import pandas as pd`
- `import pytest`
- `from geopandas.testing import assert_geodataframe_equal`
- `from shapely.geometry import LineString, MultiPolygon, Point, Polygon`

### Internal LandScout imports

- `from landscout.sources.cadastre_fr import CadastreDownload`
- `from landscout.sources.cadastre_loader_fr import CadastreParcelSource`
- `from landscout.stages.normalize_cadastre import (
    CadastreNormalizationError,
    normalize_cadastre_parcels,
)`

## 4. Contract taxonomy

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

No module-level constant, alias, schema, mapping, or meaningful dunder assignment is declared.

### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

No top-level class/model/dataclass is declared.

## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `_physical_revalidation_stub`

**Purpose:** Implements `physical revalidation stub` within the file role: Provides complete unit and regression coverage for the `normalize_cadastre` contracts exercised in this file.

**Exact signature**

```python
def _physical_revalidation_stub(monkeypatch: pytest.MonkeyPatch) -> None:
```

- Exact decorators: `pytest.fixture(autouse=True)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.fixture` | `pytest.fixture` |

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
def _physical_revalidation_stub(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        "landscout.stages.normalize_cadastre.revalidate_cadastre_parcel_source",
        lambda source: source.parcels.copy(deep=True),
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_bound_source`

**Purpose:** Implements `bound source` within the file role: Provides complete unit and regression coverage for the `normalize_cadastre` contracts exercised in this file.

**Exact signature**

```python
def _bound_source(parcels: object) -> CadastreParcelSource:
```

- Exact decorators: none.
- Declared return annotation: `CadastreParcelSource`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `CadastreParcelSource(<br>        download=download,<br>        parcels=parcels,  # type: ignore[arg-type]<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_normalize_cadastre::_normalize` via `_bound_source`
- value/type reference: `tests.unit.test_normalize_cadastre::_normalize` via `_bound_source`
- direct call: `tests.unit.test_normalize_cadastre::test_normalization_uses_the_fresh_revalidated_frame` via `_bound_source`
- value/type reference: `tests.unit.test_normalize_cadastre::test_normalization_uses_the_fresh_revalidated_frame` via `_bound_source`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `CadastreDownload` | `landscout.sources.cadastre_fr.CadastreDownload` |
| `Path` | `pathlib.Path` |
| `CadastreParcelSource` | `landscout.sources.cadastre_loader_fr.CadastreParcelSource` |

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
def _bound_source(parcels: object) -> CadastreParcelSource:
    commune = "31395"
    if isinstance(parcels, gpd.GeoDataFrame) and "commune" in parcels.columns:
        first = parcels["commune"].iloc[0]
        if isinstance(first, str):
            commune = first
    download = CadastreDownload(
        commune_code=commune,
        source_url="https://cadastre.data.gouv.fr/unused",
        download_timestamp="2026-08-16T10:00:00+00:00",
        filename="unused.json.gz",
        file_size=1,
        sha256="0" * 64,
        path=Path("unused.json.gz"),
        cache_hit=True,
    )
    return CadastreParcelSource(
        download=download,
        parcels=parcels,  # type: ignore[arg-type]
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_normalize`

**Purpose:** Implements `normalize` within the file role: Provides complete unit and regression coverage for the `normalize_cadastre` contracts exercised in this file.

**Exact signature**

```python
def _normalize(parcels: object) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `normalize_cadastre_parcels(_bound_source(parcels))`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_normalize_cadastre::test_field_normalization` via `_normalize`
- value/type reference: `tests.unit.test_normalize_cadastre::test_field_normalization` via `_normalize`
- direct call: `tests.unit.test_normalize_cadastre::test_lambert93_area_calculation` via `_normalize`
- value/type reference: `tests.unit.test_normalize_cadastre::test_lambert93_area_calculation` via `_normalize`
- direct call: `tests.unit.test_normalize_cadastre::test_output_geometry_stays_in_wgs84` via `_normalize`
- value/type reference: `tests.unit.test_normalize_cadastre::test_output_geometry_stays_in_wgs84` via `_normalize`
- direct call: `tests.unit.test_normalize_cadastre::test_invalid_geometry_is_preserved_with_null_area` via `_normalize`
- value/type reference: `tests.unit.test_normalize_cadastre::test_invalid_geometry_is_preserved_with_null_area` via `_normalize`
- direct call: `tests.unit.test_normalize_cadastre::test_missing_crs_fails` via `_normalize`
- value/type reference: `tests.unit.test_normalize_cadastre::test_missing_crs_fails` via `_normalize`
- direct call: `tests.unit.test_normalize_cadastre::test_duplicate_parcel_id_fails` via `_normalize`
- value/type reference: `tests.unit.test_normalize_cadastre::test_duplicate_parcel_id_fails` via `_normalize`
- direct call: `tests.unit.test_normalize_cadastre::test_non_geodataframe_is_rejected_safely` via `_normalize`
- value/type reference: `tests.unit.test_normalize_cadastre::test_non_geodataframe_is_rejected_safely` via `_normalize`
- direct call: `tests.unit.test_normalize_cadastre::test_duplicate_columns_are_rejected` via `_normalize`
- value/type reference: `tests.unit.test_normalize_cadastre::test_duplicate_columns_are_rejected` via `_normalize`
- direct call: `tests.unit.test_normalize_cadastre::test_normalized_target_column_collision_is_rejected` via `_normalize`
- value/type reference: `tests.unit.test_normalize_cadastre::test_normalized_target_column_collision_is_rejected` via `_normalize`
- direct call: `tests.unit.test_normalize_cadastre::test_projected_source_crs_is_rejected` via `_normalize`
- value/type reference: `tests.unit.test_normalize_cadastre::test_projected_source_crs_is_rejected` via `_normalize`
- direct call: `tests.unit.test_normalize_cadastre::test_parcel_id_must_be_an_exact_nonempty_string` via `_normalize`
- value/type reference: `tests.unit.test_normalize_cadastre::test_parcel_id_must_be_an_exact_nonempty_string` via `_normalize`
- direct call: `tests.unit.test_normalize_cadastre::test_non_polygonal_geometry_is_rejected` via `_normalize`
- value/type reference: `tests.unit.test_normalize_cadastre::test_non_polygonal_geometry_is_rejected` via `_normalize`
- direct call: `tests.unit.test_normalize_cadastre::test_valid_multipolygon_is_accepted` via `_normalize`
- value/type reference: `tests.unit.test_normalize_cadastre::test_valid_multipolygon_is_accepted` via `_normalize`
- direct call: `tests.unit.test_normalize_cadastre::test_null_and_empty_geometry_are_preserved_as_invalid` via `_normalize`
- value/type reference: `tests.unit.test_normalize_cadastre::test_null_and_empty_geometry_are_preserved_as_invalid` via `_normalize`
- direct call: `tests.unit.test_normalize_cadastre::test_normalization_does_not_mutate_input` via `_normalize`
- value/type reference: `tests.unit.test_normalize_cadastre::test_normalization_does_not_mutate_input` via `_normalize`
- direct call: `tests.unit.test_normalize_cadastre::test_every_cadastral_identity_field_requires_an_exact_nonempty_string` via `_normalize`
- value/type reference: `tests.unit.test_normalize_cadastre::test_every_cadastral_identity_field_requires_an_exact_nonempty_string` via `_normalize`
- direct call: `tests.unit.test_normalize_cadastre::test_commune_requires_canonical_french_insee_identity` via `_normalize`
- value/type reference: `tests.unit.test_normalize_cadastre::test_commune_requires_canonical_french_insee_identity` via `_normalize`
- direct call: `tests.unit.test_normalize_cadastre::test_commune_accepts_canonical_french_insee_identity` via `_normalize`
- value/type reference: `tests.unit.test_normalize_cadastre::test_commune_accepts_canonical_french_insee_identity` via `_normalize`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `normalize_cadastre_parcels` | `landscout.stages.normalize_cadastre.normalize_cadastre_parcels` |
| `_bound_source` | `tests.unit.test_normalize_cadastre._bound_source` |

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
def _normalize(parcels: object) -> gpd.GeoDataFrame:
    return normalize_cadastre_parcels(_bound_source(parcels))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_source_parcels`

**Purpose:** Implements `source parcels` within the file role: Provides complete unit and regression coverage for the `normalize_cadastre` contracts exercised in this file.

**Exact signature**

```python
def _source_parcels(
    geometries: list[object],
    ids: list[object] | None = None,
    crs: str | None = "EPSG:4326",
) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `geometries` | positional-or-keyword | `list[object]` | `required` |
| `ids` | positional-or-keyword | `list[object] \| None` | `None` |
| `crs` | positional-or-keyword | `str \| None` | `'EPSG:4326'` |

**Return and exception contract**

- Exact observed return expressions:
  - `gpd.GeoDataFrame(<br>        {<br>            "id": parcel_ids,<br>            "commune": ["31395"] * count,<br>            "prefixe": ["000"] * count,<br>            "section": ["A"] * count,<br>            "numero": [str(index + 1) for index in range(count)],<br>            "contenance": [1000.0] * count,<br>            "arpente": [False] * count,<br>            "created": ["2020-01-01"] * count,<br>            "updated": ["2024-01-01"] * count,<br>        },<br>        geometry=geometries,<br>        crs=crs,<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_normalize_cadastre::test_field_normalization` via `_source_parcels`
- value/type reference: `tests.unit.test_normalize_cadastre::test_field_normalization` via `_source_parcels`
- direct call: `tests.unit.test_normalize_cadastre::test_lambert93_area_calculation` via `_source_parcels`
- value/type reference: `tests.unit.test_normalize_cadastre::test_lambert93_area_calculation` via `_source_parcels`
- direct call: `tests.unit.test_normalize_cadastre::test_output_geometry_stays_in_wgs84` via `_source_parcels`
- value/type reference: `tests.unit.test_normalize_cadastre::test_output_geometry_stays_in_wgs84` via `_source_parcels`
- direct call: `tests.unit.test_normalize_cadastre::test_invalid_geometry_is_preserved_with_null_area` via `_source_parcels`
- value/type reference: `tests.unit.test_normalize_cadastre::test_invalid_geometry_is_preserved_with_null_area` via `_source_parcels`
- direct call: `tests.unit.test_normalize_cadastre::test_missing_crs_fails` via `_source_parcels`
- value/type reference: `tests.unit.test_normalize_cadastre::test_missing_crs_fails` via `_source_parcels`
- direct call: `tests.unit.test_normalize_cadastre::test_duplicate_parcel_id_fails` via `_source_parcels`
- value/type reference: `tests.unit.test_normalize_cadastre::test_duplicate_parcel_id_fails` via `_source_parcels`
- direct call: `tests.unit.test_normalize_cadastre::test_duplicate_columns_are_rejected` via `_source_parcels`
- value/type reference: `tests.unit.test_normalize_cadastre::test_duplicate_columns_are_rejected` via `_source_parcels`
- direct call: `tests.unit.test_normalize_cadastre::test_normalized_target_column_collision_is_rejected` via `_source_parcels`
- value/type reference: `tests.unit.test_normalize_cadastre::test_normalized_target_column_collision_is_rejected` via `_source_parcels`
- direct call: `tests.unit.test_normalize_cadastre::test_projected_source_crs_is_rejected` via `_source_parcels`
- value/type reference: `tests.unit.test_normalize_cadastre::test_projected_source_crs_is_rejected` via `_source_parcels`
- direct call: `tests.unit.test_normalize_cadastre::test_parcel_id_must_be_an_exact_nonempty_string` via `_source_parcels`
- value/type reference: `tests.unit.test_normalize_cadastre::test_parcel_id_must_be_an_exact_nonempty_string` via `_source_parcels`
- direct call: `tests.unit.test_normalize_cadastre::test_non_polygonal_geometry_is_rejected` via `_source_parcels`
- value/type reference: `tests.unit.test_normalize_cadastre::test_non_polygonal_geometry_is_rejected` via `_source_parcels`
- direct call: `tests.unit.test_normalize_cadastre::test_valid_multipolygon_is_accepted` via `_source_parcels`
- value/type reference: `tests.unit.test_normalize_cadastre::test_valid_multipolygon_is_accepted` via `_source_parcels`
- direct call: `tests.unit.test_normalize_cadastre::test_null_and_empty_geometry_are_preserved_as_invalid` via `_source_parcels`
- value/type reference: `tests.unit.test_normalize_cadastre::test_null_and_empty_geometry_are_preserved_as_invalid` via `_source_parcels`
- direct call: `tests.unit.test_normalize_cadastre::test_normalization_does_not_mutate_input` via `_source_parcels`
- value/type reference: `tests.unit.test_normalize_cadastre::test_normalization_does_not_mutate_input` via `_source_parcels`
- direct call: `tests.unit.test_normalize_cadastre::test_normalization_uses_the_fresh_revalidated_frame` via `_source_parcels`
- value/type reference: `tests.unit.test_normalize_cadastre::test_normalization_uses_the_fresh_revalidated_frame` via `_source_parcels`
- direct call: `tests.unit.test_normalize_cadastre::test_every_cadastral_identity_field_requires_an_exact_nonempty_string` via `_source_parcels`
- value/type reference: `tests.unit.test_normalize_cadastre::test_every_cadastral_identity_field_requires_an_exact_nonempty_string` via `_source_parcels`
- direct call: `tests.unit.test_normalize_cadastre::test_commune_requires_canonical_french_insee_identity` via `_source_parcels`
- value/type reference: `tests.unit.test_normalize_cadastre::test_commune_requires_canonical_french_insee_identity` via `_source_parcels`
- direct call: `tests.unit.test_normalize_cadastre::test_commune_accepts_canonical_french_insee_identity` via `_source_parcels`
- value/type reference: `tests.unit.test_normalize_cadastre::test_commune_accepts_canonical_french_insee_identity` via `_source_parcels`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `range` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
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
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _source_parcels(
    geometries: list[object],
    ids: list[object] | None = None,
    crs: str | None = "EPSG:4326",
) -> gpd.GeoDataFrame:
    parcel_ids = ids or [
        f"313950000A{index + 1:04d}" for index in range(len(geometries))
    ]
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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `valid_polygon`

**Purpose:** Implements `valid polygon` within the file role: Provides complete unit and regression coverage for the `normalize_cadastre` contracts exercised in this file.

**Exact signature**

```python
def valid_polygon() -> Polygon:
```

- Exact decorators: `pytest.fixture`.
- Declared return annotation: `Polygon`.

**Inputs**

- No parameters.

**Return and exception contract**

- Exact observed return expressions:
  - `Polygon([(2.35, 43.45), (2.36, 43.45), (2.36, 43.46), (2.35, 43.45)])`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- value/type reference: `tests.unit.test_normalize_cadastre::test_field_normalization` via `valid_polygon`
- value/type reference: `tests.unit.test_normalize_cadastre::test_lambert93_area_calculation` via `valid_polygon`
- value/type reference: `tests.unit.test_normalize_cadastre::test_output_geometry_stays_in_wgs84` via `valid_polygon`
- value/type reference: `tests.unit.test_normalize_cadastre::test_missing_crs_fails` via `valid_polygon`
- value/type reference: `tests.unit.test_normalize_cadastre::test_duplicate_parcel_id_fails` via `valid_polygon`
- value/type reference: `tests.unit.test_normalize_cadastre::test_duplicate_columns_are_rejected` via `valid_polygon`
- value/type reference: `tests.unit.test_normalize_cadastre::test_normalized_target_column_collision_is_rejected` via `valid_polygon`
- value/type reference: `tests.unit.test_normalize_cadastre::test_projected_source_crs_is_rejected` via `valid_polygon`
- value/type reference: `tests.unit.test_normalize_cadastre::test_parcel_id_must_be_an_exact_nonempty_string` via `valid_polygon`
- value/type reference: `tests.unit.test_normalize_cadastre::test_valid_multipolygon_is_accepted` via `valid_polygon`
- value/type reference: `tests.unit.test_normalize_cadastre::test_normalization_does_not_mutate_input` via `valid_polygon`
- value/type reference: `tests.unit.test_normalize_cadastre::test_normalization_uses_the_fresh_revalidated_frame` via `valid_polygon`
- value/type reference: `tests.unit.test_normalize_cadastre::test_every_cadastral_identity_field_requires_an_exact_nonempty_string` via `valid_polygon`
- value/type reference: `tests.unit.test_normalize_cadastre::test_commune_requires_canonical_french_insee_identity` via `valid_polygon`
- value/type reference: `tests.unit.test_normalize_cadastre::test_commune_accepts_canonical_french_insee_identity` via `valid_polygon`

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
def valid_polygon() -> Polygon:
    return Polygon([(2.35, 43.45), (2.36, 43.45), (2.36, 43.46), (2.35, 43.45)])
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_field_normalization`

**Purpose:** Regression invariant: field normalization. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_field_normalization(valid_polygon: Polygon) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `valid_polygon` | positional-or-keyword | `Polygon` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert list(normalized.columns) == [<br>        "parcel_id",<br>        "commune_code",<br>        "section_prefix",<br>        "section",<br>        "parcel_number",<br>        "source_contenance",<br>        "source_arpente",<br>        "source_created_at",<br>        "source_updated_at",<br>        "geometry_status",<br>        "area_m2",<br>        "geometry",<br>    ]`
  - `assert normalized.iloc[0]["parcel_id"] == "313950000A0001"`
  - `assert normalized.iloc[0]["commune_code"] == "31395"`
  - `assert normalized.iloc[0]["geometry_status"] == "VALID"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_normalize` | `tests.unit.test_normalize_cadastre._normalize` |
| `_source_parcels` | `tests.unit.test_normalize_cadastre._source_parcels` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_field_normalization(valid_polygon: Polygon) -> None:
    normalized = _normalize(_source_parcels([valid_polygon]))

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
    assert normalized.iloc[0]["parcel_id"] == "313950000A0001"
    assert normalized.iloc[0]["commune_code"] == "31395"
    assert normalized.iloc[0]["geometry_status"] == "VALID"
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_lambert93_area_calculation`

**Purpose:** Regression invariant: lambert93 area calculation. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_lambert93_area_calculation(valid_polygon: Polygon) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `valid_polygon` | positional-or-keyword | `Polygon` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert normalized.iloc[0]["area_m2"] == pytest.approx(expected_area)`
  - `assert normalized.iloc[0]["area_m2"] > 0`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_parcels` | `tests.unit.test_normalize_cadastre._source_parcels` |
| `source.to_crs` | `unresolved local/third-party receiver; no ownership inferred` |
| `_normalize` | `tests.unit.test_normalize_cadastre._normalize` |
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
def test_lambert93_area_calculation(valid_polygon: Polygon) -> None:
    source = _source_parcels([valid_polygon])
    expected_area = source.to_crs("EPSG:2154").geometry.area.iloc[0]

    normalized = _normalize(source)

    assert normalized.iloc[0]["area_m2"] == pytest.approx(expected_area)
    assert normalized.iloc[0]["area_m2"] > 0
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_output_geometry_stays_in_wgs84`

**Purpose:** Regression invariant: output geometry stays in wgs84. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_output_geometry_stays_in_wgs84(valid_polygon: Polygon) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `valid_polygon` | positional-or-keyword | `Polygon` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert normalized.crs is not None`
  - `assert normalized.crs.to_epsg() == 4326`
  - `assert normalized.geometry.iloc[0].equals_exact(valid_polygon, tolerance=0)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_parcels` | `tests.unit.test_normalize_cadastre._source_parcels` |
| `_normalize` | `tests.unit.test_normalize_cadastre._normalize` |
| `normalized.crs.to_epsg` | `unresolved local/third-party receiver; no ownership inferred` |
| `normalized.geometry.iloc[0].equals_exact` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `normalized.geometry.iloc[0].equals_exact` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_output_geometry_stays_in_wgs84(valid_polygon: Polygon) -> None:
    source = _source_parcels([valid_polygon])

    normalized = _normalize(source)

    assert normalized.crs is not None
    assert normalized.crs.to_epsg() == 4326
    assert normalized.geometry.iloc[0].equals_exact(valid_polygon, tolerance=0)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_invalid_geometry_is_preserved_with_null_area`

**Purpose:** Regression invariant: invalid geometry is preserved with null area. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_invalid_geometry_is_preserved_with_null_area() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert not bow_tie.is_valid`
  - `assert normalized.iloc[0]["geometry_status"] == "INVALID"`
  - `assert normalized["area_m2"].isna().iloc[0]`
  - `assert normalized.geometry.iloc[0].equals_exact(bow_tie, tolerance=0)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `Polygon` | `shapely.geometry.Polygon` |
| `_normalize` | `tests.unit.test_normalize_cadastre._normalize` |
| `_source_parcels` | `tests.unit.test_normalize_cadastre._source_parcels` |
| `normalized["area_m2"].isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `normalized.geometry.iloc[0].equals_exact` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `normalized.geometry.iloc[0].equals_exact` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_invalid_geometry_is_preserved_with_null_area() -> None:
    bow_tie = Polygon([(2.35, 43.45), (2.36, 43.46), (2.35, 43.46), (2.36, 43.45)])
    assert not bow_tie.is_valid

    normalized = _normalize(_source_parcels([bow_tie]))

    assert normalized.iloc[0]["geometry_status"] == "INVALID"
    assert normalized["area_m2"].isna().iloc[0]
    assert normalized.geometry.iloc[0].equals_exact(bow_tie, tolerance=0)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_missing_crs_fails`

**Purpose:** Regression invariant: missing crs fails. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_missing_crs_fails(valid_polygon: Polygon) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `valid_polygon` | positional-or-keyword | `Polygon` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(CadastreNormalizationError, match="CRS")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_parcels` | `tests.unit.test_normalize_cadastre._source_parcels` |
| `pytest.raises` | `pytest.raises` |
| `_normalize` | `tests.unit.test_normalize_cadastre._normalize` |

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
def test_missing_crs_fails(valid_polygon: Polygon) -> None:
    source = _source_parcels([valid_polygon], crs=None)

    with pytest.raises(CadastreNormalizationError, match="CRS"):
        _normalize(source)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_duplicate_parcel_id_fails`

**Purpose:** Regression invariant: duplicate parcel id fails. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_duplicate_parcel_id_fails(valid_polygon: Polygon) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `valid_polygon` | positional-or-keyword | `Polygon` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(CadastreNormalizationError, match="unique")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_parcels` | `tests.unit.test_normalize_cadastre._source_parcels` |
| `pytest.raises` | `pytest.raises` |
| `_normalize` | `tests.unit.test_normalize_cadastre._normalize` |

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
def test_duplicate_parcel_id_fails(valid_polygon: Polygon) -> None:
    source = _source_parcels(
        [valid_polygon, valid_polygon], ids=["duplicate", "duplicate"]
    )

    with pytest.raises(CadastreNormalizationError, match="unique"):
        _normalize(source)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_non_geodataframe_is_rejected_safely`

**Purpose:** Regression invariant: non geodataframe is rejected safely. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_non_geodataframe_is_rejected_safely() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(CadastreNormalizationError, match="GeoDataFrame")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `_normalize` | `tests.unit.test_normalize_cadastre._normalize` |
| `pd.DataFrame` | `pandas.DataFrame` |

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
def test_non_geodataframe_is_rejected_safely() -> None:
    with pytest.raises(CadastreNormalizationError, match="GeoDataFrame"):
        _normalize(pd.DataFrame({"id": ["parcel"]}))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_duplicate_columns_are_rejected`

**Purpose:** Regression invariant: duplicate columns are rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_duplicate_columns_are_rejected(valid_polygon: Polygon) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `valid_polygon` | positional-or-keyword | `Polygon` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(CadastreNormalizationError, match="columns.*unique")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_parcels` | `tests.unit.test_normalize_cadastre._source_parcels` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `pd.concat` | `pandas.concat` |
| `pytest.raises` | `pytest.raises` |
| `_normalize` | `tests.unit.test_normalize_cadastre._normalize` |

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
def test_duplicate_columns_are_rejected(valid_polygon: Polygon) -> None:
    source = _source_parcels([valid_polygon])
    duplicate = gpd.GeoDataFrame(
        pd.concat([source, source[["id"]]], axis=1),
        geometry="geometry",
        crs=source.crs,
    )

    with pytest.raises(CadastreNormalizationError, match="columns.*unique"):
        _normalize(duplicate)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_normalized_target_column_collision_is_rejected`

**Purpose:** Regression invariant: normalized target column collision is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_normalized_target_column_collision_is_rejected(
    valid_polygon: Polygon,
    collision: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "collision",
    [
        "parcel_id",
        "commune_code",
        "section_prefix",
        "parcel_number",
        "geometry_status",
        "area_m2",
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `valid_polygon` | positional-or-keyword | `Polygon` | `required` |
| `collision` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(CadastreNormalizationError, match="collide")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_parcels` | `tests.unit.test_normalize_cadastre._source_parcels` |
| `pytest.raises` | `pytest.raises` |
| `_normalize` | `tests.unit.test_normalize_cadastre._normalize` |
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
| In-memory mutation | `source[collision] = "forged"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_normalized_target_column_collision_is_rejected(
    valid_polygon: Polygon,
    collision: str,
) -> None:
    source = _source_parcels([valid_polygon])
    source[collision] = "forged"

    with pytest.raises(CadastreNormalizationError, match="collide"):
        _normalize(source)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_projected_source_crs_is_rejected`

**Purpose:** Regression invariant: projected source crs is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_projected_source_crs_is_rejected(valid_polygon: Polygon) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `valid_polygon` | positional-or-keyword | `Polygon` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(CadastreNormalizationError, match="4326")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_parcels([valid_polygon]).to_crs` | `unresolved local/third-party receiver; no ownership inferred` |
| `_source_parcels` | `tests.unit.test_normalize_cadastre._source_parcels` |
| `pytest.raises` | `pytest.raises` |
| `_normalize` | `tests.unit.test_normalize_cadastre._normalize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `_source_parcels([valid_polygon]).to_crs` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_projected_source_crs_is_rejected(valid_polygon: Polygon) -> None:
    source = _source_parcels([valid_polygon]).to_crs("EPSG:2154")

    with pytest.raises(CadastreNormalizationError, match="4326"):
        _normalize(source)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_parcel_id_must_be_an_exact_nonempty_string`

**Purpose:** Regression invariant: parcel id must be an exact nonempty string. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_parcel_id_must_be_an_exact_nonempty_string(
    valid_polygon: Polygon,
    identifier: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("identifier", [1, "", " ", " parcel", "parcel "])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `valid_polygon` | positional-or-keyword | `Polygon` | `required` |
| `identifier` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(CadastreNormalizationError, match="parcel_id")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_parcels` | `tests.unit.test_normalize_cadastre._source_parcels` |
| `pytest.raises` | `pytest.raises` |
| `_normalize` | `tests.unit.test_normalize_cadastre._normalize` |
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
def test_parcel_id_must_be_an_exact_nonempty_string(
    valid_polygon: Polygon,
    identifier: object,
) -> None:
    source = _source_parcels([valid_polygon], ids=[identifier])

    with pytest.raises(CadastreNormalizationError, match="parcel_id"):
        _normalize(source)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_non_polygonal_geometry_is_rejected`

**Purpose:** Regression invariant: non polygonal geometry is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_non_polygonal_geometry_is_rejected(geometry: object) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "geometry",
    [Point(2.35, 43.45), LineString([(2.35, 43.45), (2.36, 43.46)])],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `geometry` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(CadastreNormalizationError, match="Polygon")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `_normalize` | `tests.unit.test_normalize_cadastre._normalize` |
| `_source_parcels` | `tests.unit.test_normalize_cadastre._source_parcels` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `Point` | `shapely.geometry.Point` |
| `LineString` | `shapely.geometry.LineString` |

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
def test_non_polygonal_geometry_is_rejected(geometry: object) -> None:
    with pytest.raises(CadastreNormalizationError, match="Polygon"):
        _normalize(_source_parcels([geometry]))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_valid_multipolygon_is_accepted`

**Purpose:** Regression invariant: valid multipolygon is accepted. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_valid_multipolygon_is_accepted(valid_polygon: Polygon) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `valid_polygon` | positional-or-keyword | `Polygon` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert normalized.loc[0, "geometry_status"] == "VALID"`
  - `assert normalized.loc[0, "area_m2"] > 0`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_normalize` | `tests.unit.test_normalize_cadastre._normalize` |
| `_source_parcels` | `tests.unit.test_normalize_cadastre._source_parcels` |
| `MultiPolygon` | `shapely.geometry.MultiPolygon` |

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
def test_valid_multipolygon_is_accepted(valid_polygon: Polygon) -> None:
    normalized = _normalize(_source_parcels([MultiPolygon([valid_polygon])]))

    assert normalized.loc[0, "geometry_status"] == "VALID"
    assert normalized.loc[0, "area_m2"] > 0
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_null_and_empty_geometry_are_preserved_as_invalid`

**Purpose:** Regression invariant: null and empty geometry are preserved as invalid. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_null_and_empty_geometry_are_preserved_as_invalid(geometry: object) -> None:
```

- Exact decorators: `pytest.mark.parametrize("geometry", [None, Polygon()])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `geometry` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert normalized.loc[0, "geometry_status"] == "INVALID"`
  - `assert pd.isna(normalized.loc[0, "area_m2"])`
  - `assert normalized.geometry.isna().iloc[0]`
  - `assert normalized.geometry.is_empty.iloc[0]`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_normalize` | `tests.unit.test_normalize_cadastre._normalize` |
| `_source_parcels` | `tests.unit.test_normalize_cadastre._source_parcels` |
| `pd.isna` | `pandas.isna` |
| `normalized.geometry.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `Polygon` | `shapely.geometry.Polygon` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `normalized.geometry.isna` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_null_and_empty_geometry_are_preserved_as_invalid(geometry: object) -> None:
    normalized = _normalize(_source_parcels([geometry]))

    assert normalized.loc[0, "geometry_status"] == "INVALID"
    assert pd.isna(normalized.loc[0, "area_m2"])
    if geometry is None:
        assert normalized.geometry.isna().iloc[0]
    else:
        assert normalized.geometry.is_empty.iloc[0]
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_normalization_does_not_mutate_input`

**Purpose:** Regression invariant: normalization does not mutate input. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_normalization_does_not_mutate_input(valid_polygon: Polygon) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `valid_polygon` | positional-or-keyword | `Polygon` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_parcels` | `tests.unit.test_normalize_cadastre._source_parcels` |
| `deepcopy` | `copy.deepcopy` |
| `_normalize` | `tests.unit.test_normalize_cadastre._normalize` |
| `assert_geodataframe_equal` | `geopandas.testing.assert_geodataframe_equal` |

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
def test_normalization_does_not_mutate_input(valid_polygon: Polygon) -> None:
    source = _source_parcels([valid_polygon])
    before = deepcopy(source)

    _normalize(source)

    assert_geodataframe_equal(source, before)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_normalization_uses_the_fresh_revalidated_frame`

**Purpose:** Regression invariant: normalization uses the fresh revalidated frame. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_normalization_uses_the_fresh_revalidated_frame(
    valid_polygon: Polygon,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `valid_polygon` | positional-or-keyword | `Polygon` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert normalized.loc[0, "parcel_id"] == "313950000A0001"`
  - `assert supplied.loc[0, "id"] == "FORGED-AFTER-COMPARISON"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_parcels` | `tests.unit.test_normalize_cadastre._source_parcels` |
| `supplied.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `_bound_source` | `tests.unit.test_normalize_cadastre._bound_source` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `normalize_cadastre_parcels` | `landscout.stages.normalize_cadastre.normalize_cadastre_parcels` |

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
def test_normalization_uses_the_fresh_revalidated_frame(
    valid_polygon: Polygon,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    supplied = _source_parcels([valid_polygon])
    fresh = supplied.copy(deep=True)
    source = _bound_source(supplied)

    def return_fresh_and_mutate_supplied(_: object) -> gpd.GeoDataFrame:
        supplied.loc[0, "id"] = "FORGED-AFTER-COMPARISON"
        return fresh

    monkeypatch.setattr(
        "landscout.stages.normalize_cadastre.revalidate_cadastre_parcel_source",
        return_fresh_and_mutate_supplied,
    )

    normalized = normalize_cadastre_parcels(source)

    assert normalized.loc[0, "parcel_id"] == "313950000A0001"
    assert supplied.loc[0, "id"] == "FORGED-AFTER-COMPARISON"
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_normalization_uses_the_fresh_revalidated_frame.return_fresh_and_mutate_supplied`

**Purpose:** Implements `return fresh and mutate supplied` within the file role: Provides complete unit and regression coverage for the `normalize_cadastre` contracts exercised in this file.

**Exact signature**

```python
def return_fresh_and_mutate_supplied(_: object) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `_` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `fresh`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
- No calls.

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
| In-memory mutation | `supplied.loc[0, "id"] = "FORGED-AFTER-COMPARISON"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def return_fresh_and_mutate_supplied(_: object) -> gpd.GeoDataFrame:
        supplied.loc[0, "id"] = "FORGED-AFTER-COMPARISON"
        return fresh
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_every_cadastral_identity_field_requires_an_exact_nonempty_string`

**Purpose:** Regression invariant: every cadastral identity field requires an exact nonempty string. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_every_cadastral_identity_field_requires_an_exact_nonempty_string(
    valid_polygon: Polygon,
    column: str,
    value: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("column", ["id", "commune", "prefixe", "section", "numero"])`, `pytest.mark.parametrize(
    "value",
    [None, 123, True, "", " leading", "trailing "],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `valid_polygon` | positional-or-keyword | `Polygon` | `required` |
| `column` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(CadastreNormalizationError, match=column)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_parcels` | `tests.unit.test_normalize_cadastre._source_parcels` |
| `source[column].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_normalize` | `tests.unit.test_normalize_cadastre._normalize` |
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
| In-memory mutation | `source[column] = source[column].astype(object)`<br>`source.loc[0, column] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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
        _normalize(source)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_commune_requires_canonical_french_insee_identity`

**Purpose:** Regression invariant: commune requires canonical french insee identity. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_commune_requires_canonical_french_insee_identity(
    valid_polygon: Polygon,
    commune: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("commune", ["3139", "2a004", "ABCDE", "971000"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `valid_polygon` | positional-or-keyword | `Polygon` | `required` |
| `commune` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(CadastreNormalizationError, match="commune")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_parcels` | `tests.unit.test_normalize_cadastre._source_parcels` |
| `pytest.raises` | `pytest.raises` |
| `_normalize` | `tests.unit.test_normalize_cadastre._normalize` |
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
| In-memory mutation | `source.loc[0, "commune"] = commune`<br>`source.loc[0, "id"] = f"{commune}0000A0001"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_commune_requires_canonical_french_insee_identity(
    valid_polygon: Polygon,
    commune: str,
) -> None:
    source = _source_parcels([valid_polygon])
    source.loc[0, "commune"] = commune
    source.loc[0, "id"] = f"{commune}0000A0001"

    with pytest.raises(CadastreNormalizationError, match="commune"):
        _normalize(source)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_commune_accepts_canonical_french_insee_identity`

**Purpose:** Regression invariant: commune accepts canonical french insee identity. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_commune_accepts_canonical_french_insee_identity(
    valid_polygon: Polygon,
    commune: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("commune", ["31395", "2A004", "2B033"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `valid_polygon` | positional-or-keyword | `Polygon` | `required` |
| `commune` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.loc[0, "commune_code"] == commune`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_parcels` | `tests.unit.test_normalize_cadastre._source_parcels` |
| `_normalize` | `tests.unit.test_normalize_cadastre._normalize` |
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
| In-memory mutation | `source.loc[0, "commune"] = commune`<br>`source.loc[0, "id"] = f"{commune}0000A0001"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_commune_accepts_canonical_french_insee_identity(
    valid_polygon: Polygon,
    commune: str,
) -> None:
    source = _source_parcels([valid_polygon])
    source.loc[0, "commune"] = commune
    source.loc[0, "id"] = f"{commune}0000A0001"

    result = _normalize(source)

    assert result.loc[0, "commune_code"] == commune
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.


## 7. Test-specific regression contract

- Test functions: **19**.
- Pytest fixtures (decorator-proven): **2**.

### Fixtures

- `_physical_revalidation_stub` — decorators: `pytest.fixture(autouse=True)`.
- `valid_polygon` — decorators: `pytest.fixture`.

### Per-test regression index

| Test | Parametrization | Expected exception contexts | Assertion count | Exact regression purpose |
|---|---|---|---:|---|
| `test_field_normalization` | none | none | 4 | Proves field normalization using the exact source reproduced in section 7. |
| `test_lambert93_area_calculation` | none | none | 2 | Proves lambert93 area calculation using the exact source reproduced in section 7. |
| `test_output_geometry_stays_in_wgs84` | none | none | 3 | Proves output geometry stays in wgs84 using the exact source reproduced in section 7. |
| `test_invalid_geometry_is_preserved_with_null_area` | none | none | 4 | Proves invalid geometry is preserved with null area using the exact source reproduced in section 7. |
| `test_missing_crs_fails` | none | pytest.raises(CadastreNormalizationError, match="CRS") | 0 | Proves missing crs fails using the exact source reproduced in section 7. |
| `test_duplicate_parcel_id_fails` | none | pytest.raises(CadastreNormalizationError, match="unique") | 0 | Proves duplicate parcel id fails using the exact source reproduced in section 7. |
| `test_non_geodataframe_is_rejected_safely` | none | pytest.raises(CadastreNormalizationError, match="GeoDataFrame") | 0 | Proves non geodataframe is rejected safely using the exact source reproduced in section 7. |
| `test_duplicate_columns_are_rejected` | none | pytest.raises(CadastreNormalizationError, match="columns.*unique") | 0 | Proves duplicate columns are rejected using the exact source reproduced in section 7. |
| `test_normalized_target_column_collision_is_rejected` | pytest.mark.parametrize(<br>    "collision",<br>    [<br>        "parcel_id",<br>        "commune_code",<br>        "section_prefix",<br>        "parcel_number",<br>        "geometry_status",<br>        "area_m2",<br>    ],<br>) | pytest.raises(CadastreNormalizationError, match="collide") | 0 | Proves normalized target column collision is rejected using the exact source reproduced in section 7. |
| `test_projected_source_crs_is_rejected` | none | pytest.raises(CadastreNormalizationError, match="4326") | 0 | Proves projected source crs is rejected using the exact source reproduced in section 7. |
| `test_parcel_id_must_be_an_exact_nonempty_string` | pytest.mark.parametrize("identifier", [1, "", " ", " parcel", "parcel "]) | pytest.raises(CadastreNormalizationError, match="parcel_id") | 0 | Proves parcel id must be an exact nonempty string using the exact source reproduced in section 7. |
| `test_non_polygonal_geometry_is_rejected` | pytest.mark.parametrize(<br>    "geometry",<br>    [Point(2.35, 43.45), LineString([(2.35, 43.45), (2.36, 43.46)])],<br>) | pytest.raises(CadastreNormalizationError, match="Polygon") | 0 | Proves non polygonal geometry is rejected using the exact source reproduced in section 7. |
| `test_valid_multipolygon_is_accepted` | none | none | 2 | Proves valid multipolygon is accepted using the exact source reproduced in section 7. |
| `test_null_and_empty_geometry_are_preserved_as_invalid` | pytest.mark.parametrize("geometry", [None, Polygon()]) | none | 4 | Proves null and empty geometry are preserved as invalid using the exact source reproduced in section 7. |
| `test_normalization_does_not_mutate_input` | none | none | 0 | Proves normalization does not mutate input using the exact source reproduced in section 7. |
| `test_normalization_uses_the_fresh_revalidated_frame` | none | none | 2 | Proves normalization uses the fresh revalidated frame using the exact source reproduced in section 7. |
| `test_every_cadastral_identity_field_requires_an_exact_nonempty_string` | pytest.mark.parametrize("column", ["id", "commune", "prefixe", "section", "numero"]); pytest.mark.parametrize(<br>    "value",<br>    [None, 123, True, "", " leading", "trailing "],<br>) | pytest.raises(CadastreNormalizationError, match=column) | 0 | Proves every cadastral identity field requires an exact nonempty string using the exact source reproduced in section 7. |
| `test_commune_requires_canonical_french_insee_identity` | pytest.mark.parametrize("commune", ["3139", "2a004", "ABCDE", "971000"]) | pytest.raises(CadastreNormalizationError, match="commune") | 0 | Proves commune requires canonical french insee identity using the exact source reproduced in section 7. |
| `test_commune_accepts_canonical_french_insee_identity` | pytest.mark.parametrize("commune", ["31395", "2A004", "2B033"]) | none | 1 | Proves commune accepts canonical french insee identity using the exact source reproduced in section 7. |

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
from copy import deepcopy
from pathlib import Path

import geopandas as gpd
import pandas as pd
import pytest
from geopandas.testing import assert_geodataframe_equal
from shapely.geometry import LineString, MultiPolygon, Point, Polygon

from landscout.sources.cadastre_fr import CadastreDownload
from landscout.sources.cadastre_loader_fr import CadastreParcelSource
from landscout.stages.normalize_cadastre import (
    CadastreNormalizationError,
    normalize_cadastre_parcels,
)


@pytest.fixture(autouse=True)
def _physical_revalidation_stub(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        "landscout.stages.normalize_cadastre.revalidate_cadastre_parcel_source",
        lambda source: source.parcels.copy(deep=True),
    )


def _bound_source(parcels: object) -> CadastreParcelSource:
    commune = "31395"
    if isinstance(parcels, gpd.GeoDataFrame) and "commune" in parcels.columns:
        first = parcels["commune"].iloc[0]
        if isinstance(first, str):
            commune = first
    download = CadastreDownload(
        commune_code=commune,
        source_url="https://cadastre.data.gouv.fr/unused",
        download_timestamp="2026-08-16T10:00:00+00:00",
        filename="unused.json.gz",
        file_size=1,
        sha256="0" * 64,
        path=Path("unused.json.gz"),
        cache_hit=True,
    )
    return CadastreParcelSource(
        download=download,
        parcels=parcels,  # type: ignore[arg-type]
    )


def _normalize(parcels: object) -> gpd.GeoDataFrame:
    return normalize_cadastre_parcels(_bound_source(parcels))


def _source_parcels(
    geometries: list[object],
    ids: list[object] | None = None,
    crs: str | None = "EPSG:4326",
) -> gpd.GeoDataFrame:
    parcel_ids = ids or [
        f"313950000A{index + 1:04d}" for index in range(len(geometries))
    ]
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


@pytest.fixture
def valid_polygon() -> Polygon:
    return Polygon([(2.35, 43.45), (2.36, 43.45), (2.36, 43.46), (2.35, 43.45)])


def test_field_normalization(valid_polygon: Polygon) -> None:
    normalized = _normalize(_source_parcels([valid_polygon]))

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
    assert normalized.iloc[0]["parcel_id"] == "313950000A0001"
    assert normalized.iloc[0]["commune_code"] == "31395"
    assert normalized.iloc[0]["geometry_status"] == "VALID"


def test_lambert93_area_calculation(valid_polygon: Polygon) -> None:
    source = _source_parcels([valid_polygon])
    expected_area = source.to_crs("EPSG:2154").geometry.area.iloc[0]

    normalized = _normalize(source)

    assert normalized.iloc[0]["area_m2"] == pytest.approx(expected_area)
    assert normalized.iloc[0]["area_m2"] > 0


def test_output_geometry_stays_in_wgs84(valid_polygon: Polygon) -> None:
    source = _source_parcels([valid_polygon])

    normalized = _normalize(source)

    assert normalized.crs is not None
    assert normalized.crs.to_epsg() == 4326
    assert normalized.geometry.iloc[0].equals_exact(valid_polygon, tolerance=0)


def test_invalid_geometry_is_preserved_with_null_area() -> None:
    bow_tie = Polygon([(2.35, 43.45), (2.36, 43.46), (2.35, 43.46), (2.36, 43.45)])
    assert not bow_tie.is_valid

    normalized = _normalize(_source_parcels([bow_tie]))

    assert normalized.iloc[0]["geometry_status"] == "INVALID"
    assert normalized["area_m2"].isna().iloc[0]
    assert normalized.geometry.iloc[0].equals_exact(bow_tie, tolerance=0)


def test_missing_crs_fails(valid_polygon: Polygon) -> None:
    source = _source_parcels([valid_polygon], crs=None)

    with pytest.raises(CadastreNormalizationError, match="CRS"):
        _normalize(source)


def test_duplicate_parcel_id_fails(valid_polygon: Polygon) -> None:
    source = _source_parcels(
        [valid_polygon, valid_polygon], ids=["duplicate", "duplicate"]
    )

    with pytest.raises(CadastreNormalizationError, match="unique"):
        _normalize(source)


def test_non_geodataframe_is_rejected_safely() -> None:
    with pytest.raises(CadastreNormalizationError, match="GeoDataFrame"):
        _normalize(pd.DataFrame({"id": ["parcel"]}))  # type: ignore[arg-type]


def test_duplicate_columns_are_rejected(valid_polygon: Polygon) -> None:
    source = _source_parcels([valid_polygon])
    duplicate = gpd.GeoDataFrame(
        pd.concat([source, source[["id"]]], axis=1),
        geometry="geometry",
        crs=source.crs,
    )

    with pytest.raises(CadastreNormalizationError, match="columns.*unique"):
        _normalize(duplicate)


@pytest.mark.parametrize(
    "collision",
    [
        "parcel_id",
        "commune_code",
        "section_prefix",
        "parcel_number",
        "geometry_status",
        "area_m2",
    ],
)
def test_normalized_target_column_collision_is_rejected(
    valid_polygon: Polygon,
    collision: str,
) -> None:
    source = _source_parcels([valid_polygon])
    source[collision] = "forged"

    with pytest.raises(CadastreNormalizationError, match="collide"):
        _normalize(source)


def test_projected_source_crs_is_rejected(valid_polygon: Polygon) -> None:
    source = _source_parcels([valid_polygon]).to_crs("EPSG:2154")

    with pytest.raises(CadastreNormalizationError, match="4326"):
        _normalize(source)


@pytest.mark.parametrize("identifier", [1, "", " ", " parcel", "parcel "])
def test_parcel_id_must_be_an_exact_nonempty_string(
    valid_polygon: Polygon,
    identifier: object,
) -> None:
    source = _source_parcels([valid_polygon], ids=[identifier])

    with pytest.raises(CadastreNormalizationError, match="parcel_id"):
        _normalize(source)


@pytest.mark.parametrize(
    "geometry",
    [Point(2.35, 43.45), LineString([(2.35, 43.45), (2.36, 43.46)])],
)
def test_non_polygonal_geometry_is_rejected(geometry: object) -> None:
    with pytest.raises(CadastreNormalizationError, match="Polygon"):
        _normalize(_source_parcels([geometry]))


def test_valid_multipolygon_is_accepted(valid_polygon: Polygon) -> None:
    normalized = _normalize(_source_parcels([MultiPolygon([valid_polygon])]))

    assert normalized.loc[0, "geometry_status"] == "VALID"
    assert normalized.loc[0, "area_m2"] > 0


@pytest.mark.parametrize("geometry", [None, Polygon()])
def test_null_and_empty_geometry_are_preserved_as_invalid(geometry: object) -> None:
    normalized = _normalize(_source_parcels([geometry]))

    assert normalized.loc[0, "geometry_status"] == "INVALID"
    assert pd.isna(normalized.loc[0, "area_m2"])
    if geometry is None:
        assert normalized.geometry.isna().iloc[0]
    else:
        assert normalized.geometry.is_empty.iloc[0]


def test_normalization_does_not_mutate_input(valid_polygon: Polygon) -> None:
    source = _source_parcels([valid_polygon])
    before = deepcopy(source)

    _normalize(source)

    assert_geodataframe_equal(source, before)


def test_normalization_uses_the_fresh_revalidated_frame(
    valid_polygon: Polygon,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    supplied = _source_parcels([valid_polygon])
    fresh = supplied.copy(deep=True)
    source = _bound_source(supplied)

    def return_fresh_and_mutate_supplied(_: object) -> gpd.GeoDataFrame:
        supplied.loc[0, "id"] = "FORGED-AFTER-COMPARISON"
        return fresh

    monkeypatch.setattr(
        "landscout.stages.normalize_cadastre.revalidate_cadastre_parcel_source",
        return_fresh_and_mutate_supplied,
    )

    normalized = normalize_cadastre_parcels(source)

    assert normalized.loc[0, "parcel_id"] == "313950000A0001"
    assert supplied.loc[0, "id"] == "FORGED-AFTER-COMPARISON"


@pytest.mark.parametrize("column", ["id", "commune", "prefixe", "section", "numero"])
@pytest.mark.parametrize(
    "value",
    [None, 123, True, "", " leading", "trailing "],
)
def test_every_cadastral_identity_field_requires_an_exact_nonempty_string(
    valid_polygon: Polygon,
    column: str,
    value: object,
) -> None:
    source = _source_parcels([valid_polygon])
    source[column] = source[column].astype(object)
    source.loc[0, column] = value

    with pytest.raises(CadastreNormalizationError, match=column):
        _normalize(source)


@pytest.mark.parametrize("commune", ["3139", "2a004", "ABCDE", "971000"])
def test_commune_requires_canonical_french_insee_identity(
    valid_polygon: Polygon,
    commune: str,
) -> None:
    source = _source_parcels([valid_polygon])
    source.loc[0, "commune"] = commune
    source.loc[0, "id"] = f"{commune}0000A0001"

    with pytest.raises(CadastreNormalizationError, match="commune"):
        _normalize(source)


@pytest.mark.parametrize("commune", ["31395", "2A004", "2B033"])
def test_commune_accepts_canonical_french_insee_identity(
    valid_polygon: Polygon,
    commune: str,
) -> None:
    source = _source_parcels([valid_polygon])
    source.loc[0, "commune"] = commune
    source.loc[0, "id"] = f"{commune}0000A0001"

    result = _normalize(source)

    assert result.loc[0, "commune_code"] == commune
```

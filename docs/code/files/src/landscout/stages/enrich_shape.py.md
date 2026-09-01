# `src/landscout/stages/enrich_shape.py`

## File identity

- Repository path: `src/landscout/stages/enrich_shape.py`
- File type: Python source
- Layer: pipeline stage
- Domain: factual transformation, evidence, or policy boundary
- Responsibility: Adds parcel shape metrics and diagnostics for valid cadastral geometries.
- Source SHA256: `244ecb7f0cd10d6104da76275df57829e13e80a5966727da8bfd329b60498887`

## 1. STEP 7F.1A.4 contract delta

- Revalidates shape configuration and the canonical parcel prefix before computing factual shape metrics.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Adds parcel shape metrics and diagnostics for valid cadastral geometries.

The file belongs to the **pipeline stage** layer and **factual transformation, evidence, or policy boundary** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from math import isfinite`

### Third-party packages

- `import geopandas as gpd`
- `from shapely.errors import GEOSException`

### Internal LandScout imports

- `from landscout.common.cadastre_contract import validate_normalized_cadastre_parcels`
- `from landscout.geo.crs import LAMBERT93, WGS84`
- `from landscout.geo.geometry import parcel_shape_metrics_m`

## 4. Contract taxonomy

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `REQUIRED_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
REQUIRED_COLUMNS = frozenset({"parcel_id", "geometry_status", "area_m2", "geometry"})
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `DERIVED_METRIC_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
DERIVED_METRIC_COLUMNS = (
    "length_m",
    "width_m",
    "length_width_ratio",
    "compactness",
    "centroid_lat",
    "centroid_lon",
)
```

- Qualified consumers:
  - import: `tests.unit.test_enrich_shape::<module>` via `from landscout.stages.enrich_shape import (
    DERIVED_METRIC_COLUMNS,
    ShapeEnrichmentError,
    enrich_parcel_shapes,
)`
  - value/type reference: `tests.unit.test_enrich_shape::test_failed_geometry_does_not_remove_other_rows` via `DERIVED_METRIC_COLUMNS`
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `length_m`
  - `width_m`
  - `length_width_ratio`
  - `compactness`
  - `centroid_lat`
  - `centroid_lon`

### `SUPPORTED_GEOMETRY_TYPES`

- Category: module constant or closed domain.
- Exact declaration:

```python
SUPPORTED_GEOMETRY_TYPES = frozenset({"Polygon", "MultiPolygon"})
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

### `ShapeEnrichmentError`

**Source purpose:** Raised when candidate parcels cannot be enriched safely.

- Exact decorators: none.
- Exact bases: `ValueError`.

**Fields and model attributes**

No direct class/model/dataclass or `self` field assignment is declared.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.enrich_shape import ShapeEnrichmentError, enrich_parcel_shapes`
- constructor call: `landscout.stages.enrich_shape::enrich_parcel_shapes` via `ShapeEnrichmentError`
- value/type reference: `landscout.stages.enrich_shape::enrich_parcel_shapes` via `ShapeEnrichmentError`
- import: `tests.unit.test_enrich_shape::<module>` via `from landscout.stages.enrich_shape import (
    DERIVED_METRIC_COLUMNS,
    ShapeEnrichmentError,
    enrich_parcel_shapes,
)`
- value/type reference: `tests.unit.test_enrich_shape::test_missing_crs_fails` via `ShapeEnrichmentError`
- value/type reference: `tests.unit.test_enrich_shape::test_missing_parcel_id_fails` via `ShapeEnrichmentError`
- value/type reference: `tests.unit.test_enrich_shape::test_null_parcel_id_fails` via `ShapeEnrichmentError`
- value/type reference: `tests.unit.test_enrich_shape::test_duplicate_parcel_id_fails` via `ShapeEnrichmentError`
- value/type reference: `tests.unit.test_enrich_shape::test_enrichment_requires_exact_non_empty_parcel_ids` via `ShapeEnrichmentError`
- value/type reference: `tests.unit.test_enrich_shape::test_valid_candidate_area_requires_strict_positive_finite_number` via `ShapeEnrichmentError`
- value/type reference: `tests.unit.test_enrich_shape::test_shape_enrichment_rejects_noncanonical_geometry_status` via `ShapeEnrichmentError`

**Exact class source**

```python
class ShapeEnrichmentError(ValueError):
    """Raised when candidate parcels cannot be enriched safely."""
```


## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `enrich_parcel_shapes`

**Purpose:** Implements `enrich parcel shapes` within the file role: Adds parcel shape metrics and diagnostics for valid cadastral geometries.

**Exact signature**

```python
def enrich_parcel_shapes(parcels: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `output`
- Explicit raise paths:
  - `ShapeEnrichmentError(str(error))`.
  - `ShapeEnrichmentError(<br>            "Candidate parcels collide with generated shape columns: "<br>            + ", ".join(sorted(collisions))<br>        )` under lexical guard `collisions`.
  - `ShapeEnrichmentError("Shape enrichment did not preserve exact parcel IDs")` under lexical guard `len(output) != len(validated) or input_ids != output_ids`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.stages::<module>` via `from landscout.stages.enrich_shape import ShapeEnrichmentError, enrich_parcel_shapes`
- import: `tests.unit.test_enrich_shape::<module>` via `from landscout.stages.enrich_shape import (
    DERIVED_METRIC_COLUMNS,
    ShapeEnrichmentError,
    enrich_parcel_shapes,
)`
- direct call: `tests.unit.test_enrich_shape::test_square_metrics` via `enrich_parcel_shapes`
- value/type reference: `tests.unit.test_enrich_shape::test_square_metrics` via `enrich_parcel_shapes`
- direct call: `tests.unit.test_enrich_shape::test_rectangle_metrics` via `enrich_parcel_shapes`
- value/type reference: `tests.unit.test_enrich_shape::test_rectangle_metrics` via `enrich_parcel_shapes`
- direct call: `tests.unit.test_enrich_shape::test_rotated_rectangle_metrics` via `enrich_parcel_shapes`
- value/type reference: `tests.unit.test_enrich_shape::test_rotated_rectangle_metrics` via `enrich_parcel_shapes`
- direct call: `tests.unit.test_enrich_shape::test_elongated_parcel` via `enrich_parcel_shapes`
- value/type reference: `tests.unit.test_enrich_shape::test_elongated_parcel` via `enrich_parcel_shapes`
- direct call: `tests.unit.test_enrich_shape::test_centroid_coordinates` via `enrich_parcel_shapes`
- value/type reference: `tests.unit.test_enrich_shape::test_centroid_coordinates` via `enrich_parcel_shapes`
- direct call: `tests.unit.test_enrich_shape::test_output_geometry_remains_wgs84` via `enrich_parcel_shapes`
- value/type reference: `tests.unit.test_enrich_shape::test_output_geometry_remains_wgs84` via `enrich_parcel_shapes`
- direct call: `tests.unit.test_enrich_shape::test_missing_crs_fails` via `enrich_parcel_shapes`
- value/type reference: `tests.unit.test_enrich_shape::test_missing_crs_fails` via `enrich_parcel_shapes`
- direct call: `tests.unit.test_enrich_shape::test_missing_parcel_id_fails` via `enrich_parcel_shapes`
- value/type reference: `tests.unit.test_enrich_shape::test_missing_parcel_id_fails` via `enrich_parcel_shapes`
- direct call: `tests.unit.test_enrich_shape::test_null_parcel_id_fails` via `enrich_parcel_shapes`
- value/type reference: `tests.unit.test_enrich_shape::test_null_parcel_id_fails` via `enrich_parcel_shapes`
- direct call: `tests.unit.test_enrich_shape::test_duplicate_parcel_id_fails` via `enrich_parcel_shapes`
- value/type reference: `tests.unit.test_enrich_shape::test_duplicate_parcel_id_fails` via `enrich_parcel_shapes`
- direct call: `tests.unit.test_enrich_shape::test_enrichment_requires_exact_non_empty_parcel_ids` via `enrich_parcel_shapes`
- value/type reference: `tests.unit.test_enrich_shape::test_enrichment_requires_exact_non_empty_parcel_ids` via `enrich_parcel_shapes`
- direct call: `tests.unit.test_enrich_shape::test_valid_candidate_area_requires_strict_positive_finite_number` via `enrich_parcel_shapes`
- value/type reference: `tests.unit.test_enrich_shape::test_valid_candidate_area_requires_strict_positive_finite_number` via `enrich_parcel_shapes`
- direct call: `tests.unit.test_enrich_shape::test_failed_geometry_does_not_remove_other_rows` via `enrich_parcel_shapes`
- value/type reference: `tests.unit.test_enrich_shape::test_failed_geometry_does_not_remove_other_rows` via `enrich_parcel_shapes`
- direct call: `tests.unit.test_enrich_shape::test_exact_parcel_ids_are_preserved` via `enrich_parcel_shapes`
- value/type reference: `tests.unit.test_enrich_shape::test_exact_parcel_ids_are_preserved` via `enrich_parcel_shapes`
- direct call: `tests.unit.test_enrich_shape::test_enrichment_matches_centralized_shape_metrics` via `enrich_parcel_shapes`
- value/type reference: `tests.unit.test_enrich_shape::test_enrichment_matches_centralized_shape_metrics` via `enrich_parcel_shapes`
- direct call: `tests.unit.test_enrich_shape::test_shape_enrichment_rejects_noncanonical_geometry_status` via `enrich_parcel_shapes`
- value/type reference: `tests.unit.test_enrich_shape::test_shape_enrichment_rejects_noncanonical_geometry_status` via `enrich_parcel_shapes`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `validate_normalized_cadastre_parcels` | `landscout.common.cadastre_contract.validate_normalized_cadastre_parcels` |
| `ShapeEnrichmentError` | `landscout.stages.enrich_shape.ShapeEnrichmentError` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `", ".join` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `validated.reset_index(drop=True).copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `validated.reset_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |
| `output.geometry.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `output.geometry.geom_type.isin` | `unresolved local/third-party receiver; no ownership inferred` |
| `output.loc[measurable].to_crs` | `unresolved local/third-party receiver; no ownership inferred` |
| `gpd.GeoSeries(<br>        projected_centroids, index=projected.index, crs=LAMBERT93<br>    ).to_crs` | `unresolved local/third-party receiver; no ownership inferred` |
| `gpd.GeoSeries` | `geopandas.GeoSeries` |
| `projected.geometry.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcel_shape_metrics_m` | `landscout.geo.geometry.parcel_shape_metrics_m` |
| `all` | `unresolved local/third-party receiver; no ownership inferred` |
| `isfinite` | `math.isfinite` |
| `zip` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `output.geometry.isna`<br>`output.geometry.geom_type.isin`<br>`output.loc[measurable].to_crs`<br>`gpd.GeoSeries(<br>        projected_centroids, index=projected.index, crs=LAMBERT93<br>    ).to_crs`<br>`projected.geometry.items` |
| External process/environment | None directly present. |
| In-memory mutation | `output["shape_status"] = "ERROR"`<br>`output[column] = float("nan")`<br>`output.loc[index, "shape_status"] = "VALID"`<br>`output.loc[index, column] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def enrich_parcel_shapes(parcels: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    try:
        validated = validate_normalized_cadastre_parcels(parcels)
    except ValueError as error:
        raise ShapeEnrichmentError(str(error)) from error
    collisions = {"shape_status", *DERIVED_METRIC_COLUMNS} & set(validated.columns)
    if collisions:
        raise ShapeEnrichmentError(
            "Candidate parcels collide with generated shape columns: "
            + ", ".join(sorted(collisions))
        )

    output = validated.reset_index(drop=True).copy()
    output["shape_status"] = "ERROR"
    for column in DERIVED_METRIC_COLUMNS:
        output[column] = float("nan")

    measurable = (
        (output["geometry_status"] == "VALID")
        & ~output.geometry.isna()
        & ~output.geometry.is_empty
        & output.geometry.is_valid
        & output.geometry.geom_type.isin(SUPPORTED_GEOMETRY_TYPES)
    )
    projected = output.loc[measurable].to_crs(LAMBERT93)
    projected_centroids = projected.geometry.centroid
    centroids_wgs84 = gpd.GeoSeries(
        projected_centroids, index=projected.index, crs=LAMBERT93
    ).to_crs(WGS84)

    for index, geometry in projected.geometry.items():
        try:
            shape = parcel_shape_metrics_m(geometry, LAMBERT93)
            center = centroids_wgs84.loc[index]
            latitude = float(center.y)
            longitude = float(center.x)
            metrics = (
                shape.length_m,
                shape.width_m,
                shape.length_width_ratio,
                shape.compactness,
                latitude,
                longitude,
            )
            if not all(isfinite(value) for value in metrics):
                continue
        except (
            AttributeError,
            GEOSException,
            IndexError,
            TypeError,
            ValueError,
            ZeroDivisionError,
        ):
            continue

        output.loc[index, "shape_status"] = "VALID"
        for column, value in zip(DERIVED_METRIC_COLUMNS, metrics, strict=True):
            output.loc[index, column] = value

    input_ids = set(validated["parcel_id"])
    output_ids = set(output["parcel_id"])
    if len(output) != len(validated) or input_ids != output_ids:
        raise ShapeEnrichmentError("Shape enrichment did not preserve exact parcel IDs")
    return output
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.


## 7. Validation and data-contract summary

- Canonical schema/mapping declarations inventoried above: `REQUIRED_COLUMNS`, `DERIVED_METRIC_COLUMNS`.
- Exact value/null/index/CRS/geometry/hash behavior is claimed only where the reproduced validators and operations enforce it.

## 8. Public exports and package ownership

This module declares no `__all__`; no package-level public guarantee is inferred from direct importability alone.

## 9. Trust, provenance, side effects, and business boundary

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.
- Configured identity, textual lineage, byte identity, physical source reconstruction, local envelope validation, and source-complete validation remain distinct trust levels. This companion attributes only the levels implemented in the exact source.
- Filesystem, network, hashing, CRS/geometry, process, mutation, and expected-exception evidence is listed per callable; an empty category is not silently promoted to an effect.

## 10. Change impact

A source-byte change invalidates the SHA above and requires re-auditing imports/re-exports, constants/aliases/schemas, model fields/immutability, qualified callers, side effects, controlled errors, tests, source/artifact locks, and the exact full snapshot.

## 11. Exact complete current file content

The following UTF-8 snapshot is the complete current repository file, not an excerpt. Its raw-byte SHA256 is the value in **File identity**.

```python
from math import isfinite

import geopandas as gpd  # type: ignore[import-untyped]
from shapely.errors import GEOSException  # type: ignore[import-untyped]

from landscout.common.cadastre_contract import validate_normalized_cadastre_parcels
from landscout.geo.crs import LAMBERT93, WGS84
from landscout.geo.geometry import parcel_shape_metrics_m

REQUIRED_COLUMNS = frozenset({"parcel_id", "geometry_status", "area_m2", "geometry"})
DERIVED_METRIC_COLUMNS = (
    "length_m",
    "width_m",
    "length_width_ratio",
    "compactness",
    "centroid_lat",
    "centroid_lon",
)
SUPPORTED_GEOMETRY_TYPES = frozenset({"Polygon", "MultiPolygon"})


class ShapeEnrichmentError(ValueError):
    """Raised when candidate parcels cannot be enriched safely."""


def enrich_parcel_shapes(parcels: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    try:
        validated = validate_normalized_cadastre_parcels(parcels)
    except ValueError as error:
        raise ShapeEnrichmentError(str(error)) from error
    collisions = {"shape_status", *DERIVED_METRIC_COLUMNS} & set(validated.columns)
    if collisions:
        raise ShapeEnrichmentError(
            "Candidate parcels collide with generated shape columns: "
            + ", ".join(sorted(collisions))
        )

    output = validated.reset_index(drop=True).copy()
    output["shape_status"] = "ERROR"
    for column in DERIVED_METRIC_COLUMNS:
        output[column] = float("nan")

    measurable = (
        (output["geometry_status"] == "VALID")
        & ~output.geometry.isna()
        & ~output.geometry.is_empty
        & output.geometry.is_valid
        & output.geometry.geom_type.isin(SUPPORTED_GEOMETRY_TYPES)
    )
    projected = output.loc[measurable].to_crs(LAMBERT93)
    projected_centroids = projected.geometry.centroid
    centroids_wgs84 = gpd.GeoSeries(
        projected_centroids, index=projected.index, crs=LAMBERT93
    ).to_crs(WGS84)

    for index, geometry in projected.geometry.items():
        try:
            shape = parcel_shape_metrics_m(geometry, LAMBERT93)
            center = centroids_wgs84.loc[index]
            latitude = float(center.y)
            longitude = float(center.x)
            metrics = (
                shape.length_m,
                shape.width_m,
                shape.length_width_ratio,
                shape.compactness,
                latitude,
                longitude,
            )
            if not all(isfinite(value) for value in metrics):
                continue
        except (
            AttributeError,
            GEOSException,
            IndexError,
            TypeError,
            ValueError,
            ZeroDivisionError,
        ):
            continue

        output.loc[index, "shape_status"] = "VALID"
        for column, value in zip(DERIVED_METRIC_COLUMNS, metrics, strict=True):
            output.loc[index, column] = value

    input_ids = set(validated["parcel_id"])
    output_ids = set(output["parcel_id"])
    if len(output) != len(validated) or input_ids != output_ids:
        raise ShapeEnrichmentError("Shape enrichment did not preserve exact parcel IDs")
    return output
```

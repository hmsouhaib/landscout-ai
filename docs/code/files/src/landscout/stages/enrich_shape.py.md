# `src/landscout/stages/enrich_shape.py`

## File identity

- Repository path: `src/landscout/stages/enrich_shape.py`
- File type: Python source
- Layer: processing stage
- Domain: cadastre
- Responsibility: Adds parcel shape metrics and diagnostics for valid cadastral geometries.
- Source SHA256: `2cc39475e1c0e5d90ea0a4623c37a0448a4de6bd27bbc43995d1445c481b6b0f`

## 1. Purpose

Adds parcel shape metrics and diagnostics for valid cadastral geometries.

## 2. Position in LandScout architecture

This file belongs to the **processing stage** layer and the **cadastre** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from math import isfinite`
- `from numbers import Real`

### Third-party packages

- `import geopandas as gpd`
- `from shapely.errors import GEOSException`

### Internal LandScout imports

- `from landscout.common.cadastre_contract import validate_cadastre_geometry_statuses`
- `from landscout.geo.crs import LAMBERT93, WGS84`
- `from landscout.geo.geometry import parcel_shape_metrics_m`

## 4. Contract taxonomy

### A. Python constants

#### `REQUIRED_COLUMNS`

```python
REQUIRED_COLUMNS = frozenset(
    {"parcel_id", "geometry_status", "area_m2", "geometry"}
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/stages/enrich_shape.py::enrich_parcel_shapes` (value reference).

#### `DERIVED_METRIC_COLUMNS`

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

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `tests/unit/test_enrich_shape.py::<module>` (import), `src/landscout/stages/enrich_shape.py::enrich_parcel_shapes` (value reference), `tests/unit/test_enrich_shape.py::test_failed_geometry_does_not_remove_other_rows` (value reference).

#### `SUPPORTED_GEOMETRY_TYPES`

```python
SUPPORTED_GEOMETRY_TYPES = frozenset({"Polygon", "MultiPolygon"})
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `src/landscout/stages/enrich_shape.py::enrich_parcel_shapes` (value reference).


### B. Type aliases and closed domains

No module-level Literal/Annotated/TypeAlias declaration is present.

### C. Meaningful dunder contracts

No meaningful module-level dunder contract is declared.

### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

### `ShapeEnrichmentError`

**Purpose:** Raised when candidate parcels cannot be enriched safely.

**Kind:** controlled exception.

**Inheritance:** `ValueError`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.enrich_shape import ShapeEnrichmentError, enrich_parcel_shapes`.
- import: `tests/unit/test_enrich_shape.py::<module>` via `from landscout.stages.enrich_shape import (
    DERIVED_METRIC_COLUMNS,
    ShapeEnrichmentError,
    enrich_parcel_shapes,
)`.
- constructor call: `src/landscout/stages/enrich_shape.py::enrich_parcel_shapes` via `ShapeEnrichmentError`.
- expected exception type: `tests/unit/test_enrich_shape.py::test_missing_crs_fails` via `pytest.raises(ShapeEnrichmentError, match='CRS')`.
- expected exception type: `tests/unit/test_enrich_shape.py::test_missing_parcel_id_fails` via `pytest.raises(ShapeEnrichmentError, match='parcel_id')`.
- expected exception type: `tests/unit/test_enrich_shape.py::test_null_parcel_id_fails` via `pytest.raises(ShapeEnrichmentError, match='null')`.
- expected exception type: `tests/unit/test_enrich_shape.py::test_duplicate_parcel_id_fails` via `pytest.raises(ShapeEnrichmentError, match='unique')`.
- expected exception type: `tests/unit/test_enrich_shape.py::test_enrichment_requires_exact_non_empty_parcel_ids` via `pytest.raises(ShapeEnrichmentError, match='exact non-empty strings')`.
- expected exception type: `tests/unit/test_enrich_shape.py::test_valid_candidate_area_requires_strict_positive_finite_number` via `pytest.raises(ShapeEnrichmentError, match='strict positive finite numeric')`.
- expected exception type: `tests/unit/test_enrich_shape.py::test_shape_enrichment_rejects_noncanonical_geometry_status` via `pytest.raises(ShapeEnrichmentError, match='geometry_status')`.

**Exact class source**

```python
class ShapeEnrichmentError(ValueError):
    """Raised when candidate parcels cannot be enriched safely."""
```


## 6. Functions and methods

### `enrich_parcel_shapes`

**Exact signature**

```python
def enrich_parcel_shapes(parcels: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
```

**Purpose**

Copies every input parcel column and appends shape_status plus six geometry measurements; failed or non-measurable rows remain ERROR with null metrics.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
output
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(parcels, gpd.GeoDataFrame)`.
- Guard with a raise path: `parcels.columns.duplicated().any()`.
- Guard with a raise path: `missing_columns`.
- Guard with a raise path: `parcels.crs is None`.
- Guard with a raise path: `parcels.crs != WGS84`.
- Guard with a raise path: `parcels.active_geometry_name != 'geometry'`.
- Guard with a raise path: `identifiers.isna().any()`.
- Guard with a raise path: `any((not isinstance(identifier, str) or not identifier or identifier != identifier.strip() for identifier in identifiers))`.
- Guard with a raise path: `identifiers.duplicated().any()`.
- Guard with a raise path: `any((isinstance(value, bool) or not isinstance(value, Real) or (not isfinite(float(value))) or (float(value) <= 0) for value in parcels.loc[valid_geometry, 'area_m2']))`.
- Guard with a raise path: `len(output) != len(parcels) or input_ids != output_ids`.
- Explicit raise expressions: `ShapeEnrichmentError('An active geometry column is required')`, `ShapeEnrichmentError('Candidate parcel CRS is required')`, `ShapeEnrichmentError('Candidate parcel columns must be unique')`, `ShapeEnrichmentError('Candidate parcels must be a GeoDataFrame')`, `ShapeEnrichmentError('Candidate parcels must use EPSG:4326')`, `ShapeEnrichmentError('Shape enrichment did not preserve exact parcel IDs')`, `ShapeEnrichmentError('area_m2 must be a strict positive finite numeric value when geometry_status is VALID')`, `ShapeEnrichmentError('parcel_id values must be exact non-empty strings')`, `ShapeEnrichmentError('parcel_id values must be unique')`, `ShapeEnrichmentError('parcel_id values must not be null')`, `ShapeEnrichmentError(f'Missing required candidate columns: {formatted}')`, `ShapeEnrichmentError(str(error))`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `gpd.GeoSeries(projected_centroids, index=projected.index, crs=LAMBERT93).to_crs`, `output.geometry.geom_type.isin`, `output.geometry.isna`, `output.loc[measurable].to_crs`, `parcels['geometry_status'].tolist`, `projected.geometry.items`, `validate_cadastre_geometry_statuses`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `output.loc[index, 'shape_status']`, `output.loc[index, column]`, `output['shape_status']`, `output[column]`.
- Input mutation: none.

**Repository interfaces and consumers**

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.enrich_shape import ShapeEnrichmentError, enrich_parcel_shapes`.
- import: `tests/unit/test_enrich_shape.py::<module>` via `from landscout.stages.enrich_shape import (
    DERIVED_METRIC_COLUMNS,
    ShapeEnrichmentError,
    enrich_parcel_shapes,
)`.
- direct call: `tests/unit/test_enrich_shape.py::test_square_metrics` via `enrich_parcel_shapes`.
- direct call: `tests/unit/test_enrich_shape.py::test_rectangle_metrics` via `enrich_parcel_shapes`.
- direct call: `tests/unit/test_enrich_shape.py::test_rotated_rectangle_metrics` via `enrich_parcel_shapes`.
- direct call: `tests/unit/test_enrich_shape.py::test_elongated_parcel` via `enrich_parcel_shapes`.
- direct call: `tests/unit/test_enrich_shape.py::test_centroid_coordinates` via `enrich_parcel_shapes`.
- direct call: `tests/unit/test_enrich_shape.py::test_output_geometry_remains_wgs84` via `enrich_parcel_shapes`.
- direct call: `tests/unit/test_enrich_shape.py::test_missing_crs_fails` via `enrich_parcel_shapes`.
- direct call: `tests/unit/test_enrich_shape.py::test_missing_parcel_id_fails` via `enrich_parcel_shapes`.
- direct call: `tests/unit/test_enrich_shape.py::test_null_parcel_id_fails` via `enrich_parcel_shapes`.
- direct call: `tests/unit/test_enrich_shape.py::test_duplicate_parcel_id_fails` via `enrich_parcel_shapes`.
- direct call: `tests/unit/test_enrich_shape.py::test_enrichment_requires_exact_non_empty_parcel_ids` via `enrich_parcel_shapes`.
- direct call: `tests/unit/test_enrich_shape.py::test_valid_candidate_area_requires_strict_positive_finite_number` via `enrich_parcel_shapes`.
- direct call: `tests/unit/test_enrich_shape.py::test_failed_geometry_does_not_remove_other_rows` via `enrich_parcel_shapes`.
- direct call: `tests/unit/test_enrich_shape.py::test_exact_parcel_ids_are_preserved` via `enrich_parcel_shapes`.
- direct call: `tests/unit/test_enrich_shape.py::test_enrichment_matches_centralized_shape_metrics` via `enrich_parcel_shapes`.
- direct call: `tests/unit/test_enrich_shape.py::test_shape_enrichment_rejects_noncanonical_geometry_status` via `enrich_parcel_shapes`.

**Complete source-ordered implementation**

```python
def enrich_parcel_shapes(parcels: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    if not isinstance(parcels, gpd.GeoDataFrame):
        raise ShapeEnrichmentError("Candidate parcels must be a GeoDataFrame")
    if parcels.columns.duplicated().any():
        raise ShapeEnrichmentError("Candidate parcel columns must be unique")
    missing_columns = REQUIRED_COLUMNS - set(parcels.columns)
    if missing_columns:
        formatted = ", ".join(sorted(missing_columns))
        raise ShapeEnrichmentError(f"Missing required candidate columns: {formatted}")
    if parcels.crs is None:
        raise ShapeEnrichmentError("Candidate parcel CRS is required")
    if parcels.crs != WGS84:
        raise ShapeEnrichmentError("Candidate parcels must use EPSG:4326")
    if parcels.active_geometry_name != "geometry":
        raise ShapeEnrichmentError("An active geometry column is required")
    identifiers = parcels["parcel_id"]
    if identifiers.isna().any():
        raise ShapeEnrichmentError("parcel_id values must not be null")
    if any(
        not isinstance(identifier, str)
        or not identifier
        or identifier != identifier.strip()
        for identifier in identifiers
    ):
        raise ShapeEnrichmentError(
            "parcel_id values must be exact non-empty strings"
        )
    if identifiers.duplicated().any():
        raise ShapeEnrichmentError("parcel_id values must be unique")
    try:
        validate_cadastre_geometry_statuses(parcels["geometry_status"].tolist())
    except ValueError as error:
        raise ShapeEnrichmentError(str(error)) from error
    valid_geometry = parcels["geometry_status"] == "VALID"
    if any(
        isinstance(value, bool)
        or not isinstance(value, Real)
        or not isfinite(float(value))
        or float(value) <= 0
        for value in parcels.loc[valid_geometry, "area_m2"]
    ):
        raise ShapeEnrichmentError(
            "area_m2 must be a strict positive finite numeric value when "
            "geometry_status is VALID"
        )

    output = parcels.reset_index(drop=True).copy()
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
        except (AttributeError, GEOSException, IndexError, TypeError, ValueError, ZeroDivisionError):
            continue

        output.loc[index, "shape_status"] = "VALID"
        for column, value in zip(DERIVED_METRIC_COLUMNS, metrics, strict=True):
            output.loc[index, column] = value

    input_ids = set(parcels["parcel_id"])
    output_ids = set(output["parcel_id"])
    if len(output) != len(parcels) or input_ids != output_ids:
        raise ShapeEnrichmentError("Shape enrichment did not preserve exact parcel IDs")
    return output
```

**Business boundary**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.


## 7. Data contracts

### Frame-preservation and semantic notes

- The output preserves every input column, column order, row order, CRS, active geometry, and values, resets the row index to a deterministic RangeIndex, then appends `shape_status`, `length_m`, `width_m`, `length_width_ratio`, `compactness`, `centroid_lat`, and `centroid_lon`.
- `shape_status` starts as `ERROR` for every row and becomes `VALID` only after successful measurable geometry calculations. Every derived metric remains NaN on failed/non-measurable rows.

### `SHAPE_ENRICHMENT_APPEND_COLUMNS` — source-reviewed frame contract

Columns appended after every pass-through input column; output index is reset to RangeIndex.

| Position | Exact column | Dtype | Nullability/domain | Classification | Source/calculation/business meaning |
|---:|---|---|---|---|---|
| 1 | `shape_status` | non-null string values | never null; VALID or ERROR | diagnostic | Starts ERROR; becomes VALID only after all metric and centroid calculations succeed. |
| 2 | `length_m` | float64 | finite on shape_status=VALID; NaN on ERROR | geometry metric | Long side of the minimum rotated rectangle in metres. |
| 3 | `width_m` | float64 | finite positive on VALID; NaN on ERROR | geometry metric | Short side of the minimum rotated rectangle in metres. |
| 4 | `length_width_ratio` | float64 | finite and >=1 on VALID; NaN on ERROR | geometry metric | Dimensionless length/width ratio. |
| 5 | `compactness` | float64 | finite on VALID; NaN on ERROR | geometry metric | Dimensionless 4πA/P² compactness measurement. |
| 6 | `centroid_lat` | float64 | finite on VALID; NaN on ERROR | derived geographic fact | Latitude of the Lambert-93 geometry centroid transformed to EPSG:4326. |
| 7 | `centroid_lon` | float64 | finite on VALID; NaN on ERROR | derived geographic fact | Longitude of the Lambert-93 geometry centroid transformed to EPSG:4326. |

### `REQUIRED_COLUMNS` — required input frame fields (unordered when stored as a set)

```python
REQUIRED_COLUMNS = frozenset(
    {"parcel_id", "geometry_status", "area_m2", "geometry"}
)
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `area_m2` | float64 when builder initializes NaN/numeric metric; otherwise exact source numeric dtype shown by implementation | null only on the explicit no-measurement/invalid path | geometry metric | Square-metre geometry measurement; not a policy threshold unless the field belongs to configuration. |
| 2 | `geometry` | GeoPandas geometry dtype | nullable only where the owning geometry-status contract permits it | source/geometry fact | Active geometry; never an authorization or suitability result. |
| 3 | `geometry_status` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | derived factual classification | Stores one value from its separately documented closed domain; domain values are not columns. |
| 4 | `parcel_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |

### `DERIVED_METRIC_COLUMNS` — canonical or derived frame-column schema

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

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `length_m` | builder/source numeric dtype shown by the implementation; no cast is inferred from the name | null on explicit no-match/unknown paths | derived fact or proxy metric | Numeric evidence in the unit encoded by the suffix; it does not establish legal/capacity suitability. |
| 2 | `width_m` | builder/source numeric dtype shown by the implementation; no cast is inferred from the name | null on explicit no-match/unknown paths | derived fact or proxy metric | Numeric evidence in the unit encoded by the suffix; it does not establish legal/capacity suitability. |
| 3 | `length_width_ratio` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 4 | `compactness` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 5 | `centroid_lat` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 6 | `centroid_lon` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |


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

The module contributes to the cadastre flow through the exact facts, proxy evidence, policy results, diagnostics, or prechecks identified above.

## 15. Explicit non-goals

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

## 16. Tests

Test consumers and framework invocation are included in per-symbol interfaces. Test modules distinguish fixture injection from parameterized values and reproduce setup/action/assertion source.

## 17. Change impact

Any source-byte change invalidates the SHA above. Review exact exports, aliases, canonical frame schemas/dtypes, configured source/policy identities, callers, framework hooks, artifacts, and all linked tests before updating this companion.

# `src/landscout/stages/enrich_shape.py`

## File identity

- Repository path: `src/landscout/stages/enrich_shape.py`
- File type: Python source
- Primary responsibility: Adds parcel shape metrics and diagnostics for valid cadastral geometries.
- Layer / domain: `stage` / `cadastre`
- Public or internal role: Module symbols without a package re-export are internal unless imported directly by repository code.
- Source SHA256: `2cc39475e1c0e5d90ea0a4623c37a0448a4de6bd27bbc43995d1445c481b6b0f`

## 1. Purpose

Adds parcel shape metrics and diagnostics for valid cadastral geometries.

## 2. Position in LandScout architecture

This file is a `stage` artifact in the `cadastre` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from math import isfinite` — required by the implementation paths and symbols documented below.
- `from numbers import Real` — required by the implementation paths and symbols documented below.

### Third-party

- `import geopandas as gpd` — required by the implementation paths and symbols documented below.
- `from shapely.errors import GEOSException` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout.common.cadastre_contract import validate_cadastre_geometry_statuses` — required by the implementation paths and symbols documented below.
- `from landscout.geo.crs import LAMBERT93, WGS84` — required by the implementation paths and symbols documented below.
- `from landscout.geo.geometry import parcel_shape_metrics_m` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `REQUIRED_COLUMNS` | `frozenset( {"parcel_id", "geometry_status", "area_m2", "geometry"} )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `DERIVED_METRIC_COLUMNS` | `( "length_m", "width_m", "length_width_ratio", "compactness", "centroid_lat", "centroid_lon", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `SUPPORTED_GEOMETRY_TYPES` | `frozenset({"Polygon", "MultiPolygon"})` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

### `ShapeEnrichmentError`

**Purpose:** Raised when candidate parcels cannot be enriched safely.

**Inheritance:** `ValueError`.

**Model form and mutability:** class inheriting from `ValueError`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

## 6. Functions and methods

### `enrich_parcel_shapes`

**Signature**

```python
def enrich_parcel_shapes(parcels: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
```

**Purpose**

Enriches parcel shapes according to the exact implementation and guards in this file.

**Inputs**

- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `output`.

**Algorithm**

1. Checks `not isinstance(parcels, gpd.GeoDataFrame)`. When true: Raises `ShapeEnrichmentError('Candidate parcels must be a GeoDataFrame')`.
2. Checks `parcels.columns.duplicated().any()`. When true: Raises `ShapeEnrichmentError('Candidate parcel columns must be unique')`.
3. Computes `missing_columns` from `REQUIRED_COLUMNS - set(parcels.columns)`.
4. Checks `missing_columns`. When true: Computes `formatted` from `', '.join(sorted(missing_columns))`. Raises `ShapeEnrichmentError(f'Missing required candidate columns: {formatted}')`.
5. Checks `parcels.crs is None`. When true: Raises `ShapeEnrichmentError('Candidate parcel CRS is required')`.
6. Checks `parcels.crs != WGS84`. When true: Raises `ShapeEnrichmentError('Candidate parcels must use EPSG:4326')`.
7. Checks `parcels.active_geometry_name != 'geometry'`. When true: Raises `ShapeEnrichmentError('An active geometry column is required')`.
8. Computes `identifiers` from `parcels['parcel_id']`.
9. Checks `identifiers.isna().any()`. When true: Raises `ShapeEnrichmentError('parcel_id values must not be null')`.
10. Checks `any((not isinstance(identifier, str) or not identifier or identifier != identifier.strip() for identifier in identifiers))`. When true: Raises `ShapeEnrichmentError('parcel_id values must be exact non-empty strings')`.
11. Checks `identifiers.duplicated().any()`. When true: Raises `ShapeEnrichmentError('parcel_id values must be unique')`.
12. Runs guarded operation: Calls `validate_cadastre_geometry_statuses(parcels['geometry_status'].tolist())` for its validation or side effect. Handles `ValueError`.
13. Computes `valid_geometry` from `parcels['geometry_status'] == 'VALID'`.
14. Checks `any((isinstance(value, bool) or not isinstance(value, Real) or (not isfinite(float(value))) or (float(value) <= 0) for value in parcels.loc[valid_geometry, 'area_m2']))`. When true: Raises `ShapeEnrichmentError('area_m2 must be a strict positive finite numeric value when geometry_status is VALID')`.
15. Computes `output` from `parcels.reset_index(drop=True).copy()`.
16. Computes `output['shape_status']` from `'ERROR'`.
17. Iterates `column` over `DERIVED_METRIC_COLUMNS`. For each value: Computes `output[column]` from `float('nan')`.
18. Computes `measurable` from `(output['geometry_status'] == 'VALID') & ~output.geometry.isna() & ~output.geometry.is_empty & output.geometry.is_valid & output.geometry.geom_type.isin(SUPPORTED_GEOMETRY_TYPES)`.
19. Computes `projected` from `output.loc[measurable].to_crs(LAMBERT93)`.
20. Computes `projected_centroids` from `projected.geometry.centroid`.
21. Computes `centroids_wgs84` from `gpd.GeoSeries(projected_centroids, index=projected.index, crs=LAMBERT93).to_crs(WGS84)`.
22. Iterates `(index, geometry)` over `projected.geometry.items()`. For each value: Runs guarded operation: Computes `shape` from `parcel_shape_metrics_m(geometry, LAMBERT93)`. Computes `center` from `centroids_wgs84.loc[index]`. Computes `latitude` from `float(center.y)`. Computes `longitude` from `float(center.x)`. Executes 2 additional source-ordered statement(s). Handles `(AttributeError, GEOSException, IndexError, TypeError, ValueError, ZeroDivisionError)`. Computes `output.loc[index, 'shape_status']` from `'VALID'`. Iterates `(column, value)` over `zip(DERIVED_METRIC_COLUMNS, metrics, strict=True)`. For each value: Computes `output.loc[index, column]` from `value`.
23. Computes `input_ids` from `set(parcels['parcel_id'])`.
24. Computes `output_ids` from `set(output['parcel_id'])`.
25. Checks `len(output) != len(parcels) or input_ids != output_ids`. When true: Raises `ShapeEnrichmentError('Shape enrichment did not preserve exact parcel IDs')`.
26. Returns `output`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(parcels, gpd.GeoDataFrame)` is true.
- Rejects or diverts the path when `parcels.columns.duplicated().any()` is true.
- Rejects or diverts the path when `missing_columns` is true.
- Rejects or diverts the path when `parcels.crs is None` is true.
- Rejects or diverts the path when `parcels.crs != WGS84` is true.
- Rejects or diverts the path when `parcels.active_geometry_name != 'geometry'` is true.
- Rejects or diverts the path when `identifiers.isna().any()` is true.
- Rejects or diverts the path when `any((not isinstance(identifier, str) or not identifier or identifier != identifier.strip() for identifier in identifiers))` is true.
- Rejects or diverts the path when `identifiers.duplicated().any()` is true.
- Rejects or diverts the path when `any((isinstance(value, bool) or not isinstance(value, Real) or (not isfinite(float(value))) or (float(value) <= 0) for value in parcels.loc[valid_geometry, 'area_m2']))` is true.
- Rejects or diverts the path when `len(output) != len(parcels) or input_ids != output_ids` is true.

**Exceptions**

- Explicitly raises: `ShapeEnrichmentError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `gpd.GeoSeries(projected_centroids, index=projected.index, crs=LAMBERT93).to_crs`, `output.loc[measurable].to_crs`, `parcels.reset_index(drop=True).copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `', '.join`, `ShapeEnrichmentError`, `all`, `any`, `float`, `gpd.GeoSeries`, `gpd.GeoSeries(projected_centroids, index=projected.index, crs=LAMBERT93).to_crs`, `identifier.strip`, `identifiers.duplicated`, `identifiers.duplicated().any`, `identifiers.isna`, `identifiers.isna().any`, `isfinite`, `isinstance`, `len`, `output.geometry.geom_type.isin`, `output.geometry.isna`, `output.loc[measurable].to_crs`, `parcel_shape_metrics_m`, `parcels.columns.duplicated`, `parcels.columns.duplicated().any`, `parcels.reset_index`, `parcels.reset_index(drop=True).copy`, `parcels['geometry_status'].tolist`, `projected.geometry.items`, `set`, `sorted`, `str`, `validate_cadastre_geometry_statuses`, `zip`.

**Known repository callers**

- `tests/unit/test_enrich_shape.py` — `test_centroid_coordinates`
- `tests/unit/test_enrich_shape.py` — `test_duplicate_parcel_id_fails`
- `tests/unit/test_enrich_shape.py` — `test_elongated_parcel`
- `tests/unit/test_enrich_shape.py` — `test_enrichment_matches_centralized_shape_metrics`
- `tests/unit/test_enrich_shape.py` — `test_enrichment_requires_exact_non_empty_parcel_ids`
- `tests/unit/test_enrich_shape.py` — `test_exact_parcel_ids_are_preserved`
- `tests/unit/test_enrich_shape.py` — `test_failed_geometry_does_not_remove_other_rows`
- `tests/unit/test_enrich_shape.py` — `test_missing_crs_fails`
- `tests/unit/test_enrich_shape.py` — `test_missing_parcel_id_fails`
- `tests/unit/test_enrich_shape.py` — `test_null_parcel_id_fails`
- `tests/unit/test_enrich_shape.py` — `test_output_geometry_remains_wgs84`
- `tests/unit/test_enrich_shape.py` — `test_rectangle_metrics`
- `tests/unit/test_enrich_shape.py` — `test_rotated_rectangle_metrics`
- `tests/unit/test_enrich_shape.py` — `test_shape_enrichment_rejects_noncanonical_geometry_status`
- `tests/unit/test_enrich_shape.py` — `test_square_metrics`
- `tests/unit/test_enrich_shape.py` — `test_valid_candidate_area_requires_strict_positive_finite_number`

**Tests**

- `tests/unit/test_enrich_shape.py::test_centroid_coordinates`
- `tests/unit/test_enrich_shape.py::test_duplicate_parcel_id_fails`
- `tests/unit/test_enrich_shape.py::test_elongated_parcel`
- `tests/unit/test_enrich_shape.py::test_enrichment_matches_centralized_shape_metrics`
- `tests/unit/test_enrich_shape.py::test_enrichment_requires_exact_non_empty_parcel_ids`
- `tests/unit/test_enrich_shape.py::test_exact_parcel_ids_are_preserved`
- `tests/unit/test_enrich_shape.py::test_failed_geometry_does_not_remove_other_rows`
- `tests/unit/test_enrich_shape.py::test_missing_crs_fails`
- `tests/unit/test_enrich_shape.py::test_missing_parcel_id_fails`
- `tests/unit/test_enrich_shape.py::test_null_parcel_id_fails`
- `tests/unit/test_enrich_shape.py::test_output_geometry_remains_wgs84`
- `tests/unit/test_enrich_shape.py::test_rectangle_metrics`
- `tests/unit/test_enrich_shape.py::test_rotated_rectangle_metrics`
- `tests/unit/test_enrich_shape.py::test_shape_enrichment_rejects_noncanonical_geometry_status`
- `tests/unit/test_enrich_shape.py::test_square_metrics`
- `tests/unit/test_enrich_shape.py::test_valid_candidate_area_requires_strict_positive_finite_number`

**Business interpretation**

This symbol contributes to the `cadastre` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `centroid_lat` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `centroid_lon` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `compactness` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `geometry_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `length_m` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | linear distance/length in metres; proxy meaning is limited by the introducing stage. Consumers and exact calculations are the functions that reference this column above. |
| `length_width_ratio` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `parcel_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `shape_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `width_m` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | linear distance/length in metres; proxy meaning is limited by the introducing stage. Consumers and exact calculations are the functions that reference this column above. |

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

This file contributes to LandScout's `cadastre` evidence flow as described by its purpose and public symbols. It preserves the distinction among fact, proxy evidence, policy interpretation, diagnostic status, and parcel precheck.

## 15. Explicit non-goals

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

## 16. Tests

Direct name-resolved tests appear under each symbol. Higher-level tests may exercise private helpers through a public source-complete function; companion documents for all test files describe their fixtures, actions, assertions, and boundaries.

## 17. Change impact

Changing this file requires reviewing its static callers, package exports, directly mapped tests, relevant schema/hash/version constants, source locks, persisted artifact contracts, and the corresponding pipeline/cross-cutting documents. Any byte change makes the SHA256 above stale and requires regenerating this companion.

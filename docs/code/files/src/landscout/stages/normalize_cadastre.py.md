# `src/landscout/stages/normalize_cadastre.py`

## File identity

- Repository path: `src/landscout/stages/normalize_cadastre.py`
- File type: Python source
- Primary responsibility: Projects raw cadastral facts into the stable parcel schema while preserving source geometry and classifying geometry quality.
- Layer / domain: `stage` / `cadastre`
- Public or internal role: Module symbols without a package re-export are internal unless imported directly by repository code.
- Source SHA256: `53d7e407793c3e7fd9cef659f483b83acf612a95dd06dac21ff7182c9a06e679`

## 1. Purpose

Projects raw cadastral facts into the stable parcel schema while preserving source geometry and classifying geometry quality.

## 2. Position in LandScout architecture

This file is a `stage` artifact in the `cadastre` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `import re` — required by the implementation paths and symbols documented below.

### Third-party

- `import geopandas as gpd` — required by the implementation paths and symbols documented below.
- `import numpy as np` — required by the implementation paths and symbols documented below.
- `from pyproj import CRS` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout.geo.crs import LAMBERT93, WGS84` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `FIELD_MAPPING` | `{ "id": "parcel_id", "commune": "commune_code", "prefixe": "section_prefix", "section": "section", "numero": "parcel_number", "contenance": "source_contenance", "arpente": "source_arpente", "created": "source_created_at", "updated": "source_updated_at", }` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `REQUIRED_IDENTITY_COLUMNS` | `frozenset( {"id", "commune", "prefixe", "section", "numero"} )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `CANONICAL_COMMUNE_PATTERN` | `re.compile(r"^(?:\d{5}&#124;2[AB]\d{3})$")` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

### `CadastreNormalizationError`

**Purpose:** Raised when cadastral parcels cannot be normalized safely.

**Inheritance:** `ValueError`.

**Model form and mutability:** class inheriting from `ValueError`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

## 6. Functions and methods

### `normalize_cadastre_parcels`

**Signature**

```python
def normalize_cadastre_parcels(parcels: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
```

**Purpose**

Normalizes cadastre parcels according to the exact implementation and guards in this file.

**Inputs**

- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `gpd.GeoDataFrame(normalized[output_columns], geometry=geometry_column, crs=parcels.crs)`.

**Algorithm**

1. Checks `not isinstance(parcels, gpd.GeoDataFrame)`. When true: Raises `CadastreNormalizationError('Cadastre input must be a GeoDataFrame')`.
2. Checks `parcels.columns.duplicated().any()`. When true: Raises `CadastreNormalizationError('Cadastre input columns must be unique')`.
3. Checks `parcels.crs is None`. When true: Raises `CadastreNormalizationError('Cadastre input CRS is required')`.
4. Runs guarded operation: Computes `source_crs` from `CRS.from_user_input(parcels.crs)`. Handles `Exception`.
5. Checks `not source_crs.equals(CRS.from_user_input(WGS84))`. When true: Raises `CadastreNormalizationError('Cadastre source geometry must use EPSG:4326')`.
6. Computes `missing_columns` from `REQUIRED_IDENTITY_COLUMNS - set(parcels.columns)`.
7. Checks `missing_columns`. When true: Computes `formatted` from `', '.join(sorted(missing_columns))`. Raises `CadastreNormalizationError(f'Missing required cadastral identity columns: {formatted}')`.
8. Iterates `column` over `('id', 'commune', 'prefixe', 'section', 'numero')`. For each value: Computes `values` from `parcels[column].tolist()`. Checks `any((not isinstance(value, str) or not value or value != value.strip() for value in values))`. When true: Computes `label` from `'parcel_id' if column == 'id' else column`. Raises `CadastreNormalizationError(f'{label} values must be non-empty exact strings')`.
9. Checks `parcels['id'].duplicated().any()`. When true: Raises `CadastreNormalizationError('parcel_id values must be unique')`.
10. Checks `any((CANONICAL_COMMUNE_PATTERN.fullmatch(value) is None for value in parcels['commune'].tolist()))`. When true: Raises `CadastreNormalizationError('commune values must be canonical French INSEE strings')`.
11. Computes `geometry_column` from `parcels.active_geometry_name`.
12. Checks `geometry_column is None or geometry_column not in parcels.columns`. When true: Raises `CadastreNormalizationError('Cadastre geometry column is required')`.
13. Computes `non_null_geometry` from `parcels.geometry.dropna()`.
14. Computes `unsupported` from `sorted(set(non_null_geometry.geom_type.dropna()) - {'Polygon', 'MultiPolygon'})`.
15. Checks `unsupported`. When true: Raises `CadastreNormalizationError('Cadastre geometry must be Polygon or MultiPolygon; found: ' + ', '.join(unsupported))`.
16. Computes `normalized` from `parcels.rename(columns=FIELD_MAPPING).copy()`.
17. Iterates `output_column` over `FIELD_MAPPING.values()`. For each value: Checks `output_column not in normalized.columns`. When true: Computes `normalized[output_column]` from `None`.
18. Computes `valid_geometry` from `~normalized.geometry.isna() & ~normalized.geometry.is_empty & normalized.geometry.is_valid`.
19. Computes `normalized['geometry_status']` from `'INVALID'`.
20. Computes `normalized.loc[valid_geometry, 'geometry_status']` from `'VALID'`.
21. Computes `normalized['area_m2']` from `float('nan')`.
22. Computes `projected` from `normalized.loc[valid_geometry].to_crs(LAMBERT93)`.
23. Computes `normalized.loc[valid_geometry, 'area_m2']` from `projected.geometry.area`.
24. Computes `valid_areas` from `normalized.loc[valid_geometry, 'area_m2'].to_numpy(dtype='float64')`.
25. Checks `not np.isfinite(valid_areas).all() or (valid_areas <= 0).any()`. When true: Raises `CadastreNormalizationError('VALID cadastre parcel areas must be finite and positive')`.
26. Computes `output_columns` from `[*FIELD_MAPPING.values(), 'geometry_status', 'area_m2', geometry_column]`.
27. Returns `gpd.GeoDataFrame(normalized[output_columns], geometry=geometry_column, crs=parcels.crs)`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(parcels, gpd.GeoDataFrame)` is true.
- Rejects or diverts the path when `parcels.columns.duplicated().any()` is true.
- Rejects or diverts the path when `parcels.crs is None` is true.
- Rejects or diverts the path when `not source_crs.equals(CRS.from_user_input(WGS84))` is true.
- Rejects or diverts the path when `missing_columns` is true.
- Rejects or diverts the path when `parcels['id'].duplicated().any()` is true.
- Rejects or diverts the path when `any((CANONICAL_COMMUNE_PATTERN.fullmatch(value) is None for value in parcels['commune'].tolist()))` is true.
- Rejects or diverts the path when `geometry_column is None or geometry_column not in parcels.columns` is true.
- Rejects or diverts the path when `unsupported` is true.
- Rejects or diverts the path when `not np.isfinite(valid_areas).all() or (valid_areas <= 0).any()` is true.
- Rejects or diverts the path when `any((not isinstance(value, str) or not value or value != value.strip() for value in values))` is true.

**Exceptions**

- Explicitly raises: `CadastreNormalizationError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `normalized.loc[valid_geometry].to_crs`, `parcels.rename(columns=FIELD_MAPPING).copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `', '.join`, `(valid_areas <= 0).any`, `CANONICAL_COMMUNE_PATTERN.fullmatch`, `CRS.from_user_input`, `CadastreNormalizationError`, `FIELD_MAPPING.values`, `any`, `float`, `gpd.GeoDataFrame`, `isinstance`, `non_null_geometry.geom_type.dropna`, `normalized.geometry.isna`, `normalized.loc[valid_geometry, 'area_m2'].to_numpy`, `normalized.loc[valid_geometry].to_crs`, `np.isfinite`, `np.isfinite(valid_areas).all`, `parcels.columns.duplicated`, `parcels.columns.duplicated().any`, `parcels.geometry.dropna`, `parcels.rename`, `parcels.rename(columns=FIELD_MAPPING).copy`, `parcels['commune'].tolist`, `parcels['id'].duplicated`, `parcels['id'].duplicated().any`, `parcels[column].tolist`, `set`, `sorted`, `source_crs.equals`, `value.strip`.

**Known repository callers**

- `tests/unit/test_normalize_cadastre.py` — `test_commune_accepts_canonical_french_insee_identity`
- `tests/unit/test_normalize_cadastre.py` — `test_commune_requires_canonical_french_insee_identity`
- `tests/unit/test_normalize_cadastre.py` — `test_duplicate_columns_are_rejected`
- `tests/unit/test_normalize_cadastre.py` — `test_duplicate_parcel_id_fails`
- `tests/unit/test_normalize_cadastre.py` — `test_every_cadastral_identity_field_requires_an_exact_nonempty_string`
- `tests/unit/test_normalize_cadastre.py` — `test_field_normalization`
- `tests/unit/test_normalize_cadastre.py` — `test_invalid_geometry_is_preserved_with_null_area`
- `tests/unit/test_normalize_cadastre.py` — `test_lambert93_area_calculation`
- `tests/unit/test_normalize_cadastre.py` — `test_missing_crs_fails`
- `tests/unit/test_normalize_cadastre.py` — `test_non_geodataframe_is_rejected_safely`
- `tests/unit/test_normalize_cadastre.py` — `test_non_polygonal_geometry_is_rejected`
- `tests/unit/test_normalize_cadastre.py` — `test_normalization_does_not_mutate_input`
- `tests/unit/test_normalize_cadastre.py` — `test_null_and_empty_geometry_are_preserved_as_invalid`
- `tests/unit/test_normalize_cadastre.py` — `test_output_geometry_stays_in_wgs84`
- `tests/unit/test_normalize_cadastre.py` — `test_parcel_id_must_be_an_exact_nonempty_string`
- `tests/unit/test_normalize_cadastre.py` — `test_projected_source_crs_is_rejected`
- `tests/unit/test_normalize_cadastre.py` — `test_valid_multipolygon_is_accepted`

**Tests**

- `tests/unit/test_normalize_cadastre.py::test_commune_accepts_canonical_french_insee_identity`
- `tests/unit/test_normalize_cadastre.py::test_commune_requires_canonical_french_insee_identity`
- `tests/unit/test_normalize_cadastre.py::test_duplicate_columns_are_rejected`
- `tests/unit/test_normalize_cadastre.py::test_duplicate_parcel_id_fails`
- `tests/unit/test_normalize_cadastre.py::test_every_cadastral_identity_field_requires_an_exact_nonempty_string`
- `tests/unit/test_normalize_cadastre.py::test_field_normalization`
- `tests/unit/test_normalize_cadastre.py::test_invalid_geometry_is_preserved_with_null_area`
- `tests/unit/test_normalize_cadastre.py::test_lambert93_area_calculation`
- `tests/unit/test_normalize_cadastre.py::test_missing_crs_fails`
- `tests/unit/test_normalize_cadastre.py::test_non_geodataframe_is_rejected_safely`
- `tests/unit/test_normalize_cadastre.py::test_non_polygonal_geometry_is_rejected`
- `tests/unit/test_normalize_cadastre.py::test_normalization_does_not_mutate_input`
- `tests/unit/test_normalize_cadastre.py::test_null_and_empty_geometry_are_preserved_as_invalid`
- `tests/unit/test_normalize_cadastre.py::test_output_geometry_stays_in_wgs84`
- `tests/unit/test_normalize_cadastre.py::test_parcel_id_must_be_an_exact_nonempty_string`
- `tests/unit/test_normalize_cadastre.py::test_projected_source_crs_is_rejected`
- `tests/unit/test_normalize_cadastre.py::test_valid_multipolygon_is_accepted`

**Business interpretation**

This symbol contributes to the `cadastre` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `commune` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `geometry_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `id` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |

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

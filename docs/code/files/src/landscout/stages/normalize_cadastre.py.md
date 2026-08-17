# `src/landscout/stages/normalize_cadastre.py`

## File identity

- Repository path: `src/landscout/stages/normalize_cadastre.py`
- File type: Python source
- Layer: processing/policy stage
- Domain: cadastre
- Responsibility: Projects raw cadastral facts into the stable parcel schema while preserving source geometry and classifying geometry quality.
- Source SHA256: `53d7e407793c3e7fd9cef659f483b83acf612a95dd06dac21ff7182c9a06e679`

## 1. Purpose

Projects raw cadastral facts into the stable parcel schema while preserving source geometry and classifying geometry quality.

## 2. Position in LandScout architecture

This file belongs to the **processing/policy stage** layer and the **cadastre** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `import re`

### Third-party packages

- `import geopandas as gpd`
- `import numpy as np`
- `from pyproj import CRS`

### Internal LandScout imports

- `from landscout.geo.crs import LAMBERT93, WGS84`

## 4. Contract taxonomy

### A. Python constants

#### `FIELD_MAPPING`

```python
FIELD_MAPPING = {
    "id": "parcel_id",
    "commune": "commune_code",
    "prefixe": "section_prefix",
    "section": "section",
    "numero": "parcel_number",
    "contenance": "source_contenance",
    "arpente": "source_arpente",
    "created": "source_created_at",
    "updated": "source_updated_at",
}
```

Explicit mapping between source/input and target/output fields; keys and values are documented separately. Consumers include `src/landscout/stages/normalize_cadastre.py::normalize_cadastre_parcels` (value argument/reference).

#### `REQUIRED_IDENTITY_COLUMNS`

```python
REQUIRED_IDENTITY_COLUMNS = frozenset(
    {"id", "commune", "prefixe", "section", "numero"}
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section.

#### `CANONICAL_COMMUNE_PATTERN`

```python
CANONICAL_COMMUNE_PATTERN = re.compile(r"^(?:\d{5}|2[AB]\d{3})$")
```

Compiled/text regular expression used by the named validation path; the fenced declaration preserves every metacharacter exactly.


### B. Type aliases and closed domains

No module-level Literal/Annotated/TypeAlias declaration is present.

### C. Meaningful dunder contracts

No meaningful module-level dunder contract is declared.

### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

### `CadastreNormalizationError`

**Purpose:** Raised when cadastral parcels cannot be normalized safely.

**Kind:** controlled exception.

**Inheritance:** `ValueError`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.normalize_cadastre import (
    CadastreNormalizationError,
    normalize_cadastre_parcels,
)`.
- direct call or construction: `src/landscout/stages/normalize_cadastre.py::normalize_cadastre_parcels` via `CadastreNormalizationError`.
- callback/function object: `tests/unit/test_normalize_cadastre.py::test_missing_crs_fails` via `pytest.raises(CadastreNormalizationError, match='CRS')`.
- callback/function object: `tests/unit/test_normalize_cadastre.py::test_duplicate_parcel_id_fails` via `pytest.raises(CadastreNormalizationError, match='unique')`.
- callback/function object: `tests/unit/test_normalize_cadastre.py::test_non_geodataframe_is_rejected_safely` via `pytest.raises(CadastreNormalizationError, match='GeoDataFrame')`.
- callback/function object: `tests/unit/test_normalize_cadastre.py::test_duplicate_columns_are_rejected` via `pytest.raises(CadastreNormalizationError, match='columns.*unique')`.
- callback/function object: `tests/unit/test_normalize_cadastre.py::test_projected_source_crs_is_rejected` via `pytest.raises(CadastreNormalizationError, match='4326')`.
- callback/function object: `tests/unit/test_normalize_cadastre.py::test_parcel_id_must_be_an_exact_nonempty_string` via `pytest.raises(CadastreNormalizationError, match='parcel_id')`.
- callback/function object: `tests/unit/test_normalize_cadastre.py::test_non_polygonal_geometry_is_rejected` via `pytest.raises(CadastreNormalizationError, match='Polygon')`.
- callback/function object: `tests/unit/test_normalize_cadastre.py::test_every_cadastral_identity_field_requires_an_exact_nonempty_string` via `pytest.raises(CadastreNormalizationError, match=column)`.
- callback/function object: `tests/unit/test_normalize_cadastre.py::test_commune_requires_canonical_french_insee_identity` via `pytest.raises(CadastreNormalizationError, match='commune')`.
- import/re-export: `tests/unit/test_normalize_cadastre.py::<module>` via `from landscout.stages.normalize_cadastre import (
    CadastreNormalizationError,
    normalize_cadastre_parcels,
)`.

**Exact class source**

```python
class CadastreNormalizationError(ValueError):
    """Raised when cadastral parcels cannot be normalized safely."""
```


## 6. Functions and methods

### `normalize_cadastre_parcels`

**Exact signature**

```python
def normalize_cadastre_parcels(parcels: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
```

**Purpose**

Renames nine Etalab Cadastre fields into the stable LandScout parcel vocabulary, classifies polygon geometry as VALID/INVALID, computes Lambert-93 area for valid rows, and returns the exact 12-column WGS84 parcel frame.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
gpd.GeoDataFrame(normalized[output_columns], geometry=geometry_column, crs=parcels.crs)
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(parcels, gpd.GeoDataFrame)`.
- Guard with a raise path: `parcels.columns.duplicated().any()`.
- Guard with a raise path: `parcels.crs is None`.
- Guard with a raise path: `not source_crs.equals(CRS.from_user_input(WGS84))`.
- Guard with a raise path: `missing_columns`.
- Guard with a raise path: `parcels['id'].duplicated().any()`.
- Guard with a raise path: `any((CANONICAL_COMMUNE_PATTERN.fullmatch(value) is None for value in parcels['commune'].tolist()))`.
- Guard with a raise path: `geometry_column is None or geometry_column not in parcels.columns`.
- Guard with a raise path: `unsupported`.
- Guard with a raise path: `not np.isfinite(valid_areas).all() or (valid_areas <= 0).any()`.
- Guard with a raise path: `any((not isinstance(value, str) or not value or value != value.strip() for value in values))`.
- Explicit raise expressions: `CadastreNormalizationError('Cadastre geometry column is required')`, `CadastreNormalizationError('Cadastre geometry must be Polygon or MultiPolygon; found: ' + ', '.join(unsupported))`, `CadastreNormalizationError('Cadastre input CRS is required')`, `CadastreNormalizationError('Cadastre input CRS is unreadable')`, `CadastreNormalizationError('Cadastre input columns must be unique')`, `CadastreNormalizationError('Cadastre input must be a GeoDataFrame')`, `CadastreNormalizationError('Cadastre source geometry must use EPSG:4326')`, `CadastreNormalizationError('VALID cadastre parcel areas must be finite and positive')`, `CadastreNormalizationError('commune values must be canonical French INSEE strings')`, `CadastreNormalizationError('parcel_id values must be unique')`, `CadastreNormalizationError(f'Missing required cadastral identity columns: {formatted}')`, `CadastreNormalizationError(f'{label} values must be non-empty exact strings')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `(valid_areas <= 0).any`, `non_null_geometry.geom_type.dropna`, `normalized.geometry.isna`, `normalized.loc[valid_geometry, 'area_m2'].to_numpy`, `normalized.loc[valid_geometry].to_crs`, `np.isfinite(valid_areas).all`, `parcels.geometry.dropna`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: `normalized.loc[valid_geometry, 'area_m2']`, `normalized.loc[valid_geometry, 'geometry_status']`, `normalized['area_m2']`, `normalized['geometry_status']`, `normalized[output_column]`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.normalize_cadastre import (
    CadastreNormalizationError,
    normalize_cadastre_parcels,
)`.
- direct call or construction: `tests/unit/test_normalize_cadastre.py::test_field_normalization` via `normalize_cadastre_parcels`.
- direct call or construction: `tests/unit/test_normalize_cadastre.py::test_lambert93_area_calculation` via `normalize_cadastre_parcels`.
- direct call or construction: `tests/unit/test_normalize_cadastre.py::test_output_geometry_stays_in_wgs84` via `normalize_cadastre_parcels`.
- direct call or construction: `tests/unit/test_normalize_cadastre.py::test_invalid_geometry_is_preserved_with_null_area` via `normalize_cadastre_parcels`.
- direct call or construction: `tests/unit/test_normalize_cadastre.py::test_missing_crs_fails` via `normalize_cadastre_parcels`.
- direct call or construction: `tests/unit/test_normalize_cadastre.py::test_duplicate_parcel_id_fails` via `normalize_cadastre_parcels`.
- direct call or construction: `tests/unit/test_normalize_cadastre.py::test_non_geodataframe_is_rejected_safely` via `normalize_cadastre_parcels`.
- direct call or construction: `tests/unit/test_normalize_cadastre.py::test_duplicate_columns_are_rejected` via `normalize_cadastre_parcels`.
- direct call or construction: `tests/unit/test_normalize_cadastre.py::test_projected_source_crs_is_rejected` via `normalize_cadastre_parcels`.
- direct call or construction: `tests/unit/test_normalize_cadastre.py::test_parcel_id_must_be_an_exact_nonempty_string` via `normalize_cadastre_parcels`.
- direct call or construction: `tests/unit/test_normalize_cadastre.py::test_non_polygonal_geometry_is_rejected` via `normalize_cadastre_parcels`.
- direct call or construction: `tests/unit/test_normalize_cadastre.py::test_valid_multipolygon_is_accepted` via `normalize_cadastre_parcels`.
- direct call or construction: `tests/unit/test_normalize_cadastre.py::test_null_and_empty_geometry_are_preserved_as_invalid` via `normalize_cadastre_parcels`.
- direct call or construction: `tests/unit/test_normalize_cadastre.py::test_normalization_does_not_mutate_input` via `normalize_cadastre_parcels`.
- direct call or construction: `tests/unit/test_normalize_cadastre.py::test_every_cadastral_identity_field_requires_an_exact_nonempty_string` via `normalize_cadastre_parcels`.
- direct call or construction: `tests/unit/test_normalize_cadastre.py::test_commune_requires_canonical_french_insee_identity` via `normalize_cadastre_parcels`.
- direct call or construction: `tests/unit/test_normalize_cadastre.py::test_commune_accepts_canonical_french_insee_identity` via `normalize_cadastre_parcels`.
- import/re-export: `tests/unit/test_normalize_cadastre.py::<module>` via `from landscout.stages.normalize_cadastre import (
    CadastreNormalizationError,
    normalize_cadastre_parcels,
)`.

**Complete source-ordered implementation**

```python
def normalize_cadastre_parcels(parcels: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    if not isinstance(parcels, gpd.GeoDataFrame):
        raise CadastreNormalizationError("Cadastre input must be a GeoDataFrame")
    if parcels.columns.duplicated().any():
        raise CadastreNormalizationError("Cadastre input columns must be unique")
    if parcels.crs is None:
        raise CadastreNormalizationError("Cadastre input CRS is required")
    try:
        source_crs = CRS.from_user_input(parcels.crs)
    except Exception as error:
        raise CadastreNormalizationError("Cadastre input CRS is unreadable") from error
    if not source_crs.equals(CRS.from_user_input(WGS84)):
        raise CadastreNormalizationError("Cadastre source geometry must use EPSG:4326")

    missing_columns = REQUIRED_IDENTITY_COLUMNS - set(parcels.columns)
    if missing_columns:
        formatted = ", ".join(sorted(missing_columns))
        raise CadastreNormalizationError(
            f"Missing required cadastral identity columns: {formatted}"
        )
    for column in ("id", "commune", "prefixe", "section", "numero"):
        values = parcels[column].tolist()
        if any(
            not isinstance(value, str)
            or not value
            or value != value.strip()
            for value in values
        ):
            label = "parcel_id" if column == "id" else column
            raise CadastreNormalizationError(
                f"{label} values must be non-empty exact strings"
            )
    if parcels["id"].duplicated().any():
        raise CadastreNormalizationError("parcel_id values must be unique")
    if any(
        CANONICAL_COMMUNE_PATTERN.fullmatch(value) is None
        for value in parcels["commune"].tolist()
    ):
        raise CadastreNormalizationError(
            "commune values must be canonical French INSEE strings"
        )

    geometry_column = parcels.active_geometry_name
    if geometry_column is None or geometry_column not in parcels.columns:
        raise CadastreNormalizationError("Cadastre geometry column is required")
    non_null_geometry = parcels.geometry.dropna()
    unsupported = sorted(
        set(non_null_geometry.geom_type.dropna()) - {"Polygon", "MultiPolygon"}
    )
    if unsupported:
        raise CadastreNormalizationError(
            "Cadastre geometry must be Polygon or MultiPolygon; found: "
            + ", ".join(unsupported)
        )

    normalized = parcels.rename(columns=FIELD_MAPPING).copy()
    for output_column in FIELD_MAPPING.values():
        if output_column not in normalized.columns:
            normalized[output_column] = None

    valid_geometry = (
        ~normalized.geometry.isna()
        & ~normalized.geometry.is_empty
        & normalized.geometry.is_valid
    )
    normalized["geometry_status"] = "INVALID"
    normalized.loc[valid_geometry, "geometry_status"] = "VALID"
    normalized["area_m2"] = float("nan")
    projected = normalized.loc[valid_geometry].to_crs(LAMBERT93)
    normalized.loc[valid_geometry, "area_m2"] = projected.geometry.area
    valid_areas = normalized.loc[valid_geometry, "area_m2"].to_numpy(
        dtype="float64"
    )
    if not np.isfinite(valid_areas).all() or (valid_areas <= 0).any():
        raise CadastreNormalizationError(
            "VALID cadastre parcel areas must be finite and positive"
        )

    output_columns = [
        *FIELD_MAPPING.values(),
        "geometry_status",
        "area_m2",
        geometry_column,
    ]
    return gpd.GeoDataFrame(
        normalized[output_columns], geometry=geometry_column, crs=parcels.crs
    )
```

**Business boundary**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.


## 7. Data contracts

### Frame-preservation and semantic notes

- Raw Etalab input names and normalized output names are distinct contracts; `FIELD_MAPPING` below is the complete rename map.
- The exact output order is `parcel_id`, `commune_code`, `section_prefix`, `section`, `parcel_number`, `source_contenance`, `source_arpente`, `source_created_at`, `source_updated_at`, `geometry_status`, `area_m2`, `geometry`.
- `geometry_status` is non-null and restricted to `VALID` or `INVALID`. `area_m2` is finite and positive for VALID rows and null/NaN for INVALID rows.
- The nine renamed source columns preserve their source Pandas values/dtypes; the stage does not invent download/provider/hash lineage.

### `NORMALIZED_CADASTRE_OUTPUT (function-local exact order)` — source-reviewed frame contract

Complete output GeoDataFrame returned by normalize_cadastre_parcels.

| Position | Exact column | Dtype | Nullability/domain | Classification | Source/calculation/business meaning |
|---:|---|---|---|---|---|
| 1 | `parcel_id` | source-preserved string values | non-null, non-empty, no edge whitespace, unique | normalized source identity | Exact Etalab `id`; no download/provider/hash lineage is added. |
| 2 | `commune_code` | source-preserved string values | non-null canonical INSEE string | normalized source fact | Exact Etalab `commune` renamed; canonical pattern is validated. |
| 3 | `section_prefix` | source-preserved string values | non-null, non-empty, no edge whitespace | normalized source fact | Exact Etalab `prefixe` renamed. |
| 4 | `section` | source-preserved string values | non-null, non-empty, no edge whitespace | normalized source fact | Exact Etalab `section` retained under the same name. |
| 5 | `parcel_number` | source-preserved string values | non-null, non-empty, no edge whitespace | normalized source fact | Exact Etalab `numero` renamed. |
| 6 | `source_contenance` | source-preserved/dynamic dtype | source nulls allowed; all-null object column inserted when absent | source fact | Exact Etalab `contenance`; no unit reinterpretation in this stage. |
| 7 | `source_arpente` | source-preserved/dynamic dtype | source nulls allowed; all-null object column inserted when absent | source fact | Exact Etalab `arpente` value; no Boolean coercion. |
| 8 | `source_created_at` | source-preserved/dynamic dtype | source nulls allowed; all-null object column inserted when absent | source fact | Exact Etalab `created` value. |
| 9 | `source_updated_at` | source-preserved/dynamic dtype | source nulls allowed; all-null object column inserted when absent | source fact | Exact Etalab `updated` value. |
| 10 | `geometry_status` | non-null string values | never null; exactly VALID or INVALID | derived factual geometry classification | VALID requires non-null, non-empty, Shapely-valid Polygon/MultiPolygon; INVALID preserves null/empty/invalid polygonal geometry. |
| 11 | `area_m2` | float64 | finite positive for VALID; NaN/null for INVALID | geometry metric | Area measured on a calculation-only EPSG:2154 copy; stored geometry remains EPSG:4326. |
| 12 | `geometry` | GeoPandas geometry dtype | may be null/empty/invalid only when geometry_status=INVALID | source geometry fact | Original active Polygon/MultiPolygon geometry in EPSG:4326; not repaired or reprojected in storage. |

### `FIELD_MAPPING` — mapping between source/input and output keys or columns

```python
FIELD_MAPPING = {
    "id": "parcel_id",
    "commune": "commune_code",
    "prefixe": "section_prefix",
    "section": "section",
    "numero": "parcel_number",
    "contenance": "source_contenance",
    "arpente": "source_arpente",
    "created": "source_created_at",
    "updated": "source_updated_at",
}
```

| Source/input key or column | Target/output key or column | Contract |
|---|---|---|
| `id` | `parcel_id` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `commune` | `commune_code` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `prefixe` | `section_prefix` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `section` | `section` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `numero` | `parcel_number` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `contenance` | `source_contenance` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `arpente` | `source_arpente` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `created` | `source_created_at` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `updated` | `source_updated_at` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |

### `REQUIRED_IDENTITY_COLUMNS` — required input frame fields (unordered when stored as a set)

```python
REQUIRED_IDENTITY_COLUMNS = frozenset(
    {"id", "commune", "prefixe", "section", "numero"}
)
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `commune` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 2 | `id` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 3 | `numero` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 4 | `prefixe` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 5 | `section` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |


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

# `src/landscout/stages/normalize_cadastre.py`

## File identity

- Repository path: `src/landscout/stages/normalize_cadastre.py`
- File type: Python source
- Layer: pipeline stage
- Domain: factual transformation, evidence, or policy boundary
- Responsibility: Source-completely normalizes a fresh physical `CadastreParcelSource` into the stable canonical parcel schema.
- Source SHA256: `ec01db7f8fd7e16d6938ab0c36a4fa2b2343d88ed126f833ef1da6e45a25fa50`

## 1. STEP 7F.1A.4 contract delta

- Consumes only the fresh source-complete Cadastre frame and emits the shared canonical parcel contract without trusting caller-coordinated rows.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Source-completely normalizes a fresh physical `CadastreParcelSource` into the stable canonical parcel schema.

The file belongs to the **pipeline stage** layer and **factual transformation, evidence, or policy boundary** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `import re`

### Third-party packages

- `import geopandas as gpd`
- `import numpy as np`
- `from pyproj import CRS`

### Internal LandScout imports

- `from landscout.common.cadastre_contract import (
    CADASTRE_NORMALIZED_PREFIX,
    validate_normalized_cadastre_parcels,
)`
- `from landscout.geo.crs import LAMBERT93, WGS84`
- `from landscout.sources.cadastre_loader_fr import (
    CadastreLoadError,
    CadastreParcelSource,
    revalidate_cadastre_parcel_source,
)`

## 4. Contract taxonomy

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `FIELD_MAPPING`

- Category: canonical schema/mapping declaration.
- Exact declaration:

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

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact mapping keys:
  - `id`
  - `commune`
  - `prefixe`
  - `section`
  - `numero`
  - `contenance`
  - `arpente`
  - `created`
  - `updated`

### `REQUIRED_IDENTITY_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
REQUIRED_IDENTITY_COLUMNS = frozenset({"id", "commune", "prefixe", "section", "numero"})
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `CANONICAL_COMMUNE_PATTERN`

- Category: module constant or closed domain.
- Exact declaration:

```python
CANONICAL_COMMUNE_PATTERN = re.compile(r"^(?:\d{5}|2[AB]\d{3})$")
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

### `CadastreNormalizationError`

**Source purpose:** Raised when cadastral parcels cannot be normalized safely.

- Exact decorators: none.
- Exact bases: `ValueError`.

**Fields and model attributes**

No direct class/model/dataclass or `self` field assignment is declared.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.normalize_cadastre import (
    CadastreNormalizationError,
    normalize_cadastre_parcels,
)`
- constructor call: `landscout.stages.normalize_cadastre::normalize_cadastre_parcels` via `CadastreNormalizationError`
- value/type reference: `landscout.stages.normalize_cadastre::normalize_cadastre_parcels` via `CadastreNormalizationError`
- import: `tests.unit.test_normalize_cadastre::<module>` via `from landscout.stages.normalize_cadastre import (
    CadastreNormalizationError,
    normalize_cadastre_parcels,
)`
- value/type reference: `tests.unit.test_normalize_cadastre::test_missing_crs_fails` via `CadastreNormalizationError`
- value/type reference: `tests.unit.test_normalize_cadastre::test_duplicate_parcel_id_fails` via `CadastreNormalizationError`
- value/type reference: `tests.unit.test_normalize_cadastre::test_non_geodataframe_is_rejected_safely` via `CadastreNormalizationError`
- value/type reference: `tests.unit.test_normalize_cadastre::test_duplicate_columns_are_rejected` via `CadastreNormalizationError`
- value/type reference: `tests.unit.test_normalize_cadastre::test_normalized_target_column_collision_is_rejected` via `CadastreNormalizationError`
- value/type reference: `tests.unit.test_normalize_cadastre::test_projected_source_crs_is_rejected` via `CadastreNormalizationError`
- value/type reference: `tests.unit.test_normalize_cadastre::test_parcel_id_must_be_an_exact_nonempty_string` via `CadastreNormalizationError`
- value/type reference: `tests.unit.test_normalize_cadastre::test_non_polygonal_geometry_is_rejected` via `CadastreNormalizationError`
- value/type reference: `tests.unit.test_normalize_cadastre::test_every_cadastral_identity_field_requires_an_exact_nonempty_string` via `CadastreNormalizationError`
- value/type reference: `tests.unit.test_normalize_cadastre::test_commune_requires_canonical_french_insee_identity` via `CadastreNormalizationError`

**Exact class source**

```python
class CadastreNormalizationError(ValueError):
    """Raised when cadastral parcels cannot be normalized safely."""
```


## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `normalize_cadastre_parcels`

**Purpose:** Implements `normalize cadastre parcels` within the file role: Source-completely normalizes a fresh physical `CadastreParcelSource` into the stable canonical parcel schema.

**Exact signature**

```python
def normalize_cadastre_parcels(source: CadastreParcelSource) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source` | positional-or-keyword | `CadastreParcelSource` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `output`
- Explicit raise paths:
  - `CadastreNormalizationError(<br>            "Cadastre input must be an exact CadastreParcelSource"<br>        )` under lexical guard `type(source) is not CadastreParcelSource`.
  - `CadastreNormalizationError(<br>            "Cadastre physical source revalidation failed"<br>        )`.
  - `CadastreNormalizationError(<br>            "Fresh Cadastre parcels must be a GeoDataFrame"<br>        )` under lexical guard `not isinstance(parcels, gpd.GeoDataFrame)`.
  - `CadastreNormalizationError("Cadastre input columns must be unique")` under lexical guard `parcels.columns.duplicated().any()`.
  - `CadastreNormalizationError("Cadastre input CRS is required")` under lexical guard `parcels.crs is None`.
  - `CadastreNormalizationError("Cadastre input CRS is unreadable")`.
  - `CadastreNormalizationError("Cadastre source geometry must use EPSG:4326")` under lexical guard `not source_crs.equals(CRS.from_user_input(WGS84))`.
  - `CadastreNormalizationError(<br>            f"Missing required cadastral identity columns: {formatted}"<br>        )` under lexical guard `missing_columns`.
  - `CadastreNormalizationError(<br>            "Cadastre source attributes collide with normalized columns: "<br>            + ", ".join(sorted(target_collisions))<br>        )` under lexical guard `target_collisions`.
  - `CadastreNormalizationError(<br>                f"{label} values must be non-empty exact strings"<br>            )` under lexical guard `any(<br>            not isinstance(value, str) or not value or value != value.strip()<br>            for value in values<br>        )`.
  - `CadastreNormalizationError("parcel_id values must be unique")` under lexical guard `parcels["id"].duplicated().any()`.
  - `CadastreNormalizationError(<br>            "commune values must be canonical French INSEE strings"<br>        )` under lexical guard `any(<br>        CANONICAL_COMMUNE_PATTERN.fullmatch(value) is None<br>        for value in parcels["commune"].tolist()<br>    )`.
  - `CadastreNormalizationError(<br>            "Cadastre parcel commune differs from its physical download identity"<br>        )` under lexical guard `any(<br>        value != source.download.commune_code for value in parcels["commune"].tolist()<br>    )`.
  - `CadastreNormalizationError("Cadastre geometry column is required")` under lexical guard `geometry_column is None or geometry_column not in parcels.columns`.
  - `CadastreNormalizationError(<br>            "Cadastre active geometry must use the canonical geometry name"<br>        )` under lexical guard `geometry_column != "geometry"`.
  - `CadastreNormalizationError(<br>            "Cadastre geometry must be Polygon or MultiPolygon; found: "<br>            + ", ".join(unsupported)<br>        )` under lexical guard `unsupported`.
  - `CadastreNormalizationError("Cadastre geometry must be exactly 2D")` under lexical guard `any(bool(value) for value in non_null_geometry.has_z)`.
  - `CadastreNormalizationError(<br>            "VALID cadastre parcel areas must be finite and positive"<br>        )` under lexical guard `not np.isfinite(valid_areas).all() or (valid_areas <= 0).any()`.
  - `CadastreNormalizationError(str(error))`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.stages::<module>` via `from landscout.stages.normalize_cadastre import (
    CadastreNormalizationError,
    normalize_cadastre_parcels,
)`
- import: `tests.unit.test_normalize_cadastre::<module>` via `from landscout.stages.normalize_cadastre import (
    CadastreNormalizationError,
    normalize_cadastre_parcels,
)`
- direct call: `tests.unit.test_normalize_cadastre::_normalize` via `normalize_cadastre_parcels`
- value/type reference: `tests.unit.test_normalize_cadastre::_normalize` via `normalize_cadastre_parcels`
- direct call: `tests.unit.test_normalize_cadastre::test_normalization_uses_the_fresh_revalidated_frame` via `normalize_cadastre_parcels`
- value/type reference: `tests.unit.test_normalize_cadastre::test_normalization_uses_the_fresh_revalidated_frame` via `normalize_cadastre_parcels`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `CadastreNormalizationError` | `landscout.stages.normalize_cadastre.CadastreNormalizationError` |
| `revalidate_cadastre_parcel_source` | `landscout.sources.cadastre_loader_fr.revalidate_cadastre_parcel_source` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels.columns.duplicated().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels.columns.duplicated` | `unresolved local/third-party receiver; no ownership inferred` |
| `CRS.from_user_input` | `pyproj.CRS.from_user_input` |
| `source_crs.equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `", ".join` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels[column].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `value.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels["id"].duplicated().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels["id"].duplicated` | `unresolved local/third-party receiver; no ownership inferred` |
| `CANONICAL_COMMUNE_PATTERN.fullmatch` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels["commune"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels.geometry.dropna` | `unresolved local/third-party receiver; no ownership inferred` |
| `non_null_geometry.geom_type.dropna` | `unresolved local/third-party receiver; no ownership inferred` |
| `bool` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels.rename(columns=FIELD_MAPPING).reset_index(drop=True).copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels.rename(columns=FIELD_MAPPING).reset_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels.rename` | `unresolved local/third-party receiver; no ownership inferred` |
| `FIELD_MAPPING.values` | `unresolved local/third-party receiver; no ownership inferred` |
| `normalized.geometry.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |
| `normalized.loc[valid_geometry].to_crs` | `unresolved local/third-party receiver; no ownership inferred` |
| `normalized.loc[valid_geometry, "area_m2"].to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `np.isfinite(valid_areas).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `np.isfinite` | `numpy.isfinite` |
| `(valid_areas <= 0).any` | `unresolved local/third-party receiver; no ownership inferred` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `validate_normalized_cadastre_parcels` | `landscout.common.cadastre_contract.validate_normalized_cadastre_parcels` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `parcels.geometry.dropna`<br>`non_null_geometry.geom_type.dropna`<br>`normalized.geometry.isna`<br>`normalized.loc[valid_geometry].to_crs`<br>`normalized.loc[valid_geometry, "area_m2"].to_numpy` |
| External process/environment | None directly present. |
| In-memory mutation | `parcels.rename(columns=FIELD_MAPPING)`<br>`normalized[output_column] = None`<br>`normalized["geometry_status"] = "INVALID"`<br>`normalized.loc[valid_geometry, "geometry_status"] = "VALID"`<br>`normalized["area_m2"] = float("nan")`<br>`normalized.loc[valid_geometry, "area_m2"] = projected.geometry.area` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def normalize_cadastre_parcels(source: CadastreParcelSource) -> gpd.GeoDataFrame:
    if type(source) is not CadastreParcelSource:
        raise CadastreNormalizationError(
            "Cadastre input must be an exact CadastreParcelSource"
        )
    try:
        parcels = revalidate_cadastre_parcel_source(source)
    except CadastreLoadError as error:
        raise CadastreNormalizationError(
            "Cadastre physical source revalidation failed"
        ) from error
    if not isinstance(parcels, gpd.GeoDataFrame):
        raise CadastreNormalizationError(
            "Fresh Cadastre parcels must be a GeoDataFrame"
        )
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
    target_collisions = (
        set(CADASTRE_NORMALIZED_PREFIX) - {"section", "geometry"}
    ) & set(parcels.columns)
    if target_collisions:
        raise CadastreNormalizationError(
            "Cadastre source attributes collide with normalized columns: "
            + ", ".join(sorted(target_collisions))
        )
    for column in ("id", "commune", "prefixe", "section", "numero"):
        values = parcels[column].tolist()
        if any(
            not isinstance(value, str) or not value or value != value.strip()
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
    if any(
        value != source.download.commune_code for value in parcels["commune"].tolist()
    ):
        raise CadastreNormalizationError(
            "Cadastre parcel commune differs from its physical download identity"
        )

    geometry_column = parcels.active_geometry_name
    if geometry_column is None or geometry_column not in parcels.columns:
        raise CadastreNormalizationError("Cadastre geometry column is required")
    if geometry_column != "geometry":
        raise CadastreNormalizationError(
            "Cadastre active geometry must use the canonical geometry name"
        )
    non_null_geometry = parcels.geometry.dropna()
    unsupported = sorted(
        set(non_null_geometry.geom_type.dropna()) - {"Polygon", "MultiPolygon"}
    )
    if unsupported:
        raise CadastreNormalizationError(
            "Cadastre geometry must be Polygon or MultiPolygon; found: "
            + ", ".join(unsupported)
        )
    if any(bool(value) for value in non_null_geometry.has_z):
        raise CadastreNormalizationError("Cadastre geometry must be exactly 2D")

    normalized = parcels.rename(columns=FIELD_MAPPING).reset_index(drop=True).copy()
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
    valid_areas = normalized.loc[valid_geometry, "area_m2"].to_numpy(dtype="float64")
    if not np.isfinite(valid_areas).all() or (valid_areas <= 0).any():
        raise CadastreNormalizationError(
            "VALID cadastre parcel areas must be finite and positive"
        )

    output = gpd.GeoDataFrame(
        normalized[list(CADASTRE_NORMALIZED_PREFIX)],
        geometry="geometry",
        crs=parcels.crs,
    )
    try:
        validate_normalized_cadastre_parcels(output)
    except ValueError as error:
        raise CadastreNormalizationError(str(error)) from error
    return output
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.


## 7. Validation and data-contract summary

- Canonical schema/mapping declarations inventoried above: `FIELD_MAPPING`, `REQUIRED_IDENTITY_COLUMNS`.
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
import re

import geopandas as gpd  # type: ignore[import-untyped]
import numpy as np
from pyproj import CRS

from landscout.common.cadastre_contract import (
    CADASTRE_NORMALIZED_PREFIX,
    validate_normalized_cadastre_parcels,
)
from landscout.geo.crs import LAMBERT93, WGS84
from landscout.sources.cadastre_loader_fr import (
    CadastreLoadError,
    CadastreParcelSource,
    revalidate_cadastre_parcel_source,
)

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
REQUIRED_IDENTITY_COLUMNS = frozenset({"id", "commune", "prefixe", "section", "numero"})
CANONICAL_COMMUNE_PATTERN = re.compile(r"^(?:\d{5}|2[AB]\d{3})$")


class CadastreNormalizationError(ValueError):
    """Raised when cadastral parcels cannot be normalized safely."""


def normalize_cadastre_parcels(source: CadastreParcelSource) -> gpd.GeoDataFrame:
    if type(source) is not CadastreParcelSource:
        raise CadastreNormalizationError(
            "Cadastre input must be an exact CadastreParcelSource"
        )
    try:
        parcels = revalidate_cadastre_parcel_source(source)
    except CadastreLoadError as error:
        raise CadastreNormalizationError(
            "Cadastre physical source revalidation failed"
        ) from error
    if not isinstance(parcels, gpd.GeoDataFrame):
        raise CadastreNormalizationError(
            "Fresh Cadastre parcels must be a GeoDataFrame"
        )
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
    target_collisions = (
        set(CADASTRE_NORMALIZED_PREFIX) - {"section", "geometry"}
    ) & set(parcels.columns)
    if target_collisions:
        raise CadastreNormalizationError(
            "Cadastre source attributes collide with normalized columns: "
            + ", ".join(sorted(target_collisions))
        )
    for column in ("id", "commune", "prefixe", "section", "numero"):
        values = parcels[column].tolist()
        if any(
            not isinstance(value, str) or not value or value != value.strip()
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
    if any(
        value != source.download.commune_code for value in parcels["commune"].tolist()
    ):
        raise CadastreNormalizationError(
            "Cadastre parcel commune differs from its physical download identity"
        )

    geometry_column = parcels.active_geometry_name
    if geometry_column is None or geometry_column not in parcels.columns:
        raise CadastreNormalizationError("Cadastre geometry column is required")
    if geometry_column != "geometry":
        raise CadastreNormalizationError(
            "Cadastre active geometry must use the canonical geometry name"
        )
    non_null_geometry = parcels.geometry.dropna()
    unsupported = sorted(
        set(non_null_geometry.geom_type.dropna()) - {"Polygon", "MultiPolygon"}
    )
    if unsupported:
        raise CadastreNormalizationError(
            "Cadastre geometry must be Polygon or MultiPolygon; found: "
            + ", ".join(unsupported)
        )
    if any(bool(value) for value in non_null_geometry.has_z):
        raise CadastreNormalizationError("Cadastre geometry must be exactly 2D")

    normalized = parcels.rename(columns=FIELD_MAPPING).reset_index(drop=True).copy()
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
    valid_areas = normalized.loc[valid_geometry, "area_m2"].to_numpy(dtype="float64")
    if not np.isfinite(valid_areas).all() or (valid_areas <= 0).any():
        raise CadastreNormalizationError(
            "VALID cadastre parcel areas must be finite and positive"
        )

    output = gpd.GeoDataFrame(
        normalized[list(CADASTRE_NORMALIZED_PREFIX)],
        geometry="geometry",
        crs=parcels.crs,
    )
    try:
        validate_normalized_cadastre_parcels(output)
    except ValueError as error:
        raise CadastreNormalizationError(str(error)) from error
    return output
```

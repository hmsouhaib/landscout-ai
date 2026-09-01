# `src/landscout/common/cadastre_contract.py`

## File identity

- Repository path: `src/landscout/common/cadastre_contract.py`
- File type: Python source
- Layer: internal common contract
- Domain: shared validation and schema contracts
- Responsibility: Validates the canonical normalized Cadastre prefix, identity, 2D geometry/status facts, and recomputed EPSG:2154 parcel areas.
- Source SHA256: `d4114d81eba70240885bf959ce1f1aaebe09ef2cb21f284fecb6e98e3e79f95e`

## 1. STEP 7F.1A.4 contract delta

- Centralizes the canonical normalized parcel identity, 2D geometry/status, deterministic index/schema, and independently recomputed EPSG:2154 area contract.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Validates the canonical normalized Cadastre prefix, identity, 2D geometry/status facts, and recomputed EPSG:2154 parcel areas.

The file belongs to the **internal common contract** layer and **shared validation and schema contracts** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `import re`
- `from collections.abc import Iterable`
- `from math import isfinite`
- `from numbers import Real`

### Third-party packages

- `import geopandas as gpd`
- `import pandas as pd`
- `from pyproj import CRS`

### Internal LandScout imports

- `from landscout.geo.crs import LAMBERT93, WGS84`

## 4. Contract taxonomy

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `CADASTRE_GEOMETRY_STATUSES`

- Category: module constant or closed domain.
- Exact declaration:

```python
CADASTRE_GEOMETRY_STATUSES = frozenset({"VALID", "INVALID"})
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `CADASTRE_NORMALIZED_PREFIX`

- Category: module constant or closed domain.
- Exact declaration:

```python
CADASTRE_NORMALIZED_PREFIX = (
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
)
```

- Qualified consumers:
  - import: `landscout.stages.normalize_cadastre::<module>` via `from landscout.common.cadastre_contract import (
    CADASTRE_NORMALIZED_PREFIX,
    validate_normalized_cadastre_parcels,
)`
  - value/type reference: `landscout.stages.normalize_cadastre::normalize_cadastre_parcels` via `CADASTRE_NORMALIZED_PREFIX`
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `parcel_id`
  - `commune_code`
  - `section_prefix`
  - `section`
  - `parcel_number`
  - `source_contenance`
  - `source_arpente`
  - `source_created_at`
  - `source_updated_at`
  - `geometry_status`
  - `area_m2`
  - `geometry`

### `CADASTRE_AREA_ABSOLUTE_TOLERANCE_M2`

- Category: module constant or closed domain.
- Exact declaration:

```python
CADASTRE_AREA_ABSOLUTE_TOLERANCE_M2 = 1e-6
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `CADASTRE_AREA_RELATIVE_TOLERANCE`

- Category: module constant or closed domain.
- Exact declaration:

```python
CADASTRE_AREA_RELATIVE_TOLERANCE = 1e-12
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_CANONICAL_COMMUNE`

- Category: module constant or closed domain.
- Exact declaration:

```python
_CANONICAL_COMMUNE = re.compile(r"^(?:\d{5}|2[AB]\d{3})$")
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

No top-level class/model/dataclass is declared.

## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `validate_cadastre_geometry_statuses`

**Purpose:** Require the exact geometry-status vocabulary emitted by normalization.

**Exact signature**

```python
def validate_cadastre_geometry_statuses(values: Iterable[object]) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `values` | positional-or-keyword | `Iterable[object]` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `ValueError(<br>            "geometry_status must contain only exact VALID or INVALID strings"<br>        )` under lexical guard `any(<br>        type(value) is not str or value not in CADASTRE_GEOMETRY_STATUSES<br>        for value in values<br>    )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.common.cadastre_contract::validate_normalized_cadastre_parcels` via `validate_cadastre_geometry_statuses`
- value/type reference: `landscout.common.cadastre_contract::validate_normalized_cadastre_parcels` via `validate_cadastre_geometry_statuses`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |

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
def validate_cadastre_geometry_statuses(values: Iterable[object]) -> None:
    """Require the exact geometry-status vocabulary emitted by normalization."""

    if any(
        type(value) is not str or value not in CADASTRE_GEOMETRY_STATUSES
        for value in values
    ):
        raise ValueError(
            "geometry_status must contain only exact VALID or INVALID strings"
        )
```

**Business boundary**

- This contract validates or represents inputs; it does not rank parcels, combine criteria, or create a legal, access, grid-capacity, environmental, or planning conclusion.

### `_require_exact_strings`

**Purpose:** Implements `require exact strings` within the file role: Validates the canonical normalized Cadastre prefix, identity, 2D geometry/status facts, and recomputed EPSG:2154 parcel areas.

**Exact signature**

```python
def _require_exact_strings(values: Iterable[object], label: str) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `values` | positional-or-keyword | `Iterable[object]` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `ValueError(f"{label} values must not be null")` under lexical guard `any(bool(pd.isna(value)) for value in items)`.
  - `ValueError(f"{label} values must be exact non-empty strings")` under lexical guard `any(<br>        type(value) is not str or not value or value != value.strip() for value in items<br>    )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.common.cadastre_contract::validate_normalized_cadastre_parcels` via `_require_exact_strings`
- value/type reference: `landscout.common.cadastre_contract::validate_normalized_cadastre_parcels` via `_require_exact_strings`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `bool` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.isna` | `pandas.isna` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `value.strip` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _require_exact_strings(values: Iterable[object], label: str) -> None:
    items = tuple(values)
    if any(bool(pd.isna(value)) for value in items):
        raise ValueError(f"{label} values must not be null")
    if any(
        type(value) is not str or not value or value != value.strip() for value in items
    ):
        raise ValueError(f"{label} values must be exact non-empty strings")
```

**Business boundary**

- This contract validates or represents inputs; it does not rank parcels, combine criteria, or create a legal, access, grid-capacity, environmental, or planning conclusion.

### `validate_normalized_cadastre_parcels`

**Purpose:** Validate the canonical normalized Cadastre prefix and cross-field facts.

**Exact signature**

```python
def validate_normalized_cadastre_parcels(
    parcels: object,
) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `parcels`
- Explicit raise paths:
  - `ValueError(  # noqa: TRY004 - one stable validation-error contract<br>            "Normalized Cadastre parcels must be a GeoDataFrame"<br>        )` under lexical guard `not isinstance(parcels, gpd.GeoDataFrame)`.
  - `ValueError("Normalized Cadastre parcel columns must be unique")` under lexical guard `parcels.columns.duplicated().any()`.
  - `ValueError(<br>            "Normalized Cadastre parcels must retain the exact canonical column prefix "<br>            "including parcel_id"<br>        )` under lexical guard `tuple(str(column) for column in parcels.columns[:12]) != (<br>        CADASTRE_NORMALIZED_PREFIX<br>    )`.
  - `ValueError("Normalized Cadastre parcels require active geometry")` under lexical guard `parcels.active_geometry_name != "geometry"`.
  - `ValueError("Normalized Cadastre parcel CRS is required")` under lexical guard `parcels.crs is None`.
  - `ValueError("Normalized Cadastre parcel CRS is unreadable")`.
  - `ValueError("Normalized Cadastre parcels must use EPSG:4326")` under lexical guard `not crs.equals(CRS.from_user_input(WGS84))`.
  - `ValueError("parcel_id values must be unique")` under lexical guard `parcels["parcel_id"].duplicated().any()`.
  - `ValueError("commune_code values must be canonical French INSEE strings")` under lexical guard `any(<br>        _CANONICAL_COMMUNE.fullmatch(value) is None<br>        for value in parcels["commune_code"].tolist()<br>    )`.
  - `ValueError(<br>            "parcel_id must equal commune, prefix, section, and parcel number identity"<br>        )` under lexical guard `not parcels["parcel_id"].equals(expected_ids)`.
  - `ValueError("Normalized Cadastre parcel geometry must be exactly 2D")` under lexical guard `any(bool(value) for value in geometry.loc[non_null].has_z)`.
  - `ValueError("Normalized Cadastre geometry must be Polygon or MultiPolygon")` under lexical guard `unsupported`.
  - `ValueError("geometry_status differs from the actual parcel geometry")` under lexical guard `not recorded_valid.equals(factually_valid)`.
  - `ValueError(<br>            "area_m2 must be numeric and finite and must be a strict positive "<br>            "finite numeric value when geometry_status is VALID"<br>        )` under lexical guard `any(<br>        isinstance(value, bool)<br>        or not isinstance(value, Real)<br>        or not isfinite(float(value))<br>        for value in valid_areas<br>    )`.
  - `ValueError(<br>            "area_m2 must be greater than zero and must be a strict positive "<br>            "finite numeric value when geometry_status is VALID"<br>        )` under lexical guard `any(float(value) <= 0 for value in valid_areas)`.
  - `ValueError("INVALID parcel area_m2 must be null")` under lexical guard `invalid_areas.notna().any()`.
  - `ValueError(<br>                    "VALID parcel area_m2 differs from measured EPSG:2154 geometry area"<br>                )` under lexical guard `recorded_valid.any()`.

**Qualified relationships**

Inbound conservative repository consumers:
- import: `landscout.stages.enrich_shape::<module>` via `from landscout.common.cadastre_contract import validate_normalized_cadastre_parcels`
- direct call: `landscout.stages.enrich_shape::enrich_parcel_shapes` via `validate_normalized_cadastre_parcels`
- value/type reference: `landscout.stages.enrich_shape::enrich_parcel_shapes` via `validate_normalized_cadastre_parcels`
- import: `landscout.stages.filter_parcels::<module>` via `from landscout.common.cadastre_contract import validate_normalized_cadastre_parcels`
- direct call: `landscout.stages.filter_parcels::filter_parcels_by_area` via `validate_normalized_cadastre_parcels`
- value/type reference: `landscout.stages.filter_parcels::filter_parcels_by_area` via `validate_normalized_cadastre_parcels`
- direct call: `landscout.stages.filter_parcels::_validate_shape_filter_input` via `validate_normalized_cadastre_parcels`
- value/type reference: `landscout.stages.filter_parcels::_validate_shape_filter_input` via `validate_normalized_cadastre_parcels`
- import: `landscout.stages.normalize_cadastre::<module>` via `from landscout.common.cadastre_contract import (
    CADASTRE_NORMALIZED_PREFIX,
    validate_normalized_cadastre_parcels,
)`
- direct call: `landscout.stages.normalize_cadastre::normalize_cadastre_parcels` via `validate_normalized_cadastre_parcels`
- value/type reference: `landscout.stages.normalize_cadastre::normalize_cadastre_parcels` via `validate_normalized_cadastre_parcels`
- import: `landscout.stages.profile_shape::<module>` via `from landscout.common.cadastre_contract import validate_normalized_cadastre_parcels`
- direct call: `landscout.stages.profile_shape::profile_shape_distribution` via `validate_normalized_cadastre_parcels`
- value/type reference: `landscout.stages.profile_shape::profile_shape_distribution` via `validate_normalized_cadastre_parcels`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels.columns.duplicated().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels.columns.duplicated` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `CRS.from_user_input` | `pyproj.CRS.from_user_input` |
| `crs.equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `_require_exact_strings` | `landscout.common.cadastre_contract._require_exact_strings` |
| `parcels["parcel_id"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels["parcel_id"].duplicated().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels["parcel_id"].duplicated` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels["commune_code"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `_CANONICAL_COMMUNE.fullmatch` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels[column].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels["section"].str.zfill` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels["parcel_number"].str.zfill` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels["parcel_id"].equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `validate_cadastre_geometry_statuses` | `landscout.common.cadastre_contract.validate_cadastre_geometry_statuses` |
| `parcels["geometry_status"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `bool` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry.loc[non_null].geom_type.dropna` | `unresolved local/third-party receiver; no ownership inferred` |
| `recorded_valid.equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `isfinite` | `math.isfinite` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |
| `invalid_areas.notna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `invalid_areas.notna` | `unresolved local/third-party receiver; no ownership inferred` |
| `recorded_valid.any` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels.loc[recorded_valid].to_crs` | `unresolved local/third-party receiver; no ownership inferred` |
| `zip` | `unresolved local/third-party receiver; no ownership inferred` |
| `max` | `unresolved local/third-party receiver; no ownership inferred` |
| `abs` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `validate_cadastre_geometry_statuses`<br>`parcels["geometry_status"].tolist`<br>`geometry.isna`<br>`geometry.loc[non_null].geom_type.dropna`<br>`parcels.loc[recorded_valid].to_crs` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def validate_normalized_cadastre_parcels(
    parcels: object,
) -> gpd.GeoDataFrame:
    """Validate the canonical normalized Cadastre prefix and cross-field facts."""

    if not isinstance(parcels, gpd.GeoDataFrame):
        raise ValueError(  # noqa: TRY004 - one stable validation-error contract
            "Normalized Cadastre parcels must be a GeoDataFrame"
        )
    if parcels.columns.duplicated().any():
        raise ValueError("Normalized Cadastre parcel columns must be unique")
    if tuple(str(column) for column in parcels.columns[:12]) != (
        CADASTRE_NORMALIZED_PREFIX
    ):
        raise ValueError(
            "Normalized Cadastre parcels must retain the exact canonical column prefix "
            "including parcel_id"
        )
    if parcels.active_geometry_name != "geometry":
        raise ValueError("Normalized Cadastre parcels require active geometry")
    if parcels.crs is None:
        raise ValueError("Normalized Cadastre parcel CRS is required")
    try:
        crs = CRS.from_user_input(parcels.crs)
    except Exception as error:
        raise ValueError("Normalized Cadastre parcel CRS is unreadable") from error
    if not crs.equals(CRS.from_user_input(WGS84)):
        raise ValueError("Normalized Cadastre parcels must use EPSG:4326")

    _require_exact_strings(parcels["parcel_id"].tolist(), "parcel_id")
    if parcels["parcel_id"].duplicated().any():
        raise ValueError("parcel_id values must be unique")
    _require_exact_strings(parcels["commune_code"].tolist(), "commune_code")
    if any(
        _CANONICAL_COMMUNE.fullmatch(value) is None
        for value in parcels["commune_code"].tolist()
    ):
        raise ValueError("commune_code values must be canonical French INSEE strings")
    for column in ("section_prefix", "section", "parcel_number"):
        _require_exact_strings(parcels[column].tolist(), column)
    expected_ids = (
        parcels["commune_code"]
        + parcels["section_prefix"]
        + parcels["section"].str.zfill(2)
        + parcels["parcel_number"].str.zfill(4)
    )
    if not parcels["parcel_id"].equals(expected_ids):
        raise ValueError(
            "parcel_id must equal commune, prefix, section, and parcel number identity"
        )

    validate_cadastre_geometry_statuses(parcels["geometry_status"].tolist())
    geometry = parcels.geometry
    non_null = ~geometry.isna()
    if any(bool(value) for value in geometry.loc[non_null].has_z):
        raise ValueError("Normalized Cadastre parcel geometry must be exactly 2D")
    unsupported = set(geometry.loc[non_null].geom_type.dropna()) - {
        "Polygon",
        "MultiPolygon",
    }
    if unsupported:
        raise ValueError("Normalized Cadastre geometry must be Polygon or MultiPolygon")
    factually_valid = non_null & ~geometry.is_empty & geometry.is_valid
    recorded_valid = parcels["geometry_status"] == "VALID"
    if not recorded_valid.equals(factually_valid):
        raise ValueError("geometry_status differs from the actual parcel geometry")

    valid_areas = parcels.loc[recorded_valid, "area_m2"]
    if any(
        isinstance(value, bool)
        or not isinstance(value, Real)
        or not isfinite(float(value))
        for value in valid_areas
    ):
        raise ValueError(
            "area_m2 must be numeric and finite and must be a strict positive "
            "finite numeric value when geometry_status is VALID"
        )
    if any(float(value) <= 0 for value in valid_areas):
        raise ValueError(
            "area_m2 must be greater than zero and must be a strict positive "
            "finite numeric value when geometry_status is VALID"
        )
    invalid_areas = parcels.loc[~recorded_valid, "area_m2"]
    if invalid_areas.notna().any():
        raise ValueError("INVALID parcel area_m2 must be null")

    if recorded_valid.any():
        measured = parcels.loc[recorded_valid].to_crs(LAMBERT93).geometry.area
        for stored, actual in zip(valid_areas, measured, strict=True):
            tolerance = max(
                CADASTRE_AREA_ABSOLUTE_TOLERANCE_M2,
                abs(float(actual)) * CADASTRE_AREA_RELATIVE_TOLERANCE,
            )
            if abs(float(stored) - float(actual)) > tolerance:
                raise ValueError(
                    "VALID parcel area_m2 differs from measured EPSG:2154 geometry area"
                )
    return parcels
```

**Business boundary**

- This contract validates or represents inputs; it does not rank parcels, combine criteria, or create a legal, access, grid-capacity, environmental, or planning conclusion.


## 7. Validation and data-contract summary

- Canonical schema/mapping declarations inventoried above: none at module scope.
- Exact value/null/index/CRS/geometry/hash behavior is claimed only where the reproduced validators and operations enforce it.

## 8. Public exports and package ownership

This module declares no `__all__`; no package-level public guarantee is inferred from direct importability alone.

## 9. Trust, provenance, side effects, and business boundary

- This contract validates or represents inputs; it does not rank parcels, combine criteria, or create a legal, access, grid-capacity, environmental, or planning conclusion.
- Configured identity, textual lineage, byte identity, physical source reconstruction, local envelope validation, and source-complete validation remain distinct trust levels. This companion attributes only the levels implemented in the exact source.
- Filesystem, network, hashing, CRS/geometry, process, mutation, and expected-exception evidence is listed per callable; an empty category is not silently promoted to an effect.

## 10. Change impact

A source-byte change invalidates the SHA above and requires re-auditing imports/re-exports, constants/aliases/schemas, model fields/immutability, qualified callers, side effects, controlled errors, tests, source/artifact locks, and the exact full snapshot.

## 11. Exact complete current file content

The following UTF-8 snapshot is the complete current repository file, not an excerpt. Its raw-byte SHA256 is the value in **File identity**.

```python
"""Internal contracts shared by normalized cadastral stages."""

import re
from collections.abc import Iterable
from math import isfinite
from numbers import Real

import geopandas as gpd  # type: ignore[import-untyped]
import pandas as pd  # type: ignore[import-untyped]
from pyproj import CRS

from landscout.geo.crs import LAMBERT93, WGS84

CADASTRE_GEOMETRY_STATUSES = frozenset({"VALID", "INVALID"})
CADASTRE_NORMALIZED_PREFIX = (
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
)
CADASTRE_AREA_ABSOLUTE_TOLERANCE_M2 = 1e-6
CADASTRE_AREA_RELATIVE_TOLERANCE = 1e-12
_CANONICAL_COMMUNE = re.compile(r"^(?:\d{5}|2[AB]\d{3})$")


def validate_cadastre_geometry_statuses(values: Iterable[object]) -> None:
    """Require the exact geometry-status vocabulary emitted by normalization."""

    if any(
        type(value) is not str or value not in CADASTRE_GEOMETRY_STATUSES
        for value in values
    ):
        raise ValueError(
            "geometry_status must contain only exact VALID or INVALID strings"
        )


def _require_exact_strings(values: Iterable[object], label: str) -> None:
    items = tuple(values)
    if any(bool(pd.isna(value)) for value in items):
        raise ValueError(f"{label} values must not be null")
    if any(
        type(value) is not str or not value or value != value.strip() for value in items
    ):
        raise ValueError(f"{label} values must be exact non-empty strings")


def validate_normalized_cadastre_parcels(
    parcels: object,
) -> gpd.GeoDataFrame:
    """Validate the canonical normalized Cadastre prefix and cross-field facts."""

    if not isinstance(parcels, gpd.GeoDataFrame):
        raise ValueError(  # noqa: TRY004 - one stable validation-error contract
            "Normalized Cadastre parcels must be a GeoDataFrame"
        )
    if parcels.columns.duplicated().any():
        raise ValueError("Normalized Cadastre parcel columns must be unique")
    if tuple(str(column) for column in parcels.columns[:12]) != (
        CADASTRE_NORMALIZED_PREFIX
    ):
        raise ValueError(
            "Normalized Cadastre parcels must retain the exact canonical column prefix "
            "including parcel_id"
        )
    if parcels.active_geometry_name != "geometry":
        raise ValueError("Normalized Cadastre parcels require active geometry")
    if parcels.crs is None:
        raise ValueError("Normalized Cadastre parcel CRS is required")
    try:
        crs = CRS.from_user_input(parcels.crs)
    except Exception as error:
        raise ValueError("Normalized Cadastre parcel CRS is unreadable") from error
    if not crs.equals(CRS.from_user_input(WGS84)):
        raise ValueError("Normalized Cadastre parcels must use EPSG:4326")

    _require_exact_strings(parcels["parcel_id"].tolist(), "parcel_id")
    if parcels["parcel_id"].duplicated().any():
        raise ValueError("parcel_id values must be unique")
    _require_exact_strings(parcels["commune_code"].tolist(), "commune_code")
    if any(
        _CANONICAL_COMMUNE.fullmatch(value) is None
        for value in parcels["commune_code"].tolist()
    ):
        raise ValueError("commune_code values must be canonical French INSEE strings")
    for column in ("section_prefix", "section", "parcel_number"):
        _require_exact_strings(parcels[column].tolist(), column)
    expected_ids = (
        parcels["commune_code"]
        + parcels["section_prefix"]
        + parcels["section"].str.zfill(2)
        + parcels["parcel_number"].str.zfill(4)
    )
    if not parcels["parcel_id"].equals(expected_ids):
        raise ValueError(
            "parcel_id must equal commune, prefix, section, and parcel number identity"
        )

    validate_cadastre_geometry_statuses(parcels["geometry_status"].tolist())
    geometry = parcels.geometry
    non_null = ~geometry.isna()
    if any(bool(value) for value in geometry.loc[non_null].has_z):
        raise ValueError("Normalized Cadastre parcel geometry must be exactly 2D")
    unsupported = set(geometry.loc[non_null].geom_type.dropna()) - {
        "Polygon",
        "MultiPolygon",
    }
    if unsupported:
        raise ValueError("Normalized Cadastre geometry must be Polygon or MultiPolygon")
    factually_valid = non_null & ~geometry.is_empty & geometry.is_valid
    recorded_valid = parcels["geometry_status"] == "VALID"
    if not recorded_valid.equals(factually_valid):
        raise ValueError("geometry_status differs from the actual parcel geometry")

    valid_areas = parcels.loc[recorded_valid, "area_m2"]
    if any(
        isinstance(value, bool)
        or not isinstance(value, Real)
        or not isfinite(float(value))
        for value in valid_areas
    ):
        raise ValueError(
            "area_m2 must be numeric and finite and must be a strict positive "
            "finite numeric value when geometry_status is VALID"
        )
    if any(float(value) <= 0 for value in valid_areas):
        raise ValueError(
            "area_m2 must be greater than zero and must be a strict positive "
            "finite numeric value when geometry_status is VALID"
        )
    invalid_areas = parcels.loc[~recorded_valid, "area_m2"]
    if invalid_areas.notna().any():
        raise ValueError("INVALID parcel area_m2 must be null")

    if recorded_valid.any():
        measured = parcels.loc[recorded_valid].to_crs(LAMBERT93).geometry.area
        for stored, actual in zip(valid_areas, measured, strict=True):
            tolerance = max(
                CADASTRE_AREA_ABSOLUTE_TOLERANCE_M2,
                abs(float(actual)) * CADASTRE_AREA_RELATIVE_TOLERANCE,
            )
            if abs(float(stored) - float(actual)) > tolerance:
                raise ValueError(
                    "VALID parcel area_m2 differs from measured EPSG:2154 geometry area"
                )
    return parcels
```

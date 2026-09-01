# `tests/unit/test_normalize_access_ign.py`

## File identity

- Repository path: `tests/unit/test_normalize_access_ign.py`
- File type: Python source
- Layer: unit/regression test
- Domain: isolated contract test evidence
- Responsibility: Provides complete unit and regression coverage for the `normalize_access_ign` contracts exercised in this file.
- Source SHA256: `2cbb2d2b2664f861fd36f81be31e0af2903b93c06dde70e5ce22fcadc5994adf`

## 1. STEP 7F.1A.4 contract delta

- Refreshes permanent STEP 7F.1A.4 regression coverage for normalize access ign; the exact fixtures, mutations, calls, controlled failures, and assertions are inventoried below.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Provides complete unit and regression coverage for the `normalize_access_ign` contracts exercised in this file.

The file belongs to the **unit/regression test** layer and **isolated contract test evidence** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `import json`
- `import tempfile`
- `from copy import deepcopy`
- `from dataclasses import replace`
- `from hashlib import sha256`
- `from pathlib import Path`
- `from typing import Any, cast`
- `from uuid import uuid4`

### Third-party packages

- `import geopandas as gpd`
- `import pandas as pd`
- `import pyogrio`
- `import pytest`
- `from geopandas.testing import assert_geodataframe_equal`
- `from shapely.geometry import LineString, MultiLineString, Point, Polygon`

### Internal LandScout imports

- `import landscout.stages.normalize_access_ign as road_normalization`
- `from landscout import stages`
- `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
)`
- `from landscout.stages.normalize_access_ign import (
    IgnRoadNormalizationError,
    NormalizedIgnRoadData,
    normalize_ign_roads,
)`
- `import landscout.stages.normalize_access_ign as access_normalization`

## 4. Contract taxonomy

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `ROAD_LAYER`

- Category: module constant or closed domain.
- Exact declaration:

```python
ROAD_LAYER = "troncon_de_route"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `ALTERNATE_ROAD_LAYER`

- Category: module constant or closed domain.
- Exact declaration:

```python
ALTERNATE_ROAD_LAYER = "voie_secondaire"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `DEPARTMENT_LAYER`

- Category: module constant or closed domain.
- Exact declaration:

```python
DEPARTMENT_LAYER = "departement"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `ARCHIVE_SHA256`

- Category: module constant or closed domain.
- Exact declaration:

```python
ARCHIVE_SHA256 = "a" * 64
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `SOURCE_URL`

- Category: module constant or closed domain.
- Exact declaration:

```python
SOURCE_URL = "https://example.test/BDTOPO_D031.7z"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_FIXTURE_ROOT`

- Category: module constant or closed domain.
- Exact declaration:

```python
_FIXTURE_ROOT = Path(tempfile.mkdtemp(prefix="landscout-road-ign-"))
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_SOURCE_CONFIG_PAYLOAD`

- Category: module constant or closed domain.
- Exact declaration:

```python
_SOURCE_CONFIG_PAYLOAD = load_ign_bdtopo_source_config().model_dump(mode="json")
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `SOURCE_CONFIG`

- Category: module constant or closed domain.
- Exact declaration:

```python
SOURCE_CONFIG = IgnBdTopoSourceConfig.model_validate(_SOURCE_CONFIG_PAYLOAD)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `OUTPUT_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
OUTPUT_COLUMNS = (
    "road_feature_id",
    "road_feature_type",
    "source_provider",
    "source_product",
    "source_layer",
    "source_feature_id",
    "source_department_code",
    "source_edition",
    "source_product_version",
    "source_download_timestamp",
    "source_archive_sha256",
    "source_url",
    "nature_raw",
    "importance_raw",
    "fictitious_raw",
    "position_relative_to_ground_raw",
    "asset_status_raw",
    "lane_count_raw",
    "carriageway_width_raw",
    "private_raw",
    "traffic_direction_raw",
    "urban_raw",
    "mean_light_vehicle_speed_raw",
    "light_vehicle_access_raw",
    "closure_period_raw",
    "restriction_nature_raw",
    "restriction_height_raw",
    "restriction_total_weight_raw",
    "restriction_axle_weight_raw",
    "restriction_width_raw",
    "restriction_length_raw",
    "dangerous_goods_forbidden_raw",
    "administrative_classification_raw",
    "manager_raw",
    "source_name_raw",
    "source_identifiers_raw",
    "source_created_at",
    "source_modified_at",
    "source_confirmed_at",
    "planimetric_acquisition_method",
    "planimetric_precision_raw",
    "spatial_role",
    "geometry_status",
    "geometry",
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `road_feature_id`
  - `road_feature_type`
  - `source_provider`
  - `source_product`
  - `source_layer`
  - `source_feature_id`
  - `source_department_code`
  - `source_edition`
  - `source_product_version`
  - `source_download_timestamp`
  - `source_archive_sha256`
  - `source_url`
  - `nature_raw`
  - `importance_raw`
  - `fictitious_raw`
  - `position_relative_to_ground_raw`
  - `asset_status_raw`
  - `lane_count_raw`
  - `carriageway_width_raw`
  - `private_raw`
  - `traffic_direction_raw`
  - `urban_raw`
  - `mean_light_vehicle_speed_raw`
  - `light_vehicle_access_raw`
  - `closure_period_raw`
  - `restriction_nature_raw`
  - `restriction_height_raw`
  - `restriction_total_weight_raw`
  - `restriction_axle_weight_raw`
  - `restriction_width_raw`
  - `restriction_length_raw`
  - `dangerous_goods_forbidden_raw`
  - `administrative_classification_raw`
  - `manager_raw`
  - `source_name_raw`
  - `source_identifiers_raw`
  - `source_created_at`
  - `source_modified_at`
  - `source_confirmed_at`
  - `planimetric_acquisition_method`
  - `planimetric_precision_raw`
  - `spatial_role`
  - `geometry_status`
  - `geometry`

### `RAW_FIELD_MAPPING`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
RAW_FIELD_MAPPING = (
    ("nature", "nature_raw"),
    ("importance", "importance_raw"),
    ("fictif", "fictitious_raw"),
    ("position_par_rapport_au_sol", "position_relative_to_ground_raw"),
    ("etat_de_l_objet", "asset_status_raw"),
    ("nombre_de_voies", "lane_count_raw"),
    ("largeur_de_chaussee", "carriageway_width_raw"),
    ("prive", "private_raw"),
    ("sens_de_circulation", "traffic_direction_raw"),
    ("urbain", "urban_raw"),
    ("vitesse_moyenne_vl", "mean_light_vehicle_speed_raw"),
    ("acces_vehicule_leger", "light_vehicle_access_raw"),
    ("periode_de_fermeture", "closure_period_raw"),
    ("nature_de_la_restriction", "restriction_nature_raw"),
    ("restriction_de_hauteur", "restriction_height_raw"),
    ("restriction_de_poids_total", "restriction_total_weight_raw"),
    ("restriction_de_poids_par_essieu", "restriction_axle_weight_raw"),
    ("restriction_de_largeur", "restriction_width_raw"),
    ("restriction_de_longueur", "restriction_length_raw"),
    ("matieres_dangereuses_interdites", "dangerous_goods_forbidden_raw"),
    ("cpx_classement_administratif", "administrative_classification_raw"),
    ("cpx_gestionnaire", "manager_raw"),
    ("sources", "source_name_raw"),
    ("identifiants_sources", "source_identifiers_raw"),
    ("date_creation", "source_created_at"),
    ("date_modification", "source_modified_at"),
    ("date_de_confirmation", "source_confirmed_at"),
    ("methode_d_acquisition_planimetrique", "planimetric_acquisition_method"),
    ("precision_planimetrique", "planimetric_precision_raw"),
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.


### Executable module-import-time statements

### Module-import-time executable statement at line 43

- Category: executable import-time registration/guard/statement; it is not a constant or function-local side effect.
- Exact call expressions: `_SOURCE_CONFIG_PAYLOAD.update`.
- Exact statement:

```python
_SOURCE_CONFIG_PAYLOAD.update(
    {
        "source_url": SOURCE_URL,
        "checksum_url": None,
        "official_checksum_algorithm": None,
        "official_checksum": None,
        "expected_archive_size_bytes": 1234,
    }
)
```


## 5. Classes, models, dataclasses, and fields

No top-level class/model/dataclass is declared.

## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `_road_frame`

**Purpose:** Implements `road frame` within the file role: Provides complete unit and regression coverage for the `normalize_access_ign` contracts exercised in this file.

**Exact signature**

```python
def _road_frame(
    geometries: list[object] | None = None,
    *,
    identifiers: list[object] | None = None,
    crs: str | None = "EPSG:2154",
    index: list[object] | None = None,
) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `geometries` | positional-or-keyword | `list[object] \| None` | `None` |
| `identifiers` | keyword-only | `list[object] \| None` | `None` |
| `crs` | keyword-only | `str \| None` | `'EPSG:2154'` |
| `index` | keyword-only | `list[object] \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `gpd.GeoDataFrame(<br>        values,<br>        geometry=source_geometries,<br>        crs=crs,<br>        index=source_index,<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_normalize_access_ign::_source` via `_road_frame`
- value/type reference: `tests.unit.test_normalize_access_ign::_source` via `_road_frame`
- direct call: `tests.unit.test_normalize_access_ign::_with_alternate_road_layer` via `_road_frame`
- value/type reference: `tests.unit.test_normalize_access_ign::_with_alternate_road_layer` via `_road_frame`
- direct call: `tests.unit.test_normalize_access_ign::test_valid_multilinestring_is_preserved` via `_road_frame`
- value/type reference: `tests.unit.test_normalize_access_ign::test_valid_multilinestring_is_preserved` via `_road_frame`
- direct call: `tests.unit.test_normalize_access_ign::test_z_coordinates_are_preserved_exactly` via `_road_frame`
- value/type reference: `tests.unit.test_normalize_access_ign::test_z_coordinates_are_preserved_exactly` via `_road_frame`
- direct call: `tests.unit.test_normalize_access_ign::test_row_count_order_geometry_and_range_index_are_preserved` via `_road_frame`
- value/type reference: `tests.unit.test_normalize_access_ign::test_row_count_order_geometry_and_range_index_are_preserved` via `_road_frame`
- direct call: `tests.unit.test_normalize_access_ign::test_raw_access_and_restriction_values_are_copied_without_interpretation` via `_road_frame`
- value/type reference: `tests.unit.test_normalize_access_ign::test_raw_access_and_restriction_values_are_copied_without_interpretation` via `_road_frame`
- direct call: `tests.unit.test_normalize_access_ign::test_null_or_empty_cleabs_is_rejected` via `_road_frame`
- value/type reference: `tests.unit.test_normalize_access_ign::test_null_or_empty_cleabs_is_rejected` via `_road_frame`
- direct call: `tests.unit.test_normalize_access_ign::test_unsafe_cleabs_is_rejected` via `_road_frame`
- value/type reference: `tests.unit.test_normalize_access_ign::test_unsafe_cleabs_is_rejected` via `_road_frame`
- direct call: `tests.unit.test_normalize_access_ign::test_duplicate_cleabs_is_rejected` via `_road_frame`
- value/type reference: `tests.unit.test_normalize_access_ign::test_duplicate_cleabs_is_rejected` via `_road_frame`
- direct call: `tests.unit.test_normalize_access_ign::test_wrong_or_missing_road_crs_is_rejected` via `_road_frame`
- value/type reference: `tests.unit.test_normalize_access_ign::test_wrong_or_missing_road_crs_is_rejected` via `_road_frame`
- direct call: `tests.unit.test_normalize_access_ign::test_valid_unsupported_geometry_type_is_rejected` via `_road_frame`
- value/type reference: `tests.unit.test_normalize_access_ign::test_valid_unsupported_geometry_type_is_rejected` via `_road_frame`
- direct call: `tests.unit.test_normalize_access_ign::test_null_empty_and_invalid_geometry_are_preserved_with_status` via `_road_frame`
- value/type reference: `tests.unit.test_normalize_access_ign::test_null_empty_and_invalid_geometry_are_preserved_with_status` via `_road_frame`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `LineString` | `shapely.geometry.LineString` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `range` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.Timestamp` | `pandas.Timestamp` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |

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
def _road_frame(
    geometries: list[object] | None = None,
    *,
    identifiers: list[object] | None = None,
    crs: str | None = "EPSG:2154",
    index: list[object] | None = None,
) -> gpd.GeoDataFrame:
    source_geometries = geometries or [LineString([(0, 0), (100, 100)])]
    count = len(source_geometries)
    source_ids = identifiers or [f"ROAD-{number + 1}" for number in range(count)]
    source_index = index or [100 + number for number in range(count)]
    values: dict[str, list[object]] = {
        "cleabs": source_ids,
        "nature": ["Route à 1 chaussée"] * count,
        "importance": ["2"] * count,
        "fictif": ["Non"] * count,
        "position_par_rapport_au_sol": [-1] * count,
        "etat_de_l_objet": ["En service"] * count,
        "nombre_de_voies": [2] * count,
        "largeur_de_chaussee": [7.5] * count,
        "prive": ["Non"] * count,
        "sens_de_circulation": ["Double sens"] * count,
        "urbain": ["Non"] * count,
        "vitesse_moyenne_vl": [80] * count,
        "acces_vehicule_leger": ["Libre"] * count,
        "periode_de_fermeture": [None] * count,
        "nature_de_la_restriction": ["Poids total"] * count,
        "restriction_de_hauteur": [4.2] * count,
        "restriction_de_poids_total": [19.0] * count,
        "restriction_de_poids_par_essieu": [11.5] * count,
        "restriction_de_largeur": [3.2] * count,
        "restriction_de_longueur": [18.0] * count,
        "matieres_dangereuses_interdites": ["Oui"] * count,
        "cpx_classement_administratif": ["Départementale"] * count,
        "cpx_gestionnaire": ["CD31"] * count,
        "sources": ["IGN 2026"] * count,
        "identifiants_sources": ["source-road-id"] * count,
        "date_creation": [pd.Timestamp("2024-01-01", tz="UTC")] * count,
        "date_modification": [pd.Timestamp("2025-01-01", tz="UTC")] * count,
        "date_de_confirmation": [pd.Timestamp("2025-06-01", tz="UTC")] * count,
        "methode_d_acquisition_planimetrique": ["Photogrammétrie"] * count,
        "precision_planimetrique": [2.5] * count,
    }
    return gpd.GeoDataFrame(
        values,
        geometry=source_geometries,
        crs=crs,
        index=source_index,
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_summary`

**Purpose:** Implements `summary` within the file role: Provides complete unit and regression coverage for the `normalize_access_ign` contracts exercised in this file.

**Exact signature**

```python
def _summary(
    frame: gpd.GeoDataFrame,
    *,
    layer: str = ROAD_LAYER,
) -> IgnBdTopoLayerSummary:
```

- Exact decorators: none.
- Declared return annotation: `IgnBdTopoLayerSummary`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `layer` | keyword-only | `str` | `ROAD_LAYER` |

**Return and exception contract**

- Exact observed return expressions:
  - `IgnBdTopoLayerSummary(<br>        logical_name="road_segments",<br>        source_layer_name=layer,<br>        crs=str(frame.crs),<br>        feature_count=len(frame),<br>        columns=tuple(str(column) for column in frame.columns),<br>        dtypes=tuple(<br>            (str(column), str(dtype)) for column, dtype in frame.dtypes.items()<br>        ),<br>        null_geometry_count=int(null_mask.sum()),<br>        empty_geometry_count=int(empty_mask.sum()),<br>        invalid_geometry_count=int(invalid_mask.sum()),<br>        geometry_types=tuple(<br>            sorted(<br>                str(value) for value in geometry[~null_mask].geom_type.dropna().unique()<br>            )<br>        ),<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_normalize_access_ign::_source` via `_summary`
- value/type reference: `tests.unit.test_normalize_access_ign::_source` via `_summary`
- direct call: `tests.unit.test_normalize_access_ign::_with_alternate_road_layer` via `_summary`
- value/type reference: `tests.unit.test_normalize_access_ign::_with_alternate_road_layer` via `_summary`
- direct call: `tests.unit.test_normalize_access_ign::test_high_level_rejects_coordinated_road_frame_and_summary_forgery` via `_summary`
- value/type reference: `tests.unit.test_normalize_access_ign::test_high_level_rejects_coordinated_road_frame_and_summary_forgery` via `_summary`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `geometry.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoLayerSummary` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoLayerSummary` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.dtypes.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `int` | `unresolved local/third-party receiver; no ownership inferred` |
| `null_mask.sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `empty_mask.sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `invalid_mask.sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry[~null_mask].geom_type.dropna().unique` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry[~null_mask].geom_type.dropna` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `geometry.isna`<br>`geometry[~null_mask].geom_type.dropna().unique`<br>`geometry[~null_mask].geom_type.dropna` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _summary(
    frame: gpd.GeoDataFrame,
    *,
    layer: str = ROAD_LAYER,
) -> IgnBdTopoLayerSummary:
    geometry = frame.geometry
    null_mask = geometry.isna()
    empty_mask = ~null_mask & geometry.is_empty
    invalid_mask = ~null_mask & ~geometry.is_empty & ~geometry.is_valid
    return IgnBdTopoLayerSummary(
        logical_name="road_segments",
        source_layer_name=layer,
        crs=str(frame.crs),
        feature_count=len(frame),
        columns=tuple(str(column) for column in frame.columns),
        dtypes=tuple(
            (str(column), str(dtype)) for column, dtype in frame.dtypes.items()
        ),
        null_geometry_count=int(null_mask.sum()),
        empty_geometry_count=int(empty_mask.sum()),
        invalid_geometry_count=int(invalid_mask.sum()),
        geometry_types=tuple(
            sorted(
                str(value) for value in geometry[~null_mask].geom_type.dropna().unique()
            )
        ),
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_source`

**Purpose:** Implements `source` within the file role: Provides complete unit and regression coverage for the `normalize_access_ign` contracts exercised in this file.

**Exact signature**

```python
def _source(frame: gpd.GeoDataFrame | None = None) -> IgnBdTopoRoadData:
```

- Exact decorators: none.
- Declared return annotation: `IgnBdTopoRoadData`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame` | positional-or-keyword | `gpd.GeoDataFrame \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `IgnBdTopoRoadData(<br>        extraction=extraction,<br>        road_segments=road_frame,<br>        road_segments_summary=_summary(road_frame),<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_normalize_access_ign::test_road_normalization_reproduces_configured_logical_layer` via `_source`
- value/type reference: `tests.unit.test_normalize_access_ign::test_road_normalization_reproduces_configured_logical_layer` via `_source`
- direct call: `tests.unit.test_normalize_access_ign::test_valid_linestring_normalization_has_exact_schema_identity_and_lineage` via `_source`
- value/type reference: `tests.unit.test_normalize_access_ign::test_valid_linestring_normalization_has_exact_schema_identity_and_lineage` via `_source`
- direct call: `tests.unit.test_normalize_access_ign::test_valid_multilinestring_is_preserved` via `_source`
- value/type reference: `tests.unit.test_normalize_access_ign::test_valid_multilinestring_is_preserved` via `_source`
- direct call: `tests.unit.test_normalize_access_ign::test_z_coordinates_are_preserved_exactly` via `_source`
- value/type reference: `tests.unit.test_normalize_access_ign::test_z_coordinates_are_preserved_exactly` via `_source`
- direct call: `tests.unit.test_normalize_access_ign::test_row_count_order_geometry_and_range_index_are_preserved` via `_source`
- value/type reference: `tests.unit.test_normalize_access_ign::test_row_count_order_geometry_and_range_index_are_preserved` via `_source`
- direct call: `tests.unit.test_normalize_access_ign::test_raw_access_and_restriction_values_are_copied_without_interpretation` via `_source`
- value/type reference: `tests.unit.test_normalize_access_ign::test_raw_access_and_restriction_values_are_copied_without_interpretation` via `_source`
- direct call: `tests.unit.test_normalize_access_ign::test_every_raw_field_preserves_source_values_nulls_and_dtype` via `_source`
- value/type reference: `tests.unit.test_normalize_access_ign::test_every_raw_field_preserves_source_values_nulls_and_dtype` via `_source`
- direct call: `tests.unit.test_normalize_access_ign::test_missing_required_source_field_is_rejected` via `_source`
- value/type reference: `tests.unit.test_normalize_access_ign::test_missing_required_source_field_is_rejected` via `_source`
- direct call: `tests.unit.test_normalize_access_ign::test_null_or_empty_cleabs_is_rejected` via `_source`
- value/type reference: `tests.unit.test_normalize_access_ign::test_null_or_empty_cleabs_is_rejected` via `_source`
- direct call: `tests.unit.test_normalize_access_ign::test_unsafe_cleabs_is_rejected` via `_source`
- value/type reference: `tests.unit.test_normalize_access_ign::test_unsafe_cleabs_is_rejected` via `_source`
- direct call: `tests.unit.test_normalize_access_ign::test_duplicate_cleabs_is_rejected` via `_source`
- value/type reference: `tests.unit.test_normalize_access_ign::test_duplicate_cleabs_is_rejected` via `_source`
- direct call: `tests.unit.test_normalize_access_ign::test_wrong_or_missing_road_crs_is_rejected` via `_source`
- value/type reference: `tests.unit.test_normalize_access_ign::test_wrong_or_missing_road_crs_is_rejected` via `_source`
- direct call: `tests.unit.test_normalize_access_ign::test_wrong_archive_identity_is_rejected` via `_source`
- value/type reference: `tests.unit.test_normalize_access_ign::test_wrong_archive_identity_is_rejected` via `_source`
- direct call: `tests.unit.test_normalize_access_ign::test_wrong_source_spatial_role_is_rejected` via `_source`
- value/type reference: `tests.unit.test_normalize_access_ign::test_wrong_source_spatial_role_is_rejected` via `_source`
- direct call: `tests.unit.test_normalize_access_ign::test_summary_row_count_mismatch_is_rejected` via `_source`
- value/type reference: `tests.unit.test_normalize_access_ign::test_summary_row_count_mismatch_is_rejected` via `_source`
- direct call: `tests.unit.test_normalize_access_ign::test_road_summary_requires_strict_structural_types` via `_source`
- value/type reference: `tests.unit.test_normalize_access_ign::test_road_summary_requires_strict_structural_types` via `_source`
- direct call: `tests.unit.test_normalize_access_ign::test_road_archive_sha256_requires_canonical_lowercase` via `_source`
- value/type reference: `tests.unit.test_normalize_access_ign::test_road_archive_sha256_requires_canonical_lowercase` via `_source`
- direct call: `tests.unit.test_normalize_access_ign::test_summary_crs_mismatch_is_rejected` via `_source`
- value/type reference: `tests.unit.test_normalize_access_ign::test_summary_crs_mismatch_is_rejected` via `_source`
- direct call: `tests.unit.test_normalize_access_ign::test_forged_ordered_summary_schema_is_rejected` via `_source`
- value/type reference: `tests.unit.test_normalize_access_ign::test_forged_ordered_summary_schema_is_rejected` via `_source`
- direct call: `tests.unit.test_normalize_access_ign::test_road_source_rejects_physical_role_collision` via `_source`
- value/type reference: `tests.unit.test_normalize_access_ign::test_road_source_rejects_physical_role_collision` via `_source`
- direct call: `tests.unit.test_normalize_access_ign::test_road_source_rejects_duplicate_layer_inventory` via `_source`
- value/type reference: `tests.unit.test_normalize_access_ign::test_road_source_rejects_duplicate_layer_inventory` via `_source`
- direct call: `tests.unit.test_normalize_access_ign::test_summary_geometry_facts_mismatch_is_rejected` via `_source`
- value/type reference: `tests.unit.test_normalize_access_ign::test_summary_geometry_facts_mismatch_is_rejected` via `_source`
- direct call: `tests.unit.test_normalize_access_ign::test_summary_layer_must_exist_in_extraction_inventory` via `_source`
- value/type reference: `tests.unit.test_normalize_access_ign::test_summary_layer_must_exist_in_extraction_inventory` via `_source`
- direct call: `tests.unit.test_normalize_access_ign::test_summary_layer_and_logical_name_must_be_exact` via `_source`
- value/type reference: `tests.unit.test_normalize_access_ign::test_summary_layer_and_logical_name_must_be_exact` via `_source`
- direct call: `tests.unit.test_normalize_access_ign::test_valid_unsupported_geometry_type_is_rejected` via `_source`
- value/type reference: `tests.unit.test_normalize_access_ign::test_valid_unsupported_geometry_type_is_rejected` via `_source`
- direct call: `tests.unit.test_normalize_access_ign::test_null_empty_and_invalid_geometry_are_preserved_with_status` via `_source`
- value/type reference: `tests.unit.test_normalize_access_ign::test_null_empty_and_invalid_geometry_are_preserved_with_status` via `_source`
- direct call: `tests.unit.test_normalize_access_ign::test_normalization_does_not_mutate_input` via `_source`
- value/type reference: `tests.unit.test_normalize_access_ign::test_normalization_does_not_mutate_input` via `_source`
- direct call: `tests.unit.test_normalize_access_ign::test_road_normalization_uses_distinct_fresh_revalidated_frame` via `_source`
- value/type reference: `tests.unit.test_normalize_access_ign::test_road_normalization_uses_distinct_fresh_revalidated_frame` via `_source`
- direct call: `tests.unit.test_normalize_access_ign::test_high_level_rejects_coordinated_road_frame_and_summary_forgery` via `_source`
- value/type reference: `tests.unit.test_normalize_access_ign::test_high_level_rejects_coordinated_road_frame_and_summary_forgery` via `_source`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_road_frame` | `tests.unit.test_normalize_access_ign._road_frame` |
| `uuid4` | `uuid.uuid4` |
| `extraction_path.mkdir` | `unresolved local/third-party receiver; no ownership inferred` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `LineString` | `shapely.geometry.LineString` |
| `pyogrio.write_dataframe` | `pyogrio.write_dataframe` |
| `Polygon` | `shapely.geometry.Polygon` |
| `gpd.read_file` | `geopandas.read_file` |
| `geopackage_path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `pyogrio.list_layers` | `pyogrio.list_layers` |
| `sha256(payload).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |
| `(extraction_path / ".landscout-extraction.json").write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoDownload` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoDownload` |
| `Path` | `pathlib.Path` |
| `IgnBdTopoExtraction` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoExtraction` |
| `IgnBdTopoRoadData` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoRoadData` |
| `_summary` | `tests.unit.test_normalize_access_ign._summary` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `gpd.read_file`<br>`geopackage_path.read_bytes` |
| Filesystem/archive write or publication | `extraction_path.mkdir`<br>`(extraction_path / ".landscout-extraction.json").write_text` |
| Hashing/byte identity | `sha256(payload).hexdigest`<br>`sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _source(frame: gpd.GeoDataFrame | None = None) -> IgnBdTopoRoadData:
    road_frame = frame if frame is not None else _road_frame()
    extraction_path = _FIXTURE_ROOT / uuid4().hex
    extraction_path.mkdir(parents=True)
    geopackage_path = extraction_path / "data.gpkg"
    crs = road_frame.crs or "EPSG:2154"
    dummy = gpd.GeoDataFrame(
        {"id": ["dummy"]},
        geometry=[LineString([(0, 0), (1, 1)])],
        crs=crs,
    )
    pyogrio.write_dataframe(
        dummy, geopackage_path, layer="ligne_electrique", driver="GPKG"
    )
    pyogrio.write_dataframe(
        dummy,
        geopackage_path,
        layer="poste_de_transformation",
        driver="GPKG",
        append=True,
    )
    pyogrio.write_dataframe(
        road_frame,
        geopackage_path,
        layer=ROAD_LAYER,
        driver="GPKG",
        append=True,
    )
    pyogrio.write_dataframe(
        gpd.GeoDataFrame(
            {"code_insee": ["31"]},
            geometry=[Polygon([(0, 0), (0, 10), (10, 10), (10, 0)])],
            crs="EPSG:2154",
        ),
        geopackage_path,
        layer=DEPARTMENT_LAYER,
        driver="GPKG",
        append=True,
    )
    road_frame = gpd.read_file(geopackage_path, layer=ROAD_LAYER, engine="pyogrio")
    payload = geopackage_path.read_bytes()
    layer_names = tuple(str(row[0]) for row in pyogrio.list_layers(geopackage_path))
    digest = sha256(payload).hexdigest()
    (extraction_path / ".landscout-extraction.json").write_text(
        json.dumps(
            {
                "schema_version": 3,
                "archive_sha256": ARCHIVE_SHA256,
                "geopackage_relative_path": "data.gpkg",
                "geopackage_size_bytes": len(payload),
                "geopackage_sha256": digest,
                "all_layer_names": list(layer_names),
                "electric_lines_layer": "ligne_electrique",
                "transformation_posts_layer": "poste_de_transformation",
                "road_segments_layer": ROAD_LAYER,
                "department_layer": DEPARTMENT_LAYER,
                "extracted_entries": [
                    {
                        "relative_path": "data.gpkg",
                        "kind": "file",
                        "size_bytes": len(payload),
                        "sha256": digest,
                    }
                ],
                "spatial_role": "PROXY_GEOMETRY",
            }
        ),
        encoding="utf-8",
    )
    archive = IgnBdTopoDownload(
        provider=SOURCE_CONFIG.provider,
        product="BD TOPO",
        department_code="31",
        edition="2026-06-15",
        product_version="3.5",
        projection="EPSG:2154",
        package_format="GPKG",
        archive_format="7z",
        source_url=SOURCE_URL,
        checksum_url=None,
        download_timestamp="2026-08-11T15:32:03+00:00",
        filename="BDTOPO_D031.7z",
        file_size=1234,
        sha256=ARCHIVE_SHA256,
        official_checksum_algorithm=None,
        official_checksum=None,
        official_checksum_validated=False,
        path=Path("cache/BDTOPO_D031.7z"),
        cache_hit=True,
    )
    extraction = IgnBdTopoExtraction(
        archive=archive,
        extraction_path=extraction_path,
        geopackage_path=geopackage_path,
        geopackage_filename="data.gpkg",
        geopackage_size_bytes=len(payload),
        geopackage_sha256=digest,
        all_layer_names=layer_names,
        electric_lines_layer="ligne_electrique",
        transformation_posts_layer="poste_de_transformation",
        road_segments_layer=ROAD_LAYER,
        department_layer=DEPARTMENT_LAYER,
        cache_hit=True,
    )
    return IgnBdTopoRoadData(
        extraction=extraction,
        road_segments=road_frame,
        road_segments_summary=_summary(road_frame),
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_with_alternate_road_layer`

**Purpose:** Implements `with alternate road layer` within the file role: Provides complete unit and regression coverage for the `normalize_access_ign` contracts exercised in this file.

**Exact signature**

```python
def _with_alternate_road_layer(
    source: IgnBdTopoRoadData,
) -> tuple[IgnBdTopoRoadData, IgnBdTopoRoadData]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[IgnBdTopoRoadData, IgnBdTopoRoadData]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source` | positional-or-keyword | `IgnBdTopoRoadData` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `configured, forged`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_normalize_access_ign::test_road_normalization_reproduces_configured_logical_layer` via `_with_alternate_road_layer`
- value/type reference: `tests.unit.test_normalize_access_ign::test_road_normalization_reproduces_configured_logical_layer` via `_with_alternate_road_layer`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_road_frame` | `tests.unit.test_normalize_access_ign._road_frame` |
| `LineString` | `shapely.geometry.LineString` |
| `pyogrio.write_dataframe` | `pyogrio.write_dataframe` |
| `geopackage_path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `pyogrio.list_layers` | `pyogrio.list_layers` |
| `sha256(payload).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |
| `json.loads` | `json.loads` |
| `marker_path.read_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `marker.update` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `marker_path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `replace` | `dataclasses.replace` |
| `load_ign_bdtopo_roads` | `landscout.sources.ign_bdtopo_fr.load_ign_bdtopo_roads` |
| `gpd.read_file` | `geopandas.read_file` |
| `IgnBdTopoRoadData` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoRoadData` |
| `_summary` | `tests.unit.test_normalize_access_ign._summary` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `geopackage_path.read_bytes`<br>`marker_path.read_text`<br>`gpd.read_file` |
| Filesystem/archive write or publication | `marker_path.write_text` |
| Hashing/byte identity | `sha256(payload).hexdigest`<br>`sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `marker.update(<br>        geopackage_size_bytes=len(payload),<br>        geopackage_sha256=digest,<br>        all_layer_names=list(layer_names),<br>        extracted_entries=[<br>            {<br>                "relative_path": "data.gpkg",<br>                "kind": "file",<br>                "size_bytes": len(payload),<br>                "sha256": digest,<br>            }<br>        ],<br>    )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _with_alternate_road_layer(
    source: IgnBdTopoRoadData,
) -> tuple[IgnBdTopoRoadData, IgnBdTopoRoadData]:
    alternate = _road_frame(
        [LineString([(500, 500), (600, 600)])],
        identifiers=["ALTERNATE-ROAD"],
    )
    geopackage_path = source.extraction.geopackage_path
    pyogrio.write_dataframe(
        alternate,
        geopackage_path,
        layer=ALTERNATE_ROAD_LAYER,
        driver="GPKG",
        append=True,
    )
    payload = geopackage_path.read_bytes()
    layer_names = tuple(str(row[0]) for row in pyogrio.list_layers(geopackage_path))
    digest = sha256(payload).hexdigest()
    marker_path = source.extraction.extraction_path / ".landscout-extraction.json"
    marker = json.loads(marker_path.read_text(encoding="utf-8"))
    marker.update(
        geopackage_size_bytes=len(payload),
        geopackage_sha256=digest,
        all_layer_names=list(layer_names),
        extracted_entries=[
            {
                "relative_path": "data.gpkg",
                "kind": "file",
                "size_bytes": len(payload),
                "sha256": digest,
            }
        ],
    )
    marker_path.write_text(json.dumps(marker), encoding="utf-8")
    extraction = replace(
        source.extraction,
        geopackage_size_bytes=len(payload),
        geopackage_sha256=digest,
        all_layer_names=layer_names,
    )
    configured = load_ign_bdtopo_roads(extraction, SOURCE_CONFIG)
    alternate_loaded = gpd.read_file(
        geopackage_path,
        layer=ALTERNATE_ROAD_LAYER,
        engine="pyogrio",
    )
    forged = IgnBdTopoRoadData(
        extraction=extraction,
        road_segments=alternate_loaded,
        road_segments_summary=_summary(
            alternate_loaded,
            layer=ALTERNATE_ROAD_LAYER,
        ),
    )
    return configured, forged
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_road_normalization_reproduces_configured_logical_layer`

**Purpose:** Regression invariant: road normalization reproduces configured logical layer. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_road_normalization_reproduces_configured_logical_layer() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnRoadNormalizationError, match="source\|configured\|physical")`
- Exact assertions:
  - `assert normalized.road_segments["source_layer"].eq(ROAD_LAYER).all()`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_with_alternate_road_layer` | `tests.unit.test_normalize_access_ign._with_alternate_road_layer` |
| `_source` | `tests.unit.test_normalize_access_ign._source` |
| `load_ign_bdtopo_roads` | `landscout.sources.ign_bdtopo_fr.load_ign_bdtopo_roads` |
| `normalize_ign_roads` | `landscout.stages.normalize_access_ign.normalize_ign_roads` |
| `normalized.road_segments["source_layer"].eq(ROAD_LAYER).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `normalized.road_segments["source_layer"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |

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
def test_road_normalization_reproduces_configured_logical_layer() -> None:
    configured, forged = _with_alternate_road_layer(_source())

    loaded = load_ign_bdtopo_roads(configured.extraction, SOURCE_CONFIG)
    normalized = normalize_ign_roads(loaded, SOURCE_CONFIG)
    assert normalized.road_segments["source_layer"].eq(ROAD_LAYER).all()

    with pytest.raises(IgnRoadNormalizationError, match="source|configured|physical"):
        normalize_ign_roads(forged, SOURCE_CONFIG)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_public_api_exports_only_stable_road_normalization_symbols`

**Purpose:** Regression invariant: public api exports only stable road normalization symbols. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_public_api_exports_only_stable_road_normalization_symbols() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert set(access_normalization.__all__) == expected`
  - `assert expected <= set(stages.__all__)`
  - `assert all(hasattr(stages, name) for name in expected)`
  - `assert not hasattr(stages, "_validate_road_source")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `all` | `unresolved local/third-party receiver; no ownership inferred` |
| `hasattr` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_public_api_exports_only_stable_road_normalization_symbols() -> None:
    import landscout.stages.normalize_access_ign as access_normalization

    expected = {
        "IgnRoadNormalizationError",
        "NormalizedIgnRoadData",
        "normalize_ign_roads",
    }
    assert set(access_normalization.__all__) == expected
    assert expected <= set(stages.__all__)
    assert all(hasattr(stages, name) for name in expected)
    assert not hasattr(stages, "_validate_road_source")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_valid_linestring_normalization_has_exact_schema_identity_and_lineage`

**Purpose:** Regression invariant: valid linestring normalization has exact schema identity and lineage. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_valid_linestring_normalization_has_exact_schema_identity_and_lineage() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert type(normalized) is NormalizedIgnRoadData`
  - `assert list(roads.columns) == list(OUTPUT_COLUMNS)`
  - `assert isinstance(roads.index, pd.RangeIndex)`
  - `assert roads.index.tolist() == [0]`
  - `assert row["road_feature_id"] == "IGN_BDTOPO:ROAD_SEGMENT:ROAD-1"`
  - `assert row["road_feature_type"] == "ROAD_SEGMENT"`
  - `assert row["source_feature_id"] == "ROAD-1"`
  - `assert row["source_provider"] == "IGN"`
  - `assert row["source_product"] == "BD_TOPO"`
  - `assert row["source_layer"] == ROAD_LAYER`
  - `assert row["source_department_code"] == "31"`
  - `assert row["source_edition"] == "2026-06-15"`
  - `assert row["source_product_version"] == "3.5"`
  - `assert row["source_download_timestamp"] == "2026-08-11T15:32:03+00:00"`
  - `assert row["source_archive_sha256"] == ARCHIVE_SHA256`
  - `assert row["source_url"] == SOURCE_URL`
  - `assert row["spatial_role"] == "PROXY_GEOMETRY"`
  - `assert row["geometry_status"] == "VALID"`
  - `assert roads.crs is not None and roads.crs.to_epsg() == 2154`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `normalize_ign_roads` | `landscout.stages.normalize_access_ign.normalize_ign_roads` |
| `_source` | `tests.unit.test_normalize_access_ign._source` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `roads.index.tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `roads.crs.to_epsg` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_valid_linestring_normalization_has_exact_schema_identity_and_lineage() -> None:
    normalized = normalize_ign_roads(_source(), SOURCE_CONFIG)

    assert type(normalized) is NormalizedIgnRoadData
    roads = normalized.road_segments
    assert list(roads.columns) == list(OUTPUT_COLUMNS)
    assert isinstance(roads.index, pd.RangeIndex)
    assert roads.index.tolist() == [0]
    row = roads.iloc[0]
    assert row["road_feature_id"] == "IGN_BDTOPO:ROAD_SEGMENT:ROAD-1"
    assert row["road_feature_type"] == "ROAD_SEGMENT"
    assert row["source_feature_id"] == "ROAD-1"
    assert row["source_provider"] == "IGN"
    assert row["source_product"] == "BD_TOPO"
    assert row["source_layer"] == ROAD_LAYER
    assert row["source_department_code"] == "31"
    assert row["source_edition"] == "2026-06-15"
    assert row["source_product_version"] == "3.5"
    assert row["source_download_timestamp"] == "2026-08-11T15:32:03+00:00"
    assert row["source_archive_sha256"] == ARCHIVE_SHA256
    assert row["source_url"] == SOURCE_URL
    assert row["spatial_role"] == "PROXY_GEOMETRY"
    assert row["geometry_status"] == "VALID"
    assert roads.crs is not None and roads.crs.to_epsg() == 2154
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_valid_multilinestring_is_preserved`

**Purpose:** Regression invariant: valid multilinestring is preserved. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_valid_multilinestring_is_preserved() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert roads.iloc[0]["geometry_status"] == "VALID"`
  - `assert roads.geometry.iloc[0].equals_exact(geometry, tolerance=0)`
  - `assert roads.geometry.iloc[0].geom_type == "MultiLineString"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `MultiLineString` | `shapely.geometry.MultiLineString` |
| `normalize_ign_roads` | `landscout.stages.normalize_access_ign.normalize_ign_roads` |
| `_source` | `tests.unit.test_normalize_access_ign._source` |
| `_road_frame` | `tests.unit.test_normalize_access_ign._road_frame` |
| `roads.geometry.iloc[0].equals_exact` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `roads.geometry.iloc[0].equals_exact` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_valid_multilinestring_is_preserved() -> None:
    geometry = MultiLineString([[(0, 0), (10, 10)], [(20, 20), (30, 30)]])

    roads = normalize_ign_roads(
        _source(_road_frame([geometry])), SOURCE_CONFIG
    ).road_segments

    assert roads.iloc[0]["geometry_status"] == "VALID"
    assert roads.geometry.iloc[0].equals_exact(geometry, tolerance=0)
    assert roads.geometry.iloc[0].geom_type == "MultiLineString"
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_z_coordinates_are_preserved_exactly`

**Purpose:** Regression invariant: z coordinates are preserved exactly. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_z_coordinates_are_preserved_exactly() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert roads.geometry.iloc[0].has_z`
  - `assert roads.geometry.iloc[0].wkb == geometry.wkb`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `LineString` | `shapely.geometry.LineString` |
| `normalize_ign_roads` | `landscout.stages.normalize_access_ign.normalize_ign_roads` |
| `_source` | `tests.unit.test_normalize_access_ign._source` |
| `_road_frame` | `tests.unit.test_normalize_access_ign._road_frame` |

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
def test_z_coordinates_are_preserved_exactly() -> None:
    geometry = LineString([(0, 0, 12), (10, 10, 24)])

    roads = normalize_ign_roads(
        _source(_road_frame([geometry])), SOURCE_CONFIG
    ).road_segments

    assert roads.geometry.iloc[0].has_z
    assert roads.geometry.iloc[0].wkb == geometry.wkb
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_row_count_order_geometry_and_range_index_are_preserved`

**Purpose:** Regression invariant: row count order geometry and range index are preserved. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_row_count_order_geometry_and_range_index_are_preserved() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert len(roads) == 2`
  - `assert roads["source_feature_id"].tolist() == ["SECOND", "FIRST"]`
  - `assert roads["road_feature_id"].tolist() == [<br>        "IGN_BDTOPO:ROAD_SEGMENT:SECOND",<br>        "IGN_BDTOPO:ROAD_SEGMENT:FIRST",<br>    ]`
  - `assert isinstance(roads.index, pd.RangeIndex)`
  - `assert roads.geometry.to_wkb().tolist() == [value.wkb for value in geometries]`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `LineString` | `shapely.geometry.LineString` |
| `_source` | `tests.unit.test_normalize_access_ign._source` |
| `_road_frame` | `tests.unit.test_normalize_access_ign._road_frame` |
| `normalize_ign_roads` | `landscout.stages.normalize_access_ign.normalize_ign_roads` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `roads["source_feature_id"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `roads["road_feature_id"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `roads.geometry.to_wkb().tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `roads.geometry.to_wkb` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `roads.geometry.to_wkb().tolist`<br>`roads.geometry.to_wkb` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_row_count_order_geometry_and_range_index_are_preserved() -> None:
    geometries = [
        LineString([(20, 0), (20, 10)]),
        LineString([(5, 0), (5, 10)]),
    ]
    source = _source(
        _road_frame(
            geometries,
            identifiers=["SECOND", "FIRST"],
            index=[91, 14],
        )
    )

    roads = normalize_ign_roads(source, SOURCE_CONFIG).road_segments

    assert len(roads) == 2
    assert roads["source_feature_id"].tolist() == ["SECOND", "FIRST"]
    assert roads["road_feature_id"].tolist() == [
        "IGN_BDTOPO:ROAD_SEGMENT:SECOND",
        "IGN_BDTOPO:ROAD_SEGMENT:FIRST",
    ]
    assert isinstance(roads.index, pd.RangeIndex)
    assert roads.geometry.to_wkb().tolist() == [value.wkb for value in geometries]
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_raw_access_and_restriction_values_are_copied_without_interpretation`

**Purpose:** Regression invariant: raw access and restriction values are copied without interpretation. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_raw_access_and_restriction_values_are_copied_without_interpretation() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert row["importance_raw"] == "00"`
  - `assert row["private_raw"] == "Valeur IGN non interprétée"`
  - `assert row["light_vehicle_access_raw"] == "Inconnu"`
  - `assert row["restriction_total_weight_raw"] == 19.75`
  - `assert pd.isna(row["restriction_nature_raw"])`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_road_frame` | `tests.unit.test_normalize_access_ign._road_frame` |
| `normalize_ign_roads` | `landscout.stages.normalize_access_ign.normalize_ign_roads` |
| `_source` | `tests.unit.test_normalize_access_ign._source` |
| `pd.isna` | `pandas.isna` |

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
| In-memory mutation | `source.loc[source.index[0], "importance"] = "00"`<br>`source.loc[source.index[0], "prive"] = "Valeur IGN non interprétée"`<br>`source.loc[source.index[0], "acces_vehicule_leger"] = "Inconnu"`<br>`source.loc[source.index[0], "restriction_de_poids_total"] = 19.75`<br>`source.loc[source.index[0], "nature_de_la_restriction"] = None` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_raw_access_and_restriction_values_are_copied_without_interpretation() -> None:
    source = _road_frame()
    source.loc[source.index[0], "importance"] = "00"
    source.loc[source.index[0], "prive"] = "Valeur IGN non interprétée"
    source.loc[source.index[0], "acces_vehicule_leger"] = "Inconnu"
    source.loc[source.index[0], "restriction_de_poids_total"] = 19.75
    source.loc[source.index[0], "nature_de_la_restriction"] = None

    row = normalize_ign_roads(_source(source), SOURCE_CONFIG).road_segments.iloc[0]

    assert row["importance_raw"] == "00"
    assert row["private_raw"] == "Valeur IGN non interprétée"
    assert row["light_vehicle_access_raw"] == "Inconnu"
    assert row["restriction_total_weight_raw"] == 19.75
    assert pd.isna(row["restriction_nature_raw"])
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_every_raw_field_preserves_source_values_nulls_and_dtype`

**Purpose:** Regression invariant: every raw field preserves source values nulls and dtype. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_every_raw_field_preserves_source_values_nulls_and_dtype() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source` | `tests.unit.test_normalize_access_ign._source` |
| `normalize_ign_roads` | `landscout.stages.normalize_access_ign.normalize_ign_roads` |
| `pd.testing.assert_series_equal` | `pandas.testing.assert_series_equal` |
| `source.road_segments[source_column].reset_index` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_every_raw_field_preserves_source_values_nulls_and_dtype() -> None:
    source = _source()

    roads = normalize_ign_roads(source, SOURCE_CONFIG).road_segments

    for source_column, output_column in RAW_FIELD_MAPPING:
        pd.testing.assert_series_equal(
            roads[output_column],
            source.road_segments[source_column].reset_index(drop=True),
            check_names=False,
            check_dtype=True,
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_missing_required_source_field_is_rejected`

**Purpose:** Regression invariant: missing required source field is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_missing_required_source_field_is_rejected(column: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "column",
    [
        "cleabs",
        "nature",
        "nombre_de_voies",
        "acces_vehicule_leger",
        "restriction_de_poids_total",
        "identifiants_sources",
        "geometry",
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `column` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        IgnRoadNormalizationError,<br>        match="freshly read physical source\|road segments",<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source` | `tests.unit.test_normalize_access_ign._source` |
| `source.road_segments.drop` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `normalize_ign_roads` | `landscout.stages.normalize_access_ign.normalize_ign_roads` |
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
| In-memory mutation | `source.road_segments.drop(columns=column)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_missing_required_source_field_is_rejected(column: str) -> None:
    source = _source()
    frame = source.road_segments.drop(columns=column)
    mutated = replace(source, road_segments=frame)

    with pytest.raises(
        IgnRoadNormalizationError,
        match="freshly read physical source|road segments",
    ):
        normalize_ign_roads(mutated, SOURCE_CONFIG)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_null_or_empty_cleabs_is_rejected`

**Purpose:** Regression invariant: null or empty cleabs is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_null_or_empty_cleabs_is_rejected(identifier: object) -> None:
```

- Exact decorators: `pytest.mark.parametrize("identifier", [None, "", "   ", 123])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `identifier` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnRoadNormalizationError, match="cleabs")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `normalize_ign_roads` | `landscout.stages.normalize_access_ign.normalize_ign_roads` |
| `_source` | `tests.unit.test_normalize_access_ign._source` |
| `_road_frame` | `tests.unit.test_normalize_access_ign._road_frame` |
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
def test_null_or_empty_cleabs_is_rejected(identifier: object) -> None:
    with pytest.raises(IgnRoadNormalizationError, match="cleabs"):
        normalize_ign_roads(
            _source(_road_frame(identifiers=[identifier])), SOURCE_CONFIG
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unsafe_cleabs_is_rejected`

**Purpose:** Regression invariant: unsafe cleabs is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_unsafe_cleabs_is_rejected(identifier: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "identifier",
    [" leading", "trailing ", "ROAD:BAD", "ROAD\nBAD", "ROAD\tBAD"],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `identifier` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnRoadNormalizationError, match="cleabs")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `normalize_ign_roads` | `landscout.stages.normalize_access_ign.normalize_ign_roads` |
| `_source` | `tests.unit.test_normalize_access_ign._source` |
| `_road_frame` | `tests.unit.test_normalize_access_ign._road_frame` |
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
def test_unsafe_cleabs_is_rejected(identifier: str) -> None:
    with pytest.raises(IgnRoadNormalizationError, match="cleabs"):
        normalize_ign_roads(
            _source(_road_frame(identifiers=[identifier])), SOURCE_CONFIG
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_duplicate_cleabs_is_rejected`

**Purpose:** Regression invariant: duplicate cleabs is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_duplicate_cleabs_is_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnRoadNormalizationError, match="unique")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_road_frame` | `tests.unit.test_normalize_access_ign._road_frame` |
| `LineString` | `shapely.geometry.LineString` |
| `pytest.raises` | `pytest.raises` |
| `normalize_ign_roads` | `landscout.stages.normalize_access_ign.normalize_ign_roads` |
| `_source` | `tests.unit.test_normalize_access_ign._source` |

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
def test_duplicate_cleabs_is_rejected() -> None:
    frame = _road_frame(
        [LineString([(0, 0), (1, 1)]), LineString([(2, 2), (3, 3)])],
        identifiers=["DUPLICATE", "DUPLICATE"],
    )

    with pytest.raises(IgnRoadNormalizationError, match="unique"):
        normalize_ign_roads(_source(frame), SOURCE_CONFIG)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_wrong_or_missing_road_crs_is_rejected`

**Purpose:** Regression invariant: wrong or missing road crs is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_wrong_or_missing_road_crs_is_rejected(crs: str | None) -> None:
```

- Exact decorators: `pytest.mark.parametrize("crs", [None, "EPSG:4326", "EPSG:3857"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `crs` | positional-or-keyword | `str \| None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnRoadNormalizationError, match="CRS\|2154")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `normalize_ign_roads` | `landscout.stages.normalize_access_ign.normalize_ign_roads` |
| `_source` | `tests.unit.test_normalize_access_ign._source` |
| `_road_frame` | `tests.unit.test_normalize_access_ign._road_frame` |
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
def test_wrong_or_missing_road_crs_is_rejected(crs: str | None) -> None:
    with pytest.raises(IgnRoadNormalizationError, match="CRS|2154"):
        normalize_ign_roads(_source(_road_frame(crs=crs)), SOURCE_CONFIG)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_wrong_archive_identity_is_rejected`

**Purpose:** Regression invariant: wrong archive identity is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_wrong_archive_identity_is_rejected(
    field: str,
    value: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("field", "value"),
    [
        ("provider", "OTHER"),
        ("product", "OTHER"),
        ("projection", "EPSG:4326"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `field` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnRoadNormalizationError, match="lineage\|config")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source` | `tests.unit.test_normalize_access_ign._source` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `normalize_ign_roads` | `landscout.stages.normalize_access_ign.normalize_ign_roads` |
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
def test_wrong_archive_identity_is_rejected(
    field: str,
    value: str,
) -> None:
    source = _source()
    archive = replace(source.extraction.archive, **{field: value})
    mutated = replace(source, extraction=replace(source.extraction, archive=archive))

    with pytest.raises(IgnRoadNormalizationError, match="lineage|config"):
        normalize_ign_roads(mutated, SOURCE_CONFIG)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_wrong_source_spatial_role_is_rejected`

**Purpose:** Regression invariant: wrong source spatial role is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_wrong_source_spatial_role_is_rejected(component: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize("component", ["archive", "extraction", "summary"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `component` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        IgnRoadNormalizationError,<br>        match="role\|spatial\|lineage\|integrity\|PROXY_GEOMETRY",<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source` | `tests.unit.test_normalize_access_ign._source` |
| `cast` | `typing.cast` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `normalize_ign_roads` | `landscout.stages.normalize_access_ign.normalize_ign_roads` |
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
def test_wrong_source_spatial_role_is_rejected(component: str) -> None:
    source = _source()
    wrong_role = cast(Any, "AUTHORITATIVE_ACCESS")
    if component == "archive":
        archive = replace(source.extraction.archive, spatial_role=wrong_role)
        mutated = replace(
            source,
            extraction=replace(source.extraction, archive=archive),
        )
    elif component == "extraction":
        mutated = replace(
            source,
            extraction=replace(source.extraction, spatial_role=wrong_role),
        )
    else:
        mutated = replace(
            source,
            road_segments_summary=replace(
                source.road_segments_summary,
                spatial_role=wrong_role,
            ),
        )

    with pytest.raises(
        IgnRoadNormalizationError,
        match="role|spatial|lineage|integrity|PROXY_GEOMETRY",
    ):
        normalize_ign_roads(mutated, SOURCE_CONFIG)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_summary_row_count_mismatch_is_rejected`

**Purpose:** Regression invariant: summary row count mismatch is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_summary_row_count_mismatch_is_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnRoadNormalizationError, match="summary\|physical")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source` | `tests.unit.test_normalize_access_ign._source` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `normalize_ign_roads` | `landscout.stages.normalize_access_ign.normalize_ign_roads` |

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
def test_summary_row_count_mismatch_is_rejected() -> None:
    source = _source()
    summary = replace(source.road_segments_summary, feature_count=2)

    with pytest.raises(IgnRoadNormalizationError, match="summary|physical"):
        normalize_ign_roads(
            replace(source, road_segments_summary=summary), SOURCE_CONFIG
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_road_summary_requires_strict_structural_types`

**Purpose:** Regression invariant: road summary requires strict structural types. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_road_summary_requires_strict_structural_types(
    field: str, value: object
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("field", "value"),
    [
        ("feature_count", True),
        ("feature_count", 1.0),
        ("feature_count", "1"),
        ("feature_count", -1),
        ("null_geometry_count", False),
        ("null_geometry_count", 0.0),
        ("empty_geometry_count", "0"),
        ("invalid_geometry_count", -1),
        ("columns", ["cleabs", "geometry"]),
        ("columns", ("cleabs", "cleabs")),
        ("dtypes", [("cleabs", "str")]),
        ("dtypes", (("cleabs",),)),
        ("geometry_types", ["LineString"]),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `field` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnRoadNormalizationError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source` | `tests.unit.test_normalize_access_ign._source` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `normalize_ign_roads` | `landscout.stages.normalize_access_ign.normalize_ign_roads` |
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
def test_road_summary_requires_strict_structural_types(
    field: str, value: object
) -> None:
    source = _source()
    changed = replace(source.road_segments_summary, **{field: value})

    with pytest.raises(IgnRoadNormalizationError):
        normalize_ign_roads(
            replace(source, road_segments_summary=changed), SOURCE_CONFIG
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_road_archive_sha256_requires_canonical_lowercase`

**Purpose:** Regression invariant: road archive sha256 requires canonical lowercase. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_road_archive_sha256_requires_canonical_lowercase(value: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize("value", ["A" * 64, "a" * 63, "a" * 65, "g" * 64])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnRoadNormalizationError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source` | `tests.unit.test_normalize_access_ign._source` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `normalize_ign_roads` | `landscout.stages.normalize_access_ign.normalize_ign_roads` |
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
def test_road_archive_sha256_requires_canonical_lowercase(value: str) -> None:
    source = _source()
    extraction = replace(
        source.extraction,
        archive=replace(source.extraction.archive, sha256=value),
    )

    with pytest.raises(IgnRoadNormalizationError):
        normalize_ign_roads(replace(source, extraction=extraction), SOURCE_CONFIG)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_summary_crs_mismatch_is_rejected`

**Purpose:** Regression invariant: summary crs mismatch is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_summary_crs_mismatch_is_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        IgnRoadNormalizationError,<br>        match="summary\|physical\|CRS\|2154",<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source` | `tests.unit.test_normalize_access_ign._source` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `normalize_ign_roads` | `landscout.stages.normalize_access_ign.normalize_ign_roads` |

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
def test_summary_crs_mismatch_is_rejected() -> None:
    source = _source()
    summary = replace(source.road_segments_summary, crs="EPSG:4326")

    with pytest.raises(
        IgnRoadNormalizationError,
        match="summary|physical|CRS|2154",
    ):
        normalize_ign_roads(
            replace(source, road_segments_summary=summary), SOURCE_CONFIG
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_forged_ordered_summary_schema_is_rejected`

**Purpose:** Regression invariant: forged ordered summary schema is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_forged_ordered_summary_schema_is_rejected(mutation: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize("mutation", ["missing", "extra", "reordered", "dtype"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `mutation` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        IgnRoadNormalizationError,<br>        match="summary\|physical\|schema\|columns\|dtype",<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source` | `tests.unit.test_normalize_access_ign._source` |
| `replace` | `dataclasses.replace` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `reversed` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `normalize_ign_roads` | `landscout.stages.normalize_access_ign.normalize_ign_roads` |
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
| In-memory mutation | `dtypes[0] = (dtypes[0][0], "float64")` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_forged_ordered_summary_schema_is_rejected(mutation: str) -> None:
    source = _source()
    summary = source.road_segments_summary
    if mutation == "missing":
        changed = replace(summary, columns=summary.columns[:-1])
    elif mutation == "extra":
        changed = replace(summary, columns=(*summary.columns, "invented"))
    elif mutation == "reordered":
        changed = replace(summary, columns=tuple(reversed(summary.columns)))
    else:
        dtypes = list(summary.dtypes)
        dtypes[0] = (dtypes[0][0], "float64")
        changed = replace(summary, dtypes=tuple(dtypes))

    with pytest.raises(
        IgnRoadNormalizationError,
        match="summary|physical|schema|columns|dtype",
    ):
        normalize_ign_roads(
            replace(source, road_segments_summary=changed), SOURCE_CONFIG
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_road_source_rejects_physical_role_collision`

**Purpose:** Regression invariant: road source rejects physical role collision. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_road_source_rejects_physical_role_collision(role: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize("role", ["electric", "post"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `role` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        IgnRoadNormalizationError,<br>        match="summary\|physical\|same layer\|distinct\|role",<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source` | `tests.unit.test_normalize_access_ign._source` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `normalize_ign_roads` | `landscout.stages.normalize_access_ign.normalize_ign_roads` |
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
def test_road_source_rejects_physical_role_collision(role: str) -> None:
    source = _source()
    selected = (
        source.extraction.electric_lines_layer
        if role == "electric"
        else source.extraction.transformation_posts_layer
    )
    summary = replace(source.road_segments_summary, source_layer_name=selected)
    with pytest.raises(
        IgnRoadNormalizationError,
        match="summary|physical|same layer|distinct|role",
    ):
        normalize_ign_roads(
            replace(
                source,
                road_segments_summary=summary,
            ),
            SOURCE_CONFIG,
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_road_source_rejects_duplicate_layer_inventory`

**Purpose:** Regression invariant: road source rejects duplicate layer inventory. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_road_source_rejects_duplicate_layer_inventory() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        IgnRoadNormalizationError,<br>        match="integrity\|inventory\|duplicate",<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source` | `tests.unit.test_normalize_access_ign._source` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `normalize_ign_roads` | `landscout.stages.normalize_access_ign.normalize_ign_roads` |

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
def test_road_source_rejects_duplicate_layer_inventory() -> None:
    source = _source()
    extraction = replace(
        source.extraction,
        all_layer_names=(*source.extraction.all_layer_names, ROAD_LAYER),
    )

    with pytest.raises(
        IgnRoadNormalizationError,
        match="integrity|inventory|duplicate",
    ):
        normalize_ign_roads(replace(source, extraction=extraction), SOURCE_CONFIG)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_summary_geometry_facts_mismatch_is_rejected`

**Purpose:** Regression invariant: summary geometry facts mismatch is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_summary_geometry_facts_mismatch_is_rejected(
    field: str,
    value: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("field", "value"),
    [
        ("null_geometry_count", 1),
        ("empty_geometry_count", 1),
        ("invalid_geometry_count", 1),
        ("geometry_types", ("MultiLineString",)),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `field` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        IgnRoadNormalizationError,<br>        match="summary\|physical\|geometry summary",<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source` | `tests.unit.test_normalize_access_ign._source` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `normalize_ign_roads` | `landscout.stages.normalize_access_ign.normalize_ign_roads` |
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
def test_summary_geometry_facts_mismatch_is_rejected(
    field: str,
    value: object,
) -> None:
    source = _source()
    summary = replace(source.road_segments_summary, **{field: value})

    with pytest.raises(
        IgnRoadNormalizationError,
        match="summary|physical|geometry summary",
    ):
        normalize_ign_roads(
            replace(source, road_segments_summary=summary), SOURCE_CONFIG
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_summary_layer_must_exist_in_extraction_inventory`

**Purpose:** Regression invariant: summary layer must exist in extraction inventory. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_summary_layer_must_exist_in_extraction_inventory() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        IgnRoadNormalizationError,<br>        match="integrity\|layer inventory",<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source` | `tests.unit.test_normalize_access_ign._source` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `normalize_ign_roads` | `landscout.stages.normalize_access_ign.normalize_ign_roads` |

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
def test_summary_layer_must_exist_in_extraction_inventory() -> None:
    source = _source()
    extraction = replace(source.extraction, all_layer_names=("other_layer",))

    with pytest.raises(
        IgnRoadNormalizationError,
        match="integrity|layer inventory",
    ):
        normalize_ign_roads(replace(source, extraction=extraction), SOURCE_CONFIG)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_summary_layer_and_logical_name_must_be_exact`

**Purpose:** Regression invariant: summary layer and logical name must be exact. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_summary_layer_and_logical_name_must_be_exact() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnRoadNormalizationError, match="summary\|physical layer")`
  - `pytest.raises(IgnRoadNormalizationError, match="summary\|logical name")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source` | `tests.unit.test_normalize_access_ign._source` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `normalize_ign_roads` | `landscout.stages.normalize_access_ign.normalize_ign_roads` |
| `cast` | `typing.cast` |

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
def test_summary_layer_and_logical_name_must_be_exact() -> None:
    source = _source()
    wrong_layer = replace(source.road_segments_summary, source_layer_name="route")
    with pytest.raises(IgnRoadNormalizationError, match="summary|physical layer"):
        normalize_ign_roads(
            replace(source, road_segments_summary=wrong_layer), SOURCE_CONFIG
        )

    wrong_logical = replace(
        source.road_segments_summary,
        logical_name=cast(Any, "electric_lines"),
    )
    with pytest.raises(IgnRoadNormalizationError, match="summary|logical name"):
        normalize_ign_roads(
            replace(source, road_segments_summary=wrong_logical), SOURCE_CONFIG
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_valid_unsupported_geometry_type_is_rejected`

**Purpose:** Regression invariant: valid unsupported geometry type is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_valid_unsupported_geometry_type_is_rejected(geometry: object) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "geometry",
    [Point(1, 1), Polygon([(0, 0), (0, 1), (1, 1), (1, 0), (0, 0)])],
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
  - `pytest.raises(IgnRoadNormalizationError, match="geometry types")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `normalize_ign_roads` | `landscout.stages.normalize_access_ign.normalize_ign_roads` |
| `_source` | `tests.unit.test_normalize_access_ign._source` |
| `_road_frame` | `tests.unit.test_normalize_access_ign._road_frame` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `Point` | `shapely.geometry.Point` |
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
def test_valid_unsupported_geometry_type_is_rejected(geometry: object) -> None:
    with pytest.raises(IgnRoadNormalizationError, match="geometry types"):
        normalize_ign_roads(_source(_road_frame([geometry])), SOURCE_CONFIG)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_null_empty_and_invalid_geometry_are_preserved_with_status`

**Purpose:** Regression invariant: null empty and invalid geometry are preserved with status. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_null_empty_and_invalid_geometry_are_preserved_with_status() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert roads["geometry_status"].tolist() == ["NULL", "EMPTY", "INVALID"]`
  - `assert roads.geometry.iloc[0] is None`
  - `assert roads.geometry.iloc[1].is_empty`
  - `assert roads.geometry.iloc[2].equals_exact(invalid, tolerance=0)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `Polygon` | `shapely.geometry.Polygon` |
| `_road_frame` | `tests.unit.test_normalize_access_ign._road_frame` |
| `LineString` | `shapely.geometry.LineString` |
| `normalize_ign_roads` | `landscout.stages.normalize_access_ign.normalize_ign_roads` |
| `_source` | `tests.unit.test_normalize_access_ign._source` |
| `roads["geometry_status"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `roads.geometry.iloc[2].equals_exact` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `roads["geometry_status"].tolist`<br>`roads.geometry.iloc[2].equals_exact` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_null_empty_and_invalid_geometry_are_preserved_with_status() -> None:
    invalid = Polygon([(0, 0), (2, 2), (2, 0), (0, 2), (0, 0)])
    frame = _road_frame(
        [None, LineString(), invalid],
        identifiers=["NULL", "EMPTY", "INVALID"],
    )

    roads = normalize_ign_roads(_source(frame), SOURCE_CONFIG).road_segments

    assert roads["geometry_status"].tolist() == ["NULL", "EMPTY", "INVALID"]
    assert roads.geometry.iloc[0] is None
    assert roads.geometry.iloc[1].is_empty
    assert roads.geometry.iloc[2].equals_exact(invalid, tolerance=0)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_normalization_does_not_mutate_input`

**Purpose:** Regression invariant: normalization does not mutate input. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_normalization_does_not_mutate_input() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source` | `tests.unit.test_normalize_access_ign._source` |
| `deepcopy` | `copy.deepcopy` |
| `normalize_ign_roads` | `landscout.stages.normalize_access_ign.normalize_ign_roads` |
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
def test_normalization_does_not_mutate_input() -> None:
    source = _source()
    before = deepcopy(source.road_segments)

    normalize_ign_roads(source, SOURCE_CONFIG)

    assert_geodataframe_equal(source.road_segments, before)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_road_normalization_uses_distinct_fresh_revalidated_frame`

**Purpose:** Regression invariant: road normalization uses distinct fresh revalidated frame. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_road_normalization_uses_distinct_fresh_revalidated_frame(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert normalized.road_segments.loc[0, "nature_raw"] == expected_nature`
  - `assert source.road_segments.loc[0, "nature"] == "FORGED AFTER REVALIDATION"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source` | `tests.unit.test_normalize_access_ign._source` |
| `replace` | `dataclasses.replace` |
| `source.road_segments.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `normalize_ign_roads` | `landscout.stages.normalize_access_ign.normalize_ign_roads` |

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
def test_road_normalization_uses_distinct_fresh_revalidated_frame(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    source = _source()
    fresh = replace(
        source,
        road_segments=source.road_segments.copy(deep=True),
    )
    expected_nature = fresh.road_segments.loc[0, "nature"]

    def return_fresh_and_mutate_supplied(
        _: object,
        __: object,
    ) -> IgnBdTopoRoadData:
        source.road_segments.loc[0, "nature"] = "FORGED AFTER REVALIDATION"
        return fresh

    monkeypatch.setattr(
        road_normalization,
        "_revalidate_ign_bdtopo_road_data",
        return_fresh_and_mutate_supplied,
    )

    normalized = normalize_ign_roads(source, SOURCE_CONFIG)

    assert normalized.road_segments.loc[0, "nature_raw"] == expected_nature
    assert source.road_segments.loc[0, "nature"] == "FORGED AFTER REVALIDATION"
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_road_normalization_uses_distinct_fresh_revalidated_frame.return_fresh_and_mutate_supplied`

**Purpose:** Implements `return fresh and mutate supplied` within the file role: Provides complete unit and regression coverage for the `normalize_access_ign` contracts exercised in this file.

**Exact signature**

```python
def return_fresh_and_mutate_supplied(
        _: object,
        __: object,
    ) -> IgnBdTopoRoadData:
```

- Exact decorators: none.
- Declared return annotation: `IgnBdTopoRoadData`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `_` | positional-or-keyword | `object` | `required` |
| `__` | positional-or-keyword | `object` | `required` |

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
| In-memory mutation | `source.road_segments.loc[0, "nature"] = "FORGED AFTER REVALIDATION"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def return_fresh_and_mutate_supplied(
        _: object,
        __: object,
    ) -> IgnBdTopoRoadData:
        source.road_segments.loc[0, "nature"] = "FORGED AFTER REVALIDATION"
        return fresh
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_high_level_rejects_coordinated_road_frame_and_summary_forgery`

**Purpose:** Regression invariant: high level rejects coordinated road frame and summary forgery. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_high_level_rejects_coordinated_road_frame_and_summary_forgery() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnRoadNormalizationError, match="physical\|fresh\|source")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source` | `tests.unit.test_normalize_access_ign._source` |
| `source.road_segments.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `_summary` | `tests.unit.test_normalize_access_ign._summary` |
| `pytest.raises` | `pytest.raises` |
| `normalize_ign_roads` | `landscout.stages.normalize_access_ign.normalize_ign_roads` |
| `replace` | `dataclasses.replace` |

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
| In-memory mutation | `forged.loc[0, "nature"] = "Invented road nature"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_high_level_rejects_coordinated_road_frame_and_summary_forgery() -> None:
    source = _source()
    forged = source.road_segments.copy()
    forged.loc[0, "nature"] = "Invented road nature"
    forged_summary = _summary(forged)

    with pytest.raises(IgnRoadNormalizationError, match="physical|fresh|source"):
        normalize_ign_roads(
            replace(
                source,
                road_segments=forged,
                road_segments_summary=forged_summary,
            ),
            SOURCE_CONFIG,
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_malformed_public_input_has_controlled_error`

**Purpose:** Regression invariant: malformed public input has controlled error. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_malformed_public_input_has_controlled_error() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnRoadNormalizationError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `normalize_ign_roads` | `landscout.stages.normalize_access_ign.normalize_ign_roads` |
| `cast` | `typing.cast` |
| `object` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_malformed_public_input_has_controlled_error() -> None:
    with pytest.raises(IgnRoadNormalizationError):
        normalize_ign_roads(cast(Any, object()), SOURCE_CONFIG)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.


## 7. Test-specific regression contract

- Test functions: **31**.
- Pytest fixtures (decorator-proven): **0**.

### Per-test regression index

| Test | Parametrization | Expected exception contexts | Assertion count | Exact regression purpose |
|---|---|---|---:|---|
| `test_road_normalization_reproduces_configured_logical_layer` | none | pytest.raises(IgnRoadNormalizationError, match="source\|configured\|physical") | 1 | Proves road normalization reproduces configured logical layer using the exact source reproduced in section 7. |
| `test_public_api_exports_only_stable_road_normalization_symbols` | none | none | 4 | Proves public api exports only stable road normalization symbols using the exact source reproduced in section 7. |
| `test_valid_linestring_normalization_has_exact_schema_identity_and_lineage` | none | none | 19 | Proves valid linestring normalization has exact schema identity and lineage using the exact source reproduced in section 7. |
| `test_valid_multilinestring_is_preserved` | none | none | 3 | Proves valid multilinestring is preserved using the exact source reproduced in section 7. |
| `test_z_coordinates_are_preserved_exactly` | none | none | 2 | Proves z coordinates are preserved exactly using the exact source reproduced in section 7. |
| `test_row_count_order_geometry_and_range_index_are_preserved` | none | none | 5 | Proves row count order geometry and range index are preserved using the exact source reproduced in section 7. |
| `test_raw_access_and_restriction_values_are_copied_without_interpretation` | none | none | 5 | Proves raw access and restriction values are copied without interpretation using the exact source reproduced in section 7. |
| `test_every_raw_field_preserves_source_values_nulls_and_dtype` | none | none | 0 | Proves every raw field preserves source values nulls and dtype using the exact source reproduced in section 7. |
| `test_missing_required_source_field_is_rejected` | pytest.mark.parametrize(<br>    "column",<br>    [<br>        "cleabs",<br>        "nature",<br>        "nombre_de_voies",<br>        "acces_vehicule_leger",<br>        "restriction_de_poids_total",<br>        "identifiants_sources",<br>        "geometry",<br>    ],<br>) | pytest.raises(<br>        IgnRoadNormalizationError,<br>        match="freshly read physical source\|road segments",<br>    ) | 0 | Proves missing required source field is rejected using the exact source reproduced in section 7. |
| `test_null_or_empty_cleabs_is_rejected` | pytest.mark.parametrize("identifier", [None, "", "   ", 123]) | pytest.raises(IgnRoadNormalizationError, match="cleabs") | 0 | Proves null or empty cleabs is rejected using the exact source reproduced in section 7. |
| `test_unsafe_cleabs_is_rejected` | pytest.mark.parametrize(<br>    "identifier",<br>    [" leading", "trailing ", "ROAD:BAD", "ROAD\nBAD", "ROAD\tBAD"],<br>) | pytest.raises(IgnRoadNormalizationError, match="cleabs") | 0 | Proves unsafe cleabs is rejected using the exact source reproduced in section 7. |
| `test_duplicate_cleabs_is_rejected` | none | pytest.raises(IgnRoadNormalizationError, match="unique") | 0 | Proves duplicate cleabs is rejected using the exact source reproduced in section 7. |
| `test_wrong_or_missing_road_crs_is_rejected` | pytest.mark.parametrize("crs", [None, "EPSG:4326", "EPSG:3857"]) | pytest.raises(IgnRoadNormalizationError, match="CRS\|2154") | 0 | Proves wrong or missing road crs is rejected using the exact source reproduced in section 7. |
| `test_wrong_archive_identity_is_rejected` | pytest.mark.parametrize(<br>    ("field", "value"),<br>    [<br>        ("provider", "OTHER"),<br>        ("product", "OTHER"),<br>        ("projection", "EPSG:4326"),<br>    ],<br>) | pytest.raises(IgnRoadNormalizationError, match="lineage\|config") | 0 | Proves wrong archive identity is rejected using the exact source reproduced in section 7. |
| `test_wrong_source_spatial_role_is_rejected` | pytest.mark.parametrize("component", ["archive", "extraction", "summary"]) | pytest.raises(<br>        IgnRoadNormalizationError,<br>        match="role\|spatial\|lineage\|integrity\|PROXY_GEOMETRY",<br>    ) | 0 | Proves wrong source spatial role is rejected using the exact source reproduced in section 7. |
| `test_summary_row_count_mismatch_is_rejected` | none | pytest.raises(IgnRoadNormalizationError, match="summary\|physical") | 0 | Proves summary row count mismatch is rejected using the exact source reproduced in section 7. |
| `test_road_summary_requires_strict_structural_types` | pytest.mark.parametrize(<br>    ("field", "value"),<br>    [<br>        ("feature_count", True),<br>        ("feature_count", 1.0),<br>        ("feature_count", "1"),<br>        ("feature_count", -1),<br>        ("null_geometry_count", False),<br>        ("null_geometry_count", 0.0),<br>        ("empty_geometry_count", "0"),<br>        ("invalid_geometry_count", -1),<br>        ("columns", ["cleabs", "geometry"]),<br>        ("columns", ("cleabs", "cleabs")),<br>        ("dtypes", [("cleabs", "str")]),<br>        ("dtypes", (("cleabs",),)),<br>        ("geometry_types", ["LineString"]),<br>    ],<br>) | pytest.raises(IgnRoadNormalizationError) | 0 | Proves road summary requires strict structural types using the exact source reproduced in section 7. |
| `test_road_archive_sha256_requires_canonical_lowercase` | pytest.mark.parametrize("value", ["A" * 64, "a" * 63, "a" * 65, "g" * 64]) | pytest.raises(IgnRoadNormalizationError) | 0 | Proves road archive sha256 requires canonical lowercase using the exact source reproduced in section 7. |
| `test_summary_crs_mismatch_is_rejected` | none | pytest.raises(<br>        IgnRoadNormalizationError,<br>        match="summary\|physical\|CRS\|2154",<br>    ) | 0 | Proves summary crs mismatch is rejected using the exact source reproduced in section 7. |
| `test_forged_ordered_summary_schema_is_rejected` | pytest.mark.parametrize("mutation", ["missing", "extra", "reordered", "dtype"]) | pytest.raises(<br>        IgnRoadNormalizationError,<br>        match="summary\|physical\|schema\|columns\|dtype",<br>    ) | 0 | Proves forged ordered summary schema is rejected using the exact source reproduced in section 7. |
| `test_road_source_rejects_physical_role_collision` | pytest.mark.parametrize("role", ["electric", "post"]) | pytest.raises(<br>        IgnRoadNormalizationError,<br>        match="summary\|physical\|same layer\|distinct\|role",<br>    ) | 0 | Proves road source rejects physical role collision using the exact source reproduced in section 7. |
| `test_road_source_rejects_duplicate_layer_inventory` | none | pytest.raises(<br>        IgnRoadNormalizationError,<br>        match="integrity\|inventory\|duplicate",<br>    ) | 0 | Proves road source rejects duplicate layer inventory using the exact source reproduced in section 7. |
| `test_summary_geometry_facts_mismatch_is_rejected` | pytest.mark.parametrize(<br>    ("field", "value"),<br>    [<br>        ("null_geometry_count", 1),<br>        ("empty_geometry_count", 1),<br>        ("invalid_geometry_count", 1),<br>        ("geometry_types", ("MultiLineString",)),<br>    ],<br>) | pytest.raises(<br>        IgnRoadNormalizationError,<br>        match="summary\|physical\|geometry summary",<br>    ) | 0 | Proves summary geometry facts mismatch is rejected using the exact source reproduced in section 7. |
| `test_summary_layer_must_exist_in_extraction_inventory` | none | pytest.raises(<br>        IgnRoadNormalizationError,<br>        match="integrity\|layer inventory",<br>    ) | 0 | Proves summary layer must exist in extraction inventory using the exact source reproduced in section 7. |
| `test_summary_layer_and_logical_name_must_be_exact` | none | pytest.raises(IgnRoadNormalizationError, match="summary\|physical layer"); pytest.raises(IgnRoadNormalizationError, match="summary\|logical name") | 0 | Proves summary layer and logical name must be exact using the exact source reproduced in section 7. |
| `test_valid_unsupported_geometry_type_is_rejected` | pytest.mark.parametrize(<br>    "geometry",<br>    [Point(1, 1), Polygon([(0, 0), (0, 1), (1, 1), (1, 0), (0, 0)])],<br>) | pytest.raises(IgnRoadNormalizationError, match="geometry types") | 0 | Proves valid unsupported geometry type is rejected using the exact source reproduced in section 7. |
| `test_null_empty_and_invalid_geometry_are_preserved_with_status` | none | none | 4 | Proves null empty and invalid geometry are preserved with status using the exact source reproduced in section 7. |
| `test_normalization_does_not_mutate_input` | none | none | 0 | Proves normalization does not mutate input using the exact source reproduced in section 7. |
| `test_road_normalization_uses_distinct_fresh_revalidated_frame` | none | none | 2 | Proves road normalization uses distinct fresh revalidated frame using the exact source reproduced in section 7. |
| `test_high_level_rejects_coordinated_road_frame_and_summary_forgery` | none | pytest.raises(IgnRoadNormalizationError, match="physical\|fresh\|source") | 0 | Proves high level rejects coordinated road frame and summary forgery using the exact source reproduced in section 7. |
| `test_malformed_public_input_has_controlled_error` | none | pytest.raises(IgnRoadNormalizationError) | 0 | Proves malformed public input has controlled error using the exact source reproduced in section 7. |

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
from __future__ import annotations

import json
import tempfile
from copy import deepcopy
from dataclasses import replace
from hashlib import sha256
from pathlib import Path
from typing import Any, cast
from uuid import uuid4

import geopandas as gpd
import pandas as pd
import pyogrio
import pytest
from geopandas.testing import assert_geodataframe_equal
from shapely.geometry import LineString, MultiLineString, Point, Polygon

import landscout.stages.normalize_access_ign as road_normalization
from landscout import stages
from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
)
from landscout.stages.normalize_access_ign import (
    IgnRoadNormalizationError,
    NormalizedIgnRoadData,
    normalize_ign_roads,
)

ROAD_LAYER = "troncon_de_route"
ALTERNATE_ROAD_LAYER = "voie_secondaire"
DEPARTMENT_LAYER = "departement"
ARCHIVE_SHA256 = "a" * 64
SOURCE_URL = "https://example.test/BDTOPO_D031.7z"
_FIXTURE_ROOT = Path(tempfile.mkdtemp(prefix="landscout-road-ign-"))
_SOURCE_CONFIG_PAYLOAD = load_ign_bdtopo_source_config().model_dump(mode="json")
_SOURCE_CONFIG_PAYLOAD.update(
    {
        "source_url": SOURCE_URL,
        "checksum_url": None,
        "official_checksum_algorithm": None,
        "official_checksum": None,
        "expected_archive_size_bytes": 1234,
    }
)
SOURCE_CONFIG = IgnBdTopoSourceConfig.model_validate(_SOURCE_CONFIG_PAYLOAD)

OUTPUT_COLUMNS = (
    "road_feature_id",
    "road_feature_type",
    "source_provider",
    "source_product",
    "source_layer",
    "source_feature_id",
    "source_department_code",
    "source_edition",
    "source_product_version",
    "source_download_timestamp",
    "source_archive_sha256",
    "source_url",
    "nature_raw",
    "importance_raw",
    "fictitious_raw",
    "position_relative_to_ground_raw",
    "asset_status_raw",
    "lane_count_raw",
    "carriageway_width_raw",
    "private_raw",
    "traffic_direction_raw",
    "urban_raw",
    "mean_light_vehicle_speed_raw",
    "light_vehicle_access_raw",
    "closure_period_raw",
    "restriction_nature_raw",
    "restriction_height_raw",
    "restriction_total_weight_raw",
    "restriction_axle_weight_raw",
    "restriction_width_raw",
    "restriction_length_raw",
    "dangerous_goods_forbidden_raw",
    "administrative_classification_raw",
    "manager_raw",
    "source_name_raw",
    "source_identifiers_raw",
    "source_created_at",
    "source_modified_at",
    "source_confirmed_at",
    "planimetric_acquisition_method",
    "planimetric_precision_raw",
    "spatial_role",
    "geometry_status",
    "geometry",
)
RAW_FIELD_MAPPING = (
    ("nature", "nature_raw"),
    ("importance", "importance_raw"),
    ("fictif", "fictitious_raw"),
    ("position_par_rapport_au_sol", "position_relative_to_ground_raw"),
    ("etat_de_l_objet", "asset_status_raw"),
    ("nombre_de_voies", "lane_count_raw"),
    ("largeur_de_chaussee", "carriageway_width_raw"),
    ("prive", "private_raw"),
    ("sens_de_circulation", "traffic_direction_raw"),
    ("urbain", "urban_raw"),
    ("vitesse_moyenne_vl", "mean_light_vehicle_speed_raw"),
    ("acces_vehicule_leger", "light_vehicle_access_raw"),
    ("periode_de_fermeture", "closure_period_raw"),
    ("nature_de_la_restriction", "restriction_nature_raw"),
    ("restriction_de_hauteur", "restriction_height_raw"),
    ("restriction_de_poids_total", "restriction_total_weight_raw"),
    ("restriction_de_poids_par_essieu", "restriction_axle_weight_raw"),
    ("restriction_de_largeur", "restriction_width_raw"),
    ("restriction_de_longueur", "restriction_length_raw"),
    ("matieres_dangereuses_interdites", "dangerous_goods_forbidden_raw"),
    ("cpx_classement_administratif", "administrative_classification_raw"),
    ("cpx_gestionnaire", "manager_raw"),
    ("sources", "source_name_raw"),
    ("identifiants_sources", "source_identifiers_raw"),
    ("date_creation", "source_created_at"),
    ("date_modification", "source_modified_at"),
    ("date_de_confirmation", "source_confirmed_at"),
    ("methode_d_acquisition_planimetrique", "planimetric_acquisition_method"),
    ("precision_planimetrique", "planimetric_precision_raw"),
)


def _road_frame(
    geometries: list[object] | None = None,
    *,
    identifiers: list[object] | None = None,
    crs: str | None = "EPSG:2154",
    index: list[object] | None = None,
) -> gpd.GeoDataFrame:
    source_geometries = geometries or [LineString([(0, 0), (100, 100)])]
    count = len(source_geometries)
    source_ids = identifiers or [f"ROAD-{number + 1}" for number in range(count)]
    source_index = index or [100 + number for number in range(count)]
    values: dict[str, list[object]] = {
        "cleabs": source_ids,
        "nature": ["Route à 1 chaussée"] * count,
        "importance": ["2"] * count,
        "fictif": ["Non"] * count,
        "position_par_rapport_au_sol": [-1] * count,
        "etat_de_l_objet": ["En service"] * count,
        "nombre_de_voies": [2] * count,
        "largeur_de_chaussee": [7.5] * count,
        "prive": ["Non"] * count,
        "sens_de_circulation": ["Double sens"] * count,
        "urbain": ["Non"] * count,
        "vitesse_moyenne_vl": [80] * count,
        "acces_vehicule_leger": ["Libre"] * count,
        "periode_de_fermeture": [None] * count,
        "nature_de_la_restriction": ["Poids total"] * count,
        "restriction_de_hauteur": [4.2] * count,
        "restriction_de_poids_total": [19.0] * count,
        "restriction_de_poids_par_essieu": [11.5] * count,
        "restriction_de_largeur": [3.2] * count,
        "restriction_de_longueur": [18.0] * count,
        "matieres_dangereuses_interdites": ["Oui"] * count,
        "cpx_classement_administratif": ["Départementale"] * count,
        "cpx_gestionnaire": ["CD31"] * count,
        "sources": ["IGN 2026"] * count,
        "identifiants_sources": ["source-road-id"] * count,
        "date_creation": [pd.Timestamp("2024-01-01", tz="UTC")] * count,
        "date_modification": [pd.Timestamp("2025-01-01", tz="UTC")] * count,
        "date_de_confirmation": [pd.Timestamp("2025-06-01", tz="UTC")] * count,
        "methode_d_acquisition_planimetrique": ["Photogrammétrie"] * count,
        "precision_planimetrique": [2.5] * count,
    }
    return gpd.GeoDataFrame(
        values,
        geometry=source_geometries,
        crs=crs,
        index=source_index,
    )


def _summary(
    frame: gpd.GeoDataFrame,
    *,
    layer: str = ROAD_LAYER,
) -> IgnBdTopoLayerSummary:
    geometry = frame.geometry
    null_mask = geometry.isna()
    empty_mask = ~null_mask & geometry.is_empty
    invalid_mask = ~null_mask & ~geometry.is_empty & ~geometry.is_valid
    return IgnBdTopoLayerSummary(
        logical_name="road_segments",
        source_layer_name=layer,
        crs=str(frame.crs),
        feature_count=len(frame),
        columns=tuple(str(column) for column in frame.columns),
        dtypes=tuple(
            (str(column), str(dtype)) for column, dtype in frame.dtypes.items()
        ),
        null_geometry_count=int(null_mask.sum()),
        empty_geometry_count=int(empty_mask.sum()),
        invalid_geometry_count=int(invalid_mask.sum()),
        geometry_types=tuple(
            sorted(
                str(value) for value in geometry[~null_mask].geom_type.dropna().unique()
            )
        ),
    )


def _source(frame: gpd.GeoDataFrame | None = None) -> IgnBdTopoRoadData:
    road_frame = frame if frame is not None else _road_frame()
    extraction_path = _FIXTURE_ROOT / uuid4().hex
    extraction_path.mkdir(parents=True)
    geopackage_path = extraction_path / "data.gpkg"
    crs = road_frame.crs or "EPSG:2154"
    dummy = gpd.GeoDataFrame(
        {"id": ["dummy"]},
        geometry=[LineString([(0, 0), (1, 1)])],
        crs=crs,
    )
    pyogrio.write_dataframe(
        dummy, geopackage_path, layer="ligne_electrique", driver="GPKG"
    )
    pyogrio.write_dataframe(
        dummy,
        geopackage_path,
        layer="poste_de_transformation",
        driver="GPKG",
        append=True,
    )
    pyogrio.write_dataframe(
        road_frame,
        geopackage_path,
        layer=ROAD_LAYER,
        driver="GPKG",
        append=True,
    )
    pyogrio.write_dataframe(
        gpd.GeoDataFrame(
            {"code_insee": ["31"]},
            geometry=[Polygon([(0, 0), (0, 10), (10, 10), (10, 0)])],
            crs="EPSG:2154",
        ),
        geopackage_path,
        layer=DEPARTMENT_LAYER,
        driver="GPKG",
        append=True,
    )
    road_frame = gpd.read_file(geopackage_path, layer=ROAD_LAYER, engine="pyogrio")
    payload = geopackage_path.read_bytes()
    layer_names = tuple(str(row[0]) for row in pyogrio.list_layers(geopackage_path))
    digest = sha256(payload).hexdigest()
    (extraction_path / ".landscout-extraction.json").write_text(
        json.dumps(
            {
                "schema_version": 3,
                "archive_sha256": ARCHIVE_SHA256,
                "geopackage_relative_path": "data.gpkg",
                "geopackage_size_bytes": len(payload),
                "geopackage_sha256": digest,
                "all_layer_names": list(layer_names),
                "electric_lines_layer": "ligne_electrique",
                "transformation_posts_layer": "poste_de_transformation",
                "road_segments_layer": ROAD_LAYER,
                "department_layer": DEPARTMENT_LAYER,
                "extracted_entries": [
                    {
                        "relative_path": "data.gpkg",
                        "kind": "file",
                        "size_bytes": len(payload),
                        "sha256": digest,
                    }
                ],
                "spatial_role": "PROXY_GEOMETRY",
            }
        ),
        encoding="utf-8",
    )
    archive = IgnBdTopoDownload(
        provider=SOURCE_CONFIG.provider,
        product="BD TOPO",
        department_code="31",
        edition="2026-06-15",
        product_version="3.5",
        projection="EPSG:2154",
        package_format="GPKG",
        archive_format="7z",
        source_url=SOURCE_URL,
        checksum_url=None,
        download_timestamp="2026-08-11T15:32:03+00:00",
        filename="BDTOPO_D031.7z",
        file_size=1234,
        sha256=ARCHIVE_SHA256,
        official_checksum_algorithm=None,
        official_checksum=None,
        official_checksum_validated=False,
        path=Path("cache/BDTOPO_D031.7z"),
        cache_hit=True,
    )
    extraction = IgnBdTopoExtraction(
        archive=archive,
        extraction_path=extraction_path,
        geopackage_path=geopackage_path,
        geopackage_filename="data.gpkg",
        geopackage_size_bytes=len(payload),
        geopackage_sha256=digest,
        all_layer_names=layer_names,
        electric_lines_layer="ligne_electrique",
        transformation_posts_layer="poste_de_transformation",
        road_segments_layer=ROAD_LAYER,
        department_layer=DEPARTMENT_LAYER,
        cache_hit=True,
    )
    return IgnBdTopoRoadData(
        extraction=extraction,
        road_segments=road_frame,
        road_segments_summary=_summary(road_frame),
    )


def _with_alternate_road_layer(
    source: IgnBdTopoRoadData,
) -> tuple[IgnBdTopoRoadData, IgnBdTopoRoadData]:
    alternate = _road_frame(
        [LineString([(500, 500), (600, 600)])],
        identifiers=["ALTERNATE-ROAD"],
    )
    geopackage_path = source.extraction.geopackage_path
    pyogrio.write_dataframe(
        alternate,
        geopackage_path,
        layer=ALTERNATE_ROAD_LAYER,
        driver="GPKG",
        append=True,
    )
    payload = geopackage_path.read_bytes()
    layer_names = tuple(str(row[0]) for row in pyogrio.list_layers(geopackage_path))
    digest = sha256(payload).hexdigest()
    marker_path = source.extraction.extraction_path / ".landscout-extraction.json"
    marker = json.loads(marker_path.read_text(encoding="utf-8"))
    marker.update(
        geopackage_size_bytes=len(payload),
        geopackage_sha256=digest,
        all_layer_names=list(layer_names),
        extracted_entries=[
            {
                "relative_path": "data.gpkg",
                "kind": "file",
                "size_bytes": len(payload),
                "sha256": digest,
            }
        ],
    )
    marker_path.write_text(json.dumps(marker), encoding="utf-8")
    extraction = replace(
        source.extraction,
        geopackage_size_bytes=len(payload),
        geopackage_sha256=digest,
        all_layer_names=layer_names,
    )
    configured = load_ign_bdtopo_roads(extraction, SOURCE_CONFIG)
    alternate_loaded = gpd.read_file(
        geopackage_path,
        layer=ALTERNATE_ROAD_LAYER,
        engine="pyogrio",
    )
    forged = IgnBdTopoRoadData(
        extraction=extraction,
        road_segments=alternate_loaded,
        road_segments_summary=_summary(
            alternate_loaded,
            layer=ALTERNATE_ROAD_LAYER,
        ),
    )
    return configured, forged


def test_road_normalization_reproduces_configured_logical_layer() -> None:
    configured, forged = _with_alternate_road_layer(_source())

    loaded = load_ign_bdtopo_roads(configured.extraction, SOURCE_CONFIG)
    normalized = normalize_ign_roads(loaded, SOURCE_CONFIG)
    assert normalized.road_segments["source_layer"].eq(ROAD_LAYER).all()

    with pytest.raises(IgnRoadNormalizationError, match="source|configured|physical"):
        normalize_ign_roads(forged, SOURCE_CONFIG)


def test_public_api_exports_only_stable_road_normalization_symbols() -> None:
    import landscout.stages.normalize_access_ign as access_normalization

    expected = {
        "IgnRoadNormalizationError",
        "NormalizedIgnRoadData",
        "normalize_ign_roads",
    }
    assert set(access_normalization.__all__) == expected
    assert expected <= set(stages.__all__)
    assert all(hasattr(stages, name) for name in expected)
    assert not hasattr(stages, "_validate_road_source")


def test_valid_linestring_normalization_has_exact_schema_identity_and_lineage() -> None:
    normalized = normalize_ign_roads(_source(), SOURCE_CONFIG)

    assert type(normalized) is NormalizedIgnRoadData
    roads = normalized.road_segments
    assert list(roads.columns) == list(OUTPUT_COLUMNS)
    assert isinstance(roads.index, pd.RangeIndex)
    assert roads.index.tolist() == [0]
    row = roads.iloc[0]
    assert row["road_feature_id"] == "IGN_BDTOPO:ROAD_SEGMENT:ROAD-1"
    assert row["road_feature_type"] == "ROAD_SEGMENT"
    assert row["source_feature_id"] == "ROAD-1"
    assert row["source_provider"] == "IGN"
    assert row["source_product"] == "BD_TOPO"
    assert row["source_layer"] == ROAD_LAYER
    assert row["source_department_code"] == "31"
    assert row["source_edition"] == "2026-06-15"
    assert row["source_product_version"] == "3.5"
    assert row["source_download_timestamp"] == "2026-08-11T15:32:03+00:00"
    assert row["source_archive_sha256"] == ARCHIVE_SHA256
    assert row["source_url"] == SOURCE_URL
    assert row["spatial_role"] == "PROXY_GEOMETRY"
    assert row["geometry_status"] == "VALID"
    assert roads.crs is not None and roads.crs.to_epsg() == 2154


def test_valid_multilinestring_is_preserved() -> None:
    geometry = MultiLineString([[(0, 0), (10, 10)], [(20, 20), (30, 30)]])

    roads = normalize_ign_roads(
        _source(_road_frame([geometry])), SOURCE_CONFIG
    ).road_segments

    assert roads.iloc[0]["geometry_status"] == "VALID"
    assert roads.geometry.iloc[0].equals_exact(geometry, tolerance=0)
    assert roads.geometry.iloc[0].geom_type == "MultiLineString"


def test_z_coordinates_are_preserved_exactly() -> None:
    geometry = LineString([(0, 0, 12), (10, 10, 24)])

    roads = normalize_ign_roads(
        _source(_road_frame([geometry])), SOURCE_CONFIG
    ).road_segments

    assert roads.geometry.iloc[0].has_z
    assert roads.geometry.iloc[0].wkb == geometry.wkb


def test_row_count_order_geometry_and_range_index_are_preserved() -> None:
    geometries = [
        LineString([(20, 0), (20, 10)]),
        LineString([(5, 0), (5, 10)]),
    ]
    source = _source(
        _road_frame(
            geometries,
            identifiers=["SECOND", "FIRST"],
            index=[91, 14],
        )
    )

    roads = normalize_ign_roads(source, SOURCE_CONFIG).road_segments

    assert len(roads) == 2
    assert roads["source_feature_id"].tolist() == ["SECOND", "FIRST"]
    assert roads["road_feature_id"].tolist() == [
        "IGN_BDTOPO:ROAD_SEGMENT:SECOND",
        "IGN_BDTOPO:ROAD_SEGMENT:FIRST",
    ]
    assert isinstance(roads.index, pd.RangeIndex)
    assert roads.geometry.to_wkb().tolist() == [value.wkb for value in geometries]


def test_raw_access_and_restriction_values_are_copied_without_interpretation() -> None:
    source = _road_frame()
    source.loc[source.index[0], "importance"] = "00"
    source.loc[source.index[0], "prive"] = "Valeur IGN non interprétée"
    source.loc[source.index[0], "acces_vehicule_leger"] = "Inconnu"
    source.loc[source.index[0], "restriction_de_poids_total"] = 19.75
    source.loc[source.index[0], "nature_de_la_restriction"] = None

    row = normalize_ign_roads(_source(source), SOURCE_CONFIG).road_segments.iloc[0]

    assert row["importance_raw"] == "00"
    assert row["private_raw"] == "Valeur IGN non interprétée"
    assert row["light_vehicle_access_raw"] == "Inconnu"
    assert row["restriction_total_weight_raw"] == 19.75
    assert pd.isna(row["restriction_nature_raw"])


def test_every_raw_field_preserves_source_values_nulls_and_dtype() -> None:
    source = _source()

    roads = normalize_ign_roads(source, SOURCE_CONFIG).road_segments

    for source_column, output_column in RAW_FIELD_MAPPING:
        pd.testing.assert_series_equal(
            roads[output_column],
            source.road_segments[source_column].reset_index(drop=True),
            check_names=False,
            check_dtype=True,
        )


@pytest.mark.parametrize(
    "column",
    [
        "cleabs",
        "nature",
        "nombre_de_voies",
        "acces_vehicule_leger",
        "restriction_de_poids_total",
        "identifiants_sources",
        "geometry",
    ],
)
def test_missing_required_source_field_is_rejected(column: str) -> None:
    source = _source()
    frame = source.road_segments.drop(columns=column)
    mutated = replace(source, road_segments=frame)

    with pytest.raises(
        IgnRoadNormalizationError,
        match="freshly read physical source|road segments",
    ):
        normalize_ign_roads(mutated, SOURCE_CONFIG)


@pytest.mark.parametrize("identifier", [None, "", "   ", 123])
def test_null_or_empty_cleabs_is_rejected(identifier: object) -> None:
    with pytest.raises(IgnRoadNormalizationError, match="cleabs"):
        normalize_ign_roads(
            _source(_road_frame(identifiers=[identifier])), SOURCE_CONFIG
        )


@pytest.mark.parametrize(
    "identifier",
    [" leading", "trailing ", "ROAD:BAD", "ROAD\nBAD", "ROAD\tBAD"],
)
def test_unsafe_cleabs_is_rejected(identifier: str) -> None:
    with pytest.raises(IgnRoadNormalizationError, match="cleabs"):
        normalize_ign_roads(
            _source(_road_frame(identifiers=[identifier])), SOURCE_CONFIG
        )


def test_duplicate_cleabs_is_rejected() -> None:
    frame = _road_frame(
        [LineString([(0, 0), (1, 1)]), LineString([(2, 2), (3, 3)])],
        identifiers=["DUPLICATE", "DUPLICATE"],
    )

    with pytest.raises(IgnRoadNormalizationError, match="unique"):
        normalize_ign_roads(_source(frame), SOURCE_CONFIG)


@pytest.mark.parametrize("crs", [None, "EPSG:4326", "EPSG:3857"])
def test_wrong_or_missing_road_crs_is_rejected(crs: str | None) -> None:
    with pytest.raises(IgnRoadNormalizationError, match="CRS|2154"):
        normalize_ign_roads(_source(_road_frame(crs=crs)), SOURCE_CONFIG)


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("provider", "OTHER"),
        ("product", "OTHER"),
        ("projection", "EPSG:4326"),
    ],
)
def test_wrong_archive_identity_is_rejected(
    field: str,
    value: str,
) -> None:
    source = _source()
    archive = replace(source.extraction.archive, **{field: value})
    mutated = replace(source, extraction=replace(source.extraction, archive=archive))

    with pytest.raises(IgnRoadNormalizationError, match="lineage|config"):
        normalize_ign_roads(mutated, SOURCE_CONFIG)


@pytest.mark.parametrize("component", ["archive", "extraction", "summary"])
def test_wrong_source_spatial_role_is_rejected(component: str) -> None:
    source = _source()
    wrong_role = cast(Any, "AUTHORITATIVE_ACCESS")
    if component == "archive":
        archive = replace(source.extraction.archive, spatial_role=wrong_role)
        mutated = replace(
            source,
            extraction=replace(source.extraction, archive=archive),
        )
    elif component == "extraction":
        mutated = replace(
            source,
            extraction=replace(source.extraction, spatial_role=wrong_role),
        )
    else:
        mutated = replace(
            source,
            road_segments_summary=replace(
                source.road_segments_summary,
                spatial_role=wrong_role,
            ),
        )

    with pytest.raises(
        IgnRoadNormalizationError,
        match="role|spatial|lineage|integrity|PROXY_GEOMETRY",
    ):
        normalize_ign_roads(mutated, SOURCE_CONFIG)


def test_summary_row_count_mismatch_is_rejected() -> None:
    source = _source()
    summary = replace(source.road_segments_summary, feature_count=2)

    with pytest.raises(IgnRoadNormalizationError, match="summary|physical"):
        normalize_ign_roads(
            replace(source, road_segments_summary=summary), SOURCE_CONFIG
        )


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("feature_count", True),
        ("feature_count", 1.0),
        ("feature_count", "1"),
        ("feature_count", -1),
        ("null_geometry_count", False),
        ("null_geometry_count", 0.0),
        ("empty_geometry_count", "0"),
        ("invalid_geometry_count", -1),
        ("columns", ["cleabs", "geometry"]),
        ("columns", ("cleabs", "cleabs")),
        ("dtypes", [("cleabs", "str")]),
        ("dtypes", (("cleabs",),)),
        ("geometry_types", ["LineString"]),
    ],
)
def test_road_summary_requires_strict_structural_types(
    field: str, value: object
) -> None:
    source = _source()
    changed = replace(source.road_segments_summary, **{field: value})

    with pytest.raises(IgnRoadNormalizationError):
        normalize_ign_roads(
            replace(source, road_segments_summary=changed), SOURCE_CONFIG
        )


@pytest.mark.parametrize("value", ["A" * 64, "a" * 63, "a" * 65, "g" * 64])
def test_road_archive_sha256_requires_canonical_lowercase(value: str) -> None:
    source = _source()
    extraction = replace(
        source.extraction,
        archive=replace(source.extraction.archive, sha256=value),
    )

    with pytest.raises(IgnRoadNormalizationError):
        normalize_ign_roads(replace(source, extraction=extraction), SOURCE_CONFIG)


def test_summary_crs_mismatch_is_rejected() -> None:
    source = _source()
    summary = replace(source.road_segments_summary, crs="EPSG:4326")

    with pytest.raises(
        IgnRoadNormalizationError,
        match="summary|physical|CRS|2154",
    ):
        normalize_ign_roads(
            replace(source, road_segments_summary=summary), SOURCE_CONFIG
        )


@pytest.mark.parametrize("mutation", ["missing", "extra", "reordered", "dtype"])
def test_forged_ordered_summary_schema_is_rejected(mutation: str) -> None:
    source = _source()
    summary = source.road_segments_summary
    if mutation == "missing":
        changed = replace(summary, columns=summary.columns[:-1])
    elif mutation == "extra":
        changed = replace(summary, columns=(*summary.columns, "invented"))
    elif mutation == "reordered":
        changed = replace(summary, columns=tuple(reversed(summary.columns)))
    else:
        dtypes = list(summary.dtypes)
        dtypes[0] = (dtypes[0][0], "float64")
        changed = replace(summary, dtypes=tuple(dtypes))

    with pytest.raises(
        IgnRoadNormalizationError,
        match="summary|physical|schema|columns|dtype",
    ):
        normalize_ign_roads(
            replace(source, road_segments_summary=changed), SOURCE_CONFIG
        )


@pytest.mark.parametrize("role", ["electric", "post"])
def test_road_source_rejects_physical_role_collision(role: str) -> None:
    source = _source()
    selected = (
        source.extraction.electric_lines_layer
        if role == "electric"
        else source.extraction.transformation_posts_layer
    )
    summary = replace(source.road_segments_summary, source_layer_name=selected)
    with pytest.raises(
        IgnRoadNormalizationError,
        match="summary|physical|same layer|distinct|role",
    ):
        normalize_ign_roads(
            replace(
                source,
                road_segments_summary=summary,
            ),
            SOURCE_CONFIG,
        )


def test_road_source_rejects_duplicate_layer_inventory() -> None:
    source = _source()
    extraction = replace(
        source.extraction,
        all_layer_names=(*source.extraction.all_layer_names, ROAD_LAYER),
    )

    with pytest.raises(
        IgnRoadNormalizationError,
        match="integrity|inventory|duplicate",
    ):
        normalize_ign_roads(replace(source, extraction=extraction), SOURCE_CONFIG)


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("null_geometry_count", 1),
        ("empty_geometry_count", 1),
        ("invalid_geometry_count", 1),
        ("geometry_types", ("MultiLineString",)),
    ],
)
def test_summary_geometry_facts_mismatch_is_rejected(
    field: str,
    value: object,
) -> None:
    source = _source()
    summary = replace(source.road_segments_summary, **{field: value})

    with pytest.raises(
        IgnRoadNormalizationError,
        match="summary|physical|geometry summary",
    ):
        normalize_ign_roads(
            replace(source, road_segments_summary=summary), SOURCE_CONFIG
        )


def test_summary_layer_must_exist_in_extraction_inventory() -> None:
    source = _source()
    extraction = replace(source.extraction, all_layer_names=("other_layer",))

    with pytest.raises(
        IgnRoadNormalizationError,
        match="integrity|layer inventory",
    ):
        normalize_ign_roads(replace(source, extraction=extraction), SOURCE_CONFIG)


def test_summary_layer_and_logical_name_must_be_exact() -> None:
    source = _source()
    wrong_layer = replace(source.road_segments_summary, source_layer_name="route")
    with pytest.raises(IgnRoadNormalizationError, match="summary|physical layer"):
        normalize_ign_roads(
            replace(source, road_segments_summary=wrong_layer), SOURCE_CONFIG
        )

    wrong_logical = replace(
        source.road_segments_summary,
        logical_name=cast(Any, "electric_lines"),
    )
    with pytest.raises(IgnRoadNormalizationError, match="summary|logical name"):
        normalize_ign_roads(
            replace(source, road_segments_summary=wrong_logical), SOURCE_CONFIG
        )


@pytest.mark.parametrize(
    "geometry",
    [Point(1, 1), Polygon([(0, 0), (0, 1), (1, 1), (1, 0), (0, 0)])],
)
def test_valid_unsupported_geometry_type_is_rejected(geometry: object) -> None:
    with pytest.raises(IgnRoadNormalizationError, match="geometry types"):
        normalize_ign_roads(_source(_road_frame([geometry])), SOURCE_CONFIG)


def test_null_empty_and_invalid_geometry_are_preserved_with_status() -> None:
    invalid = Polygon([(0, 0), (2, 2), (2, 0), (0, 2), (0, 0)])
    frame = _road_frame(
        [None, LineString(), invalid],
        identifiers=["NULL", "EMPTY", "INVALID"],
    )

    roads = normalize_ign_roads(_source(frame), SOURCE_CONFIG).road_segments

    assert roads["geometry_status"].tolist() == ["NULL", "EMPTY", "INVALID"]
    assert roads.geometry.iloc[0] is None
    assert roads.geometry.iloc[1].is_empty
    assert roads.geometry.iloc[2].equals_exact(invalid, tolerance=0)


def test_normalization_does_not_mutate_input() -> None:
    source = _source()
    before = deepcopy(source.road_segments)

    normalize_ign_roads(source, SOURCE_CONFIG)

    assert_geodataframe_equal(source.road_segments, before)


def test_road_normalization_uses_distinct_fresh_revalidated_frame(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    source = _source()
    fresh = replace(
        source,
        road_segments=source.road_segments.copy(deep=True),
    )
    expected_nature = fresh.road_segments.loc[0, "nature"]

    def return_fresh_and_mutate_supplied(
        _: object,
        __: object,
    ) -> IgnBdTopoRoadData:
        source.road_segments.loc[0, "nature"] = "FORGED AFTER REVALIDATION"
        return fresh

    monkeypatch.setattr(
        road_normalization,
        "_revalidate_ign_bdtopo_road_data",
        return_fresh_and_mutate_supplied,
    )

    normalized = normalize_ign_roads(source, SOURCE_CONFIG)

    assert normalized.road_segments.loc[0, "nature_raw"] == expected_nature
    assert source.road_segments.loc[0, "nature"] == "FORGED AFTER REVALIDATION"


def test_high_level_rejects_coordinated_road_frame_and_summary_forgery() -> None:
    source = _source()
    forged = source.road_segments.copy()
    forged.loc[0, "nature"] = "Invented road nature"
    forged_summary = _summary(forged)

    with pytest.raises(IgnRoadNormalizationError, match="physical|fresh|source"):
        normalize_ign_roads(
            replace(
                source,
                road_segments=forged,
                road_segments_summary=forged_summary,
            ),
            SOURCE_CONFIG,
        )


def test_malformed_public_input_has_controlled_error() -> None:
    with pytest.raises(IgnRoadNormalizationError):
        normalize_ign_roads(cast(Any, object()), SOURCE_CONFIG)
```

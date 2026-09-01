# `tests/unit/test_normalize_grid_ign.py`

## File identity

- Repository path: `tests/unit/test_normalize_grid_ign.py`
- File type: Python source
- Layer: unit/regression test
- Domain: isolated contract test evidence
- Responsibility: Provides complete unit and regression coverage for the `normalize_grid_ign` contracts exercised in this file.
- Source SHA256: `1a25cd5fb8517d9d4065c2af6c5517d6bb75b0ae2a599fc90f3f925ba1659c20`

## 1. STEP 7F.1A.4 contract delta

- Refreshes permanent STEP 7F.1A.4 regression coverage for normalize grid ign; the exact fixtures, mutations, calls, controlled failures, and assertions are inventoried below.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Provides complete unit and regression coverage for the `normalize_grid_ign` contracts exercised in this file.

The file belongs to the **unit/regression test** layer and **isolated contract test evidence** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `import json`
- `import tempfile`
- `from copy import deepcopy`
- `from dataclasses import replace`
- `from hashlib import sha256`
- `from math import isfinite`
- `from pathlib import Path`
- `from typing import Any, Literal, cast`
- `from uuid import uuid4`

### Third-party packages

- `import geopandas as gpd`
- `import numpy as np`
- `import pandas as pd`
- `import pyogrio`
- `import pytest`
- `from geopandas.testing import assert_geodataframe_equal`
- `from shapely.geometry import (
    LineString,
    MultiLineString,
    MultiPolygon,
    Point,
    Polygon,
)`

### Internal LandScout imports

- `import landscout.stages.normalize_grid_ign as grid_normalization`
- `from landscout import stages`
- `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_source_config,
)`
- `from landscout.stages.normalize_grid_ign import (
    LINE_OUTPUT_COLUMNS,
    TRANSFORMATION_POST_OUTPUT_COLUMNS,
    IgnGridNormalizationError,
    NormalizedIgnElectricityData,
    parse_ign_voltage,
)`
- `from landscout.stages.normalize_grid_ign import (
    _IgnGridSourceContext as IgnGridSourceContext,
)`
- `from landscout.stages.normalize_grid_ign import (
    _normalize_ign_electric_lines as normalize_ign_electric_lines,
)`
- `from landscout.stages.normalize_grid_ign import (
    _normalize_ign_transformation_posts as normalize_ign_transformation_posts,
)`
- `from landscout.stages.normalize_grid_ign import (
    normalize_ign_electricity as _normalize_ign_electricity,
)`

## 4. Contract taxonomy

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `LINE_LAYER`

- Category: module constant or closed domain.
- Exact declaration:

```python
LINE_LAYER = "LIGNE_ELECTRIQUE_V2"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `POST_LAYER`

- Category: module constant or closed domain.
- Exact declaration:

```python
POST_LAYER = "POSTE_DE_TRANSFORMATION_V2"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `ROAD_LAYER`

- Category: module constant or closed domain.
- Exact declaration:

```python
ROAD_LAYER = "TRONCON_DE_ROUTE"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `DEPARTMENT_LAYER`

- Category: module constant or closed domain.
- Exact declaration:

```python
DEPARTMENT_LAYER = "DEPARTEMENT"
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
_FIXTURE_ROOT = Path(tempfile.mkdtemp(prefix="landscout-grid-ign-"))
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


### Executable module-import-time statements

### Module-import-time executable statement at line 65

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

### `normalize_ign_electricity`

**Purpose:** Implements `normalize ign electricity` within the file role: Provides complete unit and regression coverage for the `normalize_grid_ign` contracts exercised in this file.

**Exact signature**

```python
def normalize_ign_electricity(
    source: IgnBdTopoElectricityData,
) -> NormalizedIgnElectricityData:
```

- Exact decorators: none.
- Declared return annotation: `NormalizedIgnElectricityData`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source` | positional-or-keyword | `IgnBdTopoElectricityData` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_normalize_ign_electricity(source, SOURCE_CONFIG)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_normalize_grid_ign::test_grid_summary_requires_strict_structural_types` via `normalize_ign_electricity`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_grid_summary_requires_strict_structural_types` via `normalize_ign_electricity`
- direct call: `tests.unit.test_normalize_grid_ign::test_grid_archive_sha256_requires_canonical_lowercase` via `normalize_ign_electricity`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_grid_archive_sha256_requires_canonical_lowercase` via `normalize_ign_electricity`
- direct call: `tests.unit.test_normalize_grid_ign::test_high_level_path_uses_discovered_layer_names_and_archive_lineage` via `normalize_ign_electricity`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_high_level_path_uses_discovered_layer_names_and_archive_lineage` via `normalize_ign_electricity`
- direct call: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_coordinated_frame_and_summary_forgery` via `normalize_ign_electricity`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_coordinated_frame_and_summary_forgery` via `normalize_ign_electricity`
- direct call: `tests.unit.test_normalize_grid_ign::test_source_complete_grid_validation_does_not_mutate_supplied_frames` via `normalize_ign_electricity`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_source_complete_grid_validation_does_not_mutate_supplied_frames` via `normalize_ign_electricity`
- direct call: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_incompatible_archive_identity` via `normalize_ign_electricity`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_incompatible_archive_identity` via `normalize_ign_electricity`
- direct call: `tests.unit.test_normalize_grid_ign::test_archive_identity_requires_exact_pinned_strings` via `normalize_ign_electricity`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_archive_identity_requires_exact_pinned_strings` via `normalize_ign_electricity`
- direct call: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_summary_row_count_mismatch` via `normalize_ign_electricity`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_summary_row_count_mismatch` via `normalize_ign_electricity`
- direct call: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_summary_layer_name_mismatch` via `normalize_ign_electricity`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_summary_layer_name_mismatch` via `normalize_ign_electricity`
- direct call: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_wrong_logical_name` via `normalize_ign_electricity`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_wrong_logical_name` via `normalize_ign_electricity`
- direct call: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_summary_crs_mismatch` via `normalize_ign_electricity`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_summary_crs_mismatch` via `normalize_ign_electricity`
- direct call: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_forged_ordered_summary_schema` via `normalize_ign_electricity`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_forged_ordered_summary_schema` via `normalize_ign_electricity`
- direct call: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_duplicate_or_missing_layer_inventory` via `normalize_ign_electricity`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_duplicate_or_missing_layer_inventory` via `normalize_ign_electricity`
- direct call: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_colliding_electricity_roles` via `normalize_ign_electricity`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_colliding_electricity_roles` via `normalize_ign_electricity`
- direct call: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_stale_geometry_counts_after_frame_mutation` via `normalize_ign_electricity`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_stale_geometry_counts_after_frame_mutation` via `normalize_ign_electricity`
- direct call: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_stale_geometry_types_after_frame_mutation` via `normalize_ign_electricity`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_stale_geometry_types_after_frame_mutation` via `normalize_ign_electricity`
- direct call: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_any_spatial_role_mismatch` via `normalize_ign_electricity`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_any_spatial_role_mismatch` via `normalize_ign_electricity`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_normalize_ign_electricity` | `landscout.stages.normalize_grid_ign.normalize_ign_electricity` |

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
def normalize_ign_electricity(
    source: IgnBdTopoElectricityData,
) -> NormalizedIgnElectricityData:
    return _normalize_ign_electricity(source, SOURCE_CONFIG)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_line_source`

**Purpose:** Implements `line source` within the file role: Provides complete unit and regression coverage for the `normalize_grid_ign` contracts exercised in this file.

**Exact signature**

```python
def _line_source(
    geometries: list[object] | None = None,
    *,
    identifiers: list[object] | None = None,
    voltages: list[object] | None = None,
    precisions: list[object] | None = None,
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
| `voltages` | keyword-only | `list[object] \| None` | `None` |
| `precisions` | keyword-only | `list[object] \| None` | `None` |
| `crs` | keyword-only | `str \| None` | `'EPSG:2154'` |
| `index` | keyword-only | `list[object] \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `gpd.GeoDataFrame(<br>        {<br>            "cleabs": source_ids,<br>            "voltage": source_voltages,<br>            "gestionnaire": ["Réseau de Transport d'Électricité"] * count,<br>            "siren_gestionnaire": ["444619258"] * count,<br>            "etat_de_l_objet": ["En service"] * count,<br>            "sources": ["RTE 2024"] * count,<br>            "identifiants_sources": ["source-id"] * count,<br>            "date_creation": pd.to_datetime(["2024-01-01"] * count),<br>            "date_modification": pd.to_datetime(["2025-01-01"] * count),<br>            "date_de_confirmation": pd.to_datetime(["2024-12-18"] * count),<br>            "methode_d_acquisition_planimetrique": ["Photogrammétrie"] * count,<br>            "precision_planimetrique": source_precisions,<br>        },<br>        geometry=source_geometries,<br>        crs=crs,<br>        index=source_index,<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_normalize_grid_ign::_source_bundle` via `_line_source`
- value/type reference: `tests.unit.test_normalize_grid_ign::_source_bundle` via `_line_source`
- direct call: `tests.unit.test_normalize_grid_ign::test_internal_source_context_rejects_uppercase_sha256` via `_line_source`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_internal_source_context_rejects_uppercase_sha256` via `_line_source`
- direct call: `tests.unit.test_normalize_grid_ign::test_valid_line_has_stable_identity_lineage_and_range_index` via `_line_source`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_valid_line_has_stable_identity_lineage_and_range_index` via `_line_source`
- direct call: `tests.unit.test_normalize_grid_ign::test_deenergized_voltage_does_not_override_source_asset_status` via `_line_source`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_deenergized_voltage_does_not_override_source_asset_status` via `_line_source`
- direct call: `tests.unit.test_normalize_grid_ign::test_null_or_empty_line_cleabs_fails` via `_line_source`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_null_or_empty_line_cleabs_fails` via `_line_source`
- direct call: `tests.unit.test_normalize_grid_ign::test_unsafe_source_id_is_rejected_without_rewriting` via `_line_source`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_unsafe_source_id_is_rejected_without_rewriting` via `_line_source`
- direct call: `tests.unit.test_normalize_grid_ign::test_duplicate_line_cleabs_fails` via `_line_source`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_duplicate_line_cleabs_fails` via `_line_source`
- direct call: `tests.unit.test_normalize_grid_ign::test_line_missing_or_wrong_crs_fails` via `_line_source`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_line_missing_or_wrong_crs_fails` via `_line_source`
- direct call: `tests.unit.test_normalize_grid_ign::test_line_geometry_quality_is_preserved_without_row_loss_or_repair` via `_line_source`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_line_geometry_quality_is_preserved_without_row_loss_or_repair` via `_line_source`
- direct call: `tests.unit.test_normalize_grid_ign::test_z_coordinates_are_preserved` via `_line_source`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_z_coordinates_are_preserved` via `_line_source`
- direct call: `tests.unit.test_normalize_grid_ign::test_unusual_duplicate_source_index_is_not_preserved_as_identity` via `_line_source`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_unusual_duplicate_source_index_is_not_preserved_as_identity` via `_line_source`
- direct call: `tests.unit.test_normalize_grid_ign::test_line_normalization_does_not_mutate_input_and_has_stable_columns` via `_line_source`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_line_normalization_does_not_mutate_input_and_has_stable_columns` via `_line_source`
- direct call: `tests.unit.test_normalize_grid_ign::test_missing_required_line_field_fails` via `_line_source`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_missing_required_line_field_fails` via `_line_source`
- direct call: `tests.unit.test_normalize_grid_ign::test_valid_or_null_line_precision_is_normalized_to_float` via `_line_source`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_valid_or_null_line_precision_is_normalized_to_float` via `_line_source`
- direct call: `tests.unit.test_normalize_grid_ign::test_invalid_line_precision_fails` via `_line_source`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_invalid_line_precision_fails` via `_line_source`
- direct call: `tests.unit.test_normalize_grid_ign::test_normalized_voltage_never_emits_non_finite_numeric_values` via `_line_source`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_normalized_voltage_never_emits_non_finite_numeric_values` via `_line_source`
- direct call: `tests.unit.test_normalize_grid_ign::test_appropriate_multigeometry_types_are_accepted` via `_line_source`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_appropriate_multigeometry_types_are_accepted` via `_line_source`
- direct call: `tests.unit.test_normalize_grid_ign::test_valid_polygon_or_point_is_rejected_as_electric_line` via `_line_source`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_valid_polygon_or_point_is_rejected_as_electric_line` via `_line_source`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `LineString` | `shapely.geometry.LineString` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `range` | `unresolved local/third-party receiver; no ownership inferred` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `pd.to_datetime` | `pandas.to_datetime` |

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
def _line_source(
    geometries: list[object] | None = None,
    *,
    identifiers: list[object] | None = None,
    voltages: list[object] | None = None,
    precisions: list[object] | None = None,
    crs: str | None = "EPSG:2154",
    index: list[object] | None = None,
) -> gpd.GeoDataFrame:
    source_geometries = (
        geometries if geometries is not None else [LineString([(0, 0), (100, 100)])]
    )
    count = len(source_geometries)
    source_ids = (
        identifiers
        if identifiers is not None
        else [f"LIGNE-{item + 1}" for item in range(count)]
    )
    source_voltages = voltages if voltages is not None else ["225 kV"] * count
    source_precisions = precisions if precisions is not None else [2.5] * count
    source_index = index if index is not None else [100 + item for item in range(count)]
    return gpd.GeoDataFrame(
        {
            "cleabs": source_ids,
            "voltage": source_voltages,
            "gestionnaire": ["Réseau de Transport d'Électricité"] * count,
            "siren_gestionnaire": ["444619258"] * count,
            "etat_de_l_objet": ["En service"] * count,
            "sources": ["RTE 2024"] * count,
            "identifiants_sources": ["source-id"] * count,
            "date_creation": pd.to_datetime(["2024-01-01"] * count),
            "date_modification": pd.to_datetime(["2025-01-01"] * count),
            "date_de_confirmation": pd.to_datetime(["2024-12-18"] * count),
            "methode_d_acquisition_planimetrique": ["Photogrammétrie"] * count,
            "precision_planimetrique": source_precisions,
        },
        geometry=source_geometries,
        crs=crs,
        index=source_index,
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_post_source`

**Purpose:** Implements `post source` within the file role: Provides complete unit and regression coverage for the `normalize_grid_ign` contracts exercised in this file.

**Exact signature**

```python
def _post_source(
    geometries: list[object] | None = None,
    *,
    identifiers: list[object] | None = None,
    precisions: list[object] | None = None,
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
| `precisions` | keyword-only | `list[object] \| None` | `None` |
| `crs` | keyword-only | `str \| None` | `'EPSG:2154'` |
| `index` | keyword-only | `list[object] \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `gpd.GeoDataFrame(<br>        {<br>            "cleabs": source_ids,<br>            "toponyme": ["Poste de test"] * count,<br>            "statut_du_toponyme": ["Validé"] * count,<br>            "importance": ["5"] * count,<br>            "etat_de_l_objet": ["En service"] * count,<br>            "sources": ["RTE 2021"] * count,<br>            "identifiants_sources": ["source-post-id"] * count,<br>            "date_creation": pd.to_datetime(["2023-01-01"] * count),<br>            "date_modification": pd.to_datetime(["2025-02-01"] * count),<br>            "date_de_confirmation": pd.to_datetime(["2025-01-15"] * count),<br>            "methode_d_acquisition_planimetrique": ["Orthophotographie"] * count,<br>            "precision_planimetrique": source_precisions,<br>        },<br>        geometry=source_geometries,<br>        crs=crs,<br>        index=source_index,<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_normalize_grid_ign::_source_bundle` via `_post_source`
- value/type reference: `tests.unit.test_normalize_grid_ign::_source_bundle` via `_post_source`
- direct call: `tests.unit.test_normalize_grid_ign::test_valid_post_has_stable_lineage_and_no_voltage_inference` via `_post_source`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_valid_post_has_stable_lineage_and_no_voltage_inference` via `_post_source`
- direct call: `tests.unit.test_normalize_grid_ign::test_post_geometry_crs_and_input_are_preserved` via `_post_source`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_post_geometry_crs_and_input_are_preserved` via `_post_source`
- direct call: `tests.unit.test_normalize_grid_ign::test_duplicate_post_cleabs_fails` via `_post_source`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_duplicate_post_cleabs_fails` via `_post_source`
- direct call: `tests.unit.test_normalize_grid_ign::test_null_post_geometry_and_precision_are_preserved` via `_post_source`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_null_post_geometry_and_precision_are_preserved` via `_post_source`
- direct call: `tests.unit.test_normalize_grid_ign::test_invalid_post_precision_fails` via `_post_source`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_invalid_post_precision_fails` via `_post_source`
- direct call: `tests.unit.test_normalize_grid_ign::test_appropriate_multigeometry_types_are_accepted` via `_post_source`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_appropriate_multigeometry_types_are_accepted` via `_post_source`
- direct call: `tests.unit.test_normalize_grid_ign::test_valid_line_or_point_is_rejected_as_transformation_post` via `_post_source`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_valid_line_or_point_is_rejected_as_transformation_post` via `_post_source`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `Polygon` | `shapely.geometry.Polygon` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `range` | `unresolved local/third-party receiver; no ownership inferred` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `pd.to_datetime` | `pandas.to_datetime` |

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
def _post_source(
    geometries: list[object] | None = None,
    *,
    identifiers: list[object] | None = None,
    precisions: list[object] | None = None,
    crs: str | None = "EPSG:2154",
    index: list[object] | None = None,
) -> gpd.GeoDataFrame:
    source_geometries = (
        geometries
        if geometries is not None
        else [Polygon([(0, 0), (0, 20), (20, 20), (20, 0), (0, 0)])]
    )
    count = len(source_geometries)
    source_ids = (
        identifiers
        if identifiers is not None
        else [f"POSTE-{item + 1}" for item in range(count)]
    )
    source_precisions = precisions if precisions is not None else [5.0] * count
    source_index = index if index is not None else [200 + item for item in range(count)]
    return gpd.GeoDataFrame(
        {
            "cleabs": source_ids,
            "toponyme": ["Poste de test"] * count,
            "statut_du_toponyme": ["Validé"] * count,
            "importance": ["5"] * count,
            "etat_de_l_objet": ["En service"] * count,
            "sources": ["RTE 2021"] * count,
            "identifiants_sources": ["source-post-id"] * count,
            "date_creation": pd.to_datetime(["2023-01-01"] * count),
            "date_modification": pd.to_datetime(["2025-02-01"] * count),
            "date_de_confirmation": pd.to_datetime(["2025-01-15"] * count),
            "methode_d_acquisition_planimetrique": ["Orthophotographie"] * count,
            "precision_planimetrique": source_precisions,
        },
        geometry=source_geometries,
        crs=crs,
        index=source_index,
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_context`

**Purpose:** Implements `context` within the file role: Provides complete unit and regression coverage for the `normalize_grid_ign` contracts exercised in this file.

**Exact signature**

```python
def _context(source_layer: str) -> IgnGridSourceContext:
```

- Exact decorators: none.
- Declared return annotation: `IgnGridSourceContext`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source_layer` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `IgnGridSourceContext(<br>        source_layer=source_layer,<br>        department_code="31",<br>        edition="2026-06-15",<br>        product_version="3.5",<br>        download_timestamp="2026-08-11T15:32:03+00:00",<br>        archive_sha256=ARCHIVE_SHA256,<br>        source_url=SOURCE_URL,<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_normalize_grid_ign::test_internal_source_context_accepts_supported_department_codes` via `_context`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_internal_source_context_accepts_supported_department_codes` via `_context`
- direct call: `tests.unit.test_normalize_grid_ign::test_internal_source_context_rejects_uppercase_sha256` via `_context`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_internal_source_context_rejects_uppercase_sha256` via `_context`
- direct call: `tests.unit.test_normalize_grid_ign::test_internal_source_context_rejects_invalid_lineage_values` via `_context`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_internal_source_context_rejects_invalid_lineage_values` via `_context`
- direct call: `tests.unit.test_normalize_grid_ign::test_valid_line_has_stable_identity_lineage_and_range_index` via `_context`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_valid_line_has_stable_identity_lineage_and_range_index` via `_context`
- direct call: `tests.unit.test_normalize_grid_ign::test_deenergized_voltage_does_not_override_source_asset_status` via `_context`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_deenergized_voltage_does_not_override_source_asset_status` via `_context`
- direct call: `tests.unit.test_normalize_grid_ign::test_null_or_empty_line_cleabs_fails` via `_context`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_null_or_empty_line_cleabs_fails` via `_context`
- direct call: `tests.unit.test_normalize_grid_ign::test_unsafe_source_id_is_rejected_without_rewriting` via `_context`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_unsafe_source_id_is_rejected_without_rewriting` via `_context`
- direct call: `tests.unit.test_normalize_grid_ign::test_duplicate_line_cleabs_fails` via `_context`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_duplicate_line_cleabs_fails` via `_context`
- direct call: `tests.unit.test_normalize_grid_ign::test_line_missing_or_wrong_crs_fails` via `_context`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_line_missing_or_wrong_crs_fails` via `_context`
- direct call: `tests.unit.test_normalize_grid_ign::test_line_geometry_quality_is_preserved_without_row_loss_or_repair` via `_context`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_line_geometry_quality_is_preserved_without_row_loss_or_repair` via `_context`
- direct call: `tests.unit.test_normalize_grid_ign::test_z_coordinates_are_preserved` via `_context`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_z_coordinates_are_preserved` via `_context`
- direct call: `tests.unit.test_normalize_grid_ign::test_unusual_duplicate_source_index_is_not_preserved_as_identity` via `_context`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_unusual_duplicate_source_index_is_not_preserved_as_identity` via `_context`
- direct call: `tests.unit.test_normalize_grid_ign::test_line_normalization_does_not_mutate_input_and_has_stable_columns` via `_context`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_line_normalization_does_not_mutate_input_and_has_stable_columns` via `_context`
- direct call: `tests.unit.test_normalize_grid_ign::test_missing_required_line_field_fails` via `_context`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_missing_required_line_field_fails` via `_context`
- direct call: `tests.unit.test_normalize_grid_ign::test_valid_or_null_line_precision_is_normalized_to_float` via `_context`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_valid_or_null_line_precision_is_normalized_to_float` via `_context`
- direct call: `tests.unit.test_normalize_grid_ign::test_invalid_line_precision_fails` via `_context`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_invalid_line_precision_fails` via `_context`
- direct call: `tests.unit.test_normalize_grid_ign::test_normalized_voltage_never_emits_non_finite_numeric_values` via `_context`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_normalized_voltage_never_emits_non_finite_numeric_values` via `_context`
- direct call: `tests.unit.test_normalize_grid_ign::test_valid_post_has_stable_lineage_and_no_voltage_inference` via `_context`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_valid_post_has_stable_lineage_and_no_voltage_inference` via `_context`
- direct call: `tests.unit.test_normalize_grid_ign::test_post_geometry_crs_and_input_are_preserved` via `_context`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_post_geometry_crs_and_input_are_preserved` via `_context`
- direct call: `tests.unit.test_normalize_grid_ign::test_duplicate_post_cleabs_fails` via `_context`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_duplicate_post_cleabs_fails` via `_context`
- direct call: `tests.unit.test_normalize_grid_ign::test_null_post_geometry_and_precision_are_preserved` via `_context`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_null_post_geometry_and_precision_are_preserved` via `_context`
- direct call: `tests.unit.test_normalize_grid_ign::test_invalid_post_precision_fails` via `_context`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_invalid_post_precision_fails` via `_context`
- direct call: `tests.unit.test_normalize_grid_ign::test_appropriate_multigeometry_types_are_accepted` via `_context`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_appropriate_multigeometry_types_are_accepted` via `_context`
- direct call: `tests.unit.test_normalize_grid_ign::test_valid_polygon_or_point_is_rejected_as_electric_line` via `_context`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_valid_polygon_or_point_is_rejected_as_electric_line` via `_context`
- direct call: `tests.unit.test_normalize_grid_ign::test_valid_line_or_point_is_rejected_as_transformation_post` via `_context`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_valid_line_or_point_is_rejected_as_transformation_post` via `_context`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `IgnGridSourceContext` | `landscout.stages.normalize_grid_ign._IgnGridSourceContext` |

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
def _context(source_layer: str) -> IgnGridSourceContext:
    return IgnGridSourceContext(
        source_layer=source_layer,
        department_code="31",
        edition="2026-06-15",
        product_version="3.5",
        download_timestamp="2026-08-11T15:32:03+00:00",
        archive_sha256=ARCHIVE_SHA256,
        source_url=SOURCE_URL,
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_summary`

**Purpose:** Implements `summary` within the file role: Provides complete unit and regression coverage for the `normalize_grid_ign` contracts exercised in this file.

**Exact signature**

```python
def _summary(
    frame: gpd.GeoDataFrame,
    logical_name: Literal["electric_lines", "transformation_posts"],
    layer_name: str,
) -> IgnBdTopoLayerSummary:
```

- Exact decorators: none.
- Declared return annotation: `IgnBdTopoLayerSummary`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `logical_name` | positional-or-keyword | `Literal['electric_lines', 'transformation_posts']` | `required` |
| `layer_name` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `IgnBdTopoLayerSummary(<br>        logical_name=logical_name,<br>        source_layer_name=layer_name,<br>        crs=str(frame.crs),<br>        feature_count=len(frame),<br>        columns=tuple(str(column) for column in frame.columns),<br>        dtypes=tuple(<br>            (str(column), str(dtype)) for column, dtype in frame.dtypes.items()<br>        ),<br>        null_geometry_count=int(null_mask.sum()),<br>        empty_geometry_count=int(empty_mask.sum()),<br>        invalid_geometry_count=int(invalid_mask.sum()),<br>        geometry_types=geometry_types,<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_normalize_grid_ign::_source_bundle` via `_summary`
- value/type reference: `tests.unit.test_normalize_grid_ign::_source_bundle` via `_summary`
- direct call: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_coordinated_frame_and_summary_forgery` via `_summary`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_coordinated_frame_and_summary_forgery` via `_summary`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `geometry.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry[~null_mask].geom_type.dropna().unique` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry[~null_mask].geom_type.dropna` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoLayerSummary` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoLayerSummary` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.dtypes.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `int` | `unresolved local/third-party receiver; no ownership inferred` |
| `null_mask.sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `empty_mask.sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `invalid_mask.sum` | `unresolved local/third-party receiver; no ownership inferred` |

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
    logical_name: Literal["electric_lines", "transformation_posts"],
    layer_name: str,
) -> IgnBdTopoLayerSummary:
    geometry = frame.geometry
    null_mask = geometry.isna()
    empty_mask = ~null_mask & geometry.is_empty
    invalid_mask = ~null_mask & ~geometry.is_empty & ~geometry.is_valid
    geometry_types = tuple(
        sorted(str(value) for value in geometry[~null_mask].geom_type.dropna().unique())
    )
    return IgnBdTopoLayerSummary(
        logical_name=logical_name,
        source_layer_name=layer_name,
        crs=str(frame.crs),
        feature_count=len(frame),
        columns=tuple(str(column) for column in frame.columns),
        dtypes=tuple(
            (str(column), str(dtype)) for column, dtype in frame.dtypes.items()
        ),
        null_geometry_count=int(null_mask.sum()),
        empty_geometry_count=int(empty_mask.sum()),
        invalid_geometry_count=int(invalid_mask.sum()),
        geometry_types=geometry_types,
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_source_bundle`

**Purpose:** Implements `source bundle` within the file role: Provides complete unit and regression coverage for the `normalize_grid_ign` contracts exercised in this file.

**Exact signature**

```python
def _source_bundle(
    lines: gpd.GeoDataFrame | None = None,
    posts: gpd.GeoDataFrame | None = None,
) -> IgnBdTopoElectricityData:
```

- Exact decorators: none.
- Declared return annotation: `IgnBdTopoElectricityData`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `lines` | positional-or-keyword | `gpd.GeoDataFrame \| None` | `None` |
| `posts` | positional-or-keyword | `gpd.GeoDataFrame \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `IgnBdTopoElectricityData(<br>        extraction=extraction,<br>        electric_lines=line_frame,<br>        transformation_posts=post_frame,<br>        electric_lines_summary=_summary(line_frame, "electric_lines", LINE_LAYER),<br>        transformation_posts_summary=_summary(<br>            post_frame, "transformation_posts", POST_LAYER<br>        ),<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_normalize_grid_ign::_source_bundle_with_archive` via `_source_bundle`
- value/type reference: `tests.unit.test_normalize_grid_ign::_source_bundle_with_archive` via `_source_bundle`
- direct call: `tests.unit.test_normalize_grid_ign::test_supported_package_api_keeps_high_level_normalization` via `_source_bundle`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_supported_package_api_keeps_high_level_normalization` via `_source_bundle`
- direct call: `tests.unit.test_normalize_grid_ign::test_grid_summary_requires_strict_structural_types` via `_source_bundle`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_grid_summary_requires_strict_structural_types` via `_source_bundle`
- direct call: `tests.unit.test_normalize_grid_ign::test_high_level_path_uses_discovered_layer_names_and_archive_lineage` via `_source_bundle`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_high_level_path_uses_discovered_layer_names_and_archive_lineage` via `_source_bundle`
- direct call: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_coordinated_frame_and_summary_forgery` via `_source_bundle`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_coordinated_frame_and_summary_forgery` via `_source_bundle`
- direct call: `tests.unit.test_normalize_grid_ign::test_source_complete_grid_validation_does_not_mutate_supplied_frames` via `_source_bundle`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_source_complete_grid_validation_does_not_mutate_supplied_frames` via `_source_bundle`
- direct call: `tests.unit.test_normalize_grid_ign::test_grid_normalization_uses_distinct_fresh_revalidated_frames` via `_source_bundle`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_grid_normalization_uses_distinct_fresh_revalidated_frames` via `_source_bundle`
- direct call: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_summary_row_count_mismatch` via `_source_bundle`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_summary_row_count_mismatch` via `_source_bundle`
- direct call: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_summary_layer_name_mismatch` via `_source_bundle`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_summary_layer_name_mismatch` via `_source_bundle`
- direct call: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_wrong_logical_name` via `_source_bundle`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_wrong_logical_name` via `_source_bundle`
- direct call: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_summary_crs_mismatch` via `_source_bundle`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_summary_crs_mismatch` via `_source_bundle`
- direct call: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_forged_ordered_summary_schema` via `_source_bundle`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_forged_ordered_summary_schema` via `_source_bundle`
- direct call: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_duplicate_or_missing_layer_inventory` via `_source_bundle`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_duplicate_or_missing_layer_inventory` via `_source_bundle`
- direct call: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_colliding_electricity_roles` via `_source_bundle`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_colliding_electricity_roles` via `_source_bundle`
- direct call: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_stale_geometry_counts_after_frame_mutation` via `_source_bundle`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_stale_geometry_counts_after_frame_mutation` via `_source_bundle`
- direct call: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_stale_geometry_types_after_frame_mutation` via `_source_bundle`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_stale_geometry_types_after_frame_mutation` via `_source_bundle`
- direct call: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_any_spatial_role_mismatch` via `_source_bundle`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_any_spatial_role_mismatch` via `_source_bundle`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_line_source` | `tests.unit.test_normalize_grid_ign._line_source` |
| `_post_source` | `tests.unit.test_normalize_grid_ign._post_source` |
| `uuid4` | `uuid.uuid4` |
| `extraction_path.mkdir` | `unresolved local/third-party receiver; no ownership inferred` |
| `pyogrio.write_dataframe` | `pyogrio.write_dataframe` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `LineString` | `shapely.geometry.LineString` |
| `Polygon` | `shapely.geometry.Polygon` |
| `gpd.read_file` | `geopandas.read_file` |
| `geopackage_path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `pyogrio.list_layers` | `pyogrio.list_layers` |
| `sha256(payload).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `(extraction_path / ".landscout-extraction.json").write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `IgnBdTopoDownload` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoDownload` |
| `Path` | `pathlib.Path` |
| `IgnBdTopoExtraction` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoExtraction` |
| `IgnBdTopoElectricityData` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoElectricityData` |
| `_summary` | `tests.unit.test_normalize_grid_ign._summary` |

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
def _source_bundle(
    lines: gpd.GeoDataFrame | None = None,
    posts: gpd.GeoDataFrame | None = None,
) -> IgnBdTopoElectricityData:
    line_frame = lines if lines is not None else _line_source()
    post_frame = posts if posts is not None else _post_source()
    extraction_path = _FIXTURE_ROOT / uuid4().hex
    extraction_path.mkdir(parents=True)
    geopackage_path = extraction_path / "data.gpkg"
    pyogrio.write_dataframe(
        line_frame, geopackage_path, layer=LINE_LAYER, driver="GPKG"
    )
    pyogrio.write_dataframe(
        post_frame,
        geopackage_path,
        layer=POST_LAYER,
        driver="GPKG",
        append=True,
    )
    pyogrio.write_dataframe(
        gpd.GeoDataFrame(
            {"id": ["road"]},
            geometry=[LineString([(0, 0), (1, 1)])],
            crs="EPSG:2154",
        ),
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
    line_frame = gpd.read_file(geopackage_path, layer=LINE_LAYER, engine="pyogrio")
    post_frame = gpd.read_file(geopackage_path, layer=POST_LAYER, engine="pyogrio")
    payload = geopackage_path.read_bytes()
    layer_names = tuple(str(row[0]) for row in pyogrio.list_layers(geopackage_path))
    digest = sha256(payload).hexdigest()
    marker = {
        "schema_version": 3,
        "archive_sha256": ARCHIVE_SHA256,
        "geopackage_relative_path": "data.gpkg",
        "geopackage_size_bytes": len(payload),
        "geopackage_sha256": digest,
        "all_layer_names": list(layer_names),
        "electric_lines_layer": LINE_LAYER,
        "transformation_posts_layer": POST_LAYER,
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
    (extraction_path / ".landscout-extraction.json").write_text(
        json.dumps(marker), encoding="utf-8"
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
        electric_lines_layer=LINE_LAYER,
        transformation_posts_layer=POST_LAYER,
        road_segments_layer=ROAD_LAYER,
        department_layer=DEPARTMENT_LAYER,
        cache_hit=True,
    )
    return IgnBdTopoElectricityData(
        extraction=extraction,
        electric_lines=line_frame,
        transformation_posts=post_frame,
        electric_lines_summary=_summary(line_frame, "electric_lines", LINE_LAYER),
        transformation_posts_summary=_summary(
            post_frame, "transformation_posts", POST_LAYER
        ),
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_source_bundle_with_archive`

**Purpose:** Implements `source bundle with archive` within the file role: Provides complete unit and regression coverage for the `normalize_grid_ign` contracts exercised in this file.

**Exact signature**

```python
def _source_bundle_with_archive(**changes: object) -> IgnBdTopoElectricityData:
```

- Exact decorators: none.
- Declared return annotation: `IgnBdTopoElectricityData`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `**changes` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- Exact observed return expressions:
  - `replace(source, extraction=replace(source.extraction, archive=archive))`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_normalize_grid_ign::test_grid_archive_sha256_requires_canonical_lowercase` via `_source_bundle_with_archive`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_grid_archive_sha256_requires_canonical_lowercase` via `_source_bundle_with_archive`
- direct call: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_incompatible_archive_identity` via `_source_bundle_with_archive`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_high_level_rejects_incompatible_archive_identity` via `_source_bundle_with_archive`
- direct call: `tests.unit.test_normalize_grid_ign::test_archive_identity_requires_exact_pinned_strings` via `_source_bundle_with_archive`
- value/type reference: `tests.unit.test_normalize_grid_ign::test_archive_identity_requires_exact_pinned_strings` via `_source_bundle_with_archive`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_bundle` | `tests.unit.test_normalize_grid_ign._source_bundle` |
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
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _source_bundle_with_archive(**changes: object) -> IgnBdTopoElectricityData:
    source = _source_bundle()
    archive = replace(source.extraction.archive, **changes)
    return replace(source, extraction=replace(source.extraction, archive=archive))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_low_level_normalization_is_not_part_of_stages_public_api`

**Purpose:** Regression invariant: low level normalization is not part of stages public api. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_low_level_normalization_is_not_part_of_stages_public_api(name: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "name",
    [
        "IgnGridSourceContext",
        "normalize_ign_electric_lines",
        "normalize_ign_transformation_posts",
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `name` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert name not in stages.__all__`
  - `assert not hasattr(stages, name)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `hasattr` | `unresolved local/third-party receiver; no ownership inferred` |
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
def test_low_level_normalization_is_not_part_of_stages_public_api(name: str) -> None:
    assert name not in stages.__all__
    assert not hasattr(stages, name)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_supported_package_api_keeps_high_level_normalization`

**Purpose:** Regression invariant: supported package api keeps high level normalization. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_supported_package_api_keeps_high_level_normalization() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert expected_names <= set(stages.__all__)`
  - `assert normalized.electric_lines["source_layer"].unique().tolist() == [LINE_LAYER]`
  - `assert normalized.transformation_posts["source_layer"].unique().tolist() == [<br>        POST_LAYER<br>    ]`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `stages.normalize_ign_electricity` | `landscout.stages.normalize_ign_electricity` |
| `_source_bundle` | `tests.unit.test_normalize_grid_ign._source_bundle` |
| `normalized.electric_lines["source_layer"].unique().tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `normalized.electric_lines["source_layer"].unique` | `unresolved local/third-party receiver; no ownership inferred` |
| `normalized.transformation_posts["source_layer"].unique().tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `normalized.transformation_posts["source_layer"].unique` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_supported_package_api_keeps_high_level_normalization() -> None:
    expected_names = {
        "IgnGridNormalizationError",
        "IgnVoltageNormalization",
        "NormalizedIgnElectricityData",
        "parse_ign_voltage",
        "normalize_ign_electricity",
    }

    assert expected_names <= set(stages.__all__)
    normalized = stages.normalize_ign_electricity(_source_bundle(), SOURCE_CONFIG)
    assert normalized.electric_lines["source_layer"].unique().tolist() == [LINE_LAYER]
    assert normalized.transformation_posts["source_layer"].unique().tolist() == [
        POST_LAYER
    ]
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_internal_source_context_accepts_supported_department_codes`

**Purpose:** Regression invariant: internal source context accepts supported department codes. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_internal_source_context_accepts_supported_department_codes(
    department_code: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("department_code", ["31", "2A", "2B", "971", "976"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `department_code` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `replace` | `dataclasses.replace` |
| `_context` | `tests.unit.test_normalize_grid_ign._context` |
| `grid_normalization._validate_source_context` | `landscout.stages.normalize_grid_ign._validate_source_context` |
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
def test_internal_source_context_accepts_supported_department_codes(
    department_code: str,
) -> None:
    context = replace(_context(LINE_LAYER), department_code=department_code)

    grid_normalization._validate_source_context(context)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_internal_source_context_rejects_uppercase_sha256`

**Purpose:** Regression invariant: internal source context rejects uppercase sha256. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_internal_source_context_rejects_uppercase_sha256() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnGridNormalizationError, match="archive_sha256")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `replace` | `dataclasses.replace` |
| `_context` | `tests.unit.test_normalize_grid_ign._context` |
| `pytest.raises` | `pytest.raises` |
| `normalize_ign_electric_lines` | `landscout.stages.normalize_grid_ign._normalize_ign_electric_lines` |
| `_line_source` | `tests.unit.test_normalize_grid_ign._line_source` |

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
def test_internal_source_context_rejects_uppercase_sha256() -> None:
    archive_sha256 = "A" * 64
    context = replace(_context(LINE_LAYER), archive_sha256=archive_sha256)

    with pytest.raises(IgnGridNormalizationError, match="archive_sha256"):
        normalize_ign_electric_lines(_line_source(), context)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_grid_summary_requires_strict_structural_types`

**Purpose:** Regression invariant: grid summary requires strict structural types. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_grid_summary_requires_strict_structural_types(
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
  - `pytest.raises(IgnGridNormalizationError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_bundle` | `tests.unit.test_normalize_grid_ign._source_bundle` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `normalize_ign_electricity` | `tests.unit.test_normalize_grid_ign.normalize_ign_electricity` |
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
def test_grid_summary_requires_strict_structural_types(
    field: str, value: object
) -> None:
    source = _source_bundle()
    changed = replace(source.electric_lines_summary, **{field: value})

    with pytest.raises(IgnGridNormalizationError):
        normalize_ign_electricity(replace(source, electric_lines_summary=changed))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_grid_archive_sha256_requires_canonical_lowercase`

**Purpose:** Regression invariant: grid archive sha256 requires canonical lowercase. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_grid_archive_sha256_requires_canonical_lowercase(value: str) -> None:
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
  - `pytest.raises(IgnGridNormalizationError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_bundle_with_archive` | `tests.unit.test_normalize_grid_ign._source_bundle_with_archive` |
| `pytest.raises` | `pytest.raises` |
| `normalize_ign_electricity` | `tests.unit.test_normalize_grid_ign.normalize_ign_electricity` |
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
def test_grid_archive_sha256_requires_canonical_lowercase(value: str) -> None:
    source = _source_bundle_with_archive(sha256=value)

    with pytest.raises(IgnGridNormalizationError):
        normalize_ign_electricity(source)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_internal_source_context_rejects_invalid_lineage_values`

**Purpose:** Regression invariant: internal source context rejects invalid lineage values. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_internal_source_context_rejects_invalid_lineage_values(
    field: str,
    value: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("field", "value"),
    [
        ("source_layer", ""),
        ("source_layer", " LIGNE_ELECTRIQUE "),
        ("source_layer", 42),
        ("department_code", "XYZ"),
        ("edition", "2026-02-31"),
        ("download_timestamp", "not-a-datetime"),
        ("download_timestamp", "2026-08-11T15:32:03"),
        ("archive_sha256", "a" * 63),
        ("archive_sha256", "g" * 64),
        ("source_url", "not-a-url"),
        ("source_url", "file:///tmp/archive.7z"),
        ("product_version", ""),
        ("product_version", " 3.5 "),
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
  - `pytest.raises(IgnGridNormalizationError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `replace` | `dataclasses.replace` |
| `_context` | `tests.unit.test_normalize_grid_ign._context` |
| `pytest.raises` | `pytest.raises` |
| `grid_normalization._validate_source_context` | `landscout.stages.normalize_grid_ign._validate_source_context` |
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
def test_internal_source_context_rejects_invalid_lineage_values(
    field: str,
    value: object,
) -> None:
    context = replace(_context(LINE_LAYER), **{field: value})

    with pytest.raises(IgnGridNormalizationError):
        grid_normalization._validate_source_context(context)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_exact_voltage_parser_is_generic_and_finite`

**Purpose:** Regression invariant: exact voltage parser is generic and finite. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_exact_voltage_parser_is_generic_and_finite(
    raw: str, expected_kv: float
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("raw", "expected_kv"),
    [
        ("63 kV", 63.0),
        ("150 kV", 150.0),
        ("225 kV", 225.0),
        ("400 kV", 400.0),
        ("110 kV", 110.0),
        ("  90 KV  ", 90.0),
        ("72,5 kv", 72.5),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `raw` | positional-or-keyword | `str` | `required` |
| `expected_kv` | positional-or-keyword | `float` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert parsed.raw == raw`
  - `assert parsed.status == "EXACT"`
  - `assert parsed.voltage_kv == expected_kv`
  - `assert parsed.voltage_kv is not None and isfinite(parsed.voltage_kv)`
  - `assert parsed.voltage_upper_bound_kv is None`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `parse_ign_voltage` | `landscout.stages.normalize_grid_ign.parse_ign_voltage` |
| `isfinite` | `math.isfinite` |
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
def test_exact_voltage_parser_is_generic_and_finite(
    raw: str, expected_kv: float
) -> None:
    parsed = parse_ign_voltage(raw)

    assert parsed.raw == raw
    assert parsed.status == "EXACT"
    assert parsed.voltage_kv == expected_kv
    assert parsed.voltage_kv is not None and isfinite(parsed.voltage_kv)
    assert parsed.voltage_upper_bound_kv is None
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_bounded_voltage_is_generic_finite_and_not_exact`

**Purpose:** Regression invariant: bounded voltage is generic finite and not exact. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_bounded_voltage_is_generic_finite_and_not_exact(
    raw: str, expected_upper_bound: float
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("raw", "expected_upper_bound"),
    [("<63 kV", 63.0), ("<90 kV", 90.0), (" < 110 KV ", 110.0)],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `raw` | positional-or-keyword | `str` | `required` |
| `expected_upper_bound` | positional-or-keyword | `float` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert parsed.raw == raw`
  - `assert parsed.status == "BELOW"`
  - `assert parsed.voltage_kv is None`
  - `assert parsed.voltage_upper_bound_kv == expected_upper_bound`
  - `assert isfinite(parsed.voltage_upper_bound_kv)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `parse_ign_voltage` | `landscout.stages.normalize_grid_ign.parse_ign_voltage` |
| `isfinite` | `math.isfinite` |
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
def test_bounded_voltage_is_generic_finite_and_not_exact(
    raw: str, expected_upper_bound: float
) -> None:
    parsed = parse_ign_voltage(raw)

    assert parsed.raw == raw
    assert parsed.status == "BELOW"
    assert parsed.voltage_kv is None
    assert parsed.voltage_upper_bound_kv == expected_upper_bound
    assert isfinite(parsed.voltage_upper_bound_kv)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unknown_voltage_parser`

**Purpose:** Regression invariant: unknown voltage parser. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_unknown_voltage_parser(raw: str | None) -> None:
```

- Exact decorators: `pytest.mark.parametrize("raw", ["Inconnue", " INCONNUE ", "inconnu", None])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `raw` | positional-or-keyword | `str \| None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert parsed.raw == raw`
  - `assert parsed.status == "UNKNOWN"`
  - `assert parsed.voltage_kv is None`
  - `assert parsed.voltage_upper_bound_kv is None`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `parse_ign_voltage` | `landscout.stages.normalize_grid_ign.parse_ign_voltage` |
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
def test_unknown_voltage_parser(raw: str | None) -> None:
    parsed = parse_ign_voltage(raw)

    assert parsed.raw == raw
    assert parsed.status == "UNKNOWN"
    assert parsed.voltage_kv is None
    assert parsed.voltage_upper_bound_kv is None
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_deenergized_voltage_parser`

**Purpose:** Regression invariant: deenergized voltage parser. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_deenergized_voltage_parser(raw: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize("raw", ["Hors tension", " HORS TENSION "])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `raw` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert parsed.raw == raw`
  - `assert parsed.status == "DEENERGIZED"`
  - `assert parsed.voltage_kv is None`
  - `assert parsed.voltage_upper_bound_kv is None`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `parse_ign_voltage` | `landscout.stages.normalize_grid_ign.parse_ign_voltage` |
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
def test_deenergized_voltage_parser(raw: str) -> None:
    parsed = parse_ign_voltage(raw)

    assert parsed.raw == raw
    assert parsed.status == "DEENERGIZED"
    assert parsed.voltage_kv is None
    assert parsed.voltage_upper_bound_kv is None
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unexpected_or_non_scalar_voltage_is_controlled_unparsed`

**Purpose:** Regression invariant: unexpected or non scalar voltage is controlled unparsed. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_unexpected_or_non_scalar_voltage_is_controlled_unparsed(
    value: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "value",
    ["Très haute tension future", ["63 kV"], np.array(["63 kV"])],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert parsed.status == "UNPARSED"`
  - `assert parsed.voltage_kv is None`
  - `assert parsed.voltage_upper_bound_kv is None`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `parse_ign_voltage` | `landscout.stages.normalize_grid_ign.parse_ign_voltage` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `np.array` | `numpy.array` |

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
def test_unexpected_or_non_scalar_voltage_is_controlled_unparsed(
    value: object,
) -> None:
    parsed = parse_ign_voltage(value)

    assert parsed.status == "UNPARSED"
    assert parsed.voltage_kv is None
    assert parsed.voltage_upper_bound_kv is None
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_invalid_or_overflowing_numeric_voltage_is_unparsed`

**Purpose:** Regression invariant: invalid or overflowing numeric voltage is unparsed. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_invalid_or_overflowing_numeric_voltage_is_unparsed(raw: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "raw",
    ["0 kV", "<0 kV", "-63 kV", "63 V", f"{'9' * 400} kV", f"<{'9' * 400} kV"],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `raw` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert parsed.status == "UNPARSED"`
  - `assert parsed.voltage_kv is None`
  - `assert parsed.voltage_upper_bound_kv is None`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `parse_ign_voltage` | `landscout.stages.normalize_grid_ign.parse_ign_voltage` |
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
def test_invalid_or_overflowing_numeric_voltage_is_unparsed(raw: str) -> None:
    parsed = parse_ign_voltage(raw)

    assert parsed.status == "UNPARSED"
    assert parsed.voltage_kv is None
    assert parsed.voltage_upper_bound_kv is None
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_valid_line_has_stable_identity_lineage_and_range_index`

**Purpose:** Regression invariant: valid line has stable identity lineage and range index. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_valid_line_has_stable_identity_lineage_and_range_index() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert list(normalized.columns) == list(LINE_OUTPUT_COLUMNS)`
  - `assert isinstance(normalized.index, pd.RangeIndex)`
  - `assert row["grid_feature_id"] == "IGN_BDTOPO:ELECTRIC_LINE:LIGNE-1"`
  - `assert row["source_feature_id"] == "LIGNE-1"`
  - `assert row["source_provider"] == "IGN"`
  - `assert row["source_product"] == "BD_TOPO"`
  - `assert row["source_layer"] == LINE_LAYER`
  - `assert row["source_department_code"] == "31"`
  - `assert row["source_edition"] == "2026-06-15"`
  - `assert row["source_product_version"] == "3.5"`
  - `assert row["source_download_timestamp"] == "2026-08-11T15:32:03+00:00"`
  - `assert row["source_archive_sha256"] == ARCHIVE_SHA256`
  - `assert row["source_url"] == SOURCE_URL`
  - `assert row["manager_name"] == "Réseau de Transport d'Électricité"`
  - `assert row["asset_status_raw"] == "En service"`
  - `assert row["source_identifiers_raw"] == "source-id"`
  - `assert row["planimetric_precision_m"] == 2.5`
  - `assert row["spatial_role"] == "PROXY_GEOMETRY"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_line_source` | `tests.unit.test_normalize_grid_ign._line_source` |
| `normalize_ign_electric_lines` | `landscout.stages.normalize_grid_ign._normalize_ign_electric_lines` |
| `_context` | `tests.unit.test_normalize_grid_ign._context` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_valid_line_has_stable_identity_lineage_and_range_index() -> None:
    source = _line_source()

    normalized = normalize_ign_electric_lines(source, _context(LINE_LAYER))

    row = normalized.iloc[0]
    assert list(normalized.columns) == list(LINE_OUTPUT_COLUMNS)
    assert isinstance(normalized.index, pd.RangeIndex)
    assert row["grid_feature_id"] == "IGN_BDTOPO:ELECTRIC_LINE:LIGNE-1"
    assert row["source_feature_id"] == "LIGNE-1"
    assert row["source_provider"] == "IGN"
    assert row["source_product"] == "BD_TOPO"
    assert row["source_layer"] == LINE_LAYER
    assert row["source_department_code"] == "31"
    assert row["source_edition"] == "2026-06-15"
    assert row["source_product_version"] == "3.5"
    assert row["source_download_timestamp"] == "2026-08-11T15:32:03+00:00"
    assert row["source_archive_sha256"] == ARCHIVE_SHA256
    assert row["source_url"] == SOURCE_URL
    assert row["manager_name"] == "Réseau de Transport d'Électricité"
    assert row["asset_status_raw"] == "En service"
    assert row["source_identifiers_raw"] == "source-id"
    assert row["planimetric_precision_m"] == 2.5
    assert row["spatial_role"] == "PROXY_GEOMETRY"
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_deenergized_voltage_does_not_override_source_asset_status`

**Purpose:** Regression invariant: deenergized voltage does not override source asset status. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_deenergized_voltage_does_not_override_source_asset_status() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert normalized.iloc[0]["voltage_status"] == "DEENERGIZED"`
  - `assert normalized.iloc[0]["asset_status_raw"] == "En service"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `normalize_ign_electric_lines` | `landscout.stages.normalize_grid_ign._normalize_ign_electric_lines` |
| `_line_source` | `tests.unit.test_normalize_grid_ign._line_source` |
| `_context` | `tests.unit.test_normalize_grid_ign._context` |

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
def test_deenergized_voltage_does_not_override_source_asset_status() -> None:
    normalized = normalize_ign_electric_lines(
        _line_source(voltages=["Hors tension"]), _context(LINE_LAYER)
    )

    assert normalized.iloc[0]["voltage_status"] == "DEENERGIZED"
    assert normalized.iloc[0]["asset_status_raw"] == "En service"
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_null_or_empty_line_cleabs_fails`

**Purpose:** Regression invariant: null or empty line cleabs fails. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_null_or_empty_line_cleabs_fails(identifier: object) -> None:
```

- Exact decorators: `pytest.mark.parametrize("identifier", [None, "", "   "])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `identifier` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnGridNormalizationError, match="cleabs\|null\|empty")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `normalize_ign_electric_lines` | `landscout.stages.normalize_grid_ign._normalize_ign_electric_lines` |
| `_line_source` | `tests.unit.test_normalize_grid_ign._line_source` |
| `_context` | `tests.unit.test_normalize_grid_ign._context` |
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
def test_null_or_empty_line_cleabs_fails(identifier: object) -> None:
    with pytest.raises(IgnGridNormalizationError, match="cleabs|null|empty"):
        normalize_ign_electric_lines(
            _line_source(identifiers=[identifier]), _context(LINE_LAYER)
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unsafe_source_id_is_rejected_without_rewriting`

**Purpose:** Regression invariant: unsafe source id is rejected without rewriting. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_unsafe_source_id_is_rejected_without_rewriting(identifier: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "identifier",
    [" leading", "trailing ", "IGN:BAD", "IGN\nCONTROL", "IGN\tCONTROL"],
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
  - `pytest.raises(IgnGridNormalizationError, match="cleabs\|whitespace\|control\|:")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `normalize_ign_electric_lines` | `landscout.stages.normalize_grid_ign._normalize_ign_electric_lines` |
| `_line_source` | `tests.unit.test_normalize_grid_ign._line_source` |
| `_context` | `tests.unit.test_normalize_grid_ign._context` |
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
def test_unsafe_source_id_is_rejected_without_rewriting(identifier: str) -> None:
    with pytest.raises(IgnGridNormalizationError, match="cleabs|whitespace|control|:"):
        normalize_ign_electric_lines(
            _line_source(identifiers=[identifier]), _context(LINE_LAYER)
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_duplicate_line_cleabs_fails`

**Purpose:** Regression invariant: duplicate line cleabs fails. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_duplicate_line_cleabs_fails() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnGridNormalizationError, match="unique")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_line_source` | `tests.unit.test_normalize_grid_ign._line_source` |
| `LineString` | `shapely.geometry.LineString` |
| `pytest.raises` | `pytest.raises` |
| `normalize_ign_electric_lines` | `landscout.stages.normalize_grid_ign._normalize_ign_electric_lines` |
| `_context` | `tests.unit.test_normalize_grid_ign._context` |

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
def test_duplicate_line_cleabs_fails() -> None:
    source = _line_source(
        geometries=[
            LineString([(0, 0), (10, 10)]),
            LineString([(20, 20), (30, 30)]),
        ],
        identifiers=["DUPLICATE", "DUPLICATE"],
    )

    with pytest.raises(IgnGridNormalizationError, match="unique"):
        normalize_ign_electric_lines(source, _context(LINE_LAYER))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_line_missing_or_wrong_crs_fails`

**Purpose:** Regression invariant: line missing or wrong crs fails. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_line_missing_or_wrong_crs_fails(crs: str | None) -> None:
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
  - `pytest.raises(IgnGridNormalizationError, match="CRS\|2154")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `normalize_ign_electric_lines` | `landscout.stages.normalize_grid_ign._normalize_ign_electric_lines` |
| `_line_source` | `tests.unit.test_normalize_grid_ign._line_source` |
| `_context` | `tests.unit.test_normalize_grid_ign._context` |
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
def test_line_missing_or_wrong_crs_fails(crs: str | None) -> None:
    with pytest.raises(IgnGridNormalizationError, match="CRS|2154"):
        normalize_ign_electric_lines(_line_source(crs=crs), _context(LINE_LAYER))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_line_geometry_quality_is_preserved_without_row_loss_or_repair`

**Purpose:** Regression invariant: line geometry quality is preserved without row loss or repair. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_line_geometry_quality_is_preserved_without_row_loss_or_repair() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert normalized["geometry_status"].tolist() == [<br>        "VALID",<br>        "NULL",<br>        "EMPTY",<br>        "INVALID",<br>    ]`
  - `assert normalized["source_feature_id"].tolist() == [<br>        "VALID",<br>        "NULL",<br>        "EMPTY",<br>        "INVALID",<br>    ]`
  - `assert normalized.geometry.iloc[1] is None`
  - `assert normalized.geometry.iloc[2].is_empty`
  - `assert normalized.geometry.iloc[3].equals_exact(invalid, tolerance=0)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `Polygon` | `shapely.geometry.Polygon` |
| `_line_source` | `tests.unit.test_normalize_grid_ign._line_source` |
| `LineString` | `shapely.geometry.LineString` |
| `normalize_ign_electric_lines` | `landscout.stages.normalize_grid_ign._normalize_ign_electric_lines` |
| `_context` | `tests.unit.test_normalize_grid_ign._context` |
| `normalized["geometry_status"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `normalized["source_feature_id"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `normalized.geometry.iloc[3].equals_exact` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `normalized["geometry_status"].tolist`<br>`normalized.geometry.iloc[3].equals_exact` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_line_geometry_quality_is_preserved_without_row_loss_or_repair() -> None:
    invalid = Polygon([(0, 0), (20, 20), (20, 0), (0, 20), (0, 0)])
    source = _line_source(
        geometries=[LineString([(0, 0), (10, 10)]), None, LineString(), invalid],
        identifiers=["VALID", "NULL", "EMPTY", "INVALID"],
        voltages=["63 kV"] * 4,
    )

    normalized = normalize_ign_electric_lines(source, _context(LINE_LAYER))

    assert normalized["geometry_status"].tolist() == [
        "VALID",
        "NULL",
        "EMPTY",
        "INVALID",
    ]
    assert normalized["source_feature_id"].tolist() == [
        "VALID",
        "NULL",
        "EMPTY",
        "INVALID",
    ]
    assert normalized.geometry.iloc[1] is None
    assert normalized.geometry.iloc[2].is_empty
    assert normalized.geometry.iloc[3].equals_exact(invalid, tolerance=0)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_z_coordinates_are_preserved`

**Purpose:** Regression invariant: z coordinates are preserved. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_z_coordinates_are_preserved() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert source.geometry.iloc[0].has_z`
  - `assert normalized.geometry.iloc[0].has_z`
  - `assert normalized.geometry.iloc[0].equals_exact(<br>        source.geometry.iloc[0], tolerance=0<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_line_source` | `tests.unit.test_normalize_grid_ign._line_source` |
| `LineString` | `shapely.geometry.LineString` |
| `normalize_ign_electric_lines` | `landscout.stages.normalize_grid_ign._normalize_ign_electric_lines` |
| `_context` | `tests.unit.test_normalize_grid_ign._context` |
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
def test_z_coordinates_are_preserved() -> None:
    source = _line_source(geometries=[LineString([(0, 0, 10), (10, 10, 20)])])

    normalized = normalize_ign_electric_lines(source, _context(LINE_LAYER))

    assert source.geometry.iloc[0].has_z
    assert normalized.geometry.iloc[0].has_z
    assert normalized.geometry.iloc[0].equals_exact(
        source.geometry.iloc[0], tolerance=0
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unusual_duplicate_source_index_is_not_preserved_as_identity`

**Purpose:** Regression invariant: unusual duplicate source index is not preserved as identity. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_unusual_duplicate_source_index_is_not_preserved_as_identity() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert isinstance(normalized.index, pd.RangeIndex)`
  - `assert normalized.index.tolist() == [0, 1]`
  - `assert normalized["source_feature_id"].tolist() == ["FIRST", "SECOND"]`
  - `assert normalized["grid_feature_id"].tolist() == [<br>        "IGN_BDTOPO:ELECTRIC_LINE:FIRST",<br>        "IGN_BDTOPO:ELECTRIC_LINE:SECOND",<br>    ]`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_line_source` | `tests.unit.test_normalize_grid_ign._line_source` |
| `LineString` | `shapely.geometry.LineString` |
| `normalize_ign_electric_lines` | `landscout.stages.normalize_grid_ign._normalize_ign_electric_lines` |
| `_context` | `tests.unit.test_normalize_grid_ign._context` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `normalized.index.tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `normalized["source_feature_id"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `normalized["grid_feature_id"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_unusual_duplicate_source_index_is_not_preserved_as_identity() -> None:
    source = _line_source(
        geometries=[
            LineString([(0, 0), (10, 10)]),
            LineString([(20, 20), (30, 30)]),
        ],
        identifiers=["FIRST", "SECOND"],
        index=[77, 77],
    )

    normalized = normalize_ign_electric_lines(source, _context(LINE_LAYER))

    assert isinstance(normalized.index, pd.RangeIndex)
    assert normalized.index.tolist() == [0, 1]
    assert normalized["source_feature_id"].tolist() == ["FIRST", "SECOND"]
    assert normalized["grid_feature_id"].tolist() == [
        "IGN_BDTOPO:ELECTRIC_LINE:FIRST",
        "IGN_BDTOPO:ELECTRIC_LINE:SECOND",
    ]
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_line_normalization_does_not_mutate_input_and_has_stable_columns`

**Purpose:** Regression invariant: line normalization does not mutate input and has stable columns. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_line_normalization_does_not_mutate_input_and_has_stable_columns() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert list(normalized.columns) == list(LINE_OUTPUT_COLUMNS)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_line_source` | `tests.unit.test_normalize_grid_ign._line_source` |
| `source.loc[:, list(reversed(source.columns))].set_geometry` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `reversed` | `unresolved local/third-party receiver; no ownership inferred` |
| `deepcopy` | `copy.deepcopy` |
| `normalize_ign_electric_lines` | `landscout.stages.normalize_grid_ign._normalize_ign_electric_lines` |
| `_context` | `tests.unit.test_normalize_grid_ign._context` |
| `assert_geodataframe_equal` | `geopandas.testing.assert_geodataframe_equal` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `source.loc[:, list(reversed(source.columns))].set_geometry` |
| External process/environment | None directly present. |
| In-memory mutation | `source.loc[:, list(reversed(source.columns))].set_geometry("geometry")` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_line_normalization_does_not_mutate_input_and_has_stable_columns() -> None:
    source = _line_source()
    reordered = source.loc[:, list(reversed(source.columns))].set_geometry("geometry")
    before = deepcopy(reordered)

    normalized = normalize_ign_electric_lines(reordered, _context(LINE_LAYER))

    assert_geodataframe_equal(reordered, before)
    assert list(normalized.columns) == list(LINE_OUTPUT_COLUMNS)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_missing_required_line_field_fails`

**Purpose:** Regression invariant: missing required line field fails. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_missing_required_line_field_fails(column: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize("column", ["cleabs", "geometry", "identifiants_sources"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `column` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnGridNormalizationError, match=column)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_line_source().drop` | `unresolved local/third-party receiver; no ownership inferred` |
| `_line_source` | `tests.unit.test_normalize_grid_ign._line_source` |
| `pytest.raises` | `pytest.raises` |
| `normalize_ign_electric_lines` | `landscout.stages.normalize_grid_ign._normalize_ign_electric_lines` |
| `_context` | `tests.unit.test_normalize_grid_ign._context` |
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
| In-memory mutation | `_line_source().drop(columns=column)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_missing_required_line_field_fails(column: str) -> None:
    source = _line_source().drop(columns=column)

    with pytest.raises(IgnGridNormalizationError, match=column):
        normalize_ign_electric_lines(source, _context(LINE_LAYER))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_valid_or_null_line_precision_is_normalized_to_float`

**Purpose:** Regression invariant: valid or null line precision is normalized to float. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_valid_or_null_line_precision_is_normalized_to_float(
    precision: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("precision", [0, 2.5, None, float("nan")])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `precision` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert str(normalized["planimetric_precision_m"].dtype) == "float64"`
  - `assert pd.isna(normalized.iloc[0]["planimetric_precision_m"])`
  - `assert normalized.iloc[0]["planimetric_precision_m"] == float(precision)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `normalize_ign_electric_lines` | `landscout.stages.normalize_grid_ign._normalize_ign_electric_lines` |
| `_line_source` | `tests.unit.test_normalize_grid_ign._line_source` |
| `_context` | `tests.unit.test_normalize_grid_ign._context` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `np.isnan` | `numpy.isnan` |
| `pd.isna` | `pandas.isna` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |
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
def test_valid_or_null_line_precision_is_normalized_to_float(
    precision: object,
) -> None:
    normalized = normalize_ign_electric_lines(
        _line_source(precisions=[precision]), _context(LINE_LAYER)
    )

    assert str(normalized["planimetric_precision_m"].dtype) == "float64"
    if precision is None or (isinstance(precision, float) and np.isnan(precision)):
        assert pd.isna(normalized.iloc[0]["planimetric_precision_m"])
    else:
        assert normalized.iloc[0]["planimetric_precision_m"] == float(precision)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_invalid_line_precision_fails`

**Purpose:** Regression invariant: invalid line precision fails. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_invalid_line_precision_fails(precision: object) -> None:
```

- Exact decorators: `pytest.mark.parametrize("precision", [-1, float("inf"), float("-inf"), True, "2.5"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `precision` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnGridNormalizationError, match="precision_planimetrique")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `normalize_ign_electric_lines` | `landscout.stages.normalize_grid_ign._normalize_ign_electric_lines` |
| `_line_source` | `tests.unit.test_normalize_grid_ign._line_source` |
| `_context` | `tests.unit.test_normalize_grid_ign._context` |
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
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_invalid_line_precision_fails(precision: object) -> None:
    with pytest.raises(IgnGridNormalizationError, match="precision_planimetrique"):
        normalize_ign_electric_lines(
            _line_source(precisions=[precision]), _context(LINE_LAYER)
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_normalized_voltage_never_emits_non_finite_numeric_values`

**Purpose:** Regression invariant: normalized voltage never emits non finite numeric values. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_normalized_voltage_never_emits_non_finite_numeric_values() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert normalized["voltage_status"].tolist() == [<br>        "EXACT",<br>        "BELOW",<br>        "UNPARSED",<br>        "UNKNOWN",<br>    ]`
  - `assert np.isfinite(normalized["voltage_kv"].dropna()).all()`
  - `assert np.isfinite(normalized["voltage_upper_bound_kv"].dropna()).all()`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_line_source` | `tests.unit.test_normalize_grid_ign._line_source` |
| `LineString` | `shapely.geometry.LineString` |
| `normalize_ign_electric_lines` | `landscout.stages.normalize_grid_ign._normalize_ign_electric_lines` |
| `_context` | `tests.unit.test_normalize_grid_ign._context` |
| `normalized["voltage_status"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `np.isfinite(normalized["voltage_kv"].dropna()).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `np.isfinite` | `numpy.isfinite` |
| `normalized["voltage_kv"].dropna` | `unresolved local/third-party receiver; no ownership inferred` |
| `np.isfinite(normalized["voltage_upper_bound_kv"].dropna()).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `normalized["voltage_upper_bound_kv"].dropna` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_normalized_voltage_never_emits_non_finite_numeric_values() -> None:
    huge = f"{'9' * 400} kV"
    source = _line_source(
        geometries=[LineString([(0, 0), (1, 1)])] * 4,
        identifiers=["EXACT", "BELOW", "OVERFLOW", "MISSING"],
        voltages=["225 kV", "<90 kV", huge, None],
    )

    normalized = normalize_ign_electric_lines(source, _context(LINE_LAYER))

    assert normalized["voltage_status"].tolist() == [
        "EXACT",
        "BELOW",
        "UNPARSED",
        "UNKNOWN",
    ]
    assert np.isfinite(normalized["voltage_kv"].dropna()).all()
    assert np.isfinite(normalized["voltage_upper_bound_kv"].dropna()).all()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_valid_post_has_stable_lineage_and_no_voltage_inference`

**Purpose:** Regression invariant: valid post has stable lineage and no voltage inference. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_valid_post_has_stable_lineage_and_no_voltage_inference() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert list(normalized.columns) == list(TRANSFORMATION_POST_OUTPUT_COLUMNS)`
  - `assert isinstance(normalized.index, pd.RangeIndex)`
  - `assert row["grid_feature_id"] == "IGN_BDTOPO:TRANSFORMATION_POST:POSTE-1"`
  - `assert row["source_layer"] == POST_LAYER`
  - `assert row["source_department_code"] == "31"`
  - `assert row["source_archive_sha256"] == ARCHIVE_SHA256`
  - `assert row["name"] == "Poste de test"`
  - `assert row["voltage_status"] == "UNKNOWN"`
  - `assert pd.isna(row["voltage_kv"])`
  - `assert row["spatial_role"] == "PROXY_GEOMETRY"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_post_source` | `tests.unit.test_normalize_grid_ign._post_source` |
| `normalize_ign_transformation_posts` | `landscout.stages.normalize_grid_ign._normalize_ign_transformation_posts` |
| `_context` | `tests.unit.test_normalize_grid_ign._context` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
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
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_valid_post_has_stable_lineage_and_no_voltage_inference() -> None:
    source = _post_source()

    normalized = normalize_ign_transformation_posts(source, _context(POST_LAYER))

    row = normalized.iloc[0]
    assert list(normalized.columns) == list(TRANSFORMATION_POST_OUTPUT_COLUMNS)
    assert isinstance(normalized.index, pd.RangeIndex)
    assert row["grid_feature_id"] == "IGN_BDTOPO:TRANSFORMATION_POST:POSTE-1"
    assert row["source_layer"] == POST_LAYER
    assert row["source_department_code"] == "31"
    assert row["source_archive_sha256"] == ARCHIVE_SHA256
    assert row["name"] == "Poste de test"
    assert row["voltage_status"] == "UNKNOWN"
    assert pd.isna(row["voltage_kv"])
    assert row["spatial_role"] == "PROXY_GEOMETRY"
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_post_geometry_crs_and_input_are_preserved`

**Purpose:** Regression invariant: post geometry crs and input are preserved. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_post_geometry_crs_and_input_are_preserved() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert normalized.crs is not None and normalized.crs.to_epsg() == 2154`
  - `assert normalized.geometry.iloc[0].equals_exact(<br>        source.geometry.iloc[0], tolerance=0<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_post_source` | `tests.unit.test_normalize_grid_ign._post_source` |
| `deepcopy` | `copy.deepcopy` |
| `normalize_ign_transformation_posts` | `landscout.stages.normalize_grid_ign._normalize_ign_transformation_posts` |
| `_context` | `tests.unit.test_normalize_grid_ign._context` |
| `assert_geodataframe_equal` | `geopandas.testing.assert_geodataframe_equal` |
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
def test_post_geometry_crs_and_input_are_preserved() -> None:
    source = _post_source()
    before = deepcopy(source)

    normalized = normalize_ign_transformation_posts(source, _context(POST_LAYER))

    assert_geodataframe_equal(source, before)
    assert normalized.crs is not None and normalized.crs.to_epsg() == 2154
    assert normalized.geometry.iloc[0].equals_exact(
        source.geometry.iloc[0], tolerance=0
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_duplicate_post_cleabs_fails`

**Purpose:** Regression invariant: duplicate post cleabs fails. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_duplicate_post_cleabs_fails() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnGridNormalizationError, match="unique")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `Polygon` | `shapely.geometry.Polygon` |
| `_post_source` | `tests.unit.test_normalize_grid_ign._post_source` |
| `pytest.raises` | `pytest.raises` |
| `normalize_ign_transformation_posts` | `landscout.stages.normalize_grid_ign._normalize_ign_transformation_posts` |
| `_context` | `tests.unit.test_normalize_grid_ign._context` |

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
def test_duplicate_post_cleabs_fails() -> None:
    polygon = Polygon([(0, 0), (0, 20), (20, 20), (20, 0), (0, 0)])
    source = _post_source(
        geometries=[polygon, polygon], identifiers=["DUPLICATE", "DUPLICATE"]
    )

    with pytest.raises(IgnGridNormalizationError, match="unique"):
        normalize_ign_transformation_posts(source, _context(POST_LAYER))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_null_post_geometry_and_precision_are_preserved`

**Purpose:** Regression invariant: null post geometry and precision are preserved. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_null_post_geometry_and_precision_are_preserved() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert normalized.iloc[0]["geometry_status"] == "NULL"`
  - `assert normalized.geometry.iloc[0] is None`
  - `assert normalized.iloc[0]["voltage_status"] == "UNKNOWN"`
  - `assert normalized["voltage_kv"].isna().all()`
  - `assert normalized["planimetric_precision_m"].isna().all()`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `normalize_ign_transformation_posts` | `landscout.stages.normalize_grid_ign._normalize_ign_transformation_posts` |
| `_post_source` | `tests.unit.test_normalize_grid_ign._post_source` |
| `_context` | `tests.unit.test_normalize_grid_ign._context` |
| `normalized["voltage_kv"].isna().all` | `unresolved local/third-party receiver; no ownership inferred` |
| `normalized["voltage_kv"].isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `normalized["planimetric_precision_m"].isna().all` | `unresolved local/third-party receiver; no ownership inferred` |
| `normalized["planimetric_precision_m"].isna` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_null_post_geometry_and_precision_are_preserved() -> None:
    normalized = normalize_ign_transformation_posts(
        _post_source(geometries=[None], precisions=[None]), _context(POST_LAYER)
    )

    assert normalized.iloc[0]["geometry_status"] == "NULL"
    assert normalized.geometry.iloc[0] is None
    assert normalized.iloc[0]["voltage_status"] == "UNKNOWN"
    assert normalized["voltage_kv"].isna().all()
    assert normalized["planimetric_precision_m"].isna().all()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_invalid_post_precision_fails`

**Purpose:** Regression invariant: invalid post precision fails. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_invalid_post_precision_fails() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnGridNormalizationError, match="precision_planimetrique")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `normalize_ign_transformation_posts` | `landscout.stages.normalize_grid_ign._normalize_ign_transformation_posts` |
| `_post_source` | `tests.unit.test_normalize_grid_ign._post_source` |
| `_context` | `tests.unit.test_normalize_grid_ign._context` |

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
def test_invalid_post_precision_fails() -> None:
    with pytest.raises(IgnGridNormalizationError, match="precision_planimetrique"):
        normalize_ign_transformation_posts(
            _post_source(precisions=["5.0"]), _context(POST_LAYER)
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_appropriate_multigeometry_types_are_accepted`

**Purpose:** Regression invariant: appropriate multigeometry types are accepted. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_appropriate_multigeometry_types_are_accepted() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert lines.iloc[0]["geometry_status"] == "VALID"`
  - `assert lines.geometry.iloc[0].geom_type == "MultiLineString"`
  - `assert posts.iloc[0]["geometry_status"] == "VALID"`
  - `assert posts.geometry.iloc[0].geom_type == "MultiPolygon"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `MultiLineString` | `shapely.geometry.MultiLineString` |
| `MultiPolygon` | `shapely.geometry.MultiPolygon` |
| `Polygon` | `shapely.geometry.Polygon` |
| `normalize_ign_electric_lines` | `landscout.stages.normalize_grid_ign._normalize_ign_electric_lines` |
| `_line_source` | `tests.unit.test_normalize_grid_ign._line_source` |
| `_context` | `tests.unit.test_normalize_grid_ign._context` |
| `normalize_ign_transformation_posts` | `landscout.stages.normalize_grid_ign._normalize_ign_transformation_posts` |
| `_post_source` | `tests.unit.test_normalize_grid_ign._post_source` |

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
def test_appropriate_multigeometry_types_are_accepted() -> None:
    multilines = MultiLineString([[(0, 0), (10, 10)], [(20, 20), (30, 30)]])
    multipolygon = MultiPolygon(
        [
            Polygon([(0, 0), (0, 5), (5, 5), (5, 0), (0, 0)]),
            Polygon([(10, 10), (10, 15), (15, 15), (15, 10), (10, 10)]),
        ]
    )

    lines = normalize_ign_electric_lines(
        _line_source(geometries=[multilines]), _context(LINE_LAYER)
    )
    posts = normalize_ign_transformation_posts(
        _post_source(geometries=[multipolygon]), _context(POST_LAYER)
    )

    assert lines.iloc[0]["geometry_status"] == "VALID"
    assert lines.geometry.iloc[0].geom_type == "MultiLineString"
    assert posts.iloc[0]["geometry_status"] == "VALID"
    assert posts.geometry.iloc[0].geom_type == "MultiPolygon"
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_valid_polygon_or_point_is_rejected_as_electric_line`

**Purpose:** Regression invariant: valid polygon or point is rejected as electric line. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_valid_polygon_or_point_is_rejected_as_electric_line(
    geometry: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "geometry",
    [
        Polygon([(0, 0), (0, 5), (5, 5), (5, 0), (0, 0)]),
        Point(1, 1),
    ],
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
  - `pytest.raises(IgnGridNormalizationError, match="geometry types")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `normalize_ign_electric_lines` | `landscout.stages.normalize_grid_ign._normalize_ign_electric_lines` |
| `_line_source` | `tests.unit.test_normalize_grid_ign._line_source` |
| `_context` | `tests.unit.test_normalize_grid_ign._context` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `Polygon` | `shapely.geometry.Polygon` |
| `Point` | `shapely.geometry.Point` |

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
def test_valid_polygon_or_point_is_rejected_as_electric_line(
    geometry: object,
) -> None:
    with pytest.raises(IgnGridNormalizationError, match="geometry types"):
        normalize_ign_electric_lines(
            _line_source(geometries=[geometry]), _context(LINE_LAYER)
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_valid_line_or_point_is_rejected_as_transformation_post`

**Purpose:** Regression invariant: valid line or point is rejected as transformation post. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_valid_line_or_point_is_rejected_as_transformation_post(
    geometry: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("geometry", [LineString([(0, 0), (10, 10)]), Point(1, 1)])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `geometry` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnGridNormalizationError, match="geometry types")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `normalize_ign_transformation_posts` | `landscout.stages.normalize_grid_ign._normalize_ign_transformation_posts` |
| `_post_source` | `tests.unit.test_normalize_grid_ign._post_source` |
| `_context` | `tests.unit.test_normalize_grid_ign._context` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `LineString` | `shapely.geometry.LineString` |
| `Point` | `shapely.geometry.Point` |

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
def test_valid_line_or_point_is_rejected_as_transformation_post(
    geometry: object,
) -> None:
    with pytest.raises(IgnGridNormalizationError, match="geometry types"):
        normalize_ign_transformation_posts(
            _post_source(geometries=[geometry]), _context(POST_LAYER)
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_high_level_path_uses_discovered_layer_names_and_archive_lineage`

**Purpose:** Regression invariant: high level path uses discovered layer names and archive lineage. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_high_level_path_uses_discovered_layer_names_and_archive_lineage() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert normalized.electric_lines["source_layer"].unique().tolist() == [LINE_LAYER]`
  - `assert normalized.transformation_posts["source_layer"].unique().tolist() == [<br>        POST_LAYER<br>    ]`
  - `assert frame["source_department_code"].unique().tolist() == ["31"]`
  - `assert frame["source_edition"].unique().tolist() == ["2026-06-15"]`
  - `assert frame["source_product_version"].unique().tolist() == ["3.5"]`
  - `assert frame["source_archive_sha256"].unique().tolist() == [ARCHIVE_SHA256]`
  - `assert frame["source_url"].unique().tolist() == [SOURCE_URL]`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_bundle` | `tests.unit.test_normalize_grid_ign._source_bundle` |
| `normalize_ign_electricity` | `tests.unit.test_normalize_grid_ign.normalize_ign_electricity` |
| `normalized.electric_lines["source_layer"].unique().tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `normalized.electric_lines["source_layer"].unique` | `unresolved local/third-party receiver; no ownership inferred` |
| `normalized.transformation_posts["source_layer"].unique().tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `normalized.transformation_posts["source_layer"].unique` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame["source_department_code"].unique().tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame["source_department_code"].unique` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame["source_edition"].unique().tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame["source_edition"].unique` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame["source_product_version"].unique().tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame["source_product_version"].unique` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame["source_archive_sha256"].unique().tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame["source_archive_sha256"].unique` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame["source_url"].unique().tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame["source_url"].unique` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `frame["source_archive_sha256"].unique().tolist`<br>`frame["source_archive_sha256"].unique` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_high_level_path_uses_discovered_layer_names_and_archive_lineage() -> None:
    source = _source_bundle()

    normalized = normalize_ign_electricity(source)

    assert normalized.electric_lines["source_layer"].unique().tolist() == [LINE_LAYER]
    assert normalized.transformation_posts["source_layer"].unique().tolist() == [
        POST_LAYER
    ]
    for frame in (normalized.electric_lines, normalized.transformation_posts):
        assert frame["source_department_code"].unique().tolist() == ["31"]
        assert frame["source_edition"].unique().tolist() == ["2026-06-15"]
        assert frame["source_product_version"].unique().tolist() == ["3.5"]
        assert frame["source_archive_sha256"].unique().tolist() == [ARCHIVE_SHA256]
        assert frame["source_url"].unique().tolist() == [SOURCE_URL]
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_high_level_rejects_coordinated_frame_and_summary_forgery`

**Purpose:** Regression invariant: high level rejects coordinated frame and summary forgery. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_high_level_rejects_coordinated_frame_and_summary_forgery() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnGridNormalizationError, match="physical\|fresh\|source")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_bundle` | `tests.unit.test_normalize_grid_ign._source_bundle` |
| `source.electric_lines.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `_summary` | `tests.unit.test_normalize_grid_ign._summary` |
| `pytest.raises` | `pytest.raises` |
| `normalize_ign_electricity` | `tests.unit.test_normalize_grid_ign.normalize_ign_electricity` |
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
| In-memory mutation | `forged.loc[0, "voltage"] = "400 kV"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_high_level_rejects_coordinated_frame_and_summary_forgery() -> None:
    source = _source_bundle()
    forged = source.electric_lines.copy()
    forged.loc[0, "voltage"] = "400 kV"
    forged_summary = _summary(forged, "electric_lines", LINE_LAYER)

    with pytest.raises(IgnGridNormalizationError, match="physical|fresh|source"):
        normalize_ign_electricity(
            replace(
                source,
                electric_lines=forged,
                electric_lines_summary=forged_summary,
            )
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_complete_grid_validation_does_not_mutate_supplied_frames`

**Purpose:** Regression invariant: source complete grid validation does not mutate supplied frames. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_complete_grid_validation_does_not_mutate_supplied_frames() -> None:
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
| `_source_bundle` | `tests.unit.test_normalize_grid_ign._source_bundle` |
| `deepcopy` | `copy.deepcopy` |
| `normalize_ign_electricity` | `tests.unit.test_normalize_grid_ign.normalize_ign_electricity` |
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
def test_source_complete_grid_validation_does_not_mutate_supplied_frames() -> None:
    source = _source_bundle()
    lines_before = deepcopy(source.electric_lines)
    posts_before = deepcopy(source.transformation_posts)

    normalize_ign_electricity(source)

    assert_geodataframe_equal(source.electric_lines, lines_before)
    assert_geodataframe_equal(source.transformation_posts, posts_before)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_grid_normalization_uses_distinct_fresh_revalidated_frames`

**Purpose:** Regression invariant: grid normalization uses distinct fresh revalidated frames. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_grid_normalization_uses_distinct_fresh_revalidated_frames(
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
  - `assert normalized.electric_lines.loc[0, "voltage_raw"] == expected_voltage`
  - `assert source.electric_lines.loc[0, "voltage"] == "FORGED AFTER REVALIDATION"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_bundle` | `tests.unit.test_normalize_grid_ign._source_bundle` |
| `replace` | `dataclasses.replace` |
| `source.electric_lines.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `source.transformation_posts.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `_normalize_ign_electricity` | `landscout.stages.normalize_grid_ign.normalize_ign_electricity` |

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
def test_grid_normalization_uses_distinct_fresh_revalidated_frames(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    source = _source_bundle()
    fresh = replace(
        source,
        electric_lines=source.electric_lines.copy(deep=True),
        transformation_posts=source.transformation_posts.copy(deep=True),
    )
    expected_voltage = fresh.electric_lines.loc[0, "voltage"]

    def return_fresh_and_mutate_supplied(
        _: object,
        __: object,
    ) -> IgnBdTopoElectricityData:
        source.electric_lines.loc[0, "voltage"] = "FORGED AFTER REVALIDATION"
        return fresh

    monkeypatch.setattr(
        grid_normalization,
        "_revalidate_ign_bdtopo_electricity_data",
        return_fresh_and_mutate_supplied,
    )

    normalized = _normalize_ign_electricity(source, SOURCE_CONFIG)

    assert normalized.electric_lines.loc[0, "voltage_raw"] == expected_voltage
    assert source.electric_lines.loc[0, "voltage"] == "FORGED AFTER REVALIDATION"
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_grid_normalization_uses_distinct_fresh_revalidated_frames.return_fresh_and_mutate_supplied`

**Purpose:** Implements `return fresh and mutate supplied` within the file role: Provides complete unit and regression coverage for the `normalize_grid_ign` contracts exercised in this file.

**Exact signature**

```python
def return_fresh_and_mutate_supplied(
        _: object,
        __: object,
    ) -> IgnBdTopoElectricityData:
```

- Exact decorators: none.
- Declared return annotation: `IgnBdTopoElectricityData`.

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
| In-memory mutation | `source.electric_lines.loc[0, "voltage"] = "FORGED AFTER REVALIDATION"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def return_fresh_and_mutate_supplied(
        _: object,
        __: object,
    ) -> IgnBdTopoElectricityData:
        source.electric_lines.loc[0, "voltage"] = "FORGED AFTER REVALIDATION"
        return fresh
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_high_level_rejects_incompatible_archive_identity`

**Purpose:** Regression invariant: high level rejects incompatible archive identity. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_high_level_rejects_incompatible_archive_identity(
    field: str,
    value: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("field", "value"),
    [
        ("provider", "Unrelated data vendor"),
        ("product", "OTHER PRODUCT"),
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
  - `pytest.raises(IgnGridNormalizationError, match="lineage\|config")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_bundle_with_archive` | `tests.unit.test_normalize_grid_ign._source_bundle_with_archive` |
| `pytest.raises` | `pytest.raises` |
| `normalize_ign_electricity` | `tests.unit.test_normalize_grid_ign.normalize_ign_electricity` |
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
def test_high_level_rejects_incompatible_archive_identity(
    field: str,
    value: str,
) -> None:
    source = _source_bundle_with_archive(**{field: value})

    with pytest.raises(IgnGridNormalizationError, match="lineage|config"):
        normalize_ign_electricity(source)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_archive_identity_requires_exact_pinned_strings`

**Purpose:** Regression invariant: archive identity requires exact pinned strings. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_archive_identity_requires_exact_pinned_strings() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnGridNormalizationError, match="provider\|product\|config")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_bundle_with_archive` | `tests.unit.test_normalize_grid_ign._source_bundle_with_archive` |
| `pytest.raises` | `pytest.raises` |
| `normalize_ign_electricity` | `tests.unit.test_normalize_grid_ign.normalize_ign_electricity` |

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
def test_archive_identity_requires_exact_pinned_strings() -> None:
    provider = "INSTITUT NATIONAL DE L'INFORMATION GEOGRAPHIQUE ET FORESTIERE (ign)"
    product = "bd-topo"
    source = _source_bundle_with_archive(
        provider=provider,
        product=product,
    )

    with pytest.raises(IgnGridNormalizationError, match="provider|product|config"):
        normalize_ign_electricity(source)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_high_level_rejects_summary_row_count_mismatch`

**Purpose:** Regression invariant: high level rejects summary row count mismatch. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_high_level_rejects_summary_row_count_mismatch() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnGridNormalizationError, match="summary\|physical")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_bundle` | `tests.unit.test_normalize_grid_ign._source_bundle` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `normalize_ign_electricity` | `tests.unit.test_normalize_grid_ign.normalize_ign_electricity` |

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
def test_high_level_rejects_summary_row_count_mismatch() -> None:
    source = _source_bundle()
    summary = replace(
        source.electric_lines_summary,
        feature_count=source.electric_lines_summary.feature_count + 1,
    )

    with pytest.raises(IgnGridNormalizationError, match="summary|physical"):
        normalize_ign_electricity(replace(source, electric_lines_summary=summary))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_high_level_rejects_summary_layer_name_mismatch`

**Purpose:** Regression invariant: high level rejects summary layer name mismatch. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_high_level_rejects_summary_layer_name_mismatch() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnGridNormalizationError, match="summary\|physical")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_bundle` | `tests.unit.test_normalize_grid_ign._source_bundle` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `normalize_ign_electricity` | `tests.unit.test_normalize_grid_ign.normalize_ign_electricity` |

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
def test_high_level_rejects_summary_layer_name_mismatch() -> None:
    source = _source_bundle()
    summary = replace(source.electric_lines_summary, source_layer_name="WRONG")

    with pytest.raises(IgnGridNormalizationError, match="summary|physical"):
        normalize_ign_electricity(replace(source, electric_lines_summary=summary))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_high_level_rejects_wrong_logical_name`

**Purpose:** Regression invariant: high level rejects wrong logical name. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_high_level_rejects_wrong_logical_name() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnGridNormalizationError, match="summary\|physical")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_bundle` | `tests.unit.test_normalize_grid_ign._source_bundle` |
| `replace` | `dataclasses.replace` |
| `cast` | `typing.cast` |
| `pytest.raises` | `pytest.raises` |
| `normalize_ign_electricity` | `tests.unit.test_normalize_grid_ign.normalize_ign_electricity` |

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
def test_high_level_rejects_wrong_logical_name() -> None:
    source = _source_bundle()
    summary = replace(
        source.electric_lines_summary,
        logical_name=cast(Any, "transformation_posts"),
    )

    with pytest.raises(IgnGridNormalizationError, match="summary|physical"):
        normalize_ign_electricity(replace(source, electric_lines_summary=summary))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_high_level_rejects_summary_crs_mismatch`

**Purpose:** Regression invariant: high level rejects summary crs mismatch. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_high_level_rejects_summary_crs_mismatch() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnGridNormalizationError, match="summary\|physical\|CRS\|2154")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_bundle` | `tests.unit.test_normalize_grid_ign._source_bundle` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `normalize_ign_electricity` | `tests.unit.test_normalize_grid_ign.normalize_ign_electricity` |

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
def test_high_level_rejects_summary_crs_mismatch() -> None:
    source = _source_bundle()
    summary = replace(source.electric_lines_summary, crs="EPSG:4326")

    with pytest.raises(IgnGridNormalizationError, match="summary|physical|CRS|2154"):
        normalize_ign_electricity(replace(source, electric_lines_summary=summary))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_high_level_rejects_forged_ordered_summary_schema`

**Purpose:** Regression invariant: high level rejects forged ordered summary schema. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_high_level_rejects_forged_ordered_summary_schema(mutation: str) -> None:
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
  - `pytest.raises(<br>        IgnGridNormalizationError,<br>        match="summary\|physical\|schema\|columns\|dtype",<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_bundle` | `tests.unit.test_normalize_grid_ign._source_bundle` |
| `replace` | `dataclasses.replace` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `reversed` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `normalize_ign_electricity` | `tests.unit.test_normalize_grid_ign.normalize_ign_electricity` |
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
| In-memory mutation | `dtypes[0] = (dtypes[0][0], "object")` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_high_level_rejects_forged_ordered_summary_schema(mutation: str) -> None:
    source = _source_bundle()
    summary = source.electric_lines_summary
    if mutation == "missing":
        changed = replace(summary, columns=summary.columns[:-1])
    elif mutation == "extra":
        changed = replace(summary, columns=(*summary.columns, "invented"))
    elif mutation == "reordered":
        changed = replace(summary, columns=tuple(reversed(summary.columns)))
    else:
        dtypes = list(summary.dtypes)
        dtypes[0] = (dtypes[0][0], "object")
        changed = replace(summary, dtypes=tuple(dtypes))

    with pytest.raises(
        IgnGridNormalizationError,
        match="summary|physical|schema|columns|dtype",
    ):
        normalize_ign_electricity(replace(source, electric_lines_summary=changed))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_high_level_rejects_duplicate_or_missing_layer_inventory`

**Purpose:** Regression invariant: high level rejects duplicate or missing layer inventory. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_high_level_rejects_duplicate_or_missing_layer_inventory() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        IgnGridNormalizationError,<br>        match="integrity\|inventory\|duplicate",<br>    )`
  - `pytest.raises(<br>        IgnGridNormalizationError,<br>        match="integrity\|inventory\|selected",<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_bundle` | `tests.unit.test_normalize_grid_ign._source_bundle` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `normalize_ign_electricity` | `tests.unit.test_normalize_grid_ign.normalize_ign_electricity` |

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
def test_high_level_rejects_duplicate_or_missing_layer_inventory() -> None:
    source = _source_bundle()
    duplicate = replace(
        source,
        extraction=replace(
            source.extraction,
            all_layer_names=(LINE_LAYER, POST_LAYER, LINE_LAYER),
        ),
    )
    with pytest.raises(
        IgnGridNormalizationError,
        match="integrity|inventory|duplicate",
    ):
        normalize_ign_electricity(duplicate)

    missing = replace(
        source,
        extraction=replace(
            source.extraction,
            all_layer_names=(POST_LAYER,),
        ),
    )
    with pytest.raises(
        IgnGridNormalizationError,
        match="integrity|inventory|selected",
    ):
        normalize_ign_electricity(missing)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_high_level_rejects_colliding_electricity_roles`

**Purpose:** Regression invariant: high level rejects colliding electricity roles. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_high_level_rejects_colliding_electricity_roles() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        IgnGridNormalizationError,<br>        match="integrity\|same layer\|distinct\|role",<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_bundle` | `tests.unit.test_normalize_grid_ign._source_bundle` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `normalize_ign_electricity` | `tests.unit.test_normalize_grid_ign.normalize_ign_electricity` |

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
def test_high_level_rejects_colliding_electricity_roles() -> None:
    source = _source_bundle()
    extraction = replace(
        source.extraction,
        transformation_posts_layer=LINE_LAYER,
    )
    post_summary = replace(
        source.transformation_posts_summary,
        source_layer_name=LINE_LAYER,
    )

    with pytest.raises(
        IgnGridNormalizationError,
        match="integrity|same layer|distinct|role",
    ):
        normalize_ign_electricity(
            replace(
                source,
                extraction=extraction,
                transformation_posts_summary=post_summary,
            )
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_high_level_rejects_stale_geometry_counts_after_frame_mutation`

**Purpose:** Regression invariant: high level rejects stale geometry counts after frame mutation. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_high_level_rejects_stale_geometry_counts_after_frame_mutation() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        IgnGridNormalizationError,<br>        match="freshly read physical source\|geometry summary",<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_bundle` | `tests.unit.test_normalize_grid_ign._source_bundle` |
| `source.electric_lines.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `normalize_ign_electricity` | `tests.unit.test_normalize_grid_ign.normalize_ign_electricity` |
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
| In-memory mutation | `mutated.at[mutated.index[0], "geometry"] = None` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_high_level_rejects_stale_geometry_counts_after_frame_mutation() -> None:
    source = _source_bundle()
    mutated = source.electric_lines.copy()
    mutated.at[mutated.index[0], "geometry"] = None

    with pytest.raises(
        IgnGridNormalizationError,
        match="freshly read physical source|geometry summary",
    ):
        normalize_ign_electricity(replace(source, electric_lines=mutated))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_high_level_rejects_stale_geometry_types_after_frame_mutation`

**Purpose:** Regression invariant: high level rejects stale geometry types after frame mutation. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_high_level_rejects_stale_geometry_types_after_frame_mutation() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        IgnGridNormalizationError,<br>        match="freshly read physical source\|geometry summary",<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_bundle` | `tests.unit.test_normalize_grid_ign._source_bundle` |
| `source.electric_lines.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `MultiLineString` | `shapely.geometry.MultiLineString` |
| `pytest.raises` | `pytest.raises` |
| `normalize_ign_electricity` | `tests.unit.test_normalize_grid_ign.normalize_ign_electricity` |
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
| In-memory mutation | `mutated.at[mutated.index[0], "geometry"] = MultiLineString(<br>        [[(0, 0), (10, 10)], [(20, 20), (30, 30)]]<br>    )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_high_level_rejects_stale_geometry_types_after_frame_mutation() -> None:
    source = _source_bundle()
    mutated = source.electric_lines.copy()
    mutated.at[mutated.index[0], "geometry"] = MultiLineString(
        [[(0, 0), (10, 10)], [(20, 20), (30, 30)]]
    )

    with pytest.raises(
        IgnGridNormalizationError,
        match="freshly read physical source|geometry summary",
    ):
        normalize_ign_electricity(replace(source, electric_lines=mutated))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_high_level_rejects_any_spatial_role_mismatch`

**Purpose:** Regression invariant: high level rejects any spatial role mismatch. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_high_level_rejects_any_spatial_role_mismatch(component: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "component", ["source", "extraction", "archive", "line_summary", "post_summary"]
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `component` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        IgnGridNormalizationError,<br>        match="source-complete\|role\|spatial\|lineage\|integrity\|PROXY_GEOMETRY",<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_bundle` | `tests.unit.test_normalize_grid_ign._source_bundle` |
| `cast` | `typing.cast` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `normalize_ign_electricity` | `tests.unit.test_normalize_grid_ign.normalize_ign_electricity` |
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
def test_high_level_rejects_any_spatial_role_mismatch(component: str) -> None:
    source = _source_bundle()
    wrong_role = cast(Any, "EXACT_RTE_GEOMETRY")
    if component == "source":
        inconsistent = replace(source, spatial_role=wrong_role)
    elif component == "extraction":
        inconsistent = replace(
            source, extraction=replace(source.extraction, spatial_role=wrong_role)
        )
    elif component == "archive":
        extraction = replace(
            source.extraction,
            archive=replace(source.extraction.archive, spatial_role=wrong_role),
        )
        inconsistent = replace(source, extraction=extraction)
    elif component == "line_summary":
        inconsistent = replace(
            source,
            electric_lines_summary=replace(
                source.electric_lines_summary, spatial_role=wrong_role
            ),
        )
    else:
        inconsistent = replace(
            source,
            transformation_posts_summary=replace(
                source.transformation_posts_summary, spatial_role=wrong_role
            ),
        )

    with pytest.raises(
        IgnGridNormalizationError,
        match="source-complete|role|spatial|lineage|integrity|PROXY_GEOMETRY",
    ):
        normalize_ign_electricity(inconsistent)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.


## 7. Test-specific regression contract

- Test functions: **51**.
- Pytest fixtures (decorator-proven): **0**.

### Per-test regression index

| Test | Parametrization | Expected exception contexts | Assertion count | Exact regression purpose |
|---|---|---|---:|---|
| `test_low_level_normalization_is_not_part_of_stages_public_api` | pytest.mark.parametrize(<br>    "name",<br>    [<br>        "IgnGridSourceContext",<br>        "normalize_ign_electric_lines",<br>        "normalize_ign_transformation_posts",<br>    ],<br>) | none | 2 | Proves low level normalization is not part of stages public api using the exact source reproduced in section 7. |
| `test_supported_package_api_keeps_high_level_normalization` | none | none | 3 | Proves supported package api keeps high level normalization using the exact source reproduced in section 7. |
| `test_internal_source_context_accepts_supported_department_codes` | pytest.mark.parametrize("department_code", ["31", "2A", "2B", "971", "976"]) | none | 0 | Proves internal source context accepts supported department codes using the exact source reproduced in section 7. |
| `test_internal_source_context_rejects_uppercase_sha256` | none | pytest.raises(IgnGridNormalizationError, match="archive_sha256") | 0 | Proves internal source context rejects uppercase sha256 using the exact source reproduced in section 7. |
| `test_grid_summary_requires_strict_structural_types` | pytest.mark.parametrize(<br>    ("field", "value"),<br>    [<br>        ("feature_count", True),<br>        ("feature_count", 1.0),<br>        ("feature_count", "1"),<br>        ("feature_count", -1),<br>        ("null_geometry_count", False),<br>        ("null_geometry_count", 0.0),<br>        ("empty_geometry_count", "0"),<br>        ("invalid_geometry_count", -1),<br>        ("columns", ["cleabs", "geometry"]),<br>        ("columns", ("cleabs", "cleabs")),<br>        ("dtypes", [("cleabs", "str")]),<br>        ("dtypes", (("cleabs",),)),<br>        ("geometry_types", ["LineString"]),<br>    ],<br>) | pytest.raises(IgnGridNormalizationError) | 0 | Proves grid summary requires strict structural types using the exact source reproduced in section 7. |
| `test_grid_archive_sha256_requires_canonical_lowercase` | pytest.mark.parametrize("value", ["A" * 64, "a" * 63, "a" * 65, "g" * 64]) | pytest.raises(IgnGridNormalizationError) | 0 | Proves grid archive sha256 requires canonical lowercase using the exact source reproduced in section 7. |
| `test_internal_source_context_rejects_invalid_lineage_values` | pytest.mark.parametrize(<br>    ("field", "value"),<br>    [<br>        ("source_layer", ""),<br>        ("source_layer", " LIGNE_ELECTRIQUE "),<br>        ("source_layer", 42),<br>        ("department_code", "XYZ"),<br>        ("edition", "2026-02-31"),<br>        ("download_timestamp", "not-a-datetime"),<br>        ("download_timestamp", "2026-08-11T15:32:03"),<br>        ("archive_sha256", "a" * 63),<br>        ("archive_sha256", "g" * 64),<br>        ("source_url", "not-a-url"),<br>        ("source_url", "file:///tmp/archive.7z"),<br>        ("product_version", ""),<br>        ("product_version", " 3.5 "),<br>    ],<br>) | pytest.raises(IgnGridNormalizationError) | 0 | Proves internal source context rejects invalid lineage values using the exact source reproduced in section 7. |
| `test_exact_voltage_parser_is_generic_and_finite` | pytest.mark.parametrize(<br>    ("raw", "expected_kv"),<br>    [<br>        ("63 kV", 63.0),<br>        ("150 kV", 150.0),<br>        ("225 kV", 225.0),<br>        ("400 kV", 400.0),<br>        ("110 kV", 110.0),<br>        ("  90 KV  ", 90.0),<br>        ("72,5 kv", 72.5),<br>    ],<br>) | none | 5 | Proves exact voltage parser is generic and finite using the exact source reproduced in section 7. |
| `test_bounded_voltage_is_generic_finite_and_not_exact` | pytest.mark.parametrize(<br>    ("raw", "expected_upper_bound"),<br>    [("<63 kV", 63.0), ("<90 kV", 90.0), (" < 110 KV ", 110.0)],<br>) | none | 5 | Proves bounded voltage is generic finite and not exact using the exact source reproduced in section 7. |
| `test_unknown_voltage_parser` | pytest.mark.parametrize("raw", ["Inconnue", " INCONNUE ", "inconnu", None]) | none | 4 | Proves unknown voltage parser using the exact source reproduced in section 7. |
| `test_deenergized_voltage_parser` | pytest.mark.parametrize("raw", ["Hors tension", " HORS TENSION "]) | none | 4 | Proves deenergized voltage parser using the exact source reproduced in section 7. |
| `test_unexpected_or_non_scalar_voltage_is_controlled_unparsed` | pytest.mark.parametrize(<br>    "value",<br>    ["Très haute tension future", ["63 kV"], np.array(["63 kV"])],<br>) | none | 3 | Proves unexpected or non scalar voltage is controlled unparsed using the exact source reproduced in section 7. |
| `test_invalid_or_overflowing_numeric_voltage_is_unparsed` | pytest.mark.parametrize(<br>    "raw",<br>    ["0 kV", "<0 kV", "-63 kV", "63 V", f"{'9' * 400} kV", f"<{'9' * 400} kV"],<br>) | none | 3 | Proves invalid or overflowing numeric voltage is unparsed using the exact source reproduced in section 7. |
| `test_valid_line_has_stable_identity_lineage_and_range_index` | none | none | 18 | Proves valid line has stable identity lineage and range index using the exact source reproduced in section 7. |
| `test_deenergized_voltage_does_not_override_source_asset_status` | none | none | 2 | Proves deenergized voltage does not override source asset status using the exact source reproduced in section 7. |
| `test_null_or_empty_line_cleabs_fails` | pytest.mark.parametrize("identifier", [None, "", "   "]) | pytest.raises(IgnGridNormalizationError, match="cleabs\|null\|empty") | 0 | Proves null or empty line cleabs fails using the exact source reproduced in section 7. |
| `test_unsafe_source_id_is_rejected_without_rewriting` | pytest.mark.parametrize(<br>    "identifier",<br>    [" leading", "trailing ", "IGN:BAD", "IGN\nCONTROL", "IGN\tCONTROL"],<br>) | pytest.raises(IgnGridNormalizationError, match="cleabs\|whitespace\|control\|:") | 0 | Proves unsafe source id is rejected without rewriting using the exact source reproduced in section 7. |
| `test_duplicate_line_cleabs_fails` | none | pytest.raises(IgnGridNormalizationError, match="unique") | 0 | Proves duplicate line cleabs fails using the exact source reproduced in section 7. |
| `test_line_missing_or_wrong_crs_fails` | pytest.mark.parametrize("crs", [None, "EPSG:4326", "EPSG:3857"]) | pytest.raises(IgnGridNormalizationError, match="CRS\|2154") | 0 | Proves line missing or wrong crs fails using the exact source reproduced in section 7. |
| `test_line_geometry_quality_is_preserved_without_row_loss_or_repair` | none | none | 5 | Proves line geometry quality is preserved without row loss or repair using the exact source reproduced in section 7. |
| `test_z_coordinates_are_preserved` | none | none | 3 | Proves z coordinates are preserved using the exact source reproduced in section 7. |
| `test_unusual_duplicate_source_index_is_not_preserved_as_identity` | none | none | 4 | Proves unusual duplicate source index is not preserved as identity using the exact source reproduced in section 7. |
| `test_line_normalization_does_not_mutate_input_and_has_stable_columns` | none | none | 1 | Proves line normalization does not mutate input and has stable columns using the exact source reproduced in section 7. |
| `test_missing_required_line_field_fails` | pytest.mark.parametrize("column", ["cleabs", "geometry", "identifiants_sources"]) | pytest.raises(IgnGridNormalizationError, match=column) | 0 | Proves missing required line field fails using the exact source reproduced in section 7. |
| `test_valid_or_null_line_precision_is_normalized_to_float` | pytest.mark.parametrize("precision", [0, 2.5, None, float("nan")]) | none | 3 | Proves valid or null line precision is normalized to float using the exact source reproduced in section 7. |
| `test_invalid_line_precision_fails` | pytest.mark.parametrize("precision", [-1, float("inf"), float("-inf"), True, "2.5"]) | pytest.raises(IgnGridNormalizationError, match="precision_planimetrique") | 0 | Proves invalid line precision fails using the exact source reproduced in section 7. |
| `test_normalized_voltage_never_emits_non_finite_numeric_values` | none | none | 3 | Proves normalized voltage never emits non finite numeric values using the exact source reproduced in section 7. |
| `test_valid_post_has_stable_lineage_and_no_voltage_inference` | none | none | 10 | Proves valid post has stable lineage and no voltage inference using the exact source reproduced in section 7. |
| `test_post_geometry_crs_and_input_are_preserved` | none | none | 2 | Proves post geometry crs and input are preserved using the exact source reproduced in section 7. |
| `test_duplicate_post_cleabs_fails` | none | pytest.raises(IgnGridNormalizationError, match="unique") | 0 | Proves duplicate post cleabs fails using the exact source reproduced in section 7. |
| `test_null_post_geometry_and_precision_are_preserved` | none | none | 5 | Proves null post geometry and precision are preserved using the exact source reproduced in section 7. |
| `test_invalid_post_precision_fails` | none | pytest.raises(IgnGridNormalizationError, match="precision_planimetrique") | 0 | Proves invalid post precision fails using the exact source reproduced in section 7. |
| `test_appropriate_multigeometry_types_are_accepted` | none | none | 4 | Proves appropriate multigeometry types are accepted using the exact source reproduced in section 7. |
| `test_valid_polygon_or_point_is_rejected_as_electric_line` | pytest.mark.parametrize(<br>    "geometry",<br>    [<br>        Polygon([(0, 0), (0, 5), (5, 5), (5, 0), (0, 0)]),<br>        Point(1, 1),<br>    ],<br>) | pytest.raises(IgnGridNormalizationError, match="geometry types") | 0 | Proves valid polygon or point is rejected as electric line using the exact source reproduced in section 7. |
| `test_valid_line_or_point_is_rejected_as_transformation_post` | pytest.mark.parametrize("geometry", [LineString([(0, 0), (10, 10)]), Point(1, 1)]) | pytest.raises(IgnGridNormalizationError, match="geometry types") | 0 | Proves valid line or point is rejected as transformation post using the exact source reproduced in section 7. |
| `test_high_level_path_uses_discovered_layer_names_and_archive_lineage` | none | none | 7 | Proves high level path uses discovered layer names and archive lineage using the exact source reproduced in section 7. |
| `test_high_level_rejects_coordinated_frame_and_summary_forgery` | none | pytest.raises(IgnGridNormalizationError, match="physical\|fresh\|source") | 0 | Proves high level rejects coordinated frame and summary forgery using the exact source reproduced in section 7. |
| `test_source_complete_grid_validation_does_not_mutate_supplied_frames` | none | none | 0 | Proves source complete grid validation does not mutate supplied frames using the exact source reproduced in section 7. |
| `test_grid_normalization_uses_distinct_fresh_revalidated_frames` | none | none | 2 | Proves grid normalization uses distinct fresh revalidated frames using the exact source reproduced in section 7. |
| `test_high_level_rejects_incompatible_archive_identity` | pytest.mark.parametrize(<br>    ("field", "value"),<br>    [<br>        ("provider", "Unrelated data vendor"),<br>        ("product", "OTHER PRODUCT"),<br>        ("projection", "EPSG:4326"),<br>    ],<br>) | pytest.raises(IgnGridNormalizationError, match="lineage\|config") | 0 | Proves high level rejects incompatible archive identity using the exact source reproduced in section 7. |
| `test_archive_identity_requires_exact_pinned_strings` | none | pytest.raises(IgnGridNormalizationError, match="provider\|product\|config") | 0 | Proves archive identity requires exact pinned strings using the exact source reproduced in section 7. |
| `test_high_level_rejects_summary_row_count_mismatch` | none | pytest.raises(IgnGridNormalizationError, match="summary\|physical") | 0 | Proves high level rejects summary row count mismatch using the exact source reproduced in section 7. |
| `test_high_level_rejects_summary_layer_name_mismatch` | none | pytest.raises(IgnGridNormalizationError, match="summary\|physical") | 0 | Proves high level rejects summary layer name mismatch using the exact source reproduced in section 7. |
| `test_high_level_rejects_wrong_logical_name` | none | pytest.raises(IgnGridNormalizationError, match="summary\|physical") | 0 | Proves high level rejects wrong logical name using the exact source reproduced in section 7. |
| `test_high_level_rejects_summary_crs_mismatch` | none | pytest.raises(IgnGridNormalizationError, match="summary\|physical\|CRS\|2154") | 0 | Proves high level rejects summary crs mismatch using the exact source reproduced in section 7. |
| `test_high_level_rejects_forged_ordered_summary_schema` | pytest.mark.parametrize("mutation", ["missing", "extra", "reordered", "dtype"]) | pytest.raises(<br>        IgnGridNormalizationError,<br>        match="summary\|physical\|schema\|columns\|dtype",<br>    ) | 0 | Proves high level rejects forged ordered summary schema using the exact source reproduced in section 7. |
| `test_high_level_rejects_duplicate_or_missing_layer_inventory` | none | pytest.raises(<br>        IgnGridNormalizationError,<br>        match="integrity\|inventory\|duplicate",<br>    ); pytest.raises(<br>        IgnGridNormalizationError,<br>        match="integrity\|inventory\|selected",<br>    ) | 0 | Proves high level rejects duplicate or missing layer inventory using the exact source reproduced in section 7. |
| `test_high_level_rejects_colliding_electricity_roles` | none | pytest.raises(<br>        IgnGridNormalizationError,<br>        match="integrity\|same layer\|distinct\|role",<br>    ) | 0 | Proves high level rejects colliding electricity roles using the exact source reproduced in section 7. |
| `test_high_level_rejects_stale_geometry_counts_after_frame_mutation` | none | pytest.raises(<br>        IgnGridNormalizationError,<br>        match="freshly read physical source\|geometry summary",<br>    ) | 0 | Proves high level rejects stale geometry counts after frame mutation using the exact source reproduced in section 7. |
| `test_high_level_rejects_stale_geometry_types_after_frame_mutation` | none | pytest.raises(<br>        IgnGridNormalizationError,<br>        match="freshly read physical source\|geometry summary",<br>    ) | 0 | Proves high level rejects stale geometry types after frame mutation using the exact source reproduced in section 7. |
| `test_high_level_rejects_any_spatial_role_mismatch` | pytest.mark.parametrize(<br>    "component", ["source", "extraction", "archive", "line_summary", "post_summary"]<br>) | pytest.raises(<br>        IgnGridNormalizationError,<br>        match="source-complete\|role\|spatial\|lineage\|integrity\|PROXY_GEOMETRY",<br>    ) | 0 | Proves high level rejects any spatial role mismatch using the exact source reproduced in section 7. |

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
from math import isfinite
from pathlib import Path
from typing import Any, Literal, cast
from uuid import uuid4

import geopandas as gpd
import numpy as np
import pandas as pd
import pyogrio
import pytest
from geopandas.testing import assert_geodataframe_equal
from shapely.geometry import (
    LineString,
    MultiLineString,
    MultiPolygon,
    Point,
    Polygon,
)

import landscout.stages.normalize_grid_ign as grid_normalization
from landscout import stages
from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_source_config,
)
from landscout.stages.normalize_grid_ign import (
    LINE_OUTPUT_COLUMNS,
    TRANSFORMATION_POST_OUTPUT_COLUMNS,
    IgnGridNormalizationError,
    NormalizedIgnElectricityData,
    parse_ign_voltage,
)
from landscout.stages.normalize_grid_ign import (
    _IgnGridSourceContext as IgnGridSourceContext,
)
from landscout.stages.normalize_grid_ign import (
    _normalize_ign_electric_lines as normalize_ign_electric_lines,
)
from landscout.stages.normalize_grid_ign import (
    _normalize_ign_transformation_posts as normalize_ign_transformation_posts,
)
from landscout.stages.normalize_grid_ign import (
    normalize_ign_electricity as _normalize_ign_electricity,
)

LINE_LAYER = "LIGNE_ELECTRIQUE_V2"
POST_LAYER = "POSTE_DE_TRANSFORMATION_V2"
ROAD_LAYER = "TRONCON_DE_ROUTE"
DEPARTMENT_LAYER = "DEPARTEMENT"
ARCHIVE_SHA256 = "a" * 64
SOURCE_URL = "https://example.test/BDTOPO_D031.7z"
_FIXTURE_ROOT = Path(tempfile.mkdtemp(prefix="landscout-grid-ign-"))
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


def normalize_ign_electricity(
    source: IgnBdTopoElectricityData,
) -> NormalizedIgnElectricityData:
    return _normalize_ign_electricity(source, SOURCE_CONFIG)


def _line_source(
    geometries: list[object] | None = None,
    *,
    identifiers: list[object] | None = None,
    voltages: list[object] | None = None,
    precisions: list[object] | None = None,
    crs: str | None = "EPSG:2154",
    index: list[object] | None = None,
) -> gpd.GeoDataFrame:
    source_geometries = (
        geometries if geometries is not None else [LineString([(0, 0), (100, 100)])]
    )
    count = len(source_geometries)
    source_ids = (
        identifiers
        if identifiers is not None
        else [f"LIGNE-{item + 1}" for item in range(count)]
    )
    source_voltages = voltages if voltages is not None else ["225 kV"] * count
    source_precisions = precisions if precisions is not None else [2.5] * count
    source_index = index if index is not None else [100 + item for item in range(count)]
    return gpd.GeoDataFrame(
        {
            "cleabs": source_ids,
            "voltage": source_voltages,
            "gestionnaire": ["Réseau de Transport d'Électricité"] * count,
            "siren_gestionnaire": ["444619258"] * count,
            "etat_de_l_objet": ["En service"] * count,
            "sources": ["RTE 2024"] * count,
            "identifiants_sources": ["source-id"] * count,
            "date_creation": pd.to_datetime(["2024-01-01"] * count),
            "date_modification": pd.to_datetime(["2025-01-01"] * count),
            "date_de_confirmation": pd.to_datetime(["2024-12-18"] * count),
            "methode_d_acquisition_planimetrique": ["Photogrammétrie"] * count,
            "precision_planimetrique": source_precisions,
        },
        geometry=source_geometries,
        crs=crs,
        index=source_index,
    )


def _post_source(
    geometries: list[object] | None = None,
    *,
    identifiers: list[object] | None = None,
    precisions: list[object] | None = None,
    crs: str | None = "EPSG:2154",
    index: list[object] | None = None,
) -> gpd.GeoDataFrame:
    source_geometries = (
        geometries
        if geometries is not None
        else [Polygon([(0, 0), (0, 20), (20, 20), (20, 0), (0, 0)])]
    )
    count = len(source_geometries)
    source_ids = (
        identifiers
        if identifiers is not None
        else [f"POSTE-{item + 1}" for item in range(count)]
    )
    source_precisions = precisions if precisions is not None else [5.0] * count
    source_index = index if index is not None else [200 + item for item in range(count)]
    return gpd.GeoDataFrame(
        {
            "cleabs": source_ids,
            "toponyme": ["Poste de test"] * count,
            "statut_du_toponyme": ["Validé"] * count,
            "importance": ["5"] * count,
            "etat_de_l_objet": ["En service"] * count,
            "sources": ["RTE 2021"] * count,
            "identifiants_sources": ["source-post-id"] * count,
            "date_creation": pd.to_datetime(["2023-01-01"] * count),
            "date_modification": pd.to_datetime(["2025-02-01"] * count),
            "date_de_confirmation": pd.to_datetime(["2025-01-15"] * count),
            "methode_d_acquisition_planimetrique": ["Orthophotographie"] * count,
            "precision_planimetrique": source_precisions,
        },
        geometry=source_geometries,
        crs=crs,
        index=source_index,
    )


def _context(source_layer: str) -> IgnGridSourceContext:
    return IgnGridSourceContext(
        source_layer=source_layer,
        department_code="31",
        edition="2026-06-15",
        product_version="3.5",
        download_timestamp="2026-08-11T15:32:03+00:00",
        archive_sha256=ARCHIVE_SHA256,
        source_url=SOURCE_URL,
    )


def _summary(
    frame: gpd.GeoDataFrame,
    logical_name: Literal["electric_lines", "transformation_posts"],
    layer_name: str,
) -> IgnBdTopoLayerSummary:
    geometry = frame.geometry
    null_mask = geometry.isna()
    empty_mask = ~null_mask & geometry.is_empty
    invalid_mask = ~null_mask & ~geometry.is_empty & ~geometry.is_valid
    geometry_types = tuple(
        sorted(str(value) for value in geometry[~null_mask].geom_type.dropna().unique())
    )
    return IgnBdTopoLayerSummary(
        logical_name=logical_name,
        source_layer_name=layer_name,
        crs=str(frame.crs),
        feature_count=len(frame),
        columns=tuple(str(column) for column in frame.columns),
        dtypes=tuple(
            (str(column), str(dtype)) for column, dtype in frame.dtypes.items()
        ),
        null_geometry_count=int(null_mask.sum()),
        empty_geometry_count=int(empty_mask.sum()),
        invalid_geometry_count=int(invalid_mask.sum()),
        geometry_types=geometry_types,
    )


def _source_bundle(
    lines: gpd.GeoDataFrame | None = None,
    posts: gpd.GeoDataFrame | None = None,
) -> IgnBdTopoElectricityData:
    line_frame = lines if lines is not None else _line_source()
    post_frame = posts if posts is not None else _post_source()
    extraction_path = _FIXTURE_ROOT / uuid4().hex
    extraction_path.mkdir(parents=True)
    geopackage_path = extraction_path / "data.gpkg"
    pyogrio.write_dataframe(
        line_frame, geopackage_path, layer=LINE_LAYER, driver="GPKG"
    )
    pyogrio.write_dataframe(
        post_frame,
        geopackage_path,
        layer=POST_LAYER,
        driver="GPKG",
        append=True,
    )
    pyogrio.write_dataframe(
        gpd.GeoDataFrame(
            {"id": ["road"]},
            geometry=[LineString([(0, 0), (1, 1)])],
            crs="EPSG:2154",
        ),
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
    line_frame = gpd.read_file(geopackage_path, layer=LINE_LAYER, engine="pyogrio")
    post_frame = gpd.read_file(geopackage_path, layer=POST_LAYER, engine="pyogrio")
    payload = geopackage_path.read_bytes()
    layer_names = tuple(str(row[0]) for row in pyogrio.list_layers(geopackage_path))
    digest = sha256(payload).hexdigest()
    marker = {
        "schema_version": 3,
        "archive_sha256": ARCHIVE_SHA256,
        "geopackage_relative_path": "data.gpkg",
        "geopackage_size_bytes": len(payload),
        "geopackage_sha256": digest,
        "all_layer_names": list(layer_names),
        "electric_lines_layer": LINE_LAYER,
        "transformation_posts_layer": POST_LAYER,
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
    (extraction_path / ".landscout-extraction.json").write_text(
        json.dumps(marker), encoding="utf-8"
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
        electric_lines_layer=LINE_LAYER,
        transformation_posts_layer=POST_LAYER,
        road_segments_layer=ROAD_LAYER,
        department_layer=DEPARTMENT_LAYER,
        cache_hit=True,
    )
    return IgnBdTopoElectricityData(
        extraction=extraction,
        electric_lines=line_frame,
        transformation_posts=post_frame,
        electric_lines_summary=_summary(line_frame, "electric_lines", LINE_LAYER),
        transformation_posts_summary=_summary(
            post_frame, "transformation_posts", POST_LAYER
        ),
    )


def _source_bundle_with_archive(**changes: object) -> IgnBdTopoElectricityData:
    source = _source_bundle()
    archive = replace(source.extraction.archive, **changes)
    return replace(source, extraction=replace(source.extraction, archive=archive))


@pytest.mark.parametrize(
    "name",
    [
        "IgnGridSourceContext",
        "normalize_ign_electric_lines",
        "normalize_ign_transformation_posts",
    ],
)
def test_low_level_normalization_is_not_part_of_stages_public_api(name: str) -> None:
    assert name not in stages.__all__
    assert not hasattr(stages, name)


def test_supported_package_api_keeps_high_level_normalization() -> None:
    expected_names = {
        "IgnGridNormalizationError",
        "IgnVoltageNormalization",
        "NormalizedIgnElectricityData",
        "parse_ign_voltage",
        "normalize_ign_electricity",
    }

    assert expected_names <= set(stages.__all__)
    normalized = stages.normalize_ign_electricity(_source_bundle(), SOURCE_CONFIG)
    assert normalized.electric_lines["source_layer"].unique().tolist() == [LINE_LAYER]
    assert normalized.transformation_posts["source_layer"].unique().tolist() == [
        POST_LAYER
    ]


@pytest.mark.parametrize("department_code", ["31", "2A", "2B", "971", "976"])
def test_internal_source_context_accepts_supported_department_codes(
    department_code: str,
) -> None:
    context = replace(_context(LINE_LAYER), department_code=department_code)

    grid_normalization._validate_source_context(context)


def test_internal_source_context_rejects_uppercase_sha256() -> None:
    archive_sha256 = "A" * 64
    context = replace(_context(LINE_LAYER), archive_sha256=archive_sha256)

    with pytest.raises(IgnGridNormalizationError, match="archive_sha256"):
        normalize_ign_electric_lines(_line_source(), context)


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
def test_grid_summary_requires_strict_structural_types(
    field: str, value: object
) -> None:
    source = _source_bundle()
    changed = replace(source.electric_lines_summary, **{field: value})

    with pytest.raises(IgnGridNormalizationError):
        normalize_ign_electricity(replace(source, electric_lines_summary=changed))


@pytest.mark.parametrize("value", ["A" * 64, "a" * 63, "a" * 65, "g" * 64])
def test_grid_archive_sha256_requires_canonical_lowercase(value: str) -> None:
    source = _source_bundle_with_archive(sha256=value)

    with pytest.raises(IgnGridNormalizationError):
        normalize_ign_electricity(source)


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("source_layer", ""),
        ("source_layer", " LIGNE_ELECTRIQUE "),
        ("source_layer", 42),
        ("department_code", "XYZ"),
        ("edition", "2026-02-31"),
        ("download_timestamp", "not-a-datetime"),
        ("download_timestamp", "2026-08-11T15:32:03"),
        ("archive_sha256", "a" * 63),
        ("archive_sha256", "g" * 64),
        ("source_url", "not-a-url"),
        ("source_url", "file:///tmp/archive.7z"),
        ("product_version", ""),
        ("product_version", " 3.5 "),
    ],
)
def test_internal_source_context_rejects_invalid_lineage_values(
    field: str,
    value: object,
) -> None:
    context = replace(_context(LINE_LAYER), **{field: value})

    with pytest.raises(IgnGridNormalizationError):
        grid_normalization._validate_source_context(context)


@pytest.mark.parametrize(
    ("raw", "expected_kv"),
    [
        ("63 kV", 63.0),
        ("150 kV", 150.0),
        ("225 kV", 225.0),
        ("400 kV", 400.0),
        ("110 kV", 110.0),
        ("  90 KV  ", 90.0),
        ("72,5 kv", 72.5),
    ],
)
def test_exact_voltage_parser_is_generic_and_finite(
    raw: str, expected_kv: float
) -> None:
    parsed = parse_ign_voltage(raw)

    assert parsed.raw == raw
    assert parsed.status == "EXACT"
    assert parsed.voltage_kv == expected_kv
    assert parsed.voltage_kv is not None and isfinite(parsed.voltage_kv)
    assert parsed.voltage_upper_bound_kv is None


@pytest.mark.parametrize(
    ("raw", "expected_upper_bound"),
    [("<63 kV", 63.0), ("<90 kV", 90.0), (" < 110 KV ", 110.0)],
)
def test_bounded_voltage_is_generic_finite_and_not_exact(
    raw: str, expected_upper_bound: float
) -> None:
    parsed = parse_ign_voltage(raw)

    assert parsed.raw == raw
    assert parsed.status == "BELOW"
    assert parsed.voltage_kv is None
    assert parsed.voltage_upper_bound_kv == expected_upper_bound
    assert isfinite(parsed.voltage_upper_bound_kv)


@pytest.mark.parametrize("raw", ["Inconnue", " INCONNUE ", "inconnu", None])
def test_unknown_voltage_parser(raw: str | None) -> None:
    parsed = parse_ign_voltage(raw)

    assert parsed.raw == raw
    assert parsed.status == "UNKNOWN"
    assert parsed.voltage_kv is None
    assert parsed.voltage_upper_bound_kv is None


@pytest.mark.parametrize("raw", ["Hors tension", " HORS TENSION "])
def test_deenergized_voltage_parser(raw: str) -> None:
    parsed = parse_ign_voltage(raw)

    assert parsed.raw == raw
    assert parsed.status == "DEENERGIZED"
    assert parsed.voltage_kv is None
    assert parsed.voltage_upper_bound_kv is None


@pytest.mark.parametrize(
    "value",
    ["Très haute tension future", ["63 kV"], np.array(["63 kV"])],
)
def test_unexpected_or_non_scalar_voltage_is_controlled_unparsed(
    value: object,
) -> None:
    parsed = parse_ign_voltage(value)

    assert parsed.status == "UNPARSED"
    assert parsed.voltage_kv is None
    assert parsed.voltage_upper_bound_kv is None


@pytest.mark.parametrize(
    "raw",
    ["0 kV", "<0 kV", "-63 kV", "63 V", f"{'9' * 400} kV", f"<{'9' * 400} kV"],
)
def test_invalid_or_overflowing_numeric_voltage_is_unparsed(raw: str) -> None:
    parsed = parse_ign_voltage(raw)

    assert parsed.status == "UNPARSED"
    assert parsed.voltage_kv is None
    assert parsed.voltage_upper_bound_kv is None


def test_valid_line_has_stable_identity_lineage_and_range_index() -> None:
    source = _line_source()

    normalized = normalize_ign_electric_lines(source, _context(LINE_LAYER))

    row = normalized.iloc[0]
    assert list(normalized.columns) == list(LINE_OUTPUT_COLUMNS)
    assert isinstance(normalized.index, pd.RangeIndex)
    assert row["grid_feature_id"] == "IGN_BDTOPO:ELECTRIC_LINE:LIGNE-1"
    assert row["source_feature_id"] == "LIGNE-1"
    assert row["source_provider"] == "IGN"
    assert row["source_product"] == "BD_TOPO"
    assert row["source_layer"] == LINE_LAYER
    assert row["source_department_code"] == "31"
    assert row["source_edition"] == "2026-06-15"
    assert row["source_product_version"] == "3.5"
    assert row["source_download_timestamp"] == "2026-08-11T15:32:03+00:00"
    assert row["source_archive_sha256"] == ARCHIVE_SHA256
    assert row["source_url"] == SOURCE_URL
    assert row["manager_name"] == "Réseau de Transport d'Électricité"
    assert row["asset_status_raw"] == "En service"
    assert row["source_identifiers_raw"] == "source-id"
    assert row["planimetric_precision_m"] == 2.5
    assert row["spatial_role"] == "PROXY_GEOMETRY"


def test_deenergized_voltage_does_not_override_source_asset_status() -> None:
    normalized = normalize_ign_electric_lines(
        _line_source(voltages=["Hors tension"]), _context(LINE_LAYER)
    )

    assert normalized.iloc[0]["voltage_status"] == "DEENERGIZED"
    assert normalized.iloc[0]["asset_status_raw"] == "En service"


@pytest.mark.parametrize("identifier", [None, "", "   "])
def test_null_or_empty_line_cleabs_fails(identifier: object) -> None:
    with pytest.raises(IgnGridNormalizationError, match="cleabs|null|empty"):
        normalize_ign_electric_lines(
            _line_source(identifiers=[identifier]), _context(LINE_LAYER)
        )


@pytest.mark.parametrize(
    "identifier",
    [" leading", "trailing ", "IGN:BAD", "IGN\nCONTROL", "IGN\tCONTROL"],
)
def test_unsafe_source_id_is_rejected_without_rewriting(identifier: str) -> None:
    with pytest.raises(IgnGridNormalizationError, match="cleabs|whitespace|control|:"):
        normalize_ign_electric_lines(
            _line_source(identifiers=[identifier]), _context(LINE_LAYER)
        )


def test_duplicate_line_cleabs_fails() -> None:
    source = _line_source(
        geometries=[
            LineString([(0, 0), (10, 10)]),
            LineString([(20, 20), (30, 30)]),
        ],
        identifiers=["DUPLICATE", "DUPLICATE"],
    )

    with pytest.raises(IgnGridNormalizationError, match="unique"):
        normalize_ign_electric_lines(source, _context(LINE_LAYER))


@pytest.mark.parametrize("crs", [None, "EPSG:4326", "EPSG:3857"])
def test_line_missing_or_wrong_crs_fails(crs: str | None) -> None:
    with pytest.raises(IgnGridNormalizationError, match="CRS|2154"):
        normalize_ign_electric_lines(_line_source(crs=crs), _context(LINE_LAYER))


def test_line_geometry_quality_is_preserved_without_row_loss_or_repair() -> None:
    invalid = Polygon([(0, 0), (20, 20), (20, 0), (0, 20), (0, 0)])
    source = _line_source(
        geometries=[LineString([(0, 0), (10, 10)]), None, LineString(), invalid],
        identifiers=["VALID", "NULL", "EMPTY", "INVALID"],
        voltages=["63 kV"] * 4,
    )

    normalized = normalize_ign_electric_lines(source, _context(LINE_LAYER))

    assert normalized["geometry_status"].tolist() == [
        "VALID",
        "NULL",
        "EMPTY",
        "INVALID",
    ]
    assert normalized["source_feature_id"].tolist() == [
        "VALID",
        "NULL",
        "EMPTY",
        "INVALID",
    ]
    assert normalized.geometry.iloc[1] is None
    assert normalized.geometry.iloc[2].is_empty
    assert normalized.geometry.iloc[3].equals_exact(invalid, tolerance=0)


def test_z_coordinates_are_preserved() -> None:
    source = _line_source(geometries=[LineString([(0, 0, 10), (10, 10, 20)])])

    normalized = normalize_ign_electric_lines(source, _context(LINE_LAYER))

    assert source.geometry.iloc[0].has_z
    assert normalized.geometry.iloc[0].has_z
    assert normalized.geometry.iloc[0].equals_exact(
        source.geometry.iloc[0], tolerance=0
    )


def test_unusual_duplicate_source_index_is_not_preserved_as_identity() -> None:
    source = _line_source(
        geometries=[
            LineString([(0, 0), (10, 10)]),
            LineString([(20, 20), (30, 30)]),
        ],
        identifiers=["FIRST", "SECOND"],
        index=[77, 77],
    )

    normalized = normalize_ign_electric_lines(source, _context(LINE_LAYER))

    assert isinstance(normalized.index, pd.RangeIndex)
    assert normalized.index.tolist() == [0, 1]
    assert normalized["source_feature_id"].tolist() == ["FIRST", "SECOND"]
    assert normalized["grid_feature_id"].tolist() == [
        "IGN_BDTOPO:ELECTRIC_LINE:FIRST",
        "IGN_BDTOPO:ELECTRIC_LINE:SECOND",
    ]


def test_line_normalization_does_not_mutate_input_and_has_stable_columns() -> None:
    source = _line_source()
    reordered = source.loc[:, list(reversed(source.columns))].set_geometry("geometry")
    before = deepcopy(reordered)

    normalized = normalize_ign_electric_lines(reordered, _context(LINE_LAYER))

    assert_geodataframe_equal(reordered, before)
    assert list(normalized.columns) == list(LINE_OUTPUT_COLUMNS)


@pytest.mark.parametrize("column", ["cleabs", "geometry", "identifiants_sources"])
def test_missing_required_line_field_fails(column: str) -> None:
    source = _line_source().drop(columns=column)

    with pytest.raises(IgnGridNormalizationError, match=column):
        normalize_ign_electric_lines(source, _context(LINE_LAYER))


@pytest.mark.parametrize("precision", [0, 2.5, None, float("nan")])
def test_valid_or_null_line_precision_is_normalized_to_float(
    precision: object,
) -> None:
    normalized = normalize_ign_electric_lines(
        _line_source(precisions=[precision]), _context(LINE_LAYER)
    )

    assert str(normalized["planimetric_precision_m"].dtype) == "float64"
    if precision is None or (isinstance(precision, float) and np.isnan(precision)):
        assert pd.isna(normalized.iloc[0]["planimetric_precision_m"])
    else:
        assert normalized.iloc[0]["planimetric_precision_m"] == float(precision)


@pytest.mark.parametrize("precision", [-1, float("inf"), float("-inf"), True, "2.5"])
def test_invalid_line_precision_fails(precision: object) -> None:
    with pytest.raises(IgnGridNormalizationError, match="precision_planimetrique"):
        normalize_ign_electric_lines(
            _line_source(precisions=[precision]), _context(LINE_LAYER)
        )


def test_normalized_voltage_never_emits_non_finite_numeric_values() -> None:
    huge = f"{'9' * 400} kV"
    source = _line_source(
        geometries=[LineString([(0, 0), (1, 1)])] * 4,
        identifiers=["EXACT", "BELOW", "OVERFLOW", "MISSING"],
        voltages=["225 kV", "<90 kV", huge, None],
    )

    normalized = normalize_ign_electric_lines(source, _context(LINE_LAYER))

    assert normalized["voltage_status"].tolist() == [
        "EXACT",
        "BELOW",
        "UNPARSED",
        "UNKNOWN",
    ]
    assert np.isfinite(normalized["voltage_kv"].dropna()).all()
    assert np.isfinite(normalized["voltage_upper_bound_kv"].dropna()).all()


def test_valid_post_has_stable_lineage_and_no_voltage_inference() -> None:
    source = _post_source()

    normalized = normalize_ign_transformation_posts(source, _context(POST_LAYER))

    row = normalized.iloc[0]
    assert list(normalized.columns) == list(TRANSFORMATION_POST_OUTPUT_COLUMNS)
    assert isinstance(normalized.index, pd.RangeIndex)
    assert row["grid_feature_id"] == "IGN_BDTOPO:TRANSFORMATION_POST:POSTE-1"
    assert row["source_layer"] == POST_LAYER
    assert row["source_department_code"] == "31"
    assert row["source_archive_sha256"] == ARCHIVE_SHA256
    assert row["name"] == "Poste de test"
    assert row["voltage_status"] == "UNKNOWN"
    assert pd.isna(row["voltage_kv"])
    assert row["spatial_role"] == "PROXY_GEOMETRY"


def test_post_geometry_crs_and_input_are_preserved() -> None:
    source = _post_source()
    before = deepcopy(source)

    normalized = normalize_ign_transformation_posts(source, _context(POST_LAYER))

    assert_geodataframe_equal(source, before)
    assert normalized.crs is not None and normalized.crs.to_epsg() == 2154
    assert normalized.geometry.iloc[0].equals_exact(
        source.geometry.iloc[0], tolerance=0
    )


def test_duplicate_post_cleabs_fails() -> None:
    polygon = Polygon([(0, 0), (0, 20), (20, 20), (20, 0), (0, 0)])
    source = _post_source(
        geometries=[polygon, polygon], identifiers=["DUPLICATE", "DUPLICATE"]
    )

    with pytest.raises(IgnGridNormalizationError, match="unique"):
        normalize_ign_transformation_posts(source, _context(POST_LAYER))


def test_null_post_geometry_and_precision_are_preserved() -> None:
    normalized = normalize_ign_transformation_posts(
        _post_source(geometries=[None], precisions=[None]), _context(POST_LAYER)
    )

    assert normalized.iloc[0]["geometry_status"] == "NULL"
    assert normalized.geometry.iloc[0] is None
    assert normalized.iloc[0]["voltage_status"] == "UNKNOWN"
    assert normalized["voltage_kv"].isna().all()
    assert normalized["planimetric_precision_m"].isna().all()


def test_invalid_post_precision_fails() -> None:
    with pytest.raises(IgnGridNormalizationError, match="precision_planimetrique"):
        normalize_ign_transformation_posts(
            _post_source(precisions=["5.0"]), _context(POST_LAYER)
        )


def test_appropriate_multigeometry_types_are_accepted() -> None:
    multilines = MultiLineString([[(0, 0), (10, 10)], [(20, 20), (30, 30)]])
    multipolygon = MultiPolygon(
        [
            Polygon([(0, 0), (0, 5), (5, 5), (5, 0), (0, 0)]),
            Polygon([(10, 10), (10, 15), (15, 15), (15, 10), (10, 10)]),
        ]
    )

    lines = normalize_ign_electric_lines(
        _line_source(geometries=[multilines]), _context(LINE_LAYER)
    )
    posts = normalize_ign_transformation_posts(
        _post_source(geometries=[multipolygon]), _context(POST_LAYER)
    )

    assert lines.iloc[0]["geometry_status"] == "VALID"
    assert lines.geometry.iloc[0].geom_type == "MultiLineString"
    assert posts.iloc[0]["geometry_status"] == "VALID"
    assert posts.geometry.iloc[0].geom_type == "MultiPolygon"


@pytest.mark.parametrize(
    "geometry",
    [
        Polygon([(0, 0), (0, 5), (5, 5), (5, 0), (0, 0)]),
        Point(1, 1),
    ],
)
def test_valid_polygon_or_point_is_rejected_as_electric_line(
    geometry: object,
) -> None:
    with pytest.raises(IgnGridNormalizationError, match="geometry types"):
        normalize_ign_electric_lines(
            _line_source(geometries=[geometry]), _context(LINE_LAYER)
        )


@pytest.mark.parametrize("geometry", [LineString([(0, 0), (10, 10)]), Point(1, 1)])
def test_valid_line_or_point_is_rejected_as_transformation_post(
    geometry: object,
) -> None:
    with pytest.raises(IgnGridNormalizationError, match="geometry types"):
        normalize_ign_transformation_posts(
            _post_source(geometries=[geometry]), _context(POST_LAYER)
        )


def test_high_level_path_uses_discovered_layer_names_and_archive_lineage() -> None:
    source = _source_bundle()

    normalized = normalize_ign_electricity(source)

    assert normalized.electric_lines["source_layer"].unique().tolist() == [LINE_LAYER]
    assert normalized.transformation_posts["source_layer"].unique().tolist() == [
        POST_LAYER
    ]
    for frame in (normalized.electric_lines, normalized.transformation_posts):
        assert frame["source_department_code"].unique().tolist() == ["31"]
        assert frame["source_edition"].unique().tolist() == ["2026-06-15"]
        assert frame["source_product_version"].unique().tolist() == ["3.5"]
        assert frame["source_archive_sha256"].unique().tolist() == [ARCHIVE_SHA256]
        assert frame["source_url"].unique().tolist() == [SOURCE_URL]


def test_high_level_rejects_coordinated_frame_and_summary_forgery() -> None:
    source = _source_bundle()
    forged = source.electric_lines.copy()
    forged.loc[0, "voltage"] = "400 kV"
    forged_summary = _summary(forged, "electric_lines", LINE_LAYER)

    with pytest.raises(IgnGridNormalizationError, match="physical|fresh|source"):
        normalize_ign_electricity(
            replace(
                source,
                electric_lines=forged,
                electric_lines_summary=forged_summary,
            )
        )


def test_source_complete_grid_validation_does_not_mutate_supplied_frames() -> None:
    source = _source_bundle()
    lines_before = deepcopy(source.electric_lines)
    posts_before = deepcopy(source.transformation_posts)

    normalize_ign_electricity(source)

    assert_geodataframe_equal(source.electric_lines, lines_before)
    assert_geodataframe_equal(source.transformation_posts, posts_before)


def test_grid_normalization_uses_distinct_fresh_revalidated_frames(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    source = _source_bundle()
    fresh = replace(
        source,
        electric_lines=source.electric_lines.copy(deep=True),
        transformation_posts=source.transformation_posts.copy(deep=True),
    )
    expected_voltage = fresh.electric_lines.loc[0, "voltage"]

    def return_fresh_and_mutate_supplied(
        _: object,
        __: object,
    ) -> IgnBdTopoElectricityData:
        source.electric_lines.loc[0, "voltage"] = "FORGED AFTER REVALIDATION"
        return fresh

    monkeypatch.setattr(
        grid_normalization,
        "_revalidate_ign_bdtopo_electricity_data",
        return_fresh_and_mutate_supplied,
    )

    normalized = _normalize_ign_electricity(source, SOURCE_CONFIG)

    assert normalized.electric_lines.loc[0, "voltage_raw"] == expected_voltage
    assert source.electric_lines.loc[0, "voltage"] == "FORGED AFTER REVALIDATION"


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("provider", "Unrelated data vendor"),
        ("product", "OTHER PRODUCT"),
        ("projection", "EPSG:4326"),
    ],
)
def test_high_level_rejects_incompatible_archive_identity(
    field: str,
    value: str,
) -> None:
    source = _source_bundle_with_archive(**{field: value})

    with pytest.raises(IgnGridNormalizationError, match="lineage|config"):
        normalize_ign_electricity(source)


def test_archive_identity_requires_exact_pinned_strings() -> None:
    provider = "INSTITUT NATIONAL DE L'INFORMATION GEOGRAPHIQUE ET FORESTIERE (ign)"
    product = "bd-topo"
    source = _source_bundle_with_archive(
        provider=provider,
        product=product,
    )

    with pytest.raises(IgnGridNormalizationError, match="provider|product|config"):
        normalize_ign_electricity(source)


def test_high_level_rejects_summary_row_count_mismatch() -> None:
    source = _source_bundle()
    summary = replace(
        source.electric_lines_summary,
        feature_count=source.electric_lines_summary.feature_count + 1,
    )

    with pytest.raises(IgnGridNormalizationError, match="summary|physical"):
        normalize_ign_electricity(replace(source, electric_lines_summary=summary))


def test_high_level_rejects_summary_layer_name_mismatch() -> None:
    source = _source_bundle()
    summary = replace(source.electric_lines_summary, source_layer_name="WRONG")

    with pytest.raises(IgnGridNormalizationError, match="summary|physical"):
        normalize_ign_electricity(replace(source, electric_lines_summary=summary))


def test_high_level_rejects_wrong_logical_name() -> None:
    source = _source_bundle()
    summary = replace(
        source.electric_lines_summary,
        logical_name=cast(Any, "transformation_posts"),
    )

    with pytest.raises(IgnGridNormalizationError, match="summary|physical"):
        normalize_ign_electricity(replace(source, electric_lines_summary=summary))


def test_high_level_rejects_summary_crs_mismatch() -> None:
    source = _source_bundle()
    summary = replace(source.electric_lines_summary, crs="EPSG:4326")

    with pytest.raises(IgnGridNormalizationError, match="summary|physical|CRS|2154"):
        normalize_ign_electricity(replace(source, electric_lines_summary=summary))


@pytest.mark.parametrize("mutation", ["missing", "extra", "reordered", "dtype"])
def test_high_level_rejects_forged_ordered_summary_schema(mutation: str) -> None:
    source = _source_bundle()
    summary = source.electric_lines_summary
    if mutation == "missing":
        changed = replace(summary, columns=summary.columns[:-1])
    elif mutation == "extra":
        changed = replace(summary, columns=(*summary.columns, "invented"))
    elif mutation == "reordered":
        changed = replace(summary, columns=tuple(reversed(summary.columns)))
    else:
        dtypes = list(summary.dtypes)
        dtypes[0] = (dtypes[0][0], "object")
        changed = replace(summary, dtypes=tuple(dtypes))

    with pytest.raises(
        IgnGridNormalizationError,
        match="summary|physical|schema|columns|dtype",
    ):
        normalize_ign_electricity(replace(source, electric_lines_summary=changed))


def test_high_level_rejects_duplicate_or_missing_layer_inventory() -> None:
    source = _source_bundle()
    duplicate = replace(
        source,
        extraction=replace(
            source.extraction,
            all_layer_names=(LINE_LAYER, POST_LAYER, LINE_LAYER),
        ),
    )
    with pytest.raises(
        IgnGridNormalizationError,
        match="integrity|inventory|duplicate",
    ):
        normalize_ign_electricity(duplicate)

    missing = replace(
        source,
        extraction=replace(
            source.extraction,
            all_layer_names=(POST_LAYER,),
        ),
    )
    with pytest.raises(
        IgnGridNormalizationError,
        match="integrity|inventory|selected",
    ):
        normalize_ign_electricity(missing)


def test_high_level_rejects_colliding_electricity_roles() -> None:
    source = _source_bundle()
    extraction = replace(
        source.extraction,
        transformation_posts_layer=LINE_LAYER,
    )
    post_summary = replace(
        source.transformation_posts_summary,
        source_layer_name=LINE_LAYER,
    )

    with pytest.raises(
        IgnGridNormalizationError,
        match="integrity|same layer|distinct|role",
    ):
        normalize_ign_electricity(
            replace(
                source,
                extraction=extraction,
                transformation_posts_summary=post_summary,
            )
        )


def test_high_level_rejects_stale_geometry_counts_after_frame_mutation() -> None:
    source = _source_bundle()
    mutated = source.electric_lines.copy()
    mutated.at[mutated.index[0], "geometry"] = None

    with pytest.raises(
        IgnGridNormalizationError,
        match="freshly read physical source|geometry summary",
    ):
        normalize_ign_electricity(replace(source, electric_lines=mutated))


def test_high_level_rejects_stale_geometry_types_after_frame_mutation() -> None:
    source = _source_bundle()
    mutated = source.electric_lines.copy()
    mutated.at[mutated.index[0], "geometry"] = MultiLineString(
        [[(0, 0), (10, 10)], [(20, 20), (30, 30)]]
    )

    with pytest.raises(
        IgnGridNormalizationError,
        match="freshly read physical source|geometry summary",
    ):
        normalize_ign_electricity(replace(source, electric_lines=mutated))


@pytest.mark.parametrize(
    "component", ["source", "extraction", "archive", "line_summary", "post_summary"]
)
def test_high_level_rejects_any_spatial_role_mismatch(component: str) -> None:
    source = _source_bundle()
    wrong_role = cast(Any, "EXACT_RTE_GEOMETRY")
    if component == "source":
        inconsistent = replace(source, spatial_role=wrong_role)
    elif component == "extraction":
        inconsistent = replace(
            source, extraction=replace(source.extraction, spatial_role=wrong_role)
        )
    elif component == "archive":
        extraction = replace(
            source.extraction,
            archive=replace(source.extraction.archive, spatial_role=wrong_role),
        )
        inconsistent = replace(source, extraction=extraction)
    elif component == "line_summary":
        inconsistent = replace(
            source,
            electric_lines_summary=replace(
                source.electric_lines_summary, spatial_role=wrong_role
            ),
        )
    else:
        inconsistent = replace(
            source,
            transformation_posts_summary=replace(
                source.transformation_posts_summary, spatial_role=wrong_role
            ),
        )

    with pytest.raises(
        IgnGridNormalizationError,
        match="source-complete|role|spatial|lineage|integrity|PROXY_GEOMETRY",
    ):
        normalize_ign_electricity(inconsistent)
```

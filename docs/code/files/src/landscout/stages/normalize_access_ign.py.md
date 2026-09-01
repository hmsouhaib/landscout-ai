# `src/landscout/stages/normalize_access_ign.py`

## File identity

- Repository path: `src/landscout/stages/normalize_access_ign.py`
- File type: Python source
- Layer: pipeline stage
- Domain: factual transformation, evidence, or policy boundary
- Responsibility: Source-completely normalizes IGN road segments and raw access attributes without interpreting suitability.
- Source SHA256: `a9f84f4d65fa9c597a1069cfb36c7cd5313bf20c12fbfd30cda719d6e4eccf35`

## 1. STEP 7F.1A.4 contract delta

- Consumes the fresh config-bound road object returned by independent source-complete revalidation instead of the supplied caller object.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Source-completely normalizes IGN road segments and raw access attributes without interpreting suitability.

The file belongs to the **pipeline stage** layer and **factual transformation, evidence, or policy boundary** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `import re`
- `import unicodedata`
- `from dataclasses import dataclass`
- `from datetime import date, datetime`

### Third-party packages

- `import geopandas as gpd`
- `import pandas as pd`
- `from pydantic import HttpUrl, TypeAdapter, ValidationError`
- `from pyproj import CRS`

### Internal LandScout imports

- `from landscout.sources.ign_bdtopo_fr import (
    DepartmentCode,
    EditionString,
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    _revalidate_ign_bdtopo_road_data,
    _validate_layer_summary_contract,
)`

## 4. Contract taxonomy

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `__all__`

- Category: explicit package/module export list.
- Exact declaration:

```python
__all__ = [
    "IgnRoadNormalizationError",
    "NormalizedIgnRoadData",
    "normalize_ign_roads",
]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `IgnRoadNormalizationError`
  - `NormalizedIgnRoadData`
  - `normalize_ign_roads`

### `_SOURCE_PROVIDER`

- Category: module constant or closed domain.
- Exact declaration:

```python
_SOURCE_PROVIDER = "IGN"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_SOURCE_PRODUCT`

- Category: module constant or closed domain.
- Exact declaration:

```python
_SOURCE_PRODUCT = "BD_TOPO"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_SPATIAL_ROLE`

- Category: module constant or closed domain.
- Exact declaration:

```python
_SPATIAL_ROLE = "PROXY_GEOMETRY"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_ROAD_FEATURE_TYPE`

- Category: module constant or closed domain.
- Exact declaration:

```python
_ROAD_FEATURE_TYPE = "ROAD_SEGMENT"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_OUTPUT_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
_OUTPUT_COLUMNS = (
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

### `_RAW_FIELD_MAPPING`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
_RAW_FIELD_MAPPING = (
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

### `_REQUIRED_SOURCE_FIELDS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
_REQUIRED_SOURCE_FIELDS = frozenset(
    {"cleabs", "geometry", *(source for source, _ in _RAW_FIELD_MAPPING)}
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_ROAD_GEOMETRY_TYPES`

- Category: module constant or closed domain.
- Exact declaration:

```python
_ROAD_GEOMETRY_TYPES = frozenset({"LineString", "MultiLineString"})
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_DEPARTMENT_CODE_VALIDATOR`

- Category: module constant or closed domain.
- Exact declaration:

```python
_DEPARTMENT_CODE_VALIDATOR = TypeAdapter(DepartmentCode)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_EDITION_VALIDATOR`

- Category: module constant or closed domain.
- Exact declaration:

```python
_EDITION_VALIDATOR = TypeAdapter(EditionString)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_HTTP_URL_VALIDATOR`

- Category: module constant or closed domain.
- Exact declaration:

```python
_HTTP_URL_VALIDATOR = TypeAdapter(HttpUrl)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_SHA256_PATTERN`

- Category: module constant or closed domain.
- Exact declaration:

```python
_SHA256_PATTERN = re.compile(r"^[0-9a-f]{64}$")
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_IGN_PROVIDER_IDENTITIES`

- Category: module constant or closed domain.
- Exact declaration:

```python
_IGN_PROVIDER_IDENTITIES = frozenset(
    {
        "ign",
        "institut national de l information geographique et forestiere",
        "institut national de l information geographique et forestiere ign",
    }
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

### `IgnRoadNormalizationError`

**Source purpose:** Raised when factual IGN road data cannot be normalized safely.

- Exact decorators: none.
- Exact bases: `ValueError`.

**Fields and model attributes**

No direct class/model/dataclass or `self` field assignment is declared.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.normalize_access_ign import (
    IgnRoadNormalizationError,
    NormalizedIgnRoadData,
    normalize_ign_roads,
)`
- constructor call: `landscout.stages.normalize_access_ign::_validated_lambert93` via `IgnRoadNormalizationError`
- value/type reference: `landscout.stages.normalize_access_ign::_validated_lambert93` via `IgnRoadNormalizationError`
- constructor call: `landscout.stages.normalize_access_ign::_required_exact_string` via `IgnRoadNormalizationError`
- value/type reference: `landscout.stages.normalize_access_ign::_required_exact_string` via `IgnRoadNormalizationError`
- constructor call: `landscout.stages.normalize_access_ign::_validate_source_context` via `IgnRoadNormalizationError`
- value/type reference: `landscout.stages.normalize_access_ign::_validate_source_context` via `IgnRoadNormalizationError`
- constructor call: `landscout.stages.normalize_access_ign::_normalized_identity` via `IgnRoadNormalizationError`
- value/type reference: `landscout.stages.normalize_access_ign::_normalized_identity` via `IgnRoadNormalizationError`
- constructor call: `landscout.stages.normalize_access_ign::_validate_layer_summary` via `IgnRoadNormalizationError`
- value/type reference: `landscout.stages.normalize_access_ign::_validate_layer_summary` via `IgnRoadNormalizationError`
- constructor call: `landscout.stages.normalize_access_ign::_validate_source_bundle` via `IgnRoadNormalizationError`
- value/type reference: `landscout.stages.normalize_access_ign::_validate_source_bundle` via `IgnRoadNormalizationError`
- constructor call: `landscout.stages.normalize_access_ign::_validate_identifiers` via `IgnRoadNormalizationError`
- value/type reference: `landscout.stages.normalize_access_ign::_validate_identifiers` via `IgnRoadNormalizationError`
- constructor call: `landscout.stages.normalize_access_ign::_validate_source_frame` via `IgnRoadNormalizationError`
- value/type reference: `landscout.stages.normalize_access_ign::_validate_source_frame` via `IgnRoadNormalizationError`
- constructor call: `landscout.stages.normalize_access_ign::_normalize_road_frame` via `IgnRoadNormalizationError`
- value/type reference: `landscout.stages.normalize_access_ign::_normalize_road_frame` via `IgnRoadNormalizationError`
- constructor call: `landscout.stages.normalize_access_ign::normalize_ign_roads` via `IgnRoadNormalizationError`
- value/type reference: `landscout.stages.normalize_access_ign::normalize_ign_roads` via `IgnRoadNormalizationError`
- import: `tests.unit.test_apply_road_vehicle_proxy_policy::<module>` via `from landscout.stages.normalize_access_ign import (
    IgnRoadNormalizationError,
    NormalizedIgnRoadData,
)`
- constructor call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_normalization_failure_stops_policy_loading` via `IgnRoadNormalizationError`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_normalization_failure_stops_policy_loading` via `IgnRoadNormalizationError`
- constructor call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_valid_geometry_status_with_unsupported_geometry_is_not_repaired` via `IgnRoadNormalizationError`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_valid_geometry_status_with_unsupported_geometry_is_not_repaired` via `IgnRoadNormalizationError`
- import: `tests.unit.test_normalize_access_ign::<module>` via `from landscout.stages.normalize_access_ign import (
    IgnRoadNormalizationError,
    NormalizedIgnRoadData,
    normalize_ign_roads,
)`
- value/type reference: `tests.unit.test_normalize_access_ign::test_road_normalization_reproduces_configured_logical_layer` via `IgnRoadNormalizationError`
- value/type reference: `tests.unit.test_normalize_access_ign::test_missing_required_source_field_is_rejected` via `IgnRoadNormalizationError`
- value/type reference: `tests.unit.test_normalize_access_ign::test_null_or_empty_cleabs_is_rejected` via `IgnRoadNormalizationError`
- value/type reference: `tests.unit.test_normalize_access_ign::test_unsafe_cleabs_is_rejected` via `IgnRoadNormalizationError`
- value/type reference: `tests.unit.test_normalize_access_ign::test_duplicate_cleabs_is_rejected` via `IgnRoadNormalizationError`
- value/type reference: `tests.unit.test_normalize_access_ign::test_wrong_or_missing_road_crs_is_rejected` via `IgnRoadNormalizationError`
- value/type reference: `tests.unit.test_normalize_access_ign::test_wrong_archive_identity_is_rejected` via `IgnRoadNormalizationError`
- value/type reference: `tests.unit.test_normalize_access_ign::test_wrong_source_spatial_role_is_rejected` via `IgnRoadNormalizationError`
- value/type reference: `tests.unit.test_normalize_access_ign::test_summary_row_count_mismatch_is_rejected` via `IgnRoadNormalizationError`
- value/type reference: `tests.unit.test_normalize_access_ign::test_road_summary_requires_strict_structural_types` via `IgnRoadNormalizationError`
- value/type reference: `tests.unit.test_normalize_access_ign::test_road_archive_sha256_requires_canonical_lowercase` via `IgnRoadNormalizationError`
- value/type reference: `tests.unit.test_normalize_access_ign::test_summary_crs_mismatch_is_rejected` via `IgnRoadNormalizationError`
- value/type reference: `tests.unit.test_normalize_access_ign::test_forged_ordered_summary_schema_is_rejected` via `IgnRoadNormalizationError`
- value/type reference: `tests.unit.test_normalize_access_ign::test_road_source_rejects_physical_role_collision` via `IgnRoadNormalizationError`
- value/type reference: `tests.unit.test_normalize_access_ign::test_road_source_rejects_duplicate_layer_inventory` via `IgnRoadNormalizationError`
- value/type reference: `tests.unit.test_normalize_access_ign::test_summary_geometry_facts_mismatch_is_rejected` via `IgnRoadNormalizationError`
- value/type reference: `tests.unit.test_normalize_access_ign::test_summary_layer_must_exist_in_extraction_inventory` via `IgnRoadNormalizationError`
- value/type reference: `tests.unit.test_normalize_access_ign::test_summary_layer_and_logical_name_must_be_exact` via `IgnRoadNormalizationError`
- value/type reference: `tests.unit.test_normalize_access_ign::test_valid_unsupported_geometry_type_is_rejected` via `IgnRoadNormalizationError`
- value/type reference: `tests.unit.test_normalize_access_ign::test_high_level_rejects_coordinated_road_frame_and_summary_forgery` via `IgnRoadNormalizationError`
- value/type reference: `tests.unit.test_normalize_access_ign::test_malformed_public_input_has_controlled_error` via `IgnRoadNormalizationError`

**Exact class source**

```python
class IgnRoadNormalizationError(ValueError):
    """Raised when factual IGN road data cannot be normalized safely."""
```

### `_IgnRoadSourceContext`

**Source purpose:** Defines `_IgnRoadSourceContext`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `source_layer` | `str` | `required` | `source_layer: str` |
| `department_code` | `str` | `required` | `department_code: str` |
| `edition` | `str` | `required` | `edition: str` |
| `product_version` | `str \| None` | `required` | `product_version: str \| None` |
| `download_timestamp` | `str` | `required` | `download_timestamp: str` |
| `archive_sha256` | `str` | `required` | `archive_sha256: str` |
| `source_url` | `str` | `required` | `source_url: str` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- value/type reference: `landscout.stages.normalize_access_ign::_validate_source_context` via `_IgnRoadSourceContext`
- constructor call: `landscout.stages.normalize_access_ign::_validate_source_bundle` via `_IgnRoadSourceContext`
- value/type reference: `landscout.stages.normalize_access_ign::_validate_source_bundle` via `_IgnRoadSourceContext`
- value/type reference: `landscout.stages.normalize_access_ign::_normalize_road_frame` via `_IgnRoadSourceContext`

**Exact class source**

```python
class _IgnRoadSourceContext:
    source_layer: str
    department_code: str
    edition: str
    product_version: str | None
    download_timestamp: str
    archive_sha256: str
    source_url: str
```

### `NormalizedIgnRoadData`

**Source purpose:** Stable factual IGN road catalog with no access-policy interpretation.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `road_segments` | `gpd.GeoDataFrame` | `required` | `road_segments: gpd.GeoDataFrame` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.normalize_access_ign import (
    IgnRoadNormalizationError,
    NormalizedIgnRoadData,
    normalize_ign_roads,
)`
- import: `landscout.stages.apply_road_vehicle_proxy_policy::<module>` via `from landscout.stages.normalize_access_ign import (
    NormalizedIgnRoadData,
    normalize_ign_roads,
)`
- value/type reference: `landscout.stages.apply_road_vehicle_proxy_policy::_apply_ign_road_vehicle_proxy_policy` via `NormalizedIgnRoadData`
- constructor call: `landscout.stages.normalize_access_ign::_normalize_ign_roads` via `NormalizedIgnRoadData`
- value/type reference: `landscout.stages.normalize_access_ign::_normalize_ign_roads` via `NormalizedIgnRoadData`
- value/type reference: `landscout.stages.normalize_access_ign::normalize_ign_roads` via `NormalizedIgnRoadData`
- import: `tests.unit.test_apply_road_vehicle_proxy_policy::<module>` via `from landscout.stages.normalize_access_ign import (
    IgnRoadNormalizationError,
    NormalizedIgnRoadData,
)`
- constructor call: `tests.unit.test_apply_road_vehicle_proxy_policy::_apply` via `NormalizedIgnRoadData`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::_apply` via `NormalizedIgnRoadData`
- constructor call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_malformed_policy_path_has_controlled_error` via `NormalizedIgnRoadData`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_malformed_policy_path_has_controlled_error` via `NormalizedIgnRoadData`
- constructor call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_source_complete_normalization_is_invoked_exactly_once` via `NormalizedIgnRoadData`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_source_complete_normalization_is_invoked_exactly_once` via `NormalizedIgnRoadData`
- constructor call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_generated_policy_column_collision_fails_before_policy_loading` via `NormalizedIgnRoadData`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_generated_policy_column_collision_fails_before_policy_loading` via `NormalizedIgnRoadData`
- constructor call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_source_object_is_not_mutated` via `NormalizedIgnRoadData`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_source_object_is_not_mutated` via `NormalizedIgnRoadData`
- import: `tests.unit.test_normalize_access_ign::<module>` via `from landscout.stages.normalize_access_ign import (
    IgnRoadNormalizationError,
    NormalizedIgnRoadData,
    normalize_ign_roads,
)`
- value/type reference: `tests.unit.test_normalize_access_ign::test_valid_linestring_normalization_has_exact_schema_identity_and_lineage` via `NormalizedIgnRoadData`

**Exact class source**

```python
class NormalizedIgnRoadData:
    """Stable factual IGN road catalog with no access-policy interpretation."""

    road_segments: gpd.GeoDataFrame
```


## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `_validated_lambert93`

**Purpose:** Implements `validated lambert93` within the file role: Source-completely normalizes IGN road segments and raw access attributes without interpreting suitability.

**Exact signature**

```python
def _validated_lambert93(crs_value: object, label: str) -> CRS:
```

- Exact decorators: none.
- Declared return annotation: `CRS`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `crs_value` | positional-or-keyword | `object` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `source_crs`
- Explicit raise paths:
  - `IgnRoadNormalizationError(f"{label} CRS is required")` under lexical guard `crs_value is None`.
  - `IgnRoadNormalizationError(f"{label} CRS is unreadable")`.
  - `IgnRoadNormalizationError(f"{label} must use EPSG:2154")` under lexical guard `not source_crs.is_projected or not source_crs.equals(expected_crs)`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.normalize_access_ign::_validate_layer_summary` via `_validated_lambert93`
- value/type reference: `landscout.stages.normalize_access_ign::_validate_layer_summary` via `_validated_lambert93`
- direct call: `landscout.stages.normalize_access_ign::_validate_source_bundle` via `_validated_lambert93`
- value/type reference: `landscout.stages.normalize_access_ign::_validate_source_bundle` via `_validated_lambert93`
- direct call: `landscout.stages.normalize_access_ign::_validate_source_frame` via `_validated_lambert93`
- value/type reference: `landscout.stages.normalize_access_ign::_validate_source_frame` via `_validated_lambert93`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `IgnRoadNormalizationError` | `landscout.stages.normalize_access_ign.IgnRoadNormalizationError` |
| `CRS.from_user_input` | `pyproj.CRS.from_user_input` |
| `CRS.from_epsg` | `pyproj.CRS.from_epsg` |
| `source_crs.equals` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _validated_lambert93(crs_value: object, label: str) -> CRS:
    if crs_value is None:
        raise IgnRoadNormalizationError(f"{label} CRS is required")
    try:
        source_crs = CRS.from_user_input(crs_value)
    except Exception as error:
        raise IgnRoadNormalizationError(f"{label} CRS is unreadable") from error
    expected_crs = CRS.from_epsg(2154)
    if not source_crs.is_projected or not source_crs.equals(expected_crs):
        raise IgnRoadNormalizationError(f"{label} must use EPSG:2154")
    return source_crs
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_required_exact_string`

**Purpose:** Implements `required exact string` within the file role: Source-completely normalizes IGN road segments and raw access attributes without interpreting suitability.

**Exact signature**

```python
def _required_exact_string(value: object, label: str) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `value`
- Explicit raise paths:
  - `IgnRoadNormalizationError(f"IGN road {label} must be a string")` under lexical guard `not isinstance(value, str) or not value.strip()`.
  - `IgnRoadNormalizationError(<br>            f"IGN road {label} must not contain edge whitespace"<br>        )` under lexical guard `value != value.strip()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.normalize_access_ign::_validate_source_context` via `_required_exact_string`
- value/type reference: `landscout.stages.normalize_access_ign::_validate_source_context` via `_required_exact_string`
- direct call: `landscout.stages.normalize_access_ign::_validate_layer_summary` via `_required_exact_string`
- value/type reference: `landscout.stages.normalize_access_ign::_validate_layer_summary` via `_required_exact_string`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `value.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnRoadNormalizationError` | `landscout.stages.normalize_access_ign.IgnRoadNormalizationError` |

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
def _required_exact_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise IgnRoadNormalizationError(f"IGN road {label} must be a string")
    if value != value.strip():
        raise IgnRoadNormalizationError(
            f"IGN road {label} must not contain edge whitespace"
        )
    return value
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_source_context`

**Purpose:** Implements `validate source context` within the file role: Source-completely normalizes IGN road segments and raw access attributes without interpreting suitability.

**Exact signature**

```python
def _validate_source_context(context: _IgnRoadSourceContext) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `context` | positional-or-keyword | `_IgnRoadSourceContext` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `IgnRoadNormalizationError(<br>            "IGN road department_code is invalid"<br>        )`.
  - `IgnRoadNormalizationError(<br>            "IGN road department_code must not be rewritten"<br>        )` under lexical guard `validated_department != department_code`.
  - `IgnRoadNormalizationError(<br>            "IGN road edition must be a valid ISO calendar date"<br>        )`.
  - `IgnRoadNormalizationError("IGN road edition must not be rewritten")` under lexical guard `validated_edition != edition`.
  - `IgnRoadNormalizationError(<br>            "IGN road download_timestamp must be a valid ISO datetime"<br>        )`.
  - `IgnRoadNormalizationError(<br>            "IGN road download_timestamp must be timezone-aware"<br>        )` under lexical guard `timestamp.tzinfo is None or timestamp.utcoffset() is None`.
  - `IgnRoadNormalizationError(<br>            "IGN road archive_sha256 must contain 64 hexadecimal characters"<br>        )` under lexical guard `_SHA256_PATTERN.fullmatch(archive_sha256) is None`.
  - `IgnRoadNormalizationError(<br>            "IGN road source_url must be a valid HTTP(S) URL"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.normalize_access_ign::_normalize_road_frame` via `_validate_source_context`
- value/type reference: `landscout.stages.normalize_access_ign::_normalize_road_frame` via `_validate_source_context`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_required_exact_string` | `landscout.stages.normalize_access_ign._required_exact_string` |
| `_DEPARTMENT_CODE_VALIDATOR.validate_python` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnRoadNormalizationError` | `landscout.stages.normalize_access_ign.IgnRoadNormalizationError` |
| `_EDITION_VALIDATOR.validate_python` | `unresolved local/third-party receiver; no ownership inferred` |
| `date.fromisoformat` | `datetime.date.fromisoformat` |
| `datetime.fromisoformat` | `datetime.datetime.fromisoformat` |
| `timestamp.utcoffset` | `unresolved local/third-party receiver; no ownership inferred` |
| `_SHA256_PATTERN.fullmatch` | `unresolved local/third-party receiver; no ownership inferred` |
| `_HTTP_URL_VALIDATOR.validate_python` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_SHA256_PATTERN.fullmatch` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _validate_source_context(context: _IgnRoadSourceContext) -> None:
    _required_exact_string(context.source_layer, "source_layer")
    department_code = _required_exact_string(context.department_code, "department_code")
    edition = _required_exact_string(context.edition, "edition")
    timestamp_raw = _required_exact_string(
        context.download_timestamp, "download_timestamp"
    )
    archive_sha256 = _required_exact_string(context.archive_sha256, "archive_sha256")
    source_url = _required_exact_string(context.source_url, "source_url")

    try:
        validated_department = _DEPARTMENT_CODE_VALIDATOR.validate_python(
            department_code
        )
    except ValidationError as error:
        raise IgnRoadNormalizationError(
            "IGN road department_code is invalid"
        ) from error
    if validated_department != department_code:
        raise IgnRoadNormalizationError(
            "IGN road department_code must not be rewritten"
        )

    try:
        validated_edition = _EDITION_VALIDATOR.validate_python(edition)
        date.fromisoformat(validated_edition)
    except (ValidationError, ValueError) as error:
        raise IgnRoadNormalizationError(
            "IGN road edition must be a valid ISO calendar date"
        ) from error
    if validated_edition != edition:
        raise IgnRoadNormalizationError("IGN road edition must not be rewritten")

    try:
        timestamp = datetime.fromisoformat(timestamp_raw)
    except ValueError as error:
        raise IgnRoadNormalizationError(
            "IGN road download_timestamp must be a valid ISO datetime"
        ) from error
    if timestamp.tzinfo is None or timestamp.utcoffset() is None:
        raise IgnRoadNormalizationError(
            "IGN road download_timestamp must be timezone-aware"
        )

    if _SHA256_PATTERN.fullmatch(archive_sha256) is None:
        raise IgnRoadNormalizationError(
            "IGN road archive_sha256 must contain 64 hexadecimal characters"
        )
    try:
        _HTTP_URL_VALIDATOR.validate_python(source_url)
    except ValidationError as error:
        raise IgnRoadNormalizationError(
            "IGN road source_url must be a valid HTTP(S) URL"
        ) from error

    if context.product_version is not None:
        _required_exact_string(context.product_version, "product_version")
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_normalized_identity`

**Purpose:** Implements `normalized identity` within the file role: Source-completely normalizes IGN road segments and raw access attributes without interpreting suitability.

**Exact signature**

```python
def _normalized_identity(value: object, label: str) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `" ".join(re.findall(r"[a-z0-9]+", without_accents))`
- Explicit raise paths:
  - `IgnRoadNormalizationError(f"IGN archive {label} must be a string")` under lexical guard `not isinstance(value, str) or not value.strip()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.normalize_access_ign::_validate_source_bundle` via `_normalized_identity`
- value/type reference: `landscout.stages.normalize_access_ign::_validate_source_bundle` via `_normalized_identity`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `value.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnRoadNormalizationError` | `landscout.stages.normalize_access_ign.IgnRoadNormalizationError` |
| `unicodedata.normalize` | `unicodedata.normalize` |
| `value.casefold` | `unresolved local/third-party receiver; no ownership inferred` |
| `"".join` | `unresolved local/third-party receiver; no ownership inferred` |
| `unicodedata.combining` | `unicodedata.combining` |
| `" ".join` | `unresolved local/third-party receiver; no ownership inferred` |
| `re.findall` | `re.findall` |

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
def _normalized_identity(value: object, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise IgnRoadNormalizationError(f"IGN archive {label} must be a string")
    decomposed = unicodedata.normalize("NFKD", value.casefold())
    without_accents = "".join(
        character for character in decomposed if not unicodedata.combining(character)
    )
    return " ".join(re.findall(r"[a-z0-9]+", without_accents))
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_geometry_summary`

**Purpose:** Implements `geometry summary` within the file role: Source-completely normalizes IGN road segments and raw access attributes without interpreting suitability.

**Exact signature**

```python
def _geometry_summary(
    frame: gpd.GeoDataFrame,
) -> tuple[int, int, int, tuple[str, ...]]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[int, int, int, tuple[str, ...]]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `(<br>        int(null_mask.sum()),<br>        int(empty_mask.sum()),<br>        int(invalid_mask.sum()),<br>        geometry_types,<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.normalize_access_ign::_validate_layer_summary` via `_geometry_summary`
- value/type reference: `landscout.stages.normalize_access_ign::_validate_layer_summary` via `_geometry_summary`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `geometry.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry[~null_mask].geom_type.dropna().unique` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry[~null_mask].geom_type.dropna` | `unresolved local/third-party receiver; no ownership inferred` |
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
def _geometry_summary(
    frame: gpd.GeoDataFrame,
) -> tuple[int, int, int, tuple[str, ...]]:
    geometry = frame.geometry
    null_mask = geometry.isna()
    empty_mask = ~null_mask & geometry.is_empty
    invalid_mask = ~null_mask & ~geometry.is_empty & ~geometry.is_valid
    geometry_types = tuple(
        sorted(str(value) for value in geometry[~null_mask].geom_type.dropna().unique())
    )
    return (
        int(null_mask.sum()),
        int(empty_mask.sum()),
        int(invalid_mask.sum()),
        geometry_types,
    )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_layer_summary`

**Purpose:** Implements `validate layer summary` within the file role: Source-completely normalizes IGN road segments and raw access attributes without interpreting suitability.

**Exact signature**

```python
def _validate_layer_summary(
    frame: gpd.GeoDataFrame,
    summary: IgnBdTopoLayerSummary,
    all_layer_names: tuple[str, ...],
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `summary` | positional-or-keyword | `IgnBdTopoLayerSummary` | `required` |
| `all_layer_names` | positional-or-keyword | `tuple[str, ...]` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `IgnRoadNormalizationError(<br>            "IGN road summary schema contract is invalid"<br>        )`.
  - `IgnRoadNormalizationError("IGN road summary has the wrong logical name")` under lexical guard `summary.logical_name != "road_segments"`.
  - `IgnRoadNormalizationError(<br>            "IGN road summary physical layer is absent from the extraction layer inventory"<br>        )` under lexical guard `source_layer not in all_layer_names`.
  - `IgnRoadNormalizationError(<br>            "IGN road summary row count does not match the source frame"<br>        )` under lexical guard `summary.feature_count != len(frame)`.
  - `IgnRoadNormalizationError(<br>            "IGN road summary schema columns or dtypes do not match the source frame"<br>        )` under lexical guard `summary.columns != observed_columns or summary.dtypes != observed_dtypes`.
  - `IgnRoadNormalizationError(<br>            "IGN road source requires an active geometry column"<br>        )` under lexical guard `frame.active_geometry_name != "geometry"`.
  - `IgnRoadNormalizationError(<br>            "IGN road summary CRS does not match the source frame"<br>        )` under lexical guard `not frame_crs.equals(summary_crs)`.
  - `IgnRoadNormalizationError(<br>            "IGN road geometry summary does not match the source frame"<br>        )` under lexical guard `_geometry_summary(frame) != expected_geometry`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.normalize_access_ign::_validate_source_bundle` via `_validate_layer_summary`
- value/type reference: `landscout.stages.normalize_access_ign::_validate_source_bundle` via `_validate_layer_summary`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validate_layer_summary_contract` | `landscout.sources.ign_bdtopo_fr._validate_layer_summary_contract` |
| `IgnRoadNormalizationError` | `landscout.stages.normalize_access_ign.IgnRoadNormalizationError` |
| `_required_exact_string` | `landscout.stages.normalize_access_ign._required_exact_string` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.dtypes.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validated_lambert93` | `landscout.stages.normalize_access_ign._validated_lambert93` |
| `frame_crs.equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `_geometry_summary` | `landscout.stages.normalize_access_ign._geometry_summary` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `_geometry_summary` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _validate_layer_summary(
    frame: gpd.GeoDataFrame,
    summary: IgnBdTopoLayerSummary,
    all_layer_names: tuple[str, ...],
) -> None:
    try:
        _validate_layer_summary_contract(summary)
    except Exception as error:
        raise IgnRoadNormalizationError(
            "IGN road summary schema contract is invalid"
        ) from error
    if summary.logical_name != "road_segments":
        raise IgnRoadNormalizationError("IGN road summary has the wrong logical name")
    source_layer = _required_exact_string(
        summary.source_layer_name, "summary physical layer"
    )
    if source_layer not in all_layer_names:
        raise IgnRoadNormalizationError(
            "IGN road summary physical layer is absent from the extraction layer inventory"
        )
    if summary.feature_count != len(frame):
        raise IgnRoadNormalizationError(
            "IGN road summary row count does not match the source frame"
        )
    observed_columns = tuple(str(column) for column in frame.columns)
    observed_dtypes = tuple(
        (str(column), str(dtype)) for column, dtype in frame.dtypes.items()
    )
    if summary.columns != observed_columns or summary.dtypes != observed_dtypes:
        raise IgnRoadNormalizationError(
            "IGN road summary schema columns or dtypes do not match the source frame"
        )
    if frame.active_geometry_name != "geometry":
        raise IgnRoadNormalizationError(
            "IGN road source requires an active geometry column"
        )
    frame_crs = _validated_lambert93(frame.crs, "IGN road source")
    summary_crs = _validated_lambert93(summary.crs, "IGN road summary")
    if not frame_crs.equals(summary_crs):
        raise IgnRoadNormalizationError(
            "IGN road summary CRS does not match the source frame"
        )
    expected_geometry = (
        summary.null_geometry_count,
        summary.empty_geometry_count,
        summary.invalid_geometry_count,
        summary.geometry_types,
    )
    if _geometry_summary(frame) != expected_geometry:
        raise IgnRoadNormalizationError(
            "IGN road geometry summary does not match the source frame"
        )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_source_bundle`

**Purpose:** Implements `validate source bundle` within the file role: Source-completely normalizes IGN road segments and raw access attributes without interpreting suitability.

**Exact signature**

```python
def _validate_source_bundle(source: IgnBdTopoRoadData) -> _IgnRoadSourceContext:
```

- Exact decorators: none.
- Declared return annotation: `_IgnRoadSourceContext`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source` | positional-or-keyword | `IgnBdTopoRoadData` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_IgnRoadSourceContext(<br>        source_layer=source.road_segments_summary.source_layer_name,<br>        department_code=archive.department_code,<br>        edition=archive.edition,<br>        product_version=archive.product_version,<br>        download_timestamp=archive.download_timestamp,<br>        archive_sha256=archive.sha256,<br>        source_url=archive.source_url,<br>    )`
- Explicit raise paths:
  - `IgnRoadNormalizationError("IGN road extraction type is invalid")` under lexical guard `type(source.extraction) is not IgnBdTopoExtraction`.
  - `IgnRoadNormalizationError("IGN road archive type is invalid")` under lexical guard `type(source.extraction.archive) is not IgnBdTopoDownload`.
  - `IgnRoadNormalizationError("IGN road summary type is invalid")` under lexical guard `type(source.road_segments_summary) is not IgnBdTopoLayerSummary`.
  - `IgnRoadNormalizationError(<br>            "IGN archive provider is incompatible with the IGN road normalizer"<br>        )` under lexical guard `provider not in _IGN_PROVIDER_IDENTITIES`.
  - `IgnRoadNormalizationError(<br>            "IGN archive product is incompatible with the BD TOPO road normalizer"<br>        )` under lexical guard `product.replace(" ", "") != "bdtopo"`.
  - `IgnRoadNormalizationError(<br>            "IGN road source spatial roles must all be PROXY_GEOMETRY"<br>        )` under lexical guard `any(role != _SPATIAL_ROLE for role in roles)`.
  - `IgnRoadNormalizationError(<br>            "IGN road layer inventory must be a unique non-empty tuple"<br>        )` under lexical guard `type(layer_names) is not tuple<br>        or not layer_names<br>        or any(<br>            not isinstance(name, str) or not name or name != name.strip()<br>            for name in layer_names<br>        )<br>        or len(set(layer_names)) != len(layer_names)`.
  - `IgnRoadNormalizationError(<br>            "IGN road extraction selected layer is absent from the layer inventory"<br>        )` under lexical guard `any(layer not in layer_names for layer in selected_layers)`.
  - `IgnRoadNormalizationError(<br>            "IGN electricity roles must use distinct layers, not the same layer"<br>        )` under lexical guard `selected_layers[0] == selected_layers[1]`.
  - `IgnRoadNormalizationError(<br>            "IGN road and electricity roles must use distinct layers, not the same layer"<br>        )` under lexical guard `road_layer in selected_layers`.
  - `IgnRoadNormalizationError(<br>            "IGN road_segments must be a GeoDataFrame with an active geometry column"<br>        )` under lexical guard `not isinstance(source.road_segments, gpd.GeoDataFrame)`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.normalize_access_ign::_normalize_ign_roads` via `_validate_source_bundle`
- value/type reference: `landscout.stages.normalize_access_ign::_normalize_ign_roads` via `_validate_source_bundle`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnRoadNormalizationError` | `landscout.stages.normalize_access_ign.IgnRoadNormalizationError` |
| `_normalized_identity` | `landscout.stages.normalize_access_ign._normalized_identity` |
| `product.replace` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validated_lambert93` | `landscout.stages.normalize_access_ign._validated_lambert93` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `name.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validate_source_frame` | `landscout.stages.normalize_access_ign._validate_source_frame` |
| `_validate_layer_summary` | `landscout.stages.normalize_access_ign._validate_layer_summary` |
| `_IgnRoadSourceContext` | `landscout.stages.normalize_access_ign._IgnRoadSourceContext` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `product.replace` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _validate_source_bundle(source: IgnBdTopoRoadData) -> _IgnRoadSourceContext:
    if type(source.extraction) is not IgnBdTopoExtraction:
        raise IgnRoadNormalizationError("IGN road extraction type is invalid")
    if type(source.extraction.archive) is not IgnBdTopoDownload:
        raise IgnRoadNormalizationError("IGN road archive type is invalid")
    if type(source.road_segments_summary) is not IgnBdTopoLayerSummary:
        raise IgnRoadNormalizationError("IGN road summary type is invalid")
    archive = source.extraction.archive
    provider = _normalized_identity(archive.provider, "provider")
    product = _normalized_identity(archive.product, "product")
    if provider not in _IGN_PROVIDER_IDENTITIES:
        raise IgnRoadNormalizationError(
            "IGN archive provider is incompatible with the IGN road normalizer"
        )
    if product.replace(" ", "") != "bdtopo":
        raise IgnRoadNormalizationError(
            "IGN archive product is incompatible with the BD TOPO road normalizer"
        )
    _validated_lambert93(archive.projection, "IGN archive projection")
    roles = (
        archive.spatial_role,
        source.extraction.spatial_role,
        source.road_segments_summary.spatial_role,
    )
    if any(role != _SPATIAL_ROLE for role in roles):
        raise IgnRoadNormalizationError(
            "IGN road source spatial roles must all be PROXY_GEOMETRY"
        )
    layer_names = source.extraction.all_layer_names
    if (
        type(layer_names) is not tuple
        or not layer_names
        or any(
            not isinstance(name, str) or not name or name != name.strip()
            for name in layer_names
        )
        or len(set(layer_names)) != len(layer_names)
    ):
        raise IgnRoadNormalizationError(
            "IGN road layer inventory must be a unique non-empty tuple"
        )
    selected_layers = (
        source.extraction.electric_lines_layer,
        source.extraction.transformation_posts_layer,
    )
    if any(layer not in layer_names for layer in selected_layers):
        raise IgnRoadNormalizationError(
            "IGN road extraction selected layer is absent from the layer inventory"
        )
    if selected_layers[0] == selected_layers[1]:
        raise IgnRoadNormalizationError(
            "IGN electricity roles must use distinct layers, not the same layer"
        )
    road_layer = source.road_segments_summary.source_layer_name
    if road_layer in selected_layers:
        raise IgnRoadNormalizationError(
            "IGN road and electricity roles must use distinct layers, not the same layer"
        )
    if not isinstance(source.road_segments, gpd.GeoDataFrame):
        raise IgnRoadNormalizationError(
            "IGN road_segments must be a GeoDataFrame with an active geometry column"
        )
    _validate_source_frame(source.road_segments)
    _validate_layer_summary(
        source.road_segments,
        source.road_segments_summary,
        source.extraction.all_layer_names,
    )
    return _IgnRoadSourceContext(
        source_layer=source.road_segments_summary.source_layer_name,
        department_code=archive.department_code,
        edition=archive.edition,
        product_version=archive.product_version,
        download_timestamp=archive.download_timestamp,
        archive_sha256=archive.sha256,
        source_url=archive.source_url,
    )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_identifiers`

**Purpose:** Implements `validate identifiers` within the file role: Source-completely normalizes IGN road segments and raw access attributes without interpreting suitability.

**Exact signature**

```python
def _validate_identifiers(frame: gpd.GeoDataFrame) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `IgnRoadNormalizationError("IGN road cleabs values must not be null")` under lexical guard `identifiers.isna().any()`.
  - `IgnRoadNormalizationError("IGN road cleabs values must be strings")` under lexical guard `any(not isinstance(identifier, str) for identifier in values)`.
  - `IgnRoadNormalizationError("IGN road cleabs values must not be empty")` under lexical guard `any(not identifier.strip() for identifier in values)`.
  - `IgnRoadNormalizationError(<br>            "IGN road cleabs values must not contain edge whitespace"<br>        )` under lexical guard `any(identifier != identifier.strip() for identifier in values)`.
  - `IgnRoadNormalizationError("IGN road cleabs values must not contain ':'")` under lexical guard `any(":" in identifier for identifier in values)`.
  - `IgnRoadNormalizationError(<br>            "IGN road cleabs values must not contain control characters"<br>        )` under lexical guard `any(<br>        unicodedata.category(character) == "Cc"<br>        for identifier in values<br>        for character in identifier<br>    )`.
  - `IgnRoadNormalizationError("IGN road cleabs values must be unique")` under lexical guard `identifiers.duplicated().any()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.normalize_access_ign::_validate_source_frame` via `_validate_identifiers`
- value/type reference: `landscout.stages.normalize_access_ign::_validate_source_frame` via `_validate_identifiers`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `identifiers.isna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `identifiers.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnRoadNormalizationError` | `landscout.stages.normalize_access_ign.IgnRoadNormalizationError` |
| `identifiers.tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `identifier.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `unicodedata.category` | `unicodedata.category` |
| `identifiers.duplicated().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `identifiers.duplicated` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _validate_identifiers(frame: gpd.GeoDataFrame) -> None:
    identifiers = frame["cleabs"]
    if identifiers.isna().any():
        raise IgnRoadNormalizationError("IGN road cleabs values must not be null")
    values = identifiers.tolist()
    if any(not isinstance(identifier, str) for identifier in values):
        raise IgnRoadNormalizationError("IGN road cleabs values must be strings")
    if any(not identifier.strip() for identifier in values):
        raise IgnRoadNormalizationError("IGN road cleabs values must not be empty")
    if any(identifier != identifier.strip() for identifier in values):
        raise IgnRoadNormalizationError(
            "IGN road cleabs values must not contain edge whitespace"
        )
    if any(":" in identifier for identifier in values):
        raise IgnRoadNormalizationError("IGN road cleabs values must not contain ':'")
    if any(
        unicodedata.category(character) == "Cc"
        for identifier in values
        for character in identifier
    ):
        raise IgnRoadNormalizationError(
            "IGN road cleabs values must not contain control characters"
        )
    if identifiers.duplicated().any():
        raise IgnRoadNormalizationError("IGN road cleabs values must be unique")
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_source_frame`

**Purpose:** Implements `validate source frame` within the file role: Source-completely normalizes IGN road segments and raw access attributes without interpreting suitability.

**Exact signature**

```python
def _validate_source_frame(frame: gpd.GeoDataFrame) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `IgnRoadNormalizationError(<br>            "IGN road source columns must not contain duplicates"<br>        )` under lexical guard `frame.columns.duplicated().any()`.
  - `IgnRoadNormalizationError(<br>            f"Missing required IGN road source columns: {formatted}"<br>        )` under lexical guard `missing`.
  - `IgnRoadNormalizationError(<br>            "IGN road source requires an active geometry column"<br>        )` under lexical guard `frame.active_geometry_name != "geometry"`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.normalize_access_ign::_validate_source_bundle` via `_validate_source_frame`
- value/type reference: `landscout.stages.normalize_access_ign::_validate_source_bundle` via `_validate_source_frame`
- direct call: `landscout.stages.normalize_access_ign::_normalize_road_frame` via `_validate_source_frame`
- value/type reference: `landscout.stages.normalize_access_ign::_normalize_road_frame` via `_validate_source_frame`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `frame.columns.duplicated().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.columns.duplicated` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnRoadNormalizationError` | `landscout.stages.normalize_access_ign.IgnRoadNormalizationError` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `", ".join` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validated_lambert93` | `landscout.stages.normalize_access_ign._validated_lambert93` |
| `_validate_identifiers` | `landscout.stages.normalize_access_ign._validate_identifiers` |

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
def _validate_source_frame(frame: gpd.GeoDataFrame) -> None:
    if frame.columns.duplicated().any():
        raise IgnRoadNormalizationError(
            "IGN road source columns must not contain duplicates"
        )
    missing = _REQUIRED_SOURCE_FIELDS - set(frame.columns)
    if missing:
        formatted = ", ".join(sorted(missing))
        raise IgnRoadNormalizationError(
            f"Missing required IGN road source columns: {formatted}"
        )
    if frame.active_geometry_name != "geometry":
        raise IgnRoadNormalizationError(
            "IGN road source requires an active geometry column"
        )
    _validated_lambert93(frame.crs, "IGN road source")
    _validate_identifiers(frame)
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_geometry_status`

**Purpose:** Implements `geometry status` within the file role: Source-completely normalizes IGN road segments and raw access attributes without interpreting suitability.

**Exact signature**

```python
def _geometry_status(geometry: gpd.GeoSeries) -> pd.Series:
```

- Exact decorators: none.
- Declared return annotation: `pd.Series`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `geometry` | positional-or-keyword | `gpd.GeoSeries` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `status`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.normalize_access_ign::_normalize_road_frame` via `_geometry_status`
- value/type reference: `landscout.stages.normalize_access_ign::_normalize_road_frame` via `_geometry_status`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pd.Series` | `pandas.Series` |
| `geometry.isna` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `geometry.isna` |
| External process/environment | None directly present. |
| In-memory mutation | `status.loc[null_mask] = "NULL"`<br>`status.loc[empty_mask] = "EMPTY"`<br>`status.loc[invalid_mask] = "INVALID"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _geometry_status(geometry: gpd.GeoSeries) -> pd.Series:
    status = pd.Series("VALID", index=geometry.index, dtype="object")
    null_mask = geometry.isna()
    empty_mask = ~null_mask & geometry.is_empty
    invalid_mask = ~null_mask & ~geometry.is_empty & ~geometry.is_valid
    status.loc[null_mask] = "NULL"
    status.loc[empty_mask] = "EMPTY"
    status.loc[invalid_mask] = "INVALID"
    return status
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_normalize_road_frame`

**Purpose:** Implements `normalize road frame` within the file role: Source-completely normalizes IGN road segments and raw access attributes without interpreting suitability.

**Exact signature**

```python
def _normalize_road_frame(
    frame: gpd.GeoDataFrame,
    context: _IgnRoadSourceContext,
) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `context` | positional-or-keyword | `_IgnRoadSourceContext` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `normalized`
- Explicit raise paths:
  - `IgnRoadNormalizationError(<br>            "IGN road source has unsupported VALID geometry types: "<br>            + ", ".join(unsupported)<br>        )` under lexical guard `unsupported`.
  - `IgnRoadNormalizationError("IGN road normalization changed the row count")` under lexical guard `len(normalized) != len(frame)`.
  - `IgnRoadNormalizationError(<br>            "IGN normalized road output must use a RangeIndex"<br>        )` under lexical guard `not isinstance(normalized.index, pd.RangeIndex)`.
  - `IgnRoadNormalizationError(<br>            "Normalized IGN road_feature_id values must be non-null and unique"<br>        )` under lexical guard `normalized["road_feature_id"].isna().any()<br>        or normalized["road_feature_id"].duplicated().any()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.normalize_access_ign::_normalize_ign_roads` via `_normalize_road_frame`
- value/type reference: `landscout.stages.normalize_access_ign::_normalize_ign_roads` via `_normalize_road_frame`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validate_source_context` | `landscout.stages.normalize_access_ign._validate_source_context` |
| `_validate_source_frame` | `landscout.stages.normalize_access_ign._validate_source_frame` |
| `frame.reset_index(drop=True).copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.reset_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `_geometry_status` | `landscout.stages.normalize_access_ign._geometry_status` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `valid_types.dropna` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnRoadNormalizationError` | `landscout.stages.normalize_access_ign.IgnRoadNormalizationError` |
| `", ".join` | `unresolved local/third-party receiver; no ownership inferred` |
| `working["cleabs"].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `working.index.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `source_ids.map` | `unresolved local/third-party receiver; no ownership inferred` |
| `working[source_column].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `working.geometry.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `normalized["road_feature_id"].isna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `normalized["road_feature_id"].isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `normalized["road_feature_id"].duplicated().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `normalized["road_feature_id"].duplicated` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `_geometry_status`<br>`working.geometry.copy` |
| External process/environment | None directly present. |
| In-memory mutation | `output["road_feature_id"] = source_ids.map(<br>        lambda identifier: f"IGN_BDTOPO:{_ROAD_FEATURE_TYPE}:{identifier}"<br>    )`<br>`output["road_feature_type"] = _ROAD_FEATURE_TYPE`<br>`output["source_provider"] = _SOURCE_PROVIDER`<br>`output["source_product"] = _SOURCE_PRODUCT`<br>`output["source_layer"] = context.source_layer`<br>`output["source_feature_id"] = source_ids`<br>`output["source_department_code"] = context.department_code`<br>`output["source_edition"] = context.edition`<br>`output["source_product_version"] = context.product_version`<br>`output["source_download_timestamp"] = context.download_timestamp`<br>`output["source_archive_sha256"] = context.archive_sha256`<br>`output["source_url"] = context.source_url`<br>`output[output_column] = working[source_column].copy()`<br>`output["spatial_role"] = _SPATIAL_ROLE`<br>`output["geometry_status"] = status`<br>`output["geometry"] = working.geometry.copy()` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _normalize_road_frame(
    frame: gpd.GeoDataFrame,
    context: _IgnRoadSourceContext,
) -> gpd.GeoDataFrame:
    _validate_source_context(context)
    _validate_source_frame(frame)
    working = frame.reset_index(drop=True).copy()
    status = _geometry_status(working.geometry)
    valid_types = working.loc[status == "VALID", "geometry"].geom_type
    unsupported = sorted(set(valid_types.dropna()) - _ROAD_GEOMETRY_TYPES)
    if unsupported:
        raise IgnRoadNormalizationError(
            "IGN road source has unsupported VALID geometry types: "
            + ", ".join(unsupported)
        )

    source_ids = working["cleabs"].copy()
    output = pd.DataFrame(index=working.index.copy())
    output["road_feature_id"] = source_ids.map(
        lambda identifier: f"IGN_BDTOPO:{_ROAD_FEATURE_TYPE}:{identifier}"
    )
    output["road_feature_type"] = _ROAD_FEATURE_TYPE
    output["source_provider"] = _SOURCE_PROVIDER
    output["source_product"] = _SOURCE_PRODUCT
    output["source_layer"] = context.source_layer
    output["source_feature_id"] = source_ids
    output["source_department_code"] = context.department_code
    output["source_edition"] = context.edition
    output["source_product_version"] = context.product_version
    output["source_download_timestamp"] = context.download_timestamp
    output["source_archive_sha256"] = context.archive_sha256
    output["source_url"] = context.source_url
    for source_column, output_column in _RAW_FIELD_MAPPING:
        output[output_column] = working[source_column].copy()
    output["spatial_role"] = _SPATIAL_ROLE
    output["geometry_status"] = status
    output["geometry"] = working.geometry.copy()

    normalized = gpd.GeoDataFrame(
        output.loc[:, list(_OUTPUT_COLUMNS)],
        geometry="geometry",
        crs=working.crs,
    )
    if len(normalized) != len(frame):
        raise IgnRoadNormalizationError("IGN road normalization changed the row count")
    if not isinstance(normalized.index, pd.RangeIndex):
        raise IgnRoadNormalizationError(
            "IGN normalized road output must use a RangeIndex"
        )
    if (
        normalized["road_feature_id"].isna().any()
        or normalized["road_feature_id"].duplicated().any()
    ):
        raise IgnRoadNormalizationError(
            "Normalized IGN road_feature_id values must be non-null and unique"
        )
    return normalized
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_normalize_ign_roads`

**Purpose:** Implements `normalize ign roads` within the file role: Source-completely normalizes IGN road segments and raw access attributes without interpreting suitability.

**Exact signature**

```python
def _normalize_ign_roads(
    source: IgnBdTopoRoadData,
    config: IgnBdTopoSourceConfig,
) -> NormalizedIgnRoadData:
```

- Exact decorators: none.
- Declared return annotation: `NormalizedIgnRoadData`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source` | positional-or-keyword | `IgnBdTopoRoadData` | `required` |
| `config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `NormalizedIgnRoadData(<br>        road_segments=_normalize_road_frame(fresh.road_segments, context)<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.normalize_access_ign::normalize_ign_roads` via `_normalize_ign_roads`
- value/type reference: `landscout.stages.normalize_access_ign::normalize_ign_roads` via `_normalize_ign_roads`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_revalidate_ign_bdtopo_road_data` | `landscout.sources.ign_bdtopo_fr._revalidate_ign_bdtopo_road_data` |
| `_validate_source_bundle` | `landscout.stages.normalize_access_ign._validate_source_bundle` |
| `NormalizedIgnRoadData` | `landscout.stages.normalize_access_ign.NormalizedIgnRoadData` |
| `_normalize_road_frame` | `landscout.stages.normalize_access_ign._normalize_road_frame` |

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
def _normalize_ign_roads(
    source: IgnBdTopoRoadData,
    config: IgnBdTopoSourceConfig,
) -> NormalizedIgnRoadData:
    fresh = _revalidate_ign_bdtopo_road_data(source, config)
    context = _validate_source_bundle(fresh)
    return NormalizedIgnRoadData(
        road_segments=_normalize_road_frame(fresh.road_segments, context)
    )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `normalize_ign_roads`

**Purpose:** Validate and project one already-loaded IGN road source without interpretation.

**Exact signature**

```python
def normalize_ign_roads(
    source: IgnBdTopoRoadData,
    config: IgnBdTopoSourceConfig,
) -> NormalizedIgnRoadData:
```

- Exact decorators: none.
- Declared return annotation: `NormalizedIgnRoadData`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source` | positional-or-keyword | `IgnBdTopoRoadData` | `required` |
| `config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_normalize_ign_roads(source, config)`
- Explicit raise paths:
  - `TypeError("source must be an IgnBdTopoRoadData")` under lexical guard `type(source) is not IgnBdTopoRoadData`.
  - `TypeError("config must be an IgnBdTopoSourceConfig")` under lexical guard `type(config) is not IgnBdTopoSourceConfig`.
  - `re-raise`.
  - `IgnRoadNormalizationError(<br>            f"IGN road source cannot be normalized safely: {error}"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.stages::<module>` via `from landscout.stages.normalize_access_ign import (
    IgnRoadNormalizationError,
    NormalizedIgnRoadData,
    normalize_ign_roads,
)`
- import: `landscout.stages.apply_road_vehicle_proxy_policy::<module>` via `from landscout.stages.normalize_access_ign import (
    NormalizedIgnRoadData,
    normalize_ign_roads,
)`
- direct call: `landscout.stages.apply_road_vehicle_proxy_policy::_apply_ign_road_vehicle_proxy_policy` via `normalize_ign_roads`
- value/type reference: `landscout.stages.apply_road_vehicle_proxy_policy::_apply_ign_road_vehicle_proxy_policy` via `normalize_ign_roads`
- import: `tests.unit.test_normalize_access_ign::<module>` via `from landscout.stages.normalize_access_ign import (
    IgnRoadNormalizationError,
    NormalizedIgnRoadData,
    normalize_ign_roads,
)`
- direct call: `tests.unit.test_normalize_access_ign::test_road_normalization_reproduces_configured_logical_layer` via `normalize_ign_roads`
- value/type reference: `tests.unit.test_normalize_access_ign::test_road_normalization_reproduces_configured_logical_layer` via `normalize_ign_roads`
- direct call: `tests.unit.test_normalize_access_ign::test_valid_linestring_normalization_has_exact_schema_identity_and_lineage` via `normalize_ign_roads`
- value/type reference: `tests.unit.test_normalize_access_ign::test_valid_linestring_normalization_has_exact_schema_identity_and_lineage` via `normalize_ign_roads`
- direct call: `tests.unit.test_normalize_access_ign::test_valid_multilinestring_is_preserved` via `normalize_ign_roads`
- value/type reference: `tests.unit.test_normalize_access_ign::test_valid_multilinestring_is_preserved` via `normalize_ign_roads`
- direct call: `tests.unit.test_normalize_access_ign::test_z_coordinates_are_preserved_exactly` via `normalize_ign_roads`
- value/type reference: `tests.unit.test_normalize_access_ign::test_z_coordinates_are_preserved_exactly` via `normalize_ign_roads`
- direct call: `tests.unit.test_normalize_access_ign::test_row_count_order_geometry_and_range_index_are_preserved` via `normalize_ign_roads`
- value/type reference: `tests.unit.test_normalize_access_ign::test_row_count_order_geometry_and_range_index_are_preserved` via `normalize_ign_roads`
- direct call: `tests.unit.test_normalize_access_ign::test_raw_access_and_restriction_values_are_copied_without_interpretation` via `normalize_ign_roads`
- value/type reference: `tests.unit.test_normalize_access_ign::test_raw_access_and_restriction_values_are_copied_without_interpretation` via `normalize_ign_roads`
- direct call: `tests.unit.test_normalize_access_ign::test_every_raw_field_preserves_source_values_nulls_and_dtype` via `normalize_ign_roads`
- value/type reference: `tests.unit.test_normalize_access_ign::test_every_raw_field_preserves_source_values_nulls_and_dtype` via `normalize_ign_roads`
- direct call: `tests.unit.test_normalize_access_ign::test_missing_required_source_field_is_rejected` via `normalize_ign_roads`
- value/type reference: `tests.unit.test_normalize_access_ign::test_missing_required_source_field_is_rejected` via `normalize_ign_roads`
- direct call: `tests.unit.test_normalize_access_ign::test_null_or_empty_cleabs_is_rejected` via `normalize_ign_roads`
- value/type reference: `tests.unit.test_normalize_access_ign::test_null_or_empty_cleabs_is_rejected` via `normalize_ign_roads`
- direct call: `tests.unit.test_normalize_access_ign::test_unsafe_cleabs_is_rejected` via `normalize_ign_roads`
- value/type reference: `tests.unit.test_normalize_access_ign::test_unsafe_cleabs_is_rejected` via `normalize_ign_roads`
- direct call: `tests.unit.test_normalize_access_ign::test_duplicate_cleabs_is_rejected` via `normalize_ign_roads`
- value/type reference: `tests.unit.test_normalize_access_ign::test_duplicate_cleabs_is_rejected` via `normalize_ign_roads`
- direct call: `tests.unit.test_normalize_access_ign::test_wrong_or_missing_road_crs_is_rejected` via `normalize_ign_roads`
- value/type reference: `tests.unit.test_normalize_access_ign::test_wrong_or_missing_road_crs_is_rejected` via `normalize_ign_roads`
- direct call: `tests.unit.test_normalize_access_ign::test_wrong_archive_identity_is_rejected` via `normalize_ign_roads`
- value/type reference: `tests.unit.test_normalize_access_ign::test_wrong_archive_identity_is_rejected` via `normalize_ign_roads`
- direct call: `tests.unit.test_normalize_access_ign::test_wrong_source_spatial_role_is_rejected` via `normalize_ign_roads`
- value/type reference: `tests.unit.test_normalize_access_ign::test_wrong_source_spatial_role_is_rejected` via `normalize_ign_roads`
- direct call: `tests.unit.test_normalize_access_ign::test_summary_row_count_mismatch_is_rejected` via `normalize_ign_roads`
- value/type reference: `tests.unit.test_normalize_access_ign::test_summary_row_count_mismatch_is_rejected` via `normalize_ign_roads`
- direct call: `tests.unit.test_normalize_access_ign::test_road_summary_requires_strict_structural_types` via `normalize_ign_roads`
- value/type reference: `tests.unit.test_normalize_access_ign::test_road_summary_requires_strict_structural_types` via `normalize_ign_roads`
- direct call: `tests.unit.test_normalize_access_ign::test_road_archive_sha256_requires_canonical_lowercase` via `normalize_ign_roads`
- value/type reference: `tests.unit.test_normalize_access_ign::test_road_archive_sha256_requires_canonical_lowercase` via `normalize_ign_roads`
- direct call: `tests.unit.test_normalize_access_ign::test_summary_crs_mismatch_is_rejected` via `normalize_ign_roads`
- value/type reference: `tests.unit.test_normalize_access_ign::test_summary_crs_mismatch_is_rejected` via `normalize_ign_roads`
- direct call: `tests.unit.test_normalize_access_ign::test_forged_ordered_summary_schema_is_rejected` via `normalize_ign_roads`
- value/type reference: `tests.unit.test_normalize_access_ign::test_forged_ordered_summary_schema_is_rejected` via `normalize_ign_roads`
- direct call: `tests.unit.test_normalize_access_ign::test_road_source_rejects_physical_role_collision` via `normalize_ign_roads`
- value/type reference: `tests.unit.test_normalize_access_ign::test_road_source_rejects_physical_role_collision` via `normalize_ign_roads`
- direct call: `tests.unit.test_normalize_access_ign::test_road_source_rejects_duplicate_layer_inventory` via `normalize_ign_roads`
- value/type reference: `tests.unit.test_normalize_access_ign::test_road_source_rejects_duplicate_layer_inventory` via `normalize_ign_roads`
- direct call: `tests.unit.test_normalize_access_ign::test_summary_geometry_facts_mismatch_is_rejected` via `normalize_ign_roads`
- value/type reference: `tests.unit.test_normalize_access_ign::test_summary_geometry_facts_mismatch_is_rejected` via `normalize_ign_roads`
- direct call: `tests.unit.test_normalize_access_ign::test_summary_layer_must_exist_in_extraction_inventory` via `normalize_ign_roads`
- value/type reference: `tests.unit.test_normalize_access_ign::test_summary_layer_must_exist_in_extraction_inventory` via `normalize_ign_roads`
- direct call: `tests.unit.test_normalize_access_ign::test_summary_layer_and_logical_name_must_be_exact` via `normalize_ign_roads`
- value/type reference: `tests.unit.test_normalize_access_ign::test_summary_layer_and_logical_name_must_be_exact` via `normalize_ign_roads`
- direct call: `tests.unit.test_normalize_access_ign::test_valid_unsupported_geometry_type_is_rejected` via `normalize_ign_roads`
- value/type reference: `tests.unit.test_normalize_access_ign::test_valid_unsupported_geometry_type_is_rejected` via `normalize_ign_roads`
- direct call: `tests.unit.test_normalize_access_ign::test_null_empty_and_invalid_geometry_are_preserved_with_status` via `normalize_ign_roads`
- value/type reference: `tests.unit.test_normalize_access_ign::test_null_empty_and_invalid_geometry_are_preserved_with_status` via `normalize_ign_roads`
- direct call: `tests.unit.test_normalize_access_ign::test_normalization_does_not_mutate_input` via `normalize_ign_roads`
- value/type reference: `tests.unit.test_normalize_access_ign::test_normalization_does_not_mutate_input` via `normalize_ign_roads`
- direct call: `tests.unit.test_normalize_access_ign::test_road_normalization_uses_distinct_fresh_revalidated_frame` via `normalize_ign_roads`
- value/type reference: `tests.unit.test_normalize_access_ign::test_road_normalization_uses_distinct_fresh_revalidated_frame` via `normalize_ign_roads`
- direct call: `tests.unit.test_normalize_access_ign::test_high_level_rejects_coordinated_road_frame_and_summary_forgery` via `normalize_ign_roads`
- value/type reference: `tests.unit.test_normalize_access_ign::test_high_level_rejects_coordinated_road_frame_and_summary_forgery` via `normalize_ign_roads`
- direct call: `tests.unit.test_normalize_access_ign::test_malformed_public_input_has_controlled_error` via `normalize_ign_roads`
- value/type reference: `tests.unit.test_normalize_access_ign::test_malformed_public_input_has_controlled_error` via `normalize_ign_roads`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `TypeError` | `unresolved local/third-party receiver; no ownership inferred` |
| `_normalize_ign_roads` | `landscout.stages.normalize_access_ign._normalize_ign_roads` |
| `IgnRoadNormalizationError` | `landscout.stages.normalize_access_ign.IgnRoadNormalizationError` |

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
def normalize_ign_roads(
    source: IgnBdTopoRoadData,
    config: IgnBdTopoSourceConfig,
) -> NormalizedIgnRoadData:
    """Validate and project one already-loaded IGN road source without interpretation."""

    try:
        if type(source) is not IgnBdTopoRoadData:
            raise TypeError("source must be an IgnBdTopoRoadData")
        if type(config) is not IgnBdTopoSourceConfig:
            raise TypeError("config must be an IgnBdTopoSourceConfig")
        return _normalize_ign_roads(source, config)
    except IgnRoadNormalizationError:
        raise
    except Exception as error:
        raise IgnRoadNormalizationError(
            f"IGN road source cannot be normalized safely: {error}"
        ) from error
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.


## 7. Validation and data-contract summary

- Canonical schema/mapping declarations inventoried above: `_OUTPUT_COLUMNS`, `_RAW_FIELD_MAPPING`, `_REQUIRED_SOURCE_FIELDS`.
- Exact value/null/index/CRS/geometry/hash behavior is claimed only where the reproduced validators and operations enforce it.

## 8. Public exports and package ownership

Exact `__all__` members and local origins:

| Export | Local origin binding |
|---|---|
| `IgnRoadNormalizationError` | `landscout.stages.normalize_access_ign.IgnRoadNormalizationError` |
| `NormalizedIgnRoadData` | `landscout.stages.normalize_access_ign.NormalizedIgnRoadData` |
| `normalize_ign_roads` | `landscout.stages.normalize_access_ign.normalize_ign_roads` |

## 9. Trust, provenance, side effects, and business boundary

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.
- Configured identity, textual lineage, byte identity, physical source reconstruction, local envelope validation, and source-complete validation remain distinct trust levels. This companion attributes only the levels implemented in the exact source.
- Filesystem, network, hashing, CRS/geometry, process, mutation, and expected-exception evidence is listed per callable; an empty category is not silently promoted to an effect.

## 10. Change impact

A source-byte change invalidates the SHA above and requires re-auditing imports/re-exports, constants/aliases/schemas, model fields/immutability, qualified callers, side effects, controlled errors, tests, source/artifact locks, and the exact full snapshot.

## 11. Exact complete current file content

The following UTF-8 snapshot is the complete current repository file, not an excerpt. Its raw-byte SHA256 is the value in **File identity**.

```python
"""Normalize factual IGN BD TOPO roads into a stable access-domain catalog."""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass
from datetime import date, datetime

import geopandas as gpd  # type: ignore[import-untyped]
import pandas as pd  # type: ignore[import-untyped]
from pydantic import HttpUrl, TypeAdapter, ValidationError
from pyproj import CRS

from landscout.sources.ign_bdtopo_fr import (
    DepartmentCode,
    EditionString,
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    _revalidate_ign_bdtopo_road_data,
    _validate_layer_summary_contract,
)

__all__ = [
    "IgnRoadNormalizationError",
    "NormalizedIgnRoadData",
    "normalize_ign_roads",
]

_SOURCE_PROVIDER = "IGN"
_SOURCE_PRODUCT = "BD_TOPO"
_SPATIAL_ROLE = "PROXY_GEOMETRY"
_ROAD_FEATURE_TYPE = "ROAD_SEGMENT"

_OUTPUT_COLUMNS = (
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

_RAW_FIELD_MAPPING = (
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
_REQUIRED_SOURCE_FIELDS = frozenset(
    {"cleabs", "geometry", *(source for source, _ in _RAW_FIELD_MAPPING)}
)
_ROAD_GEOMETRY_TYPES = frozenset({"LineString", "MultiLineString"})
_DEPARTMENT_CODE_VALIDATOR = TypeAdapter(DepartmentCode)
_EDITION_VALIDATOR = TypeAdapter(EditionString)
_HTTP_URL_VALIDATOR = TypeAdapter(HttpUrl)
_SHA256_PATTERN = re.compile(r"^[0-9a-f]{64}$")
_IGN_PROVIDER_IDENTITIES = frozenset(
    {
        "ign",
        "institut national de l information geographique et forestiere",
        "institut national de l information geographique et forestiere ign",
    }
)


class IgnRoadNormalizationError(ValueError):
    """Raised when factual IGN road data cannot be normalized safely."""


@dataclass(frozen=True)
class _IgnRoadSourceContext:
    source_layer: str
    department_code: str
    edition: str
    product_version: str | None
    download_timestamp: str
    archive_sha256: str
    source_url: str


@dataclass(frozen=True)
class NormalizedIgnRoadData:
    """Stable factual IGN road catalog with no access-policy interpretation."""

    road_segments: gpd.GeoDataFrame


def _validated_lambert93(crs_value: object, label: str) -> CRS:
    if crs_value is None:
        raise IgnRoadNormalizationError(f"{label} CRS is required")
    try:
        source_crs = CRS.from_user_input(crs_value)
    except Exception as error:
        raise IgnRoadNormalizationError(f"{label} CRS is unreadable") from error
    expected_crs = CRS.from_epsg(2154)
    if not source_crs.is_projected or not source_crs.equals(expected_crs):
        raise IgnRoadNormalizationError(f"{label} must use EPSG:2154")
    return source_crs


def _required_exact_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise IgnRoadNormalizationError(f"IGN road {label} must be a string")
    if value != value.strip():
        raise IgnRoadNormalizationError(
            f"IGN road {label} must not contain edge whitespace"
        )
    return value


def _validate_source_context(context: _IgnRoadSourceContext) -> None:
    _required_exact_string(context.source_layer, "source_layer")
    department_code = _required_exact_string(context.department_code, "department_code")
    edition = _required_exact_string(context.edition, "edition")
    timestamp_raw = _required_exact_string(
        context.download_timestamp, "download_timestamp"
    )
    archive_sha256 = _required_exact_string(context.archive_sha256, "archive_sha256")
    source_url = _required_exact_string(context.source_url, "source_url")

    try:
        validated_department = _DEPARTMENT_CODE_VALIDATOR.validate_python(
            department_code
        )
    except ValidationError as error:
        raise IgnRoadNormalizationError(
            "IGN road department_code is invalid"
        ) from error
    if validated_department != department_code:
        raise IgnRoadNormalizationError(
            "IGN road department_code must not be rewritten"
        )

    try:
        validated_edition = _EDITION_VALIDATOR.validate_python(edition)
        date.fromisoformat(validated_edition)
    except (ValidationError, ValueError) as error:
        raise IgnRoadNormalizationError(
            "IGN road edition must be a valid ISO calendar date"
        ) from error
    if validated_edition != edition:
        raise IgnRoadNormalizationError("IGN road edition must not be rewritten")

    try:
        timestamp = datetime.fromisoformat(timestamp_raw)
    except ValueError as error:
        raise IgnRoadNormalizationError(
            "IGN road download_timestamp must be a valid ISO datetime"
        ) from error
    if timestamp.tzinfo is None or timestamp.utcoffset() is None:
        raise IgnRoadNormalizationError(
            "IGN road download_timestamp must be timezone-aware"
        )

    if _SHA256_PATTERN.fullmatch(archive_sha256) is None:
        raise IgnRoadNormalizationError(
            "IGN road archive_sha256 must contain 64 hexadecimal characters"
        )
    try:
        _HTTP_URL_VALIDATOR.validate_python(source_url)
    except ValidationError as error:
        raise IgnRoadNormalizationError(
            "IGN road source_url must be a valid HTTP(S) URL"
        ) from error

    if context.product_version is not None:
        _required_exact_string(context.product_version, "product_version")


def _normalized_identity(value: object, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise IgnRoadNormalizationError(f"IGN archive {label} must be a string")
    decomposed = unicodedata.normalize("NFKD", value.casefold())
    without_accents = "".join(
        character for character in decomposed if not unicodedata.combining(character)
    )
    return " ".join(re.findall(r"[a-z0-9]+", without_accents))


def _geometry_summary(
    frame: gpd.GeoDataFrame,
) -> tuple[int, int, int, tuple[str, ...]]:
    geometry = frame.geometry
    null_mask = geometry.isna()
    empty_mask = ~null_mask & geometry.is_empty
    invalid_mask = ~null_mask & ~geometry.is_empty & ~geometry.is_valid
    geometry_types = tuple(
        sorted(str(value) for value in geometry[~null_mask].geom_type.dropna().unique())
    )
    return (
        int(null_mask.sum()),
        int(empty_mask.sum()),
        int(invalid_mask.sum()),
        geometry_types,
    )


def _validate_layer_summary(
    frame: gpd.GeoDataFrame,
    summary: IgnBdTopoLayerSummary,
    all_layer_names: tuple[str, ...],
) -> None:
    try:
        _validate_layer_summary_contract(summary)
    except Exception as error:
        raise IgnRoadNormalizationError(
            "IGN road summary schema contract is invalid"
        ) from error
    if summary.logical_name != "road_segments":
        raise IgnRoadNormalizationError("IGN road summary has the wrong logical name")
    source_layer = _required_exact_string(
        summary.source_layer_name, "summary physical layer"
    )
    if source_layer not in all_layer_names:
        raise IgnRoadNormalizationError(
            "IGN road summary physical layer is absent from the extraction layer inventory"
        )
    if summary.feature_count != len(frame):
        raise IgnRoadNormalizationError(
            "IGN road summary row count does not match the source frame"
        )
    observed_columns = tuple(str(column) for column in frame.columns)
    observed_dtypes = tuple(
        (str(column), str(dtype)) for column, dtype in frame.dtypes.items()
    )
    if summary.columns != observed_columns or summary.dtypes != observed_dtypes:
        raise IgnRoadNormalizationError(
            "IGN road summary schema columns or dtypes do not match the source frame"
        )
    if frame.active_geometry_name != "geometry":
        raise IgnRoadNormalizationError(
            "IGN road source requires an active geometry column"
        )
    frame_crs = _validated_lambert93(frame.crs, "IGN road source")
    summary_crs = _validated_lambert93(summary.crs, "IGN road summary")
    if not frame_crs.equals(summary_crs):
        raise IgnRoadNormalizationError(
            "IGN road summary CRS does not match the source frame"
        )
    expected_geometry = (
        summary.null_geometry_count,
        summary.empty_geometry_count,
        summary.invalid_geometry_count,
        summary.geometry_types,
    )
    if _geometry_summary(frame) != expected_geometry:
        raise IgnRoadNormalizationError(
            "IGN road geometry summary does not match the source frame"
        )


def _validate_source_bundle(source: IgnBdTopoRoadData) -> _IgnRoadSourceContext:
    if type(source.extraction) is not IgnBdTopoExtraction:
        raise IgnRoadNormalizationError("IGN road extraction type is invalid")
    if type(source.extraction.archive) is not IgnBdTopoDownload:
        raise IgnRoadNormalizationError("IGN road archive type is invalid")
    if type(source.road_segments_summary) is not IgnBdTopoLayerSummary:
        raise IgnRoadNormalizationError("IGN road summary type is invalid")
    archive = source.extraction.archive
    provider = _normalized_identity(archive.provider, "provider")
    product = _normalized_identity(archive.product, "product")
    if provider not in _IGN_PROVIDER_IDENTITIES:
        raise IgnRoadNormalizationError(
            "IGN archive provider is incompatible with the IGN road normalizer"
        )
    if product.replace(" ", "") != "bdtopo":
        raise IgnRoadNormalizationError(
            "IGN archive product is incompatible with the BD TOPO road normalizer"
        )
    _validated_lambert93(archive.projection, "IGN archive projection")
    roles = (
        archive.spatial_role,
        source.extraction.spatial_role,
        source.road_segments_summary.spatial_role,
    )
    if any(role != _SPATIAL_ROLE for role in roles):
        raise IgnRoadNormalizationError(
            "IGN road source spatial roles must all be PROXY_GEOMETRY"
        )
    layer_names = source.extraction.all_layer_names
    if (
        type(layer_names) is not tuple
        or not layer_names
        or any(
            not isinstance(name, str) or not name or name != name.strip()
            for name in layer_names
        )
        or len(set(layer_names)) != len(layer_names)
    ):
        raise IgnRoadNormalizationError(
            "IGN road layer inventory must be a unique non-empty tuple"
        )
    selected_layers = (
        source.extraction.electric_lines_layer,
        source.extraction.transformation_posts_layer,
    )
    if any(layer not in layer_names for layer in selected_layers):
        raise IgnRoadNormalizationError(
            "IGN road extraction selected layer is absent from the layer inventory"
        )
    if selected_layers[0] == selected_layers[1]:
        raise IgnRoadNormalizationError(
            "IGN electricity roles must use distinct layers, not the same layer"
        )
    road_layer = source.road_segments_summary.source_layer_name
    if road_layer in selected_layers:
        raise IgnRoadNormalizationError(
            "IGN road and electricity roles must use distinct layers, not the same layer"
        )
    if not isinstance(source.road_segments, gpd.GeoDataFrame):
        raise IgnRoadNormalizationError(
            "IGN road_segments must be a GeoDataFrame with an active geometry column"
        )
    _validate_source_frame(source.road_segments)
    _validate_layer_summary(
        source.road_segments,
        source.road_segments_summary,
        source.extraction.all_layer_names,
    )
    return _IgnRoadSourceContext(
        source_layer=source.road_segments_summary.source_layer_name,
        department_code=archive.department_code,
        edition=archive.edition,
        product_version=archive.product_version,
        download_timestamp=archive.download_timestamp,
        archive_sha256=archive.sha256,
        source_url=archive.source_url,
    )


def _validate_identifiers(frame: gpd.GeoDataFrame) -> None:
    identifiers = frame["cleabs"]
    if identifiers.isna().any():
        raise IgnRoadNormalizationError("IGN road cleabs values must not be null")
    values = identifiers.tolist()
    if any(not isinstance(identifier, str) for identifier in values):
        raise IgnRoadNormalizationError("IGN road cleabs values must be strings")
    if any(not identifier.strip() for identifier in values):
        raise IgnRoadNormalizationError("IGN road cleabs values must not be empty")
    if any(identifier != identifier.strip() for identifier in values):
        raise IgnRoadNormalizationError(
            "IGN road cleabs values must not contain edge whitespace"
        )
    if any(":" in identifier for identifier in values):
        raise IgnRoadNormalizationError("IGN road cleabs values must not contain ':'")
    if any(
        unicodedata.category(character) == "Cc"
        for identifier in values
        for character in identifier
    ):
        raise IgnRoadNormalizationError(
            "IGN road cleabs values must not contain control characters"
        )
    if identifiers.duplicated().any():
        raise IgnRoadNormalizationError("IGN road cleabs values must be unique")


def _validate_source_frame(frame: gpd.GeoDataFrame) -> None:
    if frame.columns.duplicated().any():
        raise IgnRoadNormalizationError(
            "IGN road source columns must not contain duplicates"
        )
    missing = _REQUIRED_SOURCE_FIELDS - set(frame.columns)
    if missing:
        formatted = ", ".join(sorted(missing))
        raise IgnRoadNormalizationError(
            f"Missing required IGN road source columns: {formatted}"
        )
    if frame.active_geometry_name != "geometry":
        raise IgnRoadNormalizationError(
            "IGN road source requires an active geometry column"
        )
    _validated_lambert93(frame.crs, "IGN road source")
    _validate_identifiers(frame)


def _geometry_status(geometry: gpd.GeoSeries) -> pd.Series:
    status = pd.Series("VALID", index=geometry.index, dtype="object")
    null_mask = geometry.isna()
    empty_mask = ~null_mask & geometry.is_empty
    invalid_mask = ~null_mask & ~geometry.is_empty & ~geometry.is_valid
    status.loc[null_mask] = "NULL"
    status.loc[empty_mask] = "EMPTY"
    status.loc[invalid_mask] = "INVALID"
    return status


def _normalize_road_frame(
    frame: gpd.GeoDataFrame,
    context: _IgnRoadSourceContext,
) -> gpd.GeoDataFrame:
    _validate_source_context(context)
    _validate_source_frame(frame)
    working = frame.reset_index(drop=True).copy()
    status = _geometry_status(working.geometry)
    valid_types = working.loc[status == "VALID", "geometry"].geom_type
    unsupported = sorted(set(valid_types.dropna()) - _ROAD_GEOMETRY_TYPES)
    if unsupported:
        raise IgnRoadNormalizationError(
            "IGN road source has unsupported VALID geometry types: "
            + ", ".join(unsupported)
        )

    source_ids = working["cleabs"].copy()
    output = pd.DataFrame(index=working.index.copy())
    output["road_feature_id"] = source_ids.map(
        lambda identifier: f"IGN_BDTOPO:{_ROAD_FEATURE_TYPE}:{identifier}"
    )
    output["road_feature_type"] = _ROAD_FEATURE_TYPE
    output["source_provider"] = _SOURCE_PROVIDER
    output["source_product"] = _SOURCE_PRODUCT
    output["source_layer"] = context.source_layer
    output["source_feature_id"] = source_ids
    output["source_department_code"] = context.department_code
    output["source_edition"] = context.edition
    output["source_product_version"] = context.product_version
    output["source_download_timestamp"] = context.download_timestamp
    output["source_archive_sha256"] = context.archive_sha256
    output["source_url"] = context.source_url
    for source_column, output_column in _RAW_FIELD_MAPPING:
        output[output_column] = working[source_column].copy()
    output["spatial_role"] = _SPATIAL_ROLE
    output["geometry_status"] = status
    output["geometry"] = working.geometry.copy()

    normalized = gpd.GeoDataFrame(
        output.loc[:, list(_OUTPUT_COLUMNS)],
        geometry="geometry",
        crs=working.crs,
    )
    if len(normalized) != len(frame):
        raise IgnRoadNormalizationError("IGN road normalization changed the row count")
    if not isinstance(normalized.index, pd.RangeIndex):
        raise IgnRoadNormalizationError(
            "IGN normalized road output must use a RangeIndex"
        )
    if (
        normalized["road_feature_id"].isna().any()
        or normalized["road_feature_id"].duplicated().any()
    ):
        raise IgnRoadNormalizationError(
            "Normalized IGN road_feature_id values must be non-null and unique"
        )
    return normalized


def _normalize_ign_roads(
    source: IgnBdTopoRoadData,
    config: IgnBdTopoSourceConfig,
) -> NormalizedIgnRoadData:
    fresh = _revalidate_ign_bdtopo_road_data(source, config)
    context = _validate_source_bundle(fresh)
    return NormalizedIgnRoadData(
        road_segments=_normalize_road_frame(fresh.road_segments, context)
    )


def normalize_ign_roads(
    source: IgnBdTopoRoadData,
    config: IgnBdTopoSourceConfig,
) -> NormalizedIgnRoadData:
    """Validate and project one already-loaded IGN road source without interpretation."""

    try:
        if type(source) is not IgnBdTopoRoadData:
            raise TypeError("source must be an IgnBdTopoRoadData")
        if type(config) is not IgnBdTopoSourceConfig:
            raise TypeError("config must be an IgnBdTopoSourceConfig")
        return _normalize_ign_roads(source, config)
    except IgnRoadNormalizationError:
        raise
    except Exception as error:
        raise IgnRoadNormalizationError(
            f"IGN road source cannot be normalized safely: {error}"
        ) from error
```

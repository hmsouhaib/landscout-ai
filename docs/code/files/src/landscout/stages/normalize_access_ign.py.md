# `src/landscout/stages/normalize_access_ign.py`

## File identity

- Repository path: `src/landscout/stages/normalize_access_ign.py`
- File type: Python source
- Layer: processing/policy stage
- Domain: road
- Responsibility: Source-completely normalizes IGN road segments and raw access attributes without interpreting suitability.
- Source SHA256: `7f5132849965a01ce4e6826044f2e879dd3a4c7614ae8f5cc8e2d0fed080cfa3`

## 1. Purpose

Source-completely normalizes IGN road segments and raw access attributes without interpreting suitability.

## 2. Position in LandScout architecture

This file belongs to the **processing/policy stage** layer and the **road** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

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

### A. Python constants

#### `_SOURCE_PROVIDER`

```python
_SOURCE_PROVIDER = "IGN"
```

Module-level technical/source/policy constant consumed by the exact references below.

#### `_SOURCE_PRODUCT`

```python
_SOURCE_PRODUCT = "BD_TOPO"
```

Module-level technical/source/policy constant consumed by the exact references below.

#### `_SPATIAL_ROLE`

```python
_SPATIAL_ROLE = "PROXY_GEOMETRY"
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema.

#### `_ROAD_FEATURE_TYPE`

```python
_ROAD_FEATURE_TYPE = "ROAD_SEGMENT"
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema.

#### `_OUTPUT_COLUMNS`

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

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/stages/normalize_access_ign.py::_normalize_road_frame` (value argument/reference).

#### `_RAW_FIELD_MAPPING`

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

Explicit mapping between source/input and target/output fields; keys and values are documented separately.

#### `_REQUIRED_SOURCE_FIELDS`

```python
_REQUIRED_SOURCE_FIELDS = frozenset(
    {"cleabs", "geometry", *(source for source, _ in _RAW_FIELD_MAPPING)}
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section.

#### `_ROAD_GEOMETRY_TYPES`

```python
_ROAD_GEOMETRY_TYPES = frozenset({"LineString", "MultiLineString"})
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema.

#### `_DEPARTMENT_CODE_VALIDATOR`

```python
_DEPARTMENT_CODE_VALIDATOR = TypeAdapter(DepartmentCode)
```

Module-level technical/source/policy constant consumed by the exact references below.

#### `_EDITION_VALIDATOR`

```python
_EDITION_VALIDATOR = TypeAdapter(EditionString)
```

Module-level technical/source/policy constant consumed by the exact references below.

#### `_HTTP_URL_VALIDATOR`

```python
_HTTP_URL_VALIDATOR = TypeAdapter(HttpUrl)
```

Configured/constructed URL component or origin constraint; it is textual identity until the transport/source validator proves bytes.

#### `_SHA256_PATTERN`

```python
_SHA256_PATTERN = re.compile(r"^[0-9a-f]{64}$")
```

Compiled/text regular expression used by the named validation path; the fenced declaration preserves every metacharacter exactly.

#### `_IGN_PROVIDER_IDENTITIES`

```python
_IGN_PROVIDER_IDENTITIES = frozenset(
    {
        "ign",
        "institut national de l information geographique et forestiere",
        "institut national de l information geographique et forestiere ign",
    }
)
```

Module-level technical/source/policy constant consumed by the exact references below.


### B. Type aliases and closed domains

No module-level Literal/Annotated/TypeAlias declaration is present.

### C. Meaningful dunder contracts

- `__all__` — explicit public export allow-list.
```python
__all__ = [
    "IgnRoadNormalizationError",
    "NormalizedIgnRoadData",
    "normalize_ign_roads",
]
```


### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

### `IgnRoadNormalizationError`

**Purpose:** Raised when factual IGN road data cannot be normalized safely.

**Kind:** controlled exception.

**Inheritance:** `ValueError`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.normalize_access_ign import (
    IgnRoadNormalizationError,
    NormalizedIgnRoadData,
    normalize_ign_roads,
)`.
- direct call or construction: `src/landscout/stages/normalize_access_ign.py::_validated_lambert93` via `IgnRoadNormalizationError`.
- direct call or construction: `src/landscout/stages/normalize_access_ign.py::_required_exact_string` via `IgnRoadNormalizationError`.
- direct call or construction: `src/landscout/stages/normalize_access_ign.py::_validate_source_context` via `IgnRoadNormalizationError`.
- direct call or construction: `src/landscout/stages/normalize_access_ign.py::_normalized_identity` via `IgnRoadNormalizationError`.
- direct call or construction: `src/landscout/stages/normalize_access_ign.py::_validate_layer_summary` via `IgnRoadNormalizationError`.
- direct call or construction: `src/landscout/stages/normalize_access_ign.py::_validate_source_bundle` via `IgnRoadNormalizationError`.
- direct call or construction: `src/landscout/stages/normalize_access_ign.py::_validate_identifiers` via `IgnRoadNormalizationError`.
- direct call or construction: `src/landscout/stages/normalize_access_ign.py::_validate_source_frame` via `IgnRoadNormalizationError`.
- direct call or construction: `src/landscout/stages/normalize_access_ign.py::_normalize_road_frame` via `IgnRoadNormalizationError`.
- direct call or construction: `src/landscout/stages/normalize_access_ign.py::normalize_ign_roads` via `IgnRoadNormalizationError`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_normalization_failure_stops_policy_loading` via `IgnRoadNormalizationError`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_valid_geometry_status_with_unsupported_geometry_is_not_repaired` via `IgnRoadNormalizationError`.
- import/re-export: `tests/unit/test_apply_road_vehicle_proxy_policy.py::<module>` via `from landscout.stages.normalize_access_ign import (
    IgnRoadNormalizationError,
    NormalizedIgnRoadData,
)`.
- callback/function object: `tests/unit/test_normalize_access_ign.py::test_road_normalization_reproduces_configured_logical_layer` via `pytest.raises(IgnRoadNormalizationError, match='source|configured|physical')`.
- callback/function object: `tests/unit/test_normalize_access_ign.py::test_missing_required_source_field_is_rejected` via `pytest.raises(IgnRoadNormalizationError, match=column)`.
- callback/function object: `tests/unit/test_normalize_access_ign.py::test_null_or_empty_cleabs_is_rejected` via `pytest.raises(IgnRoadNormalizationError, match='cleabs')`.
- callback/function object: `tests/unit/test_normalize_access_ign.py::test_unsafe_cleabs_is_rejected` via `pytest.raises(IgnRoadNormalizationError, match='cleabs')`.
- callback/function object: `tests/unit/test_normalize_access_ign.py::test_duplicate_cleabs_is_rejected` via `pytest.raises(IgnRoadNormalizationError, match='unique')`.
- callback/function object: `tests/unit/test_normalize_access_ign.py::test_wrong_or_missing_road_crs_is_rejected` via `pytest.raises(IgnRoadNormalizationError, match='CRS|2154')`.
- callback/function object: `tests/unit/test_normalize_access_ign.py::test_wrong_archive_identity_is_rejected` via `pytest.raises(IgnRoadNormalizationError, match=message)`.
- callback/function object: `tests/unit/test_normalize_access_ign.py::test_wrong_source_spatial_role_is_rejected` via `pytest.raises(IgnRoadNormalizationError, match='PROXY_GEOMETRY')`.
- callback/function object: `tests/unit/test_normalize_access_ign.py::test_summary_row_count_mismatch_is_rejected` via `pytest.raises(IgnRoadNormalizationError, match='row count')`.
- callback/function object: `tests/unit/test_normalize_access_ign.py::test_road_summary_requires_strict_structural_types` via `pytest.raises(IgnRoadNormalizationError)`.
- callback/function object: `tests/unit/test_normalize_access_ign.py::test_road_archive_sha256_requires_canonical_lowercase` via `pytest.raises(IgnRoadNormalizationError)`.
- callback/function object: `tests/unit/test_normalize_access_ign.py::test_summary_crs_mismatch_is_rejected` via `pytest.raises(IgnRoadNormalizationError, match='CRS|2154')`.
- callback/function object: `tests/unit/test_normalize_access_ign.py::test_forged_ordered_summary_schema_is_rejected` via `pytest.raises(IgnRoadNormalizationError, match='schema|columns|dtype')`.
- callback/function object: `tests/unit/test_normalize_access_ign.py::test_road_source_rejects_physical_role_collision` via `pytest.raises(IgnRoadNormalizationError, match='same layer|distinct|role')`.
- callback/function object: `tests/unit/test_normalize_access_ign.py::test_road_source_rejects_duplicate_layer_inventory` via `pytest.raises(IgnRoadNormalizationError, match='inventory|duplicate')`.
- callback/function object: `tests/unit/test_normalize_access_ign.py::test_summary_geometry_facts_mismatch_is_rejected` via `pytest.raises(IgnRoadNormalizationError, match='geometry summary')`.
- callback/function object: `tests/unit/test_normalize_access_ign.py::test_summary_layer_must_exist_in_extraction_inventory` via `pytest.raises(IgnRoadNormalizationError, match='layer inventory')`.
- callback/function object: `tests/unit/test_normalize_access_ign.py::test_summary_layer_and_logical_name_must_be_exact` via `pytest.raises(IgnRoadNormalizationError, match='physical layer')`.
- callback/function object: `tests/unit/test_normalize_access_ign.py::test_summary_layer_and_logical_name_must_be_exact` via `pytest.raises(IgnRoadNormalizationError, match='logical name')`.
- callback/function object: `tests/unit/test_normalize_access_ign.py::test_valid_unsupported_geometry_type_is_rejected` via `pytest.raises(IgnRoadNormalizationError, match='geometry types')`.
- callback/function object: `tests/unit/test_normalize_access_ign.py::test_high_level_rejects_coordinated_road_frame_and_summary_forgery` via `pytest.raises(IgnRoadNormalizationError, match='physical|fresh|source')`.
- callback/function object: `tests/unit/test_normalize_access_ign.py::test_malformed_public_input_has_controlled_error` via `pytest.raises(IgnRoadNormalizationError)`.
- import/re-export: `tests/unit/test_normalize_access_ign.py::<module>` via `from landscout.stages.normalize_access_ign import (
    IgnRoadNormalizationError,
    NormalizedIgnRoadData,
    normalize_ign_roads,
)`.

**Exact class source**

```python
class IgnRoadNormalizationError(ValueError):
    """Raised when factual IGN road data cannot be normalized safely."""
```

### `_IgnRoadSourceContext`

**Purpose:** Immutable result/value envelope carrying `source_layer`, `department_code`, `edition`, `product_version`, `download_timestamp`, `archive_sha256`, `source_url`.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `source_layer` | `source_layer: str` | Exact source-lineage scalar named by the field; it is compared with configuration/result/row lineage but is not physical proof without source-byte revalidation. |
| `department_code` | `department_code: str` | Stores `_IgnRoadSourceContext`'s `department code` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `edition` | `edition: str` | Stores `_IgnRoadSourceContext`'s `edition` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `product_version` | `product_version: str \| None` | Stores `_IgnRoadSourceContext`'s `product version` value under exact annotation `str | None`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `download_timestamp` | `download_timestamp: str` | Source, download, or processing time in the exact representation enforced by the owning validator; it is lineage, not physical proof by itself. |
| `archive_sha256` | `archive_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `source_url` | `source_url: str` | Exact source/evidence URL whose HTTPS/origin/path constraints are enforced by the owning configuration or source validator. |

**Interface consumers**

- direct call or construction: `src/landscout/stages/normalize_access_ign.py::_validate_source_bundle` via `_IgnRoadSourceContext`.

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

**Purpose:** Stable factual IGN road catalog with no access-policy interpretation.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `road_segments` | `road_segments: gpd.GeoDataFrame` | Pandas/GeoPandas result frame named by this field; its exact ordered schema, dtype, CRS/index, and preservation contract is documented by the owning result validator and schema declarations. |

**Interface consumers**

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.normalize_access_ign import (
    IgnRoadNormalizationError,
    NormalizedIgnRoadData,
    normalize_ign_roads,
)`.
- import/re-export: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::<module>` via `from landscout.stages.normalize_access_ign import (
    NormalizedIgnRoadData,
    normalize_ign_roads,
)`.
- direct call or construction: `src/landscout/stages/normalize_access_ign.py::_normalize_ign_roads` via `NormalizedIgnRoadData`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::_apply` via `NormalizedIgnRoadData`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_malformed_policy_path_has_controlled_error` via `NormalizedIgnRoadData`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_source_complete_normalization_is_invoked_exactly_once` via `NormalizedIgnRoadData`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_source_object_is_not_mutated` via `NormalizedIgnRoadData`.
- import/re-export: `tests/unit/test_apply_road_vehicle_proxy_policy.py::<module>` via `from landscout.stages.normalize_access_ign import (
    IgnRoadNormalizationError,
    NormalizedIgnRoadData,
)`.
- import/re-export: `tests/unit/test_normalize_access_ign.py::<module>` via `from landscout.stages.normalize_access_ign import (
    IgnRoadNormalizationError,
    NormalizedIgnRoadData,
    normalize_ign_roads,
)`.

**Exact class source**

```python
class NormalizedIgnRoadData:
    """Stable factual IGN road catalog with no access-policy interpretation."""

    road_segments: gpd.GeoDataFrame
```


## 6. Functions and methods

### `_validated_lambert93`

**Exact signature**

```python
def _validated_lambert93(crs_value: object, label: str) -> CRS:
```

**Purpose**

Checks and returns canonical lambert93; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `CRS`.
- Every observed return expression is reproduced without truncation:
```python
source_crs
```

**Validation and exceptions**

- Guard with a raise path: `crs_value is None`.
- Guard with a raise path: `not source_crs.is_projected or not source_crs.equals(expected_crs)`.
- Explicit raise expressions: `IgnRoadNormalizationError(f'{label} CRS is required')`, `IgnRoadNormalizationError(f'{label} CRS is unreadable')`, `IgnRoadNormalizationError(f'{label} must use EPSG:2154')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/assess_grid_coverage.py::_validate_coverage_summary` via `_validated_lambert93`.
- direct call or construction: `src/landscout/stages/assess_grid_coverage.py::_validate_source_coverage` via `_validated_lambert93`.
- direct call or construction: `src/landscout/stages/normalize_access_ign.py::_validate_layer_summary` via `_validated_lambert93`.
- direct call or construction: `src/landscout/stages/normalize_access_ign.py::_validate_source_bundle` via `_validated_lambert93`.
- direct call or construction: `src/landscout/stages/normalize_access_ign.py::_validate_source_frame` via `_validated_lambert93`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_validate_input` via `_validated_lambert93`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_validate_layer_summary` via `_validated_lambert93`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_validate_archive_identity` via `_validated_lambert93`.

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

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_required_exact_string`

**Exact signature**

```python
def _required_exact_string(value: object, label: str) -> str:
```

**Purpose**

Private `road` helper for required exact string; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
value
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(value, str) or not value.strip()`.
- Guard with a raise path: `value != value.strip()`.
- Explicit raise expressions: `IgnRoadNormalizationError(f'IGN road {label} must be a string')`, `IgnRoadNormalizationError(f'IGN road {label} must not contain edge whitespace')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/normalize_access_ign.py::_validate_source_context` via `_required_exact_string`.
- direct call or construction: `src/landscout/stages/normalize_access_ign.py::_validate_layer_summary` via `_required_exact_string`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_validate_source_context` via `_required_exact_string`.

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

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_validate_source_context`

**Exact signature**

```python
def _validate_source_context(context: _IgnRoadSourceContext) -> None:
```

**Purpose**

Rejects malformed or inconsistent source context; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `validated_department != department_code`.
- Guard with a raise path: `validated_edition != edition`.
- Guard with a raise path: `timestamp.tzinfo is None or timestamp.utcoffset() is None`.
- Guard with a raise path: `_SHA256_PATTERN.fullmatch(archive_sha256) is None`.
- Explicit raise expressions: `IgnRoadNormalizationError('IGN road archive_sha256 must contain 64 hexadecimal characters')`, `IgnRoadNormalizationError('IGN road department_code is invalid')`, `IgnRoadNormalizationError('IGN road department_code must not be rewritten')`, `IgnRoadNormalizationError('IGN road download_timestamp must be a valid ISO datetime')`, `IgnRoadNormalizationError('IGN road download_timestamp must be timezone-aware')`, `IgnRoadNormalizationError('IGN road edition must be a valid ISO calendar date')`, `IgnRoadNormalizationError('IGN road edition must not be rewritten')`, `IgnRoadNormalizationError('IGN road source_url must be a valid HTTP(S) URL')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `_SHA256_PATTERN.fullmatch`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/normalize_access_ign.py::_normalize_road_frame` via `_validate_source_context`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_normalize_ign_electric_lines` via `_validate_source_context`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_normalize_ign_transformation_posts` via `_validate_source_context`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_internal_source_context_accepts_supported_department_codes` via `grid_normalization._validate_source_context`.
- property/attribute access: `tests/unit/test_normalize_grid_ign.py::test_internal_source_context_accepts_supported_department_codes` via `grid_normalization._validate_source_context`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_internal_source_context_rejects_invalid_lineage_values` via `grid_normalization._validate_source_context`.
- property/attribute access: `tests/unit/test_normalize_grid_ign.py::test_internal_source_context_rejects_invalid_lineage_values` via `grid_normalization._validate_source_context`.

**Complete source-ordered implementation**

```python
def _validate_source_context(context: _IgnRoadSourceContext) -> None:
    _required_exact_string(context.source_layer, "source_layer")
    department_code = _required_exact_string(
        context.department_code, "department_code"
    )
    edition = _required_exact_string(context.edition, "edition")
    timestamp_raw = _required_exact_string(
        context.download_timestamp, "download_timestamp"
    )
    archive_sha256 = _required_exact_string(
        context.archive_sha256, "archive_sha256"
    )
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

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_normalized_identity`

**Exact signature**

```python
def _normalized_identity(value: object, label: str) -> str:
```

**Purpose**

Private `road` helper for normalized identity; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
' '.join(re.findall('[a-z0-9]+', without_accents))
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(value, str) or not value.strip()`.
- Explicit raise expressions: `IgnRoadNormalizationError(f'IGN archive {label} must be a string')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/assess_grid_coverage.py::_validate_source_coverage` via `_normalized_identity`.
- direct call or construction: `src/landscout/stages/assess_grid_coverage.py::_validate_configured_coverage_identity` via `_normalized_identity`.
- direct call or construction: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_source_coverage` via `_normalized_identity`.
- direct call or construction: `src/landscout/stages/normalize_access_ign.py::_validate_source_bundle` via `_normalized_identity`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_validate_archive_identity` via `_normalized_identity`.

**Complete source-ordered implementation**

```python
def _normalized_identity(value: object, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise IgnRoadNormalizationError(f"IGN archive {label} must be a string")
    decomposed = unicodedata.normalize("NFKD", value.casefold())
    without_accents = "".join(
        character
        for character in decomposed
        if not unicodedata.combining(character)
    )
    return " ".join(re.findall(r"[a-z0-9]+", without_accents))
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_geometry_summary`

**Exact signature**

```python
def _geometry_summary(
    frame: gpd.GeoDataFrame,
) -> tuple[int, int, int, tuple[str, ...]]:
```

**Purpose**

Private `road` helper for geometry summary; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[int, int, int, tuple[str, ...]]`.
- Every observed return expression is reproduced without truncation:
```python
(int(null_mask.sum()), int(empty_mask.sum()), int(invalid_mask.sum()), geometry_types)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `geometry.isna`, `geometry[~null_mask].geom_type.dropna`, `geometry[~null_mask].geom_type.dropna().unique`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/normalize_access_ign.py::_validate_layer_summary` via `_geometry_summary`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_validate_layer_summary` via `_geometry_summary`.

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

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_validate_layer_summary`

**Exact signature**

```python
def _validate_layer_summary(
    frame: gpd.GeoDataFrame,
    summary: IgnBdTopoLayerSummary,
    all_layer_names: tuple[str, ...],
) -> None:
```

**Purpose**

Rejects malformed or inconsistent layer summary; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `summary.logical_name != 'road_segments'`.
- Guard with a raise path: `source_layer not in all_layer_names`.
- Guard with a raise path: `summary.feature_count != len(frame)`.
- Guard with a raise path: `summary.columns != observed_columns or summary.dtypes != observed_dtypes`.
- Guard with a raise path: `frame.active_geometry_name != 'geometry'`.
- Guard with a raise path: `not frame_crs.equals(summary_crs)`.
- Guard with a raise path: `_geometry_summary(frame) != expected_geometry`.
- Explicit raise expressions: `IgnRoadNormalizationError('IGN road geometry summary does not match the source frame')`, `IgnRoadNormalizationError('IGN road source requires an active geometry column')`, `IgnRoadNormalizationError('IGN road summary CRS does not match the source frame')`, `IgnRoadNormalizationError('IGN road summary has the wrong logical name')`, `IgnRoadNormalizationError('IGN road summary physical layer is absent from the extraction layer inventory')`, `IgnRoadNormalizationError('IGN road summary row count does not match the source frame')`, `IgnRoadNormalizationError('IGN road summary schema columns or dtypes do not match the source frame')`, `IgnRoadNormalizationError('IGN road summary schema contract is invalid')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `_geometry_summary`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/enrich_planning_features.py::_normalize_layer` via `_validate_layer_summary`.
- direct call or construction: `src/landscout/stages/normalize_access_ign.py::_validate_source_bundle` via `_validate_layer_summary`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_validate_source_bundle` via `_validate_layer_summary`.

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
        raise IgnRoadNormalizationError(
            "IGN road summary has the wrong logical name"
        )
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

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_validate_source_bundle`

**Exact signature**

```python
def _validate_source_bundle(source: IgnBdTopoRoadData) -> _IgnRoadSourceContext:
```

**Purpose**

Rejects malformed or inconsistent source bundle; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `_IgnRoadSourceContext`.
- Every observed return expression is reproduced without truncation:
```python
_IgnRoadSourceContext(source_layer=source.road_segments_summary.source_layer_name, department_code=archive.department_code, edition=archive.edition, product_version=archive.product_version, download_timestamp=archive.download_timestamp, archive_sha256=archive.sha256, source_url=archive.source_url)
```

**Validation and exceptions**

- Guard with a raise path: `type(source.extraction) is not IgnBdTopoExtraction`.
- Guard with a raise path: `type(source.extraction.archive) is not IgnBdTopoDownload`.
- Guard with a raise path: `type(source.road_segments_summary) is not IgnBdTopoLayerSummary`.
- Guard with a raise path: `provider not in _IGN_PROVIDER_IDENTITIES`.
- Guard with a raise path: `product.replace(' ', '') != 'bdtopo'`.
- Guard with a raise path: `any((role != _SPATIAL_ROLE for role in roles))`.
- Guard with a raise path: `type(layer_names) is not tuple or not layer_names or any((not isinstance(name, str) or not name or name != name.strip() for name in layer_names)) or (len(set(layer_names)) != len(layer_names))`.
- Guard with a raise path: `any((layer not in layer_names for layer in selected_layers))`.
- Guard with a raise path: `selected_layers[0] == selected_layers[1]`.
- Guard with a raise path: `road_layer in selected_layers`.
- Guard with a raise path: `not isinstance(source.road_segments, gpd.GeoDataFrame)`.
- Explicit raise expressions: `IgnRoadNormalizationError('IGN archive product is incompatible with the BD TOPO road normalizer')`, `IgnRoadNormalizationError('IGN archive provider is incompatible with the IGN road normalizer')`, `IgnRoadNormalizationError('IGN electricity roles must use distinct layers, not the same layer')`, `IgnRoadNormalizationError('IGN road and electricity roles must use distinct layers, not the same layer')`, `IgnRoadNormalizationError('IGN road archive type is invalid')`, `IgnRoadNormalizationError('IGN road extraction selected layer is absent from the layer inventory')`, `IgnRoadNormalizationError('IGN road extraction type is invalid')`, `IgnRoadNormalizationError('IGN road layer inventory must be a unique non-empty tuple')`, `IgnRoadNormalizationError('IGN road source spatial roles must all be PROXY_GEOMETRY')`, `IgnRoadNormalizationError('IGN road summary type is invalid')`, `IgnRoadNormalizationError('IGN road_segments must be a GeoDataFrame with an active geometry column')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/normalize_access_ign.py::_normalize_ign_roads` via `_validate_source_bundle`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::normalize_ign_electricity` via `_validate_source_bundle`.

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

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_validate_identifiers`

**Exact signature**

```python
def _validate_identifiers(frame: gpd.GeoDataFrame) -> None:
```

**Purpose**

Rejects malformed or inconsistent identifiers; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `identifiers.isna().any()`.
- Guard with a raise path: `any((not isinstance(identifier, str) for identifier in values))`.
- Guard with a raise path: `any((not identifier.strip() for identifier in values))`.
- Guard with a raise path: `any((identifier != identifier.strip() for identifier in values))`.
- Guard with a raise path: `any((':' in identifier for identifier in values))`.
- Guard with a raise path: `any((unicodedata.category(character) == 'Cc' for identifier in values for character in identifier))`.
- Guard with a raise path: `identifiers.duplicated().any()`.
- Explicit raise expressions: `IgnRoadNormalizationError("IGN road cleabs values must not contain ':'")`, `IgnRoadNormalizationError('IGN road cleabs values must be strings')`, `IgnRoadNormalizationError('IGN road cleabs values must be unique')`, `IgnRoadNormalizationError('IGN road cleabs values must not be empty')`, `IgnRoadNormalizationError('IGN road cleabs values must not be null')`, `IgnRoadNormalizationError('IGN road cleabs values must not contain control characters')`, `IgnRoadNormalizationError('IGN road cleabs values must not contain edge whitespace')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/normalize_access_ign.py::_validate_source_frame` via `_validate_identifiers`.

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

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_validate_source_frame`

**Exact signature**

```python
def _validate_source_frame(frame: gpd.GeoDataFrame) -> None:
```

**Purpose**

Rejects malformed or inconsistent source frame; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `frame.columns.duplicated().any()`.
- Guard with a raise path: `missing`.
- Guard with a raise path: `frame.active_geometry_name != 'geometry'`.
- Explicit raise expressions: `IgnRoadNormalizationError('IGN road source columns must not contain duplicates')`, `IgnRoadNormalizationError('IGN road source requires an active geometry column')`, `IgnRoadNormalizationError(f'Missing required IGN road source columns: {formatted}')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/normalize_access_ign.py::_validate_source_bundle` via `_validate_source_frame`.
- direct call or construction: `src/landscout/stages/normalize_access_ign.py::_normalize_road_frame` via `_validate_source_frame`.

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

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_geometry_status`

**Exact signature**

```python
def _geometry_status(geometry: gpd.GeoSeries) -> pd.Series:
```

**Purpose**

Private `road` helper for geometry status; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `pd.Series`.
- Every observed return expression is reproduced without truncation:
```python
status
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `geometry.isna`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: `status.loc[empty_mask]`, `status.loc[invalid_mask]`, `status.loc[null_mask]`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/normalize_access_ign.py::_normalize_road_frame` via `_geometry_status`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_normalize_ign_electric_lines` via `_geometry_status`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_normalize_ign_transformation_posts` via `_geometry_status`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::_lines` via `_geometry_status`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::_posts` via `_geometry_status`.

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

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_normalize_road_frame`

**Exact signature**

```python
def _normalize_road_frame(
    frame: gpd.GeoDataFrame,
    context: _IgnRoadSourceContext,
) -> gpd.GeoDataFrame:
```

**Purpose**

Projects validated source facts into road frame; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
normalized
```

**Validation and exceptions**

- Guard with a raise path: `unsupported`.
- Guard with a raise path: `len(normalized) != len(frame)`.
- Guard with a raise path: `not isinstance(normalized.index, pd.RangeIndex)`.
- Guard with a raise path: `normalized['road_feature_id'].isna().any() or normalized['road_feature_id'].duplicated().any()`.
- Explicit raise expressions: `IgnRoadNormalizationError('IGN normalized road output must use a RangeIndex')`, `IgnRoadNormalizationError('IGN road normalization changed the row count')`, `IgnRoadNormalizationError('IGN road source has unsupported VALID geometry types: ' + ', '.join(unsupported))`, `IgnRoadNormalizationError('Normalized IGN road_feature_id values must be non-null and unique')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `_geometry_status`, `working.geometry.copy`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: `output['geometry']`, `output['geometry_status']`, `output['road_feature_id']`, `output['road_feature_type']`, `output['source_archive_sha256']`, `output['source_department_code']`, `output['source_download_timestamp']`, `output['source_edition']`, `output['source_feature_id']`, `output['source_layer']`, `output['source_product']`, `output['source_product_version']`, `output['source_provider']`, `output['source_url']`, `output['spatial_role']`, `output[output_column]`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/normalize_access_ign.py::_normalize_ign_roads` via `_normalize_road_frame`.

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
    if normalized["road_feature_id"].isna().any() or normalized[
        "road_feature_id"
    ].duplicated().any():
        raise IgnRoadNormalizationError(
            "Normalized IGN road_feature_id values must be non-null and unique"
        )
    return normalized
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_normalize_ign_roads`

**Exact signature**

```python
def _normalize_ign_roads(
    source: IgnBdTopoRoadData,
    config: IgnBdTopoSourceConfig,
) -> NormalizedIgnRoadData:
```

**Purpose**

Projects validated source facts into ign roads; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `NormalizedIgnRoadData`.
- Every observed return expression is reproduced without truncation:
```python
NormalizedIgnRoadData(road_segments=_normalize_road_frame(source.road_segments, context))
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/normalize_access_ign.py::normalize_ign_roads` via `_normalize_ign_roads`.

**Complete source-ordered implementation**

```python
def _normalize_ign_roads(
    source: IgnBdTopoRoadData,
    config: IgnBdTopoSourceConfig,
) -> NormalizedIgnRoadData:
    context = _validate_source_bundle(source)
    _revalidate_ign_bdtopo_road_data(source, config)
    return NormalizedIgnRoadData(
        road_segments=_normalize_road_frame(source.road_segments, context)
    )
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `normalize_ign_roads`

**Exact signature**

```python
def normalize_ign_roads(
    source: IgnBdTopoRoadData,
    config: IgnBdTopoSourceConfig,
) -> NormalizedIgnRoadData:
```

**Purpose**

Validate and project one already-loaded IGN road source without interpretation.

**Return contract**

- Declared return annotation: `NormalizedIgnRoadData`.
- Every observed return expression is reproduced without truncation:
```python
_normalize_ign_roads(source, config)
```

**Validation and exceptions**

- Guard with a raise path: `type(source) is not IgnBdTopoRoadData`.
- Guard with a raise path: `type(config) is not IgnBdTopoSourceConfig`.
- Explicit raise expressions: `IgnRoadNormalizationError('IGN road source cannot be normalized safely')`, `TypeError('config must be an IgnBdTopoSourceConfig')`, `TypeError('source must be an IgnBdTopoRoadData')`, `re-raise`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.normalize_access_ign import (
    IgnRoadNormalizationError,
    NormalizedIgnRoadData,
    normalize_ign_roads,
)`.
- direct call or construction: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::_apply_ign_road_vehicle_proxy_policy` via `normalize_ign_roads`.
- import/re-export: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::<module>` via `from landscout.stages.normalize_access_ign import (
    NormalizedIgnRoadData,
    normalize_ign_roads,
)`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_road_normalization_reproduces_configured_logical_layer` via `normalize_ign_roads`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_valid_linestring_normalization_has_exact_schema_identity_and_lineage` via `normalize_ign_roads`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_valid_multilinestring_is_preserved` via `normalize_ign_roads`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_z_coordinates_are_preserved_exactly` via `normalize_ign_roads`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_row_count_order_geometry_and_range_index_are_preserved` via `normalize_ign_roads`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_raw_access_and_restriction_values_are_copied_without_interpretation` via `normalize_ign_roads`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_every_raw_field_preserves_source_values_nulls_and_dtype` via `normalize_ign_roads`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_missing_required_source_field_is_rejected` via `normalize_ign_roads`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_null_or_empty_cleabs_is_rejected` via `normalize_ign_roads`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_unsafe_cleabs_is_rejected` via `normalize_ign_roads`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_duplicate_cleabs_is_rejected` via `normalize_ign_roads`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_wrong_or_missing_road_crs_is_rejected` via `normalize_ign_roads`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_wrong_archive_identity_is_rejected` via `normalize_ign_roads`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_wrong_source_spatial_role_is_rejected` via `normalize_ign_roads`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_summary_row_count_mismatch_is_rejected` via `normalize_ign_roads`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_road_summary_requires_strict_structural_types` via `normalize_ign_roads`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_road_archive_sha256_requires_canonical_lowercase` via `normalize_ign_roads`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_summary_crs_mismatch_is_rejected` via `normalize_ign_roads`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_forged_ordered_summary_schema_is_rejected` via `normalize_ign_roads`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_road_source_rejects_physical_role_collision` via `normalize_ign_roads`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_road_source_rejects_duplicate_layer_inventory` via `normalize_ign_roads`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_summary_geometry_facts_mismatch_is_rejected` via `normalize_ign_roads`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_summary_layer_must_exist_in_extraction_inventory` via `normalize_ign_roads`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_summary_layer_and_logical_name_must_be_exact` via `normalize_ign_roads`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_valid_unsupported_geometry_type_is_rejected` via `normalize_ign_roads`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_null_empty_and_invalid_geometry_are_preserved_with_status` via `normalize_ign_roads`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_normalization_does_not_mutate_input` via `normalize_ign_roads`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_high_level_rejects_coordinated_road_frame_and_summary_forgery` via `normalize_ign_roads`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_malformed_public_input_has_controlled_error` via `normalize_ign_roads`.
- import/re-export: `tests/unit/test_normalize_access_ign.py::<module>` via `from landscout.stages.normalize_access_ign import (
    IgnRoadNormalizationError,
    NormalizedIgnRoadData,
    normalize_ign_roads,
)`.

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
            "IGN road source cannot be normalized safely"
        ) from error
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.


## 7. Data contracts

### Frame-preservation and semantic notes

- `_OUTPUT_COLUMNS` is the complete ordered factual road schema. `_RAW_FIELD_MAPPING` copies IGN values/nulls without Boolean coercion, unit interpretation, or access suitability decisions.
- Geometry status values are a closed domain; they are stored in the `geometry_status` column but are not themselves columns.

### `_OUTPUT_COLUMNS` — canonical or derived frame-column schema

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

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `road_feature_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 2 | `road_feature_type` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 3 | `source_provider` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 4 | `source_product` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 5 | `source_layer` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 6 | `source_feature_id` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 7 | `source_department_code` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 8 | `source_edition` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 9 | `source_product_version` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 10 | `source_download_timestamp` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 11 | `source_archive_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 12 | `source_url` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 13 | `nature_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 14 | `importance_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 15 | `fictitious_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 16 | `position_relative_to_ground_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 17 | `asset_status_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 18 | `lane_count_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 19 | `carriageway_width_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 20 | `private_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 21 | `traffic_direction_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 22 | `urban_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 23 | `mean_light_vehicle_speed_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 24 | `light_vehicle_access_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 25 | `closure_period_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 26 | `restriction_nature_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 27 | `restriction_height_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 28 | `restriction_total_weight_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 29 | `restriction_axle_weight_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 30 | `restriction_width_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 31 | `restriction_length_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 32 | `dangerous_goods_forbidden_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 33 | `administrative_classification_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 34 | `manager_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 35 | `source_name_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 36 | `source_identifiers_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 37 | `source_created_at` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 38 | `source_modified_at` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 39 | `source_confirmed_at` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 40 | `planimetric_acquisition_method` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 41 | `planimetric_precision_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 42 | `spatial_role` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 43 | `geometry_status` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | derived factual classification | Stores one value from its separately documented closed domain; domain values are not columns. |
| 44 | `geometry` | GeoPandas geometry dtype | nullable only where the owning geometry-status contract permits it | source/geometry fact | Active geometry; never an authorization or suitability result. |

### `_RAW_FIELD_MAPPING` — mapping between source/input and output keys or columns

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

| Source/input key or column | Target/output key or column | Contract |
|---|---|---|
| `nature` | `nature_raw` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `importance` | `importance_raw` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `fictif` | `fictitious_raw` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `position_par_rapport_au_sol` | `position_relative_to_ground_raw` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `etat_de_l_objet` | `asset_status_raw` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `nombre_de_voies` | `lane_count_raw` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `largeur_de_chaussee` | `carriageway_width_raw` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `prive` | `private_raw` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `sens_de_circulation` | `traffic_direction_raw` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `urbain` | `urban_raw` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `vitesse_moyenne_vl` | `mean_light_vehicle_speed_raw` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `acces_vehicule_leger` | `light_vehicle_access_raw` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `periode_de_fermeture` | `closure_period_raw` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `nature_de_la_restriction` | `restriction_nature_raw` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `restriction_de_hauteur` | `restriction_height_raw` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `restriction_de_poids_total` | `restriction_total_weight_raw` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `restriction_de_poids_par_essieu` | `restriction_axle_weight_raw` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `restriction_de_largeur` | `restriction_width_raw` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `restriction_de_longueur` | `restriction_length_raw` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `matieres_dangereuses_interdites` | `dangerous_goods_forbidden_raw` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `cpx_classement_administratif` | `administrative_classification_raw` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `cpx_gestionnaire` | `manager_raw` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `sources` | `source_name_raw` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `identifiants_sources` | `source_identifiers_raw` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `date_creation` | `source_created_at` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `date_modification` | `source_modified_at` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `date_de_confirmation` | `source_confirmed_at` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `methode_d_acquisition_planimetrique` | `planimetric_acquisition_method` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `precision_planimetrique` | `planimetric_precision_raw` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |

### `_REQUIRED_SOURCE_FIELDS` — required input frame fields (unordered when stored as a set)

```python
_REQUIRED_SOURCE_FIELDS = frozenset(
    {"cleabs", "geometry", *(source for source, _ in _RAW_FIELD_MAPPING)}
)
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `acces_vehicule_leger` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 2 | `cleabs` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 3 | `cpx_classement_administratif` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 4 | `cpx_gestionnaire` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 5 | `date_creation` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 6 | `date_de_confirmation` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 7 | `date_modification` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 8 | `etat_de_l_objet` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 9 | `fictif` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 10 | `geometry` | GeoPandas geometry dtype | nullable only where the owning geometry-status contract permits it | source/geometry fact | Active geometry; never an authorization or suitability result. |
| 11 | `identifiants_sources` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 12 | `importance` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 13 | `largeur_de_chaussee` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 14 | `matieres_dangereuses_interdites` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 15 | `methode_d_acquisition_planimetrique` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 16 | `nature` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 17 | `nature_de_la_restriction` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 18 | `nombre_de_voies` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 19 | `periode_de_fermeture` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 20 | `position_par_rapport_au_sol` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 21 | `precision_planimetrique` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 22 | `prive` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 23 | `restriction_de_hauteur` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 24 | `restriction_de_largeur` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 25 | `restriction_de_longueur` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 26 | `restriction_de_poids_par_essieu` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 27 | `restriction_de_poids_total` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 28 | `sens_de_circulation` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 29 | `sources` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 30 | `urbain` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 31 | `vitesse_moyenne_vl` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |


No enum/status/Literal value is classified as a column unless it is separately present in a canonical schema declaration. Mapping keys, JSON keys, dataclass fields, and configuration leaves remain distinct categories.

## 8. Interfaces

This module defines an exact `__all__` contract:

| Export | Kind | Origin | Included in `__all__` |
|---|---|---|---|
| `IgnRoadNormalizationError` | re-exported/defined Python symbol | `defined in `src/landscout/stages/normalize_access_ign.py`` | yes |
| `NormalizedIgnRoadData` | re-exported/defined Python symbol | `defined in `src/landscout/stages/normalize_access_ign.py`` | yes |
| `normalize_ign_roads` | re-exported/defined Python symbol | `defined in `src/landscout/stages/normalize_access_ign.py`` | yes |

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

The module contributes to the road flow through the exact facts, proxy evidence, policy results, diagnostics, or prechecks identified above.

## 15. Explicit non-goals

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

## 16. Tests

Test consumers and framework invocation are included in per-symbol interfaces. Test modules distinguish fixture injection from parameterized values and reproduce setup/action/assertion source.

## 17. Change impact

Any source-byte change invalidates the SHA above. Review exact exports, aliases, canonical frame schemas/dtypes, configured source/policy identities, callers, framework hooks, artifacts, and all linked tests before updating this companion.

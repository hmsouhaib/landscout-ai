# `src/landscout/stages/road_vehicle_proxy_policy.py`

## File identity

- Repository path: `src/landscout/stages/road_vehicle_proxy_policy.py`
- File type: Python source
- Layer: pipeline stage
- Domain: factual transformation, evidence, or policy boundary
- Responsibility: Loads and compiles the checked-in general-car/light-vehicle IGN road evidence policy.
- Source SHA256: `ae277b11b2d83bd82dfcf390757abc9bfc8e4aa8583c70ff3abe67512d78196d`

## 1. STEP 7F.1A.4 contract delta

- Uses strict duplicate-safe policy YAML and immutable compiled decision mappings without changing the approved road evidence policy.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Loads and compiles the checked-in general-car/light-vehicle IGN road evidence policy.

The file belongs to the **pipeline stage** layer and **factual transformation, evidence, or policy boundary** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `from collections.abc import Mapping`
- `from dataclasses import dataclass`
- `from hashlib import sha256`
- `from pathlib import Path`
- `from typing import Annotated, Literal, Self`

### Third-party packages

- `from pydantic import (
    AfterValidator,
    BaseModel,
    ConfigDict,
    Field,
    StrictFloat,
    StrictInt,
    StringConstraints,
    model_validator,
)`

### Internal LandScout imports

- `from landscout.common.strict_yaml import StrictYamlError, loads_strict_yaml`

## 4. Contract taxonomy

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `__all__`

- Category: explicit package/module export list.
- Exact declaration:

```python
__all__ = [
    "IgnRoadVehicleProxyPolicy",
    "IgnRoadVehicleProxyPolicyError",
    "load_ign_road_vehicle_proxy_policy",
]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `IgnRoadVehicleProxyPolicy`
  - `IgnRoadVehicleProxyPolicyError`
  - `load_ign_road_vehicle_proxy_policy`

### `_DEFAULT_POLICY_PATH`

- Category: module constant or closed domain.
- Exact declaration:

```python
_DEFAULT_POLICY_PATH = (
    Path(__file__).resolve().parents[3]
    / "configs"
    / "access"
    / "ign_bdtopo_vehicle_proxy_policy.yaml"
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_POLICY_ID`

- Category: module constant or closed domain.
- Exact declaration:

```python
_POLICY_ID = "ign_bdtopo_general_vehicle_proxy_v2"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_POLICY_SCOPE`

- Category: module constant or closed domain.
- Exact declaration:

```python
_POLICY_SCOPE = "OFFICIAL_IGN_CAR_ROUTING_EVIDENCE_ONLY"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_EXPECTED_PRECEDENCE`

- Category: module constant or closed domain.
- Exact declaration:

```python
_EXPECTED_PRECEDENCE = (
    "FICTITIOUS_GEOMETRY",
    "PROJECT_GEOMETRY_NOT_SIGNIFICANT",
    "NOT_IN_SERVICE",
    "PHYSICALLY_IMPOSSIBLE",
    "NON_GENERAL_VEHICLE_NATURE",
    "RIGHTS_RESTRICTED",
    "PRIVATE_ROAD",
    "TEMPORAL_CLOSURE",
    "KNOWN_RESTRICTION",
    "OTHER_RECORDED_RESTRICTION",
    "SPECIAL_NATURE",
    "LIMITED_NATURE",
    "IMPORTANCE_6",
    "NARROW_CARRIAGEWAY",
    "OPEN_OR_TOLL",
    "UNKNOWN",
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `FICTITIOUS_GEOMETRY`
  - `PROJECT_GEOMETRY_NOT_SIGNIFICANT`
  - `NOT_IN_SERVICE`
  - `PHYSICALLY_IMPOSSIBLE`
  - `NON_GENERAL_VEHICLE_NATURE`
  - `RIGHTS_RESTRICTED`
  - `PRIVATE_ROAD`
  - `TEMPORAL_CLOSURE`
  - `KNOWN_RESTRICTION`
  - `OTHER_RECORDED_RESTRICTION`
  - `SPECIAL_NATURE`
  - `LIMITED_NATURE`
  - `IMPORTANCE_6`
  - `NARROW_CARRIAGEWAY`
  - `OPEN_OR_TOLL`
  - `UNKNOWN`

### `_ExactString`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
_ExactString = Annotated[
    str,
    StringConstraints(strict=True, min_length=1),
    AfterValidator(_exact_string),
]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_NonEmptyStrings`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
_NonEmptyStrings = Annotated[tuple[_ExactString, ...], Field(min_length=1)]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

### `IgnRoadVehicleProxyPolicyError`

**Source purpose:** Raised when the IGN road vehicle-proxy policy is unsafe or invalid.

- Exact decorators: none.
- Exact bases: `ValueError`.

**Fields and model attributes**

No direct class/model/dataclass or `self` field assignment is declared.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyPolicy,
    IgnRoadVehicleProxyPolicyError,
    load_ign_road_vehicle_proxy_policy,
)`
- constructor call: `landscout.stages.road_vehicle_proxy_policy::load_ign_road_vehicle_proxy_policy` via `IgnRoadVehicleProxyPolicyError`
- value/type reference: `landscout.stages.road_vehicle_proxy_policy::load_ign_road_vehicle_proxy_policy` via `IgnRoadVehicleProxyPolicyError`
- import: `tests.unit.test_road_vehicle_proxy_policy::<module>` via `from landscout.stages.road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyPolicy,
    IgnRoadVehicleProxyPolicyError,
    load_ign_road_vehicle_proxy_policy,
)`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_duplicate_yaml_policy_key_is_rejected` via `IgnRoadVehicleProxyPolicyError`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_invalid_config_structure_is_rejected` via `IgnRoadVehicleProxyPolicyError`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_unsupported_schema_version_is_rejected` via `IgnRoadVehicleProxyPolicyError`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_wrong_policy_identity_is_rejected` via `IgnRoadVehicleProxyPolicyError`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_both_evidence_references_are_required` via `IgnRoadVehicleProxyPolicyError`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_product_reference_document_id_is_exact` via `IgnRoadVehicleProxyPolicyError`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_unknown_evidence_reference_is_rejected` via `IgnRoadVehicleProxyPolicyError`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_asset_state_group_overlap_is_rejected` via `IgnRoadVehicleProxyPolicyError`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_missing_known_asset_state_is_rejected` via `IgnRoadVehicleProxyPolicyError`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_unknown_additional_asset_state_is_rejected` via `IgnRoadVehicleProxyPolicyError`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_semantic_values_must_be_exact_non_empty_strings` via `IgnRoadVehicleProxyPolicyError`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_duplicate_semantic_value_is_rejected` via `IgnRoadVehicleProxyPolicyError`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_semantic_groups_must_be_pairwise_disjoint` via `IgnRoadVehicleProxyPolicyError`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_duplicate_known_restriction_is_rejected` via `IgnRoadVehicleProxyPolicyError`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_invalid_width_threshold_is_rejected` via `IgnRoadVehicleProxyPolicyError`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_importance_domains_must_be_exact` via `IgnRoadVehicleProxyPolicyError`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_decision_precedence_must_be_exact` via `IgnRoadVehicleProxyPolicyError`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_output_class_vocabulary_must_be_exact` via `IgnRoadVehicleProxyPolicyError`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_malformed_yaml_has_controlled_error` via `IgnRoadVehicleProxyPolicyError`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_non_mapping_yaml_has_controlled_error` via `IgnRoadVehicleProxyPolicyError`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_missing_file_has_controlled_error` via `IgnRoadVehicleProxyPolicyError`

**Exact class source**

```python
class IgnRoadVehicleProxyPolicyError(ValueError):
    """Raised when the IGN road vehicle-proxy policy is unsafe or invalid."""
```

### `_StrictPolicyModel`

**Source purpose:** Defines `_StrictPolicyModel`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class _StrictPolicyModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)
```

### `_NavigationReferenceConfig`

**Source purpose:** Defines `_NavigationReferenceConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictPolicyModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `publisher` | `Literal['IGN']` | `required` | `publisher: Literal["IGN"]` |
| `title` | `Literal['Calcul d’itinéraire']` | `required` | `title: Literal["Calcul d’itinéraire"]` |
| `revision` | `Literal['2026-05-27']` | `required` | `revision: Literal["2026-05-27"]` |
| `evidence_scope` | `Literal['GENERAL_CAR_ROUTING_RULES']` | `required` | `evidence_scope: Literal["GENERAL_CAR_ROUTING_RULES"]` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class _NavigationReferenceConfig(_StrictPolicyModel):
    publisher: Literal["IGN"]
    title: Literal["Calcul d’itinéraire"]
    revision: Literal["2026-05-27"]
    evidence_scope: Literal["GENERAL_CAR_ROUTING_RULES"]
```

### `_BdTopoProductReferenceConfig`

**Source purpose:** Defines `_BdTopoProductReferenceConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictPolicyModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `publisher` | `Literal['IGN']` | `required` | `publisher: Literal["IGN"]` |
| `title` | `Literal['BD TOPO® Version 3.5 - Descriptif de contenu']` | `required` | `title: Literal["BD TOPO® Version 3.5 - Descriptif de contenu"]` |
| `document_id` | `Literal['DC_BDTOPO_3-5']` | `required` | `document_id: Literal["DC_BDTOPO_3-5"]` |
| `revision` | `Literal['2025-11']` | `required` | `revision: Literal["2025-11"]` |
| `evidence_scope` | `Literal['SOURCE_ATTRIBUTE_SEMANTICS']` | `required` | `evidence_scope: Literal["SOURCE_ATTRIBUTE_SEMANTICS"]` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class _BdTopoProductReferenceConfig(_StrictPolicyModel):
    publisher: Literal["IGN"]
    title: Literal["BD TOPO® Version 3.5 - Descriptif de contenu"]
    document_id: Literal["DC_BDTOPO_3-5"]
    revision: Literal["2025-11"]
    evidence_scope: Literal["SOURCE_ATTRIBUTE_SEMANTICS"]
```

### `_ReferencesConfig`

**Source purpose:** Defines `_ReferencesConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictPolicyModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `navigation` | `_NavigationReferenceConfig` | `required` | `navigation: _NavigationReferenceConfig` |
| `bdtopo_product` | `_BdTopoProductReferenceConfig` | `required` | `bdtopo_product: _BdTopoProductReferenceConfig` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class _ReferencesConfig(_StrictPolicyModel):
    navigation: _NavigationReferenceConfig
    bdtopo_product: _BdTopoProductReferenceConfig
```

### `_ClassesConfig`

**Source purpose:** Defines `_ClassesConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictPolicyModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `general_vehicle_proxy` | `Literal['GENERAL_VEHICLE_PROXY']` | `required` | `general_vehicle_proxy: Literal["GENERAL_VEHICLE_PROXY"]` |
| `limited_vehicle_proxy` | `Literal['LIMITED_VEHICLE_PROXY']` | `required` | `limited_vehicle_proxy: Literal["LIMITED_VEHICLE_PROXY"]` |
| `restricted_review` | `Literal['RESTRICTED_REVIEW']` | `required` | `restricted_review: Literal["RESTRICTED_REVIEW"]` |
| `not_general_vehicle_proxy` | `Literal['NOT_GENERAL_VEHICLE_PROXY']` | `required` | `not_general_vehicle_proxy: Literal["NOT_GENERAL_VEHICLE_PROXY"]` |
| `not_distance_proxy` | `Literal['NOT_DISTANCE_PROXY']` | `required` | `not_distance_proxy: Literal["NOT_DISTANCE_PROXY"]` |
| `unknown_review` | `Literal['UNKNOWN_REVIEW']` | `required` | `unknown_review: Literal["UNKNOWN_REVIEW"]` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class _ClassesConfig(_StrictPolicyModel):
    general_vehicle_proxy: Literal["GENERAL_VEHICLE_PROXY"]
    limited_vehicle_proxy: Literal["LIMITED_VEHICLE_PROXY"]
    restricted_review: Literal["RESTRICTED_REVIEW"]
    not_general_vehicle_proxy: Literal["NOT_GENERAL_VEHICLE_PROXY"]
    not_distance_proxy: Literal["NOT_DISTANCE_PROXY"]
    unknown_review: Literal["UNKNOWN_REVIEW"]
```

### `_AssetStateConfig`

**Source purpose:** Defines `_AssetStateConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictPolicyModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `in_service` | `_NonEmptyStrings` | `required` | `in_service: _NonEmptyStrings` |
| `project_geometry_not_significant` | `_NonEmptyStrings` | `required` | `project_geometry_not_significant: _NonEmptyStrings` |
| `under_construction` | `_NonEmptyStrings` | `required` | `under_construction: _NonEmptyStrings` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class _AssetStateConfig(_StrictPolicyModel):
    in_service: _NonEmptyStrings
    project_geometry_not_significant: _NonEmptyStrings
    under_construction: _NonEmptyStrings

    @model_validator(mode="after")
    def _valid_groups(self) -> Self:
        groups = (
            self.in_service,
            self.project_geometry_not_significant,
            self.under_construction,
        )
        for name, values in zip(
            (
                "in_service",
                "project_geometry_not_significant",
                "under_construction",
            ),
            groups,
            strict=True,
        ):
            _require_unique(values, name)
        _require_disjoint(groups, "asset_state")
        if groups != (("En service",), ("En projet",), ("En construction",)):
            raise ValueError("asset_state groups must cover the exact source domain")
        return self
```

### `_LightVehicleAccessConfig`

**Source purpose:** Defines `_LightVehicleAccessConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictPolicyModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `open` | `_NonEmptyStrings` | `required` | `open: _NonEmptyStrings` |
| `toll` | `_NonEmptyStrings` | `required` | `toll: _NonEmptyStrings` |
| `rights_restricted` | `_NonEmptyStrings` | `required` | `rights_restricted: _NonEmptyStrings` |
| `physically_impossible` | `_NonEmptyStrings` | `required` | `physically_impossible: _NonEmptyStrings` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class _LightVehicleAccessConfig(_StrictPolicyModel):
    open: _NonEmptyStrings
    toll: _NonEmptyStrings
    rights_restricted: _NonEmptyStrings
    physically_impossible: _NonEmptyStrings

    @model_validator(mode="after")
    def _valid_groups(self) -> Self:
        groups = (
            self.open,
            self.toll,
            self.rights_restricted,
            self.physically_impossible,
        )
        for name, values in zip(
            ("open", "toll", "rights_restricted", "physically_impossible"),
            groups,
            strict=True,
        ):
            _require_unique(values, name)
        _require_disjoint(groups, "light_vehicle_access")
        return self
```

### `_RoadNatureConfig`

**Source purpose:** Defines `_RoadNatureConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictPolicyModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `general_motor_road` | `_NonEmptyStrings` | `required` | `general_motor_road: _NonEmptyStrings` |
| `limited_motor_proxy` | `_NonEmptyStrings` | `required` | `limited_motor_proxy: _NonEmptyStrings` |
| `non_general_vehicle` | `_NonEmptyStrings` | `required` | `non_general_vehicle: _NonEmptyStrings` |
| `special_review` | `_NonEmptyStrings` | `required` | `special_review: _NonEmptyStrings` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class _RoadNatureConfig(_StrictPolicyModel):
    general_motor_road: _NonEmptyStrings
    limited_motor_proxy: _NonEmptyStrings
    non_general_vehicle: _NonEmptyStrings
    special_review: _NonEmptyStrings

    @model_validator(mode="after")
    def _valid_groups(self) -> Self:
        groups = (
            self.general_motor_road,
            self.limited_motor_proxy,
            self.non_general_vehicle,
            self.special_review,
        )
        for name, values in zip(
            (
                "general_motor_road",
                "limited_motor_proxy",
                "non_general_vehicle",
                "special_review",
            ),
            groups,
            strict=True,
        ):
            _require_unique(values, name)
        _require_disjoint(groups, "nature")
        return self
```

### `_ImportanceConfig`

**Source purpose:** Defines `_ImportanceConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictPolicyModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `known` | `_NonEmptyStrings` | `required` | `known: _NonEmptyStrings` |
| `limited` | `_NonEmptyStrings` | `required` | `limited: _NonEmptyStrings` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class _ImportanceConfig(_StrictPolicyModel):
    known: _NonEmptyStrings
    limited: _NonEmptyStrings

    @model_validator(mode="after")
    def _valid_domain(self) -> Self:
        _require_unique(self.known, "importance.known")
        _require_unique(self.limited, "importance.limited")
        if self.known != ("1", "2", "3", "4", "5", "6"):
            raise ValueError("importance.known must cover exactly source values 1-6")
        if self.limited != ("6",):
            raise ValueError("importance.limited must contain exactly source value '6'")
        if not set(self.limited).issubset(self.known):
            raise ValueError("importance.limited must be a subset of importance.known")
        return self
```

### `_SourceValuesConfig`

**Source purpose:** Defines `_SourceValuesConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictPolicyModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `asset_state` | `_AssetStateConfig` | `required` | `asset_state: _AssetStateConfig` |
| `light_vehicle_access` | `_LightVehicleAccessConfig` | `required` | `light_vehicle_access: _LightVehicleAccessConfig` |
| `nature` | `_RoadNatureConfig` | `required` | `nature: _RoadNatureConfig` |
| `known_restriction_review` | `_NonEmptyStrings` | `required` | `known_restriction_review: _NonEmptyStrings` |
| `importance` | `_ImportanceConfig` | `required` | `importance: _ImportanceConfig` |
| `width_below_m` | `Annotated[StrictFloat, Field(gt=0, allow_inf_nan=False)]` | `required` | `width_below_m: Annotated[StrictFloat, Field(gt=0, allow_inf_nan=False)]` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class _SourceValuesConfig(_StrictPolicyModel):
    asset_state: _AssetStateConfig
    light_vehicle_access: _LightVehicleAccessConfig
    nature: _RoadNatureConfig
    known_restriction_review: _NonEmptyStrings
    importance: _ImportanceConfig
    width_below_m: Annotated[StrictFloat, Field(gt=0, allow_inf_nan=False)]

    @model_validator(mode="after")
    def _valid_values(self) -> Self:
        _require_unique(self.known_restriction_review, "known_restriction_review")
        return self
```

### `_DecisionOutcomesConfig`

**Source purpose:** Defines `_DecisionOutcomesConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictPolicyModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `fictitious_geometry` | `Literal['NOT_DISTANCE_PROXY']` | `required` | `fictitious_geometry: Literal["NOT_DISTANCE_PROXY"]` |
| `project_geometry_not_significant` | `Literal['NOT_DISTANCE_PROXY']` | `required` | `project_geometry_not_significant: Literal["NOT_DISTANCE_PROXY"]` |
| `not_in_service` | `Literal['NOT_GENERAL_VEHICLE_PROXY']` | `required` | `not_in_service: Literal["NOT_GENERAL_VEHICLE_PROXY"]` |
| `physically_impossible` | `Literal['NOT_GENERAL_VEHICLE_PROXY']` | `required` | `physically_impossible: Literal["NOT_GENERAL_VEHICLE_PROXY"]` |
| `non_general_vehicle_nature` | `Literal['NOT_GENERAL_VEHICLE_PROXY']` | `required` | `non_general_vehicle_nature: Literal["NOT_GENERAL_VEHICLE_PROXY"]` |
| `rights_restricted` | `Literal['RESTRICTED_REVIEW']` | `required` | `rights_restricted: Literal["RESTRICTED_REVIEW"]` |
| `private_road` | `Literal['RESTRICTED_REVIEW']` | `required` | `private_road: Literal["RESTRICTED_REVIEW"]` |
| `temporal_closure` | `Literal['RESTRICTED_REVIEW']` | `required` | `temporal_closure: Literal["RESTRICTED_REVIEW"]` |
| `known_restriction` | `Literal['RESTRICTED_REVIEW']` | `required` | `known_restriction: Literal["RESTRICTED_REVIEW"]` |
| `other_recorded_restriction` | `Literal['RESTRICTED_REVIEW']` | `required` | `other_recorded_restriction: Literal["RESTRICTED_REVIEW"]` |
| `special_nature` | `Literal['RESTRICTED_REVIEW']` | `required` | `special_nature: Literal["RESTRICTED_REVIEW"]` |
| `limited_nature` | `Literal['LIMITED_VEHICLE_PROXY']` | `required` | `limited_nature: Literal["LIMITED_VEHICLE_PROXY"]` |
| `importance_6` | `Literal['LIMITED_VEHICLE_PROXY']` | `required` | `importance_6: Literal["LIMITED_VEHICLE_PROXY"]` |
| `narrow_carriageway` | `Literal['LIMITED_VEHICLE_PROXY']` | `required` | `narrow_carriageway: Literal["LIMITED_VEHICLE_PROXY"]` |
| `open_or_toll` | `Literal['GENERAL_VEHICLE_PROXY']` | `required` | `open_or_toll: Literal["GENERAL_VEHICLE_PROXY"]` |
| `unknown` | `Literal['UNKNOWN_REVIEW']` | `required` | `unknown: Literal["UNKNOWN_REVIEW"]` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class _DecisionOutcomesConfig(_StrictPolicyModel):
    fictitious_geometry: Literal["NOT_DISTANCE_PROXY"]
    project_geometry_not_significant: Literal["NOT_DISTANCE_PROXY"]
    not_in_service: Literal["NOT_GENERAL_VEHICLE_PROXY"]
    physically_impossible: Literal["NOT_GENERAL_VEHICLE_PROXY"]
    non_general_vehicle_nature: Literal["NOT_GENERAL_VEHICLE_PROXY"]
    rights_restricted: Literal["RESTRICTED_REVIEW"]
    private_road: Literal["RESTRICTED_REVIEW"]
    temporal_closure: Literal["RESTRICTED_REVIEW"]
    known_restriction: Literal["RESTRICTED_REVIEW"]
    other_recorded_restriction: Literal["RESTRICTED_REVIEW"]
    special_nature: Literal["RESTRICTED_REVIEW"]
    limited_nature: Literal["LIMITED_VEHICLE_PROXY"]
    importance_6: Literal["LIMITED_VEHICLE_PROXY"]
    narrow_carriageway: Literal["LIMITED_VEHICLE_PROXY"]
    open_or_toll: Literal["GENERAL_VEHICLE_PROXY"]
    unknown: Literal["UNKNOWN_REVIEW"]
```

### `_PolicyConfig`

**Source purpose:** Defines `_PolicyConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictPolicyModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `policy_id` | `_ExactString` | `required` | `policy_id: _ExactString` |
| `schema_version` | `StrictInt` | `required` | `schema_version: StrictInt` |
| `scope` | `_ExactString` | `required` | `scope: _ExactString` |
| `references` | `_ReferencesConfig` | `required` | `references: _ReferencesConfig` |
| `evidence_checked_on` | `Literal['2026-08-16']` | `required` | `evidence_checked_on: Literal["2026-08-16"]` |
| `vehicle_scope` | `Literal['LIGHT_VEHICLE_AND_GENERAL_CAR_NETWORK']` | `required` | `vehicle_scope: Literal["LIGHT_VEHICLE_AND_GENERAL_CAR_NETWORK"]` |
| `heavy_vehicle_access` | `Literal['NOT_PROVEN']` | `required` | `heavy_vehicle_access: Literal["NOT_PROVEN"]` |
| `classes` | `_ClassesConfig` | `required` | `classes: _ClassesConfig` |
| `source_values` | `_SourceValuesConfig` | `required` | `source_values: _SourceValuesConfig` |
| `decision_precedence` | `_NonEmptyStrings` | `required` | `decision_precedence: _NonEmptyStrings` |
| `decision_outcomes` | `_DecisionOutcomesConfig` | `required` | `decision_outcomes: _DecisionOutcomesConfig` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- value/type reference: `landscout.stages.road_vehicle_proxy_policy::_compile_policy` via `_PolicyConfig`
- value/type reference: `landscout.stages.road_vehicle_proxy_policy::load_ign_road_vehicle_proxy_policy` via `_PolicyConfig`

**Exact class source**

```python
class _PolicyConfig(_StrictPolicyModel):
    policy_id: _ExactString
    schema_version: StrictInt
    scope: _ExactString
    references: _ReferencesConfig
    evidence_checked_on: Literal["2026-08-16"]
    vehicle_scope: Literal["LIGHT_VEHICLE_AND_GENERAL_CAR_NETWORK"]
    heavy_vehicle_access: Literal["NOT_PROVEN"]
    classes: _ClassesConfig
    source_values: _SourceValuesConfig
    decision_precedence: _NonEmptyStrings
    decision_outcomes: _DecisionOutcomesConfig

    @model_validator(mode="after")
    def _valid_identity_and_precedence(self) -> Self:
        if self.policy_id != _POLICY_ID:
            raise ValueError("policy_id is not the approved v2 policy identity")
        if self.schema_version != 2:
            raise ValueError("schema_version must be exactly 2")
        if self.scope != _POLICY_SCOPE:
            raise ValueError("scope is not the approved official IGN evidence scope")
        if self.decision_precedence != _EXPECTED_PRECEDENCE:
            raise ValueError("decision_precedence differs from approved v2 order")
        return self
```

### `_CompiledClasses`

**Source purpose:** Defines `_CompiledClasses`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `general_vehicle_proxy` | `str` | `required` | `general_vehicle_proxy: str` |
| `limited_vehicle_proxy` | `str` | `required` | `limited_vehicle_proxy: str` |
| `restricted_review` | `str` | `required` | `restricted_review: str` |
| `not_general_vehicle_proxy` | `str` | `required` | `not_general_vehicle_proxy: str` |
| `not_distance_proxy` | `str` | `required` | `not_distance_proxy: str` |
| `unknown_review` | `str` | `required` | `unknown_review: str` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- constructor call: `landscout.stages.road_vehicle_proxy_policy::_compile_policy` via `_CompiledClasses`
- value/type reference: `landscout.stages.road_vehicle_proxy_policy::_compile_policy` via `_CompiledClasses`

**Exact class source**

```python
class _CompiledClasses:
    general_vehicle_proxy: str
    limited_vehicle_proxy: str
    restricted_review: str
    not_general_vehicle_proxy: str
    not_distance_proxy: str
    unknown_review: str

    @property
    def values(self) -> tuple[str, ...]:
        return (
            self.general_vehicle_proxy,
            self.limited_vehicle_proxy,
            self.restricted_review,
            self.not_general_vehicle_proxy,
            self.not_distance_proxy,
            self.unknown_review,
        )
```

### `_CompiledAssetState`

**Source purpose:** Defines `_CompiledAssetState`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `in_service` | `frozenset[str]` | `required` | `in_service: frozenset[str]` |
| `project_geometry_not_significant` | `frozenset[str]` | `required` | `project_geometry_not_significant: frozenset[str]` |
| `under_construction` | `frozenset[str]` | `required` | `under_construction: frozenset[str]` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- constructor call: `landscout.stages.road_vehicle_proxy_policy::_compile_policy` via `_CompiledAssetState`
- value/type reference: `landscout.stages.road_vehicle_proxy_policy::_compile_policy` via `_CompiledAssetState`

**Exact class source**

```python
class _CompiledAssetState:
    in_service: frozenset[str]
    project_geometry_not_significant: frozenset[str]
    under_construction: frozenset[str]
```

### `_CompiledNavigationReference`

**Source purpose:** Defines `_CompiledNavigationReference`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `publisher` | `str` | `required` | `publisher: str` |
| `title` | `str` | `required` | `title: str` |
| `revision` | `str` | `required` | `revision: str` |
| `evidence_scope` | `str` | `required` | `evidence_scope: str` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- constructor call: `landscout.stages.road_vehicle_proxy_policy::_compile_policy` via `_CompiledNavigationReference`
- value/type reference: `landscout.stages.road_vehicle_proxy_policy::_compile_policy` via `_CompiledNavigationReference`

**Exact class source**

```python
class _CompiledNavigationReference:
    publisher: str
    title: str
    revision: str
    evidence_scope: str
```

### `_CompiledBdTopoProductReference`

**Source purpose:** Defines `_CompiledBdTopoProductReference`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `publisher` | `str` | `required` | `publisher: str` |
| `title` | `str` | `required` | `title: str` |
| `document_id` | `str` | `required` | `document_id: str` |
| `revision` | `str` | `required` | `revision: str` |
| `evidence_scope` | `str` | `required` | `evidence_scope: str` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- constructor call: `landscout.stages.road_vehicle_proxy_policy::_compile_policy` via `_CompiledBdTopoProductReference`
- value/type reference: `landscout.stages.road_vehicle_proxy_policy::_compile_policy` via `_CompiledBdTopoProductReference`

**Exact class source**

```python
class _CompiledBdTopoProductReference:
    publisher: str
    title: str
    document_id: str
    revision: str
    evidence_scope: str
```

### `_CompiledLightVehicleAccess`

**Source purpose:** Defines `_CompiledLightVehicleAccess`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `open` | `frozenset[str]` | `required` | `open: frozenset[str]` |
| `toll` | `frozenset[str]` | `required` | `toll: frozenset[str]` |
| `rights_restricted` | `frozenset[str]` | `required` | `rights_restricted: frozenset[str]` |
| `physically_impossible` | `frozenset[str]` | `required` | `physically_impossible: frozenset[str]` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- constructor call: `landscout.stages.road_vehicle_proxy_policy::_compile_policy` via `_CompiledLightVehicleAccess`
- value/type reference: `landscout.stages.road_vehicle_proxy_policy::_compile_policy` via `_CompiledLightVehicleAccess`

**Exact class source**

```python
class _CompiledLightVehicleAccess:
    open: frozenset[str]
    toll: frozenset[str]
    rights_restricted: frozenset[str]
    physically_impossible: frozenset[str]
```

### `_CompiledRoadNature`

**Source purpose:** Defines `_CompiledRoadNature`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `general_motor_road` | `frozenset[str]` | `required` | `general_motor_road: frozenset[str]` |
| `limited_motor_proxy` | `frozenset[str]` | `required` | `limited_motor_proxy: frozenset[str]` |
| `non_general_vehicle` | `frozenset[str]` | `required` | `non_general_vehicle: frozenset[str]` |
| `special_review` | `frozenset[str]` | `required` | `special_review: frozenset[str]` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- constructor call: `landscout.stages.road_vehicle_proxy_policy::_compile_policy` via `_CompiledRoadNature`
- value/type reference: `landscout.stages.road_vehicle_proxy_policy::_compile_policy` via `_CompiledRoadNature`

**Exact class source**

```python
class _CompiledRoadNature:
    general_motor_road: frozenset[str]
    limited_motor_proxy: frozenset[str]
    non_general_vehicle: frozenset[str]
    special_review: frozenset[str]
```

### `_CompiledImportance`

**Source purpose:** Defines `_CompiledImportance`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `known` | `frozenset[str]` | `required` | `known: frozenset[str]` |
| `limited` | `frozenset[str]` | `required` | `limited: frozenset[str]` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- constructor call: `landscout.stages.road_vehicle_proxy_policy::_compile_policy` via `_CompiledImportance`
- value/type reference: `landscout.stages.road_vehicle_proxy_policy::_compile_policy` via `_CompiledImportance`

**Exact class source**

```python
class _CompiledImportance:
    known: frozenset[str]
    limited: frozenset[str]
```

### `_CompiledDecisionOutcomes`

**Source purpose:** Defines `_CompiledDecisionOutcomes`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `fictitious_geometry` | `str` | `required` | `fictitious_geometry: str` |
| `project_geometry_not_significant` | `str` | `required` | `project_geometry_not_significant: str` |
| `not_in_service` | `str` | `required` | `not_in_service: str` |
| `physically_impossible` | `str` | `required` | `physically_impossible: str` |
| `non_general_vehicle_nature` | `str` | `required` | `non_general_vehicle_nature: str` |
| `rights_restricted` | `str` | `required` | `rights_restricted: str` |
| `private_road` | `str` | `required` | `private_road: str` |
| `temporal_closure` | `str` | `required` | `temporal_closure: str` |
| `known_restriction` | `str` | `required` | `known_restriction: str` |
| `other_recorded_restriction` | `str` | `required` | `other_recorded_restriction: str` |
| `special_nature` | `str` | `required` | `special_nature: str` |
| `limited_nature` | `str` | `required` | `limited_nature: str` |
| `importance_6` | `str` | `required` | `importance_6: str` |
| `narrow_carriageway` | `str` | `required` | `narrow_carriageway: str` |
| `open_or_toll` | `str` | `required` | `open_or_toll: str` |
| `unknown` | `str` | `required` | `unknown: str` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- constructor call: `landscout.stages.road_vehicle_proxy_policy::_compile_policy` via `_CompiledDecisionOutcomes`
- value/type reference: `landscout.stages.road_vehicle_proxy_policy::_compile_policy` via `_CompiledDecisionOutcomes`

**Exact class source**

```python
class _CompiledDecisionOutcomes:
    fictitious_geometry: str
    project_geometry_not_significant: str
    not_in_service: str
    physically_impossible: str
    non_general_vehicle_nature: str
    rights_restricted: str
    private_road: str
    temporal_closure: str
    known_restriction: str
    other_recorded_restriction: str
    special_nature: str
    limited_nature: str
    importance_6: str
    narrow_carriageway: str
    open_or_toll: str
    unknown: str
```

### `IgnRoadVehicleProxyPolicy`

**Source purpose:** Immutable policy evidence compiled from the exact checked-in YAML bytes.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `policy_id` | `str` | `required` | `policy_id: str` |
| `schema_version` | `int` | `required` | `schema_version: int` |
| `scope` | `str` | `required` | `scope: str` |
| `navigation_reference` | `_CompiledNavigationReference` | `required` | `navigation_reference: _CompiledNavigationReference` |
| `bdtopo_product_reference` | `_CompiledBdTopoProductReference` | `required` | `bdtopo_product_reference: _CompiledBdTopoProductReference` |
| `evidence_checked_on` | `str` | `required` | `evidence_checked_on: str` |
| `vehicle_scope` | `str` | `required` | `vehicle_scope: str` |
| `heavy_vehicle_access` | `str` | `required` | `heavy_vehicle_access: str` |
| `classes` | `_CompiledClasses` | `required` | `classes: _CompiledClasses` |
| `asset_state` | `_CompiledAssetState` | `required` | `asset_state: _CompiledAssetState` |
| `light_vehicle_access` | `_CompiledLightVehicleAccess` | `required` | `light_vehicle_access: _CompiledLightVehicleAccess` |
| `nature` | `_CompiledRoadNature` | `required` | `nature: _CompiledRoadNature` |
| `known_restriction_review` | `frozenset[str]` | `required` | `known_restriction_review: frozenset[str]` |
| `importance` | `_CompiledImportance` | `required` | `importance: _CompiledImportance` |
| `width_below_m` | `float` | `required` | `width_below_m: float` |
| `decision_precedence` | `tuple[str, ...]` | `required` | `decision_precedence: tuple[str, ...]` |
| `decision_outcomes` | `_CompiledDecisionOutcomes` | `required` | `decision_outcomes: _CompiledDecisionOutcomes` |
| `config_sha256` | `str` | `required` | `config_sha256: str` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyPolicy,
    IgnRoadVehicleProxyPolicyError,
    load_ign_road_vehicle_proxy_policy,
)`
- import: `landscout.stages.apply_road_vehicle_proxy_policy::<module>` via `from landscout.stages.road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyPolicy,
    load_ign_road_vehicle_proxy_policy,
)`
- value/type reference: `landscout.stages.apply_road_vehicle_proxy_policy::_rule_outcomes` via `IgnRoadVehicleProxyPolicy`
- value/type reference: `landscout.stages.apply_road_vehicle_proxy_policy::_classify_road_frame` via `IgnRoadVehicleProxyPolicy`
- import: `landscout.stages.assess_road_proximity_coverage::<module>` via `from landscout.stages.road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyPolicy,
    load_ign_road_vehicle_proxy_policy,
)`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_validate_class_coverage` via `IgnRoadVehicleProxyPolicy`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_validate_upstream_result` via `IgnRoadVehicleProxyPolicy`
- import: `landscout.stages.enrich_road_proximity::<module>` via `from landscout.stages.road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyPolicy,
    load_ign_road_vehicle_proxy_policy,
)`
- value/type reference: `landscout.stages.enrich_road_proximity::_policy_classes` via `IgnRoadVehicleProxyPolicy`
- value/type reference: `landscout.stages.enrich_road_proximity::_require_row_lineage` via `IgnRoadVehicleProxyPolicy`
- value/type reference: `landscout.stages.enrich_road_proximity::_validate_application_roads` via `IgnRoadVehicleProxyPolicy`
- value/type reference: `landscout.stages.enrich_road_proximity::_coverage` via `IgnRoadVehicleProxyPolicy`
- value/type reference: `landscout.stages.enrich_road_proximity::_class_proximity_table` via `IgnRoadVehicleProxyPolicy`
- value/type reference: `landscout.stages.enrich_road_proximity::_validate_coverage` via `IgnRoadVehicleProxyPolicy`
- value/type reference: `landscout.stages.enrich_road_proximity::_validate_result` via `IgnRoadVehicleProxyPolicy`
- constructor call: `landscout.stages.road_vehicle_proxy_policy::_compile_policy` via `IgnRoadVehicleProxyPolicy`
- value/type reference: `landscout.stages.road_vehicle_proxy_policy::_compile_policy` via `IgnRoadVehicleProxyPolicy`
- value/type reference: `landscout.stages.road_vehicle_proxy_policy::load_ign_road_vehicle_proxy_policy` via `IgnRoadVehicleProxyPolicy`
- import: `tests.unit.test_road_vehicle_proxy_policy::<module>` via `from landscout.stages.road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyPolicy,
    IgnRoadVehicleProxyPolicyError,
    load_ign_road_vehicle_proxy_policy,
)`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::_load_payload` via `IgnRoadVehicleProxyPolicy`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_checked_in_policy_loads_with_exact_public_identity_and_reference` via `IgnRoadVehicleProxyPolicy`

**Exact class source**

```python
class IgnRoadVehicleProxyPolicy:
    """Immutable policy evidence compiled from the exact checked-in YAML bytes."""

    policy_id: str
    schema_version: int
    scope: str
    navigation_reference: _CompiledNavigationReference
    bdtopo_product_reference: _CompiledBdTopoProductReference
    evidence_checked_on: str
    vehicle_scope: str
    heavy_vehicle_access: str
    classes: _CompiledClasses
    asset_state: _CompiledAssetState
    light_vehicle_access: _CompiledLightVehicleAccess
    nature: _CompiledRoadNature
    known_restriction_review: frozenset[str]
    importance: _CompiledImportance
    width_below_m: float
    decision_precedence: tuple[str, ...]
    decision_outcomes: _CompiledDecisionOutcomes
    config_sha256: str
```


## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `_exact_string`

**Purpose:** Implements `exact string` within the file role: Loads and compiles the checked-in general-car/light-vehicle IGN road evidence policy.

**Exact signature**

```python
def _exact_string(value: str) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `value`
- Explicit raise paths:
  - `ValueError("policy strings must not contain edge whitespace")` under lexical guard `value != value.strip()`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `value.strip` | `unresolved local/third-party receiver; no ownership inferred` |
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
def _exact_string(value: str) -> str:
    if value != value.strip():
        raise ValueError("policy strings must not contain edge whitespace")
    return value
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_require_unique`

**Purpose:** Implements `require unique` within the file role: Loads and compiles the checked-in general-car/light-vehicle IGN road evidence policy.

**Exact signature**

```python
def _require_unique(values: tuple[str, ...], label: str) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `values` | positional-or-keyword | `tuple[str, ...]` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `ValueError(f"{label} contains duplicate source values")` under lexical guard `len(values) != len(set(values))`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.road_vehicle_proxy_policy::_AssetStateConfig._valid_groups` via `_require_unique`
- value/type reference: `landscout.stages.road_vehicle_proxy_policy::_AssetStateConfig._valid_groups` via `_require_unique`
- direct call: `landscout.stages.road_vehicle_proxy_policy::_LightVehicleAccessConfig._valid_groups` via `_require_unique`
- value/type reference: `landscout.stages.road_vehicle_proxy_policy::_LightVehicleAccessConfig._valid_groups` via `_require_unique`
- direct call: `landscout.stages.road_vehicle_proxy_policy::_RoadNatureConfig._valid_groups` via `_require_unique`
- value/type reference: `landscout.stages.road_vehicle_proxy_policy::_RoadNatureConfig._valid_groups` via `_require_unique`
- direct call: `landscout.stages.road_vehicle_proxy_policy::_ImportanceConfig._valid_domain` via `_require_unique`
- value/type reference: `landscout.stages.road_vehicle_proxy_policy::_ImportanceConfig._valid_domain` via `_require_unique`
- direct call: `landscout.stages.road_vehicle_proxy_policy::_SourceValuesConfig._valid_values` via `_require_unique`
- value/type reference: `landscout.stages.road_vehicle_proxy_policy::_SourceValuesConfig._valid_values` via `_require_unique`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
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
def _require_unique(values: tuple[str, ...], label: str) -> None:
    if len(values) != len(set(values)):
        raise ValueError(f"{label} contains duplicate source values")
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_require_disjoint`

**Purpose:** Implements `require disjoint` within the file role: Loads and compiles the checked-in general-car/light-vehicle IGN road evidence policy.

**Exact signature**

```python
def _require_disjoint(groups: tuple[tuple[str, ...], ...], label: str) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `groups` | positional-or-keyword | `tuple[tuple[str, ...], ...]` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `ValueError(f"{label} source groups overlap")` under lexical guard `len(flattened) != len(set(flattened))`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.road_vehicle_proxy_policy::_AssetStateConfig._valid_groups` via `_require_disjoint`
- value/type reference: `landscout.stages.road_vehicle_proxy_policy::_AssetStateConfig._valid_groups` via `_require_disjoint`
- direct call: `landscout.stages.road_vehicle_proxy_policy::_LightVehicleAccessConfig._valid_groups` via `_require_disjoint`
- value/type reference: `landscout.stages.road_vehicle_proxy_policy::_LightVehicleAccessConfig._valid_groups` via `_require_disjoint`
- direct call: `landscout.stages.road_vehicle_proxy_policy::_RoadNatureConfig._valid_groups` via `_require_disjoint`
- value/type reference: `landscout.stages.road_vehicle_proxy_policy::_RoadNatureConfig._valid_groups` via `_require_disjoint`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
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
def _require_disjoint(groups: tuple[tuple[str, ...], ...], label: str) -> None:
    flattened = tuple(value for group in groups for value in group)
    if len(flattened) != len(set(flattened)):
        raise ValueError(f"{label} source groups overlap")
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_AssetStateConfig._valid_groups`

**Purpose:** Implements `valid groups` within the file role: Loads and compiles the checked-in general-car/light-vehicle IGN road evidence policy.

**Exact signature**

```python
def _valid_groups(self) -> Self:
```

- Exact decorators: `model_validator(mode="after")`.
- Declared return annotation: `Self`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `self`
- Explicit raise paths:
  - `ValueError("asset_state groups must cover the exact source domain")` under lexical guard `groups != (("En service",), ("En projet",), ("En construction",))`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `zip` | `unresolved local/third-party receiver; no ownership inferred` |
| `_require_unique` | `landscout.stages.road_vehicle_proxy_policy._require_unique` |
| `_require_disjoint` | `landscout.stages.road_vehicle_proxy_policy._require_disjoint` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `model_validator` | `pydantic.model_validator` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `_require_disjoint` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _valid_groups(self) -> Self:
        groups = (
            self.in_service,
            self.project_geometry_not_significant,
            self.under_construction,
        )
        for name, values in zip(
            (
                "in_service",
                "project_geometry_not_significant",
                "under_construction",
            ),
            groups,
            strict=True,
        ):
            _require_unique(values, name)
        _require_disjoint(groups, "asset_state")
        if groups != (("En service",), ("En projet",), ("En construction",)):
            raise ValueError("asset_state groups must cover the exact source domain")
        return self
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_LightVehicleAccessConfig._valid_groups`

**Purpose:** Implements `valid groups` within the file role: Loads and compiles the checked-in general-car/light-vehicle IGN road evidence policy.

**Exact signature**

```python
def _valid_groups(self) -> Self:
```

- Exact decorators: `model_validator(mode="after")`.
- Declared return annotation: `Self`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `self`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `zip` | `unresolved local/third-party receiver; no ownership inferred` |
| `_require_unique` | `landscout.stages.road_vehicle_proxy_policy._require_unique` |
| `_require_disjoint` | `landscout.stages.road_vehicle_proxy_policy._require_disjoint` |
| `model_validator` | `pydantic.model_validator` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `_require_disjoint` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _valid_groups(self) -> Self:
        groups = (
            self.open,
            self.toll,
            self.rights_restricted,
            self.physically_impossible,
        )
        for name, values in zip(
            ("open", "toll", "rights_restricted", "physically_impossible"),
            groups,
            strict=True,
        ):
            _require_unique(values, name)
        _require_disjoint(groups, "light_vehicle_access")
        return self
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_RoadNatureConfig._valid_groups`

**Purpose:** Implements `valid groups` within the file role: Loads and compiles the checked-in general-car/light-vehicle IGN road evidence policy.

**Exact signature**

```python
def _valid_groups(self) -> Self:
```

- Exact decorators: `model_validator(mode="after")`.
- Declared return annotation: `Self`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `self`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `zip` | `unresolved local/third-party receiver; no ownership inferred` |
| `_require_unique` | `landscout.stages.road_vehicle_proxy_policy._require_unique` |
| `_require_disjoint` | `landscout.stages.road_vehicle_proxy_policy._require_disjoint` |
| `model_validator` | `pydantic.model_validator` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `_require_disjoint` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _valid_groups(self) -> Self:
        groups = (
            self.general_motor_road,
            self.limited_motor_proxy,
            self.non_general_vehicle,
            self.special_review,
        )
        for name, values in zip(
            (
                "general_motor_road",
                "limited_motor_proxy",
                "non_general_vehicle",
                "special_review",
            ),
            groups,
            strict=True,
        ):
            _require_unique(values, name)
        _require_disjoint(groups, "nature")
        return self
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_ImportanceConfig._valid_domain`

**Purpose:** Implements `valid domain` within the file role: Loads and compiles the checked-in general-car/light-vehicle IGN road evidence policy.

**Exact signature**

```python
def _valid_domain(self) -> Self:
```

- Exact decorators: `model_validator(mode="after")`.
- Declared return annotation: `Self`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `self`
- Explicit raise paths:
  - `ValueError("importance.known must cover exactly source values 1-6")` under lexical guard `self.known != ("1", "2", "3", "4", "5", "6")`.
  - `ValueError("importance.limited must contain exactly source value '6'")` under lexical guard `self.limited != ("6",)`.
  - `ValueError("importance.limited must be a subset of importance.known")` under lexical guard `not set(self.limited).issubset(self.known)`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_require_unique` | `landscout.stages.road_vehicle_proxy_policy._require_unique` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `set(self.limited).issubset` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `model_validator` | `pydantic.model_validator` |

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
def _valid_domain(self) -> Self:
        _require_unique(self.known, "importance.known")
        _require_unique(self.limited, "importance.limited")
        if self.known != ("1", "2", "3", "4", "5", "6"):
            raise ValueError("importance.known must cover exactly source values 1-6")
        if self.limited != ("6",):
            raise ValueError("importance.limited must contain exactly source value '6'")
        if not set(self.limited).issubset(self.known):
            raise ValueError("importance.limited must be a subset of importance.known")
        return self
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_SourceValuesConfig._valid_values`

**Purpose:** Implements `valid values` within the file role: Loads and compiles the checked-in general-car/light-vehicle IGN road evidence policy.

**Exact signature**

```python
def _valid_values(self) -> Self:
```

- Exact decorators: `model_validator(mode="after")`.
- Declared return annotation: `Self`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `self`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_require_unique` | `landscout.stages.road_vehicle_proxy_policy._require_unique` |
| `model_validator` | `pydantic.model_validator` |

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
def _valid_values(self) -> Self:
        _require_unique(self.known_restriction_review, "known_restriction_review")
        return self
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_PolicyConfig._valid_identity_and_precedence`

**Purpose:** Implements `valid identity and precedence` within the file role: Loads and compiles the checked-in general-car/light-vehicle IGN road evidence policy.

**Exact signature**

```python
def _valid_identity_and_precedence(self) -> Self:
```

- Exact decorators: `model_validator(mode="after")`.
- Declared return annotation: `Self`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `self`
- Explicit raise paths:
  - `ValueError("policy_id is not the approved v2 policy identity")` under lexical guard `self.policy_id != _POLICY_ID`.
  - `ValueError("schema_version must be exactly 2")` under lexical guard `self.schema_version != 2`.
  - `ValueError("scope is not the approved official IGN evidence scope")` under lexical guard `self.scope != _POLICY_SCOPE`.
  - `ValueError("decision_precedence differs from approved v2 order")` under lexical guard `self.decision_precedence != _EXPECTED_PRECEDENCE`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `model_validator` | `pydantic.model_validator` |

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
def _valid_identity_and_precedence(self) -> Self:
        if self.policy_id != _POLICY_ID:
            raise ValueError("policy_id is not the approved v2 policy identity")
        if self.schema_version != 2:
            raise ValueError("schema_version must be exactly 2")
        if self.scope != _POLICY_SCOPE:
            raise ValueError("scope is not the approved official IGN evidence scope")
        if self.decision_precedence != _EXPECTED_PRECEDENCE:
            raise ValueError("decision_precedence differs from approved v2 order")
        return self
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_CompiledClasses.values`

**Purpose:** Implements `values` within the file role: Loads and compiles the checked-in general-car/light-vehicle IGN road evidence policy.

**Exact signature**

```python
def values(self) -> tuple[str, ...]:
```

- Exact decorators: `property`.
- Declared return annotation: `tuple[str, ...]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `(<br>            self.general_vehicle_proxy,<br>            self.limited_vehicle_proxy,<br>            self.restricted_review,<br>            self.not_general_vehicle_proxy,<br>            self.not_distance_proxy,<br>            self.unknown_review,<br>        )`
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
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def values(self) -> tuple[str, ...]:
        return (
            self.general_vehicle_proxy,
            self.limited_vehicle_proxy,
            self.restricted_review,
            self.not_general_vehicle_proxy,
            self.not_distance_proxy,
            self.unknown_review,
        )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_compile_policy`

**Purpose:** Implements `compile policy` within the file role: Loads and compiles the checked-in general-car/light-vehicle IGN road evidence policy.

**Exact signature**

```python
def _compile_policy(
    config: _PolicyConfig,
    config_sha256: str,
) -> IgnRoadVehicleProxyPolicy:
```

- Exact decorators: none.
- Declared return annotation: `IgnRoadVehicleProxyPolicy`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `config` | positional-or-keyword | `_PolicyConfig` | `required` |
| `config_sha256` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `IgnRoadVehicleProxyPolicy(<br>        policy_id=config.policy_id,<br>        schema_version=config.schema_version,<br>        scope=config.scope,<br>        navigation_reference=_CompiledNavigationReference(<br>            publisher=config.references.navigation.publisher,<br>            title=config.references.navigation.title,<br>            revision=config.references.navigation.revision,<br>            evidence_scope=config.references.navigation.evidence_scope,<br>        ),<br>        bdtopo_product_reference=_CompiledBdTopoProductReference(<br>            publisher=config.references.bdtopo_product.publisher,<br>            title=config.references.bdtopo_product.title,<br>            document_id=config.references.bdtopo_product.document_id,<br>            revision=config.references.bdtopo_product.revision,<br>            evidence_scope=config.references.bdtopo_product.evidence_scope,<br>        ),<br>        evidence_checked_on=config.evidence_checked_on,<br>        vehicle_scope=config.vehicle_scope,<br>        heavy_vehicle_access=config.heavy_vehicle_access,<br>        classes=_CompiledClasses(<br>            general_vehicle_proxy=classes.general_vehicle_proxy,<br>            limited_vehicle_proxy=classes.limited_vehicle_proxy,<br>            restricted_review=classes.restricted_review,<br>            not_general_vehicle_proxy=classes.not_general_vehicle_proxy,<br>            not_distance_proxy=classes.not_distance_proxy,<br>            unknown_review=classes.unknown_review,<br>        ),<br>        asset_state=_CompiledAssetState(<br>            in_service=frozenset(source_values.asset_state.in_service),<br>            project_geometry_not_significant=frozenset(<br>                source_values.asset_state.project_geometry_not_significant<br>            ),<br>            under_construction=frozenset(source_values.asset_state.under_construction),<br>        ),<br>        light_vehicle_access=_CompiledLightVehicleAccess(<br>            open=frozenset(access.open),<br>            toll=frozenset(access.toll),<br>            rights_restricted=frozenset(access.rights_restricted),<br>            physically_impossible=frozenset(access.physically_impossible),<br>        ),<br>        nature=_CompiledRoadNature(<br>            general_motor_road=frozenset(nature.general_motor_road),<br>            limited_motor_proxy=frozenset(nature.limited_motor_proxy),<br>            non_general_vehicle=frozenset(nature.non_general_vehicle),<br>            special_review=frozenset(nature.special_review),<br>        ),<br>        known_restriction_review=frozenset(source_values.known_restriction_review),<br>        importance=_CompiledImportance(<br>            known=frozenset(source_values.importance.known),<br>            limited=frozenset(source_values.importance.limited),<br>        ),<br>        width_below_m=source_values.width_below_m,<br>        decision_precedence=config.decision_precedence,<br>        decision_outcomes=_CompiledDecisionOutcomes(<br>            fictitious_geometry=outcomes.fictitious_geometry,<br>            project_geometry_not_significant=(<br>                outcomes.project_geometry_not_significant<br>            ),<br>            not_in_service=outcomes.not_in_service,<br>            physically_impossible=outcomes.physically_impossible,<br>            non_general_vehicle_nature=outcomes.non_general_vehicle_nature,<br>            rights_restricted=outcomes.rights_restricted,<br>            private_road=outcomes.private_road,<br>            temporal_closure=outcomes.temporal_closure,<br>            known_restriction=outcomes.known_restriction,<br>            other_recorded_restriction=outcomes.other_recorded_restriction,<br>            special_nature=outcomes.special_nature,<br>            limited_nature=outcomes.limited_nature,<br>            importance_6=outcomes.importance_6,<br>            narrow_carriageway=outcomes.narrow_carriageway,<br>            open_or_toll=outcomes.open_or_toll,<br>            unknown=outcomes.unknown,<br>        ),<br>        config_sha256=config_sha256,<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.road_vehicle_proxy_policy::load_ign_road_vehicle_proxy_policy` via `_compile_policy`
- value/type reference: `landscout.stages.road_vehicle_proxy_policy::load_ign_road_vehicle_proxy_policy` via `_compile_policy`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `IgnRoadVehicleProxyPolicy` | `landscout.stages.road_vehicle_proxy_policy.IgnRoadVehicleProxyPolicy` |
| `_CompiledNavigationReference` | `landscout.stages.road_vehicle_proxy_policy._CompiledNavigationReference` |
| `_CompiledBdTopoProductReference` | `landscout.stages.road_vehicle_proxy_policy._CompiledBdTopoProductReference` |
| `_CompiledClasses` | `landscout.stages.road_vehicle_proxy_policy._CompiledClasses` |
| `_CompiledAssetState` | `landscout.stages.road_vehicle_proxy_policy._CompiledAssetState` |
| `frozenset` | `unresolved local/third-party receiver; no ownership inferred` |
| `_CompiledLightVehicleAccess` | `landscout.stages.road_vehicle_proxy_policy._CompiledLightVehicleAccess` |
| `_CompiledRoadNature` | `landscout.stages.road_vehicle_proxy_policy._CompiledRoadNature` |
| `_CompiledImportance` | `landscout.stages.road_vehicle_proxy_policy._CompiledImportance` |
| `_CompiledDecisionOutcomes` | `landscout.stages.road_vehicle_proxy_policy._CompiledDecisionOutcomes` |

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
def _compile_policy(
    config: _PolicyConfig,
    config_sha256: str,
) -> IgnRoadVehicleProxyPolicy:
    classes = config.classes
    source_values = config.source_values
    access = source_values.light_vehicle_access
    nature = source_values.nature
    outcomes = config.decision_outcomes
    return IgnRoadVehicleProxyPolicy(
        policy_id=config.policy_id,
        schema_version=config.schema_version,
        scope=config.scope,
        navigation_reference=_CompiledNavigationReference(
            publisher=config.references.navigation.publisher,
            title=config.references.navigation.title,
            revision=config.references.navigation.revision,
            evidence_scope=config.references.navigation.evidence_scope,
        ),
        bdtopo_product_reference=_CompiledBdTopoProductReference(
            publisher=config.references.bdtopo_product.publisher,
            title=config.references.bdtopo_product.title,
            document_id=config.references.bdtopo_product.document_id,
            revision=config.references.bdtopo_product.revision,
            evidence_scope=config.references.bdtopo_product.evidence_scope,
        ),
        evidence_checked_on=config.evidence_checked_on,
        vehicle_scope=config.vehicle_scope,
        heavy_vehicle_access=config.heavy_vehicle_access,
        classes=_CompiledClasses(
            general_vehicle_proxy=classes.general_vehicle_proxy,
            limited_vehicle_proxy=classes.limited_vehicle_proxy,
            restricted_review=classes.restricted_review,
            not_general_vehicle_proxy=classes.not_general_vehicle_proxy,
            not_distance_proxy=classes.not_distance_proxy,
            unknown_review=classes.unknown_review,
        ),
        asset_state=_CompiledAssetState(
            in_service=frozenset(source_values.asset_state.in_service),
            project_geometry_not_significant=frozenset(
                source_values.asset_state.project_geometry_not_significant
            ),
            under_construction=frozenset(source_values.asset_state.under_construction),
        ),
        light_vehicle_access=_CompiledLightVehicleAccess(
            open=frozenset(access.open),
            toll=frozenset(access.toll),
            rights_restricted=frozenset(access.rights_restricted),
            physically_impossible=frozenset(access.physically_impossible),
        ),
        nature=_CompiledRoadNature(
            general_motor_road=frozenset(nature.general_motor_road),
            limited_motor_proxy=frozenset(nature.limited_motor_proxy),
            non_general_vehicle=frozenset(nature.non_general_vehicle),
            special_review=frozenset(nature.special_review),
        ),
        known_restriction_review=frozenset(source_values.known_restriction_review),
        importance=_CompiledImportance(
            known=frozenset(source_values.importance.known),
            limited=frozenset(source_values.importance.limited),
        ),
        width_below_m=source_values.width_below_m,
        decision_precedence=config.decision_precedence,
        decision_outcomes=_CompiledDecisionOutcomes(
            fictitious_geometry=outcomes.fictitious_geometry,
            project_geometry_not_significant=(
                outcomes.project_geometry_not_significant
            ),
            not_in_service=outcomes.not_in_service,
            physically_impossible=outcomes.physically_impossible,
            non_general_vehicle_nature=outcomes.non_general_vehicle_nature,
            rights_restricted=outcomes.rights_restricted,
            private_road=outcomes.private_road,
            temporal_closure=outcomes.temporal_closure,
            known_restriction=outcomes.known_restriction,
            other_recorded_restriction=outcomes.other_recorded_restriction,
            special_nature=outcomes.special_nature,
            limited_nature=outcomes.limited_nature,
            importance_6=outcomes.importance_6,
            narrow_carriageway=outcomes.narrow_carriageway,
            open_or_toll=outcomes.open_or_toll,
            unknown=outcomes.unknown,
        ),
        config_sha256=config_sha256,
    )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `load_ign_road_vehicle_proxy_policy`

**Purpose:** Load and compile the strict policy from its exact UTF-8 file bytes.

**Exact signature**

```python
def load_ign_road_vehicle_proxy_policy(
    path: Path = _DEFAULT_POLICY_PATH,
) -> IgnRoadVehicleProxyPolicy:
```

- Exact decorators: none.
- Declared return annotation: `IgnRoadVehicleProxyPolicy`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `_DEFAULT_POLICY_PATH` |

**Return and exception contract**

- Exact observed return expressions:
  - `_compile_policy(config, sha256(policy_bytes).hexdigest())`
- Explicit raise paths:
  - `IgnRoadVehicleProxyPolicyError(<br>                "IGN road vehicle-proxy policy must be a mapping"<br>            )` under lexical guard `not isinstance(payload, Mapping)`.
  - `re-raise`.
  - `IgnRoadVehicleProxyPolicyError(str(error))`.
  - `IgnRoadVehicleProxyPolicyError(<br>            "IGN road vehicle-proxy policy is invalid"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.stages::<module>` via `from landscout.stages.road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyPolicy,
    IgnRoadVehicleProxyPolicyError,
    load_ign_road_vehicle_proxy_policy,
)`
- import: `landscout.stages.apply_road_vehicle_proxy_policy::<module>` via `from landscout.stages.road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyPolicy,
    load_ign_road_vehicle_proxy_policy,
)`
- direct call: `landscout.stages.apply_road_vehicle_proxy_policy::_apply_ign_road_vehicle_proxy_policy` via `load_ign_road_vehicle_proxy_policy`
- value/type reference: `landscout.stages.apply_road_vehicle_proxy_policy::_apply_ign_road_vehicle_proxy_policy` via `load_ign_road_vehicle_proxy_policy`
- import: `landscout.stages.assess_road_proximity_coverage::<module>` via `from landscout.stages.road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyPolicy,
    load_ign_road_vehicle_proxy_policy,
)`
- direct call: `landscout.stages.assess_road_proximity_coverage::_assess_road_proximity_coverage` via `load_ign_road_vehicle_proxy_policy`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_assess_road_proximity_coverage` via `load_ign_road_vehicle_proxy_policy`
- import: `landscout.stages.enrich_road_proximity::<module>` via `from landscout.stages.road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyPolicy,
    load_ign_road_vehicle_proxy_policy,
)`
- direct call: `landscout.stages.enrich_road_proximity::_enrich_parcel_road_proximity` via `load_ign_road_vehicle_proxy_policy`
- value/type reference: `landscout.stages.enrich_road_proximity::_enrich_parcel_road_proximity` via `load_ign_road_vehicle_proxy_policy`
- import: `tests.unit.test_apply_road_vehicle_proxy_policy::<module>` via `from landscout.stages.road_vehicle_proxy_policy import (
    load_ign_road_vehicle_proxy_policy,
)`
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_every_configured_known_restriction_is_applied` via `load_ign_road_vehicle_proxy_policy`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_every_configured_known_restriction_is_applied` via `load_ign_road_vehicle_proxy_policy`
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_policy_lineage_is_exact_on_every_row` via `load_ign_road_vehicle_proxy_policy`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_policy_lineage_is_exact_on_every_row` via `load_ign_road_vehicle_proxy_policy`
- import: `tests.unit.test_assess_road_proximity_coverage::<module>` via `from landscout.stages.road_vehicle_proxy_policy import (
    load_ign_road_vehicle_proxy_policy,
)`
- direct call: `tests.unit.test_assess_road_proximity_coverage::_proximity` via `load_ign_road_vehicle_proxy_policy`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::_proximity` via `load_ign_road_vehicle_proxy_policy`
- import: `tests.unit.test_enrich_road_proximity::<module>` via `from landscout.stages.road_vehicle_proxy_policy import (
    load_ign_road_vehicle_proxy_policy,
)`
- direct call: `tests.unit.test_enrich_road_proximity::_road_row` via `load_ign_road_vehicle_proxy_policy`
- value/type reference: `tests.unit.test_enrich_road_proximity::_road_row` via `load_ign_road_vehicle_proxy_policy`
- direct call: `tests.unit.test_enrich_road_proximity::test_selected_road_evidence_and_lineage_are_exact` via `load_ign_road_vehicle_proxy_policy`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_selected_road_evidence_and_lineage_are_exact` via `load_ign_road_vehicle_proxy_policy`
- import: `tests.unit.test_road_vehicle_proxy_policy::<module>` via `from landscout.stages.road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyPolicy,
    IgnRoadVehicleProxyPolicyError,
    load_ign_road_vehicle_proxy_policy,
)`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_duplicate_yaml_policy_key_is_rejected` via `load_ign_road_vehicle_proxy_policy`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_duplicate_yaml_policy_key_is_rejected` via `load_ign_road_vehicle_proxy_policy`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::_load_payload` via `load_ign_road_vehicle_proxy_policy`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::_load_payload` via `load_ign_road_vehicle_proxy_policy`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_checked_in_policy_loads_with_exact_public_identity_and_reference` via `load_ign_road_vehicle_proxy_policy`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_checked_in_policy_loads_with_exact_public_identity_and_reference` via `load_ign_road_vehicle_proxy_policy`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_checked_in_policy_hash_binds_exact_file_bytes` via `load_ign_road_vehicle_proxy_policy`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_checked_in_policy_hash_binds_exact_file_bytes` via `load_ign_road_vehicle_proxy_policy`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_repeat_loading_is_deterministic_and_independent` via `load_ign_road_vehicle_proxy_policy`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_repeat_loading_is_deterministic_and_independent` via `load_ign_road_vehicle_proxy_policy`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_asset_state_groups_cover_exact_v2_domain` via `load_ign_road_vehicle_proxy_policy`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_asset_state_groups_cover_exact_v2_domain` via `load_ign_road_vehicle_proxy_policy`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_importance_domains_expose_known_without_positive_classification` via `load_ign_road_vehicle_proxy_policy`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_importance_domains_expose_known_without_positive_classification` via `load_ign_road_vehicle_proxy_policy`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_decision_precedence_and_rule_outcomes_are_approved` via `load_ign_road_vehicle_proxy_policy`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_decision_precedence_and_rule_outcomes_are_approved` via `load_ign_road_vehicle_proxy_policy`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_project_geometry_rule_has_exact_precedence_position` via `load_ign_road_vehicle_proxy_policy`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_project_geometry_rule_has_exact_precedence_position` via `load_ign_road_vehicle_proxy_policy`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_approved_class_vocabulary_has_no_heavy_or_legal_claim` via `load_ign_road_vehicle_proxy_policy`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_approved_class_vocabulary_has_no_heavy_or_legal_claim` via `load_ign_road_vehicle_proxy_policy`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_observed_d031_natures_are_covered_exactly_once` via `load_ign_road_vehicle_proxy_policy`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_observed_d031_natures_are_covered_exactly_once` via `load_ign_road_vehicle_proxy_policy`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_observed_d031_access_and_importance_vocabularies_are_compatible` via `load_ign_road_vehicle_proxy_policy`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_observed_d031_access_and_importance_vocabularies_are_compatible` via `load_ign_road_vehicle_proxy_policy`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_compiled_policy_structures_are_immutable` via `load_ign_road_vehicle_proxy_policy`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_compiled_policy_structures_are_immutable` via `load_ign_road_vehicle_proxy_policy`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_mutating_source_payload_cannot_affect_another_load` via `load_ign_road_vehicle_proxy_policy`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_mutating_source_payload_cannot_affect_another_load` via `load_ign_road_vehicle_proxy_policy`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_malformed_yaml_has_controlled_error` via `load_ign_road_vehicle_proxy_policy`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_malformed_yaml_has_controlled_error` via `load_ign_road_vehicle_proxy_policy`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_missing_file_has_controlled_error` via `load_ign_road_vehicle_proxy_policy`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_missing_file_has_controlled_error` via `load_ign_road_vehicle_proxy_policy`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `Path(path).read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `Path` | `pathlib.Path` |
| `loads_strict_yaml` | `landscout.common.strict_yaml.loads_strict_yaml` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnRoadVehicleProxyPolicyError` | `landscout.stages.road_vehicle_proxy_policy.IgnRoadVehicleProxyPolicyError` |
| `_PolicyConfig.model_validate` | `landscout.stages.road_vehicle_proxy_policy._PolicyConfig.model_validate` |
| `_compile_policy` | `landscout.stages.road_vehicle_proxy_policy._compile_policy` |
| `sha256(policy_bytes).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `Path(path).read_bytes` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `sha256(policy_bytes).hexdigest`<br>`sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def load_ign_road_vehicle_proxy_policy(
    path: Path = _DEFAULT_POLICY_PATH,
) -> IgnRoadVehicleProxyPolicy:
    """Load and compile the strict policy from its exact UTF-8 file bytes."""

    try:
        policy_bytes = Path(path).read_bytes()
        payload = loads_strict_yaml(policy_bytes)
        if not isinstance(payload, Mapping):
            raise IgnRoadVehicleProxyPolicyError(
                "IGN road vehicle-proxy policy must be a mapping"
            )
        config = _PolicyConfig.model_validate(payload)
        return _compile_policy(config, sha256(policy_bytes).hexdigest())
    except IgnRoadVehicleProxyPolicyError:
        raise
    except StrictYamlError as error:
        raise IgnRoadVehicleProxyPolicyError(str(error)) from error
    except Exception as error:
        raise IgnRoadVehicleProxyPolicyError(
            "IGN road vehicle-proxy policy is invalid"
        ) from error
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.


## 7. Validation and data-contract summary

- Canonical schema/mapping declarations inventoried above: none at module scope.
- Exact value/null/index/CRS/geometry/hash behavior is claimed only where the reproduced validators and operations enforce it.

## 8. Public exports and package ownership

Exact `__all__` members and local origins:

| Export | Local origin binding |
|---|---|
| `IgnRoadVehicleProxyPolicy` | `landscout.stages.road_vehicle_proxy_policy.IgnRoadVehicleProxyPolicy` |
| `IgnRoadVehicleProxyPolicyError` | `landscout.stages.road_vehicle_proxy_policy.IgnRoadVehicleProxyPolicyError` |
| `load_ign_road_vehicle_proxy_policy` | `landscout.stages.road_vehicle_proxy_policy.load_ign_road_vehicle_proxy_policy` |

## 9. Trust, provenance, side effects, and business boundary

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.
- Configured identity, textual lineage, byte identity, physical source reconstruction, local envelope validation, and source-complete validation remain distinct trust levels. This companion attributes only the levels implemented in the exact source.
- Filesystem, network, hashing, CRS/geometry, process, mutation, and expected-exception evidence is listed per callable; an empty category is not silently promoted to an effect.

## 10. Change impact

A source-byte change invalidates the SHA above and requires re-auditing imports/re-exports, constants/aliases/schemas, model fields/immutability, qualified callers, side effects, controlled errors, tests, source/artifact locks, and the exact full snapshot.

## 11. Exact complete current file content

The following UTF-8 snapshot is the complete current repository file, not an excerpt. Its raw-byte SHA256 is the value in **File identity**.

```python
"""Compile the versioned IGN general-vehicle proxy evidence policy."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path
from typing import Annotated, Literal, Self

from pydantic import (
    AfterValidator,
    BaseModel,
    ConfigDict,
    Field,
    StrictFloat,
    StrictInt,
    StringConstraints,
    model_validator,
)

from landscout.common.strict_yaml import StrictYamlError, loads_strict_yaml

__all__ = [
    "IgnRoadVehicleProxyPolicy",
    "IgnRoadVehicleProxyPolicyError",
    "load_ign_road_vehicle_proxy_policy",
]

_DEFAULT_POLICY_PATH = (
    Path(__file__).resolve().parents[3]
    / "configs"
    / "access"
    / "ign_bdtopo_vehicle_proxy_policy.yaml"
)
_POLICY_ID = "ign_bdtopo_general_vehicle_proxy_v2"
_POLICY_SCOPE = "OFFICIAL_IGN_CAR_ROUTING_EVIDENCE_ONLY"
_EXPECTED_PRECEDENCE = (
    "FICTITIOUS_GEOMETRY",
    "PROJECT_GEOMETRY_NOT_SIGNIFICANT",
    "NOT_IN_SERVICE",
    "PHYSICALLY_IMPOSSIBLE",
    "NON_GENERAL_VEHICLE_NATURE",
    "RIGHTS_RESTRICTED",
    "PRIVATE_ROAD",
    "TEMPORAL_CLOSURE",
    "KNOWN_RESTRICTION",
    "OTHER_RECORDED_RESTRICTION",
    "SPECIAL_NATURE",
    "LIMITED_NATURE",
    "IMPORTANCE_6",
    "NARROW_CARRIAGEWAY",
    "OPEN_OR_TOLL",
    "UNKNOWN",
)


class IgnRoadVehicleProxyPolicyError(ValueError):
    """Raised when the IGN road vehicle-proxy policy is unsafe or invalid."""


def _exact_string(value: str) -> str:
    if value != value.strip():
        raise ValueError("policy strings must not contain edge whitespace")
    return value


_ExactString = Annotated[
    str,
    StringConstraints(strict=True, min_length=1),
    AfterValidator(_exact_string),
]
_NonEmptyStrings = Annotated[tuple[_ExactString, ...], Field(min_length=1)]


class _StrictPolicyModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


def _require_unique(values: tuple[str, ...], label: str) -> None:
    if len(values) != len(set(values)):
        raise ValueError(f"{label} contains duplicate source values")


def _require_disjoint(groups: tuple[tuple[str, ...], ...], label: str) -> None:
    flattened = tuple(value for group in groups for value in group)
    if len(flattened) != len(set(flattened)):
        raise ValueError(f"{label} source groups overlap")


class _NavigationReferenceConfig(_StrictPolicyModel):
    publisher: Literal["IGN"]
    title: Literal["Calcul d’itinéraire"]
    revision: Literal["2026-05-27"]
    evidence_scope: Literal["GENERAL_CAR_ROUTING_RULES"]


class _BdTopoProductReferenceConfig(_StrictPolicyModel):
    publisher: Literal["IGN"]
    title: Literal["BD TOPO® Version 3.5 - Descriptif de contenu"]
    document_id: Literal["DC_BDTOPO_3-5"]
    revision: Literal["2025-11"]
    evidence_scope: Literal["SOURCE_ATTRIBUTE_SEMANTICS"]


class _ReferencesConfig(_StrictPolicyModel):
    navigation: _NavigationReferenceConfig
    bdtopo_product: _BdTopoProductReferenceConfig


class _ClassesConfig(_StrictPolicyModel):
    general_vehicle_proxy: Literal["GENERAL_VEHICLE_PROXY"]
    limited_vehicle_proxy: Literal["LIMITED_VEHICLE_PROXY"]
    restricted_review: Literal["RESTRICTED_REVIEW"]
    not_general_vehicle_proxy: Literal["NOT_GENERAL_VEHICLE_PROXY"]
    not_distance_proxy: Literal["NOT_DISTANCE_PROXY"]
    unknown_review: Literal["UNKNOWN_REVIEW"]


class _AssetStateConfig(_StrictPolicyModel):
    in_service: _NonEmptyStrings
    project_geometry_not_significant: _NonEmptyStrings
    under_construction: _NonEmptyStrings

    @model_validator(mode="after")
    def _valid_groups(self) -> Self:
        groups = (
            self.in_service,
            self.project_geometry_not_significant,
            self.under_construction,
        )
        for name, values in zip(
            (
                "in_service",
                "project_geometry_not_significant",
                "under_construction",
            ),
            groups,
            strict=True,
        ):
            _require_unique(values, name)
        _require_disjoint(groups, "asset_state")
        if groups != (("En service",), ("En projet",), ("En construction",)):
            raise ValueError("asset_state groups must cover the exact source domain")
        return self


class _LightVehicleAccessConfig(_StrictPolicyModel):
    open: _NonEmptyStrings
    toll: _NonEmptyStrings
    rights_restricted: _NonEmptyStrings
    physically_impossible: _NonEmptyStrings

    @model_validator(mode="after")
    def _valid_groups(self) -> Self:
        groups = (
            self.open,
            self.toll,
            self.rights_restricted,
            self.physically_impossible,
        )
        for name, values in zip(
            ("open", "toll", "rights_restricted", "physically_impossible"),
            groups,
            strict=True,
        ):
            _require_unique(values, name)
        _require_disjoint(groups, "light_vehicle_access")
        return self


class _RoadNatureConfig(_StrictPolicyModel):
    general_motor_road: _NonEmptyStrings
    limited_motor_proxy: _NonEmptyStrings
    non_general_vehicle: _NonEmptyStrings
    special_review: _NonEmptyStrings

    @model_validator(mode="after")
    def _valid_groups(self) -> Self:
        groups = (
            self.general_motor_road,
            self.limited_motor_proxy,
            self.non_general_vehicle,
            self.special_review,
        )
        for name, values in zip(
            (
                "general_motor_road",
                "limited_motor_proxy",
                "non_general_vehicle",
                "special_review",
            ),
            groups,
            strict=True,
        ):
            _require_unique(values, name)
        _require_disjoint(groups, "nature")
        return self


class _ImportanceConfig(_StrictPolicyModel):
    known: _NonEmptyStrings
    limited: _NonEmptyStrings

    @model_validator(mode="after")
    def _valid_domain(self) -> Self:
        _require_unique(self.known, "importance.known")
        _require_unique(self.limited, "importance.limited")
        if self.known != ("1", "2", "3", "4", "5", "6"):
            raise ValueError("importance.known must cover exactly source values 1-6")
        if self.limited != ("6",):
            raise ValueError("importance.limited must contain exactly source value '6'")
        if not set(self.limited).issubset(self.known):
            raise ValueError("importance.limited must be a subset of importance.known")
        return self


class _SourceValuesConfig(_StrictPolicyModel):
    asset_state: _AssetStateConfig
    light_vehicle_access: _LightVehicleAccessConfig
    nature: _RoadNatureConfig
    known_restriction_review: _NonEmptyStrings
    importance: _ImportanceConfig
    width_below_m: Annotated[StrictFloat, Field(gt=0, allow_inf_nan=False)]

    @model_validator(mode="after")
    def _valid_values(self) -> Self:
        _require_unique(self.known_restriction_review, "known_restriction_review")
        return self


class _DecisionOutcomesConfig(_StrictPolicyModel):
    fictitious_geometry: Literal["NOT_DISTANCE_PROXY"]
    project_geometry_not_significant: Literal["NOT_DISTANCE_PROXY"]
    not_in_service: Literal["NOT_GENERAL_VEHICLE_PROXY"]
    physically_impossible: Literal["NOT_GENERAL_VEHICLE_PROXY"]
    non_general_vehicle_nature: Literal["NOT_GENERAL_VEHICLE_PROXY"]
    rights_restricted: Literal["RESTRICTED_REVIEW"]
    private_road: Literal["RESTRICTED_REVIEW"]
    temporal_closure: Literal["RESTRICTED_REVIEW"]
    known_restriction: Literal["RESTRICTED_REVIEW"]
    other_recorded_restriction: Literal["RESTRICTED_REVIEW"]
    special_nature: Literal["RESTRICTED_REVIEW"]
    limited_nature: Literal["LIMITED_VEHICLE_PROXY"]
    importance_6: Literal["LIMITED_VEHICLE_PROXY"]
    narrow_carriageway: Literal["LIMITED_VEHICLE_PROXY"]
    open_or_toll: Literal["GENERAL_VEHICLE_PROXY"]
    unknown: Literal["UNKNOWN_REVIEW"]


class _PolicyConfig(_StrictPolicyModel):
    policy_id: _ExactString
    schema_version: StrictInt
    scope: _ExactString
    references: _ReferencesConfig
    evidence_checked_on: Literal["2026-08-16"]
    vehicle_scope: Literal["LIGHT_VEHICLE_AND_GENERAL_CAR_NETWORK"]
    heavy_vehicle_access: Literal["NOT_PROVEN"]
    classes: _ClassesConfig
    source_values: _SourceValuesConfig
    decision_precedence: _NonEmptyStrings
    decision_outcomes: _DecisionOutcomesConfig

    @model_validator(mode="after")
    def _valid_identity_and_precedence(self) -> Self:
        if self.policy_id != _POLICY_ID:
            raise ValueError("policy_id is not the approved v2 policy identity")
        if self.schema_version != 2:
            raise ValueError("schema_version must be exactly 2")
        if self.scope != _POLICY_SCOPE:
            raise ValueError("scope is not the approved official IGN evidence scope")
        if self.decision_precedence != _EXPECTED_PRECEDENCE:
            raise ValueError("decision_precedence differs from approved v2 order")
        return self


@dataclass(frozen=True)
class _CompiledClasses:
    general_vehicle_proxy: str
    limited_vehicle_proxy: str
    restricted_review: str
    not_general_vehicle_proxy: str
    not_distance_proxy: str
    unknown_review: str

    @property
    def values(self) -> tuple[str, ...]:
        return (
            self.general_vehicle_proxy,
            self.limited_vehicle_proxy,
            self.restricted_review,
            self.not_general_vehicle_proxy,
            self.not_distance_proxy,
            self.unknown_review,
        )


@dataclass(frozen=True)
class _CompiledAssetState:
    in_service: frozenset[str]
    project_geometry_not_significant: frozenset[str]
    under_construction: frozenset[str]


@dataclass(frozen=True)
class _CompiledNavigationReference:
    publisher: str
    title: str
    revision: str
    evidence_scope: str


@dataclass(frozen=True)
class _CompiledBdTopoProductReference:
    publisher: str
    title: str
    document_id: str
    revision: str
    evidence_scope: str


@dataclass(frozen=True)
class _CompiledLightVehicleAccess:
    open: frozenset[str]
    toll: frozenset[str]
    rights_restricted: frozenset[str]
    physically_impossible: frozenset[str]


@dataclass(frozen=True)
class _CompiledRoadNature:
    general_motor_road: frozenset[str]
    limited_motor_proxy: frozenset[str]
    non_general_vehicle: frozenset[str]
    special_review: frozenset[str]


@dataclass(frozen=True)
class _CompiledImportance:
    known: frozenset[str]
    limited: frozenset[str]


@dataclass(frozen=True)
class _CompiledDecisionOutcomes:
    fictitious_geometry: str
    project_geometry_not_significant: str
    not_in_service: str
    physically_impossible: str
    non_general_vehicle_nature: str
    rights_restricted: str
    private_road: str
    temporal_closure: str
    known_restriction: str
    other_recorded_restriction: str
    special_nature: str
    limited_nature: str
    importance_6: str
    narrow_carriageway: str
    open_or_toll: str
    unknown: str


@dataclass(frozen=True)
class IgnRoadVehicleProxyPolicy:
    """Immutable policy evidence compiled from the exact checked-in YAML bytes."""

    policy_id: str
    schema_version: int
    scope: str
    navigation_reference: _CompiledNavigationReference
    bdtopo_product_reference: _CompiledBdTopoProductReference
    evidence_checked_on: str
    vehicle_scope: str
    heavy_vehicle_access: str
    classes: _CompiledClasses
    asset_state: _CompiledAssetState
    light_vehicle_access: _CompiledLightVehicleAccess
    nature: _CompiledRoadNature
    known_restriction_review: frozenset[str]
    importance: _CompiledImportance
    width_below_m: float
    decision_precedence: tuple[str, ...]
    decision_outcomes: _CompiledDecisionOutcomes
    config_sha256: str


def _compile_policy(
    config: _PolicyConfig,
    config_sha256: str,
) -> IgnRoadVehicleProxyPolicy:
    classes = config.classes
    source_values = config.source_values
    access = source_values.light_vehicle_access
    nature = source_values.nature
    outcomes = config.decision_outcomes
    return IgnRoadVehicleProxyPolicy(
        policy_id=config.policy_id,
        schema_version=config.schema_version,
        scope=config.scope,
        navigation_reference=_CompiledNavigationReference(
            publisher=config.references.navigation.publisher,
            title=config.references.navigation.title,
            revision=config.references.navigation.revision,
            evidence_scope=config.references.navigation.evidence_scope,
        ),
        bdtopo_product_reference=_CompiledBdTopoProductReference(
            publisher=config.references.bdtopo_product.publisher,
            title=config.references.bdtopo_product.title,
            document_id=config.references.bdtopo_product.document_id,
            revision=config.references.bdtopo_product.revision,
            evidence_scope=config.references.bdtopo_product.evidence_scope,
        ),
        evidence_checked_on=config.evidence_checked_on,
        vehicle_scope=config.vehicle_scope,
        heavy_vehicle_access=config.heavy_vehicle_access,
        classes=_CompiledClasses(
            general_vehicle_proxy=classes.general_vehicle_proxy,
            limited_vehicle_proxy=classes.limited_vehicle_proxy,
            restricted_review=classes.restricted_review,
            not_general_vehicle_proxy=classes.not_general_vehicle_proxy,
            not_distance_proxy=classes.not_distance_proxy,
            unknown_review=classes.unknown_review,
        ),
        asset_state=_CompiledAssetState(
            in_service=frozenset(source_values.asset_state.in_service),
            project_geometry_not_significant=frozenset(
                source_values.asset_state.project_geometry_not_significant
            ),
            under_construction=frozenset(source_values.asset_state.under_construction),
        ),
        light_vehicle_access=_CompiledLightVehicleAccess(
            open=frozenset(access.open),
            toll=frozenset(access.toll),
            rights_restricted=frozenset(access.rights_restricted),
            physically_impossible=frozenset(access.physically_impossible),
        ),
        nature=_CompiledRoadNature(
            general_motor_road=frozenset(nature.general_motor_road),
            limited_motor_proxy=frozenset(nature.limited_motor_proxy),
            non_general_vehicle=frozenset(nature.non_general_vehicle),
            special_review=frozenset(nature.special_review),
        ),
        known_restriction_review=frozenset(source_values.known_restriction_review),
        importance=_CompiledImportance(
            known=frozenset(source_values.importance.known),
            limited=frozenset(source_values.importance.limited),
        ),
        width_below_m=source_values.width_below_m,
        decision_precedence=config.decision_precedence,
        decision_outcomes=_CompiledDecisionOutcomes(
            fictitious_geometry=outcomes.fictitious_geometry,
            project_geometry_not_significant=(
                outcomes.project_geometry_not_significant
            ),
            not_in_service=outcomes.not_in_service,
            physically_impossible=outcomes.physically_impossible,
            non_general_vehicle_nature=outcomes.non_general_vehicle_nature,
            rights_restricted=outcomes.rights_restricted,
            private_road=outcomes.private_road,
            temporal_closure=outcomes.temporal_closure,
            known_restriction=outcomes.known_restriction,
            other_recorded_restriction=outcomes.other_recorded_restriction,
            special_nature=outcomes.special_nature,
            limited_nature=outcomes.limited_nature,
            importance_6=outcomes.importance_6,
            narrow_carriageway=outcomes.narrow_carriageway,
            open_or_toll=outcomes.open_or_toll,
            unknown=outcomes.unknown,
        ),
        config_sha256=config_sha256,
    )


def load_ign_road_vehicle_proxy_policy(
    path: Path = _DEFAULT_POLICY_PATH,
) -> IgnRoadVehicleProxyPolicy:
    """Load and compile the strict policy from its exact UTF-8 file bytes."""

    try:
        policy_bytes = Path(path).read_bytes()
        payload = loads_strict_yaml(policy_bytes)
        if not isinstance(payload, Mapping):
            raise IgnRoadVehicleProxyPolicyError(
                "IGN road vehicle-proxy policy must be a mapping"
            )
        config = _PolicyConfig.model_validate(payload)
        return _compile_policy(config, sha256(policy_bytes).hexdigest())
    except IgnRoadVehicleProxyPolicyError:
        raise
    except StrictYamlError as error:
        raise IgnRoadVehicleProxyPolicyError(str(error)) from error
    except Exception as error:
        raise IgnRoadVehicleProxyPolicyError(
            "IGN road vehicle-proxy policy is invalid"
        ) from error
```

# `src/landscout/stages/road_vehicle_proxy_policy.py`

## File identity

- Repository path: `src/landscout/stages/road_vehicle_proxy_policy.py`
- File type: Python source
- Layer: policy compilation stage
- Domain: road
- Responsibility: Loads and compiles the checked-in general-car/light-vehicle IGN road evidence policy.
- Source SHA256: `73b7315bf37c48510fbb8e63c28272349fa0407f1c0c5adea91142a74c481286`

## 1. Purpose

Loads and compiles the checked-in general-car/light-vehicle IGN road evidence policy.

## 2. Position in LandScout architecture

This file belongs to the **policy compilation stage** layer and the **road** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `from collections.abc import Mapping`
- `from dataclasses import dataclass`
- `from hashlib import sha256`
- `from pathlib import Path`
- `from typing import Annotated, Literal, Self`

### Third-party packages

- `import yaml`
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

- `None.`

## 4. Contract taxonomy

### A. Python constants

#### `_DEFAULT_POLICY_PATH`

```python
_DEFAULT_POLICY_PATH = (
    Path(__file__).resolve().parents[3]
    / "configs"
    / "access"
    / "ign_bdtopo_vehicle_proxy_policy.yaml"
)
```

Module-level technical/source/policy constant consumed by the exact references below.

#### `_POLICY_ID`

```python
_POLICY_ID = "ign_bdtopo_general_vehicle_proxy_v2"
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `src/landscout/stages/road_vehicle_proxy_policy.py::_PolicyConfig._valid_identity_and_precedence` (value reference).

#### `_POLICY_SCOPE`

```python
_POLICY_SCOPE = "OFFICIAL_IGN_CAR_ROUTING_EVIDENCE_ONLY"
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `src/landscout/stages/road_vehicle_proxy_policy.py::_PolicyConfig._valid_identity_and_precedence` (value reference).

#### `_EXPECTED_PRECEDENCE`

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

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `src/landscout/stages/road_vehicle_proxy_policy.py::_PolicyConfig._valid_identity_and_precedence` (value reference).


### B. Type aliases and closed domains

#### `_ExactString`

```python
_ExactString = Annotated[
    str,
    StringConstraints(strict=True, min_length=1),
    AfterValidator(_exact_string),
]
```

Annotated validation alias whose strictness, regex/bounds, and callbacks are exactly those shown above. Enforced/consumed by `src/landscout/stages/road_vehicle_proxy_policy.py::<module>` (value reference), `src/landscout/stages/road_vehicle_proxy_policy.py::_PolicyConfig` (type annotation).

#### `_NonEmptyStrings`

```python
_NonEmptyStrings = Annotated[tuple[_ExactString, ...], Field(min_length=1)]
```

Annotated validation alias whose strictness, regex/bounds, and callbacks are exactly those shown above. Enforced/consumed by `src/landscout/stages/road_vehicle_proxy_policy.py::_AssetStateConfig` (type annotation), `src/landscout/stages/road_vehicle_proxy_policy.py::_LightVehicleAccessConfig` (type annotation), `src/landscout/stages/road_vehicle_proxy_policy.py::_RoadNatureConfig` (type annotation), `src/landscout/stages/road_vehicle_proxy_policy.py::_ImportanceConfig` (type annotation), `src/landscout/stages/road_vehicle_proxy_policy.py::_SourceValuesConfig` (type annotation), `src/landscout/stages/road_vehicle_proxy_policy.py::_PolicyConfig` (type annotation).


### C. Meaningful dunder contracts

- `__all__` — explicit public export allow-list.
```python
__all__ = [
    "IgnRoadVehicleProxyPolicy",
    "IgnRoadVehicleProxyPolicyError",
    "load_ign_road_vehicle_proxy_policy",
]
```


### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

### `IgnRoadVehicleProxyPolicyError`

**Purpose:** Raised when the IGN road vehicle-proxy policy is unsafe or invalid.

**Kind:** controlled exception.

**Inheritance:** `ValueError`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyPolicy,
    IgnRoadVehicleProxyPolicyError,
    load_ign_road_vehicle_proxy_policy,
)`.
- import: `tests/unit/test_road_vehicle_proxy_policy.py::<module>` via `from landscout.stages.road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyPolicy,
    IgnRoadVehicleProxyPolicyError,
    load_ign_road_vehicle_proxy_policy,
)`.
- constructor call: `src/landscout/stages/road_vehicle_proxy_policy.py::_construct_unique_mapping` via `IgnRoadVehicleProxyPolicyError`.
- constructor call: `src/landscout/stages/road_vehicle_proxy_policy.py::load_ign_road_vehicle_proxy_policy` via `IgnRoadVehicleProxyPolicyError`.
- expected exception type: `tests/unit/test_road_vehicle_proxy_policy.py::test_invalid_config_structure_is_rejected` via `pytest.raises(IgnRoadVehicleProxyPolicyError, match=message)`.
- expected exception type: `tests/unit/test_road_vehicle_proxy_policy.py::test_unsupported_schema_version_is_rejected` via `pytest.raises(IgnRoadVehicleProxyPolicyError)`.
- expected exception type: `tests/unit/test_road_vehicle_proxy_policy.py::test_wrong_policy_identity_is_rejected` via `pytest.raises(IgnRoadVehicleProxyPolicyError)`.
- expected exception type: `tests/unit/test_road_vehicle_proxy_policy.py::test_both_evidence_references_are_required` via `pytest.raises(IgnRoadVehicleProxyPolicyError)`.
- expected exception type: `tests/unit/test_road_vehicle_proxy_policy.py::test_product_reference_document_id_is_exact` via `pytest.raises(IgnRoadVehicleProxyPolicyError)`.
- expected exception type: `tests/unit/test_road_vehicle_proxy_policy.py::test_unknown_evidence_reference_is_rejected` via `pytest.raises(IgnRoadVehicleProxyPolicyError)`.
- expected exception type: `tests/unit/test_road_vehicle_proxy_policy.py::test_asset_state_group_overlap_is_rejected` via `pytest.raises(IgnRoadVehicleProxyPolicyError)`.
- expected exception type: `tests/unit/test_road_vehicle_proxy_policy.py::test_missing_known_asset_state_is_rejected` via `pytest.raises(IgnRoadVehicleProxyPolicyError)`.
- expected exception type: `tests/unit/test_road_vehicle_proxy_policy.py::test_unknown_additional_asset_state_is_rejected` via `pytest.raises(IgnRoadVehicleProxyPolicyError)`.
- expected exception type: `tests/unit/test_road_vehicle_proxy_policy.py::test_semantic_values_must_be_exact_non_empty_strings` via `pytest.raises(IgnRoadVehicleProxyPolicyError)`.
- expected exception type: `tests/unit/test_road_vehicle_proxy_policy.py::test_duplicate_semantic_value_is_rejected` via `pytest.raises(IgnRoadVehicleProxyPolicyError, match='invalid')`.
- expected exception type: `tests/unit/test_road_vehicle_proxy_policy.py::test_semantic_groups_must_be_pairwise_disjoint` via `pytest.raises(IgnRoadVehicleProxyPolicyError, match='invalid')`.
- expected exception type: `tests/unit/test_road_vehicle_proxy_policy.py::test_duplicate_known_restriction_is_rejected` via `pytest.raises(IgnRoadVehicleProxyPolicyError)`.
- expected exception type: `tests/unit/test_road_vehicle_proxy_policy.py::test_invalid_width_threshold_is_rejected` via `pytest.raises(IgnRoadVehicleProxyPolicyError)`.
- expected exception type: `tests/unit/test_road_vehicle_proxy_policy.py::test_importance_domains_must_be_exact` via `pytest.raises(IgnRoadVehicleProxyPolicyError)`.
- expected exception type: `tests/unit/test_road_vehicle_proxy_policy.py::test_decision_precedence_must_be_exact` via `pytest.raises(IgnRoadVehicleProxyPolicyError)`.
- expected exception type: `tests/unit/test_road_vehicle_proxy_policy.py::test_output_class_vocabulary_must_be_exact` via `pytest.raises(IgnRoadVehicleProxyPolicyError)`.
- expected exception type: `tests/unit/test_road_vehicle_proxy_policy.py::test_malformed_yaml_has_controlled_error` via `pytest.raises(IgnRoadVehicleProxyPolicyError)`.
- expected exception type: `tests/unit/test_road_vehicle_proxy_policy.py::test_non_mapping_yaml_has_controlled_error` via `pytest.raises(IgnRoadVehicleProxyPolicyError)`.
- expected exception type: `tests/unit/test_road_vehicle_proxy_policy.py::test_missing_file_has_controlled_error` via `pytest.raises(IgnRoadVehicleProxyPolicyError)`.

**Exact class source**

```python
class IgnRoadVehicleProxyPolicyError(ValueError):
    """Raised when the IGN road vehicle-proxy policy is unsafe or invalid."""
```

### `_StrictPolicyModel`

**Purpose:** Validates the road contract carried by its explicit validators and inherited fields.

**Kind:** Pydantic model.

**Inheritance:** `BaseModel`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- Pydantic constructs this model during direct/model_validate or nested-model validation; its exact validators and the module's loader/build functions below define the active framework entry points.

**Exact class source**

```python
class _StrictPolicyModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)
```

### `_NavigationReferenceConfig`

**Purpose:** Validates the road contract carried by `publisher`, `title`, `revision`, `evidence_scope`.

**Kind:** Pydantic model.

**Inheritance:** `_StrictPolicyModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `publisher` | `publisher: Literal["IGN"]` | Publisher text reported by the owning source metadata or checked-in reference. |
| `title` | `title: Literal["Calcul d’itinéraire"]` | `_NavigationReferenceConfig.title` carries the title used by the reproduced constructors and validators; its declared type is `Literal['Calcul d’itinéraire']` and no legal meaning is inferred beyond that owner. |
| `revision` | `revision: Literal["2026-05-27"]` | Revision identifier of the checked-in official reference snapshot. |
| `evidence_scope` | `evidence_scope: Literal["GENERAL_CAR_ROUTING_RULES"]` | `_NavigationReferenceConfig.evidence_scope` represents the `evidence_scope` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |

**Interface consumers**

- type annotation: `src/landscout/stages/road_vehicle_proxy_policy.py::_ReferencesConfig` via `_NavigationReferenceConfig`.

**Exact class source**

```python
class _NavigationReferenceConfig(_StrictPolicyModel):
    publisher: Literal["IGN"]
    title: Literal["Calcul d’itinéraire"]
    revision: Literal["2026-05-27"]
    evidence_scope: Literal["GENERAL_CAR_ROUTING_RULES"]
```

### `_BdTopoProductReferenceConfig`

**Purpose:** Validates the road contract carried by `publisher`, `title`, `document_id`, `revision`, `evidence_scope`.

**Kind:** Pydantic model.

**Inheritance:** `_StrictPolicyModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `publisher` | `publisher: Literal["IGN"]` | Publisher text reported by the owning source metadata or checked-in reference. |
| `title` | `title: Literal["BD TOPO® Version 3.5 - Descriptif de contenu"]` | `_BdTopoProductReferenceConfig.title` carries the title used by the reproduced constructors and validators; its declared type is `Literal['BD TOPO® Version 3.5 - Descriptif de contenu']` and no legal meaning is inferred beyond that owner. |
| `document_id` | `document_id: Literal["DC_BDTOPO_3-5"]` | Exact identity for the entity named by the field; uniqueness, portability, and lineage meaning are only those explicitly validated by the owner. |
| `revision` | `revision: Literal["2025-11"]` | Revision identifier of the checked-in official reference snapshot. |
| `evidence_scope` | `evidence_scope: Literal["SOURCE_ATTRIBUTE_SEMANTICS"]` | `_BdTopoProductReferenceConfig.evidence_scope` represents the `evidence_scope` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |

**Interface consumers**

- type annotation: `src/landscout/stages/road_vehicle_proxy_policy.py::_ReferencesConfig` via `_BdTopoProductReferenceConfig`.

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

**Purpose:** Validates the road contract carried by `navigation`, `bdtopo_product`.

**Kind:** Pydantic model.

**Inheritance:** `_StrictPolicyModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `navigation` | `navigation: _NavigationReferenceConfig` | Checked-in official navigation/routing reference metadata. |
| `bdtopo_product` | `bdtopo_product: _BdTopoProductReferenceConfig` | Checked-in official BD TOPO product-reference metadata. |

**Interface consumers**

- type annotation: `src/landscout/stages/road_vehicle_proxy_policy.py::_PolicyConfig` via `_ReferencesConfig`.

**Exact class source**

```python
class _ReferencesConfig(_StrictPolicyModel):
    navigation: _NavigationReferenceConfig
    bdtopo_product: _BdTopoProductReferenceConfig
```

### `_ClassesConfig`

**Purpose:** Validates the road contract carried by `general_vehicle_proxy`, `limited_vehicle_proxy`, `restricted_review`, `not_general_vehicle_proxy`, `not_distance_proxy`, `unknown_review`.

**Kind:** Pydantic model.

**Inheritance:** `_StrictPolicyModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `general_vehicle_proxy` | `general_vehicle_proxy: Literal["GENERAL_VEHICLE_PROXY"]` | Exact road-proxy output class configured for `general_vehicle_proxy` evidence. |
| `limited_vehicle_proxy` | `limited_vehicle_proxy: Literal["LIMITED_VEHICLE_PROXY"]` | Exact road-proxy output class configured for `limited_vehicle_proxy` evidence. |
| `restricted_review` | `restricted_review: Literal["RESTRICTED_REVIEW"]` | Exact road-proxy output class configured for `restricted_review` evidence. |
| `not_general_vehicle_proxy` | `not_general_vehicle_proxy: Literal["NOT_GENERAL_VEHICLE_PROXY"]` | Exact road-proxy output class configured for `not_general_vehicle_proxy` evidence. |
| `not_distance_proxy` | `not_distance_proxy: Literal["NOT_DISTANCE_PROXY"]` | Exact road-proxy output class configured for `not_distance_proxy` evidence. |
| `unknown_review` | `unknown_review: Literal["UNKNOWN_REVIEW"]` | Exact road-proxy output class configured for `unknown_review` evidence. |

**Interface consumers**

- type annotation: `src/landscout/stages/road_vehicle_proxy_policy.py::_PolicyConfig` via `_ClassesConfig`.

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

**Purpose:** Validates the road contract carried by `in_service`, `project_geometry_not_significant`, `under_construction`.

**Kind:** Pydantic model.

**Inheritance:** `_StrictPolicyModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `in_service` | `in_service: _NonEmptyStrings` | Exact IGN asset-state source values assigned to `IN_SERVICE` evidence. |
| `project_geometry_not_significant` | `project_geometry_not_significant: _NonEmptyStrings` | Exact IGN asset-state source values assigned to `PROJECT_GEOMETRY_NOT_SIGNIFICANT` evidence. |
| `under_construction` | `under_construction: _NonEmptyStrings` | Exact IGN asset-state source values assigned to `UNDER_CONSTRUCTION` evidence. |

**Validators (exact source)**

`_valid_groups`:

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

**Interface consumers**

- type annotation: `src/landscout/stages/road_vehicle_proxy_policy.py::_SourceValuesConfig` via `_AssetStateConfig`.

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

**Purpose:** Validates the road contract carried by `open`, `toll`, `rights_restricted`, `physically_impossible`.

**Kind:** Pydantic model.

**Inheritance:** `_StrictPolicyModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `open` | `open: _NonEmptyStrings` | Exact IGN light-vehicle-access source values assigned to `OPEN` evidence. |
| `toll` | `toll: _NonEmptyStrings` | Exact IGN light-vehicle-access source values assigned to `TOLL` evidence. |
| `rights_restricted` | `rights_restricted: _NonEmptyStrings` | Exact IGN light-vehicle-access source values assigned to `RIGHTS_RESTRICTED` evidence. |
| `physically_impossible` | `physically_impossible: _NonEmptyStrings` | Exact IGN light-vehicle-access source values assigned to `PHYSICALLY_IMPOSSIBLE` evidence. |

**Validators (exact source)**

`_valid_groups`:

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

**Interface consumers**

- type annotation: `src/landscout/stages/road_vehicle_proxy_policy.py::_SourceValuesConfig` via `_LightVehicleAccessConfig`.

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

**Purpose:** Validates the road contract carried by `general_motor_road`, `limited_motor_proxy`, `non_general_vehicle`, `special_review`.

**Kind:** Pydantic model.

**Inheritance:** `_StrictPolicyModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `general_motor_road` | `general_motor_road: _NonEmptyStrings` | Exact IGN road-nature source values assigned to `GENERAL_MOTOR_ROAD` evidence. |
| `limited_motor_proxy` | `limited_motor_proxy: _NonEmptyStrings` | Exact IGN road-nature source values assigned to `LIMITED_MOTOR_PROXY` evidence. |
| `non_general_vehicle` | `non_general_vehicle: _NonEmptyStrings` | Exact IGN road-nature source values assigned to `NON_GENERAL_VEHICLE` evidence. |
| `special_review` | `special_review: _NonEmptyStrings` | Exact IGN road-nature source values assigned to `SPECIAL_REVIEW` evidence. |

**Validators (exact source)**

`_valid_groups`:

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

**Interface consumers**

- type annotation: `src/landscout/stages/road_vehicle_proxy_policy.py::_SourceValuesConfig` via `_RoadNatureConfig`.

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

**Purpose:** Validates the road contract carried by `known`, `limited`.

**Kind:** Pydantic model.

**Inheritance:** `_StrictPolicyModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `known` | `known: _NonEmptyStrings` | Exact IGN importance source values assigned to `KNOWN` evidence. |
| `limited` | `limited: _NonEmptyStrings` | Exact IGN importance source values assigned to `LIMITED` evidence. |

**Validators (exact source)**

`_valid_domain`:

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

**Interface consumers**

- type annotation: `src/landscout/stages/road_vehicle_proxy_policy.py::_SourceValuesConfig` via `_ImportanceConfig`.

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

**Purpose:** Validates the road contract carried by `asset_state`, `light_vehicle_access`, `nature`, `known_restriction_review`, `importance`, `width_below_m`.

**Kind:** Pydantic model.

**Inheritance:** `_StrictPolicyModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `asset_state` | `asset_state: _AssetStateConfig` | Compiled exact source-value group for road-policy field `asset_state`. |
| `light_vehicle_access` | `light_vehicle_access: _LightVehicleAccessConfig` | Compiled exact source-value group for road-policy field `light_vehicle_access`. |
| `nature` | `nature: _RoadNatureConfig` | Compiled exact source-value group for road-policy field `nature`. |
| `known_restriction_review` | `known_restriction_review: _NonEmptyStrings` | Compiled exact source-value group for road-policy field `known_restriction_review`. |
| `importance` | `importance: _ImportanceConfig` | Compiled exact source-value group for road-policy field `importance`. |
| `width_below_m` | `width_below_m: Annotated[StrictFloat, Field(gt=0, allow_inf_nan=False)]` | Compiled exact source-value group for road-policy field `width_below_m`. |

**Validators (exact source)**

`_valid_values`:

```python
def _valid_values(self) -> Self:
        _require_unique(
            self.known_restriction_review, "known_restriction_review"
        )
        return self
```

**Interface consumers**

- type annotation: `src/landscout/stages/road_vehicle_proxy_policy.py::_PolicyConfig` via `_SourceValuesConfig`.

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
        _require_unique(
            self.known_restriction_review, "known_restriction_review"
        )
        return self
```

### `_DecisionOutcomesConfig`

**Purpose:** Validates the road contract carried by `fictitious_geometry`, `project_geometry_not_significant`, `not_in_service`, `physically_impossible`, `non_general_vehicle_nature`, `rights_restricted`, `private_road`, `temporal_closure`, `known_restriction`, `other_recorded_restriction`, `special_nature`, `limited_nature`, `importance_6`, `narrow_carriageway`, `open_or_toll`, `unknown`.

**Kind:** Pydantic model.

**Inheritance:** `_StrictPolicyModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `fictitious_geometry` | `fictitious_geometry: Literal["NOT_DISTANCE_PROXY"]` | Road-proxy class selected when `FICTITIOUS_GEOMETRY` is the primary controlling rule. |
| `project_geometry_not_significant` | `project_geometry_not_significant: Literal["NOT_DISTANCE_PROXY"]` | Road-proxy class selected when `PROJECT_GEOMETRY_NOT_SIGNIFICANT` is the primary controlling rule. |
| `not_in_service` | `not_in_service: Literal["NOT_GENERAL_VEHICLE_PROXY"]` | Road-proxy class selected when `NOT_IN_SERVICE` is the primary controlling rule. |
| `physically_impossible` | `physically_impossible: Literal["NOT_GENERAL_VEHICLE_PROXY"]` | Road-proxy class selected when `PHYSICALLY_IMPOSSIBLE` is the primary controlling rule. |
| `non_general_vehicle_nature` | `non_general_vehicle_nature: Literal["NOT_GENERAL_VEHICLE_PROXY"]` | Road-proxy class selected when `NON_GENERAL_VEHICLE_NATURE` is the primary controlling rule. |
| `rights_restricted` | `rights_restricted: Literal["RESTRICTED_REVIEW"]` | Road-proxy class selected when `RIGHTS_RESTRICTED` is the primary controlling rule. |
| `private_road` | `private_road: Literal["RESTRICTED_REVIEW"]` | Road-proxy class selected when `PRIVATE_ROAD` is the primary controlling rule. |
| `temporal_closure` | `temporal_closure: Literal["RESTRICTED_REVIEW"]` | Road-proxy class selected when `TEMPORAL_CLOSURE` is the primary controlling rule. |
| `known_restriction` | `known_restriction: Literal["RESTRICTED_REVIEW"]` | Road-proxy class selected when `KNOWN_RESTRICTION` is the primary controlling rule. |
| `other_recorded_restriction` | `other_recorded_restriction: Literal["RESTRICTED_REVIEW"]` | Road-proxy class selected when `OTHER_RECORDED_RESTRICTION` is the primary controlling rule. |
| `special_nature` | `special_nature: Literal["RESTRICTED_REVIEW"]` | Road-proxy class selected when `SPECIAL_NATURE` is the primary controlling rule. |
| `limited_nature` | `limited_nature: Literal["LIMITED_VEHICLE_PROXY"]` | Road-proxy class selected when `LIMITED_NATURE` is the primary controlling rule. |
| `importance_6` | `importance_6: Literal["LIMITED_VEHICLE_PROXY"]` | Road-proxy class selected when `IMPORTANCE_6` is the primary controlling rule. |
| `narrow_carriageway` | `narrow_carriageway: Literal["LIMITED_VEHICLE_PROXY"]` | Road-proxy class selected when `NARROW_CARRIAGEWAY` is the primary controlling rule. |
| `open_or_toll` | `open_or_toll: Literal["GENERAL_VEHICLE_PROXY"]` | Road-proxy class selected when `OPEN_OR_TOLL` is the primary controlling rule. |
| `unknown` | `unknown: Literal["UNKNOWN_REVIEW"]` | Road-proxy class selected when `UNKNOWN` is the primary controlling rule. |

**Interface consumers**

- type annotation: `src/landscout/stages/road_vehicle_proxy_policy.py::_PolicyConfig` via `_DecisionOutcomesConfig`.

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

**Purpose:** Validates the road contract carried by `policy_id`, `schema_version`, `scope`, `references`, `evidence_checked_on`, `vehicle_scope`, `heavy_vehicle_access`, `classes`, `source_values`, `decision_precedence`, `decision_outcomes`.

**Kind:** Pydantic model.

**Inheritance:** `_StrictPolicyModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `policy_id` | `policy_id: _ExactString` | Versioned policy/profile identity or scope propagated to compiled/results rows and checked against the authoritative configuration bytes. |
| `schema_version` | `schema_version: StrictInt` | Strict compatibility version; the owning validator accepts only its documented supported integer. |
| `scope` | `scope: _ExactString` | `_PolicyConfig.scope` represents the `scope` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `references` | `references: _ReferencesConfig` | `_PolicyConfig.references` carries the references used by the reproduced constructors and validators; its declared type is `_ReferencesConfig` and no legal meaning is inferred beyond that owner. |
| `evidence_checked_on` | `evidence_checked_on: Literal["2026-08-16"]` | `_PolicyConfig.evidence_checked_on` carries the evidence checked on used by the reproduced constructors and validators; its declared type is `Literal['2026-08-16']` and no legal meaning is inferred beyond that owner. |
| `vehicle_scope` | `vehicle_scope: Literal["LIGHT_VEHICLE_AND_GENERAL_CAR_NETWORK"]` | `_PolicyConfig.vehicle_scope` represents the `vehicle_scope` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `heavy_vehicle_access` | `heavy_vehicle_access: Literal["NOT_PROVEN"]` | Explicit heavy-vehicle evidence state; current road policy requires NOT_PROVEN. |
| `classes` | `classes: _ClassesConfig` | `_PolicyConfig.classes` represents the `classes` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `source_values` | `source_values: _SourceValuesConfig` | Source fact or textual lineage named by the suffix; it becomes physical proof only where a validator rechecks bytes/source content. |
| `decision_precedence` | `decision_precedence: _NonEmptyStrings` | Complete ordered road-policy primary-rule precedence. |
| `decision_outcomes` | `decision_outcomes: _DecisionOutcomesConfig` | Configured mapping from every road-policy rule to its evidence class. |

**Validators (exact source)**

`_valid_identity_and_precedence`:

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

**Interface consumers**

- type annotation: `src/landscout/stages/road_vehicle_proxy_policy.py::_compile_policy` via `_PolicyConfig`.

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

**Purpose:** Immutable result/value envelope carrying `general_vehicle_proxy`, `limited_vehicle_proxy`, `restricted_review`, `not_general_vehicle_proxy`, `not_distance_proxy`, `unknown_review`.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `general_vehicle_proxy` | `general_vehicle_proxy: str` | Exact road-proxy output class configured for `general_vehicle_proxy` evidence. |
| `limited_vehicle_proxy` | `limited_vehicle_proxy: str` | Exact road-proxy output class configured for `limited_vehicle_proxy` evidence. |
| `restricted_review` | `restricted_review: str` | Exact road-proxy output class configured for `restricted_review` evidence. |
| `not_general_vehicle_proxy` | `not_general_vehicle_proxy: str` | Exact road-proxy output class configured for `not_general_vehicle_proxy` evidence. |
| `not_distance_proxy` | `not_distance_proxy: str` | Exact road-proxy output class configured for `not_distance_proxy` evidence. |
| `unknown_review` | `unknown_review: str` | Exact road-proxy output class configured for `unknown_review` evidence. |

**Interface consumers**

- type annotation: `src/landscout/stages/road_vehicle_proxy_policy.py::IgnRoadVehicleProxyPolicy` via `_CompiledClasses`.
- constructor call: `src/landscout/stages/road_vehicle_proxy_policy.py::_compile_policy` via `_CompiledClasses`.

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

**Purpose:** Immutable result/value envelope carrying `in_service`, `project_geometry_not_significant`, `under_construction`.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `in_service` | `in_service: frozenset[str]` | Structured `in service` collection owned by `_CompiledAssetState`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |
| `project_geometry_not_significant` | `project_geometry_not_significant: frozenset[str]` | Structured `project geometry not significant` collection owned by `_CompiledAssetState`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |
| `under_construction` | `under_construction: frozenset[str]` | Structured `under construction` collection owned by `_CompiledAssetState`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |

**Interface consumers**

- type annotation: `src/landscout/stages/road_vehicle_proxy_policy.py::IgnRoadVehicleProxyPolicy` via `_CompiledAssetState`.
- constructor call: `src/landscout/stages/road_vehicle_proxy_policy.py::_compile_policy` via `_CompiledAssetState`.

**Exact class source**

```python
class _CompiledAssetState:
    in_service: frozenset[str]
    project_geometry_not_significant: frozenset[str]
    under_construction: frozenset[str]
```

### `_CompiledNavigationReference`

**Purpose:** Immutable result/value envelope carrying `publisher`, `title`, `revision`, `evidence_scope`.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `publisher` | `publisher: str` | Publisher text reported by the owning source metadata or checked-in reference. |
| `title` | `title: str` | `_CompiledNavigationReference.title` carries the title used by the reproduced constructors and validators; its declared type is `str` and no legal meaning is inferred beyond that owner. |
| `revision` | `revision: str` | Revision identifier of the checked-in official reference snapshot. |
| `evidence_scope` | `evidence_scope: str` | `_CompiledNavigationReference.evidence_scope` represents the `evidence_scope` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |

**Interface consumers**

- type annotation: `src/landscout/stages/road_vehicle_proxy_policy.py::IgnRoadVehicleProxyPolicy` via `_CompiledNavigationReference`.
- constructor call: `src/landscout/stages/road_vehicle_proxy_policy.py::_compile_policy` via `_CompiledNavigationReference`.

**Exact class source**

```python
class _CompiledNavigationReference:
    publisher: str
    title: str
    revision: str
    evidence_scope: str
```

### `_CompiledBdTopoProductReference`

**Purpose:** Immutable result/value envelope carrying `publisher`, `title`, `document_id`, `revision`, `evidence_scope`.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `publisher` | `publisher: str` | Publisher text reported by the owning source metadata or checked-in reference. |
| `title` | `title: str` | `_CompiledBdTopoProductReference.title` carries the title used by the reproduced constructors and validators; its declared type is `str` and no legal meaning is inferred beyond that owner. |
| `document_id` | `document_id: str` | Exact identity for the entity named by the field; uniqueness, portability, and lineage meaning are only those explicitly validated by the owner. |
| `revision` | `revision: str` | Revision identifier of the checked-in official reference snapshot. |
| `evidence_scope` | `evidence_scope: str` | `_CompiledBdTopoProductReference.evidence_scope` represents the `evidence_scope` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |

**Interface consumers**

- type annotation: `src/landscout/stages/road_vehicle_proxy_policy.py::IgnRoadVehicleProxyPolicy` via `_CompiledBdTopoProductReference`.
- constructor call: `src/landscout/stages/road_vehicle_proxy_policy.py::_compile_policy` via `_CompiledBdTopoProductReference`.

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

**Purpose:** Immutable result/value envelope carrying `open`, `toll`, `rights_restricted`, `physically_impossible`.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `open` | `open: frozenset[str]` | Structured `open` collection owned by `_CompiledLightVehicleAccess`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |
| `toll` | `toll: frozenset[str]` | Structured `toll` collection owned by `_CompiledLightVehicleAccess`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |
| `rights_restricted` | `rights_restricted: frozenset[str]` | Structured `rights restricted` collection owned by `_CompiledLightVehicleAccess`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |
| `physically_impossible` | `physically_impossible: frozenset[str]` | Structured `physically impossible` collection owned by `_CompiledLightVehicleAccess`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |

**Interface consumers**

- type annotation: `src/landscout/stages/road_vehicle_proxy_policy.py::IgnRoadVehicleProxyPolicy` via `_CompiledLightVehicleAccess`.
- constructor call: `src/landscout/stages/road_vehicle_proxy_policy.py::_compile_policy` via `_CompiledLightVehicleAccess`.

**Exact class source**

```python
class _CompiledLightVehicleAccess:
    open: frozenset[str]
    toll: frozenset[str]
    rights_restricted: frozenset[str]
    physically_impossible: frozenset[str]
```

### `_CompiledRoadNature`

**Purpose:** Immutable result/value envelope carrying `general_motor_road`, `limited_motor_proxy`, `non_general_vehicle`, `special_review`.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `general_motor_road` | `general_motor_road: frozenset[str]` | Structured `general motor road` collection owned by `_CompiledRoadNature`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |
| `limited_motor_proxy` | `limited_motor_proxy: frozenset[str]` | Structured `limited motor proxy` collection owned by `_CompiledRoadNature`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |
| `non_general_vehicle` | `non_general_vehicle: frozenset[str]` | Structured `non general vehicle` collection owned by `_CompiledRoadNature`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |
| `special_review` | `special_review: frozenset[str]` | Structured `special review` collection owned by `_CompiledRoadNature`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |

**Interface consumers**

- type annotation: `src/landscout/stages/road_vehicle_proxy_policy.py::IgnRoadVehicleProxyPolicy` via `_CompiledRoadNature`.
- constructor call: `src/landscout/stages/road_vehicle_proxy_policy.py::_compile_policy` via `_CompiledRoadNature`.

**Exact class source**

```python
class _CompiledRoadNature:
    general_motor_road: frozenset[str]
    limited_motor_proxy: frozenset[str]
    non_general_vehicle: frozenset[str]
    special_review: frozenset[str]
```

### `_CompiledImportance`

**Purpose:** Immutable result/value envelope carrying `known`, `limited`.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `known` | `known: frozenset[str]` | Structured `known` collection owned by `_CompiledImportance`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |
| `limited` | `limited: frozenset[str]` | Structured `limited` collection owned by `_CompiledImportance`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |

**Interface consumers**

- type annotation: `src/landscout/stages/road_vehicle_proxy_policy.py::IgnRoadVehicleProxyPolicy` via `_CompiledImportance`.
- constructor call: `src/landscout/stages/road_vehicle_proxy_policy.py::_compile_policy` via `_CompiledImportance`.

**Exact class source**

```python
class _CompiledImportance:
    known: frozenset[str]
    limited: frozenset[str]
```

### `_CompiledDecisionOutcomes`

**Purpose:** Immutable result/value envelope carrying `fictitious_geometry`, `project_geometry_not_significant`, `not_in_service`, `physically_impossible`, `non_general_vehicle_nature`, `rights_restricted`, `private_road`, `temporal_closure`, `known_restriction`, `other_recorded_restriction`, `special_nature`, `limited_nature`, `importance_6`, `narrow_carriageway`, `open_or_toll`, `unknown`.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `fictitious_geometry` | `fictitious_geometry: str` | Road-proxy class selected when `FICTITIOUS_GEOMETRY` is the primary controlling rule. |
| `project_geometry_not_significant` | `project_geometry_not_significant: str` | Road-proxy class selected when `PROJECT_GEOMETRY_NOT_SIGNIFICANT` is the primary controlling rule. |
| `not_in_service` | `not_in_service: str` | Road-proxy class selected when `NOT_IN_SERVICE` is the primary controlling rule. |
| `physically_impossible` | `physically_impossible: str` | Road-proxy class selected when `PHYSICALLY_IMPOSSIBLE` is the primary controlling rule. |
| `non_general_vehicle_nature` | `non_general_vehicle_nature: str` | Road-proxy class selected when `NON_GENERAL_VEHICLE_NATURE` is the primary controlling rule. |
| `rights_restricted` | `rights_restricted: str` | Road-proxy class selected when `RIGHTS_RESTRICTED` is the primary controlling rule. |
| `private_road` | `private_road: str` | Road-proxy class selected when `PRIVATE_ROAD` is the primary controlling rule. |
| `temporal_closure` | `temporal_closure: str` | Road-proxy class selected when `TEMPORAL_CLOSURE` is the primary controlling rule. |
| `known_restriction` | `known_restriction: str` | Road-proxy class selected when `KNOWN_RESTRICTION` is the primary controlling rule. |
| `other_recorded_restriction` | `other_recorded_restriction: str` | Road-proxy class selected when `OTHER_RECORDED_RESTRICTION` is the primary controlling rule. |
| `special_nature` | `special_nature: str` | Road-proxy class selected when `SPECIAL_NATURE` is the primary controlling rule. |
| `limited_nature` | `limited_nature: str` | Road-proxy class selected when `LIMITED_NATURE` is the primary controlling rule. |
| `importance_6` | `importance_6: str` | Road-proxy class selected when `IMPORTANCE_6` is the primary controlling rule. |
| `narrow_carriageway` | `narrow_carriageway: str` | Road-proxy class selected when `NARROW_CARRIAGEWAY` is the primary controlling rule. |
| `open_or_toll` | `open_or_toll: str` | Road-proxy class selected when `OPEN_OR_TOLL` is the primary controlling rule. |
| `unknown` | `unknown: str` | Road-proxy class selected when `UNKNOWN` is the primary controlling rule. |

**Interface consumers**

- type annotation: `src/landscout/stages/road_vehicle_proxy_policy.py::IgnRoadVehicleProxyPolicy` via `_CompiledDecisionOutcomes`.
- constructor call: `src/landscout/stages/road_vehicle_proxy_policy.py::_compile_policy` via `_CompiledDecisionOutcomes`.

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

**Purpose:** Immutable policy evidence compiled from the exact checked-in YAML bytes.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `policy_id` | `policy_id: str` | Versioned policy/profile identity or scope propagated to compiled/results rows and checked against the authoritative configuration bytes. |
| `schema_version` | `schema_version: int` | Strict compatibility version; the owning validator accepts only its documented supported integer. |
| `scope` | `scope: str` | `IgnRoadVehicleProxyPolicy.scope` represents the `scope` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `navigation_reference` | `navigation_reference: _CompiledNavigationReference` | `IgnRoadVehicleProxyPolicy.navigation_reference` carries the navigation reference used by the reproduced constructors and validators; its declared type is `_CompiledNavigationReference` and no legal meaning is inferred beyond that owner. |
| `bdtopo_product_reference` | `bdtopo_product_reference: _CompiledBdTopoProductReference` | `IgnRoadVehicleProxyPolicy.bdtopo_product_reference` carries the bdtopo product reference used by the reproduced constructors and validators; its declared type is `_CompiledBdTopoProductReference` and no legal meaning is inferred beyond that owner. |
| `evidence_checked_on` | `evidence_checked_on: str` | `IgnRoadVehicleProxyPolicy.evidence_checked_on` carries the evidence checked on used by the reproduced constructors and validators; its declared type is `str` and no legal meaning is inferred beyond that owner. |
| `vehicle_scope` | `vehicle_scope: str` | `IgnRoadVehicleProxyPolicy.vehicle_scope` represents the `vehicle_scope` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `heavy_vehicle_access` | `heavy_vehicle_access: str` | Explicit heavy-vehicle evidence state; current road policy requires NOT_PROVEN. |
| `classes` | `classes: _CompiledClasses` | `IgnRoadVehicleProxyPolicy.classes` represents the `classes` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `asset_state` | `asset_state: _CompiledAssetState` | `IgnRoadVehicleProxyPolicy.asset_state` represents the `asset_state` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `light_vehicle_access` | `light_vehicle_access: _CompiledLightVehicleAccess` | Compiled exact IGN light-vehicle-access value groups used by the road proxy rules. |
| `nature` | `nature: _CompiledRoadNature` | Compiled exact IGN road-nature value groups used by the road proxy rules. |
| `known_restriction_review` | `known_restriction_review: frozenset[str]` | Structured `known restriction review` collection owned by `IgnRoadVehicleProxyPolicy`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |
| `importance` | `importance: _CompiledImportance` | Compiled exact IGN importance value groups used by the road proxy rules. |
| `width_below_m` | `width_below_m: float` | Metre quantity represented by `IgnRoadVehicleProxyPolicy.width_below_m`; the owning declaration and calculation/validation shown below define whether it is a measurement, distance, or threshold. |
| `decision_precedence` | `decision_precedence: tuple[str, ...]` | Complete ordered road-policy primary-rule precedence. |
| `decision_outcomes` | `decision_outcomes: _CompiledDecisionOutcomes` | Configured mapping from every road-policy rule to its evidence class. |
| `config_sha256` | `config_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |

**Interface consumers**

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyPolicy,
    IgnRoadVehicleProxyPolicyError,
    load_ign_road_vehicle_proxy_policy,
)`.
- import: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::<module>` via `from landscout.stages.road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyPolicy,
    load_ign_road_vehicle_proxy_policy,
)`.
- import: `src/landscout/stages/assess_road_proximity_coverage.py::<module>` via `from landscout.stages.road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyPolicy,
    load_ign_road_vehicle_proxy_policy,
)`.
- import: `src/landscout/stages/enrich_road_proximity.py::<module>` via `from landscout.stages.road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyPolicy,
    load_ign_road_vehicle_proxy_policy,
)`.
- import: `tests/unit/test_road_vehicle_proxy_policy.py::<module>` via `from landscout.stages.road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyPolicy,
    IgnRoadVehicleProxyPolicyError,
    load_ign_road_vehicle_proxy_policy,
)`.
- type annotation: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::_rule_outcomes` via `IgnRoadVehicleProxyPolicy`.
- type annotation: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::_classify_road_frame` via `IgnRoadVehicleProxyPolicy`.
- type annotation: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_class_coverage` via `IgnRoadVehicleProxyPolicy`.
- type annotation: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_upstream_result` via `IgnRoadVehicleProxyPolicy`.
- type annotation: `src/landscout/stages/enrich_road_proximity.py::_policy_classes` via `IgnRoadVehicleProxyPolicy`.
- type annotation: `src/landscout/stages/enrich_road_proximity.py::_require_row_lineage` via `IgnRoadVehicleProxyPolicy`.
- type annotation: `src/landscout/stages/enrich_road_proximity.py::_validate_application_roads` via `IgnRoadVehicleProxyPolicy`.
- type annotation: `src/landscout/stages/enrich_road_proximity.py::_coverage` via `IgnRoadVehicleProxyPolicy`.
- type annotation: `src/landscout/stages/enrich_road_proximity.py::_class_proximity_table` via `IgnRoadVehicleProxyPolicy`.
- type annotation: `src/landscout/stages/enrich_road_proximity.py::_validate_coverage` via `IgnRoadVehicleProxyPolicy`.
- type annotation: `src/landscout/stages/enrich_road_proximity.py::_validate_result` via `IgnRoadVehicleProxyPolicy`.
- type annotation: `src/landscout/stages/road_vehicle_proxy_policy.py::_compile_policy` via `IgnRoadVehicleProxyPolicy`.
- constructor call: `src/landscout/stages/road_vehicle_proxy_policy.py::_compile_policy` via `IgnRoadVehicleProxyPolicy`.
- type annotation: `src/landscout/stages/road_vehicle_proxy_policy.py::load_ign_road_vehicle_proxy_policy` via `IgnRoadVehicleProxyPolicy`.
- type annotation: `tests/unit/test_road_vehicle_proxy_policy.py::_load_payload` via `IgnRoadVehicleProxyPolicy`.

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

### `_UniqueKeyLoader`

**Purpose:** Private PyYAML SafeLoader subclass whose mapping constructor is replaced to reject duplicate YAML keys.

**Kind:** PyYAML loader subclass.

**Inheritance:** `yaml.SafeLoader`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- No repository construction/import/property/decorator reference was found; the exact declaration is retained because it participates in the module's runtime/framework namespace.

**Exact class source**

```python
class _UniqueKeyLoader(yaml.SafeLoader):
    pass
```


## 6. Functions and methods

### `_exact_string`

**Exact signature**

```python
def _exact_string(value: str) -> str:
```

**Purpose**

Private `road` helper for exact string; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
value
```

**Validation and exceptions**

- Guard with a raise path: `value != value.strip()`.
- Explicit raise expressions: `ValueError('policy strings must not contain edge whitespace')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- function object argument: `src/landscout/stages/road_vehicle_proxy_policy.py::<module>` via `AfterValidator(_exact_string)`.

**Complete source-ordered implementation**

```python
def _exact_string(value: str) -> str:
    if value != value.strip():
        raise ValueError("policy strings must not contain edge whitespace")
    return value
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_require_unique`

**Exact signature**

```python
def _require_unique(values: tuple[str, ...], label: str) -> None:
```

**Purpose**

Private `road` helper for require unique; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `len(values) != len(set(values))`.
- Explicit raise expressions: `ValueError(f'{label} contains duplicate source values')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/road_vehicle_proxy_policy.py::_AssetStateConfig._valid_groups` via `_require_unique`.
- direct call: `src/landscout/stages/road_vehicle_proxy_policy.py::_LightVehicleAccessConfig._valid_groups` via `_require_unique`.
- direct call: `src/landscout/stages/road_vehicle_proxy_policy.py::_RoadNatureConfig._valid_groups` via `_require_unique`.
- direct call: `src/landscout/stages/road_vehicle_proxy_policy.py::_ImportanceConfig._valid_domain` via `_require_unique`.
- direct call: `src/landscout/stages/road_vehicle_proxy_policy.py::_SourceValuesConfig._valid_values` via `_require_unique`.

**Complete source-ordered implementation**

```python
def _require_unique(values: tuple[str, ...], label: str) -> None:
    if len(values) != len(set(values)):
        raise ValueError(f"{label} contains duplicate source values")
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_require_disjoint`

**Exact signature**

```python
def _require_disjoint(groups: tuple[tuple[str, ...], ...], label: str) -> None:
```

**Purpose**

Private `road` helper for require disjoint; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `len(flattened) != len(set(flattened))`.
- Explicit raise expressions: `ValueError(f'{label} source groups overlap')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/road_vehicle_proxy_policy.py::_AssetStateConfig._valid_groups` via `_require_disjoint`.
- direct call: `src/landscout/stages/road_vehicle_proxy_policy.py::_LightVehicleAccessConfig._valid_groups` via `_require_disjoint`.
- direct call: `src/landscout/stages/road_vehicle_proxy_policy.py::_RoadNatureConfig._valid_groups` via `_require_disjoint`.

**Complete source-ordered implementation**

```python
def _require_disjoint(groups: tuple[tuple[str, ...], ...], label: str) -> None:
    flattened = tuple(value for group in groups for value in group)
    if len(flattened) != len(set(flattened)):
        raise ValueError(f"{label} source groups overlap")
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_AssetStateConfig._valid_groups`

**Exact signature**

```python
def _valid_groups(self) -> Self:
```

**Purpose**

Private `road` helper for valid groups; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `Self`.
- Every observed return expression is reproduced without truncation:
```python
self
```

**Validation and exceptions**

- Guard with a raise path: `groups != (('En service',), ('En projet',), ('En construction',))`.
- Explicit raise expressions: `ValueError('asset_state groups must cover the exact source domain')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

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

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_LightVehicleAccessConfig._valid_groups`

**Exact signature**

```python
def _valid_groups(self) -> Self:
```

**Purpose**

Private `road` helper for valid groups; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `Self`.
- Every observed return expression is reproduced without truncation:
```python
self
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

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

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_RoadNatureConfig._valid_groups`

**Exact signature**

```python
def _valid_groups(self) -> Self:
```

**Purpose**

Private `road` helper for valid groups; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `Self`.
- Every observed return expression is reproduced without truncation:
```python
self
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

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

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_ImportanceConfig._valid_domain`

**Exact signature**

```python
def _valid_domain(self) -> Self:
```

**Purpose**

Private `road` helper for valid domain; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `Self`.
- Every observed return expression is reproduced without truncation:
```python
self
```

**Validation and exceptions**

- Guard with a raise path: `self.known != ('1', '2', '3', '4', '5', '6')`.
- Guard with a raise path: `self.limited != ('6',)`.
- Guard with a raise path: `not set(self.limited).issubset(self.known)`.
- Explicit raise expressions: `ValueError("importance.limited must contain exactly source value '6'")`, `ValueError('importance.known must cover exactly source values 1-6')`, `ValueError('importance.limited must be a subset of importance.known')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

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

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_SourceValuesConfig._valid_values`

**Exact signature**

```python
def _valid_values(self) -> Self:
```

**Purpose**

Private `road` helper for valid values; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `Self`.
- Every observed return expression is reproduced without truncation:
```python
self
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

**Complete source-ordered implementation**

```python
def _valid_values(self) -> Self:
        _require_unique(
            self.known_restriction_review, "known_restriction_review"
        )
        return self
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_PolicyConfig._valid_identity_and_precedence`

**Exact signature**

```python
def _valid_identity_and_precedence(self) -> Self:
```

**Purpose**

Private `road` helper for valid identity and precedence; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `Self`.
- Every observed return expression is reproduced without truncation:
```python
self
```

**Validation and exceptions**

- Guard with a raise path: `self.policy_id != _POLICY_ID`.
- Guard with a raise path: `self.schema_version != 2`.
- Guard with a raise path: `self.scope != _POLICY_SCOPE`.
- Guard with a raise path: `self.decision_precedence != _EXPECTED_PRECEDENCE`.
- Explicit raise expressions: `ValueError('decision_precedence differs from approved v2 order')`, `ValueError('policy_id is not the approved v2 policy identity')`, `ValueError('schema_version must be exactly 2')`, `ValueError('scope is not the approved official IGN evidence scope')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

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

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_CompiledClasses.values`

**Exact signature**

```python
def values(self) -> tuple[str, ...]:
```

**Purpose**

Private `road` helper for values; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[str, ...]`.
- Every observed return expression is reproduced without truncation:
```python
(self.general_vehicle_proxy, self.limited_vehicle_proxy, self.restricted_review, self.not_general_vehicle_proxy, self.not_distance_proxy, self.unknown_review)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

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

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_construct_unique_mapping`

**Exact signature**

```python
def _construct_unique_mapping(
    loader: yaml.SafeLoader,
    node: yaml.MappingNode,
    deep: bool = False,
) -> dict[object, object]:
```

**Purpose**

Private `road` helper for construct unique mapping; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict[object, object]`.
- Every observed return expression is reproduced without truncation:
```python
result
```

**Validation and exceptions**

- Guard with a raise path: `key in result`.
- Explicit raise expressions: `IgnRoadVehicleProxyPolicyError(f'Duplicate YAML road-policy key: {key!r}')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `result[key]`.
- Input mutation: none.

**Repository interfaces and consumers**

- function object argument: `src/landscout/stages/road_vehicle_proxy_policy.py::<module>` via `_UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_unique_mapping)`.

**Complete source-ordered implementation**

```python
def _construct_unique_mapping(
    loader: yaml.SafeLoader,
    node: yaml.MappingNode,
    deep: bool = False,
) -> dict[object, object]:
    result: dict[object, object] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise IgnRoadVehicleProxyPolicyError(
                f"Duplicate YAML road-policy key: {key!r}"
            )
        result[key] = loader.construct_object(value_node, deep=deep)
    return result
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_compile_policy`

**Exact signature**

```python
def _compile_policy(
    config: _PolicyConfig,
    config_sha256: str,
) -> IgnRoadVehicleProxyPolicy:
```

**Purpose**

Validates and compiles policy; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `IgnRoadVehicleProxyPolicy`.
- Every observed return expression is reproduced without truncation:
```python
IgnRoadVehicleProxyPolicy(policy_id=config.policy_id, schema_version=config.schema_version, scope=config.scope, navigation_reference=_CompiledNavigationReference(publisher=config.references.navigation.publisher, title=config.references.navigation.title, revision=config.references.navigation.revision, evidence_scope=config.references.navigation.evidence_scope), bdtopo_product_reference=_CompiledBdTopoProductReference(publisher=config.references.bdtopo_product.publisher, title=config.references.bdtopo_product.title, document_id=config.references.bdtopo_product.document_id, revision=config.references.bdtopo_product.revision, evidence_scope=config.references.bdtopo_product.evidence_scope), evidence_checked_on=config.evidence_checked_on, vehicle_scope=config.vehicle_scope, heavy_vehicle_access=config.heavy_vehicle_access, classes=_CompiledClasses(general_vehicle_proxy=classes.general_vehicle_proxy, limited_vehicle_proxy=classes.limited_vehicle_proxy, restricted_review=classes.restricted_review, not_general_vehicle_proxy=classes.not_general_vehicle_proxy, not_distance_proxy=classes.not_distance_proxy, unknown_review=classes.unknown_review), asset_state=_CompiledAssetState(in_service=frozenset(source_values.asset_state.in_service), project_geometry_not_significant=frozenset(source_values.asset_state.project_geometry_not_significant), under_construction=frozenset(source_values.asset_state.under_construction)), light_vehicle_access=_CompiledLightVehicleAccess(open=frozenset(access.open), toll=frozenset(access.toll), rights_restricted=frozenset(access.rights_restricted), physically_impossible=frozenset(access.physically_impossible)), nature=_CompiledRoadNature(general_motor_road=frozenset(nature.general_motor_road), limited_motor_proxy=frozenset(nature.limited_motor_proxy), non_general_vehicle=frozenset(nature.non_general_vehicle), special_review=frozenset(nature.special_review)), known_restriction_review=frozenset(source_values.known_restriction_review), importance=_CompiledImportance(known=frozenset(source_values.importance.known), limited=frozenset(source_values.importance.limited)), width_below_m=source_values.width_below_m, decision_precedence=config.decision_precedence, decision_outcomes=_CompiledDecisionOutcomes(fictitious_geometry=outcomes.fictitious_geometry, project_geometry_not_significant=outcomes.project_geometry_not_significant, not_in_service=outcomes.not_in_service, physically_impossible=outcomes.physically_impossible, non_general_vehicle_nature=outcomes.non_general_vehicle_nature, rights_restricted=outcomes.rights_restricted, private_road=outcomes.private_road, temporal_closure=outcomes.temporal_closure, known_restriction=outcomes.known_restriction, other_recorded_restriction=outcomes.other_recorded_restriction, special_nature=outcomes.special_nature, limited_nature=outcomes.limited_nature, importance_6=outcomes.importance_6, narrow_carriageway=outcomes.narrow_carriageway, open_or_toll=outcomes.open_or_toll, unknown=outcomes.unknown), config_sha256=config_sha256)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/road_vehicle_proxy_policy.py::load_ign_road_vehicle_proxy_policy` via `_compile_policy`.

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
        known_restriction_review=frozenset(
            source_values.known_restriction_review
        ),
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

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `load_ign_road_vehicle_proxy_policy`

**Exact signature**

```python
def load_ign_road_vehicle_proxy_policy(
    path: Path = _DEFAULT_POLICY_PATH,
) -> IgnRoadVehicleProxyPolicy:
```

**Purpose**

Load and compile the strict policy from its exact UTF-8 file bytes.

**Return contract**

- Declared return annotation: `IgnRoadVehicleProxyPolicy`.
- Every observed return expression is reproduced without truncation:
```python
_compile_policy(config, sha256(policy_bytes).hexdigest())
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(payload, Mapping)`.
- Explicit raise expressions: `IgnRoadVehicleProxyPolicyError('IGN road vehicle-proxy policy is invalid')`, `IgnRoadVehicleProxyPolicyError('IGN road vehicle-proxy policy must be a mapping')`, `re-raise`.

**Side effects**

- Network I/O: none.
- Filesystem read: `Path(path).read_bytes`.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `sha256`, `sha256(policy_bytes).hexdigest`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyPolicy,
    IgnRoadVehicleProxyPolicyError,
    load_ign_road_vehicle_proxy_policy,
)`.
- import: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::<module>` via `from landscout.stages.road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyPolicy,
    load_ign_road_vehicle_proxy_policy,
)`.
- import: `src/landscout/stages/assess_road_proximity_coverage.py::<module>` via `from landscout.stages.road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyPolicy,
    load_ign_road_vehicle_proxy_policy,
)`.
- import: `src/landscout/stages/enrich_road_proximity.py::<module>` via `from landscout.stages.road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyPolicy,
    load_ign_road_vehicle_proxy_policy,
)`.
- import: `tests/unit/test_apply_road_vehicle_proxy_policy.py::<module>` via `from landscout.stages.road_vehicle_proxy_policy import (
    load_ign_road_vehicle_proxy_policy,
)`.
- import: `tests/unit/test_assess_road_proximity_coverage.py::<module>` via `from landscout.stages.road_vehicle_proxy_policy import (
    load_ign_road_vehicle_proxy_policy,
)`.
- import: `tests/unit/test_enrich_road_proximity.py::<module>` via `from landscout.stages.road_vehicle_proxy_policy import (
    load_ign_road_vehicle_proxy_policy,
)`.
- import: `tests/unit/test_road_vehicle_proxy_policy.py::<module>` via `from landscout.stages.road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyPolicy,
    IgnRoadVehicleProxyPolicyError,
    load_ign_road_vehicle_proxy_policy,
)`.
- direct call: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::_apply_ign_road_vehicle_proxy_policy` via `load_ign_road_vehicle_proxy_policy`.
- direct call: `src/landscout/stages/assess_road_proximity_coverage.py::_assess_road_proximity_coverage` via `load_ign_road_vehicle_proxy_policy`.
- direct call: `src/landscout/stages/enrich_road_proximity.py::_enrich_parcel_road_proximity` via `load_ign_road_vehicle_proxy_policy`.
- direct call: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_every_configured_known_restriction_is_applied` via `load_ign_road_vehicle_proxy_policy`.
- direct call: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_policy_lineage_is_exact_on_every_row` via `load_ign_road_vehicle_proxy_policy`.
- direct call: `tests/unit/test_assess_road_proximity_coverage.py::_proximity` via `load_ign_road_vehicle_proxy_policy`.
- direct call: `tests/unit/test_enrich_road_proximity.py::_road_row` via `load_ign_road_vehicle_proxy_policy`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_selected_road_evidence_and_lineage_are_exact` via `load_ign_road_vehicle_proxy_policy`.
- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::_load_payload` via `load_ign_road_vehicle_proxy_policy`.
- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_checked_in_policy_loads_with_exact_public_identity_and_reference` via `load_ign_road_vehicle_proxy_policy`.
- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_checked_in_policy_hash_binds_exact_file_bytes` via `load_ign_road_vehicle_proxy_policy`.
- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_repeat_loading_is_deterministic_and_independent` via `load_ign_road_vehicle_proxy_policy`.
- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_asset_state_groups_cover_exact_v2_domain` via `load_ign_road_vehicle_proxy_policy`.
- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_importance_domains_expose_known_without_positive_classification` via `load_ign_road_vehicle_proxy_policy`.
- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_decision_precedence_and_rule_outcomes_are_approved` via `load_ign_road_vehicle_proxy_policy`.
- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_project_geometry_rule_has_exact_precedence_position` via `load_ign_road_vehicle_proxy_policy`.
- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_approved_class_vocabulary_has_no_heavy_or_legal_claim` via `load_ign_road_vehicle_proxy_policy`.
- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_observed_d031_natures_are_covered_exactly_once` via `load_ign_road_vehicle_proxy_policy`.
- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_observed_d031_access_and_importance_vocabularies_are_compatible` via `load_ign_road_vehicle_proxy_policy`.
- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_compiled_policy_structures_are_immutable` via `load_ign_road_vehicle_proxy_policy`.
- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_mutating_source_payload_cannot_affect_another_load` via `load_ign_road_vehicle_proxy_policy`.
- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_malformed_yaml_has_controlled_error` via `load_ign_road_vehicle_proxy_policy`.
- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_missing_file_has_controlled_error` via `load_ign_road_vehicle_proxy_policy`.

**Complete source-ordered implementation**

```python
def load_ign_road_vehicle_proxy_policy(
    path: Path = _DEFAULT_POLICY_PATH,
) -> IgnRoadVehicleProxyPolicy:
    """Load and compile the strict policy from its exact UTF-8 file bytes."""

    try:
        policy_bytes = Path(path).read_bytes()
        payload = yaml.load(
            policy_bytes.decode("utf-8"),
            Loader=_UniqueKeyLoader,
        )
        if not isinstance(payload, Mapping):
            raise IgnRoadVehicleProxyPolicyError(
                "IGN road vehicle-proxy policy must be a mapping"
            )
        config = _PolicyConfig.model_validate(payload)
        return _compile_policy(config, sha256(policy_bytes).hexdigest())
    except IgnRoadVehicleProxyPolicyError:
        raise
    except Exception as error:
        raise IgnRoadVehicleProxyPolicyError(
            "IGN road vehicle-proxy policy is invalid"
        ) from error
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.


## 7. Data contracts

No module-level canonical frame schema, mapping, or dtype declaration is present. Any frame interaction is recoverable from the complete function implementations below; no string literal is promoted to a column merely because it appears in code.

No enum/status/Literal value is classified as a column unless it is separately present in a canonical schema declaration. Mapping keys, JSON keys, dataclass fields, and configuration leaves remain distinct categories.

## 8. Interfaces

This module defines an exact `__all__` contract:

| Export | Kind | Origin | Included in `__all__` |
|---|---|---|---|
| `IgnRoadVehicleProxyPolicy` | public symbol defined in this module | `defined in `src/landscout/stages/road_vehicle_proxy_policy.py`` | yes |
| `IgnRoadVehicleProxyPolicyError` | public symbol defined in this module | `defined in `src/landscout/stages/road_vehicle_proxy_policy.py`` | yes |
| `load_ign_road_vehicle_proxy_policy` | public symbol defined in this module | `defined in `src/landscout/stages/road_vehicle_proxy_policy.py`` | yes |

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

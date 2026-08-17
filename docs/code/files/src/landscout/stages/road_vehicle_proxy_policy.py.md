# `src/landscout/stages/road_vehicle_proxy_policy.py`

## File identity

- Repository path: `src/landscout/stages/road_vehicle_proxy_policy.py`
- File type: Python source
- Layer: processing/policy stage
- Domain: road
- Responsibility: Loads and compiles the checked-in general-car/light-vehicle IGN road evidence policy.
- Source SHA256: `73b7315bf37c48510fbb8e63c28272349fa0407f1c0c5adea91142a74c481286`

## 1. Purpose

Loads and compiles the checked-in general-car/light-vehicle IGN road evidence policy.

## 2. Position in LandScout architecture

This file belongs to the **processing/policy stage** layer and the **road** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

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

Module-level technical/source/policy constant consumed by the exact references below.

#### `_POLICY_SCOPE`

```python
_POLICY_SCOPE = "OFFICIAL_IGN_CAR_ROUTING_EVIDENCE_ONLY"
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema.

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

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema.


### B. Type aliases and closed domains

#### `_ExactString`

```python
_ExactString = Annotated[
    str,
    StringConstraints(strict=True, min_length=1),
    AfterValidator(_exact_string),
]
```

Annotated validation alias whose strictness, regex/bounds, and callbacks are exactly those shown above. It is consumed by annotations or Pydantic validation in this module.

#### `_NonEmptyStrings`

```python
_NonEmptyStrings = Annotated[tuple[_ExactString, ...], Field(min_length=1)]
```

Annotated validation alias whose strictness, regex/bounds, and callbacks are exactly those shown above. It is consumed by annotations or Pydantic validation in this module.


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

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyPolicy,
    IgnRoadVehicleProxyPolicyError,
    load_ign_road_vehicle_proxy_policy,
)`.
- direct call or construction: `src/landscout/stages/road_vehicle_proxy_policy.py::_construct_unique_mapping` via `IgnRoadVehicleProxyPolicyError`.
- direct call or construction: `src/landscout/stages/road_vehicle_proxy_policy.py::load_ign_road_vehicle_proxy_policy` via `IgnRoadVehicleProxyPolicyError`.
- callback/function object: `tests/unit/test_road_vehicle_proxy_policy.py::test_invalid_config_structure_is_rejected` via `pytest.raises(IgnRoadVehicleProxyPolicyError, match=message)`.
- callback/function object: `tests/unit/test_road_vehicle_proxy_policy.py::test_unsupported_schema_version_is_rejected` via `pytest.raises(IgnRoadVehicleProxyPolicyError)`.
- callback/function object: `tests/unit/test_road_vehicle_proxy_policy.py::test_wrong_policy_identity_is_rejected` via `pytest.raises(IgnRoadVehicleProxyPolicyError)`.
- callback/function object: `tests/unit/test_road_vehicle_proxy_policy.py::test_both_evidence_references_are_required` via `pytest.raises(IgnRoadVehicleProxyPolicyError)`.
- callback/function object: `tests/unit/test_road_vehicle_proxy_policy.py::test_product_reference_document_id_is_exact` via `pytest.raises(IgnRoadVehicleProxyPolicyError)`.
- callback/function object: `tests/unit/test_road_vehicle_proxy_policy.py::test_unknown_evidence_reference_is_rejected` via `pytest.raises(IgnRoadVehicleProxyPolicyError)`.
- callback/function object: `tests/unit/test_road_vehicle_proxy_policy.py::test_asset_state_group_overlap_is_rejected` via `pytest.raises(IgnRoadVehicleProxyPolicyError)`.
- callback/function object: `tests/unit/test_road_vehicle_proxy_policy.py::test_missing_known_asset_state_is_rejected` via `pytest.raises(IgnRoadVehicleProxyPolicyError)`.
- callback/function object: `tests/unit/test_road_vehicle_proxy_policy.py::test_unknown_additional_asset_state_is_rejected` via `pytest.raises(IgnRoadVehicleProxyPolicyError)`.
- callback/function object: `tests/unit/test_road_vehicle_proxy_policy.py::test_semantic_values_must_be_exact_non_empty_strings` via `pytest.raises(IgnRoadVehicleProxyPolicyError)`.
- callback/function object: `tests/unit/test_road_vehicle_proxy_policy.py::test_duplicate_semantic_value_is_rejected` via `pytest.raises(IgnRoadVehicleProxyPolicyError, match='invalid')`.
- callback/function object: `tests/unit/test_road_vehicle_proxy_policy.py::test_semantic_groups_must_be_pairwise_disjoint` via `pytest.raises(IgnRoadVehicleProxyPolicyError, match='invalid')`.
- callback/function object: `tests/unit/test_road_vehicle_proxy_policy.py::test_duplicate_known_restriction_is_rejected` via `pytest.raises(IgnRoadVehicleProxyPolicyError)`.
- callback/function object: `tests/unit/test_road_vehicle_proxy_policy.py::test_invalid_width_threshold_is_rejected` via `pytest.raises(IgnRoadVehicleProxyPolicyError)`.
- callback/function object: `tests/unit/test_road_vehicle_proxy_policy.py::test_importance_domains_must_be_exact` via `pytest.raises(IgnRoadVehicleProxyPolicyError)`.
- callback/function object: `tests/unit/test_road_vehicle_proxy_policy.py::test_decision_precedence_must_be_exact` via `pytest.raises(IgnRoadVehicleProxyPolicyError)`.
- callback/function object: `tests/unit/test_road_vehicle_proxy_policy.py::test_output_class_vocabulary_must_be_exact` via `pytest.raises(IgnRoadVehicleProxyPolicyError)`.
- callback/function object: `tests/unit/test_road_vehicle_proxy_policy.py::test_malformed_yaml_has_controlled_error` via `pytest.raises(IgnRoadVehicleProxyPolicyError)`.
- callback/function object: `tests/unit/test_road_vehicle_proxy_policy.py::test_non_mapping_yaml_has_controlled_error` via `pytest.raises(IgnRoadVehicleProxyPolicyError)`.
- callback/function object: `tests/unit/test_road_vehicle_proxy_policy.py::test_missing_file_has_controlled_error` via `pytest.raises(IgnRoadVehicleProxyPolicyError)`.
- import/re-export: `tests/unit/test_road_vehicle_proxy_policy.py::<module>` via `from landscout.stages.road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyPolicy,
    IgnRoadVehicleProxyPolicyError,
    load_ign_road_vehicle_proxy_policy,
)`.

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
| `publisher` | `publisher: Literal["IGN"]` | Stores `_NavigationReferenceConfig`'s `publisher` value under exact annotation `Literal['IGN']`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `title` | `title: Literal["Calcul d’itinéraire"]` | `_NavigationReferenceConfig`'s `title` evidence/text field; it retains the exact configured or source meaning under annotation `Literal['Calcul d’itinéraire']` and is not promoted to a legal conclusion. |
| `revision` | `revision: Literal["2026-05-27"]` | Stores `_NavigationReferenceConfig`'s `revision` value under exact annotation `Literal['2026-05-27']`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `evidence_scope` | `evidence_scope: Literal["GENERAL_CAR_ROUTING_RULES"]` | Closed or validated `evidence scope` classification on `_NavigationReferenceConfig`; accepted values and downstream branches are recoverable from the reproduced validators and consumers. |

**Interface consumers**

- Pydantic constructs this model during direct/model_validate or nested-model validation; its exact validators and the module's loader/build functions below define the active framework entry points.

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
| `publisher` | `publisher: Literal["IGN"]` | Stores `_BdTopoProductReferenceConfig`'s `publisher` value under exact annotation `Literal['IGN']`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `title` | `title: Literal["BD TOPO® Version 3.5 - Descriptif de contenu"]` | `_BdTopoProductReferenceConfig`'s `title` evidence/text field; it retains the exact configured or source meaning under annotation `Literal['BD TOPO® Version 3.5 - Descriptif de contenu']` and is not promoted to a legal conclusion. |
| `document_id` | `document_id: Literal["DC_BDTOPO_3-5"]` | Exact identity for the entity named by the field; uniqueness, portability, and lineage meaning are only those explicitly validated by the owner. |
| `revision` | `revision: Literal["2025-11"]` | Stores `_BdTopoProductReferenceConfig`'s `revision` value under exact annotation `Literal['2025-11']`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `evidence_scope` | `evidence_scope: Literal["SOURCE_ATTRIBUTE_SEMANTICS"]` | Closed or validated `evidence scope` classification on `_BdTopoProductReferenceConfig`; accepted values and downstream branches are recoverable from the reproduced validators and consumers. |

**Interface consumers**

- Pydantic constructs this model during direct/model_validate or nested-model validation; its exact validators and the module's loader/build functions below define the active framework entry points.

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
| `navigation` | `navigation: _NavigationReferenceConfig` | Stores `_ReferencesConfig`'s `navigation` value under exact annotation `_NavigationReferenceConfig`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `bdtopo_product` | `bdtopo_product: _BdTopoProductReferenceConfig` | Stores `_ReferencesConfig`'s `bdtopo product` value under exact annotation `_BdTopoProductReferenceConfig`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |

**Interface consumers**

- Pydantic constructs this model during direct/model_validate or nested-model validation; its exact validators and the module's loader/build functions below define the active framework entry points.

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
| `general_vehicle_proxy` | `general_vehicle_proxy: Literal["GENERAL_VEHICLE_PROXY"]` | Stores `_ClassesConfig`'s `general vehicle proxy` value under exact annotation `Literal['GENERAL_VEHICLE_PROXY']`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `limited_vehicle_proxy` | `limited_vehicle_proxy: Literal["LIMITED_VEHICLE_PROXY"]` | Stores `_ClassesConfig`'s `limited vehicle proxy` value under exact annotation `Literal['LIMITED_VEHICLE_PROXY']`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `restricted_review` | `restricted_review: Literal["RESTRICTED_REVIEW"]` | Stores `_ClassesConfig`'s `restricted review` value under exact annotation `Literal['RESTRICTED_REVIEW']`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `not_general_vehicle_proxy` | `not_general_vehicle_proxy: Literal["NOT_GENERAL_VEHICLE_PROXY"]` | Stores `_ClassesConfig`'s `not general vehicle proxy` value under exact annotation `Literal['NOT_GENERAL_VEHICLE_PROXY']`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `not_distance_proxy` | `not_distance_proxy: Literal["NOT_DISTANCE_PROXY"]` | Stores `_ClassesConfig`'s `not distance proxy` value under exact annotation `Literal['NOT_DISTANCE_PROXY']`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `unknown_review` | `unknown_review: Literal["UNKNOWN_REVIEW"]` | Stores `_ClassesConfig`'s `unknown review` value under exact annotation `Literal['UNKNOWN_REVIEW']`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |

**Interface consumers**

- Pydantic constructs this model during direct/model_validate or nested-model validation; its exact validators and the module's loader/build functions below define the active framework entry points.

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
| `in_service` | `in_service: _NonEmptyStrings` | Stores `_AssetStateConfig`'s `in service` value under exact annotation `_NonEmptyStrings`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `project_geometry_not_significant` | `project_geometry_not_significant: _NonEmptyStrings` | Stores `_AssetStateConfig`'s `project geometry not significant` value under exact annotation `_NonEmptyStrings`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `under_construction` | `under_construction: _NonEmptyStrings` | Stores `_AssetStateConfig`'s `under construction` value under exact annotation `_NonEmptyStrings`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |

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

- Pydantic constructs this model during direct/model_validate or nested-model validation; its exact validators and the module's loader/build functions below define the active framework entry points.

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
| `open` | `open: _NonEmptyStrings` | Stores `_LightVehicleAccessConfig`'s `open` value under exact annotation `_NonEmptyStrings`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `toll` | `toll: _NonEmptyStrings` | Stores `_LightVehicleAccessConfig`'s `toll` value under exact annotation `_NonEmptyStrings`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `rights_restricted` | `rights_restricted: _NonEmptyStrings` | Stores `_LightVehicleAccessConfig`'s `rights restricted` value under exact annotation `_NonEmptyStrings`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `physically_impossible` | `physically_impossible: _NonEmptyStrings` | Stores `_LightVehicleAccessConfig`'s `physically impossible` value under exact annotation `_NonEmptyStrings`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |

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

- Pydantic constructs this model during direct/model_validate or nested-model validation; its exact validators and the module's loader/build functions below define the active framework entry points.

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
| `general_motor_road` | `general_motor_road: _NonEmptyStrings` | Stores `_RoadNatureConfig`'s `general motor road` value under exact annotation `_NonEmptyStrings`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `limited_motor_proxy` | `limited_motor_proxy: _NonEmptyStrings` | Stores `_RoadNatureConfig`'s `limited motor proxy` value under exact annotation `_NonEmptyStrings`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `non_general_vehicle` | `non_general_vehicle: _NonEmptyStrings` | Stores `_RoadNatureConfig`'s `non general vehicle` value under exact annotation `_NonEmptyStrings`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `special_review` | `special_review: _NonEmptyStrings` | Stores `_RoadNatureConfig`'s `special review` value under exact annotation `_NonEmptyStrings`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |

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

- Pydantic constructs this model during direct/model_validate or nested-model validation; its exact validators and the module's loader/build functions below define the active framework entry points.

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
| `known` | `known: _NonEmptyStrings` | Stores `_ImportanceConfig`'s `known` value under exact annotation `_NonEmptyStrings`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `limited` | `limited: _NonEmptyStrings` | Stores `_ImportanceConfig`'s `limited` value under exact annotation `_NonEmptyStrings`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |

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

- Pydantic constructs this model during direct/model_validate or nested-model validation; its exact validators and the module's loader/build functions below define the active framework entry points.

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
| `asset_state` | `asset_state: _AssetStateConfig` | Closed or validated `asset state` classification on `_SourceValuesConfig`; accepted values and downstream branches are recoverable from the reproduced validators and consumers. |
| `light_vehicle_access` | `light_vehicle_access: _LightVehicleAccessConfig` | Stores `_SourceValuesConfig`'s `light vehicle access` value under exact annotation `_LightVehicleAccessConfig`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `nature` | `nature: _RoadNatureConfig` | Stores `_SourceValuesConfig`'s `nature` value under exact annotation `_RoadNatureConfig`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `known_restriction_review` | `known_restriction_review: _NonEmptyStrings` | Stores `_SourceValuesConfig`'s `known restriction review` value under exact annotation `_NonEmptyStrings`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `importance` | `importance: _ImportanceConfig` | Stores `_SourceValuesConfig`'s `importance` value under exact annotation `_ImportanceConfig`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `width_below_m` | `width_below_m: Annotated[StrictFloat, Field(gt=0, allow_inf_nan=False)]` | Metre value; whether measured geometry or configured policy is determined by the owning model/function, not the suffix alone. |

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

- Pydantic constructs this model during direct/model_validate or nested-model validation; its exact validators and the module's loader/build functions below define the active framework entry points.

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
| `fictitious_geometry` | `fictitious_geometry: Literal["NOT_DISTANCE_PROXY"]` | Stores `_DecisionOutcomesConfig`'s `fictitious geometry` value under exact annotation `Literal['NOT_DISTANCE_PROXY']`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `project_geometry_not_significant` | `project_geometry_not_significant: Literal["NOT_DISTANCE_PROXY"]` | Stores `_DecisionOutcomesConfig`'s `project geometry not significant` value under exact annotation `Literal['NOT_DISTANCE_PROXY']`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `not_in_service` | `not_in_service: Literal["NOT_GENERAL_VEHICLE_PROXY"]` | Stores `_DecisionOutcomesConfig`'s `not in service` value under exact annotation `Literal['NOT_GENERAL_VEHICLE_PROXY']`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `physically_impossible` | `physically_impossible: Literal["NOT_GENERAL_VEHICLE_PROXY"]` | Stores `_DecisionOutcomesConfig`'s `physically impossible` value under exact annotation `Literal['NOT_GENERAL_VEHICLE_PROXY']`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `non_general_vehicle_nature` | `non_general_vehicle_nature: Literal["NOT_GENERAL_VEHICLE_PROXY"]` | Stores `_DecisionOutcomesConfig`'s `non general vehicle nature` value under exact annotation `Literal['NOT_GENERAL_VEHICLE_PROXY']`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `rights_restricted` | `rights_restricted: Literal["RESTRICTED_REVIEW"]` | Stores `_DecisionOutcomesConfig`'s `rights restricted` value under exact annotation `Literal['RESTRICTED_REVIEW']`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `private_road` | `private_road: Literal["RESTRICTED_REVIEW"]` | Stores `_DecisionOutcomesConfig`'s `private road` value under exact annotation `Literal['RESTRICTED_REVIEW']`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `temporal_closure` | `temporal_closure: Literal["RESTRICTED_REVIEW"]` | Stores `_DecisionOutcomesConfig`'s `temporal closure` value under exact annotation `Literal['RESTRICTED_REVIEW']`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `known_restriction` | `known_restriction: Literal["RESTRICTED_REVIEW"]` | Stores `_DecisionOutcomesConfig`'s `known restriction` value under exact annotation `Literal['RESTRICTED_REVIEW']`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `other_recorded_restriction` | `other_recorded_restriction: Literal["RESTRICTED_REVIEW"]` | Stores `_DecisionOutcomesConfig`'s `other recorded restriction` value under exact annotation `Literal['RESTRICTED_REVIEW']`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `special_nature` | `special_nature: Literal["RESTRICTED_REVIEW"]` | Stores `_DecisionOutcomesConfig`'s `special nature` value under exact annotation `Literal['RESTRICTED_REVIEW']`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `limited_nature` | `limited_nature: Literal["LIMITED_VEHICLE_PROXY"]` | Stores `_DecisionOutcomesConfig`'s `limited nature` value under exact annotation `Literal['LIMITED_VEHICLE_PROXY']`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `importance_6` | `importance_6: Literal["LIMITED_VEHICLE_PROXY"]` | Stores `_DecisionOutcomesConfig`'s `importance 6` value under exact annotation `Literal['LIMITED_VEHICLE_PROXY']`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `narrow_carriageway` | `narrow_carriageway: Literal["LIMITED_VEHICLE_PROXY"]` | Stores `_DecisionOutcomesConfig`'s `narrow carriageway` value under exact annotation `Literal['LIMITED_VEHICLE_PROXY']`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `open_or_toll` | `open_or_toll: Literal["GENERAL_VEHICLE_PROXY"]` | Stores `_DecisionOutcomesConfig`'s `open or toll` value under exact annotation `Literal['GENERAL_VEHICLE_PROXY']`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `unknown` | `unknown: Literal["UNKNOWN_REVIEW"]` | Stores `_DecisionOutcomesConfig`'s `unknown` value under exact annotation `Literal['UNKNOWN_REVIEW']`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |

**Interface consumers**

- Pydantic constructs this model during direct/model_validate or nested-model validation; its exact validators and the module's loader/build functions below define the active framework entry points.

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
| `scope` | `scope: _ExactString` | Closed or validated `scope` classification on `_PolicyConfig`; accepted values and downstream branches are recoverable from the reproduced validators and consumers. |
| `references` | `references: _ReferencesConfig` | `_PolicyConfig`'s `references` evidence/text field; it retains the exact configured or source meaning under annotation `_ReferencesConfig` and is not promoted to a legal conclusion. |
| `evidence_checked_on` | `evidence_checked_on: Literal["2026-08-16"]` | `_PolicyConfig`'s `evidence checked on` evidence/text field; it retains the exact configured or source meaning under annotation `Literal['2026-08-16']` and is not promoted to a legal conclusion. |
| `vehicle_scope` | `vehicle_scope: Literal["LIGHT_VEHICLE_AND_GENERAL_CAR_NETWORK"]` | Closed or validated `vehicle scope` classification on `_PolicyConfig`; accepted values and downstream branches are recoverable from the reproduced validators and consumers. |
| `heavy_vehicle_access` | `heavy_vehicle_access: Literal["NOT_PROVEN"]` | Explicit heavy-vehicle evidence state; current road policy requires NOT_PROVEN. |
| `classes` | `classes: _ClassesConfig` | Closed or validated `classes` classification on `_PolicyConfig`; accepted values and downstream branches are recoverable from the reproduced validators and consumers. |
| `source_values` | `source_values: _SourceValuesConfig` | Source fact or textual lineage named by the suffix; it becomes physical proof only where a validator rechecks bytes/source content. |
| `decision_precedence` | `decision_precedence: _NonEmptyStrings` | Stores `_PolicyConfig`'s `decision precedence` value under exact annotation `_NonEmptyStrings`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `decision_outcomes` | `decision_outcomes: _DecisionOutcomesConfig` | Stores `_PolicyConfig`'s `decision outcomes` value under exact annotation `_DecisionOutcomesConfig`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |

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

- Pydantic constructs this model during direct/model_validate or nested-model validation; its exact validators and the module's loader/build functions below define the active framework entry points.

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
| `general_vehicle_proxy` | `general_vehicle_proxy: str` | Stores `_CompiledClasses`'s `general vehicle proxy` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `limited_vehicle_proxy` | `limited_vehicle_proxy: str` | Stores `_CompiledClasses`'s `limited vehicle proxy` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `restricted_review` | `restricted_review: str` | Stores `_CompiledClasses`'s `restricted review` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `not_general_vehicle_proxy` | `not_general_vehicle_proxy: str` | Stores `_CompiledClasses`'s `not general vehicle proxy` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `not_distance_proxy` | `not_distance_proxy: str` | Stores `_CompiledClasses`'s `not distance proxy` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `unknown_review` | `unknown_review: str` | Stores `_CompiledClasses`'s `unknown review` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |

**Interface consumers**

- direct call or construction: `src/landscout/stages/road_vehicle_proxy_policy.py::_compile_policy` via `_CompiledClasses`.

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

- direct call or construction: `src/landscout/stages/road_vehicle_proxy_policy.py::_compile_policy` via `_CompiledAssetState`.

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
| `publisher` | `publisher: str` | Stores `_CompiledNavigationReference`'s `publisher` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `title` | `title: str` | `_CompiledNavigationReference`'s `title` evidence/text field; it retains the exact configured or source meaning under annotation `str` and is not promoted to a legal conclusion. |
| `revision` | `revision: str` | Stores `_CompiledNavigationReference`'s `revision` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `evidence_scope` | `evidence_scope: str` | Closed or validated `evidence scope` classification on `_CompiledNavigationReference`; accepted values and downstream branches are recoverable from the reproduced validators and consumers. |

**Interface consumers**

- direct call or construction: `src/landscout/stages/road_vehicle_proxy_policy.py::_compile_policy` via `_CompiledNavigationReference`.

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
| `publisher` | `publisher: str` | Stores `_CompiledBdTopoProductReference`'s `publisher` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `title` | `title: str` | `_CompiledBdTopoProductReference`'s `title` evidence/text field; it retains the exact configured or source meaning under annotation `str` and is not promoted to a legal conclusion. |
| `document_id` | `document_id: str` | Exact identity for the entity named by the field; uniqueness, portability, and lineage meaning are only those explicitly validated by the owner. |
| `revision` | `revision: str` | Stores `_CompiledBdTopoProductReference`'s `revision` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `evidence_scope` | `evidence_scope: str` | Closed or validated `evidence scope` classification on `_CompiledBdTopoProductReference`; accepted values and downstream branches are recoverable from the reproduced validators and consumers. |

**Interface consumers**

- direct call or construction: `src/landscout/stages/road_vehicle_proxy_policy.py::_compile_policy` via `_CompiledBdTopoProductReference`.

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

- direct call or construction: `src/landscout/stages/road_vehicle_proxy_policy.py::_compile_policy` via `_CompiledLightVehicleAccess`.

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

- direct call or construction: `src/landscout/stages/road_vehicle_proxy_policy.py::_compile_policy` via `_CompiledRoadNature`.

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

- direct call or construction: `src/landscout/stages/road_vehicle_proxy_policy.py::_compile_policy` via `_CompiledImportance`.

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
| `fictitious_geometry` | `fictitious_geometry: str` | Stores `_CompiledDecisionOutcomes`'s `fictitious geometry` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `project_geometry_not_significant` | `project_geometry_not_significant: str` | Stores `_CompiledDecisionOutcomes`'s `project geometry not significant` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `not_in_service` | `not_in_service: str` | Stores `_CompiledDecisionOutcomes`'s `not in service` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `physically_impossible` | `physically_impossible: str` | Stores `_CompiledDecisionOutcomes`'s `physically impossible` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `non_general_vehicle_nature` | `non_general_vehicle_nature: str` | Stores `_CompiledDecisionOutcomes`'s `non general vehicle nature` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `rights_restricted` | `rights_restricted: str` | Stores `_CompiledDecisionOutcomes`'s `rights restricted` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `private_road` | `private_road: str` | Stores `_CompiledDecisionOutcomes`'s `private road` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `temporal_closure` | `temporal_closure: str` | Stores `_CompiledDecisionOutcomes`'s `temporal closure` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `known_restriction` | `known_restriction: str` | Stores `_CompiledDecisionOutcomes`'s `known restriction` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `other_recorded_restriction` | `other_recorded_restriction: str` | Stores `_CompiledDecisionOutcomes`'s `other recorded restriction` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `special_nature` | `special_nature: str` | Stores `_CompiledDecisionOutcomes`'s `special nature` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `limited_nature` | `limited_nature: str` | Stores `_CompiledDecisionOutcomes`'s `limited nature` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `importance_6` | `importance_6: str` | Stores `_CompiledDecisionOutcomes`'s `importance 6` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `narrow_carriageway` | `narrow_carriageway: str` | Stores `_CompiledDecisionOutcomes`'s `narrow carriageway` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `open_or_toll` | `open_or_toll: str` | Stores `_CompiledDecisionOutcomes`'s `open or toll` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `unknown` | `unknown: str` | Stores `_CompiledDecisionOutcomes`'s `unknown` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |

**Interface consumers**

- direct call or construction: `src/landscout/stages/road_vehicle_proxy_policy.py::_compile_policy` via `_CompiledDecisionOutcomes`.

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
| `scope` | `scope: str` | Closed or validated `scope` classification on `IgnRoadVehicleProxyPolicy`; accepted values and downstream branches are recoverable from the reproduced validators and consumers. |
| `navigation_reference` | `navigation_reference: _CompiledNavigationReference` | `IgnRoadVehicleProxyPolicy`'s `navigation reference` evidence/text field; it retains the exact configured or source meaning under annotation `_CompiledNavigationReference` and is not promoted to a legal conclusion. |
| `bdtopo_product_reference` | `bdtopo_product_reference: _CompiledBdTopoProductReference` | `IgnRoadVehicleProxyPolicy`'s `bdtopo product reference` evidence/text field; it retains the exact configured or source meaning under annotation `_CompiledBdTopoProductReference` and is not promoted to a legal conclusion. |
| `evidence_checked_on` | `evidence_checked_on: str` | `IgnRoadVehicleProxyPolicy`'s `evidence checked on` evidence/text field; it retains the exact configured or source meaning under annotation `str` and is not promoted to a legal conclusion. |
| `vehicle_scope` | `vehicle_scope: str` | Closed or validated `vehicle scope` classification on `IgnRoadVehicleProxyPolicy`; accepted values and downstream branches are recoverable from the reproduced validators and consumers. |
| `heavy_vehicle_access` | `heavy_vehicle_access: str` | Explicit heavy-vehicle evidence state; current road policy requires NOT_PROVEN. |
| `classes` | `classes: _CompiledClasses` | Closed or validated `classes` classification on `IgnRoadVehicleProxyPolicy`; accepted values and downstream branches are recoverable from the reproduced validators and consumers. |
| `asset_state` | `asset_state: _CompiledAssetState` | Closed or validated `asset state` classification on `IgnRoadVehicleProxyPolicy`; accepted values and downstream branches are recoverable from the reproduced validators and consumers. |
| `light_vehicle_access` | `light_vehicle_access: _CompiledLightVehicleAccess` | Stores `IgnRoadVehicleProxyPolicy`'s `light vehicle access` value under exact annotation `_CompiledLightVehicleAccess`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `nature` | `nature: _CompiledRoadNature` | Stores `IgnRoadVehicleProxyPolicy`'s `nature` value under exact annotation `_CompiledRoadNature`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `known_restriction_review` | `known_restriction_review: frozenset[str]` | Structured `known restriction review` collection owned by `IgnRoadVehicleProxyPolicy`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |
| `importance` | `importance: _CompiledImportance` | Stores `IgnRoadVehicleProxyPolicy`'s `importance` value under exact annotation `_CompiledImportance`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `width_below_m` | `width_below_m: float` | Metre value; whether measured geometry or configured policy is determined by the owning model/function, not the suffix alone. |
| `decision_precedence` | `decision_precedence: tuple[str, ...]` | Structured `decision precedence` collection owned by `IgnRoadVehicleProxyPolicy`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |
| `decision_outcomes` | `decision_outcomes: _CompiledDecisionOutcomes` | Stores `IgnRoadVehicleProxyPolicy`'s `decision outcomes` value under exact annotation `_CompiledDecisionOutcomes`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `config_sha256` | `config_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |

**Interface consumers**

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyPolicy,
    IgnRoadVehicleProxyPolicyError,
    load_ign_road_vehicle_proxy_policy,
)`.
- import/re-export: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::<module>` via `from landscout.stages.road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyPolicy,
    load_ign_road_vehicle_proxy_policy,
)`.
- import/re-export: `src/landscout/stages/assess_road_proximity_coverage.py::<module>` via `from landscout.stages.road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyPolicy,
    load_ign_road_vehicle_proxy_policy,
)`.
- import/re-export: `src/landscout/stages/enrich_road_proximity.py::<module>` via `from landscout.stages.road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyPolicy,
    load_ign_road_vehicle_proxy_policy,
)`.
- direct call or construction: `src/landscout/stages/road_vehicle_proxy_policy.py::_compile_policy` via `IgnRoadVehicleProxyPolicy`.
- import/re-export: `tests/unit/test_road_vehicle_proxy_policy.py::<module>` via `from landscout.stages.road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyPolicy,
    IgnRoadVehicleProxyPolicyError,
    load_ign_road_vehicle_proxy_policy,
)`.

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

- callback/function object: `src/landscout/stages/bess_planning_feature_policy.py::load_bess_planning_feature_policy_config` via `yaml.load(Path(path).read_text(encoding='utf-8'), Loader=_UniqueKeyLoader)`.
- callback/function object: `src/landscout/stages/interpret_bess_zoning.py::load_bess_zoning_policy_config` via `yaml.load(Path(path).read_text(encoding='utf-8'), Loader=_UniqueKeyLoader)`.
- callback/function object: `src/landscout/stages/resolve_planning_feature_codes.py::load_cnig_feature_code_profile` via `yaml.load(Path(path).read_text(encoding='utf-8'), Loader=_UniqueKeyLoader)`.
- callback/function object: `src/landscout/stages/road_vehicle_proxy_policy.py::load_ign_road_vehicle_proxy_policy` via `yaml.load(policy_bytes.decode('utf-8'), Loader=_UniqueKeyLoader)`.
- callback/function object: `src/landscout/stages/structure_planning_regulation.py::load_planning_regulation_structure_config` via `yaml.load(config_path.read_text(encoding='utf-8'), Loader=_UniqueKeyLoader)`.

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

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/common/bess_application_contract.py::_sha256` via `_exact_string`.
- direct call or construction: `src/landscout/common/bess_application_contract.py::_optional_official_string` via `_exact_string`.
- direct call or construction: `src/landscout/common/bess_application_contract.py::validate_bess_application_policy_frame` via `_exact_string`.
- direct call or construction: `src/landscout/common/bess_application_contract.py::_relation_identity_string` via `_exact_string`.
- direct call or construction: `src/landscout/common/bess_application_contract.py::validate_bess_application_feature_catalogs` via `_exact_string`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_sha256_string` via `_exact_string`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_validate_result_envelope` via `_exact_string`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_sha256_string` via `_exact_string`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::BessPlanningFeatureApplicationArtifactManifest._validate_manifest` via `_exact_string`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_validate_result_envelope` via `_exact_string`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::_optional_exact_string` via `_exact_string`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::_sha256_string` via `_exact_string`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::PolicySourceLock._validate_lock` via `_exact_string`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::PolicyEntry._validate_entry` via `_exact_string`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::BessPlanningFeaturePolicyConfig._validate_policy` via `_exact_string`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::BessPlanningFeaturePolicyArtifactManifest._validate_manifest` via `_exact_string`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::_validate_policy_table_rows` via `_exact_string`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::_validate_result_envelope` via `_exact_string`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::_validate_official_text` via `_exact_string`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::CnigFeatureCodeProfile._validate_profile` via `_exact_string`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::_strict_string` via `_exact_string`.
- callback/function object: `src/landscout/stages/road_vehicle_proxy_policy.py::<module>` via `AfterValidator(_exact_string)`.

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

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/road_vehicle_proxy_policy.py::_AssetStateConfig._valid_groups` via `_require_unique`.
- direct call or construction: `src/landscout/stages/road_vehicle_proxy_policy.py::_LightVehicleAccessConfig._valid_groups` via `_require_unique`.
- direct call or construction: `src/landscout/stages/road_vehicle_proxy_policy.py::_RoadNatureConfig._valid_groups` via `_require_unique`.
- direct call or construction: `src/landscout/stages/road_vehicle_proxy_policy.py::_ImportanceConfig._valid_domain` via `_require_unique`.
- direct call or construction: `src/landscout/stages/road_vehicle_proxy_policy.py::_SourceValuesConfig._valid_values` via `_require_unique`.

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

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/road_vehicle_proxy_policy.py::_AssetStateConfig._valid_groups` via `_require_disjoint`.
- direct call or construction: `src/landscout/stages/road_vehicle_proxy_policy.py::_LightVehicleAccessConfig._valid_groups` via `_require_disjoint`.
- direct call or construction: `src/landscout/stages/road_vehicle_proxy_policy.py::_RoadNatureConfig._valid_groups` via `_require_disjoint`.

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

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

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

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

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

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

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

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

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

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

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

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

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

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/common/bess_application_contract.py::_status_priority_mapping` via `priority_to_statuses.values`.
- property/attribute access: `src/landscout/common/bess_application_contract.py::_status_priority_mapping` via `priority_to_statuses.values`.
- direct call or construction: `src/landscout/common/bess_application_contract.py::_status_priority_mapping` via `status_to_priorities.values`.
- property/attribute access: `src/landscout/common/bess_application_contract.py::_status_priority_mapping` via `status_to_priorities.values`.
- callback/function object: `src/landscout/common/safe_http.py::_redirect_location` via `len(values)`.
- callback/function object: `src/landscout/sources/gpu_fr.py::_document_from_dict` via `GpuDocumentMetadata(**values, written_files=tuple(written))`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_parcel_summary` via `priority_statuses.values`.
- property/attribute access: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_parcel_summary` via `priority_statuses.values`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_parcel_summary` via `status_priorities.values`.
- property/attribute access: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_parcel_summary` via `status_priorities.values`.
- callback/function object: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_assign_columns` via `pd.array(values, dtype='Int64')`.
- callback/function object: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_assign_columns` via `pd.array(values, dtype='bool')`.
- callback/function object: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_assign_columns` via `pd.array(values, dtype='str')`.
- callback/function object: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::_object_scalar_mask` via `np.asarray(values, dtype=bool)`.
- direct call or construction: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::_classify_road_frame` via `unknown_masks.values`.
- property/attribute access: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::_classify_road_frame` via `unknown_masks.values`.
- direct call or construction: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::_classify_road_frame` via `rule_masks.values`.
- property/attribute access: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::_classify_road_frame` via `rule_masks.values`.
- callback/function object: `src/landscout/stages/assess_grid_coverage.py::_boundary_profile` via `_finite_nonnegative(values, 'Grid source boundary distance')`.
- property/attribute access: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_class_coverage` via `policy.classes.values`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::BessPlanningFeaturePolicyConfig._validate_policy` via `self.status_priority.values`.
- property/attribute access: `src/landscout/stages/bess_planning_feature_policy.py::BessPlanningFeaturePolicyConfig._validate_policy` via `self.status_priority.values`.
- callback/function object: `src/landscout/stages/enrich_grid_proximity.py::_calculation_geometries` via `force_2d(values)`.
- callback/function object: `src/landscout/stages/enrich_grid_proximity.py::_validate_tie_counts` via `len(values)`.
- direct call or construction: `src/landscout/stages/enrich_grid_proximity.py::_validate_result_contract` via `_LINE_OUTPUT_MAPPING.values`.
- property/attribute access: `src/landscout/stages/enrich_grid_proximity.py::_validate_result_contract` via `_LINE_OUTPUT_MAPPING.values`.
- direct call or construction: `src/landscout/stages/enrich_grid_proximity.py::_validate_result_contract` via `_EXACT_LINE_OUTPUT_MAPPING.values`.
- property/attribute access: `src/landscout/stages/enrich_grid_proximity.py::_validate_result_contract` via `_EXACT_LINE_OUTPUT_MAPPING.values`.
- direct call or construction: `src/landscout/stages/enrich_grid_proximity.py::_validate_result_contract` via `_POST_OUTPUT_MAPPING.values`.
- property/attribute access: `src/landscout/stages/enrich_grid_proximity.py::_validate_result_contract` via `_POST_OUTPUT_MAPPING.values`.
- callback/function object: `src/landscout/stages/enrich_grid_proximity.py::_distance_profile` via `len(values)`.
- callback/function object: `src/landscout/stages/enrich_planning_features.py::_validate_ids` via `_validate_exact_strings(values, label)`.
- callback/function object: `src/landscout/stages/enrich_planning_features.py::_standard_model` via `len(values)`.
- callback/function object: `src/landscout/stages/enrich_planning_features.py::_source_feature_ids` via `_validate_ids(values, f'{layer.logical_name} OGR FID')`.
- callback/function object: `src/landscout/stages/enrich_planning_features.py::_normalize_layer` via `np.isfinite(values)`.
- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::<module>` via `GPU_ZONING_SOURCE_FIELDS.values`.
- property/attribute access: `src/landscout/stages/enrich_planning_zoning.py::<module>` via `GPU_ZONING_SOURCE_FIELDS.values`.
- callback/function object: `src/landscout/stages/enrich_planning_zoning.py::_standard_model` via `len(values)`.
- property/attribute access: `src/landscout/stages/enrich_road_proximity.py::_policy_classes` via `policy.classes.values`.
- callback/function object: `src/landscout/stages/enrich_road_proximity.py::_calculation_geometries` via `force_2d(values)`.
- direct call or construction: `src/landscout/stages/enrich_road_proximity.py::_validate_result` via `_MATCH_OUTPUT_MAPPING.values`.
- property/attribute access: `src/landscout/stages/enrich_road_proximity.py::_validate_result` via `_MATCH_OUTPUT_MAPPING.values`.
- callback/function object: `src/landscout/stages/index_planning_regulation.py::_zoning_regulation_filenames` via `sorted(values, key=str.casefold)`.
- callback/function object: `src/landscout/stages/interpret_bess_zoning.py::_exact_id_series` via `set(values)`.
- callback/function object: `src/landscout/stages/interpret_bess_zoning.py::_exact_id_series` via `len(values)`.
- callback/function object: `src/landscout/stages/interpret_bess_zoning.py::_exact_id_series` via `tuple(values)`.
- callback/function object: `src/landscout/stages/interpret_bess_zoning.py::_compare_results` via `isinstance(values, (tuple, list, np.ndarray))`.
- callback/function object: `src/landscout/stages/interpret_bess_zoning.py::_compare_results` via `set(values)`.
- direct call or construction: `src/landscout/stages/normalize_cadastre.py::normalize_cadastre_parcels` via `FIELD_MAPPING.values`.
- property/attribute access: `src/landscout/stages/normalize_cadastre.py::normalize_cadastre_parcels` via `FIELD_MAPPING.values`.
- direct call or construction: `src/landscout/stages/profile_shape.py::profile_shape_distribution` via `width_buckets.values`.
- property/attribute access: `src/landscout/stages/profile_shape.py::profile_shape_distribution` via `width_buckets.values`.
- direct call or construction: `src/landscout/stages/profile_shape.py::profile_shape_distribution` via `ratio_buckets.values`.
- property/attribute access: `src/landscout/stages/profile_shape.py::profile_shape_distribution` via `ratio_buckets.values`.
- direct call or construction: `src/landscout/stages/profile_shape.py::profile_shape_distribution` via `compactness_buckets.values`.
- property/attribute access: `src/landscout/stages/profile_shape.py::profile_shape_distribution` via `compactness_buckets.values`.
- callback/function object: `src/landscout/stages/road_vehicle_proxy_policy.py::_require_unique` via `len(values)`.
- callback/function object: `src/landscout/stages/road_vehicle_proxy_policy.py::_require_unique` via `set(values)`.
- callback/function object: `src/landscout/stages/road_vehicle_proxy_policy.py::_AssetStateConfig._valid_groups` via `_require_unique(values, name)`.
- callback/function object: `src/landscout/stages/road_vehicle_proxy_policy.py::_LightVehicleAccessConfig._valid_groups` via `_require_unique(values, name)`.
- callback/function object: `src/landscout/stages/road_vehicle_proxy_policy.py::_RoadNatureConfig._valid_groups` via `_require_unique(values, name)`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_section_starts` via `starts_by_position.values`.
- property/attribute access: `src/landscout/stages/structure_planning_regulation.py::_section_starts` via `starts_by_position.values`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_section_starts` via `compacted.values`.
- property/attribute access: `src/landscout/stages/structure_planning_regulation.py::_section_starts` via `compacted.values`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::_coordinated_policy_mutation` via `pd.Categorical(values)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::_coordinated_policy_mutation` via `pd.Series(values, index=frame.index, dtype=dtype)`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_factual_prefix_lineage_change` via `paths.values`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_factual_prefix_lineage_change` via `paths.values`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_all_null_raw_column_transition` via `paths.values`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_all_null_raw_column_transition` via `paths.values`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_unreferenced_feature_and_row_reordering` via `paths.values`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_unreferenced_feature_and_row_reordering` via `paths.values`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_validates_upstreams_and_rebuilds_once_lightweight` via `paths.values`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_validates_upstreams_and_rebuilds_once_lightweight` via `paths.values`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_bad_upstream_before_artifact_reads` via `paths.values`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_bad_upstream_before_artifact_reads` via `paths.values`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild` via `paths.values`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild` via `paths.values`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild` via `paths.values`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild` via `paths.values`.
- callback/function object: `tests/unit/test_assess_grid_coverage.py::_parcels` via `gpd.GeoDataFrame({'parcel_id': [f'PARCEL-{position + 1}' for position in range(len(values))], 'preserved_value': list(range(len(values)))}, geometry=values, crs=crs, index=[20 + position for position in range(len(values))])`.
- callback/function object: `tests/unit/test_assess_grid_coverage.py::_parcels` via `len(values)`.
- callback/function object: `tests/unit/test_assess_grid_coverage.py::_lines` via `len(values)`.
- callback/function object: `tests/unit/test_assess_road_proximity_coverage.py::_coverage` via `gpd.GeoDataFrame({'code_insee': [department_code] * len(values), 'nom_officiel': [f'Department {position}' for position in range(len(values))]}, geometry=values, crs=crs)`.
- callback/function object: `tests/unit/test_assess_road_proximity_coverage.py::_coverage` via `len(values)`.
- callback/function object: `tests/unit/test_assess_road_proximity_coverage.py::_metric_parcels` via `len(values)`.
- callback/function object: `tests/unit/test_assess_road_proximity_coverage.py::_metric_parcels` via `gpd.GeoDataFrame({'parcel_id': ids, 'preserved_value': list(range(len(values)))}, geometry=values, crs='EPSG:2154', index=[20 + position for position in range(len(values))])`.
- callback/function object: `tests/unit/test_assess_road_proximity_coverage.py::test_internal_boundary_distance_is_full_geometry_finite_and_nonnegative` via `np.isfinite(values)`.
- callback/function object: `tests/unit/test_cadastre_loader_fr.py::_download` via `CadastreDownload(**values)`.
- callback/function object: `tests/unit/test_enrich_grid_proximity.py::_parcels` via `len(values)`.
- callback/function object: `tests/unit/test_enrich_grid_proximity.py::_parcels` via `gpd.GeoDataFrame({'parcel_id': ids, 'source_value': list(range(count))}, geometry=values, crs=crs, index=source_index)`.
- callback/function object: `tests/unit/test_enrich_grid_proximity.py::_lines` via `len(values)`.
- callback/function object: `tests/unit/test_enrich_grid_proximity.py::_lines` via `gpd.GeoDataFrame({'grid_feature_id': ids, 'grid_feature_type': feature_types or ['ELECTRIC_LINE'] * count, 'source_feature_id': [f'SOURCE-{value}' for value in ids], 'source_department_code': ['31'] * count, 'source_edition': ['2026-06-15'] * count, 'source_archive_sha256': ['a' * 64] * count, 'source_layer': ['CUSTOM_LINE_LAYER'] * count, 'spatial_role': spatial_roles or ['PROXY_GEOMETRY'] * count, 'geometry_status': geometry_statuses, 'voltage_raw': [f'{value:g} kV' if isinstance(value, (int, float)) else None for value in normalized_voltages], 'voltage_status': normalized_voltage_statuses, 'voltage_kv': normalized_voltages, 'voltage_upper_bound_kv': [np.nan] * count, 'manager_name': ['TEST MANAGER'] * count, 'asset_status_raw': ['En service'] * count}, geometry=values, crs=crs)`.
- callback/function object: `tests/unit/test_enrich_grid_proximity.py::_posts` via `len(values)`.
- callback/function object: `tests/unit/test_enrich_grid_proximity.py::_posts` via `gpd.GeoDataFrame({'grid_feature_id': ids, 'grid_feature_type': feature_types or ['TRANSFORMATION_POST'] * count, 'source_feature_id': [f'SOURCE-{value}' for value in ids], 'source_department_code': ['31'] * count, 'source_edition': ['2026-06-15'] * count, 'source_archive_sha256': ['a' * 64] * count, 'source_layer': ['CUSTOM_POST_LAYER'] * count, 'spatial_role': spatial_roles or ['PROXY_GEOMETRY'] * count, 'geometry_status': geometry_statuses, 'name': ['Test post'] * count, 'importance_raw': ['5'] * count, 'asset_status_raw': ['En service'] * count}, geometry=values, crs=crs)`.
- callback/function object: `tests/unit/test_enrich_planning_features.py::_parcels` via `gpd.GeoDataFrame({'parcel_id': ids or [f'P-{index + 1}' for index in range(len(values))], 'existing_zoning_fact': np.arange(len(values), dtype='int64') + 7}, geometry=values, crs='EPSG:2154', index=[50 + index for index in range(len(values))])`.
- callback/function object: `tests/unit/test_enrich_planning_features.py::_parcels` via `len(values)`.
- callback/function object: `tests/unit/test_enrich_planning_zoning.py::_parcels` via `len(values)`.
- callback/function object: `tests/unit/test_enrich_planning_zoning.py::_parcels` via `gpd.GeoDataFrame({'parcel_id': ids, 'existing_grid_value': [100 + position for position in range(len(values))]}, geometry=values, crs='EPSG:2154', index=[50 + position for position in range(len(values))])`.

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

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: `result[key]`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- callback/function object: `src/landscout/stages/bess_planning_feature_policy.py::<module>` via `_UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_unique_mapping)`.
- callback/function object: `src/landscout/stages/interpret_bess_zoning.py::<module>` via `_UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_unique_mapping)`.
- callback/function object: `src/landscout/stages/resolve_planning_feature_codes.py::<module>` via `_UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_unique_mapping)`.
- callback/function object: `src/landscout/stages/road_vehicle_proxy_policy.py::<module>` via `_UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_unique_mapping)`.
- callback/function object: `src/landscout/stages/structure_planning_regulation.py::<module>` via `_UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_unique_mapping)`.

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

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/road_vehicle_proxy_policy.py::load_ign_road_vehicle_proxy_policy` via `_compile_policy`.

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

- Network I/O: none directly visible.
- Filesystem read: `Path(path).read_bytes`.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `sha256`, `sha256(policy_bytes).hexdigest`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyPolicy,
    IgnRoadVehicleProxyPolicyError,
    load_ign_road_vehicle_proxy_policy,
)`.
- direct call or construction: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::_apply_ign_road_vehicle_proxy_policy` via `load_ign_road_vehicle_proxy_policy`.
- import/re-export: `src/landscout/stages/apply_road_vehicle_proxy_policy.py::<module>` via `from landscout.stages.road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyPolicy,
    load_ign_road_vehicle_proxy_policy,
)`.
- direct call or construction: `src/landscout/stages/assess_road_proximity_coverage.py::_assess_road_proximity_coverage` via `load_ign_road_vehicle_proxy_policy`.
- import/re-export: `src/landscout/stages/assess_road_proximity_coverage.py::<module>` via `from landscout.stages.road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyPolicy,
    load_ign_road_vehicle_proxy_policy,
)`.
- direct call or construction: `src/landscout/stages/enrich_road_proximity.py::_enrich_parcel_road_proximity` via `load_ign_road_vehicle_proxy_policy`.
- import/re-export: `src/landscout/stages/enrich_road_proximity.py::<module>` via `from landscout.stages.road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyPolicy,
    load_ign_road_vehicle_proxy_policy,
)`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_every_configured_known_restriction_is_applied` via `load_ign_road_vehicle_proxy_policy`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_policy_lineage_is_exact_on_every_row` via `load_ign_road_vehicle_proxy_policy`.
- import/re-export: `tests/unit/test_apply_road_vehicle_proxy_policy.py::<module>` via `from landscout.stages.road_vehicle_proxy_policy import (
    load_ign_road_vehicle_proxy_policy,
)`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::_proximity` via `load_ign_road_vehicle_proxy_policy`.
- import/re-export: `tests/unit/test_assess_road_proximity_coverage.py::<module>` via `from landscout.stages.road_vehicle_proxy_policy import (
    load_ign_road_vehicle_proxy_policy,
)`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::_road_row` via `load_ign_road_vehicle_proxy_policy`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_selected_road_evidence_and_lineage_are_exact` via `load_ign_road_vehicle_proxy_policy`.
- import/re-export: `tests/unit/test_enrich_road_proximity.py::<module>` via `from landscout.stages.road_vehicle_proxy_policy import (
    load_ign_road_vehicle_proxy_policy,
)`.
- direct call or construction: `tests/unit/test_road_vehicle_proxy_policy.py::_load_payload` via `load_ign_road_vehicle_proxy_policy`.
- direct call or construction: `tests/unit/test_road_vehicle_proxy_policy.py::test_checked_in_policy_loads_with_exact_public_identity_and_reference` via `load_ign_road_vehicle_proxy_policy`.
- direct call or construction: `tests/unit/test_road_vehicle_proxy_policy.py::test_checked_in_policy_hash_binds_exact_file_bytes` via `load_ign_road_vehicle_proxy_policy`.
- direct call or construction: `tests/unit/test_road_vehicle_proxy_policy.py::test_repeat_loading_is_deterministic_and_independent` via `load_ign_road_vehicle_proxy_policy`.
- direct call or construction: `tests/unit/test_road_vehicle_proxy_policy.py::test_asset_state_groups_cover_exact_v2_domain` via `load_ign_road_vehicle_proxy_policy`.
- direct call or construction: `tests/unit/test_road_vehicle_proxy_policy.py::test_importance_domains_expose_known_without_positive_classification` via `load_ign_road_vehicle_proxy_policy`.
- direct call or construction: `tests/unit/test_road_vehicle_proxy_policy.py::test_decision_precedence_and_rule_outcomes_are_approved` via `load_ign_road_vehicle_proxy_policy`.
- direct call or construction: `tests/unit/test_road_vehicle_proxy_policy.py::test_project_geometry_rule_has_exact_precedence_position` via `load_ign_road_vehicle_proxy_policy`.
- direct call or construction: `tests/unit/test_road_vehicle_proxy_policy.py::test_approved_class_vocabulary_has_no_heavy_or_legal_claim` via `load_ign_road_vehicle_proxy_policy`.
- direct call or construction: `tests/unit/test_road_vehicle_proxy_policy.py::test_observed_d031_natures_are_covered_exactly_once` via `load_ign_road_vehicle_proxy_policy`.
- direct call or construction: `tests/unit/test_road_vehicle_proxy_policy.py::test_observed_d031_access_and_importance_vocabularies_are_compatible` via `load_ign_road_vehicle_proxy_policy`.
- direct call or construction: `tests/unit/test_road_vehicle_proxy_policy.py::test_compiled_policy_structures_are_immutable` via `load_ign_road_vehicle_proxy_policy`.
- direct call or construction: `tests/unit/test_road_vehicle_proxy_policy.py::test_mutating_source_payload_cannot_affect_another_load` via `load_ign_road_vehicle_proxy_policy`.
- direct call or construction: `tests/unit/test_road_vehicle_proxy_policy.py::test_malformed_yaml_has_controlled_error` via `load_ign_road_vehicle_proxy_policy`.
- direct call or construction: `tests/unit/test_road_vehicle_proxy_policy.py::test_missing_file_has_controlled_error` via `load_ign_road_vehicle_proxy_policy`.
- import/re-export: `tests/unit/test_road_vehicle_proxy_policy.py::<module>` via `from landscout.stages.road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyPolicy,
    IgnRoadVehicleProxyPolicyError,
    load_ign_road_vehicle_proxy_policy,
)`.

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
| `IgnRoadVehicleProxyPolicy` | re-exported/defined Python symbol | `defined in `src/landscout/stages/road_vehicle_proxy_policy.py`` | yes |
| `IgnRoadVehicleProxyPolicyError` | re-exported/defined Python symbol | `defined in `src/landscout/stages/road_vehicle_proxy_policy.py`` | yes |
| `load_ign_road_vehicle_proxy_policy` | re-exported/defined Python symbol | `defined in `src/landscout/stages/road_vehicle_proxy_policy.py`` | yes |

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

# `src/landscout/stages/road_vehicle_proxy_policy.py`

## File identity

- Repository path: `src/landscout/stages/road_vehicle_proxy_policy.py`
- File type: Python source
- Primary responsibility: Loads and compiles the checked-in general-car/light-vehicle IGN road evidence policy.
- Layer / domain: `stage` / `road`
- Public or internal role: Contains an explicit module/package export surface; helpers prefixed with `_` remain internal unless re-exported elsewhere.
- Source SHA256: `73b7315bf37c48510fbb8e63c28272349fa0407f1c0c5adea91142a74c481286`

## 1. Purpose

Loads and compiles the checked-in general-car/light-vehicle IGN road evidence policy.

## 2. Position in LandScout architecture

This file is a `stage` artifact in the `road` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from __future__ import annotations` — required by the implementation paths and symbols documented below.
- `from collections.abc import Mapping` — required by the implementation paths and symbols documented below.
- `from dataclasses import dataclass` — required by the implementation paths and symbols documented below.
- `from hashlib import sha256` — required by the implementation paths and symbols documented below.
- `from pathlib import Path` — required by the implementation paths and symbols documented below.
- `from typing import Annotated, Literal, Self` — required by the implementation paths and symbols documented below.

### Third-party

- `import yaml` — required by the implementation paths and symbols documented below.
- `from pydantic import ( AfterValidator, BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StringConstraints, model_validator, )` — required by the implementation paths and symbols documented below.

### Internal LandScout

- None.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `_DEFAULT_POLICY_PATH` | `Path(__file__).resolve().parents[3] / "configs" / "access" / "ign_bdtopo_vehicle_proxy_policy.yaml"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_POLICY_ID` | `"ign_bdtopo_general_vehicle_proxy_v2"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_POLICY_SCOPE` | `"OFFICIAL_IGN_CAR_ROUTING_EVIDENCE_ONLY"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_EXPECTED_PRECEDENCE` | `( "FICTITIOUS_GEOMETRY", "PROJECT_GEOMETRY_NOT_SIGNIFICANT", "NOT_IN_SERVICE", "PHYSICALLY_IMPOSSIBLE", "NON_GENERAL_VEHICLE_NATURE", "RIGHTS_RESTRICTED", "PRIVATE_ROAD", "TEMPORAL_CLOSURE", "KNOWN_RESTRICTION", "OTHER_RECORDED_RESTRICTION", "SPECIAL_NATURE", "LIMITED_NATURE", "IMPORTANCE_6", "NARROW_CARRIAGEWAY", "OPEN_OR_TOLL", "UNKNOWN", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

### `IgnRoadVehicleProxyPolicyError`

**Purpose:** Raised when the IGN road vehicle-proxy policy is unsafe or invalid.

**Inheritance:** `ValueError`.

**Model form and mutability:** class inheriting from `ValueError`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

### `_StrictPolicyModel`

**Purpose:** Represents a validated policy configuration or compiled policy evidence envelope.

**Inheritance:** `BaseModel`.

**Model form and mutability:** Pydantic model; `model_config` and validators below define strictness, mutation, and extra-field behavior. Decorators: `none`.

**Validation configuration:** `model_config = ConfigDict(extra="forbid", frozen=True)`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

### `_NavigationReferenceConfig`

**Purpose:** Represents checked-in or resolved configuration fields and validates their exact domain before use.

**Inheritance:** `_StrictPolicyModel`.

**Model form and mutability:** class inheriting from `_StrictPolicyModel`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `publisher` | `Literal['IGN']` | `required` | `Literal['IGN']` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `title` | `Literal['Calcul d’itinéraire']` | `required` | `Literal['Calcul d’itinéraire']` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `revision` | `Literal['2026-05-27']` | `required` | `Literal['2026-05-27']` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `evidence_scope` | `Literal['GENERAL_CAR_ROUTING_RULES']` | `required` | `Literal['GENERAL_CAR_ROUTING_RULES']` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `_BdTopoProductReferenceConfig`

**Purpose:** Represents checked-in or resolved configuration fields and validates their exact domain before use.

**Inheritance:** `_StrictPolicyModel`.

**Model form and mutability:** class inheriting from `_StrictPolicyModel`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `publisher` | `Literal['IGN']` | `required` | `Literal['IGN']` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `title` | `Literal['BD TOPO® Version 3.5 - Descriptif de contenu']` | `required` | `Literal['BD TOPO® Version 3.5 - Descriptif de contenu']` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `document_id` | `Literal['DC_BDTOPO_3-5']` | `required` | Exact portable identity used to join lineage or evidence across frames and result envelopes. |
| `revision` | `Literal['2025-11']` | `required` | `Literal['2025-11']` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `evidence_scope` | `Literal['SOURCE_ATTRIBUTE_SEMANTICS']` | `required` | `Literal['SOURCE_ATTRIBUTE_SEMANTICS']` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `_ReferencesConfig`

**Purpose:** Represents checked-in or resolved configuration fields and validates their exact domain before use.

**Inheritance:** `_StrictPolicyModel`.

**Model form and mutability:** class inheriting from `_StrictPolicyModel`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `navigation` | `_NavigationReferenceConfig` | `required` | `_NavigationReferenceConfig` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `bdtopo_product` | `_BdTopoProductReferenceConfig` | `required` | `_BdTopoProductReferenceConfig` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `_ClassesConfig`

**Purpose:** Represents checked-in or resolved configuration fields and validates their exact domain before use.

**Inheritance:** `_StrictPolicyModel`.

**Model form and mutability:** class inheriting from `_StrictPolicyModel`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `general_vehicle_proxy` | `Literal['GENERAL_VEHICLE_PROXY']` | `required` | `Literal['GENERAL_VEHICLE_PROXY']` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `limited_vehicle_proxy` | `Literal['LIMITED_VEHICLE_PROXY']` | `required` | `Literal['LIMITED_VEHICLE_PROXY']` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `restricted_review` | `Literal['RESTRICTED_REVIEW']` | `required` | `Literal['RESTRICTED_REVIEW']` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `not_general_vehicle_proxy` | `Literal['NOT_GENERAL_VEHICLE_PROXY']` | `required` | `Literal['NOT_GENERAL_VEHICLE_PROXY']` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `not_distance_proxy` | `Literal['NOT_DISTANCE_PROXY']` | `required` | `Literal['NOT_DISTANCE_PROXY']` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `unknown_review` | `Literal['UNKNOWN_REVIEW']` | `required` | `Literal['UNKNOWN_REVIEW']` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `_AssetStateConfig`

**Purpose:** Represents checked-in or resolved configuration fields and validates their exact domain before use.

**Inheritance:** `_StrictPolicyModel`.

**Model form and mutability:** class inheriting from `_StrictPolicyModel`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `in_service` | `_NonEmptyStrings` | `required` | `_NonEmptyStrings` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `project_geometry_not_significant` | `_NonEmptyStrings` | `required` | `_NonEmptyStrings` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `under_construction` | `_NonEmptyStrings` | `required` | `_NonEmptyStrings` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- `_valid_groups` — `def _valid_groups(self) -> Self:`; decorators `model_validator(mode='after')`. The complete method algorithm appears in the function/method section.

### `_LightVehicleAccessConfig`

**Purpose:** Represents checked-in or resolved configuration fields and validates their exact domain before use.

**Inheritance:** `_StrictPolicyModel`.

**Model form and mutability:** class inheriting from `_StrictPolicyModel`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `open` | `_NonEmptyStrings` | `required` | `_NonEmptyStrings` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `toll` | `_NonEmptyStrings` | `required` | `_NonEmptyStrings` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `rights_restricted` | `_NonEmptyStrings` | `required` | `_NonEmptyStrings` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `physically_impossible` | `_NonEmptyStrings` | `required` | `_NonEmptyStrings` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- `_valid_groups` — `def _valid_groups(self) -> Self:`; decorators `model_validator(mode='after')`. The complete method algorithm appears in the function/method section.

### `_RoadNatureConfig`

**Purpose:** Represents checked-in or resolved configuration fields and validates their exact domain before use.

**Inheritance:** `_StrictPolicyModel`.

**Model form and mutability:** class inheriting from `_StrictPolicyModel`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `general_motor_road` | `_NonEmptyStrings` | `required` | `_NonEmptyStrings` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `limited_motor_proxy` | `_NonEmptyStrings` | `required` | `_NonEmptyStrings` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `non_general_vehicle` | `_NonEmptyStrings` | `required` | `_NonEmptyStrings` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `special_review` | `_NonEmptyStrings` | `required` | `_NonEmptyStrings` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- `_valid_groups` — `def _valid_groups(self) -> Self:`; decorators `model_validator(mode='after')`. The complete method algorithm appears in the function/method section.

### `_ImportanceConfig`

**Purpose:** Represents checked-in or resolved configuration fields and validates their exact domain before use.

**Inheritance:** `_StrictPolicyModel`.

**Model form and mutability:** class inheriting from `_StrictPolicyModel`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `known` | `_NonEmptyStrings` | `required` | `_NonEmptyStrings` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `limited` | `_NonEmptyStrings` | `required` | `_NonEmptyStrings` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- `_valid_domain` — `def _valid_domain(self) -> Self:`; decorators `model_validator(mode='after')`. The complete method algorithm appears in the function/method section.

### `_SourceValuesConfig`

**Purpose:** Represents checked-in or resolved configuration fields and validates their exact domain before use.

**Inheritance:** `_StrictPolicyModel`.

**Model form and mutability:** class inheriting from `_StrictPolicyModel`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `asset_state` | `_AssetStateConfig` | `required` | `_AssetStateConfig` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `light_vehicle_access` | `_LightVehicleAccessConfig` | `required` | `_LightVehicleAccessConfig` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `nature` | `_RoadNatureConfig` | `required` | `_RoadNatureConfig` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `known_restriction_review` | `_NonEmptyStrings` | `required` | `_NonEmptyStrings` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `importance` | `_ImportanceConfig` | `required` | `_ImportanceConfig` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `width_below_m` | `Annotated[StrictFloat, Field(gt=0, allow_inf_nan=False)]` | `required` | Metric distance or length in metres; the full field name identifies the measurement. |

**Validators and methods:**

- `_valid_values` — `def _valid_values(self) -> Self:`; decorators `model_validator(mode='after')`. The complete method algorithm appears in the function/method section.

### `_DecisionOutcomesConfig`

**Purpose:** Represents checked-in or resolved configuration fields and validates their exact domain before use.

**Inheritance:** `_StrictPolicyModel`.

**Model form and mutability:** class inheriting from `_StrictPolicyModel`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `fictitious_geometry` | `Literal['NOT_DISTANCE_PROXY']` | `required` | `Literal['NOT_DISTANCE_PROXY']` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `project_geometry_not_significant` | `Literal['NOT_DISTANCE_PROXY']` | `required` | `Literal['NOT_DISTANCE_PROXY']` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `not_in_service` | `Literal['NOT_GENERAL_VEHICLE_PROXY']` | `required` | `Literal['NOT_GENERAL_VEHICLE_PROXY']` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `physically_impossible` | `Literal['NOT_GENERAL_VEHICLE_PROXY']` | `required` | `Literal['NOT_GENERAL_VEHICLE_PROXY']` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `non_general_vehicle_nature` | `Literal['NOT_GENERAL_VEHICLE_PROXY']` | `required` | `Literal['NOT_GENERAL_VEHICLE_PROXY']` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `rights_restricted` | `Literal['RESTRICTED_REVIEW']` | `required` | `Literal['RESTRICTED_REVIEW']` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `private_road` | `Literal['RESTRICTED_REVIEW']` | `required` | `Literal['RESTRICTED_REVIEW']` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `temporal_closure` | `Literal['RESTRICTED_REVIEW']` | `required` | `Literal['RESTRICTED_REVIEW']` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `known_restriction` | `Literal['RESTRICTED_REVIEW']` | `required` | `Literal['RESTRICTED_REVIEW']` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `other_recorded_restriction` | `Literal['RESTRICTED_REVIEW']` | `required` | `Literal['RESTRICTED_REVIEW']` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `special_nature` | `Literal['RESTRICTED_REVIEW']` | `required` | `Literal['RESTRICTED_REVIEW']` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `limited_nature` | `Literal['LIMITED_VEHICLE_PROXY']` | `required` | `Literal['LIMITED_VEHICLE_PROXY']` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `importance_6` | `Literal['LIMITED_VEHICLE_PROXY']` | `required` | `Literal['LIMITED_VEHICLE_PROXY']` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `narrow_carriageway` | `Literal['LIMITED_VEHICLE_PROXY']` | `required` | `Literal['LIMITED_VEHICLE_PROXY']` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `open_or_toll` | `Literal['GENERAL_VEHICLE_PROXY']` | `required` | `Literal['GENERAL_VEHICLE_PROXY']` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `unknown` | `Literal['UNKNOWN_REVIEW']` | `required` | `Literal['UNKNOWN_REVIEW']` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `_PolicyConfig`

**Purpose:** Represents checked-in or resolved configuration fields and validates their exact domain before use.

**Inheritance:** `_StrictPolicyModel`.

**Model form and mutability:** class inheriting from `_StrictPolicyModel`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `policy_id` | `_ExactString` | `required` | Exact portable identity used to join lineage or evidence across frames and result envelopes. |
| `schema_version` | `StrictInt` | `required` | `StrictInt` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `scope` | `_ExactString` | `required` | `_ExactString` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `references` | `_ReferencesConfig` | `required` | `_ReferencesConfig` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `evidence_checked_on` | `Literal['2026-08-16']` | `required` | `Literal['2026-08-16']` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `vehicle_scope` | `Literal['LIGHT_VEHICLE_AND_GENERAL_CAR_NETWORK']` | `required` | `Literal['LIGHT_VEHICLE_AND_GENERAL_CAR_NETWORK']` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `heavy_vehicle_access` | `Literal['NOT_PROVEN']` | `required` | `Literal['NOT_PROVEN']` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `classes` | `_ClassesConfig` | `required` | `_ClassesConfig` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `source_values` | `_SourceValuesConfig` | `required` | Source lineage or source-bound object whose exact identity is checked before downstream use. |
| `decision_precedence` | `_NonEmptyStrings` | `required` | `_NonEmptyStrings` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `decision_outcomes` | `_DecisionOutcomesConfig` | `required` | `_DecisionOutcomesConfig` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- `_valid_identity_and_precedence` — `def _valid_identity_and_precedence(self) -> Self:`; decorators `model_validator(mode='after')`. The complete method algorithm appears in the function/method section.

### `_CompiledClasses`

**Purpose:** Groups the `CompiledClasses` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `general_vehicle_proxy` | `str` | `required` | `str` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `limited_vehicle_proxy` | `str` | `required` | `str` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `restricted_review` | `str` | `required` | `str` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `not_general_vehicle_proxy` | `str` | `required` | `str` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `not_distance_proxy` | `str` | `required` | `str` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `unknown_review` | `str` | `required` | `str` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- `values` — `def values(self) -> tuple[str, ...]:`; decorators `property`. The complete method algorithm appears in the function/method section.

### `_CompiledAssetState`

**Purpose:** Groups the `CompiledAssetState` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `in_service` | `frozenset[str]` | `required` | `frozenset[str]` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `project_geometry_not_significant` | `frozenset[str]` | `required` | `frozenset[str]` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `under_construction` | `frozenset[str]` | `required` | `frozenset[str]` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `_CompiledNavigationReference`

**Purpose:** Groups the `CompiledNavigationReference` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `publisher` | `str` | `required` | `str` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `title` | `str` | `required` | `str` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `revision` | `str` | `required` | `str` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `evidence_scope` | `str` | `required` | `str` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `_CompiledBdTopoProductReference`

**Purpose:** Groups the `CompiledBdTopoProductReference` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `publisher` | `str` | `required` | `str` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `title` | `str` | `required` | `str` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `document_id` | `str` | `required` | Exact portable identity used to join lineage or evidence across frames and result envelopes. |
| `revision` | `str` | `required` | `str` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `evidence_scope` | `str` | `required` | `str` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `_CompiledLightVehicleAccess`

**Purpose:** Groups the `CompiledLightVehicleAccess` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `open` | `frozenset[str]` | `required` | `frozenset[str]` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `toll` | `frozenset[str]` | `required` | `frozenset[str]` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `rights_restricted` | `frozenset[str]` | `required` | `frozenset[str]` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `physically_impossible` | `frozenset[str]` | `required` | `frozenset[str]` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `_CompiledRoadNature`

**Purpose:** Groups the `CompiledRoadNature` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `general_motor_road` | `frozenset[str]` | `required` | `frozenset[str]` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `limited_motor_proxy` | `frozenset[str]` | `required` | `frozenset[str]` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `non_general_vehicle` | `frozenset[str]` | `required` | `frozenset[str]` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `special_review` | `frozenset[str]` | `required` | `frozenset[str]` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `_CompiledImportance`

**Purpose:** Groups the `CompiledImportance` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `known` | `frozenset[str]` | `required` | `frozenset[str]` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `limited` | `frozenset[str]` | `required` | `frozenset[str]` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `_CompiledDecisionOutcomes`

**Purpose:** Groups the `CompiledDecisionOutcomes` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `fictitious_geometry` | `str` | `required` | `str` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `project_geometry_not_significant` | `str` | `required` | `str` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `not_in_service` | `str` | `required` | `str` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `physically_impossible` | `str` | `required` | `str` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `non_general_vehicle_nature` | `str` | `required` | `str` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `rights_restricted` | `str` | `required` | `str` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `private_road` | `str` | `required` | `str` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `temporal_closure` | `str` | `required` | `str` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `known_restriction` | `str` | `required` | `str` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `other_recorded_restriction` | `str` | `required` | `str` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `special_nature` | `str` | `required` | `str` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `limited_nature` | `str` | `required` | `str` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `importance_6` | `str` | `required` | `str` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `narrow_carriageway` | `str` | `required` | `str` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `open_or_toll` | `str` | `required` | `str` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `unknown` | `str` | `required` | `str` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `IgnRoadVehicleProxyPolicy`

**Purpose:** Immutable policy evidence compiled from the exact checked-in YAML bytes.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `policy_id` | `str` | `required` | Exact portable identity used to join lineage or evidence across frames and result envelopes. |
| `schema_version` | `int` | `required` | `int` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `scope` | `str` | `required` | `str` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `navigation_reference` | `_CompiledNavigationReference` | `required` | `_CompiledNavigationReference` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `bdtopo_product_reference` | `_CompiledBdTopoProductReference` | `required` | `_CompiledBdTopoProductReference` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `evidence_checked_on` | `str` | `required` | `str` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `vehicle_scope` | `str` | `required` | `str` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `heavy_vehicle_access` | `str` | `required` | `str` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `classes` | `_CompiledClasses` | `required` | `_CompiledClasses` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `asset_state` | `_CompiledAssetState` | `required` | `_CompiledAssetState` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `light_vehicle_access` | `_CompiledLightVehicleAccess` | `required` | `_CompiledLightVehicleAccess` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `nature` | `_CompiledRoadNature` | `required` | `_CompiledRoadNature` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `known_restriction_review` | `frozenset[str]` | `required` | `frozenset[str]` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `importance` | `_CompiledImportance` | `required` | `_CompiledImportance` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `width_below_m` | `float` | `required` | Metric distance or length in metres; the full field name identifies the measurement. |
| `decision_precedence` | `tuple[str, ...]` | `required` | `tuple[str, ...]` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `decision_outcomes` | `_CompiledDecisionOutcomes` | `required` | `_CompiledDecisionOutcomes` state used by `src/landscout/stages/road_vehicle_proxy_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `config_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |

**Validators and methods:**

- None.

### `_UniqueKeyLoader`

**Purpose:** Groups the `UniqueKeyLoader` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `yaml.SafeLoader`.

**Model form and mutability:** class inheriting from `yaml.SafeLoader`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

## 6. Functions and methods

### `_exact_string`

**Signature**

```python
def _exact_string(value: str) -> str:
```

**Purpose**

Implements exact string according to the exact implementation and guards in this file.

**Inputs**

- `value` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `value`.

**Algorithm**

1. Checks `value != value.strip()`. When true: Raises `ValueError('policy strings must not contain edge whitespace')`.
2. Returns `value`.

**Validation and invariants**

- Rejects or diverts the path when `value != value.strip()` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `value.strip`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_require_unique`

**Signature**

```python
def _require_unique(values: tuple[str, ...], label: str) -> None:
```

**Purpose**

Implements require unique according to the exact implementation and guards in this file.

**Inputs**

- `values` (`tuple[str, ...]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `len(values) != len(set(values))`. When true: Raises `ValueError(f'{label} contains duplicate source values')`.

**Validation and invariants**

- Rejects or diverts the path when `len(values) != len(set(values))` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `len`, `set`.

**Known repository callers**

- `src/landscout/stages/road_vehicle_proxy_policy.py` — `_AssetStateConfig._valid_groups`
- `src/landscout/stages/road_vehicle_proxy_policy.py` — `_ImportanceConfig._valid_domain`
- `src/landscout/stages/road_vehicle_proxy_policy.py` — `_LightVehicleAccessConfig._valid_groups`
- `src/landscout/stages/road_vehicle_proxy_policy.py` — `_RoadNatureConfig._valid_groups`
- `src/landscout/stages/road_vehicle_proxy_policy.py` — `_SourceValuesConfig._valid_values`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_require_disjoint`

**Signature**

```python
def _require_disjoint(groups: tuple[tuple[str, ...], ...], label: str) -> None:
```

**Purpose**

Implements require disjoint according to the exact implementation and guards in this file.

**Inputs**

- `groups` (`tuple[tuple[str, ...], ...]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `flattened` from `tuple((value for group in groups for value in group))`.
2. Checks `len(flattened) != len(set(flattened))`. When true: Raises `ValueError(f'{label} source groups overlap')`.

**Validation and invariants**

- Rejects or diverts the path when `len(flattened) != len(set(flattened))` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `len`, `set`, `tuple`.

**Known repository callers**

- `src/landscout/stages/road_vehicle_proxy_policy.py` — `_AssetStateConfig._valid_groups`
- `src/landscout/stages/road_vehicle_proxy_policy.py` — `_LightVehicleAccessConfig._valid_groups`
- `src/landscout/stages/road_vehicle_proxy_policy.py` — `_RoadNatureConfig._valid_groups`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_AssetStateConfig._valid_groups`

**Signature**

```python
def _valid_groups(self) -> Self:
```

**Purpose**

Implements valid groups according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `Self`. Observed return expression(s): `self`.

**Algorithm**

1. Computes `groups` from `(self.in_service, self.project_geometry_not_significant, self.under_construction)`.
2. Iterates `(name, values)` over `zip(('in_service', 'project_geometry_not_significant', 'under_construction'), groups, strict=True)`. For each value: Calls `_require_unique(values, name)` for its validation or side effect.
3. Calls `_require_disjoint(groups, 'asset_state')` for its validation or side effect.
4. Checks `groups != (('En service',), ('En projet',), ('En construction',))`. When true: Raises `ValueError('asset_state groups must cover the exact source domain')`.
5. Returns `self`.

**Validation and invariants**

- Rejects or diverts the path when `groups != (('En service',), ('En projet',), ('En construction',))` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `_require_disjoint`, `_require_unique`, `model_validator`, `zip`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_LightVehicleAccessConfig._valid_groups`

**Signature**

```python
def _valid_groups(self) -> Self:
```

**Purpose**

Implements valid groups according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `Self`. Observed return expression(s): `self`.

**Algorithm**

1. Computes `groups` from `(self.open, self.toll, self.rights_restricted, self.physically_impossible)`.
2. Iterates `(name, values)` over `zip(('open', 'toll', 'rights_restricted', 'physically_impossible'), groups, strict=True)`. For each value: Calls `_require_unique(values, name)` for its validation or side effect.
3. Calls `_require_disjoint(groups, 'light_vehicle_access')` for its validation or side effect.
4. Returns `self`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_require_disjoint`, `_require_unique`, `model_validator`, `zip`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_RoadNatureConfig._valid_groups`

**Signature**

```python
def _valid_groups(self) -> Self:
```

**Purpose**

Implements valid groups according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `Self`. Observed return expression(s): `self`.

**Algorithm**

1. Computes `groups` from `(self.general_motor_road, self.limited_motor_proxy, self.non_general_vehicle, self.special_review)`.
2. Iterates `(name, values)` over `zip(('general_motor_road', 'limited_motor_proxy', 'non_general_vehicle', 'special_review'), groups, strict=True)`. For each value: Calls `_require_unique(values, name)` for its validation or side effect.
3. Calls `_require_disjoint(groups, 'nature')` for its validation or side effect.
4. Returns `self`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_require_disjoint`, `_require_unique`, `model_validator`, `zip`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_ImportanceConfig._valid_domain`

**Signature**

```python
def _valid_domain(self) -> Self:
```

**Purpose**

Implements valid domain according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `Self`. Observed return expression(s): `self`.

**Algorithm**

1. Calls `_require_unique(self.known, 'importance.known')` for its validation or side effect.
2. Calls `_require_unique(self.limited, 'importance.limited')` for its validation or side effect.
3. Checks `self.known != ('1', '2', '3', '4', '5', '6')`. When true: Raises `ValueError('importance.known must cover exactly source values 1-6')`.
4. Checks `self.limited != ('6',)`. When true: Raises `ValueError("importance.limited must contain exactly source value '6'")`.
5. Checks `not set(self.limited).issubset(self.known)`. When true: Raises `ValueError('importance.limited must be a subset of importance.known')`.
6. Returns `self`.

**Validation and invariants**

- Rejects or diverts the path when `self.known != ('1', '2', '3', '4', '5', '6')` is true.
- Rejects or diverts the path when `self.limited != ('6',)` is true.
- Rejects or diverts the path when `not set(self.limited).issubset(self.known)` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `_require_unique`, `model_validator`, `set`, `set(self.limited).issubset`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_SourceValuesConfig._valid_values`

**Signature**

```python
def _valid_values(self) -> Self:
```

**Purpose**

Implements valid values according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `Self`. Observed return expression(s): `self`.

**Algorithm**

1. Calls `_require_unique(self.known_restriction_review, 'known_restriction_review')` for its validation or side effect.
2. Returns `self`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_require_unique`, `model_validator`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_PolicyConfig._valid_identity_and_precedence`

**Signature**

```python
def _valid_identity_and_precedence(self) -> Self:
```

**Purpose**

Implements valid identity and precedence according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `Self`. Observed return expression(s): `self`.

**Algorithm**

1. Checks `self.policy_id != _POLICY_ID`. When true: Raises `ValueError('policy_id is not the approved v2 policy identity')`.
2. Checks `self.schema_version != 2`. When true: Raises `ValueError('schema_version must be exactly 2')`.
3. Checks `self.scope != _POLICY_SCOPE`. When true: Raises `ValueError('scope is not the approved official IGN evidence scope')`.
4. Checks `self.decision_precedence != _EXPECTED_PRECEDENCE`. When true: Raises `ValueError('decision_precedence differs from approved v2 order')`.
5. Returns `self`.

**Validation and invariants**

- Rejects or diverts the path when `self.policy_id != _POLICY_ID` is true.
- Rejects or diverts the path when `self.schema_version != 2` is true.
- Rejects or diverts the path when `self.scope != _POLICY_SCOPE` is true.
- Rejects or diverts the path when `self.decision_precedence != _EXPECTED_PRECEDENCE` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `model_validator`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_CompiledClasses.values`

**Signature**

```python
def values(self) -> tuple[str, ...]:
```

**Purpose**

Implements values according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[str, ...]`. Observed return expression(s): `(self.general_vehicle_proxy, self.limited_vehicle_proxy, self.restricted_review, self.not_general_vehicle_proxy, self.not_distance_proxy, self.unknown_review)`.

**Algorithm**

1. Returns `(self.general_vehicle_proxy, self.limited_vehicle_proxy, self.restricted_review, self.not_general_vehicle_proxy, self.not_distance_proxy, self.unknown_review)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- No function calls.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_construct_unique_mapping`

**Signature**

```python
def _construct_unique_mapping(
    loader: yaml.SafeLoader,
    node: yaml.MappingNode,
    deep: bool = False,
) -> dict[object, object]:
```

**Purpose**

Implements construct unique mapping according to the exact implementation and guards in this file.

**Inputs**

- `loader` (`yaml.SafeLoader`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `node` (`yaml.MappingNode`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `deep` (`bool`; optional/default `False`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[object, object]`. Observed return expression(s): `result`.

**Algorithm**

1. Defines `result` with annotation `dict[object, object]` from `{}`.
2. Iterates `(key_node, value_node)` over `node.value`. For each value: Computes `key` from `loader.construct_object(key_node, deep=deep)`. Checks `key in result`. When true: Raises `IgnRoadVehicleProxyPolicyError(f'Duplicate YAML road-policy key: {key!r}')`. Computes `result[key]` from `loader.construct_object(value_node, deep=deep)`.
3. Returns `result`.

**Validation and invariants**

- Rejects or diverts the path when `key in result` is true.

**Exceptions**

- Explicitly raises: `IgnRoadVehicleProxyPolicyError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `IgnRoadVehicleProxyPolicyError`, `loader.construct_object`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_compile_policy`

**Signature**

```python
def _compile_policy(
    config: _PolicyConfig,
    config_sha256: str,
) -> IgnRoadVehicleProxyPolicy:
```

**Purpose**

Compiles policy according to the exact implementation and guards in this file.

**Inputs**

- `config` (`_PolicyConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `config_sha256` (`str`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `IgnRoadVehicleProxyPolicy`. Observed return expression(s): `IgnRoadVehicleProxyPolicy(policy_id=config.policy_id, schema_version=config.schema_version, scope=config.scope, navigation_reference=_CompiledNavigationReference(publisher=config.references.navigation.publisher, title=config.references.navigation.title, revision=config.references.navigation.revision, evidence_scope=config.references.navigation.evidence_scope), bdtopo_product_reference=_CompiledBd…`.

**Algorithm**

1. Computes `classes` from `config.classes`.
2. Computes `source_values` from `config.source_values`.
3. Computes `access` from `source_values.light_vehicle_access`.
4. Computes `nature` from `source_values.nature`.
5. Computes `outcomes` from `config.decision_outcomes`.
6. Returns `IgnRoadVehicleProxyPolicy(policy_id=config.policy_id, schema_version=config.schema_version, scope=config.scope, navigation_reference=_CompiledNavigationReference(publisher=config.references.navigation.publisher, title=config.references.navigation.title, revision=config.references.navigation.revision, evidence_scope=config.references.navigation.evidence_scop…`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `IgnRoadVehicleProxyPolicy`, `_CompiledAssetState`, `_CompiledBdTopoProductReference`, `_CompiledClasses`, `_CompiledDecisionOutcomes`, `_CompiledImportance`, `_CompiledLightVehicleAccess`, `_CompiledNavigationReference`, `_CompiledRoadNature`, `frozenset`.

**Known repository callers**

- `src/landscout/stages/road_vehicle_proxy_policy.py` — `load_ign_road_vehicle_proxy_policy`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `load_ign_road_vehicle_proxy_policy`

**Signature**

```python
def load_ign_road_vehicle_proxy_policy(
    path: Path = _DEFAULT_POLICY_PATH,
) -> IgnRoadVehicleProxyPolicy:
```

**Purpose**

Load and compile the strict policy from its exact UTF-8 file bytes.

**Inputs**

- `path` (`Path`; optional/default `_DEFAULT_POLICY_PATH`) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `IgnRoadVehicleProxyPolicy`. Observed return expression(s): `_compile_policy(config, sha256(policy_bytes).hexdigest())`.

**Algorithm**

1. Runs guarded operation: Computes `policy_bytes` from `Path(path).read_bytes()`. Computes `payload` from `yaml.load(policy_bytes.decode('utf-8'), Loader=_UniqueKeyLoader)`. Checks `not isinstance(payload, Mapping)`. When true: Raises `IgnRoadVehicleProxyPolicyError('IGN road vehicle-proxy policy must be a mapping')`. Computes `config` from `_PolicyConfig.model_validate(payload)`. Executes 1 additional source-ordered statement(s). Handles `IgnRoadVehicleProxyPolicyError`, `Exception`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(payload, Mapping)` is true.

**Exceptions**

- Explicitly raises: `IgnRoadVehicleProxyPolicyError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `Path(path).read_bytes`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `IgnRoadVehicleProxyPolicyError`, `Path`, `Path(path).read_bytes`, `_PolicyConfig.model_validate`, `_compile_policy`, `isinstance`, `policy_bytes.decode`, `sha256`, `sha256(policy_bytes).hexdigest`, `yaml.load`.

**Known repository callers**

- `src/landscout/stages/apply_road_vehicle_proxy_policy.py` — `_apply_ign_road_vehicle_proxy_policy`
- `src/landscout/stages/assess_road_proximity_coverage.py` — `_assess_road_proximity_coverage`
- `src/landscout/stages/enrich_road_proximity.py` — `_enrich_parcel_road_proximity`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py` — `test_every_configured_known_restriction_is_applied`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py` — `test_policy_lineage_is_exact_on_every_row`
- `tests/unit/test_assess_road_proximity_coverage.py` — `_proximity`
- `tests/unit/test_enrich_road_proximity.py` — `_road_row`
- `tests/unit/test_enrich_road_proximity.py` — `test_selected_road_evidence_and_lineage_are_exact`
- `tests/unit/test_road_vehicle_proxy_policy.py` — `_load_payload`
- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_approved_class_vocabulary_has_no_heavy_or_legal_claim`
- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_asset_state_groups_cover_exact_v2_domain`
- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_checked_in_policy_hash_binds_exact_file_bytes`
- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_checked_in_policy_loads_with_exact_public_identity_and_reference`
- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_compiled_policy_structures_are_immutable`
- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_decision_precedence_and_rule_outcomes_are_approved`
- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_importance_domains_expose_known_without_positive_classification`
- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_malformed_yaml_has_controlled_error`
- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_missing_file_has_controlled_error`
- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_mutating_source_payload_cannot_affect_another_load`
- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_observed_d031_access_and_importance_vocabularies_are_compatible`
- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_observed_d031_natures_are_covered_exactly_once`
- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_project_geometry_rule_has_exact_precedence_position`
- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_repeat_loading_is_deterministic_and_independent`

**Tests**

- `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_every_configured_known_restriction_is_applied`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_policy_lineage_is_exact_on_every_row`
- `tests/unit/test_enrich_road_proximity.py::test_selected_road_evidence_and_lineage_are_exact`
- `tests/unit/test_road_vehicle_proxy_policy.py::test_approved_class_vocabulary_has_no_heavy_or_legal_claim`
- `tests/unit/test_road_vehicle_proxy_policy.py::test_asset_state_groups_cover_exact_v2_domain`
- `tests/unit/test_road_vehicle_proxy_policy.py::test_checked_in_policy_hash_binds_exact_file_bytes`
- `tests/unit/test_road_vehicle_proxy_policy.py::test_checked_in_policy_loads_with_exact_public_identity_and_reference`
- `tests/unit/test_road_vehicle_proxy_policy.py::test_compiled_policy_structures_are_immutable`
- `tests/unit/test_road_vehicle_proxy_policy.py::test_decision_precedence_and_rule_outcomes_are_approved`
- `tests/unit/test_road_vehicle_proxy_policy.py::test_importance_domains_expose_known_without_positive_classification`
- `tests/unit/test_road_vehicle_proxy_policy.py::test_malformed_yaml_has_controlled_error`
- `tests/unit/test_road_vehicle_proxy_policy.py::test_missing_file_has_controlled_error`
- `tests/unit/test_road_vehicle_proxy_policy.py::test_mutating_source_payload_cannot_affect_another_load`
- `tests/unit/test_road_vehicle_proxy_policy.py::test_observed_d031_access_and_importance_vocabularies_are_compatible`
- `tests/unit/test_road_vehicle_proxy_policy.py::test_observed_d031_natures_are_covered_exactly_once`
- `tests/unit/test_road_vehicle_proxy_policy.py::test_project_geometry_rule_has_exact_precedence_position`
- `tests/unit/test_road_vehicle_proxy_policy.py::test_repeat_loading_is_deterministic_and_independent`

**Business interpretation**

This symbol contributes to the `road` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `2025-11` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `2026-05-27` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `2026-08-16` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `BD TOPO® Version 3.5 - Descriptif de contenu` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `Calcul d’itinéraire` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `DC_BDTOPO_3-5` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `GENERAL_CAR_ROUTING_RULES` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `GENERAL_VEHICLE_PROXY` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `IGN` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `LIGHT_VEHICLE_AND_GENERAL_CAR_NETWORK` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `LIMITED_VEHICLE_PROXY` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `NOT_DISTANCE_PROXY` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `NOT_GENERAL_VEHICLE_PROXY` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `NOT_PROVEN` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `RESTRICTED_REVIEW` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `SOURCE_ATTRIBUTE_SEMANTICS` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `UNKNOWN_REVIEW` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |

## 8. Interfaces

Known static callers, internal calls, and tests are listed for every symbol. Package-level availability is controlled by this module's `__all__` and the relevant package `__init__.py`; private helpers are not a stable public API.

## 9. Error handling

Every explicit raise and guarded condition is listed with its function. Public boundaries translate malformed source/configuration/input conditions into the controlled exception classes shown by those functions and tests; raw implementation errors are not promised as API.

## 10. Side effects

Per-function side effects are derived from actual calls. Source adapters may perform guarded network, cache, archive, or filesystem operations; stages normally operate on copies unless their preservation validators state otherwise; tests use the boundaries stated per test.

## 11. Security / trust boundaries

Trust claims are limited to the explicit byte, schema, lineage, source-complete, path, URL, geometry, or policy checks implemented by this file and its callees. Textual lineage is not treated as physical proof unless the function revalidates the physical source.

## 12. GIS / CRS rules

GIS rules apply only where geometry/CRS calls or columns are listed above. Storage geometry is not silently repaired; metric work uses the explicit CRS transformations and calculation copies visible in the algorithm. Files without GIS calls impose no CRS contract.

## 13. Provenance rules

Provenance is carried only through exact source/configuration/hash fields shown by the models, constants, and frame columns. Consult `docs/code/SOURCE_TRUST_MODEL.md` for the cross-adapter chain.

## 14. Business meaning

This file contributes to LandScout's `road` evidence flow as described by its purpose and public symbols. It preserves the distinction among fact, proxy evidence, policy interpretation, diagnostic status, and parcel precheck.

## 15. Explicit non-goals

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

## 16. Tests

Direct name-resolved tests appear under each symbol. Higher-level tests may exercise private helpers through a public source-complete function; companion documents for all test files describe their fixtures, actions, assertions, and boundaries.

## 17. Change impact

Changing this file requires reviewing its static callers, package exports, directly mapped tests, relevant schema/hash/version constants, source locks, persisted artifact contracts, and the corresponding pipeline/cross-cutting documents. Any byte change makes the SHA256 above stale and requires regenerating this companion.

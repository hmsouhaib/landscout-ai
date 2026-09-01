# `tests/unit/test_road_vehicle_proxy_policy.py`

## File identity

- Repository path: `tests/unit/test_road_vehicle_proxy_policy.py`
- File type: Python source
- Layer: unit/regression test
- Domain: isolated contract test evidence
- Responsibility: Provides complete unit and regression coverage for the `road_vehicle_proxy_policy` contracts exercised in this file.
- Source SHA256: `e20c61a170cdffde5387fd4b367e5433097c0c333c830843e52bd5e73a14b4fc`

## 1. STEP 7F.1A.4 contract delta

- Refreshes permanent STEP 7F.1A.4 regression coverage for road vehicle proxy policy; the exact fixtures, mutations, calls, controlled failures, and assertions are inventoried below.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Provides complete unit and regression coverage for the `road_vehicle_proxy_policy` contracts exercised in this file.

The file belongs to the **unit/regression test** layer and **isolated contract test evidence** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `from dataclasses import FrozenInstanceError`
- `from hashlib import sha256`
- `from pathlib import Path`
- `from typing import Any`

### Third-party packages

- `import pytest`
- `import yaml`

### Internal LandScout imports

- `from landscout import stages`
- `from landscout.stages.road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyPolicy,
    IgnRoadVehicleProxyPolicyError,
    load_ign_road_vehicle_proxy_policy,
)`
- `import landscout.stages.road_vehicle_proxy_policy as module`

## 4. Contract taxonomy

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `POLICY_PATH`

- Category: module constant or closed domain.
- Exact declaration:

```python
POLICY_PATH = Path("configs/access/ign_bdtopo_vehicle_proxy_policy.yaml")
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `EXPECTED_POLICY_ID`

- Category: module constant or closed domain.
- Exact declaration:

```python
EXPECTED_POLICY_ID = "ign_bdtopo_general_vehicle_proxy_v2"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `EXPECTED_SCOPE`

- Category: module constant or closed domain.
- Exact declaration:

```python
EXPECTED_SCOPE = "OFFICIAL_IGN_CAR_ROUTING_EVIDENCE_ONLY"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `EXPECTED_CLASSES`

- Category: module constant or closed domain.
- Exact declaration:

```python
EXPECTED_CLASSES = (
    "GENERAL_VEHICLE_PROXY",
    "LIMITED_VEHICLE_PROXY",
    "RESTRICTED_REVIEW",
    "NOT_GENERAL_VEHICLE_PROXY",
    "NOT_DISTANCE_PROXY",
    "UNKNOWN_REVIEW",
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `GENERAL_VEHICLE_PROXY`
  - `LIMITED_VEHICLE_PROXY`
  - `RESTRICTED_REVIEW`
  - `NOT_GENERAL_VEHICLE_PROXY`
  - `NOT_DISTANCE_PROXY`
  - `UNKNOWN_REVIEW`

### `EXPECTED_PRECEDENCE`

- Category: module constant or closed domain.
- Exact declaration:

```python
EXPECTED_PRECEDENCE = (
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

### `OBSERVED_NATURES`

- Category: module constant or closed domain.
- Exact declaration:

```python
OBSERVED_NATURES = {
    "Route à 1 chaussée",
    "Chemin",
    "Route empierrée",
    "Sentier",
    "Rond-point",
    "Route à 2 chaussées",
    "Type autoroutier",
    "Bretelle",
    "Escalier",
    "Bac ou liaison maritime",
}
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `Bac ou liaison maritime`
  - `Rond-point`
  - `Type autoroutier`
  - `Route à 1 chaussée`
  - `Chemin`
  - `Sentier`
  - `Bretelle`
  - `Route à 2 chaussées`
  - `Route empierrée`
  - `Escalier`

### `OBSERVED_LIGHT_VEHICLE_ACCESS`

- Category: module constant or closed domain.
- Exact declaration:

```python
OBSERVED_LIGHT_VEHICLE_ACCESS = {
    "Libre",
    "Physiquement impossible",
    "Restreint aux ayants droit",
    "A péage",
}
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `Libre`
  - `A péage`
  - `Restreint aux ayants droit`
  - `Physiquement impossible`


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

No top-level class/model/dataclass is declared.

## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `_payload`

**Purpose:** Implements `payload` within the file role: Provides complete unit and regression coverage for the `road_vehicle_proxy_policy` contracts exercised in this file.

**Exact signature**

```python
def _payload() -> dict[str, Any]:
```

- Exact decorators: none.
- Declared return annotation: `dict[str, Any]`.

**Inputs**

- No parameters.

**Return and exception contract**

- Exact observed return expressions:
  - `payload`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert isinstance(payload, dict)`

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_invalid_config_structure_is_rejected` via `_payload`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_invalid_config_structure_is_rejected` via `_payload`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_unsupported_schema_version_is_rejected` via `_payload`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_unsupported_schema_version_is_rejected` via `_payload`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_wrong_policy_identity_is_rejected` via `_payload`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_wrong_policy_identity_is_rejected` via `_payload`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_both_evidence_references_are_required` via `_payload`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_both_evidence_references_are_required` via `_payload`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_product_reference_document_id_is_exact` via `_payload`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_product_reference_document_id_is_exact` via `_payload`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_unknown_evidence_reference_is_rejected` via `_payload`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_unknown_evidence_reference_is_rejected` via `_payload`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_asset_state_group_overlap_is_rejected` via `_payload`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_asset_state_group_overlap_is_rejected` via `_payload`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_missing_known_asset_state_is_rejected` via `_payload`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_missing_known_asset_state_is_rejected` via `_payload`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_unknown_additional_asset_state_is_rejected` via `_payload`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_unknown_additional_asset_state_is_rejected` via `_payload`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_semantic_values_must_be_exact_non_empty_strings` via `_payload`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_semantic_values_must_be_exact_non_empty_strings` via `_payload`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_duplicate_semantic_value_is_rejected` via `_payload`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_duplicate_semantic_value_is_rejected` via `_payload`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_semantic_groups_must_be_pairwise_disjoint` via `_payload`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_semantic_groups_must_be_pairwise_disjoint` via `_payload`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_duplicate_known_restriction_is_rejected` via `_payload`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_duplicate_known_restriction_is_rejected` via `_payload`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_invalid_width_threshold_is_rejected` via `_payload`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_invalid_width_threshold_is_rejected` via `_payload`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_exact_width_threshold_is_accepted` via `_payload`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_exact_width_threshold_is_accepted` via `_payload`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_importance_domains_must_be_exact` via `_payload`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_importance_domains_must_be_exact` via `_payload`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_decision_precedence_must_be_exact` via `_payload`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_decision_precedence_must_be_exact` via `_payload`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_output_class_vocabulary_must_be_exact` via `_payload`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_output_class_vocabulary_must_be_exact` via `_payload`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_mutating_source_payload_cannot_affect_another_load` via `_payload`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_mutating_source_payload_cannot_affect_another_load` via `_payload`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `yaml.safe_load` | `yaml.safe_load` |
| `POLICY_PATH.read_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `POLICY_PATH.read_text` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _payload() -> dict[str, Any]:
    payload = yaml.safe_load(POLICY_PATH.read_text(encoding="utf-8"))
    assert isinstance(payload, dict)
    return payload
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_write_policy`

**Purpose:** Implements `write policy` within the file role: Provides complete unit and regression coverage for the `road_vehicle_proxy_policy` contracts exercised in this file.

**Exact signature**

```python
def _write_policy(tmp_path: Path, payload: object) -> Path:
```

- Exact decorators: none.
- Declared return annotation: `Path`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `payload` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `path`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_road_vehicle_proxy_policy::_load_payload` via `_write_policy`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::_load_payload` via `_write_policy`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `yaml.safe_dump` | `yaml.safe_dump` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `path.write_text` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _write_policy(tmp_path: Path, payload: object) -> Path:
    path = tmp_path / "policy.yaml"
    path.write_text(
        yaml.safe_dump(payload, allow_unicode=True, sort_keys=False),
        encoding="utf-8",
    )
    return path
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_duplicate_yaml_policy_key_is_rejected`

**Purpose:** Regression invariant: duplicate yaml policy key is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_duplicate_yaml_policy_key_is_rejected(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnRoadVehicleProxyPolicyError, match="Duplicate YAML.*key")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `load_ign_road_vehicle_proxy_policy` | `landscout.stages.road_vehicle_proxy_policy.load_ign_road_vehicle_proxy_policy` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `path.write_text` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_duplicate_yaml_policy_key_is_rejected(tmp_path: Path) -> None:
    path = tmp_path / "duplicate.yaml"
    path.write_text("schema_version: 2\nschema_version: 2\n", encoding="utf-8")

    with pytest.raises(IgnRoadVehicleProxyPolicyError, match="Duplicate YAML.*key"):
        load_ign_road_vehicle_proxy_policy(path)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_load_payload`

**Purpose:** Implements `load payload` within the file role: Provides complete unit and regression coverage for the `road_vehicle_proxy_policy` contracts exercised in this file.

**Exact signature**

```python
def _load_payload(tmp_path: Path, payload: object) -> IgnRoadVehicleProxyPolicy:
```

- Exact decorators: none.
- Declared return annotation: `IgnRoadVehicleProxyPolicy`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `payload` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `load_ign_road_vehicle_proxy_policy(_write_policy(tmp_path, payload))`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_invalid_config_structure_is_rejected` via `_load_payload`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_invalid_config_structure_is_rejected` via `_load_payload`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_unsupported_schema_version_is_rejected` via `_load_payload`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_unsupported_schema_version_is_rejected` via `_load_payload`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_wrong_policy_identity_is_rejected` via `_load_payload`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_wrong_policy_identity_is_rejected` via `_load_payload`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_both_evidence_references_are_required` via `_load_payload`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_both_evidence_references_are_required` via `_load_payload`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_product_reference_document_id_is_exact` via `_load_payload`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_product_reference_document_id_is_exact` via `_load_payload`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_unknown_evidence_reference_is_rejected` via `_load_payload`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_unknown_evidence_reference_is_rejected` via `_load_payload`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_asset_state_group_overlap_is_rejected` via `_load_payload`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_asset_state_group_overlap_is_rejected` via `_load_payload`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_missing_known_asset_state_is_rejected` via `_load_payload`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_missing_known_asset_state_is_rejected` via `_load_payload`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_unknown_additional_asset_state_is_rejected` via `_load_payload`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_unknown_additional_asset_state_is_rejected` via `_load_payload`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_semantic_values_must_be_exact_non_empty_strings` via `_load_payload`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_semantic_values_must_be_exact_non_empty_strings` via `_load_payload`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_duplicate_semantic_value_is_rejected` via `_load_payload`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_duplicate_semantic_value_is_rejected` via `_load_payload`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_semantic_groups_must_be_pairwise_disjoint` via `_load_payload`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_semantic_groups_must_be_pairwise_disjoint` via `_load_payload`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_duplicate_known_restriction_is_rejected` via `_load_payload`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_duplicate_known_restriction_is_rejected` via `_load_payload`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_invalid_width_threshold_is_rejected` via `_load_payload`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_invalid_width_threshold_is_rejected` via `_load_payload`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_exact_width_threshold_is_accepted` via `_load_payload`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_exact_width_threshold_is_accepted` via `_load_payload`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_importance_domains_must_be_exact` via `_load_payload`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_importance_domains_must_be_exact` via `_load_payload`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_decision_precedence_must_be_exact` via `_load_payload`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_decision_precedence_must_be_exact` via `_load_payload`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_output_class_vocabulary_must_be_exact` via `_load_payload`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_output_class_vocabulary_must_be_exact` via `_load_payload`
- direct call: `tests.unit.test_road_vehicle_proxy_policy::test_non_mapping_yaml_has_controlled_error` via `_load_payload`
- value/type reference: `tests.unit.test_road_vehicle_proxy_policy::test_non_mapping_yaml_has_controlled_error` via `_load_payload`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `load_ign_road_vehicle_proxy_policy` | `landscout.stages.road_vehicle_proxy_policy.load_ign_road_vehicle_proxy_policy` |
| `_write_policy` | `tests.unit.test_road_vehicle_proxy_policy._write_policy` |

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
def _load_payload(tmp_path: Path, payload: object) -> IgnRoadVehicleProxyPolicy:
    return load_ign_road_vehicle_proxy_policy(_write_policy(tmp_path, payload))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_checked_in_policy_loads_with_exact_public_identity_and_reference`

**Purpose:** Regression invariant: checked in policy loads with exact public identity and reference. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_checked_in_policy_loads_with_exact_public_identity_and_reference() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert type(policy) is IgnRoadVehicleProxyPolicy`
  - `assert policy.policy_id == EXPECTED_POLICY_ID`
  - `assert policy.schema_version == 2`
  - `assert policy.scope == EXPECTED_SCOPE`
  - `assert policy.navigation_reference.publisher == "IGN"`
  - `assert policy.navigation_reference.title == "Calcul d’itinéraire"`
  - `assert policy.navigation_reference.revision == "2026-05-27"`
  - `assert policy.navigation_reference.evidence_scope == "GENERAL_CAR_ROUTING_RULES"`
  - `assert policy.bdtopo_product_reference.publisher == "IGN"`
  - `assert policy.bdtopo_product_reference.title == (<br>        "BD TOPO® Version 3.5 - Descriptif de contenu"<br>    )`
  - `assert policy.bdtopo_product_reference.document_id == "DC_BDTOPO_3-5"`
  - `assert policy.bdtopo_product_reference.revision == "2025-11"`
  - `assert policy.bdtopo_product_reference.evidence_scope == (<br>        "SOURCE_ATTRIBUTE_SEMANTICS"<br>    )`
  - `assert policy.evidence_checked_on == "2026-08-16"`
  - `assert policy.vehicle_scope == "LIGHT_VEHICLE_AND_GENERAL_CAR_NETWORK"`
  - `assert policy.heavy_vehicle_access == "NOT_PROVEN"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `load_ign_road_vehicle_proxy_policy` | `landscout.stages.road_vehicle_proxy_policy.load_ign_road_vehicle_proxy_policy` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_checked_in_policy_loads_with_exact_public_identity_and_reference() -> None:
    policy = load_ign_road_vehicle_proxy_policy()

    assert type(policy) is IgnRoadVehicleProxyPolicy
    assert policy.policy_id == EXPECTED_POLICY_ID
    assert policy.schema_version == 2
    assert policy.scope == EXPECTED_SCOPE
    assert policy.navigation_reference.publisher == "IGN"
    assert policy.navigation_reference.title == "Calcul d’itinéraire"
    assert policy.navigation_reference.revision == "2026-05-27"
    assert policy.navigation_reference.evidence_scope == "GENERAL_CAR_ROUTING_RULES"
    assert policy.bdtopo_product_reference.publisher == "IGN"
    assert policy.bdtopo_product_reference.title == (
        "BD TOPO® Version 3.5 - Descriptif de contenu"
    )
    assert policy.bdtopo_product_reference.document_id == "DC_BDTOPO_3-5"
    assert policy.bdtopo_product_reference.revision == "2025-11"
    assert policy.bdtopo_product_reference.evidence_scope == (
        "SOURCE_ATTRIBUTE_SEMANTICS"
    )
    assert policy.evidence_checked_on == "2026-08-16"
    assert policy.vehicle_scope == "LIGHT_VEHICLE_AND_GENERAL_CAR_NETWORK"
    assert policy.heavy_vehicle_access == "NOT_PROVEN"
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_checked_in_policy_hash_binds_exact_file_bytes`

**Purpose:** Regression invariant: checked in policy hash binds exact file bytes. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_checked_in_policy_hash_binds_exact_file_bytes() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert policy.config_sha256 == sha256(POLICY_PATH.read_bytes()).hexdigest()`
  - `assert len(policy.config_sha256) == 64`
  - `assert policy.config_sha256 == policy.config_sha256.lower()`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `load_ign_road_vehicle_proxy_policy` | `landscout.stages.road_vehicle_proxy_policy.load_ign_road_vehicle_proxy_policy` |
| `sha256(POLICY_PATH.read_bytes()).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |
| `POLICY_PATH.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `policy.config_sha256.lower` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `sha256(POLICY_PATH.read_bytes()).hexdigest`<br>`POLICY_PATH.read_bytes` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `sha256(POLICY_PATH.read_bytes()).hexdigest`<br>`sha256`<br>`policy.config_sha256.lower` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_checked_in_policy_hash_binds_exact_file_bytes() -> None:
    policy = load_ign_road_vehicle_proxy_policy(POLICY_PATH)

    assert policy.config_sha256 == sha256(POLICY_PATH.read_bytes()).hexdigest()
    assert len(policy.config_sha256) == 64
    assert policy.config_sha256 == policy.config_sha256.lower()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_repeat_loading_is_deterministic_and_independent`

**Purpose:** Regression invariant: repeat loading is deterministic and independent. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_repeat_loading_is_deterministic_and_independent() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert first == second`
  - `assert first is not second`
  - `assert first.nature is not second.nature`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `load_ign_road_vehicle_proxy_policy` | `landscout.stages.road_vehicle_proxy_policy.load_ign_road_vehicle_proxy_policy` |

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
def test_repeat_loading_is_deterministic_and_independent() -> None:
    first = load_ign_road_vehicle_proxy_policy()
    second = load_ign_road_vehicle_proxy_policy()

    assert first == second
    assert first is not second
    assert first.nature is not second.nature
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_public_api_exports_only_stable_policy_symbols`

**Purpose:** Regression invariant: public api exports only stable policy symbols. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_public_api_exports_only_stable_policy_symbols() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert set(module.__all__) == expected`
  - `assert expected <= set(stages.__all__)`
  - `assert all(hasattr(stages, name) for name in expected)`
  - `assert not hasattr(stages, "_RoadNatureConfig")`

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
def test_public_api_exports_only_stable_policy_symbols() -> None:
    import landscout.stages.road_vehicle_proxy_policy as module

    expected = {
        "IgnRoadVehicleProxyPolicy",
        "IgnRoadVehicleProxyPolicyError",
        "load_ign_road_vehicle_proxy_policy",
    }
    assert set(module.__all__) == expected
    assert expected <= set(stages.__all__)
    assert all(hasattr(stages, name) for name in expected)
    assert not hasattr(stages, "_RoadNatureConfig")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_invalid_config_structure_is_rejected`

**Purpose:** Regression invariant: invalid config structure is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_invalid_config_structure_is_rejected(
    tmp_path: Path,
    mutation: Any,
    message: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("mutation", "message"),
    [
        (lambda payload: payload.update(unexpected=True), "invalid"),
        (
            lambda payload: payload["references"]["navigation"].update(unexpected=True),
            "invalid",
        ),
        (lambda payload: payload.pop("policy_id"), "invalid"),
        (
            lambda payload: payload["source_values"].pop("nature"),
            "invalid",
        ),
    ],
    ids=["unknown-top", "unknown-nested", "missing-id", "missing-group"],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `mutation` | positional-or-keyword | `Any` | `required` |
| `message` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnRoadVehicleProxyPolicyError, match=message)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_road_vehicle_proxy_policy._payload` |
| `mutation` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_load_payload` | `tests.unit.test_road_vehicle_proxy_policy._load_payload` |
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
def test_invalid_config_structure_is_rejected(
    tmp_path: Path,
    mutation: Any,
    message: str,
) -> None:
    payload = _payload()
    mutation(payload)

    with pytest.raises(IgnRoadVehicleProxyPolicyError, match=message):
        _load_payload(tmp_path, payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unsupported_schema_version_is_rejected`

**Purpose:** Regression invariant: unsupported schema version is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_unsupported_schema_version_is_rejected(tmp_path: Path, version: int) -> None:
```

- Exact decorators: `pytest.mark.parametrize("version", [0, 1, 3, 999])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `version` | positional-or-keyword | `int` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnRoadVehicleProxyPolicyError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_road_vehicle_proxy_policy._payload` |
| `pytest.raises` | `pytest.raises` |
| `_load_payload` | `tests.unit.test_road_vehicle_proxy_policy._load_payload` |
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
| In-memory mutation | `payload["schema_version"] = version` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_unsupported_schema_version_is_rejected(tmp_path: Path, version: int) -> None:
    payload = _payload()
    payload["schema_version"] = version

    with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_wrong_policy_identity_is_rejected`

**Purpose:** Regression invariant: wrong policy identity is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_wrong_policy_identity_is_rejected(
    tmp_path: Path,
    path: tuple[str, ...],
    value: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("path", "value"),
    [
        (("policy_id",), "ign_bdtopo_general_vehicle_proxy_v1"),
        (("scope",), "HEAVY_VEHICLE_POLICY"),
        (("heavy_vehicle_access",), "PROVEN"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `path` | positional-or-keyword | `tuple[str, ...]` | `required` |
| `value` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnRoadVehicleProxyPolicyError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_road_vehicle_proxy_policy._payload` |
| `pytest.raises` | `pytest.raises` |
| `_load_payload` | `tests.unit.test_road_vehicle_proxy_policy._load_payload` |
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
| In-memory mutation | `target[path[-1]] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_wrong_policy_identity_is_rejected(
    tmp_path: Path,
    path: tuple[str, ...],
    value: str,
) -> None:
    payload = _payload()
    target = payload
    for key in path[:-1]:
        target = target[key]
    target[path[-1]] = value

    with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_both_evidence_references_are_required`

**Purpose:** Regression invariant: both evidence references are required. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_both_evidence_references_are_required(tmp_path: Path, reference: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize("reference", ["navigation", "bdtopo_product"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `reference` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnRoadVehicleProxyPolicyError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_road_vehicle_proxy_policy._payload` |
| `payload["references"].pop` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_load_payload` | `tests.unit.test_road_vehicle_proxy_policy._load_payload` |
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
| In-memory mutation | `payload["references"].pop(reference)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_both_evidence_references_are_required(tmp_path: Path, reference: str) -> None:
    payload = _payload()
    payload["references"].pop(reference)

    with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_product_reference_document_id_is_exact`

**Purpose:** Regression invariant: product reference document id is exact. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_product_reference_document_id_is_exact(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnRoadVehicleProxyPolicyError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_road_vehicle_proxy_policy._payload` |
| `pytest.raises` | `pytest.raises` |
| `_load_payload` | `tests.unit.test_road_vehicle_proxy_policy._load_payload` |

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
| In-memory mutation | `payload["references"]["bdtopo_product"]["document_id"] = "OTHER"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_product_reference_document_id_is_exact(tmp_path: Path) -> None:
    payload = _payload()
    payload["references"]["bdtopo_product"]["document_id"] = "OTHER"

    with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unknown_evidence_reference_is_rejected`

**Purpose:** Regression invariant: unknown evidence reference is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_unknown_evidence_reference_is_rejected(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnRoadVehicleProxyPolicyError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_road_vehicle_proxy_policy._payload` |
| `pytest.raises` | `pytest.raises` |
| `_load_payload` | `tests.unit.test_road_vehicle_proxy_policy._load_payload` |

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
| In-memory mutation | `payload["references"]["other"] = payload["references"]["navigation"]` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_unknown_evidence_reference_is_rejected(tmp_path: Path) -> None:
    payload = _payload()
    payload["references"]["other"] = payload["references"]["navigation"]

    with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_asset_state_groups_cover_exact_v2_domain`

**Purpose:** Regression invariant: asset state groups cover exact v2 domain. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_asset_state_groups_cover_exact_v2_domain() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert policy.asset_state.in_service == frozenset({"En service"})`
  - `assert policy.asset_state.project_geometry_not_significant == frozenset(<br>        {"En projet"}<br>    )`
  - `assert policy.asset_state.under_construction == frozenset({"En construction"})`
  - `assert set().union(*groups) == {"En service", "En projet", "En construction"}`
  - `assert all(<br>        sum(value in group for group in groups) == 1 for value in set().union(*groups)<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `load_ign_road_vehicle_proxy_policy` | `landscout.stages.road_vehicle_proxy_policy.load_ign_road_vehicle_proxy_policy` |
| `frozenset` | `unresolved local/third-party receiver; no ownership inferred` |
| `set().union` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `all` | `unresolved local/third-party receiver; no ownership inferred` |
| `sum` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_asset_state_groups_cover_exact_v2_domain() -> None:
    policy = load_ign_road_vehicle_proxy_policy()
    groups = (
        policy.asset_state.in_service,
        policy.asset_state.project_geometry_not_significant,
        policy.asset_state.under_construction,
    )

    assert policy.asset_state.in_service == frozenset({"En service"})
    assert policy.asset_state.project_geometry_not_significant == frozenset(
        {"En projet"}
    )
    assert policy.asset_state.under_construction == frozenset({"En construction"})
    assert set().union(*groups) == {"En service", "En projet", "En construction"}
    assert all(
        sum(value in group for group in groups) == 1 for value in set().union(*groups)
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_asset_state_group_overlap_is_rejected`

**Purpose:** Regression invariant: asset state group overlap is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_asset_state_group_overlap_is_rejected(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnRoadVehicleProxyPolicyError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_road_vehicle_proxy_policy._payload` |
| `pytest.raises` | `pytest.raises` |
| `_load_payload` | `tests.unit.test_road_vehicle_proxy_policy._load_payload` |

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
| In-memory mutation | `payload["source_values"]["asset_state"]["under_construction"] = ["En projet"]` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_asset_state_group_overlap_is_rejected(tmp_path: Path) -> None:
    payload = _payload()
    payload["source_values"]["asset_state"]["under_construction"] = ["En projet"]

    with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_missing_known_asset_state_is_rejected`

**Purpose:** Regression invariant: missing known asset state is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_missing_known_asset_state_is_rejected(
    tmp_path: Path, group: str, value: str
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("group", "value"),
    [
        ("in_service", "En service"),
        ("project_geometry_not_significant", "En projet"),
        ("under_construction", "En construction"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `group` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnRoadVehicleProxyPolicyError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_road_vehicle_proxy_policy._payload` |
| `payload["source_values"]["asset_state"][group].remove` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_load_payload` | `tests.unit.test_road_vehicle_proxy_policy._load_payload` |
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
| In-memory mutation | `payload["source_values"]["asset_state"][group].remove(value)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_missing_known_asset_state_is_rejected(
    tmp_path: Path, group: str, value: str
) -> None:
    payload = _payload()
    payload["source_values"]["asset_state"][group].remove(value)

    with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unknown_additional_asset_state_is_rejected`

**Purpose:** Regression invariant: unknown additional asset state is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_unknown_additional_asset_state_is_rejected(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnRoadVehicleProxyPolicyError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_road_vehicle_proxy_policy._payload` |
| `payload["source_values"]["asset_state"]["in_service"].append` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_load_payload` | `tests.unit.test_road_vehicle_proxy_policy._load_payload` |

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
| In-memory mutation | `payload["source_values"]["asset_state"]["in_service"].append("Unknown")` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_unknown_additional_asset_state_is_rejected(tmp_path: Path) -> None:
    payload = _payload()
    payload["source_values"]["asset_state"]["in_service"].append("Unknown")

    with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_semantic_values_must_be_exact_non_empty_strings`

**Purpose:** Regression invariant: semantic values must be exact non empty strings. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_semantic_values_must_be_exact_non_empty_strings(
    tmp_path: Path, value: str
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("value", ["", " Libre", "Libre "])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `value` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnRoadVehicleProxyPolicyError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_road_vehicle_proxy_policy._payload` |
| `pytest.raises` | `pytest.raises` |
| `_load_payload` | `tests.unit.test_road_vehicle_proxy_policy._load_payload` |
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
| In-memory mutation | `payload["source_values"]["light_vehicle_access"]["open"] = [value]` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_semantic_values_must_be_exact_non_empty_strings(
    tmp_path: Path, value: str
) -> None:
    payload = _payload()
    payload["source_values"]["light_vehicle_access"]["open"] = [value]

    with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_duplicate_semantic_value_is_rejected`

**Purpose:** Regression invariant: duplicate semantic value is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_duplicate_semantic_value_is_rejected(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnRoadVehicleProxyPolicyError, match="invalid")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_road_vehicle_proxy_policy._payload` |
| `pytest.raises` | `pytest.raises` |
| `_load_payload` | `tests.unit.test_road_vehicle_proxy_policy._load_payload` |

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
| In-memory mutation | `payload["source_values"]["light_vehicle_access"]["open"] = [<br>        "Libre",<br>        "Libre",<br>    ]` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_duplicate_semantic_value_is_rejected(tmp_path: Path) -> None:
    payload = _payload()
    payload["source_values"]["light_vehicle_access"]["open"] = [
        "Libre",
        "Libre",
    ]

    with pytest.raises(IgnRoadVehicleProxyPolicyError, match="invalid"):
        _load_payload(tmp_path, payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_semantic_groups_must_be_pairwise_disjoint`

**Purpose:** Regression invariant: semantic groups must be pairwise disjoint. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_semantic_groups_must_be_pairwise_disjoint(
    tmp_path: Path,
    group: str,
    source_group: str,
    target_group: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("group", "source_group", "target_group"),
    [
        ("light_vehicle_access", "open", "toll"),
        ("nature", "general_motor_road", "limited_motor_proxy"),
        ("nature", "limited_motor_proxy", "non_general_vehicle"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `group` | positional-or-keyword | `str` | `required` |
| `source_group` | positional-or-keyword | `str` | `required` |
| `target_group` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnRoadVehicleProxyPolicyError, match="invalid")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_road_vehicle_proxy_policy._payload` |
| `payload["source_values"][group][target_group].append` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_load_payload` | `tests.unit.test_road_vehicle_proxy_policy._load_payload` |
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
| In-memory mutation | `payload["source_values"][group][target_group].append(value)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_semantic_groups_must_be_pairwise_disjoint(
    tmp_path: Path,
    group: str,
    source_group: str,
    target_group: str,
) -> None:
    payload = _payload()
    value = payload["source_values"][group][source_group][0]
    payload["source_values"][group][target_group].append(value)

    with pytest.raises(IgnRoadVehicleProxyPolicyError, match="invalid"):
        _load_payload(tmp_path, payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_duplicate_known_restriction_is_rejected`

**Purpose:** Regression invariant: duplicate known restriction is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_duplicate_known_restriction_is_rejected(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnRoadVehicleProxyPolicyError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_road_vehicle_proxy_policy._payload` |
| `restrictions.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_load_payload` | `tests.unit.test_road_vehicle_proxy_policy._load_payload` |

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
| In-memory mutation | `restrictions.append(restrictions[0])` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_duplicate_known_restriction_is_rejected(tmp_path: Path) -> None:
    payload = _payload()
    restrictions = payload["source_values"]["known_restriction_review"]
    restrictions.append(restrictions[0])

    with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_invalid_width_threshold_is_rejected`

**Purpose:** Regression invariant: invalid width threshold is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_invalid_width_threshold_is_rejected(tmp_path: Path, value: object) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "value",
    [-1.0, 0.0, float("nan"), float("inf"), float("-inf"), "2.9", True],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnRoadVehicleProxyPolicyError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_road_vehicle_proxy_policy._payload` |
| `pytest.raises` | `pytest.raises` |
| `_load_payload` | `tests.unit.test_road_vehicle_proxy_policy._load_payload` |
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
| In-memory mutation | `payload["source_values"]["width_below_m"] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_invalid_width_threshold_is_rejected(tmp_path: Path, value: object) -> None:
    payload = _payload()
    payload["source_values"]["width_below_m"] = value

    with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_exact_width_threshold_is_accepted`

**Purpose:** Regression invariant: exact width threshold is accepted. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_exact_width_threshold_is_accepted(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert _load_payload(tmp_path, payload).width_below_m == 2.9`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_road_vehicle_proxy_policy._payload` |
| `_load_payload` | `tests.unit.test_road_vehicle_proxy_policy._load_payload` |

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
| In-memory mutation | `payload["source_values"]["width_below_m"] = 2.9` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_exact_width_threshold_is_accepted(tmp_path: Path) -> None:
    payload = _payload()
    payload["source_values"]["width_below_m"] = 2.9

    assert _load_payload(tmp_path, payload).width_below_m == 2.9
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_importance_domains_must_be_exact`

**Purpose:** Regression invariant: importance domains must be exact. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_importance_domains_must_be_exact(
    tmp_path: Path, group: str, mutation: str
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("group", "mutation"),
    [
        ("known", "remove-1"),
        ("known", "remove-5"),
        ("known", "add-7"),
        ("limited", "numeric-6"),
        ("limited", "limited-5"),
        ("limited", "empty"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `group` | positional-or-keyword | `str` | `required` |
| `mutation` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnRoadVehicleProxyPolicyError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_road_vehicle_proxy_policy._payload` |
| `importance[group].remove` | `unresolved local/third-party receiver; no ownership inferred` |
| `importance[group].append` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_load_payload` | `tests.unit.test_road_vehicle_proxy_policy._load_payload` |
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
| In-memory mutation | `importance[group].remove("1")`<br>`importance[group].remove("5")`<br>`importance[group].append("7")`<br>`importance[group] = [6]`<br>`importance[group] = ["5"]`<br>`importance[group] = []` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_importance_domains_must_be_exact(
    tmp_path: Path, group: str, mutation: str
) -> None:
    payload = _payload()
    importance = payload["source_values"]["importance"]
    if mutation == "remove-1":
        importance[group].remove("1")
    elif mutation == "remove-5":
        importance[group].remove("5")
    elif mutation == "add-7":
        importance[group].append("7")
    elif mutation == "numeric-6":
        importance[group] = [6]
    elif mutation == "limited-5":
        importance[group] = ["5"]
    else:
        importance[group] = []

    with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_importance_domains_expose_known_without_positive_classification`

**Purpose:** Regression invariant: importance domains expose known without positive classification. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_importance_domains_expose_known_without_positive_classification() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert policy.importance.known == frozenset({"1", "2", "3", "4", "5", "6"})`
  - `assert policy.importance.limited == frozenset({"6"})`
  - `assert policy.importance.limited <= policy.importance.known`
  - `assert "7" not in policy.importance.known`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `load_ign_road_vehicle_proxy_policy` | `landscout.stages.road_vehicle_proxy_policy.load_ign_road_vehicle_proxy_policy` |
| `frozenset` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_importance_domains_expose_known_without_positive_classification() -> None:
    policy = load_ign_road_vehicle_proxy_policy()

    assert policy.importance.known == frozenset({"1", "2", "3", "4", "5", "6"})
    assert policy.importance.limited == frozenset({"6"})
    assert policy.importance.limited <= policy.importance.known
    assert "7" not in policy.importance.known
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_decision_precedence_must_be_exact`

**Purpose:** Regression invariant: decision precedence must be exact. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_decision_precedence_must_be_exact(tmp_path: Path, mutation: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize("mutation", ["missing", "duplicate", "unknown", "reorder"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `mutation` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnRoadVehicleProxyPolicyError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_road_vehicle_proxy_policy._payload` |
| `precedence.pop` | `unresolved local/third-party receiver; no ownership inferred` |
| `precedence.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_load_payload` | `tests.unit.test_road_vehicle_proxy_policy._load_payload` |
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
| In-memory mutation | `precedence.pop()`<br>`precedence[-1] = precedence[0]`<br>`precedence.append("INVENTED_RULE")` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_decision_precedence_must_be_exact(tmp_path: Path, mutation: str) -> None:
    payload = _payload()
    precedence = payload["decision_precedence"]
    if mutation == "missing":
        precedence.pop()
    elif mutation == "duplicate":
        precedence[-1] = precedence[0]
    elif mutation == "unknown":
        precedence.append("INVENTED_RULE")
    else:
        precedence[0], precedence[1] = precedence[1], precedence[0]

    with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_decision_precedence_and_rule_outcomes_are_approved`

**Purpose:** Regression invariant: decision precedence and rule outcomes are approved. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_decision_precedence_and_rule_outcomes_are_approved() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert policy.decision_precedence == EXPECTED_PRECEDENCE`
  - `assert policy.decision_outcomes.fictitious_geometry == "NOT_DISTANCE_PROXY"`
  - `assert policy.decision_outcomes.project_geometry_not_significant == (<br>        "NOT_DISTANCE_PROXY"<br>    )`
  - `assert policy.decision_outcomes.not_in_service == ("NOT_GENERAL_VEHICLE_PROXY")`
  - `assert policy.decision_outcomes.private_road == "RESTRICTED_REVIEW"`
  - `assert policy.decision_outcomes.rights_restricted == "RESTRICTED_REVIEW"`
  - `assert policy.decision_outcomes.temporal_closure == "RESTRICTED_REVIEW"`
  - `assert policy.decision_outcomes.physically_impossible == (<br>        "NOT_GENERAL_VEHICLE_PROXY"<br>    )`
  - `assert policy.decision_outcomes.limited_nature == "LIMITED_VEHICLE_PROXY"`
  - `assert policy.decision_outcomes.open_or_toll == "GENERAL_VEHICLE_PROXY"`
  - `assert policy.decision_outcomes.unknown == "UNKNOWN_REVIEW"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `load_ign_road_vehicle_proxy_policy` | `landscout.stages.road_vehicle_proxy_policy.load_ign_road_vehicle_proxy_policy` |

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
def test_decision_precedence_and_rule_outcomes_are_approved() -> None:
    policy = load_ign_road_vehicle_proxy_policy()

    assert policy.decision_precedence == EXPECTED_PRECEDENCE
    assert policy.decision_outcomes.fictitious_geometry == "NOT_DISTANCE_PROXY"
    assert policy.decision_outcomes.project_geometry_not_significant == (
        "NOT_DISTANCE_PROXY"
    )
    assert policy.decision_outcomes.not_in_service == ("NOT_GENERAL_VEHICLE_PROXY")
    assert policy.decision_outcomes.private_road == "RESTRICTED_REVIEW"
    assert policy.decision_outcomes.rights_restricted == "RESTRICTED_REVIEW"
    assert policy.decision_outcomes.temporal_closure == "RESTRICTED_REVIEW"
    assert policy.decision_outcomes.physically_impossible == (
        "NOT_GENERAL_VEHICLE_PROXY"
    )
    assert policy.decision_outcomes.limited_nature == "LIMITED_VEHICLE_PROXY"
    assert policy.decision_outcomes.open_or_toll == "GENERAL_VEHICLE_PROXY"
    assert policy.decision_outcomes.unknown == "UNKNOWN_REVIEW"
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_project_geometry_rule_has_exact_precedence_position`

**Purpose:** Regression invariant: project geometry rule has exact precedence position. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_project_geometry_rule_has_exact_precedence_position() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert fictitious < project < not_in_service`
  - `assert len(policy.decision_precedence) == 16`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `load_ign_road_vehicle_proxy_policy` | `landscout.stages.road_vehicle_proxy_policy.load_ign_road_vehicle_proxy_policy` |
| `policy.decision_precedence.index` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_project_geometry_rule_has_exact_precedence_position() -> None:
    policy = load_ign_road_vehicle_proxy_policy()

    fictitious = policy.decision_precedence.index("FICTITIOUS_GEOMETRY")
    project = policy.decision_precedence.index("PROJECT_GEOMETRY_NOT_SIGNIFICANT")
    not_in_service = policy.decision_precedence.index("NOT_IN_SERVICE")
    assert fictitious < project < not_in_service
    assert len(policy.decision_precedence) == 16
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_output_class_vocabulary_must_be_exact`

**Purpose:** Regression invariant: output class vocabulary must be exact. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_output_class_vocabulary_must_be_exact(tmp_path: Path, mutation: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize("mutation", ["missing", "extra", "wrong"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `mutation` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnRoadVehicleProxyPolicyError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_payload` | `tests.unit.test_road_vehicle_proxy_policy._payload` |
| `classes.pop` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_load_payload` | `tests.unit.test_road_vehicle_proxy_policy._load_payload` |
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
| In-memory mutation | `classes.pop("unknown_review")`<br>`classes["authorized"] = "AUTHORIZED"`<br>`classes["general_vehicle_proxy"] = "ROAD_APPROVED"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_output_class_vocabulary_must_be_exact(tmp_path: Path, mutation: str) -> None:
    payload = _payload()
    classes = payload["classes"]
    if mutation == "missing":
        classes.pop("unknown_review")
    elif mutation == "extra":
        classes["authorized"] = "AUTHORIZED"
    else:
        classes["general_vehicle_proxy"] = "ROAD_APPROVED"

    with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_approved_class_vocabulary_has_no_heavy_or_legal_claim`

**Purpose:** Regression invariant: approved class vocabulary has no heavy or legal claim. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_approved_class_vocabulary_has_no_heavy_or_legal_claim() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert policy.classes.values == EXPECTED_CLASSES`
  - `assert policy.heavy_vehicle_access == "NOT_PROVEN"`
  - `assert all(<br>        token not in value for value in policy.classes.values for token in forbidden<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `load_ign_road_vehicle_proxy_policy` | `landscout.stages.road_vehicle_proxy_policy.load_ign_road_vehicle_proxy_policy` |
| `all` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_approved_class_vocabulary_has_no_heavy_or_legal_claim() -> None:
    policy = load_ign_road_vehicle_proxy_policy()
    forbidden = ("TRUCK", "HEAVY", "LEGAL", "APPROVED", "BESS_ACCESSIBLE", "AUTHORIZED")

    assert policy.classes.values == EXPECTED_CLASSES
    assert policy.heavy_vehicle_access == "NOT_PROVEN"
    assert all(
        token not in value for value in policy.classes.values for token in forbidden
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_observed_d031_natures_are_covered_exactly_once`

**Purpose:** Regression invariant: observed d031 natures are covered exactly once. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_observed_d031_natures_are_covered_exactly_once() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert set().union(*groups) >= OBSERVED_NATURES`
  - `assert all(<br>        sum(value in group for group in groups) == 1 for value in OBSERVED_NATURES<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `load_ign_road_vehicle_proxy_policy` | `landscout.stages.road_vehicle_proxy_policy.load_ign_road_vehicle_proxy_policy` |
| `set().union` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `all` | `unresolved local/third-party receiver; no ownership inferred` |
| `sum` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_observed_d031_natures_are_covered_exactly_once() -> None:
    policy = load_ign_road_vehicle_proxy_policy()
    groups = (
        policy.nature.general_motor_road,
        policy.nature.limited_motor_proxy,
        policy.nature.non_general_vehicle,
        policy.nature.special_review,
    )

    assert set().union(*groups) >= OBSERVED_NATURES
    assert all(
        sum(value in group for group in groups) == 1 for value in OBSERVED_NATURES
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_observed_d031_access_and_importance_vocabularies_are_compatible`

**Purpose:** Regression invariant: observed d031 access and importance vocabularies are compatible. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_observed_d031_access_and_importance_vocabularies_are_compatible() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert set().union(*access_groups) == OBSERVED_LIGHT_VEHICLE_ACCESS`
  - `assert policy.importance.known == frozenset({"1", "2", "3", "4", "5", "6"})`
  - `assert policy.importance.limited == frozenset({"6"})`
  - `assert policy.decision_outcomes.unknown == "UNKNOWN_REVIEW"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `load_ign_road_vehicle_proxy_policy` | `landscout.stages.road_vehicle_proxy_policy.load_ign_road_vehicle_proxy_policy` |
| `set().union` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `frozenset` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_observed_d031_access_and_importance_vocabularies_are_compatible() -> None:
    policy = load_ign_road_vehicle_proxy_policy()
    access_groups = (
        policy.light_vehicle_access.open,
        policy.light_vehicle_access.toll,
        policy.light_vehicle_access.rights_restricted,
        policy.light_vehicle_access.physically_impossible,
    )

    assert set().union(*access_groups) == OBSERVED_LIGHT_VEHICLE_ACCESS
    assert policy.importance.known == frozenset({"1", "2", "3", "4", "5", "6"})
    assert policy.importance.limited == frozenset({"6"})
    assert policy.decision_outcomes.unknown == "UNKNOWN_REVIEW"
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_compiled_policy_structures_are_immutable`

**Purpose:** Regression invariant: compiled policy structures are immutable. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_compiled_policy_structures_are_immutable() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(FrozenInstanceError)`
  - `pytest.raises(AttributeError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `load_ign_road_vehicle_proxy_policy` | `landscout.stages.road_vehicle_proxy_policy.load_ign_road_vehicle_proxy_policy` |
| `pytest.raises` | `pytest.raises` |
| `policy.nature.general_motor_road.add` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `policy.scope = "changed"`<br>`policy.nature.general_motor_road.add("Invented")` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_compiled_policy_structures_are_immutable() -> None:
    policy = load_ign_road_vehicle_proxy_policy()

    with pytest.raises(FrozenInstanceError):
        policy.scope = "changed"  # type: ignore[misc]
    with pytest.raises(AttributeError):
        policy.nature.general_motor_road.add("Invented")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_mutating_source_payload_cannot_affect_another_load`

**Purpose:** Regression invariant: mutating source payload cannot affect another load. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_mutating_source_payload_cannot_affect_another_load() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert first == second`
  - `assert "Invented" not in second.nature.general_motor_road`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `load_ign_road_vehicle_proxy_policy` | `landscout.stages.road_vehicle_proxy_policy.load_ign_road_vehicle_proxy_policy` |
| `_payload` | `tests.unit.test_road_vehicle_proxy_policy._payload` |
| `mutable["source_values"]["nature"]["general_motor_road"].append` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `mutable["source_values"]["nature"]["general_motor_road"].append("Invented")` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_mutating_source_payload_cannot_affect_another_load() -> None:
    first = load_ign_road_vehicle_proxy_policy()
    mutable = _payload()
    mutable["source_values"]["nature"]["general_motor_road"].append("Invented")
    second = load_ign_road_vehicle_proxy_policy()

    assert first == second
    assert "Invented" not in second.nature.general_motor_road
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_malformed_yaml_has_controlled_error`

**Purpose:** Regression invariant: malformed yaml has controlled error. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_malformed_yaml_has_controlled_error(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnRoadVehicleProxyPolicyError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `load_ign_road_vehicle_proxy_policy` | `landscout.stages.road_vehicle_proxy_policy.load_ign_road_vehicle_proxy_policy` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `path.write_text` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_malformed_yaml_has_controlled_error(tmp_path: Path) -> None:
    path = tmp_path / "malformed.yaml"
    path.write_text("policy_id: [", encoding="utf-8")

    with pytest.raises(IgnRoadVehicleProxyPolicyError):
        load_ign_road_vehicle_proxy_policy(path)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_non_mapping_yaml_has_controlled_error`

**Purpose:** Regression invariant: non mapping yaml has controlled error. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_non_mapping_yaml_has_controlled_error(tmp_path: Path, payload: object) -> None:
```

- Exact decorators: `pytest.mark.parametrize("payload", [None, [], "policy"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `payload` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnRoadVehicleProxyPolicyError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `_load_payload` | `tests.unit.test_road_vehicle_proxy_policy._load_payload` |
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
def test_non_mapping_yaml_has_controlled_error(tmp_path: Path, payload: object) -> None:
    with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_missing_file_has_controlled_error`

**Purpose:** Regression invariant: missing file has controlled error. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_missing_file_has_controlled_error(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnRoadVehicleProxyPolicyError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `load_ign_road_vehicle_proxy_policy` | `landscout.stages.road_vehicle_proxy_policy.load_ign_road_vehicle_proxy_policy` |

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
def test_missing_file_has_controlled_error(tmp_path: Path) -> None:
    with pytest.raises(IgnRoadVehicleProxyPolicyError):
        load_ign_road_vehicle_proxy_policy(tmp_path / "missing.yaml")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.


## 7. Test-specific regression contract

- Test functions: **35**.
- Pytest fixtures (decorator-proven): **0**.

### Per-test regression index

| Test | Parametrization | Expected exception contexts | Assertion count | Exact regression purpose |
|---|---|---|---:|---|
| `test_duplicate_yaml_policy_key_is_rejected` | none | pytest.raises(IgnRoadVehicleProxyPolicyError, match="Duplicate YAML.*key") | 0 | Proves duplicate yaml policy key is rejected using the exact source reproduced in section 7. |
| `test_checked_in_policy_loads_with_exact_public_identity_and_reference` | none | none | 16 | Proves checked in policy loads with exact public identity and reference using the exact source reproduced in section 7. |
| `test_checked_in_policy_hash_binds_exact_file_bytes` | none | none | 3 | Proves checked in policy hash binds exact file bytes using the exact source reproduced in section 7. |
| `test_repeat_loading_is_deterministic_and_independent` | none | none | 3 | Proves repeat loading is deterministic and independent using the exact source reproduced in section 7. |
| `test_public_api_exports_only_stable_policy_symbols` | none | none | 4 | Proves public api exports only stable policy symbols using the exact source reproduced in section 7. |
| `test_invalid_config_structure_is_rejected` | pytest.mark.parametrize(<br>    ("mutation", "message"),<br>    [<br>        (lambda payload: payload.update(unexpected=True), "invalid"),<br>        (<br>            lambda payload: payload["references"]["navigation"].update(unexpected=True),<br>            "invalid",<br>        ),<br>        (lambda payload: payload.pop("policy_id"), "invalid"),<br>        (<br>            lambda payload: payload["source_values"].pop("nature"),<br>            "invalid",<br>        ),<br>    ],<br>    ids=["unknown-top", "unknown-nested", "missing-id", "missing-group"],<br>) | pytest.raises(IgnRoadVehicleProxyPolicyError, match=message) | 0 | Proves invalid config structure is rejected using the exact source reproduced in section 7. |
| `test_unsupported_schema_version_is_rejected` | pytest.mark.parametrize("version", [0, 1, 3, 999]) | pytest.raises(IgnRoadVehicleProxyPolicyError) | 0 | Proves unsupported schema version is rejected using the exact source reproduced in section 7. |
| `test_wrong_policy_identity_is_rejected` | pytest.mark.parametrize(<br>    ("path", "value"),<br>    [<br>        (("policy_id",), "ign_bdtopo_general_vehicle_proxy_v1"),<br>        (("scope",), "HEAVY_VEHICLE_POLICY"),<br>        (("heavy_vehicle_access",), "PROVEN"),<br>    ],<br>) | pytest.raises(IgnRoadVehicleProxyPolicyError) | 0 | Proves wrong policy identity is rejected using the exact source reproduced in section 7. |
| `test_both_evidence_references_are_required` | pytest.mark.parametrize("reference", ["navigation", "bdtopo_product"]) | pytest.raises(IgnRoadVehicleProxyPolicyError) | 0 | Proves both evidence references are required using the exact source reproduced in section 7. |
| `test_product_reference_document_id_is_exact` | none | pytest.raises(IgnRoadVehicleProxyPolicyError) | 0 | Proves product reference document id is exact using the exact source reproduced in section 7. |
| `test_unknown_evidence_reference_is_rejected` | none | pytest.raises(IgnRoadVehicleProxyPolicyError) | 0 | Proves unknown evidence reference is rejected using the exact source reproduced in section 7. |
| `test_asset_state_groups_cover_exact_v2_domain` | none | none | 5 | Proves asset state groups cover exact v2 domain using the exact source reproduced in section 7. |
| `test_asset_state_group_overlap_is_rejected` | none | pytest.raises(IgnRoadVehicleProxyPolicyError) | 0 | Proves asset state group overlap is rejected using the exact source reproduced in section 7. |
| `test_missing_known_asset_state_is_rejected` | pytest.mark.parametrize(<br>    ("group", "value"),<br>    [<br>        ("in_service", "En service"),<br>        ("project_geometry_not_significant", "En projet"),<br>        ("under_construction", "En construction"),<br>    ],<br>) | pytest.raises(IgnRoadVehicleProxyPolicyError) | 0 | Proves missing known asset state is rejected using the exact source reproduced in section 7. |
| `test_unknown_additional_asset_state_is_rejected` | none | pytest.raises(IgnRoadVehicleProxyPolicyError) | 0 | Proves unknown additional asset state is rejected using the exact source reproduced in section 7. |
| `test_semantic_values_must_be_exact_non_empty_strings` | pytest.mark.parametrize("value", ["", " Libre", "Libre "]) | pytest.raises(IgnRoadVehicleProxyPolicyError) | 0 | Proves semantic values must be exact non empty strings using the exact source reproduced in section 7. |
| `test_duplicate_semantic_value_is_rejected` | none | pytest.raises(IgnRoadVehicleProxyPolicyError, match="invalid") | 0 | Proves duplicate semantic value is rejected using the exact source reproduced in section 7. |
| `test_semantic_groups_must_be_pairwise_disjoint` | pytest.mark.parametrize(<br>    ("group", "source_group", "target_group"),<br>    [<br>        ("light_vehicle_access", "open", "toll"),<br>        ("nature", "general_motor_road", "limited_motor_proxy"),<br>        ("nature", "limited_motor_proxy", "non_general_vehicle"),<br>    ],<br>) | pytest.raises(IgnRoadVehicleProxyPolicyError, match="invalid") | 0 | Proves semantic groups must be pairwise disjoint using the exact source reproduced in section 7. |
| `test_duplicate_known_restriction_is_rejected` | none | pytest.raises(IgnRoadVehicleProxyPolicyError) | 0 | Proves duplicate known restriction is rejected using the exact source reproduced in section 7. |
| `test_invalid_width_threshold_is_rejected` | pytest.mark.parametrize(<br>    "value",<br>    [-1.0, 0.0, float("nan"), float("inf"), float("-inf"), "2.9", True],<br>) | pytest.raises(IgnRoadVehicleProxyPolicyError) | 0 | Proves invalid width threshold is rejected using the exact source reproduced in section 7. |
| `test_exact_width_threshold_is_accepted` | none | none | 1 | Proves exact width threshold is accepted using the exact source reproduced in section 7. |
| `test_importance_domains_must_be_exact` | pytest.mark.parametrize(<br>    ("group", "mutation"),<br>    [<br>        ("known", "remove-1"),<br>        ("known", "remove-5"),<br>        ("known", "add-7"),<br>        ("limited", "numeric-6"),<br>        ("limited", "limited-5"),<br>        ("limited", "empty"),<br>    ],<br>) | pytest.raises(IgnRoadVehicleProxyPolicyError) | 0 | Proves importance domains must be exact using the exact source reproduced in section 7. |
| `test_importance_domains_expose_known_without_positive_classification` | none | none | 4 | Proves importance domains expose known without positive classification using the exact source reproduced in section 7. |
| `test_decision_precedence_must_be_exact` | pytest.mark.parametrize("mutation", ["missing", "duplicate", "unknown", "reorder"]) | pytest.raises(IgnRoadVehicleProxyPolicyError) | 0 | Proves decision precedence must be exact using the exact source reproduced in section 7. |
| `test_decision_precedence_and_rule_outcomes_are_approved` | none | none | 11 | Proves decision precedence and rule outcomes are approved using the exact source reproduced in section 7. |
| `test_project_geometry_rule_has_exact_precedence_position` | none | none | 2 | Proves project geometry rule has exact precedence position using the exact source reproduced in section 7. |
| `test_output_class_vocabulary_must_be_exact` | pytest.mark.parametrize("mutation", ["missing", "extra", "wrong"]) | pytest.raises(IgnRoadVehicleProxyPolicyError) | 0 | Proves output class vocabulary must be exact using the exact source reproduced in section 7. |
| `test_approved_class_vocabulary_has_no_heavy_or_legal_claim` | none | none | 3 | Proves approved class vocabulary has no heavy or legal claim using the exact source reproduced in section 7. |
| `test_observed_d031_natures_are_covered_exactly_once` | none | none | 2 | Proves observed d031 natures are covered exactly once using the exact source reproduced in section 7. |
| `test_observed_d031_access_and_importance_vocabularies_are_compatible` | none | none | 4 | Proves observed d031 access and importance vocabularies are compatible using the exact source reproduced in section 7. |
| `test_compiled_policy_structures_are_immutable` | none | pytest.raises(FrozenInstanceError); pytest.raises(AttributeError) | 0 | Proves compiled policy structures are immutable using the exact source reproduced in section 7. |
| `test_mutating_source_payload_cannot_affect_another_load` | none | none | 2 | Proves mutating source payload cannot affect another load using the exact source reproduced in section 7. |
| `test_malformed_yaml_has_controlled_error` | none | pytest.raises(IgnRoadVehicleProxyPolicyError) | 0 | Proves malformed yaml has controlled error using the exact source reproduced in section 7. |
| `test_non_mapping_yaml_has_controlled_error` | pytest.mark.parametrize("payload", [None, [], "policy"]) | pytest.raises(IgnRoadVehicleProxyPolicyError) | 0 | Proves non mapping yaml has controlled error using the exact source reproduced in section 7. |
| `test_missing_file_has_controlled_error` | none | pytest.raises(IgnRoadVehicleProxyPolicyError) | 0 | Proves missing file has controlled error using the exact source reproduced in section 7. |

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

from dataclasses import FrozenInstanceError
from hashlib import sha256
from pathlib import Path
from typing import Any

import pytest
import yaml

from landscout import stages
from landscout.stages.road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyPolicy,
    IgnRoadVehicleProxyPolicyError,
    load_ign_road_vehicle_proxy_policy,
)

POLICY_PATH = Path("configs/access/ign_bdtopo_vehicle_proxy_policy.yaml")
EXPECTED_POLICY_ID = "ign_bdtopo_general_vehicle_proxy_v2"
EXPECTED_SCOPE = "OFFICIAL_IGN_CAR_ROUTING_EVIDENCE_ONLY"
EXPECTED_CLASSES = (
    "GENERAL_VEHICLE_PROXY",
    "LIMITED_VEHICLE_PROXY",
    "RESTRICTED_REVIEW",
    "NOT_GENERAL_VEHICLE_PROXY",
    "NOT_DISTANCE_PROXY",
    "UNKNOWN_REVIEW",
)
EXPECTED_PRECEDENCE = (
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
OBSERVED_NATURES = {
    "Route à 1 chaussée",
    "Chemin",
    "Route empierrée",
    "Sentier",
    "Rond-point",
    "Route à 2 chaussées",
    "Type autoroutier",
    "Bretelle",
    "Escalier",
    "Bac ou liaison maritime",
}
OBSERVED_LIGHT_VEHICLE_ACCESS = {
    "Libre",
    "Physiquement impossible",
    "Restreint aux ayants droit",
    "A péage",
}


def _payload() -> dict[str, Any]:
    payload = yaml.safe_load(POLICY_PATH.read_text(encoding="utf-8"))
    assert isinstance(payload, dict)
    return payload


def _write_policy(tmp_path: Path, payload: object) -> Path:
    path = tmp_path / "policy.yaml"
    path.write_text(
        yaml.safe_dump(payload, allow_unicode=True, sort_keys=False),
        encoding="utf-8",
    )
    return path


def test_duplicate_yaml_policy_key_is_rejected(tmp_path: Path) -> None:
    path = tmp_path / "duplicate.yaml"
    path.write_text("schema_version: 2\nschema_version: 2\n", encoding="utf-8")

    with pytest.raises(IgnRoadVehicleProxyPolicyError, match="Duplicate YAML.*key"):
        load_ign_road_vehicle_proxy_policy(path)


def _load_payload(tmp_path: Path, payload: object) -> IgnRoadVehicleProxyPolicy:
    return load_ign_road_vehicle_proxy_policy(_write_policy(tmp_path, payload))


def test_checked_in_policy_loads_with_exact_public_identity_and_reference() -> None:
    policy = load_ign_road_vehicle_proxy_policy()

    assert type(policy) is IgnRoadVehicleProxyPolicy
    assert policy.policy_id == EXPECTED_POLICY_ID
    assert policy.schema_version == 2
    assert policy.scope == EXPECTED_SCOPE
    assert policy.navigation_reference.publisher == "IGN"
    assert policy.navigation_reference.title == "Calcul d’itinéraire"
    assert policy.navigation_reference.revision == "2026-05-27"
    assert policy.navigation_reference.evidence_scope == "GENERAL_CAR_ROUTING_RULES"
    assert policy.bdtopo_product_reference.publisher == "IGN"
    assert policy.bdtopo_product_reference.title == (
        "BD TOPO® Version 3.5 - Descriptif de contenu"
    )
    assert policy.bdtopo_product_reference.document_id == "DC_BDTOPO_3-5"
    assert policy.bdtopo_product_reference.revision == "2025-11"
    assert policy.bdtopo_product_reference.evidence_scope == (
        "SOURCE_ATTRIBUTE_SEMANTICS"
    )
    assert policy.evidence_checked_on == "2026-08-16"
    assert policy.vehicle_scope == "LIGHT_VEHICLE_AND_GENERAL_CAR_NETWORK"
    assert policy.heavy_vehicle_access == "NOT_PROVEN"


def test_checked_in_policy_hash_binds_exact_file_bytes() -> None:
    policy = load_ign_road_vehicle_proxy_policy(POLICY_PATH)

    assert policy.config_sha256 == sha256(POLICY_PATH.read_bytes()).hexdigest()
    assert len(policy.config_sha256) == 64
    assert policy.config_sha256 == policy.config_sha256.lower()


def test_repeat_loading_is_deterministic_and_independent() -> None:
    first = load_ign_road_vehicle_proxy_policy()
    second = load_ign_road_vehicle_proxy_policy()

    assert first == second
    assert first is not second
    assert first.nature is not second.nature


def test_public_api_exports_only_stable_policy_symbols() -> None:
    import landscout.stages.road_vehicle_proxy_policy as module

    expected = {
        "IgnRoadVehicleProxyPolicy",
        "IgnRoadVehicleProxyPolicyError",
        "load_ign_road_vehicle_proxy_policy",
    }
    assert set(module.__all__) == expected
    assert expected <= set(stages.__all__)
    assert all(hasattr(stages, name) for name in expected)
    assert not hasattr(stages, "_RoadNatureConfig")


@pytest.mark.parametrize(
    ("mutation", "message"),
    [
        (lambda payload: payload.update(unexpected=True), "invalid"),
        (
            lambda payload: payload["references"]["navigation"].update(unexpected=True),
            "invalid",
        ),
        (lambda payload: payload.pop("policy_id"), "invalid"),
        (
            lambda payload: payload["source_values"].pop("nature"),
            "invalid",
        ),
    ],
    ids=["unknown-top", "unknown-nested", "missing-id", "missing-group"],
)
def test_invalid_config_structure_is_rejected(
    tmp_path: Path,
    mutation: Any,
    message: str,
) -> None:
    payload = _payload()
    mutation(payload)

    with pytest.raises(IgnRoadVehicleProxyPolicyError, match=message):
        _load_payload(tmp_path, payload)


@pytest.mark.parametrize("version", [0, 1, 3, 999])
def test_unsupported_schema_version_is_rejected(tmp_path: Path, version: int) -> None:
    payload = _payload()
    payload["schema_version"] = version

    with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)


@pytest.mark.parametrize(
    ("path", "value"),
    [
        (("policy_id",), "ign_bdtopo_general_vehicle_proxy_v1"),
        (("scope",), "HEAVY_VEHICLE_POLICY"),
        (("heavy_vehicle_access",), "PROVEN"),
    ],
)
def test_wrong_policy_identity_is_rejected(
    tmp_path: Path,
    path: tuple[str, ...],
    value: str,
) -> None:
    payload = _payload()
    target = payload
    for key in path[:-1]:
        target = target[key]
    target[path[-1]] = value

    with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)


@pytest.mark.parametrize("reference", ["navigation", "bdtopo_product"])
def test_both_evidence_references_are_required(tmp_path: Path, reference: str) -> None:
    payload = _payload()
    payload["references"].pop(reference)

    with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)


def test_product_reference_document_id_is_exact(tmp_path: Path) -> None:
    payload = _payload()
    payload["references"]["bdtopo_product"]["document_id"] = "OTHER"

    with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)


def test_unknown_evidence_reference_is_rejected(tmp_path: Path) -> None:
    payload = _payload()
    payload["references"]["other"] = payload["references"]["navigation"]

    with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)


def test_asset_state_groups_cover_exact_v2_domain() -> None:
    policy = load_ign_road_vehicle_proxy_policy()
    groups = (
        policy.asset_state.in_service,
        policy.asset_state.project_geometry_not_significant,
        policy.asset_state.under_construction,
    )

    assert policy.asset_state.in_service == frozenset({"En service"})
    assert policy.asset_state.project_geometry_not_significant == frozenset(
        {"En projet"}
    )
    assert policy.asset_state.under_construction == frozenset({"En construction"})
    assert set().union(*groups) == {"En service", "En projet", "En construction"}
    assert all(
        sum(value in group for group in groups) == 1 for value in set().union(*groups)
    )


def test_asset_state_group_overlap_is_rejected(tmp_path: Path) -> None:
    payload = _payload()
    payload["source_values"]["asset_state"]["under_construction"] = ["En projet"]

    with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)


@pytest.mark.parametrize(
    ("group", "value"),
    [
        ("in_service", "En service"),
        ("project_geometry_not_significant", "En projet"),
        ("under_construction", "En construction"),
    ],
)
def test_missing_known_asset_state_is_rejected(
    tmp_path: Path, group: str, value: str
) -> None:
    payload = _payload()
    payload["source_values"]["asset_state"][group].remove(value)

    with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)


def test_unknown_additional_asset_state_is_rejected(tmp_path: Path) -> None:
    payload = _payload()
    payload["source_values"]["asset_state"]["in_service"].append("Unknown")

    with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)


@pytest.mark.parametrize("value", ["", " Libre", "Libre "])
def test_semantic_values_must_be_exact_non_empty_strings(
    tmp_path: Path, value: str
) -> None:
    payload = _payload()
    payload["source_values"]["light_vehicle_access"]["open"] = [value]

    with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)


def test_duplicate_semantic_value_is_rejected(tmp_path: Path) -> None:
    payload = _payload()
    payload["source_values"]["light_vehicle_access"]["open"] = [
        "Libre",
        "Libre",
    ]

    with pytest.raises(IgnRoadVehicleProxyPolicyError, match="invalid"):
        _load_payload(tmp_path, payload)


@pytest.mark.parametrize(
    ("group", "source_group", "target_group"),
    [
        ("light_vehicle_access", "open", "toll"),
        ("nature", "general_motor_road", "limited_motor_proxy"),
        ("nature", "limited_motor_proxy", "non_general_vehicle"),
    ],
)
def test_semantic_groups_must_be_pairwise_disjoint(
    tmp_path: Path,
    group: str,
    source_group: str,
    target_group: str,
) -> None:
    payload = _payload()
    value = payload["source_values"][group][source_group][0]
    payload["source_values"][group][target_group].append(value)

    with pytest.raises(IgnRoadVehicleProxyPolicyError, match="invalid"):
        _load_payload(tmp_path, payload)


def test_duplicate_known_restriction_is_rejected(tmp_path: Path) -> None:
    payload = _payload()
    restrictions = payload["source_values"]["known_restriction_review"]
    restrictions.append(restrictions[0])

    with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)


@pytest.mark.parametrize(
    "value",
    [-1.0, 0.0, float("nan"), float("inf"), float("-inf"), "2.9", True],
)
def test_invalid_width_threshold_is_rejected(tmp_path: Path, value: object) -> None:
    payload = _payload()
    payload["source_values"]["width_below_m"] = value

    with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)


def test_exact_width_threshold_is_accepted(tmp_path: Path) -> None:
    payload = _payload()
    payload["source_values"]["width_below_m"] = 2.9

    assert _load_payload(tmp_path, payload).width_below_m == 2.9


@pytest.mark.parametrize(
    ("group", "mutation"),
    [
        ("known", "remove-1"),
        ("known", "remove-5"),
        ("known", "add-7"),
        ("limited", "numeric-6"),
        ("limited", "limited-5"),
        ("limited", "empty"),
    ],
)
def test_importance_domains_must_be_exact(
    tmp_path: Path, group: str, mutation: str
) -> None:
    payload = _payload()
    importance = payload["source_values"]["importance"]
    if mutation == "remove-1":
        importance[group].remove("1")
    elif mutation == "remove-5":
        importance[group].remove("5")
    elif mutation == "add-7":
        importance[group].append("7")
    elif mutation == "numeric-6":
        importance[group] = [6]
    elif mutation == "limited-5":
        importance[group] = ["5"]
    else:
        importance[group] = []

    with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)


def test_importance_domains_expose_known_without_positive_classification() -> None:
    policy = load_ign_road_vehicle_proxy_policy()

    assert policy.importance.known == frozenset({"1", "2", "3", "4", "5", "6"})
    assert policy.importance.limited == frozenset({"6"})
    assert policy.importance.limited <= policy.importance.known
    assert "7" not in policy.importance.known


@pytest.mark.parametrize("mutation", ["missing", "duplicate", "unknown", "reorder"])
def test_decision_precedence_must_be_exact(tmp_path: Path, mutation: str) -> None:
    payload = _payload()
    precedence = payload["decision_precedence"]
    if mutation == "missing":
        precedence.pop()
    elif mutation == "duplicate":
        precedence[-1] = precedence[0]
    elif mutation == "unknown":
        precedence.append("INVENTED_RULE")
    else:
        precedence[0], precedence[1] = precedence[1], precedence[0]

    with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)


def test_decision_precedence_and_rule_outcomes_are_approved() -> None:
    policy = load_ign_road_vehicle_proxy_policy()

    assert policy.decision_precedence == EXPECTED_PRECEDENCE
    assert policy.decision_outcomes.fictitious_geometry == "NOT_DISTANCE_PROXY"
    assert policy.decision_outcomes.project_geometry_not_significant == (
        "NOT_DISTANCE_PROXY"
    )
    assert policy.decision_outcomes.not_in_service == ("NOT_GENERAL_VEHICLE_PROXY")
    assert policy.decision_outcomes.private_road == "RESTRICTED_REVIEW"
    assert policy.decision_outcomes.rights_restricted == "RESTRICTED_REVIEW"
    assert policy.decision_outcomes.temporal_closure == "RESTRICTED_REVIEW"
    assert policy.decision_outcomes.physically_impossible == (
        "NOT_GENERAL_VEHICLE_PROXY"
    )
    assert policy.decision_outcomes.limited_nature == "LIMITED_VEHICLE_PROXY"
    assert policy.decision_outcomes.open_or_toll == "GENERAL_VEHICLE_PROXY"
    assert policy.decision_outcomes.unknown == "UNKNOWN_REVIEW"


def test_project_geometry_rule_has_exact_precedence_position() -> None:
    policy = load_ign_road_vehicle_proxy_policy()

    fictitious = policy.decision_precedence.index("FICTITIOUS_GEOMETRY")
    project = policy.decision_precedence.index("PROJECT_GEOMETRY_NOT_SIGNIFICANT")
    not_in_service = policy.decision_precedence.index("NOT_IN_SERVICE")
    assert fictitious < project < not_in_service
    assert len(policy.decision_precedence) == 16


@pytest.mark.parametrize("mutation", ["missing", "extra", "wrong"])
def test_output_class_vocabulary_must_be_exact(tmp_path: Path, mutation: str) -> None:
    payload = _payload()
    classes = payload["classes"]
    if mutation == "missing":
        classes.pop("unknown_review")
    elif mutation == "extra":
        classes["authorized"] = "AUTHORIZED"
    else:
        classes["general_vehicle_proxy"] = "ROAD_APPROVED"

    with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)


def test_approved_class_vocabulary_has_no_heavy_or_legal_claim() -> None:
    policy = load_ign_road_vehicle_proxy_policy()
    forbidden = ("TRUCK", "HEAVY", "LEGAL", "APPROVED", "BESS_ACCESSIBLE", "AUTHORIZED")

    assert policy.classes.values == EXPECTED_CLASSES
    assert policy.heavy_vehicle_access == "NOT_PROVEN"
    assert all(
        token not in value for value in policy.classes.values for token in forbidden
    )


def test_observed_d031_natures_are_covered_exactly_once() -> None:
    policy = load_ign_road_vehicle_proxy_policy()
    groups = (
        policy.nature.general_motor_road,
        policy.nature.limited_motor_proxy,
        policy.nature.non_general_vehicle,
        policy.nature.special_review,
    )

    assert set().union(*groups) >= OBSERVED_NATURES
    assert all(
        sum(value in group for group in groups) == 1 for value in OBSERVED_NATURES
    )


def test_observed_d031_access_and_importance_vocabularies_are_compatible() -> None:
    policy = load_ign_road_vehicle_proxy_policy()
    access_groups = (
        policy.light_vehicle_access.open,
        policy.light_vehicle_access.toll,
        policy.light_vehicle_access.rights_restricted,
        policy.light_vehicle_access.physically_impossible,
    )

    assert set().union(*access_groups) == OBSERVED_LIGHT_VEHICLE_ACCESS
    assert policy.importance.known == frozenset({"1", "2", "3", "4", "5", "6"})
    assert policy.importance.limited == frozenset({"6"})
    assert policy.decision_outcomes.unknown == "UNKNOWN_REVIEW"


def test_compiled_policy_structures_are_immutable() -> None:
    policy = load_ign_road_vehicle_proxy_policy()

    with pytest.raises(FrozenInstanceError):
        policy.scope = "changed"  # type: ignore[misc]
    with pytest.raises(AttributeError):
        policy.nature.general_motor_road.add("Invented")  # type: ignore[attr-defined]


def test_mutating_source_payload_cannot_affect_another_load() -> None:
    first = load_ign_road_vehicle_proxy_policy()
    mutable = _payload()
    mutable["source_values"]["nature"]["general_motor_road"].append("Invented")
    second = load_ign_road_vehicle_proxy_policy()

    assert first == second
    assert "Invented" not in second.nature.general_motor_road


def test_malformed_yaml_has_controlled_error(tmp_path: Path) -> None:
    path = tmp_path / "malformed.yaml"
    path.write_text("policy_id: [", encoding="utf-8")

    with pytest.raises(IgnRoadVehicleProxyPolicyError):
        load_ign_road_vehicle_proxy_policy(path)


@pytest.mark.parametrize("payload", [None, [], "policy"])
def test_non_mapping_yaml_has_controlled_error(tmp_path: Path, payload: object) -> None:
    with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)


def test_missing_file_has_controlled_error(tmp_path: Path) -> None:
    with pytest.raises(IgnRoadVehicleProxyPolicyError):
        load_ign_road_vehicle_proxy_policy(tmp_path / "missing.yaml")
```

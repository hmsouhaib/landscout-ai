# `tests/unit/test_road_vehicle_proxy_policy.py`

## File identity

- Repository path: `tests/unit/test_road_vehicle_proxy_policy.py`
- File type: Python test
- Layer: unit/regression test
- Domain: test
- Responsibility: Provides complete unit and regression coverage for the `road_vehicle_proxy_policy` contracts exercised in this file.
- Source SHA256: `32c7146437c4e120564468e06b95860cbbcf3b5c7ae15824728523759861a40f`

## 1. Purpose

Provides complete unit and regression coverage for the `road_vehicle_proxy_policy` contracts exercised in this file.

## 2. Position in LandScout architecture

This file belongs to the **unit/regression test** layer and the **test** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

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

## 4. Contract taxonomy

### A. Python constants

#### `POLICY_PATH`

```python
POLICY_PATH = Path("configs/access/ign_bdtopo_vehicle_proxy_policy.yaml")
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_road_vehicle_proxy_policy.py::_payload` (value reference), `tests/unit/test_road_vehicle_proxy_policy.py::test_checked_in_policy_hash_binds_exact_file_bytes` (value reference).

#### `EXPECTED_POLICY_ID`

```python
EXPECTED_POLICY_ID = "ign_bdtopo_general_vehicle_proxy_v2"
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_road_vehicle_proxy_policy.py::test_checked_in_policy_loads_with_exact_public_identity_and_reference` (value reference).

#### `EXPECTED_SCOPE`

```python
EXPECTED_SCOPE = "OFFICIAL_IGN_CAR_ROUTING_EVIDENCE_ONLY"
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `tests/unit/test_road_vehicle_proxy_policy.py::test_checked_in_policy_loads_with_exact_public_identity_and_reference` (value reference).

#### `EXPECTED_CLASSES`

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

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_road_vehicle_proxy_policy.py::test_approved_class_vocabulary_has_no_heavy_or_legal_claim` (value reference).

#### `EXPECTED_PRECEDENCE`

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

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `tests/unit/test_road_vehicle_proxy_policy.py::test_decision_precedence_and_rule_outcomes_are_approved` (value reference).

#### `OBSERVED_NATURES`

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

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_road_vehicle_proxy_policy.py::test_observed_d031_natures_are_covered_exactly_once` (value reference).

#### `OBSERVED_LIGHT_VEHICLE_ACCESS`

```python
OBSERVED_LIGHT_VEHICLE_ACCESS = {
    "Libre",
    "Physiquement impossible",
    "Restreint aux ayants droit",
    "A péage",
}
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_road_vehicle_proxy_policy.py::test_observed_d031_access_and_importance_vocabularies_are_compatible` (value reference).


### B. Type aliases and closed domains

No module-level Literal/Annotated/TypeAlias declaration is present.

### C. Meaningful dunder contracts

No meaningful module-level dunder contract is declared.

### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

No class/model/dataclass is declared.

## 6. Functions and methods

### `_payload`

**Exact signature**

```python
def _payload() -> dict[str, Any]:
```

**Purpose**

Private `test` helper for payload; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict[str, Any]`.
- Every observed return expression is reproduced without truncation:
```python
payload
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: `POLICY_PATH.read_text`.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_invalid_config_structure_is_rejected` via `_payload`.
- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_unsupported_schema_version_is_rejected` via `_payload`.
- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_wrong_policy_identity_is_rejected` via `_payload`.
- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_both_evidence_references_are_required` via `_payload`.
- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_product_reference_document_id_is_exact` via `_payload`.
- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_unknown_evidence_reference_is_rejected` via `_payload`.
- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_asset_state_group_overlap_is_rejected` via `_payload`.
- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_missing_known_asset_state_is_rejected` via `_payload`.
- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_unknown_additional_asset_state_is_rejected` via `_payload`.
- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_semantic_values_must_be_exact_non_empty_strings` via `_payload`.
- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_duplicate_semantic_value_is_rejected` via `_payload`.
- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_semantic_groups_must_be_pairwise_disjoint` via `_payload`.
- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_duplicate_known_restriction_is_rejected` via `_payload`.
- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_invalid_width_threshold_is_rejected` via `_payload`.
- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_exact_width_threshold_is_accepted` via `_payload`.
- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_importance_domains_must_be_exact` via `_payload`.
- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_decision_precedence_must_be_exact` via `_payload`.
- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_output_class_vocabulary_must_be_exact` via `_payload`.
- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_mutating_source_payload_cannot_affect_another_load` via `_payload`.

**Complete source-ordered implementation**

```python
def _payload() -> dict[str, Any]:
    payload = yaml.safe_load(POLICY_PATH.read_text(encoding="utf-8"))
    assert isinstance(payload, dict)
    return payload
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_write_policy`

**Exact signature**

```python
def _write_policy(tmp_path: Path, payload: object) -> Path:
```

**Purpose**

Serializes policy; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `Path`.
- Every observed return expression is reproduced without truncation:
```python
path
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: `path.write_text`.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::_load_payload` via `_write_policy`.

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

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_load_payload`

**Exact signature**

```python
def _load_payload(tmp_path: Path, payload: object) -> IgnRoadVehicleProxyPolicy:
```

**Purpose**

Reads and validates payload; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `IgnRoadVehicleProxyPolicy`.
- Every observed return expression is reproduced without truncation:
```python
load_ign_road_vehicle_proxy_policy(_write_policy(tmp_path, payload))
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

- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_invalid_config_structure_is_rejected` via `_load_payload`.
- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_unsupported_schema_version_is_rejected` via `_load_payload`.
- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_wrong_policy_identity_is_rejected` via `_load_payload`.
- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_both_evidence_references_are_required` via `_load_payload`.
- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_product_reference_document_id_is_exact` via `_load_payload`.
- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_unknown_evidence_reference_is_rejected` via `_load_payload`.
- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_asset_state_group_overlap_is_rejected` via `_load_payload`.
- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_missing_known_asset_state_is_rejected` via `_load_payload`.
- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_unknown_additional_asset_state_is_rejected` via `_load_payload`.
- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_semantic_values_must_be_exact_non_empty_strings` via `_load_payload`.
- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_duplicate_semantic_value_is_rejected` via `_load_payload`.
- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_semantic_groups_must_be_pairwise_disjoint` via `_load_payload`.
- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_duplicate_known_restriction_is_rejected` via `_load_payload`.
- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_invalid_width_threshold_is_rejected` via `_load_payload`.
- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_exact_width_threshold_is_accepted` via `_load_payload`.
- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_importance_domains_must_be_exact` via `_load_payload`.
- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_decision_precedence_must_be_exact` via `_load_payload`.
- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_output_class_vocabulary_must_be_exact` via `_load_payload`.
- direct call: `tests/unit/test_road_vehicle_proxy_policy.py::test_non_mapping_yaml_has_controlled_error` via `_load_payload`.

**Complete source-ordered implementation**

```python
def _load_payload(tmp_path: Path, payload: object) -> IgnRoadVehicleProxyPolicy:
    return load_ign_road_vehicle_proxy_policy(_write_policy(tmp_path, payload))
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_checked_in_policy_loads_with_exact_public_identity_and_reference`

**Purpose**

Exercises `checked in policy loads with exact public identity and reference`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
policy = load_ign_road_vehicle_proxy_policy()
```

**Expected result**

```python
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

**Regression protected**

Locks `checked in policy loads with exact public identity and reference` through the exact asserted conditions: `type(policy) is IgnRoadVehicleProxyPolicy`; `policy.policy_id == EXPECTED_POLICY_ID`; `policy.schema_version == 2`; `policy.scope == EXPECTED_SCOPE`; plus 12 additional reproduced assertion(s).

**Test boundary**

- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

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

### `test_checked_in_policy_hash_binds_exact_file_bytes`

**Purpose**

Exercises `checked in policy hash binds exact file bytes`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
policy = load_ign_road_vehicle_proxy_policy(POLICY_PATH)
```

**Expected result**

```python
assert policy.config_sha256 == sha256(POLICY_PATH.read_bytes()).hexdigest()
assert len(policy.config_sha256) == 64
assert policy.config_sha256 == policy.config_sha256.lower()
```

**Regression protected**

Locks `checked in policy hash binds exact file bytes` through the exact asserted conditions: `policy.config_sha256 == sha256(POLICY_PATH.read_bytes()).hexdigest()`; `len(policy.config_sha256) == 64`; `policy.config_sha256 == policy.config_sha256.lower()`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_checked_in_policy_hash_binds_exact_file_bytes() -> None:
    policy = load_ign_road_vehicle_proxy_policy(POLICY_PATH)

    assert policy.config_sha256 == sha256(POLICY_PATH.read_bytes()).hexdigest()
    assert len(policy.config_sha256) == 64
    assert policy.config_sha256 == policy.config_sha256.lower()
```

### `test_repeat_loading_is_deterministic_and_independent`

**Purpose**

Exercises `repeat loading is deterministic and independent`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
first = load_ign_road_vehicle_proxy_policy()
second = load_ign_road_vehicle_proxy_policy()
```

**Expected result**

```python
assert first == second
assert first is not second
assert first.nature is not second.nature
```

**Regression protected**

Locks `repeat loading is deterministic and independent` through the exact asserted conditions: `first == second`; `first is not second`; `first.nature is not second.nature`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_repeat_loading_is_deterministic_and_independent() -> None:
    first = load_ign_road_vehicle_proxy_policy()
    second = load_ign_road_vehicle_proxy_policy()

    assert first == second
    assert first is not second
    assert first.nature is not second.nature
```

### `test_public_api_exports_only_stable_policy_symbols`

**Purpose**

Exercises `public api exports only stable policy symbols`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
import landscout.stages.road_vehicle_proxy_policy as module
expected = {
        "IgnRoadVehicleProxyPolicy",
        "IgnRoadVehicleProxyPolicyError",
        "load_ign_road_vehicle_proxy_policy",
    }
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert set(module.__all__) == expected
assert expected <= set(stages.__all__)
assert all(hasattr(stages, name) for name in expected)
assert not hasattr(stages, "_RoadNatureConfig")
```

**Regression protected**

Locks `public api exports only stable policy symbols` through the exact asserted conditions: `set(module.__all__) == expected`; `expected <= set(stages.__all__)`; `all((hasattr(stages, name) for name in expected))`; `not hasattr(stages, '_RoadNatureConfig')`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_invalid_config_structure_is_rejected`

**Purpose**

Exercises `invalid config structure is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `message`, `mutation`.

**Setup**

```python
payload = _payload()
mutation(payload)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnRoadVehicleProxyPolicyError, match=message):
        _load_payload(tmp_path, payload)
```

**Regression protected**

Locks `invalid config structure is rejected`: the reproduced adversarial input must raise `IgnRoadVehicleProxyPolicyError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

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

### `test_unsupported_schema_version_is_rejected`

**Purpose**

Exercises `unsupported schema version is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `version`.

**Setup**

```python
payload = _payload()
payload["schema_version"] = version
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)
```

**Regression protected**

Locks `unsupported schema version is rejected`: the reproduced adversarial input must raise `IgnRoadVehicleProxyPolicyError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_unsupported_schema_version_is_rejected(
    tmp_path: Path, version: int
) -> None:
    payload = _payload()
    payload["schema_version"] = version

    with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)
```

### `test_wrong_policy_identity_is_rejected`

**Purpose**

Exercises `wrong policy identity is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `path`, `value`.

**Setup**

```python
payload = _payload()
target = payload
for key in path[:-1]:
        target = target[key]
target[path[-1]] = value
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)
```

**Regression protected**

Locks `wrong policy identity is rejected`: the reproduced adversarial input must raise `IgnRoadVehicleProxyPolicyError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

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

### `test_both_evidence_references_are_required`

**Purpose**

Exercises `both evidence references are required`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `reference`.

**Setup**

```python
payload = _payload()
payload["references"].pop(reference)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)
```

**Regression protected**

Locks `both evidence references are required`: the reproduced adversarial input must raise `IgnRoadVehicleProxyPolicyError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_both_evidence_references_are_required(
    tmp_path: Path, reference: str
) -> None:
    payload = _payload()
    payload["references"].pop(reference)

    with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)
```

### `test_product_reference_document_id_is_exact`

**Purpose**

Exercises `product reference document id is exact`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
payload = _payload()
payload["references"]["bdtopo_product"]["document_id"] = "OTHER"
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)
```

**Regression protected**

Locks `product reference document id is exact`: the reproduced adversarial input must raise `IgnRoadVehicleProxyPolicyError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_product_reference_document_id_is_exact(tmp_path: Path) -> None:
    payload = _payload()
    payload["references"]["bdtopo_product"]["document_id"] = "OTHER"

    with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)
```

### `test_unknown_evidence_reference_is_rejected`

**Purpose**

Exercises `unknown evidence reference is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
payload = _payload()
payload["references"]["other"] = payload["references"]["navigation"]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)
```

**Regression protected**

Locks `unknown evidence reference is rejected`: the reproduced adversarial input must raise `IgnRoadVehicleProxyPolicyError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_unknown_evidence_reference_is_rejected(tmp_path: Path) -> None:
    payload = _payload()
    payload["references"]["other"] = payload["references"]["navigation"]

    with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)
```

### `test_asset_state_groups_cover_exact_v2_domain`

**Purpose**

Exercises `asset state groups cover exact v2 domain`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
groups = (
        policy.asset_state.in_service,
        policy.asset_state.project_geometry_not_significant,
        policy.asset_state.under_construction,
    )
```

**Action**

```python
policy = load_ign_road_vehicle_proxy_policy()
```

**Expected result**

```python
assert policy.asset_state.in_service == frozenset({"En service"})
assert policy.asset_state.project_geometry_not_significant == frozenset(
        {"En projet"}
    )
assert policy.asset_state.under_construction == frozenset({"En construction"})
assert set().union(*groups) == {"En service", "En projet", "En construction"}
assert all(sum(value in group for group in groups) == 1 for value in set().union(*groups))
```

**Regression protected**

Locks `asset state groups cover exact v2 domain` through the exact asserted conditions: `policy.asset_state.in_service == frozenset({'En service'})`; `policy.asset_state.project_geometry_not_significant == frozenset({'En projet'})`; `policy.asset_state.under_construction == frozenset({'En construction'})`; `set().union(*groups) == {'En service', 'En projet', 'En construction'}`; plus 1 additional reproduced assertion(s).

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

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
    assert all(sum(value in group for group in groups) == 1 for value in set().union(*groups))
```

### `test_asset_state_group_overlap_is_rejected`

**Purpose**

Exercises `asset state group overlap is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
payload = _payload()
payload["source_values"]["asset_state"]["under_construction"] = [
        "En projet"
    ]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)
```

**Regression protected**

Locks `asset state group overlap is rejected`: the reproduced adversarial input must raise `IgnRoadVehicleProxyPolicyError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_asset_state_group_overlap_is_rejected(tmp_path: Path) -> None:
    payload = _payload()
    payload["source_values"]["asset_state"]["under_construction"] = [
        "En projet"
    ]

    with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)
```

### `test_missing_known_asset_state_is_rejected`

**Purpose**

Exercises `missing known asset state is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `group`, `value`.

**Setup**

```python
payload = _payload()
payload["source_values"]["asset_state"][group].remove(value)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)
```

**Regression protected**

Locks `missing known asset state is rejected`: the reproduced adversarial input must raise `IgnRoadVehicleProxyPolicyError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_missing_known_asset_state_is_rejected(
    tmp_path: Path, group: str, value: str
) -> None:
    payload = _payload()
    payload["source_values"]["asset_state"][group].remove(value)

    with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)
```

### `test_unknown_additional_asset_state_is_rejected`

**Purpose**

Exercises `unknown additional asset state is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
payload = _payload()
payload["source_values"]["asset_state"]["in_service"].append("Unknown")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)
```

**Regression protected**

Locks `unknown additional asset state is rejected`: the reproduced adversarial input must raise `IgnRoadVehicleProxyPolicyError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_unknown_additional_asset_state_is_rejected(tmp_path: Path) -> None:
    payload = _payload()
    payload["source_values"]["asset_state"]["in_service"].append("Unknown")

    with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)
```

### `test_semantic_values_must_be_exact_non_empty_strings`

**Purpose**

Exercises `semantic values must be exact non empty strings`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `value`.

**Setup**

```python
payload = _payload()
payload["source_values"]["light_vehicle_access"]["open"] = [value]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)
```

**Regression protected**

Locks `semantic values must be exact non empty strings`: the reproduced adversarial input must raise `IgnRoadVehicleProxyPolicyError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_semantic_values_must_be_exact_non_empty_strings(
    tmp_path: Path, value: str
) -> None:
    payload = _payload()
    payload["source_values"]["light_vehicle_access"]["open"] = [value]

    with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)
```

### `test_duplicate_semantic_value_is_rejected`

**Purpose**

Exercises `duplicate semantic value is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
payload = _payload()
payload["source_values"]["light_vehicle_access"]["open"] = [
        "Libre",
        "Libre",
    ]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnRoadVehicleProxyPolicyError, match="invalid"):
        _load_payload(tmp_path, payload)
```

**Regression protected**

Locks `duplicate semantic value is rejected`: the reproduced adversarial input must raise `IgnRoadVehicleProxyPolicyError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

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

### `test_semantic_groups_must_be_pairwise_disjoint`

**Purpose**

Exercises `semantic groups must be pairwise disjoint`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `group`, `source_group`, `target_group`.

**Setup**

```python
payload = _payload()
value = payload["source_values"][group][source_group][0]
payload["source_values"][group][target_group].append(value)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnRoadVehicleProxyPolicyError, match="invalid"):
        _load_payload(tmp_path, payload)
```

**Regression protected**

Locks `semantic groups must be pairwise disjoint`: the reproduced adversarial input must raise `IgnRoadVehicleProxyPolicyError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

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

### `test_duplicate_known_restriction_is_rejected`

**Purpose**

Exercises `duplicate known restriction is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
payload = _payload()
restrictions = payload["source_values"]["known_restriction_review"]
restrictions.append(restrictions[0])
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)
```

**Regression protected**

Locks `duplicate known restriction is rejected`: the reproduced adversarial input must raise `IgnRoadVehicleProxyPolicyError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_duplicate_known_restriction_is_rejected(tmp_path: Path) -> None:
    payload = _payload()
    restrictions = payload["source_values"]["known_restriction_review"]
    restrictions.append(restrictions[0])

    with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)
```

### `test_invalid_width_threshold_is_rejected`

**Purpose**

Exercises `invalid width threshold is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `value`.

**Setup**

```python
payload = _payload()
payload["source_values"]["width_below_m"] = value
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)
```

**Regression protected**

Locks `invalid width threshold is rejected`: the reproduced adversarial input must raise `IgnRoadVehicleProxyPolicyError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_invalid_width_threshold_is_rejected(tmp_path: Path, value: object) -> None:
    payload = _payload()
    payload["source_values"]["width_below_m"] = value

    with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)
```

### `test_exact_width_threshold_is_accepted`

**Purpose**

Exercises `exact width threshold is accepted`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
payload = _payload()
payload["source_values"]["width_below_m"] = 2.9
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert _load_payload(tmp_path, payload).width_below_m == 2.9
```

**Regression protected**

Locks `exact width threshold is accepted` through the exact asserted conditions: `_load_payload(tmp_path, payload).width_below_m == 2.9`.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_exact_width_threshold_is_accepted(tmp_path: Path) -> None:
    payload = _payload()
    payload["source_values"]["width_below_m"] = 2.9

    assert _load_payload(tmp_path, payload).width_below_m == 2.9
```

### `test_importance_domains_must_be_exact`

**Purpose**

Exercises `importance domains must be exact`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `group`, `mutation`.

**Setup**

```python
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
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)
```

**Regression protected**

Locks `importance domains must be exact`: the reproduced adversarial input must raise `IgnRoadVehicleProxyPolicyError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

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

### `test_importance_domains_expose_known_without_positive_classification`

**Purpose**

Exercises `importance domains expose known without positive classification`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
policy = load_ign_road_vehicle_proxy_policy()
```

**Expected result**

```python
assert policy.importance.known == frozenset({"1", "2", "3", "4", "5", "6"})
assert policy.importance.limited == frozenset({"6"})
assert policy.importance.limited <= policy.importance.known
assert "7" not in policy.importance.known
```

**Regression protected**

Locks `importance domains expose known without positive classification` through the exact asserted conditions: `policy.importance.known == frozenset({'1', '2', '3', '4', '5', '6'})`; `policy.importance.limited == frozenset({'6'})`; `policy.importance.limited <= policy.importance.known`; `'7' not in policy.importance.known`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_importance_domains_expose_known_without_positive_classification() -> None:
    policy = load_ign_road_vehicle_proxy_policy()

    assert policy.importance.known == frozenset({"1", "2", "3", "4", "5", "6"})
    assert policy.importance.limited == frozenset({"6"})
    assert policy.importance.limited <= policy.importance.known
    assert "7" not in policy.importance.known
```

### `test_decision_precedence_must_be_exact`

**Purpose**

Exercises `decision precedence must be exact`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `mutation`.

**Setup**

```python
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
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)
```

**Regression protected**

Pins the configured policy-rule ordering so a lower-priority observation cannot replace the controlling evidence.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_decision_precedence_must_be_exact(
    tmp_path: Path, mutation: str
) -> None:
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

### `test_decision_precedence_and_rule_outcomes_are_approved`

**Purpose**

Exercises `decision precedence and rule outcomes are approved`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
policy = load_ign_road_vehicle_proxy_policy()
```

**Expected result**

```python
assert policy.decision_precedence == EXPECTED_PRECEDENCE
assert policy.decision_outcomes.fictitious_geometry == "NOT_DISTANCE_PROXY"
assert policy.decision_outcomes.project_geometry_not_significant == (
        "NOT_DISTANCE_PROXY"
    )
assert policy.decision_outcomes.not_in_service == (
        "NOT_GENERAL_VEHICLE_PROXY"
    )
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

**Regression protected**

Pins the configured policy-rule ordering so a lower-priority observation cannot replace the controlling evidence.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_decision_precedence_and_rule_outcomes_are_approved() -> None:
    policy = load_ign_road_vehicle_proxy_policy()

    assert policy.decision_precedence == EXPECTED_PRECEDENCE
    assert policy.decision_outcomes.fictitious_geometry == "NOT_DISTANCE_PROXY"
    assert policy.decision_outcomes.project_geometry_not_significant == (
        "NOT_DISTANCE_PROXY"
    )
    assert policy.decision_outcomes.not_in_service == (
        "NOT_GENERAL_VEHICLE_PROXY"
    )
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

### `test_project_geometry_rule_has_exact_precedence_position`

**Purpose**

Exercises `project geometry rule has exact precedence position`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
fictitious = policy.decision_precedence.index("FICTITIOUS_GEOMETRY")
project = policy.decision_precedence.index(
        "PROJECT_GEOMETRY_NOT_SIGNIFICANT"
    )
not_in_service = policy.decision_precedence.index("NOT_IN_SERVICE")
```

**Action**

```python
policy = load_ign_road_vehicle_proxy_policy()
```

**Expected result**

```python
assert fictitious < project < not_in_service
assert len(policy.decision_precedence) == 16
```

**Regression protected**

Pins the configured policy-rule ordering so a lower-priority observation cannot replace the controlling evidence.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_project_geometry_rule_has_exact_precedence_position() -> None:
    policy = load_ign_road_vehicle_proxy_policy()

    fictitious = policy.decision_precedence.index("FICTITIOUS_GEOMETRY")
    project = policy.decision_precedence.index(
        "PROJECT_GEOMETRY_NOT_SIGNIFICANT"
    )
    not_in_service = policy.decision_precedence.index("NOT_IN_SERVICE")
    assert fictitious < project < not_in_service
    assert len(policy.decision_precedence) == 16
```

### `test_output_class_vocabulary_must_be_exact`

**Purpose**

Exercises `output class vocabulary must be exact`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `mutation`.

**Setup**

```python
payload = _payload()
classes = payload["classes"]
if mutation == "missing":
        classes.pop("unknown_review")
    elif mutation == "extra":
        classes["authorized"] = "AUTHORIZED"
    else:
        classes["general_vehicle_proxy"] = "ROAD_APPROVED"
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)
```

**Regression protected**

Locks `output class vocabulary must be exact`: the reproduced adversarial input must raise `IgnRoadVehicleProxyPolicyError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_output_class_vocabulary_must_be_exact(
    tmp_path: Path, mutation: str
) -> None:
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

### `test_approved_class_vocabulary_has_no_heavy_or_legal_claim`

**Purpose**

Exercises `approved class vocabulary has no heavy or legal claim`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
forbidden = ("TRUCK", "HEAVY", "LEGAL", "APPROVED", "BESS_ACCESSIBLE", "AUTHORIZED")
```

**Action**

```python
policy = load_ign_road_vehicle_proxy_policy()
```

**Expected result**

```python
assert policy.classes.values == EXPECTED_CLASSES
assert policy.heavy_vehicle_access == "NOT_PROVEN"
assert all(
        token not in value
        for value in policy.classes.values
        for token in forbidden
    )
```

**Regression protected**

Locks `approved class vocabulary has no heavy or legal claim` through the exact asserted conditions: `policy.classes.values == EXPECTED_CLASSES`; `policy.heavy_vehicle_access == 'NOT_PROVEN'`; `all((token not in value for value in policy.classes.values for token in forbidden))`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_approved_class_vocabulary_has_no_heavy_or_legal_claim() -> None:
    policy = load_ign_road_vehicle_proxy_policy()
    forbidden = ("TRUCK", "HEAVY", "LEGAL", "APPROVED", "BESS_ACCESSIBLE", "AUTHORIZED")

    assert policy.classes.values == EXPECTED_CLASSES
    assert policy.heavy_vehicle_access == "NOT_PROVEN"
    assert all(
        token not in value
        for value in policy.classes.values
        for token in forbidden
    )
```

### `test_observed_d031_natures_are_covered_exactly_once`

**Purpose**

Exercises `observed d031 natures are covered exactly once`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
groups = (
        policy.nature.general_motor_road,
        policy.nature.limited_motor_proxy,
        policy.nature.non_general_vehicle,
        policy.nature.special_review,
    )
```

**Action**

```python
policy = load_ign_road_vehicle_proxy_policy()
```

**Expected result**

```python
assert set().union(*groups) >= OBSERVED_NATURES
assert all(sum(value in group for group in groups) == 1 for value in OBSERVED_NATURES)
```

**Regression protected**

Locks `observed d031 natures are covered exactly once` through the exact asserted conditions: `set().union(*groups) >= OBSERVED_NATURES`; `all((sum((value in group for group in groups)) == 1 for value in OBSERVED_NATURES))`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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
    assert all(sum(value in group for group in groups) == 1 for value in OBSERVED_NATURES)
```

### `test_observed_d031_access_and_importance_vocabularies_are_compatible`

**Purpose**

Exercises `observed d031 access and importance vocabularies are compatible`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
access_groups = (
        policy.light_vehicle_access.open,
        policy.light_vehicle_access.toll,
        policy.light_vehicle_access.rights_restricted,
        policy.light_vehicle_access.physically_impossible,
    )
```

**Action**

```python
policy = load_ign_road_vehicle_proxy_policy()
```

**Expected result**

```python
assert set().union(*access_groups) == OBSERVED_LIGHT_VEHICLE_ACCESS
assert policy.importance.known == frozenset({"1", "2", "3", "4", "5", "6"})
assert policy.importance.limited == frozenset({"6"})
assert policy.decision_outcomes.unknown == "UNKNOWN_REVIEW"
```

**Regression protected**

Locks `observed d031 access and importance vocabularies are compatible` through the exact asserted conditions: `set().union(*access_groups) == OBSERVED_LIGHT_VEHICLE_ACCESS`; `policy.importance.known == frozenset({'1', '2', '3', '4', '5', '6'})`; `policy.importance.limited == frozenset({'6'})`; `policy.decision_outcomes.unknown == 'UNKNOWN_REVIEW'`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_compiled_policy_structures_are_immutable`

**Purpose**

Exercises `compiled policy structures are immutable`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
policy = load_ign_road_vehicle_proxy_policy()
```

**Expected result**

```python
with pytest.raises(FrozenInstanceError):
        policy.scope = "changed"
with pytest.raises(AttributeError):
        policy.nature.general_motor_road.add("Invented")
```

**Regression protected**

Locks `compiled policy structures are immutable`: the reproduced adversarial input must raise `FrozenInstanceError`, `AttributeError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_compiled_policy_structures_are_immutable() -> None:
    policy = load_ign_road_vehicle_proxy_policy()

    with pytest.raises(FrozenInstanceError):
        policy.scope = "changed"  # type: ignore[misc]
    with pytest.raises(AttributeError):
        policy.nature.general_motor_road.add("Invented")
```

### `test_mutating_source_payload_cannot_affect_another_load`

**Purpose**

Exercises `mutating source payload cannot affect another load`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
mutable = _payload()
mutable["source_values"]["nature"]["general_motor_road"].append("Invented")
```

**Action**

```python
first = load_ign_road_vehicle_proxy_policy()
second = load_ign_road_vehicle_proxy_policy()
```

**Expected result**

```python
assert first == second
assert "Invented" not in second.nature.general_motor_road
```

**Regression protected**

Locks `mutating source payload cannot affect another load` through the exact asserted conditions: `first == second`; `'Invented' not in second.nature.general_motor_road`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_mutating_source_payload_cannot_affect_another_load() -> None:
    first = load_ign_road_vehicle_proxy_policy()
    mutable = _payload()
    mutable["source_values"]["nature"]["general_motor_road"].append("Invented")
    second = load_ign_road_vehicle_proxy_policy()

    assert first == second
    assert "Invented" not in second.nature.general_motor_road
```

### `test_malformed_yaml_has_controlled_error`

**Purpose**

Exercises `malformed yaml has controlled error`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
path = tmp_path / "malformed.yaml"
path.write_text("policy_id: [", encoding="utf-8")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnRoadVehicleProxyPolicyError):
        load_ign_road_vehicle_proxy_policy(path)
```

**Regression protected**

Locks `malformed yaml has controlled error`: the reproduced adversarial input must raise `IgnRoadVehicleProxyPolicyError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_malformed_yaml_has_controlled_error(tmp_path: Path) -> None:
    path = tmp_path / "malformed.yaml"
    path.write_text("policy_id: [", encoding="utf-8")

    with pytest.raises(IgnRoadVehicleProxyPolicyError):
        load_ign_road_vehicle_proxy_policy(path)
```

### `test_non_mapping_yaml_has_controlled_error`

**Purpose**

Exercises `non mapping yaml has controlled error`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `payload`.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)
```

**Regression protected**

Locks `non mapping yaml has controlled error`: the reproduced adversarial input must raise `IgnRoadVehicleProxyPolicyError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_non_mapping_yaml_has_controlled_error(
    tmp_path: Path, payload: object
) -> None:
    with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)
```

### `test_missing_file_has_controlled_error`

**Purpose**

Exercises `missing file has controlled error`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnRoadVehicleProxyPolicyError):
        load_ign_road_vehicle_proxy_policy(tmp_path / "missing.yaml")
```

**Regression protected**

Locks `missing file has controlled error`: the reproduced adversarial input must raise `IgnRoadVehicleProxyPolicyError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_missing_file_has_controlled_error(tmp_path: Path) -> None:
    with pytest.raises(IgnRoadVehicleProxyPolicyError):
        load_ign_road_vehicle_proxy_policy(tmp_path / "missing.yaml")
```


## 7. Data contracts

No module-level canonical frame schema, mapping, or dtype declaration is present. Any frame interaction is recoverable from the complete function implementations below; no string literal is promoted to a column merely because it appears in code.

No enum/status/Literal value is classified as a column unless it is separately present in a canonical schema declaration. Mapping keys, JSON keys, dataclass fields, and configuration leaves remain distinct categories.

## 8. Interfaces

This module does not define `__all__`; no package-export guarantee is inferred from its absence. Symbols can still be imported directly or re-exported by a separate package initializer, as shown by the reference lists.

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

The module contributes to the test flow through the exact facts, proxy evidence, policy results, diagnostics, or prechecks identified above.

## 15. Explicit non-goals

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

## 16. Tests

Test consumers and framework invocation are included in per-symbol interfaces. Test modules distinguish fixture injection from parameterized values and reproduce setup/action/assertion source.

## 17. Change impact

Any source-byte change invalidates the SHA above. Review exact exports, aliases, canonical frame schemas/dtypes, configured source/policy identities, callers, framework hooks, artifacts, and all linked tests before updating this companion.

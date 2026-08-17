# `tests/unit/test_road_vehicle_proxy_policy.py`

## File identity

- Repository path: `tests/unit/test_road_vehicle_proxy_policy.py`
- File type: Python test
- Primary responsibility: Provides complete unit and regression coverage for the `road_vehicle_proxy_policy` contracts exercised in this file.
- Layer / domain: `unit/regression test` / `test`
- Public or internal role: Internal test support; not a production API.
- Source SHA256: `32c7146437c4e120564468e06b95860cbbcf3b5c7ae15824728523759861a40f`

## 1. Purpose

Provides complete unit and regression coverage for the `road_vehicle_proxy_policy` contracts exercised in this file.

## 2. Position in LandScout architecture

This file is a `unit/regression test` artifact in the `test` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from __future__ import annotations` — required by the implementation paths and symbols documented below.
- `from dataclasses import FrozenInstanceError` — required by the implementation paths and symbols documented below.
- `from hashlib import sha256` — required by the implementation paths and symbols documented below.
- `from pathlib import Path` — required by the implementation paths and symbols documented below.
- `from typing import Any` — required by the implementation paths and symbols documented below.

### Third-party

- `import pytest` — required by the implementation paths and symbols documented below.
- `import yaml` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout import stages` — required by the implementation paths and symbols documented below.
- `from landscout.stages.road_vehicle_proxy_policy import ( IgnRoadVehicleProxyPolicy, IgnRoadVehicleProxyPolicyError, load_ign_road_vehicle_proxy_policy, )` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `POLICY_PATH` | `Path("configs/access/ign_bdtopo_vehicle_proxy_policy.yaml")` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `EXPECTED_POLICY_ID` | `"ign_bdtopo_general_vehicle_proxy_v2"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `EXPECTED_SCOPE` | `"OFFICIAL_IGN_CAR_ROUTING_EVIDENCE_ONLY"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `EXPECTED_CLASSES` | `( "GENERAL_VEHICLE_PROXY", "LIMITED_VEHICLE_PROXY", "RESTRICTED_REVIEW", "NOT_GENERAL_VEHICLE_PROXY", "NOT_DISTANCE_PROXY", "UNKNOWN_REVIEW", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `EXPECTED_PRECEDENCE` | `( "FICTITIOUS_GEOMETRY", "PROJECT_GEOMETRY_NOT_SIGNIFICANT", "NOT_IN_SERVICE", "PHYSICALLY_IMPOSSIBLE", "NON_GENERAL_VEHICLE_NATURE", "RIGHTS_RESTRICTED", "PRIVATE_ROAD", "TEMPORAL_CLOSURE", "KNOWN_RESTRICTION", "OTHER_RECORDED_RESTRICTION", "SPECIAL_NATURE", "LIMITED_NATURE", "IMPORTANCE_6", "NARROW_CARRIAGEWAY", "OPEN_OR_TOLL", "UNKNOWN", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `OBSERVED_NATURES` | `{ "Route à 1 chaussée", "Chemin", "Route empierrée", "Sentier", "Rond-point", "Route à 2 chaussées", "Type autoroutier", "Bretelle", "Escalier", "Bac ou liaison maritime", }` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `OBSERVED_LIGHT_VEHICLE_ACCESS` | `{ "Libre", "Physiquement impossible", "Restreint aux ayants droit", "A péage", }` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

No class, model, or dataclass is declared in this file.

## 6. Functions and methods

### `_payload`

**Signature**

```python
def _payload() -> dict[str, Any]:
```

**Purpose**

Implements payload according to the exact implementation and guards in this file.

**Inputs**

- No parameters.

**Returns**

- Declared return type: `dict[str, Any]`. Observed return expression(s): `payload`.

**Algorithm**

1. Computes `payload` from `yaml.safe_load(POLICY_PATH.read_text(encoding='utf-8'))`.
2. Asserts `isinstance(payload, dict)`.
3. Returns `payload`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `POLICY_PATH.read_text`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `POLICY_PATH.read_text`, `isinstance`, `yaml.safe_load`.

**Known repository callers**

- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_asset_state_group_overlap_is_rejected`
- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_both_evidence_references_are_required`
- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_decision_precedence_must_be_exact`
- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_duplicate_known_restriction_is_rejected`
- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_duplicate_semantic_value_is_rejected`
- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_exact_width_threshold_is_accepted`
- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_importance_domains_must_be_exact`
- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_invalid_config_structure_is_rejected`
- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_invalid_width_threshold_is_rejected`
- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_missing_known_asset_state_is_rejected`
- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_mutating_source_payload_cannot_affect_another_load`
- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_output_class_vocabulary_must_be_exact`
- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_product_reference_document_id_is_exact`
- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_semantic_groups_must_be_pairwise_disjoint`
- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_semantic_values_must_be_exact_non_empty_strings`
- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_unknown_additional_asset_state_is_rejected`
- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_unknown_evidence_reference_is_rejected`
- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_unsupported_schema_version_is_rejected`
- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_wrong_policy_identity_is_rejected`

**Tests**

- `tests/unit/test_road_vehicle_proxy_policy.py::test_asset_state_group_overlap_is_rejected`
- `tests/unit/test_road_vehicle_proxy_policy.py::test_both_evidence_references_are_required`
- `tests/unit/test_road_vehicle_proxy_policy.py::test_decision_precedence_must_be_exact`
- `tests/unit/test_road_vehicle_proxy_policy.py::test_duplicate_known_restriction_is_rejected`
- `tests/unit/test_road_vehicle_proxy_policy.py::test_duplicate_semantic_value_is_rejected`
- `tests/unit/test_road_vehicle_proxy_policy.py::test_exact_width_threshold_is_accepted`
- `tests/unit/test_road_vehicle_proxy_policy.py::test_importance_domains_must_be_exact`
- `tests/unit/test_road_vehicle_proxy_policy.py::test_invalid_config_structure_is_rejected`
- `tests/unit/test_road_vehicle_proxy_policy.py::test_invalid_width_threshold_is_rejected`
- `tests/unit/test_road_vehicle_proxy_policy.py::test_missing_known_asset_state_is_rejected`
- `tests/unit/test_road_vehicle_proxy_policy.py::test_mutating_source_payload_cannot_affect_another_load`
- `tests/unit/test_road_vehicle_proxy_policy.py::test_output_class_vocabulary_must_be_exact`
- `tests/unit/test_road_vehicle_proxy_policy.py::test_product_reference_document_id_is_exact`
- `tests/unit/test_road_vehicle_proxy_policy.py::test_semantic_groups_must_be_pairwise_disjoint`
- `tests/unit/test_road_vehicle_proxy_policy.py::test_semantic_values_must_be_exact_non_empty_strings`
- `tests/unit/test_road_vehicle_proxy_policy.py::test_unknown_additional_asset_state_is_rejected`
- `tests/unit/test_road_vehicle_proxy_policy.py::test_unknown_evidence_reference_is_rejected`
- `tests/unit/test_road_vehicle_proxy_policy.py::test_unsupported_schema_version_is_rejected`
- `tests/unit/test_road_vehicle_proxy_policy.py::test_wrong_policy_identity_is_rejected`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_write_policy`

**Signature**

```python
def _write_policy(tmp_path: Path, payload: object) -> Path:
```

**Purpose**

Writes policy according to the exact implementation and guards in this file.

**Inputs**

- `tmp_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `payload` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `Path`. Observed return expression(s): `path`.

**Algorithm**

1. Computes `path` from `tmp_path / 'policy.yaml'`.
2. Calls `path.write_text(yaml.safe_dump(payload, allow_unicode=True, sort_keys=False), encoding='utf-8')` for its validation or side effect.
3. Returns `path`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `path.write_text`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `path.write_text`, `yaml.safe_dump`.

**Known repository callers**

- `tests/unit/test_road_vehicle_proxy_policy.py` — `_load_payload`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_load_payload`

**Signature**

```python
def _load_payload(tmp_path: Path, payload: object) -> IgnRoadVehicleProxyPolicy:
```

**Purpose**

Loads payload according to the exact implementation and guards in this file.

**Inputs**

- `tmp_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `payload` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `IgnRoadVehicleProxyPolicy`. Observed return expression(s): `load_ign_road_vehicle_proxy_policy(_write_policy(tmp_path, payload))`.

**Algorithm**

1. Returns `load_ign_road_vehicle_proxy_policy(_write_policy(tmp_path, payload))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `_write_policy`, `load_ign_road_vehicle_proxy_policy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `_write_policy`, `load_ign_road_vehicle_proxy_policy`.

**Known repository callers**

- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_asset_state_group_overlap_is_rejected`
- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_both_evidence_references_are_required`
- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_decision_precedence_must_be_exact`
- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_duplicate_known_restriction_is_rejected`
- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_duplicate_semantic_value_is_rejected`
- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_exact_width_threshold_is_accepted`
- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_importance_domains_must_be_exact`
- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_invalid_config_structure_is_rejected`
- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_invalid_width_threshold_is_rejected`
- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_missing_known_asset_state_is_rejected`
- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_non_mapping_yaml_has_controlled_error`
- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_output_class_vocabulary_must_be_exact`
- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_product_reference_document_id_is_exact`
- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_semantic_groups_must_be_pairwise_disjoint`
- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_semantic_values_must_be_exact_non_empty_strings`
- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_unknown_additional_asset_state_is_rejected`
- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_unknown_evidence_reference_is_rejected`
- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_unsupported_schema_version_is_rejected`
- `tests/unit/test_road_vehicle_proxy_policy.py` — `test_wrong_policy_identity_is_rejected`

**Tests**

- `tests/unit/test_road_vehicle_proxy_policy.py::test_asset_state_group_overlap_is_rejected`
- `tests/unit/test_road_vehicle_proxy_policy.py::test_both_evidence_references_are_required`
- `tests/unit/test_road_vehicle_proxy_policy.py::test_decision_precedence_must_be_exact`
- `tests/unit/test_road_vehicle_proxy_policy.py::test_duplicate_known_restriction_is_rejected`
- `tests/unit/test_road_vehicle_proxy_policy.py::test_duplicate_semantic_value_is_rejected`
- `tests/unit/test_road_vehicle_proxy_policy.py::test_exact_width_threshold_is_accepted`
- `tests/unit/test_road_vehicle_proxy_policy.py::test_importance_domains_must_be_exact`
- `tests/unit/test_road_vehicle_proxy_policy.py::test_invalid_config_structure_is_rejected`
- `tests/unit/test_road_vehicle_proxy_policy.py::test_invalid_width_threshold_is_rejected`
- `tests/unit/test_road_vehicle_proxy_policy.py::test_missing_known_asset_state_is_rejected`
- `tests/unit/test_road_vehicle_proxy_policy.py::test_non_mapping_yaml_has_controlled_error`
- `tests/unit/test_road_vehicle_proxy_policy.py::test_output_class_vocabulary_must_be_exact`
- `tests/unit/test_road_vehicle_proxy_policy.py::test_product_reference_document_id_is_exact`
- `tests/unit/test_road_vehicle_proxy_policy.py::test_semantic_groups_must_be_pairwise_disjoint`
- `tests/unit/test_road_vehicle_proxy_policy.py::test_semantic_values_must_be_exact_non_empty_strings`
- `tests/unit/test_road_vehicle_proxy_policy.py::test_unknown_additional_asset_state_is_rejected`
- `tests/unit/test_road_vehicle_proxy_policy.py::test_unknown_evidence_reference_is_rejected`
- `tests/unit/test_road_vehicle_proxy_policy.py::test_unsupported_schema_version_is_rejected`
- `tests/unit/test_road_vehicle_proxy_policy.py::test_wrong_policy_identity_is_rejected`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_checked_in_policy_loads_with_exact_public_identity_and_reference`

**Signature**

```python
def test_checked_in_policy_loads_with_exact_public_identity_and_reference() -> None:
```

**Purpose**

Protects the `checked in policy loads with exact public identity and reference` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Computes `policy` from `load_ign_road_vehicle_proxy_policy()`.

**Action**

- Calls `load_ign_road_vehicle_proxy_policy`, `type`.

**Expected result**

- Direct assertions: `assert type(policy) is IgnRoadVehicleProxyPolicy`; `assert policy.policy_id == EXPECTED_POLICY_ID`; `assert policy.schema_version == 2`; `assert policy.scope == EXPECTED_SCOPE`; `assert policy.navigation_reference.publisher == 'IGN'`; `assert policy.navigation_reference.title == 'Calcul d’itinéraire'`; `assert policy.navigation_reference.revision == '2026-05-27'`; `assert policy.navigation_reference.evidence_scope == 'GENERAL_CAR_ROUTING_RULES'`; `assert policy.bdtopo_product_reference.publisher == 'IGN'`; `assert policy.bdtopo_product_reference.title == 'BD TOPO® Version 3.5 - Descriptif de contenu'`; `assert policy.bdtopo_product_reference.document_id == 'DC_BDTOPO_3-5'`; `assert policy.bdtopo_product_reference.revision == '2025-11'`; `assert policy.bdtopo_product_reference.evidence_scope == 'SOURCE_ATTRIBUTE_SEMANTICS'`; `assert policy.evidence_checked_on == '2026-08-16'`; `assert policy.vehicle_scope == 'LIGHT_VEHICLE_AND_GENERAL_CAR_NETWORK'`; `assert policy.heavy_vehicle_access == 'NOT_PROVEN'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `checked in policy loads with exact public identity and reference` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `load_ign_road_vehicle_proxy_policy`, `type`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_checked_in_policy_hash_binds_exact_file_bytes`

**Signature**

```python
def test_checked_in_policy_hash_binds_exact_file_bytes() -> None:
```

**Purpose**

Protects the `checked in policy hash binds exact file bytes` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Computes `policy` from `load_ign_road_vehicle_proxy_policy(POLICY_PATH)`.

**Action**

- Calls `POLICY_PATH.read_bytes`, `load_ign_road_vehicle_proxy_policy`, `policy.config_sha256.lower`, `sha256`, `sha256(POLICY_PATH.read_bytes()).hexdigest`.

**Expected result**

- Direct assertions: `assert policy.config_sha256 == sha256(POLICY_PATH.read_bytes()).hexdigest()`; `assert len(policy.config_sha256) == 64`; `assert policy.config_sha256 == policy.config_sha256.lower()`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `checked in policy hash binds exact file bytes` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `POLICY_PATH.read_bytes`, `len`, `load_ign_road_vehicle_proxy_policy`, `policy.config_sha256.lower`, `sha256`, `sha256(POLICY_PATH.read_bytes()).hexdigest`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_repeat_loading_is_deterministic_and_independent`

**Signature**

```python
def test_repeat_loading_is_deterministic_and_independent() -> None:
```

**Purpose**

Protects the `repeat loading is deterministic and independent` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `first` from `load_ign_road_vehicle_proxy_policy()`.
- Computes `second` from `load_ign_road_vehicle_proxy_policy()`.

**Action**

- Calls `load_ign_road_vehicle_proxy_policy`.

**Expected result**

- Direct assertions: `assert first == second`; `assert first is not second`; `assert first.nature is not second.nature`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `repeat loading is deterministic and independent` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `load_ign_road_vehicle_proxy_policy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_public_api_exports_only_stable_policy_symbols`

**Signature**

```python
def test_public_api_exports_only_stable_policy_symbols() -> None:
```

**Purpose**

Protects the `public api exports only stable policy symbols` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Computes `expected` from `{'IgnRoadVehicleProxyPolicy', 'IgnRoadVehicleProxyPolicyError', 'load_ign_road_vehicle_proxy_policy'}`.

**Action**

- Calls `all`, `hasattr`.

**Expected result**

- Direct assertions: `assert set(module.__all__) == expected`; `assert expected <= set(stages.__all__)`; `assert all((hasattr(stages, name) for name in expected))`; `assert not hasattr(stages, '_RoadNatureConfig')`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `public api exports only stable policy symbols` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `all`, `hasattr`, `set`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_invalid_config_structure_is_rejected`

**Signature**

```python
def test_invalid_config_structure_is_rejected(
    tmp_path: Path,
    mutation: Any,
    message: str,
) -> None:
```

**Purpose**

Protects the `invalid config structure is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `mutation`, `message`.
- Contains 2 explicit setup/context statement(s).
- Computes `payload` from `_payload()`.
- Enters managed context(s) `pytest.raises(IgnRoadVehicleProxyPolicyError, match=message)` and executes: Calls `_load_payload(tmp_path, payload)` for its validation or side effect.

**Action**

- Calls `_load_payload`, `_payload`, `mutation`, `payload.pop`, `payload.update`, `payload['references']['navigation'].update`, `payload['source_values'].pop`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnRoadVehicleProxyPolicyError, match=message): _load_payload(tmp_path, payload)`.

**Regression protected**

- Protects the exact `invalid config structure is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_load_payload`, `_payload`, `mutation`, `payload.pop`, `payload.update`, `payload['references']['navigation'].update`, `payload['source_values'].pop`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unsupported_schema_version_is_rejected`

**Signature**

```python
def test_unsupported_schema_version_is_rejected(
    tmp_path: Path, version: int
) -> None:
```

**Purpose**

Protects the `unsupported schema version is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `version`.
- Contains 3 explicit setup/context statement(s).
- Computes `payload` from `_payload()`.
- Computes `payload['schema_version']` from `version`.
- Enters managed context(s) `pytest.raises(IgnRoadVehicleProxyPolicyError)` and executes: Calls `_load_payload(tmp_path, payload)` for its validation or side effect.

**Action**

- Calls `_load_payload`, `_payload`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnRoadVehicleProxyPolicyError): _load_payload(tmp_path, payload)`.

**Regression protected**

- Protects the exact `unsupported schema version is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_load_payload`, `_payload`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_wrong_policy_identity_is_rejected`

**Signature**

```python
def test_wrong_policy_identity_is_rejected(
    tmp_path: Path,
    path: tuple[str, ...],
    value: str,
) -> None:
```

**Purpose**

Protects the `wrong policy identity is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `path`, `value`.
- Contains 4 explicit setup/context statement(s).
- Computes `payload` from `_payload()`.
- Computes `target` from `payload`.
- Computes `target[path[-1]]` from `value`.
- Enters managed context(s) `pytest.raises(IgnRoadVehicleProxyPolicyError)` and executes: Calls `_load_payload(tmp_path, payload)` for its validation or side effect.

**Action**

- Calls `_load_payload`, `_payload`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnRoadVehicleProxyPolicyError): _load_payload(tmp_path, payload)`.

**Regression protected**

- Protects the exact `wrong policy identity is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_load_payload`, `_payload`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_both_evidence_references_are_required`

**Signature**

```python
def test_both_evidence_references_are_required(
    tmp_path: Path, reference: str
) -> None:
```

**Purpose**

Protects the `both evidence references are required` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `reference`.
- Contains 2 explicit setup/context statement(s).
- Computes `payload` from `_payload()`.
- Enters managed context(s) `pytest.raises(IgnRoadVehicleProxyPolicyError)` and executes: Calls `_load_payload(tmp_path, payload)` for its validation or side effect.

**Action**

- Calls `_load_payload`, `_payload`, `payload['references'].pop`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnRoadVehicleProxyPolicyError): _load_payload(tmp_path, payload)`.

**Regression protected**

- Protects the exact `both evidence references are required` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_load_payload`, `_payload`, `payload['references'].pop`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_product_reference_document_id_is_exact`

**Signature**

```python
def test_product_reference_document_id_is_exact(tmp_path: Path) -> None:
```

**Purpose**

Protects the `product reference document id is exact` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 3 explicit setup/context statement(s).
- Computes `payload` from `_payload()`.
- Computes `payload['references']['bdtopo_product']['document_id']` from `'OTHER'`.
- Enters managed context(s) `pytest.raises(IgnRoadVehicleProxyPolicyError)` and executes: Calls `_load_payload(tmp_path, payload)` for its validation or side effect.

**Action**

- Calls `_load_payload`, `_payload`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnRoadVehicleProxyPolicyError): _load_payload(tmp_path, payload)`.

**Regression protected**

- Protects the exact `product reference document id is exact` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_load_payload`, `_payload`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unknown_evidence_reference_is_rejected`

**Signature**

```python
def test_unknown_evidence_reference_is_rejected(tmp_path: Path) -> None:
```

**Purpose**

Protects the `unknown evidence reference is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 3 explicit setup/context statement(s).
- Computes `payload` from `_payload()`.
- Computes `payload['references']['other']` from `payload['references']['navigation']`.
- Enters managed context(s) `pytest.raises(IgnRoadVehicleProxyPolicyError)` and executes: Calls `_load_payload(tmp_path, payload)` for its validation or side effect.

**Action**

- Calls `_load_payload`, `_payload`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnRoadVehicleProxyPolicyError): _load_payload(tmp_path, payload)`.

**Regression protected**

- Protects the exact `unknown evidence reference is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_load_payload`, `_payload`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_asset_state_groups_cover_exact_v2_domain`

**Signature**

```python
def test_asset_state_groups_cover_exact_v2_domain() -> None:
```

**Purpose**

Protects the `asset state groups cover exact v2 domain` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `policy` from `load_ign_road_vehicle_proxy_policy()`.
- Computes `groups` from `(policy.asset_state.in_service, policy.asset_state.project_geometry_not_significant, policy.asset_state.under_construction)`.

**Action**

- Calls `all`, `frozenset`, `load_ign_road_vehicle_proxy_policy`, `sum`.

**Expected result**

- Direct assertions: `assert policy.asset_state.in_service == frozenset({'En service'})`; `assert policy.asset_state.project_geometry_not_significant == frozenset({'En projet'})`; `assert policy.asset_state.under_construction == frozenset({'En construction'})`; `assert set().union(*groups) == {'En service', 'En projet', 'En construction'}`; `assert all((sum((value in group for group in groups)) == 1 for value in set().union(*groups)))`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `asset state groups cover exact v2 domain` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `all`, `frozenset`, `load_ign_road_vehicle_proxy_policy`, `set`, `set().union`, `sum`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_asset_state_group_overlap_is_rejected`

**Signature**

```python
def test_asset_state_group_overlap_is_rejected(tmp_path: Path) -> None:
```

**Purpose**

Protects the `asset state group overlap is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 3 explicit setup/context statement(s).
- Computes `payload` from `_payload()`.
- Computes `payload['source_values']['asset_state']['under_construction']` from `['En projet']`.
- Enters managed context(s) `pytest.raises(IgnRoadVehicleProxyPolicyError)` and executes: Calls `_load_payload(tmp_path, payload)` for its validation or side effect.

**Action**

- Calls `_load_payload`, `_payload`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnRoadVehicleProxyPolicyError): _load_payload(tmp_path, payload)`.

**Regression protected**

- Protects the exact `asset state group overlap is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_load_payload`, `_payload`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_missing_known_asset_state_is_rejected`

**Signature**

```python
def test_missing_known_asset_state_is_rejected(
    tmp_path: Path, group: str, value: str
) -> None:
```

**Purpose**

Protects the `missing known asset state is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `group`, `value`.
- Contains 2 explicit setup/context statement(s).
- Computes `payload` from `_payload()`.
- Enters managed context(s) `pytest.raises(IgnRoadVehicleProxyPolicyError)` and executes: Calls `_load_payload(tmp_path, payload)` for its validation or side effect.

**Action**

- Calls `_load_payload`, `_payload`, `payload['source_values']['asset_state'][group].remove`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnRoadVehicleProxyPolicyError): _load_payload(tmp_path, payload)`.

**Regression protected**

- Protects the exact `missing known asset state is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_load_payload`, `_payload`, `payload['source_values']['asset_state'][group].remove`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unknown_additional_asset_state_is_rejected`

**Signature**

```python
def test_unknown_additional_asset_state_is_rejected(tmp_path: Path) -> None:
```

**Purpose**

Protects the `unknown additional asset state is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 2 explicit setup/context statement(s).
- Computes `payload` from `_payload()`.
- Enters managed context(s) `pytest.raises(IgnRoadVehicleProxyPolicyError)` and executes: Calls `_load_payload(tmp_path, payload)` for its validation or side effect.

**Action**

- Calls `_load_payload`, `_payload`, `payload['source_values']['asset_state']['in_service'].append`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnRoadVehicleProxyPolicyError): _load_payload(tmp_path, payload)`.

**Regression protected**

- Protects the exact `unknown additional asset state is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_load_payload`, `_payload`, `payload['source_values']['asset_state']['in_service'].append`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_semantic_values_must_be_exact_non_empty_strings`

**Signature**

```python
def test_semantic_values_must_be_exact_non_empty_strings(
    tmp_path: Path, value: str
) -> None:
```

**Purpose**

Protects the `semantic values must be exact non empty strings` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `value`.
- Contains 3 explicit setup/context statement(s).
- Computes `payload` from `_payload()`.
- Computes `payload['source_values']['light_vehicle_access']['open']` from `[value]`.
- Enters managed context(s) `pytest.raises(IgnRoadVehicleProxyPolicyError)` and executes: Calls `_load_payload(tmp_path, payload)` for its validation or side effect.

**Action**

- Calls `_load_payload`, `_payload`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnRoadVehicleProxyPolicyError): _load_payload(tmp_path, payload)`.

**Regression protected**

- Protects the exact `semantic values must be exact non empty strings` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_load_payload`, `_payload`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_duplicate_semantic_value_is_rejected`

**Signature**

```python
def test_duplicate_semantic_value_is_rejected(tmp_path: Path) -> None:
```

**Purpose**

Protects the `duplicate semantic value is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 3 explicit setup/context statement(s).
- Computes `payload` from `_payload()`.
- Computes `payload['source_values']['light_vehicle_access']['open']` from `['Libre', 'Libre']`.
- Enters managed context(s) `pytest.raises(IgnRoadVehicleProxyPolicyError, match='invalid')` and executes: Calls `_load_payload(tmp_path, payload)` for its validation or side effect.

**Action**

- Calls `_load_payload`, `_payload`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnRoadVehicleProxyPolicyError, match='invalid'): _load_payload(tmp_path, payload)`.

**Regression protected**

- Protects the exact `duplicate semantic value is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_load_payload`, `_payload`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_semantic_groups_must_be_pairwise_disjoint`

**Signature**

```python
def test_semantic_groups_must_be_pairwise_disjoint(
    tmp_path: Path,
    group: str,
    source_group: str,
    target_group: str,
) -> None:
```

**Purpose**

Protects the `semantic groups must be pairwise disjoint` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `group`, `source_group`, `target_group`.
- Contains 3 explicit setup/context statement(s).
- Computes `payload` from `_payload()`.
- Computes `value` from `payload['source_values'][group][source_group][0]`.
- Enters managed context(s) `pytest.raises(IgnRoadVehicleProxyPolicyError, match='invalid')` and executes: Calls `_load_payload(tmp_path, payload)` for its validation or side effect.

**Action**

- Calls `_load_payload`, `_payload`, `payload['source_values'][group][target_group].append`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnRoadVehicleProxyPolicyError, match='invalid'): _load_payload(tmp_path, payload)`.

**Regression protected**

- Protects the exact `semantic groups must be pairwise disjoint` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_load_payload`, `_payload`, `payload['source_values'][group][target_group].append`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_duplicate_known_restriction_is_rejected`

**Signature**

```python
def test_duplicate_known_restriction_is_rejected(tmp_path: Path) -> None:
```

**Purpose**

Protects the `duplicate known restriction is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 3 explicit setup/context statement(s).
- Computes `payload` from `_payload()`.
- Computes `restrictions` from `payload['source_values']['known_restriction_review']`.
- Enters managed context(s) `pytest.raises(IgnRoadVehicleProxyPolicyError)` and executes: Calls `_load_payload(tmp_path, payload)` for its validation or side effect.

**Action**

- Calls `_load_payload`, `_payload`, `restrictions.append`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnRoadVehicleProxyPolicyError): _load_payload(tmp_path, payload)`.

**Regression protected**

- Protects the exact `duplicate known restriction is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_load_payload`, `_payload`, `pytest.raises`, `restrictions.append`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_invalid_width_threshold_is_rejected`

**Signature**

```python
def test_invalid_width_threshold_is_rejected(tmp_path: Path, value: object) -> None:
```

**Purpose**

Protects the `invalid width threshold is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `value`.
- Contains 3 explicit setup/context statement(s).
- Computes `payload` from `_payload()`.
- Computes `payload['source_values']['width_below_m']` from `value`.
- Enters managed context(s) `pytest.raises(IgnRoadVehicleProxyPolicyError)` and executes: Calls `_load_payload(tmp_path, payload)` for its validation or side effect.

**Action**

- Calls `_load_payload`, `_payload`, `float`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnRoadVehicleProxyPolicyError): _load_payload(tmp_path, payload)`.

**Regression protected**

- Protects the exact `invalid width threshold is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_load_payload`, `_payload`, `float`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_exact_width_threshold_is_accepted`

**Signature**

```python
def test_exact_width_threshold_is_accepted(tmp_path: Path) -> None:
```

**Purpose**

Protects the `exact width threshold is accepted` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 2 explicit setup/context statement(s).
- Computes `payload` from `_payload()`.
- Computes `payload['source_values']['width_below_m']` from `2.9`.

**Action**

- Calls `_load_payload`, `_payload`.

**Expected result**

- Direct assertions: `assert _load_payload(tmp_path, payload).width_below_m == 2.9`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `exact width threshold is accepted` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_load_payload`, `_payload`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_importance_domains_must_be_exact`

**Signature**

```python
def test_importance_domains_must_be_exact(
    tmp_path: Path, group: str, mutation: str
) -> None:
```

**Purpose**

Protects the `importance domains must be exact` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `group`, `mutation`.
- Contains 3 explicit setup/context statement(s).
- Computes `payload` from `_payload()`.
- Computes `importance` from `payload['source_values']['importance']`.
- Enters managed context(s) `pytest.raises(IgnRoadVehicleProxyPolicyError)` and executes: Calls `_load_payload(tmp_path, payload)` for its validation or side effect.

**Action**

- Calls `_load_payload`, `_payload`, `importance[group].append`, `importance[group].remove`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnRoadVehicleProxyPolicyError): _load_payload(tmp_path, payload)`.

**Regression protected**

- Protects the exact `importance domains must be exact` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_load_payload`, `_payload`, `importance[group].append`, `importance[group].remove`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_importance_domains_expose_known_without_positive_classification`

**Signature**

```python
def test_importance_domains_expose_known_without_positive_classification() -> None:
```

**Purpose**

Protects the `importance domains expose known without positive classification` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Computes `policy` from `load_ign_road_vehicle_proxy_policy()`.

**Action**

- Calls `frozenset`, `load_ign_road_vehicle_proxy_policy`.

**Expected result**

- Direct assertions: `assert policy.importance.known == frozenset({'1', '2', '3', '4', '5', '6'})`; `assert policy.importance.limited == frozenset({'6'})`; `assert policy.importance.limited <= policy.importance.known`; `assert '7' not in policy.importance.known`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `importance domains expose known without positive classification` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `frozenset`, `load_ign_road_vehicle_proxy_policy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_decision_precedence_must_be_exact`

**Signature**

```python
def test_decision_precedence_must_be_exact(
    tmp_path: Path, mutation: str
) -> None:
```

**Purpose**

Protects the `decision precedence must be exact` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `mutation`.
- Contains 3 explicit setup/context statement(s).
- Computes `payload` from `_payload()`.
- Computes `precedence` from `payload['decision_precedence']`.
- Enters managed context(s) `pytest.raises(IgnRoadVehicleProxyPolicyError)` and executes: Calls `_load_payload(tmp_path, payload)` for its validation or side effect.

**Action**

- Calls `_load_payload`, `_payload`, `precedence.append`, `precedence.pop`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnRoadVehicleProxyPolicyError): _load_payload(tmp_path, payload)`.

**Regression protected**

- Protects the exact `decision precedence must be exact` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_load_payload`, `_payload`, `precedence.append`, `precedence.pop`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_decision_precedence_and_rule_outcomes_are_approved`

**Signature**

```python
def test_decision_precedence_and_rule_outcomes_are_approved() -> None:
```

**Purpose**

Protects the `decision precedence and rule outcomes are approved` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Computes `policy` from `load_ign_road_vehicle_proxy_policy()`.

**Action**

- Calls `load_ign_road_vehicle_proxy_policy`.

**Expected result**

- Direct assertions: `assert policy.decision_precedence == EXPECTED_PRECEDENCE`; `assert policy.decision_outcomes.fictitious_geometry == 'NOT_DISTANCE_PROXY'`; `assert policy.decision_outcomes.project_geometry_not_significant == 'NOT_DISTANCE_PROXY'`; `assert policy.decision_outcomes.not_in_service == 'NOT_GENERAL_VEHICLE_PROXY'`; `assert policy.decision_outcomes.private_road == 'RESTRICTED_REVIEW'`; `assert policy.decision_outcomes.rights_restricted == 'RESTRICTED_REVIEW'`; `assert policy.decision_outcomes.temporal_closure == 'RESTRICTED_REVIEW'`; `assert policy.decision_outcomes.physically_impossible == 'NOT_GENERAL_VEHICLE_PROXY'`; `assert policy.decision_outcomes.limited_nature == 'LIMITED_VEHICLE_PROXY'`; `assert policy.decision_outcomes.open_or_toll == 'GENERAL_VEHICLE_PROXY'`; `assert policy.decision_outcomes.unknown == 'UNKNOWN_REVIEW'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `decision precedence and rule outcomes are approved` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `load_ign_road_vehicle_proxy_policy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_project_geometry_rule_has_exact_precedence_position`

**Signature**

```python
def test_project_geometry_rule_has_exact_precedence_position() -> None:
```

**Purpose**

Protects the `project geometry rule has exact precedence position` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `policy` from `load_ign_road_vehicle_proxy_policy()`.
- Computes `fictitious` from `policy.decision_precedence.index('FICTITIOUS_GEOMETRY')`.
- Computes `project` from `policy.decision_precedence.index('PROJECT_GEOMETRY_NOT_SIGNIFICANT')`.
- Computes `not_in_service` from `policy.decision_precedence.index('NOT_IN_SERVICE')`.

**Action**

- Calls `load_ign_road_vehicle_proxy_policy`, `policy.decision_precedence.index`.

**Expected result**

- Direct assertions: `assert fictitious < project < not_in_service`; `assert len(policy.decision_precedence) == 16`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `project geometry rule has exact precedence position` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `len`, `load_ign_road_vehicle_proxy_policy`, `policy.decision_precedence.index`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_output_class_vocabulary_must_be_exact`

**Signature**

```python
def test_output_class_vocabulary_must_be_exact(
    tmp_path: Path, mutation: str
) -> None:
```

**Purpose**

Protects the `output class vocabulary must be exact` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `mutation`.
- Contains 3 explicit setup/context statement(s).
- Computes `payload` from `_payload()`.
- Computes `classes` from `payload['classes']`.
- Enters managed context(s) `pytest.raises(IgnRoadVehicleProxyPolicyError)` and executes: Calls `_load_payload(tmp_path, payload)` for its validation or side effect.

**Action**

- Calls `_load_payload`, `_payload`, `classes.pop`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnRoadVehicleProxyPolicyError): _load_payload(tmp_path, payload)`.

**Regression protected**

- Protects the exact `output class vocabulary must be exact` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_load_payload`, `_payload`, `classes.pop`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_approved_class_vocabulary_has_no_heavy_or_legal_claim`

**Signature**

```python
def test_approved_class_vocabulary_has_no_heavy_or_legal_claim() -> None:
```

**Purpose**

Protects the `approved class vocabulary has no heavy or legal claim` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `policy` from `load_ign_road_vehicle_proxy_policy()`.
- Computes `forbidden` from `('TRUCK', 'HEAVY', 'LEGAL', 'APPROVED', 'BESS_ACCESSIBLE', 'AUTHORIZED')`.

**Action**

- Calls `all`, `load_ign_road_vehicle_proxy_policy`.

**Expected result**

- Direct assertions: `assert policy.classes.values == EXPECTED_CLASSES`; `assert policy.heavy_vehicle_access == 'NOT_PROVEN'`; `assert all((token not in value for value in policy.classes.values for token in forbidden))`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `approved class vocabulary has no heavy or legal claim` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `all`, `load_ign_road_vehicle_proxy_policy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_observed_d031_natures_are_covered_exactly_once`

**Signature**

```python
def test_observed_d031_natures_are_covered_exactly_once() -> None:
```

**Purpose**

Protects the `observed d031 natures are covered exactly once` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `policy` from `load_ign_road_vehicle_proxy_policy()`.
- Computes `groups` from `(policy.nature.general_motor_road, policy.nature.limited_motor_proxy, policy.nature.non_general_vehicle, policy.nature.special_review)`.

**Action**

- Calls `all`, `load_ign_road_vehicle_proxy_policy`, `sum`.

**Expected result**

- Direct assertions: `assert set().union(*groups) >= OBSERVED_NATURES`; `assert all((sum((value in group for group in groups)) == 1 for value in OBSERVED_NATURES))`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `observed d031 natures are covered exactly once` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `all`, `load_ign_road_vehicle_proxy_policy`, `set`, `set().union`, `sum`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_observed_d031_access_and_importance_vocabularies_are_compatible`

**Signature**

```python
def test_observed_d031_access_and_importance_vocabularies_are_compatible() -> None:
```

**Purpose**

Protects the `observed d031 access and importance vocabularies are compatible` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `policy` from `load_ign_road_vehicle_proxy_policy()`.
- Computes `access_groups` from `(policy.light_vehicle_access.open, policy.light_vehicle_access.toll, policy.light_vehicle_access.rights_restricted, policy.light_vehicle_access.physically_impossible)`.

**Action**

- Calls `frozenset`, `load_ign_road_vehicle_proxy_policy`.

**Expected result**

- Direct assertions: `assert set().union(*access_groups) == OBSERVED_LIGHT_VEHICLE_ACCESS`; `assert policy.importance.known == frozenset({'1', '2', '3', '4', '5', '6'})`; `assert policy.importance.limited == frozenset({'6'})`; `assert policy.decision_outcomes.unknown == 'UNKNOWN_REVIEW'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `observed d031 access and importance vocabularies are compatible` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `frozenset`, `load_ign_road_vehicle_proxy_policy`, `set`, `set().union`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_compiled_policy_structures_are_immutable`

**Signature**

```python
def test_compiled_policy_structures_are_immutable() -> None:
```

**Purpose**

Protects the `compiled policy structures are immutable` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `policy` from `load_ign_road_vehicle_proxy_policy()`.
- Enters managed context(s) `pytest.raises(FrozenInstanceError)` and executes: Computes `policy.scope` from `'changed'`.
- Enters managed context(s) `pytest.raises(AttributeError)` and executes: Calls `policy.nature.general_motor_road.add('Invented')` for its validation or side effect.

**Action**

- Calls `load_ign_road_vehicle_proxy_policy`, `policy.nature.general_motor_road.add`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(FrozenInstanceError): policy.scope = 'changed'`; `with pytest.raises(AttributeError): policy.nature.general_motor_road.add('Invented')`.

**Regression protected**

- Protects the exact `compiled policy structures are immutable` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `load_ign_road_vehicle_proxy_policy`, `policy.nature.general_motor_road.add`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_mutating_source_payload_cannot_affect_another_load`

**Signature**

```python
def test_mutating_source_payload_cannot_affect_another_load() -> None:
```

**Purpose**

Protects the `mutating source payload cannot affect another load` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `first` from `load_ign_road_vehicle_proxy_policy()`.
- Computes `mutable` from `_payload()`.
- Computes `second` from `load_ign_road_vehicle_proxy_policy()`.

**Action**

- Calls `_payload`, `load_ign_road_vehicle_proxy_policy`, `mutable['source_values']['nature']['general_motor_road'].append`.

**Expected result**

- Direct assertions: `assert first == second`; `assert 'Invented' not in second.nature.general_motor_road`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `mutating source payload cannot affect another load` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_payload`, `load_ign_road_vehicle_proxy_policy`, `mutable['source_values']['nature']['general_motor_road'].append`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_malformed_yaml_has_controlled_error`

**Signature**

```python
def test_malformed_yaml_has_controlled_error(tmp_path: Path) -> None:
```

**Purpose**

Protects the `malformed yaml has controlled error` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 2 explicit setup/context statement(s).
- Computes `path` from `tmp_path / 'malformed.yaml'`.
- Enters managed context(s) `pytest.raises(IgnRoadVehicleProxyPolicyError)` and executes: Calls `load_ign_road_vehicle_proxy_policy(path)` for its validation or side effect.

**Action**

- Calls `load_ign_road_vehicle_proxy_policy`, `path.write_text`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnRoadVehicleProxyPolicyError): load_ign_road_vehicle_proxy_policy(path)`.

**Regression protected**

- Protects the exact `malformed yaml has controlled error` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `load_ign_road_vehicle_proxy_policy`, `path.write_text`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_non_mapping_yaml_has_controlled_error`

**Signature**

```python
def test_non_mapping_yaml_has_controlled_error(
    tmp_path: Path, payload: object
) -> None:
```

**Purpose**

Protects the `non mapping yaml has controlled error` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `payload`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(IgnRoadVehicleProxyPolicyError)` and executes: Calls `_load_payload(tmp_path, payload)` for its validation or side effect.

**Action**

- Calls `_load_payload`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnRoadVehicleProxyPolicyError): _load_payload(tmp_path, payload)`.

**Regression protected**

- Protects the exact `non mapping yaml has controlled error` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_load_payload`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_missing_file_has_controlled_error`

**Signature**

```python
def test_missing_file_has_controlled_error(tmp_path: Path) -> None:
```

**Purpose**

Protects the `missing file has controlled error` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(IgnRoadVehicleProxyPolicyError)` and executes: Calls `load_ign_road_vehicle_proxy_policy(tmp_path / 'missing.yaml')` for its validation or side effect.

**Action**

- Calls `load_ign_road_vehicle_proxy_policy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnRoadVehicleProxyPolicyError): load_ign_road_vehicle_proxy_policy(tmp_path / 'missing.yaml')`.

**Regression protected**

- Protects the exact `missing file has controlled error` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `load_ign_road_vehicle_proxy_policy`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `asset_state` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `authorized` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bdtopo_product` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `classes` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `decision_precedence` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `document_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `general_motor_road` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `general_vehicle_proxy` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `importance` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `in_service` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `known_restriction_review` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `light_vehicle_access` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `nature` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `navigation` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `open` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `other` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `references` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `schema_version` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_values` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `under_construction` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `width_below_m` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | linear distance/length in metres; proxy meaning is limited by the introducing stage. Consumers and exact calculations are the functions that reference this column above. |

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

This file contributes to LandScout's `test` evidence flow as described by its purpose and public symbols. It preserves the distinction among fact, proxy evidence, policy interpretation, diagnostic status, and parcel precheck.

## 15. Explicit non-goals

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

## 16. Tests

Direct name-resolved tests appear under each symbol. Higher-level tests may exercise private helpers through a public source-complete function; companion documents for all test files describe their fixtures, actions, assertions, and boundaries.

## 17. Change impact

Changing this file requires reviewing its static callers, package exports, directly mapped tests, relevant schema/hash/version constants, source locks, persisted artifact contracts, and the corresponding pipeline/cross-cutting documents. Any byte change makes the SHA256 above stale and requires regenerating this companion.

# `tests/unit/test_apply_road_vehicle_proxy_policy.py`

## File identity

- Repository path: `tests/unit/test_apply_road_vehicle_proxy_policy.py`
- File type: Python test
- Primary responsibility: Provides complete unit and regression coverage for the `apply_road_vehicle_proxy_policy` contracts exercised in this file.
- Layer / domain: `unit/regression test` / `test`
- Public or internal role: Internal test support; not a production API.
- Source SHA256: `eaa1d3944b656e8202719eb65bfe202e663d6803e47172a51d8b7dadf3b268ad`

## 1. Purpose

Provides complete unit and regression coverage for the `apply_road_vehicle_proxy_policy` contracts exercised in this file.

## 2. Position in LandScout architecture

This file is a `unit/regression test` artifact in the `test` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from __future__ import annotations` — required by the implementation paths and symbols documented below.
- `from copy import deepcopy` — required by the implementation paths and symbols documented below.
- `from dataclasses import FrozenInstanceError` — required by the implementation paths and symbols documented below.
- `from pathlib import Path` — required by the implementation paths and symbols documented below.
- `from typing import Any, cast` — required by the implementation paths and symbols documented below.

### Third-party

- `from unittest.mock import patch` — required by the implementation paths and symbols documented below.
- `import geopandas as gpd` — required by the implementation paths and symbols documented below.
- `import numpy as np` — required by the implementation paths and symbols documented below.
- `import pandas as pd` — required by the implementation paths and symbols documented below.
- `import pytest` — required by the implementation paths and symbols documented below.
- `from geopandas.testing import assert_geodataframe_equal` — required by the implementation paths and symbols documented below.
- `from shapely.geometry import LineString, Polygon` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout import stages` — required by the implementation paths and symbols documented below.
- `from landscout.sources.ign_bdtopo_fr import ( IgnBdTopoRoadData, IgnBdTopoSourceConfig, load_ign_bdtopo_source_config, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.apply_road_vehicle_proxy_policy import ( IgnRoadVehicleProxyApplicationError, IgnRoadVehicleProxyApplicationResult, apply_ign_road_vehicle_proxy_policy, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.normalize_access_ign import ( IgnRoadNormalizationError, NormalizedIgnRoadData, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.road_vehicle_proxy_policy import ( load_ign_road_vehicle_proxy_policy, )` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `SOURCE_CONFIG` | `load_ign_bdtopo_source_config()` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `POLICY_PATH` | `Path("configs/access/ign_bdtopo_vehicle_proxy_policy.yaml")` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `POLICY_COLUMNS` | `( "road_proxy_primary_rule", "road_proxy_class", "road_proxy_rule_trace_json", "road_proxy_unknown_fields_json", "road_proxy_toll_evidence", "road_proxy_policy_id", "road_proxy_policy_schema_version", "road_proxy_policy_config_sha256", "road_proxy_policy_scope", "road_proxy_policy_evidence_checked_on", "road_proxy_vehicle_scope", "road_proxy_heavy_vehicle_access", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

### `test_source_config_is_exact_pydantic_type.ConfigSubclass`

**Purpose:** Represents checked-in or resolved configuration fields and validates their exact domain before use.

**Inheritance:** `IgnBdTopoSourceConfig`.

**Model form and mutability:** class inheriting from `IgnBdTopoSourceConfig`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

## 6. Functions and methods

### `_base_row`

**Signature**

```python
def _base_row(number: int = 1) -> dict[str, object]:
```

**Purpose**

Implements base row according to the exact implementation and guards in this file.

**Inputs**

- `number` (`int`; optional/default `1`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[str, object]`. Observed return expression(s): `{'road_feature_id': f'IGN_BDTOPO:ROAD_SEGMENT:ROAD-{number}', 'road_feature_type': 'ROAD_SEGMENT', 'source_provider': 'IGN', 'source_product': 'BD_TOPO', 'source_layer': 'troncon_de_route', 'source_feature_id': f'ROAD-{number}', 'source_department_code': '31', 'source_edition': '2026-06-15', 'source_product_version': '3.5', 'source_download_timestamp': '2026-08-11T15:32:03+00:00', 'source_archive…`.

**Algorithm**

1. Returns `{'road_feature_id': f'IGN_BDTOPO:ROAD_SEGMENT:ROAD-{number}', 'road_feature_type': 'ROAD_SEGMENT', 'source_provider': 'IGN', 'source_product': 'BD_TOPO', 'source_layer': 'troncon_de_route', 'source_feature_id': f'ROAD-{number}', 'source_department_code': '31', 'source_edition': '2026-06-15', 'source_product_version': '3.5', 'source_download_timestamp': '202…`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `LineString`.

**Known repository callers**

- `tests/unit/test_apply_road_vehicle_proxy_policy.py` — `_roads`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_roads`

**Signature**

```python
def _roads(*overrides: dict[str, object]) -> gpd.GeoDataFrame:
```

**Purpose**

Implements roads according to the exact implementation and guards in this file.

**Inputs**

- `*overrides` (`dict[str, object]`; required) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `gpd.GeoDataFrame(rows, geometry='geometry', crs='EPSG:2154')`.

**Algorithm**

1. Computes `mutations` from `overrides or ({},)`.
2. Defines `rows` with annotation `list[dict[str, object]]` from `[]`.
3. Iterates `(number, mutation)` over `enumerate(mutations, start=1)`. For each value: Computes `row` from `_base_row(number)`. Calls `row.update(mutation)` for its validation or side effect. Calls `rows.append(row)` for its validation or side effect.
4. Returns `gpd.GeoDataFrame(rows, geometry='geometry', crs='EPSG:2154')`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_base_row`, `enumerate`, `gpd.GeoDataFrame`, `row.update`, `rows.append`.

**Known repository callers**

- `tests/unit/test_apply_road_vehicle_proxy_policy.py` — `_row`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py` — `_source`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py` — `test_malformed_policy_path_has_controlled_error`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py` — `test_normalized_facts_rows_index_crs_and_geometry_are_preserved`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py` — `test_policy_lineage_is_exact_on_every_row`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py` — `test_result_is_frozen_and_contains_no_unsafe_claim_vocabulary`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py` — `test_source_complete_normalization_is_invoked_exactly_once`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py` — `test_source_object_is_not_mutated`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py` — `test_unknown_geometry_status_is_rejected`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py` — `test_valid_geometry_status_with_unsupported_geometry_is_not_repaired`

**Tests**

- `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_malformed_policy_path_has_controlled_error`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_normalized_facts_rows_index_crs_and_geometry_are_preserved`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_policy_lineage_is_exact_on_every_row`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_result_is_frozen_and_contains_no_unsafe_claim_vocabulary`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_source_complete_normalization_is_invoked_exactly_once`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_source_object_is_not_mutated`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_unknown_geometry_status_is_rejected`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_valid_geometry_status_with_unsupported_geometry_is_not_repaired`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_source`

**Signature**

```python
def _source() -> IgnBdTopoRoadData:
```

**Purpose**

Implements source according to the exact implementation and guards in this file.

**Inputs**

- No parameters.

**Returns**

- Declared return type: `IgnBdTopoRoadData`. Observed return expression(s): `IgnBdTopoRoadData(extraction=cast(Any, None), road_segments=_roads(), road_segments_summary=cast(Any, None))`.

**Algorithm**

1. Returns `IgnBdTopoRoadData(extraction=cast(Any, None), road_segments=_roads(), road_segments_summary=cast(Any, None))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `IgnBdTopoRoadData`, `_roads`, `cast`.

**Known repository callers**

- `tests/unit/test_apply_road_vehicle_proxy_policy.py` — `_apply`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py` — `test_malformed_policy_path_has_controlled_error`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py` — `test_normalization_failure_stops_policy_loading`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py` — `test_policy_path_must_be_path_or_none`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py` — `test_source_complete_normalization_is_invoked_exactly_once`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py` — `test_source_config_is_exact_pydantic_type`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py` — `test_source_object_is_not_mutated`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py` — `test_valid_geometry_status_with_unsupported_geometry_is_not_repaired`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py` — `test_wrong_source_config_type_has_controlled_error`

**Tests**

- `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_malformed_policy_path_has_controlled_error`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_normalization_failure_stops_policy_loading`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_policy_path_must_be_path_or_none`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_source_complete_normalization_is_invoked_exactly_once`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_source_config_is_exact_pydantic_type`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_source_object_is_not_mutated`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_valid_geometry_status_with_unsupported_geometry_is_not_repaired`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_wrong_source_config_type_has_controlled_error`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_apply`

**Signature**

```python
def _apply(
    roads: gpd.GeoDataFrame,
    *,
    policy_path: Path | None = None,
) -> IgnRoadVehicleProxyApplicationResult:
```

**Purpose**

Applies apply according to the exact implementation and guards in this file.

**Inputs**

- `roads` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy_path` (`Path | None`; optional/default `None`) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `IgnRoadVehicleProxyApplicationResult`. Observed return expression(s): `apply_ign_road_vehicle_proxy_policy(_source(), SOURCE_CONFIG, policy_path)`.

**Algorithm**

1. Computes `normalized` from `NormalizedIgnRoadData(road_segments=roads)`.
2. Enters managed context(s) `patch('landscout.stages.apply_road_vehicle_proxy_policy.normalize_ign_roads', return_value=normalized)` and executes: Returns `apply_ign_road_vehicle_proxy_policy(_source(), SOURCE_CONFIG, policy_path)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `NormalizedIgnRoadData`, `_source`, `apply_ign_road_vehicle_proxy_policy`, `patch`.

**Known repository callers**

- `tests/unit/test_apply_road_vehicle_proxy_policy.py` — `_row`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py` — `test_normalized_facts_rows_index_crs_and_geometry_are_preserved`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py` — `test_policy_lineage_is_exact_on_every_row`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py` — `test_result_is_frozen_and_contains_no_unsafe_claim_vocabulary`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py` — `test_unknown_geometry_status_is_rejected`

**Tests**

- `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_normalized_facts_rows_index_crs_and_geometry_are_preserved`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_policy_lineage_is_exact_on_every_row`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_result_is_frozen_and_contains_no_unsafe_claim_vocabulary`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_unknown_geometry_status_is_rejected`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_row`

**Signature**

```python
def _row(
    overrides: dict[str, object] | None = None,
) -> pd.Series:
```

**Purpose**

Implements row according to the exact implementation and guards in this file.

**Inputs**

- `overrides` (`dict[str, object] | None`; optional/default `None`) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.Series`. Observed return expression(s): `result.roads.iloc[0]`.

**Algorithm**

1. Computes `result` from `_apply(_roads(overrides or {}))`.
2. Returns `result.roads.iloc[0]`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_apply`, `_roads`.

**Known repository callers**

- `tests/unit/test_apply_road_vehicle_proxy_policy.py` — `test_boolean_like_source_values_are_parsed_without_coercion`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py` — `test_each_policy_rule_selects_approved_outcome`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py` — `test_every_configured_known_restriction_is_applied`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py` — `test_general_fallback_requires_complete_positive_evidence_and_tracks_toll`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py` — `test_known_higher_rule_remains_primary_while_unknown_is_traced`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py` — `test_non_valid_geometry_uses_technical_gate`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py` — `test_open_access_does_not_hide_unresolved_evidence`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py` — `test_optional_restriction_source_contract`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py` — `test_policy_precedence_conflicts_select_first_rule`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py` — `test_trace_is_complete_unique_and_in_policy_order`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py` — `test_unknown_critical_vocabulary_never_uses_general_fallback`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py` — `test_unknown_fields_trace_is_fixed_and_deterministic`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py` — `test_width_contract`

**Tests**

- `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_boolean_like_source_values_are_parsed_without_coercion`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_each_policy_rule_selects_approved_outcome`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_every_configured_known_restriction_is_applied`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_general_fallback_requires_complete_positive_evidence_and_tracks_toll`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_known_higher_rule_remains_primary_while_unknown_is_traced`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_non_valid_geometry_uses_technical_gate`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_open_access_does_not_hide_unresolved_evidence`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_optional_restriction_source_contract`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_policy_precedence_conflicts_select_first_rule`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_trace_is_complete_unique_and_in_policy_order`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_unknown_critical_vocabulary_never_uses_general_fallback`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_unknown_fields_trace_is_fixed_and_deterministic`
- `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_width_contract`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_public_api_exports_only_stable_application_symbols`

**Signature**

```python
def test_public_api_exports_only_stable_application_symbols() -> None:
```

**Purpose**

Protects the `public api exports only stable application symbols` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Computes `expected` from `{'IgnRoadVehicleProxyApplicationError', 'IgnRoadVehicleProxyApplicationResult', 'apply_ign_road_vehicle_proxy_policy'}`.

**Action**

- Calls `all`, `hasattr`.

**Expected result**

- Direct assertions: `assert set(module.__all__) == expected`; `assert expected <= set(stages.__all__)`; `assert all((hasattr(stages, symbol) for symbol in expected))`; `assert not hasattr(stages, '_classify_road_frame')`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `public api exports only stable application symbols` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `all`, `hasattr`, `set`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_wrong_source_type_has_controlled_error`

**Signature**

```python
def test_wrong_source_type_has_controlled_error() -> None:
```

**Purpose**

Protects the `wrong source type has controlled error` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(IgnRoadVehicleProxyApplicationError)` and executes: Calls `apply_ign_road_vehicle_proxy_policy(cast(Any, object()), SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `apply_ign_road_vehicle_proxy_policy`, `cast`, `object`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnRoadVehicleProxyApplicationError): apply_ign_road_vehicle_proxy_policy(cast(Any, object()), SOURCE_CONFIG)`.

**Regression protected**

- Protects the exact `wrong source type has controlled error` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `apply_ign_road_vehicle_proxy_policy`, `cast`, `object`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_wrong_source_config_type_has_controlled_error`

**Signature**

```python
def test_wrong_source_config_type_has_controlled_error() -> None:
```

**Purpose**

Protects the `wrong source config type has controlled error` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(IgnRoadVehicleProxyApplicationError)` and executes: Calls `apply_ign_road_vehicle_proxy_policy(_source(), cast(Any, object()))` for its validation or side effect.

**Action**

- Calls `_source`, `apply_ign_road_vehicle_proxy_policy`, `cast`, `object`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnRoadVehicleProxyApplicationError): apply_ign_road_vehicle_proxy_policy(_source(), cast(Any, object()))`.

**Regression protected**

- Protects the exact `wrong source config type has controlled error` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source`, `apply_ign_road_vehicle_proxy_policy`, `cast`, `object`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_malformed_policy_path_has_controlled_error`

**Signature**

```python
def test_malformed_policy_path_has_controlled_error(tmp_path: Path) -> None:
```

**Purpose**

Protects the `malformed policy path has controlled error` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 2 explicit setup/context statement(s).
- Computes `path` from `tmp_path / 'policy.yaml'`.
- Enters managed context(s) `patch('landscout.stages.apply_road_vehicle_proxy_policy.normalize_ign_roads', return_value=NormalizedIgnRoadData(_roads())), pytest.raises(IgnRoadVehicleProxyApplicationError)` and executes: Calls `apply_ign_road_vehicle_proxy_policy(_source(), SOURCE_CONFIG, path)` for its validation or side effect.

**Action**

- Calls `NormalizedIgnRoadData`, `_roads`, `_source`, `apply_ign_road_vehicle_proxy_policy`, `path.write_text`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with patch('landscout.stages.apply_road_vehicle_proxy_policy.normalize_ign_roads', return_value=NormalizedIgnRoadData(_roads())), pytest.raises(IgnRoadVehicleProxyApplicationError): apply_ign_road_vehicle_proxy_policy(_source(), SOURCE_CONFIG, path)`.

**Regression protected**

- Protects the exact `malformed policy path has controlled error` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `NormalizedIgnRoadData`, `_roads`, `_source`, `apply_ign_road_vehicle_proxy_policy`, `patch`, `path.write_text`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_complete_normalization_is_invoked_exactly_once`

**Signature**

```python
def test_source_complete_normalization_is_invoked_exactly_once() -> None:
```

**Purpose**

Protects the `source complete normalization is invoked exactly once` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `normalized` from `NormalizedIgnRoadData(_roads())`.
- Enters managed context(s) `patch('landscout.stages.apply_road_vehicle_proxy_policy.normalize_ign_roads', return_value=normalized)` and executes: Calls `apply_ign_road_vehicle_proxy_policy(_source(), SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `NormalizedIgnRoadData`, `_roads`, `_source`, `apply_ign_road_vehicle_proxy_policy`, `validator.assert_called_once`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `source complete normalization is invoked exactly once` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `NormalizedIgnRoadData`, `_roads`, `_source`, `apply_ign_road_vehicle_proxy_policy`, `patch`, `validator.assert_called_once`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_normalization_failure_stops_policy_loading`

**Signature**

```python
def test_normalization_failure_stops_policy_loading() -> None:
```

**Purpose**

Protects the `normalization failure stops policy loading` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `patch('landscout.stages.apply_road_vehicle_proxy_policy.normalize_ign_roads', side_effect=IgnRoadNormalizationError('bad source')), patch('landscout.stages.apply_road_vehicle_proxy_policy.load_ign_road_vehicle_proxy_policy'), pytest.raises(IgnRoadVehicleProxyApplicationError)` and executes: Calls `apply_ign_road_vehicle_proxy_policy(_source(), SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `IgnRoadNormalizationError`, `_source`, `apply_ign_road_vehicle_proxy_policy`, `policy_loader.assert_not_called`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with patch('landscout.stages.apply_road_vehicle_proxy_policy.normalize_ign_roads', side_effect=IgnRoadNormalizationError('bad source')), patch('landscout.stages.apply_road_vehicle_proxy_policy.load_ign_road_vehicle_proxy_policy') as policy_loader, pytest.raises(IgnRoadVehicleProxyApplicationError): apply_ign_road_vehicle_proxy_policy(_source(), SOURCE_CONFIG)`.

**Regression protected**

- Protects the exact `normalization failure stops policy loading` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `IgnRoadNormalizationError`, `_source`, `apply_ign_road_vehicle_proxy_policy`, `patch`, `policy_loader.assert_not_called`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_normalized_facts_rows_index_crs_and_geometry_are_preserved`

**Signature**

```python
def test_normalized_facts_rows_index_crs_and_geometry_are_preserved() -> None:
```

**Purpose**

Protects the `normalized facts rows index crs and geometry are preserved` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `roads` from `_roads({'nature_raw': 'Chemin'}, {'road_feature_id': 'IGN_BDTOPO:ROAD_SEGMENT:SECOND'})`.
- Computes `before` from `deepcopy(roads)`.
- Computes `result` from `_apply(roads).roads`.

**Action**

- Calls `_apply`, `_roads`, `deepcopy`, `isinstance`, `result.geometry.to_wkb`, `result.geometry.to_wkb().equals`, `result.index.equals`, `roads.geometry.to_wkb`.

**Expected result**

- Direct assertions: `assert list(result.columns[:len(roads.columns)]) == list(roads.columns)`; `assert list(result.columns[len(roads.columns):]) == list(POLICY_COLUMNS)`; `assert isinstance(result.index, pd.RangeIndex)`; `assert result.index.equals(roads.index)`; `assert result.crs == roads.crs`; `assert result.active_geometry_name == roads.active_geometry_name`; `assert result.geometry.to_wkb().equals(roads.geometry.to_wkb())`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `normalized facts rows index crs and geometry are preserved` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_apply`, `_roads`, `assert_geodataframe_equal`, `deepcopy`, `isinstance`, `len`, `list`, `result.geometry.to_wkb`, `result.geometry.to_wkb().equals`, `result.index.equals`, `roads.geometry.to_wkb`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_object_is_not_mutated`

**Signature**

```python
def test_source_object_is_not_mutated() -> None:
```

**Purpose**

Protects the `source object is not mutated` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `source` from `_source()`.
- Computes `before` from `deepcopy(source.road_segments)`.
- Computes `normalized` from `NormalizedIgnRoadData(_roads())`.
- Enters managed context(s) `patch('landscout.stages.apply_road_vehicle_proxy_policy.normalize_ign_roads', return_value=normalized)` and executes: Calls `apply_ign_road_vehicle_proxy_policy(source, SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `NormalizedIgnRoadData`, `_roads`, `_source`, `apply_ign_road_vehicle_proxy_policy`, `deepcopy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `source object is not mutated` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks; actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `NormalizedIgnRoadData`, `_roads`, `_source`, `apply_ign_road_vehicle_proxy_policy`, `assert_geodataframe_equal`, `deepcopy`, `patch`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_non_valid_geometry_uses_technical_gate`

**Signature**

```python
def test_non_valid_geometry_uses_technical_gate(
    status: str, geometry: object
) -> None:
```

**Purpose**

Protects the `non valid geometry uses technical gate` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `status`, `geometry`.
- Contains 1 explicit setup/context statement(s).
- Computes `row` from `_row({'geometry_status': status, 'geometry': geometry})`.

**Action**

- Calls `LineString`, `_row`.

**Expected result**

- Direct assertions: `assert row.road_proxy_primary_rule == 'SOURCE_GEOMETRY_NOT_VALID'`; `assert row.road_proxy_class == 'NOT_DISTANCE_PROXY'`; `assert row.road_proxy_rule_trace_json == '["SOURCE_GEOMETRY_NOT_VALID"]'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `non valid geometry uses technical gate` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `_row`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unknown_geometry_status_is_rejected`

**Signature**

```python
def test_unknown_geometry_status_is_rejected() -> None:
```

**Purpose**

Protects the `unknown geometry status is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(IgnRoadVehicleProxyApplicationError)` and executes: Calls `_apply(_roads({'geometry_status': 'BROKEN'}))` for its validation or side effect.

**Action**

- Calls `_apply`, `_roads`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnRoadVehicleProxyApplicationError): _apply(_roads({'geometry_status': 'BROKEN'}))`.

**Regression protected**

- Protects the exact `unknown geometry status is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_apply`, `_roads`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_each_policy_rule_selects_approved_outcome`

**Signature**

```python
def test_each_policy_rule_selects_approved_outcome(
    overrides: dict[str, object], rule: str, expected_class: str
) -> None:
```

**Purpose**

Protects the `each policy rule selects approved outcome` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `overrides`, `rule`, `expected_class`.
- Contains 1 explicit setup/context statement(s).
- Computes `row` from `_row(overrides)`.

**Action**

- Calls `_row`.

**Expected result**

- Direct assertions: `assert row.road_proxy_primary_rule == rule`; `assert row.road_proxy_class == expected_class`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `each policy rule selects approved outcome` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_row`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_policy_precedence_conflicts_select_first_rule`

**Signature**

```python
def test_policy_precedence_conflicts_select_first_rule(
    overrides: dict[str, object], rule: str
) -> None:
```

**Purpose**

Protects the `policy precedence conflicts select first rule` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `overrides`, `rule`.
- Contains 0 explicit setup/context statement(s).

**Action**

- Calls `_row`.

**Expected result**

- Direct assertions: `assert _row(overrides).road_proxy_primary_rule == rule`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `policy precedence conflicts select first rule` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_row`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_boolean_like_source_values_are_parsed_without_coercion`

**Signature**

```python
def test_boolean_like_source_values_are_parsed_without_coercion(
    field: str, value: object, expected_rule: str
) -> None:
```

**Purpose**

Protects the `boolean like source values are parsed without coercion` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `field`, `value`, `expected_rule`.
- Contains 0 explicit setup/context statement(s).

**Action**

- Calls `_row`, `np.bool_`.

**Expected result**

- Direct assertions: `assert _row({field: value}).road_proxy_primary_rule == expected_rule`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `boolean like source values are parsed without coercion` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_row`, `np.bool_`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unknown_critical_vocabulary_never_uses_general_fallback`

**Signature**

```python
def test_unknown_critical_vocabulary_never_uses_general_fallback(
    field: str, value: object
) -> None:
```

**Purpose**

Protects the `unknown critical vocabulary never uses general fallback` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `field`, `value`.
- Contains 1 explicit setup/context statement(s).
- Computes `row` from `_row({field: value})`.

**Action**

- Calls `_row`.

**Expected result**

- Direct assertions: `assert row.road_proxy_primary_rule == 'UNKNOWN'`; `assert row.road_proxy_class == 'UNKNOWN_REVIEW'`; `assert field in row.road_proxy_unknown_fields_json`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `unknown critical vocabulary never uses general fallback` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_row`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_width_contract`

**Signature**

```python
def test_width_contract(value: object, expected_rule: str) -> None:
```

**Purpose**

Protects the `width contract` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `value`, `expected_rule`.
- Contains 0 explicit setup/context statement(s).

**Action**

- Calls `_row`, `float`.

**Expected result**

- Direct assertions: `assert _row({'carriageway_width_raw': value}).road_proxy_primary_rule == expected_rule`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `width contract` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_row`, `float`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_optional_restriction_source_contract`

**Signature**

```python
def test_optional_restriction_source_contract(
    field: str, value: object, expected_rule: str
) -> None:
```

**Purpose**

Protects the `optional restriction source contract` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `field`, `value`, `expected_rule`.
- Contains 0 explicit setup/context statement(s).

**Action**

- Calls `_row`.

**Expected result**

- Direct assertions: `assert _row({field: value}).road_proxy_primary_rule == expected_rule`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `optional restriction source contract` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_row`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_every_configured_known_restriction_is_applied`

**Signature**

```python
def test_every_configured_known_restriction_is_applied() -> None:
```

**Purpose**

Protects the `every configured known restriction is applied` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Computes `policy` from `load_ign_road_vehicle_proxy_policy()`.

**Action**

- Calls `_row`, `load_ign_road_vehicle_proxy_policy`.

**Expected result**

- Direct assertions: `assert _row({'restriction_nature_raw': restriction}).road_proxy_primary_rule == 'KNOWN_RESTRICTION'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `every configured known restriction is applied` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_row`, `load_ign_road_vehicle_proxy_policy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_general_fallback_requires_complete_positive_evidence_and_tracks_toll`

**Signature**

```python
def test_general_fallback_requires_complete_positive_evidence_and_tracks_toll() -> None:
```

**Purpose**

Protects the `general fallback requires complete positive evidence and tracks toll` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `open_row` from `_row()`.
- Computes `toll_row` from `_row({'light_vehicle_access_raw': 'A péage'})`.

**Action**

- Calls `_row`.

**Expected result**

- Direct assertions: `assert open_row.road_proxy_class == 'GENERAL_VEHICLE_PROXY'`; `assert not open_row.road_proxy_toll_evidence`; `assert toll_row.road_proxy_class == 'GENERAL_VEHICLE_PROXY'`; `assert toll_row.road_proxy_toll_evidence`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `general fallback requires complete positive evidence and tracks toll` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_row`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_open_access_does_not_hide_unresolved_evidence`

**Signature**

```python
def test_open_access_does_not_hide_unresolved_evidence(
    overrides: dict[str, object]
) -> None:
```

**Purpose**

Protects the `open access does not hide unresolved evidence` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `overrides`.
- Contains 0 explicit setup/context statement(s).

**Action**

- Calls `_row`.

**Expected result**

- Direct assertions: `assert _row(overrides).road_proxy_primary_rule == 'UNKNOWN'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `open access does not hide unresolved evidence` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_row`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_trace_is_complete_unique_and_in_policy_order`

**Signature**

```python
def test_trace_is_complete_unique_and_in_policy_order() -> None:
```

**Purpose**

Protects the `trace is complete unique and in policy order` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `row` from `_row({'private_raw': 1.0, 'closure_period_raw': 'Hiver', 'restriction_nature_raw': 'Plot amovible', 'nature_raw': 'Chemin', 'importance_raw': '6', 'carriageway_width_raw': 2.0})`.
- Computes `expected` from `'["PRIVATE_ROAD","TEMPORAL_CLOSURE","KNOWN_RESTRICTION","LIMITED_NATURE","IMPORTANCE_6","NARROW_CARRIAGEWAY"]'`.

**Action**

- Calls `_row`.

**Expected result**

- Direct assertions: `assert row.road_proxy_rule_trace_json == expected`; `assert row.road_proxy_primary_rule == 'PRIVATE_ROAD'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `trace is complete unique and in policy order` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_row`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_known_higher_rule_remains_primary_while_unknown_is_traced`

**Signature**

```python
def test_known_higher_rule_remains_primary_while_unknown_is_traced() -> None:
```

**Purpose**

Protects the `known higher rule remains primary while unknown is traced` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Computes `row` from `_row({'private_raw': 1.0, 'importance_raw': '7'})`.

**Action**

- Calls `_row`.

**Expected result**

- Direct assertions: `assert row.road_proxy_primary_rule == 'PRIVATE_ROAD'`; `assert row.road_proxy_rule_trace_json == '["PRIVATE_ROAD","UNKNOWN"]'`; `assert row.road_proxy_unknown_fields_json == '["importance_raw"]'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `known higher rule remains primary while unknown is traced` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_row`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unknown_fields_trace_is_fixed_and_deterministic`

**Signature**

```python
def test_unknown_fields_trace_is_fixed_and_deterministic() -> None:
```

**Purpose**

Protects the `unknown fields trace is fixed and deterministic` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Computes `row` from `_row({'fictitious_raw': None, 'asset_status_raw': 'Future', 'nature_raw': 'Future', 'light_vehicle_access_raw': 'Future', 'private_raw': None, 'importance_raw': '7', 'carriageway_width_raw': 'bad', 'closure_period_raw': ' ', 'restriction_nature_raw': 1})`.

**Action**

- Calls `_row`.

**Expected result**

- Direct assertions: `assert row.road_proxy_unknown_fields_json == '["fictitious_raw","asset_status_raw","nature_raw","light_vehicle_access_raw","private_raw","importance_raw","carriageway_width_raw","closure_period_raw","restriction_nature_raw"]'`; `assert _row().road_proxy_unknown_fields_json == '[]'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `unknown fields trace is fixed and deterministic` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_row`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_policy_lineage_is_exact_on_every_row`

**Signature**

```python
def test_policy_lineage_is_exact_on_every_row() -> None:
```

**Purpose**

Protects the `policy lineage is exact on every row` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `policy` from `load_ign_road_vehicle_proxy_policy()`.
- Computes `result` from `_apply(_roads({}, {})).roads`.

**Action**

- Calls `_apply`, `_roads`, `load_ign_road_vehicle_proxy_policy`.

**Expected result**

- Direct assertions: `assert set(result.road_proxy_policy_id) == {policy.policy_id}`; `assert set(result.road_proxy_policy_schema_version) == {policy.schema_version}`; `assert set(result.road_proxy_policy_config_sha256) == {policy.config_sha256}`; `assert set(result.road_proxy_policy_scope) == {policy.scope}`; `assert set(result.road_proxy_policy_evidence_checked_on) == {policy.evidence_checked_on}`; `assert set(result.road_proxy_vehicle_scope) == {policy.vehicle_scope}`; `assert set(result.road_proxy_heavy_vehicle_access) == {'NOT_PROVEN'}`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `policy lineage is exact on every row` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_apply`, `_roads`, `load_ign_road_vehicle_proxy_policy`, `set`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_result_is_frozen_and_contains_no_unsafe_claim_vocabulary`

**Signature**

```python
def test_result_is_frozen_and_contains_no_unsafe_claim_vocabulary() -> None:
```

**Purpose**

Protects the `result is frozen and contains no unsafe claim vocabulary` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `result` from `_apply(_roads())`.
- Computes `forbidden` from `('TRUCK_ACCESSIBLE', 'LEGAL_ACCESS', 'BESS_ACCESSIBLE', 'AUTHORIZED', 'APPROVED')`.
- Enters managed context(s) `pytest.raises(FrozenInstanceError)` and executes: Computes `result.roads` from `_roads()`.
- Computes `produced` from `' '.join(map(str, [*result.roads.columns, *result.roads.astype(str).to_numpy().ravel()]))`.

**Action**

- Calls `' '.join`, `_apply`, `_roads`, `all`, `map`, `result.roads.astype`, `result.roads.astype(str).to_numpy`, `result.roads.astype(str).to_numpy().ravel`.

**Expected result**

- Direct assertions: `assert all((token not in produced for token in forbidden))`.
- Expected exception contexts: `with pytest.raises(FrozenInstanceError): result.roads = _roads()`.

**Regression protected**

- Protects the exact `result is frozen and contains no unsafe claim vocabulary` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `' '.join`, `_apply`, `_roads`, `all`, `map`, `pytest.raises`, `result.roads.astype`, `result.roads.astype(str).to_numpy`, `result.roads.astype(str).to_numpy().ravel`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_valid_geometry_status_with_unsupported_geometry_is_not_repaired`

**Signature**

```python
def test_valid_geometry_status_with_unsupported_geometry_is_not_repaired() -> None:
```

**Purpose**

Protects the `valid geometry status with unsupported geometry is not repaired` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `polygon` from `Polygon([(0, 0), (1, 0), (1, 1), (0, 0)])`.
- Computes `roads` from `_roads({'geometry': polygon})`.
- Enters managed context(s) `patch('landscout.stages.apply_road_vehicle_proxy_policy.normalize_ign_roads', side_effect=IgnRoadNormalizationError('unsupported geometry')), pytest.raises(IgnRoadVehicleProxyApplicationError)` and executes: Calls `apply_ign_road_vehicle_proxy_policy(_source(), SOURCE_CONFIG)` for its validation or side effect.

**Action**

- Calls `IgnRoadNormalizationError`, `Polygon`, `_roads`, `_source`, `apply_ign_road_vehicle_proxy_policy`, `roads.geometry.iloc[0].equals_exact`.

**Expected result**

- Direct assertions: `assert roads.geometry.iloc[0].equals_exact(polygon, tolerance=0)`.
- Expected exception contexts: `with patch('landscout.stages.apply_road_vehicle_proxy_policy.normalize_ign_roads', side_effect=IgnRoadNormalizationError('unsupported geometry')), pytest.raises(IgnRoadVehicleProxyApplicationError): apply_ign_road_vehicle_proxy_policy(_source(), SOURCE_CONFIG)`.

**Regression protected**

- Protects the exact `valid geometry status with unsupported geometry is not repaired` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks; actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `IgnRoadNormalizationError`, `Polygon`, `_roads`, `_source`, `apply_ign_road_vehicle_proxy_policy`, `patch`, `pytest.raises`, `roads.geometry.iloc[0].equals_exact`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_policy_path_must_be_path_or_none`

**Signature**

```python
def test_policy_path_must_be_path_or_none() -> None:
```

**Purpose**

Protects the `policy path must be path or none` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(IgnRoadVehicleProxyApplicationError)` and executes: Calls `apply_ign_road_vehicle_proxy_policy(_source(), SOURCE_CONFIG, cast(Any, str(POLICY_PATH)))` for its validation or side effect.

**Action**

- Calls `_source`, `apply_ign_road_vehicle_proxy_policy`, `cast`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnRoadVehicleProxyApplicationError): apply_ign_road_vehicle_proxy_policy(_source(), SOURCE_CONFIG, cast(Any, str(POLICY_PATH)))`.

**Regression protected**

- Protects the exact `policy path must be path or none` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_source`, `apply_ign_road_vehicle_proxy_policy`, `cast`, `pytest.raises`, `str`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_config_is_exact_pydantic_type`

**Signature**

```python
def test_source_config_is_exact_pydantic_type() -> None:
```

**Purpose**

Protects the `source config is exact pydantic type` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(IgnRoadVehicleProxyApplicationError)` and executes: Calls `apply_ign_road_vehicle_proxy_policy(_source(), ConfigSubclass.model_validate(SOURCE_CONFIG.model_dump()))` for its validation or side effect.

**Action**

- Calls `ConfigSubclass.model_validate`, `SOURCE_CONFIG.model_dump`, `_source`, `apply_ign_road_vehicle_proxy_policy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(IgnRoadVehicleProxyApplicationError): apply_ign_road_vehicle_proxy_policy(_source(), ConfigSubclass.model_validate(SOURCE_CONFIG.model_dump()))`.

**Regression protected**

- Protects the exact `source config is exact pydantic type` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `ConfigSubclass.model_validate`, `SOURCE_CONFIG.model_dump`, `_source`, `apply_ign_road_vehicle_proxy_policy`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `road_proxy_class` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `road_proxy_heavy_vehicle_access` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `road_proxy_policy_config_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `road_proxy_policy_evidence_checked_on` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `road_proxy_policy_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `road_proxy_policy_schema_version` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `road_proxy_policy_scope` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `road_proxy_primary_rule` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `road_proxy_rule_trace_json` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `road_proxy_toll_evidence` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `road_proxy_unknown_fields_json` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `road_proxy_vehicle_scope` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |

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

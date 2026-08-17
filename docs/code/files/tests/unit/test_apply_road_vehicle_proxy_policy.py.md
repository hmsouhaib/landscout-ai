# `tests/unit/test_apply_road_vehicle_proxy_policy.py`

## File identity

- Repository path: `tests/unit/test_apply_road_vehicle_proxy_policy.py`
- File type: Python test
- Layer: unit/regression test
- Domain: test
- Responsibility: Provides complete unit and regression coverage for the `apply_road_vehicle_proxy_policy` contracts exercised in this file.
- Source SHA256: `eaa1d3944b656e8202719eb65bfe202e663d6803e47172a51d8b7dadf3b268ad`

## 1. Purpose

Provides complete unit and regression coverage for the `apply_road_vehicle_proxy_policy` contracts exercised in this file.

## 2. Position in LandScout architecture

This file belongs to the **unit/regression test** layer and the **test** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `from copy import deepcopy`
- `from dataclasses import FrozenInstanceError`
- `from pathlib import Path`
- `from typing import Any, cast`
- `from unittest.mock import patch`

### Third-party packages

- `import geopandas as gpd`
- `import numpy as np`
- `import pandas as pd`
- `import pytest`
- `from geopandas.testing import assert_geodataframe_equal`
- `from shapely.geometry import LineString, Polygon`

### Internal LandScout imports

- `from landscout import stages`
- `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_source_config,
)`
- `from landscout.stages.apply_road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyApplicationError,
    IgnRoadVehicleProxyApplicationResult,
    apply_ign_road_vehicle_proxy_policy,
)`
- `from landscout.stages.normalize_access_ign import (
    IgnRoadNormalizationError,
    NormalizedIgnRoadData,
)`
- `from landscout.stages.road_vehicle_proxy_policy import (
    load_ign_road_vehicle_proxy_policy,
)`

## 4. Contract taxonomy

### A. Python constants

#### `SOURCE_CONFIG`

```python
SOURCE_CONFIG = load_ign_bdtopo_source_config()
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_apply_road_vehicle_proxy_policy.py::_apply` (value reference), `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_wrong_source_type_has_controlled_error` (value reference), `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_malformed_policy_path_has_controlled_error` (value reference), `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_source_complete_normalization_is_invoked_exactly_once` (value reference), `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_normalization_failure_stops_policy_loading` (value reference), `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_source_object_is_not_mutated` (value reference), `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_valid_geometry_status_with_unsupported_geometry_is_not_repaired` (value reference), `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_policy_path_must_be_path_or_none` (value reference), `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_source_config_is_exact_pydantic_type` (value reference).

#### `POLICY_PATH`

```python
POLICY_PATH = Path("configs/access/ign_bdtopo_vehicle_proxy_policy.yaml")
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_policy_path_must_be_path_or_none` (value reference).

#### `POLICY_COLUMNS`

```python
POLICY_COLUMNS = (
    "road_proxy_primary_rule",
    "road_proxy_class",
    "road_proxy_rule_trace_json",
    "road_proxy_unknown_fields_json",
    "road_proxy_toll_evidence",
    "road_proxy_policy_id",
    "road_proxy_policy_schema_version",
    "road_proxy_policy_config_sha256",
    "road_proxy_policy_scope",
    "road_proxy_policy_evidence_checked_on",
    "road_proxy_vehicle_scope",
    "road_proxy_heavy_vehicle_access",
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_normalized_facts_rows_index_crs_and_geometry_are_preserved` (value reference).


### B. Type aliases and closed domains

No module-level Literal/Annotated/TypeAlias declaration is present.

### C. Meaningful dunder contracts

No meaningful module-level dunder contract is declared.

### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

### `test_source_config_is_exact_pydantic_type.ConfigSubclass`

**Purpose:** Encapsulates the test behavior implemented by its exact methods and attributes below.

**Kind:** class.

**Inheritance:** `IgnBdTopoSourceConfig`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- No repository construction/import/property/decorator reference was found; the exact declaration is retained because it participates in the module's runtime/framework namespace.

**Exact class source**

```python
class ConfigSubclass(IgnBdTopoSourceConfig):
        pass
```


## 6. Functions and methods

### `_base_row`

**Exact signature**

```python
def _base_row(number: int = 1) -> dict[str, object]:
```

**Purpose**

Private `test` helper for base row; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict[str, object]`.
- Every observed return expression is reproduced without truncation:
```python
{'road_feature_id': f'IGN_BDTOPO:ROAD_SEGMENT:ROAD-{number}', 'road_feature_type': 'ROAD_SEGMENT', 'source_provider': 'IGN', 'source_product': 'BD_TOPO', 'source_layer': 'troncon_de_route', 'source_feature_id': f'ROAD-{number}', 'source_department_code': '31', 'source_edition': '2026-06-15', 'source_product_version': '3.5', 'source_download_timestamp': '2026-08-11T15:32:03+00:00', 'source_archive_sha256': 'a' * 64, 'source_url': 'https://example.test/roads.7z', 'nature_raw': 'Route à 1 chaussée', 'importance_raw': '2', 'fictitious_raw': False, 'position_relative_to_ground_raw': 0, 'asset_status_raw': 'En service', 'lane_count_raw': 2.0, 'carriageway_width_raw': 7.0, 'private_raw': 0.0, 'traffic_direction_raw': 'Double sens', 'urban_raw': False, 'mean_light_vehicle_speed_raw': 80, 'light_vehicle_access_raw': 'Libre', 'closure_period_raw': None, 'restriction_nature_raw': None, 'restriction_height_raw': None, 'restriction_total_weight_raw': None, 'restriction_axle_weight_raw': None, 'restriction_width_raw': None, 'restriction_length_raw': None, 'dangerous_goods_forbidden_raw': None, 'administrative_classification_raw': None, 'manager_raw': None, 'source_name_raw': None, 'source_identifiers_raw': None, 'source_created_at': None, 'source_modified_at': None, 'source_confirmed_at': None, 'planimetric_acquisition_method': 'Photogrammétrie', 'planimetric_precision_raw': 1.5, 'spatial_role': 'PROXY_GEOMETRY', 'geometry_status': 'VALID', 'geometry': LineString([(number, 0), (number, 10)])}
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

- direct call: `tests/unit/test_apply_road_vehicle_proxy_policy.py::_roads` via `_base_row`.

**Complete source-ordered implementation**

```python
def _base_row(number: int = 1) -> dict[str, object]:
    return {
        "road_feature_id": f"IGN_BDTOPO:ROAD_SEGMENT:ROAD-{number}",
        "road_feature_type": "ROAD_SEGMENT",
        "source_provider": "IGN",
        "source_product": "BD_TOPO",
        "source_layer": "troncon_de_route",
        "source_feature_id": f"ROAD-{number}",
        "source_department_code": "31",
        "source_edition": "2026-06-15",
        "source_product_version": "3.5",
        "source_download_timestamp": "2026-08-11T15:32:03+00:00",
        "source_archive_sha256": "a" * 64,
        "source_url": "https://example.test/roads.7z",
        "nature_raw": "Route à 1 chaussée",
        "importance_raw": "2",
        "fictitious_raw": False,
        "position_relative_to_ground_raw": 0,
        "asset_status_raw": "En service",
        "lane_count_raw": 2.0,
        "carriageway_width_raw": 7.0,
        "private_raw": 0.0,
        "traffic_direction_raw": "Double sens",
        "urban_raw": False,
        "mean_light_vehicle_speed_raw": 80,
        "light_vehicle_access_raw": "Libre",
        "closure_period_raw": None,
        "restriction_nature_raw": None,
        "restriction_height_raw": None,
        "restriction_total_weight_raw": None,
        "restriction_axle_weight_raw": None,
        "restriction_width_raw": None,
        "restriction_length_raw": None,
        "dangerous_goods_forbidden_raw": None,
        "administrative_classification_raw": None,
        "manager_raw": None,
        "source_name_raw": None,
        "source_identifiers_raw": None,
        "source_created_at": None,
        "source_modified_at": None,
        "source_confirmed_at": None,
        "planimetric_acquisition_method": "Photogrammétrie",
        "planimetric_precision_raw": 1.5,
        "spatial_role": "PROXY_GEOMETRY",
        "geometry_status": "VALID",
        "geometry": LineString([(number, 0), (number, 10)]),
    }
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_roads`

**Exact signature**

```python
def _roads(*overrides: dict[str, object]) -> gpd.GeoDataFrame:
```

**Purpose**

Private `test` helper for roads; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
gpd.GeoDataFrame(rows, geometry='geometry', crs='EPSG:2154')
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
- In-memory mutation: `row`, `rows`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_apply_road_vehicle_proxy_policy.py::_source` via `_roads`.
- direct call: `tests/unit/test_apply_road_vehicle_proxy_policy.py::_row` via `_roads`.
- direct call: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_malformed_policy_path_has_controlled_error` via `_roads`.
- direct call: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_source_complete_normalization_is_invoked_exactly_once` via `_roads`.
- direct call: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_normalized_facts_rows_index_crs_and_geometry_are_preserved` via `_roads`.
- direct call: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_source_object_is_not_mutated` via `_roads`.
- direct call: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_unknown_geometry_status_is_rejected` via `_roads`.
- direct call: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_policy_lineage_is_exact_on_every_row` via `_roads`.
- direct call: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_result_is_frozen_and_contains_no_unsafe_claim_vocabulary` via `_roads`.
- direct call: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_valid_geometry_status_with_unsupported_geometry_is_not_repaired` via `_roads`.

**Complete source-ordered implementation**

```python
def _roads(*overrides: dict[str, object]) -> gpd.GeoDataFrame:
    mutations = overrides or ({},)
    rows: list[dict[str, object]] = []
    for number, mutation in enumerate(mutations, start=1):
        row = _base_row(number)
        row.update(mutation)
        rows.append(row)
    return gpd.GeoDataFrame(rows, geometry="geometry", crs="EPSG:2154")
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_source`

**Exact signature**

```python
def _source() -> IgnBdTopoRoadData:
```

**Purpose**

Private `test` helper for source; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `IgnBdTopoRoadData`.
- Every observed return expression is reproduced without truncation:
```python
IgnBdTopoRoadData(extraction=cast(Any, None), road_segments=_roads(), road_segments_summary=cast(Any, None))
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

- direct call: `tests/unit/test_apply_road_vehicle_proxy_policy.py::_apply` via `_source`.
- direct call: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_wrong_source_config_type_has_controlled_error` via `_source`.
- direct call: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_malformed_policy_path_has_controlled_error` via `_source`.
- direct call: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_source_complete_normalization_is_invoked_exactly_once` via `_source`.
- direct call: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_normalization_failure_stops_policy_loading` via `_source`.
- direct call: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_source_object_is_not_mutated` via `_source`.
- direct call: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_valid_geometry_status_with_unsupported_geometry_is_not_repaired` via `_source`.
- direct call: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_policy_path_must_be_path_or_none` via `_source`.
- direct call: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_source_config_is_exact_pydantic_type` via `_source`.

**Complete source-ordered implementation**

```python
def _source() -> IgnBdTopoRoadData:
    return IgnBdTopoRoadData(
        extraction=cast(Any, None),
        road_segments=_roads(),
        road_segments_summary=cast(Any, None),
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_apply`

**Exact signature**

```python
def _apply(
    roads: gpd.GeoDataFrame,
    *,
    policy_path: Path | None = None,
) -> IgnRoadVehicleProxyApplicationResult:
```

**Purpose**

Applies the configured policy to apply; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `IgnRoadVehicleProxyApplicationResult`.
- Every observed return expression is reproduced without truncation:
```python
apply_ign_road_vehicle_proxy_policy(_source(), SOURCE_CONFIG, policy_path)
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

- direct call: `tests/unit/test_apply_road_vehicle_proxy_policy.py::_row` via `_apply`.
- direct call: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_normalized_facts_rows_index_crs_and_geometry_are_preserved` via `_apply`.
- direct call: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_unknown_geometry_status_is_rejected` via `_apply`.
- direct call: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_policy_lineage_is_exact_on_every_row` via `_apply`.
- direct call: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_result_is_frozen_and_contains_no_unsafe_claim_vocabulary` via `_apply`.

**Complete source-ordered implementation**

```python
def _apply(
    roads: gpd.GeoDataFrame,
    *,
    policy_path: Path | None = None,
) -> IgnRoadVehicleProxyApplicationResult:
    normalized = NormalizedIgnRoadData(road_segments=roads)
    with patch(
        "landscout.stages.apply_road_vehicle_proxy_policy.normalize_ign_roads",
        return_value=normalized,
    ):
        return apply_ign_road_vehicle_proxy_policy(
            _source(), SOURCE_CONFIG, policy_path
        )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_row`

**Exact signature**

```python
def _row(
    overrides: dict[str, object] | None = None,
) -> pd.Series:
```

**Purpose**

Private `test` helper for row; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `pd.Series`.
- Every observed return expression is reproduced without truncation:
```python
result.roads.iloc[0]
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

- direct call: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_non_valid_geometry_uses_technical_gate` via `_row`.
- direct call: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_each_policy_rule_selects_approved_outcome` via `_row`.
- direct call: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_policy_precedence_conflicts_select_first_rule` via `_row`.
- direct call: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_boolean_like_source_values_are_parsed_without_coercion` via `_row`.
- direct call: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_unknown_critical_vocabulary_never_uses_general_fallback` via `_row`.
- direct call: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_width_contract` via `_row`.
- direct call: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_optional_restriction_source_contract` via `_row`.
- direct call: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_every_configured_known_restriction_is_applied` via `_row`.
- direct call: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_general_fallback_requires_complete_positive_evidence_and_tracks_toll` via `_row`.
- direct call: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_open_access_does_not_hide_unresolved_evidence` via `_row`.
- direct call: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_trace_is_complete_unique_and_in_policy_order` via `_row`.
- direct call: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_known_higher_rule_remains_primary_while_unknown_is_traced` via `_row`.
- direct call: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_unknown_fields_trace_is_fixed_and_deterministic` via `_row`.

**Complete source-ordered implementation**

```python
def _row(
    overrides: dict[str, object] | None = None,
) -> pd.Series:
    result = _apply(_roads(overrides or {}))
    return result.roads.iloc[0]
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_public_api_exports_only_stable_application_symbols`

**Purpose**

Exercises `public api exports only stable application symbols`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
import landscout.stages.apply_road_vehicle_proxy_policy as module
expected = {
        "IgnRoadVehicleProxyApplicationError",
        "IgnRoadVehicleProxyApplicationResult",
        "apply_ign_road_vehicle_proxy_policy",
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
assert all(hasattr(stages, symbol) for symbol in expected)
assert not hasattr(stages, "_classify_road_frame")
```

**Regression protected**

Locks `public api exports only stable application symbols` through the exact asserted conditions: `set(module.__all__) == expected`; `expected <= set(stages.__all__)`; `all((hasattr(stages, symbol) for symbol in expected))`; `not hasattr(stages, '_classify_road_frame')`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_public_api_exports_only_stable_application_symbols() -> None:
    import landscout.stages.apply_road_vehicle_proxy_policy as module

    expected = {
        "IgnRoadVehicleProxyApplicationError",
        "IgnRoadVehicleProxyApplicationResult",
        "apply_ign_road_vehicle_proxy_policy",
    }
    assert set(module.__all__) == expected
    assert expected <= set(stages.__all__)
    assert all(hasattr(stages, symbol) for symbol in expected)
    assert not hasattr(stages, "_classify_road_frame")
```

### `test_wrong_source_type_has_controlled_error`

**Purpose**

Exercises `wrong source type has controlled error`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
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
with pytest.raises(IgnRoadVehicleProxyApplicationError):
        apply_ign_road_vehicle_proxy_policy(
            cast(Any, object()), SOURCE_CONFIG
        )
```

**Regression protected**

Locks `wrong source type has controlled error`: the reproduced adversarial input must raise `IgnRoadVehicleProxyApplicationError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_wrong_source_type_has_controlled_error() -> None:
    with pytest.raises(IgnRoadVehicleProxyApplicationError):
        apply_ign_road_vehicle_proxy_policy(
            cast(Any, object()), SOURCE_CONFIG
        )
```

### `test_wrong_source_config_type_has_controlled_error`

**Purpose**

Exercises `wrong source config type has controlled error`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
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
with pytest.raises(IgnRoadVehicleProxyApplicationError):
        apply_ign_road_vehicle_proxy_policy(
            _source(), cast(Any, object())
        )
```

**Regression protected**

Locks `wrong source config type has controlled error`: the reproduced adversarial input must raise `IgnRoadVehicleProxyApplicationError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_wrong_source_config_type_has_controlled_error() -> None:
    with pytest.raises(IgnRoadVehicleProxyApplicationError):
        apply_ign_road_vehicle_proxy_policy(
            _source(), cast(Any, object())
        )
```

### `test_malformed_policy_path_has_controlled_error`

**Purpose**

Exercises `malformed policy path has controlled error`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
path = tmp_path / "policy.yaml"
path.write_text("policy_id: [", encoding="utf-8")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with patch(
        "landscout.stages.apply_road_vehicle_proxy_policy.normalize_ign_roads",
        return_value=NormalizedIgnRoadData(_roads()),
    ), pytest.raises(IgnRoadVehicleProxyApplicationError):
        apply_ign_road_vehicle_proxy_policy(_source(), SOURCE_CONFIG, path)
```

**Regression protected**

Locks `malformed policy path has controlled error`: the reproduced adversarial input must raise `IgnRoadVehicleProxyApplicationError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_malformed_policy_path_has_controlled_error(tmp_path: Path) -> None:
    path = tmp_path / "policy.yaml"
    path.write_text("policy_id: [", encoding="utf-8")

    with patch(
        "landscout.stages.apply_road_vehicle_proxy_policy.normalize_ign_roads",
        return_value=NormalizedIgnRoadData(_roads()),
    ), pytest.raises(IgnRoadVehicleProxyApplicationError):
        apply_ign_road_vehicle_proxy_policy(_source(), SOURCE_CONFIG, path)
```

### `test_source_complete_normalization_is_invoked_exactly_once`

**Purpose**

Exercises `source complete normalization is invoked exactly once`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
validator.assert_called_once()
```

**Action**

```python
normalized = NormalizedIgnRoadData(_roads())
with patch(
        "landscout.stages.apply_road_vehicle_proxy_policy.normalize_ign_roads",
        return_value=normalized,
    ) as validator:
        apply_ign_road_vehicle_proxy_policy(_source(), SOURCE_CONFIG)
```

**Expected result**

```python
# Completion without an exception is the asserted outcome.
```

**Regression protected**

Prevents a self-consistent but forged local object from bypassing the independent source-complete revalidation boundary.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

```python
def test_source_complete_normalization_is_invoked_exactly_once() -> None:
    normalized = NormalizedIgnRoadData(_roads())
    with patch(
        "landscout.stages.apply_road_vehicle_proxy_policy.normalize_ign_roads",
        return_value=normalized,
    ) as validator:
        apply_ign_road_vehicle_proxy_policy(_source(), SOURCE_CONFIG)

    validator.assert_called_once()
```

### `test_normalization_failure_stops_policy_loading`

**Purpose**

Exercises `normalization failure stops policy loading`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
policy_loader.assert_not_called()
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with patch(
        "landscout.stages.apply_road_vehicle_proxy_policy.normalize_ign_roads",
        side_effect=IgnRoadNormalizationError("bad source"),
    ), patch(
        "landscout.stages.apply_road_vehicle_proxy_policy.load_ign_road_vehicle_proxy_policy"
    ) as policy_loader, pytest.raises(IgnRoadVehicleProxyApplicationError):
        apply_ign_road_vehicle_proxy_policy(_source(), SOURCE_CONFIG)
```

**Regression protected**

Locks `normalization failure stops policy loading`: the reproduced adversarial input must raise `IgnRoadVehicleProxyApplicationError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

```python
def test_normalization_failure_stops_policy_loading() -> None:
    with patch(
        "landscout.stages.apply_road_vehicle_proxy_policy.normalize_ign_roads",
        side_effect=IgnRoadNormalizationError("bad source"),
    ), patch(
        "landscout.stages.apply_road_vehicle_proxy_policy.load_ign_road_vehicle_proxy_policy"
    ) as policy_loader, pytest.raises(IgnRoadVehicleProxyApplicationError):
        apply_ign_road_vehicle_proxy_policy(_source(), SOURCE_CONFIG)

    policy_loader.assert_not_called()
```

### `test_normalized_facts_rows_index_crs_and_geometry_are_preserved`

**Purpose**

Exercises `normalized facts rows index crs and geometry are preserved`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
roads = _roads(
        {"nature_raw": "Chemin"},
        {"road_feature_id": "IGN_BDTOPO:ROAD_SEGMENT:SECOND"},
    )
before = deepcopy(roads)
result = _apply(roads).roads
assert_geodataframe_equal(result.loc[:, roads.columns], roads)
assert_geodataframe_equal(roads, before)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert list(result.columns[: len(roads.columns)]) == list(roads.columns)
assert list(result.columns[len(roads.columns) :]) == list(POLICY_COLUMNS)
assert isinstance(result.index, pd.RangeIndex)
assert result.index.equals(roads.index)
assert result.crs == roads.crs
assert result.active_geometry_name == roads.active_geometry_name
assert result.geometry.to_wkb().equals(roads.geometry.to_wkb())
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_normalized_facts_rows_index_crs_and_geometry_are_preserved() -> None:
    roads = _roads(
        {"nature_raw": "Chemin"},
        {"road_feature_id": "IGN_BDTOPO:ROAD_SEGMENT:SECOND"},
    )
    before = deepcopy(roads)

    result = _apply(roads).roads

    assert list(result.columns[: len(roads.columns)]) == list(roads.columns)
    assert list(result.columns[len(roads.columns) :]) == list(POLICY_COLUMNS)
    assert isinstance(result.index, pd.RangeIndex)
    assert result.index.equals(roads.index)
    assert result.crs == roads.crs
    assert result.active_geometry_name == roads.active_geometry_name
    assert result.geometry.to_wkb().equals(roads.geometry.to_wkb())
    assert_geodataframe_equal(result.loc[:, roads.columns], roads)
    assert_geodataframe_equal(roads, before)
```

### `test_source_object_is_not_mutated`

**Purpose**

Exercises `source object is not mutated`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
source = _source()
before = deepcopy(source.road_segments)
assert_geodataframe_equal(source.road_segments, before)
```

**Action**

```python
normalized = NormalizedIgnRoadData(_roads())
with patch(
        "landscout.stages.apply_road_vehicle_proxy_policy.normalize_ign_roads",
        return_value=normalized,
    ):
        apply_ign_road_vehicle_proxy_policy(source, SOURCE_CONFIG)
```

**Expected result**

```python
# Completion without an exception is the asserted outcome.
```

**Regression protected**

Locks `source object is not mutated` by requiring the reproduced call path `_source`, `deepcopy`, `NormalizedIgnRoadData`, `assert_geodataframe_equal` without an unasserted exception.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_source_object_is_not_mutated() -> None:
    source = _source()
    before = deepcopy(source.road_segments)
    normalized = NormalizedIgnRoadData(_roads())

    with patch(
        "landscout.stages.apply_road_vehicle_proxy_policy.normalize_ign_roads",
        return_value=normalized,
    ):
        apply_ign_road_vehicle_proxy_policy(source, SOURCE_CONFIG)

    assert_geodataframe_equal(source.road_segments, before)
```

### `test_non_valid_geometry_uses_technical_gate`

**Purpose**

Exercises `non valid geometry uses technical gate`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `geometry`, `status`.

**Setup**

```python
row = _row({"geometry_status": status, "geometry": geometry})
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert row.road_proxy_primary_rule == "SOURCE_GEOMETRY_NOT_VALID"
assert row.road_proxy_class == "NOT_DISTANCE_PROXY"
assert row.road_proxy_rule_trace_json == '["SOURCE_GEOMETRY_NOT_VALID"]'
```

**Regression protected**

Pins true-null handling and prevents textual or malformed null-like values from changing the contract.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_non_valid_geometry_uses_technical_gate(
    status: str, geometry: object
) -> None:
    row = _row({"geometry_status": status, "geometry": geometry})

    assert row.road_proxy_primary_rule == "SOURCE_GEOMETRY_NOT_VALID"
    assert row.road_proxy_class == "NOT_DISTANCE_PROXY"
    assert row.road_proxy_rule_trace_json == '["SOURCE_GEOMETRY_NOT_VALID"]'
```

### `test_unknown_geometry_status_is_rejected`

**Purpose**

Exercises `unknown geometry status is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
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
with pytest.raises(IgnRoadVehicleProxyApplicationError):
        _apply(_roads({"geometry_status": "BROKEN"}))
```

**Regression protected**

Locks `unknown geometry status is rejected`: the reproduced adversarial input must raise `IgnRoadVehicleProxyApplicationError` before the prohibited success path.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_unknown_geometry_status_is_rejected() -> None:
    with pytest.raises(IgnRoadVehicleProxyApplicationError):
        _apply(_roads({"geometry_status": "BROKEN"}))
```

### `test_each_policy_rule_selects_approved_outcome`

**Purpose**

Exercises `each policy rule selects approved outcome`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `expected_class`, `overrides`, `rule`.

**Setup**

```python
row = _row(overrides)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert row.road_proxy_primary_rule == rule
assert row.road_proxy_class == expected_class
```

**Regression protected**

Locks `each policy rule selects approved outcome` through the exact asserted conditions: `row.road_proxy_primary_rule == rule`; `row.road_proxy_class == expected_class`.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_each_policy_rule_selects_approved_outcome(
    overrides: dict[str, object], rule: str, expected_class: str
) -> None:
    row = _row(overrides)

    assert row.road_proxy_primary_rule == rule
    assert row.road_proxy_class == expected_class
```

### `test_policy_precedence_conflicts_select_first_rule`

**Purpose**

Exercises `policy precedence conflicts select first rule`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `overrides`, `rule`.

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
assert _row(overrides).road_proxy_primary_rule == rule
```

**Regression protected**

Pins the configured policy-rule ordering so a lower-priority observation cannot replace the controlling evidence.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_policy_precedence_conflicts_select_first_rule(
    overrides: dict[str, object], rule: str
) -> None:
    assert _row(overrides).road_proxy_primary_rule == rule
```

### `test_boolean_like_source_values_are_parsed_without_coercion`

**Purpose**

Exercises `boolean like source values are parsed without coercion`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `expected_rule`, `field`, `value`.

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
assert _row({field: value}).road_proxy_primary_rule == expected_rule
```

**Regression protected**

Locks `boolean like source values are parsed without coercion` through the exact asserted conditions: `_row({field: value}).road_proxy_primary_rule == expected_rule`.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_boolean_like_source_values_are_parsed_without_coercion(
    field: str, value: object, expected_rule: str
) -> None:
    assert _row({field: value}).road_proxy_primary_rule == expected_rule
```

### `test_unknown_critical_vocabulary_never_uses_general_fallback`

**Purpose**

Exercises `unknown critical vocabulary never uses general fallback`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `field`, `value`.

**Setup**

```python
row = _row({field: value})
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert row.road_proxy_primary_rule == "UNKNOWN"
assert row.road_proxy_class == "UNKNOWN_REVIEW"
assert field in row.road_proxy_unknown_fields_json
```

**Regression protected**

Locks `unknown critical vocabulary never uses general fallback` through the exact asserted conditions: `row.road_proxy_primary_rule == 'UNKNOWN'`; `row.road_proxy_class == 'UNKNOWN_REVIEW'`; `field in row.road_proxy_unknown_fields_json`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_unknown_critical_vocabulary_never_uses_general_fallback(
    field: str, value: object
) -> None:
    row = _row({field: value})

    assert row.road_proxy_primary_rule == "UNKNOWN"
    assert row.road_proxy_class == "UNKNOWN_REVIEW"
    assert field in row.road_proxy_unknown_fields_json
```

### `test_width_contract`

**Purpose**

Exercises `width contract`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `expected_rule`, `value`.

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
assert _row({"carriageway_width_raw": value}).road_proxy_primary_rule == (
        expected_rule
    )
```

**Regression protected**

Locks `width contract` through the exact asserted conditions: `_row({'carriageway_width_raw': value}).road_proxy_primary_rule == expected_rule`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_width_contract(value: object, expected_rule: str) -> None:
    assert _row({"carriageway_width_raw": value}).road_proxy_primary_rule == (
        expected_rule
    )
```

### `test_optional_restriction_source_contract`

**Purpose**

Exercises `optional restriction source contract`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `expected_rule`, `field`, `value`.

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
assert _row({field: value}).road_proxy_primary_rule == expected_rule
```

**Regression protected**

Locks `optional restriction source contract` through the exact asserted conditions: `_row({field: value}).road_proxy_primary_rule == expected_rule`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_optional_restriction_source_contract(
    field: str, value: object, expected_rule: str
) -> None:
    assert _row({field: value}).road_proxy_primary_rule == expected_rule
```

### `test_every_configured_known_restriction_is_applied`

**Purpose**

Exercises `every configured known restriction is applied`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
for restriction in policy.known_restriction_review:
        assert _row(
            {"restriction_nature_raw": restriction}
        ).road_proxy_primary_rule == "KNOWN_RESTRICTION"
```

**Action**

```python
policy = load_ign_road_vehicle_proxy_policy()
```

**Expected result**

```python
# Completion without an exception is the asserted outcome.
```

**Regression protected**

Locks `every configured known restriction is applied` through the exact asserted conditions: `_row({'restriction_nature_raw': restriction}).road_proxy_primary_rule == 'KNOWN_RESTRICTION'`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_every_configured_known_restriction_is_applied() -> None:
    policy = load_ign_road_vehicle_proxy_policy()
    for restriction in policy.known_restriction_review:
        assert _row(
            {"restriction_nature_raw": restriction}
        ).road_proxy_primary_rule == "KNOWN_RESTRICTION"
```

### `test_general_fallback_requires_complete_positive_evidence_and_tracks_toll`

**Purpose**

Exercises `general fallback requires complete positive evidence and tracks toll`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
open_row = _row()
toll_row = _row({"light_vehicle_access_raw": "A péage"})
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert open_row.road_proxy_class == "GENERAL_VEHICLE_PROXY"
assert not open_row.road_proxy_toll_evidence
assert toll_row.road_proxy_class == "GENERAL_VEHICLE_PROXY"
assert toll_row.road_proxy_toll_evidence
```

**Regression protected**

Locks `general fallback requires complete positive evidence and tracks toll` through the exact asserted conditions: `open_row.road_proxy_class == 'GENERAL_VEHICLE_PROXY'`; `not open_row.road_proxy_toll_evidence`; `toll_row.road_proxy_class == 'GENERAL_VEHICLE_PROXY'`; `toll_row.road_proxy_toll_evidence`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_general_fallback_requires_complete_positive_evidence_and_tracks_toll() -> None:
    open_row = _row()
    toll_row = _row({"light_vehicle_access_raw": "A péage"})

    assert open_row.road_proxy_class == "GENERAL_VEHICLE_PROXY"
    assert not open_row.road_proxy_toll_evidence
    assert toll_row.road_proxy_class == "GENERAL_VEHICLE_PROXY"
    assert toll_row.road_proxy_toll_evidence
```

### `test_open_access_does_not_hide_unresolved_evidence`

**Purpose**

Exercises `open access does not hide unresolved evidence`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `overrides`.

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
assert _row(overrides).road_proxy_primary_rule == "UNKNOWN"
```

**Regression protected**

Locks `open access does not hide unresolved evidence` through the exact asserted conditions: `_row(overrides).road_proxy_primary_rule == 'UNKNOWN'`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_open_access_does_not_hide_unresolved_evidence(
    overrides: dict[str, object]
) -> None:
    assert _row(overrides).road_proxy_primary_rule == "UNKNOWN"
```

### `test_trace_is_complete_unique_and_in_policy_order`

**Purpose**

Exercises `trace is complete unique and in policy order`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
row = _row(
        {
            "private_raw": 1.0,
            "closure_period_raw": "Hiver",
            "restriction_nature_raw": "Plot amovible",
            "nature_raw": "Chemin",
            "importance_raw": "6",
            "carriageway_width_raw": 2.0,
        }
    )
expected = (
        '["PRIVATE_ROAD","TEMPORAL_CLOSURE","KNOWN_RESTRICTION",'
        '"LIMITED_NATURE","IMPORTANCE_6","NARROW_CARRIAGEWAY"]'
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert row.road_proxy_rule_trace_json == expected
assert row.road_proxy_primary_rule == "PRIVATE_ROAD"
```

**Regression protected**

Locks `trace is complete unique and in policy order` through the exact asserted conditions: `row.road_proxy_rule_trace_json == expected`; `row.road_proxy_primary_rule == 'PRIVATE_ROAD'`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_trace_is_complete_unique_and_in_policy_order() -> None:
    row = _row(
        {
            "private_raw": 1.0,
            "closure_period_raw": "Hiver",
            "restriction_nature_raw": "Plot amovible",
            "nature_raw": "Chemin",
            "importance_raw": "6",
            "carriageway_width_raw": 2.0,
        }
    )
    expected = (
        '["PRIVATE_ROAD","TEMPORAL_CLOSURE","KNOWN_RESTRICTION",'
        '"LIMITED_NATURE","IMPORTANCE_6","NARROW_CARRIAGEWAY"]'
    )

    assert row.road_proxy_rule_trace_json == expected
    assert row.road_proxy_primary_rule == "PRIVATE_ROAD"
```

### `test_known_higher_rule_remains_primary_while_unknown_is_traced`

**Purpose**

Exercises `known higher rule remains primary while unknown is traced`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
row = _row({"private_raw": 1.0, "importance_raw": "7"})
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert row.road_proxy_primary_rule == "PRIVATE_ROAD"
assert row.road_proxy_rule_trace_json == '["PRIVATE_ROAD","UNKNOWN"]'
assert row.road_proxy_unknown_fields_json == '["importance_raw"]'
```

**Regression protected**

Locks `known higher rule remains primary while unknown is traced` through the exact asserted conditions: `row.road_proxy_primary_rule == 'PRIVATE_ROAD'`; `row.road_proxy_rule_trace_json == '["PRIVATE_ROAD","UNKNOWN"]'`; `row.road_proxy_unknown_fields_json == '["importance_raw"]'`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_known_higher_rule_remains_primary_while_unknown_is_traced() -> None:
    row = _row({"private_raw": 1.0, "importance_raw": "7"})

    assert row.road_proxy_primary_rule == "PRIVATE_ROAD"
    assert row.road_proxy_rule_trace_json == '["PRIVATE_ROAD","UNKNOWN"]'
    assert row.road_proxy_unknown_fields_json == '["importance_raw"]'
```

### `test_unknown_fields_trace_is_fixed_and_deterministic`

**Purpose**

Exercises `unknown fields trace is fixed and deterministic`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
row = _row(
        {
            "fictitious_raw": None,
            "asset_status_raw": "Future",
            "nature_raw": "Future",
            "light_vehicle_access_raw": "Future",
            "private_raw": None,
            "importance_raw": "7",
            "carriageway_width_raw": "bad",
            "closure_period_raw": " ",
            "restriction_nature_raw": 1,
        }
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert row.road_proxy_unknown_fields_json == (
        '["fictitious_raw","asset_status_raw","nature_raw",'
        '"light_vehicle_access_raw","private_raw","importance_raw",'
        '"carriageway_width_raw","closure_period_raw",'
        '"restriction_nature_raw"]'
    )
assert _row().road_proxy_unknown_fields_json == "[]"
```

**Regression protected**

Locks `unknown fields trace is fixed and deterministic` through the exact asserted conditions: `row.road_proxy_unknown_fields_json == '["fictitious_raw","asset_status_raw","nature_raw","light_vehicle_access_raw","private_raw","importance_raw","carriageway_width_raw","closure_period_raw","restriction_nature_raw"]'`; `_row().road_proxy_unknown_fields_json == '[]'`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_unknown_fields_trace_is_fixed_and_deterministic() -> None:
    row = _row(
        {
            "fictitious_raw": None,
            "asset_status_raw": "Future",
            "nature_raw": "Future",
            "light_vehicle_access_raw": "Future",
            "private_raw": None,
            "importance_raw": "7",
            "carriageway_width_raw": "bad",
            "closure_period_raw": " ",
            "restriction_nature_raw": 1,
        }
    )
    assert row.road_proxy_unknown_fields_json == (
        '["fictitious_raw","asset_status_raw","nature_raw",'
        '"light_vehicle_access_raw","private_raw","importance_raw",'
        '"carriageway_width_raw","closure_period_raw",'
        '"restriction_nature_raw"]'
    )
    assert _row().road_proxy_unknown_fields_json == "[]"
```

### `test_policy_lineage_is_exact_on_every_row`

**Purpose**

Exercises `policy lineage is exact on every row`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
result = _apply(_roads({}, {})).roads
```

**Action**

```python
policy = load_ign_road_vehicle_proxy_policy()
```

**Expected result**

```python
assert set(result.road_proxy_policy_id) == {policy.policy_id}
assert set(result.road_proxy_policy_schema_version) == {policy.schema_version}
assert set(result.road_proxy_policy_config_sha256) == {policy.config_sha256}
assert set(result.road_proxy_policy_scope) == {policy.scope}
assert set(result.road_proxy_policy_evidence_checked_on) == {
        policy.evidence_checked_on
    }
assert set(result.road_proxy_vehicle_scope) == {policy.vehicle_scope}
assert set(result.road_proxy_heavy_vehicle_access) == {"NOT_PROVEN"}
```

**Regression protected**

Locks `policy lineage is exact on every row` through the exact asserted conditions: `set(result.road_proxy_policy_id) == {policy.policy_id}`; `set(result.road_proxy_policy_schema_version) == {policy.schema_version}`; `set(result.road_proxy_policy_config_sha256) == {policy.config_sha256}`; `set(result.road_proxy_policy_scope) == {policy.scope}`; plus 3 additional reproduced assertion(s).

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_policy_lineage_is_exact_on_every_row() -> None:
    policy = load_ign_road_vehicle_proxy_policy()
    result = _apply(_roads({}, {})).roads

    assert set(result.road_proxy_policy_id) == {policy.policy_id}
    assert set(result.road_proxy_policy_schema_version) == {policy.schema_version}
    assert set(result.road_proxy_policy_config_sha256) == {policy.config_sha256}
    assert set(result.road_proxy_policy_scope) == {policy.scope}
    assert set(result.road_proxy_policy_evidence_checked_on) == {
        policy.evidence_checked_on
    }
    assert set(result.road_proxy_vehicle_scope) == {policy.vehicle_scope}
    assert set(result.road_proxy_heavy_vehicle_access) == {"NOT_PROVEN"}
```

### `test_result_is_frozen_and_contains_no_unsafe_claim_vocabulary`

**Purpose**

Exercises `result is frozen and contains no unsafe claim vocabulary`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
result = _apply(_roads())
forbidden = (
        "TRUCK_ACCESSIBLE",
        "LEGAL_ACCESS",
        "BESS_ACCESSIBLE",
        "AUTHORIZED",
        "APPROVED",
    )
produced = " ".join(
        map(
            str,
            [*result.roads.columns, *result.roads.astype(str).to_numpy().ravel()],
        )
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(FrozenInstanceError):
        result.roads = _roads()
assert all(token not in produced for token in forbidden)
```

**Regression protected**

Locks `result is frozen and contains no unsafe claim vocabulary`: the reproduced adversarial input must raise `FrozenInstanceError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_result_is_frozen_and_contains_no_unsafe_claim_vocabulary() -> None:
    result = _apply(_roads())
    forbidden = (
        "TRUCK_ACCESSIBLE",
        "LEGAL_ACCESS",
        "BESS_ACCESSIBLE",
        "AUTHORIZED",
        "APPROVED",
    )

    with pytest.raises(FrozenInstanceError):
        result.roads = _roads()  # type: ignore[misc]
    produced = " ".join(
        map(
            str,
            [*result.roads.columns, *result.roads.astype(str).to_numpy().ravel()],
        )
    )
    assert all(token not in produced for token in forbidden)
```

### `test_valid_geometry_status_with_unsupported_geometry_is_not_repaired`

**Purpose**

Exercises `valid geometry status with unsupported geometry is not repaired`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
polygon = Polygon([(0, 0), (1, 0), (1, 1), (0, 0)])
roads = _roads({"geometry": polygon})
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with patch(
        "landscout.stages.apply_road_vehicle_proxy_policy.normalize_ign_roads",
        side_effect=IgnRoadNormalizationError("unsupported geometry"),
    ), pytest.raises(IgnRoadVehicleProxyApplicationError):
        apply_ign_road_vehicle_proxy_policy(_source(), SOURCE_CONFIG)
assert roads.geometry.iloc[0].equals_exact(polygon, tolerance=0)
```

**Regression protected**

Locks `valid geometry status with unsupported geometry is not repaired`: the reproduced adversarial input must raise `IgnRoadVehicleProxyApplicationError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_valid_geometry_status_with_unsupported_geometry_is_not_repaired() -> None:
    polygon = Polygon([(0, 0), (1, 0), (1, 1), (0, 0)])
    roads = _roads({"geometry": polygon})

    # The source-complete normalizer owns this geometry-kind rejection. The
    # application must propagate its controlled failure rather than repair it.
    with patch(
        "landscout.stages.apply_road_vehicle_proxy_policy.normalize_ign_roads",
        side_effect=IgnRoadNormalizationError("unsupported geometry"),
    ), pytest.raises(IgnRoadVehicleProxyApplicationError):
        apply_ign_road_vehicle_proxy_policy(_source(), SOURCE_CONFIG)

    assert roads.geometry.iloc[0].equals_exact(polygon, tolerance=0)
```

### `test_policy_path_must_be_path_or_none`

**Purpose**

Exercises `policy path must be path or none`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
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
with pytest.raises(IgnRoadVehicleProxyApplicationError):
        apply_ign_road_vehicle_proxy_policy(
            _source(), SOURCE_CONFIG, cast(Any, str(POLICY_PATH))
        )
```

**Regression protected**

Locks `policy path must be path or none`: the reproduced adversarial input must raise `IgnRoadVehicleProxyApplicationError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_policy_path_must_be_path_or_none() -> None:
    with pytest.raises(IgnRoadVehicleProxyApplicationError):
        apply_ign_road_vehicle_proxy_policy(
            _source(), SOURCE_CONFIG, cast(Any, str(POLICY_PATH))
        )
```

### `test_source_config_is_exact_pydantic_type`

**Purpose**

Exercises `source config is exact pydantic type`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
class ConfigSubclass(IgnBdTopoSourceConfig):
        pass
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnRoadVehicleProxyApplicationError):
        apply_ign_road_vehicle_proxy_policy(
            _source(), ConfigSubclass.model_validate(SOURCE_CONFIG.model_dump())
        )
```

**Regression protected**

Locks `source config is exact pydantic type`: the reproduced adversarial input must raise `IgnRoadVehicleProxyApplicationError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_source_config_is_exact_pydantic_type() -> None:
    class ConfigSubclass(IgnBdTopoSourceConfig):
        pass

    with pytest.raises(IgnRoadVehicleProxyApplicationError):
        apply_ign_road_vehicle_proxy_policy(
            _source(), ConfigSubclass.model_validate(SOURCE_CONFIG.model_dump())
        )
```


## 7. Data contracts

### `POLICY_COLUMNS` — canonical or derived frame-column schema

```python
POLICY_COLUMNS = (
    "road_proxy_primary_rule",
    "road_proxy_class",
    "road_proxy_rule_trace_json",
    "road_proxy_unknown_fields_json",
    "road_proxy_toll_evidence",
    "road_proxy_policy_id",
    "road_proxy_policy_schema_version",
    "road_proxy_policy_config_sha256",
    "road_proxy_policy_scope",
    "road_proxy_policy_evidence_checked_on",
    "road_proxy_vehicle_scope",
    "road_proxy_heavy_vehicle_access",
)
```


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

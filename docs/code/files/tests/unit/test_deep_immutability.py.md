# `tests/unit/test_deep_immutability.py`

## File identity

- Repository path: `tests/unit/test_deep_immutability.py`
- File type: unit/regression test
- Layer: test evidence
- Responsibility: Proves that every loaded trust-bearing configuration/policy family has no reachable mutable collection, rejects all relevant in-place mutation operations, isolates caller aliases, and preserves canonical hashes.
- Source SHA256: `325383428aaa376e3b30380bbc8e9a2c925c618e280b254a286aaa15eb80ab1a`

## 1. STEP 7F.1A.4.2 contract delta

- Rejects mutable/non-canonical leaves for both artifact records and proves canonical values, cycles, CRS evidence, immutable copies, Pydantic deep copies, aliases, and hash locks.
- Unsupported leaves are rejected rather than retained or stringified; existing valid JSON shapes, schemas, hashes, and business boundaries remain unchanged.

## 2. Purpose and architectural position

Proves that every loaded trust-bearing configuration/policy family has no reachable mutable collection, rejects all relevant in-place mutation operations, isolates caller aliases, and preserves canonical hashes.

This companion is source-bound. The SHA and complete snapshot below are authoritative for this file; summaries do not replace the implementation.

## 3. Exact imports and dependencies

- `from __future__ import annotations`
- `import operator`
- `from collections.abc import Mapping`
- `from dataclasses import fields, is_dataclass`
- `from pathlib import Path`
- `import pytest`
- `from pydantic import BaseModel`
- `from landscout.common.immutable_mapping import FrozenDict`
- `from landscout.config import AoiConfig, load_scan_config`
- `from landscout.sources.gpu_fr import ( _source_config_sha256, load_gpu_source_config, )`
- `from landscout.sources.ign_bdtopo_fr import load_ign_bdtopo_source_config`
- `from landscout.sources.inpn_protected_areas_fr import ( load_inpn_protected_areas_source_config, )`
- `from landscout.sources.rte_odre_fr import load_rte_odre_source_config`
- `from landscout.stages.aggregate_bess_planning_feature_policy import ( BessPlanningFeatureParcelAggregationArtifactRecord, )`
- `from landscout.stages.apply_bess_planning_feature_policy import ( BessPlanningFeatureApplicationArtifactRecord, )`
- `from landscout.stages.bess_planning_feature_policy import ( _canonical_json_sha256 as _bess_policy_sha256, )`
- `from landscout.stages.bess_planning_feature_policy import ( load_bess_planning_feature_policy_config, )`
- `from landscout.stages.interpret_bess_zoning import ( _policy_sha256 as _written_zoning_policy_sha256, )`
- `from landscout.stages.interpret_bess_zoning import load_bess_zoning_policy_config`
- `from landscout.stages.resolve_planning_feature_codes import ( _profile_sha256 as _cnig_profile_sha256, )`
- `from landscout.stages.resolve_planning_feature_codes import ( load_cnig_feature_code_profile, )`
- `from landscout.stages.road_vehicle_proxy_policy import ( load_ign_road_vehicle_proxy_policy, )`
- `from landscout.stages.structure_planning_regulation import ( PlanningRegulationStructureConfig, load_planning_regulation_structure_config, )`
- `from landscout.stages.structure_planning_regulation import ( _config_sha256 as _structure_config_sha256, )`

## 4. Module declarations

- `ROOT = Path(__file__).parents[2]`
- `SCAN_PATH = ROOT / "configs/scans/bess_muret.yaml"`
- `GPU_PATH = ROOT / "configs/sources/gpu_fr.yaml"`
- `IGN_PATH = ROOT / "configs/sources/ign_bdtopo_fr.yaml"`
- `RTE_PATH = ROOT / "configs/sources/rte_odre_fr.yaml"`
- `INPN_PATH = ROOT / "configs/sources/inpn_protected_areas_fr.yaml"`
- `STRUCTURE_PATH = ROOT / "configs/planning/muret_plu_structure.yaml"`
- `WRITTEN_ZONING_PATH = ROOT / "configs/planning/muret_bess_zoning_policy.yaml"`
- `CNIG_PATH = ROOT / "configs/planning/cnig_plu_2017_feature_codes.yaml"`
- `BESS_POLICY_PATH = ROOT / "configs/planning/muret_bess_cnig_feature_policy.yaml"`

## 5. Classes and lexical ownership

No classes are declared.

## 6. Functions, methods, validators, callbacks, fixtures, and tests

### `_artifact_record_payload`

- Exact signature: `def _artifact_record_payload(role: str, filename: str) -> dict[str, object]:`
- Decorators: none
- Source purpose: No callable docstring; exact source below is authoritative.

### `_loaded_trust_values`

- Exact signature: `def _loaded_trust_values() -> tuple[object, ...]:`
- Decorators: none
- Source purpose: No callable docstring; exact source below is authoritative.

### `_assert_no_reachable_mutable_collection`

- Exact signature: `def _assert_no_reachable_mutable_collection(value: object, *, seen: set[int]) -> None:`
- Decorators: none
- Source purpose: No callable docstring; exact source below is authoritative.

### `test_all_loaded_trust_families_have_no_reachable_mutable_collection`

- Exact signature: `def test_all_loaded_trust_families_have_no_reachable_mutable_collection() -> None:`
- Decorators: none
- Source purpose: No callable docstring; exact source below is authoritative.

### `test_loaded_ordered_sequence_mutation_fails_immediately`

- Exact signature: `def test_loaded_ordered_sequence_mutation_fails_immediately(operation: str) -> None:`
- Decorators: `@pytest.mark.parametrize( "operation", [ "append", "extend", "insert", "pop", "remove", "item_assignment", "slice_assignment", ], )`
- Source purpose: No callable docstring; exact source below is authoritative.

### `test_loaded_mapping_mutation_fails_immediately`

- Exact signature: `def test_loaded_mapping_mutation_fails_immediately(operation: str) -> None:`
- Decorators: `@pytest.mark.parametrize( "operation", [ "item_assignment", "update", "setdefault", "pop", "deletion", "clear", "in_place_union", "backing_attribute", ], )`
- Source purpose: No callable docstring; exact source below is authoritative.

### `test_loaded_set_semantics_mutation_fails_immediately`

- Exact signature: `def test_loaded_set_semantics_mutation_fails_immediately(operation: str) -> None:`
- Decorators: `@pytest.mark.parametrize("operation", ["add", "update", "remove", "discard", "pop"])`
- Source purpose: No callable docstring; exact source below is authoritative.

### `test_nested_input_aliases_cannot_mutate_validated_models`

- Exact signature: `def test_nested_input_aliases_cannot_mutate_validated_models() -> None:`
- Decorators: none
- Source purpose: No callable docstring; exact source below is authoritative.

### `test_canonical_config_and_policy_hashes_match_starting_commit`

- Exact signature: `def test_canonical_config_and_policy_hashes_match_starting_commit() -> None:`
- Decorators: none
- Source purpose: No callable docstring; exact source below is authoritative.

## 6B. STEP 7F.1A.4.2 authoritative changed contracts

This section supersedes older source excerpts for the named callables. The exact complete current file snapshot in section 11 remains authoritative for every declaration.

### `_mapping_values_view`

```python
def _mapping_values_view() -> object:
    source = {"dynamic": "value"}
    return source.values()
```

### `_cyclic_list`

```python
def _cyclic_list() -> object:
    value: list[object] = []
    value.append(value)
    return value
```

### `_non_string_key_mapping`

```python
def _non_string_key_mapping() -> object:
    return {1: "not canonical JSON"}
```

### `_geospatial_artifact_record_payload`

```python
def _geospatial_artifact_record_payload(
    record_type: type[BaseModel],
) -> dict[str, object]:
    crs = {
        "type": "ProjectedCRS",
        "name": "RGF93 v1 / Lambert-93",
        "coordinate_system": {"axis": [{"name": "Easting"}]},
    }
    if record_type is BessPlanningFeatureApplicationArtifactRecord:
        role, filename = "SURFACE_FEATURES", "surface.parquet"
    else:
        role, filename = "PARCELS", "parcels.parquet"
    payload = _artifact_record_payload(role, filename)
    payload["geospatial"] = True
    payload["crs"] = crs
    signature = payload["frame_schema_signature"]
    assert isinstance(signature, dict)
    signature["geometry_column"] = "geometry"
    signature["crs"] = crs
    return payload
```

### `test_artifact_integrity_record_rejects_mutable_bytearray_alias`

```python
def test_artifact_integrity_record_rejects_mutable_bytearray_alias(
    record_type: type[BaseModel],
    role: str,
    filename: str,
) -> None:
    mutable = bytearray(b"abc")
    payload = _artifact_record_payload(role, filename)
    signature = payload["frame_schema_signature"]
    assert isinstance(signature, dict)
    signature["mutable_leaf"] = mutable

    with pytest.raises(ValidationError, match="canonical JSON"):
        record_type.model_validate(payload)
```

### `test_artifact_integrity_record_rejects_noncanonical_nested_leaf`

```python
def test_artifact_integrity_record_rejects_noncanonical_nested_leaf(
    record_type: type[BaseModel],
    role: str,
    filename: str,
    value_factory: Callable[[], object],
) -> None:
    payload = _artifact_record_payload(role, filename)
    signature = payload["frame_schema_signature"]
    assert isinstance(signature, dict)
    signature["nested"] = {"leaf": value_factory()}

    with pytest.raises(ValidationError, match="canonical JSON"):
        record_type.model_validate(payload)
```

### `test_artifact_integrity_record_rejects_mutable_crs_leaf`

```python
def test_artifact_integrity_record_rejects_mutable_crs_leaf(
    record_type: type[BaseModel],
) -> None:
    payload = _geospatial_artifact_record_payload(record_type)
    crs = payload["crs"]
    assert isinstance(crs, dict)
    crs["mutable_leaf"] = bytearray(b"abc")

    with pytest.raises(ValidationError, match="canonical JSON"):
        record_type.model_validate(payload)
```

### `test_artifact_integrity_record_accepts_only_canonical_json_values`

```python
def test_artifact_integrity_record_accepts_only_canonical_json_values(
    record_type: type[BaseModel],
    role: str,
    filename: str,
) -> None:
    payload = _artifact_record_payload(role, filename)
    signature = payload["frame_schema_signature"]
    assert isinstance(signature, dict)
    signature["canonical_values"] = {
        "none": None,
        "string": "value",
        "boolean": True,
        "integer": 3,
        "float": 1.25,
        "ordered": ["list", {"nested": (1, 2)}],
    }

    record = record_type.model_validate(payload)
    retained = record.__dict__["frame_schema_signature"]
    assert retained["canonical_values"]["ordered"] == (
        "list",
        {"nested": (1, 2)},
    )
    expected = _artifact_record_payload(role, filename)
    expected_signature = expected["frame_schema_signature"]
    assert isinstance(expected_signature, dict)
    expected_signature["canonical_values"] = {
        "none": None,
        "string": "value",
        "boolean": True,
        "integer": 3,
        "float": 1.25,
        "ordered": ["list", {"nested": [1, 2]}],
    }
    assert record.model_dump(mode="json", warnings="error") == expected
```

### `test_frozen_mapping_copy_and_deepcopy_preserve_identity`

```python
def test_frozen_mapping_copy_and_deepcopy_preserve_identity() -> None:
    value = load_planning_regulation_structure_config(STRUCTURE_PATH).zone_aliases

    assert copy.copy(value) is value
    assert copy.deepcopy(value) is value
```

### `test_artifact_integrity_record_deep_model_copy_remains_immutable`

```python
def test_artifact_integrity_record_deep_model_copy_remains_immutable(
    record_type: type[BaseModel],
    role: str,
    filename: str,
) -> None:
    del role, filename
    record = record_type.model_validate(
        _geospatial_artifact_record_payload(record_type)
    )

    copied = record.model_copy(deep=True)

    assert copied is not record
    assert (
        copied.__dict__["frame_schema_signature"]
        is record.__dict__["frame_schema_signature"]
    )
    assert copied.__dict__["crs"] is record.__dict__["crs"]
    _assert_no_reachable_mutable_collection(copied, seen=set())
```
## 7. Test inventory

- Exact `test_*` count: 6
- Exact pytest fixture count: 0
- `test_all_loaded_trust_families_have_no_reachable_mutable_collection` — `def test_all_loaded_trust_families_have_no_reachable_mutable_collection() -> None:`
- `test_loaded_ordered_sequence_mutation_fails_immediately` — `def test_loaded_ordered_sequence_mutation_fails_immediately(operation: str) -> None:`
- `test_loaded_mapping_mutation_fails_immediately` — `def test_loaded_mapping_mutation_fails_immediately(operation: str) -> None:`
- `test_loaded_set_semantics_mutation_fails_immediately` — `def test_loaded_set_semantics_mutation_fails_immediately(operation: str) -> None:`
- `test_nested_input_aliases_cannot_mutate_validated_models` — `def test_nested_input_aliases_cannot_mutate_validated_models() -> None:`
- `test_canonical_config_and_policy_hashes_match_starting_commit` — `def test_canonical_config_and_policy_hashes_match_starting_commit() -> None:`

## 8. Deep-immutability and canonical-data contract

- Ordered values remain source-ordered tuples; set domains remain frozensets; retained mappings are recursively copied immutable values.
- Explicit serializers preserve the established plain JSON/Python representation where this file participates in canonical hashing or artifact validation.
- Public source/config boundaries retain reconstruction and revalidation; immutability is not treated as source authority.
- No repr, class name, object identity, memory address, or mutable backing alias is included in canonical hashes.

## 9. Trust, side effects, and business boundary

- Exact filesystem, network, hashing, serialization, CRS/geometry, and in-memory operations are defined only by the complete current source below.
- This file does not by documentation implication create a parcel score, ranking, legal conclusion, access conclusion, grid-capacity conclusion, environmental conclusion, or planning authorization.

## 10. Change impact

A source-byte change invalidates this companion SHA and requires re-auditing model reachability, alias isolation, mutation operations, field serializers, canonical hashes, schema versions, retained public-boundary validation, and permanent regressions.

## 11. Exact complete current file content

The following UTF-8 snapshot is the complete current repository file, not an excerpt. Its raw-byte SHA256 is the value in **File identity**.

```python
from __future__ import annotations

import copy
import operator
from collections.abc import Callable, Mapping
from dataclasses import fields, is_dataclass
from pathlib import Path

import numpy as np
import pytest
from pydantic import BaseModel, ValidationError

from landscout.common.immutable_mapping import FrozenDict
from landscout.config import AoiConfig, load_scan_config
from landscout.sources.gpu_fr import (
    _source_config_sha256,
    load_gpu_source_config,
)
from landscout.sources.ign_bdtopo_fr import load_ign_bdtopo_source_config
from landscout.sources.inpn_protected_areas_fr import (
    load_inpn_protected_areas_source_config,
)
from landscout.sources.rte_odre_fr import load_rte_odre_source_config
from landscout.stages.aggregate_bess_planning_feature_policy import (
    BessPlanningFeatureParcelAggregationArtifactRecord,
)
from landscout.stages.apply_bess_planning_feature_policy import (
    BessPlanningFeatureApplicationArtifactRecord,
)
from landscout.stages.bess_planning_feature_policy import (
    _canonical_json_sha256 as _bess_policy_sha256,
)
from landscout.stages.bess_planning_feature_policy import (
    load_bess_planning_feature_policy_config,
)
from landscout.stages.interpret_bess_zoning import (
    _policy_sha256 as _written_zoning_policy_sha256,
)
from landscout.stages.interpret_bess_zoning import load_bess_zoning_policy_config
from landscout.stages.resolve_planning_feature_codes import (
    _profile_sha256 as _cnig_profile_sha256,
)
from landscout.stages.resolve_planning_feature_codes import (
    load_cnig_feature_code_profile,
)
from landscout.stages.road_vehicle_proxy_policy import (
    load_ign_road_vehicle_proxy_policy,
)
from landscout.stages.structure_planning_regulation import (
    PlanningRegulationStructureConfig,
    load_planning_regulation_structure_config,
)
from landscout.stages.structure_planning_regulation import (
    _config_sha256 as _structure_config_sha256,
)

ROOT = Path(__file__).parents[2]
SCAN_PATH = ROOT / "configs/scans/bess_muret.yaml"
GPU_PATH = ROOT / "configs/sources/gpu_fr.yaml"
IGN_PATH = ROOT / "configs/sources/ign_bdtopo_fr.yaml"
RTE_PATH = ROOT / "configs/sources/rte_odre_fr.yaml"
INPN_PATH = ROOT / "configs/sources/inpn_protected_areas_fr.yaml"
STRUCTURE_PATH = ROOT / "configs/planning/muret_plu_structure.yaml"
WRITTEN_ZONING_PATH = ROOT / "configs/planning/muret_bess_zoning_policy.yaml"
CNIG_PATH = ROOT / "configs/planning/cnig_plu_2017_feature_codes.yaml"
BESS_POLICY_PATH = ROOT / "configs/planning/muret_bess_cnig_feature_policy.yaml"

ARTIFACT_RECORD_CASES = (
    (
        BessPlanningFeatureApplicationArtifactRecord,
        "RELATIONS",
        "relations.parquet",
    ),
    (
        BessPlanningFeatureParcelAggregationArtifactRecord,
        "RELATION_ASSESSMENTS",
        "relation_assessments.parquet",
    ),
)


class _MutableLeaf:
    def __init__(self) -> None:
        self.values: list[str] = ["caller-owned"]


class _StringSubclass(str):
    pass


class _IntegerSubclass(int):
    pass


def _artifact_record_payload(role: str, filename: str) -> dict[str, object]:
    return {
        "artifact_role": role,
        "filename": filename,
        "row_count": 1,
        "size_bytes": 1,
        "sha256": "a" * 64,
        "frame_schema_signature": {
            "columns": ["value"],
            "dtypes": ["int64"],
            "index_class": "pandas.core.indexes.range.RangeIndex",
            "index_names": [None],
            "index_level_dtypes": ["int64"],
        },
        "geospatial": False,
        "crs": None,
    }


def _mapping_values_view() -> object:
    source = {"dynamic": "value"}
    return source.values()


def _cyclic_list() -> object:
    value: list[object] = []
    value.append(value)
    return value


def _non_string_key_mapping() -> object:
    return {1: "not canonical JSON"}


def _geospatial_artifact_record_payload(
    record_type: type[BaseModel],
) -> dict[str, object]:
    crs = {
        "type": "ProjectedCRS",
        "name": "RGF93 v1 / Lambert-93",
        "coordinate_system": {"axis": [{"name": "Easting"}]},
    }
    if record_type is BessPlanningFeatureApplicationArtifactRecord:
        role, filename = "SURFACE_FEATURES", "surface.parquet"
    else:
        role, filename = "PARCELS", "parcels.parquet"
    payload = _artifact_record_payload(role, filename)
    payload["geospatial"] = True
    payload["crs"] = crs
    signature = payload["frame_schema_signature"]
    assert isinstance(signature, dict)
    signature["geometry_column"] = "geometry"
    signature["crs"] = crs
    return payload


@pytest.mark.parametrize("record_type,role,filename", ARTIFACT_RECORD_CASES)
def test_artifact_integrity_record_rejects_mutable_bytearray_alias(
    record_type: type[BaseModel],
    role: str,
    filename: str,
) -> None:
    mutable = bytearray(b"abc")
    payload = _artifact_record_payload(role, filename)
    signature = payload["frame_schema_signature"]
    assert isinstance(signature, dict)
    signature["mutable_leaf"] = mutable

    with pytest.raises(ValidationError, match="canonical JSON"):
        record_type.model_validate(payload)


@pytest.mark.parametrize("record_type,role,filename", ARTIFACT_RECORD_CASES)
@pytest.mark.parametrize(
    "value_factory",
    [
        lambda: b"bytes",
        lambda: _MutableLeaf(),
        _mapping_values_view,
        lambda: {"not", "json"},
        lambda: frozenset({"not", "json"}),
        lambda: np.array([1, 2]),
        lambda: np.int64(1),
        lambda: np.float64(1.5),
        lambda: _StringSubclass("value"),
        lambda: _IntegerSubclass(1),
        _non_string_key_mapping,
        _cyclic_list,
        lambda: float("nan"),
        lambda: float("inf"),
        lambda: float("-inf"),
    ],
    ids=(
        "bytes",
        "mutable-custom-object",
        "dynamic-values-view",
        "set",
        "frozenset",
        "numpy-array",
        "numpy-integer",
        "numpy-float",
        "string-subclass",
        "integer-subclass",
        "non-string-mapping-key",
        "cyclic-list",
        "nan",
        "positive-infinity",
        "negative-infinity",
    ),
)
def test_artifact_integrity_record_rejects_noncanonical_nested_leaf(
    record_type: type[BaseModel],
    role: str,
    filename: str,
    value_factory: Callable[[], object],
) -> None:
    payload = _artifact_record_payload(role, filename)
    signature = payload["frame_schema_signature"]
    assert isinstance(signature, dict)
    signature["nested"] = {"leaf": value_factory()}

    with pytest.raises(ValidationError, match="canonical JSON"):
        record_type.model_validate(payload)


@pytest.mark.parametrize("record_type", [case[0] for case in ARTIFACT_RECORD_CASES])
def test_artifact_integrity_record_rejects_mutable_crs_leaf(
    record_type: type[BaseModel],
) -> None:
    payload = _geospatial_artifact_record_payload(record_type)
    crs = payload["crs"]
    assert isinstance(crs, dict)
    crs["mutable_leaf"] = bytearray(b"abc")

    with pytest.raises(ValidationError, match="canonical JSON"):
        record_type.model_validate(payload)


@pytest.mark.parametrize("record_type,role,filename", ARTIFACT_RECORD_CASES)
def test_artifact_integrity_record_accepts_only_canonical_json_values(
    record_type: type[BaseModel],
    role: str,
    filename: str,
) -> None:
    payload = _artifact_record_payload(role, filename)
    signature = payload["frame_schema_signature"]
    assert isinstance(signature, dict)
    signature["canonical_values"] = {
        "none": None,
        "string": "value",
        "boolean": True,
        "integer": 3,
        "float": 1.25,
        "ordered": ["list", {"nested": (1, 2)}],
    }

    record = record_type.model_validate(payload)
    retained = record.__dict__["frame_schema_signature"]
    assert retained["canonical_values"]["ordered"] == (
        "list",
        {"nested": (1, 2)},
    )
    expected = _artifact_record_payload(role, filename)
    expected_signature = expected["frame_schema_signature"]
    assert isinstance(expected_signature, dict)
    expected_signature["canonical_values"] = {
        "none": None,
        "string": "value",
        "boolean": True,
        "integer": 3,
        "float": 1.25,
        "ordered": ["list", {"nested": [1, 2]}],
    }
    assert record.model_dump(mode="json", warnings="error") == expected


def test_frozen_mapping_copy_and_deepcopy_preserve_identity() -> None:
    value = load_planning_regulation_structure_config(STRUCTURE_PATH).zone_aliases

    assert copy.copy(value) is value
    assert copy.deepcopy(value) is value


@pytest.mark.parametrize("record_type,role,filename", ARTIFACT_RECORD_CASES)
def test_artifact_integrity_record_deep_model_copy_remains_immutable(
    record_type: type[BaseModel],
    role: str,
    filename: str,
) -> None:
    del role, filename
    record = record_type.model_validate(
        _geospatial_artifact_record_payload(record_type)
    )

    copied = record.model_copy(deep=True)

    assert copied is not record
    assert (
        copied.__dict__["frame_schema_signature"]
        is record.__dict__["frame_schema_signature"]
    )
    assert copied.__dict__["crs"] is record.__dict__["crs"]
    _assert_no_reachable_mutable_collection(copied, seen=set())


def _loaded_trust_values() -> tuple[object, ...]:
    return (
        load_scan_config(SCAN_PATH),
        load_gpu_source_config(GPU_PATH),
        load_ign_bdtopo_source_config(IGN_PATH),
        load_rte_odre_source_config(RTE_PATH),
        load_inpn_protected_areas_source_config(INPN_PATH),
        load_planning_regulation_structure_config(STRUCTURE_PATH),
        load_bess_zoning_policy_config(WRITTEN_ZONING_PATH),
        load_cnig_feature_code_profile(CNIG_PATH),
        load_bess_planning_feature_policy_config(BESS_POLICY_PATH),
        load_ign_road_vehicle_proxy_policy(),
        BessPlanningFeatureApplicationArtifactRecord.model_validate(
            _artifact_record_payload("RELATIONS", "relations.parquet")
        ),
        BessPlanningFeatureParcelAggregationArtifactRecord.model_validate(
            _artifact_record_payload(
                "RELATION_ASSESSMENTS", "relation_assessments.parquet"
            )
        ),
    )


def _assert_no_reachable_mutable_collection(value: object, *, seen: set[int]) -> None:
    if value is None or isinstance(value, (str, bytes, int, float, bool, Path)):
        return
    identity = id(value)
    if identity in seen:
        return
    seen.add(identity)
    assert not isinstance(value, (list, dict, set, bytearray))
    if isinstance(value, BaseModel):
        for field_name in type(value).model_fields:
            _assert_no_reachable_mutable_collection(
                getattr(value, field_name), seen=seen
            )
        return
    if is_dataclass(value) and not isinstance(value, type):
        for field in fields(value):
            _assert_no_reachable_mutable_collection(
                getattr(value, field.name), seen=seen
            )
        return
    if isinstance(value, Mapping):
        for key, member in value.items():
            _assert_no_reachable_mutable_collection(key, seen=seen)
            _assert_no_reachable_mutable_collection(member, seen=seen)
        return
    if isinstance(value, (tuple, frozenset)):
        for member in value:
            _assert_no_reachable_mutable_collection(member, seen=seen)


def test_all_loaded_trust_families_have_no_reachable_mutable_collection() -> None:
    for value in _loaded_trust_values():
        _assert_no_reachable_mutable_collection(value, seen=set())


@pytest.mark.parametrize(
    "operation",
    [
        "append",
        "extend",
        "insert",
        "pop",
        "remove",
        "item_assignment",
        "slice_assignment",
    ],
)
def test_loaded_ordered_sequence_mutation_fails_immediately(operation: str) -> None:
    values = load_scan_config(SCAN_PATH).scan_config.aoi.commune_codes

    with pytest.raises((AttributeError, TypeError)):
        if operation == "append":
            values.append("75056")
        elif operation == "extend":
            values.extend(("75056",))
        elif operation == "insert":
            values.insert(0, "75056")
        elif operation == "pop":
            values.pop()
        elif operation == "remove":
            values.remove("31395")
        elif operation == "item_assignment":
            operator.setitem(values, 0, "75056")
        else:
            operator.setitem(values, slice(0, 1), ("75056",))


@pytest.mark.parametrize(
    "operation",
    [
        "item_assignment",
        "update",
        "setdefault",
        "pop",
        "deletion",
        "clear",
        "in_place_union",
        "backing_attribute",
    ],
)
def test_loaded_mapping_mutation_fails_immediately(operation: str) -> None:
    aliases = load_planning_regulation_structure_config(STRUCTURE_PATH).zone_aliases
    assert isinstance(aliases, FrozenDict)

    with pytest.raises(TypeError, match="frozen|assignment|deletion"):
        if operation == "item_assignment":
            operator.setitem(aliases, "UX", "U")
        elif operation == "update":
            aliases.update({"UX": "U"})
        elif operation == "setdefault":
            aliases.setdefault("UX", "U")
        elif operation == "pop":
            aliases.pop("Ua")
        elif operation == "deletion":
            operator.delitem(aliases, "Ua")
        elif operation == "clear":
            aliases.clear()
        elif operation == "in_place_union":
            operator.ior(aliases, {"UX": "U"})
        else:
            aliases._data = {"UX": "U"}


@pytest.mark.parametrize("operation", ["add", "update", "remove", "discard", "pop"])
def test_loaded_set_semantics_mutation_fails_immediately(operation: str) -> None:
    values = load_ign_road_vehicle_proxy_policy().nature.general_motor_road

    with pytest.raises(AttributeError):
        getattr(values, operation)("Invented")


def test_nested_input_aliases_cannot_mutate_validated_models() -> None:
    commune_payload = {"commune_codes": ["31395"]}
    aoi = AoiConfig.model_validate(commune_payload)
    commune_payload["commune_codes"].append("75056")
    assert aoi.commune_codes == ("31395",)

    loaded = load_planning_regulation_structure_config(STRUCTURE_PATH)
    structure_payload = loaded.model_dump(mode="json", warnings="error")
    aliases = structure_payload["zone_aliases"]
    topics = structure_payload["topics"]
    assert isinstance(aliases, dict)
    assert isinstance(topics, dict)
    first_topic = next(iter(topics))
    first_terms = topics[first_topic]
    assert isinstance(first_terms, list)
    reconstructed = PlanningRegulationStructureConfig.model_validate(structure_payload)
    aliases["UX"] = "U"
    first_terms.append("caller mutation")
    assert "UX" not in reconstructed.zone_aliases
    assert "caller mutation" not in reconstructed.topics[first_topic]


def test_canonical_config_and_policy_hashes_match_starting_commit() -> None:
    structure = load_planning_regulation_structure_config(STRUCTURE_PATH)
    written_zoning = load_bess_zoning_policy_config(WRITTEN_ZONING_PATH)
    cnig = load_cnig_feature_code_profile(CNIG_PATH)
    bess_policy = load_bess_planning_feature_policy_config(BESS_POLICY_PATH)
    gpu = load_gpu_source_config(GPU_PATH)

    assert (
        _structure_config_sha256(structure)
        == "13d028fe4b58d30929ff9fdedae90e2cc95983a3296f2f83c2817d0da381107a"
    )
    assert (
        _written_zoning_policy_sha256(written_zoning)
        == "ef1f7cd0f5589e9a07428d25cd2b1a844e7cd49fb6db359951eb6c812c767586"
    )
    assert (
        _cnig_profile_sha256(cnig)
        == "5611b814eb4bc057578b908c6505094f9df5d2c2bf4ca126629b1362983c47ee"
    )
    assert (
        _bess_policy_sha256(bess_policy.model_dump(mode="json", warnings="error"))
        == "1cfca0eb3d777e9b6604748e8a81609abe7b728de8d0695711cd569180df6489"
    )
    assert (
        _source_config_sha256(gpu)
        == "c076a8fddbee2323f177b612101eb4d1b7fabcb578bac9509567205187ac7df2"
    )
```

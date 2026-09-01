from __future__ import annotations

import operator
from collections.abc import Mapping
from dataclasses import fields, is_dataclass
from pathlib import Path

import pytest
from pydantic import BaseModel

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

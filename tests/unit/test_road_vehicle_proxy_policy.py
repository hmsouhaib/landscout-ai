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
            lambda payload: payload["references"]["navigation"].update(
                unexpected=True
            ),
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
def test_unsupported_schema_version_is_rejected(
    tmp_path: Path, version: int
) -> None:
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
def test_both_evidence_references_are_required(
    tmp_path: Path, reference: str
) -> None:
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
    assert all(sum(value in group for group in groups) == 1 for value in set().union(*groups))


def test_asset_state_group_overlap_is_rejected(tmp_path: Path) -> None:
    payload = _payload()
    payload["source_values"]["asset_state"]["under_construction"] = [
        "En projet"
    ]

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


def test_project_geometry_rule_has_exact_precedence_position() -> None:
    policy = load_ign_road_vehicle_proxy_policy()

    fictitious = policy.decision_precedence.index("FICTITIOUS_GEOMETRY")
    project = policy.decision_precedence.index(
        "PROJECT_GEOMETRY_NOT_SIGNIFICANT"
    )
    not_in_service = policy.decision_precedence.index("NOT_IN_SERVICE")
    assert fictitious < project < not_in_service
    assert len(policy.decision_precedence) == 16


@pytest.mark.parametrize("mutation", ["missing", "extra", "wrong"])
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
def test_non_mapping_yaml_has_controlled_error(
    tmp_path: Path, payload: object
) -> None:
    with pytest.raises(IgnRoadVehicleProxyPolicyError):
        _load_payload(tmp_path, payload)


def test_missing_file_has_controlled_error(tmp_path: Path) -> None:
    with pytest.raises(IgnRoadVehicleProxyPolicyError):
        load_ign_road_vehicle_proxy_policy(tmp_path / "missing.yaml")

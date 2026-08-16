"""Compile the versioned IGN general-vehicle proxy evidence policy."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path
from typing import Annotated, Literal, Self

import yaml  # type: ignore[import-untyped]
from pydantic import (
    AfterValidator,
    BaseModel,
    ConfigDict,
    Field,
    StrictFloat,
    StrictInt,
    StringConstraints,
    model_validator,
)

__all__ = [
    "IgnRoadVehicleProxyPolicy",
    "IgnRoadVehicleProxyPolicyError",
    "load_ign_road_vehicle_proxy_policy",
]

_DEFAULT_POLICY_PATH = (
    Path(__file__).resolve().parents[3]
    / "configs"
    / "access"
    / "ign_bdtopo_vehicle_proxy_policy.yaml"
)
_POLICY_ID = "ign_bdtopo_general_vehicle_proxy_v1"
_POLICY_SCOPE = "OFFICIAL_IGN_CAR_ROUTING_EVIDENCE_ONLY"
_EXPECTED_PRECEDENCE = (
    "FICTITIOUS_GEOMETRY",
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


class IgnRoadVehicleProxyPolicyError(ValueError):
    """Raised when the IGN road vehicle-proxy policy is unsafe or invalid."""


def _exact_string(value: str) -> str:
    if value != value.strip():
        raise ValueError("policy strings must not contain edge whitespace")
    return value


_ExactString = Annotated[
    str,
    StringConstraints(strict=True, min_length=1),
    AfterValidator(_exact_string),
]
_NonEmptyStrings = Annotated[tuple[_ExactString, ...], Field(min_length=1)]


class _StrictPolicyModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


def _require_unique(values: tuple[str, ...], label: str) -> None:
    if len(values) != len(set(values)):
        raise ValueError(f"{label} contains duplicate source values")


def _require_disjoint(groups: tuple[tuple[str, ...], ...], label: str) -> None:
    flattened = tuple(value for group in groups for value in group)
    if len(flattened) != len(set(flattened)):
        raise ValueError(f"{label} source groups overlap")


class _ReferenceConfig(_StrictPolicyModel):
    publisher: Literal["IGN"]
    title: Literal["Geoplateforme - Calcul d'itineraire"]
    revision: Literal["2026-05-27"]
    checked_on: Literal["2026-08-16"]
    vehicle_scope: Literal["LIGHT_VEHICLE_AND_GENERAL_CAR_NETWORK"]
    heavy_vehicle_access: Literal["NOT_PROVEN"]


class _ClassesConfig(_StrictPolicyModel):
    general_vehicle_proxy: Literal["GENERAL_VEHICLE_PROXY"]
    limited_vehicle_proxy: Literal["LIMITED_VEHICLE_PROXY"]
    restricted_review: Literal["RESTRICTED_REVIEW"]
    not_general_vehicle_proxy: Literal["NOT_GENERAL_VEHICLE_PROXY"]
    not_distance_proxy: Literal["NOT_DISTANCE_PROXY"]
    unknown_review: Literal["UNKNOWN_REVIEW"]


class _AssetStateConfig(_StrictPolicyModel):
    in_service: _NonEmptyStrings
    known_not_in_service: _NonEmptyStrings

    @model_validator(mode="after")
    def _valid_groups(self) -> Self:
        _require_unique(self.in_service, "in_service")
        _require_unique(self.known_not_in_service, "known_not_in_service")
        _require_disjoint(
            (self.in_service, self.known_not_in_service), "asset_state"
        )
        return self


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


class _SourceValuesConfig(_StrictPolicyModel):
    asset_state: _AssetStateConfig
    light_vehicle_access: _LightVehicleAccessConfig
    nature: _RoadNatureConfig
    known_restriction_review: _NonEmptyStrings
    limited_importance: _NonEmptyStrings
    width_below_m: Annotated[StrictFloat, Field(gt=0, allow_inf_nan=False)]

    @model_validator(mode="after")
    def _valid_values(self) -> Self:
        _require_unique(
            self.known_restriction_review, "known_restriction_review"
        )
        _require_unique(self.limited_importance, "limited_importance")
        if self.limited_importance != ("6",):
            raise ValueError("limited_importance must contain exactly source value '6'")
        return self


class _DecisionOutcomesConfig(_StrictPolicyModel):
    fictitious_geometry: Literal["NOT_DISTANCE_PROXY"]
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


class _PolicyConfig(_StrictPolicyModel):
    policy_id: _ExactString
    schema_version: StrictInt
    scope: _ExactString
    reference: _ReferenceConfig
    classes: _ClassesConfig
    source_values: _SourceValuesConfig
    decision_precedence: _NonEmptyStrings
    decision_outcomes: _DecisionOutcomesConfig

    @model_validator(mode="after")
    def _valid_identity_and_precedence(self) -> Self:
        if self.policy_id != _POLICY_ID:
            raise ValueError("policy_id is not the approved v1 policy identity")
        if self.schema_version != 1:
            raise ValueError("schema_version must be exactly 1")
        if self.scope != _POLICY_SCOPE:
            raise ValueError("scope is not the approved official IGN evidence scope")
        if self.decision_precedence != _EXPECTED_PRECEDENCE:
            raise ValueError("decision_precedence differs from approved v1 order")
        return self


@dataclass(frozen=True)
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


@dataclass(frozen=True)
class _CompiledAssetState:
    in_service: frozenset[str]
    known_not_in_service: frozenset[str]


@dataclass(frozen=True)
class _CompiledLightVehicleAccess:
    open: frozenset[str]
    toll: frozenset[str]
    rights_restricted: frozenset[str]
    physically_impossible: frozenset[str]


@dataclass(frozen=True)
class _CompiledRoadNature:
    general_motor_road: frozenset[str]
    limited_motor_proxy: frozenset[str]
    non_general_vehicle: frozenset[str]
    special_review: frozenset[str]


@dataclass(frozen=True)
class _CompiledDecisionOutcomes:
    fictitious_geometry: str
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


@dataclass(frozen=True)
class IgnRoadVehicleProxyPolicy:
    """Immutable policy evidence compiled from the exact checked-in YAML bytes."""

    policy_id: str
    schema_version: int
    scope: str
    publisher: str
    source_reference_title: str
    source_reference_revision: str
    evidence_checked_on: str
    vehicle_scope: str
    heavy_vehicle_access: str
    classes: _CompiledClasses
    asset_state: _CompiledAssetState
    light_vehicle_access: _CompiledLightVehicleAccess
    nature: _CompiledRoadNature
    known_restriction_review: frozenset[str]
    limited_importance: frozenset[str]
    width_below_m: float
    decision_precedence: tuple[str, ...]
    decision_outcomes: _CompiledDecisionOutcomes
    config_sha256: str


class _UniqueKeyLoader(yaml.SafeLoader):
    pass


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


_UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    _construct_unique_mapping,
)


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
        publisher=config.reference.publisher,
        source_reference_title=config.reference.title,
        source_reference_revision=config.reference.revision,
        evidence_checked_on=config.reference.checked_on,
        vehicle_scope=config.reference.vehicle_scope,
        heavy_vehicle_access=config.reference.heavy_vehicle_access,
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
            known_not_in_service=frozenset(
                source_values.asset_state.known_not_in_service
            ),
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
        limited_importance=frozenset(source_values.limited_importance),
        width_below_m=source_values.width_below_m,
        decision_precedence=config.decision_precedence,
        decision_outcomes=_CompiledDecisionOutcomes(
            fictitious_geometry=outcomes.fictitious_geometry,
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

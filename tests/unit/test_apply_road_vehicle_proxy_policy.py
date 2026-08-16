from __future__ import annotations

from copy import deepcopy
from dataclasses import FrozenInstanceError
from pathlib import Path
from typing import Any, cast
from unittest.mock import patch

import geopandas as gpd  # type: ignore[import-untyped]
import numpy as np
import pandas as pd  # type: ignore[import-untyped]
import pytest
from geopandas.testing import assert_geodataframe_equal
from shapely.geometry import LineString, Polygon

from landscout import stages
from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_source_config,
)
from landscout.stages.apply_road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyApplicationError,
    IgnRoadVehicleProxyApplicationResult,
    apply_ign_road_vehicle_proxy_policy,
)
from landscout.stages.normalize_access_ign import (
    IgnRoadNormalizationError,
    NormalizedIgnRoadData,
)
from landscout.stages.road_vehicle_proxy_policy import (
    load_ign_road_vehicle_proxy_policy,
)

SOURCE_CONFIG = load_ign_bdtopo_source_config()
POLICY_PATH = Path("configs/access/ign_bdtopo_vehicle_proxy_policy.yaml")
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


def _roads(*overrides: dict[str, object]) -> gpd.GeoDataFrame:
    mutations = overrides or ({},)
    rows: list[dict[str, object]] = []
    for number, mutation in enumerate(mutations, start=1):
        row = _base_row(number)
        row.update(mutation)
        rows.append(row)
    return gpd.GeoDataFrame(rows, geometry="geometry", crs="EPSG:2154")


def _source() -> IgnBdTopoRoadData:
    return IgnBdTopoRoadData(
        extraction=cast(Any, None),
        road_segments=_roads(),
        road_segments_summary=cast(Any, None),
    )


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


def _row(
    overrides: dict[str, object] | None = None,
) -> pd.Series:
    result = _apply(_roads(overrides or {}))
    return result.roads.iloc[0]


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


def test_wrong_source_type_has_controlled_error() -> None:
    with pytest.raises(IgnRoadVehicleProxyApplicationError):
        apply_ign_road_vehicle_proxy_policy(
            cast(Any, object()), SOURCE_CONFIG
        )


def test_wrong_source_config_type_has_controlled_error() -> None:
    with pytest.raises(IgnRoadVehicleProxyApplicationError):
        apply_ign_road_vehicle_proxy_policy(
            _source(), cast(Any, object())
        )


def test_malformed_policy_path_has_controlled_error(tmp_path: Path) -> None:
    path = tmp_path / "policy.yaml"
    path.write_text("policy_id: [", encoding="utf-8")

    with patch(
        "landscout.stages.apply_road_vehicle_proxy_policy.normalize_ign_roads",
        return_value=NormalizedIgnRoadData(_roads()),
    ), pytest.raises(IgnRoadVehicleProxyApplicationError):
        apply_ign_road_vehicle_proxy_policy(_source(), SOURCE_CONFIG, path)


def test_source_complete_normalization_is_invoked_exactly_once() -> None:
    normalized = NormalizedIgnRoadData(_roads())
    with patch(
        "landscout.stages.apply_road_vehicle_proxy_policy.normalize_ign_roads",
        return_value=normalized,
    ) as validator:
        apply_ign_road_vehicle_proxy_policy(_source(), SOURCE_CONFIG)

    validator.assert_called_once()


def test_normalization_failure_stops_policy_loading() -> None:
    with patch(
        "landscout.stages.apply_road_vehicle_proxy_policy.normalize_ign_roads",
        side_effect=IgnRoadNormalizationError("bad source"),
    ), patch(
        "landscout.stages.apply_road_vehicle_proxy_policy.load_ign_road_vehicle_proxy_policy"
    ) as policy_loader, pytest.raises(IgnRoadVehicleProxyApplicationError):
        apply_ign_road_vehicle_proxy_policy(_source(), SOURCE_CONFIG)

    policy_loader.assert_not_called()


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


@pytest.mark.parametrize(
    ("status", "geometry"),
    [
        ("NULL", None),
        ("EMPTY", LineString()),
        ("INVALID", LineString([(0, 0), (1, 1), (0, 1), (1, 0)])),
    ],
)
def test_non_valid_geometry_uses_technical_gate(
    status: str, geometry: object
) -> None:
    row = _row({"geometry_status": status, "geometry": geometry})

    assert row.road_proxy_primary_rule == "SOURCE_GEOMETRY_NOT_VALID"
    assert row.road_proxy_class == "NOT_DISTANCE_PROXY"
    assert row.road_proxy_rule_trace_json == '["SOURCE_GEOMETRY_NOT_VALID"]'


def test_unknown_geometry_status_is_rejected() -> None:
    with pytest.raises(IgnRoadVehicleProxyApplicationError):
        _apply(_roads({"geometry_status": "BROKEN"}))


@pytest.mark.parametrize(
    ("overrides", "rule", "expected_class"),
    [
        ({"fictitious_raw": True}, "FICTITIOUS_GEOMETRY", "NOT_DISTANCE_PROXY"),
        (
            {"asset_status_raw": "En projet"},
            "PROJECT_GEOMETRY_NOT_SIGNIFICANT",
            "NOT_DISTANCE_PROXY",
        ),
        (
            {"asset_status_raw": "En construction"},
            "NOT_IN_SERVICE",
            "NOT_GENERAL_VEHICLE_PROXY",
        ),
        (
            {"light_vehicle_access_raw": "Physiquement impossible"},
            "PHYSICALLY_IMPOSSIBLE",
            "NOT_GENERAL_VEHICLE_PROXY",
        ),
        (
            {"nature_raw": "Escalier"},
            "NON_GENERAL_VEHICLE_NATURE",
            "NOT_GENERAL_VEHICLE_PROXY",
        ),
        (
            {"light_vehicle_access_raw": "Restreint aux ayants droit"},
            "RIGHTS_RESTRICTED",
            "RESTRICTED_REVIEW",
        ),
        ({"private_raw": 1.0}, "PRIVATE_ROAD", "RESTRICTED_REVIEW"),
        (
            {"closure_period_raw": "Fermeture hivernale"},
            "TEMPORAL_CLOSURE",
            "RESTRICTED_REVIEW",
        ),
        (
            {"restriction_nature_raw": "Plot amovible"},
            "KNOWN_RESTRICTION",
            "RESTRICTED_REVIEW",
        ),
        (
            {"restriction_nature_raw": "Nouvelle restriction"},
            "OTHER_RECORDED_RESTRICTION",
            "RESTRICTED_REVIEW",
        ),
        (
            {"nature_raw": "Bac ou liaison maritime"},
            "SPECIAL_NATURE",
            "RESTRICTED_REVIEW",
        ),
        ({"nature_raw": "Chemin"}, "LIMITED_NATURE", "LIMITED_VEHICLE_PROXY"),
        ({"importance_raw": "6"}, "IMPORTANCE_6", "LIMITED_VEHICLE_PROXY"),
        (
            {"carriageway_width_raw": 2.8},
            "NARROW_CARRIAGEWAY",
            "LIMITED_VEHICLE_PROXY",
        ),
        ({}, "OPEN_OR_TOLL", "GENERAL_VEHICLE_PROXY"),
        ({"nature_raw": "Future"}, "UNKNOWN", "UNKNOWN_REVIEW"),
    ],
)
def test_each_policy_rule_selects_approved_outcome(
    overrides: dict[str, object], rule: str, expected_class: str
) -> None:
    row = _row(overrides)

    assert row.road_proxy_primary_rule == rule
    assert row.road_proxy_class == expected_class


@pytest.mark.parametrize(
    ("overrides", "rule"),
    [
        ({"fictitious_raw": True, "private_raw": 1.0}, "FICTITIOUS_GEOMETRY"),
        (
            {
                "asset_status_raw": "En projet",
                "light_vehicle_access_raw": "Physiquement impossible",
            },
            "PROJECT_GEOMETRY_NOT_SIGNIFICANT",
        ),
        (
            {
                "light_vehicle_access_raw": "Physiquement impossible",
                "private_raw": 1.0,
            },
            "PHYSICALLY_IMPOSSIBLE",
        ),
        ({"private_raw": 1.0, "carriageway_width_raw": 2.5}, "PRIVATE_ROAD"),
        (
            {"closure_period_raw": "Hiver", "nature_raw": "Chemin"},
            "TEMPORAL_CLOSURE",
        ),
        (
            {
                "restriction_nature_raw": "Plot amovible",
                "nature_raw": "Bac ou liaison maritime",
            },
            "KNOWN_RESTRICTION",
        ),
        ({"nature_raw": "Chemin", "importance_raw": "6"}, "LIMITED_NATURE"),
        (
            {"importance_raw": "6", "carriageway_width_raw": 2.5},
            "IMPORTANCE_6",
        ),
    ],
)
def test_policy_precedence_conflicts_select_first_rule(
    overrides: dict[str, object], rule: str
) -> None:
    assert _row(overrides).road_proxy_primary_rule == rule


@pytest.mark.parametrize(
    ("field", "value", "expected_rule"),
    [
        ("fictitious_raw", False, "OPEN_OR_TOLL"),
        ("fictitious_raw", np.bool_(True), "FICTITIOUS_GEOMETRY"),
        ("fictitious_raw", None, "UNKNOWN"),
        ("fictitious_raw", "true", "UNKNOWN"),
        ("private_raw", False, "OPEN_OR_TOLL"),
        ("private_raw", True, "PRIVATE_ROAD"),
        ("private_raw", 0, "OPEN_OR_TOLL"),
        ("private_raw", 1, "PRIVATE_ROAD"),
        ("private_raw", 0.0, "OPEN_OR_TOLL"),
        ("private_raw", 1.0, "PRIVATE_ROAD"),
        ("private_raw", None, "UNKNOWN"),
        ("private_raw", 2, "UNKNOWN"),
        ("private_raw", "1", "UNKNOWN"),
    ],
)
def test_boolean_like_source_values_are_parsed_without_coercion(
    field: str, value: object, expected_rule: str
) -> None:
    assert _row({field: value}).road_proxy_primary_rule == expected_rule


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("asset_status_raw", "Future"),
        ("nature_raw", "Future"),
        ("light_vehicle_access_raw", "Future"),
        ("importance_raw", "7"),
        ("importance_raw", 6),
    ],
)
def test_unknown_critical_vocabulary_never_uses_general_fallback(
    field: str, value: object
) -> None:
    row = _row({field: value})

    assert row.road_proxy_primary_rule == "UNKNOWN"
    assert row.road_proxy_class == "UNKNOWN_REVIEW"
    assert field in row.road_proxy_unknown_fields_json


@pytest.mark.parametrize(
    ("value", "expected_rule"),
    [
        (None, "OPEN_OR_TOLL"),
        (float("nan"), "OPEN_OR_TOLL"),
        (2.9, "OPEN_OR_TOLL"),
        (2.899999, "NARROW_CARRIAGEWAY"),
        (0.0, "UNKNOWN"),
        (-1.0, "UNKNOWN"),
        (float("inf"), "UNKNOWN"),
        ("2.8", "UNKNOWN"),
        (True, "UNKNOWN"),
    ],
)
def test_width_contract(value: object, expected_rule: str) -> None:
    assert _row({"carriageway_width_raw": value}).road_proxy_primary_rule == (
        expected_rule
    )


@pytest.mark.parametrize(
    ("field", "value", "expected_rule"),
    [
        ("closure_period_raw", None, "OPEN_OR_TOLL"),
        ("closure_period_raw", "Hiver", "TEMPORAL_CLOSURE"),
        ("closure_period_raw", " ", "UNKNOWN"),
        ("closure_period_raw", 1, "UNKNOWN"),
        ("restriction_nature_raw", None, "OPEN_OR_TOLL"),
        ("restriction_nature_raw", "Plot amovible", "KNOWN_RESTRICTION"),
        (
            "restriction_nature_raw",
            "Restriction nouvelle",
            "OTHER_RECORDED_RESTRICTION",
        ),
        ("restriction_nature_raw", "", "UNKNOWN"),
        ("restriction_nature_raw", 1, "UNKNOWN"),
    ],
)
def test_optional_restriction_source_contract(
    field: str, value: object, expected_rule: str
) -> None:
    assert _row({field: value}).road_proxy_primary_rule == expected_rule


def test_every_configured_known_restriction_is_applied() -> None:
    policy = load_ign_road_vehicle_proxy_policy()
    for restriction in policy.known_restriction_review:
        assert _row(
            {"restriction_nature_raw": restriction}
        ).road_proxy_primary_rule == "KNOWN_RESTRICTION"


def test_general_fallback_requires_complete_positive_evidence_and_tracks_toll() -> None:
    open_row = _row()
    toll_row = _row({"light_vehicle_access_raw": "A péage"})

    assert open_row.road_proxy_class == "GENERAL_VEHICLE_PROXY"
    assert not open_row.road_proxy_toll_evidence
    assert toll_row.road_proxy_class == "GENERAL_VEHICLE_PROXY"
    assert toll_row.road_proxy_toll_evidence


@pytest.mark.parametrize(
    "overrides",
    [
        {"nature_raw": "Future"},
        {"private_raw": None},
        {"importance_raw": "7"},
        {"carriageway_width_raw": "wide"},
    ],
)
def test_open_access_does_not_hide_unresolved_evidence(
    overrides: dict[str, object]
) -> None:
    assert _row(overrides).road_proxy_primary_rule == "UNKNOWN"


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


def test_known_higher_rule_remains_primary_while_unknown_is_traced() -> None:
    row = _row({"private_raw": 1.0, "importance_raw": "7"})

    assert row.road_proxy_primary_rule == "PRIVATE_ROAD"
    assert row.road_proxy_rule_trace_json == '["PRIVATE_ROAD","UNKNOWN"]'
    assert row.road_proxy_unknown_fields_json == '["importance_raw"]'


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


def test_policy_path_must_be_path_or_none() -> None:
    with pytest.raises(IgnRoadVehicleProxyApplicationError):
        apply_ign_road_vehicle_proxy_policy(
            _source(), SOURCE_CONFIG, cast(Any, str(POLICY_PATH))
        )


def test_source_config_is_exact_pydantic_type() -> None:
    class ConfigSubclass(IgnBdTopoSourceConfig):
        pass

    with pytest.raises(IgnRoadVehicleProxyApplicationError):
        apply_ign_road_vehicle_proxy_policy(
            _source(), ConfigSubclass.model_validate(SOURCE_CONFIG.model_dump())
        )

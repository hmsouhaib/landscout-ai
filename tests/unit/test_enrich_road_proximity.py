from __future__ import annotations

from copy import deepcopy
from dataclasses import FrozenInstanceError
from pathlib import Path
from typing import Any, cast
from unittest.mock import patch

import geopandas as gpd  # type: ignore[import-untyped]
import pandas as pd  # type: ignore[import-untyped]
import pytest
from geopandas.testing import assert_geodataframe_equal
from pandas.testing import assert_frame_equal
from shapely.geometry import LineString, MultiPolygon, Point, Polygon

from landscout import stages
from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoRoadData,
    load_ign_bdtopo_source_config,
)
from landscout.stages.apply_road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyApplicationError,
    IgnRoadVehicleProxyApplicationResult,
)
from landscout.stages.enrich_road_proximity import (
    CLASS_PROXIMITY_COLUMNS,
    ParcelRoadProximityResult,
    RoadProximityError,
    enrich_parcel_road_proximity,
)
from landscout.stages.road_vehicle_proxy_policy import (
    load_ign_road_vehicle_proxy_policy,
)

SOURCE_CONFIG = load_ign_bdtopo_source_config()
POLICY_PATH = Path("configs/access/ign_bdtopo_vehicle_proxy_policy.yaml")
ELIGIBLE_CLASSES = (
    "GENERAL_VEHICLE_PROXY",
    "LIMITED_VEHICLE_PROXY",
    "RESTRICTED_REVIEW",
    "NOT_GENERAL_VEHICLE_PROXY",
    "UNKNOWN_REVIEW",
)
ALL_CLASSES = (
    "GENERAL_VEHICLE_PROXY",
    "LIMITED_VEHICLE_PROXY",
    "RESTRICTED_REVIEW",
    "NOT_GENERAL_VEHICLE_PROXY",
    "NOT_DISTANCE_PROXY",
    "UNKNOWN_REVIEW",
)
SELECTED_COLUMNS = (
    "nearest_road_proxy_distance_m",
    "nearest_road_feature_id",
    "nearest_source_feature_id",
    "nearest_road_tie_count",
    "nearest_road_primary_rule",
    "nearest_road_rule_trace_json",
    "nearest_road_unknown_fields_json",
    "nearest_road_toll_evidence",
    "nearest_nature_raw",
    "nearest_importance_raw",
    "nearest_asset_status_raw",
    "nearest_private_raw",
    "nearest_light_vehicle_access_raw",
    "nearest_carriageway_width_raw",
    "nearest_closure_period_raw",
    "nearest_restriction_nature_raw",
    "nearest_source_layer",
    "nearest_source_department_code",
    "nearest_source_edition",
    "nearest_source_archive_sha256",
)


def _metric_parcels(
    geometries: list[object] | None = None,
    *,
    identifiers: list[object] | None = None,
    index: list[object] | None = None,
) -> gpd.GeoDataFrame:
    values = geometries or [
        Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])
    ]
    count = len(values)
    ids = identifiers or [f"PARCEL-{position + 1}" for position in range(count)]
    frame_index = index or [100 + position for position in range(count)]
    return gpd.GeoDataFrame(
        {"parcel_id": ids, "source_value": list(range(count))},
        geometry=values,
        crs="EPSG:2154",
        index=frame_index,
    )


def _parcels(
    geometries: list[object] | None = None,
    *,
    identifiers: list[object] | None = None,
    index: list[object] | None = None,
) -> gpd.GeoDataFrame:
    return _metric_parcels(
        geometries, identifiers=identifiers, index=index
    ).to_crs("EPSG:4326")


def _road_row(
    road_class: str,
    x: float,
    *,
    identifier: str,
    geometry: object | None = None,
) -> dict[str, object]:
    policy = load_ign_road_vehicle_proxy_policy()
    primary_rule = {
        "GENERAL_VEHICLE_PROXY": "OPEN_OR_TOLL",
        "LIMITED_VEHICLE_PROXY": "LIMITED_NATURE",
        "RESTRICTED_REVIEW": "PRIVATE_ROAD",
        "NOT_GENERAL_VEHICLE_PROXY": "PHYSICALLY_IMPOSSIBLE",
        "NOT_DISTANCE_PROXY": "FICTITIOUS_GEOMETRY",
        "UNKNOWN_REVIEW": "UNKNOWN",
    }[road_class]
    return {
        "road_feature_id": identifier,
        "source_feature_id": f"SOURCE-{identifier}",
        "geometry_status": "VALID",
        "nature_raw": "Route à 1 chaussée",
        "importance_raw": "2",
        "asset_status_raw": "En service",
        "private_raw": 0.0,
        "light_vehicle_access_raw": "Libre",
        "carriageway_width_raw": 7.0,
        "closure_period_raw": None,
        "restriction_nature_raw": None,
        "source_layer": "troncon_de_route",
        "source_department_code": "31",
        "source_edition": "2026-06-15",
        "source_archive_sha256": "a" * 64,
        "road_proxy_primary_rule": primary_rule,
        "road_proxy_class": road_class,
        "road_proxy_rule_trace_json": f'["{primary_rule}"]',
        "road_proxy_unknown_fields_json": "[]",
        "road_proxy_toll_evidence": False,
        "road_proxy_policy_id": policy.policy_id,
        "road_proxy_policy_schema_version": policy.schema_version,
        "road_proxy_policy_config_sha256": policy.config_sha256,
        "road_proxy_policy_scope": policy.scope,
        "road_proxy_heavy_vehicle_access": policy.heavy_vehicle_access,
        "geometry": geometry or LineString([(x, -20), (x, 30)]),
    }


def _roads(
    rows: list[dict[str, object]] | None = None,
) -> gpd.GeoDataFrame:
    values = rows or [
        _road_row(
            "GENERAL_VEHICLE_PROXY", 20, identifier="ROAD-GENERAL"
        ),
        _road_row(
            "LIMITED_VEHICLE_PROXY", 30, identifier="ROAD-LIMITED"
        ),
        _road_row("RESTRICTED_REVIEW", 15, identifier="ROAD-RESTRICTED"),
        _road_row(
            "NOT_GENERAL_VEHICLE_PROXY", 40, identifier="ROAD-NOT-GENERAL"
        ),
        _road_row("NOT_DISTANCE_PROXY", 11, identifier="ROAD-NOT-DISTANCE"),
        _road_row("UNKNOWN_REVIEW", 50, identifier="ROAD-UNKNOWN"),
    ]
    return gpd.GeoDataFrame(values, geometry="geometry", crs="EPSG:2154")


def _source() -> IgnBdTopoRoadData:
    return IgnBdTopoRoadData(
        extraction=cast(Any, None),
        road_segments=_roads(),
        road_segments_summary=cast(Any, None),
    )


def _enrich(
    parcels: gpd.GeoDataFrame | None = None,
    roads: gpd.GeoDataFrame | None = None,
    *,
    policy_path: Path | None = None,
) -> ParcelRoadProximityResult:
    application = IgnRoadVehicleProxyApplicationResult(
        roads if roads is not None else _roads()
    )
    with patch(
        "landscout.stages.enrich_road_proximity.apply_ign_road_vehicle_proxy_policy",
        return_value=application,
    ):
        return enrich_parcel_road_proximity(
            parcels if parcels is not None else _parcels(),
            _source(),
            SOURCE_CONFIG,
            policy_path,
        )


def _row(result: ParcelRoadProximityResult, road_class: str) -> pd.Series:
    return result.class_proximity.loc[
        result.class_proximity["road_proxy_class"].eq(road_class)
    ].iloc[0]


def test_public_api_exports_only_stable_symbols() -> None:
    import landscout.stages.enrich_road_proximity as module

    expected = {
        "RoadProximityError",
        "RoadProxyClassCoverage",
        "ParcelRoadProximityResult",
        "enrich_parcel_road_proximity",
    }
    assert set(module.__all__) == expected
    assert expected <= set(stages.__all__)
    assert all(hasattr(stages, symbol) for symbol in expected)
    assert not hasattr(stages, "_nearest_class_rows")


def test_wrong_parcel_type_has_controlled_error() -> None:
    with pytest.raises(RoadProximityError):
        enrich_parcel_road_proximity(
            cast(Any, pd.DataFrame()), _source(), SOURCE_CONFIG
        )


def test_wrong_road_source_type_has_controlled_error() -> None:
    with pytest.raises(RoadProximityError):
        enrich_parcel_road_proximity(
            _parcels(), cast(Any, object()), SOURCE_CONFIG
        )


def test_wrong_source_config_type_has_controlled_error() -> None:
    with pytest.raises(RoadProximityError):
        enrich_parcel_road_proximity(
            _parcels(), _source(), cast(Any, object())
        )


def test_wrong_policy_path_type_has_controlled_error() -> None:
    with pytest.raises(RoadProximityError):
        enrich_parcel_road_proximity(
            _parcels(), _source(), SOURCE_CONFIG, cast(Any, "policy.yaml")
        )


def test_application_stage_is_invoked_exactly_once() -> None:
    application = IgnRoadVehicleProxyApplicationResult(_roads())
    with patch(
        "landscout.stages.enrich_road_proximity.apply_ign_road_vehicle_proxy_policy",
        return_value=application,
    ) as source_application:
        enrich_parcel_road_proximity(_parcels(), _source(), SOURCE_CONFIG)

    source_application.assert_called_once()


def test_application_failure_stops_proximity() -> None:
    with patch(
        "landscout.stages.enrich_road_proximity.apply_ign_road_vehicle_proxy_policy",
        side_effect=IgnRoadVehicleProxyApplicationError("bad source"),
    ), patch(
        "landscout.stages.enrich_road_proximity.STRtree"
    ) as spatial_index, pytest.raises(RoadProximityError):
        enrich_parcel_road_proximity(_parcels(), _source(), SOURCE_CONFIG)

    spatial_index.assert_not_called()


def test_malformed_policy_stops_before_application(tmp_path: Path) -> None:
    path = tmp_path / "policy.yaml"
    path.write_text("policy_id: [", encoding="utf-8")

    with patch(
        "landscout.stages.enrich_road_proximity.apply_ign_road_vehicle_proxy_policy"
    ) as source_application, pytest.raises(RoadProximityError):
        enrich_parcel_road_proximity(_parcels(), _source(), SOURCE_CONFIG, path)

    source_application.assert_not_called()


def test_independent_policy_sha_mismatch_is_rejected() -> None:
    roads = _roads()
    roads["road_proxy_policy_config_sha256"] = "b" * 64

    with pytest.raises(RoadProximityError, match="policy|SHA|lineage"):
        _enrich(roads=roads)


@pytest.mark.parametrize(
    ("mutation", "message"),
    [
        (lambda frame: frame.drop(columns="parcel_id"), "parcel_id"),
        (lambda frame: frame.assign(parcel_id=None), "parcel_id"),
        (lambda frame: frame.assign(parcel_id=123), "parcel_id"),
        (lambda frame: frame.assign(parcel_id=""), "parcel_id"),
        (lambda frame: frame.assign(parcel_id=" BAD "), "parcel_id"),
    ],
)
def test_invalid_parcel_identity_is_rejected(
    mutation: Any, message: str
) -> None:
    with pytest.raises(RoadProximityError, match=message):
        _enrich(parcels=mutation(_parcels()))


def test_duplicate_parcel_id_is_rejected() -> None:
    parcels = _parcels(
        [
            Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]),
            Polygon([(20, 0), (20, 10), (30, 10), (30, 0), (20, 0)]),
        ],
        identifiers=["DUPLICATE", "DUPLICATE"],
    )

    with pytest.raises(RoadProximityError, match="unique"):
        _enrich(parcels=parcels)


def test_duplicate_parcel_columns_are_rejected() -> None:
    parcels = _parcels()
    duplicated = gpd.GeoDataFrame(
        pd.concat([parcels, parcels[["parcel_id"]]], axis=1),
        geometry="geometry",
        crs=parcels.crs,
    )

    with pytest.raises(RoadProximityError, match="duplicate"):
        _enrich(parcels=duplicated)


def test_missing_or_inactive_geometry_is_rejected() -> None:
    parcels = _parcels()
    missing = parcels.drop(columns="geometry")
    inactive = parcels.assign(other_geometry=parcels.geometry).set_geometry(
        "other_geometry"
    )

    with pytest.raises(RoadProximityError, match="geometry"):
        _enrich(parcels=missing)
    with pytest.raises(RoadProximityError, match="active"):
        _enrich(parcels=inactive)


def test_missing_or_wrong_storage_crs_is_rejected() -> None:
    missing = _parcels().set_crs(None, allow_override=True)
    wrong = _metric_parcels()

    with pytest.raises(RoadProximityError, match="CRS"):
        _enrich(parcels=missing)
    with pytest.raises(RoadProximityError, match="4326"):
        _enrich(parcels=wrong)


@pytest.mark.parametrize(
    "geometry",
    [Point(0, 0), LineString([(0, 0), (10, 10)])],
)
def test_wrong_parcel_geometry_kind_is_rejected(geometry: object) -> None:
    with pytest.raises(RoadProximityError, match="Polygon|MultiPolygon"):
        _enrich(parcels=_parcels([geometry]))


@pytest.mark.parametrize(
    ("geometry", "message"),
    [
        (None, "null"),
        (Polygon(), "empty"),
        (
            Polygon([(0, 0), (20, 20), (20, 0), (0, 20), (0, 0)]),
            "valid",
        ),
    ],
)
def test_bad_parcel_geometry_is_rejected(
    geometry: object, message: str
) -> None:
    with pytest.raises(RoadProximityError, match=message):
        _enrich(parcels=_parcels([geometry]))


@pytest.mark.parametrize(
    "geometry",
    [
        Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]),
        MultiPolygon(
            [Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])]
        ),
    ],
)
def test_polygon_and_multipolygon_are_accepted(geometry: object) -> None:
    assert len(_enrich(parcels=_parcels([geometry])).parcels) == 1


def test_wrong_application_result_type_is_rejected() -> None:
    with patch(
        "landscout.stages.enrich_road_proximity.apply_ign_road_vehicle_proxy_policy",
        return_value=object(),
    ), pytest.raises(RoadProximityError):
        enrich_parcel_road_proximity(_parcels(), _source(), SOURCE_CONFIG)


def test_application_roads_must_be_geodataframe() -> None:
    application = IgnRoadVehicleProxyApplicationResult(
        cast(Any, pd.DataFrame(_roads().drop(columns="geometry")))
    )
    with patch(
        "landscout.stages.enrich_road_proximity.apply_ign_road_vehicle_proxy_policy",
        return_value=application,
    ), pytest.raises(RoadProximityError):
        enrich_parcel_road_proximity(_parcels(), _source(), SOURCE_CONFIG)


def test_duplicate_road_feature_id_is_rejected() -> None:
    roads = _roads()
    roads.loc[1, "road_feature_id"] = roads.loc[0, "road_feature_id"]

    with pytest.raises(RoadProximityError, match="unique"):
        _enrich(roads=roads)


def test_unknown_road_proxy_class_is_rejected() -> None:
    roads = _roads()
    roads.loc[0, "road_proxy_class"] = "INVENTED"

    with pytest.raises(RoadProximityError, match="class"):
        _enrich(roads=roads)


@pytest.mark.parametrize(
    "column",
    [
        "road_proxy_policy_id",
        "road_proxy_policy_schema_version",
        "road_proxy_policy_config_sha256",
        "road_proxy_heavy_vehicle_access",
    ],
)
def test_missing_road_policy_lineage_is_rejected(column: str) -> None:
    with pytest.raises(RoadProximityError, match="column|lineage"):
        _enrich(roads=_roads().drop(columns=column))


@pytest.mark.parametrize("status", ["NULL", "EMPTY", "INVALID"])
def test_eligible_class_requires_valid_geometry_status(status: str) -> None:
    roads = _roads()
    roads.loc[0, "geometry_status"] = status

    with pytest.raises(RoadProximityError, match="VALID"):
        _enrich(roads=roads)


def test_eligible_class_rejects_unsupported_geometry() -> None:
    roads = _roads()
    roads.at[0, "geometry"] = Point(20, 0)

    with pytest.raises(RoadProximityError, match="LineString|geometry"):
        _enrich(roads=roads)


def test_not_distance_road_is_counted_but_never_indexed() -> None:
    roads = _roads()
    roads.loc[
        roads["road_proxy_class"].eq("NOT_DISTANCE_PROXY"), "geometry_status"
    ] = "INVALID"
    result = _enrich(roads=roads)
    coverage = {item.road_proxy_class: item for item in result.class_coverage}

    assert coverage["NOT_DISTANCE_PROXY"].feature_count == 1
    assert not coverage["NOT_DISTANCE_PROXY"].distance_eligible
    assert "NOT_DISTANCE_PROXY" not in set(result.class_proximity.road_proxy_class)


def test_known_polygon_to_line_distance_is_ten_metres() -> None:
    result = _enrich()

    assert _row(
        result, "GENERAL_VEHICLE_PROXY"
    ).nearest_road_proxy_distance_m == pytest.approx(10.0, abs=1e-5)


@pytest.mark.parametrize("x", [5.0, 10.0])
def test_intersecting_or_touching_road_has_zero_distance(x: float) -> None:
    roads = _roads(
        [_road_row("GENERAL_VEHICLE_PROXY", x, identifier="ROAD-GENERAL")]
    )

    assert _row(
        _enrich(roads=roads), "GENERAL_VEHICLE_PROXY"
    ).nearest_road_proxy_distance_m == pytest.approx(0.0, abs=1e-5)


def test_distance_uses_full_polygon_not_centroid() -> None:
    distance = _row(
        _enrich(), "GENERAL_VEHICLE_PROXY"
    ).nearest_road_proxy_distance_m

    assert distance == pytest.approx(10.0, abs=1e-5)
    assert distance != pytest.approx(15.0, abs=1e-5)


def test_storage_geometry_stays_epsg4326_while_distance_is_metric() -> None:
    parcels = _parcels()
    before = deepcopy(parcels)
    result = _enrich(parcels=parcels)

    assert result.parcels.crs == parcels.crs
    assert result.parcels.crs.to_epsg() == 4326
    assert _row(
        result, "GENERAL_VEHICLE_PROXY"
    ).nearest_road_proxy_distance_m == pytest.approx(10.0, abs=1e-5)
    assert_geodataframe_equal(result.parcels, before)


def test_each_eligible_class_has_independent_distance() -> None:
    result = _enrich()
    distances = {
        road_class: _row(result, road_class).nearest_road_proxy_distance_m
        for road_class in ELIGIBLE_CLASSES
    }

    assert distances == pytest.approx(
        {
            "GENERAL_VEHICLE_PROXY": 10.0,
            "LIMITED_VEHICLE_PROXY": 20.0,
            "RESTRICTED_REVIEW": 5.0,
            "NOT_GENERAL_VEHICLE_PROXY": 30.0,
            "UNKNOWN_REVIEW": 40.0,
        },
        abs=1e-5,
    )


def test_near_not_distance_road_cannot_change_general_distance() -> None:
    result = _enrich()

    assert _row(
        result, "GENERAL_VEHICLE_PROXY"
    ).nearest_road_proxy_distance_m == pytest.approx(10.0, abs=1e-5)
    assert "ROAD-NOT-DISTANCE" not in set(
        result.class_proximity.nearest_road_feature_id.dropna()
    )


def test_single_nearest_road_has_tie_count_one() -> None:
    assert _row(
        _enrich(), "GENERAL_VEHICLE_PROXY"
    ).nearest_road_tie_count == 1


def test_exact_tie_counts_two_and_lexical_id_wins() -> None:
    roads = _roads(
        [
            _road_row("GENERAL_VEHICLE_PROXY", -10, identifier="Z-ROAD"),
            _road_row("GENERAL_VEHICLE_PROXY", 20, identifier="A-ROAD"),
        ]
    )
    row = _row(_enrich(roads=roads), "GENERAL_VEHICLE_PROXY")

    assert row.nearest_road_proxy_distance_m == pytest.approx(10.0, abs=1e-5)
    assert row.nearest_road_tie_count == 2
    assert row.nearest_road_feature_id == "A-ROAD"


def test_tie_winner_is_independent_of_source_order() -> None:
    roads = _roads(
        [
            _road_row("GENERAL_VEHICLE_PROXY", -10, identifier="Z-ROAD"),
            _road_row("GENERAL_VEHICLE_PROXY", 20, identifier="A-ROAD"),
        ]
    )
    forward = _row(_enrich(roads=roads), "GENERAL_VEHICLE_PROXY")
    reverse = _row(
        _enrich(roads=roads.iloc[::-1].reset_index(drop=True)),
        "GENERAL_VEHICLE_PROXY",
    )

    assert forward.nearest_road_feature_id == "A-ROAD"
    assert reverse.nearest_road_feature_id == "A-ROAD"
    assert forward.nearest_road_tie_count == reverse.nearest_road_tie_count == 2


def test_unequal_distance_wins_regardless_of_identifier() -> None:
    roads = _roads(
        [
            _road_row("GENERAL_VEHICLE_PROXY", 20, identifier="Z-NEAR"),
            _road_row("GENERAL_VEHICLE_PROXY", 30, identifier="A-FAR"),
        ]
    )

    assert _row(
        _enrich(roads=roads), "GENERAL_VEHICLE_PROXY"
    ).nearest_road_feature_id == "Z-NEAR"


def test_empty_eligible_class_emits_null_row_per_parcel() -> None:
    roads = _roads().loc[
        ~_roads()["road_proxy_class"].eq("UNKNOWN_REVIEW")
    ].reset_index(drop=True)
    parcels = _parcels(
        [
            Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]),
            Polygon([(50, 0), (50, 10), (60, 10), (60, 0), (50, 0)]),
        ]
    )
    result = _enrich(parcels=parcels, roads=roads)
    rows = result.class_proximity.loc[
        result.class_proximity.road_proxy_class.eq("UNKNOWN_REVIEW")
    ]

    assert len(rows) == 2
    assert rows.loc[:, list(SELECTED_COLUMNS)].isna().all().all()
    coverage = {item.road_proxy_class: item for item in result.class_coverage}
    assert coverage["UNKNOWN_REVIEW"].feature_count == 0


def test_output_shape_columns_and_order_are_deterministic() -> None:
    parcels = _parcels(
        [
            Polygon([(50, 0), (50, 10), (60, 10), (60, 0), (50, 0)]),
            Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]),
        ],
        identifiers=["SECOND", "FIRST"],
    )
    result = _enrich(parcels=parcels)

    assert len(result.class_proximity) == len(parcels) * 5
    assert list(result.class_proximity.columns) == list(CLASS_PROXIMITY_COLUMNS)
    assert result.class_proximity.parcel_id.tolist() == [
        value for parcel_id in ("SECOND", "FIRST") for value in [parcel_id] * 5
    ]
    assert result.class_proximity.road_proxy_class.tolist() == list(
        ELIGIBLE_CLASSES
    ) * 2


def test_class_coverage_is_complete_and_strict() -> None:
    result = _enrich()

    assert tuple(item.road_proxy_class for item in result.class_coverage) == (
        ALL_CLASSES
    )
    assert sum(item.feature_count for item in result.class_coverage) == 6
    assert all(
        item.distance_eligible == (item.road_proxy_class != "NOT_DISTANCE_PROXY")
        for item in result.class_coverage
    )


def test_selected_road_evidence_and_lineage_are_exact() -> None:
    policy = load_ign_road_vehicle_proxy_policy()
    row = _row(_enrich(), "GENERAL_VEHICLE_PROXY")

    assert row.nearest_road_feature_id == "ROAD-GENERAL"
    assert row.nearest_source_feature_id == "SOURCE-ROAD-GENERAL"
    assert row.nearest_road_primary_rule == "OPEN_OR_TOLL"
    assert row.nearest_road_rule_trace_json == '["OPEN_OR_TOLL"]'
    assert row.nearest_road_unknown_fields_json == "[]"
    assert not row.nearest_road_toll_evidence
    assert row.nearest_source_archive_sha256 == "a" * 64
    assert row.road_proxy_policy_id == policy.policy_id
    assert row.road_proxy_policy_schema_version == policy.schema_version
    assert row.road_proxy_policy_config_sha256 == policy.config_sha256
    assert row.road_proxy_heavy_vehicle_access == "NOT_PROVEN"
    assert row.proximity_scope == "WITHIN_VERIFIED_SOURCE_PACKAGE"


def test_parcels_and_road_application_are_not_mutated() -> None:
    parcels = _parcels(index=[777])
    roads = _roads()
    parcels_before = deepcopy(parcels)
    roads_before = deepcopy(roads)
    result = _enrich(parcels=parcels, roads=roads)

    assert_geodataframe_equal(parcels, parcels_before)
    assert_geodataframe_equal(roads, roads_before)
    assert_geodataframe_equal(result.parcels, parcels_before)
    assert result.parcels.index.equals(parcels.index)
    assert list(result.parcels.columns) == list(parcels.columns)
    assert result.parcels.dtypes.equals(parcels.dtypes)
    assert result.parcels.geometry.to_wkb().equals(parcels.geometry.to_wkb())


def _corrupt_nearest_output(column: str, value: object) -> None:
    import landscout.stages.enrich_road_proximity as module

    original = module._nearest_class_rows

    def corrupted(*args: object, **kwargs: object) -> pd.DataFrame:
        output = original(*args, **kwargs)
        if output["distance_m"].notna().any():
            output[column] = output[column].astype("object")
            output.at[0, column] = value
        return output

    with patch.object(module, "_nearest_class_rows", side_effect=corrupted), pytest.raises(
        RoadProximityError
    ):
        _enrich()


@pytest.mark.parametrize("value", [-1.0, float("nan"), float("inf")])
def test_malformed_produced_distance_is_rejected(value: object) -> None:
    _corrupt_nearest_output("distance_m", value)


@pytest.mark.parametrize("value", [0, -1, True, 1.5])
def test_malformed_produced_tie_count_is_rejected(value: object) -> None:
    _corrupt_nearest_output("tie_count", value)


def test_result_dataclasses_are_frozen() -> None:
    result = _enrich()
    coverage = result.class_coverage[0]

    with pytest.raises(FrozenInstanceError):
        result.parcels = _parcels()  # type: ignore[misc]
    with pytest.raises(FrozenInstanceError):
        coverage.feature_count = 99  # type: ignore[misc]


def test_no_business_decision_columns_or_implementation_exist() -> None:
    result = _enrich()
    forbidden = {
        "access_score",
        "bess_score",
        "accessible",
        "legal_access",
        "parcel_status",
        "retained",
        "rejected",
    }
    assert forbidden.isdisjoint(result.parcels.columns)
    assert forbidden.isdisjoint(result.class_proximity.columns)

    source = Path("src/landscout/stages/enrich_road_proximity.py").read_text(
        encoding="utf-8"
    )
    assert ".iterrows(" not in source


def test_result_parcel_frame_is_an_independent_copy() -> None:
    parcels = _parcels()
    result = _enrich(parcels=parcels)
    result.parcels.loc[result.parcels.index[0], "source_value"] = 999

    assert parcels.iloc[0].source_value == 0


def test_class_proximity_is_plain_dataframe() -> None:
    result = _enrich()

    assert type(result.class_proximity) is pd.DataFrame
    assert not isinstance(result.class_proximity, gpd.GeoDataFrame)


def test_selected_rows_belong_to_requested_class() -> None:
    result = _enrich()
    road_classes = _roads().set_index("road_feature_id")["road_proxy_class"]
    selected = result.class_proximity.dropna(subset=["nearest_road_feature_id"])

    assert all(
        road_classes.loc[row.nearest_road_feature_id] == row.road_proxy_class
        for row in selected.itertuples(index=False)
    )


def test_policy_sha_mismatch_does_not_construct_spatial_index() -> None:
    roads = _roads()
    roads["road_proxy_policy_config_sha256"] = "b" * 64

    with patch(
        "landscout.stages.enrich_road_proximity.STRtree"
    ) as spatial_index, pytest.raises(RoadProximityError):
        _enrich(roads=roads)

    spatial_index.assert_not_called()


def test_matched_output_dtypes_are_stable() -> None:
    result = _enrich()
    table = result.class_proximity

    assert str(table.nearest_road_proxy_distance_m.dtype) == "float64"
    assert str(table.nearest_road_tie_count.dtype) == "Int64"
    assert str(table.nearest_road_toll_evidence.dtype) == "boolean"


def test_parcel_preservation_uses_exact_non_geometry_values() -> None:
    parcels = _parcels()
    result = _enrich(parcels=parcels)

    assert_frame_equal(
        pd.DataFrame(result.parcels.drop(columns="geometry")),
        pd.DataFrame(parcels.drop(columns="geometry")),
        check_dtype=True,
        check_index_type=True,
    )

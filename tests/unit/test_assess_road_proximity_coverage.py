from __future__ import annotations

from copy import deepcopy
from dataclasses import FrozenInstanceError, replace
from importlib import import_module
from pathlib import Path
from typing import Any, cast
from unittest.mock import patch

import geopandas as gpd  # type: ignore[import-untyped]
import numpy as np
import pandas as pd  # type: ignore[import-untyped]
import pytest
from geopandas.testing import assert_geodataframe_equal
from pandas.testing import assert_frame_equal
from shapely.geometry import LineString, MultiPolygon, Point, Polygon

from landscout import stages
from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_source_config,
)
from landscout.stages.assess_road_proximity_coverage import (
    RoadProximityCoverageAssessmentResult,
    RoadProximityCoverageError,
    assess_road_proximity_coverage,
)
from landscout.stages.enrich_road_proximity import (
    CLASS_PROXIMITY_COLUMNS,
    ParcelRoadProximityResult,
    RoadProxyClassCoverage,
)
from landscout.stages.road_vehicle_proxy_policy import (
    load_ign_road_vehicle_proxy_policy,
)

SOURCE_CONFIG = load_ign_bdtopo_source_config()
ARCHIVE_SHA256 = "a" * 64
GEOPACKAGE_SHA256 = "b" * 64
EDITION = "2026-06-15"
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
DIAGNOSTIC_COLUMNS = (
    "road_source_boundary_distance_m",
    "road_source_coverage_position",
    "road_proximity_coverage_status",
    "road_source_coverage_provider",
    "road_source_coverage_product",
    "road_source_coverage_department_code",
    "road_source_coverage_edition",
    "road_source_coverage_product_version",
    "road_source_coverage_archive_sha256",
    "road_source_coverage_layer",
    "road_source_coverage_spatial_role",
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


def _archive() -> IgnBdTopoDownload:
    return IgnBdTopoDownload(
        provider=SOURCE_CONFIG.provider,
        product=SOURCE_CONFIG.product,
        department_code="31",
        edition=EDITION,
        product_version="3.5",
        projection="EPSG:2154",
        package_format="GPKG",
        archive_format="7z",
        source_url=str(SOURCE_CONFIG.source_url),
        checksum_url=None,
        download_timestamp="2026-08-11T15:32:03+00:00",
        filename="BDTOPO.7z",
        file_size=123,
        sha256=ARCHIVE_SHA256,
        official_checksum_algorithm=None,
        official_checksum=None,
        official_checksum_validated=False,
        path=Path("synthetic/BDTOPO.7z"),
        cache_hit=True,
    )


def _extraction() -> IgnBdTopoExtraction:
    return IgnBdTopoExtraction(
        archive=_archive(),
        extraction_path=Path("synthetic/extracted"),
        geopackage_path=Path("synthetic/extracted/data.gpkg"),
        geopackage_filename="data.gpkg",
        geopackage_size_bytes=456,
        geopackage_sha256=GEOPACKAGE_SHA256,
        all_layer_names=(
            "ligne_electrique",
            "poste_de_transformation",
            "troncon_de_route",
            "departement",
            "zone_administrative",
        ),
        electric_lines_layer="ligne_electrique",
        transformation_posts_layer="poste_de_transformation",
        road_segments_layer="troncon_de_route",
        department_layer="departement",
        cache_hit=True,
    )


def _road_source(
    extraction: IgnBdTopoExtraction | None = None,
) -> IgnBdTopoRoadData:
    package = extraction or _extraction()
    roads = gpd.GeoDataFrame(
        {"cleabs": ["ROAD-1"]},
        geometry=[LineString([(0, 0), (1, 1)])],
        crs="EPSG:2154",
    )
    summary = IgnBdTopoLayerSummary(
        logical_name="road_segments",
        source_layer_name="troncon_de_route",
        crs="EPSG:2154",
        feature_count=1,
        columns=tuple(str(column) for column in roads.columns),
        dtypes=tuple(
            (str(column), str(dtype)) for column, dtype in roads.dtypes.items()
        ),
        null_geometry_count=0,
        empty_geometry_count=0,
        invalid_geometry_count=0,
        geometry_types=("LineString",),
    )
    return IgnBdTopoRoadData(package, roads, summary)


def _coverage(
    extraction: IgnBdTopoExtraction | None = None,
    *,
    geometries: list[object] | None = None,
    crs: str | None = "EPSG:2154",
    layer: str = "departement",
    department_code: str = "31",
    provider: str | None = None,
    product: str | None = None,
    edition: str = EDITION,
    product_version: str | None = "3.5",
    archive_sha256: str = ARCHIVE_SHA256,
) -> IgnBdTopoDepartmentCoverage:
    package = extraction or _extraction()
    values = geometries
    if values is None:
        values = [Polygon([(0, 0), (0, 1000), (1000, 1000), (1000, 0), (0, 0)])]
    raw = gpd.GeoDataFrame(
        {
            "code_insee": [department_code] * len(values),
            "nom_officiel": [
                f"Department {position}" for position in range(len(values))
            ],
        },
        geometry=values,
        crs=crs,
    )
    lineage = {
        "source_provider": provider or package.archive.provider,
        "source_product": product or package.archive.product,
        "source_department_code": department_code,
        "source_edition": edition,
        "source_product_version": product_version,
        "source_archive_sha256": archive_sha256,
        "source_layer": layer,
        "spatial_role": "SOURCE_COVERAGE_BOUNDARY",
    }
    selected = raw.copy()
    for column, value in lineage.items():
        selected[column] = value
    geometry = raw.geometry
    non_null = ~geometry.isna()
    non_empty = non_null & ~geometry.is_empty
    summary = IgnBdTopoCoverageLayerSummary(
        source_layer_name=layer,
        crs="" if crs is None else str(raw.crs),
        source_feature_count=len(raw),
        selected_feature_count=len(raw),
        columns=tuple(str(column) for column in raw.columns),
        dtypes=tuple((str(column), str(dtype)) for column, dtype in raw.dtypes.items()),
        null_geometry_count=int(geometry.isna().sum()),
        empty_geometry_count=int((non_null & geometry.is_empty).sum()),
        invalid_geometry_count=int((non_empty & ~geometry.is_valid).sum()),
        geometry_types=tuple(
            sorted(str(value) for value in geometry.geom_type.dropna().unique())
        ),
        department_code_field="code_insee",
        selected_department_code=department_code,
    )
    return IgnBdTopoDepartmentCoverage(
        extraction=package,
        coverage=selected,
        summary=summary,
        source_provider=cast(str, lineage["source_provider"]),
        source_product=cast(str, lineage["source_product"]),
        source_department_code=department_code,
        source_edition=edition,
        source_product_version=product_version,
        source_archive_sha256=archive_sha256,
        source_layer=layer,
    )


def _metric_parcels(
    geometries: list[object] | None = None,
    *,
    identifiers: list[str] | None = None,
) -> gpd.GeoDataFrame:
    values = geometries or [
        Polygon([(100, 100), (100, 200), (200, 200), (200, 100), (100, 100)])
    ]
    ids = identifiers or [f"PARCEL-{position + 1}" for position in range(len(values))]
    return gpd.GeoDataFrame(
        {"parcel_id": ids, "preserved_value": list(range(len(values)))},
        geometry=values,
        crs="EPSG:2154",
        index=[20 + position for position in range(len(values))],
    )


def _parcels(
    geometries: list[object] | None = None,
    *,
    identifiers: list[str] | None = None,
) -> gpd.GeoDataFrame:
    return _metric_parcels(geometries, identifiers=identifiers).to_crs("EPSG:4326")


def _proximity(
    parcels: gpd.GeoDataFrame | None = None,
    *,
    distances: dict[str, float] | None = None,
) -> ParcelRoadProximityResult:
    source_parcels = parcels if parcels is not None else _parcels()
    policy = load_ign_road_vehicle_proxy_policy()
    configured_distances = distances or {}
    primary_rules = {
        "GENERAL_VEHICLE_PROXY": "OPEN_OR_TOLL",
        "LIMITED_VEHICLE_PROXY": "LIMITED_NATURE",
        "RESTRICTED_REVIEW": "PRIVATE_ROAD",
        "NOT_GENERAL_VEHICLE_PROXY": "PHYSICALLY_IMPOSSIBLE",
        "UNKNOWN_REVIEW": "UNKNOWN",
    }
    rows: list[dict[str, object]] = []
    for parcel_id in source_parcels["parcel_id"]:
        for position, road_class in enumerate(ELIGIBLE_CLASSES):
            distance_m = configured_distances.get(road_class, 50.0 + position)
            primary_rule = primary_rules[road_class]
            rows.append(
                {
                    "parcel_id": parcel_id,
                    "road_proxy_class": road_class,
                    "nearest_road_proxy_distance_m": distance_m,
                    "nearest_road_feature_id": f"ROAD-{road_class}",
                    "nearest_source_feature_id": f"SOURCE-{road_class}",
                    "nearest_road_tie_count": 1,
                    "nearest_road_primary_rule": primary_rule,
                    "nearest_road_rule_trace_json": f'["{primary_rule}"]',
                    "nearest_road_unknown_fields_json": "[]",
                    "nearest_road_toll_evidence": False,
                    "nearest_nature_raw": "Route à 1 chaussée",
                    "nearest_importance_raw": "2",
                    "nearest_asset_status_raw": "En service",
                    "nearest_private_raw": 0.0,
                    "nearest_light_vehicle_access_raw": "Libre",
                    "nearest_carriageway_width_raw": 7.0,
                    "nearest_closure_period_raw": None,
                    "nearest_restriction_nature_raw": None,
                    "nearest_source_layer": "troncon_de_route",
                    "nearest_source_department_code": "31",
                    "nearest_source_edition": EDITION,
                    "nearest_source_archive_sha256": ARCHIVE_SHA256,
                    "road_proxy_policy_id": policy.policy_id,
                    "road_proxy_policy_schema_version": policy.schema_version,
                    "road_proxy_policy_config_sha256": policy.config_sha256,
                    "road_proxy_heavy_vehicle_access": policy.heavy_vehicle_access,
                    "proximity_scope": "WITHIN_VERIFIED_SOURCE_PACKAGE",
                }
            )
    table = pd.DataFrame(rows, columns=CLASS_PROXIMITY_COLUMNS)
    table["nearest_road_proxy_distance_m"] = table[
        "nearest_road_proxy_distance_m"
    ].astype("float64")
    table["nearest_road_tie_count"] = table["nearest_road_tie_count"].astype("Int64")
    table["nearest_road_toll_evidence"] = table["nearest_road_toll_evidence"].astype(
        "boolean"
    )
    coverage = tuple(
        RoadProxyClassCoverage(
            road_proxy_class=road_class,
            feature_count=1,
            distance_eligible=road_class != "NOT_DISTANCE_PROXY",
        )
        for road_class in ALL_CLASSES
    )
    return ParcelRoadProximityResult(source_parcels.copy(), table, coverage)


def _without_match(
    proximity: ParcelRoadProximityResult,
    road_class: str = "UNKNOWN_REVIEW",
) -> ParcelRoadProximityResult:
    table = proximity.class_proximity.copy()
    mask = table["road_proxy_class"].eq(road_class)
    for column in SELECTED_COLUMNS:
        table.loc[mask, column] = pd.NA
    table["nearest_road_proxy_distance_m"] = table[
        "nearest_road_proxy_distance_m"
    ].astype("float64")
    table["nearest_road_tie_count"] = table["nearest_road_tie_count"].astype("Int64")
    table["nearest_road_toll_evidence"] = table["nearest_road_toll_evidence"].astype(
        "boolean"
    )
    coverage = tuple(
        replace(item, feature_count=0) if item.road_proxy_class == road_class else item
        for item in proximity.class_coverage
    )
    return replace(proximity, class_proximity=table, class_coverage=coverage)


def _measured_boundary_distance(
    parcels: gpd.GeoDataFrame,
    coverage: IgnBdTopoDepartmentCoverage,
) -> float:
    geometry = parcels.to_crs("EPSG:2154").geometry.iloc[0]
    return float(geometry.distance(coverage.coverage.geometry.iloc[0].boundary))


def _assess(
    *,
    parcels: gpd.GeoDataFrame | None = None,
    proximity: object | None = None,
    coverage: IgnBdTopoDepartmentCoverage | None = None,
    road_source: IgnBdTopoRoadData | None = None,
    source_config: IgnBdTopoSourceConfig = SOURCE_CONFIG,
    policy_path: Path | None = None,
) -> RoadProximityCoverageAssessmentResult:
    selected_parcels = parcels if parcels is not None else _parcels()
    selected_proximity = (
        proximity if proximity is not None else _proximity(selected_parcels)
    )
    selected_coverage = coverage or _coverage()
    selected_source = road_source or _road_source(selected_coverage.extraction)
    with (
        patch(
            "landscout.stages.assess_road_proximity_coverage.enrich_parcel_road_proximity",
            return_value=selected_proximity,
        ),
        patch(
            "landscout.stages.assess_road_proximity_coverage.load_ign_bdtopo_department_coverage",
            return_value=selected_coverage,
        ),
    ):
        return assess_road_proximity_coverage(
            selected_parcels,
            selected_source,
            source_config,
            policy_path,
        )


def _first_row(
    result: RoadProximityCoverageAssessmentResult,
    road_class: str = "GENERAL_VEHICLE_PROXY",
) -> pd.Series:
    return result.class_proximity.loc[
        result.class_proximity["road_proxy_class"].eq(road_class)
    ].iloc[0]


def test_public_api_exports_only_stable_symbols() -> None:
    module = import_module("landscout.stages.assess_road_proximity_coverage")

    expected = {
        "RoadProximityCoverageError",
        "RoadProximityCoverageAssessmentResult",
        "assess_road_proximity_coverage",
    }
    assert set(module.__all__) == expected
    assert expected <= set(stages.__all__)
    assert all(hasattr(stages, symbol) for symbol in expected)
    assert not hasattr(stages, "_coverage_positions")


@pytest.mark.parametrize(
    "argument", ["parcels", "road_source", "source_config", "policy_path"]
)
def test_wrong_public_input_type_is_controlled_and_fast(argument: str) -> None:
    kwargs: dict[str, object] = {
        "parcels": _parcels(),
        "road_source": _road_source(),
        "source_config": SOURCE_CONFIG,
        "policy_path": None,
    }
    kwargs[argument] = pd.DataFrame() if argument == "parcels" else object()
    with (
        patch(
            "landscout.stages.assess_road_proximity_coverage.enrich_parcel_road_proximity"
        ) as proximity_stage,
        patch(
            "landscout.stages.assess_road_proximity_coverage.load_ign_bdtopo_department_coverage"
        ) as coverage_loader,
        pytest.raises(RoadProximityCoverageError),
    ):
        assess_road_proximity_coverage(**cast(Any, kwargs))
    proximity_stage.assert_not_called()
    coverage_loader.assert_not_called()


def test_source_chain_calls_proximity_then_coverage_exactly_once() -> None:
    coverage = _coverage()
    road_source = _road_source(coverage.extraction)
    parcels = _parcels()
    proximity = _proximity(parcels)
    policy_path = Path("configs/access/ign_bdtopo_vehicle_proxy_policy.yaml")
    with (
        patch(
            "landscout.stages.assess_road_proximity_coverage.enrich_parcel_road_proximity",
            return_value=proximity,
        ) as proximity_stage,
        patch(
            "landscout.stages.assess_road_proximity_coverage.load_ign_bdtopo_department_coverage",
            return_value=coverage,
        ) as coverage_loader,
    ):
        assess_road_proximity_coverage(parcels, road_source, SOURCE_CONFIG, policy_path)
    proximity_stage.assert_called_once_with(
        parcels, road_source, SOURCE_CONFIG, policy_path
    )
    coverage_loader.assert_called_once_with(road_source.extraction, SOURCE_CONFIG)


def test_proximity_failure_stops_coverage_loading() -> None:
    with (
        patch(
            "landscout.stages.assess_road_proximity_coverage.enrich_parcel_road_proximity",
            side_effect=ValueError("bad proximity"),
        ),
        patch(
            "landscout.stages.assess_road_proximity_coverage.load_ign_bdtopo_department_coverage"
        ) as coverage_loader,
        pytest.raises(RoadProximityCoverageError),
    ):
        assess_road_proximity_coverage(_parcels(), _road_source(), SOURCE_CONFIG)
    coverage_loader.assert_not_called()


def test_coverage_loader_failure_is_controlled() -> None:
    parcels = _parcels()
    with (
        patch(
            "landscout.stages.assess_road_proximity_coverage.enrich_parcel_road_proximity",
            return_value=_proximity(parcels),
        ),
        patch(
            "landscout.stages.assess_road_proximity_coverage.load_ign_bdtopo_department_coverage",
            side_effect=ValueError("bad coverage"),
        ) as coverage_loader,
        pytest.raises(RoadProximityCoverageError),
    ):
        assess_road_proximity_coverage(parcels, _road_source(), SOURCE_CONFIG)
    coverage_loader.assert_called_once()


def test_stage_does_not_construct_a_road_spatial_index() -> None:
    with patch("shapely.STRtree", side_effect=AssertionError("forbidden")):
        _assess()
    source = Path("src/landscout/stages/assess_road_proximity_coverage.py").read_text(
        encoding="utf-8"
    )
    assert "STRtree(" not in source
    assert "query_nearest(" not in source


@pytest.mark.parametrize(
    "mutation",
    [
        lambda result: object(),
        lambda result: replace(result, parcels=result.parcels.drop(columns="geometry")),
        lambda result: replace(
            result,
            class_proximity=result.class_proximity.drop(
                columns="nearest_road_proxy_distance_m"
            ),
        ),
        lambda result: replace(
            result, class_proximity=result.class_proximity.iloc[:-1].copy()
        ),
        lambda result: replace(
            result,
            class_proximity=result.class_proximity.iloc[
                [1, 0, *range(2, 5)]
            ].reset_index(drop=True),
        ),
        lambda result: replace(
            result,
            class_proximity=result.class_proximity.assign(
                proximity_scope="GLOBAL_NEAREST"
            ),
        ),
        lambda result: replace(
            result,
            class_proximity=result.class_proximity.assign(
                road_proxy_policy_config_sha256=["c" * 64, *["d" * 64] * 4]
            ),
        ),
    ],
    ids=[
        "wrong-type",
        "bad-parcels",
        "missing-column",
        "row-count",
        "order",
        "scope",
        "policy-sha",
    ],
)
def test_malformed_upstream_result_fails_before_coverage_load(mutation: Any) -> None:
    parcels = _parcels()
    malformed = mutation(_proximity(parcels))
    with (
        patch(
            "landscout.stages.assess_road_proximity_coverage.enrich_parcel_road_proximity",
            return_value=malformed,
        ),
        patch(
            "landscout.stages.assess_road_proximity_coverage.load_ign_bdtopo_department_coverage"
        ) as coverage_loader,
        pytest.raises(RoadProximityCoverageError),
    ):
        assess_road_proximity_coverage(parcels, _road_source(), SOURCE_CONFIG)
    coverage_loader.assert_not_called()


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("source_provider", "Other provider"),
        ("source_product", "Other product"),
        ("source_department_code", "32"),
        ("source_edition", "2099-01-01"),
        ("source_product_version", "99"),
        ("source_archive_sha256", "c" * 64),
    ],
)
def test_coverage_package_lineage_must_match_road_archive(
    field: str, value: object
) -> None:
    coverage = _coverage()
    frame = coverage.coverage.copy()
    frame[field] = value
    if field == "source_department_code":
        frame[coverage.summary.department_code_field] = value
        summary = replace(coverage.summary, selected_department_code=cast(str, value))
    else:
        summary = coverage.summary
    forged = replace(coverage, coverage=frame, summary=summary, **{field: value})
    with pytest.raises(
        RoadProximityCoverageError, match="package|lineage|provider|product"
    ):
        _assess(coverage=forged, road_source=_road_source(coverage.extraction))


def test_configured_coverage_layer_cannot_be_replaced_by_real_alternate_layer() -> None:
    coverage = _coverage(layer="zone_administrative")
    with pytest.raises(RoadProximityCoverageError, match="configured|layer"):
        _assess(coverage=coverage, road_source=_road_source(coverage.extraction))


def test_selected_department_identity_is_exact() -> None:
    coverage = _coverage()
    frame = coverage.coverage.copy()
    frame[coverage.summary.department_code_field] = "32"
    forged = replace(
        coverage,
        coverage=frame,
        summary=replace(coverage.summary, selected_department_code="32"),
    )
    with pytest.raises(RoadProximityCoverageError, match="department"):
        _assess(coverage=forged)


def test_coverage_spatial_role_and_source_type_are_controlled() -> None:
    coverage = _coverage()
    frame = coverage.coverage.copy()
    frame["spatial_role"] = "PROXY_GEOMETRY"
    wrong_role = replace(
        coverage,
        coverage=frame,
        summary=replace(
            coverage.summary,
            spatial_role=cast(Any, "PROXY_GEOMETRY"),
        ),
        spatial_role=cast(Any, "PROXY_GEOMETRY"),
    )
    with pytest.raises(RoadProximityCoverageError, match="spatial|lineage"):
        _assess(coverage=wrong_role)

    parcels = _parcels()
    with (
        patch(
            "landscout.stages.assess_road_proximity_coverage.enrich_parcel_road_proximity",
            return_value=_proximity(parcels),
        ),
        patch(
            "landscout.stages.assess_road_proximity_coverage.load_ign_bdtopo_department_coverage",
            return_value=object(),
        ),
        pytest.raises(RoadProximityCoverageError),
    ):
        assess_road_proximity_coverage(parcels, _road_source(), SOURCE_CONFIG)


def test_coverage_must_retain_same_extraction_object() -> None:
    coverage = _coverage()
    forged = replace(coverage, extraction=replace(coverage.extraction))
    with pytest.raises(RoadProximityCoverageError, match="extraction"):
        _assess(coverage=forged, road_source=_road_source(coverage.extraction))


@pytest.mark.parametrize(
    ("geometries", "crs", "message"),
    [
        ([], "EPSG:2154", "one|exactly"),
        (
            [Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])] * 2,
            "EPSG:2154",
            "one|exactly",
        ),
        ([Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])], None, "CRS"),
        ([Polygon([(0, 0), (0, 1), (1, 1), (1, 0), (0, 0)])], "EPSG:4326", "2154"),
        ([None], "EPSG:2154", "null"),
        ([Polygon()], "EPSG:2154", "empty"),
        ([Polygon([(0, 0), (10, 10), (10, 0), (0, 10), (0, 0)])], "EPSG:2154", "valid"),
        ([Point(0, 0)], "EPSG:2154", "Polygon"),
        ([LineString([(0, 0), (10, 10)])], "EPSG:2154", "Polygon"),
    ],
    ids=[
        "zero",
        "two",
        "no-crs",
        "wrong-crs",
        "null",
        "empty",
        "invalid",
        "point",
        "line",
    ],
)
def test_invalid_coverage_geometry_is_rejected(
    geometries: list[object], crs: str | None, message: str
) -> None:
    coverage = _coverage(geometries=geometries, crs=crs)
    with pytest.raises(RoadProximityCoverageError, match=message):
        _assess(coverage=coverage)


@pytest.mark.parametrize(
    "geometry",
    [
        Polygon([(0, 0), (0, 1000), (1000, 1000), (1000, 0), (0, 0)]),
        MultiPolygon([Polygon([(0, 0), (0, 1000), (1000, 1000), (1000, 0), (0, 0)])]),
    ],
)
def test_polygonal_coverage_geometry_is_accepted(geometry: object) -> None:
    assert len(_assess(coverage=_coverage(geometries=[geometry])).parcels) == 1


@pytest.mark.parametrize(
    ("geometry", "position"),
    [
        (
            Polygon([(100, 100), (100, 200), (200, 200), (200, 100), (100, 100)]),
            "FULLY_COVERED",
        ),
        (
            Polygon([(0, 100), (0, 200), (100, 200), (100, 100), (0, 100)]),
            "OUTSIDE_OR_CROSSING_COVERAGE",
        ),
        (
            Polygon([(-10, 100), (-10, 200), (100, 200), (100, 100), (-10, 100)]),
            "OUTSIDE_OR_CROSSING_COVERAGE",
        ),
        (
            Polygon([(-200, 100), (-200, 200), (-100, 200), (-100, 100), (-200, 100)]),
            "OUTSIDE_OR_CROSSING_COVERAGE",
        ),
    ],
    ids=["inside", "touching", "crossing", "outside"],
)
def test_full_parcel_coverage_position_is_conservative(
    geometry: Polygon, position: str
) -> None:
    parcels = _parcels([geometry])
    row = _first_row(_assess(parcels=parcels, proximity=_proximity(parcels)))
    assert row.road_source_coverage_position == position
    if position != "FULLY_COVERED":
        assert row.road_source_boundary_distance_m == 0.0


def test_position_uses_full_geometry_not_centroid() -> None:
    crossing_with_inside_centroid = Polygon(
        [(-10, 100), (-10, 200), (300, 200), (300, 100), (-10, 100)]
    )
    parcels = _parcels([crossing_with_inside_centroid])
    row = _first_row(_assess(parcels=parcels, proximity=_proximity(parcels)))
    assert row.road_source_coverage_position == "OUTSIDE_OR_CROSSING_COVERAGE"
    assert row.road_source_boundary_distance_m == 0.0


def test_internal_boundary_distance_is_full_geometry_finite_and_nonnegative() -> None:
    parcels = _parcels()
    coverage = _coverage()
    expected = _measured_boundary_distance(parcels, coverage)
    result = _assess(parcels=parcels, proximity=_proximity(parcels), coverage=coverage)
    values = result.class_proximity["road_source_boundary_distance_m"]
    assert values.eq(expected).all()
    assert np.isfinite(values).all()
    assert values.ge(0).all()


@pytest.mark.parametrize(
    ("offset", "expected"),
    [
        (-50.0, "NOT_BOUNDARY_LIMITED"),
        (-0.001, "NOT_BOUNDARY_LIMITED"),
        (0.0, "BOUNDARY_LIMITED"),
        (50.0, "BOUNDARY_LIMITED"),
    ],
)
def test_strict_boundary_status_logic(offset: float, expected: str) -> None:
    parcels = _parcels()
    coverage = _coverage()
    margin = _measured_boundary_distance(parcels, coverage)
    proximity = _proximity(
        parcels,
        distances={road_class: margin + offset for road_class in ELIGIBLE_CLASSES},
    )
    result = _assess(parcels=parcels, proximity=proximity, coverage=coverage)
    assert result.class_proximity["road_proximity_coverage_status"].eq(expected).all()


@pytest.mark.parametrize(
    "geometry",
    [
        Polygon([(-10, 100), (-10, 200), (100, 200), (100, 100), (-10, 100)]),
        Polygon([(0, 100), (0, 200), (100, 200), (100, 100), (0, 100)]),
        Polygon([(-200, 100), (-200, 200), (-100, 200), (-100, 100), (-200, 100)]),
    ],
    ids=["crossing", "touching", "outside"],
)
def test_matched_outside_or_crossing_status(geometry: Polygon) -> None:
    parcels = _parcels([geometry])
    result = _assess(parcels=parcels, proximity=_proximity(parcels))
    assert (
        result.class_proximity["road_proximity_coverage_status"]
        .eq("OUTSIDE_OR_CROSSING_COVERAGE")
        .all()
    )


@pytest.mark.parametrize(
    "geometry",
    [
        Polygon([(100, 100), (100, 200), (200, 200), (200, 100), (100, 100)]),
        Polygon([(-200, 100), (-200, 200), (-100, 200), (-100, 100), (-200, 100)]),
    ],
    ids=["inside", "outside"],
)
def test_no_match_takes_precedence_over_coverage_position(geometry: Polygon) -> None:
    parcels = _parcels([geometry])
    proximity = _without_match(_proximity(parcels))
    result = _assess(parcels=parcels, proximity=proximity)
    assert (
        _first_row(result, "UNKNOWN_REVIEW").road_proximity_coverage_status
        == "NO_MATCH"
    )


def test_classes_are_diagnosed_independently() -> None:
    parcels = _parcels()
    coverage = _coverage()
    margin = _measured_boundary_distance(parcels, coverage)
    proximity = _proximity(
        parcels,
        distances={
            "GENERAL_VEHICLE_PROXY": margin - 1,
            "RESTRICTED_REVIEW": margin + 1,
        },
    )
    result = _assess(parcels=parcels, proximity=proximity, coverage=coverage)
    assert (
        _first_row(result, "GENERAL_VEHICLE_PROXY").road_proximity_coverage_status
        == "NOT_BOUNDARY_LIMITED"
    )
    assert (
        _first_row(result, "RESTRICTED_REVIEW").road_proximity_coverage_status
        == "BOUNDARY_LIMITED"
    )


def test_exact_coverage_lineage_is_appended_to_every_row() -> None:
    coverage = _coverage()
    result = _assess(coverage=coverage)
    expected = {
        "road_source_coverage_provider": coverage.source_provider,
        "road_source_coverage_product": coverage.source_product,
        "road_source_coverage_department_code": coverage.source_department_code,
        "road_source_coverage_edition": coverage.source_edition,
        "road_source_coverage_product_version": coverage.source_product_version,
        "road_source_coverage_archive_sha256": coverage.source_archive_sha256,
        "road_source_coverage_layer": coverage.source_layer,
        "road_source_coverage_spatial_role": coverage.spatial_role,
    }
    for column, value in expected.items():
        assert result.class_proximity[column].eq(value).all()


@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("nearest_source_department_code", "32"),
        ("nearest_source_edition", "2099-01-01"),
        ("nearest_source_archive_sha256", "c" * 64),
    ],
)
def test_matched_road_lineage_must_match_coverage(column: str, value: str) -> None:
    proximity = _proximity()
    table = proximity.class_proximity.copy()
    table[column] = value
    with pytest.raises(RoadProximityCoverageError, match="lineage|package"):
        _assess(proximity=replace(proximity, class_proximity=table))


def test_result_preserves_every_upstream_fact_and_input_object() -> None:
    parcels = _parcels(
        [
            Polygon([(100, 100), (100, 200), (200, 200), (200, 100), (100, 100)]),
            Polygon([(300, 300), (300, 400), (400, 400), (400, 300), (300, 300)]),
        ],
        identifiers=["SECOND", "FIRST"],
    )
    proximity = _proximity(parcels)
    coverage = _coverage()
    road_source = _road_source(coverage.extraction)
    parcels_before = deepcopy(parcels)
    proximity_parcels_before = deepcopy(proximity.parcels)
    table_before = deepcopy(proximity.class_proximity)
    coverage_before = deepcopy(coverage.coverage)
    roads_before = deepcopy(road_source.road_segments)
    road_summary_before = road_source.road_segments_summary
    extraction_before = road_source.extraction
    config_before = SOURCE_CONFIG.model_dump(mode="python")
    result = _assess(
        parcels=parcels,
        proximity=proximity,
        coverage=coverage,
        road_source=road_source,
    )

    assert_geodataframe_equal(parcels, parcels_before)
    assert_geodataframe_equal(proximity.parcels, proximity_parcels_before)
    assert_frame_equal(proximity.class_proximity, table_before)
    assert_geodataframe_equal(coverage.coverage, coverage_before)
    assert_geodataframe_equal(road_source.road_segments, roads_before)
    assert road_source.road_segments_summary == road_summary_before
    assert road_source.extraction is extraction_before
    assert SOURCE_CONFIG.model_dump(mode="python") == config_before
    assert_geodataframe_equal(result.parcels, proximity_parcels_before)
    assert_frame_equal(
        result.class_proximity.loc[:, list(CLASS_PROXIMITY_COLUMNS)],
        table_before,
        check_dtype=True,
        check_index_type=True,
    )
    assert (
        tuple(result.class_proximity.columns[: len(CLASS_PROXIMITY_COLUMNS)])
        == CLASS_PROXIMITY_COLUMNS
    )
    assert (
        tuple(result.class_proximity.columns[len(CLASS_PROXIMITY_COLUMNS) :])
        == DIAGNOSTIC_COLUMNS
    )
    assert result.class_coverage is proximity.class_coverage
    assert result.source_coverage is coverage


def _corrupt_generated(column: str, value: object, *, outside: bool = False) -> None:
    module = import_module("landscout.stages.assess_road_proximity_coverage")

    geometry = (
        Polygon([(-200, 100), (-200, 200), (-100, 200), (-100, 100), (-200, 100)])
        if outside
        else None
    )
    parcels = _parcels([geometry]) if geometry is not None else _parcels()
    proximity = _proximity(parcels)
    original = module._diagnosed_class_proximity

    def corrupt(*args: object, **kwargs: object) -> pd.DataFrame:
        output = original(*args, **kwargs)
        output[column] = output[column].astype("object")
        output.at[0, column] = value
        return output

    with (
        patch.object(module, "_diagnosed_class_proximity", side_effect=corrupt),
        pytest.raises(RoadProximityCoverageError),
    ):
        _assess(parcels=parcels, proximity=proximity)


@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("road_source_boundary_distance_m", -1.0),
        ("road_source_boundary_distance_m", float("nan")),
        ("road_source_boundary_distance_m", float("inf")),
        ("road_source_coverage_position", "INVENTED"),
        ("road_proximity_coverage_status", "INVENTED"),
    ],
)
def test_malformed_generated_value_is_rejected(column: str, value: object) -> None:
    _corrupt_generated(column, value)


@pytest.mark.parametrize(
    ("distance", "wrong_status"),
    [(50.0, "BOUNDARY_LIMITED"), (150.0, "NOT_BOUNDARY_LIMITED")],
)
def test_inconsistent_generated_status_is_rejected(
    distance: float, wrong_status: str
) -> None:
    module = import_module("landscout.stages.assess_road_proximity_coverage")

    parcels = _parcels()
    proximity = _proximity(
        parcels, distances={road_class: distance for road_class in ELIGIBLE_CLASSES}
    )
    original = module._diagnosed_class_proximity

    def corrupt(*args: object, **kwargs: object) -> pd.DataFrame:
        output = original(*args, **kwargs)
        output.at[0, "road_proximity_coverage_status"] = wrong_status
        return output

    with (
        patch.object(module, "_diagnosed_class_proximity", side_effect=corrupt),
        pytest.raises(RoadProximityCoverageError),
    ):
        _assess(parcels=parcels, proximity=proximity)


def test_outside_position_requires_zero_boundary_distance() -> None:
    _corrupt_generated("road_source_boundary_distance_m", 1.0, outside=True)


def test_result_is_frozen_and_has_no_business_decision_fields() -> None:
    result = _assess()
    with pytest.raises(FrozenInstanceError):
        result.parcels = _parcels()  # type: ignore[misc]
    forbidden = {
        "accessible",
        "road_access_ok",
        "legal_access",
        "truck_access",
        "bess_access",
        "score",
        "retained",
        "rejected",
    }
    assert forbidden.isdisjoint(result.parcels.columns)
    assert forbidden.isdisjoint(result.class_proximity.columns)

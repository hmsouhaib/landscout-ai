import json
import tempfile
from copy import deepcopy
from dataclasses import replace
from hashlib import sha256
from pathlib import Path
from typing import Any, cast
from unittest.mock import patch
from uuid import uuid4

import geopandas as gpd
import pyogrio
import pytest
from geopandas.testing import assert_geodataframe_equal
from pandas.testing import assert_frame_equal
from shapely.geometry import (
    LineString,
    MultiPolygon,
    Point,
    Polygon,
)

import landscout.sources.ign_bdtopo_fr as ign_source
from landscout import stages
from landscout.sources import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_source_config,
)
from landscout.stages import (
    GridCoverageAssessmentError,
    profile_grid_coverage,
)
from landscout.stages import (
    assess_grid_coverage as public_assess_grid_coverage,
)
from landscout.stages.assess_grid_coverage import (
    _assess_grid_coverage_from_proximity as assess_grid_coverage,
)
from landscout.stages.enrich_grid_proximity import (
    _enrich_parcel_grid_proximity_from_normalized as enrich_parcel_grid_proximity,
)

ARCHIVE_SHA256 = "a" * 64
EDITION = "2026-06-15"
_FIXTURE_ROOT = Path(tempfile.mkdtemp(prefix="landscout-coverage-ign-"))
_SOURCE_CONFIG_PAYLOAD = load_ign_bdtopo_source_config().model_dump(mode="json")
_SOURCE_CONFIG_PAYLOAD.update(
    {
        "source_url": "https://example.test/BDTOPO.7z",
        "checksum_url": None,
        "official_checksum_algorithm": None,
        "official_checksum": None,
        "expected_archive_size_bytes": 1,
    }
)
SOURCE_CONFIG = IgnBdTopoSourceConfig.model_validate(_SOURCE_CONFIG_PAYLOAD)
ALTERNATE_COVERAGE_LAYER = "zone_administrative"


def _coverage(
    geometry: object = Polygon([(0, 0), (0, 1000), (1000, 1000), (1000, 0), (0, 0)]),
    *,
    crs: str | None = "EPSG:2154",
    spatial_role: str = "SOURCE_COVERAGE_BOUNDARY",
) -> IgnBdTopoDepartmentCoverage:
    raw_frame = gpd.GeoDataFrame(
        {
            "code_insee": ["31"],
            "nom_officiel": ["Haute-Garonne"],
        },
        geometry=[geometry],
        crs=crs,
    )
    extraction_path = _FIXTURE_ROOT / uuid4().hex
    extraction_path.mkdir(parents=True)
    geopackage_path = extraction_path / "data.gpkg"
    dummy = gpd.GeoDataFrame(
        {"id": ["dummy"]},
        geometry=[LineString([(0, 0), (1, 1)])],
        crs=crs or "EPSG:2154",
    )
    pyogrio.write_dataframe(
        dummy, geopackage_path, layer="ligne_electrique", driver="GPKG"
    )
    pyogrio.write_dataframe(
        dummy,
        geopackage_path,
        layer="poste_de_transformation",
        driver="GPKG",
        append=True,
    )
    pyogrio.write_dataframe(
        raw_frame,
        geopackage_path,
        layer="departement",
        driver="GPKG",
        append=True,
    )
    pyogrio.write_dataframe(
        dummy,
        geopackage_path,
        layer="troncon_de_route",
        driver="GPKG",
        append=True,
    )
    raw_frame = gpd.read_file(geopackage_path, layer="departement", engine="pyogrio")
    payload = geopackage_path.read_bytes()
    digest = sha256(payload).hexdigest()
    layer_names = tuple(str(row[0]) for row in pyogrio.list_layers(geopackage_path))
    (extraction_path / ".landscout-extraction.json").write_text(
        json.dumps(
            {
                "schema_version": 3,
                "archive_sha256": ARCHIVE_SHA256,
                "geopackage_relative_path": "data.gpkg",
                "geopackage_size_bytes": len(payload),
                "geopackage_sha256": digest,
                "all_layer_names": list(layer_names),
                "electric_lines_layer": "ligne_electrique",
                "transformation_posts_layer": "poste_de_transformation",
                "road_segments_layer": "troncon_de_route",
                "department_layer": "departement",
                "extracted_entries": [
                    {
                        "relative_path": "data.gpkg",
                        "kind": "file",
                        "size_bytes": len(payload),
                        "sha256": digest,
                    }
                ],
                "spatial_role": "PROXY_GEOMETRY",
            }
        ),
        encoding="utf-8",
    )
    archive = IgnBdTopoDownload(
        provider=SOURCE_CONFIG.provider,
        product="BD TOPO",
        department_code="31",
        edition=EDITION,
        product_version="3.5",
        projection="EPSG:2154",
        package_format="GPKG",
        archive_format="7z",
        source_url="https://example.test/BDTOPO.7z",
        checksum_url=None,
        download_timestamp="2026-08-11T15:32:03+00:00",
        filename="BDTOPO.7z",
        file_size=1,
        sha256=ARCHIVE_SHA256,
        official_checksum_algorithm=None,
        official_checksum=None,
        official_checksum_validated=False,
        path=extraction_path / "BDTOPO.7z",
        cache_hit=True,
    )
    extraction = IgnBdTopoExtraction(
        archive=archive,
        extraction_path=extraction_path,
        geopackage_path=geopackage_path,
        geopackage_filename="data.gpkg",
        geopackage_size_bytes=len(payload),
        geopackage_sha256=digest,
        all_layer_names=layer_names,
        electric_lines_layer="ligne_electrique",
        transformation_posts_layer="poste_de_transformation",
        road_segments_layer="troncon_de_route",
        department_layer="departement",
        cache_hit=True,
    )
    frame = raw_frame.copy()
    for column, value in {
        "source_provider": SOURCE_CONFIG.provider,
        "source_product": "BD TOPO",
        "source_department_code": "31",
        "source_edition": EDITION,
        "source_product_version": "3.5",
        "source_archive_sha256": ARCHIVE_SHA256,
        "source_layer": "departement",
        "spatial_role": spatial_role,
    }.items():
        frame[column] = value
    geometry_type = tuple(
        sorted(str(value) for value in raw_frame.geometry.dropna().geom_type.unique())
    )
    non_null_geometry = ~frame.geometry.isna()
    non_empty_geometry = non_null_geometry & ~frame.geometry.is_empty
    summary = IgnBdTopoCoverageLayerSummary(
        source_layer_name="departement",
        crs=crs or "",
        source_feature_count=1,
        selected_feature_count=1,
        columns=("code_insee", "nom_officiel", "geometry"),
        dtypes=tuple(
            (str(column), str(dtype)) for column, dtype in raw_frame.dtypes.items()
        ),
        null_geometry_count=int(raw_frame.geometry.isna().sum()),
        empty_geometry_count=int(
            (non_null_geometry & raw_frame.geometry.is_empty).sum()
        ),
        invalid_geometry_count=int(
            (non_empty_geometry & ~raw_frame.geometry.is_valid).sum()
        ),
        geometry_types=geometry_type,
        department_code_field="code_insee",
        selected_department_code="31",
    )
    return IgnBdTopoDepartmentCoverage(
        extraction=extraction,
        coverage=frame,
        summary=summary,
        source_provider=SOURCE_CONFIG.provider,
        source_product="BD TOPO",
        source_department_code="31",
        source_edition=EDITION,
        source_product_version="3.5",
        source_archive_sha256=ARCHIVE_SHA256,
        source_layer="departement",
        spatial_role=spatial_role,
    )


def _with_alternate_coverage_layer(
    source: IgnBdTopoDepartmentCoverage,
) -> tuple[IgnBdTopoDepartmentCoverage, IgnBdTopoDepartmentCoverage]:
    alternate = gpd.GeoDataFrame(
        {"code_insee": ["31"], "nom_officiel": ["Alternate coverage"]},
        geometry=[Polygon([(0, 0), (0, 900), (900, 900), (900, 0), (0, 0)])],
        crs="EPSG:2154",
    )
    geopackage_path = source.extraction.geopackage_path
    pyogrio.write_dataframe(
        alternate,
        geopackage_path,
        layer=ALTERNATE_COVERAGE_LAYER,
        driver="GPKG",
        append=True,
    )
    payload = geopackage_path.read_bytes()
    layer_names = tuple(str(row[0]) for row in pyogrio.list_layers(geopackage_path))
    digest = sha256(payload).hexdigest()
    marker_path = source.extraction.extraction_path / ".landscout-extraction.json"
    marker = json.loads(marker_path.read_text(encoding="utf-8"))
    marker.update(
        geopackage_size_bytes=len(payload),
        geopackage_sha256=digest,
        all_layer_names=list(layer_names),
        extracted_entries=[
            {
                "relative_path": "data.gpkg",
                "kind": "file",
                "size_bytes": len(payload),
                "sha256": digest,
            }
        ],
    )
    marker_path.write_text(json.dumps(marker), encoding="utf-8")
    extraction = replace(
        source.extraction,
        geopackage_size_bytes=len(payload),
        geopackage_sha256=digest,
        all_layer_names=layer_names,
    )
    configured = load_ign_bdtopo_department_coverage(
        extraction,
        SOURCE_CONFIG,
    )
    alternate_loaded = gpd.read_file(
        geopackage_path,
        layer=ALTERNATE_COVERAGE_LAYER,
        engine="pyogrio",
    )
    forged = ign_source._department_coverage_from_frame(
        extraction,
        alternate_loaded,
        ALTERNATE_COVERAGE_LAYER,
        "code_insee",
    )
    return configured, forged


def test_coverage_assessment_reproduces_configured_logical_layer() -> None:
    configured, forged = _with_alternate_coverage_layer(_coverage())

    loaded = load_ign_bdtopo_department_coverage(configured.extraction, SOURCE_CONFIG)
    result = assess_grid_coverage(_proximity(), loaded, SOURCE_CONFIG)
    assert result.source_coverage.source_layer == "departement"

    with pytest.raises(GridCoverageAssessmentError, match="physical|configured"):
        assess_grid_coverage(_proximity(), forged, SOURCE_CONFIG)


def _parcels(
    geometries: list[object] | None = None,
    *,
    crs: str = "EPSG:2154",
) -> gpd.GeoDataFrame:
    values = geometries or [
        Polygon([(100, 100), (100, 200), (200, 200), (200, 100), (100, 100)])
    ]
    return gpd.GeoDataFrame(
        {
            "parcel_id": [f"PARCEL-{position + 1}" for position in range(len(values))],
            "preserved_value": list(range(len(values))),
        },
        geometry=values,
        crs=crs,
        index=[20 + position for position in range(len(values))],
    )


def _lines(
    distances: list[float] | None = None,
    *,
    voltage_statuses: list[str] | None = None,
    voltages: list[float | None] | None = None,
) -> gpd.GeoDataFrame:
    values = distances or [50.0]
    statuses = voltage_statuses or ["EXACT"] * len(values)
    voltage_values = voltages or [110.0] * len(values)
    identifiers = [f"LINE-{position + 1}" for position in range(len(values))]
    return gpd.GeoDataFrame(
        {
            "grid_feature_id": identifiers,
            "grid_feature_type": ["ELECTRIC_LINE"] * len(values),
            "source_feature_id": [f"SOURCE-{value}" for value in identifiers],
            "source_department_code": ["31"] * len(values),
            "source_edition": [EDITION] * len(values),
            "source_archive_sha256": [ARCHIVE_SHA256] * len(values),
            "source_layer": ["ligne_electrique"] * len(values),
            "spatial_role": ["PROXY_GEOMETRY"] * len(values),
            "geometry_status": ["VALID"] * len(values),
            "voltage_raw": [
                None if value is None else str(value) for value in voltage_values
            ],
            "voltage_status": statuses,
            "voltage_kv": voltage_values,
            "voltage_upper_bound_kv": [None] * len(values),
            "manager_name": ["RTE"] * len(values),
            "asset_status_raw": ["En service"] * len(values),
        },
        geometry=[
            LineString([(200 + value, 50), (200 + value, 250)]) for value in values
        ],
        crs="EPSG:2154",
    )


def _posts(distance_m: float = 50.0) -> gpd.GeoDataFrame:
    return gpd.GeoDataFrame(
        {
            "grid_feature_id": ["POST-1"],
            "grid_feature_type": ["TRANSFORMATION_POST"],
            "source_feature_id": ["SOURCE-POST-1"],
            "source_department_code": ["31"],
            "source_edition": [EDITION],
            "source_archive_sha256": [ARCHIVE_SHA256],
            "source_layer": ["poste_de_transformation"],
            "spatial_role": ["PROXY_GEOMETRY"],
            "geometry_status": ["VALID"],
            "name": ["Test post"],
            "importance_raw": ["5"],
            "asset_status_raw": ["En service"],
        },
        geometry=[
            Polygon(
                [
                    (200 + distance_m, 100),
                    (200 + distance_m, 110),
                    (210 + distance_m, 110),
                    (210 + distance_m, 100),
                    (200 + distance_m, 100),
                ]
            )
        ],
        crs="EPSG:2154",
    )


def _electricity_source(
    extraction: IgnBdTopoExtraction,
) -> IgnBdTopoElectricityData:
    return IgnBdTopoElectricityData(
        extraction=extraction,
        electric_lines=_lines(),
        transformation_posts=_posts(),
        electric_lines_summary=cast(Any, None),
        transformation_posts_summary=cast(Any, None),
    )


def _proximity(
    *,
    parcel_geometries: list[object] | None = None,
    parcel_crs: str = "EPSG:2154",
    line_distances: list[float] | None = None,
    post_distance_m: float = 50.0,
    voltage_statuses: list[str] | None = None,
    voltages: list[float | None] | None = None,
):
    return enrich_parcel_grid_proximity(
        _parcels(parcel_geometries, crs=parcel_crs),
        _lines(
            line_distances,
            voltage_statuses=voltage_statuses,
            voltages=voltages,
        ),
        _posts(post_distance_m),
    )


def test_clean_coverage_api_is_exported() -> None:
    assert stages.assess_grid_coverage is public_assess_grid_coverage
    assert stages.profile_grid_coverage is profile_grid_coverage
    assert "assess_grid_coverage" in stages.__all__
    assert "profile_grid_coverage" in stages.__all__


def test_public_coverage_owns_proximity_and_configured_coverage_once() -> None:
    coverage = _coverage()
    source = _electricity_source(coverage.extraction)
    parcels = _parcels()
    proximity = _proximity()

    with (
        patch(
            "landscout.stages.assess_grid_coverage.enrich_parcel_grid_proximity",
            return_value=proximity,
            create=True,
        ) as proximity_stage,
        patch(
            "landscout.stages.assess_grid_coverage.load_ign_bdtopo_department_coverage",
            return_value=coverage,
            create=True,
        ) as coverage_loader,
    ):
        result = public_assess_grid_coverage(parcels, source, SOURCE_CONFIG)

    proximity_stage.assert_called_once_with(parcels, source, SOURCE_CONFIG)
    coverage_loader.assert_called_once_with(source.extraction, SOURCE_CONFIG)
    assert result.source_coverage is coverage


def test_public_coverage_proximity_failure_stops_coverage_loading() -> None:
    coverage = _coverage()
    source = _electricity_source(coverage.extraction)

    with (
        patch(
            "landscout.stages.assess_grid_coverage.enrich_parcel_grid_proximity",
            side_effect=ValueError("physical electricity source changed"),
            create=True,
        ) as proximity_stage,
        patch(
            "landscout.stages.assess_grid_coverage.load_ign_bdtopo_department_coverage",
            create=True,
        ) as coverage_loader,
        pytest.raises(GridCoverageAssessmentError),
    ):
        public_assess_grid_coverage(_parcels(), source, SOURCE_CONFIG)

    proximity_stage.assert_called_once()
    coverage_loader.assert_not_called()


def test_public_coverage_rejects_generated_parcel_column_before_proximity() -> None:
    parcels = _parcels()
    parcels["grid_source_boundary_distance_m"] = 0.0
    source = _electricity_source(cast(Any, None))

    with (
        patch(
            "landscout.stages.assess_grid_coverage.enrich_parcel_grid_proximity",
            create=True,
        ) as proximity_stage,
        patch(
            "landscout.stages.assess_grid_coverage.load_ign_bdtopo_department_coverage",
            create=True,
        ) as coverage_loader,
        pytest.raises(GridCoverageAssessmentError, match="collides.*generated"),
    ):
        public_assess_grid_coverage(parcels, source, SOURCE_CONFIG)

    proximity_stage.assert_not_called()
    coverage_loader.assert_not_called()


def test_caller_provided_proximity_and_coverage_are_not_public_inputs() -> None:
    forged_proximity = _proximity(line_distances=[0.0], post_distance_m=0.0)
    forged_coverage = _coverage()
    assert forged_proximity.parcels["nearest_line_proxy_distance_m"].eq(0.0).all()
    assert (
        forged_proximity.parcels["nearest_line_source_archive_sha256"]
        .eq(ARCHIVE_SHA256)
        .all()
    )

    with (
        patch(
            "landscout.stages.assess_grid_coverage.enrich_parcel_grid_proximity",
            create=True,
        ) as proximity_stage,
        patch(
            "landscout.stages.assess_grid_coverage.load_ign_bdtopo_department_coverage",
            create=True,
        ) as coverage_loader,
        pytest.raises(
            GridCoverageAssessmentError,
            match="parcels|GeoDataFrame",
        ),
    ):
        public_assess_grid_coverage(
            cast(Any, forged_proximity),
            cast(Any, forged_coverage),
            SOURCE_CONFIG,
        )

    proximity_stage.assert_not_called()
    coverage_loader.assert_not_called()


@pytest.mark.parametrize(
    "geometry",
    [
        Polygon([(0, 0), (0, 1000), (1000, 1000), (1000, 0), (0, 0)]),
        MultiPolygon(
            [
                Polygon([(0, 0), (0, 1000), (1000, 1000), (1000, 0), (0, 0)]),
                Polygon([(2000, 0), (2000, 100), (2100, 100), (2100, 0), (2000, 0)]),
            ]
        ),
    ],
)
def test_polygonal_coverage_geometry_is_accepted(geometry: object) -> None:
    result = assess_grid_coverage(_proximity(), _coverage(geometry), SOURCE_CONFIG)

    assert result.parcels.iloc[0]["grid_source_boundary_distance_m"] == pytest.approx(
        100.0
    )


@pytest.mark.parametrize(
    ("geometry", "crs", "message"),
    [
        (
            Polygon([(0, 0), (0, 1000), (1000, 1000), (1000, 0), (0, 0)]),
            None,
            "CRS",
        ),
        (
            Polygon([(0, 0), (0, 1), (1, 1), (1, 0), (0, 0)]),
            "EPSG:4326",
            "2154",
        ),
        (Point(0, 0), "EPSG:2154", "Polygon"),
        (LineString([(0, 0), (10, 10)]), "EPSG:2154", "Polygon"),
        (None, "EPSG:2154", "null"),
        (Polygon(), "EPSG:2154", "empty"),
        (
            Polygon([(0, 0), (20, 20), (20, 0), (0, 20), (0, 0)]),
            "EPSG:2154",
            "valid",
        ),
    ],
)
def test_invalid_coverage_geometry_is_rejected(
    geometry: object,
    crs: str | None,
    message: str,
) -> None:
    with pytest.raises(GridCoverageAssessmentError, match=message):
        assess_grid_coverage(_proximity(), _coverage(geometry, crs=crs), SOURCE_CONFIG)


@pytest.mark.parametrize(
    ("asset_distance", "expected_status"),
    [
        (50.0, "NOT_BOUNDARY_LIMITED"),
        (100.0, "BOUNDARY_LIMITED"),
        (150.0, "BOUNDARY_LIMITED"),
    ],
)
def test_strict_geometric_boundary_proof(
    asset_distance: float,
    expected_status: str,
) -> None:
    result = assess_grid_coverage(
        _proximity(line_distances=[asset_distance], post_distance_m=asset_distance),
        _coverage(),
        SOURCE_CONFIG,
    )

    parcel = result.parcels.iloc[0]
    assert parcel["grid_source_boundary_distance_m"] == pytest.approx(100.0)
    assert parcel["nearest_line_proxy_distance_m"] == pytest.approx(asset_distance)
    assert parcel["nearest_line_coverage_status"] == expected_status
    assert parcel["nearest_exact_line_coverage_status"] == expected_status
    assert parcel["nearest_post_coverage_status"] == expected_status
    assert result.voltage_level_proximity.loc[0, "coverage_status"] == expected_status


@pytest.mark.parametrize(
    "parcel_geometry",
    [
        Polygon([(950, 100), (950, 200), (1050, 200), (1050, 100), (950, 100)]),
        Polygon([(0, 100), (0, 200), (100, 200), (100, 100), (0, 100)]),
        Polygon([(1100, 100), (1100, 200), (1200, 200), (1200, 100), (1100, 100)]),
    ],
    ids=["crossing", "touching", "outside"],
)
def test_outside_crossing_or_touching_parcel_is_conservative(
    parcel_geometry: Polygon,
) -> None:
    result = assess_grid_coverage(
        _proximity(parcel_geometries=[parcel_geometry]),
        _coverage(),
        SOURCE_CONFIG,
    )

    parcel = result.parcels.iloc[0]
    assert parcel["grid_source_boundary_distance_m"] == 0.0
    assert parcel["grid_source_coverage_position"] == "OUTSIDE_OR_CROSSING_COVERAGE"
    assert parcel["nearest_line_coverage_status"] == "OUTSIDE_OR_CROSSING_COVERAGE"
    assert parcel["nearest_exact_line_coverage_status"] == (
        "OUTSIDE_OR_CROSSING_COVERAGE"
    )
    assert parcel["nearest_post_coverage_status"] == "OUTSIDE_OR_CROSSING_COVERAGE"
    assert result.voltage_level_proximity.loc[0, "coverage_status"] == (
        "OUTSIDE_OR_CROSSING_COVERAGE"
    )


def test_no_exact_match_uses_explicit_no_match_status() -> None:
    proximity = _proximity(
        voltage_statuses=["UNKNOWN"],
        voltages=[None],
    )
    result = assess_grid_coverage(proximity, _coverage(), SOURCE_CONFIG)

    assert result.parcels["nearest_exact_line_proxy_distance_m"].isna().all()
    assert result.parcels["nearest_exact_line_coverage_status"].eq("NO_MATCH").all()
    assert result.voltage_level_proximity.empty


def test_assessment_preserves_proximity_values_and_does_not_mutate_input() -> None:
    proximity = _proximity(line_distances=[50.0, 150.0], voltages=[110.0, 275.0])
    parcels_before = deepcopy(proximity.parcels)
    table_before = deepcopy(proximity.voltage_level_proximity)

    result = assess_grid_coverage(proximity, _coverage(), SOURCE_CONFIG)

    assert_geodataframe_equal(proximity.parcels, parcels_before)
    assert_frame_equal(proximity.voltage_level_proximity, table_before)
    assert_geodataframe_equal(
        result.parcels.loc[:, parcels_before.columns],
        parcels_before,
    )
    assert_frame_equal(
        result.voltage_level_proximity.loc[:, table_before.columns],
        table_before,
    )
    assert result.parcels["parcel_id"].tolist() == parcels_before["parcel_id"].tolist()
    assert result.voltage_level_proximity[["parcel_id", "voltage_kv"]].equals(
        table_before[["parcel_id", "voltage_kv"]]
    )


def test_geographic_parcel_storage_crs_and_geometry_are_preserved() -> None:
    projected = _parcels()
    geographic = projected.to_crs("EPSG:4326")
    proximity = enrich_parcel_grid_proximity(geographic, _lines(), _posts())

    result = assess_grid_coverage(proximity, _coverage(), SOURCE_CONFIG)

    assert result.parcels.crs.to_epsg() == 4326
    assert result.parcels.geometry.geom_equals_exact(
        proximity.parcels.geometry, tolerance=0, align=False
    ).all()
    assert result.parcels.iloc[0]["grid_source_boundary_distance_m"] == pytest.approx(
        100.0, abs=1e-6
    )


def test_profile_reports_dynamic_voltage_and_boundary_distributions() -> None:
    result = assess_grid_coverage(
        _proximity(
            line_distances=[50.0, 150.0],
            post_distance_m=100.0,
            voltages=[110.0, 275.0],
        ),
        _coverage(),
        SOURCE_CONFIG,
    )

    profile = profile_grid_coverage(result)

    assert profile.parcel_count == 1
    assert profile.fully_covered_count == 1
    assert profile.outside_or_crossing_count == 0
    assert profile.boundary_distance.minimum == pytest.approx(100.0)
    assert profile.boundary_distance.p50 == pytest.approx(100.0)
    assert profile.boundary_distance.maximum == pytest.approx(100.0)
    assert profile.nearest_line.not_boundary_limited == 1
    assert profile.nearest_post.boundary_limited == 1
    assert [item.voltage_kv for item in profile.voltage_levels] == [110.0, 275.0]
    assert profile.voltage_levels[0].statuses.not_boundary_limited == 1
    assert profile.voltage_levels[1].statuses.boundary_limited == 1


def test_proximity_and_coverage_package_lineage_must_match() -> None:
    proximity = _proximity()
    coverage = _coverage()
    coverage.coverage.loc[0, "source_archive_sha256"] = "b" * 64

    with pytest.raises(GridCoverageAssessmentError, match="lineage"):
        assess_grid_coverage(proximity, coverage, SOURCE_CONFIG)


@pytest.mark.parametrize(
    ("field", "value"),
    [("source_provider", "arbitrary"), ("source_product", "roads")],
)
def test_coverage_rejects_arbitrary_source_identity(field: str, value: str) -> None:
    coverage = replace(_coverage(), **{field: value})
    coverage.coverage.loc[0, field] = value

    with pytest.raises(GridCoverageAssessmentError, match="provider|product|identity"):
        assess_grid_coverage(_proximity(), coverage, SOURCE_CONFIG)


@pytest.mark.parametrize("selected_count", [0, 2])
def test_coverage_summary_selected_count_must_match_frame(
    selected_count: int,
) -> None:
    coverage = _coverage()
    summary = replace(
        coverage.summary,
        selected_feature_count=selected_count,
    )

    with pytest.raises(GridCoverageAssessmentError, match="selected|count"):
        assess_grid_coverage(
            _proximity(), replace(coverage, summary=summary), SOURCE_CONFIG
        )


@pytest.mark.parametrize("mutation", ["missing", "extra", "reordered", "dtype"])
def test_coverage_summary_schema_must_match_selected_source_columns(
    mutation: str,
) -> None:
    coverage = _coverage()
    summary = coverage.summary
    if mutation == "missing":
        changed = replace(summary, columns=summary.columns[:-1])
    elif mutation == "extra":
        changed = replace(summary, columns=(*summary.columns, "invented"))
    elif mutation == "reordered":
        changed = replace(summary, columns=tuple(reversed(summary.columns)))
    else:
        dtypes = list(summary.dtypes)
        dtypes[0] = (dtypes[0][0], "float64")
        changed = replace(summary, dtypes=tuple(dtypes))

    with pytest.raises(
        GridCoverageAssessmentError, match="summary|column|dtype|schema"
    ):
        assess_grid_coverage(
            _proximity(), replace(coverage, summary=changed), SOURCE_CONFIG
        )


def test_coverage_summary_crs_must_match_frame() -> None:
    coverage = _coverage()
    summary = replace(coverage.summary, crs="EPSG:4326")

    with pytest.raises(GridCoverageAssessmentError, match="CRS|2154"):
        assess_grid_coverage(
            _proximity(), replace(coverage, summary=summary), SOURCE_CONFIG
        )


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("null_geometry_count", 1),
        ("empty_geometry_count", 1),
        ("invalid_geometry_count", 1),
        ("geometry_types", ("Point",)),
    ],
)
def test_coverage_summary_geometry_facts_are_validated(
    field: str,
    value: object,
) -> None:
    coverage = _coverage()
    summary = replace(coverage.summary, **{field: value})

    with pytest.raises(GridCoverageAssessmentError, match="geometry|summary"):
        assess_grid_coverage(
            _proximity(), replace(coverage, summary=summary), SOURCE_CONFIG
        )


def test_coverage_summary_selected_department_must_match() -> None:
    coverage = _coverage()
    summary = replace(coverage.summary, selected_department_code="32")

    with pytest.raises(GridCoverageAssessmentError, match="department"):
        assess_grid_coverage(
            _proximity(), replace(coverage, summary=summary), SOURCE_CONFIG
        )


@pytest.mark.parametrize("field", ["", " ", "missing"])
def test_coverage_summary_department_field_must_be_exact(field: str) -> None:
    coverage = _coverage()
    summary = replace(coverage.summary, department_code_field=field)

    with pytest.raises(GridCoverageAssessmentError, match="department|field"):
        assess_grid_coverage(
            _proximity(), replace(coverage, summary=summary), SOURCE_CONFIG
        )


def test_coverage_summary_source_count_cannot_be_smaller_than_selection() -> None:
    coverage = _coverage()
    summary = replace(coverage.summary, source_feature_count=0)

    with pytest.raises(GridCoverageAssessmentError, match="source|count"):
        assess_grid_coverage(
            _proximity(), replace(coverage, summary=summary), SOURCE_CONFIG
        )


def test_coverage_source_layer_lineage_must_match_summary_and_frame() -> None:
    coverage = _coverage()
    summary = replace(coverage.summary, source_layer_name="unknown_layer")

    with pytest.raises(GridCoverageAssessmentError, match="layer|lineage"):
        assess_grid_coverage(
            _proximity(), replace(coverage, summary=summary), SOURCE_CONFIG
        )


def test_public_assessment_loads_coverage_from_the_physical_source() -> None:
    coverage = _coverage()
    source = _electricity_source(coverage.extraction)
    parcels = _parcels()
    proximity = _proximity()

    with patch(
        "landscout.stages.assess_grid_coverage.enrich_parcel_grid_proximity",
        return_value=proximity,
    ):
        result = public_assess_grid_coverage(
            parcels,
            source,
            SOURCE_CONFIG,
        )

    assert result.source_coverage.coverage.loc[0, "nom_officiel"] == "Haute-Garonne"

from copy import deepcopy
from dataclasses import replace

import geopandas as gpd
import pytest
from geopandas.testing import assert_geodataframe_equal
from pandas.testing import assert_frame_equal
from shapely.geometry import (
    LineString,
    MultiPolygon,
    Point,
    Polygon,
)

from landscout import stages
from landscout.sources import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
)
from landscout.stages import (
    GridCoverageAssessmentError,
    assess_grid_coverage,
    enrich_parcel_grid_proximity,
    profile_grid_coverage,
)

ARCHIVE_SHA256 = "a" * 64
EDITION = "2026-06-15"


def _coverage(
    geometry: object = Polygon(
        [(0, 0), (0, 1000), (1000, 1000), (1000, 0), (0, 0)]
    ),
    *,
    crs: str | None = "EPSG:2154",
    spatial_role: str = "SOURCE_COVERAGE_BOUNDARY",
) -> IgnBdTopoDepartmentCoverage:
    frame = gpd.GeoDataFrame(
        {
            "code_insee": ["31"],
            "nom_officiel": ["Haute-Garonne"],
        },
        geometry=[geometry],
        crs=crs,
    )
    for column, value in {
        "source_provider": "IGN",
        "source_product": "BD TOPO",
        "source_department_code": "31",
        "source_edition": EDITION,
        "source_product_version": "3.5",
        "source_archive_sha256": ARCHIVE_SHA256,
        "source_layer": "departement",
        "spatial_role": spatial_role,
    }.items():
        frame[column] = value
    geometry_type = () if geometry is None else (geometry.geom_type,)
    non_null_geometry = ~frame.geometry.isna()
    non_empty_geometry = non_null_geometry & ~frame.geometry.is_empty
    summary = IgnBdTopoCoverageLayerSummary(
        source_layer_name="departement",
        crs=crs or "",
        source_feature_count=1,
        selected_feature_count=1,
        columns=("code_insee", "nom_officiel", "geometry"),
        dtypes=tuple(
            (str(column), str(frame[column].dtype))
            for column in ("code_insee", "nom_officiel", "geometry")
        ),
        null_geometry_count=int(frame.geometry.isna().sum()),
        empty_geometry_count=int(
            (non_null_geometry & frame.geometry.is_empty).sum()
        ),
        invalid_geometry_count=int(
            (non_empty_geometry & ~frame.geometry.is_valid).sum()
        ),
        geometry_types=geometry_type,
        department_code_field="code_insee",
        selected_department_code="31",
    )
    return IgnBdTopoDepartmentCoverage(
        coverage=frame,
        summary=summary,
        source_provider="IGN",
        source_product="BD TOPO",
        source_department_code="31",
        source_edition=EDITION,
        source_product_version="3.5",
        source_archive_sha256=ARCHIVE_SHA256,
        source_layer="departement",
        spatial_role=spatial_role,
    )


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
            "voltage_raw": [None if value is None else str(value) for value in voltage_values],
            "voltage_status": statuses,
            "voltage_kv": voltage_values,
            "voltage_upper_bound_kv": [None] * len(values),
            "manager_name": ["RTE"] * len(values),
            "asset_status_raw": ["En service"] * len(values),
        },
        geometry=[
            LineString([(200 + value, 50), (200 + value, 250)])
            for value in values
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
    assert stages.assess_grid_coverage is assess_grid_coverage
    assert stages.profile_grid_coverage is profile_grid_coverage
    assert "assess_grid_coverage" in stages.__all__
    assert "profile_grid_coverage" in stages.__all__


@pytest.mark.parametrize(
    "geometry",
    [
        Polygon([(0, 0), (0, 1000), (1000, 1000), (1000, 0), (0, 0)]),
        MultiPolygon(
            [
                Polygon([(0, 0), (0, 1000), (1000, 1000), (1000, 0), (0, 0)]),
                Polygon(
                    [(2000, 0), (2000, 100), (2100, 100), (2100, 0), (2000, 0)]
                ),
            ]
        ),
    ],
)
def test_polygonal_coverage_geometry_is_accepted(geometry: object) -> None:
    result = assess_grid_coverage(_proximity(), _coverage(geometry))

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
        assess_grid_coverage(_proximity(), _coverage(geometry, crs=crs))


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
        Polygon(
            [(950, 100), (950, 200), (1050, 200), (1050, 100), (950, 100)]
        ),
        Polygon([(0, 100), (0, 200), (100, 200), (100, 100), (0, 100)]),
        Polygon(
            [(1100, 100), (1100, 200), (1200, 200), (1200, 100), (1100, 100)]
        ),
    ],
    ids=["crossing", "touching", "outside"],
)
def test_outside_crossing_or_touching_parcel_is_conservative(
    parcel_geometry: Polygon,
) -> None:
    result = assess_grid_coverage(
        _proximity(parcel_geometries=[parcel_geometry]),
        _coverage(),
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
    result = assess_grid_coverage(proximity, _coverage())

    assert result.parcels["nearest_exact_line_proxy_distance_m"].isna().all()
    assert result.parcels["nearest_exact_line_coverage_status"].eq("NO_MATCH").all()
    assert result.voltage_level_proximity.empty


def test_assessment_preserves_proximity_values_and_does_not_mutate_input() -> None:
    proximity = _proximity(line_distances=[50.0, 150.0], voltages=[110.0, 275.0])
    parcels_before = deepcopy(proximity.parcels)
    table_before = deepcopy(proximity.voltage_level_proximity)

    result = assess_grid_coverage(proximity, _coverage())

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
    assert result.voltage_level_proximity[
        ["parcel_id", "voltage_kv"]
    ].equals(table_before[["parcel_id", "voltage_kv"]])


def test_geographic_parcel_storage_crs_and_geometry_are_preserved() -> None:
    projected = _parcels()
    geographic = projected.to_crs("EPSG:4326")
    proximity = enrich_parcel_grid_proximity(geographic, _lines(), _posts())

    result = assess_grid_coverage(proximity, _coverage())

    assert result.parcels.crs.to_epsg() == 4326
    assert result.parcels.geometry.geom_equals_exact(
        proximity.parcels.geometry, tolerance=0, align=False
    ).all()
    assert result.parcels.iloc[0][
        "grid_source_boundary_distance_m"
    ] == pytest.approx(100.0, abs=1e-6)


def test_profile_reports_dynamic_voltage_and_boundary_distributions() -> None:
    result = assess_grid_coverage(
        _proximity(
            line_distances=[50.0, 150.0],
            post_distance_m=100.0,
            voltages=[110.0, 275.0],
        ),
        _coverage(),
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
        assess_grid_coverage(proximity, coverage)


@pytest.mark.parametrize(
    ("field", "value"),
    [("source_provider", "arbitrary"), ("source_product", "roads")],
)
def test_coverage_rejects_arbitrary_source_identity(field: str, value: str) -> None:
    coverage = replace(_coverage(), **{field: value})
    coverage.coverage.loc[0, field] = value

    with pytest.raises(GridCoverageAssessmentError, match="provider|product|identity"):
        assess_grid_coverage(_proximity(), coverage)


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
        assess_grid_coverage(_proximity(), replace(coverage, summary=summary))


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

    with pytest.raises(GridCoverageAssessmentError, match="summary|column|dtype|schema"):
        assess_grid_coverage(_proximity(), replace(coverage, summary=changed))


def test_coverage_summary_crs_must_match_frame() -> None:
    coverage = _coverage()
    summary = replace(coverage.summary, crs="EPSG:4326")

    with pytest.raises(GridCoverageAssessmentError, match="CRS|2154"):
        assess_grid_coverage(_proximity(), replace(coverage, summary=summary))


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
        assess_grid_coverage(_proximity(), replace(coverage, summary=summary))


def test_coverage_summary_selected_department_must_match() -> None:
    coverage = _coverage()
    summary = replace(coverage.summary, selected_department_code="32")

    with pytest.raises(GridCoverageAssessmentError, match="department"):
        assess_grid_coverage(_proximity(), replace(coverage, summary=summary))


@pytest.mark.parametrize("field", ["", " ", "missing"])
def test_coverage_summary_department_field_must_be_exact(field: str) -> None:
    coverage = _coverage()
    summary = replace(coverage.summary, department_code_field=field)

    with pytest.raises(GridCoverageAssessmentError, match="department|field"):
        assess_grid_coverage(_proximity(), replace(coverage, summary=summary))


def test_coverage_summary_source_count_cannot_be_smaller_than_selection() -> None:
    coverage = _coverage()
    summary = replace(coverage.summary, source_feature_count=0)

    with pytest.raises(GridCoverageAssessmentError, match="source|count"):
        assess_grid_coverage(_proximity(), replace(coverage, summary=summary))


def test_coverage_source_layer_lineage_must_match_summary_and_frame() -> None:
    coverage = _coverage()
    summary = replace(coverage.summary, source_layer_name="unknown_layer")

    with pytest.raises(GridCoverageAssessmentError, match="layer|lineage"):
        assess_grid_coverage(_proximity(), replace(coverage, summary=summary))

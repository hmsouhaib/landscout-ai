from __future__ import annotations

from copy import deepcopy
from dataclasses import replace

import geopandas as gpd
import numpy as np
import pandas as pd
import pytest
from geopandas.testing import assert_geodataframe_equal
from pandas.api.types import is_float_dtype, is_integer_dtype
from shapely.geometry import (
    GeometryCollection,
    LineString,
    MultiLineString,
    MultiPolygon,
    Point,
    Polygon,
)

from landscout import stages
from landscout.stages import (
    GridProximityError,
    GridProximityResult,
    VoltageLevelCoverage,
    enrich_parcel_grid_proximity,
    profile_grid_proximity,
)
from landscout.stages.enrich_grid_proximity import VOLTAGE_PROXIMITY_COLUMNS

OVERFLOWING_INTEGER = 10**10000


def _geometry_status(geometry: object) -> str:
    if geometry is None:
        return "NULL"
    if geometry.is_empty:
        return "EMPTY"
    if not geometry.is_valid:
        return "INVALID"
    return "VALID"


def _parcels(
    geometries: list[object] | None = None,
    *,
    identifiers: list[object] | None = None,
    crs: str | None = "EPSG:2154",
    index: list[object] | None = None,
) -> gpd.GeoDataFrame:
    values = geometries or [
        Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])
    ]
    count = len(values)
    ids = identifiers or [f"PARCEL-{position + 1}" for position in range(count)]
    source_index = index or [100 + position for position in range(count)]
    return gpd.GeoDataFrame(
        {"parcel_id": ids, "source_value": list(range(count))},
        geometry=values,
        crs=crs,
        index=source_index,
    )


def _lines(
    geometries: list[object] | None = None,
    *,
    identifiers: list[str] | None = None,
    statuses: list[str] | None = None,
    voltage_statuses: list[str] | None = None,
    voltages: list[object] | None = None,
    crs: str | None = "EPSG:2154",
    feature_types: list[str] | None = None,
    spatial_roles: list[str] | None = None,
) -> gpd.GeoDataFrame:
    values = geometries or [LineString([(110, -20), (110, 30)])]
    count = len(values)
    ids = identifiers or [f"LINE-{position + 1}" for position in range(count)]
    geometry_statuses = statuses or [_geometry_status(value) for value in values]
    normalized_voltage_statuses = voltage_statuses or ["EXACT"] * count
    normalized_voltages = voltages or [110.0] * count
    return gpd.GeoDataFrame(
        {
            "grid_feature_id": ids,
            "grid_feature_type": feature_types or ["ELECTRIC_LINE"] * count,
            "source_feature_id": [f"SOURCE-{value}" for value in ids],
            "source_department_code": ["31"] * count,
            "source_edition": ["2026-06-15"] * count,
            "source_archive_sha256": ["a" * 64] * count,
            "source_layer": ["CUSTOM_LINE_LAYER"] * count,
            "spatial_role": spatial_roles or ["PROXY_GEOMETRY"] * count,
            "geometry_status": geometry_statuses,
            "voltage_raw": [
                f"{value:g} kV" if isinstance(value, (int, float)) else None
                for value in normalized_voltages
            ],
            "voltage_status": normalized_voltage_statuses,
            "voltage_kv": normalized_voltages,
            "voltage_upper_bound_kv": [np.nan] * count,
            "manager_name": ["TEST MANAGER"] * count,
            "asset_status_raw": ["En service"] * count,
        },
        geometry=values,
        crs=crs,
    )


def _posts(
    geometries: list[object] | None = None,
    *,
    identifiers: list[str] | None = None,
    statuses: list[str] | None = None,
    crs: str | None = "EPSG:2154",
    feature_types: list[str] | None = None,
    spatial_roles: list[str] | None = None,
) -> gpd.GeoDataFrame:
    values = geometries or [
        Polygon([(110, 0), (110, 10), (120, 10), (120, 0), (110, 0)])
    ]
    count = len(values)
    ids = identifiers or [f"POST-{position + 1}" for position in range(count)]
    geometry_statuses = statuses or [_geometry_status(value) for value in values]
    return gpd.GeoDataFrame(
        {
            "grid_feature_id": ids,
            "grid_feature_type": feature_types or ["TRANSFORMATION_POST"] * count,
            "source_feature_id": [f"SOURCE-{value}" for value in ids],
            "source_department_code": ["31"] * count,
            "source_edition": ["2026-06-15"] * count,
            "source_archive_sha256": ["a" * 64] * count,
            "source_layer": ["CUSTOM_POST_LAYER"] * count,
            "spatial_role": spatial_roles or ["PROXY_GEOMETRY"] * count,
            "geometry_status": geometry_statuses,
            "name": ["Test post"] * count,
            "importance_raw": ["5"] * count,
            "asset_status_raw": ["En service"] * count,
        },
        geometry=values,
        crs=crs,
    )


def _two_parcel_two_voltage_result() -> GridProximityResult:
    parcels = _parcels(
        [
            Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]),
            Polygon([(40, 0), (40, 10), (50, 10), (50, 0), (40, 0)]),
        ],
        identifiers=["PARCEL-2", "PARCEL-1"],
    )
    lines = _lines(
        [
            LineString([(200, -20), (200, 30)]),
            LineString([(100, -20), (100, 30)]),
        ],
        identifiers=["LINE-275", "LINE-110"],
        voltage_statuses=["EXACT", "EXACT"],
        voltages=[275.0, 110.0],
    )
    return enrich_parcel_grid_proximity(parcels, lines, _posts())


def _mutate_parcel_result(
    result: GridProximityResult,
    column: str,
    value: object,
) -> GridProximityResult:
    parcels = result.parcels.copy()
    parcels[column] = parcels[column].astype("object")
    parcels.at[0, column] = value
    return replace(result, parcels=parcels)


def _mutate_voltage_result(
    result: GridProximityResult,
    column: str,
    value: object,
) -> GridProximityResult:
    table = result.voltage_level_proximity.copy()
    table[column] = table[column].astype("object")
    table.at[0, column] = value
    return replace(result, voltage_level_proximity=table)


def test_clean_high_level_api_is_exported() -> None:
    assert stages.enrich_parcel_grid_proximity is enrich_parcel_grid_proximity
    assert stages.profile_grid_proximity is profile_grid_proximity
    assert "enrich_parcel_grid_proximity" in stages.__all__
    assert "profile_grid_proximity" in stages.__all__


def test_separated_distance_uses_parcel_edge_not_centroid() -> None:
    result = enrich_parcel_grid_proximity(_parcels(), _lines(), _posts())

    assert result.parcels.loc[0, "nearest_line_proxy_distance_m"] == pytest.approx(
        100.0
    )
    assert result.parcels.loc[0, "nearest_post_proxy_distance_m"] == pytest.approx(
        100.0
    )


def test_touching_line_has_zero_distance() -> None:
    touching = _lines([LineString([(10, -20), (10, 30)])])

    result = enrich_parcel_grid_proximity(_parcels(), touching, _posts())

    assert result.parcels.loc[0, "nearest_line_proxy_distance_m"] == 0.0


def test_post_distance_uses_parcel_and_post_polygons() -> None:
    posts = _posts(
        [Polygon([(60, 0), (60, 10), (70, 10), (70, 0), (60, 0)])]
    )

    result = enrich_parcel_grid_proximity(_parcels(), _lines(), posts)

    assert result.parcels.loc[0, "nearest_post_proxy_distance_m"] == pytest.approx(
        50.0
    )


def test_epsg4326_input_is_calculated_in_lambert93_and_preserved() -> None:
    projected = _parcels()
    geographic = projected.to_crs("EPSG:4326")
    before_geometry = geographic.geometry.copy()

    result = enrich_parcel_grid_proximity(geographic, _lines(), _posts())

    assert result.parcels.crs == geographic.crs
    assert result.parcels.loc[0, "nearest_line_proxy_distance_m"] == pytest.approx(
        100.0, abs=1e-6
    )
    assert result.parcels.geometry.geom_equals_exact(
        before_geometry.reset_index(drop=True), tolerance=0
    ).all()


def test_epsg2154_parcel_input_remains_epsg2154() -> None:
    result = enrich_parcel_grid_proximity(_parcels(), _lines(), _posts())

    assert result.parcels.crs is not None
    assert result.parcels.crs.to_epsg() == 2154


def test_valid_parcel_id_is_preserved_exactly() -> None:
    result = enrich_parcel_grid_proximity(
        _parcels(identifiers=["FR-31-VALID-ID"]), _lines(), _posts()
    )

    assert result.parcels["parcel_id"].tolist() == ["FR-31-VALID-ID"]


@pytest.mark.parametrize(
    "identifier",
    [None, "", "   ", " PARCEL-1", "PARCEL-1 ", 123],
)
def test_invalid_parcel_id_hygiene_is_rejected(identifier: object) -> None:
    with pytest.raises(GridProximityError, match="parcel_id"):
        enrich_parcel_grid_proximity(
            _parcels(identifiers=[identifier]), _lines(), _posts()
        )


@pytest.mark.parametrize(
    "geometry",
    [
        Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]),
        MultiPolygon(
            [Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])]
        ),
        Polygon([(0, 0, 5), (0, 10, 5), (10, 10, 5), (10, 0, 5), (0, 0, 5)]),
    ],
)
def test_supported_parcel_polygon_geometry_is_preserved(geometry: object) -> None:
    result = enrich_parcel_grid_proximity(_parcels([geometry]), _lines(), _posts())

    assert result.parcels.geometry.iloc[0].equals_exact(geometry, tolerance=0)
    assert result.parcels.geometry.iloc[0].has_z == geometry.has_z


@pytest.mark.parametrize(
    "geometry",
    [
        Point(1, 1),
        LineString([(0, 0), (10, 10)]),
        MultiLineString([[(0, 0), (10, 10)]]),
        GeometryCollection([Point(1, 1)]),
    ],
)
def test_semantically_wrong_parcel_geometry_is_rejected(geometry: object) -> None:
    with pytest.raises(GridProximityError, match="Polygon|MultiPolygon"):
        enrich_parcel_grid_proximity(_parcels([geometry]), _lines(), _posts())


@pytest.mark.parametrize("kind", ["parcel", "line", "post"])
def test_missing_crs_is_rejected(kind: str) -> None:
    parcels = _parcels(crs=None if kind == "parcel" else "EPSG:2154")
    lines = _lines(crs=None if kind == "line" else "EPSG:2154")
    posts = _posts(crs=None if kind == "post" else "EPSG:2154")

    with pytest.raises(GridProximityError, match="CRS"):
        enrich_parcel_grid_proximity(parcels, lines, posts)


@pytest.mark.parametrize("kind", ["line", "post"])
def test_wrong_grid_crs_is_rejected(kind: str) -> None:
    lines = _lines(crs="EPSG:4326" if kind == "line" else "EPSG:2154")
    posts = _posts(crs="EPSG:4326" if kind == "post" else "EPSG:2154")

    with pytest.raises(GridProximityError, match="2154"):
        enrich_parcel_grid_proximity(_parcels(), lines, posts)


def test_z_line_has_same_horizontal_distance_as_xy_line() -> None:
    xy = _lines([LineString([(110, -20), (110, 30)])])
    xyz = _lines([LineString([(110, -20, 500), (110, 30, 900)])])

    xy_result = enrich_parcel_grid_proximity(_parcels(), xy, _posts())
    xyz_result = enrich_parcel_grid_proximity(_parcels(), xyz, _posts())

    assert xyz.geometry.iloc[0].has_z
    assert xyz_result.parcels.loc[
        0, "nearest_line_proxy_distance_m"
    ] == pytest.approx(xy_result.parcels.loc[0, "nearest_line_proxy_distance_m"])


def test_line_tie_is_counted_and_lexical_feature_id_wins() -> None:
    lines = _lines(
        [
            LineString([(-100, -20), (-100, 30)]),
            LineString([(110, -20), (110, 30)]),
        ],
        identifiers=["Z-LINE", "A-LINE"],
    )

    result = enrich_parcel_grid_proximity(_parcels(), lines, _posts())

    row = result.parcels.iloc[0]
    assert row["nearest_line_proxy_distance_m"] == pytest.approx(100.0)
    assert row["nearest_line_tie_count"] == 2
    assert row["nearest_line_grid_feature_id"] == "A-LINE"
    assert len(result.parcels) == 1


def test_nonvalid_grid_geometries_are_excluded_without_row_loss() -> None:
    invalid = Polygon([(0, 0), (20, 20), (20, 0), (0, 20), (0, 0)])
    lines = _lines(
        [None, LineString(), invalid, LineString([(110, -20), (110, 30)])],
        identifiers=["NULL", "EMPTY", "INVALID", "VALID"],
        voltage_statuses=["UNKNOWN", "UNKNOWN", "UNKNOWN", "EXACT"],
        voltages=[None, None, None, 110.0],
    )

    result = enrich_parcel_grid_proximity(_parcels(), lines, _posts())

    assert len(result.parcels) == 1
    assert result.parcels.loc[0, "nearest_line_grid_feature_id"] == "VALID"


@pytest.mark.parametrize("kind", ["line", "post"])
def test_wrong_grid_feature_type_is_rejected(kind: str) -> None:
    lines = _lines(feature_types=["WRONG"] if kind == "line" else None)
    posts = _posts(feature_types=["WRONG"] if kind == "post" else None)

    with pytest.raises(GridProximityError, match="grid_feature_type"):
        enrich_parcel_grid_proximity(_parcels(), lines, posts)


@pytest.mark.parametrize("kind", ["line", "post"])
def test_duplicate_grid_feature_id_is_rejected(kind: str) -> None:
    if kind == "line":
        lines = _lines(
            [LineString([(100, 0), (100, 10)])] * 2,
            identifiers=["DUPLICATE", "DUPLICATE"],
        )
        posts = _posts()
    else:
        lines = _lines()
        posts = _posts(
            [
                Polygon([(50, 0), (50, 5), (55, 5), (55, 0), (50, 0)]),
                Polygon([(60, 0), (60, 5), (65, 5), (65, 0), (60, 0)]),
            ],
            identifiers=["DUPLICATE", "DUPLICATE"],
        )

    with pytest.raises(GridProximityError, match="unique"):
        enrich_parcel_grid_proximity(_parcels(), lines, posts)


@pytest.mark.parametrize("kind", ["line", "post"])
def test_wrong_spatial_role_is_rejected(kind: str) -> None:
    lines = _lines(spatial_roles=["EXACT"] if kind == "line" else None)
    posts = _posts(spatial_roles=["EXACT"] if kind == "post" else None)

    with pytest.raises(GridProximityError, match="PROXY_GEOMETRY"):
        enrich_parcel_grid_proximity(_parcels(), lines, posts)


@pytest.mark.parametrize(
    ("kind", "geometry"),
    [
        ("line", Point(100, 0)),
        ("line", Polygon([(100, 0), (100, 5), (105, 5), (105, 0), (100, 0)])),
        ("post", Point(100, 0)),
        ("post", LineString([(100, 0), (100, 10)])),
    ],
)
def test_unsupported_valid_grid_geometry_type_is_rejected(
    kind: str, geometry: object
) -> None:
    lines = _lines([geometry]) if kind == "line" else _lines()
    posts = _posts([geometry]) if kind == "post" else _posts()

    with pytest.raises(GridProximityError, match="geometry types"):
        enrich_parcel_grid_proximity(_parcels(), lines, posts)


def test_supported_multi_geometries_are_accepted() -> None:
    lines = _lines(
        [MultiLineString([[(110, -20), (110, 30)], [(120, -20), (120, 30)]])]
    )
    posts = _posts(
        [
            MultiPolygon(
                [
                    Polygon(
                        [(110, 0), (110, 5), (115, 5), (115, 0), (110, 0)]
                    )
                ]
            )
        ]
    )

    result = enrich_parcel_grid_proximity(_parcels(), lines, posts)

    assert len(result.parcels) == 1


@pytest.mark.parametrize(
    "status", ["EXACT", "BELOW", "UNKNOWN", "DEENERGIZED", "UNPARSED"]
)
def test_nearest_any_line_preserves_every_voltage_status(status: str) -> None:
    voltage = 110.0 if status == "EXACT" else None
    lines = _lines(voltage_statuses=[status], voltages=[voltage])

    result = enrich_parcel_grid_proximity(_parcels(), lines, _posts())

    assert result.parcels.loc[0, "nearest_line_voltage_status"] == status


def test_nearest_exact_and_voltage_table_exclude_nonexact_lines() -> None:
    lines = _lines(
        [
            LineString([(20, -20), (20, 30)]),
            LineString([(110, -20), (110, 30)]),
            LineString([(210, -20), (210, 30)]),
        ],
        identifiers=["BELOW", "EXACT-110", "EXACT-275"],
        voltage_statuses=["BELOW", "EXACT", "EXACT"],
        voltages=[None, 110.0, 275.0],
    )

    result = enrich_parcel_grid_proximity(_parcels(), lines, _posts())

    row = result.parcels.iloc[0]
    assert row["nearest_line_grid_feature_id"] == "BELOW"
    assert row["nearest_exact_line_grid_feature_id"] == "EXACT-110"
    assert row["nearest_exact_line_voltage_kv"] == 110.0
    assert result.voltage_level_proximity["voltage_kv"].tolist() == [110.0, 275.0]
    assert len(result.voltage_level_proximity) == 2
    assert list(result.voltage_level_proximity.columns) == list(
        VOLTAGE_PROXIMITY_COLUMNS
    )


def test_voltage_table_is_exact_ordered_cartesian_product() -> None:
    result = _two_parcel_two_voltage_result()

    assert tuple(item.voltage_kv for item in result.voltage_level_coverage) == (
        110.0,
        275.0,
    )
    assert len(result.voltage_level_proximity) == 4
    assert not result.voltage_level_proximity.duplicated(
        ["parcel_id", "voltage_kv"]
    ).any()
    for voltage_kv in (110.0, 275.0):
        rows = result.voltage_level_proximity.loc[
            result.voltage_level_proximity["voltage_kv"] == voltage_kv
        ]
        assert rows["parcel_id"].tolist() == ["PARCEL-2", "PARCEL-1"]


def test_invalid_exact_voltage_values_are_not_used_as_exact() -> None:
    lines = _lines(
        [LineString([(20, -20), (20, 30)])] * 4,
        identifiers=["ZERO", "NEGATIVE", "INFINITE", "TEXT"],
        voltage_statuses=["EXACT"] * 4,
        voltages=[0.0, -1.0, float("inf"), "110"],
    )

    result = enrich_parcel_grid_proximity(_parcels(), lines, _posts())

    assert result.parcels["nearest_exact_line_proxy_distance_m"].isna().all()
    assert result.voltage_level_proximity.empty


def test_no_exact_voltage_preserves_parcels_and_returns_empty_long_table() -> None:
    lines = _lines(voltage_statuses=["UNKNOWN"], voltages=[None])

    result = enrich_parcel_grid_proximity(_parcels(), lines, _posts())

    assert result.parcels.loc[0, "nearest_line_grid_feature_id"] == "LINE-1"
    assert result.parcels["nearest_exact_line_proxy_distance_m"].isna().all()
    assert result.parcels["nearest_exact_line_grid_feature_id"].isna().all()
    assert result.voltage_level_proximity.empty
    assert list(result.voltage_level_proximity.columns) == list(
        VOLTAGE_PROXIMITY_COLUMNS
    )
    assert is_float_dtype(
        result.parcels["nearest_exact_line_proxy_distance_m"].dtype
    )
    assert is_float_dtype(result.parcels["nearest_exact_line_voltage_kv"].dtype)
    assert is_integer_dtype(result.parcels["nearest_exact_line_tie_count"].dtype)
    assert str(result.parcels["nearest_exact_line_tie_count"].dtype) == "Int64"
    assert is_float_dtype(result.voltage_level_proximity["voltage_kv"].dtype)
    assert is_float_dtype(
        result.voltage_level_proximity["nearest_line_proxy_distance_m"].dtype
    )
    assert str(result.voltage_level_proximity["tie_count"].dtype) == "Int64"
    assert result.voltage_level_coverage == ()
    profile = profile_grid_proximity(result)
    assert profile.nearest_exact_line.count == 0
    assert profile.nearest_exact_line.missing_count == 1


@pytest.mark.parametrize("column", ["parcel_id", "geometry"])
def test_missing_parcel_column_is_rejected(column: str) -> None:
    parcels = _parcels().drop(columns=column)

    with pytest.raises(GridProximityError, match=column):
        enrich_parcel_grid_proximity(parcels, _lines(), _posts())


def test_null_parcel_id_is_rejected() -> None:
    with pytest.raises(GridProximityError, match="parcel_id"):
        enrich_parcel_grid_proximity(
            _parcels(identifiers=[None]), _lines(), _posts()
        )


def test_duplicate_parcel_id_is_rejected() -> None:
    parcels = _parcels(
        [
            Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]),
            Polygon([(20, 0), (20, 10), (30, 10), (30, 0), (20, 0)]),
        ],
        identifiers=["DUPLICATE", "DUPLICATE"],
    )

    with pytest.raises(GridProximityError, match="unique"):
        enrich_parcel_grid_proximity(parcels, _lines(), _posts())


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
def test_bad_parcel_geometry_is_rejected(geometry: object, message: str) -> None:
    with pytest.raises(GridProximityError, match=message):
        enrich_parcel_grid_proximity(
            _parcels([geometry]), _lines(), _posts()
        )


def test_inputs_are_not_mutated_and_parcel_order_and_ids_are_preserved() -> None:
    parcels = _parcels(
        [
            Polygon([(20, 0), (20, 10), (30, 10), (30, 0), (20, 0)]),
            Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]),
        ],
        identifiers=["SECOND-SPATIAL", "FIRST-SPATIAL"],
        index=[99, 99],
    )
    lines = _lines()
    posts = _posts()
    parcels_before = deepcopy(parcels)
    lines_before = deepcopy(lines)
    posts_before = deepcopy(posts)

    result = enrich_parcel_grid_proximity(parcels, lines, posts)

    assert_geodataframe_equal(parcels, parcels_before)
    assert_geodataframe_equal(lines, lines_before)
    assert_geodataframe_equal(posts, posts_before)
    assert result.parcels["parcel_id"].tolist() == [
        "SECOND-SPATIAL",
        "FIRST-SPATIAL",
    ]
    assert isinstance(result.parcels.index, pd.RangeIndex)


def test_distance_profile_is_threshold_free_and_tracks_ties() -> None:
    parcels = _parcels(
        [
            Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]),
            Polygon([(50, 0), (50, 10), (60, 10), (60, 0), (50, 0)]),
        ]
    )
    lines = _lines(
        [
            LineString([(-100, -20), (-100, 30)]),
            LineString([(110, -20), (110, 30)]),
        ],
        identifiers=["Z-LINE", "A-LINE"],
    )
    result = enrich_parcel_grid_proximity(parcels, lines, _posts())

    profile = profile_grid_proximity(result)

    assert profile.parcel_count == 2
    assert profile.nearest_line.count == 2
    assert profile.nearest_line.missing_count == 0
    assert profile.nearest_line.minimum == pytest.approx(50.0)
    assert profile.nearest_line.p50 == pytest.approx(75.0)
    assert profile.nearest_line.maximum == pytest.approx(100.0)
    assert profile.nearest_line.tie_count == 1
    assert profile.voltage_levels[0].voltage_kv == 110.0
    assert profile.voltage_levels[0].line_feature_count == 2
    assert profile.voltage_levels[0].parcel_proximity_count == 2


def test_profile_rejects_missing_voltage_cartesian_row() -> None:
    result = _two_parcel_two_voltage_result()
    table = result.voltage_level_proximity.iloc[:-1].copy()

    with pytest.raises(GridProximityError):
        profile_grid_proximity(replace(result, voltage_level_proximity=table))


def test_profile_rejects_unknown_voltage_parcel_with_same_total_count() -> None:
    result = _two_parcel_two_voltage_result()
    corrupted = _mutate_voltage_result(result, "parcel_id", "UNKNOWN-PARCEL")

    with pytest.raises(GridProximityError):
        profile_grid_proximity(corrupted)


def test_profile_rejects_duplicate_parcel_voltage_pair() -> None:
    result = _two_parcel_two_voltage_result()
    table = result.voltage_level_proximity.copy()
    table.at[1, "parcel_id"] = table.at[0, "parcel_id"]

    with pytest.raises(GridProximityError, match="unique"):
        profile_grid_proximity(replace(result, voltage_level_proximity=table))


def test_profile_rejects_voltage_rows_out_of_parcel_order() -> None:
    result = _two_parcel_two_voltage_result()
    table = result.voltage_level_proximity.iloc[[1, 0, 2, 3]].reset_index(drop=True)

    with pytest.raises(GridProximityError, match="exact parcel set"):
        profile_grid_proximity(replace(result, voltage_level_proximity=table))


@pytest.mark.parametrize(
    "value",
    [
        0,
        -1,
        1.5,
        float("inf"),
        "2",
        None,
        pytest.param(OVERFLOWING_INTEGER, id="overflowing-integer"),
    ],
)
@pytest.mark.parametrize(
    "column",
    [
        "nearest_line_tie_count",
        "nearest_exact_line_tie_count",
        "nearest_post_tie_count",
    ],
)
def test_profile_rejects_bad_required_match_tie_count(
    column: str, value: object
) -> None:
    result = _two_parcel_two_voltage_result()

    with pytest.raises(GridProximityError, match="tie_count|match"):
        profile_grid_proximity(_mutate_parcel_result(result, column, value))


@pytest.mark.parametrize(
    "value",
    [
        0,
        -1,
        1.5,
        float("inf"),
        "2",
        None,
        pytest.param(OVERFLOWING_INTEGER, id="overflowing-integer"),
    ],
)
def test_profile_rejects_bad_long_table_tie_count(value: object) -> None:
    result = _two_parcel_two_voltage_result()

    with pytest.raises(GridProximityError, match="tie_count|match"):
        profile_grid_proximity(_mutate_voltage_result(result, "tie_count", value))


@pytest.mark.parametrize(
    "column",
    [
        "nearest_line_grid_feature_id",
        "nearest_line_source_feature_id",
        "nearest_exact_line_grid_feature_id",
        "nearest_exact_line_source_feature_id",
        "nearest_post_grid_feature_id",
        "nearest_post_source_feature_id",
    ],
)
def test_profile_rejects_missing_main_match_feature_id(column: str) -> None:
    result = _two_parcel_two_voltage_result()

    with pytest.raises(GridProximityError, match="require"):
        profile_grid_proximity(_mutate_parcel_result(result, column, None))


@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("nearest_line_proxy_distance_m", None),
        ("nearest_line_proxy_distance_m", "100"),
        ("nearest_exact_line_proxy_distance_m", float("inf")),
        ("nearest_post_proxy_distance_m", -1),
    ],
)
def test_profile_rejects_bad_required_match_distance(
    column: str, value: object
) -> None:
    result = _two_parcel_two_voltage_result()

    with pytest.raises(GridProximityError):
        profile_grid_proximity(_mutate_parcel_result(result, column, value))


@pytest.mark.parametrize(
    "value",
    [None, 0, -1, float("inf"), "110", 999.0],
)
def test_profile_rejects_bad_exact_match_voltage(value: object) -> None:
    result = _two_parcel_two_voltage_result()

    with pytest.raises(GridProximityError, match="voltage|match"):
        profile_grid_proximity(
            _mutate_parcel_result(result, "nearest_exact_line_voltage_kv", value)
        )


def test_profile_rejects_bad_result_parcel_id() -> None:
    result = _two_parcel_two_voltage_result()

    with pytest.raises(GridProximityError, match="parcel_id"):
        profile_grid_proximity(_mutate_parcel_result(result, "parcel_id", " BAD "))


def test_profile_rejects_missing_required_proximity_column() -> None:
    result = _two_parcel_two_voltage_result()
    parcels = result.parcels.drop(columns="nearest_line_grid_feature_id")

    with pytest.raises(GridProximityError, match="Missing proximity"):
        profile_grid_proximity(replace(result, parcels=parcels))


@pytest.mark.parametrize("mutation", ["reversed", "duplicate"])
def test_profile_rejects_nondeterministic_or_duplicate_coverage(
    mutation: str,
) -> None:
    result = _two_parcel_two_voltage_result()
    if mutation == "reversed":
        coverage = tuple(reversed(result.voltage_level_coverage))
    else:
        coverage = (*result.voltage_level_coverage, result.voltage_level_coverage[0])

    with pytest.raises(GridProximityError, match="coverage"):
        profile_grid_proximity(replace(result, voltage_level_coverage=coverage))


@pytest.mark.parametrize(
    "voltage_kv",
    [
        0,
        -1,
        float("inf"),
        "110",
        pytest.param(OVERFLOWING_INTEGER, id="overflowing-integer"),
    ],
)
def test_profile_rejects_invalid_voltage_coverage_level(voltage_kv: object) -> None:
    result = _two_parcel_two_voltage_result()
    coverage = (
        VoltageLevelCoverage(voltage_kv=voltage_kv, line_feature_count=1),
    )

    with pytest.raises(GridProximityError, match="coverage"):
        profile_grid_proximity(replace(result, voltage_level_coverage=coverage))


@pytest.mark.parametrize(
    "feature_count", [0, -1, 1.5, float("inf"), True, "2"]
)
def test_profile_rejects_invalid_voltage_coverage_feature_count(
    feature_count: object,
) -> None:
    result = _two_parcel_two_voltage_result()
    coverage = (
        VoltageLevelCoverage(voltage_kv=110.0, line_feature_count=feature_count),
    )

    with pytest.raises(GridProximityError, match="line_feature_count"):
        profile_grid_proximity(replace(result, voltage_level_coverage=coverage))


@pytest.mark.parametrize(
    "value",
    [None, 0, -1, float("inf"), "110", 220.0],
)
def test_profile_rejects_invalid_long_table_voltage(value: object) -> None:
    result = _two_parcel_two_voltage_result()

    with pytest.raises(GridProximityError, match="Voltage proximity"):
        profile_grid_proximity(_mutate_voltage_result(result, "voltage_kv", value))


@pytest.mark.parametrize(
    "column",
    [
        "nearest_line_grid_feature_id",
        "nearest_line_source_feature_id",
        "source_department_code",
        "source_edition",
        "source_archive_sha256",
    ],
)
def test_profile_rejects_missing_long_table_match_lineage(column: str) -> None:
    result = _two_parcel_two_voltage_result()

    with pytest.raises(GridProximityError, match="require"):
        profile_grid_proximity(_mutate_voltage_result(result, column, None))


@pytest.mark.parametrize(
    "value",
    [
        None,
        -1,
        float("inf"),
        "100",
        pytest.param(OVERFLOWING_INTEGER, id="overflowing-integer"),
    ],
)
def test_profile_rejects_bad_long_table_distance(value: object) -> None:
    result = _two_parcel_two_voltage_result()

    with pytest.raises(GridProximityError):
        profile_grid_proximity(
            _mutate_voltage_result(
                result, "nearest_line_proxy_distance_m", value
            )
        )


def test_profile_allows_missing_long_table_manager_name() -> None:
    result = _two_parcel_two_voltage_result()
    mutated = _mutate_voltage_result(result, "manager_name", None)

    profile = profile_grid_proximity(mutated)

    assert profile.parcel_count == 2


@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("nearest_exact_line_proxy_distance_m", 1.0),
        ("nearest_exact_line_grid_feature_id", "LINE"),
        ("nearest_exact_line_source_feature_id", "SOURCE"),
        ("nearest_exact_line_tie_count", 1),
        ("nearest_exact_line_voltage_kv", 110.0),
    ],
)
def test_profile_rejects_nonnull_exact_field_without_exact_coverage(
    column: str, value: object
) -> None:
    result = enrich_parcel_grid_proximity(
        _parcels(),
        _lines(voltage_statuses=["UNKNOWN"], voltages=[None]),
        _posts(),
    )

    with pytest.raises(GridProximityError, match="unmatched|entirely"):
        profile_grid_proximity(_mutate_parcel_result(result, column, value))


@pytest.mark.parametrize("kind", ["line", "post"])
def test_no_valid_required_grid_feature_is_rejected(kind: str) -> None:
    lines = _lines([None]) if kind == "line" else _lines()
    posts = _posts([None]) if kind == "post" else _posts()

    with pytest.raises(GridProximityError, match="No VALID"):
        enrich_parcel_grid_proximity(_parcels(), lines, posts)

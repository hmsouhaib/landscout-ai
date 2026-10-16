"""Intrinsic in-memory dimension contract; no claim about external M readers."""

import geopandas as gpd
import pytest
from shapely import from_wkt, get_coordinate_dimension

from landscout.common.cadastre_contract import validate_normalized_cadastre_parcels


def _frame(geometry: object) -> gpd.GeoDataFrame:
    xy = from_wkt("POLYGON ((1 43, 1.001 43, 1.001 43.001, 1 43.001, 1 43))")
    valid = geometry is not None and not geometry.is_empty and geometry.is_valid
    area = gpd.GeoSeries([xy], crs=4326).to_crs(2154).area.iloc[0]
    return gpd.GeoDataFrame(
        {
            "parcel_id": ["31395000AA0001"],
            "commune_code": ["31395"],
            "section_prefix": ["000"],
            "section": ["AA"],
            "parcel_number": ["1"],
            "source_contenance": [None],
            "source_arpente": [None],
            "source_created_at": [None],
            "source_updated_at": [None],
            "geometry_status": ["VALID" if valid else "INVALID"],
            "area_m2": [area if valid else float("nan")],
        },
        geometry=[geometry],
        crs=4326,
    )


def _polygon(dimension: str, family: str):
    suffix = {"XY": "", "Z": " 7", "M": " 8", "ZM": " 7 8"}[dimension]
    ring = ", ".join(
        x + suffix for x in ("1 43", "1.001 43", "1.001 43.001", "1 43.001", "1 43")
    )
    marker = "" if dimension == "XY" else " " + dimension
    polygon = f"(({ring}))"
    return from_wkt(
        f"{family}{marker} {polygon if family == 'POLYGON' else '(' + polygon + ')'}"
    )


@pytest.mark.parametrize("family", ["POLYGON", "MULTIPOLYGON"])
def test_xy_is_accepted_without_changing_geometry_or_area(family: str) -> None:
    frame = _frame(_polygon("XY", family))
    before = frame.copy(deep=True)
    assert validate_normalized_cadastre_parcels(frame) is frame
    assert frame.geometry.to_wkb().tolist() == before.geometry.to_wkb().tolist()
    assert frame["area_m2"].equals(before["area_m2"])


@pytest.mark.parametrize("family", ["POLYGON", "MULTIPOLYGON"])
@pytest.mark.parametrize("dimension", ["Z", "M", "ZM"])
def test_non_xy_polygon_dimensions_fail_immediately(
    family: str, dimension: str
) -> None:
    geometry = _polygon(dimension, family)
    assert get_coordinate_dimension(geometry) == (4 if dimension == "ZM" else 3)
    assert bool(geometry.has_m) is (dimension in ("M", "ZM"))
    assert bool(geometry.has_z) is (dimension in ("Z", "ZM"))
    frame = _frame(geometry)
    assert frame.geometry.iloc[0].wkb == geometry.wkb
    assert get_coordinate_dimension(frame.geometry.iloc[0]) == get_coordinate_dimension(
        geometry
    )
    before = frame.geometry.to_wkb().tolist()
    with pytest.raises(ValueError, match="exactly 2D"):
        validate_normalized_cadastre_parcels(frame)
    assert frame.geometry.to_wkb().tolist() == before


@pytest.mark.parametrize(
    "wkt",
    [
        None,
        "POLYGON EMPTY",
        "MULTIPOLYGON EMPTY",
        "POLYGON ((1 43, 1.001 43.001, 1.001 43, 1 43.001, 1 43))",
    ],
)
def test_null_empty_and_invalid_xy_are_preserved(wkt: str | None) -> None:
    frame = _frame(from_wkt(wkt) if wkt is not None else None)
    before = frame.geometry.to_wkb().tolist()
    assert frame.geometry_status.tolist() == ["INVALID"]
    assert validate_normalized_cadastre_parcels(frame) is frame
    assert frame.geometry.to_wkb().tolist() == before
    assert frame.area_m2.isna().all()

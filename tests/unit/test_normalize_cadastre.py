import geopandas as gpd
import pytest
from shapely.geometry import Polygon

from landscout.stages.normalize_cadastre import (
    CadastreNormalizationError,
    normalize_cadastre_parcels,
)


def _source_parcels(
    geometries: list[Polygon], ids: list[str] | None = None, crs: str | None = "EPSG:4326"
) -> gpd.GeoDataFrame:
    parcel_ids = ids or [f"parcel-{index}" for index in range(len(geometries))]
    count = len(geometries)
    return gpd.GeoDataFrame(
        {
            "id": parcel_ids,
            "commune": ["31395"] * count,
            "prefixe": ["000"] * count,
            "section": ["A"] * count,
            "numero": [str(index + 1) for index in range(count)],
            "contenance": [1000.0] * count,
            "arpente": [False] * count,
            "created": ["2020-01-01"] * count,
            "updated": ["2024-01-01"] * count,
        },
        geometry=geometries,
        crs=crs,
    )


@pytest.fixture
def valid_polygon() -> Polygon:
    return Polygon(
        [(2.35, 43.45), (2.36, 43.45), (2.36, 43.46), (2.35, 43.45)]
    )


def test_field_normalization(valid_polygon: Polygon) -> None:
    normalized = normalize_cadastre_parcels(_source_parcels([valid_polygon]))

    assert list(normalized.columns) == [
        "parcel_id",
        "commune_code",
        "section_prefix",
        "section",
        "parcel_number",
        "source_contenance",
        "source_arpente",
        "source_created_at",
        "source_updated_at",
        "geometry_status",
        "area_m2",
        "geometry",
    ]
    assert normalized.iloc[0]["parcel_id"] == "parcel-0"
    assert normalized.iloc[0]["commune_code"] == "31395"
    assert normalized.iloc[0]["geometry_status"] == "VALID"


def test_lambert93_area_calculation(valid_polygon: Polygon) -> None:
    source = _source_parcels([valid_polygon])
    expected_area = source.to_crs("EPSG:2154").geometry.area.iloc[0]

    normalized = normalize_cadastre_parcels(source)

    assert normalized.iloc[0]["area_m2"] == pytest.approx(expected_area)
    assert normalized.iloc[0]["area_m2"] > 0


def test_output_geometry_stays_in_wgs84(valid_polygon: Polygon) -> None:
    source = _source_parcels([valid_polygon])

    normalized = normalize_cadastre_parcels(source)

    assert normalized.crs is not None
    assert normalized.crs.to_epsg() == 4326
    assert normalized.geometry.iloc[0].equals_exact(valid_polygon, tolerance=0)


def test_invalid_geometry_is_preserved_with_null_area() -> None:
    bow_tie = Polygon(
        [(2.35, 43.45), (2.36, 43.46), (2.35, 43.46), (2.36, 43.45)]
    )
    assert not bow_tie.is_valid

    normalized = normalize_cadastre_parcels(_source_parcels([bow_tie]))

    assert normalized.iloc[0]["geometry_status"] == "INVALID"
    assert normalized["area_m2"].isna().iloc[0]
    assert normalized.geometry.iloc[0].equals_exact(bow_tie, tolerance=0)


def test_missing_crs_fails(valid_polygon: Polygon) -> None:
    source = _source_parcels([valid_polygon], crs=None)

    with pytest.raises(CadastreNormalizationError, match="CRS"):
        normalize_cadastre_parcels(source)


def test_duplicate_parcel_id_fails(valid_polygon: Polygon) -> None:
    source = _source_parcels(
        [valid_polygon, valid_polygon], ids=["duplicate", "duplicate"]
    )

    with pytest.raises(CadastreNormalizationError, match="unique"):
        normalize_cadastre_parcels(source)

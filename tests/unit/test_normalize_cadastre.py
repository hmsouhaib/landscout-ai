from copy import deepcopy
from pathlib import Path

import geopandas as gpd
import pandas as pd
import pytest
from geopandas.testing import assert_geodataframe_equal
from shapely.geometry import LineString, MultiPolygon, Point, Polygon

from landscout.sources.cadastre_fr import CadastreDownload
from landscout.sources.cadastre_loader_fr import CadastreParcelSource
from landscout.stages.normalize_cadastre import (
    CadastreNormalizationError,
    normalize_cadastre_parcels,
)


@pytest.fixture(autouse=True)
def _physical_revalidation_stub(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        "landscout.stages.normalize_cadastre.revalidate_cadastre_parcel_source",
        lambda source: source.parcels.copy(deep=True),
    )


def _bound_source(parcels: object) -> CadastreParcelSource:
    commune = "31395"
    if isinstance(parcels, gpd.GeoDataFrame) and "commune" in parcels.columns:
        first = parcels["commune"].iloc[0]
        if isinstance(first, str):
            commune = first
    download = CadastreDownload(
        commune_code=commune,
        source_url="https://cadastre.data.gouv.fr/unused",
        download_timestamp="2026-08-16T10:00:00+00:00",
        filename="unused.json.gz",
        file_size=1,
        sha256="0" * 64,
        path=Path("unused.json.gz"),
        cache_hit=True,
    )
    return CadastreParcelSource(
        download=download,
        parcels=parcels,  # type: ignore[arg-type]
    )


def _normalize(parcels: object) -> gpd.GeoDataFrame:
    return normalize_cadastre_parcels(_bound_source(parcels))


def _source_parcels(
    geometries: list[object],
    ids: list[object] | None = None,
    crs: str | None = "EPSG:4326",
) -> gpd.GeoDataFrame:
    parcel_ids = ids or [
        f"313950000A{index + 1:04d}" for index in range(len(geometries))
    ]
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
    return Polygon([(2.35, 43.45), (2.36, 43.45), (2.36, 43.46), (2.35, 43.45)])


def test_field_normalization(valid_polygon: Polygon) -> None:
    normalized = _normalize(_source_parcels([valid_polygon]))

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
    assert normalized.iloc[0]["parcel_id"] == "313950000A0001"
    assert normalized.iloc[0]["commune_code"] == "31395"
    assert normalized.iloc[0]["geometry_status"] == "VALID"


def test_lambert93_area_calculation(valid_polygon: Polygon) -> None:
    source = _source_parcels([valid_polygon])
    expected_area = source.to_crs("EPSG:2154").geometry.area.iloc[0]

    normalized = _normalize(source)

    assert normalized.iloc[0]["area_m2"] == pytest.approx(expected_area)
    assert normalized.iloc[0]["area_m2"] > 0


def test_output_geometry_stays_in_wgs84(valid_polygon: Polygon) -> None:
    source = _source_parcels([valid_polygon])

    normalized = _normalize(source)

    assert normalized.crs is not None
    assert normalized.crs.to_epsg() == 4326
    assert normalized.geometry.iloc[0].equals_exact(valid_polygon, tolerance=0)


def test_invalid_geometry_is_preserved_with_null_area() -> None:
    bow_tie = Polygon([(2.35, 43.45), (2.36, 43.46), (2.35, 43.46), (2.36, 43.45)])
    assert not bow_tie.is_valid

    normalized = _normalize(_source_parcels([bow_tie]))

    assert normalized.iloc[0]["geometry_status"] == "INVALID"
    assert normalized["area_m2"].isna().iloc[0]
    assert normalized.geometry.iloc[0].equals_exact(bow_tie, tolerance=0)


def test_missing_crs_fails(valid_polygon: Polygon) -> None:
    source = _source_parcels([valid_polygon], crs=None)

    with pytest.raises(CadastreNormalizationError, match="CRS"):
        _normalize(source)


def test_duplicate_parcel_id_fails(valid_polygon: Polygon) -> None:
    source = _source_parcels(
        [valid_polygon, valid_polygon], ids=["duplicate", "duplicate"]
    )

    with pytest.raises(CadastreNormalizationError, match="unique"):
        _normalize(source)


def test_non_geodataframe_is_rejected_safely() -> None:
    with pytest.raises(CadastreNormalizationError, match="GeoDataFrame"):
        _normalize(pd.DataFrame({"id": ["parcel"]}))  # type: ignore[arg-type]


def test_duplicate_columns_are_rejected(valid_polygon: Polygon) -> None:
    source = _source_parcels([valid_polygon])
    duplicate = gpd.GeoDataFrame(
        pd.concat([source, source[["id"]]], axis=1),
        geometry="geometry",
        crs=source.crs,
    )

    with pytest.raises(CadastreNormalizationError, match="columns.*unique"):
        _normalize(duplicate)


@pytest.mark.parametrize(
    "collision",
    [
        "parcel_id",
        "commune_code",
        "section_prefix",
        "parcel_number",
        "geometry_status",
        "area_m2",
    ],
)
def test_normalized_target_column_collision_is_rejected(
    valid_polygon: Polygon,
    collision: str,
) -> None:
    source = _source_parcels([valid_polygon])
    source[collision] = "forged"

    with pytest.raises(CadastreNormalizationError, match="collide"):
        _normalize(source)


def test_projected_source_crs_is_rejected(valid_polygon: Polygon) -> None:
    source = _source_parcels([valid_polygon]).to_crs("EPSG:2154")

    with pytest.raises(CadastreNormalizationError, match="4326"):
        _normalize(source)


@pytest.mark.parametrize("identifier", [1, "", " ", " parcel", "parcel "])
def test_parcel_id_must_be_an_exact_nonempty_string(
    valid_polygon: Polygon,
    identifier: object,
) -> None:
    source = _source_parcels([valid_polygon], ids=[identifier])

    with pytest.raises(CadastreNormalizationError, match="parcel_id"):
        _normalize(source)


@pytest.mark.parametrize(
    "geometry",
    [Point(2.35, 43.45), LineString([(2.35, 43.45), (2.36, 43.46)])],
)
def test_non_polygonal_geometry_is_rejected(geometry: object) -> None:
    with pytest.raises(CadastreNormalizationError, match="Polygon"):
        _normalize(_source_parcels([geometry]))


def test_valid_multipolygon_is_accepted(valid_polygon: Polygon) -> None:
    normalized = _normalize(_source_parcels([MultiPolygon([valid_polygon])]))

    assert normalized.loc[0, "geometry_status"] == "VALID"
    assert normalized.loc[0, "area_m2"] > 0


@pytest.mark.parametrize("geometry", [None, Polygon()])
def test_null_and_empty_geometry_are_preserved_as_invalid(geometry: object) -> None:
    normalized = _normalize(_source_parcels([geometry]))

    assert normalized.loc[0, "geometry_status"] == "INVALID"
    assert pd.isna(normalized.loc[0, "area_m2"])
    if geometry is None:
        assert normalized.geometry.isna().iloc[0]
    else:
        assert normalized.geometry.is_empty.iloc[0]


def test_normalization_does_not_mutate_input(valid_polygon: Polygon) -> None:
    source = _source_parcels([valid_polygon])
    before = deepcopy(source)

    _normalize(source)

    assert_geodataframe_equal(source, before)


def test_normalization_uses_the_fresh_revalidated_frame(
    valid_polygon: Polygon,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    supplied = _source_parcels([valid_polygon])
    fresh = supplied.copy(deep=True)
    source = _bound_source(supplied)

    def return_fresh_and_mutate_supplied(_: object) -> gpd.GeoDataFrame:
        supplied.loc[0, "id"] = "FORGED-AFTER-COMPARISON"
        return fresh

    monkeypatch.setattr(
        "landscout.stages.normalize_cadastre.revalidate_cadastre_parcel_source",
        return_fresh_and_mutate_supplied,
    )

    normalized = normalize_cadastre_parcels(source)

    assert normalized.loc[0, "parcel_id"] == "313950000A0001"
    assert supplied.loc[0, "id"] == "FORGED-AFTER-COMPARISON"


@pytest.mark.parametrize("column", ["id", "commune", "prefixe", "section", "numero"])
@pytest.mark.parametrize(
    "value",
    [None, 123, True, "", " leading", "trailing "],
)
def test_every_cadastral_identity_field_requires_an_exact_nonempty_string(
    valid_polygon: Polygon,
    column: str,
    value: object,
) -> None:
    source = _source_parcels([valid_polygon])
    source[column] = source[column].astype(object)
    source.loc[0, column] = value

    with pytest.raises(CadastreNormalizationError, match=column):
        _normalize(source)


@pytest.mark.parametrize("commune", ["3139", "2a004", "ABCDE", "971000"])
def test_commune_requires_canonical_french_insee_identity(
    valid_polygon: Polygon,
    commune: str,
) -> None:
    source = _source_parcels([valid_polygon])
    source.loc[0, "commune"] = commune
    source.loc[0, "id"] = f"{commune}0000A0001"

    with pytest.raises(CadastreNormalizationError, match="commune"):
        _normalize(source)


@pytest.mark.parametrize("commune", ["31395", "2A004", "2B033"])
def test_commune_accepts_canonical_french_insee_identity(
    valid_polygon: Polygon,
    commune: str,
) -> None:
    source = _source_parcels([valid_polygon])
    source.loc[0, "commune"] = commune
    source.loc[0, "id"] = f"{commune}0000A0001"

    result = _normalize(source)

    assert result.loc[0, "commune_code"] == commune

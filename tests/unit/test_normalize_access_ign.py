from __future__ import annotations

from copy import deepcopy
from dataclasses import replace
from pathlib import Path
from typing import Any, cast

import geopandas as gpd
import pandas as pd
import pytest
from geopandas.testing import assert_geodataframe_equal
from shapely.geometry import LineString, MultiLineString, Point, Polygon

from landscout import stages
from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
)
from landscout.stages.normalize_access_ign import (
    IgnRoadNormalizationError,
    NormalizedIgnRoadData,
    normalize_ign_roads,
)

ROAD_LAYER = "troncon_de_route"
ARCHIVE_SHA256 = "a" * 64
SOURCE_URL = "https://example.test/BDTOPO_D031.7z"

OUTPUT_COLUMNS = (
    "road_feature_id",
    "road_feature_type",
    "source_provider",
    "source_product",
    "source_layer",
    "source_feature_id",
    "source_department_code",
    "source_edition",
    "source_product_version",
    "source_download_timestamp",
    "source_archive_sha256",
    "source_url",
    "nature_raw",
    "importance_raw",
    "fictitious_raw",
    "position_relative_to_ground_raw",
    "asset_status_raw",
    "lane_count_raw",
    "carriageway_width_raw",
    "private_raw",
    "traffic_direction_raw",
    "urban_raw",
    "mean_light_vehicle_speed_raw",
    "light_vehicle_access_raw",
    "closure_period_raw",
    "restriction_nature_raw",
    "restriction_height_raw",
    "restriction_total_weight_raw",
    "restriction_axle_weight_raw",
    "restriction_width_raw",
    "restriction_length_raw",
    "dangerous_goods_forbidden_raw",
    "administrative_classification_raw",
    "manager_raw",
    "source_name_raw",
    "source_identifiers_raw",
    "source_created_at",
    "source_modified_at",
    "source_confirmed_at",
    "planimetric_acquisition_method",
    "planimetric_precision_raw",
    "spatial_role",
    "geometry_status",
    "geometry",
)
RAW_FIELD_MAPPING = (
    ("nature", "nature_raw"),
    ("importance", "importance_raw"),
    ("fictif", "fictitious_raw"),
    ("position_par_rapport_au_sol", "position_relative_to_ground_raw"),
    ("etat_de_l_objet", "asset_status_raw"),
    ("nombre_de_voies", "lane_count_raw"),
    ("largeur_de_chaussee", "carriageway_width_raw"),
    ("prive", "private_raw"),
    ("sens_de_circulation", "traffic_direction_raw"),
    ("urbain", "urban_raw"),
    ("vitesse_moyenne_vl", "mean_light_vehicle_speed_raw"),
    ("acces_vehicule_leger", "light_vehicle_access_raw"),
    ("periode_de_fermeture", "closure_period_raw"),
    ("nature_de_la_restriction", "restriction_nature_raw"),
    ("restriction_de_hauteur", "restriction_height_raw"),
    ("restriction_de_poids_total", "restriction_total_weight_raw"),
    ("restriction_de_poids_par_essieu", "restriction_axle_weight_raw"),
    ("restriction_de_largeur", "restriction_width_raw"),
    ("restriction_de_longueur", "restriction_length_raw"),
    ("matieres_dangereuses_interdites", "dangerous_goods_forbidden_raw"),
    ("cpx_classement_administratif", "administrative_classification_raw"),
    ("cpx_gestionnaire", "manager_raw"),
    ("sources", "source_name_raw"),
    ("identifiants_sources", "source_identifiers_raw"),
    ("date_creation", "source_created_at"),
    ("date_modification", "source_modified_at"),
    ("date_de_confirmation", "source_confirmed_at"),
    ("methode_d_acquisition_planimetrique", "planimetric_acquisition_method"),
    ("precision_planimetrique", "planimetric_precision_raw"),
)


def _road_frame(
    geometries: list[object] | None = None,
    *,
    identifiers: list[object] | None = None,
    crs: str | None = "EPSG:2154",
    index: list[object] | None = None,
) -> gpd.GeoDataFrame:
    source_geometries = geometries or [LineString([(0, 0), (100, 100)])]
    count = len(source_geometries)
    source_ids = identifiers or [f"ROAD-{number + 1}" for number in range(count)]
    source_index = index or [100 + number for number in range(count)]
    values: dict[str, list[object]] = {
        "cleabs": source_ids,
        "nature": ["Route à 1 chaussée"] * count,
        "importance": ["2"] * count,
        "fictif": ["Non"] * count,
        "position_par_rapport_au_sol": [-1] * count,
        "etat_de_l_objet": ["En service"] * count,
        "nombre_de_voies": [2] * count,
        "largeur_de_chaussee": [7.5] * count,
        "prive": ["Non"] * count,
        "sens_de_circulation": ["Double sens"] * count,
        "urbain": ["Non"] * count,
        "vitesse_moyenne_vl": [80] * count,
        "acces_vehicule_leger": ["Libre"] * count,
        "periode_de_fermeture": [None] * count,
        "nature_de_la_restriction": ["Poids total"] * count,
        "restriction_de_hauteur": [4.2] * count,
        "restriction_de_poids_total": [19.0] * count,
        "restriction_de_poids_par_essieu": [11.5] * count,
        "restriction_de_largeur": [3.2] * count,
        "restriction_de_longueur": [18.0] * count,
        "matieres_dangereuses_interdites": ["Oui"] * count,
        "cpx_classement_administratif": ["Départementale"] * count,
        "cpx_gestionnaire": ["CD31"] * count,
        "sources": ["IGN 2026"] * count,
        "identifiants_sources": ["source-road-id"] * count,
        "date_creation": [pd.Timestamp("2024-01-01", tz="UTC")] * count,
        "date_modification": [pd.Timestamp("2025-01-01", tz="UTC")] * count,
        "date_de_confirmation": [pd.Timestamp("2025-06-01", tz="UTC")] * count,
        "methode_d_acquisition_planimetrique": ["Photogrammétrie"] * count,
        "precision_planimetrique": [2.5] * count,
    }
    return gpd.GeoDataFrame(
        values,
        geometry=source_geometries,
        crs=crs,
        index=source_index,
    )


def _summary(
    frame: gpd.GeoDataFrame,
    *,
    layer: str = ROAD_LAYER,
) -> IgnBdTopoLayerSummary:
    geometry = frame.geometry
    null_mask = geometry.isna()
    empty_mask = ~null_mask & geometry.is_empty
    invalid_mask = ~null_mask & ~geometry.is_empty & ~geometry.is_valid
    return IgnBdTopoLayerSummary(
        logical_name="road_segments",
        source_layer_name=layer,
        crs=str(frame.crs),
        feature_count=len(frame),
        columns=tuple(str(column) for column in frame.columns),
        dtypes=tuple((str(column), str(dtype)) for column, dtype in frame.dtypes.items()),
        null_geometry_count=int(null_mask.sum()),
        empty_geometry_count=int(empty_mask.sum()),
        invalid_geometry_count=int(invalid_mask.sum()),
        geometry_types=tuple(
            sorted(
                str(value)
                for value in geometry[~null_mask].geom_type.dropna().unique()
            )
        ),
    )


def _source(frame: gpd.GeoDataFrame | None = None) -> IgnBdTopoRoadData:
    road_frame = frame if frame is not None else _road_frame()
    archive = IgnBdTopoDownload(
        provider="IGN",
        product="BD TOPO",
        department_code="31",
        edition="2026-06-15",
        product_version="3.5",
        projection="EPSG:2154",
        package_format="GPKG",
        archive_format="7z",
        source_url=SOURCE_URL,
        checksum_url=None,
        download_timestamp="2026-08-11T15:32:03+00:00",
        filename="BDTOPO_D031.7z",
        file_size=1234,
        sha256=ARCHIVE_SHA256,
        official_checksum_algorithm=None,
        official_checksum=None,
        official_checksum_validated=False,
        path=Path("cache/BDTOPO_D031.7z"),
        cache_hit=True,
    )
    extraction = IgnBdTopoExtraction(
        archive=archive,
        extraction_path=Path("cache/x/source"),
        geopackage_path=Path("cache/x/source/data.gpkg"),
        geopackage_filename="data.gpkg",
        all_layer_names=("other_layer", ROAD_LAYER),
        electric_lines_layer="ligne_electrique",
        transformation_posts_layer="poste_de_transformation",
        cache_hit=True,
    )
    return IgnBdTopoRoadData(
        extraction=extraction,
        road_segments=road_frame,
        road_segments_summary=_summary(road_frame),
    )


def test_public_api_exports_only_stable_road_normalization_symbols() -> None:
    import landscout.stages.normalize_access_ign as access_normalization

    expected = {
        "IgnRoadNormalizationError",
        "NormalizedIgnRoadData",
        "normalize_ign_roads",
    }
    assert set(access_normalization.__all__) == expected
    assert expected <= set(stages.__all__)
    assert all(hasattr(stages, name) for name in expected)
    assert not hasattr(stages, "_validate_road_source")


def test_valid_linestring_normalization_has_exact_schema_identity_and_lineage() -> None:
    normalized = normalize_ign_roads(_source())

    assert type(normalized) is NormalizedIgnRoadData
    roads = normalized.road_segments
    assert list(roads.columns) == list(OUTPUT_COLUMNS)
    assert isinstance(roads.index, pd.RangeIndex)
    assert roads.index.tolist() == [0]
    row = roads.iloc[0]
    assert row["road_feature_id"] == "IGN_BDTOPO:ROAD_SEGMENT:ROAD-1"
    assert row["road_feature_type"] == "ROAD_SEGMENT"
    assert row["source_feature_id"] == "ROAD-1"
    assert row["source_provider"] == "IGN"
    assert row["source_product"] == "BD_TOPO"
    assert row["source_layer"] == ROAD_LAYER
    assert row["source_department_code"] == "31"
    assert row["source_edition"] == "2026-06-15"
    assert row["source_product_version"] == "3.5"
    assert row["source_download_timestamp"] == "2026-08-11T15:32:03+00:00"
    assert row["source_archive_sha256"] == ARCHIVE_SHA256
    assert row["source_url"] == SOURCE_URL
    assert row["spatial_role"] == "PROXY_GEOMETRY"
    assert row["geometry_status"] == "VALID"
    assert roads.crs is not None and roads.crs.to_epsg() == 2154


def test_valid_multilinestring_is_preserved() -> None:
    geometry = MultiLineString(
        [[(0, 0), (10, 10)], [(20, 20), (30, 30)]]
    )

    roads = normalize_ign_roads(_source(_road_frame([geometry]))).road_segments

    assert roads.iloc[0]["geometry_status"] == "VALID"
    assert roads.geometry.iloc[0].equals_exact(geometry, tolerance=0)
    assert roads.geometry.iloc[0].geom_type == "MultiLineString"


def test_z_coordinates_are_preserved_exactly() -> None:
    geometry = LineString([(0, 0, 12), (10, 10, 24)])

    roads = normalize_ign_roads(_source(_road_frame([geometry]))).road_segments

    assert roads.geometry.iloc[0].has_z
    assert roads.geometry.iloc[0].wkb == geometry.wkb


def test_row_count_order_geometry_and_range_index_are_preserved() -> None:
    geometries = [
        LineString([(20, 0), (20, 10)]),
        LineString([(5, 0), (5, 10)]),
    ]
    source = _source(
        _road_frame(
            geometries,
            identifiers=["SECOND", "FIRST"],
            index=[91, 14],
        )
    )

    roads = normalize_ign_roads(source).road_segments

    assert len(roads) == 2
    assert roads["source_feature_id"].tolist() == ["SECOND", "FIRST"]
    assert roads["road_feature_id"].tolist() == [
        "IGN_BDTOPO:ROAD_SEGMENT:SECOND",
        "IGN_BDTOPO:ROAD_SEGMENT:FIRST",
    ]
    assert isinstance(roads.index, pd.RangeIndex)
    assert roads.geometry.to_wkb().tolist() == [value.wkb for value in geometries]


def test_raw_access_and_restriction_values_are_copied_without_interpretation() -> None:
    source = _road_frame()
    source.loc[source.index[0], "importance"] = "00"
    source.loc[source.index[0], "prive"] = "Valeur IGN non interprétée"
    source.loc[source.index[0], "acces_vehicule_leger"] = "Inconnu"
    source.loc[source.index[0], "restriction_de_poids_total"] = 19.75
    source.loc[source.index[0], "nature_de_la_restriction"] = None

    row = normalize_ign_roads(_source(source)).road_segments.iloc[0]

    assert row["importance_raw"] == "00"
    assert row["private_raw"] == "Valeur IGN non interprétée"
    assert row["light_vehicle_access_raw"] == "Inconnu"
    assert row["restriction_total_weight_raw"] == 19.75
    assert pd.isna(row["restriction_nature_raw"])


def test_every_raw_field_preserves_source_values_nulls_and_dtype() -> None:
    source = _source()

    roads = normalize_ign_roads(source).road_segments

    for source_column, output_column in RAW_FIELD_MAPPING:
        pd.testing.assert_series_equal(
            roads[output_column],
            source.road_segments[source_column].reset_index(drop=True),
            check_names=False,
            check_dtype=True,
        )


@pytest.mark.parametrize(
    "column",
    [
        "cleabs",
        "nature",
        "nombre_de_voies",
        "acces_vehicule_leger",
        "restriction_de_poids_total",
        "identifiants_sources",
        "geometry",
    ],
)
def test_missing_required_source_field_is_rejected(column: str) -> None:
    source = _source()
    frame = source.road_segments.drop(columns=column)
    mutated = replace(source, road_segments=frame)

    with pytest.raises(IgnRoadNormalizationError, match=column):
        normalize_ign_roads(mutated)


@pytest.mark.parametrize("identifier", [None, "", "   ", 123])
def test_null_or_empty_cleabs_is_rejected(identifier: object) -> None:
    with pytest.raises(IgnRoadNormalizationError, match="cleabs"):
        normalize_ign_roads(_source(_road_frame(identifiers=[identifier])))


@pytest.mark.parametrize(
    "identifier",
    [" leading", "trailing ", "ROAD:BAD", "ROAD\nBAD", "ROAD\tBAD"],
)
def test_unsafe_cleabs_is_rejected(identifier: str) -> None:
    with pytest.raises(IgnRoadNormalizationError, match="cleabs"):
        normalize_ign_roads(_source(_road_frame(identifiers=[identifier])))


def test_duplicate_cleabs_is_rejected() -> None:
    frame = _road_frame(
        [LineString([(0, 0), (1, 1)]), LineString([(2, 2), (3, 3)])],
        identifiers=["DUPLICATE", "DUPLICATE"],
    )

    with pytest.raises(IgnRoadNormalizationError, match="unique"):
        normalize_ign_roads(_source(frame))


@pytest.mark.parametrize("crs", [None, "EPSG:4326", "EPSG:3857"])
def test_wrong_or_missing_road_crs_is_rejected(crs: str | None) -> None:
    with pytest.raises(IgnRoadNormalizationError, match="CRS|2154"):
        normalize_ign_roads(_source(_road_frame(crs=crs)))


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("provider", "OTHER", "provider"),
        ("product", "OTHER", "product"),
        ("projection", "EPSG:4326", "2154"),
    ],
)
def test_wrong_archive_identity_is_rejected(
    field: str,
    value: str,
    message: str,
) -> None:
    source = _source()
    archive = replace(source.extraction.archive, **{field: value})
    mutated = replace(source, extraction=replace(source.extraction, archive=archive))

    with pytest.raises(IgnRoadNormalizationError, match=message):
        normalize_ign_roads(mutated)


@pytest.mark.parametrize("component", ["archive", "extraction", "summary"])
def test_wrong_source_spatial_role_is_rejected(component: str) -> None:
    source = _source()
    wrong_role = cast(Any, "AUTHORITATIVE_ACCESS")
    if component == "archive":
        archive = replace(source.extraction.archive, spatial_role=wrong_role)
        mutated = replace(
            source,
            extraction=replace(source.extraction, archive=archive),
        )
    elif component == "extraction":
        mutated = replace(
            source,
            extraction=replace(source.extraction, spatial_role=wrong_role),
        )
    else:
        mutated = replace(
            source,
            road_segments_summary=replace(
                source.road_segments_summary,
                spatial_role=wrong_role,
            ),
        )

    with pytest.raises(IgnRoadNormalizationError, match="PROXY_GEOMETRY"):
        normalize_ign_roads(mutated)


def test_summary_row_count_mismatch_is_rejected() -> None:
    source = _source()
    summary = replace(source.road_segments_summary, feature_count=2)

    with pytest.raises(IgnRoadNormalizationError, match="row count"):
        normalize_ign_roads(replace(source, road_segments_summary=summary))


def test_summary_crs_mismatch_is_rejected() -> None:
    source = _source()
    summary = replace(source.road_segments_summary, crs="EPSG:4326")

    with pytest.raises(IgnRoadNormalizationError, match="CRS|2154"):
        normalize_ign_roads(replace(source, road_segments_summary=summary))


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("null_geometry_count", 1),
        ("empty_geometry_count", 1),
        ("invalid_geometry_count", 1),
        ("geometry_types", ("MultiLineString",)),
    ],
)
def test_summary_geometry_facts_mismatch_is_rejected(
    field: str,
    value: object,
) -> None:
    source = _source()
    summary = replace(source.road_segments_summary, **{field: value})

    with pytest.raises(IgnRoadNormalizationError, match="geometry summary"):
        normalize_ign_roads(replace(source, road_segments_summary=summary))


def test_summary_layer_must_exist_in_extraction_inventory() -> None:
    source = _source()
    extraction = replace(source.extraction, all_layer_names=("other_layer",))

    with pytest.raises(IgnRoadNormalizationError, match="layer inventory"):
        normalize_ign_roads(replace(source, extraction=extraction))


def test_summary_layer_and_logical_name_must_be_exact() -> None:
    source = _source()
    wrong_layer = replace(source.road_segments_summary, source_layer_name="route")
    with pytest.raises(IgnRoadNormalizationError, match="physical layer"):
        normalize_ign_roads(replace(source, road_segments_summary=wrong_layer))

    wrong_logical = replace(
        source.road_segments_summary,
        logical_name=cast(Any, "electric_lines"),
    )
    with pytest.raises(IgnRoadNormalizationError, match="logical name"):
        normalize_ign_roads(replace(source, road_segments_summary=wrong_logical))


@pytest.mark.parametrize(
    "geometry",
    [Point(1, 1), Polygon([(0, 0), (0, 1), (1, 1), (1, 0), (0, 0)])],
)
def test_valid_unsupported_geometry_type_is_rejected(geometry: object) -> None:
    with pytest.raises(IgnRoadNormalizationError, match="geometry types"):
        normalize_ign_roads(_source(_road_frame([geometry])))


def test_null_empty_and_invalid_geometry_are_preserved_with_status() -> None:
    invalid = Polygon([(0, 0), (2, 2), (2, 0), (0, 2), (0, 0)])
    frame = _road_frame(
        [None, LineString(), invalid],
        identifiers=["NULL", "EMPTY", "INVALID"],
    )

    roads = normalize_ign_roads(_source(frame)).road_segments

    assert roads["geometry_status"].tolist() == ["NULL", "EMPTY", "INVALID"]
    assert roads.geometry.iloc[0] is None
    assert roads.geometry.iloc[1].is_empty
    assert roads.geometry.iloc[2].equals_exact(invalid, tolerance=0)


def test_normalization_does_not_mutate_input() -> None:
    source = _source()
    before = deepcopy(source.road_segments)

    normalize_ign_roads(source)

    assert_geodataframe_equal(source.road_segments, before)


def test_malformed_public_input_has_controlled_error() -> None:
    with pytest.raises(IgnRoadNormalizationError):
        normalize_ign_roads(cast(Any, object()))

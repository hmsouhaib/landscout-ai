from copy import deepcopy

import geopandas as gpd
import pandas as pd
import pytest
from geopandas.testing import assert_geodataframe_equal
from shapely.geometry import LineString, Polygon

from landscout.stages.normalize_grid_ign import (
    LINE_OUTPUT_COLUMNS,
    TRANSFORMATION_POST_OUTPUT_COLUMNS,
    IgnGridNormalizationError,
    normalize_ign_electric_lines,
    normalize_ign_transformation_posts,
    parse_ign_voltage,
)


def _line_source(
    geometries: list[object] | None = None,
    *,
    identifiers: list[object] | None = None,
    voltages: list[object] | None = None,
    crs: str | None = "EPSG:2154",
) -> gpd.GeoDataFrame:
    source_geometries = geometries or [LineString([(0, 0), (100, 100)])]
    count = len(source_geometries)
    source_ids = identifiers or [f"LIGNE-{index + 1}" for index in range(count)]
    source_voltages = voltages or ["225 kV"] * count
    return gpd.GeoDataFrame(
        {
            "cleabs": source_ids,
            "voltage": source_voltages,
            "gestionnaire": ["Réseau de Transport d'Électricité"] * count,
            "siren_gestionnaire": ["444619258"] * count,
            "etat_de_l_objet": ["En service"] * count,
            "sources": ["RTE 2024"] * count,
            "identifiants_sources": ["source-id"] * count,
            "date_creation": pd.to_datetime(["2024-01-01"] * count),
            "date_modification": pd.to_datetime(["2025-01-01"] * count),
            "date_de_confirmation": pd.to_datetime(["2024-12-18"] * count),
            "methode_d_acquisition_planimetrique": ["Photogrammétrie"]
            * count,
            "precision_planimetrique": [2.5] * count,
        },
        geometry=source_geometries,
        crs=crs,
        index=[100 + index for index in range(count)],
    )


def _post_source(
    geometries: list[object] | None = None,
    *,
    identifiers: list[object] | None = None,
    crs: str | None = "EPSG:2154",
) -> gpd.GeoDataFrame:
    source_geometries = geometries or [
        Polygon([(0, 0), (0, 20), (20, 20), (20, 0), (0, 0)])
    ]
    count = len(source_geometries)
    source_ids = identifiers or [f"POSTE-{index + 1}" for index in range(count)]
    return gpd.GeoDataFrame(
        {
            "cleabs": source_ids,
            "toponyme": ["Poste de test"] * count,
            "statut_du_toponyme": ["Validé"] * count,
            "importance": ["5"] * count,
            "etat_de_l_objet": ["En service"] * count,
            "sources": ["RTE 2021"] * count,
            "identifiants_sources": ["source-post-id"] * count,
            "date_creation": pd.to_datetime(["2023-01-01"] * count),
            "date_modification": pd.to_datetime(["2025-02-01"] * count),
            "date_de_confirmation": pd.to_datetime(["2025-01-15"] * count),
            "methode_d_acquisition_planimetrique": ["Orthophotographie"]
            * count,
            "precision_planimetrique": [5.0] * count,
        },
        geometry=source_geometries,
        crs=crs,
        index=[200 + index for index in range(count)],
    )


@pytest.mark.parametrize(
    ("raw", "expected_kv"),
    [
        ("63 kV", 63.0),
        ("150 kV", 150.0),
        ("225 kV", 225.0),
        ("400 kV", 400.0),
        ("110 kV", 110.0),
        ("  90 KV  ", 90.0),
        ("72,5 kv", 72.5),
    ],
)
def test_exact_voltage_parser_is_generic(raw: str, expected_kv: float) -> None:
    parsed = parse_ign_voltage(raw)

    assert parsed.raw == raw
    assert parsed.status == "EXACT"
    assert parsed.voltage_kv == expected_kv
    assert parsed.voltage_upper_bound_kv is None


@pytest.mark.parametrize(
    ("raw", "expected_upper_bound"),
    [("<63 kV", 63.0), ("<90 kV", 90.0), (" < 110 KV ", 110.0)],
)
def test_bounded_voltage_does_not_create_exact_value(
    raw: str, expected_upper_bound: float
) -> None:
    parsed = parse_ign_voltage(raw)

    assert parsed.raw == raw
    assert parsed.status == "BELOW"
    assert parsed.voltage_kv is None
    assert parsed.voltage_upper_bound_kv == expected_upper_bound


@pytest.mark.parametrize("raw", ["Inconnue", " INCONNUE ", "inconnu", None])
def test_unknown_voltage_parser(raw: str | None) -> None:
    parsed = parse_ign_voltage(raw)

    assert parsed.raw == raw
    assert parsed.status == "UNKNOWN"
    assert parsed.voltage_kv is None
    assert parsed.voltage_upper_bound_kv is None


@pytest.mark.parametrize("raw", ["Hors tension", " HORS TENSION "])
def test_deenergized_voltage_parser(raw: str) -> None:
    parsed = parse_ign_voltage(raw)

    assert parsed.raw == raw
    assert parsed.status == "DEENERGIZED"
    assert parsed.voltage_kv is None
    assert parsed.voltage_upper_bound_kv is None


def test_unexpected_voltage_vocabulary_is_explicitly_unparsed() -> None:
    parsed = parse_ign_voltage("Très haute tension future")

    assert parsed.raw == "Très haute tension future"
    assert parsed.status == "UNPARSED"
    assert parsed.voltage_kv is None
    assert parsed.voltage_upper_bound_kv is None


@pytest.mark.parametrize("raw", ["0 kV", "<0 kV", "-63 kV", "63 V"])
def test_invalid_numeric_voltage_is_unparsed(raw: str) -> None:
    assert parse_ign_voltage(raw).status == "UNPARSED"


def test_valid_line_is_normalized_with_stable_identity_and_lineage() -> None:
    source = _line_source()

    normalized = normalize_ign_electric_lines(source)

    row = normalized.iloc[0]
    assert list(normalized.columns) == list(LINE_OUTPUT_COLUMNS)
    assert row["grid_feature_id"] == "IGN_BDTOPO:ELECTRIC_LINE:LIGNE-1"
    assert row["grid_feature_type"] == "ELECTRIC_LINE"
    assert row["source_provider"] == "IGN"
    assert row["source_product"] == "BD_TOPO"
    assert row["source_layer"] == "ligne_electrique"
    assert row["source_feature_id"] == "LIGNE-1"
    assert row["voltage_status"] == "EXACT"
    assert row["voltage_kv"] == 225.0
    assert row["manager_name"] == "Réseau de Transport d'Électricité"
    assert row["manager_siren"] == "444619258"
    assert row["asset_status_raw"] == "En service"
    assert row["source_name_raw"] == "RTE 2024"
    assert row["source_identifiers_raw"] == "source-id"
    assert row["planimetric_acquisition_method"] == "Photogrammétrie"
    assert row["planimetric_precision_m"] == 2.5
    assert row["spatial_role"] == "PROXY_GEOMETRY"
    assert row["geometry_status"] == "VALID"
    assert normalized.index.tolist() == [100]


def test_deenergized_voltage_does_not_override_source_asset_status() -> None:
    source = _line_source(voltages=["Hors tension"])

    normalized = normalize_ign_electric_lines(source)

    assert normalized.iloc[0]["voltage_status"] == "DEENERGIZED"
    assert normalized.iloc[0]["asset_status_raw"] == "En service"


@pytest.mark.parametrize("identifier", [None, "", "   "])
def test_null_or_empty_line_cleabs_fails(identifier: object) -> None:
    source = _line_source(identifiers=[identifier])

    with pytest.raises(IgnGridNormalizationError, match="cleabs|null|empty"):
        normalize_ign_electric_lines(source)


def test_duplicate_line_cleabs_fails() -> None:
    source = _line_source(
        geometries=[
            LineString([(0, 0), (10, 10)]),
            LineString([(20, 20), (30, 30)]),
        ],
        identifiers=["DUPLICATE", "DUPLICATE"],
    )

    with pytest.raises(IgnGridNormalizationError, match="unique"):
        normalize_ign_electric_lines(source)


@pytest.mark.parametrize("crs", [None, "EPSG:4326", "EPSG:3857"])
def test_line_missing_or_wrong_crs_fails(crs: str | None) -> None:
    source = _line_source(crs=crs)

    with pytest.raises(IgnGridNormalizationError, match="CRS|2154"):
        normalize_ign_electric_lines(source)


def test_line_geometry_quality_is_classified_without_row_loss_or_repair() -> None:
    invalid = Polygon([(0, 0), (20, 20), (20, 0), (0, 20), (0, 0)])
    assert not invalid.is_valid
    source = _line_source(
        geometries=[LineString([(0, 0), (10, 10)]), None, LineString(), invalid],
        identifiers=["VALID", "NULL", "EMPTY", "INVALID"],
        voltages=["63 kV"] * 4,
    )

    normalized = normalize_ign_electric_lines(source)

    assert normalized["geometry_status"].tolist() == [
        "VALID",
        "NULL",
        "EMPTY",
        "INVALID",
    ]
    assert normalized["source_feature_id"].tolist() == [
        "VALID",
        "NULL",
        "EMPTY",
        "INVALID",
    ]
    assert len(normalized) == len(source)
    assert normalized.geometry.iloc[1] is None
    assert normalized.geometry.iloc[2].is_empty
    assert normalized.geometry.iloc[3].equals_exact(invalid, tolerance=0)


def test_line_normalization_preserves_exact_ids_crs_and_geometry() -> None:
    source = _line_source(
        geometries=[
            LineString([(0, 0), (10, 10)]),
            LineString([(50, 50), (60, 60)]),
        ],
        identifiers=["FIRST", "SECOND"],
    )

    normalized = normalize_ign_electric_lines(source)

    assert normalized["source_feature_id"].tolist() == ["FIRST", "SECOND"]
    assert normalized["grid_feature_id"].tolist() == [
        "IGN_BDTOPO:ELECTRIC_LINE:FIRST",
        "IGN_BDTOPO:ELECTRIC_LINE:SECOND",
    ]
    assert normalized.crs is not None
    assert normalized.crs.to_epsg() == 2154
    assert normalized.geometry.geom_equals_exact(source.geometry, tolerance=0).all()


def test_line_normalization_does_not_mutate_input_and_ignores_source_order() -> None:
    source = _line_source()
    reordered = source.loc[:, list(reversed(source.columns))].set_geometry("geometry")
    before = deepcopy(reordered)

    normalized = normalize_ign_electric_lines(reordered)

    assert_geodataframe_equal(reordered, before)
    assert list(normalized.columns) == list(LINE_OUTPUT_COLUMNS)


def test_missing_line_source_lineage_field_fails() -> None:
    source = _line_source().drop(columns="identifiants_sources")

    with pytest.raises(IgnGridNormalizationError, match="identifiants_sources"):
        normalize_ign_electric_lines(source)


@pytest.mark.parametrize("column", ["cleabs", "geometry"])
def test_missing_required_line_identity_or_geometry_fails(column: str) -> None:
    source = _line_source().drop(columns=column)

    with pytest.raises(IgnGridNormalizationError, match=column):
        normalize_ign_electric_lines(source)


def test_valid_transformation_post_is_normalized_without_voltage_inference() -> None:
    source = _post_source()

    normalized = normalize_ign_transformation_posts(source)

    row = normalized.iloc[0]
    assert list(normalized.columns) == list(TRANSFORMATION_POST_OUTPUT_COLUMNS)
    assert row["grid_feature_id"] == "IGN_BDTOPO:TRANSFORMATION_POST:POSTE-1"
    assert row["grid_feature_type"] == "TRANSFORMATION_POST"
    assert row["source_layer"] == "poste_de_transformation"
    assert row["source_feature_id"] == "POSTE-1"
    assert row["name"] == "Poste de test"
    assert row["name_status_raw"] == "Validé"
    assert row["importance_raw"] == "5"
    assert row["asset_status_raw"] == "En service"
    assert row["source_name_raw"] == "RTE 2021"
    assert row["source_identifiers_raw"] == "source-post-id"
    assert row["voltage_status"] == "UNKNOWN"
    assert pd.isna(row["voltage_kv"])
    assert row["spatial_role"] == "PROXY_GEOMETRY"
    assert row["geometry_status"] == "VALID"


def test_post_geometry_crs_and_input_are_preserved() -> None:
    source = _post_source()
    before = deepcopy(source)

    normalized = normalize_ign_transformation_posts(source)

    assert_geodataframe_equal(source, before)
    assert normalized.crs is not None
    assert normalized.crs.to_epsg() == 2154
    assert normalized.geometry.iloc[0].equals_exact(
        source.geometry.iloc[0], tolerance=0
    )
    assert normalized.index.equals(source.index)


def test_duplicate_post_cleabs_fails() -> None:
    polygon = Polygon([(0, 0), (0, 20), (20, 20), (20, 0), (0, 0)])
    source = _post_source(
        geometries=[polygon, polygon], identifiers=["DUPLICATE", "DUPLICATE"]
    )

    with pytest.raises(IgnGridNormalizationError, match="unique"):
        normalize_ign_transformation_posts(source)


def test_null_post_geometry_is_preserved_with_unknown_voltage() -> None:
    source = _post_source(geometries=[None])

    normalized = normalize_ign_transformation_posts(source)

    assert normalized.iloc[0]["geometry_status"] == "NULL"
    assert normalized.geometry.iloc[0] is None
    assert normalized.iloc[0]["voltage_status"] == "UNKNOWN"
    assert normalized["voltage_kv"].isna().all()

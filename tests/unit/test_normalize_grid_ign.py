from __future__ import annotations

import json
import tempfile
from copy import deepcopy
from dataclasses import replace
from hashlib import sha256
from math import isfinite
from pathlib import Path
from typing import Any, Literal, cast
from uuid import uuid4

import geopandas as gpd
import numpy as np
import pandas as pd
import pyogrio
import pytest
from geopandas.testing import assert_geodataframe_equal
from shapely.geometry import (
    LineString,
    MultiLineString,
    MultiPolygon,
    Point,
    Polygon,
)

import landscout.stages.normalize_grid_ign as grid_normalization
from landscout import stages
from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_source_config,
)
from landscout.stages.normalize_grid_ign import (
    LINE_OUTPUT_COLUMNS,
    TRANSFORMATION_POST_OUTPUT_COLUMNS,
    IgnGridNormalizationError,
    NormalizedIgnElectricityData,
    parse_ign_voltage,
)
from landscout.stages.normalize_grid_ign import (
    _IgnGridSourceContext as IgnGridSourceContext,
)
from landscout.stages.normalize_grid_ign import (
    _normalize_ign_electric_lines as normalize_ign_electric_lines,
)
from landscout.stages.normalize_grid_ign import (
    _normalize_ign_transformation_posts as normalize_ign_transformation_posts,
)
from landscout.stages.normalize_grid_ign import (
    normalize_ign_electricity as _normalize_ign_electricity,
)

LINE_LAYER = "LIGNE_ELECTRIQUE_V2"
POST_LAYER = "POSTE_DE_TRANSFORMATION_V2"
ROAD_LAYER = "TRONCON_DE_ROUTE"
DEPARTMENT_LAYER = "DEPARTEMENT"
ARCHIVE_SHA256 = "a" * 64
SOURCE_URL = "https://example.test/BDTOPO_D031.7z"
_FIXTURE_ROOT = Path(tempfile.mkdtemp(prefix="landscout-grid-ign-"))
_SOURCE_CONFIG_PAYLOAD = load_ign_bdtopo_source_config().model_dump(mode="json")
_SOURCE_CONFIG_PAYLOAD.update(
    {
        "source_url": SOURCE_URL,
        "checksum_url": None,
        "official_checksum_algorithm": None,
        "official_checksum": None,
        "expected_archive_size_bytes": 1234,
    }
)
SOURCE_CONFIG = IgnBdTopoSourceConfig.model_validate(_SOURCE_CONFIG_PAYLOAD)


def normalize_ign_electricity(
    source: IgnBdTopoElectricityData,
) -> NormalizedIgnElectricityData:
    return _normalize_ign_electricity(source, SOURCE_CONFIG)


def _line_source(
    geometries: list[object] | None = None,
    *,
    identifiers: list[object] | None = None,
    voltages: list[object] | None = None,
    precisions: list[object] | None = None,
    crs: str | None = "EPSG:2154",
    index: list[object] | None = None,
) -> gpd.GeoDataFrame:
    source_geometries = (
        geometries if geometries is not None else [LineString([(0, 0), (100, 100)])]
    )
    count = len(source_geometries)
    source_ids = (
        identifiers
        if identifiers is not None
        else [f"LIGNE-{item + 1}" for item in range(count)]
    )
    source_voltages = voltages if voltages is not None else ["225 kV"] * count
    source_precisions = precisions if precisions is not None else [2.5] * count
    source_index = index if index is not None else [100 + item for item in range(count)]
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
            "methode_d_acquisition_planimetrique": ["Photogrammétrie"] * count,
            "precision_planimetrique": source_precisions,
        },
        geometry=source_geometries,
        crs=crs,
        index=source_index,
    )


def _post_source(
    geometries: list[object] | None = None,
    *,
    identifiers: list[object] | None = None,
    precisions: list[object] | None = None,
    crs: str | None = "EPSG:2154",
    index: list[object] | None = None,
) -> gpd.GeoDataFrame:
    source_geometries = (
        geometries
        if geometries is not None
        else [Polygon([(0, 0), (0, 20), (20, 20), (20, 0), (0, 0)])]
    )
    count = len(source_geometries)
    source_ids = (
        identifiers
        if identifiers is not None
        else [f"POSTE-{item + 1}" for item in range(count)]
    )
    source_precisions = precisions if precisions is not None else [5.0] * count
    source_index = index if index is not None else [200 + item for item in range(count)]
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
            "methode_d_acquisition_planimetrique": ["Orthophotographie"] * count,
            "precision_planimetrique": source_precisions,
        },
        geometry=source_geometries,
        crs=crs,
        index=source_index,
    )


def _context(source_layer: str) -> IgnGridSourceContext:
    return IgnGridSourceContext(
        source_layer=source_layer,
        department_code="31",
        edition="2026-06-15",
        product_version="3.5",
        download_timestamp="2026-08-11T15:32:03+00:00",
        archive_sha256=ARCHIVE_SHA256,
        source_url=SOURCE_URL,
    )


def _summary(
    frame: gpd.GeoDataFrame,
    logical_name: Literal["electric_lines", "transformation_posts"],
    layer_name: str,
) -> IgnBdTopoLayerSummary:
    geometry = frame.geometry
    null_mask = geometry.isna()
    empty_mask = ~null_mask & geometry.is_empty
    invalid_mask = ~null_mask & ~geometry.is_empty & ~geometry.is_valid
    geometry_types = tuple(
        sorted(str(value) for value in geometry[~null_mask].geom_type.dropna().unique())
    )
    return IgnBdTopoLayerSummary(
        logical_name=logical_name,
        source_layer_name=layer_name,
        crs=str(frame.crs),
        feature_count=len(frame),
        columns=tuple(str(column) for column in frame.columns),
        dtypes=tuple(
            (str(column), str(dtype)) for column, dtype in frame.dtypes.items()
        ),
        null_geometry_count=int(null_mask.sum()),
        empty_geometry_count=int(empty_mask.sum()),
        invalid_geometry_count=int(invalid_mask.sum()),
        geometry_types=geometry_types,
    )


def _source_bundle(
    lines: gpd.GeoDataFrame | None = None,
    posts: gpd.GeoDataFrame | None = None,
) -> IgnBdTopoElectricityData:
    line_frame = lines if lines is not None else _line_source()
    post_frame = posts if posts is not None else _post_source()
    extraction_path = _FIXTURE_ROOT / uuid4().hex
    extraction_path.mkdir(parents=True)
    geopackage_path = extraction_path / "data.gpkg"
    pyogrio.write_dataframe(
        line_frame, geopackage_path, layer=LINE_LAYER, driver="GPKG"
    )
    pyogrio.write_dataframe(
        post_frame,
        geopackage_path,
        layer=POST_LAYER,
        driver="GPKG",
        append=True,
    )
    pyogrio.write_dataframe(
        gpd.GeoDataFrame(
            {"id": ["road"]},
            geometry=[LineString([(0, 0), (1, 1)])],
            crs="EPSG:2154",
        ),
        geopackage_path,
        layer=ROAD_LAYER,
        driver="GPKG",
        append=True,
    )
    pyogrio.write_dataframe(
        gpd.GeoDataFrame(
            {"code_insee": ["31"]},
            geometry=[Polygon([(0, 0), (0, 10), (10, 10), (10, 0)])],
            crs="EPSG:2154",
        ),
        geopackage_path,
        layer=DEPARTMENT_LAYER,
        driver="GPKG",
        append=True,
    )
    line_frame = gpd.read_file(geopackage_path, layer=LINE_LAYER, engine="pyogrio")
    post_frame = gpd.read_file(geopackage_path, layer=POST_LAYER, engine="pyogrio")
    payload = geopackage_path.read_bytes()
    layer_names = tuple(str(row[0]) for row in pyogrio.list_layers(geopackage_path))
    digest = sha256(payload).hexdigest()
    marker = {
        "schema_version": 3,
        "archive_sha256": ARCHIVE_SHA256,
        "geopackage_relative_path": "data.gpkg",
        "geopackage_size_bytes": len(payload),
        "geopackage_sha256": digest,
        "all_layer_names": list(layer_names),
        "electric_lines_layer": LINE_LAYER,
        "transformation_posts_layer": POST_LAYER,
        "road_segments_layer": ROAD_LAYER,
        "department_layer": DEPARTMENT_LAYER,
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
    (extraction_path / ".landscout-extraction.json").write_text(
        json.dumps(marker), encoding="utf-8"
    )
    archive = IgnBdTopoDownload(
        provider=SOURCE_CONFIG.provider,
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
        extraction_path=extraction_path,
        geopackage_path=geopackage_path,
        geopackage_filename="data.gpkg",
        geopackage_size_bytes=len(payload),
        geopackage_sha256=digest,
        all_layer_names=layer_names,
        electric_lines_layer=LINE_LAYER,
        transformation_posts_layer=POST_LAYER,
        road_segments_layer=ROAD_LAYER,
        department_layer=DEPARTMENT_LAYER,
        cache_hit=True,
    )
    return IgnBdTopoElectricityData(
        extraction=extraction,
        electric_lines=line_frame,
        transformation_posts=post_frame,
        electric_lines_summary=_summary(line_frame, "electric_lines", LINE_LAYER),
        transformation_posts_summary=_summary(
            post_frame, "transformation_posts", POST_LAYER
        ),
    )


def _source_bundle_with_archive(**changes: object) -> IgnBdTopoElectricityData:
    source = _source_bundle()
    archive = replace(source.extraction.archive, **changes)
    return replace(source, extraction=replace(source.extraction, archive=archive))


@pytest.mark.parametrize(
    "name",
    [
        "IgnGridSourceContext",
        "normalize_ign_electric_lines",
        "normalize_ign_transformation_posts",
    ],
)
def test_low_level_normalization_is_not_part_of_stages_public_api(name: str) -> None:
    assert name not in stages.__all__
    assert not hasattr(stages, name)


def test_supported_package_api_keeps_high_level_normalization() -> None:
    expected_names = {
        "IgnGridNormalizationError",
        "IgnVoltageNormalization",
        "NormalizedIgnElectricityData",
        "parse_ign_voltage",
        "normalize_ign_electricity",
    }

    assert expected_names <= set(stages.__all__)
    normalized = stages.normalize_ign_electricity(_source_bundle(), SOURCE_CONFIG)
    assert normalized.electric_lines["source_layer"].unique().tolist() == [LINE_LAYER]
    assert normalized.transformation_posts["source_layer"].unique().tolist() == [
        POST_LAYER
    ]


@pytest.mark.parametrize("department_code", ["31", "2A", "2B", "971", "976"])
def test_internal_source_context_accepts_supported_department_codes(
    department_code: str,
) -> None:
    context = replace(_context(LINE_LAYER), department_code=department_code)

    grid_normalization._validate_source_context(context)


def test_internal_source_context_rejects_uppercase_sha256() -> None:
    archive_sha256 = "A" * 64
    context = replace(_context(LINE_LAYER), archive_sha256=archive_sha256)

    with pytest.raises(IgnGridNormalizationError, match="archive_sha256"):
        normalize_ign_electric_lines(_line_source(), context)


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("feature_count", True),
        ("feature_count", 1.0),
        ("feature_count", "1"),
        ("feature_count", -1),
        ("null_geometry_count", False),
        ("null_geometry_count", 0.0),
        ("empty_geometry_count", "0"),
        ("invalid_geometry_count", -1),
        ("columns", ["cleabs", "geometry"]),
        ("columns", ("cleabs", "cleabs")),
        ("dtypes", [("cleabs", "str")]),
        ("dtypes", (("cleabs",),)),
        ("geometry_types", ["LineString"]),
    ],
)
def test_grid_summary_requires_strict_structural_types(
    field: str, value: object
) -> None:
    source = _source_bundle()
    changed = replace(source.electric_lines_summary, **{field: value})

    with pytest.raises(IgnGridNormalizationError):
        normalize_ign_electricity(replace(source, electric_lines_summary=changed))


@pytest.mark.parametrize("value", ["A" * 64, "a" * 63, "a" * 65, "g" * 64])
def test_grid_archive_sha256_requires_canonical_lowercase(value: str) -> None:
    source = _source_bundle_with_archive(sha256=value)

    with pytest.raises(IgnGridNormalizationError):
        normalize_ign_electricity(source)


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("source_layer", ""),
        ("source_layer", " LIGNE_ELECTRIQUE "),
        ("source_layer", 42),
        ("department_code", "XYZ"),
        ("edition", "2026-02-31"),
        ("download_timestamp", "not-a-datetime"),
        ("download_timestamp", "2026-08-11T15:32:03"),
        ("archive_sha256", "a" * 63),
        ("archive_sha256", "g" * 64),
        ("source_url", "not-a-url"),
        ("source_url", "file:///tmp/archive.7z"),
        ("product_version", ""),
        ("product_version", " 3.5 "),
    ],
)
def test_internal_source_context_rejects_invalid_lineage_values(
    field: str,
    value: object,
) -> None:
    context = replace(_context(LINE_LAYER), **{field: value})

    with pytest.raises(IgnGridNormalizationError):
        grid_normalization._validate_source_context(context)


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
def test_exact_voltage_parser_is_generic_and_finite(
    raw: str, expected_kv: float
) -> None:
    parsed = parse_ign_voltage(raw)

    assert parsed.raw == raw
    assert parsed.status == "EXACT"
    assert parsed.voltage_kv == expected_kv
    assert parsed.voltage_kv is not None and isfinite(parsed.voltage_kv)
    assert parsed.voltage_upper_bound_kv is None


@pytest.mark.parametrize(
    ("raw", "expected_upper_bound"),
    [("<63 kV", 63.0), ("<90 kV", 90.0), (" < 110 KV ", 110.0)],
)
def test_bounded_voltage_is_generic_finite_and_not_exact(
    raw: str, expected_upper_bound: float
) -> None:
    parsed = parse_ign_voltage(raw)

    assert parsed.raw == raw
    assert parsed.status == "BELOW"
    assert parsed.voltage_kv is None
    assert parsed.voltage_upper_bound_kv == expected_upper_bound
    assert isfinite(parsed.voltage_upper_bound_kv)


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


@pytest.mark.parametrize(
    "value",
    ["Très haute tension future", ["63 kV"], np.array(["63 kV"])],
)
def test_unexpected_or_non_scalar_voltage_is_controlled_unparsed(
    value: object,
) -> None:
    parsed = parse_ign_voltage(value)

    assert parsed.status == "UNPARSED"
    assert parsed.voltage_kv is None
    assert parsed.voltage_upper_bound_kv is None


@pytest.mark.parametrize(
    "raw",
    ["0 kV", "<0 kV", "-63 kV", "63 V", f"{'9' * 400} kV", f"<{'9' * 400} kV"],
)
def test_invalid_or_overflowing_numeric_voltage_is_unparsed(raw: str) -> None:
    parsed = parse_ign_voltage(raw)

    assert parsed.status == "UNPARSED"
    assert parsed.voltage_kv is None
    assert parsed.voltage_upper_bound_kv is None


def test_valid_line_has_stable_identity_lineage_and_range_index() -> None:
    source = _line_source()

    normalized = normalize_ign_electric_lines(source, _context(LINE_LAYER))

    row = normalized.iloc[0]
    assert list(normalized.columns) == list(LINE_OUTPUT_COLUMNS)
    assert isinstance(normalized.index, pd.RangeIndex)
    assert row["grid_feature_id"] == "IGN_BDTOPO:ELECTRIC_LINE:LIGNE-1"
    assert row["source_feature_id"] == "LIGNE-1"
    assert row["source_provider"] == "IGN"
    assert row["source_product"] == "BD_TOPO"
    assert row["source_layer"] == LINE_LAYER
    assert row["source_department_code"] == "31"
    assert row["source_edition"] == "2026-06-15"
    assert row["source_product_version"] == "3.5"
    assert row["source_download_timestamp"] == "2026-08-11T15:32:03+00:00"
    assert row["source_archive_sha256"] == ARCHIVE_SHA256
    assert row["source_url"] == SOURCE_URL
    assert row["manager_name"] == "Réseau de Transport d'Électricité"
    assert row["asset_status_raw"] == "En service"
    assert row["source_identifiers_raw"] == "source-id"
    assert row["planimetric_precision_m"] == 2.5
    assert row["spatial_role"] == "PROXY_GEOMETRY"


def test_deenergized_voltage_does_not_override_source_asset_status() -> None:
    normalized = normalize_ign_electric_lines(
        _line_source(voltages=["Hors tension"]), _context(LINE_LAYER)
    )

    assert normalized.iloc[0]["voltage_status"] == "DEENERGIZED"
    assert normalized.iloc[0]["asset_status_raw"] == "En service"


@pytest.mark.parametrize("identifier", [None, "", "   "])
def test_null_or_empty_line_cleabs_fails(identifier: object) -> None:
    with pytest.raises(IgnGridNormalizationError, match="cleabs|null|empty"):
        normalize_ign_electric_lines(
            _line_source(identifiers=[identifier]), _context(LINE_LAYER)
        )


@pytest.mark.parametrize(
    "identifier",
    [" leading", "trailing ", "IGN:BAD", "IGN\nCONTROL", "IGN\tCONTROL"],
)
def test_unsafe_source_id_is_rejected_without_rewriting(identifier: str) -> None:
    with pytest.raises(IgnGridNormalizationError, match="cleabs|whitespace|control|:"):
        normalize_ign_electric_lines(
            _line_source(identifiers=[identifier]), _context(LINE_LAYER)
        )


def test_duplicate_line_cleabs_fails() -> None:
    source = _line_source(
        geometries=[
            LineString([(0, 0), (10, 10)]),
            LineString([(20, 20), (30, 30)]),
        ],
        identifiers=["DUPLICATE", "DUPLICATE"],
    )

    with pytest.raises(IgnGridNormalizationError, match="unique"):
        normalize_ign_electric_lines(source, _context(LINE_LAYER))


@pytest.mark.parametrize("crs", [None, "EPSG:4326", "EPSG:3857"])
def test_line_missing_or_wrong_crs_fails(crs: str | None) -> None:
    with pytest.raises(IgnGridNormalizationError, match="CRS|2154"):
        normalize_ign_electric_lines(_line_source(crs=crs), _context(LINE_LAYER))


def test_line_geometry_quality_is_preserved_without_row_loss_or_repair() -> None:
    invalid = Polygon([(0, 0), (20, 20), (20, 0), (0, 20), (0, 0)])
    source = _line_source(
        geometries=[LineString([(0, 0), (10, 10)]), None, LineString(), invalid],
        identifiers=["VALID", "NULL", "EMPTY", "INVALID"],
        voltages=["63 kV"] * 4,
    )

    normalized = normalize_ign_electric_lines(source, _context(LINE_LAYER))

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
    assert normalized.geometry.iloc[1] is None
    assert normalized.geometry.iloc[2].is_empty
    assert normalized.geometry.iloc[3].equals_exact(invalid, tolerance=0)


def test_z_coordinates_are_preserved() -> None:
    source = _line_source(geometries=[LineString([(0, 0, 10), (10, 10, 20)])])

    normalized = normalize_ign_electric_lines(source, _context(LINE_LAYER))

    assert source.geometry.iloc[0].has_z
    assert normalized.geometry.iloc[0].has_z
    assert normalized.geometry.iloc[0].equals_exact(
        source.geometry.iloc[0], tolerance=0
    )


def test_unusual_duplicate_source_index_is_not_preserved_as_identity() -> None:
    source = _line_source(
        geometries=[
            LineString([(0, 0), (10, 10)]),
            LineString([(20, 20), (30, 30)]),
        ],
        identifiers=["FIRST", "SECOND"],
        index=[77, 77],
    )

    normalized = normalize_ign_electric_lines(source, _context(LINE_LAYER))

    assert isinstance(normalized.index, pd.RangeIndex)
    assert normalized.index.tolist() == [0, 1]
    assert normalized["source_feature_id"].tolist() == ["FIRST", "SECOND"]
    assert normalized["grid_feature_id"].tolist() == [
        "IGN_BDTOPO:ELECTRIC_LINE:FIRST",
        "IGN_BDTOPO:ELECTRIC_LINE:SECOND",
    ]


def test_line_normalization_does_not_mutate_input_and_has_stable_columns() -> None:
    source = _line_source()
    reordered = source.loc[:, list(reversed(source.columns))].set_geometry("geometry")
    before = deepcopy(reordered)

    normalized = normalize_ign_electric_lines(reordered, _context(LINE_LAYER))

    assert_geodataframe_equal(reordered, before)
    assert list(normalized.columns) == list(LINE_OUTPUT_COLUMNS)


@pytest.mark.parametrize("column", ["cleabs", "geometry", "identifiants_sources"])
def test_missing_required_line_field_fails(column: str) -> None:
    source = _line_source().drop(columns=column)

    with pytest.raises(IgnGridNormalizationError, match=column):
        normalize_ign_electric_lines(source, _context(LINE_LAYER))


@pytest.mark.parametrize("precision", [0, 2.5, None, float("nan")])
def test_valid_or_null_line_precision_is_normalized_to_float(
    precision: object,
) -> None:
    normalized = normalize_ign_electric_lines(
        _line_source(precisions=[precision]), _context(LINE_LAYER)
    )

    assert str(normalized["planimetric_precision_m"].dtype) == "float64"
    if precision is None or (isinstance(precision, float) and np.isnan(precision)):
        assert pd.isna(normalized.iloc[0]["planimetric_precision_m"])
    else:
        assert normalized.iloc[0]["planimetric_precision_m"] == float(precision)


@pytest.mark.parametrize("precision", [-1, float("inf"), float("-inf"), True, "2.5"])
def test_invalid_line_precision_fails(precision: object) -> None:
    with pytest.raises(IgnGridNormalizationError, match="precision_planimetrique"):
        normalize_ign_electric_lines(
            _line_source(precisions=[precision]), _context(LINE_LAYER)
        )


def test_normalized_voltage_never_emits_non_finite_numeric_values() -> None:
    huge = f"{'9' * 400} kV"
    source = _line_source(
        geometries=[LineString([(0, 0), (1, 1)])] * 4,
        identifiers=["EXACT", "BELOW", "OVERFLOW", "MISSING"],
        voltages=["225 kV", "<90 kV", huge, None],
    )

    normalized = normalize_ign_electric_lines(source, _context(LINE_LAYER))

    assert normalized["voltage_status"].tolist() == [
        "EXACT",
        "BELOW",
        "UNPARSED",
        "UNKNOWN",
    ]
    assert np.isfinite(normalized["voltage_kv"].dropna()).all()
    assert np.isfinite(normalized["voltage_upper_bound_kv"].dropna()).all()


def test_valid_post_has_stable_lineage_and_no_voltage_inference() -> None:
    source = _post_source()

    normalized = normalize_ign_transformation_posts(source, _context(POST_LAYER))

    row = normalized.iloc[0]
    assert list(normalized.columns) == list(TRANSFORMATION_POST_OUTPUT_COLUMNS)
    assert isinstance(normalized.index, pd.RangeIndex)
    assert row["grid_feature_id"] == "IGN_BDTOPO:TRANSFORMATION_POST:POSTE-1"
    assert row["source_layer"] == POST_LAYER
    assert row["source_department_code"] == "31"
    assert row["source_archive_sha256"] == ARCHIVE_SHA256
    assert row["name"] == "Poste de test"
    assert row["voltage_status"] == "UNKNOWN"
    assert pd.isna(row["voltage_kv"])
    assert row["spatial_role"] == "PROXY_GEOMETRY"


def test_post_geometry_crs_and_input_are_preserved() -> None:
    source = _post_source()
    before = deepcopy(source)

    normalized = normalize_ign_transformation_posts(source, _context(POST_LAYER))

    assert_geodataframe_equal(source, before)
    assert normalized.crs is not None and normalized.crs.to_epsg() == 2154
    assert normalized.geometry.iloc[0].equals_exact(
        source.geometry.iloc[0], tolerance=0
    )


def test_duplicate_post_cleabs_fails() -> None:
    polygon = Polygon([(0, 0), (0, 20), (20, 20), (20, 0), (0, 0)])
    source = _post_source(
        geometries=[polygon, polygon], identifiers=["DUPLICATE", "DUPLICATE"]
    )

    with pytest.raises(IgnGridNormalizationError, match="unique"):
        normalize_ign_transformation_posts(source, _context(POST_LAYER))


def test_null_post_geometry_and_precision_are_preserved() -> None:
    normalized = normalize_ign_transformation_posts(
        _post_source(geometries=[None], precisions=[None]), _context(POST_LAYER)
    )

    assert normalized.iloc[0]["geometry_status"] == "NULL"
    assert normalized.geometry.iloc[0] is None
    assert normalized.iloc[0]["voltage_status"] == "UNKNOWN"
    assert normalized["voltage_kv"].isna().all()
    assert normalized["planimetric_precision_m"].isna().all()


def test_invalid_post_precision_fails() -> None:
    with pytest.raises(IgnGridNormalizationError, match="precision_planimetrique"):
        normalize_ign_transformation_posts(
            _post_source(precisions=["5.0"]), _context(POST_LAYER)
        )


def test_appropriate_multigeometry_types_are_accepted() -> None:
    multilines = MultiLineString([[(0, 0), (10, 10)], [(20, 20), (30, 30)]])
    multipolygon = MultiPolygon(
        [
            Polygon([(0, 0), (0, 5), (5, 5), (5, 0), (0, 0)]),
            Polygon([(10, 10), (10, 15), (15, 15), (15, 10), (10, 10)]),
        ]
    )

    lines = normalize_ign_electric_lines(
        _line_source(geometries=[multilines]), _context(LINE_LAYER)
    )
    posts = normalize_ign_transformation_posts(
        _post_source(geometries=[multipolygon]), _context(POST_LAYER)
    )

    assert lines.iloc[0]["geometry_status"] == "VALID"
    assert lines.geometry.iloc[0].geom_type == "MultiLineString"
    assert posts.iloc[0]["geometry_status"] == "VALID"
    assert posts.geometry.iloc[0].geom_type == "MultiPolygon"


@pytest.mark.parametrize(
    "geometry",
    [
        Polygon([(0, 0), (0, 5), (5, 5), (5, 0), (0, 0)]),
        Point(1, 1),
    ],
)
def test_valid_polygon_or_point_is_rejected_as_electric_line(
    geometry: object,
) -> None:
    with pytest.raises(IgnGridNormalizationError, match="geometry types"):
        normalize_ign_electric_lines(
            _line_source(geometries=[geometry]), _context(LINE_LAYER)
        )


@pytest.mark.parametrize("geometry", [LineString([(0, 0), (10, 10)]), Point(1, 1)])
def test_valid_line_or_point_is_rejected_as_transformation_post(
    geometry: object,
) -> None:
    with pytest.raises(IgnGridNormalizationError, match="geometry types"):
        normalize_ign_transformation_posts(
            _post_source(geometries=[geometry]), _context(POST_LAYER)
        )


def test_high_level_path_uses_discovered_layer_names_and_archive_lineage() -> None:
    source = _source_bundle()

    normalized = normalize_ign_electricity(source)

    assert normalized.electric_lines["source_layer"].unique().tolist() == [LINE_LAYER]
    assert normalized.transformation_posts["source_layer"].unique().tolist() == [
        POST_LAYER
    ]
    for frame in (normalized.electric_lines, normalized.transformation_posts):
        assert frame["source_department_code"].unique().tolist() == ["31"]
        assert frame["source_edition"].unique().tolist() == ["2026-06-15"]
        assert frame["source_product_version"].unique().tolist() == ["3.5"]
        assert frame["source_archive_sha256"].unique().tolist() == [ARCHIVE_SHA256]
        assert frame["source_url"].unique().tolist() == [SOURCE_URL]


def test_high_level_rejects_coordinated_frame_and_summary_forgery() -> None:
    source = _source_bundle()
    forged = source.electric_lines.copy()
    forged.loc[0, "voltage"] = "400 kV"
    forged_summary = _summary(forged, "electric_lines", LINE_LAYER)

    with pytest.raises(IgnGridNormalizationError, match="physical|fresh|source"):
        normalize_ign_electricity(
            replace(
                source,
                electric_lines=forged,
                electric_lines_summary=forged_summary,
            )
        )


def test_source_complete_grid_validation_does_not_mutate_supplied_frames() -> None:
    source = _source_bundle()
    lines_before = deepcopy(source.electric_lines)
    posts_before = deepcopy(source.transformation_posts)

    normalize_ign_electricity(source)

    assert_geodataframe_equal(source.electric_lines, lines_before)
    assert_geodataframe_equal(source.transformation_posts, posts_before)


def test_grid_normalization_uses_distinct_fresh_revalidated_frames(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    source = _source_bundle()
    fresh = replace(
        source,
        electric_lines=source.electric_lines.copy(deep=True),
        transformation_posts=source.transformation_posts.copy(deep=True),
    )
    expected_voltage = fresh.electric_lines.loc[0, "voltage"]

    def return_fresh_and_mutate_supplied(
        _: object,
        __: object,
    ) -> IgnBdTopoElectricityData:
        source.electric_lines.loc[0, "voltage"] = "FORGED AFTER REVALIDATION"
        return fresh

    monkeypatch.setattr(
        grid_normalization,
        "_revalidate_ign_bdtopo_electricity_data",
        return_fresh_and_mutate_supplied,
    )

    normalized = _normalize_ign_electricity(source, SOURCE_CONFIG)

    assert normalized.electric_lines.loc[0, "voltage_raw"] == expected_voltage
    assert source.electric_lines.loc[0, "voltage"] == "FORGED AFTER REVALIDATION"


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("provider", "Unrelated data vendor"),
        ("product", "OTHER PRODUCT"),
        ("projection", "EPSG:4326"),
    ],
)
def test_high_level_rejects_incompatible_archive_identity(
    field: str,
    value: str,
) -> None:
    source = _source_bundle_with_archive(**{field: value})

    with pytest.raises(IgnGridNormalizationError, match="lineage|config"):
        normalize_ign_electricity(source)


def test_archive_identity_requires_exact_pinned_strings() -> None:
    provider = "INSTITUT NATIONAL DE L'INFORMATION GEOGRAPHIQUE ET FORESTIERE (ign)"
    product = "bd-topo"
    source = _source_bundle_with_archive(
        provider=provider,
        product=product,
    )

    with pytest.raises(IgnGridNormalizationError, match="provider|product|config"):
        normalize_ign_electricity(source)


def test_high_level_rejects_summary_row_count_mismatch() -> None:
    source = _source_bundle()
    summary = replace(
        source.electric_lines_summary,
        feature_count=source.electric_lines_summary.feature_count + 1,
    )

    with pytest.raises(IgnGridNormalizationError, match="summary|physical"):
        normalize_ign_electricity(replace(source, electric_lines_summary=summary))


def test_high_level_rejects_summary_layer_name_mismatch() -> None:
    source = _source_bundle()
    summary = replace(source.electric_lines_summary, source_layer_name="WRONG")

    with pytest.raises(IgnGridNormalizationError, match="summary|physical"):
        normalize_ign_electricity(replace(source, electric_lines_summary=summary))


def test_high_level_rejects_wrong_logical_name() -> None:
    source = _source_bundle()
    summary = replace(
        source.electric_lines_summary,
        logical_name=cast(Any, "transformation_posts"),
    )

    with pytest.raises(IgnGridNormalizationError, match="summary|physical"):
        normalize_ign_electricity(replace(source, electric_lines_summary=summary))


def test_high_level_rejects_summary_crs_mismatch() -> None:
    source = _source_bundle()
    summary = replace(source.electric_lines_summary, crs="EPSG:4326")

    with pytest.raises(IgnGridNormalizationError, match="summary|physical|CRS|2154"):
        normalize_ign_electricity(replace(source, electric_lines_summary=summary))


@pytest.mark.parametrize("mutation", ["missing", "extra", "reordered", "dtype"])
def test_high_level_rejects_forged_ordered_summary_schema(mutation: str) -> None:
    source = _source_bundle()
    summary = source.electric_lines_summary
    if mutation == "missing":
        changed = replace(summary, columns=summary.columns[:-1])
    elif mutation == "extra":
        changed = replace(summary, columns=(*summary.columns, "invented"))
    elif mutation == "reordered":
        changed = replace(summary, columns=tuple(reversed(summary.columns)))
    else:
        dtypes = list(summary.dtypes)
        dtypes[0] = (dtypes[0][0], "object")
        changed = replace(summary, dtypes=tuple(dtypes))

    with pytest.raises(
        IgnGridNormalizationError,
        match="summary|physical|schema|columns|dtype",
    ):
        normalize_ign_electricity(replace(source, electric_lines_summary=changed))


def test_high_level_rejects_duplicate_or_missing_layer_inventory() -> None:
    source = _source_bundle()
    duplicate = replace(
        source,
        extraction=replace(
            source.extraction,
            all_layer_names=(LINE_LAYER, POST_LAYER, LINE_LAYER),
        ),
    )
    with pytest.raises(
        IgnGridNormalizationError,
        match="integrity|inventory|duplicate",
    ):
        normalize_ign_electricity(duplicate)

    missing = replace(
        source,
        extraction=replace(
            source.extraction,
            all_layer_names=(POST_LAYER,),
        ),
    )
    with pytest.raises(
        IgnGridNormalizationError,
        match="integrity|inventory|selected",
    ):
        normalize_ign_electricity(missing)


def test_high_level_rejects_colliding_electricity_roles() -> None:
    source = _source_bundle()
    extraction = replace(
        source.extraction,
        transformation_posts_layer=LINE_LAYER,
    )
    post_summary = replace(
        source.transformation_posts_summary,
        source_layer_name=LINE_LAYER,
    )

    with pytest.raises(
        IgnGridNormalizationError,
        match="integrity|same layer|distinct|role",
    ):
        normalize_ign_electricity(
            replace(
                source,
                extraction=extraction,
                transformation_posts_summary=post_summary,
            )
        )


def test_high_level_rejects_stale_geometry_counts_after_frame_mutation() -> None:
    source = _source_bundle()
    mutated = source.electric_lines.copy()
    mutated.at[mutated.index[0], "geometry"] = None

    with pytest.raises(
        IgnGridNormalizationError,
        match="freshly read physical source|geometry summary",
    ):
        normalize_ign_electricity(replace(source, electric_lines=mutated))


def test_high_level_rejects_stale_geometry_types_after_frame_mutation() -> None:
    source = _source_bundle()
    mutated = source.electric_lines.copy()
    mutated.at[mutated.index[0], "geometry"] = MultiLineString(
        [[(0, 0), (10, 10)], [(20, 20), (30, 30)]]
    )

    with pytest.raises(
        IgnGridNormalizationError,
        match="freshly read physical source|geometry summary",
    ):
        normalize_ign_electricity(replace(source, electric_lines=mutated))


@pytest.mark.parametrize(
    "component", ["source", "extraction", "archive", "line_summary", "post_summary"]
)
def test_high_level_rejects_any_spatial_role_mismatch(component: str) -> None:
    source = _source_bundle()
    wrong_role = cast(Any, "EXACT_RTE_GEOMETRY")
    if component == "source":
        inconsistent = replace(source, spatial_role=wrong_role)
    elif component == "extraction":
        inconsistent = replace(
            source, extraction=replace(source.extraction, spatial_role=wrong_role)
        )
    elif component == "archive":
        extraction = replace(
            source.extraction,
            archive=replace(source.extraction.archive, spatial_role=wrong_role),
        )
        inconsistent = replace(source, extraction=extraction)
    elif component == "line_summary":
        inconsistent = replace(
            source,
            electric_lines_summary=replace(
                source.electric_lines_summary, spatial_role=wrong_role
            ),
        )
    else:
        inconsistent = replace(
            source,
            transformation_posts_summary=replace(
                source.transformation_posts_summary, spatial_role=wrong_role
            ),
        )

    with pytest.raises(
        IgnGridNormalizationError,
        match="source-complete|role|spatial|lineage|integrity|PROXY_GEOMETRY",
    ):
        normalize_ign_electricity(inconsistent)

import gzip
import json
from pathlib import Path
from unittest.mock import patch

import geopandas as gpd
import pytest

from landscout.sources.cadastre_loader_fr import (
    CadastreLoadError,
    EmptyCadastreDatasetError,
    MissingGeometryColumnError,
    UnsupportedGeometryTypeError,
    load_cadastre_parcels,
)


def _write_geojson(path: Path, features: list[dict]) -> None:
    content = {"type": "FeatureCollection", "features": features}
    path.write_text(json.dumps(content), encoding="utf-8")


def test_load_valid_geojson_preserves_attributes(tmp_path: Path) -> None:
    path = tmp_path / "parcels.geojson"
    _write_geojson(
        path,
        [
            {
                "type": "Feature",
                "properties": {"id": "parcel-1", "section": "AB", "numero": "42"},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[1, 43], [2, 43], [2, 44], [1, 43]]],
                },
            },
            {
                "type": "Feature",
                "properties": {"id": "parcel-2", "section": "AC", "numero": "7"},
                "geometry": {
                    "type": "MultiPolygon",
                    "coordinates": [[[[3, 43], [4, 43], [4, 44], [3, 43]]]],
                },
            },
        ],
    )

    parcels = load_cadastre_parcels(path)

    assert len(parcels) == 2
    assert list(parcels.columns) == ["id", "section", "numero", "geometry"]
    assert set(parcels.geometry.geom_type) == {"Polygon", "MultiPolygon"}
    assert parcels.crs is not None


def test_load_valid_gzipped_geojson(tmp_path: Path) -> None:
    plain_path = tmp_path / "parcels.geojson"
    gzip_path = tmp_path / "parcels.json.gz"
    _write_geojson(
        plain_path,
        [
            {
                "type": "Feature",
                "properties": {"id": "parcel-1"},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[1, 43], [2, 43], [2, 44], [1, 43]]],
                },
            }
        ],
    )
    gzip_path.write_bytes(gzip.compress(plain_path.read_bytes()))

    parcels = load_cadastre_parcels(gzip_path)

    assert len(parcels) == 1
    assert parcels.iloc[0]["id"] == "parcel-1"


def test_empty_dataset_fails(tmp_path: Path) -> None:
    path = tmp_path / "empty.geojson"
    _write_geojson(path, [])

    with pytest.raises(EmptyCadastreDatasetError):
        load_cadastre_parcels(path)


def test_missing_file_fails(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError):
        load_cadastre_parcels(tmp_path / "missing.geojson")


def test_invalid_file_fails(tmp_path: Path) -> None:
    path = tmp_path / "invalid.geojson"
    path.write_text("not GeoJSON", encoding="utf-8")

    with pytest.raises(CadastreLoadError):
        load_cadastre_parcels(path)


def test_missing_geometry_column_fails(tmp_path: Path) -> None:
    path = tmp_path / "parcels.geojson"
    path.touch()
    frame_without_geometry = gpd.GeoDataFrame({"id": ["parcel-1"]})

    with (
        patch(
            "landscout.sources.cadastre_loader_fr.gpd.read_file",
            return_value=frame_without_geometry,
        ),
        pytest.raises(MissingGeometryColumnError),
    ):
        load_cadastre_parcels(path)


def test_unsupported_geometry_type_fails(tmp_path: Path) -> None:
    path = tmp_path / "points.geojson"
    _write_geojson(
        path,
        [
            {
                "type": "Feature",
                "properties": {"id": "point-1"},
                "geometry": {"type": "Point", "coordinates": [1, 43]},
            }
        ],
    )

    with pytest.raises(UnsupportedGeometryTypeError, match="Point"):
        load_cadastre_parcels(path)

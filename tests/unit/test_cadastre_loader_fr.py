import gzip
import json
from hashlib import sha256
from pathlib import Path
from unittest.mock import patch

import geopandas as gpd
import pytest

import landscout.sources.cadastre_loader_fr as cadastre_loader
from landscout import sources
from landscout.sources.cadastre_fr import CadastreDownload
from landscout.sources.cadastre_loader_fr import (
    CadastreLoadError,
    CadastreParcelSource,
    EmptyCadastreDatasetError,
    MissingGeometryColumnError,
    UnsupportedGeometryTypeError,
    load_cadastre_parcels,
    revalidate_cadastre_parcel_source,
)

COMMUNE_CODE = "31395"
OFFICIAL_FILENAME = f"cadastre-{COMMUNE_CODE}-parcelles.json.gz"
OFFICIAL_URL = (
    "https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes/"
    f"31/{COMMUNE_CODE}/{OFFICIAL_FILENAME}"
)


def test_public_sources_export_the_source_bound_cadastre_api() -> None:
    expected = {
        "CadastreLoadError",
        "CadastreParcelSource",
        "EmptyCadastreDatasetError",
        "MissingGeometryColumnError",
        "UnsupportedGeometryTypeError",
        "load_cadastre_parcels",
        "revalidate_cadastre_parcel_source",
    }
    assert sources.CadastreParcelSource is CadastreParcelSource
    assert sources.load_cadastre_parcels is load_cadastre_parcels
    assert (
        sources.revalidate_cadastre_parcel_source is revalidate_cadastre_parcel_source
    )
    assert set(cadastre_loader.__all__) == expected
    assert expected <= set(sources.__all__)


def _write_geojson(path: Path, features: list[dict]) -> None:
    content = {"type": "FeatureCollection", "features": features}
    path.write_text(json.dumps(content), encoding="utf-8")


def _write_gzipped_geojson(path: Path, features: list[dict]) -> None:
    content = json.dumps({"type": "FeatureCollection", "features": features}).encode()
    path.write_bytes(gzip.compress(content))


def _download(path: Path, **changes: object) -> CadastreDownload:
    content = path.read_bytes() if path.is_file() else b"missing"
    values: dict[str, object] = {
        "commune_code": COMMUNE_CODE,
        "source_url": OFFICIAL_URL,
        "download_timestamp": "2026-08-16T10:00:00+00:00",
        "filename": path.name,
        "file_size": len(content),
        "sha256": sha256(content).hexdigest(),
        "path": path,
        "cache_hit": True,
    }
    values.update(changes)
    return CadastreDownload(**values)  # type: ignore[arg-type]


def test_load_valid_geojson_preserves_attributes(tmp_path: Path) -> None:
    path = tmp_path / OFFICIAL_FILENAME
    _write_gzipped_geojson(
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

    source = load_cadastre_parcels(_download(path))
    assert type(source) is CadastreParcelSource
    parcels = source.parcels

    assert len(parcels) == 2
    assert list(parcels.columns) == ["id", "section", "numero", "geometry"]
    assert set(parcels.geometry.geom_type) == {"Polygon", "MultiPolygon"}
    assert parcels.crs is not None


def test_load_valid_gzipped_geojson(tmp_path: Path) -> None:
    plain_path = tmp_path / "parcels.geojson"
    gzip_path = tmp_path / OFFICIAL_FILENAME
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

    parcels = load_cadastre_parcels(_download(gzip_path)).parcels

    assert len(parcels) == 1
    assert parcels.iloc[0]["id"] == "parcel-1"


def test_empty_dataset_fails(tmp_path: Path) -> None:
    path = tmp_path / OFFICIAL_FILENAME
    _write_gzipped_geojson(path, [])

    with pytest.raises(EmptyCadastreDatasetError):
        load_cadastre_parcels(_download(path))


def test_missing_file_fails(tmp_path: Path) -> None:
    with pytest.raises(CadastreLoadError, match="exist"):
        load_cadastre_parcels(_download(tmp_path / OFFICIAL_FILENAME))


def test_invalid_file_fails(tmp_path: Path) -> None:
    path = tmp_path / OFFICIAL_FILENAME
    path.write_bytes(gzip.compress(b"not GeoJSON"))

    with pytest.raises(CadastreLoadError):
        load_cadastre_parcels(_download(path))


def test_missing_geometry_column_fails(tmp_path: Path) -> None:
    path = tmp_path / OFFICIAL_FILENAME
    path.write_bytes(gzip.compress(b"{" + b" " * 5 + b"}"))
    frame_without_geometry = gpd.GeoDataFrame({"id": ["parcel-1"]})

    with (
        patch(
            "landscout.sources.cadastre_loader_fr.gpd.read_file",
            return_value=frame_without_geometry,
        ),
        pytest.raises(MissingGeometryColumnError),
    ):
        load_cadastre_parcels(_download(path))


def test_noncanonical_active_geometry_name_fails_with_controlled_error(
    tmp_path: Path,
) -> None:
    path = tmp_path / OFFICIAL_FILENAME
    path.write_bytes(gzip.compress(b"{}"))
    frame = gpd.GeoDataFrame(
        {"id": ["parcel-1"], "shape": [gpd.points_from_xy([1], [43])[0]]},
        geometry="shape",
        crs="EPSG:4326",
    )

    with (
        patch(
            "landscout.sources.cadastre_loader_fr.gpd.read_file",
            return_value=frame,
        ),
        pytest.raises(MissingGeometryColumnError, match="canonical geometry"),
    ):
        load_cadastre_parcels(_download(path))


def test_unsupported_geometry_type_fails(tmp_path: Path) -> None:
    path = tmp_path / OFFICIAL_FILENAME
    _write_gzipped_geojson(
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
        load_cadastre_parcels(_download(path))


@pytest.mark.parametrize(
    "geometry",
    [
        {
            "type": "Polygon",
            "coordinates": [[[1, 43, 1], [2, 43, 1], [2, 44, 1], [1, 43, 1]]],
        },
        {
            "type": "MultiPolygon",
            "coordinates": [[[[1, 43, 1], [2, 43, 1], [2, 44, 1], [1, 43, 1]]]],
        },
    ],
)
def test_three_dimensional_cadastre_geometry_is_rejected(
    tmp_path: Path,
    geometry: dict[str, object],
) -> None:
    path = tmp_path / OFFICIAL_FILENAME
    _write_gzipped_geojson(
        path,
        [{"type": "Feature", "properties": {"id": "parcel"}, "geometry": geometry}],
    )

    with pytest.raises(UnsupportedGeometryTypeError, match="2D"):
        load_cadastre_parcels(_download(path))


@pytest.mark.parametrize(
    ("changes", "message"),
    [
        ({"sha256": "0" * 64}, "SHA|checksum"),
        ({"sha256": "A" * 64}, "SHA"),
        ({"sha256": "a" * 63}, "SHA"),
        ({"file_size": True}, "size"),
        ({"file_size": 0}, "size"),
        ({"filename": "other.json.gz"}, "filename"),
        ({"source_url": ""}, "URL"),
        ({"source_url": OFFICIAL_URL.replace("https://", "http://")}, "URL"),
        (
            {"source_url": OFFICIAL_URL.replace("cadastre.data.gouv.fr", "evil.test")},
            "URL",
        ),
        ({"commune_code": "31446"}, "URL|commune"),
    ],
)
def test_malformed_verified_download_is_rejected_before_parsing(
    tmp_path: Path,
    changes: dict[str, object],
    message: str,
) -> None:
    path = tmp_path / OFFICIAL_FILENAME
    _write_gzipped_geojson(path, [])

    with (
        patch(
            "landscout.sources.cadastre_loader_fr.gpd.read_file",
            side_effect=AssertionError("parser must not run"),
        ),
        pytest.raises(CadastreLoadError, match=message),
    ):
        load_cadastre_parcels(_download(path, **changes))


def test_wrong_public_input_type_is_controlled() -> None:
    with pytest.raises(CadastreLoadError, match="CadastreDownload"):
        load_cadastre_parcels(Path("untrusted.json.gz"))  # type: ignore[arg-type]


def test_physical_mutation_after_download_is_rejected_before_parsing(
    tmp_path: Path,
) -> None:
    path = tmp_path / OFFICIAL_FILENAME
    _write_gzipped_geojson(path, [])
    download = _download(path)
    content = bytearray(path.read_bytes())
    content[-1] ^= 1
    path.write_bytes(content)

    with (
        patch(
            "landscout.sources.cadastre_loader_fr.gpd.read_file",
            side_effect=AssertionError("parser must not run"),
        ),
        pytest.raises(CadastreLoadError, match="SHA|checksum|gzip"),
    ):
        load_cadastre_parcels(download)


def test_physical_change_during_read_is_rejected_by_post_read_verification(
    tmp_path: Path,
) -> None:
    path = tmp_path / OFFICIAL_FILENAME
    _write_gzipped_geojson(
        path,
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
    download = _download(path)
    original_read = gpd.read_file

    def mutate_after_read(*args: object, **kwargs: object) -> gpd.GeoDataFrame:
        frame = original_read(*args, **kwargs)
        path.write_bytes(gzip.compress(b'{"type":"FeatureCollection","features":[]}'))
        return frame

    with (
        patch(
            "landscout.sources.cadastre_loader_fr.gpd.read_file",
            side_effect=mutate_after_read,
        ),
        pytest.raises(CadastreLoadError, match="changed|SHA|size"),
    ):
        load_cadastre_parcels(download)


def test_supplied_cadastre_frame_mutation_is_rejected_by_fresh_reread(
    tmp_path: Path,
) -> None:
    path = tmp_path / OFFICIAL_FILENAME
    _write_gzipped_geojson(
        path,
        [
            {
                "type": "Feature",
                "properties": {"id": "313950000A0001"},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[1, 43], [2, 43], [2, 44], [1, 43]]],
                },
            }
        ],
    )
    source = load_cadastre_parcels(_download(path))
    source.parcels.loc[0, "id"] = "FORGED"

    with pytest.raises(CadastreLoadError, match="freshly read"):
        revalidate_cadastre_parcel_source(source)

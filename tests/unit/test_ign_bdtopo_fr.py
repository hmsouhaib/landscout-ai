import io
import json
from datetime import UTC, datetime, timedelta
from hashlib import sha256
from pathlib import Path
from unittest.mock import patch
from urllib.error import HTTPError

import geopandas as gpd
import py7zr
import pyogrio
import pytest
import yaml
from geopandas.testing import assert_geodataframe_equal
from pydantic import ValidationError
from shapely.geometry import LineString, MultiLineString, MultiPolygon, Polygon

from landscout import sources
from landscout.sources import ign_bdtopo_fr
from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_layer,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)

PROJECT_ROOT = Path(__file__).parents[2]
CONFIG_PATH = PROJECT_ROOT / "configs/sources/ign_bdtopo_fr.yaml"
SYNTHETIC_SOURCE_URL = "https://example.test/BDTOPO_TEST_D031.7z"
LINE_LAYER = "LIGNE_ELECTRIQUE"
POST_LAYER = "POSTE_DE_TRANSFORMATION"
DEPARTMENT_LAYER = "DEPARTEMENT"
ROAD_LAYER = "TRONCON_DE_ROUTE"


def _config_data() -> dict:
    with CONFIG_PATH.open(encoding="utf-8") as stream:
        return yaml.safe_load(stream)


def _synthetic_config(
    source_config: IgnBdTopoSourceConfig,
    *,
    official_checksum: str | None = None,
) -> IgnBdTopoSourceConfig:
    content = source_config.model_dump(mode="json")
    content.update(
        {
            "source_url": SYNTHETIC_SOURCE_URL,
            "checksum_url": None,
            "official_checksum_algorithm": (
                "sha256" if official_checksum is not None else None
            ),
            "official_checksum": official_checksum,
            "expected_archive_size_bytes": None,
        }
    )
    return IgnBdTopoSourceConfig.model_validate(content)


def _write_gpkg(
    path: Path,
    *,
    include_lines: bool = True,
    include_posts: bool = True,
    line_layer: str = LINE_LAYER,
    post_layer: str = POST_LAYER,
    crs: str | None = "EPSG:2154",
    invalid_post: bool = False,
    include_department: bool = False,
    department_layer: str = DEPARTMENT_LAYER,
    department_codes: list[str] | None = None,
    department_geometries: list[object] | None = None,
    include_roads: bool = False,
    road_layer: str = ROAD_LAYER,
    road_crs: str | None = None,
    road_geometry_kind: str = "mixed",
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    layer_written = False
    if include_lines:
        lines = gpd.GeoDataFrame(
            {
                "object_id": ["L_VALID", "L_NULL"],
                "nature": ["HT", "UNKNOWN"],
                "tension": ["225 kV", None],
            },
            geometry=[LineString([(0, 0), (100, 100)]), None],
            crs=crs,
        )
        pyogrio.write_dataframe(
            lines,
            path,
            layer=line_layer,
            driver="GPKG",
        )
        layer_written = True
    if include_posts:
        invalid = Polygon([(0, 0), (20, 20), (20, 0), (0, 20), (0, 0)])
        geometries = [
            Polygon([(0, 0), (0, 20), (20, 20), (20, 0), (0, 0)]),
            None,
        ]
        object_ids = ["P_VALID", "P_NULL"]
        if invalid_post:
            geometries.append(invalid)
            object_ids.append("P_INVALID")
        posts = gpd.GeoDataFrame(
            {
                "object_id": object_ids,
                "nature": ["POSTE"] * len(object_ids),
            },
            geometry=geometries,
            crs=crs,
        )
        pyogrio.write_dataframe(
            posts,
            path,
            layer=post_layer,
            driver="GPKG",
            append=layer_written,
        )
        layer_written = True
    if include_roads:
        if road_geometry_kind == "line":
            road_geometries = [
                LineString([(0, 0), (100, 100)]),
                LineString([(200, 200), (300, 260)]),
            ]
        elif road_geometry_kind == "multiline":
            road_geometries = [
                MultiLineString([[(0, 0), (100, 100)]]),
                MultiLineString(
                    [
                        [(200, 200), (250, 250)],
                        [(250, 250), (300, 260)],
                    ]
                ),
            ]
        else:
            road_geometries = [
                LineString([(0, 0), (100, 100)]),
                MultiLineString(
                    [
                        [(200, 200), (250, 250)],
                        [(250, 250), (300, 260)],
                    ]
                ),
            ]
        roads = gpd.GeoDataFrame(
            {
                "object_id": ["R_LINE", "R_MULTI"],
                "nature": ["Route à 1 chaussée", "Bretelle"],
            },
            geometry=road_geometries,
            crs=road_crs or crs,
        )
        pyogrio.write_dataframe(
            roads,
            path,
            layer=road_layer,
            driver="GPKG",
            append=layer_written,
        )
        layer_written = True
    if include_department:
        codes = department_codes or ["31", "32"]
        geometries = department_geometries or [
            MultiPolygon(
                [Polygon([(0, 0), (0, 1000), (1000, 1000), (1000, 0), (0, 0)])]
            ),
            MultiPolygon(
                [
                    Polygon(
                        [
                            (1000, 0),
                            (1000, 1000),
                            (2000, 1000),
                            (2000, 0),
                            (1000, 0),
                        ]
                    )
                ]
            ),
        ][: len(codes)]
        departments = gpd.GeoDataFrame(
            {
                "code_insee": codes,
                "nom_officiel": [f"Department {code}" for code in codes],
            },
            geometry=geometries,
            crs=crs,
        )
        pyogrio.write_dataframe(
            departments,
            path,
            layer=department_layer,
            driver="GPKG",
            append=layer_written,
        )


def _pack_7z(
    archive_path: Path,
    members: list[tuple[Path, str]],
) -> bytes:
    archive_path.parent.mkdir(parents=True, exist_ok=True)
    with py7zr.SevenZipFile(archive_path, "w") as archive:
        for source, archive_name in members:
            archive.write(source, arcname=archive_name)
    return archive_path.read_bytes()


def _synthetic_archive_bytes(
    root: Path,
    *,
    include_lines: bool = True,
    include_posts: bool = True,
    invalid_post: bool = False,
    include_department: bool = False,
    include_roads: bool = False,
    road_crs: str | None = None,
    road_geometry_kind: str = "mixed",
) -> bytes:
    gpkg_path = root / "fixture" / "BDTOPO_TEST.gpkg"
    _write_gpkg(
        gpkg_path,
        include_lines=include_lines,
        include_posts=include_posts,
        invalid_post=invalid_post,
        include_department=include_department,
        include_roads=include_roads,
        road_crs=road_crs,
        road_geometry_kind=road_geometry_kind,
    )
    return _pack_7z(
        root / "fixture.7z",
        [(gpkg_path, "BDTOPO_TEST/GPKG/BDTOPO_TEST.gpkg")],
    )


def _response(content: bytes) -> io.BytesIO:
    return io.BytesIO(content)


def _metadata_path(archive_path: Path) -> Path:
    return archive_path.parent / f"{archive_path.name}.metadata.json"


def _extraction_metadata_path(extraction_path: Path) -> Path:
    return extraction_path / ".landscout-extraction.json"


def _extracted_fixture(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    *,
    include_roads: bool = False,
) -> tuple[IgnBdTopoSourceConfig, IgnBdTopoDownload, IgnBdTopoExtraction]:
    archive_content = _synthetic_archive_bytes(
        tmp_path / "source",
        include_roads=include_roads,
    )
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=tmp_path / "extracted",
    )
    return config, download, extraction


def _expire_cache(metadata_path: Path) -> bytes:
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    metadata["download_timestamp"] = (
        datetime.now(UTC) - timedelta(days=365)
    ).isoformat()
    metadata_path.write_text(json.dumps(metadata), encoding="utf-8")
    return metadata_path.read_bytes()


@pytest.fixture
def source_config() -> IgnBdTopoSourceConfig:
    return load_ign_bdtopo_source_config(CONFIG_PATH)


def test_valid_source_config_loads(source_config: IgnBdTopoSourceConfig) -> None:
    assert "IGN" in source_config.provider
    assert source_config.department_code == "31"
    assert source_config.projection == "EPSG:2154"
    assert source_config.format == "GPKG"
    assert source_config.edition == "2026-06-15"
    assert source_config.access.road_segments.class_label == "Tronçon de route"
    assert source_config.access.road_segments.match_tokens == ("tronçon", "route")
    assert source_config.coverage.department_layer.match_tokens == ("departement",)
    assert (
        source_config.coverage.department_layer.department_code_field
        == "code_insee"
    )


@pytest.mark.parametrize("mutation", ["missing", "blank_field", "empty_tokens"])
def test_invalid_department_coverage_config_fails(mutation: str) -> None:
    content = _config_data()
    if mutation == "missing":
        del content["coverage"]
    elif mutation == "blank_field":
        content["coverage"]["department_layer"]["department_code_field"] = " "
    else:
        content["coverage"]["department_layer"]["match_tokens"] = []

    with pytest.raises(ValidationError):
        IgnBdTopoSourceConfig.model_validate(content)


@pytest.mark.parametrize("field", ["source_url", "edition"])
def test_missing_required_source_field_fails(field: str) -> None:
    content = _config_data()
    del content[field]

    with pytest.raises(ValidationError):
        IgnBdTopoSourceConfig.model_validate(content)


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("department_code", "3"),
        ("department_code", "XX"),
        ("projection", "EPSG:4326"),
        ("format", "SHP"),
        ("archive_format", "zip"),
    ],
)
def test_invalid_source_configuration_fails(field: str, value: str) -> None:
    content = _config_data()
    content[field] = value

    with pytest.raises(ValidationError):
        IgnBdTopoSourceConfig.model_validate(content)


def test_unknown_source_config_field_is_rejected() -> None:
    content = _config_data()
    content["invented"] = "not allowed"

    with pytest.raises(ValidationError):
        IgnBdTopoSourceConfig.model_validate(content)


def test_successful_archive_download_persists_sha256(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(tmp_path)
    config = _synthetic_config(source_config)

    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        result = download_ign_bdtopo_archive(config, tmp_path / "cache")

    assert result.cache_hit is False
    assert result.path.read_bytes() == archive_content
    assert result.file_size == len(archive_content)
    assert result.sha256 == sha256(archive_content).hexdigest()
    metadata = json.loads(_metadata_path(result.path).read_text(encoding="utf-8"))
    assert metadata["sha256"] == result.sha256
    assert metadata["source_url"] == SYNTHETIC_SOURCE_URL
    assert metadata["official_checksum"] is None


def test_archive_integrity_reports_local_sha256_and_no_fabricated_checksum(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_path = tmp_path / "fixture.7z"
    archive_content = _synthetic_archive_bytes(tmp_path / "source")
    archive_path.write_bytes(archive_content)

    integrity = validate_ign_bdtopo_archive(
        archive_path,
        _synthetic_config(source_config),
    )

    assert integrity.file_size == len(archive_content)
    assert integrity.sha256 == sha256(archive_content).hexdigest()
    assert integrity.official_checksum is None
    assert integrity.official_checksum_algorithm is None
    assert integrity.official_checksum_validated is False


def test_fresh_cache_is_reused_without_network(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    content = _synthetic_archive_bytes(tmp_path)
    config = _synthetic_config(source_config)
    cache_dir = tmp_path / "cache"
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https", return_value=_response(content)
    ):
        first = download_ign_bdtopo_archive(config, cache_dir)

    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        side_effect=AssertionError("network must not be called"),
    ):
        second = download_ign_bdtopo_archive(config, cache_dir)

    assert second.cache_hit is True
    assert second.path == first.path
    assert second.sha256 == first.sha256
    assert second.download_timestamp == first.download_timestamp


def test_stale_recovery_backup_rejects_cache_before_network(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    content = _synthetic_archive_bytes(tmp_path)
    config = _synthetic_config(source_config)
    cache_dir = tmp_path / "cache"
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(content),
    ):
        first = download_ign_bdtopo_archive(config, cache_dir)
    recovery_path = first.path.with_name(f"{first.path.name}.bak")
    recovery_bytes = b"manual IGN recovery material"
    recovery_path.write_bytes(recovery_bytes)

    with (
        patch(
            "landscout.sources.ign_bdtopo_fr.open_safe_https",
            side_effect=AssertionError("stale recovery must fail before network"),
        ) as opener,
        pytest.raises(IgnBdTopoDownloadError, match="backup|recovery|manual"),
    ):
        download_ign_bdtopo_archive(config, cache_dir)

    opener.assert_not_called()
    assert recovery_path.read_bytes() == recovery_bytes
    assert first.path.read_bytes() == content


def test_expired_cache_is_refreshed(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    old_content = _synthetic_archive_bytes(tmp_path / "v1")
    new_content = _synthetic_archive_bytes(tmp_path / "v2", invalid_post=True)
    config = _synthetic_config(source_config)
    cache_dir = tmp_path / "cache"
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(old_content),
    ):
        first = download_ign_bdtopo_archive(config, cache_dir)
    _expire_cache(_metadata_path(first.path))

    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(new_content),
    ) as opener:
        refreshed = download_ign_bdtopo_archive(config, cache_dir)

    assert opener.call_count == 1
    assert refreshed.cache_hit is False
    assert refreshed.path.read_bytes() == new_content
    assert refreshed.sha256 != first.sha256
    assert not list(cache_dir.glob("*.part"))
    assert not list(cache_dir.glob("*.bak"))


def test_failed_refresh_preserves_valid_cache(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    content = _synthetic_archive_bytes(tmp_path)
    config = _synthetic_config(source_config)
    cache_dir = tmp_path / "cache"
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https", return_value=_response(content)
    ):
        first = download_ign_bdtopo_archive(config, cache_dir)
    metadata_path = _metadata_path(first.path)
    old_archive = first.path.read_bytes()
    expired_metadata = _expire_cache(metadata_path)
    error = HTTPError(SYNTHETIC_SOURCE_URL, 503, "Unavailable", None, None)

    with (
        patch("landscout.sources.ign_bdtopo_fr.open_safe_https", side_effect=error),
        pytest.raises(IgnBdTopoDownloadError),
    ):
        download_ign_bdtopo_archive(config, cache_dir)

    assert first.path.read_bytes() == old_archive
    assert metadata_path.read_bytes() == expired_metadata
    assert not list(cache_dir.glob("*.part"))
    assert not list(cache_dir.glob("*.bak"))


def test_corrupt_new_archive_is_rejected_and_temporary_files_are_cleaned(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    config = _synthetic_config(source_config)
    cache_dir = tmp_path / "cache"
    with (
        patch(
            "landscout.sources.ign_bdtopo_fr.open_safe_https",
            return_value=_response(b"not a 7z archive"),
        ),
        pytest.raises(IgnBdTopoArchiveError),
    ):
        download_ign_bdtopo_archive(config, cache_dir)

    assert not list(cache_dir.glob("*.7z"))
    assert not list(cache_dir.glob("*.part"))
    assert not list(cache_dir.glob("*.bak"))


def test_corrupt_refresh_preserves_valid_cache(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    content = _synthetic_archive_bytes(tmp_path)
    config = _synthetic_config(source_config)
    cache_dir = tmp_path / "cache"
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https", return_value=_response(content)
    ):
        first = download_ign_bdtopo_archive(config, cache_dir)
    metadata_path = _metadata_path(first.path)
    old_archive = first.path.read_bytes()
    expired_metadata = _expire_cache(metadata_path)

    with (
        patch(
            "landscout.sources.ign_bdtopo_fr.open_safe_https",
            return_value=_response(b"broken refresh"),
        ),
        pytest.raises(IgnBdTopoArchiveError),
    ):
        download_ign_bdtopo_archive(config, cache_dir)

    assert first.path.read_bytes() == old_archive
    assert metadata_path.read_bytes() == expired_metadata
    assert not list(cache_dir.glob("*.part"))


def test_metadata_publication_failure_restores_previous_cache_pair(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    old_content = _synthetic_archive_bytes(tmp_path / "v1")
    new_content = _synthetic_archive_bytes(tmp_path / "v2", invalid_post=True)
    config = _synthetic_config(source_config)
    cache_dir = tmp_path / "cache"
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(old_content),
    ):
        first = download_ign_bdtopo_archive(config, cache_dir)
    metadata_path = _metadata_path(first.path)
    old_archive = first.path.read_bytes()
    expired_metadata = _expire_cache(metadata_path)
    original_replace = ign_bdtopo_fr._replace_file
    failure_injected = False

    def fail_metadata_publication(source: Path, target: Path) -> None:
        nonlocal failure_injected
        if source.name.endswith(".metadata.json.part") and target == metadata_path:
            failure_injected = True
            raise PermissionError("simulated persistent metadata lock")
        original_replace(source, target)

    with (
        patch(
            "landscout.sources.ign_bdtopo_fr.open_safe_https",
            return_value=_response(new_content),
        ),
        patch.object(
            ign_bdtopo_fr,
            "_replace_file",
            side_effect=fail_metadata_publication,
        ),
        pytest.raises(IgnBdTopoDownloadError),
    ):
        download_ign_bdtopo_archive(config, cache_dir)

    assert failure_injected
    assert first.path.read_bytes() == old_archive
    assert metadata_path.read_bytes() == expired_metadata
    assert not list(cache_dir.glob("*.part"))
    assert not list(cache_dir.glob("*.bak"))


def test_publication_and_rollback_failure_preserves_exact_recovery_backups(
    tmp_path: Path,
) -> None:
    archive_path = tmp_path / "cached.7z"
    metadata_path = tmp_path / "cached.7z.metadata.json"
    temporary_archive = tmp_path / "cached.7z.part"
    temporary_metadata = tmp_path / "cached.7z.metadata.json.part"
    old_archive = b"exact old archive"
    old_metadata = b"exact old metadata"
    archive_path.write_bytes(old_archive)
    metadata_path.write_bytes(old_metadata)
    temporary_archive.write_bytes(b"replacement archive")
    temporary_metadata.write_bytes(b"replacement metadata")
    archive_backup = archive_path.with_name(f"{archive_path.name}.bak")
    metadata_backup = metadata_path.with_name(f"{metadata_path.name}.bak")
    original_replace = ign_bdtopo_fr._replace_file

    def fail_publication_and_rollback(source: Path, target: Path) -> None:
        if source == temporary_metadata and target == metadata_path:
            raise OSError("simulated metadata publication failure")
        if source == archive_backup and target == archive_path:
            raise OSError("simulated archive rollback failure")
        original_replace(source, target)

    with (
        patch.object(
            ign_bdtopo_fr,
            "_replace_file",
            side_effect=fail_publication_and_rollback,
        ),
        pytest.raises(IgnBdTopoDownloadError, match="rollback"),
    ):
        ign_bdtopo_fr._publish_cache_pair(
            temporary_archive,
            temporary_metadata,
            archive_path,
            metadata_path,
        )

    assert archive_backup.read_bytes() == old_archive
    assert metadata_backup.read_bytes() == old_metadata


def test_cleanup_failure_does_not_mask_double_failure_recovery_error(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    old_content = _synthetic_archive_bytes(tmp_path / "v1")
    new_content = _synthetic_archive_bytes(tmp_path / "v2", invalid_post=True)
    config = _synthetic_config(source_config)
    cache_dir = tmp_path / "cache"
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(old_content),
    ):
        first = download_ign_bdtopo_archive(config, cache_dir)
    metadata_path = _metadata_path(first.path)
    old_archive = first.path.read_bytes()
    old_metadata = _expire_cache(metadata_path)
    temporary_metadata = metadata_path.with_name(f"{metadata_path.name}.part")
    archive_backup = first.path.with_name(f"{first.path.name}.bak")
    metadata_backup = metadata_path.with_name(f"{metadata_path.name}.bak")
    original_replace = ign_bdtopo_fr._replace_file
    original_unlink = Path.unlink
    rollback_failed = False

    def fail_publication_and_rollback(source: Path, target: Path) -> None:
        nonlocal rollback_failed
        if source == temporary_metadata and target == metadata_path:
            raise OSError("simulated metadata publication failure")
        if source == archive_backup and target == first.path:
            rollback_failed = True
            raise OSError("simulated archive rollback failure")
        original_replace(source, target)

    def fail_temporary_cleanup(path: Path, *, missing_ok: bool = False) -> None:
        if rollback_failed and path == temporary_metadata:
            raise PermissionError("simulated temporary cleanup failure")
        original_unlink(path, missing_ok=missing_ok)

    with (
        patch(
            "landscout.sources.ign_bdtopo_fr.open_safe_https",
            return_value=_response(new_content),
        ),
        patch.object(
            ign_bdtopo_fr,
            "_replace_file",
            side_effect=fail_publication_and_rollback,
        ),
        patch.object(Path, "unlink", new=fail_temporary_cleanup),
        pytest.raises(IgnBdTopoDownloadError, match="rollback"),
    ):
        download_ign_bdtopo_archive(config, cache_dir)

    assert archive_backup.read_bytes() == old_archive
    assert metadata_backup.read_bytes() == old_metadata


def test_stale_cache_recovery_backup_fails_closed_without_destroying_it(
    tmp_path: Path,
) -> None:
    archive_path = tmp_path / "cached.7z"
    metadata_path = tmp_path / "cached.7z.metadata.json"
    temporary_archive = tmp_path / "cached.7z.part"
    temporary_metadata = tmp_path / "cached.7z.metadata.json.part"
    archive_backup = tmp_path / "cached.7z.bak"
    archive_path.write_bytes(b"old archive")
    metadata_path.write_bytes(b"old metadata")
    temporary_archive.write_bytes(b"new archive")
    temporary_metadata.write_bytes(b"new metadata")
    archive_backup.write_bytes(b"manual recovery archive")

    with pytest.raises(IgnBdTopoDownloadError, match="backup|recovery|manual"):
        ign_bdtopo_fr._publish_cache_pair(
            temporary_archive,
            temporary_metadata,
            archive_path,
            metadata_path,
        )

    assert archive_path.read_bytes() == b"old archive"
    assert metadata_path.read_bytes() == b"old metadata"
    assert archive_backup.read_bytes() == b"manual recovery archive"


def test_official_checksum_mismatch_is_rejected(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(tmp_path)
    config = _synthetic_config(source_config, official_checksum="0" * 64)
    cache_dir = tmp_path / "cache"

    with (
        patch(
            "landscout.sources.ign_bdtopo_fr.open_safe_https",
            return_value=_response(archive_content),
        ),
        pytest.raises(IgnBdTopoArchiveError, match="checksum|SHA"),
    ):
        download_ign_bdtopo_archive(config, cache_dir)

    assert not list(cache_dir.glob("*.7z"))
    assert not list(cache_dir.glob("*.part"))


def test_unsafe_parent_archive_member_is_rejected(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    gpkg_path = tmp_path / "unsafe-source.gpkg"
    _write_gpkg(gpkg_path)
    archive_content = _pack_7z(
        tmp_path / "unsafe.7z",
        [(gpkg_path, "../escape.gpkg")],
    )
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")

    with pytest.raises(IgnBdTopoArchiveError, match="unsafe|member|path"):
        extract_ign_bdtopo_archive(
            download,
            config,
            extraction_dir=tmp_path / "extracted",
        )

    assert not (tmp_path / "escape.gpkg").exists()
    assert not list(tmp_path.glob("*.part"))


def test_geopackage_is_discovered_recursively(tmp_path: Path) -> None:
    gpkg_path = tmp_path / "nested" / "data" / "bdtopo.gpkg"
    _write_gpkg(gpkg_path)

    assert discover_ign_bdtopo_geopackage(tmp_path) == gpkg_path


def test_multiple_geopackages_are_rejected_as_ambiguous(tmp_path: Path) -> None:
    _write_gpkg(tmp_path / "a" / "one.gpkg")
    _write_gpkg(tmp_path / "b" / "two.gpkg")

    with pytest.raises(IgnBdTopoArchiveError, match="GeoPackage|exactly one|ambiguous"):
        discover_ign_bdtopo_geopackage(tmp_path)


def test_real_layer_names_are_listed_and_discovered(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    gpkg_path = tmp_path / "bdtopo.gpkg"
    _write_gpkg(gpkg_path)

    all_layers = list_ign_bdtopo_layers(gpkg_path)
    selection = discover_ign_bdtopo_layers(gpkg_path, source_config)

    assert set(all_layers) == {LINE_LAYER, POST_LAYER}
    assert selection.electric_lines_layer == LINE_LAYER
    assert selection.transformation_posts_layer == POST_LAYER
    assert set(selection.all_layer_names) == {LINE_LAYER, POST_LAYER}


def test_missing_electric_line_layer_fails(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    gpkg_path = tmp_path / "posts-only.gpkg"
    _write_gpkg(gpkg_path, include_lines=False)

    with pytest.raises(IgnBdTopoLayerError, match="electric|line|Ligne"):
        discover_ign_bdtopo_layers(gpkg_path, source_config)


def test_missing_transformation_post_layer_fails(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    gpkg_path = tmp_path / "lines-only.gpkg"
    _write_gpkg(gpkg_path, include_posts=False)

    with pytest.raises(IgnBdTopoLayerError, match="transformation|post|Poste"):
        discover_ign_bdtopo_layers(gpkg_path, source_config)


def test_ambiguous_electric_line_layers_fail(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    gpkg_path = tmp_path / "ambiguous-lines.gpkg"
    _write_gpkg(gpkg_path)
    secondary_lines = gpd.GeoDataFrame(
        {"object_id": ["L_SECONDARY"]},
        geometry=[LineString([(0, 0), (50, 50)])],
        crs="EPSG:2154",
    )
    pyogrio.write_dataframe(
        secondary_lines,
        gpkg_path,
        layer="LIGNE_ELECTRIQUE_SECONDAIRE",
        driver="GPKG",
        append=True,
    )

    with pytest.raises(IgnBdTopoLayerError, match="unambiguous|found 2"):
        discover_ign_bdtopo_layers(gpkg_path, source_config)


def test_synthetic_archive_extracts_and_discovers_required_layers(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(tmp_path / "source")
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")

    extraction = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=tmp_path / "extracted",
    )

    assert extraction.geopackage_path.is_file()
    assert extraction.electric_lines_layer == LINE_LAYER
    assert extraction.transformation_posts_layer == POST_LAYER


def test_schema_v2_extraction_metadata_binds_physical_geopackage(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    config, download, extraction = _extracted_fixture(tmp_path, source_config)
    metadata = json.loads(
        _extraction_metadata_path(extraction.extraction_path).read_text(
            encoding="utf-8"
        )
    )

    assert metadata["schema_version"] == 2
    assert metadata["geopackage_size_bytes"] == extraction.geopackage_path.stat().st_size
    assert metadata["geopackage_sha256"] == sha256(
        extraction.geopackage_path.read_bytes()
    ).hexdigest()
    assert extraction.geopackage_size_bytes == metadata["geopackage_size_bytes"]
    assert extraction.geopackage_sha256 == metadata["geopackage_sha256"]

    cached = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=extraction.extraction_path,
    )
    assert cached.cache_hit is True
    assert cached.geopackage_size_bytes == metadata["geopackage_size_bytes"]
    assert cached.geopackage_sha256 == metadata["geopackage_sha256"]


def test_same_size_geopackage_tamper_invalidates_extraction_cache(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    config, download, extraction = _extracted_fixture(tmp_path, source_config)
    original = extraction.geopackage_path.read_bytes()
    tampered = bytearray(original)
    tampered[-1] ^= 1
    extraction.geopackage_path.write_bytes(tampered)
    assert extraction.geopackage_path.stat().st_size == len(original)

    rebuilt = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=extraction.extraction_path,
    )

    assert rebuilt.cache_hit is False
    assert rebuilt.geopackage_path.read_bytes() == original


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("geopackage_sha256", "0" * 64),
        ("geopackage_size_bytes", 1),
        ("schema_version", 1),
        ("geopackage_relative_path", "../escape.gpkg"),
    ],
)
def test_forged_extraction_metadata_never_returns_cache_hit(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    field: str,
    value: object,
) -> None:
    config, download, extraction = _extracted_fixture(tmp_path, source_config)
    metadata_path = _extraction_metadata_path(extraction.extraction_path)
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    metadata[field] = value
    metadata_path.write_text(json.dumps(metadata), encoding="utf-8")

    rebuilt = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=extraction.extraction_path,
    )

    assert rebuilt.cache_hit is False


@pytest.mark.parametrize(
    "value",
    ["", "abc", "A" * 64, "a" * 63, "a" * 65],
)
def test_malformed_geopackage_sha_is_not_trusted(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    value: str,
) -> None:
    config, download, extraction = _extracted_fixture(tmp_path, source_config)
    metadata_path = _extraction_metadata_path(extraction.extraction_path)
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    metadata["geopackage_sha256"] = value
    metadata_path.write_text(json.dumps(metadata), encoding="utf-8")

    rebuilt = extract_ign_bdtopo_archive(
        download, config, extraction_dir=extraction.extraction_path
    )

    assert rebuilt.cache_hit is False


@pytest.mark.parametrize("value", [0, -1, True, "100"])
def test_malformed_geopackage_size_is_not_trusted(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    value: object,
) -> None:
    config, download, extraction = _extracted_fixture(tmp_path, source_config)
    metadata_path = _extraction_metadata_path(extraction.extraction_path)
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    metadata["geopackage_size_bytes"] = value
    metadata_path.write_text(json.dumps(metadata), encoding="utf-8")

    rebuilt = extract_ign_bdtopo_archive(
        download, config, extraction_dir=extraction.extraction_path
    )

    assert rebuilt.cache_hit is False


def test_default_extraction_path_is_short_and_content_addressed(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(tmp_path / "source")
    config = _synthetic_config(source_config)
    cache_dir = tmp_path / "cache"
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, cache_dir)

    extraction = extract_ign_bdtopo_archive(download, config)

    assert extraction.extraction_path == cache_dir / "x" / download.sha256[:16]
    assert len(extraction.extraction_path.name) == 16
    assert extraction.geopackage_path.is_file()


def test_layer_loader_retains_crs_counts_and_null_geometries(tmp_path: Path) -> None:
    gpkg_path = tmp_path / "bdtopo.gpkg"
    _write_gpkg(gpkg_path)

    loaded = load_ign_bdtopo_layer(
        gpkg_path,
        LINE_LAYER,
        "electric_lines",
    )
    frame = loaded.data
    summary = loaded.summary

    assert frame.crs is not None
    assert frame.crs.to_epsg() == 2154
    assert len(frame) == 2
    assert frame["object_id"].tolist() == ["L_VALID", "L_NULL"]
    assert frame.geometry.isna().sum() == 1
    assert summary.feature_count == 2
    assert summary.null_geometry_count == 1
    assert summary.invalid_geometry_count == 0


def test_invalid_geometry_is_preserved_without_repair(tmp_path: Path) -> None:
    gpkg_path = tmp_path / "bdtopo.gpkg"
    _write_gpkg(gpkg_path, invalid_post=True)

    loaded = load_ign_bdtopo_layer(
        gpkg_path,
        POST_LAYER,
        "transformation_posts",
    )
    frame = loaded.data
    summary = loaded.summary

    invalid_row = frame.loc[frame["object_id"] == "P_INVALID"].iloc[0]
    assert len(frame) == 3
    assert invalid_row.geometry.is_valid is False
    assert summary.feature_count == 3
    assert summary.null_geometry_count == 1
    assert summary.invalid_geometry_count == 1


def test_geographic_crs_is_rejected(tmp_path: Path) -> None:
    gpkg_path = tmp_path / "geographic.gpkg"
    _write_gpkg(gpkg_path, include_posts=False, crs="EPSG:4326")

    with pytest.raises(IgnBdTopoLayerError, match="2154|Lambert|projected|CRS"):
        load_ign_bdtopo_layer(gpkg_path, LINE_LAYER, "electric_lines")


def test_electricity_loader_retains_both_layer_counts(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(
        tmp_path / "source", invalid_post=True
    )
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=tmp_path / "extracted",
    )

    electricity = load_ign_bdtopo_electricity(extraction, config)

    assert len(electricity.electric_lines) == 2
    assert len(electricity.transformation_posts) == 3
    assert electricity.electric_lines.crs.to_epsg() == 2154
    assert electricity.transformation_posts.crs.to_epsg() == 2154
    assert electricity.transformation_posts_summary.invalid_geometry_count == 1


def test_road_layer_discovery_loads_selected_physical_layer(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(tmp_path / "source", include_roads=True)
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download, config, extraction_dir=tmp_path / "extracted"
    )

    loaded = ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, config)

    assert loaded.extraction is extraction
    assert loaded.road_segments_summary.source_layer_name == ROAD_LAYER
    assert loaded.road_segments_summary.logical_name == "road_segments"
    assert loaded.road_segments["object_id"].tolist() == ["R_LINE", "R_MULTI"]
    assert loaded.road_segments_summary.spatial_role == "PROXY_GEOMETRY"


@pytest.mark.parametrize(
    "role",
    ["electric_lines", "transformation_posts"],
)
def test_road_physical_layer_cannot_collide_with_electricity_roles(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    role: str,
) -> None:
    config, _, extraction = _extracted_fixture(
        tmp_path,
        source_config,
        include_roads=True,
    )
    content = config.model_dump(mode="json")
    selected = content["logical_layers"][role]
    content["access"]["road_segments"] = selected
    colliding = IgnBdTopoSourceConfig.model_validate(content)

    with pytest.raises(IgnBdTopoLayerError, match="same layer|collid|role"):
        ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, colliding)


def test_missing_road_layer_fails_safely(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(tmp_path / "source")
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download, config, extraction_dir=tmp_path / "extracted"
    )

    with pytest.raises(IgnBdTopoLayerError, match="road|route|found 0"):
        ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, config)


def test_ambiguous_road_layer_fails_safely(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    gpkg_path = tmp_path / "source" / "ambiguous-roads.gpkg"
    _write_gpkg(gpkg_path, include_roads=True)
    secondary = gpd.GeoDataFrame(
        {"object_id": ["R_SECONDARY"]},
        geometry=[LineString([(0, 0), (10, 10)])],
        crs="EPSG:2154",
    )
    pyogrio.write_dataframe(
        secondary,
        gpkg_path,
        layer="TRONCON_DE_ROUTE_SECONDAIRE",
        driver="GPKG",
        append=True,
    )
    archive_content = _pack_7z(
        tmp_path / "ambiguous-roads.7z",
        [(gpkg_path, "PACKAGE/ambiguous-roads.gpkg")],
    )
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download, config, extraction_dir=tmp_path / "extracted"
    )

    with pytest.raises(IgnBdTopoLayerError, match="road|route|found 2"):
        ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, config)


def test_road_loader_rejects_wrong_archive_config_department(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(tmp_path / "source", include_roads=True)
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download, config, extraction_dir=tmp_path / "extracted"
    )
    other_department = IgnBdTopoSourceConfig.model_validate(
        {**config.model_dump(mode="json"), "department_code": "32"}
    )

    with pytest.raises(IgnBdTopoLayerError, match="department|archive|lineage"):
        ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, other_department)


def test_road_loader_rejects_changed_layer_inventory(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(tmp_path / "source", include_roads=True)
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download, config, extraction_dir=tmp_path / "extracted"
    )
    added = gpd.GeoDataFrame(
        {"object_id": ["ADDED"]},
        geometry=[LineString([(0, 0), (1, 1)])],
        crs="EPSG:2154",
    )
    pyogrio.write_dataframe(
        added,
        extraction.geopackage_path,
        layer="ADDED_AFTER_EXTRACTION",
        driver="GPKG",
        append=True,
    )

    with pytest.raises(IgnBdTopoLayerError, match="inventory|changed"):
        ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, config)


def test_road_loader_rejects_geographic_crs(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(
        tmp_path / "source", include_roads=True, road_crs="EPSG:4326"
    )
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download, config, extraction_dir=tmp_path / "extracted"
    )

    with pytest.raises(IgnBdTopoLayerError, match="2154|Lambert|projected|CRS"):
        ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, config)


@pytest.mark.parametrize(
    ("road_geometry_kind", "expected_geometry_type"),
    [("line", "LineString"), ("multiline", "MultiLineString")],
)
def test_road_loader_preserves_lambert93_lines_unchanged(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    road_geometry_kind: str,
    expected_geometry_type: str,
) -> None:
    archive_content = _synthetic_archive_bytes(
        tmp_path / "source",
        include_roads=True,
        road_geometry_kind=road_geometry_kind,
    )
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download, config, extraction_dir=tmp_path / "extracted"
    )
    expected = gpd.read_file(
        extraction.geopackage_path, layer=ROAD_LAYER, engine="pyogrio"
    )

    loaded = ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, config)

    assert_geodataframe_equal(loaded.road_segments, expected, check_crs=True)
    assert loaded.road_segments.crs.to_epsg() == 2154
    assert loaded.road_segments_summary.geometry_types == (expected_geometry_type,)


def test_road_layer_does_not_change_electricity_loading_or_cache_shape(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(tmp_path / "source", include_roads=True)
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download, config, extraction_dir=tmp_path / "extracted"
    )

    electricity = load_ign_bdtopo_electricity(extraction, config)
    metadata = json.loads(
        (extraction.extraction_path / ".landscout-extraction.json").read_text(
            encoding="utf-8"
        )
    )

    assert len(electricity.electric_lines) == 2
    assert len(electricity.transformation_posts) == 2
    assert electricity.electric_lines_summary.source_layer_name == LINE_LAYER
    assert electricity.transformation_posts_summary.source_layer_name == POST_LAYER
    assert "road_segments_layer" not in metadata
    assert set(metadata) == {
        "schema_version",
        "archive_sha256",
        "geopackage_relative_path",
        "geopackage_size_bytes",
        "geopackage_sha256",
        "all_layer_names",
        "electric_lines_layer",
        "transformation_posts_layer",
        "spatial_role",
    }


def test_public_sources_export_only_stable_road_api() -> None:
    assert sources.IgnBdTopoRoadData is ign_bdtopo_fr.IgnBdTopoRoadData
    assert sources.load_ign_bdtopo_roads is ign_bdtopo_fr.load_ign_bdtopo_roads
    assert "IgnBdTopoRoadData" in sources.__all__
    assert "load_ign_bdtopo_roads" in sources.__all__
    assert not hasattr(sources, "_discover_road_layer")


def test_department_coverage_loader_selects_configured_identity(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(
        tmp_path / "source",
        include_department=True,
    )
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=tmp_path / "extracted",
    )

    loaded = load_ign_bdtopo_department_coverage(extraction, config)

    assert loaded.source_layer == DEPARTMENT_LAYER
    assert loaded.source_department_code == "31"
    assert loaded.spatial_role == "SOURCE_COVERAGE_BOUNDARY"
    assert len(loaded.coverage) == 1
    assert loaded.coverage.loc[0, "code_insee"] == "31"
    assert loaded.coverage.loc[0, "source_department_code"] == "31"
    assert loaded.coverage.loc[0, "source_archive_sha256"] == download.sha256
    assert loaded.coverage.loc[0, "spatial_role"] == "SOURCE_COVERAGE_BOUNDARY"
    assert loaded.coverage.crs.to_epsg() == 2154
    assert loaded.summary.source_feature_count == 2
    assert loaded.summary.selected_feature_count == 1
    assert loaded.summary.department_code_field == "code_insee"
    assert loaded.summary.geometry_types == ("MultiPolygon",)


@pytest.mark.parametrize(
    "department_codes",
    [["32"], ["31", "31"]],
    ids=["missing", "duplicate"],
)
def test_department_coverage_requires_one_authoritative_feature(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    department_codes: list[str],
) -> None:
    gpkg_path = tmp_path / "source" / "coverage.gpkg"
    geometries = [
        Polygon([(0, 0), (0, 100), (100, 100), (100, 0), (0, 0)])
        for _ in department_codes
    ]
    _write_gpkg(
        gpkg_path,
        include_department=True,
        department_codes=department_codes,
        department_geometries=geometries,
    )
    archive_content = _pack_7z(
        tmp_path / "coverage.7z",
        [(gpkg_path, "PACKAGE/coverage.gpkg")],
    )
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=tmp_path / "extracted",
    )

    with pytest.raises(IgnBdTopoLayerError, match="exactly one|found"):
        load_ign_bdtopo_department_coverage(extraction, config)


def test_department_coverage_requires_configured_identity_field(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(
        tmp_path / "source",
        include_department=True,
    )
    content = _synthetic_config(source_config).model_dump(mode="json")
    content["coverage"]["department_layer"]["department_code_field"] = (
        "missing_code"
    )
    config = IgnBdTopoSourceConfig.model_validate(content)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=tmp_path / "extracted",
    )

    with pytest.raises(IgnBdTopoLayerError, match="identity field|missing_code"):
        load_ign_bdtopo_department_coverage(extraction, config)


def test_missing_department_coverage_layer_fails(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(tmp_path / "source")
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=tmp_path / "extracted",
    )

    with pytest.raises(IgnBdTopoLayerError, match="department|found 0"):
        load_ign_bdtopo_department_coverage(extraction, config)


def test_department_coverage_layer_discovery_must_be_unambiguous(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    gpkg_path = tmp_path / "source" / "ambiguous.gpkg"
    _write_gpkg(gpkg_path, include_department=True)
    second = gpd.GeoDataFrame(
        {"code_insee": ["31"]},
        geometry=[Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])],
        crs="EPSG:2154",
    )
    pyogrio.write_dataframe(
        second,
        gpkg_path,
        layer="DEPARTEMENT_SECONDAIRE",
        driver="GPKG",
        append=True,
    )
    archive_content = _pack_7z(
        tmp_path / "ambiguous.7z",
        [(gpkg_path, "PACKAGE/ambiguous.gpkg")],
    )
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=tmp_path / "extracted",
    )

    with pytest.raises(IgnBdTopoLayerError, match="unambiguous|found 2"):
        load_ign_bdtopo_department_coverage(extraction, config)


@pytest.mark.parametrize(
    ("consumer", "layer", "old_bytes", "new_bytes"),
    [
        ("electricity", LINE_LAYER, b"HT", b"HX"),
        ("roads", ROAD_LAYER, b"Bretelle", b"BretellX"),
        ("coverage", DEPARTMENT_LAYER, b"Department 31", b"Department 3X"),
    ],
)
def test_direct_consumers_reject_same_inventory_content_tampering(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    consumer: str,
    layer: str,
    old_bytes: bytes,
    new_bytes: bytes,
) -> None:
    config, _, extraction = _extracted_fixture(
        tmp_path,
        source_config,
        include_roads=True,
    )
    if consumer == "coverage":
        # Rebuild once with the configured department layer present.
        archive_content = _synthetic_archive_bytes(
            tmp_path / "coverage-source",
            include_roads=True,
            include_department=True,
        )
        with patch(
            "landscout.sources.ign_bdtopo_fr.open_safe_https",
            return_value=_response(archive_content),
        ):
            download = download_ign_bdtopo_archive(config, tmp_path / "coverage-cache")
        extraction = extract_ign_bdtopo_archive(
            download,
            config,
            extraction_dir=tmp_path / "coverage-extracted",
        )

    size_before = extraction.geopackage_path.stat().st_size
    content = extraction.geopackage_path.read_bytes()
    assert old_bytes in content
    extraction.geopackage_path.write_bytes(content.replace(old_bytes, new_bytes, 1))
    assert extraction.geopackage_path.stat().st_size == size_before

    with pytest.raises(IgnBdTopoLayerError, match="integrity|SHA|physical|changed"):
        if consumer == "electricity":
            load_ign_bdtopo_electricity(extraction, config)
        elif consumer == "roads":
            ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, config)
        else:
            load_ign_bdtopo_department_coverage(extraction, config)


def test_road_loader_rejects_source_change_after_physical_read(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
) -> None:
    config, _, extraction = _extracted_fixture(
        tmp_path,
        source_config,
        include_roads=True,
    )
    original_read = ign_bdtopo_fr.gpd.read_file

    def mutate_after_read(*args: object, **kwargs: object) -> gpd.GeoDataFrame:
        frame = original_read(*args, **kwargs)
        content = extraction.geopackage_path.read_bytes()
        extraction.geopackage_path.write_bytes(
            content.replace(b"Bretelle", b"BretellX", 1)
        )
        return frame

    with (
        patch.object(ign_bdtopo_fr.gpd, "read_file", side_effect=mutate_after_read),
        pytest.raises(IgnBdTopoLayerError, match="changed|integrity|SHA"),
    ):
        ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, config)

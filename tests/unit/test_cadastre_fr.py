import gzip
import io
import json
from datetime import UTC, datetime, timedelta
from hashlib import sha256
from pathlib import Path
from unittest.mock import patch
from urllib.error import HTTPError

import pytest

from landscout.sources.cadastre_fr import (
    CadastreDownloadError,
    build_cadastre_parcelles_url,
    download_cadastre_parcelles,
)

COMMUNE_CODE = "31395"
EXPECTED_URL = (
    "https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes/"
    "31/31395/cadastre-31395-parcelles.json.gz"
)
ARCHIVE_CONTENT = gzip.compress(b'{"type":"FeatureCollection","features":[]}')
REFRESHED_ARCHIVE_CONTENT = gzip.compress(
    b'{"type":"FeatureCollection","features":[{"type":"Feature"}]}'
)


def _set_cache_age(metadata_path: Path, age: timedelta) -> None:
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    metadata["download_timestamp"] = (datetime.now(UTC) - age).isoformat()
    metadata_path.write_text(json.dumps(metadata), encoding="utf-8")


def test_build_cadastre_parcelles_url() -> None:
    assert build_cadastre_parcelles_url(COMMUNE_CODE) == EXPECTED_URL


def test_successful_download(tmp_path: Path) -> None:
    with patch(
        "landscout.sources.cadastre_fr.urlopen",
        return_value=io.BytesIO(ARCHIVE_CONTENT),
    ):
        result = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert result.path.read_bytes() == ARCHIVE_CONTENT
    assert result.source_url == EXPECTED_URL
    assert result.file_size == len(ARCHIVE_CONTENT)
    assert result.cache_hit is False
    metadata_path = tmp_path / f"{result.filename}.metadata.json"
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    assert metadata["download_timestamp"] == result.download_timestamp


def test_fresh_cache_is_reused(tmp_path: Path) -> None:
    with patch(
        "landscout.sources.cadastre_fr.urlopen",
        return_value=io.BytesIO(ARCHIVE_CONTENT),
    ) as opener:
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
        second = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert opener.call_count == 1
    assert first.cache_hit is False
    assert second.cache_hit is True
    assert second.sha256 == first.sha256
    assert second.download_timestamp == first.download_timestamp


def test_expired_cache_is_downloaded_again(tmp_path: Path) -> None:
    with patch(
        "landscout.sources.cadastre_fr.urlopen",
        side_effect=[io.BytesIO(ARCHIVE_CONTENT), io.BytesIO(REFRESHED_ARCHIVE_CONTENT)],
    ) as opener:
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
        metadata_path = tmp_path / f"{first.filename}.metadata.json"
        _set_cache_age(metadata_path, timedelta(hours=169))
        refreshed = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert opener.call_count == 2
    assert refreshed.cache_hit is False
    assert refreshed.path.read_bytes() == REFRESHED_ARCHIVE_CONTENT
    assert refreshed.sha256 == sha256(REFRESHED_ARCHIVE_CONTENT).hexdigest()


def test_failed_refresh_preserves_cached_archive(tmp_path: Path) -> None:
    with patch(
        "landscout.sources.cadastre_fr.urlopen",
        return_value=io.BytesIO(ARCHIVE_CONTENT),
    ):
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    original_archive = first.path.read_bytes()
    metadata_path = tmp_path / f"{first.filename}.metadata.json"
    _set_cache_age(metadata_path, timedelta(hours=169))
    error = HTTPError(EXPECTED_URL, 503, "Unavailable", hdrs=None, fp=None)

    with (
        patch("landscout.sources.cadastre_fr.urlopen", side_effect=error),
        pytest.raises(CadastreDownloadError),
    ):
        download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert first.path.read_bytes() == original_archive
    assert metadata_path.is_file()


def test_failed_http_response(tmp_path: Path) -> None:
    error = HTTPError(EXPECTED_URL, 404, "Not Found", hdrs=None, fp=None)

    with (
        patch("landscout.sources.cadastre_fr.urlopen", side_effect=error),
        pytest.raises(CadastreDownloadError),
    ):
        download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert not list(tmp_path.glob("*"))


def test_checksum_generation(tmp_path: Path) -> None:
    with patch(
        "landscout.sources.cadastre_fr.urlopen",
        return_value=io.BytesIO(ARCHIVE_CONTENT),
    ):
        result = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert result.sha256 == sha256(ARCHIVE_CONTENT).hexdigest()

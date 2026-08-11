import gzip
import io
import json
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


def test_valid_cache_is_reused(tmp_path: Path) -> None:
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

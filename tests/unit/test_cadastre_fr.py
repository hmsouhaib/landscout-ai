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
    _is_valid_gzip,
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
CORRUPTED_ARCHIVE_CONTENT = ARCHIVE_CONTENT[:-8]


def _set_cache_age(metadata_path: Path, age: timedelta) -> None:
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    metadata["download_timestamp"] = (datetime.now(UTC) - age).isoformat()
    metadata_path.write_text(json.dumps(metadata), encoding="utf-8")


def _update_metadata_integrity(metadata_path: Path, archive_path: Path) -> None:
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    content = archive_path.read_bytes()
    metadata["file_size"] = len(content)
    metadata["sha256"] = sha256(content).hexdigest()
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


def test_valid_gzip_is_accepted(tmp_path: Path) -> None:
    archive_path = tmp_path / "valid.json.gz"
    archive_path.write_bytes(ARCHIVE_CONTENT)

    assert _is_valid_gzip(archive_path)


def test_truncated_gzip_is_rejected(tmp_path: Path) -> None:
    archive_path = tmp_path / "truncated.json.gz"
    archive_path.write_bytes(CORRUPTED_ARCHIVE_CONTENT)

    assert not _is_valid_gzip(archive_path)


def test_corrupted_cached_archive_triggers_fresh_download(tmp_path: Path) -> None:
    with patch(
        "landscout.sources.cadastre_fr.urlopen",
        side_effect=[io.BytesIO(ARCHIVE_CONTENT), io.BytesIO(REFRESHED_ARCHIVE_CONTENT)],
    ) as opener:
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
        metadata_path = tmp_path / f"{first.filename}.metadata.json"
        first.path.write_bytes(CORRUPTED_ARCHIVE_CONTENT)
        _update_metadata_integrity(metadata_path, first.path)
        refreshed = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert opener.call_count == 2
    assert refreshed.cache_hit is False
    assert refreshed.path.read_bytes() == REFRESHED_ARCHIVE_CONTENT


def test_corrupted_new_download_preserves_existing_archive(tmp_path: Path) -> None:
    with patch(
        "landscout.sources.cadastre_fr.urlopen",
        return_value=io.BytesIO(ARCHIVE_CONTENT),
    ):
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    original_archive = first.path.read_bytes()
    metadata_path = tmp_path / f"{first.filename}.metadata.json"
    _set_cache_age(metadata_path, timedelta(hours=169))

    with (
        patch(
            "landscout.sources.cadastre_fr.urlopen",
            return_value=io.BytesIO(CORRUPTED_ARCHIVE_CONTENT),
        ),
        pytest.raises(CadastreDownloadError),
    ):
        download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert first.path.read_bytes() == original_archive
    assert not list(tmp_path.glob("*.part"))


@pytest.mark.parametrize(
    ("code", "department"),
    [("2A004", "2A"), ("2B033", "2B")],
)
def test_corsica_cadastre_urls_are_canonical(code: str, department: str) -> None:
    url = build_cadastre_parcelles_url(code)

    assert f"/{department}/{code}/cadastre-{code}-parcelles.json.gz" in url


@pytest.mark.parametrize("code", [31395, "2a004", " 31395 ", "ABCDE"])
def test_noncanonical_commune_code_is_controlled(code: object) -> None:
    with pytest.raises((TypeError, ValueError), match="Commune code"):
        build_cadastre_parcelles_url(code)  # type: ignore[arg-type]


@pytest.mark.parametrize(
    "timeout",
    [0, -1, float("nan"), float("inf"), "60", True],
)
def test_download_timeout_is_strict_finite_positive(
    tmp_path: Path,
    timeout: object,
) -> None:
    with pytest.raises(ValueError, match="timeout"):
        download_cadastre_parcelles(
            COMMUNE_CODE,
            tmp_path,
            timeout=timeout,  # type: ignore[arg-type]
        )


@pytest.mark.parametrize(
    "max_age",
    [-1, float("nan"), float("inf"), "168", True],
)
def test_cache_age_is_strict_finite_nonnegative(
    tmp_path: Path,
    max_age: object,
) -> None:
    with pytest.raises(ValueError, match="max_cache_age_hours"):
        download_cadastre_parcelles(
            COMMUNE_CODE,
            tmp_path,
            max_cache_age_hours=max_age,  # type: ignore[arg-type]
        )


@pytest.mark.parametrize("field", ["file_size", "sha256", "download_timestamp"])
def test_malformed_cached_metadata_triggers_refresh(
    tmp_path: Path,
    field: str,
) -> None:
    with patch(
        "landscout.sources.cadastre_fr.urlopen",
        side_effect=[io.BytesIO(ARCHIVE_CONTENT), io.BytesIO(REFRESHED_ARCHIVE_CONTENT)],
    ) as opener:
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
        metadata_path = tmp_path / f"{first.filename}.metadata.json"
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        metadata[field] = {
            "file_size": first.file_size + 1,
            "sha256": "0" * 64,
            "download_timestamp": "not-a-timestamp",
        }[field]
        metadata_path.write_text(json.dumps(metadata), encoding="utf-8")
        refreshed = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert opener.call_count == 2
    assert refreshed.path.read_bytes() == REFRESHED_ARCHIVE_CONTENT


def test_future_cached_timestamp_triggers_refresh(tmp_path: Path) -> None:
    with patch(
        "landscout.sources.cadastre_fr.urlopen",
        side_effect=[io.BytesIO(ARCHIVE_CONTENT), io.BytesIO(REFRESHED_ARCHIVE_CONTENT)],
    ) as opener:
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
        metadata_path = tmp_path / f"{first.filename}.metadata.json"
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        metadata["download_timestamp"] = (
            datetime.now(UTC) + timedelta(hours=1)
        ).isoformat()
        metadata_path.write_text(json.dumps(metadata), encoding="utf-8")
        refreshed = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert opener.call_count == 2
    assert refreshed.path.read_bytes() == REFRESHED_ARCHIVE_CONTENT


def test_metadata_publication_failure_restores_previous_cache_pair(
    tmp_path: Path,
) -> None:
    with patch(
        "landscout.sources.cadastre_fr.urlopen",
        return_value=io.BytesIO(ARCHIVE_CONTENT),
    ):
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
    metadata_path = tmp_path / f"{first.filename}.metadata.json"
    _set_cache_age(metadata_path, timedelta(hours=169))
    archive_before = first.path.read_bytes()
    metadata_before = metadata_path.read_bytes()
    temporary_metadata = metadata_path.with_suffix(f"{metadata_path.suffix}.part")
    original_replace = __import__(
        "landscout.sources.cadastre_fr",
        fromlist=["_replace_file"],
    )._replace_file

    def fail_metadata_publication(source: Path, target: Path) -> None:
        if source == temporary_metadata and target == metadata_path:
            raise OSError("simulated metadata publication failure")
        original_replace(source, target)

    with (
        patch(
            "landscout.sources.cadastre_fr.urlopen",
            return_value=io.BytesIO(REFRESHED_ARCHIVE_CONTENT),
        ),
        patch(
            "landscout.sources.cadastre_fr._replace_file",
            side_effect=fail_metadata_publication,
        ),
        pytest.raises(CadastreDownloadError, match="publication"),
    ):
        download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert first.path.read_bytes() == archive_before
    assert metadata_path.read_bytes() == metadata_before
    assert not list(tmp_path.glob("*.part"))
    assert not list(tmp_path.glob("*.bak"))


def test_first_metadata_publication_failure_leaves_no_half_pair(
    tmp_path: Path,
) -> None:
    expected_path = tmp_path / "cadastre-31395-parcelles.json.gz"
    metadata_path = tmp_path / f"{expected_path.name}.metadata.json"
    temporary_metadata = metadata_path.with_suffix(f"{metadata_path.suffix}.part")
    original_replace = __import__(
        "landscout.sources.cadastre_fr",
        fromlist=["_replace_file"],
    )._replace_file

    def fail_metadata_publication(source: Path, target: Path) -> None:
        if source == temporary_metadata and target == metadata_path:
            raise OSError("simulated metadata publication failure")
        original_replace(source, target)

    with (
        patch(
            "landscout.sources.cadastre_fr.urlopen",
            return_value=io.BytesIO(ARCHIVE_CONTENT),
        ),
        patch(
            "landscout.sources.cadastre_fr._replace_file",
            side_effect=fail_metadata_publication,
        ),
        pytest.raises(CadastreDownloadError, match="publication"),
    ):
        download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert not expected_path.exists()
    assert not metadata_path.exists()
    assert not list(tmp_path.glob("*.part"))
    assert not list(tmp_path.glob("*.bak"))

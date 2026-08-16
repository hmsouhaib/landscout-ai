import gzip
import io
import json
from datetime import UTC, datetime, timedelta
from hashlib import sha256
from pathlib import Path
from unittest.mock import patch
from urllib.error import HTTPError

import pytest

from landscout.sources import cadastre_fr
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
        "landscout.sources.cadastre_fr.open_safe_https",
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
        "landscout.sources.cadastre_fr.open_safe_https",
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
        "landscout.sources.cadastre_fr.open_safe_https",
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
        "landscout.sources.cadastre_fr.open_safe_https",
        return_value=io.BytesIO(ARCHIVE_CONTENT),
    ):
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    original_archive = first.path.read_bytes()
    metadata_path = tmp_path / f"{first.filename}.metadata.json"
    _set_cache_age(metadata_path, timedelta(hours=169))
    error = HTTPError(EXPECTED_URL, 503, "Unavailable", hdrs=None, fp=None)

    with (
        patch("landscout.sources.cadastre_fr.open_safe_https", side_effect=error),
        pytest.raises(CadastreDownloadError),
    ):
        download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert first.path.read_bytes() == original_archive
    assert metadata_path.is_file()


def test_failed_http_response(tmp_path: Path) -> None:
    error = HTTPError(EXPECTED_URL, 404, "Not Found", hdrs=None, fp=None)

    with (
        patch("landscout.sources.cadastre_fr.open_safe_https", side_effect=error),
        pytest.raises(CadastreDownloadError),
    ):
        download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert not list(tmp_path.glob("*"))


def test_checksum_generation(tmp_path: Path) -> None:
    with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
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
        "landscout.sources.cadastre_fr.open_safe_https",
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
        "landscout.sources.cadastre_fr.open_safe_https",
        return_value=io.BytesIO(ARCHIVE_CONTENT),
    ):
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    original_archive = first.path.read_bytes()
    metadata_path = tmp_path / f"{first.filename}.metadata.json"
    _set_cache_age(metadata_path, timedelta(hours=169))

    with (
        patch(
            "landscout.sources.cadastre_fr.open_safe_https",
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
        "landscout.sources.cadastre_fr.open_safe_https",
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
        "landscout.sources.cadastre_fr.open_safe_https",
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
        "landscout.sources.cadastre_fr.open_safe_https",
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
            "landscout.sources.cadastre_fr.open_safe_https",
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
            "landscout.sources.cadastre_fr.open_safe_https",
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


@pytest.mark.parametrize("rollback_target", ["archive", "metadata"])
def test_publication_and_rollback_failure_preserves_recovery_backup(
    tmp_path: Path,
    rollback_target: str,
) -> None:
    with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        return_value=io.BytesIO(ARCHIVE_CONTENT),
    ):
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
    metadata_path = tmp_path / f"{first.filename}.metadata.json"
    _set_cache_age(metadata_path, timedelta(hours=169))
    archive_backup = first.path.with_suffix(f"{first.path.suffix}.bak")
    metadata_backup = metadata_path.with_suffix(f"{metadata_path.suffix}.bak")
    temporary_metadata = metadata_path.with_suffix(f"{metadata_path.suffix}.part")
    original_replace = cadastre_fr._replace_file

    def fail_publication_and_rollback(source: Path, target: Path) -> None:
        if source == temporary_metadata and target == metadata_path:
            raise OSError("publication failure")
        if rollback_target == "archive" and source == archive_backup:
            raise OSError("archive rollback failure")
        if rollback_target == "metadata" and source == metadata_backup:
            raise OSError("metadata rollback failure")
        original_replace(source, target)

    with (
        patch(
            "landscout.sources.cadastre_fr.open_safe_https",
            return_value=io.BytesIO(REFRESHED_ARCHIVE_CONTENT),
        ),
        patch.object(
            cadastre_fr,
            "_replace_file",
            side_effect=fail_publication_and_rollback,
        ),
        pytest.raises(CadastreDownloadError, match="rollback"),
    ):
        download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    useful_backups = [path for path in (archive_backup, metadata_backup) if path.exists()]
    assert useful_backups


def test_stale_recovery_backup_rejects_cache_before_network_and_preserves_bytes(
    tmp_path: Path,
) -> None:
    with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        return_value=io.BytesIO(ARCHIVE_CONTENT),
    ):
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
    recovery_path = first.path.with_suffix(f"{first.path.suffix}.bak")
    recovery_bytes = b"manual cadastre recovery material"
    recovery_path.write_bytes(recovery_bytes)

    with (
        patch(
            "landscout.sources.cadastre_fr.open_safe_https",
            side_effect=AssertionError("recovery state must fail before network"),
        ) as opener,
        pytest.raises(CadastreDownloadError, match="backup|recovery|manual"),
    ):
        download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    opener.assert_not_called()
    assert recovery_path.read_bytes() == recovery_bytes
    assert first.path.read_bytes() == ARCHIVE_CONTENT


def test_next_run_after_double_failure_preserves_recovery_before_network(
    tmp_path: Path,
) -> None:
    with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        return_value=io.BytesIO(ARCHIVE_CONTENT),
    ):
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
    metadata_path = tmp_path / f"{first.filename}.metadata.json"
    _set_cache_age(metadata_path, timedelta(hours=169))
    old_archive = first.path.read_bytes()
    old_metadata = metadata_path.read_bytes()
    temporary_metadata = metadata_path.with_suffix(f"{metadata_path.suffix}.part")
    archive_backup = first.path.with_suffix(f"{first.path.suffix}.bak")
    metadata_backup = metadata_path.with_suffix(f"{metadata_path.suffix}.bak")
    original_replace = cadastre_fr._replace_file

    def fail_publication_and_rollback(source: Path, target: Path) -> None:
        if source == temporary_metadata and target == metadata_path:
            raise OSError("publication failed")
        if source == archive_backup and target == first.path:
            raise OSError("rollback failed")
        original_replace(source, target)

    with (
        patch(
            "landscout.sources.cadastre_fr.open_safe_https",
            return_value=io.BytesIO(REFRESHED_ARCHIVE_CONTENT),
        ),
        patch.object(
            cadastre_fr,
            "_replace_file",
            side_effect=fail_publication_and_rollback,
        ),
        pytest.raises(CadastreDownloadError, match="rollback"),
    ):
        download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert archive_backup.read_bytes() == old_archive
    assert metadata_backup.read_bytes() == old_metadata
    archive_recovery = archive_backup.read_bytes()
    metadata_recovery = metadata_backup.read_bytes()

    with (
        patch(
            "landscout.sources.cadastre_fr.open_safe_https",
            side_effect=AssertionError("recovery state must fail before network"),
        ) as opener,
        pytest.raises(CadastreDownloadError, match="backup|recovery|manual"),
    ):
        download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    opener.assert_not_called()
    assert archive_backup.read_bytes() == archive_recovery
    assert metadata_backup.read_bytes() == metadata_recovery


@pytest.mark.parametrize("temporary_role", ["archive", "metadata"])
@pytest.mark.parametrize("link_kind", ["symlink", "junction"])
def test_temporary_link_or_junction_cannot_modify_target_before_network(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    temporary_role: str,
    link_kind: str,
) -> None:
    archive_path = tmp_path / "cadastre-31395-parcelles.json.gz"
    metadata_path = tmp_path / f"{archive_path.name}.metadata.json"
    temporary_paths = {
        "archive": archive_path.with_suffix(f"{archive_path.suffix}.part"),
        "metadata": metadata_path.with_suffix(f"{metadata_path.suffix}.part"),
    }
    unsafe_path = temporary_paths[temporary_role]
    sentinel = tmp_path / "do-not-overwrite.txt"
    sentinel_bytes = b"irreplaceable cadastre sentinel"
    sentinel.write_bytes(sentinel_bytes)
    original_is_symlink = Path.is_symlink
    original_is_junction = Path.is_junction
    original_open = Path.open

    def simulated_is_symlink(path: Path) -> bool:
        return (
            link_kind == "symlink" and path == unsafe_path
        ) or original_is_symlink(path)

    def simulated_is_junction(path: Path) -> bool:
        return (
            link_kind == "junction" and path == unsafe_path
        ) or original_is_junction(path)

    def simulated_symlink_open(
        path: Path, *args: object, **kwargs: object
    ) -> object:
        if path == unsafe_path:
            return original_open(sentinel, *args, **kwargs)
        return original_open(path, *args, **kwargs)

    network_calls = 0

    def record_network(*args: object, **kwargs: object) -> io.BytesIO:
        nonlocal network_calls
        network_calls += 1
        return io.BytesIO(ARCHIVE_CONTENT)

    monkeypatch.setattr(Path, "is_symlink", simulated_is_symlink)
    monkeypatch.setattr(Path, "is_junction", simulated_is_junction)
    monkeypatch.setattr(Path, "open", simulated_symlink_open)
    monkeypatch.setattr(cadastre_fr, "open_safe_https", record_network)

    with pytest.raises(CadastreDownloadError, match="temporary|link|cache"):
        download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert network_calls == 0
    assert sentinel.read_bytes() == sentinel_bytes


def test_broken_recovery_symlink_is_rejected_before_network(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    archive_path = tmp_path / "cadastre-31395-parcelles.json.gz"
    recovery_path = archive_path.with_suffix(f"{archive_path.suffix}.bak")
    original_is_symlink = Path.is_symlink

    def simulated_is_symlink(path: Path) -> bool:
        return path == recovery_path or original_is_symlink(path)

    network_calls = 0

    def fail_network(*args: object, **kwargs: object) -> io.BytesIO:
        nonlocal network_calls
        network_calls += 1
        raise AssertionError("broken recovery link must fail before network")

    monkeypatch.setattr(Path, "is_symlink", simulated_is_symlink)
    monkeypatch.setattr(cadastre_fr, "open_safe_https", fail_network)

    with pytest.raises(CadastreDownloadError, match="backup|recovery|manual"):
        download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert network_calls == 0


def test_cleanup_failure_does_not_mask_double_failure_recovery_error(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        return_value=io.BytesIO(ARCHIVE_CONTENT),
    ):
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
    metadata_path = tmp_path / f"{first.filename}.metadata.json"
    _set_cache_age(metadata_path, timedelta(hours=169))
    old_archive = first.path.read_bytes()
    old_metadata = metadata_path.read_bytes()
    temporary_metadata = metadata_path.with_suffix(f"{metadata_path.suffix}.part")
    archive_backup = first.path.with_suffix(f"{first.path.suffix}.bak")
    metadata_backup = metadata_path.with_suffix(f"{metadata_path.suffix}.bak")
    original_replace = cadastre_fr._replace_file
    original_unlink = Path.unlink
    rollback_failed = False

    def fail_publication_and_rollback(source: Path, target: Path) -> None:
        nonlocal rollback_failed
        if source == temporary_metadata and target == metadata_path:
            raise OSError("publication failed")
        if source == archive_backup and target == first.path:
            rollback_failed = True
            raise OSError("rollback failed")
        original_replace(source, target)

    def fail_temporary_cleanup(path: Path, *, missing_ok: bool = False) -> None:
        if rollback_failed and path == temporary_metadata:
            raise PermissionError("temporary cleanup failed")
        original_unlink(path, missing_ok=missing_ok)

    monkeypatch.setattr(
        cadastre_fr,
        "open_safe_https",
        lambda *args, **kwargs: io.BytesIO(REFRESHED_ARCHIVE_CONTENT),
    )
    monkeypatch.setattr(cadastre_fr, "_replace_file", fail_publication_and_rollback)
    monkeypatch.setattr(Path, "unlink", fail_temporary_cleanup)

    with pytest.raises(CadastreDownloadError, match="rollback"):
        download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert archive_backup.read_bytes() == old_archive
    assert metadata_backup.read_bytes() == old_metadata

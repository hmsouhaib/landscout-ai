from __future__ import annotations

import inspect
import io
import json
import stat
import warnings
import zipfile
from contextlib import contextmanager
from dataclasses import FrozenInstanceError, fields, replace
from datetime import datetime
from hashlib import sha256
from pathlib import Path
from typing import Any, Self

import pytest
import yaml

from landscout import sources
from landscout.common import safe_http
from landscout.common.safe_http import SafeHttpsError
from landscout.sources import inpn_protected_areas_fr as inpn
from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasDownload,
    InpnProtectedAreasExtractedFile,
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasSourceError,
    download_inpn_protected_areas_archive,
    extract_inpn_protected_areas_archive,
    load_inpn_protected_areas_source_config,
)

CONFIG_PATH = Path("configs/sources/inpn_protected_areas_fr.yaml")
EXPECTED_EXPORTS = {
    "InpnProtectedAreasDownload",
    "InpnProtectedAreasExtractedFile",
    "InpnProtectedAreasExtraction",
    "InpnProtectedAreasSourceConfig",
    "InpnProtectedAreasSourceError",
    "download_inpn_protected_areas_archive",
    "extract_inpn_protected_areas_archive",
    "load_inpn_protected_areas_source_config",
}
class _Response:
    def __init__(
        self,
        payload: bytes,
        *,
        url: str,
        status_code: int = 200,
        location: str | None = None,
    ) -> None:
        self.raw = io.BytesIO(payload)
        self.url = url
        self.status_code = status_code
        self.headers = {} if location is None else {"Location": location}
        self.closed = False

    @property
    def is_redirect(self) -> bool:
        return self.status_code in {301, 302, 303, 307, 308} and "Location" in self.headers

    def raise_for_status(self) -> None:
        if self.status_code >= 400:
            raise OSError(f"HTTP {self.status_code}")

    def iter_content(self, chunk_size: int = 8192) -> Any:
        while chunk := self.raw.read(chunk_size):
            yield chunk

    def close(self) -> None:
        self.closed = True

    def read(self, size: int = -1) -> bytes:
        return self.raw.read(size)

    def __enter__(self) -> Self:
        return self

    def __exit__(self, *args: object) -> None:
        self.close()


class _Session:
    def __init__(
        self,
        response: _Response | None = None,
        *,
        responses: list[_Response] | None = None,
        error: Exception | None = None,
    ) -> None:
        self.responses = list(responses or ([] if response is None else [response]))
        self.error = error
        self.calls: list[tuple[str, dict[str, object]]] = []

    def get(self, url: str, **kwargs: object) -> _Response:
        self.calls.append((url, kwargs))
        if self.error is not None:
            raise self.error
        if not self.responses:
            raise AssertionError("No fake HTTP response was configured")
        response = self.responses.pop(0)
        response.raw.seek(0)
        return response

    @contextmanager
    def open(
        self,
        url: str,
        *,
        timeout: float,
        headers: dict[str, str] | None = None,
        max_redirects: int = 10,
    ) -> Any:
        response = self.get(
            url,
            timeout=timeout,
            headers=headers,
            max_redirects=max_redirects,
        )
        if not 200 <= response.status_code < 300:
            raise SafeHttpsError(f"HTTP status {response.status_code}")
        try:
            yield response
        finally:
            response.close()


def _zip_bytes(
    members: dict[str, bytes] | list[tuple[str, bytes]] | None = None,
) -> bytes:
    values = members or {"EP/readme.txt": b"protected areas"}
    entries = list(values.items()) if isinstance(values, dict) else values
    stream = io.BytesIO()
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UserWarning)
        with zipfile.ZipFile(stream, "w", compression=zipfile.ZIP_STORED) as archive:
            for name, payload in entries:
                info = zipfile.ZipInfo(name, date_time=(2026, 7, 1, 0, 0, 0))
                info.compress_type = zipfile.ZIP_STORED
                archive.writestr(info, payload)
    return stream.getvalue()


def _special_zip(name: str, mode: int) -> bytes:
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, "w") as archive:
        info = zipfile.ZipInfo(name)
        info.create_system = 3
        info.external_attr = mode << 16
        archive.writestr(info, b"target")
    return stream.getvalue()


def _unsupported_compression_zip() -> bytes:
    payload = bytearray(_zip_bytes())
    local = payload.index(b"PK\x03\x04")
    central = payload.index(b"PK\x01\x02")
    payload[local + 8 : local + 10] = (99).to_bytes(2, "little")
    payload[central + 10 : central + 12] = (99).to_bytes(2, "little")
    return bytes(payload)


def _config_payload() -> dict[str, object]:
    payload = yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))
    assert isinstance(payload, dict)
    return payload


def _write_config(tmp_path: Path, payload: dict[str, object]) -> Path:
    path = tmp_path / "source.yaml"
    path.write_text(
        yaml.safe_dump(payload, allow_unicode=True, sort_keys=False),
        encoding="utf-8",
    )
    return path


def _config(
    tmp_path: Path,
    expected_bytes: bytes | None = None,
) -> InpnProtectedAreasSourceConfig:
    snapshot = _zip_bytes() if expected_bytes is None else expected_bytes
    payload = _config_payload()
    payload["cache_root"] = str(tmp_path / "cache")
    payload["expected_archive_size_bytes"] = len(snapshot)
    payload["expected_archive_sha256"] = sha256(snapshot).hexdigest()
    return InpnProtectedAreasSourceConfig.model_validate(payload)


def _session(
    config: InpnProtectedAreasSourceConfig,
    payload: bytes | None = None,
    *,
    status_code: int = 200,
    redirect_chain: tuple[str, ...] = (),
) -> _Session:
    archive_url = str(config.archive_url)
    if not redirect_chain:
        return _Session(
            _Response(
                payload if payload is not None else _zip_bytes(),
                url=archive_url,
                status_code=status_code,
            )
        )
    responses: list[_Response] = []
    current_url = archive_url
    for target_url in redirect_chain:
        responses.append(
            _Response(
                b"",
                url=current_url,
                status_code=302,
                location=target_url,
            )
        )
        current_url = target_url
    responses.append(
        _Response(
            payload if payload is not None else _zip_bytes(),
            url=current_url,
            status_code=status_code,
        )
    )
    return _Session(responses=responses)


def _download(
    tmp_path: Path,
    *,
    payload: bytes | None = None,
) -> tuple[
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasDownload,
    _Session,
]:
    snapshot = _zip_bytes() if payload is None else payload
    config = _config(tmp_path, snapshot)
    session = _session(config, snapshot)
    result = _download_with_session(config, session)
    return config, result, session


def _download_with_session(
    config: InpnProtectedAreasSourceConfig,
    session: _Session,
    *,
    timeout_seconds: float = 120.0,
) -> InpnProtectedAreasDownload:
    with pytest.MonkeyPatch.context() as monkeypatch:
        monkeypatch.setattr(inpn, "open_safe_https", session.open)
        return download_inpn_protected_areas_archive(
            config,
            timeout_seconds=timeout_seconds,
        )


def _download_metadata_path(download: InpnProtectedAreasDownload) -> Path:
    return download.path.with_name(f"{download.filename}.metadata.json")


def _extraction_metadata_path(extraction: InpnProtectedAreasExtraction) -> Path:
    candidates = sorted(
        path
        for path in extraction.extraction_path.iterdir()
        if path.is_file()
        and path.name.startswith(".landscout")
        and path.suffix == ".json"
    )
    assert len(candidates) == 1
    return candidates[0]


def _read_json(path: Path) -> dict[str, object]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(payload, dict)
    return payload


def _write_json(path: Path, payload: dict[str, object]) -> None:
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def test_checked_in_config_loads_with_exact_source_identity() -> None:
    config = load_inpn_protected_areas_source_config()

    assert type(config) is InpnProtectedAreasSourceConfig
    assert config.provider == "PatriNat"
    assert config.authority == "MNHN"
    assert config.program == "INPN"
    assert config.dataset_id == "EP"
    assert config.dataset_name == "Base de référence des espaces protégés français"
    assert config.declared_version == "07/2026"
    assert str(config.reference_page_url).startswith("https://www.patrinat.fr/")
    assert str(config.archive_url) == "https://assets.patrinat.fr/files/donnees/ep/EP.zip"
    assert config.archive_filename == "EP.zip"
    assert config.expected_archive_size_bytes == 99_835_011
    assert (
        config.expected_archive_sha256
        == "73688bc37205a5e7f59e2065a0b81fc8cf2a242bdec5d7d2786f083671c4abe5"
    )


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("expected_archive_size_bytes", 0),
        ("expected_archive_size_bytes", -1),
        ("expected_archive_size_bytes", True),
        ("expected_archive_size_bytes", 1.0),
        ("expected_archive_sha256", "0" * 63),
        ("expected_archive_sha256", "A" * 64),
        ("expected_archive_sha256", None),
    ],
)
def test_config_rejects_invalid_expected_snapshot_integrity(
    field: str,
    value: object,
) -> None:
    payload = _config_payload()
    payload[field] = value

    with pytest.raises((TypeError, ValueError)):
        InpnProtectedAreasSourceConfig.model_validate(payload)


@pytest.mark.parametrize(
    "mutation",
    [
        "unknown_key",
        "missing_dataset_id",
        "wrong_dataset_id",
        "empty_version",
        "malformed_reference_url",
        "malformed_archive_url",
        "non_https_archive_url",
        "wrong_archive_filename",
    ],
)
def test_config_rejects_noncanonical_values(tmp_path: Path, mutation: str) -> None:
    payload = _config_payload()
    if mutation == "unknown_key":
        payload["unexpected"] = True
    elif mutation == "missing_dataset_id":
        payload.pop("dataset_id")
    elif mutation == "wrong_dataset_id":
        payload["dataset_id"] = "ZNIEFF"
    elif mutation == "empty_version":
        payload["declared_version"] = " "
    elif mutation == "malformed_reference_url":
        payload["reference_page_url"] = "not-a-url"
    elif mutation == "malformed_archive_url":
        payload["archive_url"] = "://bad"
    elif mutation == "non_https_archive_url":
        payload["archive_url"] = "http://assets.patrinat.fr/files/donnees/ep/EP.zip"
    else:
        payload["archive_filename"] = "other.zip"

    with pytest.raises(InpnProtectedAreasSourceError):
        load_inpn_protected_areas_source_config(_write_config(tmp_path, payload))


def test_wrong_download_config_type_has_controlled_error() -> None:
    with pytest.raises(InpnProtectedAreasSourceError, match="config|type"):
        download_inpn_protected_areas_archive(object())  # type: ignore[arg-type]


@pytest.mark.parametrize(
    "timeout",
    [
        0,
        -1,
        float("nan"),
        float("inf"),
        "30",
        True,
        pytest.param(10**10000, id="overflow-int"),
    ],
)
def test_download_timeout_is_strict_finite_positive(timeout: object) -> None:
    with pytest.raises(InpnProtectedAreasSourceError, match="timeout"):
        download_inpn_protected_areas_archive(
            load_inpn_protected_areas_source_config(),
            timeout_seconds=timeout,  # type: ignore[arg-type]
        )


def test_download_api_has_no_arbitrary_http_session_injection() -> None:
    assert "session" not in inspect.signature(
        download_inpn_protected_areas_archive
    ).parameters


def test_download_cache_setup_failure_is_controlled(tmp_path: Path) -> None:
    cache_file = tmp_path / "cache-is-a-file"
    cache_file.write_bytes(b"not a directory")
    payload = _config_payload()
    payload["cache_root"] = str(cache_file)
    config = InpnProtectedAreasSourceConfig.model_validate(payload)

    with pytest.raises(InpnProtectedAreasSourceError, match="download|cache"):
        _download_with_session(config, _session(config))


def test_valid_zip_download_binds_exact_bytes_and_lineage(tmp_path: Path) -> None:
    payload = _zip_bytes(
        {
            "EP/data/areas.shp": b"shape",
            "EP/data/areas.dbf": b"table",
        }
    )
    config = _config(tmp_path, payload)
    session = _session(config, payload)

    result = _download_with_session(config, session)

    assert result.cache_hit is False
    assert result.path.read_bytes() == payload
    assert result.file_size == len(payload)
    assert result.sha256 == sha256(payload).hexdigest()
    assert len(result.sha256) == 64 and result.sha256 == result.sha256.lower()
    timestamp = datetime.fromisoformat(result.download_timestamp)
    assert timestamp.tzinfo is not None
    assert timestamp.utcoffset() is not None
    assert timestamp.utcoffset().total_seconds() == 0
    assert result.filename == config.archive_filename == "EP.zip"
    for field in (
        "provider",
        "authority",
        "program",
        "dataset_id",
        "dataset_name",
        "declared_version",
        "reference_page_url",
        "archive_url",
    ):
        expected = getattr(config, field)
        if field.endswith("_url"):
            expected = str(expected)
        assert getattr(result, field) == expected
    assert len(session.calls) == 1
    requested_url, request_options = session.calls[0]
    assert requested_url == str(config.archive_url)
    assert request_options["timeout"] == pytest.approx(120.0)
    metadata = _read_json(_download_metadata_path(result))
    assert metadata["schema_version"] == 1
    assert metadata["file_size"] == len(payload)
    assert metadata["sha256"] == result.sha256


@pytest.mark.parametrize("mismatch", ["size", "sha256"])
def test_cold_download_must_match_configured_snapshot_before_publication(
    tmp_path: Path,
    mismatch: str,
) -> None:
    expected = _zip_bytes()
    if mismatch == "size":
        downloaded = _zip_bytes({"EP/other.txt": b"a longer protected-area payload"})
        assert len(downloaded) != len(expected)
    else:
        downloaded = _zip_bytes({"EP/readme.txt": b"protected areaz"})
        assert len(downloaded) == len(expected)
        assert sha256(downloaded).digest() != sha256(expected).digest()
    config = _config(tmp_path, expected)

    with pytest.raises(InpnProtectedAreasSourceError, match="size|SHA|snapshot|integrity"):
        _download_with_session(config, _session(config, downloaded))

    assert not list(Path(config.cache_root).rglob("EP.zip"))
    assert not list(Path(config.cache_root).rglob("*.metadata.json"))


def test_coordinated_cache_and_metadata_snapshot_change_is_not_a_cache_hit(
    tmp_path: Path,
) -> None:
    config, first, _ = _download(tmp_path)
    replacement = _zip_bytes({"EP/readme.txt": b"protected areaz"})
    assert len(replacement) == first.file_size
    first.path.write_bytes(replacement)
    metadata_path = _download_metadata_path(first)
    metadata = _read_json(metadata_path)
    metadata["file_size"] = len(replacement)
    metadata["sha256"] = sha256(replacement).hexdigest()
    _write_json(metadata_path, metadata)
    no_network = _Session(error=SafeHttpsError("configured snapshot requires refresh"))

    with pytest.raises(InpnProtectedAreasSourceError):
        _download_with_session(config, no_network)

    assert len(no_network.calls) == 1


@pytest.mark.parametrize(
    ("payload", "status", "error"),
    [
        (_zip_bytes(), 300, None),
        (_zip_bytes(), 304, None),
        (_zip_bytes(), 503, None),
        (b"", 200, None),
        (b"<html>temporary failure</html>", 200, None),
        (b"PK not really a zip", 200, None),
        (_zip_bytes(), 200, OSError("network failed")),
    ],
    ids=[
        "http-300",
        "http-304",
        "http-error",
        "empty",
        "html",
        "invalid-zip",
        "transport-error",
    ],
)
def test_http_and_payload_failures_are_controlled(
    tmp_path: Path,
    payload: bytes,
    status: int,
    error: Exception | None,
) -> None:
    config = _config(tmp_path)
    session = (
        _Session(error=error)
        if error is not None
        else _session(config, payload, status_code=status)
    )

    with pytest.raises(InpnProtectedAreasSourceError):
        _download_with_session(config, session)

    assert not list(Path(config.cache_root).rglob("*.part"))


def test_unsupported_zip_compression_has_controlled_error(tmp_path: Path) -> None:
    payload = _unsupported_compression_zip()
    config = _config(tmp_path, payload)

    with pytest.raises(InpnProtectedAreasSourceError, match="ZIP|archive"):
        _download_with_session(config, _session(config, payload))


def test_malformed_response_headers_have_controlled_error(tmp_path: Path) -> None:
    config = _config(tmp_path)
    response = _Response(_zip_bytes(), url=str(config.archive_url))
    response.headers = None  # type: ignore[assignment]

    with pytest.raises(InpnProtectedAreasSourceError, match="response|download"):
        _download_with_session(config, _Session(response))


def test_midstream_protocol_failure_has_controlled_error(tmp_path: Path) -> None:
    class _FailingRaw:
        decode_content = False

        def seek(self, offset: int) -> int:
            return offset

        def read(self, size: int = -1) -> bytes:
            raise OSError("connection ended mid-stream")

    config = _config(tmp_path)
    response = _Response(_zip_bytes(), url=str(config.archive_url))
    response.raw = _FailingRaw()  # type: ignore[assignment]

    with pytest.raises(InpnProtectedAreasSourceError, match="response|download"):
        _download_with_session(config, _Session(response))


def test_valid_physical_and_metadata_cache_is_reused(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config, first, _ = _download(tmp_path)

    def fail_dns(*args: object, **kwargs: object) -> list[tuple[Any, ...]]:
        raise AssertionError("DNS used for valid cache hit")

    def fail_http(*args: object, **kwargs: object) -> Any:
        raise AssertionError("HTTP used for valid cache hit")

    monkeypatch.setattr(safe_http.socket, "getaddrinfo", fail_dns)
    monkeypatch.setattr(inpn, "open_safe_https", fail_http)

    second = download_inpn_protected_areas_archive(config)

    assert second.cache_hit is True
    assert second.file_size == first.file_size
    assert second.sha256 == first.sha256


@pytest.mark.parametrize(
    "mutation",
    [
        "physical_size",
        "physical_sha",
        "metadata_sha",
        "metadata_size",
        "metadata_url",
        "metadata_version",
        "metadata_schema",
        "metadata_schema_bool",
        "metadata_schema_float",
        "metadata_unknown",
        "metadata_duplicate",
        "metadata_timestamp",
        "metadata_malformed",
        "invalid_cached_zip",
    ],
)
def test_invalid_download_cache_is_a_miss(
    tmp_path: Path,
    mutation: str,
) -> None:
    config, first, _ = _download(tmp_path)
    metadata_path = _download_metadata_path(first)
    metadata = _read_json(metadata_path)
    if mutation == "physical_size":
        first.path.write_bytes(_zip_bytes({"different.txt": b"much longer content"}))
    elif mutation == "physical_sha":
        replacement = _zip_bytes({"EP/readme.txt": b"protected areaz"})
        assert len(replacement) == first.file_size
        first.path.write_bytes(replacement)
    elif mutation == "metadata_sha":
        metadata["sha256"] = "0" * 64
        _write_json(metadata_path, metadata)
    elif mutation == "metadata_size":
        metadata["file_size"] = first.file_size + 1
        _write_json(metadata_path, metadata)
    elif mutation == "metadata_url":
        metadata["archive_url"] = "https://example.test/EP.zip"
        _write_json(metadata_path, metadata)
    elif mutation == "metadata_version":
        metadata["declared_version"] = "06/2026"
        _write_json(metadata_path, metadata)
    elif mutation in {"metadata_schema", "metadata_schema_bool", "metadata_schema_float"}:
        schema_values: dict[str, object] = {
            "metadata_schema": 2,
            "metadata_schema_bool": True,
            "metadata_schema_float": 1.0,
        }
        metadata["schema_version"] = schema_values[mutation]
        _write_json(metadata_path, metadata)
    elif mutation == "metadata_unknown":
        metadata["unexpected"] = True
        _write_json(metadata_path, metadata)
    elif mutation == "metadata_duplicate":
        metadata_json = json.dumps(metadata, separators=(",", ":"))
        metadata_path.write_text(
            metadata_json.replace(
                '"schema_version":1',
                '"schema_version":1,"schema_version":1',
                1,
            ),
            encoding="utf-8",
        )
    elif mutation == "metadata_timestamp":
        metadata["download_timestamp"] = "2026-08-16T12:00:00"
        _write_json(metadata_path, metadata)
    elif mutation == "metadata_malformed":
        metadata_path.write_text("{", encoding="utf-8")
    else:
        invalid_zip = b"not a zip"
        first.path.write_bytes(invalid_zip)
        metadata["file_size"] = len(invalid_zip)
        metadata["sha256"] = sha256(invalid_zip).hexdigest()
        _write_json(metadata_path, metadata)

    session = _session(config)
    refreshed = _download_with_session(config, session)

    assert refreshed.cache_hit is False
    assert len(session.calls) == 1


def _force_cache_miss(download: InpnProtectedAreasDownload) -> tuple[Path, bytes]:
    metadata_path = _download_metadata_path(download)
    metadata = _read_json(metadata_path)
    metadata["sha256"] = "0" * 64
    _write_json(metadata_path, metadata)
    return metadata_path, metadata_path.read_bytes()


def test_successful_first_and_replacement_publication(tmp_path: Path) -> None:
    config, first, _ = _download(tmp_path)
    _force_cache_miss(first)
    replacement = _zip_bytes()

    second = _download_with_session(config, _session(config, replacement))

    assert second.cache_hit is False
    assert second.path.read_bytes() == replacement
    assert _read_json(_download_metadata_path(second))["sha256"] == second.sha256
    assert not list(Path(config.cache_root).rglob("*.part"))


@pytest.mark.parametrize("failure_target", ["archive", "metadata"])
def test_publication_failure_restores_old_pair(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    failure_target: str,
) -> None:
    config, first, _ = _download(tmp_path)
    metadata_path, _ = _force_cache_miss(first)
    old_archive = first.path.read_bytes()
    old_metadata = metadata_path.read_bytes()
    original_replace = inpn._replace_file
    failed = False

    def fail_once(source: Path, target: Path) -> None:
        nonlocal failed
        wanted = first.path if failure_target == "archive" else metadata_path
        if source.name.endswith(".part") and target == wanted and not failed:
            failed = True
            raise OSError("publication failed")
        original_replace(source, target)

    monkeypatch.setattr(inpn, "_replace_file", fail_once)
    with pytest.raises(InpnProtectedAreasSourceError, match="publication|download"):
        _download_with_session(config, _session(config))

    assert first.path.read_bytes() == old_archive
    assert metadata_path.read_bytes() == old_metadata
    assert not list(Path(config.cache_root).rglob("*.part"))
    assert not list(Path(config.cache_root).rglob("*.bak"))


def test_rollback_failure_preserves_recovery_material(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config, first, _ = _download(tmp_path)
    metadata_path = _download_metadata_path(first)
    old_archive = first.path.read_bytes()
    old_metadata = metadata_path.read_bytes()
    original_replace = inpn._replace_file
    monkeypatch.setattr(inpn, "_load_cached_download", lambda *args: None)

    def fail_publication_and_rollback(source: Path, target: Path) -> None:
        if source.name.endswith(".part") and target == metadata_path:
            raise OSError("publication failed")
        if source.name.endswith(".bak"):
            raise OSError("rollback failed")
        original_replace(source, target)

    monkeypatch.setattr(inpn, "_replace_file", fail_publication_and_rollback)
    with pytest.raises(InpnProtectedAreasSourceError, match="rollback"):
        _download_with_session(config, _session(config))

    archive_backup = first.path.with_name(f"{first.path.name}.bak")
    metadata_backup = metadata_path.with_name(f"{metadata_path.name}.bak")
    assert archive_backup.read_bytes() == old_archive
    assert metadata_backup.read_bytes() == old_metadata


def test_failed_replacement_restores_a_still_reusable_valid_download_pair(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config, first, _ = _download(tmp_path)
    metadata_path = _download_metadata_path(first)
    old_archive = first.path.read_bytes()
    old_metadata = metadata_path.read_bytes()
    original_load = inpn._load_cached_download
    original_replace = inpn._replace_file

    monkeypatch.setattr(inpn, "_load_cached_download", lambda *args: None)

    def fail_metadata(source: Path, target: Path) -> None:
        if source.name.endswith(".part") and target == metadata_path:
            raise OSError("publication failed")
        original_replace(source, target)

    monkeypatch.setattr(inpn, "_replace_file", fail_metadata)
    with pytest.raises(InpnProtectedAreasSourceError, match="publication"):
        _download_with_session(config, _session(config))

    assert first.path.read_bytes() == old_archive
    assert metadata_path.read_bytes() == old_metadata
    monkeypatch.setattr(inpn, "_load_cached_download", original_load)
    monkeypatch.setattr(inpn, "_replace_file", original_replace)
    reused = _download_with_session(
        config,
        _Session(error=AssertionError("network used")),
    )
    assert reused.cache_hit is True


@pytest.mark.parametrize(
    "member_name",
    [
        "../evil.txt",
        "nested/../../evil.txt",
        "/absolute/evil.txt",
        r"C:\evil.txt",
        r"\\server\share\evil.txt",
        r"..\mixed\evil.txt",
        ".",
        "CON.txt",
        "folder/NUL.data",
        "folder/COM¹.parquet",
        "folder/LPT³.dbf",
        "folder/bad:name.txt",
        "folder/trailing. ",
        "folder/ leading.txt",
        "folder/control\n.txt",
    ],
)
def test_unsafe_zip_member_paths_are_rejected(
    tmp_path: Path,
    member_name: str,
) -> None:
    payload = _zip_bytes([(member_name, b"bad")])
    config = _config(tmp_path, payload)
    with pytest.raises(InpnProtectedAreasSourceError, match="ZIP|archive|member|path"):
        _download_with_session(config, _session(config, payload))


@pytest.mark.parametrize(
    "members",
    [
        [("same.txt", b"a"), ("same.txt", b"b")],
        [("folder/file.txt", b"a"), (r"folder\file.txt", b"b")],
        [("folder/file.txt", b"a"), ("folder/./file.txt", b"b")],
        [("Folder/File.txt", b"a"), ("folder/file.txt", b"b")],
        [("blocked", b"a"), ("blocked/child.txt", b"b")],
    ],
)
def test_duplicate_or_colliding_zip_destinations_are_rejected(
    tmp_path: Path,
    members: list[tuple[str, bytes]],
) -> None:
    payload = _zip_bytes(members)
    config = _config(tmp_path, payload)
    with pytest.raises(InpnProtectedAreasSourceError, match="duplicate|collid|archive"):
        _download_with_session(config, _session(config, payload))


@pytest.mark.parametrize(
    ("mode", "message"),
    [(stat.S_IFLNK | 0o777, "symbolic|link"), (stat.S_IFIFO | 0o644, "special")],
)
def test_zip_links_and_special_files_are_rejected(
    tmp_path: Path,
    mode: int,
    message: str,
) -> None:
    payload = _special_zip("unsafe", mode)
    config = _config(tmp_path, payload)
    with pytest.raises(InpnProtectedAreasSourceError, match=message):
        _download_with_session(config, _session(config, payload))


def test_complete_zip_inventory_is_validated_before_member_copy(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    payload = _zip_bytes(
        [("safe-first.txt", b"safe"), ("../unsafe-last.txt", b"unsafe")]
    )
    config = _config(tmp_path, payload)
    opened = 0
    original_open = zipfile.ZipFile.open

    def record_open(self: zipfile.ZipFile, *args: object, **kwargs: object) -> Any:
        nonlocal opened
        opened += 1
        return original_open(self, *args, **kwargs)

    monkeypatch.setattr(zipfile.ZipFile, "open", record_open)

    with pytest.raises(InpnProtectedAreasSourceError):
        _download_with_session(config, _session(config, payload))

    assert opened == 0


def test_extraction_validates_complete_inventory_before_copying(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config, download, _ = _download(tmp_path)
    payload = _zip_bytes(
        [("safe-first.txt", b"safe"), ("../unsafe-last.txt", b"unsafe")]
    )
    download.path.write_bytes(payload)
    forged = replace(
        download,
        file_size=len(payload),
        sha256=sha256(payload).hexdigest(),
    )
    copied = 0
    original_copy = inpn.copyfileobj

    def record_copy(*args: object, **kwargs: object) -> None:
        nonlocal copied
        copied += 1
        original_copy(*args, **kwargs)

    monkeypatch.setattr(inpn, "copyfileobj", record_copy)

    with pytest.raises(InpnProtectedAreasSourceError):
        extract_inpn_protected_areas_archive(forged, config)

    assert copied == 0
    assert not (download.path.parent / "x" / forged.sha256).exists()


def test_normal_nested_members_are_accepted(tmp_path: Path) -> None:
    config, download, _ = _download(
        tmp_path,
        payload=_zip_bytes({"EP/docs/readme.txt": b"ok"}),
    )

    assert download.path.is_file()
    assert download.filename == config.archive_filename


def test_extraction_inventory_is_complete_ordered_and_hashed(tmp_path: Path) -> None:
    payloads = {
        "z-last/empty.cpg": b"",
        "EP/data/areas.shp": b"shape",
        "EP/data/areas.dbf": b"table",
        "EP/metadata.xml": b"<metadata/>",
    }
    config, download, _ = _download(tmp_path, payload=_zip_bytes(payloads))

    extraction = extract_inpn_protected_areas_archive(download, config)

    expected_paths = sorted(payloads)
    assert extraction.cache_hit is False
    assert [item.relative_path for item in extraction.files] == expected_paths
    assert len(extraction.files) == len(payloads)
    by_path = {item.relative_path: item for item in extraction.files}
    for relative_path, payload in payloads.items():
        item = by_path[relative_path]
        assert item.file_size == len(payload)
        assert item.sha256 == sha256(payload).hexdigest()
        assert (
            extraction.extraction_path.joinpath(*relative_path.split("/")).read_bytes()
            == payload
        )
    assert by_path["z-last/empty.cpg"].file_size == 0
    assert by_path["z-last/empty.cpg"].sha256 == sha256(b"").hexdigest()
    metadata = _read_json(_extraction_metadata_path(extraction))
    assert metadata["schema_version"] == 1
    assert metadata["archive_sha256"] == download.sha256
    assert metadata["archive_size"] == download.file_size
    assert not list(extraction.extraction_path.parent.glob("*.part"))


def test_valid_extraction_cache_is_reused(tmp_path: Path) -> None:
    config, download, _ = _download(tmp_path)
    first = extract_inpn_protected_areas_archive(download, config)

    second = extract_inpn_protected_areas_archive(download, config)

    assert second.cache_hit is True
    assert second.files == first.files
    assert second.extraction_path == first.extraction_path


@pytest.mark.parametrize(
    "mutation",
    [
        "same_size_content",
        "size",
        "missing",
        "unexpected",
        "file_sha",
        "archive_sha",
        "archive_size",
        "schema",
        "schema_bool",
        "schema_float",
        "unknown",
        "boolean_file_size",
    ],
)
def test_invalid_extraction_cache_is_rebuilt(
    tmp_path: Path,
    mutation: str,
) -> None:
    original = b"original"
    config, download, _ = _download(
        tmp_path,
        payload=_zip_bytes({"EP/value.txt": original}),
    )
    first = extract_inpn_protected_areas_archive(download, config)
    data_path = first.extraction_path / "EP" / "value.txt"
    metadata_path = _extraction_metadata_path(first)
    metadata = _read_json(metadata_path)
    if mutation == "same_size_content":
        data_path.write_bytes(b"forged!!")
        assert data_path.stat().st_size == len(original)
    elif mutation == "size":
        data_path.write_bytes(b"different size")
    elif mutation == "missing":
        data_path.unlink()
    elif mutation == "unexpected":
        (first.extraction_path / "unexpected.txt").write_bytes(b"unexpected")
    elif mutation == "file_sha":
        file_entries = metadata["files"]
        assert isinstance(file_entries, list)
        assert isinstance(file_entries[0], dict)
        file_entries[0]["sha256"] = "0" * 64
        _write_json(metadata_path, metadata)
    elif mutation == "archive_sha":
        metadata["archive_sha256"] = "0" * 64
        _write_json(metadata_path, metadata)
    elif mutation == "archive_size":
        metadata["archive_size"] = download.file_size + 1
        _write_json(metadata_path, metadata)
    elif mutation in {"schema", "schema_bool", "schema_float"}:
        schema_values: dict[str, object] = {
            "schema": 2,
            "schema_bool": True,
            "schema_float": 1.0,
        }
        metadata["schema_version"] = schema_values[mutation]
        _write_json(metadata_path, metadata)
    elif mutation == "unknown":
        metadata["unexpected"] = True
        _write_json(metadata_path, metadata)
    else:
        file_entries = metadata["files"]
        assert isinstance(file_entries, list)
        assert isinstance(file_entries[0], dict)
        file_entries[0]["file_size"] = True
        _write_json(metadata_path, metadata)

    refreshed = extract_inpn_protected_areas_archive(download, config)

    assert refreshed.cache_hit is False
    assert (refreshed.extraction_path / "EP" / "value.txt").read_bytes() == original
    assert not (refreshed.extraction_path / "unexpected.txt").exists()


def _tree_snapshot(root: Path) -> dict[str, bytes]:
    return {
        path.relative_to(root).as_posix(): path.read_bytes()
        for path in sorted(root.rglob("*"))
        if path.is_file()
    }


def test_first_extraction_publication_failure_leaves_no_half_root(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config, download, _ = _download(tmp_path)
    root = download.path.parent / "x" / download.sha256
    original_replace = inpn._replace_directory

    def fail_publish(source: Path, target: Path) -> None:
        if source.name.endswith(".part") and target == root:
            raise OSError("publication failed")
        original_replace(source, target)

    monkeypatch.setattr(inpn, "_replace_directory", fail_publish)

    with pytest.raises(InpnProtectedAreasSourceError, match="publication"):
        extract_inpn_protected_areas_archive(download, config)

    assert not root.exists()
    assert not root.with_name(f"{root.name}.part").exists()
    assert not root.with_name(f"{root.name}.bak").exists()


def test_extraction_replacement_failure_restores_old_tree(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config, download, _ = _download(tmp_path)
    first = extract_inpn_protected_areas_archive(download, config)
    (first.extraction_path / "EP" / "readme.txt").write_bytes(b"tampered cache")
    before = _tree_snapshot(first.extraction_path)
    original_replace = inpn._replace_directory
    failed = False

    def fail_once(source: Path, target: Path) -> None:
        nonlocal failed
        if source.name.endswith(".part") and target == first.extraction_path and not failed:
            failed = True
            raise OSError("publication failed")
        original_replace(source, target)

    monkeypatch.setattr(inpn, "_replace_directory", fail_once)

    with pytest.raises(InpnProtectedAreasSourceError, match="publication"):
        extract_inpn_protected_areas_archive(download, config)

    assert _tree_snapshot(first.extraction_path) == before
    assert not first.extraction_path.with_name(
        f"{first.extraction_path.name}.bak"
    ).exists()


def test_extraction_rollback_failure_preserves_backup(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config, download, _ = _download(tmp_path)
    first = extract_inpn_protected_areas_archive(download, config)
    (first.extraction_path / "EP" / "readme.txt").write_bytes(b"tampered")
    before = _tree_snapshot(first.extraction_path)
    backup = first.extraction_path.with_name(f"{first.extraction_path.name}.bak")
    original_replace = inpn._replace_directory

    def fail_publish_and_rollback(source: Path, target: Path) -> None:
        if source.name.endswith(".part") and target == first.extraction_path:
            raise OSError("publication failed")
        if source == backup and target == first.extraction_path:
            raise OSError("rollback failed")
        original_replace(source, target)

    monkeypatch.setattr(inpn, "_replace_directory", fail_publish_and_rollback)

    with pytest.raises(InpnProtectedAreasSourceError, match="rollback"):
        extract_inpn_protected_areas_archive(download, config)

    assert _tree_snapshot(backup) == before
    assert not first.extraction_path.with_name(
        f"{first.extraction_path.name}.part"
    ).exists()


def test_extraction_backup_move_failure_leaves_old_tree_untouched(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config, download, _ = _download(tmp_path)
    first = extract_inpn_protected_areas_archive(download, config)
    (first.extraction_path / "EP" / "readme.txt").write_bytes(b"tampered")
    before = _tree_snapshot(first.extraction_path)
    backup = first.extraction_path.with_name(f"{first.extraction_path.name}.bak")
    original_replace = inpn._replace_directory

    def fail_backup_move(source: Path, target: Path) -> None:
        if source == first.extraction_path and target == backup:
            raise OSError("cannot stage old tree")
        original_replace(source, target)

    monkeypatch.setattr(inpn, "_replace_directory", fail_backup_move)

    with pytest.raises(InpnProtectedAreasSourceError, match="publication|stage"):
        extract_inpn_protected_areas_archive(download, config)

    assert first.extraction_path.is_dir()
    assert _tree_snapshot(first.extraction_path) == before
    assert not backup.exists()


@pytest.mark.parametrize("bad_input", [None, object(), True])
def test_extraction_rejects_wrong_download_type(
    tmp_path: Path,
    bad_input: object,
) -> None:
    with pytest.raises(InpnProtectedAreasSourceError, match="download|type"):
        extract_inpn_protected_areas_archive(
            bad_input,  # type: ignore[arg-type]
            _config(tmp_path),
        )


def test_extraction_rejects_wrong_config_type(tmp_path: Path) -> None:
    _, download, _ = _download(tmp_path)
    with pytest.raises(InpnProtectedAreasSourceError, match="config|type"):
        extract_inpn_protected_areas_archive(
            download,
            object(),  # type: ignore[arg-type]
        )


def test_extraction_cache_setup_failure_is_controlled(tmp_path: Path) -> None:
    config, download, _ = _download(tmp_path)
    extraction_parent = download.path.parent / "x"
    extraction_parent.write_bytes(b"not a directory")

    with pytest.raises(InpnProtectedAreasSourceError, match="extract|cache"):
        extract_inpn_protected_areas_archive(download, config)


def test_extraction_rejects_stale_download_bytes(tmp_path: Path) -> None:
    config, download, _ = _download(tmp_path)
    replacement = _zip_bytes({"EP/readme.txt": b"forged contents"})
    download.path.write_bytes(replacement)

    with pytest.raises(InpnProtectedAreasSourceError, match="SHA|size|archive|download"):
        extract_inpn_protected_areas_archive(download, config)


def test_result_dataclasses_are_frozen(tmp_path: Path) -> None:
    config, download, _ = _download(tmp_path)
    extraction = extract_inpn_protected_areas_archive(download, config)

    with pytest.raises(FrozenInstanceError):
        download.cache_hit = True  # type: ignore[misc]
    with pytest.raises(FrozenInstanceError):
        extraction.cache_hit = True  # type: ignore[misc]
    with pytest.raises(FrozenInstanceError):
        extraction.files[0].sha256 = "0" * 64  # type: ignore[misc]


def test_public_api_exports_only_stable_high_level_symbols() -> None:
    assert set(inpn.__all__) == EXPECTED_EXPORTS
    assert EXPECTED_EXPORTS <= set(sources.__all__)
    assert all(getattr(sources, name) is getattr(inpn, name) for name in EXPECTED_EXPORTS)
    assert not hasattr(sources, "_validated_zip_members")
    assert not hasattr(sources, "_inventory")
    assert not hasattr(sources, "validate_inpn_protected_area_geometry")


def test_result_schemas_are_factual_inventory_only() -> None:
    assert [field.name for field in fields(InpnProtectedAreasDownload)] == [
        "provider",
        "authority",
        "program",
        "dataset_id",
        "dataset_name",
        "declared_version",
        "reference_page_url",
        "archive_url",
        "download_timestamp",
        "filename",
        "file_size",
        "sha256",
        "path",
        "cache_hit",
    ]
    assert [field.name for field in fields(InpnProtectedAreasExtractedFile)] == [
        "relative_path",
        "file_size",
        "sha256",
    ]
    assert [field.name for field in fields(InpnProtectedAreasExtraction)] == [
        "download",
        "extraction_path",
        "files",
        "cache_hit",
    ]
    forbidden = {
        "geometry",
        "normalize",
        "parcel",
        "overlay",
        "severity",
        "score",
        "reject",
        "exclude",
        "bess",
    }
    assert not any(
        fragment in name.casefold()
        for name in inpn.__all__
        for fragment in forbidden
    )


def test_strict_metadata_rejects_boolean_numeric_values_as_cache_hits(
    tmp_path: Path,
) -> None:
    config, first, _ = _download(tmp_path)
    metadata_path = _download_metadata_path(first)
    metadata = _read_json(metadata_path)
    metadata["file_size"] = True
    _write_json(metadata_path, metadata)
    session = _session(config)

    refreshed = _download_with_session(config, session)

    assert refreshed.cache_hit is False
    assert len(session.calls) == 1


def test_cache_path_binds_version_and_filename(tmp_path: Path) -> None:
    _, download, _ = _download(tmp_path)

    assert download.path.name == "EP.zip"
    assert "07-2026" in download.path.parts
    metadata = _read_json(_download_metadata_path(download))
    assert metadata["dataset_id"] == "EP"
    assert metadata["declared_version"] == "07/2026"
    assert metadata["filename"] == "EP.zip"


def test_download_uses_no_hidden_reference_page_scrape(tmp_path: Path) -> None:
    config = _config(tmp_path)
    session = _session(config)

    _download_with_session(config, session)

    assert [url for url, _ in session.calls] == [str(config.archive_url)]
    assert str(config.reference_page_url) not in [url for url, _ in session.calls]


def test_exact_file_inventory_does_not_omit_unknown_suffixes(tmp_path: Path) -> None:
    members = {
        "EP/a.dbf": b"dbf",
        "EP/a.shx": b"shx",
        "EP/a.prj": b"prj",
        "EP/a.cpg": b"cpg",
        "EP/a.xml": b"xml",
        "EP/a.csv": b"csv",
        "EP/a.sqlite": b"sqlite",
        "EP/a.gpkg": b"gpkg",
        "EP/a.unknown": b"unknown",
    }
    config, download, _ = _download(tmp_path, payload=_zip_bytes(members))

    extraction = extract_inpn_protected_areas_archive(download, config)

    assert {item.relative_path for item in extraction.files} == set(members)


def test_archive_and_extraction_cache_reuse_are_independent(tmp_path: Path) -> None:
    config, first_download, _ = _download(tmp_path)
    first_extraction = extract_inpn_protected_areas_archive(first_download, config)

    second_download = _download_with_session(
        config,
        _Session(error=AssertionError("network used")),
    )
    second_extraction = extract_inpn_protected_areas_archive(second_download, config)

    assert first_download.cache_hit is False
    assert first_extraction.cache_hit is False
    assert second_download.cache_hit is True
    assert second_extraction.cache_hit is True


def test_no_stale_parts_after_download_or_extraction_success(tmp_path: Path) -> None:
    config, download, _ = _download(tmp_path)
    extraction = extract_inpn_protected_areas_archive(download, config)

    assert extraction.extraction_path.is_dir()
    assert not list(Path(config.cache_root).rglob("*.part"))
    assert not list(Path(config.cache_root).rglob("*.bak"))

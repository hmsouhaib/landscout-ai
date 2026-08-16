from __future__ import annotations

import io
import json
import socket
import stat
import warnings
import zipfile
from dataclasses import FrozenInstanceError, fields, replace
from datetime import datetime
from hashlib import sha256
from pathlib import Path
from typing import Any, Self

import pytest
import yaml
from urllib3.exceptions import ProtocolError

from landscout import sources
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
PUBLIC_IPV4 = "93.184.216.34"
PUBLIC_IPV6 = "2606:4700:4700::1111"


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


def _dns_records(
    addresses: tuple[str, ...],
    port: int,
) -> list[tuple[int, int, int, str, tuple[object, ...]]]:
    records: list[tuple[int, int, int, str, tuple[object, ...]]] = []
    for address in addresses:
        if ":" in address:
            records.append(
                (
                    socket.AF_INET6,
                    socket.SOCK_STREAM,
                    socket.IPPROTO_TCP,
                    "",
                    (address, port, 0, 0),
                )
            )
        else:
            records.append(
                (
                    socket.AF_INET,
                    socket.SOCK_STREAM,
                    socket.IPPROTO_TCP,
                    "",
                    (address, port),
                )
            )
    return records


@pytest.fixture(autouse=True)
def _public_dns(
    monkeypatch: pytest.MonkeyPatch,
) -> list[tuple[str, int]]:
    calls: list[tuple[str, int]] = []

    def resolve(hostname: str, port: int, **kwargs: object) -> list[tuple[Any, ...]]:
        assert kwargs == {"type": socket.SOCK_STREAM}
        calls.append((hostname, port))
        return _dns_records((PUBLIC_IPV4,), port)

    monkeypatch.setattr(inpn.socket, "getaddrinfo", resolve)
    return calls


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


def _config(tmp_path: Path) -> InpnProtectedAreasSourceConfig:
    payload = _config_payload()
    payload["cache_root"] = str(tmp_path / "cache")
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
    config = _config(tmp_path)
    session = _session(config, payload)
    result = download_inpn_protected_areas_archive(config, session=session)
    return config, result, session


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


def test_malformed_session_has_controlled_error(tmp_path: Path) -> None:
    with pytest.raises(InpnProtectedAreasSourceError, match="session|download"):
        download_inpn_protected_areas_archive(
            _config(tmp_path),
            session=object(),  # type: ignore[arg-type]
        )


def test_download_cache_setup_failure_is_controlled(tmp_path: Path) -> None:
    cache_file = tmp_path / "cache-is-a-file"
    cache_file.write_bytes(b"not a directory")
    payload = _config_payload()
    payload["cache_root"] = str(cache_file)
    config = InpnProtectedAreasSourceConfig.model_validate(payload)

    with pytest.raises(InpnProtectedAreasSourceError, match="download|cache"):
        download_inpn_protected_areas_archive(config, session=_session(config))


def test_valid_zip_download_binds_exact_bytes_and_lineage(tmp_path: Path) -> None:
    payload = _zip_bytes(
        {
            "EP/data/areas.shp": b"shape",
            "EP/data/areas.dbf": b"table",
        }
    )
    config = _config(tmp_path)
    session = _session(config, payload)

    result = download_inpn_protected_areas_archive(config, session=session)

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
    assert session.calls == [
        (
            str(config.archive_url),
            {
                    "allow_redirects": False,
                "stream": True,
                "timeout": pytest.approx(120.0),
            },
        )
    ]
    metadata = _read_json(_download_metadata_path(result))
    assert metadata["schema_version"] == 1
    assert metadata["file_size"] == len(payload)
    assert metadata["sha256"] == result.sha256


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
        download_inpn_protected_areas_archive(config, session=session)

    assert not list(Path(config.cache_root).rglob("*.part"))


def test_unsupported_zip_compression_has_controlled_error(tmp_path: Path) -> None:
    config = _config(tmp_path)

    with pytest.raises(InpnProtectedAreasSourceError, match="ZIP|archive"):
        download_inpn_protected_areas_archive(
            config,
            session=_session(config, _unsupported_compression_zip()),
        )


@pytest.mark.parametrize(
    "redirect_chain",
    [
        ("http://cdn.example.test/EP.zip",),
        ("file:///tmp/EP.zip",),
        ("ftp://example.test/EP.zip",),
        ("https://localhost/EP.zip",),
        ("https://127.0.0.1/EP.zip",),
        ("https://10.0.0.2/EP.zip",),
        ("https://2130706433/EP.zip",),
        ("https://0x7f000001/EP.zip",),
        ("https://[::1]/EP.zip",),
        ("https://[fd00::1]/EP.zip",),
        ("https://[fe80::1]/EP.zip",),
        ("https://user:secret@example.test/EP.zip",),
        ("https://cdn.example.test/EP.zip", "http://redirect.test/EP.zip"),
    ],
)
def test_unsafe_redirect_destination_is_rejected(
    tmp_path: Path,
    redirect_chain: tuple[str, ...],
) -> None:
    config = _config(tmp_path)
    session = _session(
        config,
        redirect_chain=redirect_chain,
    )

    with pytest.raises(InpnProtectedAreasSourceError, match="redirect|URL|HTTPS|host"):
        download_inpn_protected_areas_archive(config, session=session)

    requested_urls = [url for url, _ in session.calls]
    assert redirect_chain[-1] not in requested_urls
    assert all(call["allow_redirects"] is False for _, call in session.calls)


def test_safe_https_redirect_keeps_configured_archive_lineage(
    tmp_path: Path,
    _public_dns: list[tuple[str, int]],
) -> None:
    config = _config(tmp_path)
    session = _session(
        config,
        redirect_chain=("https://cdn.example.test/snapshot/EP.zip",),
    )

    result = download_inpn_protected_areas_archive(config, session=session)

    assert result.archive_url == str(config.archive_url)
    assert [url for url, _ in session.calls] == [
        str(config.archive_url),
        "https://cdn.example.test/snapshot/EP.zip",
    ]
    assert all(call["allow_redirects"] is False for _, call in session.calls)
    assert {hostname for hostname, _ in _public_dns} == {
        "assets.patrinat.fr",
        "cdn.example.test",
    }


def test_direct_official_url_resolves_public_dns_before_http(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config = _config(tmp_path)
    session = _session(config)
    events: list[tuple[str, str, int | None]] = []

    def resolve(hostname: str, port: int, **kwargs: object) -> list[tuple[Any, ...]]:
        assert kwargs == {"type": socket.SOCK_STREAM}
        events.append(("dns", hostname, port))
        return _dns_records((PUBLIC_IPV4,), port)

    original_get = session.get

    def get(url: str, **kwargs: object) -> _Response:
        events.append(("http", url, None))
        return original_get(url, **kwargs)

    monkeypatch.setattr(inpn.socket, "getaddrinfo", resolve)
    monkeypatch.setattr(session, "get", get)

    result = download_inpn_protected_areas_archive(config, session=session)

    assert result.cache_hit is False
    assert events[:2] == [
        ("dns", "assets.patrinat.fr", 443),
        ("http", str(config.archive_url), None),
    ]


def test_public_ipv4_and_ipv6_dns_answers_are_accepted(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config = _config(tmp_path)
    session = _session(config)
    resolved: list[tuple[str, int]] = []

    def resolve(hostname: str, port: int, **kwargs: object) -> list[tuple[Any, ...]]:
        assert kwargs == {"type": socket.SOCK_STREAM}
        resolved.append((hostname, port))
        return _dns_records((PUBLIC_IPV4, PUBLIC_IPV6, PUBLIC_IPV4), port)

    monkeypatch.setattr(inpn.socket, "getaddrinfo", resolve)

    result = download_inpn_protected_areas_archive(config, session=session)

    assert result.cache_hit is False
    assert session.calls
    assert resolved
    assert set(resolved) == {("assets.patrinat.fr", 443)}


@pytest.mark.parametrize(
    "addresses",
    [
        ("127.0.0.1",),
        ("10.0.0.2",),
        ("169.254.1.1",),
        ("0.0.0.0",),
        ("240.0.0.1",),
        ("::1",),
        ("fd00::1",),
        ("fe80::1",),
        ("::",),
        (PUBLIC_IPV4, "10.0.0.2"),
        ("::ffff:127.0.0.1",),
        ("224.0.0.1",),
        ("ff02::1",),
    ],
    ids=[
        "loopback-v4",
        "private-v4",
        "link-local-v4",
        "unspecified-v4",
        "reserved-v4",
        "loopback-v6",
        "private-v6",
        "link-local-v6",
        "unspecified-v6",
        "mixed-public-private",
        "mapped-private-v4",
        "multicast-v4",
        "multicast-v6",
    ],
)
def test_nonpublic_dns_answer_rejects_redirect_before_request(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    addresses: tuple[str, ...],
) -> None:
    config = _config(tmp_path)
    redirect_url = "https://redirect.example.test/EP.zip"
    session = _session(config, redirect_chain=(redirect_url,))

    def resolve(hostname: str, port: int, **kwargs: object) -> list[tuple[Any, ...]]:
        assert kwargs == {"type": socket.SOCK_STREAM}
        selected = addresses if hostname == "redirect.example.test" else (PUBLIC_IPV4,)
        return _dns_records(selected, port)

    monkeypatch.setattr(inpn.socket, "getaddrinfo", resolve)

    with pytest.raises(InpnProtectedAreasSourceError, match="DNS|address|URL|redirect"):
        download_inpn_protected_areas_archive(config, session=session)

    assert [url for url, _ in session.calls] == [str(config.archive_url)]


@pytest.mark.parametrize(
    "url",
    [
        "https://127.0.0.1/EP.zip",
        "https://10.0.0.2/EP.zip",
        "https://2130706433/EP.zip",
        "https://0x7f000001/EP.zip",
        "https://[::1]/EP.zip",
        "https://[fd00::1]/EP.zip",
        "https://[fe80::1]/EP.zip",
    ],
)
def test_unsafe_literal_ip_validation_never_uses_dns(
    monkeypatch: pytest.MonkeyPatch,
    url: str,
) -> None:
    def fail_dns(*args: object, **kwargs: object) -> list[tuple[Any, ...]]:
        raise AssertionError("literal IP used DNS")

    monkeypatch.setattr(inpn.socket, "getaddrinfo", fail_dns)

    with pytest.raises(InpnProtectedAreasSourceError):
        inpn._validate_destination_url(url)


def test_public_literal_ip_validation_never_uses_dns(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def fail_dns(*args: object, **kwargs: object) -> list[tuple[Any, ...]]:
        raise AssertionError("literal IP used DNS")

    monkeypatch.setattr(inpn.socket, "getaddrinfo", fail_dns)

    assert (
        inpn._validate_destination_url(f"https://{PUBLIC_IPV4}/EP.zip")
        == f"https://{PUBLIC_IPV4}/EP.zip"
    )


@pytest.mark.parametrize(
    "case",
    [
        "zero",
        "short-record",
        "malformed-after-public",
        "unsupported-family",
        "bad-sockaddr",
        "wrong-address-version",
        "invalid-address-string",
        "non-string-address",
    ],
)
def test_unusable_dns_results_fail_before_http(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    case: str,
) -> None:
    config = _config(tmp_path)
    session = _session(config)

    def resolve(hostname: str, port: int, **kwargs: object) -> list[tuple[Any, ...]]:
        assert hostname == "assets.patrinat.fr"
        assert kwargs == {"type": socket.SOCK_STREAM}
        public = _dns_records((PUBLIC_IPV4,), port)[0]
        if case == "zero":
            return []
        if case == "short-record":
            return [(socket.AF_INET, socket.SOCK_STREAM)]
        if case == "malformed-after-public":
            return [public, ("malformed",)]
        if case == "unsupported-family":
            return [(9999, socket.SOCK_STREAM, 0, "", (PUBLIC_IPV4, port))]
        if case == "bad-sockaddr":
            return [(socket.AF_INET, socket.SOCK_STREAM, 0, "", (PUBLIC_IPV4,))]
        if case == "wrong-address-version":
            return [(socket.AF_INET, socket.SOCK_STREAM, 0, "", (PUBLIC_IPV6, port))]
        if case == "invalid-address-string":
            return [(socket.AF_INET, socket.SOCK_STREAM, 0, "", ("not-an-ip", port))]
        return [(socket.AF_INET, socket.SOCK_STREAM, 0, "", (123, port))]

    monkeypatch.setattr(inpn.socket, "getaddrinfo", resolve)

    with pytest.raises(InpnProtectedAreasSourceError, match="DNS|address|URL"):
        download_inpn_protected_areas_archive(config, session=session)

    assert session.calls == []


@pytest.mark.parametrize(
    "error",
    [
        socket.gaierror("DNS lookup failed"),
        OSError("resolver failed"),
        UnicodeError("invalid DNS name"),
    ],
    ids=["gaierror", "oserror", "unicode-error"],
)
def test_dns_resolution_errors_are_controlled_before_http(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    error: Exception,
) -> None:
    config = _config(tmp_path)
    session = _session(config)

    def fail_resolution(*args: object, **kwargs: object) -> list[tuple[Any, ...]]:
        raise error

    monkeypatch.setattr(inpn.socket, "getaddrinfo", fail_resolution)

    with pytest.raises(InpnProtectedAreasSourceError, match="DNS|address|URL"):
        download_inpn_protected_areas_archive(config, session=session)

    assert session.calls == []


def test_dns_resolution_uses_explicit_https_port(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config = _config(tmp_path)
    redirect_url = "https://cdn.example.test:8443/EP.zip"
    session = _session(config, redirect_chain=(redirect_url,))
    resolved: list[tuple[str, int]] = []

    def resolve(hostname: str, port: int, **kwargs: object) -> list[tuple[Any, ...]]:
        assert kwargs == {"type": socket.SOCK_STREAM}
        resolved.append((hostname, port))
        return _dns_records((PUBLIC_IPV4,), port)

    monkeypatch.setattr(inpn.socket, "getaddrinfo", resolve)

    download_inpn_protected_areas_archive(config, session=session)

    assert ("cdn.example.test", 8443) in resolved


def test_malformed_response_headers_have_controlled_error(tmp_path: Path) -> None:
    config = _config(tmp_path)
    response = _Response(_zip_bytes(), url=str(config.archive_url))
    response.headers = None  # type: ignore[assignment]

    with pytest.raises(InpnProtectedAreasSourceError, match="response|download"):
        download_inpn_protected_areas_archive(
            config,
            session=_Session(response),
        )


def test_midstream_protocol_failure_has_controlled_error(tmp_path: Path) -> None:
    class _FailingRaw:
        decode_content = False

        def seek(self, offset: int) -> int:
            return offset

        def read(self, size: int = -1) -> bytes:
            raise ProtocolError("connection ended mid-stream")

    config = _config(tmp_path)
    response = _Response(_zip_bytes(), url=str(config.archive_url))
    response.raw = _FailingRaw()  # type: ignore[assignment]

    with pytest.raises(InpnProtectedAreasSourceError, match="response|download"):
        download_inpn_protected_areas_archive(
            config,
            session=_Session(response),
        )


def test_valid_physical_and_metadata_cache_is_reused(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config, first, _ = _download(tmp_path)
    no_network = _Session(error=AssertionError("network used"))

    def fail_dns(*args: object, **kwargs: object) -> list[tuple[Any, ...]]:
        raise AssertionError("DNS used for valid cache hit")

    monkeypatch.setattr(inpn.socket, "getaddrinfo", fail_dns)

    second = download_inpn_protected_areas_archive(config, session=no_network)

    assert second.cache_hit is True
    assert second.file_size == first.file_size
    assert second.sha256 == first.sha256
    assert no_network.calls == []


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

    session = _session(config, _zip_bytes({"EP/fresh.txt": b"fresh"}))
    refreshed = download_inpn_protected_areas_archive(config, session=session)

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
    replacement = _zip_bytes({"EP/replacement.txt": b"replacement"})

    second = download_inpn_protected_areas_archive(
        config,
        session=_session(config, replacement),
    )

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
        download_inpn_protected_areas_archive(
            config,
            session=_session(config, _zip_bytes({"fresh.txt": b"fresh"})),
        )

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
        download_inpn_protected_areas_archive(
            config,
            session=_session(config, _zip_bytes({"fresh.txt": b"fresh"})),
        )

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
        download_inpn_protected_areas_archive(
            config,
            session=_session(config, _zip_bytes({"EP/fresh.txt": b"fresh"})),
        )

    assert first.path.read_bytes() == old_archive
    assert metadata_path.read_bytes() == old_metadata
    monkeypatch.setattr(inpn, "_load_cached_download", original_load)
    monkeypatch.setattr(inpn, "_replace_file", original_replace)
    reused = download_inpn_protected_areas_archive(
        config,
        session=_Session(error=AssertionError("network used")),
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
    config = _config(tmp_path)
    with pytest.raises(InpnProtectedAreasSourceError, match="ZIP|archive|member|path"):
        download_inpn_protected_areas_archive(
            config,
            session=_session(config, _zip_bytes([(member_name, b"bad")])),
        )


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
    config = _config(tmp_path)
    with pytest.raises(InpnProtectedAreasSourceError, match="duplicate|collid|archive"):
        download_inpn_protected_areas_archive(
            config,
            session=_session(config, _zip_bytes(members)),
        )


@pytest.mark.parametrize(
    ("mode", "message"),
    [(stat.S_IFLNK | 0o777, "symbolic|link"), (stat.S_IFIFO | 0o644, "special")],
)
def test_zip_links_and_special_files_are_rejected(
    tmp_path: Path,
    mode: int,
    message: str,
) -> None:
    config = _config(tmp_path)
    with pytest.raises(InpnProtectedAreasSourceError, match=message):
        download_inpn_protected_areas_archive(
            config,
            session=_session(config, _special_zip("unsafe", mode)),
        )


def test_complete_zip_inventory_is_validated_before_member_copy(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config = _config(tmp_path)
    payload = _zip_bytes(
        [("safe-first.txt", b"safe"), ("../unsafe-last.txt", b"unsafe")]
    )
    opened = 0
    original_open = zipfile.ZipFile.open

    def record_open(self: zipfile.ZipFile, *args: object, **kwargs: object) -> Any:
        nonlocal opened
        opened += 1
        return original_open(self, *args, **kwargs)

    monkeypatch.setattr(zipfile.ZipFile, "open", record_open)

    with pytest.raises(InpnProtectedAreasSourceError):
        download_inpn_protected_areas_archive(
            config,
            session=_session(config, payload),
        )

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
    session = _session(config, _zip_bytes({"fresh.txt": b"fresh"}))

    refreshed = download_inpn_protected_areas_archive(config, session=session)

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

    download_inpn_protected_areas_archive(config, session=session)

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

    second_download = download_inpn_protected_areas_archive(
        config,
        session=_Session(error=AssertionError("network used")),
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

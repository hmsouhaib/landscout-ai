from __future__ import annotations

import io
import socket
import ssl
from typing import Any
from urllib.request import Request

import pytest

from landscout.common import safe_http
from landscout.common.safe_http import SafeHttpsError, open_safe_https

PUBLIC_IPV4 = "93.184.216.34"
PUBLIC_IPV6 = "2606:4700:4700::1111"


def _http_response(
    status: int = 200,
    *,
    body: bytes = b"ok",
    headers: dict[str, str] | None = None,
) -> bytes:
    reason = {
        200: "OK",
        301: "Moved Permanently",
        302: "Found",
        303: "See Other",
        307: "Temporary Redirect",
        308: "Permanent Redirect",
    }.get(status, "Response")
    values = {"Content-Length": str(len(body)), **(headers or {})}
    header_bytes = "".join(f"{name}: {value}\r\n" for name, value in values.items())
    return f"HTTP/1.1 {status} {reason}\r\n{header_bytes}\r\n".encode() + body


def _dns_records(
    addresses: tuple[str, ...],
    port: int,
) -> list[tuple[int, int, int, str, tuple[object, ...]]]:
    result: list[tuple[int, int, int, str, tuple[object, ...]]] = []
    for address in addresses:
        if ":" in address:
            result.append(
                (
                    socket.AF_INET6,
                    socket.SOCK_STREAM,
                    socket.IPPROTO_TCP,
                    "",
                    (address, port, 0, 0),
                )
            )
        else:
            result.append(
                (
                    socket.AF_INET,
                    socket.SOCK_STREAM,
                    socket.IPPROTO_TCP,
                    "",
                    (address, port),
                )
            )
    return result


class _FakeSocket:
    def __init__(
        self,
        family: int,
        response_bytes: bytes,
        connected: list[tuple[int, tuple[object, ...]]],
        sent: list[bytes],
    ) -> None:
        self.family = family
        self._response_bytes = response_bytes
        self._connected = connected
        self._sent = sent
        self._endpoint: tuple[object, ...] | None = None
        self.closed = False
        self.timeout: float | None = None

    def settimeout(self, timeout: float) -> None:
        self.timeout = timeout

    def connect(self, endpoint: tuple[object, ...]) -> None:
        self._endpoint = endpoint
        self._connected.append((self.family, endpoint))

    def getpeername(self) -> tuple[object, ...]:
        assert self._endpoint is not None
        return self._endpoint

    def sendall(self, payload: bytes) -> None:
        self._sent.append(payload)

    def makefile(self, *args: object, **kwargs: object) -> io.BytesIO:
        return io.BytesIO(self._response_bytes)

    def setsockopt(self, *args: object, **kwargs: object) -> None:
        return None

    def close(self) -> None:
        self.closed = True


class _FakeTlsContext:
    check_hostname = True
    verify_mode = ssl.CERT_REQUIRED

    def __init__(self, server_names: list[str]) -> None:
        self._server_names = server_names

    def wrap_socket(self, sock: _FakeSocket, *, server_hostname: str) -> _FakeSocket:
        self._server_names.append(server_hostname)
        return sock


class _NetworkHarness:
    def __init__(self, responses: list[bytes]) -> None:
        self.responses = list(responses)
        self.connected: list[tuple[int, tuple[object, ...]]] = []
        self.sent: list[bytes] = []
        self.server_names: list[str] = []
        self.contexts: list[_FakeTlsContext] = []
        self.sockets: list[_FakeSocket] = []

    def socket(
        self,
        family: int = socket.AF_INET,
        type: int = socket.SOCK_STREAM,
        proto: int = 0,
        fileno: int | None = None,
    ) -> _FakeSocket:
        assert type == socket.SOCK_STREAM
        assert fileno is None
        if not self.responses:
            raise AssertionError("Unexpected additional socket connection")
        result = _FakeSocket(
            family,
            self.responses.pop(0),
            self.connected,
            self.sent,
        )
        self.sockets.append(result)
        return result

    def context(self, *args: object, **kwargs: object) -> _FakeTlsContext:
        context = _FakeTlsContext(self.server_names)
        self.contexts.append(context)
        return context


def _install_network(
    monkeypatch: pytest.MonkeyPatch,
    *,
    responses: list[bytes] | None = None,
) -> _NetworkHarness:
    harness = _NetworkHarness(responses or [_http_response()])
    monkeypatch.setattr(safe_http.socket, "socket", harness.socket)
    monkeypatch.setattr(safe_http.ssl, "create_default_context", harness.context)
    return harness


def _install_dns(
    monkeypatch: pytest.MonkeyPatch,
    addresses: tuple[str, ...],
) -> list[tuple[str, int]]:
    calls: list[tuple[str, int]] = []

    def resolve(hostname: str, port: int, **kwargs: object) -> list[tuple[Any, ...]]:
        assert kwargs == {"type": socket.SOCK_STREAM}
        calls.append((hostname, port))
        return _dns_records(addresses, port)

    monkeypatch.setattr(safe_http.socket, "getaddrinfo", resolve)
    return calls


def _read(url: str = "https://source.example/archive.zip") -> bytes:
    with open_safe_https(url, timeout=12.5) as response:
        return response.read()


@pytest.mark.parametrize(
    "header_name",
    [
        "Authorization",
        "authorization",
        "Proxy-Authorization",
        "Cookie",
        "Cookie2",
        "Host",
        "Connection",
        "Proxy-Connection",
        "Keep-Alive",
        "Transfer-Encoding",
        "TE",
        "Trailer",
        "Upgrade",
    ],
)
def test_sensitive_and_hop_by_hop_headers_fail_before_dns(
    monkeypatch: pytest.MonkeyPatch,
    header_name: str,
) -> None:
    monkeypatch.setattr(
        safe_http.socket,
        "getaddrinfo",
        lambda *args, **kwargs: pytest.fail("DNS used after forbidden header"),
    )

    with (
        pytest.raises(SafeHttpsError, match="header|forbidden|owned"),
        open_safe_https(
            "https://source.example/archive.zip",
            timeout=12.5,
            headers={header_name: "secret"},
        ),
    ):
        pass


def test_case_insensitive_duplicate_header_names_fail_before_dns(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        safe_http.socket,
        "getaddrinfo",
        lambda *args, **kwargs: pytest.fail("DNS used after duplicate header"),
    )

    with (
        pytest.raises(SafeHttpsError, match="duplicate|ambiguous"),
        open_safe_https(
            "https://source.example/archive.zip",
            timeout=12.5,
            headers={"Accept": "application/zip", "accept": "application/json"},
        ),
    ):
        pass


def test_request_and_explicit_headers_cannot_ambiguously_override_each_other(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        safe_http.socket,
        "getaddrinfo",
        lambda *args, **kwargs: pytest.fail("DNS used after duplicate header"),
    )
    request = Request(
        "https://source.example/archive.zip",
        headers={"Accept": "application/zip"},
    )

    with (
        pytest.raises(SafeHttpsError, match="duplicate|ambiguous"),
        open_safe_https(
            request,
            timeout=12.5,
            headers={"accept": "application/json"},
        ),
    ):
        pass


def test_cross_origin_redirect_cannot_receive_a_sensitive_header(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        safe_http.socket,
        "getaddrinfo",
        lambda *args, **kwargs: pytest.fail(
            "DNS used before sensitive redirect header rejection"
        ),
    )
    harness = _install_network(
        monkeypatch,
        responses=[
            _http_response(
                302,
                body=b"",
                headers={"Location": "https://cdn.example/file"},
            ),
            _http_response(body=b"archive"),
        ],
    )

    with (
        pytest.raises(SafeHttpsError, match="header|forbidden"),
        open_safe_https(
            "https://source.example/archive.zip",
            timeout=12.5,
            headers={"Authorization": "Bearer secret"},
        ),
    ):
        pass

    assert harness.sent == []


def test_cross_origin_redirect_forwards_only_safe_ordinary_headers(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _install_dns(monkeypatch, (PUBLIC_IPV4,))
    harness = _install_network(
        monkeypatch,
        responses=[
            _http_response(
                302,
                body=b"",
                headers={"Location": "https://cdn.example/file"},
            ),
            _http_response(body=b"archive"),
        ],
    )

    with open_safe_https(
        "https://source.example/archive.zip",
        timeout=12.5,
        headers={"User-Agent": "LandScout-Test", "Accept": "application/zip"},
    ) as response:
        assert response.read() == b"archive"

    assert len(harness.sent) == 2
    for request in harness.sent:
        assert b"User-Agent: LandScout-Test" in request
        assert b"Accept: application/zip" in request
        assert b"Authorization:" not in request
        assert b"Cookie:" not in request


@pytest.mark.parametrize(
    "addresses",
    [
        (PUBLIC_IPV4,),
        (PUBLIC_IPV4, PUBLIC_IPV6),
        (PUBLIC_IPV4, PUBLIC_IPV4),
    ],
    ids=["public-ipv4", "public-ipv4-and-ipv6", "duplicate-public"],
)
def test_public_dns_answers_are_accepted(
    monkeypatch: pytest.MonkeyPatch,
    addresses: tuple[str, ...],
) -> None:
    calls = _install_dns(monkeypatch, addresses)
    harness = _install_network(monkeypatch)

    assert _read() == b"ok"
    assert calls == [("source.example", 443)]
    assert harness.connected


@pytest.mark.parametrize(
    "records",
    [
        [],
        [(socket.AF_INET, socket.SOCK_STREAM)],
        [(9999, socket.SOCK_STREAM, socket.IPPROTO_TCP, "", (PUBLIC_IPV4, 443))],
        [
            (
                socket.AF_INET,
                socket.SOCK_DGRAM,
                socket.IPPROTO_UDP,
                "",
                (PUBLIC_IPV4, 443),
            )
        ],
        [(socket.AF_INET, socket.SOCK_STREAM, object(), "", (PUBLIC_IPV4, 443))],
        [(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP, "", (PUBLIC_IPV4,))],
        [
            (
                socket.AF_INET,
                socket.SOCK_STREAM,
                socket.IPPROTO_TCP,
                "",
                (PUBLIC_IPV6, 443),
            )
        ],
        [(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP, "", (123, 443))],
    ],
    ids=[
        "zero",
        "short-record",
        "unsupported-family",
        "wrong-socket-type",
        "non-integer-protocol",
        "bad-sockaddr",
        "family-mismatch",
        "non-string-address",
    ],
)
def test_malformed_or_unusable_dns_results_fail_before_socket(
    monkeypatch: pytest.MonkeyPatch,
    records: list[tuple[Any, ...]],
) -> None:
    monkeypatch.setattr(
        safe_http.socket, "getaddrinfo", lambda *args, **kwargs: records
    )
    monkeypatch.setattr(
        safe_http.socket,
        "socket",
        lambda *args, **kwargs: pytest.fail("socket used after invalid DNS"),
    )

    with pytest.raises(SafeHttpsError, match="DNS|address"):
        _read()


@pytest.mark.parametrize(
    "address",
    [
        "127.0.0.1",
        "10.0.0.2",
        "169.254.1.1",
        "0.0.0.0",
        "240.0.0.1",
        "224.0.0.1",
        "::1",
        "fd00::1",
        "fe80::1",
        "::",
        "ff02::1",
        "::ffff:127.0.0.1",
    ],
    ids=[
        "ipv4-loopback",
        "ipv4-private",
        "ipv4-link-local",
        "ipv4-unspecified",
        "ipv4-reserved",
        "ipv4-multicast",
        "ipv6-loopback",
        "ipv6-private",
        "ipv6-link-local",
        "ipv6-unspecified",
        "ipv6-multicast",
        "ipv4-mapped-private",
    ],
)
def test_any_nonpublic_dns_answer_fails_before_socket(
    monkeypatch: pytest.MonkeyPatch,
    address: str,
) -> None:
    _install_dns(monkeypatch, (address,))
    monkeypatch.setattr(
        safe_http.socket,
        "socket",
        lambda *args, **kwargs: pytest.fail("socket used after unsafe DNS"),
    )

    with pytest.raises(SafeHttpsError, match="public|global|address|DNS"):
        _read()


def test_mixed_public_private_dns_answer_fails_closed(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _install_dns(monkeypatch, (PUBLIC_IPV4, "127.0.0.1"))
    monkeypatch.setattr(
        safe_http.socket,
        "socket",
        lambda *args, **kwargs: pytest.fail("socket used after mixed DNS"),
    )

    with pytest.raises(SafeHttpsError, match="public|global|address|DNS"):
        _read()


@pytest.mark.parametrize(
    "error",
    [
        socket.gaierror("DNS failed"),
        OSError("resolver failed"),
        UnicodeError("bad hostname"),
    ],
    ids=["gaierror", "oserror", "unicode-error"],
)
def test_dns_errors_are_controlled_before_socket(
    monkeypatch: pytest.MonkeyPatch,
    error: Exception,
) -> None:
    def fail(*args: object, **kwargs: object) -> list[tuple[Any, ...]]:
        raise error

    monkeypatch.setattr(safe_http.socket, "getaddrinfo", fail)
    monkeypatch.setattr(
        safe_http.socket,
        "socket",
        lambda *args, **kwargs: pytest.fail("socket used after DNS failure"),
    )

    with pytest.raises(SafeHttpsError, match="DNS|resolve"):
        _read()


@pytest.mark.parametrize(
    "url",
    [
        "http://source.example/archive.zip",
        "https://user:secret@source.example/archive.zip",
        "https://localhost/archive.zip",
        "https://api.localhost/archive.zip",
        "https://localhost\u3002/archive.zip",
        "https://api.localhost\uff0e/archive.zip",
        "https://api.localhost\uff61/archive.zip",
        "https:///archive.zip",
    ],
    ids=[
        "http",
        "credentials",
        "localhost",
        "localhost-subdomain",
        "localhost-ideographic-trailing-dot",
        "localhost-subdomain-fullwidth-trailing-dot",
        "localhost-subdomain-halfwidth-trailing-dot",
        "missing-host",
    ],
)
def test_unsafe_url_identity_fails_before_dns(
    monkeypatch: pytest.MonkeyPatch,
    url: str,
) -> None:
    monkeypatch.setattr(
        safe_http.socket,
        "getaddrinfo",
        lambda *args, **kwargs: pytest.fail("DNS used for lexically unsafe URL"),
    )

    with pytest.raises(SafeHttpsError, match="HTTPS|credential|localhost|host|URL"):
        _read(url)


@pytest.mark.parametrize(
    "url",
    [
        "https://127.0.0.1/archive.zip",
        "https://127.1/archive.zip",
        "https://0177.0.0.1/archive.zip",
        "https://10.0.0.2/archive.zip",
        "https://2130706433/archive.zip",
        "https://0x7f000001/archive.zip",
        "https://[::1]/archive.zip",
        "https://[fd00::1]/archive.zip",
        "https://[fe80::1]/archive.zip",
        "https://999999999999999999999/archive.zip",
        "https://0xnotanaddress/archive.zip",
    ],
)
def test_literal_and_malformed_numeric_ip_rejection_never_uses_dns(
    monkeypatch: pytest.MonkeyPatch,
    url: str,
) -> None:
    monkeypatch.setattr(
        safe_http.socket,
        "getaddrinfo",
        lambda *args, **kwargs: pytest.fail("literal address unexpectedly used DNS"),
    )

    with pytest.raises(SafeHttpsError, match="public|global|address|IP|URL"):
        _read(url)


def test_public_literal_ip_uses_exact_socket_without_dns(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        safe_http.socket,
        "getaddrinfo",
        lambda *args, **kwargs: pytest.fail("public literal unexpectedly used DNS"),
    )
    harness = _install_network(monkeypatch)

    assert _read(f"https://{PUBLIC_IPV4}/archive.zip") == b"ok"
    assert harness.connected == [(socket.AF_INET, (PUBLIC_IPV4, 443))]


def test_explicit_https_port_is_resolved_and_connected_exactly(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    calls = _install_dns(monkeypatch, (PUBLIC_IPV4,))
    harness = _install_network(monkeypatch)

    assert _read("https://source.example:8443/archive.zip") == b"ok"
    assert calls == [("source.example", 8443)]
    assert harness.connected == [(socket.AF_INET, (PUBLIC_IPV4, 8443))]
    assert harness.server_names == ["source.example"]
    assert b"\r\nHost: source.example:8443\r\n" in b"".join(harness.sent)


def test_safe_https_redirect_is_manually_revalidated(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    calls = _install_dns(monkeypatch, (PUBLIC_IPV4,))
    harness = _install_network(
        monkeypatch,
        responses=[
            _http_response(
                302, body=b"", headers={"Location": "https://cdn.example/file"}
            ),
            _http_response(body=b"archive"),
        ],
    )

    with open_safe_https(
        "https://source.example/archive.zip",
        timeout=12.5,
    ) as response:
        assert response.read() == b"archive"
        assert response.url == "https://cdn.example/file"
        assert response.history == ("https://source.example/archive.zip",)
    assert calls == [("source.example", 443), ("cdn.example", 443)]
    assert [endpoint for _, endpoint in harness.connected] == [
        (PUBLIC_IPV4, 443),
        (PUBLIC_IPV4, 443),
    ]
    assert harness.server_names == ["source.example", "cdn.example"]
    assert b"\r\nHost: source.example\r\n" in harness.sent[0]
    assert b"\r\nHost: cdn.example\r\n" in harness.sent[1]


def test_unsafe_redirect_is_rejected_before_target_socket(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def resolve(hostname: str, port: int, **kwargs: object) -> list[tuple[Any, ...]]:
        address = PUBLIC_IPV4 if hostname == "source.example" else "127.0.0.1"
        return _dns_records((address,), port)

    monkeypatch.setattr(safe_http.socket, "getaddrinfo", resolve)
    harness = _install_network(
        monkeypatch,
        responses=[
            _http_response(
                302,
                body=b"",
                headers={"Location": "https://private.example/file"},
            )
        ],
    )

    with pytest.raises(SafeHttpsError, match="public|global|address|DNS"):
        _read()
    assert harness.connected == [(socket.AF_INET, (PUBLIC_IPV4, 443))]


def test_redirect_loop_is_rejected(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _install_dns(monkeypatch, (PUBLIC_IPV4,))
    _install_network(
        monkeypatch,
        responses=[_http_response(302, body=b"", headers={"Location": "/archive.zip"})],
    )

    with pytest.raises(SafeHttpsError, match="loop"):
        _read()


def test_redirect_limit_is_enforced(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _install_dns(monkeypatch, (PUBLIC_IPV4,))
    redirects = [
        _http_response(302, body=b"", headers={"Location": f"/step-{index}"})
        for index in range(12)
    ]
    _install_network(monkeypatch, responses=redirects)

    with pytest.raises(SafeHttpsError, match="redirect"):
        _read()


def test_validated_dns_snapshot_binds_actual_socket_and_preserves_tls_host(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    resolutions = 0

    def rebind(hostname: str, port: int, **kwargs: object) -> list[tuple[Any, ...]]:
        nonlocal resolutions
        resolutions += 1
        address = PUBLIC_IPV4 if resolutions == 1 else "127.0.0.1"
        return _dns_records((address,), port)

    monkeypatch.setattr(safe_http.socket, "getaddrinfo", rebind)
    harness = _install_network(monkeypatch)

    assert _read("https://rebind.example/archive.zip") == b"ok"
    assert resolutions == 1
    assert harness.connected == [(socket.AF_INET, (PUBLIC_IPV4, 443))]
    assert harness.server_names == ["rebind.example"]
    request = b"".join(harness.sent).decode("ascii")
    assert request.startswith("GET /archive.zip HTTP/1.1\r\n")
    assert "\r\nHost: rebind.example\r\n" in request


def test_environment_proxy_does_not_change_bound_destination(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("HTTP_PROXY", "http://127.0.0.1:9999")
    monkeypatch.setenv("HTTPS_PROXY", "http://127.0.0.1:9999")
    monkeypatch.setenv("ALL_PROXY", "http://127.0.0.1:9999")
    _install_dns(monkeypatch, (PUBLIC_IPV4,))
    harness = _install_network(monkeypatch)

    assert _read() == b"ok"
    assert harness.connected == [(socket.AF_INET, (PUBLIC_IPV4, 443))]


@pytest.mark.parametrize(
    "header_name",
    ["Host ", "Bad Header"],
    ids=["host-with-trailing-space", "non-token-field-name"],
)
def test_malformed_header_name_is_rejected_before_dns(
    monkeypatch: pytest.MonkeyPatch,
    header_name: str,
) -> None:
    monkeypatch.setattr(
        safe_http.socket,
        "getaddrinfo",
        lambda *args, **kwargs: pytest.fail("DNS used after malformed header name"),
    )

    with (
        pytest.raises(SafeHttpsError, match="header|Host"),
        open_safe_https(
            "https://source.example/archive.zip",
            timeout=12.5,
            headers={header_name: "attacker.example"},
        ),
    ):
        pass


def test_tls_context_keeps_hostname_verification_enabled(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _install_dns(monkeypatch, (PUBLIC_IPV4,))
    harness = _install_network(monkeypatch)

    assert _read() == b"ok"
    assert harness.server_names == ["source.example"]
    assert len(harness.contexts) == 1
    assert harness.contexts[0].check_hostname is True
    assert harness.contexts[0].verify_mode == ssl.CERT_REQUIRED

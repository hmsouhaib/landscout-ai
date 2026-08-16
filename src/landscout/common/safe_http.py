"""Narrow outbound HTTPS transport with DNS-to-socket binding.

The helpers in this module are internal.  They deliberately avoid ambient
proxy configuration and connect a TLS socket only to an address returned by
the validation lookup performed for that exact request hop.
"""

from __future__ import annotations

import http.client
import ipaddress
import re
import socket
import ssl
from collections.abc import Mapping
from dataclasses import dataclass
from math import isfinite
from numbers import Real
from types import TracebackType
from typing import Self
from urllib.parse import SplitResult, urljoin, urlsplit, urlunsplit
from urllib.request import Request

_REDIRECT_STATUSES = frozenset({301, 302, 303, 307, 308})
_DEFAULT_MAX_REDIRECTS = 10
_NUMERIC_HOST_PATTERN = re.compile(r"^[0-9A-Fa-fxX.]+$")
_HEADER_NAME_PATTERN = re.compile(r"^[!#$%&'*+\-.^_`|~0-9A-Za-z]+$")


class SafeHttpsError(OSError):
    """Raised when an outbound HTTPS destination or exchange is unsafe."""


@dataclass(frozen=True)
class _ResolvedAddress:
    family: int
    address: ipaddress.IPv4Address | ipaddress.IPv6Address

    @property
    def socket_address(self) -> tuple[object, ...]:
        if self.family == socket.AF_INET:
            return (str(self.address), self.port)
        return (str(self.address), self.port, 0, 0)

    # The port is attached after resolution so the address remains an exact,
    # immutable description of the validated endpoint.
    port: int


@dataclass(frozen=True)
class _ResolvedDestination:
    url: str
    hostname: str
    port: int
    request_target: str
    addresses: tuple[_ResolvedAddress, ...]


def _is_globally_routable_address(
    address: ipaddress.IPv4Address | ipaddress.IPv6Address,
) -> bool:
    if (
        not address.is_global
        or address.is_private
        or address.is_loopback
        or address.is_link_local
        or address.is_unspecified
        or address.is_multicast
        or address.is_reserved
    ):
        return False
    if isinstance(address, ipaddress.IPv6Address):
        mapped = address.ipv4_mapped
        if mapped is not None and not _is_globally_routable_address(mapped):
            return False
    return True


def _strict_literal_address(
    hostname: str,
) -> ipaddress.IPv4Address | ipaddress.IPv6Address | None:
    try:
        return ipaddress.ip_address(hostname)
    except ValueError:
        pass

    # inet_aton recognises legacy IPv4 spellings such as 127.1.  They are
    # interpreted here only so that they can be subjected to the same public
    # address gate without a second DNS lookup.
    try:
        packed = socket.inet_aton(hostname)
    except OSError:
        packed = None
    if packed is not None:
        return ipaddress.ip_address(packed)

    if hostname.isdecimal() or hostname.casefold().startswith("0x"):
        base = 16 if hostname.casefold().startswith("0x") else 10
        try:
            return ipaddress.IPv4Address(int(hostname, base))
        except (ValueError, ipaddress.AddressValueError, OverflowError) as error:
            raise SafeHttpsError("Malformed numeric IP destination") from error

    # A host made entirely from numeric-IP syntax must not fall through to
    # ordinary DNS merely because its numeric representation is malformed.
    if any(character.isdigit() for character in hostname) and _NUMERIC_HOST_PATTERN.fullmatch(
        hostname
    ):
        raise SafeHttpsError("Malformed numeric IP destination")
    return None


def _resolve_public_addresses(
    hostname: str,
    port: int,
) -> tuple[_ResolvedAddress, ...]:
    try:
        records = socket.getaddrinfo(hostname, port, type=socket.SOCK_STREAM)
        addresses: dict[
            tuple[int, int],
            _ResolvedAddress,
        ] = {}
        for record in records:
            if type(record) is not tuple or len(record) != 5:
                raise TypeError("DNS result must be a five-item tuple")
            family, socket_type, protocol, canonical_name, sockaddr = record
            if family == socket.AF_INET:
                expected_version = 4
                expected_sockaddr_length = 2
            elif family == socket.AF_INET6:
                expected_version = 6
                expected_sockaddr_length = 4
            else:
                raise ValueError("DNS result uses an unsupported address family")
            if socket_type != socket.SOCK_STREAM:
                raise ValueError("DNS result is not a stream address")
            if type(protocol) is not int or protocol not in {
                0,
                socket.IPPROTO_TCP,
            }:
                raise ValueError("DNS result is not a TCP-compatible address")
            if type(canonical_name) is not str:
                raise TypeError("DNS canonical name must be a string")
            if type(sockaddr) is not tuple or len(sockaddr) != expected_sockaddr_length:
                raise TypeError("DNS result has an invalid socket address")
            validated_sockaddr: tuple[object, ...] = tuple(sockaddr)
            if (
                type(validated_sockaddr[0]) is not str
                or type(validated_sockaddr[1]) is not int
            ):
                raise TypeError("DNS result has an invalid socket address")
            if validated_sockaddr[1] != port:
                raise ValueError("DNS result uses an unexpected destination port")
            if expected_version == 6 and (
                type(validated_sockaddr[2]) is not int
                or type(validated_sockaddr[3]) is not int
            ):
                raise TypeError("DNS result has an invalid IPv6 socket address")
            address = ipaddress.ip_address(validated_sockaddr[0])
            if address.version != expected_version:
                raise ValueError("DNS address family does not match its IP address")
            if not _is_globally_routable_address(address):
                raise SafeHttpsError(
                    f"DNS resolved {hostname} to a non-public address"
                )
            addresses[(address.version, int(address))] = _ResolvedAddress(
                family=family,
                address=address,
                port=port,
            )
        if not addresses:
            raise ValueError("DNS resolution returned no usable address")
        return tuple(addresses[key] for key in sorted(addresses))
    except SafeHttpsError:
        raise
    except (
        OSError,
        UnicodeError,
        IndexError,
        TypeError,
        ValueError,
        OverflowError,
    ) as error:
        raise SafeHttpsError(f"DNS resolution failed for host: {hostname}") from error


def _canonical_hostname(hostname: str) -> str:
    if not hostname:
        raise SafeHttpsError("HTTPS URL hostname is empty")
    try:
        canonical = (
            hostname.encode("idna").decode("ascii").casefold().rstrip(".")
        )
    except UnicodeError as error:
        raise SafeHttpsError("HTTPS URL hostname is malformed") from error
    if not canonical:
        raise SafeHttpsError("HTTPS URL hostname is empty")
    if canonical == "localhost" or canonical.endswith(".localhost"):
        raise SafeHttpsError("Localhost HTTPS destinations are forbidden")
    return canonical


def _canonical_url(parsed: SplitResult, hostname: str, port: int) -> str:
    address = _strict_literal_address(hostname)
    host_text = f"[{hostname}]" if address is not None and address.version == 6 else hostname
    netloc = host_text if port == 443 else f"{host_text}:{port}"
    return urlunsplit(("https", netloc, parsed.path or "/", parsed.query, ""))


def _resolve_destination(value: str) -> _ResolvedDestination:
    try:
        if type(value) is not str or not value:
            raise TypeError("HTTPS URL must be an exact non-empty string")
        if any(ord(character) < 32 or ord(character) == 127 for character in value):
            raise ValueError("HTTPS URL contains a control character")
        parsed = urlsplit(value)
        if parsed.scheme.casefold() != "https" or parsed.hostname is None:
            raise ValueError("Remote URL must use HTTPS and include a hostname")
        if parsed.username is not None or parsed.password is not None:
            raise ValueError("Remote URL credentials are forbidden")
        if parsed.fragment:
            raise ValueError("Remote URL fragments are forbidden")
        hostname = _canonical_hostname(parsed.hostname)
        port = 443 if parsed.port is None else parsed.port
        if not 1 <= port <= 65535:
            raise ValueError("HTTPS URL port is invalid")
        literal = _strict_literal_address(hostname)
        if literal is None:
            addresses = _resolve_public_addresses(hostname, port)
        else:
            if not _is_globally_routable_address(literal):
                raise ValueError("Non-public IP HTTPS destinations are forbidden")
            family = socket.AF_INET if literal.version == 4 else socket.AF_INET6
            addresses = (_ResolvedAddress(family, literal, port),)
        request_target = parsed.path or "/"
        if parsed.query:
            request_target = f"{request_target}?{parsed.query}"
        return _ResolvedDestination(
            url=_canonical_url(parsed, hostname, port),
            hostname=hostname,
            port=port,
            request_target=request_target,
            addresses=addresses,
        )
    except SafeHttpsError:
        raise
    except (
        AttributeError,
        IndexError,
        TypeError,
        UnicodeError,
        ValueError,
        OverflowError,
    ) as error:
        raise SafeHttpsError(f"Unsafe HTTPS URL: {value}") from error


class _BoundHTTPSConnection(http.client.HTTPSConnection):
    """HTTPS connection whose transport endpoint is one validated IP."""

    def __init__(
        self,
        hostname: str,
        port: int,
        address: _ResolvedAddress,
        *,
        timeout: float,
        context: ssl.SSLContext,
    ) -> None:
        super().__init__(hostname, port=port, timeout=timeout, context=context)
        self._validated_address = address
        self._tls_context = context

    def connect(self) -> None:
        if getattr(self, "_tunnel_host", None) is not None:
            raise SafeHttpsError("HTTPS proxy tunnels are forbidden")
        raw_socket = socket.socket(
            self._validated_address.family,
            socket.SOCK_STREAM,
        )
        try:
            raw_socket.settimeout(self.timeout)
            raw_socket.connect(self._validated_address.socket_address)
            peer = raw_socket.getpeername()
            if type(peer) is not tuple or not peer or type(peer[0]) is not str:
                raise SafeHttpsError("Connected HTTPS peer address is malformed")
            peer_address = ipaddress.ip_address(peer[0].split("%", maxsplit=1)[0])
            if peer_address != self._validated_address.address:
                raise SafeHttpsError(
                    "Connected HTTPS peer differs from the validated DNS address"
                )
            self.sock = self._tls_context.wrap_socket(
                raw_socket,
                server_hostname=self.host,
            )
        except Exception:
            raw_socket.close()
            raise


class SafeHttpsResponse:
    """Streaming final response returned by :func:`open_safe_https`."""

    def __init__(
        self,
        response: http.client.HTTPResponse,
        connection: _BoundHTTPSConnection,
        *,
        url: str,
        history: tuple[str, ...],
    ) -> None:
        self._response = response
        self._connection = connection
        self.url = url
        self.history = history
        self.status = response.status
        self.headers = response.headers
        self._closed = False

    def read(self, amount: int | None = None) -> bytes:
        try:
            return self._response.read(amount)
        except Exception as error:
            raise SafeHttpsError("HTTPS response stream failed") from error

    def close(self) -> None:
        if self._closed:
            return
        self._closed = True
        try:
            self._response.close()
        finally:
            self._connection.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        self.close()


def _validated_timeout(value: object) -> float:
    if isinstance(value, bool) or not isinstance(value, Real):
        raise SafeHttpsError("HTTPS timeout must be a strict positive finite number")
    try:
        timeout = float(value)
    except (OverflowError, TypeError, ValueError) as error:
        raise SafeHttpsError(
            "HTTPS timeout must be a strict positive finite number"
        ) from error
    if not isfinite(timeout) or timeout <= 0:
        raise SafeHttpsError("HTTPS timeout must be a strict positive finite number")
    return timeout


def _request_parts(
    value: str | Request,
    supplied_headers: Mapping[str, str] | None,
) -> tuple[str, dict[str, str]]:
    if isinstance(value, Request):
        if value.data is not None or value.get_method().upper() != "GET":
            raise SafeHttpsError("Safe HTTPS source transport supports GET only")
        url = value.full_url
        combined = dict(value.header_items())
    elif type(value) is str:
        url = value
        combined = {}
    else:
        raise SafeHttpsError("HTTPS request must be an exact URL string or Request")
    if supplied_headers is not None:
        if not isinstance(supplied_headers, Mapping):
            raise SafeHttpsError("HTTPS request headers must be a mapping")
        combined.update(supplied_headers)
    output: dict[str, str] = {}
    for name, header_value in combined.items():
        if type(name) is not str or type(header_value) is not str:
            raise SafeHttpsError("HTTPS header names and values must be exact strings")
        if _HEADER_NAME_PATTERN.fullmatch(name) is None:
            raise SafeHttpsError("HTTPS header name is invalid")
        if name.casefold() == "host":
            raise SafeHttpsError("Caller-supplied Host headers are forbidden")
        if any(
            ord(character) < 32 or ord(character) == 127
            for character in name + header_value
        ):
            raise SafeHttpsError("HTTPS headers contain control characters")
        output[name] = header_value
    output["Connection"] = "close"
    return url, output


def _open_destination(
    destination: _ResolvedDestination,
    timeout: float,
    headers: Mapping[str, str],
) -> tuple[http.client.HTTPResponse, _BoundHTTPSConnection]:
    context = ssl.create_default_context()
    last_error: BaseException | None = None
    for address in destination.addresses:
        connection = _BoundHTTPSConnection(
            destination.hostname,
            destination.port,
            address,
            timeout=timeout,
            context=context,
        )
        try:
            connection.request(
                "GET",
                destination.request_target,
                headers=dict(headers),
            )
            return connection.getresponse(), connection
        except SafeHttpsError:
            connection.close()
            raise
        except ssl.SSLError as error:
            connection.close()
            raise SafeHttpsError("HTTPS TLS verification failed") from error
        except (OSError, http.client.HTTPException) as error:
            last_error = error
            connection.close()
    raise SafeHttpsError(
        "Every validated HTTPS destination address failed"
    ) from last_error


def _redirect_location(response: http.client.HTTPResponse) -> str:
    values = response.headers.get_all("Location", failobj=[])
    if len(values) != 1 or type(values[0]) is not str or not values[0]:
        raise SafeHttpsError("HTTPS redirect requires exactly one Location header")
    return values[0]


def open_safe_https(
    url: str | Request,
    *,
    timeout: float,
    headers: Mapping[str, str] | None = None,
    max_redirects: int = _DEFAULT_MAX_REDIRECTS,
) -> SafeHttpsResponse:
    """Open one source GET with validated redirects and a bound TLS socket."""

    validated_timeout = _validated_timeout(timeout)
    if type(max_redirects) is not int or max_redirects < 0:
        raise SafeHttpsError("max_redirects must be a non-negative integer")
    current_url, request_headers = _request_parts(url, headers)
    history: list[str] = []
    seen: set[str] = set()

    while True:
        destination = _resolve_destination(current_url)
        if destination.url in seen:
            raise SafeHttpsError("HTTPS redirect loop detected")
        seen.add(destination.url)
        response: http.client.HTTPResponse | None = None
        connection: _BoundHTTPSConnection | None = None
        try:
            response, connection = _open_destination(
                destination,
                validated_timeout,
                request_headers,
            )
            status = response.status
            if status in _REDIRECT_STATUSES:
                if len(history) >= max_redirects:
                    raise SafeHttpsError("HTTPS redirect limit exceeded")
                location = _redirect_location(response)
                history.append(destination.url)
                current_url = urljoin(destination.url, location)
                continue
            if not 200 <= status < 300:
                raise SafeHttpsError(f"HTTPS source returned status {status}")
            return SafeHttpsResponse(
                response,
                connection,
                url=destination.url,
                history=tuple(history),
            )
        except SafeHttpsError:
            raise
        except (OSError, http.client.HTTPException, ValueError) as error:
            raise SafeHttpsError("Safe HTTPS exchange failed") from error
        finally:
            if response is not None and (
                response.status in _REDIRECT_STATUSES
                or not 200 <= response.status < 300
            ):
                response.close()
                if connection is not None:
                    connection.close()

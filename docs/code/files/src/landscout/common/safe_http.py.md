# `src/landscout/common/safe_http.py`

## File identity

- Repository path: `src/landscout/common/safe_http.py`
- File type: Python source
- Layer: internal common contract
- Domain: common contract
- Responsibility: Implements the shared HTTPS trust boundary that binds validated DNS answers to the actual TLS socket and owns redirects.
- Source SHA256: `f63952179ee94bf8e4838f2658e7f7b7dbd7e4b91bc4e532eb1a44f1e2b5133f`

## 1. Purpose

Implements the shared HTTPS trust boundary that binds validated DNS answers to the actual TLS socket and owns redirects.

## 2. Position in LandScout architecture

This file belongs to the **internal common contract** layer and the **common contract** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `import http.client`
- `import ipaddress`
- `import re`
- `import socket`
- `import ssl`
- `from collections.abc import Mapping`
- `from dataclasses import dataclass`
- `from math import isfinite`
- `from numbers import Real`
- `from types import TracebackType`
- `from typing import Self`
- `from urllib.parse import SplitResult, urljoin, urlsplit, urlunsplit`
- `from urllib.request import Request`

### Third-party packages

- `None.`

### Internal LandScout imports

- `None.`

## 4. Contract taxonomy

### A. Python constants

#### `_REDIRECT_STATUSES`

```python
_REDIRECT_STATUSES = frozenset({301, 302, 303, 307, 308})
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema.

#### `_DEFAULT_MAX_REDIRECTS`

```python
_DEFAULT_MAX_REDIRECTS = 10
```

Module-level technical/source/policy constant consumed by the exact references below.

#### `_NUMERIC_HOST_PATTERN`

```python
_NUMERIC_HOST_PATTERN = re.compile(r"^[0-9A-Fa-fxX.]+$")
```

Compiled/text regular expression used by the named validation path; the fenced declaration preserves every metacharacter exactly.

#### `_HEADER_NAME_PATTERN`

```python
_HEADER_NAME_PATTERN = re.compile(r"^[!#$%&'*+\-.^_`|~0-9A-Za-z]+$")
```

Compiled/text regular expression used by the named validation path; the fenced declaration preserves every metacharacter exactly.


### B. Type aliases and closed domains

No module-level Literal/Annotated/TypeAlias declaration is present.

### C. Meaningful dunder contracts

No meaningful module-level dunder contract is declared.

### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

### `SafeHttpsError`

**Purpose:** Raised when an outbound HTTPS destination or exchange is unsafe.

**Kind:** controlled exception.

**Inheritance:** `OSError`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- direct call or construction: `src/landscout/common/safe_http.py::_strict_literal_address` via `SafeHttpsError`.
- direct call or construction: `src/landscout/common/safe_http.py::_resolve_public_addresses` via `SafeHttpsError`.
- direct call or construction: `src/landscout/common/safe_http.py::_canonical_hostname` via `SafeHttpsError`.
- direct call or construction: `src/landscout/common/safe_http.py::_resolve_destination` via `SafeHttpsError`.
- direct call or construction: `src/landscout/common/safe_http.py::_BoundHTTPSConnection.connect` via `SafeHttpsError`.
- direct call or construction: `src/landscout/common/safe_http.py::SafeHttpsResponse.read` via `SafeHttpsError`.
- direct call or construction: `src/landscout/common/safe_http.py::_validated_timeout` via `SafeHttpsError`.
- direct call or construction: `src/landscout/common/safe_http.py::_request_parts` via `SafeHttpsError`.
- direct call or construction: `src/landscout/common/safe_http.py::_open_destination` via `SafeHttpsError`.
- direct call or construction: `src/landscout/common/safe_http.py::_redirect_location` via `SafeHttpsError`.
- direct call or construction: `src/landscout/common/safe_http.py::open_safe_https` via `SafeHttpsError`.
- import/re-export: `src/landscout/sources/inpn_protected_areas_fr.py::<module>` via `from landscout.common.safe_http import SafeHttpsError, open_safe_https`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::_Session.open` via `SafeHttpsError`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::test_coordinated_cache_and_metadata_snapshot_change_is_not_a_cache_hit` via `SafeHttpsError`.
- import/re-export: `tests/unit/test_inpn_protected_areas_fr.py::<module>` via `from landscout.common.safe_http import SafeHttpsError`.
- callback/function object: `tests/unit/test_safe_http.py::test_malformed_or_unusable_dns_results_fail_before_socket` via `pytest.raises(SafeHttpsError, match='DNS|address')`.
- callback/function object: `tests/unit/test_safe_http.py::test_any_nonpublic_dns_answer_fails_before_socket` via `pytest.raises(SafeHttpsError, match='public|global|address|DNS')`.
- callback/function object: `tests/unit/test_safe_http.py::test_mixed_public_private_dns_answer_fails_closed` via `pytest.raises(SafeHttpsError, match='public|global|address|DNS')`.
- callback/function object: `tests/unit/test_safe_http.py::test_dns_errors_are_controlled_before_socket` via `pytest.raises(SafeHttpsError, match='DNS|resolve')`.
- callback/function object: `tests/unit/test_safe_http.py::test_unsafe_url_identity_fails_before_dns` via `pytest.raises(SafeHttpsError, match='HTTPS|credential|localhost|host|URL')`.
- callback/function object: `tests/unit/test_safe_http.py::test_literal_and_malformed_numeric_ip_rejection_never_uses_dns` via `pytest.raises(SafeHttpsError, match='public|global|address|IP|URL')`.
- callback/function object: `tests/unit/test_safe_http.py::test_unsafe_redirect_is_rejected_before_target_socket` via `pytest.raises(SafeHttpsError, match='public|global|address|DNS')`.
- callback/function object: `tests/unit/test_safe_http.py::test_redirect_loop_is_rejected` via `pytest.raises(SafeHttpsError, match='loop')`.
- callback/function object: `tests/unit/test_safe_http.py::test_redirect_limit_is_enforced` via `pytest.raises(SafeHttpsError, match='redirect')`.
- callback/function object: `tests/unit/test_safe_http.py::test_malformed_header_name_is_rejected_before_dns` via `pytest.raises(SafeHttpsError, match='header|Host')`.
- import/re-export: `tests/unit/test_safe_http.py::<module>` via `from landscout.common.safe_http import SafeHttpsError, open_safe_https`.

**Exact class source**

```python
class SafeHttpsError(OSError):
    """Raised when an outbound HTTPS destination or exchange is unsafe."""
```

### `_ResolvedAddress`

**Purpose:** One validated public IPv4 or IPv6 destination and the numeric socket endpoint derived from the same DNS snapshot.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `family` | `family: int` | AF_INET or AF_INET6 socket family validated from one getaddrinfo record. |
| `address` | `address: ipaddress.IPv4Address \| ipaddress.IPv6Address` | Globally routable parsed IPv4/IPv6 address from the validated DNS snapshot. |
| `port` | `port: int` | Validated HTTPS destination port attached to the immutable numeric endpoint. |

**Interface consumers**

- direct call or construction: `src/landscout/common/safe_http.py::_resolve_public_addresses` via `_ResolvedAddress`.
- direct call or construction: `src/landscout/common/safe_http.py::_resolve_destination` via `_ResolvedAddress`.

**Exact class source**

```python
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
```

### `_ResolvedDestination`

**Purpose:** Canonical request identity plus the complete validated public-address set for one HTTPS hop.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `url` | `url: str` | Exact source/evidence URL whose HTTPS/origin/path constraints are enforced by the owning configuration or source validator. |
| `hostname` | `hostname: str` | Stores `_ResolvedDestination`'s `hostname` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `port` | `port: int` | Stores `_ResolvedDestination`'s `port` value under exact annotation `int`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `request_target` | `request_target: str` | Stores `_ResolvedDestination`'s `request target` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `addresses` | `addresses: tuple[_ResolvedAddress, ...]` | Structured `addresses` collection owned by `_ResolvedDestination`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |

**Interface consumers**

- direct call or construction: `src/landscout/common/safe_http.py::_resolve_destination` via `_ResolvedDestination`.

**Exact class source**

```python
class _ResolvedDestination:
    url: str
    hostname: str
    port: int
    request_target: str
    addresses: tuple[_ResolvedAddress, ...]
```

### `_BoundHTTPSConnection`

**Purpose:** HTTPS connection whose transport endpoint is one validated IP.

**Kind:** class.

**Inheritance:** `http.client.HTTPSConnection`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `_validated_address` | `self._validated_address = address  # assigned in __init__` | Stores `_BoundHTTPSConnection`'s ` validated address` value under exact annotation `not explicitly annotated`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `_tls_context` | `self._tls_context = context  # assigned in __init__` | `_BoundHTTPSConnection`'s ` tls context` evidence/text field; it retains the exact configured or source meaning under annotation `not explicitly annotated` and is not promoted to a legal conclusion. |
| `sock` | `self.sock = self._tls_context.wrap_socket(raw_socket, server_hostname=self.host)  # assigned in connect` | Stores `_BoundHTTPSConnection`'s `sock` value under exact annotation `not explicitly annotated`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |

**Interface consumers**

- direct call or construction: `src/landscout/common/safe_http.py::_open_destination` via `_BoundHTTPSConnection`.

**Exact class source**

```python
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
```

### `SafeHttpsResponse`

**Purpose:** Streaming final response returned by :func:`open_safe_https`.

**Kind:** class.

**Inheritance:** plain object.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `_response` | `self._response = response  # assigned in __init__` | Stores `SafeHttpsResponse`'s ` response` value under exact annotation `not explicitly annotated`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `_connection` | `self._connection = connection  # assigned in __init__` | Stores `SafeHttpsResponse`'s ` connection` value under exact annotation `not explicitly annotated`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `url` | `self.url = url  # assigned in __init__` | Exact source/evidence URL whose HTTPS/origin/path constraints are enforced by the owning configuration or source validator. |
| `history` | `self.history = history  # assigned in __init__` | Stores `SafeHttpsResponse`'s `history` value under exact annotation `not explicitly annotated`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `status` | `self.status = response.status  # assigned in __init__` | Closed or validated `status` classification on `SafeHttpsResponse`; accepted values and downstream branches are recoverable from the reproduced validators and consumers. |
| `headers` | `self.headers = response.headers  # assigned in __init__` | Stores `SafeHttpsResponse`'s `headers` value under exact annotation `not explicitly annotated`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `_closed` | `self._closed = False  # assigned in __init__` | Stores `SafeHttpsResponse`'s ` closed` value under exact annotation `not explicitly annotated`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |

**Interface consumers**

- direct call or construction: `src/landscout/common/safe_http.py::open_safe_https` via `SafeHttpsResponse`.

**Exact class source**

```python
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
```


## 6. Functions and methods

### `_ResolvedAddress.socket_address`

**Exact signature**

```python
def socket_address(self) -> tuple[object, ...]:
```

**Purpose**

Private `common contract` helper for socket address; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[object, ...]`.
- Every observed return expression is reproduced without truncation:
```python
(str(self.address), self.port, 0, 0)

(str(self.address), self.port)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- callback/property argument: `src/landscout/common/safe_http.py::_BoundHTTPSConnection.connect` via `raw_socket.connect(self._validated_address.socket_address)`.
- property/attribute access: `src/landscout/common/safe_http.py::_BoundHTTPSConnection.connect` via `self._validated_address.socket_address`.

**Complete source-ordered implementation**

```python
def socket_address(self) -> tuple[object, ...]:
        if self.family == socket.AF_INET:
            return (str(self.address), self.port)
        return (str(self.address), self.port, 0, 0)
```

**Business boundary**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `_is_globally_routable_address`

**Exact signature**

```python
def _is_globally_routable_address(
    address: ipaddress.IPv4Address | ipaddress.IPv6Address,
) -> bool:
```

**Purpose**

Tests whether globally routable address; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `bool`.
- Every observed return expression is reproduced without truncation:
```python
True

False

False
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/common/safe_http.py::_resolve_public_addresses` via `_is_globally_routable_address`.
- direct call or construction: `src/landscout/common/safe_http.py::_resolve_destination` via `_is_globally_routable_address`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `_strict_literal_address`

**Exact signature**

```python
def _strict_literal_address(
    hostname: str,
) -> ipaddress.IPv4Address | ipaddress.IPv6Address | None:
```

**Purpose**

Private `common contract` helper for strict literal address; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `ipaddress.IPv4Address | ipaddress.IPv6Address | None`.
- Every observed return expression is reproduced without truncation:
```python
None

ipaddress.ip_address(hostname)

ipaddress.ip_address(packed)

ipaddress.IPv4Address(int(hostname, base))
```

**Validation and exceptions**

- Guard with a raise path: `hostname.isdecimal() or hostname.casefold().startswith('0x')`.
- Guard with a raise path: `any((character.isdigit() for character in hostname)) and _NUMERIC_HOST_PATTERN.fullmatch(hostname)`.
- Explicit raise expressions: `SafeHttpsError('Malformed numeric IP destination')`.

**Side effects**

- Network I/O: `socket.inet_aton`.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/common/safe_http.py::_canonical_url` via `_strict_literal_address`.
- direct call or construction: `src/landscout/common/safe_http.py::_resolve_destination` via `_strict_literal_address`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `_resolve_public_addresses`

**Exact signature**

```python
def _resolve_public_addresses(
    hostname: str,
    port: int,
) -> tuple[_ResolvedAddress, ...]:
```

**Purpose**

Resolves public addresses; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `tuple[_ResolvedAddress, ...]`.
- Every observed return expression is reproduced without truncation:
```python
tuple((addresses[key] for key in sorted(addresses)))
```

**Validation and exceptions**

- Guard with a raise path: `not addresses`.
- Guard with a raise path: `type(record) is not tuple or len(record) != 5`.
- Guard with a raise path: `socket_type != socket.SOCK_STREAM`.
- Guard with a raise path: `type(protocol) is not int or protocol not in {0, socket.IPPROTO_TCP}`.
- Guard with a raise path: `type(canonical_name) is not str`.
- Guard with a raise path: `type(sockaddr) is not tuple or len(sockaddr) != expected_sockaddr_length`.
- Guard with a raise path: `type(validated_sockaddr[0]) is not str or type(validated_sockaddr[1]) is not int`.
- Guard with a raise path: `validated_sockaddr[1] != port`.
- Guard with a raise path: `expected_version == 6 and (type(validated_sockaddr[2]) is not int or type(validated_sockaddr[3]) is not int)`.
- Guard with a raise path: `address.version != expected_version`.
- Guard with a raise path: `not _is_globally_routable_address(address)`.
- Explicit raise expressions: `SafeHttpsError(f'DNS resolution failed for host: {hostname}')`, `SafeHttpsError(f'DNS resolved {hostname} to a non-public address')`, `TypeError('DNS canonical name must be a string')`, `TypeError('DNS result has an invalid IPv6 socket address')`, `TypeError('DNS result has an invalid socket address')`, `TypeError('DNS result must be a five-item tuple')`, `ValueError('DNS address family does not match its IP address')`, `ValueError('DNS resolution returned no usable address')`, `ValueError('DNS result is not a TCP-compatible address')`, `ValueError('DNS result is not a stream address')`, `ValueError('DNS result uses an unexpected destination port')`, `ValueError('DNS result uses an unsupported address family')`, `re-raise`.

**Side effects**

- Network I/O: `socket.getaddrinfo`.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: `addresses[address.version, int(address)]`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/common/safe_http.py::_resolve_destination` via `_resolve_public_addresses`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `_canonical_hostname`

**Exact signature**

```python
def _canonical_hostname(hostname: str) -> str:
```

**Purpose**

Private `common contract` helper for canonical hostname; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
canonical
```

**Validation and exceptions**

- Guard with a raise path: `not hostname`.
- Guard with a raise path: `not canonical`.
- Guard with a raise path: `canonical == 'localhost' or canonical.endswith('.localhost')`.
- Explicit raise expressions: `SafeHttpsError('HTTPS URL hostname is empty')`, `SafeHttpsError('HTTPS URL hostname is malformed')`, `SafeHttpsError('Localhost HTTPS destinations are forbidden')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/common/safe_http.py::_resolve_destination` via `_canonical_hostname`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `_canonical_url`

**Exact signature**

```python
def _canonical_url(parsed: SplitResult, hostname: str, port: int) -> str:
```

**Purpose**

Private `common contract` helper for canonical url; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
urlunsplit(('https', netloc, parsed.path or '/', parsed.query, ''))
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/common/safe_http.py::_resolve_destination` via `_canonical_url`.

**Complete source-ordered implementation**

```python
def _canonical_url(parsed: SplitResult, hostname: str, port: int) -> str:
    address = _strict_literal_address(hostname)
    host_text = f"[{hostname}]" if address is not None and address.version == 6 else hostname
    netloc = host_text if port == 443 else f"{host_text}:{port}"
    return urlunsplit(("https", netloc, parsed.path or "/", parsed.query, ""))
```

**Business boundary**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `_resolve_destination`

**Exact signature**

```python
def _resolve_destination(value: str) -> _ResolvedDestination:
```

**Purpose**

Resolves destination; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `_ResolvedDestination`.
- Every observed return expression is reproduced without truncation:
```python
_ResolvedDestination(url=_canonical_url(parsed, hostname, port), hostname=hostname, port=port, request_target=request_target, addresses=addresses)
```

**Validation and exceptions**

- Guard with a raise path: `type(value) is not str or not value`.
- Guard with a raise path: `any((ord(character) < 32 or ord(character) == 127 for character in value))`.
- Guard with a raise path: `parsed.scheme.casefold() != 'https' or parsed.hostname is None`.
- Guard with a raise path: `parsed.username is not None or parsed.password is not None`.
- Guard with a raise path: `parsed.fragment`.
- Guard with a raise path: `not 1 <= port <= 65535`.
- Guard with a raise path: `not _is_globally_routable_address(literal)`.
- Explicit raise expressions: `SafeHttpsError(f'Unsafe HTTPS URL: {value}')`, `TypeError('HTTPS URL must be an exact non-empty string')`, `ValueError('HTTPS URL contains a control character')`, `ValueError('HTTPS URL port is invalid')`, `ValueError('Non-public IP HTTPS destinations are forbidden')`, `ValueError('Remote URL credentials are forbidden')`, `ValueError('Remote URL fragments are forbidden')`, `ValueError('Remote URL must use HTTPS and include a hostname')`, `re-raise`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/common/safe_http.py::open_safe_https` via `_resolve_destination`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `_BoundHTTPSConnection.__init__`

**Exact signature**

```python
def __init__(
        self,
        hostname: str,
        port: int,
        address: _ResolvedAddress,
        *,
        timeout: float,
        context: ssl.SSLContext,
    ) -> None:
```

**Purpose**

Private `common contract` helper for init; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: `self._tls_context`, `self._validated_address`.
- Input mutation: `self._tls_context`, `self._validated_address`.

**Repository interfaces and consumers**


**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `_BoundHTTPSConnection.connect`

**Exact signature**

```python
def connect(self) -> None:
```

**Purpose**

Private `common contract` helper for connect; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `getattr(self, '_tunnel_host', None) is not None`.
- Guard with a raise path: `type(peer) is not tuple or not peer or type(peer[0]) is not str`.
- Guard with a raise path: `peer_address != self._validated_address.address`.
- Explicit raise expressions: `SafeHttpsError('Connected HTTPS peer address is malformed')`, `SafeHttpsError('Connected HTTPS peer differs from the validated DNS address')`, `SafeHttpsError('HTTPS proxy tunnels are forbidden')`, `re-raise`.

**Side effects**

- Network I/O: `raw_socket.close`, `raw_socket.connect`, `raw_socket.getpeername`, `raw_socket.settimeout`, `self._tls_context.wrap_socket`, `socket.socket`.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: `self.sock`.
- Input mutation: `self.sock`.

**Repository interfaces and consumers**


**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `SafeHttpsResponse.__init__`

**Exact signature**

```python
def __init__(
        self,
        response: http.client.HTTPResponse,
        connection: _BoundHTTPSConnection,
        *,
        url: str,
        history: tuple[str, ...],
    ) -> None:
```

**Purpose**

Private `common contract` helper for init; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: `self._closed`, `self._connection`, `self._response`, `self.headers`, `self.history`, `self.status`, `self.url`.
- Input mutation: `self._closed`, `self._connection`, `self._response`, `self.headers`, `self.history`, `self.status`, `self.url`.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/common/safe_http.py::_BoundHTTPSConnection.__init__` via `super().__init__`.
- property/attribute access: `src/landscout/common/safe_http.py::_BoundHTTPSConnection.__init__` via `super().__init__`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `SafeHttpsResponse.read`

**Exact signature**

```python
def read(self, amount: int | None = None) -> bytes:
```

**Purpose**

Reads read; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `bytes`.
- Every observed return expression is reproduced without truncation:
```python
self._response.read(amount)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `SafeHttpsError('HTTPS response stream failed')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/sources/cadastre_fr.py::_sha256` via `stream.read`.
- property/attribute access: `src/landscout/sources/cadastre_fr.py::_sha256` via `stream.read`.
- direct call or construction: `src/landscout/sources/cadastre_fr.py::_is_valid_gzip` via `stream.read`.
- property/attribute access: `src/landscout/sources/cadastre_fr.py::_is_valid_gzip` via `stream.read`.
- direct call or construction: `src/landscout/sources/cadastre_loader_fr.py::_validate_download` via `stream.read`.
- property/attribute access: `src/landscout/sources/cadastre_loader_fr.py::_validate_download` via `stream.read`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_request_json` via `response.read`.
- property/attribute access: `src/landscout/sources/gpu_fr.py::_request_json` via `response.read`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_sha256` via `stream.read`.
- property/attribute access: `src/landscout/sources/gpu_fr.py::_sha256` via `stream.read`.
- direct call or construction: `src/landscout/sources/ign_bdtopo_fr.py::_calculate_checksums` via `stream.read`.
- property/attribute access: `src/landscout/sources/ign_bdtopo_fr.py::_calculate_checksums` via `stream.read`.
- direct call or construction: `src/landscout/sources/ign_bdtopo_fr.py::_geopackage_integrity` via `stream.read`.
- property/attribute access: `src/landscout/sources/ign_bdtopo_fr.py::_geopackage_integrity` via `stream.read`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::_sha256_file` via `stream.read`.
- property/attribute access: `src/landscout/sources/inpn_protected_areas_fr.py::_sha256_file` via `stream.read`.
- direct call or construction: `src/landscout/sources/rte_odre_fr.py::_read_response_json` via `response.read`.
- property/attribute access: `src/landscout/sources/rte_odre_fr.py::_read_response_json` via `response.read`.
- direct call or construction: `src/landscout/sources/rte_odre_fr.py::_sha256` via `stream.read`.
- property/attribute access: `src/landscout/sources/rte_odre_fr.py::_sha256` via `stream.read`.
- direct call or construction: `src/landscout/stages/index_planning_regulation.py::_file_sha256` via `stream.read`.
- property/attribute access: `src/landscout/stages/index_planning_regulation.py::_file_sha256` via `stream.read`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild` via `monkeypatch.setattr(module, '_read_verified_artifact', read)`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::_Response.iter_content` via `self.raw.read`.
- property/attribute access: `tests/unit/test_inpn_protected_areas_fr.py::_Response.iter_content` via `self.raw.read`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::_Response.read` via `self.raw.read`.
- property/attribute access: `tests/unit/test_inpn_protected_areas_fr.py::_Response.read` via `self.raw.read`.
- direct call or construction: `tests/unit/test_safe_http.py::_read` via `response.read`.
- property/attribute access: `tests/unit/test_safe_http.py::_read` via `response.read`.
- direct call or construction: `tests/unit/test_safe_http.py::test_safe_https_redirect_is_manually_revalidated` via `response.read`.
- property/attribute access: `tests/unit/test_safe_http.py::test_safe_https_redirect_is_manually_revalidated` via `response.read`.

**Complete source-ordered implementation**

```python
def read(self, amount: int | None = None) -> bytes:
        try:
            return self._response.read(amount)
        except Exception as error:
            raise SafeHttpsError("HTTPS response stream failed") from error
```

**Business boundary**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `SafeHttpsResponse.close`

**Exact signature**

```python
def close(self) -> None:
```

**Purpose**

Private `common contract` helper for close; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- Every observed return expression is reproduced without truncation:
```python
None
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: `self._closed`.
- Input mutation: `self._closed`.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/common/safe_http.py::_BoundHTTPSConnection.connect` via `raw_socket.close`.
- property/attribute access: `src/landscout/common/safe_http.py::_BoundHTTPSConnection.connect` via `raw_socket.close`.
- direct call or construction: `src/landscout/common/safe_http.py::SafeHttpsResponse.__exit__` via `self.close`.
- property/attribute access: `src/landscout/common/safe_http.py::SafeHttpsResponse.__exit__` via `self.close`.
- direct call or construction: `src/landscout/common/safe_http.py::_open_destination` via `connection.close`.
- property/attribute access: `src/landscout/common/safe_http.py::_open_destination` via `connection.close`.
- direct call or construction: `src/landscout/common/safe_http.py::open_safe_https` via `response.close`.
- property/attribute access: `src/landscout/common/safe_http.py::open_safe_https` via `response.close`.
- direct call or construction: `src/landscout/common/safe_http.py::open_safe_https` via `connection.close`.
- property/attribute access: `src/landscout/common/safe_http.py::open_safe_https` via `connection.close`.
- direct call or construction: `tests/unit/test_gpu_fr.py::_Response.__exit__` via `self.close`.
- property/attribute access: `tests/unit/test_gpu_fr.py::_Response.__exit__` via `self.close`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::_Response.__exit__` via `self.close`.
- property/attribute access: `tests/unit/test_inpn_protected_areas_fr.py::_Response.__exit__` via `self.close`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::_Session.open` via `response.close`.
- property/attribute access: `tests/unit/test_inpn_protected_areas_fr.py::_Session.open` via `response.close`.

**Complete source-ordered implementation**

```python
def close(self) -> None:
        if self._closed:
            return
        self._closed = True
        try:
            self._response.close()
        finally:
            self._connection.close()
```

**Business boundary**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `SafeHttpsResponse.__enter__`

**Exact signature**

```python
def __enter__(self) -> Self:
```

**Purpose**

Private `common contract` helper for enter; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `Self`.
- Every observed return expression is reproduced without truncation:
```python
self
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

**Complete source-ordered implementation**

```python
def __enter__(self) -> Self:
        return self
```

**Business boundary**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `SafeHttpsResponse.__exit__`

**Exact signature**

```python
def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
```

**Purpose**

Private `common contract` helper for exit; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

**Complete source-ordered implementation**

```python
def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        self.close()
```

**Business boundary**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `_validated_timeout`

**Exact signature**

```python
def _validated_timeout(value: object) -> float:
```

**Purpose**

Checks and returns canonical timeout; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `float`.
- Every observed return expression is reproduced without truncation:
```python
timeout
```

**Validation and exceptions**

- Guard with a raise path: `isinstance(value, bool) or not isinstance(value, Real)`.
- Guard with a raise path: `not isfinite(timeout) or timeout <= 0`.
- Explicit raise expressions: `SafeHttpsError('HTTPS timeout must be a strict positive finite number')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/common/safe_http.py::open_safe_https` via `_validated_timeout`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `_request_parts`

**Exact signature**

```python
def _request_parts(
    value: str | Request,
    supplied_headers: Mapping[str, str] | None,
) -> tuple[str, dict[str, str]]:
```

**Purpose**

Private `common contract` helper for request parts; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[str, dict[str, str]]`.
- Every observed return expression is reproduced without truncation:
```python
(url, output)
```

**Validation and exceptions**

- Guard with a raise path: `isinstance(value, Request)`.
- Guard with a raise path: `supplied_headers is not None`.
- Guard with a raise path: `value.data is not None or value.get_method().upper() != 'GET'`.
- Guard with a raise path: `not isinstance(supplied_headers, Mapping)`.
- Guard with a raise path: `type(name) is not str or type(header_value) is not str`.
- Guard with a raise path: `_HEADER_NAME_PATTERN.fullmatch(name) is None`.
- Guard with a raise path: `name.casefold() == 'host'`.
- Guard with a raise path: `any((ord(character) < 32 or ord(character) == 127 for character in name + header_value))`.
- Explicit raise expressions: `SafeHttpsError('Caller-supplied Host headers are forbidden')`, `SafeHttpsError('HTTPS header name is invalid')`, `SafeHttpsError('HTTPS header names and values must be exact strings')`, `SafeHttpsError('HTTPS headers contain control characters')`, `SafeHttpsError('HTTPS request headers must be a mapping')`, `SafeHttpsError('HTTPS request must be an exact URL string or Request')`, `SafeHttpsError('Safe HTTPS source transport supports GET only')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: `output['Connection']`, `output[name]`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/common/safe_http.py::open_safe_https` via `_request_parts`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `_open_destination`

**Exact signature**

```python
def _open_destination(
    destination: _ResolvedDestination,
    timeout: float,
    headers: Mapping[str, str],
) -> tuple[http.client.HTTPResponse, _BoundHTTPSConnection]:
```

**Purpose**

Private `common contract` helper for open destination; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[http.client.HTTPResponse, _BoundHTTPSConnection]`.
- Every observed return expression is reproduced without truncation:
```python
(connection.getresponse(), connection)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `SafeHttpsError('Every validated HTTPS destination address failed')`, `SafeHttpsError('HTTPS TLS verification failed')`, `re-raise`.

**Side effects**

- Network I/O: `connection.getresponse`, `connection.request`.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/common/safe_http.py::open_safe_https` via `_open_destination`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `_redirect_location`

**Exact signature**

```python
def _redirect_location(response: http.client.HTTPResponse) -> str:
```

**Purpose**

Private `common contract` helper for redirect location; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
values[0]
```

**Validation and exceptions**

- Guard with a raise path: `len(values) != 1 or type(values[0]) is not str or (not values[0])`.
- Explicit raise expressions: `SafeHttpsError('HTTPS redirect requires exactly one Location header')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/common/safe_http.py::open_safe_https` via `_redirect_location`.

**Complete source-ordered implementation**

```python
def _redirect_location(response: http.client.HTTPResponse) -> str:
    values = response.headers.get_all("Location", failobj=[])
    if len(values) != 1 or type(values[0]) is not str or not values[0]:
        raise SafeHttpsError("HTTPS redirect requires exactly one Location header")
    return values[0]
```

**Business boundary**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `open_safe_https`

**Exact signature**

```python
def open_safe_https(
    url: str | Request,
    *,
    timeout: float,
    headers: Mapping[str, str] | None = None,
    max_redirects: int = _DEFAULT_MAX_REDIRECTS,
) -> SafeHttpsResponse:
```

**Purpose**

Open one source GET with validated redirects and a bound TLS socket.

**Return contract**

- Declared return annotation: `SafeHttpsResponse`.
- Every observed return expression is reproduced without truncation:
```python
SafeHttpsResponse(response, connection, url=destination.url, history=tuple(history))
```

**Validation and exceptions**

- Guard with a raise path: `type(max_redirects) is not int or max_redirects < 0`.
- Guard with a raise path: `destination.url in seen`.
- Guard with a raise path: `status in _REDIRECT_STATUSES`.
- Guard with a raise path: `not 200 <= status < 300`.
- Guard with a raise path: `len(history) >= max_redirects`.
- Explicit raise expressions: `SafeHttpsError('HTTPS redirect limit exceeded')`, `SafeHttpsError('HTTPS redirect loop detected')`, `SafeHttpsError('Safe HTTPS exchange failed')`, `SafeHttpsError('max_redirects must be a non-negative integer')`, `SafeHttpsError(f'HTTPS source returned status {status}')`, `re-raise`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/sources/cadastre_fr.py::download_cadastre_parcelles` via `open_safe_https`.
- import/re-export: `src/landscout/sources/cadastre_fr.py::<module>` via `from landscout.common.safe_http import open_safe_https`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_request_json` via `open_safe_https`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::download_gpu_document` via `open_safe_https`.
- import/re-export: `src/landscout/sources/gpu_fr.py::<module>` via `from landscout.common.safe_http import open_safe_https`.
- direct call or construction: `src/landscout/sources/ign_bdtopo_fr.py::download_ign_bdtopo_archive` via `open_safe_https`.
- import/re-export: `src/landscout/sources/ign_bdtopo_fr.py::<module>` via `from landscout.common.safe_http import open_safe_https`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::_download_archive_bytes` via `open_safe_https`.
- import/re-export: `src/landscout/sources/inpn_protected_areas_fr.py::<module>` via `from landscout.common.safe_http import SafeHttpsError, open_safe_https`.
- direct call or construction: `src/landscout/sources/rte_odre_fr.py::_read_response_json` via `open_safe_https`.
- direct call or construction: `src/landscout/sources/rte_odre_fr.py::download_rte_odre_dataset` via `open_safe_https`.
- import/re-export: `src/landscout/sources/rte_odre_fr.py::<module>` via `from landscout.common.safe_http import open_safe_https`.
- direct call or construction: `tests/unit/test_safe_http.py::_read` via `open_safe_https`.
- direct call or construction: `tests/unit/test_safe_http.py::test_safe_https_redirect_is_manually_revalidated` via `open_safe_https`.
- direct call or construction: `tests/unit/test_safe_http.py::test_malformed_header_name_is_rejected_before_dns` via `open_safe_https`.
- import/re-export: `tests/unit/test_safe_http.py::<module>` via `from landscout.common.safe_http import SafeHttpsError, open_safe_https`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.


## 7. Data contracts

### Frame-preservation and semantic notes

- HTTP header names such as `Connection` belong to the request-header mapping and are not DataFrame columns.

No module-level canonical frame schema, mapping, or dtype declaration is present. Any frame interaction is recoverable from the complete function implementations below; no string literal is promoted to a column merely because it appears in code.

No enum/status/Literal value is classified as a column unless it is separately present in a canonical schema declaration. Mapping keys, JSON keys, dataclass fields, and configuration leaves remain distinct categories.

## 8. Interfaces

This module does not define `__all__`; no package-export guarantee is inferred from its absence. Symbols can still be imported directly or re-exported by a separate package initializer, as shown by the reference lists.

## 9. Error handling

Controlled exceptions, local raise guards, delegated validators, and framework assertions are documented per exact function implementation. No broader error guarantee is inferred.

## 10. Side effects

Network I/O, filesystem reads/writes, in-memory mutation, input mutation, geometry/CRS calculations, hashing, and process/environment effects are listed separately for every function.

## 11. Security / trust boundaries

Textual URL/provider/hash fields are provenance claims, not physical proof. Physical proof exists only where the reproduced implementation revalidates transport, bytes, archive structure, source layers, geometry, or result hashes.

- Configured source identity: none; the helper is dataset-agnostic.
- URL validation: HTTPS-only, no credentials/fragment/unsafe host/header, strict literal/numeric IP handling, all-address public DNS validation per hop.
- Safe transport: one validated DNS snapshot is converted into numeric socket endpoints; the socket never re-resolves the hostname; peer IP is checked; original hostname remains TLS SNI/certificate and HTTP Host identity; redirects are owned and revalidated.
- Physical bytes/cache/archive/layer/result: not interpreted here. The response is a stream; each adapter owns its byte pins, cache, archive, layer, and result semantics.

## 12. GIS / CRS rules

Only the explicit CRS/geometry validators and calculation copies in this module establish GIS behavior. No geometry repair, reprojection, or metric meaning is inferred from a field name alone.

## 13. Provenance rules

Configured identity, row lineage, byte identity, cache metadata, and source-complete revalidation are separate levels. This companion claims only the levels implemented above.

## 14. Business meaning

The module contributes to the common contract flow through the exact facts, proxy evidence, policy results, diagnostics, or prechecks identified above.

## 15. Explicit non-goals

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

## 16. Tests

Test consumers and framework invocation are included in per-symbol interfaces. Test modules distinguish fixture injection from parameterized values and reproduce setup/action/assertion source.

## 17. Change impact

Any source-byte change invalidates the SHA above. Review exact exports, aliases, canonical frame schemas/dtypes, configured source/policy identities, callers, framework hooks, artifacts, and all linked tests before updating this companion.

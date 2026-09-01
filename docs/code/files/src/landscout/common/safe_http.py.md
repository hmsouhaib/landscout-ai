# `src/landscout/common/safe_http.py`

## File identity

- Repository path: `src/landscout/common/safe_http.py`
- File type: Python source
- Layer: internal common contract
- Domain: shared validation and schema contracts
- Responsibility: Implements the shared HTTPS trust boundary, including numeric DNS-to-TLS binding, caller-header ownership, and manual redirects.
- Source SHA256: `a67d00b8aa312f26e4785813a2dcaa58ffdb8daccc6526c5953c7d521dd13ecf`

## 1. STEP 7F.1A.4 contract delta

- Rejects case-insensitive duplicate and caller-owned credential/hop-by-hop headers before DNS while preserving the DNS-snapshot-to-socket/TLS redirect boundary.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Implements the shared HTTPS trust boundary, including numeric DNS-to-TLS binding, caller-header ownership, and manual redirects.

The file belongs to the **internal common contract** layer and **shared validation and schema contracts** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

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

- None.

### Internal LandScout imports

- None.

## 4. Contract taxonomy

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `_REDIRECT_STATUSES`

- Category: module constant or closed domain.
- Exact declaration:

```python
_REDIRECT_STATUSES = frozenset({301, 302, 303, 307, 308})
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_DEFAULT_MAX_REDIRECTS`

- Category: module constant or closed domain.
- Exact declaration:

```python
_DEFAULT_MAX_REDIRECTS = 10
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_NUMERIC_HOST_PATTERN`

- Category: module constant or closed domain.
- Exact declaration:

```python
_NUMERIC_HOST_PATTERN = re.compile(r"^[0-9A-Fa-fxX.]+$")
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_HEADER_NAME_PATTERN`

- Category: module constant or closed domain.
- Exact declaration:

```python
_HEADER_NAME_PATTERN = re.compile(r"^[!#$%&'*+\-.^_`|~0-9A-Za-z]+$")
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_FORBIDDEN_CALLER_HEADER_NAMES`

- Category: module constant or closed domain.
- Exact declaration:

```python
_FORBIDDEN_CALLER_HEADER_NAMES = frozenset(
    {
        "authorization",
        "proxy-authorization",
        "cookie",
        "cookie2",
        "host",
        "connection",
        "proxy-connection",
        "keep-alive",
        "transfer-encoding",
        "te",
        "trailer",
        "upgrade",
    }
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

### `SafeHttpsError`

**Source purpose:** Raised when an outbound HTTPS destination or exchange is unsafe.

- Exact decorators: none.
- Exact bases: `OSError`.

**Fields and model attributes**

No direct class/model/dataclass or `self` field assignment is declared.

**Qualified consumers**

- constructor call: `landscout.common.safe_http::_strict_literal_address` via `SafeHttpsError`
- value/type reference: `landscout.common.safe_http::_strict_literal_address` via `SafeHttpsError`
- constructor call: `landscout.common.safe_http::_resolve_public_addresses` via `SafeHttpsError`
- value/type reference: `landscout.common.safe_http::_resolve_public_addresses` via `SafeHttpsError`
- constructor call: `landscout.common.safe_http::_canonical_hostname` via `SafeHttpsError`
- value/type reference: `landscout.common.safe_http::_canonical_hostname` via `SafeHttpsError`
- constructor call: `landscout.common.safe_http::_resolve_destination` via `SafeHttpsError`
- value/type reference: `landscout.common.safe_http::_resolve_destination` via `SafeHttpsError`
- constructor call: `landscout.common.safe_http::_BoundHTTPSConnection.connect` via `SafeHttpsError`
- value/type reference: `landscout.common.safe_http::_BoundHTTPSConnection.connect` via `SafeHttpsError`
- constructor call: `landscout.common.safe_http::SafeHttpsResponse.read` via `SafeHttpsError`
- value/type reference: `landscout.common.safe_http::SafeHttpsResponse.read` via `SafeHttpsError`
- constructor call: `landscout.common.safe_http::_validated_timeout` via `SafeHttpsError`
- value/type reference: `landscout.common.safe_http::_validated_timeout` via `SafeHttpsError`
- constructor call: `landscout.common.safe_http::_request_parts` via `SafeHttpsError`
- value/type reference: `landscout.common.safe_http::_request_parts` via `SafeHttpsError`
- constructor call: `landscout.common.safe_http::_open_destination` via `SafeHttpsError`
- value/type reference: `landscout.common.safe_http::_open_destination` via `SafeHttpsError`
- constructor call: `landscout.common.safe_http::_redirect_location` via `SafeHttpsError`
- value/type reference: `landscout.common.safe_http::_redirect_location` via `SafeHttpsError`
- constructor call: `landscout.common.safe_http::open_safe_https` via `SafeHttpsError`
- value/type reference: `landscout.common.safe_http::open_safe_https` via `SafeHttpsError`
- import: `landscout.sources.inpn_protected_areas_fr::<module>` via `from landscout.common.safe_http import SafeHttpsError, open_safe_https`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_download_archive_bytes` via `SafeHttpsError`
- import: `tests.unit.test_inpn_protected_areas_fr::<module>` via `from landscout.common.safe_http import SafeHttpsError`
- constructor call: `tests.unit.test_inpn_protected_areas_fr::_Session.open` via `SafeHttpsError`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::_Session.open` via `SafeHttpsError`
- constructor call: `tests.unit.test_inpn_protected_areas_fr::test_coordinated_cache_and_metadata_snapshot_change_is_not_a_cache_hit` via `SafeHttpsError`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_coordinated_cache_and_metadata_snapshot_change_is_not_a_cache_hit` via `SafeHttpsError`
- import: `tests.unit.test_safe_http::<module>` via `from landscout.common.safe_http import SafeHttpsError, open_safe_https`
- value/type reference: `tests.unit.test_safe_http::test_sensitive_and_hop_by_hop_headers_fail_before_dns` via `SafeHttpsError`
- value/type reference: `tests.unit.test_safe_http::test_case_insensitive_duplicate_header_names_fail_before_dns` via `SafeHttpsError`
- value/type reference: `tests.unit.test_safe_http::test_request_and_explicit_headers_cannot_ambiguously_override_each_other` via `SafeHttpsError`
- value/type reference: `tests.unit.test_safe_http::test_cross_origin_redirect_cannot_receive_a_sensitive_header` via `SafeHttpsError`
- value/type reference: `tests.unit.test_safe_http::test_malformed_or_unusable_dns_results_fail_before_socket` via `SafeHttpsError`
- value/type reference: `tests.unit.test_safe_http::test_any_nonpublic_dns_answer_fails_before_socket` via `SafeHttpsError`
- value/type reference: `tests.unit.test_safe_http::test_mixed_public_private_dns_answer_fails_closed` via `SafeHttpsError`
- value/type reference: `tests.unit.test_safe_http::test_dns_errors_are_controlled_before_socket` via `SafeHttpsError`
- value/type reference: `tests.unit.test_safe_http::test_unsafe_url_identity_fails_before_dns` via `SafeHttpsError`
- value/type reference: `tests.unit.test_safe_http::test_literal_and_malformed_numeric_ip_rejection_never_uses_dns` via `SafeHttpsError`
- value/type reference: `tests.unit.test_safe_http::test_unsafe_redirect_is_rejected_before_target_socket` via `SafeHttpsError`
- value/type reference: `tests.unit.test_safe_http::test_redirect_loop_is_rejected` via `SafeHttpsError`
- value/type reference: `tests.unit.test_safe_http::test_redirect_limit_is_enforced` via `SafeHttpsError`
- value/type reference: `tests.unit.test_safe_http::test_malformed_header_name_is_rejected_before_dns` via `SafeHttpsError`

**Exact class source**

```python
class SafeHttpsError(OSError):
    """Raised when an outbound HTTPS destination or exchange is unsafe."""
```

### `_ResolvedAddress`

**Source purpose:** Defines `_ResolvedAddress`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `family` | `int` | `required` | `family: int` |
| `address` | `ipaddress.IPv4Address \| ipaddress.IPv6Address` | `required` | `address: ipaddress.IPv4Address \| ipaddress.IPv6Address` |
| `port` | `int` | `required` | `port: int` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- constructor call: `landscout.common.safe_http::_resolve_public_addresses` via `_ResolvedAddress`
- value/type reference: `landscout.common.safe_http::_resolve_public_addresses` via `_ResolvedAddress`
- constructor call: `landscout.common.safe_http::_resolve_destination` via `_ResolvedAddress`
- value/type reference: `landscout.common.safe_http::_resolve_destination` via `_ResolvedAddress`
- value/type reference: `landscout.common.safe_http::_BoundHTTPSConnection.__init__` via `_ResolvedAddress`

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

**Source purpose:** Defines `_ResolvedDestination`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `url` | `str` | `required` | `url: str` |
| `hostname` | `str` | `required` | `hostname: str` |
| `port` | `int` | `required` | `port: int` |
| `request_target` | `str` | `required` | `request_target: str` |
| `addresses` | `tuple[_ResolvedAddress, ...]` | `required` | `addresses: tuple[_ResolvedAddress, ...]` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- constructor call: `landscout.common.safe_http::_resolve_destination` via `_ResolvedDestination`
- value/type reference: `landscout.common.safe_http::_resolve_destination` via `_ResolvedDestination`
- value/type reference: `landscout.common.safe_http::_open_destination` via `_ResolvedDestination`

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

**Source purpose:** HTTPS connection whose transport endpoint is one validated IP.

- Exact decorators: none.
- Exact bases: `http.client.HTTPSConnection`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `_validated_address` | `assigned instance field` | `address` | `self._validated_address = address` |
| `_tls_context` | `assigned instance field` | `context` | `self._tls_context = context` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- value/type reference: `landscout.common.safe_http::SafeHttpsResponse.__init__` via `_BoundHTTPSConnection`
- constructor call: `landscout.common.safe_http::_open_destination` via `_BoundHTTPSConnection`
- value/type reference: `landscout.common.safe_http::_open_destination` via `_BoundHTTPSConnection`
- value/type reference: `landscout.common.safe_http::open_safe_https` via `_BoundHTTPSConnection`

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

**Source purpose:** Streaming final response returned by :func:`open_safe_https`.

- Exact decorators: none.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `_response` | `assigned instance field` | `response` | `self._response = response` |
| `_connection` | `assigned instance field` | `connection` | `self._connection = connection` |
| `url` | `assigned instance field` | `url` | `self.url = url` |
| `history` | `assigned instance field` | `history` | `self.history = history` |
| `status` | `assigned instance field` | `response.status` | `self.status = response.status` |
| `headers` | `assigned instance field` | `response.headers` | `self.headers = response.headers` |
| `_closed` | `assigned instance field` | `False` | `self._closed = False` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- constructor call: `landscout.common.safe_http::open_safe_https` via `SafeHttpsResponse`
- value/type reference: `landscout.common.safe_http::open_safe_https` via `SafeHttpsResponse`

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


## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `_ResolvedAddress.socket_address`

**Purpose:** Implements `socket address` within the file role: Implements the shared HTTPS trust boundary, including numeric DNS-to-TLS binding, caller-header ownership, and manual redirects.

**Exact signature**

```python
def socket_address(self) -> tuple[object, ...]:
```

- Exact decorators: `property`.
- Declared return annotation: `tuple[object, ...]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `(str(self.address), self.port)`
  - `(str(self.address), self.port, 0, 0)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `str` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def socket_address(self) -> tuple[object, ...]:
        if self.family == socket.AF_INET:
            return (str(self.address), self.port)
        return (str(self.address), self.port, 0, 0)
```

**Business boundary**

- This contract validates or represents inputs; it does not rank parcels, combine criteria, or create a legal, access, grid-capacity, environmental, or planning conclusion.

### `_is_globally_routable_address`

**Purpose:** Implements `is globally routable address` within the file role: Implements the shared HTTPS trust boundary, including numeric DNS-to-TLS binding, caller-header ownership, and manual redirects.

**Exact signature**

```python
def _is_globally_routable_address(
    address: ipaddress.IPv4Address | ipaddress.IPv6Address,
) -> bool:
```

- Exact decorators: none.
- Declared return annotation: `bool`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `address` | positional-or-keyword | `ipaddress.IPv4Address \| ipaddress.IPv6Address` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `False`
  - `True`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.common.safe_http::_is_globally_routable_address` via `_is_globally_routable_address`
- value/type reference: `landscout.common.safe_http::_is_globally_routable_address` via `_is_globally_routable_address`
- direct call: `landscout.common.safe_http::_resolve_public_addresses` via `_is_globally_routable_address`
- value/type reference: `landscout.common.safe_http::_resolve_public_addresses` via `_is_globally_routable_address`
- direct call: `landscout.common.safe_http::_resolve_destination` via `_is_globally_routable_address`
- value/type reference: `landscout.common.safe_http::_resolve_destination` via `_is_globally_routable_address`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `_is_globally_routable_address` | `landscout.common.safe_http._is_globally_routable_address` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- This contract validates or represents inputs; it does not rank parcels, combine criteria, or create a legal, access, grid-capacity, environmental, or planning conclusion.

### `_strict_literal_address`

**Purpose:** Implements `strict literal address` within the file role: Implements the shared HTTPS trust boundary, including numeric DNS-to-TLS binding, caller-header ownership, and manual redirects.

**Exact signature**

```python
def _strict_literal_address(
    hostname: str,
) -> ipaddress.IPv4Address | ipaddress.IPv6Address | None:
```

- Exact decorators: none.
- Declared return annotation: `ipaddress.IPv4Address | ipaddress.IPv6Address | None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `hostname` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `ipaddress.ip_address(hostname)`
  - `ipaddress.ip_address(packed)`
  - `ipaddress.IPv4Address(int(hostname, base))`
  - `None`
- Explicit raise paths:
  - `SafeHttpsError("Malformed numeric IP destination")` under lexical guard `hostname.isdecimal() or hostname.casefold().startswith("0x")`.
  - `SafeHttpsError("Malformed numeric IP destination")` under lexical guard `any(<br>        character.isdigit() for character in hostname<br>    ) and _NUMERIC_HOST_PATTERN.fullmatch(hostname)`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.common.safe_http::_canonical_url` via `_strict_literal_address`
- value/type reference: `landscout.common.safe_http::_canonical_url` via `_strict_literal_address`
- direct call: `landscout.common.safe_http::_resolve_destination` via `_strict_literal_address`
- value/type reference: `landscout.common.safe_http::_resolve_destination` via `_strict_literal_address`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `ipaddress.ip_address` | `ipaddress.ip_address` |
| `socket.inet_aton` | `socket.inet_aton` |
| `hostname.isdecimal` | `unresolved local/third-party receiver; no ownership inferred` |
| `hostname.casefold().startswith` | `unresolved local/third-party receiver; no ownership inferred` |
| `hostname.casefold` | `unresolved local/third-party receiver; no ownership inferred` |
| `ipaddress.IPv4Address` | `ipaddress.IPv4Address` |
| `int` | `unresolved local/third-party receiver; no ownership inferred` |
| `SafeHttpsError` | `landscout.common.safe_http.SafeHttpsError` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `character.isdigit` | `unresolved local/third-party receiver; no ownership inferred` |
| `_NUMERIC_HOST_PATTERN.fullmatch` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | `socket.inet_aton` |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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
    if any(
        character.isdigit() for character in hostname
    ) and _NUMERIC_HOST_PATTERN.fullmatch(hostname):
        raise SafeHttpsError("Malformed numeric IP destination")
    return None
```

**Business boundary**

- This contract validates or represents inputs; it does not rank parcels, combine criteria, or create a legal, access, grid-capacity, environmental, or planning conclusion.

### `_resolve_public_addresses`

**Purpose:** Implements `resolve public addresses` within the file role: Implements the shared HTTPS trust boundary, including numeric DNS-to-TLS binding, caller-header ownership, and manual redirects.

**Exact signature**

```python
def _resolve_public_addresses(
    hostname: str,
    port: int,
) -> tuple[_ResolvedAddress, ...]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[_ResolvedAddress, ...]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `hostname` | positional-or-keyword | `str` | `required` |
| `port` | positional-or-keyword | `int` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `tuple(addresses[key] for key in sorted(addresses))`
- Explicit raise paths:
  - `TypeError("DNS result must be a five-item tuple")` under lexical guard `type(record) is not tuple or len(record) != 5`.
  - `ValueError("DNS result uses an unsupported address family")` under lexical guard `family == socket.AF_INET`.
  - `ValueError("DNS result is not a stream address")` under lexical guard `socket_type != socket.SOCK_STREAM`.
  - `ValueError("DNS result is not a TCP-compatible address")` under lexical guard `type(protocol) is not int or protocol not in {<br>                0,<br>                socket.IPPROTO_TCP,<br>            }`.
  - `TypeError("DNS canonical name must be a string")` under lexical guard `type(canonical_name) is not str`.
  - `TypeError("DNS result has an invalid socket address")` under lexical guard `type(sockaddr) is not tuple or len(sockaddr) != expected_sockaddr_length`.
  - `TypeError("DNS result has an invalid socket address")` under lexical guard `type(validated_sockaddr[0]) is not str<br>                or type(validated_sockaddr[1]) is not int`.
  - `ValueError("DNS result uses an unexpected destination port")` under lexical guard `validated_sockaddr[1] != port`.
  - `TypeError("DNS result has an invalid IPv6 socket address")` under lexical guard `expected_version == 6 and (<br>                type(validated_sockaddr[2]) is not int<br>                or type(validated_sockaddr[3]) is not int<br>            )`.
  - `ValueError("DNS address family does not match its IP address")` under lexical guard `address.version != expected_version`.
  - `SafeHttpsError(f"DNS resolved {hostname} to a non-public address")` under lexical guard `not _is_globally_routable_address(address)`.
  - `ValueError("DNS resolution returned no usable address")` under lexical guard `not addresses`.
  - `re-raise`.
  - `SafeHttpsError(f"DNS resolution failed for host: {hostname}")`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.common.safe_http::_resolve_destination` via `_resolve_public_addresses`
- value/type reference: `landscout.common.safe_http::_resolve_destination` via `_resolve_public_addresses`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `socket.getaddrinfo` | `socket.getaddrinfo` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `TypeError` | `unresolved local/third-party receiver; no ownership inferred` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `ipaddress.ip_address` | `ipaddress.ip_address` |
| `_is_globally_routable_address` | `landscout.common.safe_http._is_globally_routable_address` |
| `SafeHttpsError` | `landscout.common.safe_http.SafeHttpsError` |
| `int` | `unresolved local/third-party receiver; no ownership inferred` |
| `_ResolvedAddress` | `landscout.common.safe_http._ResolvedAddress` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | `socket.getaddrinfo` |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `addresses[(address.version, int(address))] = _ResolvedAddress(<br>                family=family,<br>                address=address,<br>                port=port,<br>            )` |
| Direct parameter mutation | None directly present. |

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
                raise SafeHttpsError(f"DNS resolved {hostname} to a non-public address")
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

- This contract validates or represents inputs; it does not rank parcels, combine criteria, or create a legal, access, grid-capacity, environmental, or planning conclusion.

### `_canonical_hostname`

**Purpose:** Implements `canonical hostname` within the file role: Implements the shared HTTPS trust boundary, including numeric DNS-to-TLS binding, caller-header ownership, and manual redirects.

**Exact signature**

```python
def _canonical_hostname(hostname: str) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `hostname` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `canonical`
- Explicit raise paths:
  - `SafeHttpsError("HTTPS URL hostname is empty")` under lexical guard `not hostname`.
  - `SafeHttpsError("HTTPS URL hostname is malformed")`.
  - `SafeHttpsError("HTTPS URL hostname is empty")` under lexical guard `not canonical`.
  - `SafeHttpsError("Localhost HTTPS destinations are forbidden")` under lexical guard `canonical == "localhost" or canonical.endswith(".localhost")`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.common.safe_http::_resolve_destination` via `_canonical_hostname`
- value/type reference: `landscout.common.safe_http::_resolve_destination` via `_canonical_hostname`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `SafeHttpsError` | `landscout.common.safe_http.SafeHttpsError` |
| `hostname.encode("idna").decode("ascii").casefold().rstrip` | `unresolved local/third-party receiver; no ownership inferred` |
| `hostname.encode("idna").decode("ascii").casefold` | `unresolved local/third-party receiver; no ownership inferred` |
| `hostname.encode("idna").decode` | `unresolved local/third-party receiver; no ownership inferred` |
| `hostname.encode` | `unresolved local/third-party receiver; no ownership inferred` |
| `canonical.endswith` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _canonical_hostname(hostname: str) -> str:
    if not hostname:
        raise SafeHttpsError("HTTPS URL hostname is empty")
    try:
        canonical = hostname.encode("idna").decode("ascii").casefold().rstrip(".")
    except UnicodeError as error:
        raise SafeHttpsError("HTTPS URL hostname is malformed") from error
    if not canonical:
        raise SafeHttpsError("HTTPS URL hostname is empty")
    if canonical == "localhost" or canonical.endswith(".localhost"):
        raise SafeHttpsError("Localhost HTTPS destinations are forbidden")
    return canonical
```

**Business boundary**

- This contract validates or represents inputs; it does not rank parcels, combine criteria, or create a legal, access, grid-capacity, environmental, or planning conclusion.

### `_canonical_url`

**Purpose:** Implements `canonical url` within the file role: Implements the shared HTTPS trust boundary, including numeric DNS-to-TLS binding, caller-header ownership, and manual redirects.

**Exact signature**

```python
def _canonical_url(parsed: SplitResult, hostname: str, port: int) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parsed` | positional-or-keyword | `SplitResult` | `required` |
| `hostname` | positional-or-keyword | `str` | `required` |
| `port` | positional-or-keyword | `int` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `urlunsplit(("https", netloc, parsed.path or "/", parsed.query, ""))`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.common.safe_http::_resolve_destination` via `_canonical_url`
- value/type reference: `landscout.common.safe_http::_resolve_destination` via `_canonical_url`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_strict_literal_address` | `landscout.common.safe_http._strict_literal_address` |
| `urlunsplit` | `urllib.parse.urlunsplit` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _canonical_url(parsed: SplitResult, hostname: str, port: int) -> str:
    address = _strict_literal_address(hostname)
    host_text = (
        f"[{hostname}]" if address is not None and address.version == 6 else hostname
    )
    netloc = host_text if port == 443 else f"{host_text}:{port}"
    return urlunsplit(("https", netloc, parsed.path or "/", parsed.query, ""))
```

**Business boundary**

- This contract validates or represents inputs; it does not rank parcels, combine criteria, or create a legal, access, grid-capacity, environmental, or planning conclusion.

### `_resolve_destination`

**Purpose:** Implements `resolve destination` within the file role: Implements the shared HTTPS trust boundary, including numeric DNS-to-TLS binding, caller-header ownership, and manual redirects.

**Exact signature**

```python
def _resolve_destination(value: str) -> _ResolvedDestination:
```

- Exact decorators: none.
- Declared return annotation: `_ResolvedDestination`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_ResolvedDestination(<br>            url=_canonical_url(parsed, hostname, port),<br>            hostname=hostname,<br>            port=port,<br>            request_target=request_target,<br>            addresses=addresses,<br>        )`
- Explicit raise paths:
  - `TypeError("HTTPS URL must be an exact non-empty string")` under lexical guard `type(value) is not str or not value`.
  - `ValueError("HTTPS URL contains a control character")` under lexical guard `any(ord(character) < 32 or ord(character) == 127 for character in value)`.
  - `ValueError("Remote URL must use HTTPS and include a hostname")` under lexical guard `parsed.scheme.casefold() != "https" or parsed.hostname is None`.
  - `ValueError("Remote URL credentials are forbidden")` under lexical guard `parsed.username is not None or parsed.password is not None`.
  - `ValueError("Remote URL fragments are forbidden")` under lexical guard `parsed.fragment`.
  - `ValueError("HTTPS URL port is invalid")` under lexical guard `not 1 <= port <= 65535`.
  - `ValueError("Non-public IP HTTPS destinations are forbidden")` under lexical guard `literal is None`.
  - `re-raise`.
  - `SafeHttpsError(f"Unsafe HTTPS URL: {value}")`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.common.safe_http::open_safe_https` via `_resolve_destination`
- value/type reference: `landscout.common.safe_http::open_safe_https` via `_resolve_destination`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `TypeError` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `ord` | `unresolved local/third-party receiver; no ownership inferred` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `urlsplit` | `urllib.parse.urlsplit` |
| `parsed.scheme.casefold` | `unresolved local/third-party receiver; no ownership inferred` |
| `_canonical_hostname` | `landscout.common.safe_http._canonical_hostname` |
| `_strict_literal_address` | `landscout.common.safe_http._strict_literal_address` |
| `_resolve_public_addresses` | `landscout.common.safe_http._resolve_public_addresses` |
| `_is_globally_routable_address` | `landscout.common.safe_http._is_globally_routable_address` |
| `_ResolvedAddress` | `landscout.common.safe_http._ResolvedAddress` |
| `_ResolvedDestination` | `landscout.common.safe_http._ResolvedDestination` |
| `_canonical_url` | `landscout.common.safe_http._canonical_url` |
| `SafeHttpsError` | `landscout.common.safe_http.SafeHttpsError` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- This contract validates or represents inputs; it does not rank parcels, combine criteria, or create a legal, access, grid-capacity, environmental, or planning conclusion.

### `_BoundHTTPSConnection.__init__`

**Purpose:** Implements `init` within the file role: Implements the shared HTTPS trust boundary, including numeric DNS-to-TLS binding, caller-header ownership, and manual redirects.

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

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |
| `hostname` | positional-or-keyword | `str` | `required` |
| `port` | positional-or-keyword | `int` | `required` |
| `address` | positional-or-keyword | `_ResolvedAddress` | `required` |
| `timeout` | keyword-only | `float` | `required` |
| `context` | keyword-only | `ssl.SSLContext` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `super().__init__` | `unresolved local/third-party receiver; no ownership inferred` |
| `super` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `self._validated_address = address`<br>`self._tls_context = context` |
| Direct parameter mutation | `self._validated_address = address`<br>`self._tls_context = context` |

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

- This contract validates or represents inputs; it does not rank parcels, combine criteria, or create a legal, access, grid-capacity, environmental, or planning conclusion.

### `_BoundHTTPSConnection.connect`

**Purpose:** Implements `connect` within the file role: Implements the shared HTTPS trust boundary, including numeric DNS-to-TLS binding, caller-header ownership, and manual redirects.

**Exact signature**

```python
def connect(self) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `SafeHttpsError("HTTPS proxy tunnels are forbidden")` under lexical guard `getattr(self, "_tunnel_host", None) is not None`.
  - `SafeHttpsError("Connected HTTPS peer address is malformed")` under lexical guard `type(peer) is not tuple or not peer or type(peer[0]) is not str`.
  - `SafeHttpsError(<br>                    "Connected HTTPS peer differs from the validated DNS address"<br>                )` under lexical guard `peer_address != self._validated_address.address`.
  - `re-raise`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `SafeHttpsError` | `landscout.common.safe_http.SafeHttpsError` |
| `socket.socket` | `socket.socket` |
| `raw_socket.settimeout` | `unresolved local/third-party receiver; no ownership inferred` |
| `raw_socket.connect` | `unresolved local/third-party receiver; no ownership inferred` |
| `raw_socket.getpeername` | `unresolved local/third-party receiver; no ownership inferred` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `ipaddress.ip_address` | `ipaddress.ip_address` |
| `peer[0].split` | `unresolved local/third-party receiver; no ownership inferred` |
| `self._tls_context.wrap_socket` | `landscout.common.safe_http._BoundHTTPSConnection._tls_context.wrap_socket` |
| `raw_socket.close` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | `socket.socket`<br>`raw_socket.settimeout`<br>`raw_socket.connect`<br>`raw_socket.getpeername`<br>`raw_socket.close` |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `self.sock = self._tls_context.wrap_socket(<br>                raw_socket,<br>                server_hostname=self.host,<br>            )` |
| Direct parameter mutation | `self.sock = self._tls_context.wrap_socket(<br>                raw_socket,<br>                server_hostname=self.host,<br>            )` |

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

- This contract validates or represents inputs; it does not rank parcels, combine criteria, or create a legal, access, grid-capacity, environmental, or planning conclusion.

### `SafeHttpsResponse.__init__`

**Purpose:** Implements `init` within the file role: Implements the shared HTTPS trust boundary, including numeric DNS-to-TLS binding, caller-header ownership, and manual redirects.

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

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |
| `response` | positional-or-keyword | `http.client.HTTPResponse` | `required` |
| `connection` | positional-or-keyword | `_BoundHTTPSConnection` | `required` |
| `url` | keyword-only | `str` | `required` |
| `history` | keyword-only | `tuple[str, ...]` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
- No calls.

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `self._response = response`<br>`self._connection = connection`<br>`self.url = url`<br>`self.history = history`<br>`self.status = response.status`<br>`self.headers = response.headers`<br>`self._closed = False` |
| Direct parameter mutation | `self._response = response`<br>`self._connection = connection`<br>`self.url = url`<br>`self.history = history`<br>`self.status = response.status`<br>`self.headers = response.headers`<br>`self._closed = False` |

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

- This contract validates or represents inputs; it does not rank parcels, combine criteria, or create a legal, access, grid-capacity, environmental, or planning conclusion.

### `SafeHttpsResponse.read`

**Purpose:** Implements `read` within the file role: Implements the shared HTTPS trust boundary, including numeric DNS-to-TLS binding, caller-header ownership, and manual redirects.

**Exact signature**

```python
def read(self, amount: int | None = None) -> bytes:
```

- Exact decorators: none.
- Declared return annotation: `bytes`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |
| `amount` | positional-or-keyword | `int \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `self._response.read(amount)`
- Explicit raise paths:
  - `SafeHttpsError("HTTPS response stream failed")`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `self._response.read` | `landscout.common.safe_http.SafeHttpsResponse._response.read` |
| `SafeHttpsError` | `landscout.common.safe_http.SafeHttpsError` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def read(self, amount: int | None = None) -> bytes:
        try:
            return self._response.read(amount)
        except Exception as error:
            raise SafeHttpsError("HTTPS response stream failed") from error
```

**Business boundary**

- This contract validates or represents inputs; it does not rank parcels, combine criteria, or create a legal, access, grid-capacity, environmental, or planning conclusion.

### `SafeHttpsResponse.close`

**Purpose:** Implements `close` within the file role: Implements the shared HTTPS trust boundary, including numeric DNS-to-TLS binding, caller-header ownership, and manual redirects.

**Exact signature**

```python
def close(self) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `None`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.common.safe_http::SafeHttpsResponse.__exit__` via `self.close`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `self._response.close` | `landscout.common.safe_http.SafeHttpsResponse._response.close` |
| `self._connection.close` | `landscout.common.safe_http.SafeHttpsResponse._connection.close` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `self._closed = True` |
| Direct parameter mutation | `self._closed = True` |

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

- This contract validates or represents inputs; it does not rank parcels, combine criteria, or create a legal, access, grid-capacity, environmental, or planning conclusion.

### `SafeHttpsResponse.__enter__`

**Purpose:** Implements `enter` within the file role: Implements the shared HTTPS trust boundary, including numeric DNS-to-TLS binding, caller-header ownership, and manual redirects.

**Exact signature**

```python
def __enter__(self) -> Self:
```

- Exact decorators: none.
- Declared return annotation: `Self`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `self`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
- No calls.

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def __enter__(self) -> Self:
        return self
```

**Business boundary**

- This contract validates or represents inputs; it does not rank parcels, combine criteria, or create a legal, access, grid-capacity, environmental, or planning conclusion.

### `SafeHttpsResponse.__exit__`

**Purpose:** Implements `exit` within the file role: Implements the shared HTTPS trust boundary, including numeric DNS-to-TLS binding, caller-header ownership, and manual redirects.

**Exact signature**

```python
def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |
| `exc_type` | positional-or-keyword | `type[BaseException] \| None` | `required` |
| `exc_value` | positional-or-keyword | `BaseException \| None` | `required` |
| `traceback` | positional-or-keyword | `TracebackType \| None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `self.close` | `landscout.common.safe_http.SafeHttpsResponse.close` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- This contract validates or represents inputs; it does not rank parcels, combine criteria, or create a legal, access, grid-capacity, environmental, or planning conclusion.

### `_validated_timeout`

**Purpose:** Implements `validated timeout` within the file role: Implements the shared HTTPS trust boundary, including numeric DNS-to-TLS binding, caller-header ownership, and manual redirects.

**Exact signature**

```python
def _validated_timeout(value: object) -> float:
```

- Exact decorators: none.
- Declared return annotation: `float`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `timeout`
- Explicit raise paths:
  - `SafeHttpsError("HTTPS timeout must be a strict positive finite number")` under lexical guard `isinstance(value, bool) or not isinstance(value, Real)`.
  - `SafeHttpsError(<br>            "HTTPS timeout must be a strict positive finite number"<br>        )`.
  - `SafeHttpsError("HTTPS timeout must be a strict positive finite number")` under lexical guard `not isfinite(timeout) or timeout <= 0`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.common.safe_http::open_safe_https` via `_validated_timeout`
- value/type reference: `landscout.common.safe_http::open_safe_https` via `_validated_timeout`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `SafeHttpsError` | `landscout.common.safe_http.SafeHttpsError` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |
| `isfinite` | `math.isfinite` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- This contract validates or represents inputs; it does not rank parcels, combine criteria, or create a legal, access, grid-capacity, environmental, or planning conclusion.

### `_request_parts`

**Purpose:** Implements `request parts` within the file role: Implements the shared HTTPS trust boundary, including numeric DNS-to-TLS binding, caller-header ownership, and manual redirects.

**Exact signature**

```python
def _request_parts(
    value: str | Request,
    supplied_headers: Mapping[str, str] | None,
) -> tuple[str, dict[str, str]]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[str, dict[str, str]]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `str \| Request` | `required` |
| `supplied_headers` | positional-or-keyword | `Mapping[str, str] \| None` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `url, output`
- Explicit raise paths:
  - `SafeHttpsError("Safe HTTPS source transport supports GET only")` under lexical guard `isinstance(value, Request)`.
  - `SafeHttpsError("HTTPS request must be an exact URL string or Request")` under lexical guard `isinstance(value, Request)`.
  - `SafeHttpsError("HTTPS request headers must be a mapping")` under lexical guard `supplied_headers is not None`.
  - `SafeHttpsError("HTTPS header names and values must be exact strings")` under lexical guard `type(name) is not str or type(header_value) is not str`.
  - `SafeHttpsError("HTTPS header name is invalid")` under lexical guard `_HEADER_NAME_PATTERN.fullmatch(name) is None`.
  - `SafeHttpsError(<br>                "HTTPS header names must not be duplicate or ambiguous"<br>            )` under lexical guard `normalized_name in seen_names`.
  - `SafeHttpsError("Caller-supplied HTTPS header is forbidden")` under lexical guard `normalized_name in _FORBIDDEN_CALLER_HEADER_NAMES`.
  - `SafeHttpsError("HTTPS headers contain control characters")` under lexical guard `any(<br>            ord(character) < 32 or ord(character) == 127<br>            for character in name + header_value<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.common.safe_http::open_safe_https` via `_request_parts`
- value/type reference: `landscout.common.safe_http::open_safe_https` via `_request_parts`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `value.get_method().upper` | `unresolved local/third-party receiver; no ownership inferred` |
| `value.get_method` | `unresolved local/third-party receiver; no ownership inferred` |
| `SafeHttpsError` | `landscout.common.safe_http.SafeHttpsError` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `value.header_items` | `unresolved local/third-party receiver; no ownership inferred` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `combined.extend` | `unresolved local/third-party receiver; no ownership inferred` |
| `supplied_headers.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `_HEADER_NAME_PATTERN.fullmatch` | `unresolved local/third-party receiver; no ownership inferred` |
| `name.casefold` | `unresolved local/third-party receiver; no ownership inferred` |
| `seen_names.add` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `ord` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `combined.extend(supplied_headers.items())`<br>`seen_names.add(normalized_name)`<br>`output[name] = header_value`<br>`output["Connection"] = "close"` |
| Direct parameter mutation | None directly present. |

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
        combined = list(value.header_items())
    elif type(value) is str:
        url = value
        combined = []
    else:
        raise SafeHttpsError("HTTPS request must be an exact URL string or Request")
    if supplied_headers is not None:
        if not isinstance(supplied_headers, Mapping):
            raise SafeHttpsError("HTTPS request headers must be a mapping")
        combined.extend(supplied_headers.items())
    output: dict[str, str] = {}
    seen_names: set[str] = set()
    for name, header_value in combined:
        if type(name) is not str or type(header_value) is not str:
            raise SafeHttpsError("HTTPS header names and values must be exact strings")
        if _HEADER_NAME_PATTERN.fullmatch(name) is None:
            raise SafeHttpsError("HTTPS header name is invalid")
        normalized_name = name.casefold()
        if normalized_name in seen_names:
            raise SafeHttpsError(
                "HTTPS header names must not be duplicate or ambiguous"
            )
        seen_names.add(normalized_name)
        if normalized_name in _FORBIDDEN_CALLER_HEADER_NAMES:
            raise SafeHttpsError("Caller-supplied HTTPS header is forbidden")
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

- This contract validates or represents inputs; it does not rank parcels, combine criteria, or create a legal, access, grid-capacity, environmental, or planning conclusion.

### `_open_destination`

**Purpose:** Implements `open destination` within the file role: Implements the shared HTTPS trust boundary, including numeric DNS-to-TLS binding, caller-header ownership, and manual redirects.

**Exact signature**

```python
def _open_destination(
    destination: _ResolvedDestination,
    timeout: float,
    headers: Mapping[str, str],
) -> tuple[http.client.HTTPResponse, _BoundHTTPSConnection]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[http.client.HTTPResponse, _BoundHTTPSConnection]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `destination` | positional-or-keyword | `_ResolvedDestination` | `required` |
| `timeout` | positional-or-keyword | `float` | `required` |
| `headers` | positional-or-keyword | `Mapping[str, str]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `connection.getresponse(), connection`
- Explicit raise paths:
  - `re-raise`.
  - `SafeHttpsError("HTTPS TLS verification failed")`.
  - `SafeHttpsError(<br>        "Every validated HTTPS destination address failed"<br>    )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.common.safe_http::open_safe_https` via `_open_destination`
- value/type reference: `landscout.common.safe_http::open_safe_https` via `_open_destination`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `ssl.create_default_context` | `ssl.create_default_context` |
| `_BoundHTTPSConnection` | `landscout.common.safe_http._BoundHTTPSConnection` |
| `connection.request` | `unresolved local/third-party receiver; no ownership inferred` |
| `dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `connection.getresponse` | `unresolved local/third-party receiver; no ownership inferred` |
| `connection.close` | `unresolved local/third-party receiver; no ownership inferred` |
| `SafeHttpsError` | `landscout.common.safe_http.SafeHttpsError` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | `connection.request`<br>`connection.getresponse` |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- This contract validates or represents inputs; it does not rank parcels, combine criteria, or create a legal, access, grid-capacity, environmental, or planning conclusion.

### `_redirect_location`

**Purpose:** Implements `redirect location` within the file role: Implements the shared HTTPS trust boundary, including numeric DNS-to-TLS binding, caller-header ownership, and manual redirects.

**Exact signature**

```python
def _redirect_location(response: http.client.HTTPResponse) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `response` | positional-or-keyword | `http.client.HTTPResponse` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `values[0]`
- Explicit raise paths:
  - `SafeHttpsError("HTTPS redirect requires exactly one Location header")` under lexical guard `len(values) != 1 or type(values[0]) is not str or not values[0]`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.common.safe_http::open_safe_https` via `_redirect_location`
- value/type reference: `landscout.common.safe_http::open_safe_https` via `_redirect_location`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `response.headers.get_all` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `SafeHttpsError` | `landscout.common.safe_http.SafeHttpsError` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _redirect_location(response: http.client.HTTPResponse) -> str:
    values = response.headers.get_all("Location", failobj=[])
    if len(values) != 1 or type(values[0]) is not str or not values[0]:
        raise SafeHttpsError("HTTPS redirect requires exactly one Location header")
    return values[0]
```

**Business boundary**

- This contract validates or represents inputs; it does not rank parcels, combine criteria, or create a legal, access, grid-capacity, environmental, or planning conclusion.

### `open_safe_https`

**Purpose:** Open one source GET with validated redirects and a bound TLS socket.

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

- Exact decorators: none.
- Declared return annotation: `SafeHttpsResponse`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `url` | positional-or-keyword | `str \| Request` | `required` |
| `timeout` | keyword-only | `float` | `required` |
| `headers` | keyword-only | `Mapping[str, str] \| None` | `None` |
| `max_redirects` | keyword-only | `int` | `_DEFAULT_MAX_REDIRECTS` |

**Return and exception contract**

- Exact observed return expressions:
  - `SafeHttpsResponse(<br>                response,<br>                connection,<br>                url=destination.url,<br>                history=tuple(history),<br>            )`
- Explicit raise paths:
  - `SafeHttpsError("max_redirects must be a non-negative integer")` under lexical guard `type(max_redirects) is not int or max_redirects < 0`.
  - `SafeHttpsError("HTTPS redirect loop detected")` under lexical guard `destination.url in seen`.
  - `SafeHttpsError("HTTPS redirect limit exceeded")` under lexical guard `status in _REDIRECT_STATUSES`.
  - `SafeHttpsError(f"HTTPS source returned status {status}")` under lexical guard `not 200 <= status < 300`.
  - `re-raise`.
  - `SafeHttpsError("Safe HTTPS exchange failed")`.

**Qualified relationships**

Inbound conservative repository consumers:
- import: `landscout.sources.cadastre_fr::<module>` via `from landscout.common.safe_http import open_safe_https`
- direct call: `landscout.sources.cadastre_fr::download_cadastre_parcelles` via `open_safe_https`
- value/type reference: `landscout.sources.cadastre_fr::download_cadastre_parcelles` via `open_safe_https`
- import: `landscout.sources.gpu_fr::<module>` via `from landscout.common.safe_http import open_safe_https`
- direct call: `landscout.sources.gpu_fr::_request_json` via `open_safe_https`
- value/type reference: `landscout.sources.gpu_fr::_request_json` via `open_safe_https`
- direct call: `landscout.sources.gpu_fr::download_gpu_document` via `open_safe_https`
- value/type reference: `landscout.sources.gpu_fr::download_gpu_document` via `open_safe_https`
- import: `landscout.sources.ign_bdtopo_fr::<module>` via `from landscout.common.safe_http import open_safe_https`
- direct call: `landscout.sources.ign_bdtopo_fr::download_ign_bdtopo_archive` via `open_safe_https`
- value/type reference: `landscout.sources.ign_bdtopo_fr::download_ign_bdtopo_archive` via `open_safe_https`
- import: `landscout.sources.inpn_protected_areas_fr::<module>` via `from landscout.common.safe_http import SafeHttpsError, open_safe_https`
- direct call: `landscout.sources.inpn_protected_areas_fr::_download_archive_bytes` via `open_safe_https`
- value/type reference: `landscout.sources.inpn_protected_areas_fr::_download_archive_bytes` via `open_safe_https`
- import: `landscout.sources.rte_odre_fr::<module>` via `from landscout.common.safe_http import open_safe_https`
- direct call: `landscout.sources.rte_odre_fr::_read_response_json` via `open_safe_https`
- value/type reference: `landscout.sources.rte_odre_fr::_read_response_json` via `open_safe_https`
- direct call: `landscout.sources.rte_odre_fr::download_rte_odre_dataset` via `open_safe_https`
- value/type reference: `landscout.sources.rte_odre_fr::download_rte_odre_dataset` via `open_safe_https`
- import: `tests.unit.test_safe_http::<module>` via `from landscout.common.safe_http import SafeHttpsError, open_safe_https`
- direct call: `tests.unit.test_safe_http::_read` via `open_safe_https`
- value/type reference: `tests.unit.test_safe_http::_read` via `open_safe_https`
- direct call: `tests.unit.test_safe_http::test_sensitive_and_hop_by_hop_headers_fail_before_dns` via `open_safe_https`
- value/type reference: `tests.unit.test_safe_http::test_sensitive_and_hop_by_hop_headers_fail_before_dns` via `open_safe_https`
- direct call: `tests.unit.test_safe_http::test_case_insensitive_duplicate_header_names_fail_before_dns` via `open_safe_https`
- value/type reference: `tests.unit.test_safe_http::test_case_insensitive_duplicate_header_names_fail_before_dns` via `open_safe_https`
- direct call: `tests.unit.test_safe_http::test_request_and_explicit_headers_cannot_ambiguously_override_each_other` via `open_safe_https`
- value/type reference: `tests.unit.test_safe_http::test_request_and_explicit_headers_cannot_ambiguously_override_each_other` via `open_safe_https`
- direct call: `tests.unit.test_safe_http::test_cross_origin_redirect_cannot_receive_a_sensitive_header` via `open_safe_https`
- value/type reference: `tests.unit.test_safe_http::test_cross_origin_redirect_cannot_receive_a_sensitive_header` via `open_safe_https`
- direct call: `tests.unit.test_safe_http::test_cross_origin_redirect_forwards_only_safe_ordinary_headers` via `open_safe_https`
- value/type reference: `tests.unit.test_safe_http::test_cross_origin_redirect_forwards_only_safe_ordinary_headers` via `open_safe_https`
- direct call: `tests.unit.test_safe_http::test_safe_https_redirect_is_manually_revalidated` via `open_safe_https`
- value/type reference: `tests.unit.test_safe_http::test_safe_https_redirect_is_manually_revalidated` via `open_safe_https`
- direct call: `tests.unit.test_safe_http::test_malformed_header_name_is_rejected_before_dns` via `open_safe_https`
- value/type reference: `tests.unit.test_safe_http::test_malformed_header_name_is_rejected_before_dns` via `open_safe_https`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validated_timeout` | `landscout.common.safe_http._validated_timeout` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `SafeHttpsError` | `landscout.common.safe_http.SafeHttpsError` |
| `_request_parts` | `landscout.common.safe_http._request_parts` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `_resolve_destination` | `landscout.common.safe_http._resolve_destination` |
| `seen.add` | `unresolved local/third-party receiver; no ownership inferred` |
| `_open_destination` | `landscout.common.safe_http._open_destination` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `_redirect_location` | `landscout.common.safe_http._redirect_location` |
| `history.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `urljoin` | `urllib.parse.urljoin` |
| `SafeHttpsResponse` | `landscout.common.safe_http.SafeHttpsResponse` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `response.close` | `unresolved local/third-party receiver; no ownership inferred` |
| `connection.close` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `seen.add(destination.url)`<br>`history.append(destination.url)` |
| Direct parameter mutation | None directly present. |

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

- This contract validates or represents inputs; it does not rank parcels, combine criteria, or create a legal, access, grid-capacity, environmental, or planning conclusion.


## 7. Validation and data-contract summary

- Canonical schema/mapping declarations inventoried above: none at module scope.
- Exact value/null/index/CRS/geometry/hash behavior is claimed only where the reproduced validators and operations enforce it.

## 8. Public exports and package ownership

This module declares no `__all__`; no package-level public guarantee is inferred from direct importability alone.

## 9. Trust, provenance, side effects, and business boundary

- This contract validates or represents inputs; it does not rank parcels, combine criteria, or create a legal, access, grid-capacity, environmental, or planning conclusion.
- Configured identity, textual lineage, byte identity, physical source reconstruction, local envelope validation, and source-complete validation remain distinct trust levels. This companion attributes only the levels implemented in the exact source.
- Filesystem, network, hashing, CRS/geometry, process, mutation, and expected-exception evidence is listed per callable; an empty category is not silently promoted to an effect.

## 10. Change impact

A source-byte change invalidates the SHA above and requires re-auditing imports/re-exports, constants/aliases/schemas, model fields/immutability, qualified callers, side effects, controlled errors, tests, source/artifact locks, and the exact full snapshot.

## 11. Exact complete current file content

The following UTF-8 snapshot is the complete current repository file, not an excerpt. Its raw-byte SHA256 is the value in **File identity**.

```python
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
_FORBIDDEN_CALLER_HEADER_NAMES = frozenset(
    {
        "authorization",
        "proxy-authorization",
        "cookie",
        "cookie2",
        "host",
        "connection",
        "proxy-connection",
        "keep-alive",
        "transfer-encoding",
        "te",
        "trailer",
        "upgrade",
    }
)


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
    if any(
        character.isdigit() for character in hostname
    ) and _NUMERIC_HOST_PATTERN.fullmatch(hostname):
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
                raise SafeHttpsError(f"DNS resolved {hostname} to a non-public address")
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
        canonical = hostname.encode("idna").decode("ascii").casefold().rstrip(".")
    except UnicodeError as error:
        raise SafeHttpsError("HTTPS URL hostname is malformed") from error
    if not canonical:
        raise SafeHttpsError("HTTPS URL hostname is empty")
    if canonical == "localhost" or canonical.endswith(".localhost"):
        raise SafeHttpsError("Localhost HTTPS destinations are forbidden")
    return canonical


def _canonical_url(parsed: SplitResult, hostname: str, port: int) -> str:
    address = _strict_literal_address(hostname)
    host_text = (
        f"[{hostname}]" if address is not None and address.version == 6 else hostname
    )
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
        combined = list(value.header_items())
    elif type(value) is str:
        url = value
        combined = []
    else:
        raise SafeHttpsError("HTTPS request must be an exact URL string or Request")
    if supplied_headers is not None:
        if not isinstance(supplied_headers, Mapping):
            raise SafeHttpsError("HTTPS request headers must be a mapping")
        combined.extend(supplied_headers.items())
    output: dict[str, str] = {}
    seen_names: set[str] = set()
    for name, header_value in combined:
        if type(name) is not str or type(header_value) is not str:
            raise SafeHttpsError("HTTPS header names and values must be exact strings")
        if _HEADER_NAME_PATTERN.fullmatch(name) is None:
            raise SafeHttpsError("HTTPS header name is invalid")
        normalized_name = name.casefold()
        if normalized_name in seen_names:
            raise SafeHttpsError(
                "HTTPS header names must not be duplicate or ambiguous"
            )
        seen_names.add(normalized_name)
        if normalized_name in _FORBIDDEN_CALLER_HEADER_NAMES:
            raise SafeHttpsError("Caller-supplied HTTPS header is forbidden")
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
```

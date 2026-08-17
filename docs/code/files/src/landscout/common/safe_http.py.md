# `src/landscout/common/safe_http.py`

## File identity

- Repository path: `src/landscout/common/safe_http.py`
- File type: Python source
- Primary responsibility: Implements the shared HTTPS trust boundary that binds validated DNS answers to the actual TLS socket and owns redirects.
- Layer / domain: `internal common contract/utility` / `common`
- Public or internal role: Module symbols without a package re-export are internal unless imported directly by repository code.
- Source SHA256: `f63952179ee94bf8e4838f2658e7f7b7dbd7e4b91bc4e532eb1a44f1e2b5133f`

## 1. Purpose

Implements the shared HTTPS trust boundary that binds validated DNS answers to the actual TLS socket and owns redirects.

## 2. Position in LandScout architecture

This file is a `internal common contract/utility` artifact in the `common` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from __future__ import annotations` — required by the implementation paths and symbols documented below.
- `import http.client` — required by the implementation paths and symbols documented below.
- `import ipaddress` — required by the implementation paths and symbols documented below.
- `import re` — required by the implementation paths and symbols documented below.
- `import socket` — required by the implementation paths and symbols documented below.
- `import ssl` — required by the implementation paths and symbols documented below.
- `from collections.abc import Mapping` — required by the implementation paths and symbols documented below.
- `from dataclasses import dataclass` — required by the implementation paths and symbols documented below.
- `from math import isfinite` — required by the implementation paths and symbols documented below.
- `from numbers import Real` — required by the implementation paths and symbols documented below.
- `from types import TracebackType` — required by the implementation paths and symbols documented below.
- `from typing import Self` — required by the implementation paths and symbols documented below.
- `from urllib.parse import SplitResult, urljoin, urlsplit, urlunsplit` — required by the implementation paths and symbols documented below.
- `from urllib.request import Request` — required by the implementation paths and symbols documented below.

### Third-party

- None.

### Internal LandScout

- None.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `_REDIRECT_STATUSES` | `frozenset({301, 302, 303, 307, 308})` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_DEFAULT_MAX_REDIRECTS` | `10` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_NUMERIC_HOST_PATTERN` | `re.compile(r"^[0-9A-Fa-fxX.]+$")` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_HEADER_NAME_PATTERN` | `re.compile(r"^[!#$%&'*+\-.^_`&#124;~0-9A-Za-z]+$")` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

### `SafeHttpsError`

**Purpose:** Raised when an outbound HTTPS destination or exchange is unsafe.

**Inheritance:** `OSError`.

**Model form and mutability:** class inheriting from `OSError`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

### `_ResolvedAddress`

**Purpose:** Groups the `ResolvedAddress` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `family` | `int` | `required` | Socket address family (`AF_INET` or `AF_INET6`) selected from a validated resolver record. |
| `address` | `ipaddress.IPv4Address | ipaddress.IPv6Address` | `required` | Parsed IP address that passed every globally-routable-address guard. |
| `port` | `int` | `required` | Validated TCP destination port; HTTPS defaults to 443 when the URL omits it. |

**Validators and methods:**

- `socket_address` — `def socket_address(self) -> tuple[object, ...]:`; decorators `property`. The complete method algorithm appears in the function/method section.

### `_ResolvedDestination`

**Purpose:** Groups the `ResolvedDestination` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `url` | `str` | `required` | Canonical HTTPS URL retained for request identity, redirects, lineage, or provenance according to the owning model. |
| `hostname` | `str` | `required` | Canonical original hostname used for DNS, TLS SNI, certificate verification, and HTTP Host identity. |
| `port` | `int` | `required` | Validated TCP destination port; HTTPS defaults to 443 when the URL omits it. |
| `request_target` | `str` | `required` | Origin-form HTTP request path plus query sent to the bound HTTPS connection. |
| `addresses` | `tuple[_ResolvedAddress, ...]` | `required` | Non-empty immutable ordered set of validated public IP candidates returned by the resolver. |

**Validators and methods:**

- None.

### `_BoundHTTPSConnection`

**Purpose:** HTTPS connection whose transport endpoint is one validated IP.

**Inheritance:** `http.client.HTTPSConnection`.

**Model form and mutability:** class inheriting from `http.client.HTTPSConnection`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `_validated_address` | `not explicitly annotated` | `assigned in `__init__` from `address`` | `not explicitly annotated` state used by `src/landscout/common/safe_http.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `_tls_context` | `not explicitly annotated` | `assigned in `__init__` from `context`` | `not explicitly annotated` state used by `src/landscout/common/safe_http.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `sock` | `not explicitly annotated` | `assigned in `connect` from `self._tls_context.wrap_socket(raw_socket, server_hostname=self.host)`` | `not explicitly annotated` state used by `src/landscout/common/safe_http.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- `__init__` — `def __init__(         self,         hostname: str,         port: int,         address: _ResolvedAddress,         *,         timeout: float,         context: ssl.SSLContext,     ) -> None:`; decorators `none`. The complete method algorithm appears in the function/method section.
- `connect` — `def connect(self) -> None:`; decorators `none`. The complete method algorithm appears in the function/method section.

### `SafeHttpsResponse`

**Purpose:** Streaming final response returned by :func:`open_safe_https`.

**Inheritance:** `object`.

**Model form and mutability:** class inheriting from `object`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `_response` | `not explicitly annotated` | `assigned in `__init__` from `response`` | `not explicitly annotated` state used by `src/landscout/common/safe_http.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `_connection` | `not explicitly annotated` | `assigned in `__init__` from `connection`` | `not explicitly annotated` state used by `src/landscout/common/safe_http.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `url` | `not explicitly annotated` | `assigned in `__init__` from `url`` | Canonical HTTPS URL retained for request identity, redirects, lineage, or provenance according to the owning model. |
| `history` | `not explicitly annotated` | `assigned in `__init__` from `history`` | `not explicitly annotated` state used by `src/landscout/common/safe_http.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `status` | `not explicitly annotated` | `assigned in `__init__` from `response.status`` | `not explicitly annotated` state used by `src/landscout/common/safe_http.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `headers` | `not explicitly annotated` | `assigned in `__init__` from `response.headers`` | `not explicitly annotated` state used by `src/landscout/common/safe_http.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `_closed` | `not explicitly annotated` | `assigned in `__init__` from `False`` | `not explicitly annotated` state used by `src/landscout/common/safe_http.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- `__init__` — `def __init__(         self,         response: http.client.HTTPResponse,         connection: _BoundHTTPSConnection,         *,         url: str,         history: tuple[str, ...],     ) -> None:`; decorators `none`. The complete method algorithm appears in the function/method section.
- `read` — `def read(self, amount: int | None = None) -> bytes:`; decorators `none`. The complete method algorithm appears in the function/method section.
- `close` — `def close(self) -> None:`; decorators `none`. The complete method algorithm appears in the function/method section.
- `__enter__` — `def __enter__(self) -> Self:`; decorators `none`. The complete method algorithm appears in the function/method section.
- `__exit__` — `def __exit__(         self,         exc_type: type[BaseException] | None,         exc_value: BaseException | None,         traceback: TracebackType | None,     ) -> None:`; decorators `none`. The complete method algorithm appears in the function/method section.

## 6. Functions and methods

### `_ResolvedAddress.socket_address`

**Signature**

```python
def socket_address(self) -> tuple[object, ...]:
```

**Purpose**

Implements socket address according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[object, ...]`. Observed return expression(s): `(str(self.address), self.port, 0, 0)`; `(str(self.address), self.port)`.

**Algorithm**

1. Checks `self.family == socket.AF_INET`. When true: Returns `(str(self.address), self.port)`.
2. Returns `(str(self.address), self.port, 0, 0)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `str`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `common` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `_is_globally_routable_address`

**Signature**

```python
def _is_globally_routable_address(
    address: ipaddress.IPv4Address | ipaddress.IPv6Address,
) -> bool:
```

**Purpose**

Returns whether `globally routable address` satisfies the exact predicates and branches listed below.

**Inputs**

- `address` (`ipaddress.IPv4Address | ipaddress.IPv6Address`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bool`. Observed return expression(s): `True`; `False`.

**Algorithm**

1. Checks `not address.is_global or address.is_private or address.is_loopback or address.is_link_local or address.is_unspecified or address.is_multicast or address.is_reserved`. When true: Returns `False`.
2. Checks `isinstance(address, ipaddress.IPv6Address)`. When true: Computes `mapped` from `address.ipv4_mapped`. Checks `mapped is not None and (not _is_globally_routable_address(mapped))`. When true: Returns `False`.
3. Returns `True`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_is_globally_routable_address`, `isinstance`.

**Known repository callers**

- `src/landscout/common/safe_http.py` — `_resolve_destination`
- `src/landscout/common/safe_http.py` — `_resolve_public_addresses`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `common` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `_strict_literal_address`

**Signature**

```python
def _strict_literal_address(
    hostname: str,
) -> ipaddress.IPv4Address | ipaddress.IPv6Address | None:
```

**Purpose**

Implements strict literal address according to the exact implementation and guards in this file.

**Inputs**

- `hostname` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `ipaddress.IPv4Address | ipaddress.IPv6Address | None`. Observed return expression(s): `None`; `ipaddress.ip_address(hostname)`; `ipaddress.ip_address(packed)`; `ipaddress.IPv4Address(int(hostname, base))`.

**Algorithm**

1. Runs guarded operation: Returns `ipaddress.ip_address(hostname)`. Handles `ValueError`.
2. Runs guarded operation: Computes `packed` from `socket.inet_aton(hostname)`. Handles `OSError`.
3. Checks `packed is not None`. When true: Returns `ipaddress.ip_address(packed)`.
4. Checks `hostname.isdecimal() or hostname.casefold().startswith('0x')`. When true: Computes `base` from `16 if hostname.casefold().startswith('0x') else 10`. Runs guarded operation: Returns `ipaddress.IPv4Address(int(hostname, base))`. Handles `(ValueError, ipaddress.AddressValueError, OverflowError)`.
5. Checks `any((character.isdigit() for character in hostname)) and _NUMERIC_HOST_PATTERN.fullmatch(hostname)`. When true: Raises `SafeHttpsError('Malformed numeric IP destination')`.
6. Returns `None`.

**Validation and invariants**

- Rejects or diverts the path when `hostname.isdecimal() or hostname.casefold().startswith('0x')` is true.
- Rejects or diverts the path when `any((character.isdigit() for character in hostname)) and _NUMERIC_HOST_PATTERN.fullmatch(hostname)` is true.

**Exceptions**

- Explicitly raises: `SafeHttpsError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `SafeHttpsError`, `_NUMERIC_HOST_PATTERN.fullmatch`, `any`, `character.isdigit`, `hostname.casefold`, `hostname.casefold().startswith`, `hostname.isdecimal`, `int`, `ipaddress.IPv4Address`, `ipaddress.ip_address`, `socket.inet_aton`.

**Known repository callers**

- `src/landscout/common/safe_http.py` — `_canonical_url`
- `src/landscout/common/safe_http.py` — `_resolve_destination`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `common` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `_resolve_public_addresses`

**Signature**

```python
def _resolve_public_addresses(
    hostname: str,
    port: int,
) -> tuple[_ResolvedAddress, ...]:
```

**Purpose**

Resolves public addresses according to the exact implementation and guards in this file.

**Inputs**

- `hostname` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `port` (`int`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[_ResolvedAddress, ...]`. Observed return expression(s): `tuple((addresses[key] for key in sorted(addresses)))`.

**Algorithm**

1. Runs guarded operation: Computes `records` from `socket.getaddrinfo(hostname, port, type=socket.SOCK_STREAM)`. Defines `addresses` with annotation `dict[tuple[int, int], _ResolvedAddress]` from `{}`. Iterates `record` over `records`. For each value: Checks `type(record) is not tuple or len(record) != 5`. When true: Raises `TypeError('DNS result must be a five-item tuple')`. Computes `(family, socket_type, protocol, canonical_name, sockaddr)` from `record`. Checks `family == socket.AF_INET`. When true: Computes `expected_version` from `4`. Computes `expected_sockaddr_length` from `2`. Otherwise: Checks `family == socket.AF_INET6`. When true: Computes `expected_version` from `6`. Computes `expected_sockaddr_length` from `4`. Otherwise: Raises `ValueError('DNS result uses an unsupported address family')`. Executes 12 additional source-ordered statement(s). Checks `not addresses`. When true: Raises `ValueError('DNS resolution returned no usable address')`. Executes 1 additional source-ordered statement(s). Handles `SafeHttpsError`, `(OSError, UnicodeError, IndexError, TypeError, ValueError, OverflowError)`.

**Validation and invariants**

- Rejects or diverts the path when `not addresses` is true.
- Rejects or diverts the path when `type(record) is not tuple or len(record) != 5` is true.
- Rejects or diverts the path when `socket_type != socket.SOCK_STREAM` is true.
- Rejects or diverts the path when `type(protocol) is not int or protocol not in {0, socket.IPPROTO_TCP}` is true.
- Rejects or diverts the path when `type(canonical_name) is not str` is true.
- Rejects or diverts the path when `type(sockaddr) is not tuple or len(sockaddr) != expected_sockaddr_length` is true.
- Rejects or diverts the path when `type(validated_sockaddr[0]) is not str or type(validated_sockaddr[1]) is not int` is true.
- Rejects or diverts the path when `validated_sockaddr[1] != port` is true.
- Rejects or diverts the path when `expected_version == 6 and (type(validated_sockaddr[2]) is not int or type(validated_sockaddr[3]) is not int)` is true.
- Rejects or diverts the path when `address.version != expected_version` is true.
- Rejects or diverts the path when `not _is_globally_routable_address(address)` is true.

**Exceptions**

- Explicitly raises: `SafeHttpsError`, `TypeError`, `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `SafeHttpsError`, `TypeError`, `ValueError`, `_ResolvedAddress`, `_is_globally_routable_address`, `int`, `ipaddress.ip_address`, `len`, `socket.getaddrinfo`, `sorted`, `tuple`, `type`.

**Known repository callers**

- `src/landscout/common/safe_http.py` — `_resolve_destination`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `common` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `_canonical_hostname`

**Signature**

```python
def _canonical_hostname(hostname: str) -> str:
```

**Purpose**

Implements canonical hostname according to the exact implementation and guards in this file.

**Inputs**

- `hostname` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `canonical`.

**Algorithm**

1. Checks `not hostname`. When true: Raises `SafeHttpsError('HTTPS URL hostname is empty')`.
2. Runs guarded operation: Computes `canonical` from `hostname.encode('idna').decode('ascii').casefold().rstrip('.')`. Handles `UnicodeError`.
3. Checks `not canonical`. When true: Raises `SafeHttpsError('HTTPS URL hostname is empty')`.
4. Checks `canonical == 'localhost' or canonical.endswith('.localhost')`. When true: Raises `SafeHttpsError('Localhost HTTPS destinations are forbidden')`.
5. Returns `canonical`.

**Validation and invariants**

- Rejects or diverts the path when `not hostname` is true.
- Rejects or diverts the path when `not canonical` is true.
- Rejects or diverts the path when `canonical == 'localhost' or canonical.endswith('.localhost')` is true.

**Exceptions**

- Explicitly raises: `SafeHttpsError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `SafeHttpsError`, `canonical.endswith`, `hostname.encode`, `hostname.encode('idna').decode`, `hostname.encode('idna').decode('ascii').casefold`, `hostname.encode('idna').decode('ascii').casefold().rstrip`.

**Known repository callers**

- `src/landscout/common/safe_http.py` — `_resolve_destination`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `common` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `_canonical_url`

**Signature**

```python
def _canonical_url(parsed: SplitResult, hostname: str, port: int) -> str:
```

**Purpose**

Implements canonical url according to the exact implementation and guards in this file.

**Inputs**

- `parsed` (`SplitResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `hostname` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `port` (`int`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `urlunsplit(('https', netloc, parsed.path or '/', parsed.query, ''))`.

**Algorithm**

1. Computes `address` from `_strict_literal_address(hostname)`.
2. Computes `host_text` from `f'[{hostname}]' if address is not None and address.version == 6 else hostname`.
3. Computes `netloc` from `host_text if port == 443 else f'{host_text}:{port}'`.
4. Returns `urlunsplit(('https', netloc, parsed.path or '/', parsed.query, ''))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_strict_literal_address`, `urlunsplit`.

**Known repository callers**

- `src/landscout/common/safe_http.py` — `_resolve_destination`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `common` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `_resolve_destination`

**Signature**

```python
def _resolve_destination(value: str) -> _ResolvedDestination:
```

**Purpose**

Resolves destination according to the exact implementation and guards in this file.

**Inputs**

- `value` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `_ResolvedDestination`. Observed return expression(s): `_ResolvedDestination(url=_canonical_url(parsed, hostname, port), hostname=hostname, port=port, request_target=request_target, addresses=addresses)`.

**Algorithm**

1. Runs guarded operation: Checks `type(value) is not str or not value`. When true: Raises `TypeError('HTTPS URL must be an exact non-empty string')`. Checks `any((ord(character) < 32 or ord(character) == 127 for character in value))`. When true: Raises `ValueError('HTTPS URL contains a control character')`. Computes `parsed` from `urlsplit(value)`. Checks `parsed.scheme.casefold() != 'https' or parsed.hostname is None`. When true: Raises `ValueError('Remote URL must use HTTPS and include a hostname')`. Executes 10 additional source-ordered statement(s). Handles `SafeHttpsError`, `(AttributeError, IndexError, TypeError, UnicodeError, ValueError, OverflowError)`.

**Validation and invariants**

- Rejects or diverts the path when `type(value) is not str or not value` is true.
- Rejects or diverts the path when `any((ord(character) < 32 or ord(character) == 127 for character in value))` is true.
- Rejects or diverts the path when `parsed.scheme.casefold() != 'https' or parsed.hostname is None` is true.
- Rejects or diverts the path when `parsed.username is not None or parsed.password is not None` is true.
- Rejects or diverts the path when `parsed.fragment` is true.
- Rejects or diverts the path when `not 1 <= port <= 65535` is true.
- Rejects or diverts the path when `not _is_globally_routable_address(literal)` is true.

**Exceptions**

- Explicitly raises: `SafeHttpsError`, `TypeError`, `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `SafeHttpsError`, `TypeError`, `ValueError`, `_ResolvedAddress`, `_ResolvedDestination`, `_canonical_hostname`, `_canonical_url`, `_is_globally_routable_address`, `_resolve_public_addresses`, `_strict_literal_address`, `any`, `ord`, `parsed.scheme.casefold`, `type`, `urlsplit`.

**Known repository callers**

- `src/landscout/common/safe_http.py` — `open_safe_https`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `common` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `_BoundHTTPSConnection.__init__`

**Signature**

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

Implements init according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `hostname` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `port` (`int`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `address` (`_ResolvedAddress`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `timeout` (`float`; required) — network timeout in seconds; validation rejects unsupported or non-positive values. Nullability and accepted values are exactly those enforced by the guards listed below.
- `context` (`ssl.SSLContext`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Calls `super().__init__(hostname, port=port, timeout=timeout, context=context)` for its validation or side effect.
2. Computes `self._validated_address` from `address`.
3. Computes `self._tls_context` from `context`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `super`, `super().__init__`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `common` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `_BoundHTTPSConnection.connect`

**Signature**

```python
def connect(self) -> None:
```

**Purpose**

Implements connect according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `getattr(self, '_tunnel_host', None) is not None`. When true: Raises `SafeHttpsError('HTTPS proxy tunnels are forbidden')`.
2. Computes `raw_socket` from `socket.socket(self._validated_address.family, socket.SOCK_STREAM)`.
3. Runs guarded operation: Calls `raw_socket.settimeout(self.timeout)` for its validation or side effect. Calls `raw_socket.connect(self._validated_address.socket_address)` for its validation or side effect. Computes `peer` from `raw_socket.getpeername()`. Checks `type(peer) is not tuple or not peer or type(peer[0]) is not str`. When true: Raises `SafeHttpsError('Connected HTTPS peer address is malformed')`. Executes 3 additional source-ordered statement(s). Handles `Exception`.

**Validation and invariants**

- Rejects or diverts the path when `getattr(self, '_tunnel_host', None) is not None` is true.
- Rejects or diverts the path when `type(peer) is not tuple or not peer or type(peer[0]) is not str` is true.
- Rejects or diverts the path when `peer_address != self._validated_address.address` is true.

**Exceptions**

- Explicitly raises: `SafeHttpsError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `SafeHttpsError`, `getattr`, `ipaddress.ip_address`, `peer[0].split`, `raw_socket.close`, `raw_socket.connect`, `raw_socket.getpeername`, `raw_socket.settimeout`, `self._tls_context.wrap_socket`, `socket.socket`, `type`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `common` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `SafeHttpsResponse.__init__`

**Signature**

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

Implements init according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `response` (`http.client.HTTPResponse`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `connection` (`_BoundHTTPSConnection`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `url` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `history` (`tuple[str, ...]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `self._response` from `response`.
2. Computes `self._connection` from `connection`.
3. Computes `self.url` from `url`.
4. Computes `self.history` from `history`.
5. Computes `self.status` from `response.status`.
6. Computes `self.headers` from `response.headers`.
7. Computes `self._closed` from `False`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- No function calls.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `common` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `SafeHttpsResponse.read`

**Signature**

```python
def read(self, amount: int | None = None) -> bytes:
```

**Purpose**

Reads and validates read according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `amount` (`int | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bytes`. Observed return expression(s): `self._response.read(amount)`.

**Algorithm**

1. Runs guarded operation: Returns `self._response.read(amount)`. Handles `Exception`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `SafeHttpsError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `SafeHttpsError`, `self._response.read`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `common` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `SafeHttpsResponse.close`

**Signature**

```python
def close(self) -> None:
```

**Purpose**

Implements close according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. Observed return expression(s): `None`.

**Algorithm**

1. Checks `self._closed`. When true: Returns `None`.
2. Computes `self._closed` from `True`.
3. Runs guarded operation: Calls `self._response.close()` for its validation or side effect. Handles no explicit exception types. Finally: Calls `self._connection.close()` for its validation or side effect.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `self._connection.close`, `self._response.close`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `common` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `SafeHttpsResponse.__enter__`

**Signature**

```python
def __enter__(self) -> Self:
```

**Purpose**

Implements enter according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `Self`. Observed return expression(s): `self`.

**Algorithm**

1. Returns `self`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- No function calls.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `common` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `SafeHttpsResponse.__exit__`

**Signature**

```python
def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
```

**Purpose**

Implements exit according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `exc_type` (`type[BaseException] | None`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `exc_value` (`BaseException | None`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `traceback` (`TracebackType | None`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Calls `self.close()` for its validation or side effect.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `self.close`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `common` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `_validated_timeout`

**Signature**

```python
def _validated_timeout(value: object) -> float:
```

**Purpose**

Validates and returns canonical timeout according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `float`. Observed return expression(s): `timeout`.

**Algorithm**

1. Checks `isinstance(value, bool) or not isinstance(value, Real)`. When true: Raises `SafeHttpsError('HTTPS timeout must be a strict positive finite number')`.
2. Runs guarded operation: Computes `timeout` from `float(value)`. Handles `(OverflowError, TypeError, ValueError)`.
3. Checks `not isfinite(timeout) or timeout <= 0`. When true: Raises `SafeHttpsError('HTTPS timeout must be a strict positive finite number')`.
4. Returns `timeout`.

**Validation and invariants**

- Rejects or diverts the path when `isinstance(value, bool) or not isinstance(value, Real)` is true.
- Rejects or diverts the path when `not isfinite(timeout) or timeout <= 0` is true.

**Exceptions**

- Explicitly raises: `SafeHttpsError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `SafeHttpsError`, `float`, `isfinite`, `isinstance`.

**Known repository callers**

- `src/landscout/common/safe_http.py` — `open_safe_https`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `common` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `_request_parts`

**Signature**

```python
def _request_parts(
    value: str | Request,
    supplied_headers: Mapping[str, str] | None,
) -> tuple[str, dict[str, str]]:
```

**Purpose**

Implements request parts according to the exact implementation and guards in this file.

**Inputs**

- `value` (`str | Request`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `supplied_headers` (`Mapping[str, str] | None`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[str, dict[str, str]]`. Observed return expression(s): `(url, output)`.

**Algorithm**

1. Checks `isinstance(value, Request)`. When true: Checks `value.data is not None or value.get_method().upper() != 'GET'`. When true: Raises `SafeHttpsError('Safe HTTPS source transport supports GET only')`. Computes `url` from `value.full_url`. Computes `combined` from `dict(value.header_items())`. Otherwise: Checks `type(value) is str`. When true: Computes `url` from `value`. Computes `combined` from `{}`. Otherwise: Raises `SafeHttpsError('HTTPS request must be an exact URL string or Request')`.
2. Checks `supplied_headers is not None`. When true: Checks `not isinstance(supplied_headers, Mapping)`. When true: Raises `SafeHttpsError('HTTPS request headers must be a mapping')`. Calls `combined.update(supplied_headers)` for its validation or side effect.
3. Defines `output` with annotation `dict[str, str]` from `{}`.
4. Iterates `(name, header_value)` over `combined.items()`. For each value: Checks `type(name) is not str or type(header_value) is not str`. When true: Raises `SafeHttpsError('HTTPS header names and values must be exact strings')`. Checks `_HEADER_NAME_PATTERN.fullmatch(name) is None`. When true: Raises `SafeHttpsError('HTTPS header name is invalid')`. Checks `name.casefold() == 'host'`. When true: Raises `SafeHttpsError('Caller-supplied Host headers are forbidden')`. Executes 2 additional source-ordered statement(s).
5. Computes `output['Connection']` from `'close'`.
6. Returns `(url, output)`.

**Validation and invariants**

- Rejects or diverts the path when `isinstance(value, Request)` is true.
- Rejects or diverts the path when `supplied_headers is not None` is true.
- Rejects or diverts the path when `value.data is not None or value.get_method().upper() != 'GET'` is true.
- Rejects or diverts the path when `not isinstance(supplied_headers, Mapping)` is true.
- Rejects or diverts the path when `type(name) is not str or type(header_value) is not str` is true.
- Rejects or diverts the path when `_HEADER_NAME_PATTERN.fullmatch(name) is None` is true.
- Rejects or diverts the path when `name.casefold() == 'host'` is true.
- Rejects or diverts the path when `any((ord(character) < 32 or ord(character) == 127 for character in name + header_value))` is true.

**Exceptions**

- Explicitly raises: `SafeHttpsError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `SafeHttpsError`, `_HEADER_NAME_PATTERN.fullmatch`, `any`, `combined.items`, `combined.update`, `dict`, `isinstance`, `name.casefold`, `ord`, `type`, `value.get_method`, `value.get_method().upper`, `value.header_items`.

**Known repository callers**

- `src/landscout/common/safe_http.py` — `open_safe_https`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `common` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `_open_destination`

**Signature**

```python
def _open_destination(
    destination: _ResolvedDestination,
    timeout: float,
    headers: Mapping[str, str],
) -> tuple[http.client.HTTPResponse, _BoundHTTPSConnection]:
```

**Purpose**

Implements open destination according to the exact implementation and guards in this file.

**Inputs**

- `destination` (`_ResolvedDestination`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `timeout` (`float`; required) — network timeout in seconds; validation rejects unsupported or non-positive values. Nullability and accepted values are exactly those enforced by the guards listed below.
- `headers` (`Mapping[str, str]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[http.client.HTTPResponse, _BoundHTTPSConnection]`. Observed return expression(s): `(connection.getresponse(), connection)`.

**Algorithm**

1. Computes `context` from `ssl.create_default_context()`.
2. Defines `last_error` with annotation `BaseException | None` from `None`.
3. Iterates `address` over `destination.addresses`. For each value: Computes `connection` from `_BoundHTTPSConnection(destination.hostname, destination.port, address, timeout=timeout, context=context)`. Runs guarded operation: Calls `connection.request('GET', destination.request_target, headers=dict(headers))` for its validation or side effect. Returns `(connection.getresponse(), connection)`. Handles `SafeHttpsError`, `ssl.SSLError`, `(OSError, http.client.HTTPException)`.
4. Raises `SafeHttpsError('Every validated HTTPS destination address failed')`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `SafeHttpsError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `connection.request`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `SafeHttpsError`, `_BoundHTTPSConnection`, `connection.close`, `connection.getresponse`, `connection.request`, `dict`, `ssl.create_default_context`.

**Known repository callers**

- `src/landscout/common/safe_http.py` — `open_safe_https`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `common` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `_redirect_location`

**Signature**

```python
def _redirect_location(response: http.client.HTTPResponse) -> str:
```

**Purpose**

Implements redirect location according to the exact implementation and guards in this file.

**Inputs**

- `response` (`http.client.HTTPResponse`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `values[0]`.

**Algorithm**

1. Computes `values` from `response.headers.get_all('Location', failobj=[])`.
2. Checks `len(values) != 1 or type(values[0]) is not str or (not values[0])`. When true: Raises `SafeHttpsError('HTTPS redirect requires exactly one Location header')`.
3. Returns `values[0]`.

**Validation and invariants**

- Rejects or diverts the path when `len(values) != 1 or type(values[0]) is not str or (not values[0])` is true.

**Exceptions**

- Explicitly raises: `SafeHttpsError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `SafeHttpsError`, `len`, `response.headers.get_all`, `type`.

**Known repository callers**

- `src/landscout/common/safe_http.py` — `open_safe_https`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `common` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `open_safe_https`

**Signature**

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

**Inputs**

- `url` (`str | Request`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `timeout` (`float`; required) — network timeout in seconds; validation rejects unsupported or non-positive values. Nullability and accepted values are exactly those enforced by the guards listed below.
- `headers` (`Mapping[str, str] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `max_redirects` (`int`; optional/default `_DEFAULT_MAX_REDIRECTS`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `SafeHttpsResponse`. Observed return expression(s): `SafeHttpsResponse(response, connection, url=destination.url, history=tuple(history))`.

**Algorithm**

1. Computes `validated_timeout` from `_validated_timeout(timeout)`.
2. Checks `type(max_redirects) is not int or max_redirects < 0`. When true: Raises `SafeHttpsError('max_redirects must be a non-negative integer')`.
3. Computes `(current_url, request_headers)` from `_request_parts(url, headers)`.
4. Defines `history` with annotation `list[str]` from `[]`.
5. Defines `seen` with annotation `set[str]` from `set()`.
6. Repeats the guarded body while `True` remains true.

**Validation and invariants**

- Rejects or diverts the path when `type(max_redirects) is not int or max_redirects < 0` is true.
- Rejects or diverts the path when `destination.url in seen` is true.
- Rejects or diverts the path when `status in _REDIRECT_STATUSES` is true.
- Rejects or diverts the path when `not 200 <= status < 300` is true.
- Rejects or diverts the path when `len(history) >= max_redirects` is true.

**Exceptions**

- Explicitly raises: `SafeHttpsError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `_open_destination`, `_request_parts`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `SafeHttpsError`, `SafeHttpsResponse`, `_open_destination`, `_redirect_location`, `_request_parts`, `_resolve_destination`, `_validated_timeout`, `connection.close`, `history.append`, `len`, `response.close`, `seen.add`, `set`, `tuple`, `type`, `urljoin`.

**Known repository callers**

- `src/landscout/sources/cadastre_fr.py` — `download_cadastre_parcelles`
- `src/landscout/sources/gpu_fr.py` — `_request_json`
- `src/landscout/sources/gpu_fr.py` — `download_gpu_document`
- `src/landscout/sources/ign_bdtopo_fr.py` — `download_ign_bdtopo_archive`
- `src/landscout/sources/inpn_protected_areas_fr.py` — `_download_archive_bytes`
- `src/landscout/sources/rte_odre_fr.py` — `_read_response_json`
- `src/landscout/sources/rte_odre_fr.py` — `download_rte_odre_dataset`
- `tests/unit/test_safe_http.py` — `_read`
- `tests/unit/test_safe_http.py` — `test_malformed_header_name_is_rejected_before_dns`
- `tests/unit/test_safe_http.py` — `test_safe_https_redirect_is_manually_revalidated`

**Tests**

- `tests/unit/test_safe_http.py::test_malformed_header_name_is_rejected_before_dns`
- `tests/unit/test_safe_http.py::test_safe_https_redirect_is_manually_revalidated`

**Business interpretation**

This symbol contributes to the `common` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `Connection` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |

## 8. Interfaces

Known static callers, internal calls, and tests are listed for every symbol. Package-level availability is controlled by this module's `__all__` and the relevant package `__init__.py`; private helpers are not a stable public API.

## 9. Error handling

Every explicit raise and guarded condition is listed with its function. Public boundaries translate malformed source/configuration/input conditions into the controlled exception classes shown by those functions and tests; raw implementation errors are not promised as API.

## 10. Side effects

Per-function side effects are derived from actual calls. Source adapters may perform guarded network, cache, archive, or filesystem operations; stages normally operate on copies unless their preservation validators state otherwise; tests use the boundaries stated per test.

## 11. Security / trust boundaries

Trust claims are limited to the explicit byte, schema, lineage, source-complete, path, URL, geometry, or policy checks implemented by this file and its callees. Textual lineage is not treated as physical proof unless the function revalidates the physical source.

## 12. GIS / CRS rules

GIS rules apply only where geometry/CRS calls or columns are listed above. Storage geometry is not silently repaired; metric work uses the explicit CRS transformations and calculation copies visible in the algorithm. Files without GIS calls impose no CRS contract.

## 13. Provenance rules

Provenance is carried only through exact source/configuration/hash fields shown by the models, constants, and frame columns. Consult `docs/code/SOURCE_TRUST_MODEL.md` for the cross-adapter chain.

## 14. Business meaning

This file contributes to LandScout's `common` evidence flow as described by its purpose and public symbols. It preserves the distinction among fact, proxy evidence, policy interpretation, diagnostic status, and parcel precheck.

## 15. Explicit non-goals

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

## 16. Tests

Direct name-resolved tests appear under each symbol. Higher-level tests may exercise private helpers through a public source-complete function; companion documents for all test files describe their fixtures, actions, assertions, and boundaries.

## 17. Change impact

Changing this file requires reviewing its static callers, package exports, directly mapped tests, relevant schema/hash/version constants, source locks, persisted artifact contracts, and the corresponding pipeline/cross-cutting documents. Any byte change makes the SHA256 above stale and requires regenerating this companion.

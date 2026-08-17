# `tests/unit/test_safe_http.py`

## File identity

- Repository path: `tests/unit/test_safe_http.py`
- File type: Python test
- Layer: unit/regression test
- Domain: test
- Responsibility: Provides complete unit and regression coverage for the `safe_http` contracts exercised in this file.
- Source SHA256: `90db8d4bcb2e56bb66c2f7a58817fbd49564af39d42777e2cddde008f425ac64`

## 1. Purpose

Provides complete unit and regression coverage for the `safe_http` contracts exercised in this file.

## 2. Position in LandScout architecture

This file belongs to the **unit/regression test** layer and the **test** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `import io`
- `import socket`
- `import ssl`
- `from typing import Any`

### Third-party packages

- `import pytest`

### Internal LandScout imports

- `from landscout.common import safe_http`
- `from landscout.common.safe_http import SafeHttpsError, open_safe_https`

## 4. Contract taxonomy

### A. Python constants

#### `PUBLIC_IPV4`

```python
PUBLIC_IPV4 = "93.184.216.34"
```

Module-level technical/source/policy constant consumed by the exact references below.

#### `PUBLIC_IPV6`

```python
PUBLIC_IPV6 = "2606:4700:4700::1111"
```

Module-level technical/source/policy constant consumed by the exact references below.


### B. Type aliases and closed domains

No module-level Literal/Annotated/TypeAlias declaration is present.

### C. Meaningful dunder contracts

No meaningful module-level dunder contract is declared.

### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

### `_FakeSocket`

**Purpose:** Encapsulates the test behavior implemented by its exact methods and attributes below.

**Kind:** class.

**Inheritance:** plain object.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `family` | `self.family = family  # assigned in __init__` | Closed or validated `family` classification on `_FakeSocket`; accepted values and downstream branches are recoverable from the reproduced validators and consumers. |
| `_response_bytes` | `self._response_bytes = response_bytes  # assigned in __init__` | Stores `_FakeSocket`'s ` response bytes` value under exact annotation `not explicitly annotated`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `_connected` | `self._connected = connected  # assigned in __init__` | Stores `_FakeSocket`'s ` connected` value under exact annotation `not explicitly annotated`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `_sent` | `self._sent = sent  # assigned in __init__` | Stores `_FakeSocket`'s ` sent` value under exact annotation `not explicitly annotated`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `_endpoint` | `self._endpoint = None  # assigned in __init__` | Stores `_FakeSocket`'s ` endpoint` value under exact annotation `not explicitly annotated`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `closed` | `self.closed = False  # assigned in __init__` | Stores `_FakeSocket`'s `closed` value under exact annotation `not explicitly annotated`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `timeout` | `self.timeout = None  # assigned in __init__` | Stores `_FakeSocket`'s `timeout` value under exact annotation `not explicitly annotated`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |

**Interface consumers**

- direct call or construction: `tests/unit/test_safe_http.py::_NetworkHarness.socket` via `_FakeSocket`.

**Exact class source**

```python
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
```

### `_FakeTlsContext`

**Purpose:** Encapsulates the test behavior implemented by its exact methods and attributes below.

**Kind:** class.

**Inheritance:** plain object.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `_server_names` | `self._server_names = server_names  # assigned in __init__` | Stores `_FakeTlsContext`'s ` server names` value under exact annotation `not explicitly annotated`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |

**Interface consumers**

- direct call or construction: `tests/unit/test_safe_http.py::_NetworkHarness.context` via `_FakeTlsContext`.

**Exact class source**

```python
class _FakeTlsContext:
    check_hostname = True
    verify_mode = ssl.CERT_REQUIRED

    def __init__(self, server_names: list[str]) -> None:
        self._server_names = server_names

    def wrap_socket(self, sock: _FakeSocket, *, server_hostname: str) -> _FakeSocket:
        self._server_names.append(server_hostname)
        return sock
```

### `_NetworkHarness`

**Purpose:** Encapsulates the test behavior implemented by its exact methods and attributes below.

**Kind:** class.

**Inheritance:** plain object.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `responses` | `self.responses = list(responses)  # assigned in __init__` | Stores `_NetworkHarness`'s `responses` value under exact annotation `not explicitly annotated`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `connected` | `self.connected = []  # assigned in __init__` | Stores `_NetworkHarness`'s `connected` value under exact annotation `not explicitly annotated`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `sent` | `self.sent = []  # assigned in __init__` | Stores `_NetworkHarness`'s `sent` value under exact annotation `not explicitly annotated`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `server_names` | `self.server_names = []  # assigned in __init__` | Stores `_NetworkHarness`'s `server names` value under exact annotation `not explicitly annotated`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `contexts` | `self.contexts = []  # assigned in __init__` | `_NetworkHarness`'s `contexts` evidence/text field; it retains the exact configured or source meaning under annotation `not explicitly annotated` and is not promoted to a legal conclusion. |
| `sockets` | `self.sockets = []  # assigned in __init__` | Stores `_NetworkHarness`'s `sockets` value under exact annotation `not explicitly annotated`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |

**Interface consumers**

- direct call or construction: `tests/unit/test_safe_http.py::_install_network` via `_NetworkHarness`.

**Exact class source**

```python
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
```


## 6. Functions and methods

### `_http_response`

**Exact signature**

```python
def _http_response(
    status: int = 200,
    *,
    body: bytes = b"ok",
    headers: dict[str, str] | None = None,
) -> bytes:
```

**Purpose**

Private `test` helper for http response; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `bytes`.
- Every observed return expression is reproduced without truncation:
```python
f'HTTP/1.1 {status} {reason}\r\n{header_bytes}\r\n'.encode() + body
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

- direct call or construction: `tests/unit/test_safe_http.py::_install_network` via `_http_response`.
- direct call or construction: `tests/unit/test_safe_http.py::test_safe_https_redirect_is_manually_revalidated` via `_http_response`.
- direct call or construction: `tests/unit/test_safe_http.py::test_unsafe_redirect_is_rejected_before_target_socket` via `_http_response`.
- direct call or construction: `tests/unit/test_safe_http.py::test_redirect_loop_is_rejected` via `_http_response`.
- direct call or construction: `tests/unit/test_safe_http.py::test_redirect_limit_is_enforced` via `_http_response`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_dns_records`

**Exact signature**

```python
def _dns_records(
    addresses: tuple[str, ...],
    port: int,
) -> list[tuple[int, int, int, str, tuple[object, ...]]]:
```

**Purpose**

Private `test` helper for dns records; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `list[tuple[int, int, int, str, tuple[object, ...]]]`.
- Every observed return expression is reproduced without truncation:
```python
result
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

- direct call or construction: `tests/unit/test_safe_http.py::_install_dns.resolve` via `_dns_records`.
- direct call or construction: `tests/unit/test_safe_http.py::test_unsafe_redirect_is_rejected_before_target_socket.resolve` via `_dns_records`.
- direct call or construction: `tests/unit/test_safe_http.py::test_validated_dns_snapshot_binds_actual_socket_and_preserves_tls_host.rebind` via `_dns_records`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_FakeSocket.__init__`

**Exact signature**

```python
def __init__(
        self,
        family: int,
        response_bytes: bytes,
        connected: list[tuple[int, tuple[object, ...]]],
        sent: list[bytes],
    ) -> None:
```

**Purpose**

Private `test` helper for init; its complete implementation below is the authoritative behavioral contract.

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
- In-memory mutation: `self._connected`, `self._response_bytes`, `self._sent`, `self.closed`, `self.family`.
- Input mutation: `self._connected`, `self._endpoint`, `self._response_bytes`, `self._sent`, `self.closed`, `self.family`, `self.timeout`.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/common/safe_http.py::_BoundHTTPSConnection.__init__` via `super().__init__`.
- property/attribute access: `src/landscout/common/safe_http.py::_BoundHTTPSConnection.__init__` via `super().__init__`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_FakeSocket.settimeout`

**Exact signature**

```python
def settimeout(self, timeout: float) -> None:
```

**Purpose**

Private `test` helper for settimeout; its complete implementation below is the authoritative behavioral contract.

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
- In-memory mutation: `self.timeout`.
- Input mutation: `self.timeout`.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/common/safe_http.py::_BoundHTTPSConnection.connect` via `raw_socket.settimeout`.
- property/attribute access: `src/landscout/common/safe_http.py::_BoundHTTPSConnection.connect` via `raw_socket.settimeout`.

**Complete source-ordered implementation**

```python
def settimeout(self, timeout: float) -> None:
        self.timeout = timeout
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_FakeSocket.connect`

**Exact signature**

```python
def connect(self, endpoint: tuple[object, ...]) -> None:
```

**Purpose**

Private `test` helper for connect; its complete implementation below is the authoritative behavioral contract.

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
- In-memory mutation: `self._endpoint`.
- Input mutation: `self._endpoint`.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/common/safe_http.py::_BoundHTTPSConnection.connect` via `raw_socket.connect`.
- property/attribute access: `src/landscout/common/safe_http.py::_BoundHTTPSConnection.connect` via `raw_socket.connect`.

**Complete source-ordered implementation**

```python
def connect(self, endpoint: tuple[object, ...]) -> None:
        self._endpoint = endpoint
        self._connected.append((self.family, endpoint))
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_FakeSocket.getpeername`

**Exact signature**

```python
def getpeername(self) -> tuple[object, ...]:
```

**Purpose**

Private `test` helper for getpeername; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[object, ...]`.
- Every observed return expression is reproduced without truncation:
```python
self._endpoint
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

- direct call or construction: `src/landscout/common/safe_http.py::_BoundHTTPSConnection.connect` via `raw_socket.getpeername`.
- property/attribute access: `src/landscout/common/safe_http.py::_BoundHTTPSConnection.connect` via `raw_socket.getpeername`.

**Complete source-ordered implementation**

```python
def getpeername(self) -> tuple[object, ...]:
        assert self._endpoint is not None
        return self._endpoint
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_FakeSocket.sendall`

**Exact signature**

```python
def sendall(self, payload: bytes) -> None:
```

**Purpose**

Private `test` helper for sendall; its complete implementation below is the authoritative behavioral contract.

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
def sendall(self, payload: bytes) -> None:
        self._sent.append(payload)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_FakeSocket.makefile`

**Exact signature**

```python
def makefile(self, *args: object, **kwargs: object) -> io.BytesIO:
```

**Purpose**

Private `test` helper for makefile; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `io.BytesIO`.
- Every observed return expression is reproduced without truncation:
```python
io.BytesIO(self._response_bytes)
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
def makefile(self, *args: object, **kwargs: object) -> io.BytesIO:
        return io.BytesIO(self._response_bytes)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_FakeSocket.setsockopt`

**Exact signature**

```python
def setsockopt(self, *args: object, **kwargs: object) -> None:
```

**Purpose**

Private `test` helper for setsockopt; its complete implementation below is the authoritative behavioral contract.

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
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

**Complete source-ordered implementation**

```python
def setsockopt(self, *args: object, **kwargs: object) -> None:
        return None
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_FakeSocket.close`

**Exact signature**

```python
def close(self) -> None:
```

**Purpose**

Private `test` helper for close; its complete implementation below is the authoritative behavioral contract.

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
- In-memory mutation: `self.closed`.
- Input mutation: `self.closed`.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/common/safe_http.py::_BoundHTTPSConnection.connect` via `raw_socket.close`.
- property/attribute access: `src/landscout/common/safe_http.py::_BoundHTTPSConnection.connect` via `raw_socket.close`.
- direct call or construction: `src/landscout/common/safe_http.py::SafeHttpsResponse.close` via `self._response.close`.
- property/attribute access: `src/landscout/common/safe_http.py::SafeHttpsResponse.close` via `self._response.close`.
- direct call or construction: `src/landscout/common/safe_http.py::SafeHttpsResponse.close` via `self._connection.close`.
- property/attribute access: `src/landscout/common/safe_http.py::SafeHttpsResponse.close` via `self._connection.close`.
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
        self.closed = True
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_FakeTlsContext.__init__`

**Exact signature**

```python
def __init__(self, server_names: list[str]) -> None:
```

**Purpose**

Private `test` helper for init; its complete implementation below is the authoritative behavioral contract.

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
- In-memory mutation: `self._server_names`.
- Input mutation: `self._server_names`.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/common/safe_http.py::_BoundHTTPSConnection.__init__` via `super().__init__`.
- property/attribute access: `src/landscout/common/safe_http.py::_BoundHTTPSConnection.__init__` via `super().__init__`.

**Complete source-ordered implementation**

```python
def __init__(self, server_names: list[str]) -> None:
        self._server_names = server_names
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_FakeTlsContext.wrap_socket`

**Exact signature**

```python
def wrap_socket(self, sock: _FakeSocket, *, server_hostname: str) -> _FakeSocket:
```

**Purpose**

Private `test` helper for wrap socket; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `_FakeSocket`.
- Every observed return expression is reproduced without truncation:
```python
sock
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

- direct call or construction: `src/landscout/common/safe_http.py::_BoundHTTPSConnection.connect` via `self._tls_context.wrap_socket`.
- property/attribute access: `src/landscout/common/safe_http.py::_BoundHTTPSConnection.connect` via `self._tls_context.wrap_socket`.

**Complete source-ordered implementation**

```python
def wrap_socket(self, sock: _FakeSocket, *, server_hostname: str) -> _FakeSocket:
        self._server_names.append(server_hostname)
        return sock
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_NetworkHarness.__init__`

**Exact signature**

```python
def __init__(self, responses: list[bytes]) -> None:
```

**Purpose**

Private `test` helper for init; its complete implementation below is the authoritative behavioral contract.

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
- In-memory mutation: `self.responses`.
- Input mutation: `self.connected`, `self.contexts`, `self.responses`, `self.sent`, `self.server_names`, `self.sockets`.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/common/safe_http.py::_BoundHTTPSConnection.__init__` via `super().__init__`.
- property/attribute access: `src/landscout/common/safe_http.py::_BoundHTTPSConnection.__init__` via `super().__init__`.

**Complete source-ordered implementation**

```python
def __init__(self, responses: list[bytes]) -> None:
        self.responses = list(responses)
        self.connected: list[tuple[int, tuple[object, ...]]] = []
        self.sent: list[bytes] = []
        self.server_names: list[str] = []
        self.contexts: list[_FakeTlsContext] = []
        self.sockets: list[_FakeSocket] = []
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_NetworkHarness.socket`

**Exact signature**

```python
def socket(
        self,
        family: int = socket.AF_INET,
        type: int = socket.SOCK_STREAM,
        proto: int = 0,
        fileno: int | None = None,
    ) -> _FakeSocket:
```

**Purpose**

Private `test` helper for socket; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `_FakeSocket`.
- Every observed return expression is reproduced without truncation:
```python
result
```

**Validation and exceptions**

- Guard with a raise path: `not self.responses`.
- Explicit raise expressions: `AssertionError('Unexpected additional socket connection')`.

**Side effects**

- Network I/O: `_FakeSocket`, `self.sockets.append`.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/common/safe_http.py::_BoundHTTPSConnection.connect` via `socket.socket`.
- property/attribute access: `src/landscout/common/safe_http.py::_BoundHTTPSConnection.connect` via `socket.socket`.
- callback/property argument: `tests/unit/test_inpn_protected_areas_fr.py::test_valid_physical_and_metadata_cache_is_reused` via `monkeypatch.setattr(safe_http.socket, 'getaddrinfo', fail_dns)`.
- property/attribute access: `tests/unit/test_inpn_protected_areas_fr.py::test_valid_physical_and_metadata_cache_is_reused` via `safe_http.socket`.
- callback/property argument: `tests/unit/test_safe_http.py::_install_network` via `monkeypatch.setattr(safe_http.socket, 'socket', harness.socket)`.
- property/attribute access: `tests/unit/test_safe_http.py::_install_network` via `safe_http.socket`.
- property/attribute access: `tests/unit/test_safe_http.py::_install_network` via `harness.socket`.
- callback/property argument: `tests/unit/test_safe_http.py::_install_dns` via `monkeypatch.setattr(safe_http.socket, 'getaddrinfo', resolve)`.
- property/attribute access: `tests/unit/test_safe_http.py::_install_dns` via `safe_http.socket`.
- callback/property argument: `tests/unit/test_safe_http.py::test_malformed_or_unusable_dns_results_fail_before_socket` via `monkeypatch.setattr(safe_http.socket, 'getaddrinfo', lambda *args, **kwargs: records)`.
- property/attribute access: `tests/unit/test_safe_http.py::test_malformed_or_unusable_dns_results_fail_before_socket` via `safe_http.socket`.
- callback/property argument: `tests/unit/test_safe_http.py::test_malformed_or_unusable_dns_results_fail_before_socket` via `monkeypatch.setattr(safe_http.socket, 'socket', lambda *args, **kwargs: pytest.fail('socket used after invalid DNS'))`.
- callback/property argument: `tests/unit/test_safe_http.py::test_any_nonpublic_dns_answer_fails_before_socket` via `monkeypatch.setattr(safe_http.socket, 'socket', lambda *args, **kwargs: pytest.fail('socket used after unsafe DNS'))`.
- property/attribute access: `tests/unit/test_safe_http.py::test_any_nonpublic_dns_answer_fails_before_socket` via `safe_http.socket`.
- callback/property argument: `tests/unit/test_safe_http.py::test_mixed_public_private_dns_answer_fails_closed` via `monkeypatch.setattr(safe_http.socket, 'socket', lambda *args, **kwargs: pytest.fail('socket used after mixed DNS'))`.
- property/attribute access: `tests/unit/test_safe_http.py::test_mixed_public_private_dns_answer_fails_closed` via `safe_http.socket`.
- callback/property argument: `tests/unit/test_safe_http.py::test_dns_errors_are_controlled_before_socket` via `monkeypatch.setattr(safe_http.socket, 'getaddrinfo', fail)`.
- property/attribute access: `tests/unit/test_safe_http.py::test_dns_errors_are_controlled_before_socket` via `safe_http.socket`.
- callback/property argument: `tests/unit/test_safe_http.py::test_dns_errors_are_controlled_before_socket` via `monkeypatch.setattr(safe_http.socket, 'socket', lambda *args, **kwargs: pytest.fail('socket used after DNS failure'))`.
- callback/property argument: `tests/unit/test_safe_http.py::test_unsafe_url_identity_fails_before_dns` via `monkeypatch.setattr(safe_http.socket, 'getaddrinfo', lambda *args, **kwargs: pytest.fail('DNS used for lexically unsafe URL'))`.
- property/attribute access: `tests/unit/test_safe_http.py::test_unsafe_url_identity_fails_before_dns` via `safe_http.socket`.
- callback/property argument: `tests/unit/test_safe_http.py::test_literal_and_malformed_numeric_ip_rejection_never_uses_dns` via `monkeypatch.setattr(safe_http.socket, 'getaddrinfo', lambda *args, **kwargs: pytest.fail('literal address unexpectedly used DNS'))`.
- property/attribute access: `tests/unit/test_safe_http.py::test_literal_and_malformed_numeric_ip_rejection_never_uses_dns` via `safe_http.socket`.
- callback/property argument: `tests/unit/test_safe_http.py::test_public_literal_ip_uses_exact_socket_without_dns` via `monkeypatch.setattr(safe_http.socket, 'getaddrinfo', lambda *args, **kwargs: pytest.fail('public literal unexpectedly used DNS'))`.
- property/attribute access: `tests/unit/test_safe_http.py::test_public_literal_ip_uses_exact_socket_without_dns` via `safe_http.socket`.
- callback/property argument: `tests/unit/test_safe_http.py::test_unsafe_redirect_is_rejected_before_target_socket` via `monkeypatch.setattr(safe_http.socket, 'getaddrinfo', resolve)`.
- property/attribute access: `tests/unit/test_safe_http.py::test_unsafe_redirect_is_rejected_before_target_socket` via `safe_http.socket`.
- callback/property argument: `tests/unit/test_safe_http.py::test_validated_dns_snapshot_binds_actual_socket_and_preserves_tls_host` via `monkeypatch.setattr(safe_http.socket, 'getaddrinfo', rebind)`.
- property/attribute access: `tests/unit/test_safe_http.py::test_validated_dns_snapshot_binds_actual_socket_and_preserves_tls_host` via `safe_http.socket`.
- callback/property argument: `tests/unit/test_safe_http.py::test_malformed_header_name_is_rejected_before_dns` via `monkeypatch.setattr(safe_http.socket, 'getaddrinfo', lambda *args, **kwargs: pytest.fail('DNS used after malformed header name'))`.
- property/attribute access: `tests/unit/test_safe_http.py::test_malformed_header_name_is_rejected_before_dns` via `safe_http.socket`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_NetworkHarness.context`

**Exact signature**

```python
def context(self, *args: object, **kwargs: object) -> _FakeTlsContext:
```

**Purpose**

Private `test` helper for context; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `_FakeTlsContext`.
- Every observed return expression is reproduced without truncation:
```python
context
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

- callback/function object: `src/landscout/common/safe_http.py::_BoundHTTPSConnection.__init__` via `super().__init__(hostname, port=port, timeout=timeout, context=context)`.
- callback/function object: `src/landscout/common/safe_http.py::_open_destination` via `_BoundHTTPSConnection(destination.hostname, destination.port, address, timeout=timeout, context=context)`.
- callback/function object: `src/landscout/sources/ign_bdtopo_fr.py::_read_verified_layer_frames` via `_verify_unchanged_extraction(context)`.
- callback/function object: `src/landscout/sources/ign_bdtopo_fr.py::load_ign_bdtopo_electricity` via `_read_verified_layer_frames(context, (configured_selection.electric_lines_layer, configured_selection.transformation_posts_layer))`.
- callback/function object: `src/landscout/sources/ign_bdtopo_fr.py::load_ign_bdtopo_roads` via `_read_verified_layer_frames(context, (layer_name,))`.
- callback/function object: `src/landscout/sources/ign_bdtopo_fr.py::load_ign_bdtopo_department_coverage` via `_read_verified_layer_frames(context, (layer_name,))`.
- callback/function object: `src/landscout/stages/enrich_planning_features.py::_normalize_layer` via `_validate_layer_summary(layer, context)`.
- callback/function object: `src/landscout/stages/enrich_planning_features.py::_normalized_catalogs` via `_normalize_layer(fresh_layer, LAYER_SPECS[logical], context, source)`.
- callback/function object: `src/landscout/stages/enrich_planning_features.py::_validate_normalized_planning_feature_inputs` via `_attach_parcel_summaries(source_parcels, metric_parcels, surface_work, line_work, point_work, context)`.
- callback/function object: `src/landscout/stages/enrich_planning_features.py::intersect_parcels_with_gpu_planning_features` via `_attach_parcel_summaries(parcels, metric, surface_work, line_work, point_work, context)`.
- callback/function object: `src/landscout/stages/enrich_planning_zoning.py::intersect_parcels_with_gpu_zoning` via `_normalize_zones(source_zones, context)`.
- callback/function object: `src/landscout/stages/enrich_planning_zoning.py::intersect_parcels_with_gpu_zoning` via `_parcel_summary(parcels, metric_parcels, zones, work, context)`.
- callback/function object: `src/landscout/stages/index_planning_regulation.py::search_planning_regulation` via `_build_hits(index, validated_terms, context)`.
- callback/function object: `src/landscout/stages/index_planning_regulation.py::search_planning_regulation` via `PlanningRegulationSearchResult(document_id=index.document_id, archive_sha256=index.archive_sha256, pdf_sha256=index.pdf_sha256, search_normalization_profile=index.search_normalization_profile, search_hash_schema_version=SEARCH_HASH_SCHEMA_VERSION, index_content_sha256=index.index_content_sha256, requested_terms=requested, context_characters=context, hit_count=len(hits), hits_content_sha256=_hits_content_sha256(index, requested, context, hits), hits=hits)`.
- callback/function object: `src/landscout/stages/index_planning_regulation.py::search_planning_regulation` via `_hits_content_sha256(index, requested, context, hits)`.
- callback/function object: `src/landscout/stages/index_planning_regulation.py::_validate_planning_regulation_search_result` via `_hits_content_sha256(index, requested, context, result.hits, search_schema)`.
- callback/function object: `src/landscout/stages/index_planning_regulation.py::_validate_planning_regulation_search_result` via `_build_hits(index, validated_terms, context)`.
- callback/function object: `src/landscout/stages/normalize_access_ign.py::_normalize_road_frame` via `_validate_source_context(context)`.
- callback/function object: `src/landscout/stages/normalize_access_ign.py::_normalize_ign_roads` via `_normalize_road_frame(source.road_segments, context)`.
- callback/function object: `src/landscout/stages/normalize_grid_ign.py::_normalize_ign_electric_lines` via `_validate_source_context(context)`.
- callback/function object: `src/landscout/stages/normalize_grid_ign.py::_normalize_ign_electric_lines` via `_base_output(working, feature_type='ELECTRIC_LINE', context=context)`.
- callback/function object: `src/landscout/stages/normalize_grid_ign.py::_normalize_ign_transformation_posts` via `_validate_source_context(context)`.
- callback/function object: `src/landscout/stages/normalize_grid_ign.py::_normalize_ign_transformation_posts` via `_base_output(working, feature_type='TRANSFORMATION_POST', context=context)`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::_download_with_session` via `pytest.MonkeyPatch.context`.
- property/attribute access: `tests/unit/test_inpn_protected_areas_fr.py::_download_with_session` via `pytest.MonkeyPatch.context`.
- callback/function object: `tests/unit/test_normalize_grid_ign.py::test_internal_source_context_accepts_supported_department_codes` via `grid_normalization._validate_source_context(context)`.
- callback/function object: `tests/unit/test_normalize_grid_ign.py::test_internal_source_context_rejects_uppercase_sha256` via `normalize_ign_electric_lines(_line_source(), context)`.
- callback/function object: `tests/unit/test_normalize_grid_ign.py::test_internal_source_context_rejects_invalid_lineage_values` via `grid_normalization._validate_source_context(context)`.
- callback/property argument: `tests/unit/test_safe_http.py::_install_network` via `monkeypatch.setattr(safe_http.ssl, 'create_default_context', harness.context)`.
- property/attribute access: `tests/unit/test_safe_http.py::_install_network` via `harness.context`.

**Complete source-ordered implementation**

```python
def context(self, *args: object, **kwargs: object) -> _FakeTlsContext:
        context = _FakeTlsContext(self.server_names)
        self.contexts.append(context)
        return context
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_install_network`

**Exact signature**

```python
def _install_network(
    monkeypatch: pytest.MonkeyPatch,
    *,
    responses: list[bytes] | None = None,
) -> _NetworkHarness:
```

**Purpose**

Private `test` helper for install network; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `_NetworkHarness`.
- Every observed return expression is reproduced without truncation:
```python
harness
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

- direct call or construction: `tests/unit/test_safe_http.py::test_public_dns_answers_are_accepted` via `_install_network`.
- direct call or construction: `tests/unit/test_safe_http.py::test_public_literal_ip_uses_exact_socket_without_dns` via `_install_network`.
- direct call or construction: `tests/unit/test_safe_http.py::test_explicit_https_port_is_resolved_and_connected_exactly` via `_install_network`.
- direct call or construction: `tests/unit/test_safe_http.py::test_safe_https_redirect_is_manually_revalidated` via `_install_network`.
- direct call or construction: `tests/unit/test_safe_http.py::test_unsafe_redirect_is_rejected_before_target_socket` via `_install_network`.
- direct call or construction: `tests/unit/test_safe_http.py::test_redirect_loop_is_rejected` via `_install_network`.
- direct call or construction: `tests/unit/test_safe_http.py::test_redirect_limit_is_enforced` via `_install_network`.
- direct call or construction: `tests/unit/test_safe_http.py::test_validated_dns_snapshot_binds_actual_socket_and_preserves_tls_host` via `_install_network`.
- direct call or construction: `tests/unit/test_safe_http.py::test_environment_proxy_does_not_change_bound_destination` via `_install_network`.
- direct call or construction: `tests/unit/test_safe_http.py::test_tls_context_keeps_hostname_verification_enabled` via `_install_network`.

**Complete source-ordered implementation**

```python
def _install_network(
    monkeypatch: pytest.MonkeyPatch,
    *,
    responses: list[bytes] | None = None,
) -> _NetworkHarness:
    harness = _NetworkHarness(responses or [_http_response()])
    monkeypatch.setattr(safe_http.socket, "socket", harness.socket)
    monkeypatch.setattr(safe_http.ssl, "create_default_context", harness.context)
    return harness
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_install_dns`

**Exact signature**

```python
def _install_dns(
    monkeypatch: pytest.MonkeyPatch,
    addresses: tuple[str, ...],
) -> list[tuple[str, int]]:
```

**Purpose**

Private `test` helper for install dns; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `list[tuple[str, int]]`.
- Every observed return expression is reproduced without truncation:
```python
calls

_dns_records(addresses, port)
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

- direct call or construction: `tests/unit/test_safe_http.py::test_public_dns_answers_are_accepted` via `_install_dns`.
- direct call or construction: `tests/unit/test_safe_http.py::test_any_nonpublic_dns_answer_fails_before_socket` via `_install_dns`.
- direct call or construction: `tests/unit/test_safe_http.py::test_mixed_public_private_dns_answer_fails_closed` via `_install_dns`.
- direct call or construction: `tests/unit/test_safe_http.py::test_explicit_https_port_is_resolved_and_connected_exactly` via `_install_dns`.
- direct call or construction: `tests/unit/test_safe_http.py::test_safe_https_redirect_is_manually_revalidated` via `_install_dns`.
- direct call or construction: `tests/unit/test_safe_http.py::test_redirect_loop_is_rejected` via `_install_dns`.
- direct call or construction: `tests/unit/test_safe_http.py::test_redirect_limit_is_enforced` via `_install_dns`.
- direct call or construction: `tests/unit/test_safe_http.py::test_environment_proxy_does_not_change_bound_destination` via `_install_dns`.
- direct call or construction: `tests/unit/test_safe_http.py::test_tls_context_keeps_hostname_verification_enabled` via `_install_dns`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_install_dns.resolve`

**Exact signature**

```python
def resolve(hostname: str, port: int, **kwargs: object) -> list[tuple[Any, ...]]:
```

**Purpose**

Resolves resolve; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `list[tuple[Any, ...]]`.
- Every observed return expression is reproduced without truncation:
```python
_dns_records(addresses, port)
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

- direct call or construction: `src/landscout/config.py::_resolve_profile_path` via `scan_path.resolve`.
- property/attribute access: `src/landscout/config.py::_resolve_profile_path` via `scan_path.resolve`.
- direct call or construction: `src/landscout/config.py::load_scan_config` via `path.resolve`.
- property/attribute access: `src/landscout/config.py::load_scan_config` via `path.resolve`.
- direct call or construction: `src/landscout/sources/cadastre_loader_fr.py::load_cadastre_parcels` via `path.resolve`.
- property/attribute access: `src/landscout/sources/cadastre_loader_fr.py::load_cadastre_parcels` via `path.resolve`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_inventory` via `path.resolve`.
- property/attribute access: `src/landscout/sources/gpu_fr.py::_inventory` via `path.resolve`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_inventory` via `root.resolve`.
- property/attribute access: `src/landscout/sources/gpu_fr.py::_inventory` via `root.resolve`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::discover_gpu_spatial_layers` via `item.dataset_path.resolve`.
- property/attribute access: `src/landscout/sources/gpu_fr.py::discover_gpu_spatial_layers` via `item.dataset_path.resolve`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_validated_spatial_root` via `root.resolve`.
- property/attribute access: `src/landscout/sources/gpu_fr.py::_validated_spatial_root` via `root.resolve`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_contained_spatial_path` via `path.resolve`.
- property/attribute access: `src/landscout/sources/gpu_fr.py::_contained_spatial_path` via `path.resolve`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_spatial_dataset_relative_path` via `path.resolve`.
- property/attribute access: `src/landscout/sources/gpu_fr.py::_spatial_dataset_relative_path` via `path.resolve`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_spatial_source_family` via `candidate.resolve`.
- property/attribute access: `src/landscout/sources/gpu_fr.py::_spatial_source_family` via `candidate.resolve`.
- direct call or construction: `src/landscout/sources/ign_bdtopo_fr.py::_safe_relative_path` via `path.resolve`.
- property/attribute access: `src/landscout/sources/ign_bdtopo_fr.py::_safe_relative_path` via `path.resolve`.
- direct call or construction: `src/landscout/sources/ign_bdtopo_fr.py::_safe_relative_path` via `root.resolve`.
- property/attribute access: `src/landscout/sources/ign_bdtopo_fr.py::_safe_relative_path` via `root.resolve`.
- direct call or construction: `src/landscout/sources/ign_bdtopo_fr.py::_resolve_relative_path` via `candidate.resolve`.
- property/attribute access: `src/landscout/sources/ign_bdtopo_fr.py::_resolve_relative_path` via `candidate.resolve`.
- direct call or construction: `src/landscout/sources/ign_bdtopo_fr.py::_resolve_relative_path` via `root.resolve`.
- property/attribute access: `src/landscout/sources/ign_bdtopo_fr.py::_resolve_relative_path` via `root.resolve`.
- direct call or construction: `src/landscout/sources/ign_bdtopo_fr.py::_validate_extraction_envelope` via `expected_path.resolve`.
- property/attribute access: `src/landscout/sources/ign_bdtopo_fr.py::_validate_extraction_envelope` via `expected_path.resolve`.
- direct call or construction: `src/landscout/sources/ign_bdtopo_fr.py::_validate_extraction_envelope` via `discovered_path.resolve`.
- property/attribute access: `src/landscout/sources/ign_bdtopo_fr.py::_validate_extraction_envelope` via `discovered_path.resolve`.
- direct call or construction: `src/landscout/sources/ign_bdtopo_fr.py::_validate_extraction_envelope` via `extraction.geopackage_path.resolve`.
- property/attribute access: `src/landscout/sources/ign_bdtopo_fr.py::_validate_extraction_envelope` via `extraction.geopackage_path.resolve`.
- direct call or construction: `src/landscout/sources/ign_bdtopo_fr.py::_load_cached_extraction` via `geopackage_path.resolve`.
- property/attribute access: `src/landscout/sources/ign_bdtopo_fr.py::_load_cached_extraction` via `geopackage_path.resolve`.
- direct call or construction: `src/landscout/sources/ign_bdtopo_fr.py::_load_cached_extraction` via `discovered_path.resolve`.
- property/attribute access: `src/landscout/sources/ign_bdtopo_fr.py::_load_cached_extraction` via `discovered_path.resolve`.
- direct call or construction: `src/landscout/stages/index_planning_regulation.py::_locate_regulation_pdf` via `root.resolve`.
- property/attribute access: `src/landscout/stages/index_planning_regulation.py::_locate_regulation_pdf` via `root.resolve`.
- direct call or construction: `src/landscout/stages/index_planning_regulation.py::_locate_regulation_pdf` via `path.resolve`.
- property/attribute access: `src/landscout/stages/index_planning_regulation.py::_locate_regulation_pdf` via `path.resolve`.
- direct call or construction: `src/landscout/stages/road_vehicle_proxy_policy.py::<module>` via `Path(__file__).resolve`.
- property/attribute access: `src/landscout/stages/road_vehicle_proxy_policy.py::<module>` via `Path(__file__).resolve`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::_materialize_layer` via `reference.dataset_path.resolve`.
- property/attribute access: `tests/unit/test_enrich_planning_features.py::_materialize_layer` via `reference.dataset_path.resolve`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::_planning_document` via `layer.reference.dataset_path.resolve`.
- property/attribute access: `tests/unit/test_enrich_planning_features.py::_planning_document` via `layer.reference.dataset_path.resolve`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_common_planning_contracts_import_without_initializing_stages` via `Path(__file__).resolve`.
- property/attribute access: `tests/unit/test_enrich_planning_features.py::test_common_planning_contracts_import_without_initializing_stages` via `Path(__file__).resolve`.
- callback/function object: `tests/unit/test_safe_http.py::_install_dns` via `monkeypatch.setattr(safe_http.socket, 'getaddrinfo', resolve)`.
- callback/function object: `tests/unit/test_safe_http.py::test_unsafe_redirect_is_rejected_before_target_socket` via `monkeypatch.setattr(safe_http.socket, 'getaddrinfo', resolve)`.

**Complete source-ordered implementation**

```python
def resolve(hostname: str, port: int, **kwargs: object) -> list[tuple[Any, ...]]:
        assert kwargs == {"type": socket.SOCK_STREAM}
        calls.append((hostname, port))
        return _dns_records(addresses, port)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_read`

**Exact signature**

```python
def _read(url: str = "https://source.example/archive.zip") -> bytes:
```

**Purpose**

Reads read; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `bytes`.
- Every observed return expression is reproduced without truncation:
```python
response.read()
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: `open_safe_https`.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_safe_http.py::test_public_dns_answers_are_accepted` via `_read`.
- direct call or construction: `tests/unit/test_safe_http.py::test_malformed_or_unusable_dns_results_fail_before_socket` via `_read`.
- direct call or construction: `tests/unit/test_safe_http.py::test_any_nonpublic_dns_answer_fails_before_socket` via `_read`.
- direct call or construction: `tests/unit/test_safe_http.py::test_mixed_public_private_dns_answer_fails_closed` via `_read`.
- direct call or construction: `tests/unit/test_safe_http.py::test_dns_errors_are_controlled_before_socket` via `_read`.
- direct call or construction: `tests/unit/test_safe_http.py::test_unsafe_url_identity_fails_before_dns` via `_read`.
- direct call or construction: `tests/unit/test_safe_http.py::test_literal_and_malformed_numeric_ip_rejection_never_uses_dns` via `_read`.
- direct call or construction: `tests/unit/test_safe_http.py::test_public_literal_ip_uses_exact_socket_without_dns` via `_read`.
- direct call or construction: `tests/unit/test_safe_http.py::test_explicit_https_port_is_resolved_and_connected_exactly` via `_read`.
- direct call or construction: `tests/unit/test_safe_http.py::test_unsafe_redirect_is_rejected_before_target_socket` via `_read`.
- direct call or construction: `tests/unit/test_safe_http.py::test_redirect_loop_is_rejected` via `_read`.
- direct call or construction: `tests/unit/test_safe_http.py::test_redirect_limit_is_enforced` via `_read`.
- direct call or construction: `tests/unit/test_safe_http.py::test_validated_dns_snapshot_binds_actual_socket_and_preserves_tls_host` via `_read`.
- direct call or construction: `tests/unit/test_safe_http.py::test_environment_proxy_does_not_change_bound_destination` via `_read`.
- direct call or construction: `tests/unit/test_safe_http.py::test_tls_context_keeps_hostname_verification_enabled` via `_read`.

**Complete source-ordered implementation**

```python
def _read(url: str = "https://source.example/archive.zip") -> bytes:
    with open_safe_https(url, timeout=12.5) as response:
        return response.read()
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_public_dns_answers_are_accepted`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `addresses`.

**Setup**

```python
calls = _install_dns(monkeypatch, addresses)
harness = _install_network(monkeypatch)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert _read() == b"ok"
assert calls == [("source.example", 443)]
assert harness.connected
```

**Regression protected**

Proves that one or multiple well-formed globally routable IPv4/IPv6 resolver records are retained as the validated destination candidates.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_public_dns_answers_are_accepted(
    monkeypatch: pytest.MonkeyPatch,
    addresses: tuple[str, ...],
) -> None:
    calls = _install_dns(monkeypatch, addresses)
    harness = _install_network(monkeypatch)

    assert _read() == b"ok"
    assert calls == [("source.example", 443)]
    assert harness.connected
```

### `test_malformed_or_unusable_dns_results_fail_before_socket`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `records`.

**Setup**

```python
monkeypatch.setattr(safe_http.socket, "getaddrinfo", lambda *args, **kwargs: records)
monkeypatch.setattr(
        safe_http.socket,
        "socket",
        lambda *args, **kwargs: pytest.fail("socket used after invalid DNS"),
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(SafeHttpsError, match="DNS|address"):
        _read()
```

**Regression protected**

Prevents malformed getaddrinfo tuple/family/protocol/sockaddr/address records or an empty answer set from being skipped; every answer must parse before any socket is opened.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

```python
def test_malformed_or_unusable_dns_results_fail_before_socket(
    monkeypatch: pytest.MonkeyPatch,
    records: list[tuple[Any, ...]],
) -> None:
    monkeypatch.setattr(safe_http.socket, "getaddrinfo", lambda *args, **kwargs: records)
    monkeypatch.setattr(
        safe_http.socket,
        "socket",
        lambda *args, **kwargs: pytest.fail("socket used after invalid DNS"),
    )

    with pytest.raises(SafeHttpsError, match="DNS|address"):
        _read()
```

### `test_any_nonpublic_dns_answer_fails_before_socket`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `address`.

**Setup**

```python
_install_dns(monkeypatch, (address,))
monkeypatch.setattr(
        safe_http.socket,
        "socket",
        lambda *args, **kwargs: pytest.fail("socket used after unsafe DNS"),
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(SafeHttpsError, match="public|global|address|DNS"):
        _read()
```

**Regression protected**

Prevents loopback, private, link-local, unspecified, multicast, reserved, mapped-private, or otherwise non-global DNS answers from reaching socket creation.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

```python
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
```

### `test_mixed_public_private_dns_answer_fails_closed`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
_install_dns(monkeypatch, (PUBLIC_IPV4, "127.0.0.1"))
monkeypatch.setattr(
        safe_http.socket,
        "socket",
        lambda *args, **kwargs: pytest.fail("socket used after mixed DNS"),
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(SafeHttpsError, match="public|global|address|DNS"):
        _read()
```

**Regression protected**

Prevents an attacker-controlled mixed DNS answer from being accepted by selecting only its public member; one non-public member rejects the whole destination.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

```python
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
```

### `test_dns_errors_are_controlled_before_socket`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `error`.

**Setup**

```python
def fail(*args: object, **kwargs: object) -> list[tuple[Any, ...]]:
        raise error
monkeypatch.setattr(safe_http.socket, "getaddrinfo", fail)
monkeypatch.setattr(
        safe_http.socket,
        "socket",
        lambda *args, **kwargs: pytest.fail("socket used after DNS failure"),
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(SafeHttpsError, match="DNS|resolve"):
        _read()
```

**Regression protected**

Converts resolver failures into SafeHttpsError and proves no transport socket is created after DNS failure.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

```python
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
```

### `test_dns_errors_are_controlled_before_socket.fail`

**Exact signature**

```python
def fail(*args: object, **kwargs: object) -> list[tuple[Any, ...]]:
```

**Purpose**

Private `test` helper for fail; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `list[tuple[Any, ...]]`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `error`.

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

- direct call or construction: `tests/unit/test_gpu_fr.py::test_download_rejects_document_inconsistent_with_config` via `pytest.fail`.
- property/attribute access: `tests/unit/test_gpu_fr.py::test_download_rejects_document_inconsistent_with_config` via `pytest.fail`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_download_rejects_forged_unsafe_archive_name_before_io` via `pytest.fail`.
- property/attribute access: `tests/unit/test_gpu_fr.py::test_download_rejects_forged_unsafe_archive_name_before_io` via `pytest.fail`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_fresh_cache_is_reused` via `pytest.fail`.
- property/attribute access: `tests/unit/test_gpu_fr.py::test_fresh_cache_is_reused` via `pytest.fail`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_stale_recovery_backup_rejects_cache_before_network.fail_network` via `pytest.fail`.
- property/attribute access: `tests/unit/test_gpu_fr.py::test_stale_recovery_backup_rejects_cache_before_network.fail_network` via `pytest.fail`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_failed_refresh_preserves_previous_cache` via `monkeypatch.setattr(gpu, 'open_safe_https', fail)`.
- direct call or construction: `tests/unit/test_safe_http.py::test_malformed_or_unusable_dns_results_fail_before_socket` via `pytest.fail`.
- property/attribute access: `tests/unit/test_safe_http.py::test_malformed_or_unusable_dns_results_fail_before_socket` via `pytest.fail`.
- direct call or construction: `tests/unit/test_safe_http.py::test_any_nonpublic_dns_answer_fails_before_socket` via `pytest.fail`.
- property/attribute access: `tests/unit/test_safe_http.py::test_any_nonpublic_dns_answer_fails_before_socket` via `pytest.fail`.
- direct call or construction: `tests/unit/test_safe_http.py::test_mixed_public_private_dns_answer_fails_closed` via `pytest.fail`.
- property/attribute access: `tests/unit/test_safe_http.py::test_mixed_public_private_dns_answer_fails_closed` via `pytest.fail`.
- callback/function object: `tests/unit/test_safe_http.py::test_dns_errors_are_controlled_before_socket` via `monkeypatch.setattr(safe_http.socket, 'getaddrinfo', fail)`.
- direct call or construction: `tests/unit/test_safe_http.py::test_dns_errors_are_controlled_before_socket` via `pytest.fail`.
- property/attribute access: `tests/unit/test_safe_http.py::test_dns_errors_are_controlled_before_socket` via `pytest.fail`.
- direct call or construction: `tests/unit/test_safe_http.py::test_unsafe_url_identity_fails_before_dns` via `pytest.fail`.
- property/attribute access: `tests/unit/test_safe_http.py::test_unsafe_url_identity_fails_before_dns` via `pytest.fail`.
- direct call or construction: `tests/unit/test_safe_http.py::test_literal_and_malformed_numeric_ip_rejection_never_uses_dns` via `pytest.fail`.
- property/attribute access: `tests/unit/test_safe_http.py::test_literal_and_malformed_numeric_ip_rejection_never_uses_dns` via `pytest.fail`.
- direct call or construction: `tests/unit/test_safe_http.py::test_public_literal_ip_uses_exact_socket_without_dns` via `pytest.fail`.
- property/attribute access: `tests/unit/test_safe_http.py::test_public_literal_ip_uses_exact_socket_without_dns` via `pytest.fail`.
- direct call or construction: `tests/unit/test_safe_http.py::test_malformed_header_name_is_rejected_before_dns` via `pytest.fail`.
- property/attribute access: `tests/unit/test_safe_http.py::test_malformed_header_name_is_rejected_before_dns` via `pytest.fail`.

**Complete source-ordered implementation**

```python
def fail(*args: object, **kwargs: object) -> list[tuple[Any, ...]]:
        raise error
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unsafe_url_identity_fails_before_dns`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `url`.

**Setup**

```python
monkeypatch.setattr(
        safe_http.socket,
        "getaddrinfo",
        lambda *args, **kwargs: pytest.fail("DNS used for lexically unsafe URL"),
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(SafeHttpsError, match="HTTPS|credential|localhost|host|URL"):
        _read(url)
```

**Regression protected**

Rejects non-HTTPS, credentialed, localhost, malformed-port, or otherwise unsafe URL identity before resolver or socket activity.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

```python
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
```

### `test_literal_and_malformed_numeric_ip_rejection_never_uses_dns`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `url`.

**Setup**

```python
monkeypatch.setattr(
        safe_http.socket,
        "getaddrinfo",
        lambda *args, **kwargs: pytest.fail("literal address unexpectedly used DNS"),
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(SafeHttpsError, match="public|global|address|IP|URL"):
        _read(url)
```

**Regression protected**

Pins strict literal/numeric-IP parsing: unsafe or malformed numeric forms fail locally and cannot be reinterpreted through DNS.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

```python
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
```

### `test_public_literal_ip_uses_exact_socket_without_dns`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
monkeypatch.setattr(
        safe_http.socket,
        "getaddrinfo",
        lambda *args, **kwargs: pytest.fail("public literal unexpectedly used DNS"),
    )
harness = _install_network(monkeypatch)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert _read(f"https://{PUBLIC_IPV4}/archive.zip") == b"ok"
assert harness.connected == [(socket.AF_INET, (PUBLIC_IPV4, 443))]
```

**Regression protected**

Proves a globally routable literal IP bypasses DNS and the bound socket connects to that exact numeric endpoint.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
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
```

### `test_explicit_https_port_is_resolved_and_connected_exactly`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
calls = _install_dns(monkeypatch, (PUBLIC_IPV4,))
harness = _install_network(monkeypatch)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert _read("https://source.example:8443/archive.zip") == b"ok"
assert calls == [("source.example", 8443)]
assert harness.connected == [(socket.AF_INET, (PUBLIC_IPV4, 8443))]
assert harness.server_names == ["source.example"]
assert b"\r\nHost: source.example:8443\r\n" in b"".join(harness.sent)
```

**Regression protected**

Pins explicit-port handling across DNS, numeric socket endpoint, HTTP Host header, and original hostname TLS SNI.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
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
```

### `test_safe_https_redirect_is_manually_revalidated`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
calls = _install_dns(monkeypatch, (PUBLIC_IPV4,))
harness = _install_network(
        monkeypatch,
        responses=[
            _http_response(302, body=b"", headers={"Location": "https://cdn.example/file"}),
            _http_response(body=b"archive"),
        ],
    )
```

**Action**

```python
with open_safe_https(
        "https://source.example/archive.zip",
        timeout=12.5,
    ) as response:
        assert response.read() == b"archive"
        assert response.url == "https://cdn.example/file"
        assert response.history == ("https://source.example/archive.zip",)
```

**Expected result**

```python
assert calls == [("source.example", 443), ("cdn.example", 443)]
assert [endpoint for _, endpoint in harness.connected] == [
        (PUBLIC_IPV4, 443),
        (PUBLIC_IPV4, 443),
    ]
assert harness.server_names == ["source.example", "cdn.example"]
assert b"\r\nHost: source.example\r\n" in harness.sent[0]
assert b"\r\nHost: cdn.example\r\n" in harness.sent[1]
```

**Regression protected**

Proves each redirect target is resolved/validated before its own request and that final URL/history plus per-hop Host/SNI identities remain exact.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_safe_https_redirect_is_manually_revalidated(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    calls = _install_dns(monkeypatch, (PUBLIC_IPV4,))
    harness = _install_network(
        monkeypatch,
        responses=[
            _http_response(302, body=b"", headers={"Location": "https://cdn.example/file"}),
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
```

### `test_unsafe_redirect_is_rejected_before_target_socket`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
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
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(SafeHttpsError, match="public|global|address|DNS"):
        _read()
assert harness.connected == [(socket.AF_INET, (PUBLIC_IPV4, 443))]
```

**Regression protected**

Prevents an unsafe Location target from creating a second-hop socket while allowing only the already validated first request needed to receive the redirect.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
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
```

### `test_unsafe_redirect_is_rejected_before_target_socket.resolve`

**Exact signature**

```python
def resolve(hostname: str, port: int, **kwargs: object) -> list[tuple[Any, ...]]:
```

**Purpose**

Resolves resolve; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `list[tuple[Any, ...]]`.
- Every observed return expression is reproduced without truncation:
```python
_dns_records((address,), port)
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

- direct call or construction: `src/landscout/config.py::_resolve_profile_path` via `scan_path.resolve`.
- property/attribute access: `src/landscout/config.py::_resolve_profile_path` via `scan_path.resolve`.
- direct call or construction: `src/landscout/config.py::load_scan_config` via `path.resolve`.
- property/attribute access: `src/landscout/config.py::load_scan_config` via `path.resolve`.
- direct call or construction: `src/landscout/sources/cadastre_loader_fr.py::load_cadastre_parcels` via `path.resolve`.
- property/attribute access: `src/landscout/sources/cadastre_loader_fr.py::load_cadastre_parcels` via `path.resolve`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_inventory` via `path.resolve`.
- property/attribute access: `src/landscout/sources/gpu_fr.py::_inventory` via `path.resolve`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_inventory` via `root.resolve`.
- property/attribute access: `src/landscout/sources/gpu_fr.py::_inventory` via `root.resolve`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::discover_gpu_spatial_layers` via `item.dataset_path.resolve`.
- property/attribute access: `src/landscout/sources/gpu_fr.py::discover_gpu_spatial_layers` via `item.dataset_path.resolve`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_validated_spatial_root` via `root.resolve`.
- property/attribute access: `src/landscout/sources/gpu_fr.py::_validated_spatial_root` via `root.resolve`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_contained_spatial_path` via `path.resolve`.
- property/attribute access: `src/landscout/sources/gpu_fr.py::_contained_spatial_path` via `path.resolve`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_spatial_dataset_relative_path` via `path.resolve`.
- property/attribute access: `src/landscout/sources/gpu_fr.py::_spatial_dataset_relative_path` via `path.resolve`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_spatial_source_family` via `candidate.resolve`.
- property/attribute access: `src/landscout/sources/gpu_fr.py::_spatial_source_family` via `candidate.resolve`.
- direct call or construction: `src/landscout/sources/ign_bdtopo_fr.py::_safe_relative_path` via `path.resolve`.
- property/attribute access: `src/landscout/sources/ign_bdtopo_fr.py::_safe_relative_path` via `path.resolve`.
- direct call or construction: `src/landscout/sources/ign_bdtopo_fr.py::_safe_relative_path` via `root.resolve`.
- property/attribute access: `src/landscout/sources/ign_bdtopo_fr.py::_safe_relative_path` via `root.resolve`.
- direct call or construction: `src/landscout/sources/ign_bdtopo_fr.py::_resolve_relative_path` via `candidate.resolve`.
- property/attribute access: `src/landscout/sources/ign_bdtopo_fr.py::_resolve_relative_path` via `candidate.resolve`.
- direct call or construction: `src/landscout/sources/ign_bdtopo_fr.py::_resolve_relative_path` via `root.resolve`.
- property/attribute access: `src/landscout/sources/ign_bdtopo_fr.py::_resolve_relative_path` via `root.resolve`.
- direct call or construction: `src/landscout/sources/ign_bdtopo_fr.py::_validate_extraction_envelope` via `expected_path.resolve`.
- property/attribute access: `src/landscout/sources/ign_bdtopo_fr.py::_validate_extraction_envelope` via `expected_path.resolve`.
- direct call or construction: `src/landscout/sources/ign_bdtopo_fr.py::_validate_extraction_envelope` via `discovered_path.resolve`.
- property/attribute access: `src/landscout/sources/ign_bdtopo_fr.py::_validate_extraction_envelope` via `discovered_path.resolve`.
- direct call or construction: `src/landscout/sources/ign_bdtopo_fr.py::_validate_extraction_envelope` via `extraction.geopackage_path.resolve`.
- property/attribute access: `src/landscout/sources/ign_bdtopo_fr.py::_validate_extraction_envelope` via `extraction.geopackage_path.resolve`.
- direct call or construction: `src/landscout/sources/ign_bdtopo_fr.py::_load_cached_extraction` via `geopackage_path.resolve`.
- property/attribute access: `src/landscout/sources/ign_bdtopo_fr.py::_load_cached_extraction` via `geopackage_path.resolve`.
- direct call or construction: `src/landscout/sources/ign_bdtopo_fr.py::_load_cached_extraction` via `discovered_path.resolve`.
- property/attribute access: `src/landscout/sources/ign_bdtopo_fr.py::_load_cached_extraction` via `discovered_path.resolve`.
- direct call or construction: `src/landscout/stages/index_planning_regulation.py::_locate_regulation_pdf` via `root.resolve`.
- property/attribute access: `src/landscout/stages/index_planning_regulation.py::_locate_regulation_pdf` via `root.resolve`.
- direct call or construction: `src/landscout/stages/index_planning_regulation.py::_locate_regulation_pdf` via `path.resolve`.
- property/attribute access: `src/landscout/stages/index_planning_regulation.py::_locate_regulation_pdf` via `path.resolve`.
- direct call or construction: `src/landscout/stages/road_vehicle_proxy_policy.py::<module>` via `Path(__file__).resolve`.
- property/attribute access: `src/landscout/stages/road_vehicle_proxy_policy.py::<module>` via `Path(__file__).resolve`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::_materialize_layer` via `reference.dataset_path.resolve`.
- property/attribute access: `tests/unit/test_enrich_planning_features.py::_materialize_layer` via `reference.dataset_path.resolve`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::_planning_document` via `layer.reference.dataset_path.resolve`.
- property/attribute access: `tests/unit/test_enrich_planning_features.py::_planning_document` via `layer.reference.dataset_path.resolve`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_common_planning_contracts_import_without_initializing_stages` via `Path(__file__).resolve`.
- property/attribute access: `tests/unit/test_enrich_planning_features.py::test_common_planning_contracts_import_without_initializing_stages` via `Path(__file__).resolve`.
- callback/function object: `tests/unit/test_safe_http.py::_install_dns` via `monkeypatch.setattr(safe_http.socket, 'getaddrinfo', resolve)`.
- callback/function object: `tests/unit/test_safe_http.py::test_unsafe_redirect_is_rejected_before_target_socket` via `monkeypatch.setattr(safe_http.socket, 'getaddrinfo', resolve)`.

**Complete source-ordered implementation**

```python
def resolve(hostname: str, port: int, **kwargs: object) -> list[tuple[Any, ...]]:
        address = PUBLIC_IPV4 if hostname == "source.example" else "127.0.0.1"
        return _dns_records((address,), port)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_redirect_loop_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
_install_dns(monkeypatch, (PUBLIC_IPV4,))
_install_network(
        monkeypatch,
        responses=[
            _http_response(302, body=b"", headers={"Location": "/archive.zip"})
        ],
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(SafeHttpsError, match="loop"):
        _read()
```

**Regression protected**

Prevents cyclic Location chains from causing unbounded requests and preserves controlled cleanup.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_redirect_loop_is_rejected(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _install_dns(monkeypatch, (PUBLIC_IPV4,))
    _install_network(
        monkeypatch,
        responses=[
            _http_response(302, body=b"", headers={"Location": "/archive.zip"})
        ],
    )

    with pytest.raises(SafeHttpsError, match="loop"):
        _read()
```

### `test_redirect_limit_is_enforced`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
_install_dns(monkeypatch, (PUBLIC_IPV4,))
redirects = [
        _http_response(302, body=b"", headers={"Location": f"/step-{index}"})
        for index in range(12)
    ]
_install_network(monkeypatch, responses=redirects)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(SafeHttpsError, match="redirect"):
        _read()
```

**Regression protected**

Pins the finite redirect budget so a non-cyclic chain cannot exceed the configured maximum.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
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
```

### `test_validated_dns_snapshot_binds_actual_socket_and_preserves_tls_host`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
resolutions = 0
def rebind(hostname: str, port: int, **kwargs: object) -> list[tuple[Any, ...]]:
        nonlocal resolutions
        resolutions += 1
        address = PUBLIC_IPV4 if resolutions == 1 else "127.0.0.1"
        return _dns_records((address,), port)
monkeypatch.setattr(safe_http.socket, "getaddrinfo", rebind)
harness = _install_network(monkeypatch)
request = b"".join(harness.sent).decode("ascii")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert _read("https://rebind.example/archive.zip") == b"ok"
assert resolutions == 1
assert harness.connected == [(socket.AF_INET, (PUBLIC_IPV4, 443))]
assert harness.server_names == ["rebind.example"]
assert request.startswith("GET /archive.zip HTTP/1.1\r\n")
assert "\r\nHost: rebind.example\r\n" in request
```

**Regression protected**

Prevents DNS rebinding: validation must occur once, the actual socket must connect to an IP from that validated snapshot, a later hostname answer cannot redirect transport to loopback/private space, and TLS SNI/certificate plus HTTP Host must remain the original hostname.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
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
```

### `test_validated_dns_snapshot_binds_actual_socket_and_preserves_tls_host.rebind`

**Exact signature**

```python
def rebind(hostname: str, port: int, **kwargs: object) -> list[tuple[Any, ...]]:
```

**Purpose**

Private `test` helper for rebind; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `list[tuple[Any, ...]]`.
- Every observed return expression is reproduced without truncation:
```python
_dns_records((address,), port)
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

- callback/function object: `tests/unit/test_safe_http.py::test_validated_dns_snapshot_binds_actual_socket_and_preserves_tls_host` via `monkeypatch.setattr(safe_http.socket, 'getaddrinfo', rebind)`.

**Complete source-ordered implementation**

```python
def rebind(hostname: str, port: int, **kwargs: object) -> list[tuple[Any, ...]]:
        nonlocal resolutions
        resolutions += 1
        address = PUBLIC_IPV4 if resolutions == 1 else "127.0.0.1"
        return _dns_records((address,), port)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_environment_proxy_does_not_change_bound_destination`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
monkeypatch.setenv("HTTP_PROXY", "http://127.0.0.1:9999")
monkeypatch.setenv("HTTPS_PROXY", "http://127.0.0.1:9999")
monkeypatch.setenv("ALL_PROXY", "http://127.0.0.1:9999")
_install_dns(monkeypatch, (PUBLIC_IPV4,))
harness = _install_network(monkeypatch)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert _read() == b"ok"
assert harness.connected == [(socket.AF_INET, (PUBLIC_IPV4, 443))]
```

**Regression protected**

Proves HTTP(S)_PROXY/NO_PROXY environment state cannot redirect transport because the helper opens its own validated numeric socket.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
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
```

### `test_malformed_header_name_is_rejected_before_dns`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `header_name`.

**Setup**

```python
monkeypatch.setattr(
        safe_http.socket,
        "getaddrinfo",
        lambda *args, **kwargs: pytest.fail("DNS used after malformed header name"),
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(SafeHttpsError, match="header|Host"), open_safe_https(
        "https://source.example/archive.zip",
        timeout=12.5,
        headers={header_name: "attacker.example"},
    ):
        pass
```

**Regression protected**

Rejects invalid RFC token header names and Host-like whitespace variants before DNS, preventing ambiguous duplicate Host parsing.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_malformed_header_name_is_rejected_before_dns(
    monkeypatch: pytest.MonkeyPatch,
    header_name: str,
) -> None:
    monkeypatch.setattr(
        safe_http.socket,
        "getaddrinfo",
        lambda *args, **kwargs: pytest.fail("DNS used after malformed header name"),
    )

    with pytest.raises(SafeHttpsError, match="header|Host"), open_safe_https(
        "https://source.example/archive.zip",
        timeout=12.5,
        headers={header_name: "attacker.example"},
    ):
        pass
```

### `test_tls_context_keeps_hostname_verification_enabled`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
_install_dns(monkeypatch, (PUBLIC_IPV4,))
harness = _install_network(monkeypatch)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert _read() == b"ok"
assert harness.server_names == ["source.example"]
assert len(harness.contexts) == 1
assert harness.contexts[0].check_hostname is True
assert harness.contexts[0].verify_mode == ssl.CERT_REQUIRED
```

**Regression protected**

Pins default certificate verification and hostname checking on the TLS context used for the bound numeric socket.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
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
```


## 7. Data contracts

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


## 12. GIS / CRS rules

Only the explicit CRS/geometry validators and calculation copies in this module establish GIS behavior. No geometry repair, reprojection, or metric meaning is inferred from a field name alone.

## 13. Provenance rules

Configured identity, row lineage, byte identity, cache metadata, and source-complete revalidation are separate levels. This companion claims only the levels implemented above.

## 14. Business meaning

The module contributes to the test flow through the exact facts, proxy evidence, policy results, diagnostics, or prechecks identified above.

## 15. Explicit non-goals

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

## 16. Tests

Test consumers and framework invocation are included in per-symbol interfaces. Test modules distinguish fixture injection from parameterized values and reproduce setup/action/assertion source.

## 17. Change impact

Any source-byte change invalidates the SHA above. Review exact exports, aliases, canonical frame schemas/dtypes, configured source/policy identities, callers, framework hooks, artifacts, and all linked tests before updating this companion.

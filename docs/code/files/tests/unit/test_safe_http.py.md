# `tests/unit/test_safe_http.py`

## File identity

- Repository path: `tests/unit/test_safe_http.py`
- File type: Python source
- Layer: unit/regression test
- Domain: isolated contract test evidence
- Responsibility: Provides complete unit and regression coverage for the `safe_http` contracts exercised in this file.
- Source SHA256: `da5bf1e22f8aac6d3c0634d88786dcb5c79a7c764902490d0157f9b6965b69f0`

## 1. STEP 7F.1A.4 contract delta

- Refreshes permanent STEP 7F.1A.4 regression coverage for safe http; the exact fixtures, mutations, calls, controlled failures, and assertions are inventoried below.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Provides complete unit and regression coverage for the `safe_http` contracts exercised in this file.

The file belongs to the **unit/regression test** layer and **isolated contract test evidence** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `import io`
- `import socket`
- `import ssl`
- `from typing import Any`
- `from urllib.request import Request`

### Third-party packages

- `import pytest`

### Internal LandScout imports

- `from landscout.common import safe_http`
- `from landscout.common.safe_http import SafeHttpsError, open_safe_https`

## 4. Contract taxonomy

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `PUBLIC_IPV4`

- Category: module constant or closed domain.
- Exact declaration:

```python
PUBLIC_IPV4 = "93.184.216.34"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `PUBLIC_IPV6`

- Category: module constant or closed domain.
- Exact declaration:

```python
PUBLIC_IPV6 = "2606:4700:4700::1111"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

### `_FakeSocket`

**Source purpose:** Defines `_FakeSocket`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `family` | `assigned instance field` | `family` | `self.family = family` |
| `_response_bytes` | `assigned instance field` | `response_bytes` | `self._response_bytes = response_bytes` |
| `_connected` | `assigned instance field` | `connected` | `self._connected = connected` |
| `_sent` | `assigned instance field` | `sent` | `self._sent = sent` |
| `_endpoint` | `tuple[object, ...] \| None` | `None` | `self._endpoint: tuple[object, ...] \| None = None` |
| `closed` | `assigned instance field` | `False` | `self.closed = False` |
| `timeout` | `float \| None` | `None` | `self.timeout: float \| None = None` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- value/type reference: `tests.unit.test_safe_http::_FakeTlsContext.wrap_socket` via `_FakeSocket`
- value/type reference: `tests.unit.test_safe_http::_NetworkHarness.__init__` via `_FakeSocket`
- constructor call: `tests.unit.test_safe_http::_NetworkHarness.socket` via `_FakeSocket`
- value/type reference: `tests.unit.test_safe_http::_NetworkHarness.socket` via `_FakeSocket`

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

**Source purpose:** Defines `_FakeTlsContext`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `check_hostname` | `inferred from assignment` | `True` | `check_hostname = True` |
| `verify_mode` | `inferred from assignment` | `ssl.CERT_REQUIRED` | `verify_mode = ssl.CERT_REQUIRED` |
| `_server_names` | `assigned instance field` | `server_names` | `self._server_names = server_names` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- value/type reference: `tests.unit.test_safe_http::_NetworkHarness.__init__` via `_FakeTlsContext`
- constructor call: `tests.unit.test_safe_http::_NetworkHarness.context` via `_FakeTlsContext`
- value/type reference: `tests.unit.test_safe_http::_NetworkHarness.context` via `_FakeTlsContext`

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

**Source purpose:** Defines `_NetworkHarness`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `responses` | `assigned instance field` | `list(responses)` | `self.responses = list(responses)` |
| `connected` | `list[tuple[int, tuple[object, ...]]]` | `[]` | `self.connected: list[tuple[int, tuple[object, ...]]] = []` |
| `sent` | `list[bytes]` | `[]` | `self.sent: list[bytes] = []` |
| `server_names` | `list[str]` | `[]` | `self.server_names: list[str] = []` |
| `contexts` | `list[_FakeTlsContext]` | `[]` | `self.contexts: list[_FakeTlsContext] = []` |
| `sockets` | `list[_FakeSocket]` | `[]` | `self.sockets: list[_FakeSocket] = []` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- constructor call: `tests.unit.test_safe_http::_install_network` via `_NetworkHarness`
- value/type reference: `tests.unit.test_safe_http::_install_network` via `_NetworkHarness`

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


## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `_http_response`

**Purpose:** Implements `http response` within the file role: Provides complete unit and regression coverage for the `safe_http` contracts exercised in this file.

**Exact signature**

```python
def _http_response(
    status: int = 200,
    *,
    body: bytes = b"ok",
    headers: dict[str, str] | None = None,
) -> bytes:
```

- Exact decorators: none.
- Declared return annotation: `bytes`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `status` | positional-or-keyword | `int` | `200` |
| `body` | keyword-only | `bytes` | `b'ok'` |
| `headers` | keyword-only | `dict[str, str] \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `f"HTTP/1.1 {status} {reason}\r\n{header_bytes}\r\n".encode() + body`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_safe_http::_install_network` via `_http_response`
- value/type reference: `tests.unit.test_safe_http::_install_network` via `_http_response`
- direct call: `tests.unit.test_safe_http::test_cross_origin_redirect_cannot_receive_a_sensitive_header` via `_http_response`
- value/type reference: `tests.unit.test_safe_http::test_cross_origin_redirect_cannot_receive_a_sensitive_header` via `_http_response`
- direct call: `tests.unit.test_safe_http::test_cross_origin_redirect_forwards_only_safe_ordinary_headers` via `_http_response`
- value/type reference: `tests.unit.test_safe_http::test_cross_origin_redirect_forwards_only_safe_ordinary_headers` via `_http_response`
- direct call: `tests.unit.test_safe_http::test_safe_https_redirect_is_manually_revalidated` via `_http_response`
- value/type reference: `tests.unit.test_safe_http::test_safe_https_redirect_is_manually_revalidated` via `_http_response`
- direct call: `tests.unit.test_safe_http::test_unsafe_redirect_is_rejected_before_target_socket` via `_http_response`
- value/type reference: `tests.unit.test_safe_http::test_unsafe_redirect_is_rejected_before_target_socket` via `_http_response`
- direct call: `tests.unit.test_safe_http::test_redirect_loop_is_rejected` via `_http_response`
- value/type reference: `tests.unit.test_safe_http::test_redirect_loop_is_rejected` via `_http_response`
- direct call: `tests.unit.test_safe_http::test_redirect_limit_is_enforced` via `_http_response`
- value/type reference: `tests.unit.test_safe_http::test_redirect_limit_is_enforced` via `_http_response`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `{<br>        200: "OK",<br>        301: "Moved Permanently",<br>        302: "Found",<br>        303: "See Other",<br>        307: "Temporary Redirect",<br>        308: "Permanent Redirect",<br>    }.get` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `"".join` | `unresolved local/third-party receiver; no ownership inferred` |
| `values.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `f"HTTP/1.1 {status} {reason}\r\n{header_bytes}\r\n".encode` | `unresolved local/third-party receiver; no ownership inferred` |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_dns_records`

**Purpose:** Implements `dns records` within the file role: Provides complete unit and regression coverage for the `safe_http` contracts exercised in this file.

**Exact signature**

```python
def _dns_records(
    addresses: tuple[str, ...],
    port: int,
) -> list[tuple[int, int, int, str, tuple[object, ...]]]:
```

- Exact decorators: none.
- Declared return annotation: `list[tuple[int, int, int, str, tuple[object, ...]]]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `addresses` | positional-or-keyword | `tuple[str, ...]` | `required` |
| `port` | positional-or-keyword | `int` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `result`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_safe_http::_install_dns.resolve` via `_dns_records`
- value/type reference: `tests.unit.test_safe_http::_install_dns.resolve` via `_dns_records`
- direct call: `tests.unit.test_safe_http::test_unsafe_redirect_is_rejected_before_target_socket.resolve` via `_dns_records`
- value/type reference: `tests.unit.test_safe_http::test_unsafe_redirect_is_rejected_before_target_socket.resolve` via `_dns_records`
- direct call: `tests.unit.test_safe_http::test_validated_dns_snapshot_binds_actual_socket_and_preserves_tls_host.rebind` via `_dns_records`
- value/type reference: `tests.unit.test_safe_http::test_validated_dns_snapshot_binds_actual_socket_and_preserves_tls_host.rebind` via `_dns_records`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `result.append` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `result.append(<br>                (<br>                    socket.AF_INET6,<br>                    socket.SOCK_STREAM,<br>                    socket.IPPROTO_TCP,<br>                    "",<br>                    (address, port, 0, 0),<br>                )<br>            )`<br>`result.append(<br>                (<br>                    socket.AF_INET,<br>                    socket.SOCK_STREAM,<br>                    socket.IPPROTO_TCP,<br>                    "",<br>                    (address, port),<br>                )<br>            )` |
| Direct parameter mutation | None directly present. |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_FakeSocket.__init__`

**Purpose:** Implements `init` within the file role: Provides complete unit and regression coverage for the `safe_http` contracts exercised in this file.

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

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |
| `family` | positional-or-keyword | `int` | `required` |
| `response_bytes` | positional-or-keyword | `bytes` | `required` |
| `connected` | positional-or-keyword | `list[tuple[int, tuple[object, ...]]]` | `required` |
| `sent` | positional-or-keyword | `list[bytes]` | `required` |

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
| In-memory mutation | `self.family = family`<br>`self._response_bytes = response_bytes`<br>`self._connected = connected`<br>`self._sent = sent`<br>`self._endpoint: tuple[object, ...] \| None = None`<br>`self.closed = False`<br>`self.timeout: float \| None = None` |
| Direct parameter mutation | `self.family = family`<br>`self._response_bytes = response_bytes`<br>`self._connected = connected`<br>`self._sent = sent`<br>`self._endpoint: tuple[object, ...] \| None = None`<br>`self.closed = False`<br>`self.timeout: float \| None = None` |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_FakeSocket.settimeout`

**Purpose:** Implements `settimeout` within the file role: Provides complete unit and regression coverage for the `safe_http` contracts exercised in this file.

**Exact signature**

```python
def settimeout(self, timeout: float) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |
| `timeout` | positional-or-keyword | `float` | `required` |

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
| In-memory mutation | `self.timeout = timeout` |
| Direct parameter mutation | `self.timeout = timeout` |

**Complete source-ordered implementation**

```python
def settimeout(self, timeout: float) -> None:
        self.timeout = timeout
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_FakeSocket.connect`

**Purpose:** Implements `connect` within the file role: Provides complete unit and regression coverage for the `safe_http` contracts exercised in this file.

**Exact signature**

```python
def connect(self, endpoint: tuple[object, ...]) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |
| `endpoint` | positional-or-keyword | `tuple[object, ...]` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `self._connected.append` | `tests.unit.test_safe_http._FakeSocket._connected.append` |

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
| In-memory mutation | `self._endpoint = endpoint`<br>`self._connected.append((self.family, endpoint))` |
| Direct parameter mutation | `self._endpoint = endpoint`<br>`self._connected.append((self.family, endpoint))` |

**Complete source-ordered implementation**

```python
def connect(self, endpoint: tuple[object, ...]) -> None:
        self._endpoint = endpoint
        self._connected.append((self.family, endpoint))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_FakeSocket.getpeername`

**Purpose:** Implements `getpeername` within the file role: Provides complete unit and regression coverage for the `safe_http` contracts exercised in this file.

**Exact signature**

```python
def getpeername(self) -> tuple[object, ...]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[object, ...]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `self._endpoint`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert self._endpoint is not None`

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
def getpeername(self) -> tuple[object, ...]:
        assert self._endpoint is not None
        return self._endpoint
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_FakeSocket.sendall`

**Purpose:** Implements `sendall` within the file role: Provides complete unit and regression coverage for the `safe_http` contracts exercised in this file.

**Exact signature**

```python
def sendall(self, payload: bytes) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |
| `payload` | positional-or-keyword | `bytes` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `self._sent.append` | `tests.unit.test_safe_http._FakeSocket._sent.append` |

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
| In-memory mutation | `self._sent.append(payload)` |
| Direct parameter mutation | `self._sent.append(payload)` |

**Complete source-ordered implementation**

```python
def sendall(self, payload: bytes) -> None:
        self._sent.append(payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_FakeSocket.makefile`

**Purpose:** Implements `makefile` within the file role: Provides complete unit and regression coverage for the `safe_http` contracts exercised in this file.

**Exact signature**

```python
def makefile(self, *args: object, **kwargs: object) -> io.BytesIO:
```

- Exact decorators: none.
- Declared return annotation: `io.BytesIO`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- Exact observed return expressions:
  - `io.BytesIO(self._response_bytes)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `io.BytesIO` | `io.BytesIO` |

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
def makefile(self, *args: object, **kwargs: object) -> io.BytesIO:
        return io.BytesIO(self._response_bytes)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_FakeSocket.setsockopt`

**Purpose:** Implements `setsockopt` within the file role: Provides complete unit and regression coverage for the `safe_http` contracts exercised in this file.

**Exact signature**

```python
def setsockopt(self, *args: object, **kwargs: object) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- Exact observed return expressions:
  - `None`
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
def setsockopt(self, *args: object, **kwargs: object) -> None:
        return None
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_FakeSocket.close`

**Purpose:** Implements `close` within the file role: Provides complete unit and regression coverage for the `safe_http` contracts exercised in this file.

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
| In-memory mutation | `self.closed = True` |
| Direct parameter mutation | `self.closed = True` |

**Complete source-ordered implementation**

```python
def close(self) -> None:
        self.closed = True
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_FakeTlsContext.__init__`

**Purpose:** Implements `init` within the file role: Provides complete unit and regression coverage for the `safe_http` contracts exercised in this file.

**Exact signature**

```python
def __init__(self, server_names: list[str]) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |
| `server_names` | positional-or-keyword | `list[str]` | `required` |

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
| In-memory mutation | `self._server_names = server_names` |
| Direct parameter mutation | `self._server_names = server_names` |

**Complete source-ordered implementation**

```python
def __init__(self, server_names: list[str]) -> None:
        self._server_names = server_names
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_FakeTlsContext.wrap_socket`

**Purpose:** Implements `wrap socket` within the file role: Provides complete unit and regression coverage for the `safe_http` contracts exercised in this file.

**Exact signature**

```python
def wrap_socket(self, sock: _FakeSocket, *, server_hostname: str) -> _FakeSocket:
```

- Exact decorators: none.
- Declared return annotation: `_FakeSocket`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |
| `sock` | positional-or-keyword | `_FakeSocket` | `required` |
| `server_hostname` | keyword-only | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `sock`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `self._server_names.append` | `tests.unit.test_safe_http._FakeTlsContext._server_names.append` |

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
| In-memory mutation | `self._server_names.append(server_hostname)` |
| Direct parameter mutation | `self._server_names.append(server_hostname)` |

**Complete source-ordered implementation**

```python
def wrap_socket(self, sock: _FakeSocket, *, server_hostname: str) -> _FakeSocket:
        self._server_names.append(server_hostname)
        return sock
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_NetworkHarness.__init__`

**Purpose:** Implements `init` within the file role: Provides complete unit and regression coverage for the `safe_http` contracts exercised in this file.

**Exact signature**

```python
def __init__(self, responses: list[bytes]) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |
| `responses` | positional-or-keyword | `list[bytes]` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `list` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `self.responses = list(responses)`<br>`self.connected: list[tuple[int, tuple[object, ...]]] = []`<br>`self.sent: list[bytes] = []`<br>`self.server_names: list[str] = []`<br>`self.contexts: list[_FakeTlsContext] = []`<br>`self.sockets: list[_FakeSocket] = []` |
| Direct parameter mutation | `self.responses = list(responses)`<br>`self.connected: list[tuple[int, tuple[object, ...]]] = []`<br>`self.sent: list[bytes] = []`<br>`self.server_names: list[str] = []`<br>`self.contexts: list[_FakeTlsContext] = []`<br>`self.sockets: list[_FakeSocket] = []` |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_NetworkHarness.socket`

**Purpose:** Implements `socket` within the file role: Provides complete unit and regression coverage for the `safe_http` contracts exercised in this file.

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

- Exact decorators: none.
- Declared return annotation: `_FakeSocket`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |
| `family` | positional-or-keyword | `int` | `socket.AF_INET` |
| `type` | positional-or-keyword | `int` | `socket.SOCK_STREAM` |
| `proto` | positional-or-keyword | `int` | `0` |
| `fileno` | positional-or-keyword | `int \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `result`
- Explicit raise paths:
  - `AssertionError("Unexpected additional socket connection")` under lexical guard `not self.responses`.
- Exact assertions:
  - `assert type == socket.SOCK_STREAM`
  - `assert fileno is None`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `AssertionError` | `unresolved local/third-party receiver; no ownership inferred` |
| `_FakeSocket` | `tests.unit.test_safe_http._FakeSocket` |
| `self.responses.pop` | `tests.unit.test_safe_http._NetworkHarness.responses.pop` |
| `self.sockets.append` | `tests.unit.test_safe_http._NetworkHarness.sockets.append` |

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
| In-memory mutation | `self.responses.pop(0)`<br>`self.sockets.append(result)` |
| Direct parameter mutation | `self.responses.pop(0)`<br>`self.sockets.append(result)` |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_NetworkHarness.context`

**Purpose:** Implements `context` within the file role: Provides complete unit and regression coverage for the `safe_http` contracts exercised in this file.

**Exact signature**

```python
def context(self, *args: object, **kwargs: object) -> _FakeTlsContext:
```

- Exact decorators: none.
- Declared return annotation: `_FakeTlsContext`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- Exact observed return expressions:
  - `context`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_FakeTlsContext` | `tests.unit.test_safe_http._FakeTlsContext` |
| `self.contexts.append` | `tests.unit.test_safe_http._NetworkHarness.contexts.append` |

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
| In-memory mutation | `self.contexts.append(context)` |
| Direct parameter mutation | `self.contexts.append(context)` |

**Complete source-ordered implementation**

```python
def context(self, *args: object, **kwargs: object) -> _FakeTlsContext:
        context = _FakeTlsContext(self.server_names)
        self.contexts.append(context)
        return context
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_install_network`

**Purpose:** Implements `install network` within the file role: Provides complete unit and regression coverage for the `safe_http` contracts exercised in this file.

**Exact signature**

```python
def _install_network(
    monkeypatch: pytest.MonkeyPatch,
    *,
    responses: list[bytes] | None = None,
) -> _NetworkHarness:
```

- Exact decorators: none.
- Declared return annotation: `_NetworkHarness`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |
| `responses` | keyword-only | `list[bytes] \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `harness`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_safe_http::test_cross_origin_redirect_cannot_receive_a_sensitive_header` via `_install_network`
- value/type reference: `tests.unit.test_safe_http::test_cross_origin_redirect_cannot_receive_a_sensitive_header` via `_install_network`
- direct call: `tests.unit.test_safe_http::test_cross_origin_redirect_forwards_only_safe_ordinary_headers` via `_install_network`
- value/type reference: `tests.unit.test_safe_http::test_cross_origin_redirect_forwards_only_safe_ordinary_headers` via `_install_network`
- direct call: `tests.unit.test_safe_http::test_public_dns_answers_are_accepted` via `_install_network`
- value/type reference: `tests.unit.test_safe_http::test_public_dns_answers_are_accepted` via `_install_network`
- direct call: `tests.unit.test_safe_http::test_public_literal_ip_uses_exact_socket_without_dns` via `_install_network`
- value/type reference: `tests.unit.test_safe_http::test_public_literal_ip_uses_exact_socket_without_dns` via `_install_network`
- direct call: `tests.unit.test_safe_http::test_explicit_https_port_is_resolved_and_connected_exactly` via `_install_network`
- value/type reference: `tests.unit.test_safe_http::test_explicit_https_port_is_resolved_and_connected_exactly` via `_install_network`
- direct call: `tests.unit.test_safe_http::test_safe_https_redirect_is_manually_revalidated` via `_install_network`
- value/type reference: `tests.unit.test_safe_http::test_safe_https_redirect_is_manually_revalidated` via `_install_network`
- direct call: `tests.unit.test_safe_http::test_unsafe_redirect_is_rejected_before_target_socket` via `_install_network`
- value/type reference: `tests.unit.test_safe_http::test_unsafe_redirect_is_rejected_before_target_socket` via `_install_network`
- direct call: `tests.unit.test_safe_http::test_redirect_loop_is_rejected` via `_install_network`
- value/type reference: `tests.unit.test_safe_http::test_redirect_loop_is_rejected` via `_install_network`
- direct call: `tests.unit.test_safe_http::test_redirect_limit_is_enforced` via `_install_network`
- value/type reference: `tests.unit.test_safe_http::test_redirect_limit_is_enforced` via `_install_network`
- direct call: `tests.unit.test_safe_http::test_validated_dns_snapshot_binds_actual_socket_and_preserves_tls_host` via `_install_network`
- value/type reference: `tests.unit.test_safe_http::test_validated_dns_snapshot_binds_actual_socket_and_preserves_tls_host` via `_install_network`
- direct call: `tests.unit.test_safe_http::test_environment_proxy_does_not_change_bound_destination` via `_install_network`
- value/type reference: `tests.unit.test_safe_http::test_environment_proxy_does_not_change_bound_destination` via `_install_network`
- direct call: `tests.unit.test_safe_http::test_tls_context_keeps_hostname_verification_enabled` via `_install_network`
- value/type reference: `tests.unit.test_safe_http::test_tls_context_keeps_hostname_verification_enabled` via `_install_network`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_NetworkHarness` | `tests.unit.test_safe_http._NetworkHarness` |
| `_http_response` | `tests.unit.test_safe_http._http_response` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_install_dns`

**Purpose:** Implements `install dns` within the file role: Provides complete unit and regression coverage for the `safe_http` contracts exercised in this file.

**Exact signature**

```python
def _install_dns(
    monkeypatch: pytest.MonkeyPatch,
    addresses: tuple[str, ...],
) -> list[tuple[str, int]]:
```

- Exact decorators: none.
- Declared return annotation: `list[tuple[str, int]]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |
| `addresses` | positional-or-keyword | `tuple[str, ...]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `calls`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_safe_http::test_cross_origin_redirect_forwards_only_safe_ordinary_headers` via `_install_dns`
- value/type reference: `tests.unit.test_safe_http::test_cross_origin_redirect_forwards_only_safe_ordinary_headers` via `_install_dns`
- direct call: `tests.unit.test_safe_http::test_public_dns_answers_are_accepted` via `_install_dns`
- value/type reference: `tests.unit.test_safe_http::test_public_dns_answers_are_accepted` via `_install_dns`
- direct call: `tests.unit.test_safe_http::test_any_nonpublic_dns_answer_fails_before_socket` via `_install_dns`
- value/type reference: `tests.unit.test_safe_http::test_any_nonpublic_dns_answer_fails_before_socket` via `_install_dns`
- direct call: `tests.unit.test_safe_http::test_mixed_public_private_dns_answer_fails_closed` via `_install_dns`
- value/type reference: `tests.unit.test_safe_http::test_mixed_public_private_dns_answer_fails_closed` via `_install_dns`
- direct call: `tests.unit.test_safe_http::test_explicit_https_port_is_resolved_and_connected_exactly` via `_install_dns`
- value/type reference: `tests.unit.test_safe_http::test_explicit_https_port_is_resolved_and_connected_exactly` via `_install_dns`
- direct call: `tests.unit.test_safe_http::test_safe_https_redirect_is_manually_revalidated` via `_install_dns`
- value/type reference: `tests.unit.test_safe_http::test_safe_https_redirect_is_manually_revalidated` via `_install_dns`
- direct call: `tests.unit.test_safe_http::test_redirect_loop_is_rejected` via `_install_dns`
- value/type reference: `tests.unit.test_safe_http::test_redirect_loop_is_rejected` via `_install_dns`
- direct call: `tests.unit.test_safe_http::test_redirect_limit_is_enforced` via `_install_dns`
- value/type reference: `tests.unit.test_safe_http::test_redirect_limit_is_enforced` via `_install_dns`
- direct call: `tests.unit.test_safe_http::test_environment_proxy_does_not_change_bound_destination` via `_install_dns`
- value/type reference: `tests.unit.test_safe_http::test_environment_proxy_does_not_change_bound_destination` via `_install_dns`
- direct call: `tests.unit.test_safe_http::test_tls_context_keeps_hostname_verification_enabled` via `_install_dns`
- value/type reference: `tests.unit.test_safe_http::test_tls_context_keeps_hostname_verification_enabled` via `_install_dns`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_install_dns.resolve`

**Purpose:** Implements `resolve` within the file role: Provides complete unit and regression coverage for the `safe_http` contracts exercised in this file.

**Exact signature**

```python
def resolve(hostname: str, port: int, **kwargs: object) -> list[tuple[Any, ...]]:
```

- Exact decorators: none.
- Declared return annotation: `list[tuple[Any, ...]]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `hostname` | positional-or-keyword | `str` | `required` |
| `port` | positional-or-keyword | `int` | `required` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- Exact observed return expressions:
  - `_dns_records(addresses, port)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert kwargs == {"type": socket.SOCK_STREAM}`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `calls.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `_dns_records` | `tests.unit.test_safe_http._dns_records` |

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
| In-memory mutation | `calls.append((hostname, port))` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def resolve(hostname: str, port: int, **kwargs: object) -> list[tuple[Any, ...]]:
        assert kwargs == {"type": socket.SOCK_STREAM}
        calls.append((hostname, port))
        return _dns_records(addresses, port)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_read`

**Purpose:** Implements `read` within the file role: Provides complete unit and regression coverage for the `safe_http` contracts exercised in this file.

**Exact signature**

```python
def _read(url: str = "https://source.example/archive.zip") -> bytes:
```

- Exact decorators: none.
- Declared return annotation: `bytes`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `url` | positional-or-keyword | `str` | `'https://source.example/archive.zip'` |

**Return and exception contract**

- Exact observed return expressions:
  - `response.read()`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_safe_http::test_public_dns_answers_are_accepted` via `_read`
- value/type reference: `tests.unit.test_safe_http::test_public_dns_answers_are_accepted` via `_read`
- direct call: `tests.unit.test_safe_http::test_malformed_or_unusable_dns_results_fail_before_socket` via `_read`
- value/type reference: `tests.unit.test_safe_http::test_malformed_or_unusable_dns_results_fail_before_socket` via `_read`
- direct call: `tests.unit.test_safe_http::test_any_nonpublic_dns_answer_fails_before_socket` via `_read`
- value/type reference: `tests.unit.test_safe_http::test_any_nonpublic_dns_answer_fails_before_socket` via `_read`
- direct call: `tests.unit.test_safe_http::test_mixed_public_private_dns_answer_fails_closed` via `_read`
- value/type reference: `tests.unit.test_safe_http::test_mixed_public_private_dns_answer_fails_closed` via `_read`
- direct call: `tests.unit.test_safe_http::test_dns_errors_are_controlled_before_socket` via `_read`
- value/type reference: `tests.unit.test_safe_http::test_dns_errors_are_controlled_before_socket` via `_read`
- direct call: `tests.unit.test_safe_http::test_unsafe_url_identity_fails_before_dns` via `_read`
- value/type reference: `tests.unit.test_safe_http::test_unsafe_url_identity_fails_before_dns` via `_read`
- direct call: `tests.unit.test_safe_http::test_literal_and_malformed_numeric_ip_rejection_never_uses_dns` via `_read`
- value/type reference: `tests.unit.test_safe_http::test_literal_and_malformed_numeric_ip_rejection_never_uses_dns` via `_read`
- direct call: `tests.unit.test_safe_http::test_public_literal_ip_uses_exact_socket_without_dns` via `_read`
- value/type reference: `tests.unit.test_safe_http::test_public_literal_ip_uses_exact_socket_without_dns` via `_read`
- direct call: `tests.unit.test_safe_http::test_explicit_https_port_is_resolved_and_connected_exactly` via `_read`
- value/type reference: `tests.unit.test_safe_http::test_explicit_https_port_is_resolved_and_connected_exactly` via `_read`
- direct call: `tests.unit.test_safe_http::test_unsafe_redirect_is_rejected_before_target_socket` via `_read`
- value/type reference: `tests.unit.test_safe_http::test_unsafe_redirect_is_rejected_before_target_socket` via `_read`
- direct call: `tests.unit.test_safe_http::test_redirect_loop_is_rejected` via `_read`
- value/type reference: `tests.unit.test_safe_http::test_redirect_loop_is_rejected` via `_read`
- direct call: `tests.unit.test_safe_http::test_redirect_limit_is_enforced` via `_read`
- value/type reference: `tests.unit.test_safe_http::test_redirect_limit_is_enforced` via `_read`
- direct call: `tests.unit.test_safe_http::test_validated_dns_snapshot_binds_actual_socket_and_preserves_tls_host` via `_read`
- value/type reference: `tests.unit.test_safe_http::test_validated_dns_snapshot_binds_actual_socket_and_preserves_tls_host` via `_read`
- direct call: `tests.unit.test_safe_http::test_environment_proxy_does_not_change_bound_destination` via `_read`
- value/type reference: `tests.unit.test_safe_http::test_environment_proxy_does_not_change_bound_destination` via `_read`
- direct call: `tests.unit.test_safe_http::test_tls_context_keeps_hostname_verification_enabled` via `_read`
- value/type reference: `tests.unit.test_safe_http::test_tls_context_keeps_hostname_verification_enabled` via `_read`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `open_safe_https` | `landscout.common.safe_http.open_safe_https` |
| `response.read` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | `open_safe_https` |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _read(url: str = "https://source.example/archive.zip") -> bytes:
    with open_safe_https(url, timeout=12.5) as response:
        return response.read()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_sensitive_and_hop_by_hop_headers_fail_before_dns`

**Purpose:** Regression invariant: sensitive and hop by hop headers fail before dns. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_sensitive_and_hop_by_hop_headers_fail_before_dns(
    monkeypatch: pytest.MonkeyPatch,
    header_name: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
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
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |
| `header_name` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(SafeHttpsError, match="header\|forbidden\|owned")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `open_safe_https` | `landscout.common.safe_http.open_safe_https` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | `open_safe_https` |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_case_insensitive_duplicate_header_names_fail_before_dns`

**Purpose:** Regression invariant: case insensitive duplicate header names fail before dns. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_case_insensitive_duplicate_header_names_fail_before_dns(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(SafeHttpsError, match="duplicate\|ambiguous")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `open_safe_https` | `landscout.common.safe_http.open_safe_https` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | `open_safe_https` |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_request_and_explicit_headers_cannot_ambiguously_override_each_other`

**Purpose:** Regression invariant: request and explicit headers cannot ambiguously override each other. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_request_and_explicit_headers_cannot_ambiguously_override_each_other(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(SafeHttpsError, match="duplicate\|ambiguous")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `Request` | `urllib.request.Request` |
| `pytest.raises` | `pytest.raises` |
| `open_safe_https` | `landscout.common.safe_http.open_safe_https` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | `open_safe_https` |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_cross_origin_redirect_cannot_receive_a_sensitive_header`

**Purpose:** Regression invariant: cross origin redirect cannot receive a sensitive header. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_cross_origin_redirect_cannot_receive_a_sensitive_header(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(SafeHttpsError, match="header\|forbidden")`
- Exact assertions:
  - `assert harness.sent == []`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `_install_network` | `tests.unit.test_safe_http._install_network` |
| `_http_response` | `tests.unit.test_safe_http._http_response` |
| `pytest.raises` | `pytest.raises` |
| `open_safe_https` | `landscout.common.safe_http.open_safe_https` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | `open_safe_https` |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_cross_origin_redirect_forwards_only_safe_ordinary_headers`

**Purpose:** Regression invariant: cross origin redirect forwards only safe ordinary headers. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_cross_origin_redirect_forwards_only_safe_ordinary_headers(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert response.read() == b"archive"`
  - `assert len(harness.sent) == 2`
  - `assert b"User-Agent: LandScout-Test" in request`
  - `assert b"Accept: application/zip" in request`
  - `assert b"Authorization:" not in request`
  - `assert b"Cookie:" not in request`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_install_dns` | `tests.unit.test_safe_http._install_dns` |
| `_install_network` | `tests.unit.test_safe_http._install_network` |
| `_http_response` | `tests.unit.test_safe_http._http_response` |
| `open_safe_https` | `landscout.common.safe_http.open_safe_https` |
| `response.read` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | `open_safe_https` |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_public_dns_answers_are_accepted`

**Purpose:** Regression invariant: public dns answers are accepted. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_public_dns_answers_are_accepted(
    monkeypatch: pytest.MonkeyPatch,
    addresses: tuple[str, ...],
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "addresses",
    [
        (PUBLIC_IPV4,),
        (PUBLIC_IPV4, PUBLIC_IPV6),
        (PUBLIC_IPV4, PUBLIC_IPV4),
    ],
    ids=["public-ipv4", "public-ipv4-and-ipv6", "duplicate-public"],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |
| `addresses` | positional-or-keyword | `tuple[str, ...]` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert _read() == b"ok"`
  - `assert calls == [("source.example", 443)]`
  - `assert harness.connected`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_install_dns` | `tests.unit.test_safe_http._install_dns` |
| `_install_network` | `tests.unit.test_safe_http._install_network` |
| `_read` | `tests.unit.test_safe_http._read` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_malformed_or_unusable_dns_results_fail_before_socket`

**Purpose:** Regression invariant: malformed or unusable dns results fail before socket. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_malformed_or_unusable_dns_results_fail_before_socket(
    monkeypatch: pytest.MonkeyPatch,
    records: list[tuple[Any, ...]],
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
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
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |
| `records` | positional-or-keyword | `list[tuple[Any, ...]]` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(SafeHttpsError, match="DNS\|address")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_read` | `tests.unit.test_safe_http._read` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `object` | `unresolved local/third-party receiver; no ownership inferred` |

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
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_any_nonpublic_dns_answer_fails_before_socket`

**Purpose:** Regression invariant: any nonpublic dns answer fails before socket. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_any_nonpublic_dns_answer_fails_before_socket(
    monkeypatch: pytest.MonkeyPatch,
    address: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
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
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |
| `address` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(SafeHttpsError, match="public\|global\|address\|DNS")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_install_dns` | `tests.unit.test_safe_http._install_dns` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_read` | `tests.unit.test_safe_http._read` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_mixed_public_private_dns_answer_fails_closed`

**Purpose:** Regression invariant: mixed public private dns answer fails closed. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_mixed_public_private_dns_answer_fails_closed(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(SafeHttpsError, match="public\|global\|address\|DNS")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_install_dns` | `tests.unit.test_safe_http._install_dns` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_read` | `tests.unit.test_safe_http._read` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_dns_errors_are_controlled_before_socket`

**Purpose:** Regression invariant: dns errors are controlled before socket. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_dns_errors_are_controlled_before_socket(
    monkeypatch: pytest.MonkeyPatch,
    error: Exception,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "error",
    [
        socket.gaierror("DNS failed"),
        OSError("resolver failed"),
        UnicodeError("bad hostname"),
    ],
    ids=["gaierror", "oserror", "unicode-error"],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |
| `error` | positional-or-keyword | `Exception` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(SafeHttpsError, match="DNS\|resolve")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_read` | `tests.unit.test_safe_http._read` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `socket.gaierror` | `socket.gaierror` |
| `OSError` | `unresolved local/third-party receiver; no ownership inferred` |
| `UnicodeError` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | `socket.gaierror` |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_dns_errors_are_controlled_before_socket.fail`

**Purpose:** Implements `fail` within the file role: Provides complete unit and regression coverage for the `safe_http` contracts exercised in this file.

**Exact signature**

```python
def fail(*args: object, **kwargs: object) -> list[tuple[Any, ...]]:
```

- Exact decorators: none.
- Declared return annotation: `list[tuple[Any, ...]]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `error`.

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
def fail(*args: object, **kwargs: object) -> list[tuple[Any, ...]]:
        raise error
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unsafe_url_identity_fails_before_dns`

**Purpose:** Regression invariant: unsafe url identity fails before dns. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_unsafe_url_identity_fails_before_dns(
    monkeypatch: pytest.MonkeyPatch,
    url: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
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
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |
| `url` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(SafeHttpsError, match="HTTPS\|credential\|localhost\|host\|URL")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_read` | `tests.unit.test_safe_http._read` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_literal_and_malformed_numeric_ip_rejection_never_uses_dns`

**Purpose:** Regression invariant: literal and malformed numeric ip rejection never uses dns. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_literal_and_malformed_numeric_ip_rejection_never_uses_dns(
    monkeypatch: pytest.MonkeyPatch,
    url: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
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
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |
| `url` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(SafeHttpsError, match="public\|global\|address\|IP\|URL")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_read` | `tests.unit.test_safe_http._read` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_public_literal_ip_uses_exact_socket_without_dns`

**Purpose:** Regression invariant: public literal ip uses exact socket without dns. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_public_literal_ip_uses_exact_socket_without_dns(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert _read(f"https://{PUBLIC_IPV4}/archive.zip") == b"ok"`
  - `assert harness.connected == [(socket.AF_INET, (PUBLIC_IPV4, 443))]`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `_install_network` | `tests.unit.test_safe_http._install_network` |
| `_read` | `tests.unit.test_safe_http._read` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_explicit_https_port_is_resolved_and_connected_exactly`

**Purpose:** Regression invariant: explicit https port is resolved and connected exactly. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_explicit_https_port_is_resolved_and_connected_exactly(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert _read("https://source.example:8443/archive.zip") == b"ok"`
  - `assert calls == [("source.example", 8443)]`
  - `assert harness.connected == [(socket.AF_INET, (PUBLIC_IPV4, 8443))]`
  - `assert harness.server_names == ["source.example"]`
  - `assert b"\r\nHost: source.example:8443\r\n" in b"".join(harness.sent)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_install_dns` | `tests.unit.test_safe_http._install_dns` |
| `_install_network` | `tests.unit.test_safe_http._install_network` |
| `_read` | `tests.unit.test_safe_http._read` |
| `b"".join` | `unresolved local/third-party receiver; no ownership inferred` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_safe_https_redirect_is_manually_revalidated`

**Purpose:** Regression invariant: safe https redirect is manually revalidated. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_safe_https_redirect_is_manually_revalidated(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert response.read() == b"archive"`
  - `assert response.url == "https://cdn.example/file"`
  - `assert response.history == ("https://source.example/archive.zip",)`
  - `assert calls == [("source.example", 443), ("cdn.example", 443)]`
  - `assert [endpoint for _, endpoint in harness.connected] == [<br>        (PUBLIC_IPV4, 443),<br>        (PUBLIC_IPV4, 443),<br>    ]`
  - `assert harness.server_names == ["source.example", "cdn.example"]`
  - `assert b"\r\nHost: source.example\r\n" in harness.sent[0]`
  - `assert b"\r\nHost: cdn.example\r\n" in harness.sent[1]`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_install_dns` | `tests.unit.test_safe_http._install_dns` |
| `_install_network` | `tests.unit.test_safe_http._install_network` |
| `_http_response` | `tests.unit.test_safe_http._http_response` |
| `open_safe_https` | `landscout.common.safe_http.open_safe_https` |
| `response.read` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | `open_safe_https` |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unsafe_redirect_is_rejected_before_target_socket`

**Purpose:** Regression invariant: unsafe redirect is rejected before target socket. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_unsafe_redirect_is_rejected_before_target_socket(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(SafeHttpsError, match="public\|global\|address\|DNS")`
- Exact assertions:
  - `assert harness.connected == [(socket.AF_INET, (PUBLIC_IPV4, 443))]`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `_install_network` | `tests.unit.test_safe_http._install_network` |
| `_http_response` | `tests.unit.test_safe_http._http_response` |
| `pytest.raises` | `pytest.raises` |
| `_read` | `tests.unit.test_safe_http._read` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unsafe_redirect_is_rejected_before_target_socket.resolve`

**Purpose:** Implements `resolve` within the file role: Provides complete unit and regression coverage for the `safe_http` contracts exercised in this file.

**Exact signature**

```python
def resolve(hostname: str, port: int, **kwargs: object) -> list[tuple[Any, ...]]:
```

- Exact decorators: none.
- Declared return annotation: `list[tuple[Any, ...]]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `hostname` | positional-or-keyword | `str` | `required` |
| `port` | positional-or-keyword | `int` | `required` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- Exact observed return expressions:
  - `_dns_records((address,), port)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_dns_records` | `tests.unit.test_safe_http._dns_records` |

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
def resolve(hostname: str, port: int, **kwargs: object) -> list[tuple[Any, ...]]:
        address = PUBLIC_IPV4 if hostname == "source.example" else "127.0.0.1"
        return _dns_records((address,), port)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_redirect_loop_is_rejected`

**Purpose:** Regression invariant: redirect loop is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_redirect_loop_is_rejected(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(SafeHttpsError, match="loop")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_install_dns` | `tests.unit.test_safe_http._install_dns` |
| `_install_network` | `tests.unit.test_safe_http._install_network` |
| `_http_response` | `tests.unit.test_safe_http._http_response` |
| `pytest.raises` | `pytest.raises` |
| `_read` | `tests.unit.test_safe_http._read` |

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
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_redirect_limit_is_enforced`

**Purpose:** Regression invariant: redirect limit is enforced. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_redirect_limit_is_enforced(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(SafeHttpsError, match="redirect")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_install_dns` | `tests.unit.test_safe_http._install_dns` |
| `_http_response` | `tests.unit.test_safe_http._http_response` |
| `range` | `unresolved local/third-party receiver; no ownership inferred` |
| `_install_network` | `tests.unit.test_safe_http._install_network` |
| `pytest.raises` | `pytest.raises` |
| `_read` | `tests.unit.test_safe_http._read` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_validated_dns_snapshot_binds_actual_socket_and_preserves_tls_host`

**Purpose:** Regression invariant: validated dns snapshot binds actual socket and preserves tls host. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_validated_dns_snapshot_binds_actual_socket_and_preserves_tls_host(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert _read("https://rebind.example/archive.zip") == b"ok"`
  - `assert resolutions == 1`
  - `assert harness.connected == [(socket.AF_INET, (PUBLIC_IPV4, 443))]`
  - `assert harness.server_names == ["rebind.example"]`
  - `assert request.startswith("GET /archive.zip HTTP/1.1\r\n")`
  - `assert "\r\nHost: rebind.example\r\n" in request`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `_install_network` | `tests.unit.test_safe_http._install_network` |
| `_read` | `tests.unit.test_safe_http._read` |
| `b"".join(harness.sent).decode` | `unresolved local/third-party receiver; no ownership inferred` |
| `b"".join` | `unresolved local/third-party receiver; no ownership inferred` |
| `request.startswith` | `unresolved local/third-party receiver; no ownership inferred` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_validated_dns_snapshot_binds_actual_socket_and_preserves_tls_host.rebind`

**Purpose:** Implements `rebind` within the file role: Provides complete unit and regression coverage for the `safe_http` contracts exercised in this file.

**Exact signature**

```python
def rebind(hostname: str, port: int, **kwargs: object) -> list[tuple[Any, ...]]:
```

- Exact decorators: none.
- Declared return annotation: `list[tuple[Any, ...]]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `hostname` | positional-or-keyword | `str` | `required` |
| `port` | positional-or-keyword | `int` | `required` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- Exact observed return expressions:
  - `_dns_records((address,), port)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_dns_records` | `tests.unit.test_safe_http._dns_records` |

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
def rebind(hostname: str, port: int, **kwargs: object) -> list[tuple[Any, ...]]:
        nonlocal resolutions
        resolutions += 1
        address = PUBLIC_IPV4 if resolutions == 1 else "127.0.0.1"
        return _dns_records((address,), port)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_environment_proxy_does_not_change_bound_destination`

**Purpose:** Regression invariant: environment proxy does not change bound destination. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_environment_proxy_does_not_change_bound_destination(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert _read() == b"ok"`
  - `assert harness.connected == [(socket.AF_INET, (PUBLIC_IPV4, 443))]`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `monkeypatch.setenv` | `unresolved local/third-party receiver; no ownership inferred` |
| `_install_dns` | `tests.unit.test_safe_http._install_dns` |
| `_install_network` | `tests.unit.test_safe_http._install_network` |
| `_read` | `tests.unit.test_safe_http._read` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_malformed_header_name_is_rejected_before_dns`

**Purpose:** Regression invariant: malformed header name is rejected before dns. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_malformed_header_name_is_rejected_before_dns(
    monkeypatch: pytest.MonkeyPatch,
    header_name: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "header_name",
    ["Host ", "Bad Header"],
    ids=["host-with-trailing-space", "non-token-field-name"],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |
| `header_name` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(SafeHttpsError, match="header\|Host")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `open_safe_https` | `landscout.common.safe_http.open_safe_https` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | `open_safe_https` |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

    with (
        pytest.raises(SafeHttpsError, match="header|Host"),
        open_safe_https(
            "https://source.example/archive.zip",
            timeout=12.5,
            headers={header_name: "attacker.example"},
        ),
    ):
        pass
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_tls_context_keeps_hostname_verification_enabled`

**Purpose:** Regression invariant: tls context keeps hostname verification enabled. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_tls_context_keeps_hostname_verification_enabled(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert _read() == b"ok"`
  - `assert harness.server_names == ["source.example"]`
  - `assert len(harness.contexts) == 1`
  - `assert harness.contexts[0].check_hostname is True`
  - `assert harness.contexts[0].verify_mode == ssl.CERT_REQUIRED`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_install_dns` | `tests.unit.test_safe_http._install_dns` |
| `_install_network` | `tests.unit.test_safe_http._install_network` |
| `_read` | `tests.unit.test_safe_http._read` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.


## 7. Test-specific regression contract

- Test functions: **22**.
- Pytest fixtures (decorator-proven): **0**.

### Per-test regression index

| Test | Parametrization | Expected exception contexts | Assertion count | Exact regression purpose |
|---|---|---|---:|---|
| `test_sensitive_and_hop_by_hop_headers_fail_before_dns` | pytest.mark.parametrize(<br>    "header_name",<br>    [<br>        "Authorization",<br>        "authorization",<br>        "Proxy-Authorization",<br>        "Cookie",<br>        "Cookie2",<br>        "Host",<br>        "Connection",<br>        "Proxy-Connection",<br>        "Keep-Alive",<br>        "Transfer-Encoding",<br>        "TE",<br>        "Trailer",<br>        "Upgrade",<br>    ],<br>) | pytest.raises(SafeHttpsError, match="header\|forbidden\|owned") | 0 | Proves sensitive and hop by hop headers fail before dns using the exact source reproduced in section 7. |
| `test_case_insensitive_duplicate_header_names_fail_before_dns` | none | pytest.raises(SafeHttpsError, match="duplicate\|ambiguous") | 0 | Proves case insensitive duplicate header names fail before dns using the exact source reproduced in section 7. |
| `test_request_and_explicit_headers_cannot_ambiguously_override_each_other` | none | pytest.raises(SafeHttpsError, match="duplicate\|ambiguous") | 0 | Proves request and explicit headers cannot ambiguously override each other using the exact source reproduced in section 7. |
| `test_cross_origin_redirect_cannot_receive_a_sensitive_header` | none | pytest.raises(SafeHttpsError, match="header\|forbidden") | 1 | Proves cross origin redirect cannot receive a sensitive header using the exact source reproduced in section 7. |
| `test_cross_origin_redirect_forwards_only_safe_ordinary_headers` | none | none | 6 | Proves cross origin redirect forwards only safe ordinary headers using the exact source reproduced in section 7. |
| `test_public_dns_answers_are_accepted` | pytest.mark.parametrize(<br>    "addresses",<br>    [<br>        (PUBLIC_IPV4,),<br>        (PUBLIC_IPV4, PUBLIC_IPV6),<br>        (PUBLIC_IPV4, PUBLIC_IPV4),<br>    ],<br>    ids=["public-ipv4", "public-ipv4-and-ipv6", "duplicate-public"],<br>) | none | 3 | Proves public dns answers are accepted using the exact source reproduced in section 7. |
| `test_malformed_or_unusable_dns_results_fail_before_socket` | pytest.mark.parametrize(<br>    "records",<br>    [<br>        [],<br>        [(socket.AF_INET, socket.SOCK_STREAM)],<br>        [(9999, socket.SOCK_STREAM, socket.IPPROTO_TCP, "", (PUBLIC_IPV4, 443))],<br>        [<br>            (<br>                socket.AF_INET,<br>                socket.SOCK_DGRAM,<br>                socket.IPPROTO_UDP,<br>                "",<br>                (PUBLIC_IPV4, 443),<br>            )<br>        ],<br>        [(socket.AF_INET, socket.SOCK_STREAM, object(), "", (PUBLIC_IPV4, 443))],<br>        [(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP, "", (PUBLIC_IPV4,))],<br>        [<br>            (<br>                socket.AF_INET,<br>                socket.SOCK_STREAM,<br>                socket.IPPROTO_TCP,<br>                "",<br>                (PUBLIC_IPV6, 443),<br>            )<br>        ],<br>        [(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP, "", (123, 443))],<br>    ],<br>    ids=[<br>        "zero",<br>        "short-record",<br>        "unsupported-family",<br>        "wrong-socket-type",<br>        "non-integer-protocol",<br>        "bad-sockaddr",<br>        "family-mismatch",<br>        "non-string-address",<br>    ],<br>) | pytest.raises(SafeHttpsError, match="DNS\|address") | 0 | Proves malformed or unusable dns results fail before socket using the exact source reproduced in section 7. |
| `test_any_nonpublic_dns_answer_fails_before_socket` | pytest.mark.parametrize(<br>    "address",<br>    [<br>        "127.0.0.1",<br>        "10.0.0.2",<br>        "169.254.1.1",<br>        "0.0.0.0",<br>        "240.0.0.1",<br>        "224.0.0.1",<br>        "::1",<br>        "fd00::1",<br>        "fe80::1",<br>        "::",<br>        "ff02::1",<br>        "::ffff:127.0.0.1",<br>    ],<br>    ids=[<br>        "ipv4-loopback",<br>        "ipv4-private",<br>        "ipv4-link-local",<br>        "ipv4-unspecified",<br>        "ipv4-reserved",<br>        "ipv4-multicast",<br>        "ipv6-loopback",<br>        "ipv6-private",<br>        "ipv6-link-local",<br>        "ipv6-unspecified",<br>        "ipv6-multicast",<br>        "ipv4-mapped-private",<br>    ],<br>) | pytest.raises(SafeHttpsError, match="public\|global\|address\|DNS") | 0 | Proves any nonpublic dns answer fails before socket using the exact source reproduced in section 7. |
| `test_mixed_public_private_dns_answer_fails_closed` | none | pytest.raises(SafeHttpsError, match="public\|global\|address\|DNS") | 0 | Proves mixed public private dns answer fails closed using the exact source reproduced in section 7. |
| `test_dns_errors_are_controlled_before_socket` | pytest.mark.parametrize(<br>    "error",<br>    [<br>        socket.gaierror("DNS failed"),<br>        OSError("resolver failed"),<br>        UnicodeError("bad hostname"),<br>    ],<br>    ids=["gaierror", "oserror", "unicode-error"],<br>) | pytest.raises(SafeHttpsError, match="DNS\|resolve") | 0 | Proves dns errors are controlled before socket using the exact source reproduced in section 7. |
| `test_unsafe_url_identity_fails_before_dns` | pytest.mark.parametrize(<br>    "url",<br>    [<br>        "http://source.example/archive.zip",<br>        "https://user:secret@source.example/archive.zip",<br>        "https://localhost/archive.zip",<br>        "https://api.localhost/archive.zip",<br>        "https://localhost\u3002/archive.zip",<br>        "https://api.localhost\uff0e/archive.zip",<br>        "https://api.localhost\uff61/archive.zip",<br>        "https:///archive.zip",<br>    ],<br>    ids=[<br>        "http",<br>        "credentials",<br>        "localhost",<br>        "localhost-subdomain",<br>        "localhost-ideographic-trailing-dot",<br>        "localhost-subdomain-fullwidth-trailing-dot",<br>        "localhost-subdomain-halfwidth-trailing-dot",<br>        "missing-host",<br>    ],<br>) | pytest.raises(SafeHttpsError, match="HTTPS\|credential\|localhost\|host\|URL") | 0 | Proves unsafe url identity fails before dns using the exact source reproduced in section 7. |
| `test_literal_and_malformed_numeric_ip_rejection_never_uses_dns` | pytest.mark.parametrize(<br>    "url",<br>    [<br>        "https://127.0.0.1/archive.zip",<br>        "https://127.1/archive.zip",<br>        "https://0177.0.0.1/archive.zip",<br>        "https://10.0.0.2/archive.zip",<br>        "https://2130706433/archive.zip",<br>        "https://0x7f000001/archive.zip",<br>        "https://[::1]/archive.zip",<br>        "https://[fd00::1]/archive.zip",<br>        "https://[fe80::1]/archive.zip",<br>        "https://999999999999999999999/archive.zip",<br>        "https://0xnotanaddress/archive.zip",<br>    ],<br>) | pytest.raises(SafeHttpsError, match="public\|global\|address\|IP\|URL") | 0 | Proves literal and malformed numeric ip rejection never uses dns using the exact source reproduced in section 7. |
| `test_public_literal_ip_uses_exact_socket_without_dns` | none | none | 2 | Proves public literal ip uses exact socket without dns using the exact source reproduced in section 7. |
| `test_explicit_https_port_is_resolved_and_connected_exactly` | none | none | 5 | Proves explicit https port is resolved and connected exactly using the exact source reproduced in section 7. |
| `test_safe_https_redirect_is_manually_revalidated` | none | none | 8 | Proves safe https redirect is manually revalidated using the exact source reproduced in section 7. |
| `test_unsafe_redirect_is_rejected_before_target_socket` | none | pytest.raises(SafeHttpsError, match="public\|global\|address\|DNS") | 1 | Proves unsafe redirect is rejected before target socket using the exact source reproduced in section 7. |
| `test_redirect_loop_is_rejected` | none | pytest.raises(SafeHttpsError, match="loop") | 0 | Proves redirect loop is rejected using the exact source reproduced in section 7. |
| `test_redirect_limit_is_enforced` | none | pytest.raises(SafeHttpsError, match="redirect") | 0 | Proves redirect limit is enforced using the exact source reproduced in section 7. |
| `test_validated_dns_snapshot_binds_actual_socket_and_preserves_tls_host` | none | none | 6 | Proves validated dns snapshot binds actual socket and preserves tls host using the exact source reproduced in section 7. |
| `test_environment_proxy_does_not_change_bound_destination` | none | none | 2 | Proves environment proxy does not change bound destination using the exact source reproduced in section 7. |
| `test_malformed_header_name_is_rejected_before_dns` | pytest.mark.parametrize(<br>    "header_name",<br>    ["Host ", "Bad Header"],<br>    ids=["host-with-trailing-space", "non-token-field-name"],<br>) | pytest.raises(SafeHttpsError, match="header\|Host") | 0 | Proves malformed header name is rejected before dns using the exact source reproduced in section 7. |
| `test_tls_context_keeps_hostname_verification_enabled` | none | none | 5 | Proves tls context keeps hostname verification enabled using the exact source reproduced in section 7. |

## 8. Public exports and package ownership

This module declares no `__all__`; no package-level public guarantee is inferred from direct importability alone.

## 9. Trust, provenance, side effects, and business boundary

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.
- Configured identity, textual lineage, byte identity, physical source reconstruction, local envelope validation, and source-complete validation remain distinct trust levels. This companion attributes only the levels implemented in the exact source.
- Filesystem, network, hashing, CRS/geometry, process, mutation, and expected-exception evidence is listed per callable; an empty category is not silently promoted to an effect.

## 10. Change impact

A source-byte change invalidates the SHA above and requires re-auditing imports/re-exports, constants/aliases/schemas, model fields/immutability, qualified callers, side effects, controlled errors, tests, source/artifact locks, and the exact full snapshot.

## 11. Exact complete current file content

The following UTF-8 snapshot is the complete current repository file, not an excerpt. Its raw-byte SHA256 is the value in **File identity**.

```python
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
```

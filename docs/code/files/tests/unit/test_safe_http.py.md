# `tests/unit/test_safe_http.py`

## File identity

- Repository path: `tests/unit/test_safe_http.py`
- File type: Python test
- Primary responsibility: Provides complete unit and regression coverage for the `safe_http` contracts exercised in this file.
- Layer / domain: `unit/regression test` / `test`
- Public or internal role: Internal test support; not a production API.
- Source SHA256: `90db8d4bcb2e56bb66c2f7a58817fbd49564af39d42777e2cddde008f425ac64`

## 1. Purpose

Provides complete unit and regression coverage for the `safe_http` contracts exercised in this file.

## 2. Position in LandScout architecture

This file is a `unit/regression test` artifact in the `test` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from __future__ import annotations` — required by the implementation paths and symbols documented below.
- `import io` — required by the implementation paths and symbols documented below.
- `import socket` — required by the implementation paths and symbols documented below.
- `import ssl` — required by the implementation paths and symbols documented below.
- `from typing import Any` — required by the implementation paths and symbols documented below.

### Third-party

- `import pytest` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout.common import safe_http` — required by the implementation paths and symbols documented below.
- `from landscout.common.safe_http import SafeHttpsError, open_safe_https` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `PUBLIC_IPV4` | `"93.184.216.34"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `PUBLIC_IPV6` | `"2606:4700:4700::1111"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

### `_FakeSocket`

**Purpose:** Groups the `FakeSocket` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `object`.

**Model form and mutability:** class inheriting from `object`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `family` | `not explicitly annotated` | `assigned in `__init__` from `family`` | Socket address family (`AF_INET` or `AF_INET6`) selected from a validated resolver record. |
| `_response_bytes` | `not explicitly annotated` | `assigned in `__init__` from `response_bytes`` | `not explicitly annotated` state used by `tests/unit/test_safe_http.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `_connected` | `not explicitly annotated` | `assigned in `__init__` from `connected`` | `not explicitly annotated` state used by `tests/unit/test_safe_http.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `_sent` | `not explicitly annotated` | `assigned in `__init__` from `sent`` | `not explicitly annotated` state used by `tests/unit/test_safe_http.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `_endpoint` | `tuple[object, ...] | None` | `assigned in `__init__` from `None`` | `tuple[object, ...] | None` state used by `tests/unit/test_safe_http.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `closed` | `not explicitly annotated` | `assigned in `__init__` from `False`` | `not explicitly annotated` state used by `tests/unit/test_safe_http.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `timeout` | `float | None` | `assigned in `__init__` from `None`` | `float | None` state used by `tests/unit/test_safe_http.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- `__init__` — `def __init__(         self,         family: int,         response_bytes: bytes,         connected: list[tuple[int, tuple[object, ...]]],         sent: list[bytes],     ) -> None:`; decorators `none`. The complete method algorithm appears in the function/method section.
- `settimeout` — `def settimeout(self, timeout: float) -> None:`; decorators `none`. The complete method algorithm appears in the function/method section.
- `connect` — `def connect(self, endpoint: tuple[object, ...]) -> None:`; decorators `none`. The complete method algorithm appears in the function/method section.
- `getpeername` — `def getpeername(self) -> tuple[object, ...]:`; decorators `none`. The complete method algorithm appears in the function/method section.
- `sendall` — `def sendall(self, payload: bytes) -> None:`; decorators `none`. The complete method algorithm appears in the function/method section.
- `makefile` — `def makefile(self, *args: object, **kwargs: object) -> io.BytesIO:`; decorators `none`. The complete method algorithm appears in the function/method section.
- `setsockopt` — `def setsockopt(self, *args: object, **kwargs: object) -> None:`; decorators `none`. The complete method algorithm appears in the function/method section.
- `close` — `def close(self) -> None:`; decorators `none`. The complete method algorithm appears in the function/method section.

### `_FakeTlsContext`

**Purpose:** Groups the `FakeTlsContext` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `object`.

**Model form and mutability:** class inheriting from `object`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `_server_names` | `not explicitly annotated` | `assigned in `__init__` from `server_names`` | `not explicitly annotated` state used by `tests/unit/test_safe_http.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- `__init__` — `def __init__(self, server_names: list[str]) -> None:`; decorators `none`. The complete method algorithm appears in the function/method section.
- `wrap_socket` — `def wrap_socket(self, sock: _FakeSocket, *, server_hostname: str) -> _FakeSocket:`; decorators `none`. The complete method algorithm appears in the function/method section.

### `_NetworkHarness`

**Purpose:** Groups the `NetworkHarness` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `object`.

**Model form and mutability:** class inheriting from `object`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `responses` | `not explicitly annotated` | `assigned in `__init__` from `list(responses)`` | `not explicitly annotated` state used by `tests/unit/test_safe_http.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `connected` | `list[tuple[int, tuple[object, ...]]]` | `assigned in `__init__` from `[]`` | `list[tuple[int, tuple[object, ...]]]` state used by `tests/unit/test_safe_http.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `sent` | `list[bytes]` | `assigned in `__init__` from `[]`` | `list[bytes]` state used by `tests/unit/test_safe_http.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `server_names` | `list[str]` | `assigned in `__init__` from `[]`` | `list[str]` state used by `tests/unit/test_safe_http.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `contexts` | `list[_FakeTlsContext]` | `assigned in `__init__` from `[]`` | `list[_FakeTlsContext]` state used by `tests/unit/test_safe_http.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `sockets` | `list[_FakeSocket]` | `assigned in `__init__` from `[]`` | `list[_FakeSocket]` state used by `tests/unit/test_safe_http.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- `__init__` — `def __init__(self, responses: list[bytes]) -> None:`; decorators `none`. The complete method algorithm appears in the function/method section.
- `socket` — `def socket(         self,         family: int = socket.AF_INET,         type: int = socket.SOCK_STREAM,         proto: int = 0,         fileno: int | None = None,     ) -> _FakeSocket:`; decorators `none`. The complete method algorithm appears in the function/method section.
- `context` — `def context(self, *args: object, **kwargs: object) -> _FakeTlsContext:`; decorators `none`. The complete method algorithm appears in the function/method section.

## 6. Functions and methods

### `_http_response`

**Signature**

```python
def _http_response(
    status: int = 200,
    *,
    body: bytes = b"ok",
    headers: dict[str, str] | None = None,
) -> bytes:
```

**Purpose**

Implements http response according to the exact implementation and guards in this file.

**Inputs**

- `status` (`int`; optional/default `200`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `body` (`bytes`; optional/default `b'ok'`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `headers` (`dict[str, str] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bytes`. Observed return expression(s): `f'HTTP/1.1 {status} {reason}\r\n{header_bytes}\r\n'.encode() + body`.

**Algorithm**

1. Computes `reason` from `{200: 'OK', 301: 'Moved Permanently', 302: 'Found', 303: 'See Other', 307: 'Temporary Redirect', 308: 'Permanent Redirect'}.get(status, 'Response')`.
2. Computes `values` from `{'Content-Length': str(len(body)), **(headers or {})}`.
3. Computes `header_bytes` from `''.join((f'{name}: {value}\r\n' for name, value in values.items()))`.
4. Returns `f'HTTP/1.1 {status} {reason}\r\n{header_bytes}\r\n'.encode() + body`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `''.join`, `f'HTTP/1.1 {status} {reason}\r\n{header_bytes}\r\n'.encode`, `len`, `str`, `values.items`, `{200: 'OK', 301: 'Moved Permanently', 302: 'Found', 303: 'See Other', 307: 'Temporary Redirect', 308: 'Permanent Redirect'}.get`.

**Known repository callers**

- `tests/unit/test_safe_http.py` — `_install_network`
- `tests/unit/test_safe_http.py` — `test_redirect_limit_is_enforced`
- `tests/unit/test_safe_http.py` — `test_redirect_loop_is_rejected`
- `tests/unit/test_safe_http.py` — `test_safe_https_redirect_is_manually_revalidated`
- `tests/unit/test_safe_http.py` — `test_unsafe_redirect_is_rejected_before_target_socket`

**Tests**

- `tests/unit/test_safe_http.py::test_redirect_limit_is_enforced`
- `tests/unit/test_safe_http.py::test_redirect_loop_is_rejected`
- `tests/unit/test_safe_http.py::test_safe_https_redirect_is_manually_revalidated`
- `tests/unit/test_safe_http.py::test_unsafe_redirect_is_rejected_before_target_socket`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_dns_records`

**Signature**

```python
def _dns_records(
    addresses: tuple[str, ...],
    port: int,
) -> list[tuple[int, int, int, str, tuple[object, ...]]]:
```

**Purpose**

Implements dns records according to the exact implementation and guards in this file.

**Inputs**

- `addresses` (`tuple[str, ...]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `port` (`int`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `list[tuple[int, int, int, str, tuple[object, ...]]]`. Observed return expression(s): `result`.

**Algorithm**

1. Defines `result` with annotation `list[tuple[int, int, int, str, tuple[object, ...]]]` from `[]`.
2. Iterates `address` over `addresses`. For each value: Checks `':' in address`. When true: Calls `result.append((socket.AF_INET6, socket.SOCK_STREAM, socket.IPPROTO_TCP, '', (address, port, 0, 0)))` for its validation or side effect. Otherwise: Calls `result.append((socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP, '', (address, port)))` for its validation or side effect.
3. Returns `result`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `result.append`.

**Known repository callers**

- `tests/unit/test_safe_http.py` — `_install_dns.resolve`
- `tests/unit/test_safe_http.py` — `_install_dns`
- `tests/unit/test_safe_http.py` — `test_unsafe_redirect_is_rejected_before_target_socket.resolve`
- `tests/unit/test_safe_http.py` — `test_unsafe_redirect_is_rejected_before_target_socket`
- `tests/unit/test_safe_http.py` — `test_validated_dns_snapshot_binds_actual_socket_and_preserves_tls_host.rebind`
- `tests/unit/test_safe_http.py` — `test_validated_dns_snapshot_binds_actual_socket_and_preserves_tls_host`

**Tests**

- `tests/unit/test_safe_http.py::test_unsafe_redirect_is_rejected_before_target_socket`
- `tests/unit/test_safe_http.py::test_validated_dns_snapshot_binds_actual_socket_and_preserves_tls_host`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_FakeSocket.__init__`

**Signature**

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

Implements init according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `family` (`int`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `response_bytes` (`bytes`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `connected` (`list[tuple[int, tuple[object, ...]]]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `sent` (`list[bytes]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `self.family` from `family`.
2. Computes `self._response_bytes` from `response_bytes`.
3. Computes `self._connected` from `connected`.
4. Computes `self._sent` from `sent`.
5. Defines `self._endpoint` with annotation `tuple[object, ...] | None` from `None`.
6. Computes `self.closed` from `False`.
7. Defines `self.timeout` with annotation `float | None` from `None`.

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

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_FakeSocket.settimeout`

**Signature**

```python
def settimeout(self, timeout: float) -> None:
```

**Purpose**

Implements settimeout according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `timeout` (`float`; required) — network timeout in seconds; validation rejects unsupported or non-positive values. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `self.timeout` from `timeout`.

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

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_FakeSocket.connect`

**Signature**

```python
def connect(self, endpoint: tuple[object, ...]) -> None:
```

**Purpose**

Implements connect according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `endpoint` (`tuple[object, ...]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `self._endpoint` from `endpoint`.
2. Calls `self._connected.append((self.family, endpoint))` for its validation or side effect.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `self._connected.append`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_FakeSocket.getpeername`

**Signature**

```python
def getpeername(self) -> tuple[object, ...]:
```

**Purpose**

Implements getpeername according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[object, ...]`. Observed return expression(s): `self._endpoint`.

**Algorithm**

1. Asserts `self._endpoint is not None`.
2. Returns `self._endpoint`.

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

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_FakeSocket.sendall`

**Signature**

```python
def sendall(self, payload: bytes) -> None:
```

**Purpose**

Implements sendall according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `payload` (`bytes`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Calls `self._sent.append(payload)` for its validation or side effect.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `self._sent.append`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_FakeSocket.makefile`

**Signature**

```python
def makefile(self, *args: object, **kwargs: object) -> io.BytesIO:
```

**Purpose**

Implements makefile according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `io.BytesIO`. Observed return expression(s): `io.BytesIO(self._response_bytes)`.

**Algorithm**

1. Returns `io.BytesIO(self._response_bytes)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `io.BytesIO`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_FakeSocket.setsockopt`

**Signature**

```python
def setsockopt(self, *args: object, **kwargs: object) -> None:
```

**Purpose**

Implements setsockopt according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. Observed return expression(s): `None`.

**Algorithm**

1. Returns `None`.

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

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_FakeSocket.close`

**Signature**

```python
def close(self) -> None:
```

**Purpose**

Implements close according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `self.closed` from `True`.

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

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_FakeTlsContext.__init__`

**Signature**

```python
def __init__(self, server_names: list[str]) -> None:
```

**Purpose**

Implements init according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `server_names` (`list[str]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `self._server_names` from `server_names`.

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

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_FakeTlsContext.wrap_socket`

**Signature**

```python
def wrap_socket(self, sock: _FakeSocket, *, server_hostname: str) -> _FakeSocket:
```

**Purpose**

Implements wrap socket according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `sock` (`_FakeSocket`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `server_hostname` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `_FakeSocket`. Observed return expression(s): `sock`.

**Algorithm**

1. Calls `self._server_names.append(server_hostname)` for its validation or side effect.
2. Returns `sock`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `self._server_names.append`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_NetworkHarness.__init__`

**Signature**

```python
def __init__(self, responses: list[bytes]) -> None:
```

**Purpose**

Implements init according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `responses` (`list[bytes]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `self.responses` from `list(responses)`.
2. Defines `self.connected` with annotation `list[tuple[int, tuple[object, ...]]]` from `[]`.
3. Defines `self.sent` with annotation `list[bytes]` from `[]`.
4. Defines `self.server_names` with annotation `list[str]` from `[]`.
5. Defines `self.contexts` with annotation `list[_FakeTlsContext]` from `[]`.
6. Defines `self.sockets` with annotation `list[_FakeSocket]` from `[]`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `list`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_NetworkHarness.socket`

**Signature**

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

Implements socket according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `family` (`int`; optional/default `socket.AF_INET`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `type` (`int`; optional/default `socket.SOCK_STREAM`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `proto` (`int`; optional/default `0`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `fileno` (`int | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `_FakeSocket`. Observed return expression(s): `result`.

**Algorithm**

1. Asserts `type == socket.SOCK_STREAM`.
2. Asserts `fileno is None`.
3. Checks `not self.responses`. When true: Raises `AssertionError('Unexpected additional socket connection')`.
4. Computes `result` from `_FakeSocket(family, self.responses.pop(0), self.connected, self.sent)`.
5. Calls `self.sockets.append(result)` for its validation or side effect.
6. Returns `result`.

**Validation and invariants**

- Rejects or diverts the path when `not self.responses` is true.

**Exceptions**

- Explicitly raises: `AssertionError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `AssertionError`, `_FakeSocket`, `self.responses.pop`, `self.sockets.append`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_NetworkHarness.context`

**Signature**

```python
def context(self, *args: object, **kwargs: object) -> _FakeTlsContext:
```

**Purpose**

Implements context according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `_FakeTlsContext`. Observed return expression(s): `context`.

**Algorithm**

1. Computes `context` from `_FakeTlsContext(self.server_names)`.
2. Calls `self.contexts.append(context)` for its validation or side effect.
3. Returns `context`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_FakeTlsContext`, `self.contexts.append`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_install_network`

**Signature**

```python
def _install_network(
    monkeypatch: pytest.MonkeyPatch,
    *,
    responses: list[bytes] | None = None,
) -> _NetworkHarness:
```

**Purpose**

Implements install network according to the exact implementation and guards in this file.

**Inputs**

- `monkeypatch` (`pytest.MonkeyPatch`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `responses` (`list[bytes] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `_NetworkHarness`. Observed return expression(s): `harness`.

**Algorithm**

1. Computes `harness` from `_NetworkHarness(responses or [_http_response()])`.
2. Calls `monkeypatch.setattr(safe_http.socket, 'socket', harness.socket)` for its validation or side effect.
3. Calls `monkeypatch.setattr(safe_http.ssl, 'create_default_context', harness.context)` for its validation or side effect.
4. Returns `harness`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_NetworkHarness`, `_http_response`, `monkeypatch.setattr`.

**Known repository callers**

- `tests/unit/test_safe_http.py` — `test_environment_proxy_does_not_change_bound_destination`
- `tests/unit/test_safe_http.py` — `test_explicit_https_port_is_resolved_and_connected_exactly`
- `tests/unit/test_safe_http.py` — `test_public_dns_answers_are_accepted`
- `tests/unit/test_safe_http.py` — `test_public_literal_ip_uses_exact_socket_without_dns`
- `tests/unit/test_safe_http.py` — `test_redirect_limit_is_enforced`
- `tests/unit/test_safe_http.py` — `test_redirect_loop_is_rejected`
- `tests/unit/test_safe_http.py` — `test_safe_https_redirect_is_manually_revalidated`
- `tests/unit/test_safe_http.py` — `test_tls_context_keeps_hostname_verification_enabled`
- `tests/unit/test_safe_http.py` — `test_unsafe_redirect_is_rejected_before_target_socket`
- `tests/unit/test_safe_http.py` — `test_validated_dns_snapshot_binds_actual_socket_and_preserves_tls_host`

**Tests**

- `tests/unit/test_safe_http.py::test_environment_proxy_does_not_change_bound_destination`
- `tests/unit/test_safe_http.py::test_explicit_https_port_is_resolved_and_connected_exactly`
- `tests/unit/test_safe_http.py::test_public_dns_answers_are_accepted`
- `tests/unit/test_safe_http.py::test_public_literal_ip_uses_exact_socket_without_dns`
- `tests/unit/test_safe_http.py::test_redirect_limit_is_enforced`
- `tests/unit/test_safe_http.py::test_redirect_loop_is_rejected`
- `tests/unit/test_safe_http.py::test_safe_https_redirect_is_manually_revalidated`
- `tests/unit/test_safe_http.py::test_tls_context_keeps_hostname_verification_enabled`
- `tests/unit/test_safe_http.py::test_unsafe_redirect_is_rejected_before_target_socket`
- `tests/unit/test_safe_http.py::test_validated_dns_snapshot_binds_actual_socket_and_preserves_tls_host`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_install_dns`

**Signature**

```python
def _install_dns(
    monkeypatch: pytest.MonkeyPatch,
    addresses: tuple[str, ...],
) -> list[tuple[str, int]]:
```

**Purpose**

Implements install dns according to the exact implementation and guards in this file.

**Inputs**

- `monkeypatch` (`pytest.MonkeyPatch`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `addresses` (`tuple[str, ...]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `list[tuple[str, int]]`. Observed return expression(s): `calls`; `_dns_records(addresses, port)`.

**Algorithm**

1. Defines `calls` with annotation `list[tuple[str, int]]` from `[]`.
2. Defines the local helper `resolve`; its behavior is documented with the parent function's nested helpers.
3. Calls `monkeypatch.setattr(safe_http.socket, 'getaddrinfo', resolve)` for its validation or side effect.
4. Returns `calls`.

**Meaningful nested/local helpers**

- `resolve` — `def resolve(hostname: str, port: int, **kwargs: object) -> list[tuple[Any, ...]]:`. It executes 3 top-level statement(s), uses `_dns_records`, `calls.append`, and has no explicit raises. Trivial test callbacks are intentionally grouped here with their parent.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_dns_records`, `calls.append`, `monkeypatch.setattr`.

**Known repository callers**

- `tests/unit/test_safe_http.py` — `test_any_nonpublic_dns_answer_fails_before_socket`
- `tests/unit/test_safe_http.py` — `test_environment_proxy_does_not_change_bound_destination`
- `tests/unit/test_safe_http.py` — `test_explicit_https_port_is_resolved_and_connected_exactly`
- `tests/unit/test_safe_http.py` — `test_mixed_public_private_dns_answer_fails_closed`
- `tests/unit/test_safe_http.py` — `test_public_dns_answers_are_accepted`
- `tests/unit/test_safe_http.py` — `test_redirect_limit_is_enforced`
- `tests/unit/test_safe_http.py` — `test_redirect_loop_is_rejected`
- `tests/unit/test_safe_http.py` — `test_safe_https_redirect_is_manually_revalidated`
- `tests/unit/test_safe_http.py` — `test_tls_context_keeps_hostname_verification_enabled`

**Tests**

- `tests/unit/test_safe_http.py::test_any_nonpublic_dns_answer_fails_before_socket`
- `tests/unit/test_safe_http.py::test_environment_proxy_does_not_change_bound_destination`
- `tests/unit/test_safe_http.py::test_explicit_https_port_is_resolved_and_connected_exactly`
- `tests/unit/test_safe_http.py::test_mixed_public_private_dns_answer_fails_closed`
- `tests/unit/test_safe_http.py::test_public_dns_answers_are_accepted`
- `tests/unit/test_safe_http.py::test_redirect_limit_is_enforced`
- `tests/unit/test_safe_http.py::test_redirect_loop_is_rejected`
- `tests/unit/test_safe_http.py::test_safe_https_redirect_is_manually_revalidated`
- `tests/unit/test_safe_http.py::test_tls_context_keeps_hostname_verification_enabled`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_install_dns.resolve`

**Signature**

```python
def resolve(hostname: str, port: int, **kwargs: object) -> list[tuple[Any, ...]]:
```

**Purpose**

Resolves resolve according to the exact implementation and guards in this file.

**Inputs**

- `hostname` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `port` (`int`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `list[tuple[Any, ...]]`. Observed return expression(s): `_dns_records(addresses, port)`.

**Algorithm**

1. Asserts `kwargs == {'type': socket.SOCK_STREAM}`.
2. Calls `calls.append((hostname, port))` for its validation or side effect.
3. Returns `_dns_records(addresses, port)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_dns_records`, `calls.append`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_read`

**Signature**

```python
def _read(url: str = "https://source.example/archive.zip") -> bytes:
```

**Purpose**

Reads and validates read according to the exact implementation and guards in this file.

**Inputs**

- `url` (`str`; optional/default `'https://source.example/archive.zip'`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bytes`. Observed return expression(s): `response.read()`.

**Algorithm**

1. Enters managed context(s) `open_safe_https(url, timeout=12.5)` and executes: Returns `response.read()`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `open_safe_https`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `open_safe_https`, `response.read`.

**Known repository callers**

- `tests/unit/test_safe_http.py` — `test_any_nonpublic_dns_answer_fails_before_socket`
- `tests/unit/test_safe_http.py` — `test_dns_errors_are_controlled_before_socket`
- `tests/unit/test_safe_http.py` — `test_environment_proxy_does_not_change_bound_destination`
- `tests/unit/test_safe_http.py` — `test_explicit_https_port_is_resolved_and_connected_exactly`
- `tests/unit/test_safe_http.py` — `test_literal_and_malformed_numeric_ip_rejection_never_uses_dns`
- `tests/unit/test_safe_http.py` — `test_malformed_or_unusable_dns_results_fail_before_socket`
- `tests/unit/test_safe_http.py` — `test_mixed_public_private_dns_answer_fails_closed`
- `tests/unit/test_safe_http.py` — `test_public_dns_answers_are_accepted`
- `tests/unit/test_safe_http.py` — `test_public_literal_ip_uses_exact_socket_without_dns`
- `tests/unit/test_safe_http.py` — `test_redirect_limit_is_enforced`
- `tests/unit/test_safe_http.py` — `test_redirect_loop_is_rejected`
- `tests/unit/test_safe_http.py` — `test_tls_context_keeps_hostname_verification_enabled`
- `tests/unit/test_safe_http.py` — `test_unsafe_redirect_is_rejected_before_target_socket`
- `tests/unit/test_safe_http.py` — `test_unsafe_url_identity_fails_before_dns`
- `tests/unit/test_safe_http.py` — `test_validated_dns_snapshot_binds_actual_socket_and_preserves_tls_host`

**Tests**

- `tests/unit/test_safe_http.py::test_any_nonpublic_dns_answer_fails_before_socket`
- `tests/unit/test_safe_http.py::test_dns_errors_are_controlled_before_socket`
- `tests/unit/test_safe_http.py::test_environment_proxy_does_not_change_bound_destination`
- `tests/unit/test_safe_http.py::test_explicit_https_port_is_resolved_and_connected_exactly`
- `tests/unit/test_safe_http.py::test_literal_and_malformed_numeric_ip_rejection_never_uses_dns`
- `tests/unit/test_safe_http.py::test_malformed_or_unusable_dns_results_fail_before_socket`
- `tests/unit/test_safe_http.py::test_mixed_public_private_dns_answer_fails_closed`
- `tests/unit/test_safe_http.py::test_public_dns_answers_are_accepted`
- `tests/unit/test_safe_http.py::test_public_literal_ip_uses_exact_socket_without_dns`
- `tests/unit/test_safe_http.py::test_redirect_limit_is_enforced`
- `tests/unit/test_safe_http.py::test_redirect_loop_is_rejected`
- `tests/unit/test_safe_http.py::test_tls_context_keeps_hostname_verification_enabled`
- `tests/unit/test_safe_http.py::test_unsafe_redirect_is_rejected_before_target_socket`
- `tests/unit/test_safe_http.py::test_unsafe_url_identity_fails_before_dns`
- `tests/unit/test_safe_http.py::test_validated_dns_snapshot_binds_actual_socket_and_preserves_tls_host`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_dns_errors_are_controlled_before_socket.fail`

**Signature**

```python
def fail(*args: object, **kwargs: object) -> list[tuple[Any, ...]]:
```

**Purpose**

Implements fail according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `list[tuple[Any, ...]]`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Raises `error`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `error`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- No function calls.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unsafe_redirect_is_rejected_before_target_socket.resolve`

**Signature**

```python
def resolve(hostname: str, port: int, **kwargs: object) -> list[tuple[Any, ...]]:
```

**Purpose**

Resolves resolve according to the exact implementation and guards in this file.

**Inputs**

- `hostname` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `port` (`int`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `list[tuple[Any, ...]]`. Observed return expression(s): `_dns_records((address,), port)`.

**Algorithm**

1. Computes `address` from `PUBLIC_IPV4 if hostname == 'source.example' else '127.0.0.1'`.
2. Returns `_dns_records((address,), port)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_dns_records`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_validated_dns_snapshot_binds_actual_socket_and_preserves_tls_host.rebind`

**Signature**

```python
def rebind(hostname: str, port: int, **kwargs: object) -> list[tuple[Any, ...]]:
```

**Purpose**

Implements rebind according to the exact implementation and guards in this file.

**Inputs**

- `hostname` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `port` (`int`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `list[tuple[Any, ...]]`. Observed return expression(s): `_dns_records((address,), port)`.

**Algorithm**

1. Executes `nonlocal resolutions`.
2. Updates `resolutions` using `` and `1`.
3. Computes `address` from `PUBLIC_IPV4 if resolutions == 1 else '127.0.0.1'`.
4. Returns `_dns_records((address,), port)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_dns_records`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_public_dns_answers_are_accepted`

**Signature**

```python
def test_public_dns_answers_are_accepted(
    monkeypatch: pytest.MonkeyPatch,
    addresses: tuple[str, ...],
) -> None:
```

**Purpose**

Protects the `public dns answers are accepted` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `monkeypatch`, `addresses`.
- Contains 2 explicit setup/context statement(s).
- Computes `calls` from `_install_dns(monkeypatch, addresses)`.
- Computes `harness` from `_install_network(monkeypatch)`.

**Action**

- Calls `_install_dns`, `_install_network`, `_read`.

**Expected result**

- Direct assertions: `assert _read() == b'ok'`; `assert calls == [('source.example', 443)]`; `assert harness.connected`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `public dns answers are accepted` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks; fake/blocked network. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_install_dns`, `_install_network`, `_read`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_malformed_or_unusable_dns_results_fail_before_socket`

**Signature**

```python
def test_malformed_or_unusable_dns_results_fail_before_socket(
    monkeypatch: pytest.MonkeyPatch,
    records: list[tuple[Any, ...]],
) -> None:
```

**Purpose**

Protects the `malformed or unusable dns results fail before socket` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `monkeypatch`, `records`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(SafeHttpsError, match='DNS|address')` and executes: Calls `_read()` for its validation or side effect.

**Action**

- Calls `_read`, `monkeypatch.setattr`, `object`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(SafeHttpsError, match='DNS|address'): _read()`.

**Regression protected**

- Protects the exact `malformed or unusable dns results fail before socket` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_read`, `monkeypatch.setattr`, `object`, `pytest.fail`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_any_nonpublic_dns_answer_fails_before_socket`

**Signature**

```python
def test_any_nonpublic_dns_answer_fails_before_socket(
    monkeypatch: pytest.MonkeyPatch,
    address: str,
) -> None:
```

**Purpose**

Protects the `any nonpublic dns answer fails before socket` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `monkeypatch`, `address`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(SafeHttpsError, match='public|global|address|DNS')` and executes: Calls `_read()` for its validation or side effect.

**Action**

- Calls `_install_dns`, `_read`, `monkeypatch.setattr`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(SafeHttpsError, match='public|global|address|DNS'): _read()`.

**Regression protected**

- Protects the exact `any nonpublic dns answer fails before socket` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_install_dns`, `_read`, `monkeypatch.setattr`, `pytest.fail`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_mixed_public_private_dns_answer_fails_closed`

**Signature**

```python
def test_mixed_public_private_dns_answer_fails_closed(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `mixed public private dns answer fails closed` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `monkeypatch`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(SafeHttpsError, match='public|global|address|DNS')` and executes: Calls `_read()` for its validation or side effect.

**Action**

- Calls `_install_dns`, `_read`, `monkeypatch.setattr`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(SafeHttpsError, match='public|global|address|DNS'): _read()`.

**Regression protected**

- Protects the exact `mixed public private dns answer fails closed` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_install_dns`, `_read`, `monkeypatch.setattr`, `pytest.fail`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_dns_errors_are_controlled_before_socket`

**Signature**

```python
def test_dns_errors_are_controlled_before_socket(
    monkeypatch: pytest.MonkeyPatch,
    error: Exception,
) -> None:
```

**Purpose**

Protects the `dns errors are controlled before socket` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `monkeypatch`, `error`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(SafeHttpsError, match='DNS|resolve')` and executes: Calls `_read()` for its validation or side effect.

**Action**

- Calls `OSError`, `UnicodeError`, `_read`, `monkeypatch.setattr`, `socket.gaierror`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(SafeHttpsError, match='DNS|resolve'): _read()`.

**Regression protected**

- Protects the exact `dns errors are controlled before socket` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `OSError`, `UnicodeError`, `_read`, `monkeypatch.setattr`, `pytest.fail`, `pytest.mark.parametrize`, `pytest.raises`, `socket.gaierror`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unsafe_url_identity_fails_before_dns`

**Signature**

```python
def test_unsafe_url_identity_fails_before_dns(
    monkeypatch: pytest.MonkeyPatch,
    url: str,
) -> None:
```

**Purpose**

Protects the `unsafe url identity fails before dns` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `monkeypatch`, `url`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(SafeHttpsError, match='HTTPS|credential|localhost|host|URL')` and executes: Calls `_read(url)` for its validation or side effect.

**Action**

- Calls `_read`, `monkeypatch.setattr`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(SafeHttpsError, match='HTTPS|credential|localhost|host|URL'): _read(url)`.

**Regression protected**

- Protects the exact `unsafe url identity fails before dns` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_read`, `monkeypatch.setattr`, `pytest.fail`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_literal_and_malformed_numeric_ip_rejection_never_uses_dns`

**Signature**

```python
def test_literal_and_malformed_numeric_ip_rejection_never_uses_dns(
    monkeypatch: pytest.MonkeyPatch,
    url: str,
) -> None:
```

**Purpose**

Protects the `literal and malformed numeric ip rejection never uses dns` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `monkeypatch`, `url`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(SafeHttpsError, match='public|global|address|IP|URL')` and executes: Calls `_read(url)` for its validation or side effect.

**Action**

- Calls `_read`, `monkeypatch.setattr`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(SafeHttpsError, match='public|global|address|IP|URL'): _read(url)`.

**Regression protected**

- Protects the exact `literal and malformed numeric ip rejection never uses dns` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_read`, `monkeypatch.setattr`, `pytest.fail`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_public_literal_ip_uses_exact_socket_without_dns`

**Signature**

```python
def test_public_literal_ip_uses_exact_socket_without_dns(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `public literal ip uses exact socket without dns` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `monkeypatch`.
- Contains 1 explicit setup/context statement(s).
- Computes `harness` from `_install_network(monkeypatch)`.

**Action**

- Calls `_install_network`, `_read`, `monkeypatch.setattr`.

**Expected result**

- Direct assertions: `assert _read(f'https://{PUBLIC_IPV4}/archive.zip') == b'ok'`; `assert harness.connected == [(socket.AF_INET, (PUBLIC_IPV4, 443))]`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `public literal ip uses exact socket without dns` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks; fake/blocked network. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_install_network`, `_read`, `monkeypatch.setattr`, `pytest.fail`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_explicit_https_port_is_resolved_and_connected_exactly`

**Signature**

```python
def test_explicit_https_port_is_resolved_and_connected_exactly(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `explicit https port is resolved and connected exactly` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `monkeypatch`.
- Contains 2 explicit setup/context statement(s).
- Computes `calls` from `_install_dns(monkeypatch, (PUBLIC_IPV4,))`.
- Computes `harness` from `_install_network(monkeypatch)`.

**Action**

- Calls `_install_dns`, `_install_network`, `_read`, `b''.join`.

**Expected result**

- Direct assertions: `assert _read('https://source.example:8443/archive.zip') == b'ok'`; `assert calls == [('source.example', 8443)]`; `assert harness.connected == [(socket.AF_INET, (PUBLIC_IPV4, 8443))]`; `assert harness.server_names == ['source.example']`; `assert b'\r\nHost: source.example:8443\r\n' in b''.join(harness.sent)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `explicit https port is resolved and connected exactly` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks; fake/blocked network. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_install_dns`, `_install_network`, `_read`, `b''.join`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_safe_https_redirect_is_manually_revalidated`

**Signature**

```python
def test_safe_https_redirect_is_manually_revalidated(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `safe https redirect is manually revalidated` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `monkeypatch`.
- Contains 3 explicit setup/context statement(s).
- Computes `calls` from `_install_dns(monkeypatch, (PUBLIC_IPV4,))`.
- Computes `harness` from `_install_network(monkeypatch, responses=[_http_response(302, body=b'', headers={'Location': 'https://cdn.example/file'}), _http_response(body=b'archive')])`.
- Enters managed context(s) `open_safe_https('https://source.example/archive.zip', timeout=12.5)` and executes: Asserts `response.read() == b'archive'`. Asserts `response.url == 'https://cdn.example/file'`. Asserts `response.history == ('https://source.example/archive.zip',)`.

**Action**

- Calls `_http_response`, `_install_dns`, `_install_network`, `open_safe_https`, `response.read`.

**Expected result**

- Direct assertions: `assert calls == [('source.example', 443), ('cdn.example', 443)]`; `assert [endpoint for _, endpoint in harness.connected] == [(PUBLIC_IPV4, 443), (PUBLIC_IPV4, 443)]`; `assert harness.server_names == ['source.example', 'cdn.example']`; `assert b'\r\nHost: source.example\r\n' in harness.sent[0]`; `assert b'\r\nHost: cdn.example\r\n' in harness.sent[1]`; `assert response.read() == b'archive'`; `assert response.url == 'https://cdn.example/file'`; `assert response.history == ('https://source.example/archive.zip',)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `safe https redirect is manually revalidated` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks; fake/blocked network. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_http_response`, `_install_dns`, `_install_network`, `open_safe_https`, `response.read`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unsafe_redirect_is_rejected_before_target_socket`

**Signature**

```python
def test_unsafe_redirect_is_rejected_before_target_socket(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `unsafe redirect is rejected before target socket` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `monkeypatch`.
- Contains 2 explicit setup/context statement(s).
- Computes `harness` from `_install_network(monkeypatch, responses=[_http_response(302, body=b'', headers={'Location': 'https://private.example/file'})])`.
- Enters managed context(s) `pytest.raises(SafeHttpsError, match='public|global|address|DNS')` and executes: Calls `_read()` for its validation or side effect.

**Action**

- Calls `_dns_records`, `_http_response`, `_install_network`, `_read`, `monkeypatch.setattr`.

**Expected result**

- Direct assertions: `assert harness.connected == [(socket.AF_INET, (PUBLIC_IPV4, 443))]`.
- Expected exception contexts: `with pytest.raises(SafeHttpsError, match='public|global|address|DNS'): _read()`.

**Regression protected**

- Protects the exact `unsafe redirect is rejected before target socket` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks; fake/blocked network. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_dns_records`, `_http_response`, `_install_network`, `_read`, `monkeypatch.setattr`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_redirect_loop_is_rejected`

**Signature**

```python
def test_redirect_loop_is_rejected(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `redirect loop is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `monkeypatch`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(SafeHttpsError, match='loop')` and executes: Calls `_read()` for its validation or side effect.

**Action**

- Calls `_http_response`, `_install_dns`, `_install_network`, `_read`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(SafeHttpsError, match='loop'): _read()`.

**Regression protected**

- Protects the exact `redirect loop is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks; fake/blocked network. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_http_response`, `_install_dns`, `_install_network`, `_read`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_redirect_limit_is_enforced`

**Signature**

```python
def test_redirect_limit_is_enforced(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `redirect limit is enforced` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `monkeypatch`.
- Contains 2 explicit setup/context statement(s).
- Computes `redirects` from `[_http_response(302, body=b'', headers={'Location': f'/step-{index}'}) for index in range(12)]`.
- Enters managed context(s) `pytest.raises(SafeHttpsError, match='redirect')` and executes: Calls `_read()` for its validation or side effect.

**Action**

- Calls `_http_response`, `_install_dns`, `_install_network`, `_read`, `range`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(SafeHttpsError, match='redirect'): _read()`.

**Regression protected**

- Protects the exact `redirect limit is enforced` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks; fake/blocked network. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_http_response`, `_install_dns`, `_install_network`, `_read`, `pytest.raises`, `range`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_validated_dns_snapshot_binds_actual_socket_and_preserves_tls_host`

**Signature**

```python
def test_validated_dns_snapshot_binds_actual_socket_and_preserves_tls_host(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `validated dns snapshot binds actual socket and preserves tls host` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `monkeypatch`.
- Contains 3 explicit setup/context statement(s).
- Computes `resolutions` from `0`.
- Computes `harness` from `_install_network(monkeypatch)`.
- Computes `request` from `b''.join(harness.sent).decode('ascii')`.

**Action**

- Calls `_dns_records`, `_install_network`, `_read`, `b''.join`, `b''.join(harness.sent).decode`, `monkeypatch.setattr`, `request.startswith`.

**Expected result**

- Direct assertions: `assert _read('https://rebind.example/archive.zip') == b'ok'`; `assert resolutions == 1`; `assert harness.connected == [(socket.AF_INET, (PUBLIC_IPV4, 443))]`; `assert harness.server_names == ['rebind.example']`; `assert request.startswith('GET /archive.zip HTTP/1.1\r\n')`; `assert '\r\nHost: rebind.example\r\n' in request`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `validated dns snapshot binds actual socket and preserves tls host` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks; fake/blocked network. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_dns_records`, `_install_network`, `_read`, `b''.join`, `b''.join(harness.sent).decode`, `monkeypatch.setattr`, `request.startswith`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_environment_proxy_does_not_change_bound_destination`

**Signature**

```python
def test_environment_proxy_does_not_change_bound_destination(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `environment proxy does not change bound destination` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `monkeypatch`.
- Contains 1 explicit setup/context statement(s).
- Computes `harness` from `_install_network(monkeypatch)`.

**Action**

- Calls `_install_dns`, `_install_network`, `_read`, `monkeypatch.setenv`.

**Expected result**

- Direct assertions: `assert _read() == b'ok'`; `assert harness.connected == [(socket.AF_INET, (PUBLIC_IPV4, 443))]`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `environment proxy does not change bound destination` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks; fake/blocked network. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_install_dns`, `_install_network`, `_read`, `monkeypatch.setenv`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_malformed_header_name_is_rejected_before_dns`

**Signature**

```python
def test_malformed_header_name_is_rejected_before_dns(
    monkeypatch: pytest.MonkeyPatch,
    header_name: str,
) -> None:
```

**Purpose**

Protects the `malformed header name is rejected before dns` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `monkeypatch`, `header_name`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(SafeHttpsError, match='header|Host'), open_safe_https('https://source.example/archive.zip', timeout=12.5, headers={header_name: 'attacker.example'})` and executes: Executes `pass` control flow.

**Action**

- Calls `monkeypatch.setattr`, `open_safe_https`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(SafeHttpsError, match='header|Host'), open_safe_https('https://source.example/archive.zip', timeout=12.5, headers={header_name: 'attacker.example'}): pass`.

**Regression protected**

- Protects the exact `malformed header name is rejected before dns` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks; fake/blocked network. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `monkeypatch.setattr`, `open_safe_https`, `pytest.fail`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_tls_context_keeps_hostname_verification_enabled`

**Signature**

```python
def test_tls_context_keeps_hostname_verification_enabled(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `tls context keeps hostname verification enabled` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `monkeypatch`.
- Contains 1 explicit setup/context statement(s).
- Computes `harness` from `_install_network(monkeypatch)`.

**Action**

- Calls `_install_dns`, `_install_network`, `_read`.

**Expected result**

- Direct assertions: `assert _read() == b'ok'`; `assert harness.server_names == ['source.example']`; `assert len(harness.contexts) == 1`; `assert harness.contexts[0].check_hostname is True`; `assert harness.contexts[0].verify_mode == ssl.CERT_REQUIRED`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `tls context keeps hostname verification enabled` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks; fake/blocked network. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_install_dns`, `_install_network`, `_read`, `len`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

## 7. Data contracts

No DataFrame/GeoDataFrame column is referenced directly. Object and scalar contracts are documented through classes, parameters, returns, constants, and validators.

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

This file contributes to LandScout's `test` evidence flow as described by its purpose and public symbols. It preserves the distinction among fact, proxy evidence, policy interpretation, diagnostic status, and parcel precheck.

## 15. Explicit non-goals

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

## 16. Tests

Direct name-resolved tests appear under each symbol. Higher-level tests may exercise private helpers through a public source-complete function; companion documents for all test files describe their fixtures, actions, assertions, and boundaries.

## 17. Change impact

Changing this file requires reviewing its static callers, package exports, directly mapped tests, relevant schema/hash/version constants, source locks, persisted artifact contracts, and the corresponding pipeline/cross-cutting documents. Any byte change makes the SHA256 above stale and requires regenerating this companion.

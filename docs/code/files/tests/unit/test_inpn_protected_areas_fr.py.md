# `tests/unit/test_inpn_protected_areas_fr.py`

## File identity

- Repository path: `tests/unit/test_inpn_protected_areas_fr.py`
- File type: Python test
- Layer: unit/regression test
- Domain: test
- Responsibility: Provides complete unit and regression coverage for the `inpn_protected_areas_fr` contracts exercised in this file.
- Source SHA256: `1f4561a2e58cd09b3a1d934ce0998af09d9f81eb67ae53cd47e5c830ad60366d`

## 1. Purpose

Provides complete unit and regression coverage for the `inpn_protected_areas_fr` contracts exercised in this file.

## 2. Position in LandScout architecture

This file belongs to the **unit/regression test** layer and the **test** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `import inspect`
- `import io`
- `import json`
- `import stat`
- `import warnings`
- `import zipfile`
- `from contextlib import contextmanager`
- `from dataclasses import FrozenInstanceError, fields, replace`
- `from datetime import datetime`
- `from hashlib import sha256`
- `from pathlib import Path`
- `from typing import Any, Self`

### Third-party packages

- `import pytest`
- `import yaml`

### Internal LandScout imports

- `from landscout import sources`
- `from landscout.common import safe_http`
- `from landscout.common.safe_http import SafeHttpsError`
- `from landscout.sources import inpn_protected_areas_fr as inpn`
- `from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasDownload,
    InpnProtectedAreasExtractedFile,
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasSourceError,
    download_inpn_protected_areas_archive,
    extract_inpn_protected_areas_archive,
    load_inpn_protected_areas_source_config,
)`

## 4. Contract taxonomy

### A. Python constants

#### `CONFIG_PATH`

```python
CONFIG_PATH = Path("configs/sources/inpn_protected_areas_fr.yaml")
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_inpn_protected_areas_fr.py::_config_payload` (value reference).

#### `EXPECTED_EXPORTS`

```python
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
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_inpn_protected_areas_fr.py::test_public_api_exports_only_stable_high_level_symbols` (value reference).


### B. Type aliases and closed domains

No module-level Literal/Annotated/TypeAlias declaration is present.

### C. Meaningful dunder contracts

No meaningful module-level dunder contract is declared.

### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

### `_Response`

**Purpose:** Encapsulates the test behavior implemented by its exact methods and attributes below.

**Kind:** class.

**Inheritance:** plain object.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `raw` | `self.raw = io.BytesIO(payload)  # assigned in __init__` | Exact raw source value retained before the owning parser/normalizer derives additional facts. |
| `url` | `self.url = url  # assigned in __init__` | Deterministic test-double state `url` used by the reproduced network/source regression harness. |
| `status_code` | `self.status_code = status_code  # assigned in __init__` | Deterministic test-double state `status_code` used by the reproduced network/source regression harness. |
| `headers` | `self.headers = {} if location is None else {'Location': location}  # assigned in __init__` | Deterministic test-double state `headers` used by the reproduced network/source regression harness. |
| `closed` | `self.closed = False  # assigned in __init__` | Deterministic test-double state `closed` used by the reproduced network/source regression harness. |

**Interface consumers**

- type annotation: `tests/unit/test_inpn_protected_areas_fr.py::_Session.__init__` via `_Response`.
- type annotation: `tests/unit/test_inpn_protected_areas_fr.py::_Session.get` via `_Response`.
- constructor call: `tests/unit/test_inpn_protected_areas_fr.py::_session` via `_Response`.
- type annotation: `tests/unit/test_inpn_protected_areas_fr.py::_session` via `_Response`.
- constructor call: `tests/unit/test_inpn_protected_areas_fr.py::test_malformed_response_headers_have_controlled_error` via `_Response`.
- constructor call: `tests/unit/test_inpn_protected_areas_fr.py::test_midstream_protocol_failure_has_controlled_error` via `_Response`.

**Exact class source**

```python
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
```

### `_Session`

**Purpose:** Encapsulates the test behavior implemented by its exact methods and attributes below.

**Kind:** class.

**Inheritance:** plain object.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `responses` | `self.responses = list(responses or ([] if response is None else [response]))  # assigned in __init__` | Deterministic test-double state `responses` used by the reproduced network/source regression harness. |
| `error` | `self.error = error  # assigned in __init__` | Deterministic test-double state `error` used by the reproduced network/source regression harness. |
| `calls` | `self.calls = []  # assigned in __init__` | Deterministic test-double state `calls` used by the reproduced network/source regression harness. |

**Interface consumers**

- type annotation: `tests/unit/test_inpn_protected_areas_fr.py::_session` via `_Session`.
- constructor call: `tests/unit/test_inpn_protected_areas_fr.py::_session` via `_Session`.
- type annotation: `tests/unit/test_inpn_protected_areas_fr.py::_download` via `_Session`.
- type annotation: `tests/unit/test_inpn_protected_areas_fr.py::_download_with_session` via `_Session`.
- constructor call: `tests/unit/test_inpn_protected_areas_fr.py::test_coordinated_cache_and_metadata_snapshot_change_is_not_a_cache_hit` via `_Session`.
- constructor call: `tests/unit/test_inpn_protected_areas_fr.py::test_http_and_payload_failures_are_controlled` via `_Session`.
- constructor call: `tests/unit/test_inpn_protected_areas_fr.py::test_malformed_response_headers_have_controlled_error` via `_Session`.
- constructor call: `tests/unit/test_inpn_protected_areas_fr.py::test_midstream_protocol_failure_has_controlled_error` via `_Session`.
- constructor call: `tests/unit/test_inpn_protected_areas_fr.py::test_failed_replacement_restores_a_still_reusable_valid_download_pair` via `_Session`.
- constructor call: `tests/unit/test_inpn_protected_areas_fr.py::test_archive_and_extraction_cache_reuse_are_independent` via `_Session`.

**Exact class source**

```python
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
```

### `test_midstream_protocol_failure_has_controlled_error._FailingRaw`

**Purpose:** Encapsulates the test behavior implemented by its exact methods and attributes below.

**Kind:** class.

**Inheritance:** plain object.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- constructor call: `tests/unit/test_inpn_protected_areas_fr.py::test_midstream_protocol_failure_has_controlled_error` via `_FailingRaw`.

**Exact class source**

```python
class _FailingRaw:
        decode_content = False

        def seek(self, offset: int) -> int:
            return offset

        def read(self, size: int = -1) -> bytes:
            raise OSError("connection ended mid-stream")
```


## 6. Functions and methods

### `_Response.__init__`

**Exact signature**

```python
def __init__(
        self,
        payload: bytes,
        *,
        url: str,
        status_code: int = 200,
        location: str | None = None,
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

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `self.closed`, `self.headers`, `self.raw`, `self.status_code`, `self.url`.
- Input mutation: none.

**Repository interfaces and consumers**

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_Response.is_redirect`

**Exact signature**

```python
def is_redirect(self) -> bool:
```

**Purpose**

Tests whether redirect; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `bool`.
- Every observed return expression is reproduced without truncation:
```python
self.status_code in {301, 302, 303, 307, 308} and 'Location' in self.headers
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

**Complete source-ordered implementation**

```python
def is_redirect(self) -> bool:
        return self.status_code in {301, 302, 303, 307, 308} and "Location" in self.headers
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_Response.raise_for_status`

**Exact signature**

```python
def raise_for_status(self) -> None:
```

**Purpose**

Private `test` helper for raise for status; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `self.status_code >= 400`.
- Explicit raise expressions: `OSError(f'HTTP {self.status_code}')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

**Complete source-ordered implementation**

```python
def raise_for_status(self) -> None:
        if self.status_code >= 400:
            raise OSError(f"HTTP {self.status_code}")
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_Response.iter_content`

**Exact signature**

```python
def iter_content(self, chunk_size: int = 8192) -> Any:
```

**Purpose**

Private `test` helper for iter content; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `Any`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: `self.raw.read`.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

**Complete source-ordered implementation**

```python
def iter_content(self, chunk_size: int = 8192) -> Any:
        while chunk := self.raw.read(chunk_size):
            yield chunk
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_Response.close`

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

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `self.closed`.
- Input mutation: none.

**Repository interfaces and consumers**

- method call: `tests/unit/test_inpn_protected_areas_fr.py::_Response.__exit__` via `self.close`.

**Complete source-ordered implementation**

```python
def close(self) -> None:
        self.closed = True
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_Response.read`

**Exact signature**

```python
def read(self, size: int = -1) -> bytes:
```

**Purpose**

Reads read; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `bytes`.
- Every observed return expression is reproduced without truncation:
```python
self.raw.read(size)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: `self.raw.read`.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

**Complete source-ordered implementation**

```python
def read(self, size: int = -1) -> bytes:
        return self.raw.read(size)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_Response.__enter__`

**Exact signature**

```python
def __enter__(self) -> Self:
```

**Purpose**

Private `test` helper for enter; its complete implementation below is the authoritative behavioral contract.

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

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

**Complete source-ordered implementation**

```python
def __enter__(self) -> Self:
        return self
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_Response.__exit__`

**Exact signature**

```python
def __exit__(self, *args: object) -> None:
```

**Purpose**

Private `test` helper for exit; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

**Complete source-ordered implementation**

```python
def __exit__(self, *args: object) -> None:
        self.close()
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_Session.__init__`

**Exact signature**

```python
def __init__(
        self,
        response: _Response | None = None,
        *,
        responses: list[_Response] | None = None,
        error: Exception | None = None,
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

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `self.error`, `self.responses`.
- Input mutation: none.

**Repository interfaces and consumers**

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_Session.get`

**Exact signature**

```python
def get(self, url: str, **kwargs: object) -> _Response:
```

**Purpose**

Private `test` helper for get; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `_Response`.
- Every observed return expression is reproduced without truncation:
```python
response
```

**Validation and exceptions**

- Guard with a raise path: `self.error is not None`.
- Guard with a raise path: `not self.responses`.
- Explicit raise expressions: `AssertionError('No fake HTTP response was configured')`, `self.error`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `self.calls`, `self.responses`.
- Input mutation: none.

**Repository interfaces and consumers**

- method call: `tests/unit/test_inpn_protected_areas_fr.py::_Session.open` via `self.get`.

**Complete source-ordered implementation**

```python
def get(self, url: str, **kwargs: object) -> _Response:
        self.calls.append((url, kwargs))
        if self.error is not None:
            raise self.error
        if not self.responses:
            raise AssertionError("No fake HTTP response was configured")
        response = self.responses.pop(0)
        response.raw.seek(0)
        return response
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_Session.open`

**Exact signature**

```python
def open(
        self,
        url: str,
        *,
        timeout: float,
        headers: dict[str, str] | None = None,
        max_redirects: int = 10,
    ) -> Any:
```

**Purpose**

Private `test` helper for open; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `Any`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `not 200 <= response.status_code < 300`.
- Explicit raise expressions: `SafeHttpsError(f'HTTP status {response.status_code}')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- function object argument: `tests/unit/test_inpn_protected_areas_fr.py::_download_with_session` via `monkeypatch.setattr(inpn, 'open_safe_https', session.open)`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_zip_bytes`

**Exact signature**

```python
def _zip_bytes(
    members: dict[str, bytes] | list[tuple[str, bytes]] | None = None,
) -> bytes:
```

**Purpose**

Private `test` helper for zip bytes; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `bytes`.
- Every observed return expression is reproduced without truncation:
```python
stream.getvalue()
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `info.compress_type`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_inpn_protected_areas_fr.py::_unsupported_compression_zip` via `_zip_bytes`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::_config` via `_zip_bytes`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::_session` via `_zip_bytes`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::_download` via `_zip_bytes`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_valid_zip_download_binds_exact_bytes_and_lineage` via `_zip_bytes`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_cold_download_must_match_configured_snapshot_before_publication` via `_zip_bytes`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_coordinated_cache_and_metadata_snapshot_change_is_not_a_cache_hit` via `_zip_bytes`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_malformed_response_headers_have_controlled_error` via `_zip_bytes`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_midstream_protocol_failure_has_controlled_error` via `_zip_bytes`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_invalid_download_cache_is_a_miss` via `_zip_bytes`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_successful_first_and_replacement_publication` via `_zip_bytes`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_unsafe_zip_member_paths_are_rejected` via `_zip_bytes`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_duplicate_or_colliding_zip_destinations_are_rejected` via `_zip_bytes`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_complete_zip_inventory_is_validated_before_member_copy` via `_zip_bytes`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_validates_complete_inventory_before_copying` via `_zip_bytes`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_normal_nested_members_are_accepted` via `_zip_bytes`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_inventory_is_complete_ordered_and_hashed` via `_zip_bytes`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_invalid_extraction_cache_is_rebuilt` via `_zip_bytes`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_rejects_stale_download_bytes` via `_zip_bytes`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_exact_file_inventory_does_not_omit_unknown_suffixes` via `_zip_bytes`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_special_zip`

**Exact signature**

```python
def _special_zip(name: str, mode: int) -> bytes:
```

**Purpose**

Private `test` helper for special zip; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `bytes`.
- Every observed return expression is reproduced without truncation:
```python
stream.getvalue()
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `info.create_system`, `info.external_attr`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_zip_links_and_special_files_are_rejected` via `_special_zip`.

**Complete source-ordered implementation**

```python
def _special_zip(name: str, mode: int) -> bytes:
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, "w") as archive:
        info = zipfile.ZipInfo(name)
        info.create_system = 3
        info.external_attr = mode << 16
        archive.writestr(info, b"target")
    return stream.getvalue()
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_unsupported_compression_zip`

**Exact signature**

```python
def _unsupported_compression_zip() -> bytes:
```

**Purpose**

Private `test` helper for unsupported compression zip; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `bytes`.
- Every observed return expression is reproduced without truncation:
```python
bytes(payload)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `payload[central + 10:central + 12]`, `payload[local + 8:local + 10]`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_unsupported_zip_compression_has_controlled_error` via `_unsupported_compression_zip`.

**Complete source-ordered implementation**

```python
def _unsupported_compression_zip() -> bytes:
    payload = bytearray(_zip_bytes())
    local = payload.index(b"PK\x03\x04")
    central = payload.index(b"PK\x01\x02")
    payload[local + 8 : local + 10] = (99).to_bytes(2, "little")
    payload[central + 10 : central + 12] = (99).to_bytes(2, "little")
    return bytes(payload)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_config_payload`

**Exact signature**

```python
def _config_payload() -> dict[str, object]:
```

**Purpose**

Private `test` helper for config payload; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict[str, object]`.
- Every observed return expression is reproduced without truncation:
```python
payload
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: `CONFIG_PATH.read_text`.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_inpn_protected_areas_fr.py::_config` via `_config_payload`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_config_rejects_invalid_expected_snapshot_integrity` via `_config_payload`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_config_rejects_noncanonical_values` via `_config_payload`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_download_cache_setup_failure_is_controlled` via `_config_payload`.

**Complete source-ordered implementation**

```python
def _config_payload() -> dict[str, object]:
    payload = yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))
    assert isinstance(payload, dict)
    return payload
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_write_config`

**Exact signature**

```python
def _write_config(tmp_path: Path, payload: dict[str, object]) -> Path:
```

**Purpose**

Serializes config; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `Path`.
- Every observed return expression is reproduced without truncation:
```python
path
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: `path.write_text`.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_config_rejects_noncanonical_values` via `_write_config`.

**Complete source-ordered implementation**

```python
def _write_config(tmp_path: Path, payload: dict[str, object]) -> Path:
    path = tmp_path / "source.yaml"
    path.write_text(
        yaml.safe_dump(payload, allow_unicode=True, sort_keys=False),
        encoding="utf-8",
    )
    return path
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_config`

**Exact signature**

```python
def _config(
    tmp_path: Path,
    expected_bytes: bytes | None = None,
) -> InpnProtectedAreasSourceConfig:
```

**Purpose**

Private `test` helper for config; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `InpnProtectedAreasSourceConfig`.
- Every observed return expression is reproduced without truncation:
```python
InpnProtectedAreasSourceConfig.model_validate(payload)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `InpnProtectedAreasSourceConfig.model_validate`.
- Hashing: `sha256`, `sha256(snapshot).hexdigest`.
- Environment/process effects: none.
- In-memory mutation: `payload['cache_root']`, `payload['expected_archive_sha256']`, `payload['expected_archive_size_bytes']`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_inpn_protected_areas_fr.py::_download` via `_config`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_valid_zip_download_binds_exact_bytes_and_lineage` via `_config`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_cold_download_must_match_configured_snapshot_before_publication` via `_config`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_http_and_payload_failures_are_controlled` via `_config`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_unsupported_zip_compression_has_controlled_error` via `_config`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_malformed_response_headers_have_controlled_error` via `_config`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_midstream_protocol_failure_has_controlled_error` via `_config`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_unsafe_zip_member_paths_are_rejected` via `_config`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_duplicate_or_colliding_zip_destinations_are_rejected` via `_config`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_zip_links_and_special_files_are_rejected` via `_config`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_complete_zip_inventory_is_validated_before_member_copy` via `_config`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_rejects_wrong_download_type` via `_config`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_download_uses_no_hidden_reference_page_scrape` via `_config`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_session`

**Exact signature**

```python
def _session(
    config: InpnProtectedAreasSourceConfig,
    payload: bytes | None = None,
    *,
    status_code: int = 200,
    redirect_chain: tuple[str, ...] = (),
) -> _Session:
```

**Purpose**

Private `test` helper for session; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `_Session`.
- Every observed return expression is reproduced without truncation:
```python
_Session(responses=responses)

_Session(_Response(payload if payload is not None else _zip_bytes(), url=archive_url, status_code=status_code))
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `responses`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_inpn_protected_areas_fr.py::_download` via `_session`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_download_cache_setup_failure_is_controlled` via `_session`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_valid_zip_download_binds_exact_bytes_and_lineage` via `_session`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_cold_download_must_match_configured_snapshot_before_publication` via `_session`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_http_and_payload_failures_are_controlled` via `_session`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_unsupported_zip_compression_has_controlled_error` via `_session`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_invalid_download_cache_is_a_miss` via `_session`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_successful_first_and_replacement_publication` via `_session`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_publication_failure_restores_old_pair` via `_session`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_rollback_failure_preserves_recovery_material` via `_session`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_failed_replacement_restores_a_still_reusable_valid_download_pair` via `_session`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_unsafe_zip_member_paths_are_rejected` via `_session`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_duplicate_or_colliding_zip_destinations_are_rejected` via `_session`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_zip_links_and_special_files_are_rejected` via `_session`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_complete_zip_inventory_is_validated_before_member_copy` via `_session`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_strict_metadata_rejects_boolean_numeric_values_as_cache_hits` via `_session`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_download_uses_no_hidden_reference_page_scrape` via `_session`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_download`

**Exact signature**

```python
def _download(
    tmp_path: Path,
    *,
    payload: bytes | None = None,
) -> tuple[
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasDownload,
    _Session,
]:
```

**Purpose**

Acquires, verifies, and records download; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `tuple[InpnProtectedAreasSourceConfig, InpnProtectedAreasDownload, _Session]`.
- Every observed return expression is reproduced without truncation:
```python
(config, result, session)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: `_download_with_session`.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_coordinated_cache_and_metadata_snapshot_change_is_not_a_cache_hit` via `_download`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_valid_physical_and_metadata_cache_is_reused` via `_download`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_invalid_download_cache_is_a_miss` via `_download`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_successful_first_and_replacement_publication` via `_download`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_publication_failure_restores_old_pair` via `_download`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_rollback_failure_preserves_recovery_material` via `_download`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_failed_replacement_restores_a_still_reusable_valid_download_pair` via `_download`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_validates_complete_inventory_before_copying` via `_download`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_normal_nested_members_are_accepted` via `_download`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_inventory_is_complete_ordered_and_hashed` via `_download`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_valid_extraction_cache_is_reused` via `_download`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_invalid_extraction_cache_is_rebuilt` via `_download`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_first_extraction_publication_failure_leaves_no_half_root` via `_download`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_replacement_failure_restores_old_tree` via `_download`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_rollback_failure_preserves_backup` via `_download`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_backup_move_failure_leaves_old_tree_untouched` via `_download`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_rejects_wrong_config_type` via `_download`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_cache_setup_failure_is_controlled` via `_download`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_rejects_stale_download_bytes` via `_download`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_result_dataclasses_are_frozen` via `_download`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_strict_metadata_rejects_boolean_numeric_values_as_cache_hits` via `_download`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_cache_path_binds_version_and_filename` via `_download`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_exact_file_inventory_does_not_omit_unknown_suffixes` via `_download`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_archive_and_extraction_cache_reuse_are_independent` via `_download`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_no_stale_parts_after_download_or_extraction_success` via `_download`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_download_with_session`

**Exact signature**

```python
def _download_with_session(
    config: InpnProtectedAreasSourceConfig,
    session: _Session,
    *,
    timeout_seconds: float = 120.0,
) -> InpnProtectedAreasDownload:
```

**Purpose**

Acquires, verifies, and records with session; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `InpnProtectedAreasDownload`.
- Every observed return expression is reproduced without truncation:
```python
download_inpn_protected_areas_archive(config, timeout_seconds=timeout_seconds)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: `download_inpn_protected_areas_archive`.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `download_inpn_protected_areas_archive`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_inpn_protected_areas_fr.py::_download` via `_download_with_session`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_download_cache_setup_failure_is_controlled` via `_download_with_session`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_valid_zip_download_binds_exact_bytes_and_lineage` via `_download_with_session`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_cold_download_must_match_configured_snapshot_before_publication` via `_download_with_session`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_coordinated_cache_and_metadata_snapshot_change_is_not_a_cache_hit` via `_download_with_session`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_http_and_payload_failures_are_controlled` via `_download_with_session`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_unsupported_zip_compression_has_controlled_error` via `_download_with_session`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_malformed_response_headers_have_controlled_error` via `_download_with_session`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_midstream_protocol_failure_has_controlled_error` via `_download_with_session`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_invalid_download_cache_is_a_miss` via `_download_with_session`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_successful_first_and_replacement_publication` via `_download_with_session`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_publication_failure_restores_old_pair` via `_download_with_session`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_rollback_failure_preserves_recovery_material` via `_download_with_session`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_failed_replacement_restores_a_still_reusable_valid_download_pair` via `_download_with_session`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_unsafe_zip_member_paths_are_rejected` via `_download_with_session`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_duplicate_or_colliding_zip_destinations_are_rejected` via `_download_with_session`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_zip_links_and_special_files_are_rejected` via `_download_with_session`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_complete_zip_inventory_is_validated_before_member_copy` via `_download_with_session`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_strict_metadata_rejects_boolean_numeric_values_as_cache_hits` via `_download_with_session`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_download_uses_no_hidden_reference_page_scrape` via `_download_with_session`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_archive_and_extraction_cache_reuse_are_independent` via `_download_with_session`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_download_metadata_path`

**Exact signature**

```python
def _download_metadata_path(download: InpnProtectedAreasDownload) -> Path:
```

**Purpose**

Acquires, verifies, and records metadata path; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `Path`.
- Every observed return expression is reproduced without truncation:
```python
download.path.with_name(f'{download.filename}.metadata.json')
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_valid_zip_download_binds_exact_bytes_and_lineage` via `_download_metadata_path`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_coordinated_cache_and_metadata_snapshot_change_is_not_a_cache_hit` via `_download_metadata_path`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_invalid_download_cache_is_a_miss` via `_download_metadata_path`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::_force_cache_miss` via `_download_metadata_path`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_successful_first_and_replacement_publication` via `_download_metadata_path`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_rollback_failure_preserves_recovery_material` via `_download_metadata_path`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_failed_replacement_restores_a_still_reusable_valid_download_pair` via `_download_metadata_path`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_strict_metadata_rejects_boolean_numeric_values_as_cache_hits` via `_download_metadata_path`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_cache_path_binds_version_and_filename` via `_download_metadata_path`.

**Complete source-ordered implementation**

```python
def _download_metadata_path(download: InpnProtectedAreasDownload) -> Path:
    return download.path.with_name(f"{download.filename}.metadata.json")
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_extraction_metadata_path`

**Exact signature**

```python
def _extraction_metadata_path(extraction: InpnProtectedAreasExtraction) -> Path:
```

**Purpose**

Private `test` helper for extraction metadata path; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `Path`.
- Every observed return expression is reproduced without truncation:
```python
candidates[0]
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: `extraction.extraction_path.iterdir`, `path.is_file`.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_inventory_is_complete_ordered_and_hashed` via `_extraction_metadata_path`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_invalid_extraction_cache_is_rebuilt` via `_extraction_metadata_path`.

**Complete source-ordered implementation**

```python
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
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_read_json`

**Exact signature**

```python
def _read_json(path: Path) -> dict[str, object]:
```

**Purpose**

Reads json; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `dict[str, object]`.
- Every observed return expression is reproduced without truncation:
```python
payload
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: `path.read_text`.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_valid_zip_download_binds_exact_bytes_and_lineage` via `_read_json`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_coordinated_cache_and_metadata_snapshot_change_is_not_a_cache_hit` via `_read_json`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_invalid_download_cache_is_a_miss` via `_read_json`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::_force_cache_miss` via `_read_json`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_successful_first_and_replacement_publication` via `_read_json`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_inventory_is_complete_ordered_and_hashed` via `_read_json`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_invalid_extraction_cache_is_rebuilt` via `_read_json`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_strict_metadata_rejects_boolean_numeric_values_as_cache_hits` via `_read_json`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_cache_path_binds_version_and_filename` via `_read_json`.

**Complete source-ordered implementation**

```python
def _read_json(path: Path) -> dict[str, object]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(payload, dict)
    return payload
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_write_json`

**Exact signature**

```python
def _write_json(path: Path, payload: dict[str, object]) -> None:
```

**Purpose**

Serializes json; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: `path.write_text`.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_coordinated_cache_and_metadata_snapshot_change_is_not_a_cache_hit` via `_write_json`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_invalid_download_cache_is_a_miss` via `_write_json`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::_force_cache_miss` via `_write_json`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_invalid_extraction_cache_is_rebuilt` via `_write_json`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_strict_metadata_rejects_boolean_numeric_values_as_cache_hits` via `_write_json`.

**Complete source-ordered implementation**

```python
def _write_json(path: Path, payload: dict[str, object]) -> None:
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_checked_in_config_loads_with_exact_source_identity`

**Purpose**

Exercises `checked in config loads with exact source identity`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
config = load_inpn_protected_areas_source_config()
```

**Expected result**

```python
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
```

**Regression protected**

Locks `checked in config loads with exact source identity` through the exact asserted conditions: `type(config) is InpnProtectedAreasSourceConfig`; `config.provider == 'PatriNat'`; `config.authority == 'MNHN'`; `config.program == 'INPN'`; plus 8 additional reproduced assertion(s).

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
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
```

### `test_config_rejects_invalid_expected_snapshot_integrity`

**Purpose**

Exercises `config rejects invalid expected snapshot integrity`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `field`, `value`.

**Setup**

```python
payload = _config_payload()
payload[field] = value
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises((TypeError, ValueError)):
        InpnProtectedAreasSourceConfig.model_validate(payload)
```

**Regression protected**

Locks `config rejects invalid expected snapshot integrity`: the reproduced adversarial input must raise `(TypeError, ValueError)` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_config_rejects_invalid_expected_snapshot_integrity(
    field: str,
    value: object,
) -> None:
    payload = _config_payload()
    payload[field] = value

    with pytest.raises((TypeError, ValueError)):
        InpnProtectedAreasSourceConfig.model_validate(payload)
```

### `test_config_rejects_noncanonical_values`

**Purpose**

Exercises `config rejects noncanonical values`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `mutation`.

**Setup**

```python
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
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(InpnProtectedAreasSourceError):
        load_inpn_protected_areas_source_config(_write_config(tmp_path, payload))
```

**Regression protected**

Locks `config rejects noncanonical values`: the reproduced adversarial input must raise `InpnProtectedAreasSourceError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
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
```

### `test_wrong_download_config_type_has_controlled_error`

**Purpose**

Exercises `wrong download config type has controlled error`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(InpnProtectedAreasSourceError, match="config|type"):
        download_inpn_protected_areas_archive(object())
```

**Regression protected**

Locks `wrong download config type has controlled error`: the reproduced adversarial input must raise `InpnProtectedAreasSourceError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_wrong_download_config_type_has_controlled_error() -> None:
    with pytest.raises(InpnProtectedAreasSourceError, match="config|type"):
        download_inpn_protected_areas_archive(object())
```

### `test_download_timeout_is_strict_finite_positive`

**Purpose**

Exercises `download timeout is strict finite positive`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `timeout`.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(InpnProtectedAreasSourceError, match="timeout"):
        download_inpn_protected_areas_archive(
            load_inpn_protected_areas_source_config(),
            timeout_seconds=timeout,  # type: ignore[arg-type]
        )
```

**Regression protected**

Locks `download timeout is strict finite positive`: the reproduced adversarial input must raise `InpnProtectedAreasSourceError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_download_timeout_is_strict_finite_positive(timeout: object) -> None:
    with pytest.raises(InpnProtectedAreasSourceError, match="timeout"):
        download_inpn_protected_areas_archive(
            load_inpn_protected_areas_source_config(),
            timeout_seconds=timeout,  # type: ignore[arg-type]
        )
```

### `test_download_api_has_no_arbitrary_http_session_injection`

**Purpose**

Exercises `download api has no arbitrary http session injection`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert "session" not in inspect.signature(
        download_inpn_protected_areas_archive
    ).parameters
```

**Regression protected**

Locks `download api has no arbitrary http session injection` through the exact asserted conditions: `'session' not in inspect.signature(download_inpn_protected_areas_archive).parameters`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_download_api_has_no_arbitrary_http_session_injection() -> None:
    assert "session" not in inspect.signature(
        download_inpn_protected_areas_archive
    ).parameters
```

### `test_download_cache_setup_failure_is_controlled`

**Purpose**

Exercises `download cache setup failure is controlled`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
cache_file = tmp_path / "cache-is-a-file"
cache_file.write_bytes(b"not a directory")
payload = _config_payload()
payload["cache_root"] = str(cache_file)
config = InpnProtectedAreasSourceConfig.model_validate(payload)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(InpnProtectedAreasSourceError, match="download|cache"):
        _download_with_session(config, _session(config))
```

**Regression protected**

Locks `download cache setup failure is controlled`: the reproduced adversarial input must raise `InpnProtectedAreasSourceError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_download_cache_setup_failure_is_controlled(tmp_path: Path) -> None:
    cache_file = tmp_path / "cache-is-a-file"
    cache_file.write_bytes(b"not a directory")
    payload = _config_payload()
    payload["cache_root"] = str(cache_file)
    config = InpnProtectedAreasSourceConfig.model_validate(payload)

    with pytest.raises(InpnProtectedAreasSourceError, match="download|cache"):
        _download_with_session(config, _session(config))
```

### `test_valid_zip_download_binds_exact_bytes_and_lineage`

**Purpose**

Exercises `valid zip download binds exact bytes and lineage`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
payload = _zip_bytes(
        {
            "EP/data/areas.shp": b"shape",
            "EP/data/areas.dbf": b"table",
        }
    )
config = _config(tmp_path, payload)
session = _session(config, payload)
result = _download_with_session(config, session)
timestamp = datetime.fromisoformat(result.download_timestamp)
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
requested_url, request_options = session.calls[0]
metadata = _read_json(_download_metadata_path(result))
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert result.cache_hit is False
assert result.path.read_bytes() == payload
assert result.file_size == len(payload)
assert result.sha256 == sha256(payload).hexdigest()
assert len(result.sha256) == 64 and result.sha256 == result.sha256.lower()
assert timestamp.tzinfo is not None
assert timestamp.utcoffset() is not None
assert timestamp.utcoffset().total_seconds() == 0
assert result.filename == config.archive_filename == "EP.zip"
assert len(session.calls) == 1
assert requested_url == str(config.archive_url)
assert request_options["timeout"] == pytest.approx(120.0)
assert metadata["schema_version"] == 1
assert metadata["file_size"] == len(payload)
assert metadata["sha256"] == result.sha256
```

**Regression protected**

Pins verified cache reuse and ensures the successful local path avoids the external operation asserted by the test.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
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
```

### `test_cold_download_must_match_configured_snapshot_before_publication`

**Purpose**

Exercises `cold download must match configured snapshot before publication`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `mismatch`.

**Setup**

```python
expected = _zip_bytes()
if mismatch == "size":
        downloaded = _zip_bytes({"EP/other.txt": b"a longer protected-area payload"})
        assert len(downloaded) != len(expected)
    else:
        downloaded = _zip_bytes({"EP/readme.txt": b"protected areaz"})
        assert len(downloaded) == len(expected)
        assert sha256(downloaded).digest() != sha256(expected).digest()
config = _config(tmp_path, expected)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(InpnProtectedAreasSourceError, match="size|SHA|snapshot|integrity"):
        _download_with_session(config, _session(config, downloaded))
assert not list(Path(config.cache_root).rglob("EP.zip"))
assert not list(Path(config.cache_root).rglob("*.metadata.json"))
```

**Regression protected**

Locks `cold download must match configured snapshot before publication`: the reproduced adversarial input must raise `InpnProtectedAreasSourceError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
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
```

### `test_coordinated_cache_and_metadata_snapshot_change_is_not_a_cache_hit`

**Purpose**

Exercises `coordinated cache and metadata snapshot change is not a cache hit`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
config, first, _ = _download(tmp_path)
replacement = _zip_bytes({"EP/readme.txt": b"protected areaz"})
first.path.write_bytes(replacement)
metadata_path = _download_metadata_path(first)
metadata = _read_json(metadata_path)
metadata["file_size"] = len(replacement)
metadata["sha256"] = sha256(replacement).hexdigest()
_write_json(metadata_path, metadata)
```

**Action**

```python
no_network = _Session(error=SafeHttpsError("configured snapshot requires refresh"))
```

**Expected result**

```python
assert len(replacement) == first.file_size
with pytest.raises(InpnProtectedAreasSourceError):
        _download_with_session(config, no_network)
assert len(no_network.calls) == 1
```

**Regression protected**

Pins verified cache reuse and ensures the successful local path avoids the external operation asserted by the test.

**Test boundary**

- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
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
```

### `test_http_and_payload_failures_are_controlled`

**Purpose**

Exercises `http and payload failures are controlled`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `error`, `payload`, `status`.

**Setup**

```python
config = _config(tmp_path)
session = (
        _Session(error=error)
        if error is not None
        else _session(config, payload, status_code=status)
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(InpnProtectedAreasSourceError):
        _download_with_session(config, session)
assert not list(Path(config.cache_root).rglob("*.part"))
```

**Regression protected**

Locks `http and payload failures are controlled`: the reproduced adversarial input must raise `InpnProtectedAreasSourceError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
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
```

### `test_unsupported_zip_compression_has_controlled_error`

**Purpose**

Exercises `unsupported zip compression has controlled error`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
payload = _unsupported_compression_zip()
config = _config(tmp_path, payload)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(InpnProtectedAreasSourceError, match="ZIP|archive"):
        _download_with_session(config, _session(config, payload))
```

**Regression protected**

Locks `unsupported zip compression has controlled error`: the reproduced adversarial input must raise `InpnProtectedAreasSourceError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_unsupported_zip_compression_has_controlled_error(tmp_path: Path) -> None:
    payload = _unsupported_compression_zip()
    config = _config(tmp_path, payload)

    with pytest.raises(InpnProtectedAreasSourceError, match="ZIP|archive"):
        _download_with_session(config, _session(config, payload))
```

### `test_malformed_response_headers_have_controlled_error`

**Purpose**

Exercises `malformed response headers have controlled error`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
config = _config(tmp_path)
response = _Response(_zip_bytes(), url=str(config.archive_url))
response.headers = None
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(InpnProtectedAreasSourceError, match="response|download"):
        _download_with_session(config, _Session(response))
```

**Regression protected**

Locks `malformed response headers have controlled error`: the reproduced adversarial input must raise `InpnProtectedAreasSourceError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_malformed_response_headers_have_controlled_error(tmp_path: Path) -> None:
    config = _config(tmp_path)
    response = _Response(_zip_bytes(), url=str(config.archive_url))
    response.headers = None  # type: ignore[assignment]

    with pytest.raises(InpnProtectedAreasSourceError, match="response|download"):
        _download_with_session(config, _Session(response))
```

### `test_midstream_protocol_failure_has_controlled_error`

**Purpose**

Exercises `midstream protocol failure has controlled error`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
class _FailingRaw:
        decode_content = False

        def seek(self, offset: int) -> int:
            return offset

        def read(self, size: int = -1) -> bytes:
            raise OSError("connection ended mid-stream")
config = _config(tmp_path)
response = _Response(_zip_bytes(), url=str(config.archive_url))
response.raw = _FailingRaw()
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(InpnProtectedAreasSourceError, match="response|download"):
        _download_with_session(config, _Session(response))
```

**Regression protected**

Locks `midstream protocol failure has controlled error`: the reproduced adversarial input must raise `InpnProtectedAreasSourceError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
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
```

### `test_midstream_protocol_failure_has_controlled_error._FailingRaw.seek`

**Exact signature**

```python
def seek(self, offset: int) -> int:
```

**Purpose**

Private `test` helper for seek; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `int`.
- Every observed return expression is reproduced without truncation:
```python
offset
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

**Complete source-ordered implementation**

```python
def seek(self, offset: int) -> int:
            return offset
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_midstream_protocol_failure_has_controlled_error._FailingRaw.read`

**Exact signature**

```python
def read(self, size: int = -1) -> bytes:
```

**Purpose**

Reads read; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `bytes`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `OSError('connection ended mid-stream')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

**Complete source-ordered implementation**

```python
def read(self, size: int = -1) -> bytes:
            raise OSError("connection ended mid-stream")
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_valid_physical_and_metadata_cache_is_reused`

**Purpose**

Exercises `valid physical and metadata cache is reused`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
config, first, _ = _download(tmp_path)
def fail_dns(*args: object, **kwargs: object) -> list[tuple[Any, ...]]:
        raise AssertionError("DNS used for valid cache hit")
def fail_http(*args: object, **kwargs: object) -> Any:
        raise AssertionError("HTTP used for valid cache hit")
monkeypatch.setattr(safe_http.socket, "getaddrinfo", fail_dns)
monkeypatch.setattr(inpn, "open_safe_https", fail_http)
```

**Action**

```python
second = download_inpn_protected_areas_archive(config)
```

**Expected result**

```python
assert second.cache_hit is True
assert second.file_size == first.file_size
assert second.sha256 == first.sha256
```

**Regression protected**

Pins verified cache reuse and ensures the successful local path avoids the external operation asserted by the test.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
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
```

### `test_valid_physical_and_metadata_cache_is_reused.fail_dns`

**Exact signature**

```python
def fail_dns(*args: object, **kwargs: object) -> list[tuple[Any, ...]]:
```

**Purpose**

Private `test` helper for fail dns; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `list[tuple[Any, ...]]`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `AssertionError('DNS used for valid cache hit')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- function object argument: `tests/unit/test_inpn_protected_areas_fr.py::test_valid_physical_and_metadata_cache_is_reused` via `monkeypatch.setattr(safe_http.socket, 'getaddrinfo', fail_dns)`.

**Complete source-ordered implementation**

```python
def fail_dns(*args: object, **kwargs: object) -> list[tuple[Any, ...]]:
        raise AssertionError("DNS used for valid cache hit")
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_valid_physical_and_metadata_cache_is_reused.fail_http`

**Exact signature**

```python
def fail_http(*args: object, **kwargs: object) -> Any:
```

**Purpose**

Private `test` helper for fail http; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `Any`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `AssertionError('HTTP used for valid cache hit')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- function object argument: `tests/unit/test_inpn_protected_areas_fr.py::test_valid_physical_and_metadata_cache_is_reused` via `monkeypatch.setattr(inpn, 'open_safe_https', fail_http)`.

**Complete source-ordered implementation**

```python
def fail_http(*args: object, **kwargs: object) -> Any:
        raise AssertionError("HTTP used for valid cache hit")
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_invalid_download_cache_is_a_miss`

**Purpose**

Exercises `invalid download cache is a miss`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `mutation`.

**Setup**

```python
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
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert refreshed.cache_hit is False
assert len(session.calls) == 1
```

**Regression protected**

Prevents coordinated metadata/content mutation from being accepted without agreement with the authoritative byte or result envelope.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
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
```

### `_force_cache_miss`

**Exact signature**

```python
def _force_cache_miss(download: InpnProtectedAreasDownload) -> tuple[Path, bytes]:
```

**Purpose**

Private `test` helper for force cache miss; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[Path, bytes]`.
- Every observed return expression is reproduced without truncation:
```python
(metadata_path, metadata_path.read_bytes())
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: `_download_metadata_path`.
- Filesystem read: `metadata_path.read_bytes`.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `metadata['sha256']`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_successful_first_and_replacement_publication` via `_force_cache_miss`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_publication_failure_restores_old_pair` via `_force_cache_miss`.

**Complete source-ordered implementation**

```python
def _force_cache_miss(download: InpnProtectedAreasDownload) -> tuple[Path, bytes]:
    metadata_path = _download_metadata_path(download)
    metadata = _read_json(metadata_path)
    metadata["sha256"] = "0" * 64
    _write_json(metadata_path, metadata)
    return metadata_path, metadata_path.read_bytes()
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_successful_first_and_replacement_publication`

**Purpose**

Exercises `successful first and replacement publication`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
config, first, _ = _download(tmp_path)
_force_cache_miss(first)
replacement = _zip_bytes()
second = _download_with_session(config, _session(config, replacement))
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert second.cache_hit is False
assert second.path.read_bytes() == replacement
assert _read_json(_download_metadata_path(second))["sha256"] == second.sha256
assert not list(Path(config.cache_root).rglob("*.part"))
```

**Regression protected**

Pins verified cache reuse and ensures the successful local path avoids the external operation asserted by the test.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_successful_first_and_replacement_publication(tmp_path: Path) -> None:
    config, first, _ = _download(tmp_path)
    _force_cache_miss(first)
    replacement = _zip_bytes()

    second = _download_with_session(config, _session(config, replacement))

    assert second.cache_hit is False
    assert second.path.read_bytes() == replacement
    assert _read_json(_download_metadata_path(second))["sha256"] == second.sha256
    assert not list(Path(config.cache_root).rglob("*.part"))
```

### `test_publication_failure_restores_old_pair`

**Purpose**

Exercises `publication failure restores old pair`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `failure_target`.

**Setup**

```python
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
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(InpnProtectedAreasSourceError, match="publication|download"):
        _download_with_session(config, _session(config))
assert first.path.read_bytes() == old_archive
assert metadata_path.read_bytes() == old_metadata
assert not list(Path(config.cache_root).rglob("*.part"))
assert not list(Path(config.cache_root).rglob("*.bak"))
```

**Regression protected**

Locks `publication failure restores old pair`: the reproduced adversarial input must raise `InpnProtectedAreasSourceError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
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
```

### `test_publication_failure_restores_old_pair.fail_once`

**Exact signature**

```python
def fail_once(source: Path, target: Path) -> None:
```

**Purpose**

Private `test` helper for fail once; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `source.name.endswith('.part') and target == wanted and (not failed)`.
- Explicit raise expressions: `OSError('publication failed')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- function object argument: `tests/unit/test_inpn_protected_areas_fr.py::test_publication_failure_restores_old_pair` via `monkeypatch.setattr(inpn, '_replace_file', fail_once)`.

**Complete source-ordered implementation**

```python
def fail_once(source: Path, target: Path) -> None:
        nonlocal failed
        wanted = first.path if failure_target == "archive" else metadata_path
        if source.name.endswith(".part") and target == wanted and not failed:
            failed = True
            raise OSError("publication failed")
        original_replace(source, target)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_rollback_failure_preserves_recovery_material`

**Purpose**

Exercises `rollback failure preserves recovery material`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
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
archive_backup = first.path.with_name(f"{first.path.name}.bak")
metadata_backup = metadata_path.with_name(f"{metadata_path.name}.bak")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(InpnProtectedAreasSourceError, match="rollback"):
        _download_with_session(config, _session(config))
assert archive_backup.read_bytes() == old_archive
assert metadata_backup.read_bytes() == old_metadata
```

**Regression protected**

Prevents cache publication/rollback failures from destroying the last recoverable bytes; the exact old archive/metadata or extraction tree asserted below must survive in recovery material.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
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
```

### `test_rollback_failure_preserves_recovery_material.fail_publication_and_rollback`

**Exact signature**

```python
def fail_publication_and_rollback(source: Path, target: Path) -> None:
```

**Purpose**

Private `test` helper for fail publication and rollback; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `source.name.endswith('.part') and target == metadata_path`.
- Guard with a raise path: `source.name.endswith('.bak')`.
- Explicit raise expressions: `OSError('publication failed')`, `OSError('rollback failed')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- function object argument: `tests/unit/test_inpn_protected_areas_fr.py::test_rollback_failure_preserves_recovery_material` via `monkeypatch.setattr(inpn, '_replace_file', fail_publication_and_rollback)`.

**Complete source-ordered implementation**

```python
def fail_publication_and_rollback(source: Path, target: Path) -> None:
        if source.name.endswith(".part") and target == metadata_path:
            raise OSError("publication failed")
        if source.name.endswith(".bak"):
            raise OSError("rollback failed")
        original_replace(source, target)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_broken_download_recovery_symlink_is_rejected`

**Purpose**

Exercises `broken download recovery symlink is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `backup_role`.

**Setup**

```python
archive_path = tmp_path / "EP.zip"
metadata_path = tmp_path / "EP.zip.metadata.json"
temporary_archive = tmp_path / "EP.zip.part"
temporary_metadata = tmp_path / "EP.zip.metadata.json.part"
temporary_archive.write_bytes(b"replacement archive")
temporary_metadata.write_bytes(b"replacement metadata")
recovery_paths = {
        "archive": archive_path.with_name(f"{archive_path.name}.bak"),
        "metadata": metadata_path.with_name(f"{metadata_path.name}.bak"),
    }
broken_link = recovery_paths[backup_role]
original_is_symlink = Path.is_symlink
def simulated_is_symlink(path: Path) -> bool:
        return path == broken_link or original_is_symlink(path)
monkeypatch.setattr(Path, "is_symlink", simulated_is_symlink)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(InpnProtectedAreasSourceError, match="backup|recovery|manual"):
        inpn._publish_cache_pair(
            temporary_archive,
            temporary_metadata,
            archive_path,
            metadata_path,
        )
assert not archive_path.exists()
assert not metadata_path.exists()
assert temporary_archive.read_bytes() == b"replacement archive"
assert temporary_metadata.read_bytes() == b"replacement metadata"
```

**Regression protected**

Locks `broken download recovery symlink is rejected`: the reproduced adversarial input must raise `InpnProtectedAreasSourceError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_broken_download_recovery_symlink_is_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    backup_role: str,
) -> None:
    archive_path = tmp_path / "EP.zip"
    metadata_path = tmp_path / "EP.zip.metadata.json"
    temporary_archive = tmp_path / "EP.zip.part"
    temporary_metadata = tmp_path / "EP.zip.metadata.json.part"
    temporary_archive.write_bytes(b"replacement archive")
    temporary_metadata.write_bytes(b"replacement metadata")
    recovery_paths = {
        "archive": archive_path.with_name(f"{archive_path.name}.bak"),
        "metadata": metadata_path.with_name(f"{metadata_path.name}.bak"),
    }
    broken_link = recovery_paths[backup_role]
    original_is_symlink = Path.is_symlink

    def simulated_is_symlink(path: Path) -> bool:
        return path == broken_link or original_is_symlink(path)

    monkeypatch.setattr(Path, "is_symlink", simulated_is_symlink)

    with pytest.raises(InpnProtectedAreasSourceError, match="backup|recovery|manual"):
        inpn._publish_cache_pair(
            temporary_archive,
            temporary_metadata,
            archive_path,
            metadata_path,
        )

    assert not archive_path.exists()
    assert not metadata_path.exists()
    assert temporary_archive.read_bytes() == b"replacement archive"
    assert temporary_metadata.read_bytes() == b"replacement metadata"
```

### `test_broken_download_recovery_symlink_is_rejected.simulated_is_symlink`

**Exact signature**

```python
def simulated_is_symlink(path: Path) -> bool:
```

**Purpose**

Private `test` helper for simulated is symlink; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `bool`.
- Every observed return expression is reproduced without truncation:
```python
path == broken_link or original_is_symlink(path)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- function object argument: `tests/unit/test_inpn_protected_areas_fr.py::test_broken_download_recovery_symlink_is_rejected` via `monkeypatch.setattr(Path, 'is_symlink', simulated_is_symlink)`.

**Complete source-ordered implementation**

```python
def simulated_is_symlink(path: Path) -> bool:
        return path == broken_link or original_is_symlink(path)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_existing_normal_download_recovery_backup_remains_unchanged`

**Purpose**

Exercises `existing normal download recovery backup remains unchanged`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
archive_path = tmp_path / "EP.zip"
metadata_path = tmp_path / "EP.zip.metadata.json"
temporary_archive = tmp_path / "EP.zip.part"
temporary_metadata = tmp_path / "EP.zip.metadata.json.part"
archive_backup = archive_path.with_name(f"{archive_path.name}.bak")
recovery_bytes = b"manual INPN recovery archive"
temporary_archive.write_bytes(b"replacement archive")
temporary_metadata.write_bytes(b"replacement metadata")
archive_backup.write_bytes(recovery_bytes)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(InpnProtectedAreasSourceError, match="backup|recovery|manual"):
        inpn._publish_cache_pair(
            temporary_archive,
            temporary_metadata,
            archive_path,
            metadata_path,
        )
assert archive_backup.read_bytes() == recovery_bytes
assert temporary_archive.read_bytes() == b"replacement archive"
assert temporary_metadata.read_bytes() == b"replacement metadata"
```

**Regression protected**

Locks `existing normal download recovery backup remains unchanged`: the reproduced adversarial input must raise `InpnProtectedAreasSourceError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_existing_normal_download_recovery_backup_remains_unchanged(
    tmp_path: Path,
) -> None:
    archive_path = tmp_path / "EP.zip"
    metadata_path = tmp_path / "EP.zip.metadata.json"
    temporary_archive = tmp_path / "EP.zip.part"
    temporary_metadata = tmp_path / "EP.zip.metadata.json.part"
    archive_backup = archive_path.with_name(f"{archive_path.name}.bak")
    recovery_bytes = b"manual INPN recovery archive"
    temporary_archive.write_bytes(b"replacement archive")
    temporary_metadata.write_bytes(b"replacement metadata")
    archive_backup.write_bytes(recovery_bytes)

    with pytest.raises(InpnProtectedAreasSourceError, match="backup|recovery|manual"):
        inpn._publish_cache_pair(
            temporary_archive,
            temporary_metadata,
            archive_path,
            metadata_path,
        )

    assert archive_backup.read_bytes() == recovery_bytes
    assert temporary_archive.read_bytes() == b"replacement archive"
    assert temporary_metadata.read_bytes() == b"replacement metadata"
```

### `test_failed_replacement_restores_a_still_reusable_valid_download_pair`

**Purpose**

Exercises `failed replacement restores a still reusable valid download pair`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
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
monkeypatch.setattr(inpn, "_load_cached_download", original_load)
monkeypatch.setattr(inpn, "_replace_file", original_replace)
reused = _download_with_session(
        config,
        _Session(error=AssertionError("network used")),
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(InpnProtectedAreasSourceError, match="publication"):
        _download_with_session(config, _session(config))
assert first.path.read_bytes() == old_archive
assert metadata_path.read_bytes() == old_metadata
assert reused.cache_hit is True
```

**Regression protected**

Pins verified cache reuse and ensures the successful local path avoids the external operation asserted by the test.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
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
```

### `test_failed_replacement_restores_a_still_reusable_valid_download_pair.fail_metadata`

**Exact signature**

```python
def fail_metadata(source: Path, target: Path) -> None:
```

**Purpose**

Private `test` helper for fail metadata; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `source.name.endswith('.part') and target == metadata_path`.
- Explicit raise expressions: `OSError('publication failed')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- function object argument: `tests/unit/test_inpn_protected_areas_fr.py::test_failed_replacement_restores_a_still_reusable_valid_download_pair` via `monkeypatch.setattr(inpn, '_replace_file', fail_metadata)`.

**Complete source-ordered implementation**

```python
def fail_metadata(source: Path, target: Path) -> None:
        if source.name.endswith(".part") and target == metadata_path:
            raise OSError("publication failed")
        original_replace(source, target)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unsafe_zip_member_paths_are_rejected`

**Purpose**

Exercises `unsafe zip member paths are rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `member_name`.

**Setup**

```python
payload = _zip_bytes([(member_name, b"bad")])
config = _config(tmp_path, payload)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(InpnProtectedAreasSourceError, match="ZIP|archive|member|path"):
        _download_with_session(config, _session(config, payload))
```

**Regression protected**

Locks `unsafe zip member paths are rejected`: the reproduced adversarial input must raise `InpnProtectedAreasSourceError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_unsafe_zip_member_paths_are_rejected(
    tmp_path: Path,
    member_name: str,
) -> None:
    payload = _zip_bytes([(member_name, b"bad")])
    config = _config(tmp_path, payload)
    with pytest.raises(InpnProtectedAreasSourceError, match="ZIP|archive|member|path"):
        _download_with_session(config, _session(config, payload))
```

### `test_duplicate_or_colliding_zip_destinations_are_rejected`

**Purpose**

Exercises `duplicate or colliding zip destinations are rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `members`.

**Setup**

```python
payload = _zip_bytes(members)
config = _config(tmp_path, payload)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(InpnProtectedAreasSourceError, match="duplicate|collid|archive"):
        _download_with_session(config, _session(config, payload))
```

**Regression protected**

Locks `duplicate or colliding zip destinations are rejected`: the reproduced adversarial input must raise `InpnProtectedAreasSourceError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_duplicate_or_colliding_zip_destinations_are_rejected(
    tmp_path: Path,
    members: list[tuple[str, bytes]],
) -> None:
    payload = _zip_bytes(members)
    config = _config(tmp_path, payload)
    with pytest.raises(InpnProtectedAreasSourceError, match="duplicate|collid|archive"):
        _download_with_session(config, _session(config, payload))
```

### `test_zip_links_and_special_files_are_rejected`

**Purpose**

Exercises `zip links and special files are rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `message`, `mode`.

**Setup**

```python
payload = _special_zip("unsafe", mode)
config = _config(tmp_path, payload)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(InpnProtectedAreasSourceError, match=message):
        _download_with_session(config, _session(config, payload))
```

**Regression protected**

Locks `zip links and special files are rejected`: the reproduced adversarial input must raise `InpnProtectedAreasSourceError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_zip_links_and_special_files_are_rejected(
    tmp_path: Path,
    mode: int,
    message: str,
) -> None:
    payload = _special_zip("unsafe", mode)
    config = _config(tmp_path, payload)
    with pytest.raises(InpnProtectedAreasSourceError, match=message):
        _download_with_session(config, _session(config, payload))
```

### `test_complete_zip_inventory_is_validated_before_member_copy`

**Purpose**

Exercises `complete zip inventory is validated before member copy`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
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
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(InpnProtectedAreasSourceError):
        _download_with_session(config, _session(config, payload))
assert opened == 0
```

**Regression protected**

Locks `complete zip inventory is validated before member copy`: the reproduced adversarial input must raise `InpnProtectedAreasSourceError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
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
```

### `test_complete_zip_inventory_is_validated_before_member_copy.record_open`

**Exact signature**

```python
def record_open(self: zipfile.ZipFile, *args: object, **kwargs: object) -> Any:
```

**Purpose**

Private `test` helper for record open; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `Any`.
- Every observed return expression is reproduced without truncation:
```python
original_open(self, *args, **kwargs)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- function object argument: `tests/unit/test_inpn_protected_areas_fr.py::test_complete_zip_inventory_is_validated_before_member_copy` via `monkeypatch.setattr(zipfile.ZipFile, 'open', record_open)`.

**Complete source-ordered implementation**

```python
def record_open(self: zipfile.ZipFile, *args: object, **kwargs: object) -> Any:
        nonlocal opened
        opened += 1
        return original_open(self, *args, **kwargs)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_extraction_validates_complete_inventory_before_copying`

**Purpose**

Exercises `extraction validates complete inventory before copying`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
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
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(InpnProtectedAreasSourceError):
        extract_inpn_protected_areas_archive(forged, config)
assert copied == 0
assert not (download.path.parent / "x" / forged.sha256).exists()
```

**Regression protected**

Locks `extraction validates complete inventory before copying`: the reproduced adversarial input must raise `InpnProtectedAreasSourceError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
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
```

### `test_extraction_validates_complete_inventory_before_copying.record_copy`

**Exact signature**

```python
def record_copy(*args: object, **kwargs: object) -> None:
```

**Purpose**

Private `test` helper for record copy; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- function object argument: `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_validates_complete_inventory_before_copying` via `monkeypatch.setattr(inpn, 'copyfileobj', record_copy)`.

**Complete source-ordered implementation**

```python
def record_copy(*args: object, **kwargs: object) -> None:
        nonlocal copied
        copied += 1
        original_copy(*args, **kwargs)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_normal_nested_members_are_accepted`

**Purpose**

Exercises `normal nested members are accepted`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
config, download, _ = _download(
        tmp_path,
        payload=_zip_bytes({"EP/docs/readme.txt": b"ok"}),
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert download.path.is_file()
assert download.filename == config.archive_filename
```

**Regression protected**

Locks `normal nested members are accepted` through the exact asserted conditions: `download.path.is_file()`; `download.filename == config.archive_filename`.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_normal_nested_members_are_accepted(tmp_path: Path) -> None:
    config, download, _ = _download(
        tmp_path,
        payload=_zip_bytes({"EP/docs/readme.txt": b"ok"}),
    )

    assert download.path.is_file()
    assert download.filename == config.archive_filename
```

### `test_extraction_inventory_is_complete_ordered_and_hashed`

**Purpose**

Exercises `extraction inventory is complete ordered and hashed`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
payloads = {
        "z-last/empty.cpg": b"",
        "EP/data/areas.shp": b"shape",
        "EP/data/areas.dbf": b"table",
        "EP/metadata.xml": b"<metadata/>",
    }
config, download, _ = _download(tmp_path, payload=_zip_bytes(payloads))
expected_paths = sorted(payloads)
by_path = {item.relative_path: item for item in extraction.files}
for relative_path, payload in payloads.items():
        item = by_path[relative_path]
        assert item.file_size == len(payload)
        assert item.sha256 == sha256(payload).hexdigest()
        assert (
            extraction.extraction_path.joinpath(*relative_path.split("/")).read_bytes()
            == payload
        )
metadata = _read_json(_extraction_metadata_path(extraction))
```

**Action**

```python
extraction = extract_inpn_protected_areas_archive(download, config)
```

**Expected result**

```python
assert extraction.cache_hit is False
assert [item.relative_path for item in extraction.files] == expected_paths
assert len(extraction.files) == len(payloads)
assert by_path["z-last/empty.cpg"].file_size == 0
assert by_path["z-last/empty.cpg"].sha256 == sha256(b"").hexdigest()
assert metadata["schema_version"] == 1
assert metadata["archive_sha256"] == download.sha256
assert metadata["archive_size"] == download.file_size
assert not list(extraction.extraction_path.parent.glob("*.part"))
```

**Regression protected**

Pins verified cache reuse and ensures the successful local path avoids the external operation asserted by the test.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
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
```

### `test_valid_extraction_cache_is_reused`

**Purpose**

Exercises `valid extraction cache is reused`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
config, download, _ = _download(tmp_path)
```

**Action**

```python
first = extract_inpn_protected_areas_archive(download, config)
second = extract_inpn_protected_areas_archive(download, config)
```

**Expected result**

```python
assert second.cache_hit is True
assert second.files == first.files
assert second.extraction_path == first.extraction_path
```

**Regression protected**

Pins verified cache reuse and ensures the successful local path avoids the external operation asserted by the test.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_valid_extraction_cache_is_reused(tmp_path: Path) -> None:
    config, download, _ = _download(tmp_path)
    first = extract_inpn_protected_areas_archive(download, config)

    second = extract_inpn_protected_areas_archive(download, config)

    assert second.cache_hit is True
    assert second.files == first.files
    assert second.extraction_path == first.extraction_path
```

### `test_invalid_extraction_cache_is_rebuilt`

**Purpose**

Exercises `invalid extraction cache is rebuilt`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `mutation`.

**Setup**

```python
original = b"original"
config, download, _ = _download(
        tmp_path,
        payload=_zip_bytes({"EP/value.txt": original}),
    )
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
```

**Action**

```python
first = extract_inpn_protected_areas_archive(download, config)
refreshed = extract_inpn_protected_areas_archive(download, config)
```

**Expected result**

```python
assert refreshed.cache_hit is False
assert (refreshed.extraction_path / "EP" / "value.txt").read_bytes() == original
assert not (refreshed.extraction_path / "unexpected.txt").exists()
```

**Regression protected**

Prevents coordinated metadata/content mutation from being accepted without agreement with the authoritative byte or result envelope.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
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
```

### `_tree_snapshot`

**Exact signature**

```python
def _tree_snapshot(root: Path) -> dict[str, bytes]:
```

**Purpose**

Private `test` helper for tree snapshot; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict[str, bytes]`.
- Every observed return expression is reproduced without truncation:
```python
{path.relative_to(root).as_posix(): path.read_bytes() for path in sorted(root.rglob('*')) if path.is_file()}
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: `path.is_file`, `path.read_bytes`, `root.rglob`.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_replacement_failure_restores_old_tree` via `_tree_snapshot`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_rollback_failure_preserves_backup` via `_tree_snapshot`.
- direct call: `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_backup_move_failure_leaves_old_tree_untouched` via `_tree_snapshot`.

**Complete source-ordered implementation**

```python
def _tree_snapshot(root: Path) -> dict[str, bytes]:
    return {
        path.relative_to(root).as_posix(): path.read_bytes()
        for path in sorted(root.rglob("*"))
        if path.is_file()
    }
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_first_extraction_publication_failure_leaves_no_half_root`

**Purpose**

Exercises `first extraction publication failure leaves no half root`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
config, download, _ = _download(tmp_path)
root = download.path.parent / "x" / download.sha256
original_replace = inpn._replace_directory
def fail_publish(source: Path, target: Path) -> None:
        if source.name.endswith(".part") and target == root:
            raise OSError("publication failed")
        original_replace(source, target)
monkeypatch.setattr(inpn, "_replace_directory", fail_publish)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(InpnProtectedAreasSourceError, match="publication"):
        extract_inpn_protected_areas_archive(download, config)
assert not root.exists()
assert not root.with_name(f"{root.name}.part").exists()
assert not root.with_name(f"{root.name}.bak").exists()
```

**Regression protected**

Locks `first extraction publication failure leaves no half root`: the reproduced adversarial input must raise `InpnProtectedAreasSourceError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
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
```

### `test_first_extraction_publication_failure_leaves_no_half_root.fail_publish`

**Exact signature**

```python
def fail_publish(source: Path, target: Path) -> None:
```

**Purpose**

Private `test` helper for fail publish; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `source.name.endswith('.part') and target == root`.
- Explicit raise expressions: `OSError('publication failed')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- function object argument: `tests/unit/test_inpn_protected_areas_fr.py::test_first_extraction_publication_failure_leaves_no_half_root` via `monkeypatch.setattr(inpn, '_replace_directory', fail_publish)`.

**Complete source-ordered implementation**

```python
def fail_publish(source: Path, target: Path) -> None:
        if source.name.endswith(".part") and target == root:
            raise OSError("publication failed")
        original_replace(source, target)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_extraction_replacement_failure_restores_old_tree`

**Purpose**

Exercises `extraction replacement failure restores old tree`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
config, download, _ = _download(tmp_path)
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
```

**Action**

```python
first = extract_inpn_protected_areas_archive(download, config)
```

**Expected result**

```python
with pytest.raises(InpnProtectedAreasSourceError, match="publication"):
        extract_inpn_protected_areas_archive(download, config)
assert _tree_snapshot(first.extraction_path) == before
assert not first.extraction_path.with_name(
        f"{first.extraction_path.name}.bak"
    ).exists()
```

**Regression protected**

Locks `extraction replacement failure restores old tree`: the reproduced adversarial input must raise `InpnProtectedAreasSourceError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
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
```

### `test_extraction_replacement_failure_restores_old_tree.fail_once`

**Exact signature**

```python
def fail_once(source: Path, target: Path) -> None:
```

**Purpose**

Private `test` helper for fail once; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `source.name.endswith('.part') and target == first.extraction_path and (not failed)`.
- Explicit raise expressions: `OSError('publication failed')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- function object argument: `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_replacement_failure_restores_old_tree` via `monkeypatch.setattr(inpn, '_replace_directory', fail_once)`.

**Complete source-ordered implementation**

```python
def fail_once(source: Path, target: Path) -> None:
        nonlocal failed
        if source.name.endswith(".part") and target == first.extraction_path and not failed:
            failed = True
            raise OSError("publication failed")
        original_replace(source, target)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_extraction_rollback_failure_preserves_backup`

**Purpose**

Exercises `extraction rollback failure preserves backup`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
config, download, _ = _download(tmp_path)
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
```

**Action**

```python
first = extract_inpn_protected_areas_archive(download, config)
```

**Expected result**

```python
with pytest.raises(InpnProtectedAreasSourceError, match="rollback"):
        extract_inpn_protected_areas_archive(download, config)
assert _tree_snapshot(backup) == before
assert not first.extraction_path.with_name(
        f"{first.extraction_path.name}.part"
    ).exists()
```

**Regression protected**

Prevents cache publication/rollback failures from destroying the last recoverable bytes; the exact old archive/metadata or extraction tree asserted below must survive in recovery material.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
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
```

### `test_extraction_rollback_failure_preserves_backup.fail_publish_and_rollback`

**Exact signature**

```python
def fail_publish_and_rollback(source: Path, target: Path) -> None:
```

**Purpose**

Private `test` helper for fail publish and rollback; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `source.name.endswith('.part') and target == first.extraction_path`.
- Guard with a raise path: `source == backup and target == first.extraction_path`.
- Explicit raise expressions: `OSError('publication failed')`, `OSError('rollback failed')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- function object argument: `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_rollback_failure_preserves_backup` via `monkeypatch.setattr(inpn, '_replace_directory', fail_publish_and_rollback)`.

**Complete source-ordered implementation**

```python
def fail_publish_and_rollback(source: Path, target: Path) -> None:
        if source.name.endswith(".part") and target == first.extraction_path:
            raise OSError("publication failed")
        if source == backup and target == first.extraction_path:
            raise OSError("rollback failed")
        original_replace(source, target)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_extraction_backup_move_failure_leaves_old_tree_untouched`

**Purpose**

Exercises `extraction backup move failure leaves old tree untouched`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
config, download, _ = _download(tmp_path)
(first.extraction_path / "EP" / "readme.txt").write_bytes(b"tampered")
before = _tree_snapshot(first.extraction_path)
backup = first.extraction_path.with_name(f"{first.extraction_path.name}.bak")
original_replace = inpn._replace_directory
def fail_backup_move(source: Path, target: Path) -> None:
        if source == first.extraction_path and target == backup:
            raise OSError("cannot stage old tree")
        original_replace(source, target)
monkeypatch.setattr(inpn, "_replace_directory", fail_backup_move)
```

**Action**

```python
first = extract_inpn_protected_areas_archive(download, config)
```

**Expected result**

```python
with pytest.raises(InpnProtectedAreasSourceError, match="publication|stage"):
        extract_inpn_protected_areas_archive(download, config)
assert first.extraction_path.is_dir()
assert _tree_snapshot(first.extraction_path) == before
assert not backup.exists()
```

**Regression protected**

Locks `extraction backup move failure leaves old tree untouched`: the reproduced adversarial input must raise `InpnProtectedAreasSourceError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
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
```

### `test_extraction_backup_move_failure_leaves_old_tree_untouched.fail_backup_move`

**Exact signature**

```python
def fail_backup_move(source: Path, target: Path) -> None:
```

**Purpose**

Private `test` helper for fail backup move; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `source == first.extraction_path and target == backup`.
- Explicit raise expressions: `OSError('cannot stage old tree')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- function object argument: `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_backup_move_failure_leaves_old_tree_untouched` via `monkeypatch.setattr(inpn, '_replace_directory', fail_backup_move)`.

**Complete source-ordered implementation**

```python
def fail_backup_move(source: Path, target: Path) -> None:
        if source == first.extraction_path and target == backup:
            raise OSError("cannot stage old tree")
        original_replace(source, target)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_extraction_rejects_wrong_download_type`

**Purpose**

Exercises `extraction rejects wrong download type`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `bad_input`.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(InpnProtectedAreasSourceError, match="download|type"):
        extract_inpn_protected_areas_archive(
            bad_input,  # type: ignore[arg-type]
            _config(tmp_path),
        )
```

**Regression protected**

Locks `extraction rejects wrong download type`: the reproduced adversarial input must raise `InpnProtectedAreasSourceError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_extraction_rejects_wrong_download_type(
    tmp_path: Path,
    bad_input: object,
) -> None:
    with pytest.raises(InpnProtectedAreasSourceError, match="download|type"):
        extract_inpn_protected_areas_archive(
            bad_input,  # type: ignore[arg-type]
            _config(tmp_path),
        )
```

### `test_extraction_rejects_wrong_config_type`

**Purpose**

Exercises `extraction rejects wrong config type`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
_, download, _ = _download(tmp_path)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(InpnProtectedAreasSourceError, match="config|type"):
        extract_inpn_protected_areas_archive(
            download,
            object(),  # type: ignore[arg-type]
        )
```

**Regression protected**

Locks `extraction rejects wrong config type`: the reproduced adversarial input must raise `InpnProtectedAreasSourceError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_extraction_rejects_wrong_config_type(tmp_path: Path) -> None:
    _, download, _ = _download(tmp_path)
    with pytest.raises(InpnProtectedAreasSourceError, match="config|type"):
        extract_inpn_protected_areas_archive(
            download,
            object(),  # type: ignore[arg-type]
        )
```

### `test_extraction_cache_setup_failure_is_controlled`

**Purpose**

Exercises `extraction cache setup failure is controlled`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
config, download, _ = _download(tmp_path)
extraction_parent = download.path.parent / "x"
extraction_parent.write_bytes(b"not a directory")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(InpnProtectedAreasSourceError, match="extract|cache"):
        extract_inpn_protected_areas_archive(download, config)
```

**Regression protected**

Locks `extraction cache setup failure is controlled`: the reproduced adversarial input must raise `InpnProtectedAreasSourceError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_extraction_cache_setup_failure_is_controlled(tmp_path: Path) -> None:
    config, download, _ = _download(tmp_path)
    extraction_parent = download.path.parent / "x"
    extraction_parent.write_bytes(b"not a directory")

    with pytest.raises(InpnProtectedAreasSourceError, match="extract|cache"):
        extract_inpn_protected_areas_archive(download, config)
```

### `test_extraction_rejects_stale_download_bytes`

**Purpose**

Exercises `extraction rejects stale download bytes`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
config, download, _ = _download(tmp_path)
replacement = _zip_bytes({"EP/readme.txt": b"forged contents"})
download.path.write_bytes(replacement)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(InpnProtectedAreasSourceError, match="SHA|size|archive|download"):
        extract_inpn_protected_areas_archive(download, config)
```

**Regression protected**

Locks `extraction rejects stale download bytes`: the reproduced adversarial input must raise `InpnProtectedAreasSourceError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_extraction_rejects_stale_download_bytes(tmp_path: Path) -> None:
    config, download, _ = _download(tmp_path)
    replacement = _zip_bytes({"EP/readme.txt": b"forged contents"})
    download.path.write_bytes(replacement)

    with pytest.raises(InpnProtectedAreasSourceError, match="SHA|size|archive|download"):
        extract_inpn_protected_areas_archive(download, config)
```

### `test_result_dataclasses_are_frozen`

**Purpose**

Exercises `result dataclasses are frozen`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
config, download, _ = _download(tmp_path)
```

**Action**

```python
extraction = extract_inpn_protected_areas_archive(download, config)
```

**Expected result**

```python
with pytest.raises(FrozenInstanceError):
        download.cache_hit = True
with pytest.raises(FrozenInstanceError):
        extraction.cache_hit = True
with pytest.raises(FrozenInstanceError):
        extraction.files[0].sha256 = "0" * 64
```

**Regression protected**

Pins verified cache reuse and ensures the successful local path avoids the external operation asserted by the test.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_result_dataclasses_are_frozen(tmp_path: Path) -> None:
    config, download, _ = _download(tmp_path)
    extraction = extract_inpn_protected_areas_archive(download, config)

    with pytest.raises(FrozenInstanceError):
        download.cache_hit = True  # type: ignore[misc]
    with pytest.raises(FrozenInstanceError):
        extraction.cache_hit = True  # type: ignore[misc]
    with pytest.raises(FrozenInstanceError):
        extraction.files[0].sha256 = "0" * 64
```

### `test_public_api_exports_only_stable_high_level_symbols`

**Purpose**

Exercises `public api exports only stable high level symbols`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert set(inpn.__all__) == EXPECTED_EXPORTS
assert EXPECTED_EXPORTS <= set(sources.__all__)
assert all(getattr(sources, name) is getattr(inpn, name) for name in EXPECTED_EXPORTS)
assert not hasattr(sources, "_validated_zip_members")
assert not hasattr(sources, "_inventory")
assert not hasattr(sources, "validate_inpn_protected_area_geometry")
```

**Regression protected**

Locks `public api exports only stable high level symbols` through the exact asserted conditions: `set(inpn.__all__) == EXPECTED_EXPORTS`; `EXPECTED_EXPORTS <= set(sources.__all__)`; `all((getattr(sources, name) is getattr(inpn, name) for name in EXPECTED_EXPORTS))`; `not hasattr(sources, '_validated_zip_members')`; plus 2 additional reproduced assertion(s).

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_public_api_exports_only_stable_high_level_symbols() -> None:
    assert set(inpn.__all__) == EXPECTED_EXPORTS
    assert EXPECTED_EXPORTS <= set(sources.__all__)
    assert all(getattr(sources, name) is getattr(inpn, name) for name in EXPECTED_EXPORTS)
    assert not hasattr(sources, "_validated_zip_members")
    assert not hasattr(sources, "_inventory")
    assert not hasattr(sources, "validate_inpn_protected_area_geometry")
```

### `test_result_schemas_are_factual_inventory_only`

**Purpose**

Exercises `result schemas are factual inventory only`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
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
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
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
assert not any(
        fragment in name.casefold()
        for name in inpn.__all__
        for fragment in forbidden
    )
```

**Regression protected**

Pins verified cache reuse and ensures the successful local path avoids the external operation asserted by the test.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
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
```

### `test_strict_metadata_rejects_boolean_numeric_values_as_cache_hits`

**Purpose**

Exercises `strict metadata rejects boolean numeric values as cache hits`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
config, first, _ = _download(tmp_path)
metadata_path = _download_metadata_path(first)
metadata = _read_json(metadata_path)
metadata["file_size"] = True
_write_json(metadata_path, metadata)
session = _session(config)
refreshed = _download_with_session(config, session)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert refreshed.cache_hit is False
assert len(session.calls) == 1
```

**Regression protected**

Pins verified cache reuse and ensures the successful local path avoids the external operation asserted by the test.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
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
```

### `test_cache_path_binds_version_and_filename`

**Purpose**

Exercises `cache path binds version and filename`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
_, download, _ = _download(tmp_path)
metadata = _read_json(_download_metadata_path(download))
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert download.path.name == "EP.zip"
assert "07-2026" in download.path.parts
assert metadata["dataset_id"] == "EP"
assert metadata["declared_version"] == "07/2026"
assert metadata["filename"] == "EP.zip"
```

**Regression protected**

Locks `cache path binds version and filename` through the exact asserted conditions: `download.path.name == 'EP.zip'`; `'07-2026' in download.path.parts`; `metadata['dataset_id'] == 'EP'`; `metadata['declared_version'] == '07/2026'`; plus 1 additional reproduced assertion(s).

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_cache_path_binds_version_and_filename(tmp_path: Path) -> None:
    _, download, _ = _download(tmp_path)

    assert download.path.name == "EP.zip"
    assert "07-2026" in download.path.parts
    metadata = _read_json(_download_metadata_path(download))
    assert metadata["dataset_id"] == "EP"
    assert metadata["declared_version"] == "07/2026"
    assert metadata["filename"] == "EP.zip"
```

### `test_download_uses_no_hidden_reference_page_scrape`

**Purpose**

Exercises `download uses no hidden reference page scrape`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
config = _config(tmp_path)
session = _session(config)
_download_with_session(config, session)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert [url for url, _ in session.calls] == [str(config.archive_url)]
assert str(config.reference_page_url) not in [url for url, _ in session.calls]
```

**Regression protected**

Locks `download uses no hidden reference page scrape` through the exact asserted conditions: `[url for url, _ in session.calls] == [str(config.archive_url)]`; `str(config.reference_page_url) not in [url for url, _ in session.calls]`.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_download_uses_no_hidden_reference_page_scrape(tmp_path: Path) -> None:
    config = _config(tmp_path)
    session = _session(config)

    _download_with_session(config, session)

    assert [url for url, _ in session.calls] == [str(config.archive_url)]
    assert str(config.reference_page_url) not in [url for url, _ in session.calls]
```

### `test_exact_file_inventory_does_not_omit_unknown_suffixes`

**Purpose**

Exercises `exact file inventory does not omit unknown suffixes`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
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
```

**Action**

```python
extraction = extract_inpn_protected_areas_archive(download, config)
```

**Expected result**

```python
assert {item.relative_path for item in extraction.files} == set(members)
```

**Regression protected**

Locks `exact file inventory does not omit unknown suffixes` through the exact asserted conditions: `{item.relative_path for item in extraction.files} == set(members)`.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
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
```

### `test_archive_and_extraction_cache_reuse_are_independent`

**Purpose**

Exercises `archive and extraction cache reuse are independent`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
config, first_download, _ = _download(tmp_path)
second_download = _download_with_session(
        config,
        _Session(error=AssertionError("network used")),
    )
```

**Action**

```python
first_extraction = extract_inpn_protected_areas_archive(first_download, config)
second_extraction = extract_inpn_protected_areas_archive(second_download, config)
```

**Expected result**

```python
assert first_download.cache_hit is False
assert first_extraction.cache_hit is False
assert second_download.cache_hit is True
assert second_extraction.cache_hit is True
```

**Regression protected**

Pins verified cache reuse and ensures the successful local path avoids the external operation asserted by the test.

**Test boundary**

- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
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
```

### `test_no_stale_parts_after_download_or_extraction_success`

**Purpose**

Exercises `no stale parts after download or extraction success`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
config, download, _ = _download(tmp_path)
```

**Action**

```python
extraction = extract_inpn_protected_areas_archive(download, config)
```

**Expected result**

```python
assert extraction.extraction_path.is_dir()
assert not list(Path(config.cache_root).rglob("*.part"))
assert not list(Path(config.cache_root).rglob("*.bak"))
```

**Regression protected**

Locks `no stale parts after download or extraction success` through the exact asserted conditions: `extraction.extraction_path.is_dir()`; `not list(Path(config.cache_root).rglob('*.part'))`; `not list(Path(config.cache_root).rglob('*.bak'))`.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_no_stale_parts_after_download_or_extraction_success(tmp_path: Path) -> None:
    config, download, _ = _download(tmp_path)
    extraction = extract_inpn_protected_areas_archive(download, config)

    assert extraction.extraction_path.is_dir()
    assert not list(Path(config.cache_root).rglob("*.part"))
    assert not list(Path(config.cache_root).rglob("*.bak"))
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

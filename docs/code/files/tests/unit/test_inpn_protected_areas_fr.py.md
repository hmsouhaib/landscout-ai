# `tests/unit/test_inpn_protected_areas_fr.py`

## File identity

- Repository path: `tests/unit/test_inpn_protected_areas_fr.py`
- File type: Python source
- Layer: unit/regression test
- Domain: isolated contract test evidence
- Responsibility: Provides complete unit and regression coverage for the `inpn_protected_areas_fr` contracts exercised in this file.
- Source SHA256: `3de30791195ceaa0b42b863626513920e1f90335b726e17747d847180070af8a`

## 1. STEP 7F.1B.1 contract delta

- Adds permanent public extraction-revalidation coverage without altering the existing acquisition/cache/ZIP/extraction suite.
- Regressions require fresh returned objects, exact types and configured path, caller tuple equality, current path/size/SHA facts, missing/extra/same-size mutation rejection, and link/junction rejection.

## 2. Purpose and architectural position

Provides complete unit and regression coverage for the `inpn_protected_areas_fr` contracts exercised in this file.

The file belongs to the **unit/regression test** layer and **isolated contract test evidence** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

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
- `from pydantic import ValidationError`

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

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `CONFIG_PATH`

- Category: module constant or closed domain.
- Exact declaration:

```python
CONFIG_PATH = Path("configs/sources/inpn_protected_areas_fr.yaml")
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `EXPECTED_EXPORTS`

- Category: module constant or closed domain.
- Exact declaration:

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

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `download_inpn_protected_areas_archive`
  - `InpnProtectedAreasDownload`
  - `InpnProtectedAreasSourceConfig`
  - `InpnProtectedAreasSourceError`
  - `extract_inpn_protected_areas_archive`
  - `InpnProtectedAreasExtraction`
  - `load_inpn_protected_areas_source_config`
  - `InpnProtectedAreasExtractedFile`


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

### `_Response`

**Source purpose:** Defines `_Response`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `raw` | `assigned instance field` | `io.BytesIO(payload)` | `self.raw = io.BytesIO(payload)` |
| `url` | `assigned instance field` | `url` | `self.url = url` |
| `status_code` | `assigned instance field` | `status_code` | `self.status_code = status_code` |
| `headers` | `assigned instance field` | `{} if location is None else {"Location": location}` | `self.headers = {} if location is None else {"Location": location}` |
| `closed` | `assigned instance field` | `False` | `self.closed = False` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- value/type reference: `tests.unit.test_inpn_protected_areas_fr::_Session.__init__` via `_Response`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::_Session.get` via `_Response`
- constructor call: `tests.unit.test_inpn_protected_areas_fr::_session` via `_Response`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::_session` via `_Response`
- constructor call: `tests.unit.test_inpn_protected_areas_fr::test_malformed_response_headers_have_controlled_error` via `_Response`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_malformed_response_headers_have_controlled_error` via `_Response`
- constructor call: `tests.unit.test_inpn_protected_areas_fr::test_midstream_protocol_failure_has_controlled_error` via `_Response`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_midstream_protocol_failure_has_controlled_error` via `_Response`

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
        return (
            self.status_code in {301, 302, 303, 307, 308} and "Location" in self.headers
        )

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

**Source purpose:** Defines `_Session`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `responses` | `assigned instance field` | `list(responses or ([] if response is None else [response]))` | `self.responses = list(responses or ([] if response is None else [response]))` |
| `error` | `assigned instance field` | `error` | `self.error = error` |
| `calls` | `list[tuple[str, dict[str, object]]]` | `[]` | `self.calls: list[tuple[str, dict[str, object]]] = []` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- constructor call: `tests.unit.test_inpn_protected_areas_fr::_session` via `_Session`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::_session` via `_Session`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::_download` via `_Session`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::_download_with_session` via `_Session`
- constructor call: `tests.unit.test_inpn_protected_areas_fr::test_coordinated_cache_and_metadata_snapshot_change_is_not_a_cache_hit` via `_Session`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_coordinated_cache_and_metadata_snapshot_change_is_not_a_cache_hit` via `_Session`
- constructor call: `tests.unit.test_inpn_protected_areas_fr::test_http_and_payload_failures_are_controlled` via `_Session`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_http_and_payload_failures_are_controlled` via `_Session`
- constructor call: `tests.unit.test_inpn_protected_areas_fr::test_malformed_response_headers_have_controlled_error` via `_Session`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_malformed_response_headers_have_controlled_error` via `_Session`
- constructor call: `tests.unit.test_inpn_protected_areas_fr::test_midstream_protocol_failure_has_controlled_error` via `_Session`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_midstream_protocol_failure_has_controlled_error` via `_Session`
- constructor call: `tests.unit.test_inpn_protected_areas_fr::test_failed_replacement_restores_a_still_reusable_valid_download_pair` via `_Session`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_failed_replacement_restores_a_still_reusable_valid_download_pair` via `_Session`
- constructor call: `tests.unit.test_inpn_protected_areas_fr::test_archive_and_extraction_cache_reuse_are_independent` via `_Session`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_archive_and_extraction_cache_reuse_are_independent` via `_Session`

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

**Source purpose:** Defines `test_midstream_protocol_failure_has_controlled_error._FailingRaw`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `decode_content` | `inferred from assignment` | `False` | `decode_content = False` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class _FailingRaw:
        decode_content = False

        def seek(self, offset: int) -> int:
            return offset

        def read(self, size: int = -1) -> bytes:
            raise OSError("connection ended mid-stream")
```


## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `_Response.__init__`

**Purpose:** Implements `init` within the file role: Provides complete unit and regression coverage for the `inpn_protected_areas_fr` contracts exercised in this file.

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

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |
| `payload` | positional-or-keyword | `bytes` | `required` |
| `url` | keyword-only | `str` | `required` |
| `status_code` | keyword-only | `int` | `200` |
| `location` | keyword-only | `str \| None` | `None` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
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
| In-memory mutation | `self.raw = io.BytesIO(payload)`<br>`self.url = url`<br>`self.status_code = status_code`<br>`self.headers = {} if location is None else {"Location": location}`<br>`self.closed = False` |
| Direct parameter mutation | `self.raw = io.BytesIO(payload)`<br>`self.url = url`<br>`self.status_code = status_code`<br>`self.headers = {} if location is None else {"Location": location}`<br>`self.closed = False` |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_Response.is_redirect`

**Purpose:** Implements `is redirect` within the file role: Provides complete unit and regression coverage for the `inpn_protected_areas_fr` contracts exercised in this file.

**Exact signature**

```python
def is_redirect(self) -> bool:
```

- Exact decorators: `property`.
- Declared return annotation: `bool`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `self.status_code in {301, 302, 303, 307, 308} and "Location" in self.headers`
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
def is_redirect(self) -> bool:
        return (
            self.status_code in {301, 302, 303, 307, 308} and "Location" in self.headers
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_Response.raise_for_status`

**Purpose:** Implements `raise for status` within the file role: Provides complete unit and regression coverage for the `inpn_protected_areas_fr` contracts exercised in this file.

**Exact signature**

```python
def raise_for_status(self) -> None:
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
  - `OSError(f"HTTP {self.status_code}")` under lexical guard `self.status_code >= 400`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `OSError` | `unresolved local/third-party receiver; no ownership inferred` |

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
def raise_for_status(self) -> None:
        if self.status_code >= 400:
            raise OSError(f"HTTP {self.status_code}")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_Response.iter_content`

**Purpose:** Implements `iter content` within the file role: Provides complete unit and regression coverage for the `inpn_protected_areas_fr` contracts exercised in this file.

**Exact signature**

```python
def iter_content(self, chunk_size: int = 8192) -> Any:
```

- Exact decorators: none.
- Declared return annotation: `Any`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |
| `chunk_size` | positional-or-keyword | `int` | `8192` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `self.raw.read` | `tests.unit.test_inpn_protected_areas_fr._Response.raw.read` |

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
def iter_content(self, chunk_size: int = 8192) -> Any:
        while chunk := self.raw.read(chunk_size):
            yield chunk
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_Response.close`

**Purpose:** Implements `close` within the file role: Provides complete unit and regression coverage for the `inpn_protected_areas_fr` contracts exercised in this file.

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
- direct call: `tests.unit.test_inpn_protected_areas_fr::_Response.__exit__` via `self.close`

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

### `_Response.read`

**Purpose:** Implements `read` within the file role: Provides complete unit and regression coverage for the `inpn_protected_areas_fr` contracts exercised in this file.

**Exact signature**

```python
def read(self, size: int = -1) -> bytes:
```

- Exact decorators: none.
- Declared return annotation: `bytes`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |
| `size` | positional-or-keyword | `int` | `-1` |

**Return and exception contract**

- Exact observed return expressions:
  - `self.raw.read(size)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `self.raw.read` | `tests.unit.test_inpn_protected_areas_fr._Response.raw.read` |

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
def read(self, size: int = -1) -> bytes:
        return self.raw.read(size)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_Response.__enter__`

**Purpose:** Implements `enter` within the file role: Provides complete unit and regression coverage for the `inpn_protected_areas_fr` contracts exercised in this file.

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_Response.__exit__`

**Purpose:** Implements `exit` within the file role: Provides complete unit and regression coverage for the `inpn_protected_areas_fr` contracts exercised in this file.

**Exact signature**

```python
def __exit__(self, *args: object) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |
| `*args` | variadic positional | `object` | `variadic` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `self.close` | `tests.unit.test_inpn_protected_areas_fr._Response.close` |

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
def __exit__(self, *args: object) -> None:
        self.close()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_Session.__init__`

**Purpose:** Implements `init` within the file role: Provides complete unit and regression coverage for the `inpn_protected_areas_fr` contracts exercised in this file.

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

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |
| `response` | positional-or-keyword | `_Response \| None` | `None` |
| `responses` | keyword-only | `list[_Response] \| None` | `None` |
| `error` | keyword-only | `Exception \| None` | `None` |

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
| In-memory mutation | `self.responses = list(responses or ([] if response is None else [response]))`<br>`self.error = error`<br>`self.calls: list[tuple[str, dict[str, object]]] = []` |
| Direct parameter mutation | `self.responses = list(responses or ([] if response is None else [response]))`<br>`self.error = error`<br>`self.calls: list[tuple[str, dict[str, object]]] = []` |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_Session.get`

**Purpose:** Implements `get` within the file role: Provides complete unit and regression coverage for the `inpn_protected_areas_fr` contracts exercised in this file.

**Exact signature**

```python
def get(self, url: str, **kwargs: object) -> _Response:
```

- Exact decorators: none.
- Declared return annotation: `_Response`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |
| `url` | positional-or-keyword | `str` | `required` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- Exact observed return expressions:
  - `response`
- Explicit raise paths:
  - `self.error` under lexical guard `self.error is not None`.
  - `AssertionError("No fake HTTP response was configured")` under lexical guard `not self.responses`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_inpn_protected_areas_fr::_Session.open` via `self.get`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `self.calls.append` | `tests.unit.test_inpn_protected_areas_fr._Session.calls.append` |
| `AssertionError` | `unresolved local/third-party receiver; no ownership inferred` |
| `self.responses.pop` | `tests.unit.test_inpn_protected_areas_fr._Session.responses.pop` |
| `response.raw.seek` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `self.calls.append((url, kwargs))`<br>`self.responses.pop(0)` |
| Direct parameter mutation | `self.calls.append((url, kwargs))`<br>`self.responses.pop(0)` |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_Session.open`

**Purpose:** Implements `open` within the file role: Provides complete unit and regression coverage for the `inpn_protected_areas_fr` contracts exercised in this file.

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

- Exact decorators: `contextmanager`.
- Declared return annotation: `Any`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |
| `url` | positional-or-keyword | `str` | `required` |
| `timeout` | keyword-only | `float` | `required` |
| `headers` | keyword-only | `dict[str, str] \| None` | `None` |
| `max_redirects` | keyword-only | `int` | `10` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `SafeHttpsError(f"HTTP status {response.status_code}")` under lexical guard `not 200 <= response.status_code < 300`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `self.get` | `tests.unit.test_inpn_protected_areas_fr._Session.get` |
| `SafeHttpsError` | `landscout.common.safe_http.SafeHttpsError` |
| `response.close` | `unresolved local/third-party receiver; no ownership inferred` |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_zip_bytes`

**Purpose:** Implements `zip bytes` within the file role: Provides complete unit and regression coverage for the `inpn_protected_areas_fr` contracts exercised in this file.

**Exact signature**

```python
def _zip_bytes(
    members: dict[str, bytes] | list[tuple[str, bytes]] | None = None,
) -> bytes:
```

- Exact decorators: none.
- Declared return annotation: `bytes`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `members` | positional-or-keyword | `dict[str, bytes] \| list[tuple[str, bytes]] \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `stream.getvalue()`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_inpn_protected_areas_fr::_unsupported_compression_zip` via `_zip_bytes`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::_unsupported_compression_zip` via `_zip_bytes`
- direct call: `tests.unit.test_inpn_protected_areas_fr::_config` via `_zip_bytes`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::_config` via `_zip_bytes`
- direct call: `tests.unit.test_inpn_protected_areas_fr::_session` via `_zip_bytes`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::_session` via `_zip_bytes`
- direct call: `tests.unit.test_inpn_protected_areas_fr::_download` via `_zip_bytes`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::_download` via `_zip_bytes`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_valid_zip_download_binds_exact_bytes_and_lineage` via `_zip_bytes`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_valid_zip_download_binds_exact_bytes_and_lineage` via `_zip_bytes`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_cold_download_must_match_configured_snapshot_before_publication` via `_zip_bytes`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_cold_download_must_match_configured_snapshot_before_publication` via `_zip_bytes`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_coordinated_cache_and_metadata_snapshot_change_is_not_a_cache_hit` via `_zip_bytes`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_coordinated_cache_and_metadata_snapshot_change_is_not_a_cache_hit` via `_zip_bytes`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_http_and_payload_failures_are_controlled` via `_zip_bytes`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_http_and_payload_failures_are_controlled` via `_zip_bytes`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_malformed_response_headers_have_controlled_error` via `_zip_bytes`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_malformed_response_headers_have_controlled_error` via `_zip_bytes`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_midstream_protocol_failure_has_controlled_error` via `_zip_bytes`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_midstream_protocol_failure_has_controlled_error` via `_zip_bytes`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_invalid_download_cache_is_a_miss` via `_zip_bytes`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_invalid_download_cache_is_a_miss` via `_zip_bytes`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_successful_first_and_replacement_publication` via `_zip_bytes`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_successful_first_and_replacement_publication` via `_zip_bytes`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_unsafe_zip_member_paths_are_rejected` via `_zip_bytes`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_unsafe_zip_member_paths_are_rejected` via `_zip_bytes`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_duplicate_or_colliding_zip_destinations_are_rejected` via `_zip_bytes`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_duplicate_or_colliding_zip_destinations_are_rejected` via `_zip_bytes`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_complete_zip_inventory_is_validated_before_member_copy` via `_zip_bytes`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_complete_zip_inventory_is_validated_before_member_copy` via `_zip_bytes`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_extraction_validates_complete_inventory_before_copying` via `_zip_bytes`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_extraction_validates_complete_inventory_before_copying` via `_zip_bytes`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_normal_nested_members_are_accepted` via `_zip_bytes`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_normal_nested_members_are_accepted` via `_zip_bytes`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_extraction_inventory_is_complete_ordered_and_hashed` via `_zip_bytes`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_extraction_inventory_is_complete_ordered_and_hashed` via `_zip_bytes`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_invalid_extraction_cache_is_rebuilt` via `_zip_bytes`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_invalid_extraction_cache_is_rebuilt` via `_zip_bytes`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_extraction_rejects_stale_download_bytes` via `_zip_bytes`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_extraction_rejects_stale_download_bytes` via `_zip_bytes`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_exact_file_inventory_does_not_omit_unknown_suffixes` via `_zip_bytes`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_exact_file_inventory_does_not_omit_unknown_suffixes` via `_zip_bytes`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `values.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `io.BytesIO` | `io.BytesIO` |
| `warnings.catch_warnings` | `warnings.catch_warnings` |
| `warnings.simplefilter` | `warnings.simplefilter` |
| `zipfile.ZipFile` | `zipfile.ZipFile` |
| `zipfile.ZipInfo` | `zipfile.ZipInfo` |
| `archive.writestr` | `unresolved local/third-party receiver; no ownership inferred` |
| `stream.getvalue` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `zipfile.ZipFile`<br>`zipfile.ZipInfo` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `info.compress_type = zipfile.ZIP_STORED` |
| Direct parameter mutation | None directly present. |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_special_zip`

**Purpose:** Implements `special zip` within the file role: Provides complete unit and regression coverage for the `inpn_protected_areas_fr` contracts exercised in this file.

**Exact signature**

```python
def _special_zip(name: str, mode: int) -> bytes:
```

- Exact decorators: none.
- Declared return annotation: `bytes`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `name` | positional-or-keyword | `str` | `required` |
| `mode` | positional-or-keyword | `int` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `stream.getvalue()`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_zip_links_and_special_files_are_rejected` via `_special_zip`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_zip_links_and_special_files_are_rejected` via `_special_zip`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `io.BytesIO` | `io.BytesIO` |
| `zipfile.ZipFile` | `zipfile.ZipFile` |
| `zipfile.ZipInfo` | `zipfile.ZipInfo` |
| `archive.writestr` | `unresolved local/third-party receiver; no ownership inferred` |
| `stream.getvalue` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `zipfile.ZipFile`<br>`zipfile.ZipInfo` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `info.create_system = 3`<br>`info.external_attr = mode << 16` |
| Direct parameter mutation | None directly present. |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_unsupported_compression_zip`

**Purpose:** Implements `unsupported compression zip` within the file role: Provides complete unit and regression coverage for the `inpn_protected_areas_fr` contracts exercised in this file.

**Exact signature**

```python
def _unsupported_compression_zip() -> bytes:
```

- Exact decorators: none.
- Declared return annotation: `bytes`.

**Inputs**

- No parameters.

**Return and exception contract**

- Exact observed return expressions:
  - `bytes(payload)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_unsupported_zip_compression_has_controlled_error` via `_unsupported_compression_zip`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_unsupported_zip_compression_has_controlled_error` via `_unsupported_compression_zip`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `bytearray` | `unresolved local/third-party receiver; no ownership inferred` |
| `_zip_bytes` | `tests.unit.test_inpn_protected_areas_fr._zip_bytes` |
| `payload.index` | `unresolved local/third-party receiver; no ownership inferred` |
| `(99).to_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `bytes` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `payload[local + 8 : local + 10] = (99).to_bytes(2, "little")`<br>`payload[central + 10 : central + 12] = (99).to_bytes(2, "little")` |
| Direct parameter mutation | None directly present. |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_config_payload`

**Purpose:** Implements `config payload` within the file role: Provides complete unit and regression coverage for the `inpn_protected_areas_fr` contracts exercised in this file.

**Exact signature**

```python
def _config_payload() -> dict[str, object]:
```

- Exact decorators: none.
- Declared return annotation: `dict[str, object]`.

**Inputs**

- No parameters.

**Return and exception contract**

- Exact observed return expressions:
  - `payload`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert isinstance(payload, dict)`

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_inpn_protected_areas_fr::_config` via `_config_payload`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::_config` via `_config_payload`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_config_rejects_invalid_expected_snapshot_integrity` via `_config_payload`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_config_rejects_invalid_expected_snapshot_integrity` via `_config_payload`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_config_rejects_noncanonical_values` via `_config_payload`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_config_rejects_noncanonical_values` via `_config_payload`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_download_cache_setup_failure_is_controlled` via `_config_payload`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_download_cache_setup_failure_is_controlled` via `_config_payload`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `yaml.safe_load` | `yaml.safe_load` |
| `CONFIG_PATH.read_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `CONFIG_PATH.read_text` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _config_payload() -> dict[str, object]:
    payload = yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))
    assert isinstance(payload, dict)
    return payload
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_write_config`

**Purpose:** Implements `write config` within the file role: Provides complete unit and regression coverage for the `inpn_protected_areas_fr` contracts exercised in this file.

**Exact signature**

```python
def _write_config(tmp_path: Path, payload: dict[str, object]) -> Path:
```

- Exact decorators: none.
- Declared return annotation: `Path`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `payload` | positional-or-keyword | `dict[str, object]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `path`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_config_rejects_noncanonical_values` via `_write_config`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_config_rejects_noncanonical_values` via `_write_config`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `yaml.safe_dump` | `yaml.safe_dump` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `path.write_text` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_config`

**Purpose:** Implements `config` within the file role: Provides complete unit and regression coverage for the `inpn_protected_areas_fr` contracts exercised in this file.

**Exact signature**

```python
def _config(
    tmp_path: Path,
    expected_bytes: bytes | None = None,
) -> InpnProtectedAreasSourceConfig:
```

- Exact decorators: none.
- Declared return annotation: `InpnProtectedAreasSourceConfig`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `expected_bytes` | positional-or-keyword | `bytes \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `InpnProtectedAreasSourceConfig.model_validate(payload)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_inpn_protected_areas_fr::_download` via `_config`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::_download` via `_config`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_valid_zip_download_binds_exact_bytes_and_lineage` via `_config`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_valid_zip_download_binds_exact_bytes_and_lineage` via `_config`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_cold_download_must_match_configured_snapshot_before_publication` via `_config`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_cold_download_must_match_configured_snapshot_before_publication` via `_config`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_http_and_payload_failures_are_controlled` via `_config`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_http_and_payload_failures_are_controlled` via `_config`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_unsupported_zip_compression_has_controlled_error` via `_config`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_unsupported_zip_compression_has_controlled_error` via `_config`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_malformed_response_headers_have_controlled_error` via `_config`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_malformed_response_headers_have_controlled_error` via `_config`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_midstream_protocol_failure_has_controlled_error` via `_config`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_midstream_protocol_failure_has_controlled_error` via `_config`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_unsafe_zip_member_paths_are_rejected` via `_config`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_unsafe_zip_member_paths_are_rejected` via `_config`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_duplicate_or_colliding_zip_destinations_are_rejected` via `_config`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_duplicate_or_colliding_zip_destinations_are_rejected` via `_config`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_zip_links_and_special_files_are_rejected` via `_config`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_zip_links_and_special_files_are_rejected` via `_config`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_complete_zip_inventory_is_validated_before_member_copy` via `_config`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_complete_zip_inventory_is_validated_before_member_copy` via `_config`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_extraction_rejects_wrong_download_type` via `_config`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_extraction_rejects_wrong_download_type` via `_config`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_download_uses_no_hidden_reference_page_scrape` via `_config`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_download_uses_no_hidden_reference_page_scrape` via `_config`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_zip_bytes` | `tests.unit.test_inpn_protected_areas_fr._zip_bytes` |
| `_config_payload` | `tests.unit.test_inpn_protected_areas_fr._config_payload` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256(snapshot).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |
| `InpnProtectedAreasSourceConfig.model_validate` | `landscout.sources.inpn_protected_areas_fr.InpnProtectedAreasSourceConfig.model_validate` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `sha256(snapshot).hexdigest`<br>`sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `payload["cache_root"] = str(tmp_path / "cache")`<br>`payload["expected_archive_size_bytes"] = len(snapshot)`<br>`payload["expected_archive_sha256"] = sha256(snapshot).hexdigest()` |
| Direct parameter mutation | None directly present. |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_session`

**Purpose:** Implements `session` within the file role: Provides complete unit and regression coverage for the `inpn_protected_areas_fr` contracts exercised in this file.

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

- Exact decorators: none.
- Declared return annotation: `_Session`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `config` | positional-or-keyword | `InpnProtectedAreasSourceConfig` | `required` |
| `payload` | positional-or-keyword | `bytes \| None` | `None` |
| `status_code` | keyword-only | `int` | `200` |
| `redirect_chain` | keyword-only | `tuple[str, ...]` | `()` |

**Return and exception contract**

- Exact observed return expressions:
  - `_Session(<br>            _Response(<br>                payload if payload is not None else _zip_bytes(),<br>                url=archive_url,<br>                status_code=status_code,<br>            )<br>        )`
  - `_Session(responses=responses)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_inpn_protected_areas_fr::_download` via `_session`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::_download` via `_session`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_download_cache_setup_failure_is_controlled` via `_session`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_download_cache_setup_failure_is_controlled` via `_session`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_valid_zip_download_binds_exact_bytes_and_lineage` via `_session`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_valid_zip_download_binds_exact_bytes_and_lineage` via `_session`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_cold_download_must_match_configured_snapshot_before_publication` via `_session`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_cold_download_must_match_configured_snapshot_before_publication` via `_session`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_http_and_payload_failures_are_controlled` via `_session`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_http_and_payload_failures_are_controlled` via `_session`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_unsupported_zip_compression_has_controlled_error` via `_session`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_unsupported_zip_compression_has_controlled_error` via `_session`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_invalid_download_cache_is_a_miss` via `_session`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_invalid_download_cache_is_a_miss` via `_session`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_successful_first_and_replacement_publication` via `_session`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_successful_first_and_replacement_publication` via `_session`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_publication_failure_restores_old_pair` via `_session`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_publication_failure_restores_old_pair` via `_session`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_rollback_failure_preserves_recovery_material` via `_session`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_rollback_failure_preserves_recovery_material` via `_session`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_failed_replacement_restores_a_still_reusable_valid_download_pair` via `_session`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_failed_replacement_restores_a_still_reusable_valid_download_pair` via `_session`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_unsafe_zip_member_paths_are_rejected` via `_session`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_unsafe_zip_member_paths_are_rejected` via `_session`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_duplicate_or_colliding_zip_destinations_are_rejected` via `_session`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_duplicate_or_colliding_zip_destinations_are_rejected` via `_session`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_zip_links_and_special_files_are_rejected` via `_session`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_zip_links_and_special_files_are_rejected` via `_session`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_complete_zip_inventory_is_validated_before_member_copy` via `_session`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_complete_zip_inventory_is_validated_before_member_copy` via `_session`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_strict_metadata_rejects_boolean_numeric_values_as_cache_hits` via `_session`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_strict_metadata_rejects_boolean_numeric_values_as_cache_hits` via `_session`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_download_uses_no_hidden_reference_page_scrape` via `_session`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_download_uses_no_hidden_reference_page_scrape` via `_session`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `_Session` | `tests.unit.test_inpn_protected_areas_fr._Session` |
| `_Response` | `tests.unit.test_inpn_protected_areas_fr._Response` |
| `_zip_bytes` | `tests.unit.test_inpn_protected_areas_fr._zip_bytes` |
| `responses.append` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `responses.append(<br>            _Response(<br>                b"",<br>                url=current_url,<br>                status_code=302,<br>                location=target_url,<br>            )<br>        )`<br>`responses.append(<br>        _Response(<br>            payload if payload is not None else _zip_bytes(),<br>            url=current_url,<br>            status_code=status_code,<br>        )<br>    )` |
| Direct parameter mutation | None directly present. |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_download`

**Purpose:** Implements `download` within the file role: Provides complete unit and regression coverage for the `inpn_protected_areas_fr` contracts exercised in this file.

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

- Exact decorators: none.
- Declared return annotation: `tuple[InpnProtectedAreasSourceConfig, InpnProtectedAreasDownload, _Session]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `payload` | keyword-only | `bytes \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `config, result, session`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_coordinated_cache_and_metadata_snapshot_change_is_not_a_cache_hit` via `_download`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_coordinated_cache_and_metadata_snapshot_change_is_not_a_cache_hit` via `_download`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_valid_physical_and_metadata_cache_is_reused` via `_download`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_valid_physical_and_metadata_cache_is_reused` via `_download`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_invalid_download_cache_is_a_miss` via `_download`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_invalid_download_cache_is_a_miss` via `_download`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_successful_first_and_replacement_publication` via `_download`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_successful_first_and_replacement_publication` via `_download`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_publication_failure_restores_old_pair` via `_download`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_publication_failure_restores_old_pair` via `_download`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_rollback_failure_preserves_recovery_material` via `_download`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_rollback_failure_preserves_recovery_material` via `_download`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_failed_replacement_restores_a_still_reusable_valid_download_pair` via `_download`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_failed_replacement_restores_a_still_reusable_valid_download_pair` via `_download`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_extraction_validates_complete_inventory_before_copying` via `_download`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_extraction_validates_complete_inventory_before_copying` via `_download`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_normal_nested_members_are_accepted` via `_download`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_normal_nested_members_are_accepted` via `_download`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_extraction_inventory_is_complete_ordered_and_hashed` via `_download`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_extraction_inventory_is_complete_ordered_and_hashed` via `_download`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_valid_extraction_cache_is_reused` via `_download`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_valid_extraction_cache_is_reused` via `_download`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_invalid_extraction_cache_is_rebuilt` via `_download`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_invalid_extraction_cache_is_rebuilt` via `_download`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_first_extraction_publication_failure_leaves_no_half_root` via `_download`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_first_extraction_publication_failure_leaves_no_half_root` via `_download`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_extraction_replacement_failure_restores_old_tree` via `_download`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_extraction_replacement_failure_restores_old_tree` via `_download`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_extraction_rollback_failure_preserves_backup` via `_download`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_extraction_rollback_failure_preserves_backup` via `_download`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_extraction_backup_move_failure_leaves_old_tree_untouched` via `_download`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_extraction_backup_move_failure_leaves_old_tree_untouched` via `_download`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_extraction_rejects_wrong_config_type` via `_download`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_extraction_rejects_wrong_config_type` via `_download`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_extraction_cache_setup_failure_is_controlled` via `_download`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_extraction_cache_setup_failure_is_controlled` via `_download`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_extraction_rejects_stale_download_bytes` via `_download`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_extraction_rejects_stale_download_bytes` via `_download`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_result_dataclasses_are_frozen` via `_download`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_result_dataclasses_are_frozen` via `_download`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_strict_metadata_rejects_boolean_numeric_values_as_cache_hits` via `_download`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_strict_metadata_rejects_boolean_numeric_values_as_cache_hits` via `_download`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_cache_path_binds_version_and_filename` via `_download`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_cache_path_binds_version_and_filename` via `_download`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_exact_file_inventory_does_not_omit_unknown_suffixes` via `_download`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_exact_file_inventory_does_not_omit_unknown_suffixes` via `_download`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_archive_and_extraction_cache_reuse_are_independent` via `_download`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_archive_and_extraction_cache_reuse_are_independent` via `_download`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_no_stale_parts_after_download_or_extraction_success` via `_download`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_no_stale_parts_after_download_or_extraction_success` via `_download`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_zip_bytes` | `tests.unit.test_inpn_protected_areas_fr._zip_bytes` |
| `_config` | `tests.unit.test_inpn_protected_areas_fr._config` |
| `_session` | `tests.unit.test_inpn_protected_areas_fr._session` |
| `_download_with_session` | `tests.unit.test_inpn_protected_areas_fr._download_with_session` |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_download_with_session`

**Purpose:** Implements `download with session` within the file role: Provides complete unit and regression coverage for the `inpn_protected_areas_fr` contracts exercised in this file.

**Exact signature**

```python
def _download_with_session(
    config: InpnProtectedAreasSourceConfig,
    session: _Session,
    *,
    timeout_seconds: float = 120.0,
) -> InpnProtectedAreasDownload:
```

- Exact decorators: none.
- Declared return annotation: `InpnProtectedAreasDownload`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `config` | positional-or-keyword | `InpnProtectedAreasSourceConfig` | `required` |
| `session` | positional-or-keyword | `_Session` | `required` |
| `timeout_seconds` | keyword-only | `float` | `120.0` |

**Return and exception contract**

- Exact observed return expressions:
  - `download_inpn_protected_areas_archive(<br>            config,<br>            timeout_seconds=timeout_seconds,<br>        )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_inpn_protected_areas_fr::_download` via `_download_with_session`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::_download` via `_download_with_session`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_download_cache_setup_failure_is_controlled` via `_download_with_session`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_download_cache_setup_failure_is_controlled` via `_download_with_session`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_valid_zip_download_binds_exact_bytes_and_lineage` via `_download_with_session`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_valid_zip_download_binds_exact_bytes_and_lineage` via `_download_with_session`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_cold_download_must_match_configured_snapshot_before_publication` via `_download_with_session`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_cold_download_must_match_configured_snapshot_before_publication` via `_download_with_session`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_coordinated_cache_and_metadata_snapshot_change_is_not_a_cache_hit` via `_download_with_session`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_coordinated_cache_and_metadata_snapshot_change_is_not_a_cache_hit` via `_download_with_session`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_http_and_payload_failures_are_controlled` via `_download_with_session`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_http_and_payload_failures_are_controlled` via `_download_with_session`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_unsupported_zip_compression_has_controlled_error` via `_download_with_session`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_unsupported_zip_compression_has_controlled_error` via `_download_with_session`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_malformed_response_headers_have_controlled_error` via `_download_with_session`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_malformed_response_headers_have_controlled_error` via `_download_with_session`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_midstream_protocol_failure_has_controlled_error` via `_download_with_session`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_midstream_protocol_failure_has_controlled_error` via `_download_with_session`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_invalid_download_cache_is_a_miss` via `_download_with_session`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_invalid_download_cache_is_a_miss` via `_download_with_session`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_successful_first_and_replacement_publication` via `_download_with_session`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_successful_first_and_replacement_publication` via `_download_with_session`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_publication_failure_restores_old_pair` via `_download_with_session`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_publication_failure_restores_old_pair` via `_download_with_session`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_rollback_failure_preserves_recovery_material` via `_download_with_session`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_rollback_failure_preserves_recovery_material` via `_download_with_session`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_failed_replacement_restores_a_still_reusable_valid_download_pair` via `_download_with_session`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_failed_replacement_restores_a_still_reusable_valid_download_pair` via `_download_with_session`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_unsafe_zip_member_paths_are_rejected` via `_download_with_session`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_unsafe_zip_member_paths_are_rejected` via `_download_with_session`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_duplicate_or_colliding_zip_destinations_are_rejected` via `_download_with_session`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_duplicate_or_colliding_zip_destinations_are_rejected` via `_download_with_session`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_zip_links_and_special_files_are_rejected` via `_download_with_session`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_zip_links_and_special_files_are_rejected` via `_download_with_session`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_complete_zip_inventory_is_validated_before_member_copy` via `_download_with_session`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_complete_zip_inventory_is_validated_before_member_copy` via `_download_with_session`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_strict_metadata_rejects_boolean_numeric_values_as_cache_hits` via `_download_with_session`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_strict_metadata_rejects_boolean_numeric_values_as_cache_hits` via `_download_with_session`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_download_uses_no_hidden_reference_page_scrape` via `_download_with_session`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_download_uses_no_hidden_reference_page_scrape` via `_download_with_session`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_archive_and_extraction_cache_reuse_are_independent` via `_download_with_session`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_archive_and_extraction_cache_reuse_are_independent` via `_download_with_session`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.MonkeyPatch.context` | `pytest.MonkeyPatch.context` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `download_inpn_protected_areas_archive` | `landscout.sources.inpn_protected_areas_fr.download_inpn_protected_areas_archive` |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_download_metadata_path`

**Purpose:** Implements `download metadata path` within the file role: Provides complete unit and regression coverage for the `inpn_protected_areas_fr` contracts exercised in this file.

**Exact signature**

```python
def _download_metadata_path(download: InpnProtectedAreasDownload) -> Path:
```

- Exact decorators: none.
- Declared return annotation: `Path`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `download` | positional-or-keyword | `InpnProtectedAreasDownload` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `download.path.with_name(f"{download.filename}.metadata.json")`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_valid_zip_download_binds_exact_bytes_and_lineage` via `_download_metadata_path`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_valid_zip_download_binds_exact_bytes_and_lineage` via `_download_metadata_path`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_coordinated_cache_and_metadata_snapshot_change_is_not_a_cache_hit` via `_download_metadata_path`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_coordinated_cache_and_metadata_snapshot_change_is_not_a_cache_hit` via `_download_metadata_path`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_invalid_download_cache_is_a_miss` via `_download_metadata_path`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_invalid_download_cache_is_a_miss` via `_download_metadata_path`
- direct call: `tests.unit.test_inpn_protected_areas_fr::_force_cache_miss` via `_download_metadata_path`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::_force_cache_miss` via `_download_metadata_path`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_successful_first_and_replacement_publication` via `_download_metadata_path`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_successful_first_and_replacement_publication` via `_download_metadata_path`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_rollback_failure_preserves_recovery_material` via `_download_metadata_path`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_rollback_failure_preserves_recovery_material` via `_download_metadata_path`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_failed_replacement_restores_a_still_reusable_valid_download_pair` via `_download_metadata_path`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_failed_replacement_restores_a_still_reusable_valid_download_pair` via `_download_metadata_path`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_strict_metadata_rejects_boolean_numeric_values_as_cache_hits` via `_download_metadata_path`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_strict_metadata_rejects_boolean_numeric_values_as_cache_hits` via `_download_metadata_path`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_cache_path_binds_version_and_filename` via `_download_metadata_path`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_cache_path_binds_version_and_filename` via `_download_metadata_path`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `download.path.with_name` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _download_metadata_path(download: InpnProtectedAreasDownload) -> Path:
    return download.path.with_name(f"{download.filename}.metadata.json")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_extraction_metadata_path`

**Purpose:** Implements `extraction metadata path` within the file role: Provides complete unit and regression coverage for the `inpn_protected_areas_fr` contracts exercised in this file.

**Exact signature**

```python
def _extraction_metadata_path(extraction: InpnProtectedAreasExtraction) -> Path:
```

- Exact decorators: none.
- Declared return annotation: `Path`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `extraction` | positional-or-keyword | `InpnProtectedAreasExtraction` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `candidates[0]`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert len(candidates) == 1`

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_extraction_inventory_is_complete_ordered_and_hashed` via `_extraction_metadata_path`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_extraction_inventory_is_complete_ordered_and_hashed` via `_extraction_metadata_path`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_invalid_extraction_cache_is_rebuilt` via `_extraction_metadata_path`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_invalid_extraction_cache_is_rebuilt` via `_extraction_metadata_path`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `extraction.extraction_path.iterdir` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.name.startswith` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `extraction.extraction_path.iterdir`<br>`path.is_file` |
| Filesystem/archive write or publication | `extraction.extraction_path.iterdir` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_read_json`

**Purpose:** Implements `read json` within the file role: Provides complete unit and regression coverage for the `inpn_protected_areas_fr` contracts exercised in this file.

**Exact signature**

```python
def _read_json(path: Path) -> dict[str, object]:
```

- Exact decorators: none.
- Declared return annotation: `dict[str, object]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `payload`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert isinstance(payload, dict)`

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_valid_zip_download_binds_exact_bytes_and_lineage` via `_read_json`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_valid_zip_download_binds_exact_bytes_and_lineage` via `_read_json`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_coordinated_cache_and_metadata_snapshot_change_is_not_a_cache_hit` via `_read_json`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_coordinated_cache_and_metadata_snapshot_change_is_not_a_cache_hit` via `_read_json`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_invalid_download_cache_is_a_miss` via `_read_json`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_invalid_download_cache_is_a_miss` via `_read_json`
- direct call: `tests.unit.test_inpn_protected_areas_fr::_force_cache_miss` via `_read_json`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::_force_cache_miss` via `_read_json`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_successful_first_and_replacement_publication` via `_read_json`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_successful_first_and_replacement_publication` via `_read_json`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_extraction_inventory_is_complete_ordered_and_hashed` via `_read_json`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_extraction_inventory_is_complete_ordered_and_hashed` via `_read_json`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_invalid_extraction_cache_is_rebuilt` via `_read_json`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_invalid_extraction_cache_is_rebuilt` via `_read_json`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_strict_metadata_rejects_boolean_numeric_values_as_cache_hits` via `_read_json`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_strict_metadata_rejects_boolean_numeric_values_as_cache_hits` via `_read_json`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_cache_path_binds_version_and_filename` via `_read_json`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_cache_path_binds_version_and_filename` via `_read_json`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `json.loads` | `json.loads` |
| `path.read_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `path.read_text` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _read_json(path: Path) -> dict[str, object]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(payload, dict)
    return payload
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_write_json`

**Purpose:** Implements `write json` within the file role: Provides complete unit and regression coverage for the `inpn_protected_areas_fr` contracts exercised in this file.

**Exact signature**

```python
def _write_json(path: Path, payload: dict[str, object]) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |
| `payload` | positional-or-keyword | `dict[str, object]` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_coordinated_cache_and_metadata_snapshot_change_is_not_a_cache_hit` via `_write_json`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_coordinated_cache_and_metadata_snapshot_change_is_not_a_cache_hit` via `_write_json`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_invalid_download_cache_is_a_miss` via `_write_json`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_invalid_download_cache_is_a_miss` via `_write_json`
- direct call: `tests.unit.test_inpn_protected_areas_fr::_force_cache_miss` via `_write_json`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::_force_cache_miss` via `_write_json`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_invalid_extraction_cache_is_rebuilt` via `_write_json`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_invalid_extraction_cache_is_rebuilt` via `_write_json`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_strict_metadata_rejects_boolean_numeric_values_as_cache_hits` via `_write_json`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_strict_metadata_rejects_boolean_numeric_values_as_cache_hits` via `_write_json`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `path.write_text` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _write_json(path: Path, payload: dict[str, object]) -> None:
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_checked_in_config_loads_with_exact_source_identity`

**Purpose:** Regression invariant: checked in config loads with exact source identity. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_checked_in_config_loads_with_exact_source_identity() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert type(config) is InpnProtectedAreasSourceConfig`
  - `assert config.provider == "PatriNat"`
  - `assert config.authority == "MNHN"`
  - `assert config.program == "INPN"`
  - `assert config.dataset_id == "EP"`
  - `assert config.dataset_name == "Base de référence des espaces protégés français"`
  - `assert config.declared_version == "07/2026"`
  - `assert str(config.reference_page_url).startswith("https://www.patrinat.fr/")`
  - `assert (<br>        str(config.archive_url) == "https://assets.patrinat.fr/files/donnees/ep/EP.zip"<br>    )`
  - `assert config.archive_filename == "EP.zip"`
  - `assert config.expected_archive_size_bytes == 99_835_011`
  - `assert (<br>        config.expected_archive_sha256<br>        == "73688bc37205a5e7f59e2065a0b81fc8cf2a242bdec5d7d2786f083671c4abe5"<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `load_inpn_protected_areas_source_config` | `landscout.sources.inpn_protected_areas_fr.load_inpn_protected_areas_source_config` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `str(config.reference_page_url).startswith` | `unresolved local/third-party receiver; no ownership inferred` |
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
    assert (
        str(config.archive_url) == "https://assets.patrinat.fr/files/donnees/ep/EP.zip"
    )
    assert config.archive_filename == "EP.zip"
    assert config.expected_archive_size_bytes == 99_835_011
    assert (
        config.expected_archive_sha256
        == "73688bc37205a5e7f59e2065a0b81fc8cf2a242bdec5d7d2786f083671c4abe5"
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_config_yaml_rejects_duplicate_keys`

**Purpose:** Regression invariant: source config yaml rejects duplicate keys. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_config_yaml_rejects_duplicate_keys(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(InpnProtectedAreasSourceError, match="config")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `CONFIG_PATH.read_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `load_inpn_protected_areas_source_config` | `landscout.sources.inpn_protected_areas_fr.load_inpn_protected_areas_source_config` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `CONFIG_PATH.read_text` |
| Filesystem/archive write or publication | `path.write_text` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_source_config_yaml_rejects_duplicate_keys(tmp_path: Path) -> None:
    path = tmp_path / "source.yaml"
    path.write_text(
        CONFIG_PATH.read_text(encoding="utf-8") + "\nprovider: PatriNat\n",
        encoding="utf-8",
    )

    with pytest.raises(InpnProtectedAreasSourceError, match="config"):
        load_inpn_protected_areas_source_config(path)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_loaded_source_config_is_immutable`

**Purpose:** Regression invariant: loaded source config is immutable. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_loaded_source_config_is_immutable() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValidationError, match="frozen")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `load_inpn_protected_areas_source_config` | `landscout.sources.inpn_protected_areas_fr.load_inpn_protected_areas_source_config` |
| `pytest.raises` | `pytest.raises` |

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
| In-memory mutation | `config.declared_version = "08/2026"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_loaded_source_config_is_immutable() -> None:
    config = load_inpn_protected_areas_source_config()

    with pytest.raises(ValidationError, match="frozen"):
        config.declared_version = "08/2026"
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_config_rejects_invalid_expected_snapshot_integrity`

**Purpose:** Regression invariant: config rejects invalid expected snapshot integrity. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_config_rejects_invalid_expected_snapshot_integrity(
    field: str,
    value: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("field", "value"),
    [
        ("expected_archive_size_bytes", 0),
        ("expected_archive_size_bytes", -1),
        ("expected_archive_size_bytes", True),
        ("expected_archive_size_bytes", 1.0),
        ("expected_archive_size_bytes", "99835011"),
        ("expected_archive_size_bytes", float("nan")),
        ("expected_archive_size_bytes", float("inf")),
        ("expected_archive_size_bytes", float("-inf")),
        ("expected_archive_sha256", "0" * 63),
        ("expected_archive_sha256", "A" * 64),
        ("expected_archive_sha256", None),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `field` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises((TypeError, ValueError))`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_config_payload` | `tests.unit.test_inpn_protected_areas_fr._config_payload` |
| `pytest.raises` | `pytest.raises` |
| `InpnProtectedAreasSourceConfig.model_validate` | `landscout.sources.inpn_protected_areas_fr.InpnProtectedAreasSourceConfig.model_validate` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `payload[field] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_config_rejects_noncanonical_values`

**Purpose:** Regression invariant: config rejects noncanonical values. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_config_rejects_noncanonical_values(tmp_path: Path, mutation: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
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
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `mutation` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(InpnProtectedAreasSourceError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_config_payload` | `tests.unit.test_inpn_protected_areas_fr._config_payload` |
| `payload.pop` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `load_inpn_protected_areas_source_config` | `landscout.sources.inpn_protected_areas_fr.load_inpn_protected_areas_source_config` |
| `_write_config` | `tests.unit.test_inpn_protected_areas_fr._write_config` |
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
| In-memory mutation | `payload["unexpected"] = True`<br>`payload.pop("dataset_id")`<br>`payload["dataset_id"] = "ZNIEFF"`<br>`payload["declared_version"] = " "`<br>`payload["reference_page_url"] = "not-a-url"`<br>`payload["archive_url"] = "://bad"`<br>`payload["archive_url"] = "http://assets.patrinat.fr/files/donnees/ep/EP.zip"`<br>`payload["archive_filename"] = "other.zip"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_wrong_download_config_type_has_controlled_error`

**Purpose:** Regression invariant: wrong download config type has controlled error. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_wrong_download_config_type_has_controlled_error() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(InpnProtectedAreasSourceError, match="config\|type")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `download_inpn_protected_areas_archive` | `landscout.sources.inpn_protected_areas_fr.download_inpn_protected_areas_archive` |
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
def test_wrong_download_config_type_has_controlled_error() -> None:
    with pytest.raises(InpnProtectedAreasSourceError, match="config|type"):
        download_inpn_protected_areas_archive(object())
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_download_timeout_is_strict_finite_positive`

**Purpose:** Regression invariant: download timeout is strict finite positive. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_download_timeout_is_strict_finite_positive(timeout: object) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
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
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `timeout` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(InpnProtectedAreasSourceError, match="timeout")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `download_inpn_protected_areas_archive` | `landscout.sources.inpn_protected_areas_fr.download_inpn_protected_areas_archive` |
| `load_inpn_protected_areas_source_config` | `landscout.sources.inpn_protected_areas_fr.load_inpn_protected_areas_source_config` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.param` | `pytest.param` |

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
def test_download_timeout_is_strict_finite_positive(timeout: object) -> None:
    with pytest.raises(InpnProtectedAreasSourceError, match="timeout"):
        download_inpn_protected_areas_archive(
            load_inpn_protected_areas_source_config(),
            timeout_seconds=timeout,  # type: ignore[arg-type]
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_download_api_has_no_arbitrary_http_session_injection`

**Purpose:** Regression invariant: download api has no arbitrary http session injection. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_download_api_has_no_arbitrary_http_session_injection() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert (<br>        "session"<br>        not in inspect.signature(download_inpn_protected_areas_archive).parameters<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `inspect.signature` | `inspect.signature` |

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
def test_download_api_has_no_arbitrary_http_session_injection() -> None:
    assert (
        "session"
        not in inspect.signature(download_inpn_protected_areas_archive).parameters
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_download_cache_setup_failure_is_controlled`

**Purpose:** Regression invariant: download cache setup failure is controlled. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_download_cache_setup_failure_is_controlled(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(InpnProtectedAreasSourceError, match="download\|cache")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `cache_file.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `_config_payload` | `tests.unit.test_inpn_protected_areas_fr._config_payload` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `InpnProtectedAreasSourceConfig.model_validate` | `landscout.sources.inpn_protected_areas_fr.InpnProtectedAreasSourceConfig.model_validate` |
| `pytest.raises` | `pytest.raises` |
| `_download_with_session` | `tests.unit.test_inpn_protected_areas_fr._download_with_session` |
| `_session` | `tests.unit.test_inpn_protected_areas_fr._session` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `cache_file.write_bytes` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `payload["cache_root"] = str(cache_file)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_valid_zip_download_binds_exact_bytes_and_lineage`

**Purpose:** Regression invariant: valid zip download binds exact bytes and lineage. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_valid_zip_download_binds_exact_bytes_and_lineage(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.cache_hit is False`
  - `assert result.path.read_bytes() == payload`
  - `assert result.file_size == len(payload)`
  - `assert result.sha256 == sha256(payload).hexdigest()`
  - `assert len(result.sha256) == 64 and result.sha256 == result.sha256.lower()`
  - `assert timestamp.tzinfo is not None`
  - `assert timestamp.utcoffset() is not None`
  - `assert timestamp.utcoffset().total_seconds() == 0`
  - `assert result.filename == config.archive_filename == "EP.zip"`
  - `assert getattr(result, field) == expected`
  - `assert len(session.calls) == 1`
  - `assert requested_url == str(config.archive_url)`
  - `assert request_options["timeout"] == pytest.approx(120.0)`
  - `assert metadata["schema_version"] == 1`
  - `assert metadata["file_size"] == len(payload)`
  - `assert metadata["sha256"] == result.sha256`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_zip_bytes` | `tests.unit.test_inpn_protected_areas_fr._zip_bytes` |
| `_config` | `tests.unit.test_inpn_protected_areas_fr._config` |
| `_session` | `tests.unit.test_inpn_protected_areas_fr._session` |
| `_download_with_session` | `tests.unit.test_inpn_protected_areas_fr._download_with_session` |
| `result.path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256(payload).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |
| `result.sha256.lower` | `unresolved local/third-party receiver; no ownership inferred` |
| `datetime.fromisoformat` | `datetime.datetime.fromisoformat` |
| `timestamp.utcoffset` | `unresolved local/third-party receiver; no ownership inferred` |
| `timestamp.utcoffset().total_seconds` | `unresolved local/third-party receiver; no ownership inferred` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `field.endswith` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.approx` | `pytest.approx` |
| `_read_json` | `tests.unit.test_inpn_protected_areas_fr._read_json` |
| `_download_metadata_path` | `tests.unit.test_inpn_protected_areas_fr._download_metadata_path` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `result.path.read_bytes` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `sha256(payload).hexdigest`<br>`sha256`<br>`result.sha256.lower` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_cold_download_must_match_configured_snapshot_before_publication`

**Purpose:** Regression invariant: cold download must match configured snapshot before publication. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_cold_download_must_match_configured_snapshot_before_publication(
    tmp_path: Path,
    mismatch: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("mismatch", ["size", "sha256"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `mismatch` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        InpnProtectedAreasSourceError, match="size\|SHA\|snapshot\|integrity"<br>    )`
- Exact assertions:
  - `assert len(downloaded) != len(expected)`
  - `assert len(downloaded) == len(expected)`
  - `assert sha256(downloaded).digest() != sha256(expected).digest()`
  - `assert not list(Path(config.cache_root).rglob("EP.zip"))`
  - `assert not list(Path(config.cache_root).rglob("*.metadata.json"))`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_zip_bytes` | `tests.unit.test_inpn_protected_areas_fr._zip_bytes` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256(downloaded).digest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |
| `sha256(expected).digest` | `unresolved local/third-party receiver; no ownership inferred` |
| `_config` | `tests.unit.test_inpn_protected_areas_fr._config` |
| `pytest.raises` | `pytest.raises` |
| `_download_with_session` | `tests.unit.test_inpn_protected_areas_fr._download_with_session` |
| `_session` | `tests.unit.test_inpn_protected_areas_fr._session` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `Path(config.cache_root).rglob` | `unresolved local/third-party receiver; no ownership inferred` |
| `Path` | `pathlib.Path` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `sha256(downloaded).digest`<br>`sha256`<br>`sha256(expected).digest` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

    with pytest.raises(
        InpnProtectedAreasSourceError, match="size|SHA|snapshot|integrity"
    ):
        _download_with_session(config, _session(config, downloaded))

    assert not list(Path(config.cache_root).rglob("EP.zip"))
    assert not list(Path(config.cache_root).rglob("*.metadata.json"))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_coordinated_cache_and_metadata_snapshot_change_is_not_a_cache_hit`

**Purpose:** Regression invariant: coordinated cache and metadata snapshot change is not a cache hit. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_coordinated_cache_and_metadata_snapshot_change_is_not_a_cache_hit(
    tmp_path: Path,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(InpnProtectedAreasSourceError)`
- Exact assertions:
  - `assert len(replacement) == first.file_size`
  - `assert len(no_network.calls) == 1`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_download` | `tests.unit.test_inpn_protected_areas_fr._download` |
| `_zip_bytes` | `tests.unit.test_inpn_protected_areas_fr._zip_bytes` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `first.path.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `_download_metadata_path` | `tests.unit.test_inpn_protected_areas_fr._download_metadata_path` |
| `_read_json` | `tests.unit.test_inpn_protected_areas_fr._read_json` |
| `sha256(replacement).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |
| `_write_json` | `tests.unit.test_inpn_protected_areas_fr._write_json` |
| `_Session` | `tests.unit.test_inpn_protected_areas_fr._Session` |
| `SafeHttpsError` | `landscout.common.safe_http.SafeHttpsError` |
| `pytest.raises` | `pytest.raises` |
| `_download_with_session` | `tests.unit.test_inpn_protected_areas_fr._download_with_session` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `first.path.write_bytes` |
| Hashing/byte identity | `sha256(replacement).hexdigest`<br>`sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `metadata["file_size"] = len(replacement)`<br>`metadata["sha256"] = sha256(replacement).hexdigest()` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_http_and_payload_failures_are_controlled`

**Purpose:** Regression invariant: http and payload failures are controlled. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_http_and_payload_failures_are_controlled(
    tmp_path: Path,
    payload: bytes,
    status: int,
    error: Exception | None,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
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
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `payload` | positional-or-keyword | `bytes` | `required` |
| `status` | positional-or-keyword | `int` | `required` |
| `error` | positional-or-keyword | `Exception \| None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(InpnProtectedAreasSourceError)`
- Exact assertions:
  - `assert not list(Path(config.cache_root).rglob("*.part"))`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_config` | `tests.unit.test_inpn_protected_areas_fr._config` |
| `_Session` | `tests.unit.test_inpn_protected_areas_fr._Session` |
| `_session` | `tests.unit.test_inpn_protected_areas_fr._session` |
| `pytest.raises` | `pytest.raises` |
| `_download_with_session` | `tests.unit.test_inpn_protected_areas_fr._download_with_session` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `Path(config.cache_root).rglob` | `unresolved local/third-party receiver; no ownership inferred` |
| `Path` | `pathlib.Path` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `_zip_bytes` | `tests.unit.test_inpn_protected_areas_fr._zip_bytes` |
| `OSError` | `unresolved local/third-party receiver; no ownership inferred` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unsupported_zip_compression_has_controlled_error`

**Purpose:** Regression invariant: unsupported zip compression has controlled error. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_unsupported_zip_compression_has_controlled_error(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(InpnProtectedAreasSourceError, match="ZIP\|archive")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_unsupported_compression_zip` | `tests.unit.test_inpn_protected_areas_fr._unsupported_compression_zip` |
| `_config` | `tests.unit.test_inpn_protected_areas_fr._config` |
| `pytest.raises` | `pytest.raises` |
| `_download_with_session` | `tests.unit.test_inpn_protected_areas_fr._download_with_session` |
| `_session` | `tests.unit.test_inpn_protected_areas_fr._session` |

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
def test_unsupported_zip_compression_has_controlled_error(tmp_path: Path) -> None:
    payload = _unsupported_compression_zip()
    config = _config(tmp_path, payload)

    with pytest.raises(InpnProtectedAreasSourceError, match="ZIP|archive"):
        _download_with_session(config, _session(config, payload))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_malformed_response_headers_have_controlled_error`

**Purpose:** Regression invariant: malformed response headers have controlled error. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_malformed_response_headers_have_controlled_error(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(InpnProtectedAreasSourceError, match="response\|download")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_config` | `tests.unit.test_inpn_protected_areas_fr._config` |
| `_Response` | `tests.unit.test_inpn_protected_areas_fr._Response` |
| `_zip_bytes` | `tests.unit.test_inpn_protected_areas_fr._zip_bytes` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_download_with_session` | `tests.unit.test_inpn_protected_areas_fr._download_with_session` |
| `_Session` | `tests.unit.test_inpn_protected_areas_fr._Session` |

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
| In-memory mutation | `response.headers = None` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_malformed_response_headers_have_controlled_error(tmp_path: Path) -> None:
    config = _config(tmp_path)
    response = _Response(_zip_bytes(), url=str(config.archive_url))
    response.headers = None  # type: ignore[assignment]

    with pytest.raises(InpnProtectedAreasSourceError, match="response|download"):
        _download_with_session(config, _Session(response))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_midstream_protocol_failure_has_controlled_error`

**Purpose:** Regression invariant: midstream protocol failure has controlled error. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_midstream_protocol_failure_has_controlled_error(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(InpnProtectedAreasSourceError, match="response\|download")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_config` | `tests.unit.test_inpn_protected_areas_fr._config` |
| `_Response` | `tests.unit.test_inpn_protected_areas_fr._Response` |
| `_zip_bytes` | `tests.unit.test_inpn_protected_areas_fr._zip_bytes` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `_FailingRaw` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_download_with_session` | `tests.unit.test_inpn_protected_areas_fr._download_with_session` |
| `_Session` | `tests.unit.test_inpn_protected_areas_fr._Session` |

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
| In-memory mutation | `response.raw = _FailingRaw()` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_midstream_protocol_failure_has_controlled_error._FailingRaw.seek`

**Purpose:** Implements `seek` within the file role: Provides complete unit and regression coverage for the `inpn_protected_areas_fr` contracts exercised in this file.

**Exact signature**

```python
def seek(self, offset: int) -> int:
```

- Exact decorators: none.
- Declared return annotation: `int`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |
| `offset` | positional-or-keyword | `int` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `offset`
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
def seek(self, offset: int) -> int:
            return offset
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_midstream_protocol_failure_has_controlled_error._FailingRaw.read`

**Purpose:** Implements `read` within the file role: Provides complete unit and regression coverage for the `inpn_protected_areas_fr` contracts exercised in this file.

**Exact signature**

```python
def read(self, size: int = -1) -> bytes:
```

- Exact decorators: none.
- Declared return annotation: `bytes`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |
| `size` | positional-or-keyword | `int` | `-1` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `OSError("connection ended mid-stream")`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `OSError` | `unresolved local/third-party receiver; no ownership inferred` |

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
def read(self, size: int = -1) -> bytes:
            raise OSError("connection ended mid-stream")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_valid_physical_and_metadata_cache_is_reused`

**Purpose:** Regression invariant: valid physical and metadata cache is reused. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_valid_physical_and_metadata_cache_is_reused(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert second.cache_hit is True`
  - `assert second.file_size == first.file_size`
  - `assert second.sha256 == first.sha256`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_download` | `tests.unit.test_inpn_protected_areas_fr._download` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `download_inpn_protected_areas_archive` | `landscout.sources.inpn_protected_areas_fr.download_inpn_protected_areas_archive` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_valid_physical_and_metadata_cache_is_reused.fail_dns`

**Purpose:** Implements `fail dns` within the file role: Provides complete unit and regression coverage for the `inpn_protected_areas_fr` contracts exercised in this file.

**Exact signature**

```python
def fail_dns(*args: object, **kwargs: object) -> list[tuple[Any, ...]]:
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
  - `AssertionError("DNS used for valid cache hit")`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `AssertionError` | `unresolved local/third-party receiver; no ownership inferred` |

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
def fail_dns(*args: object, **kwargs: object) -> list[tuple[Any, ...]]:
        raise AssertionError("DNS used for valid cache hit")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_valid_physical_and_metadata_cache_is_reused.fail_http`

**Purpose:** Implements `fail http` within the file role: Provides complete unit and regression coverage for the `inpn_protected_areas_fr` contracts exercised in this file.

**Exact signature**

```python
def fail_http(*args: object, **kwargs: object) -> Any:
```

- Exact decorators: none.
- Declared return annotation: `Any`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `AssertionError("HTTP used for valid cache hit")`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `AssertionError` | `unresolved local/third-party receiver; no ownership inferred` |

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
def fail_http(*args: object, **kwargs: object) -> Any:
        raise AssertionError("HTTP used for valid cache hit")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_invalid_download_cache_is_a_miss`

**Purpose:** Regression invariant: invalid download cache is a miss. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_invalid_download_cache_is_a_miss(
    tmp_path: Path,
    mutation: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
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
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `mutation` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert len(replacement) == first.file_size`
  - `assert refreshed.cache_hit is False`
  - `assert len(session.calls) == 1`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_download` | `tests.unit.test_inpn_protected_areas_fr._download` |
| `_download_metadata_path` | `tests.unit.test_inpn_protected_areas_fr._download_metadata_path` |
| `_read_json` | `tests.unit.test_inpn_protected_areas_fr._read_json` |
| `first.path.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `_zip_bytes` | `tests.unit.test_inpn_protected_areas_fr._zip_bytes` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `_write_json` | `tests.unit.test_inpn_protected_areas_fr._write_json` |
| `json.dumps` | `json.dumps` |
| `metadata_path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_json.replace` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256(invalid_zip).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |
| `_session` | `tests.unit.test_inpn_protected_areas_fr._session` |
| `_download_with_session` | `tests.unit.test_inpn_protected_areas_fr._download_with_session` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `first.path.write_bytes`<br>`metadata_path.write_text`<br>`metadata_json.replace` |
| Hashing/byte identity | `sha256(invalid_zip).hexdigest`<br>`sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `metadata["sha256"] = "0" * 64`<br>`metadata["file_size"] = first.file_size + 1`<br>`metadata["archive_url"] = "https://example.test/EP.zip"`<br>`metadata["declared_version"] = "06/2026"`<br>`metadata["schema_version"] = schema_values[mutation]`<br>`metadata["unexpected"] = True`<br>`metadata["download_timestamp"] = "2026-08-16T12:00:00"`<br>`metadata["file_size"] = len(invalid_zip)`<br>`metadata["sha256"] = sha256(invalid_zip).hexdigest()` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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
    elif mutation in {
        "metadata_schema",
        "metadata_schema_bool",
        "metadata_schema_float",
    }:
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_force_cache_miss`

**Purpose:** Implements `force cache miss` within the file role: Provides complete unit and regression coverage for the `inpn_protected_areas_fr` contracts exercised in this file.

**Exact signature**

```python
def _force_cache_miss(download: InpnProtectedAreasDownload) -> tuple[Path, bytes]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[Path, bytes]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `download` | positional-or-keyword | `InpnProtectedAreasDownload` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `metadata_path, metadata_path.read_bytes()`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_successful_first_and_replacement_publication` via `_force_cache_miss`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_successful_first_and_replacement_publication` via `_force_cache_miss`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_publication_failure_restores_old_pair` via `_force_cache_miss`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_publication_failure_restores_old_pair` via `_force_cache_miss`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_download_metadata_path` | `tests.unit.test_inpn_protected_areas_fr._download_metadata_path` |
| `_read_json` | `tests.unit.test_inpn_protected_areas_fr._read_json` |
| `_write_json` | `tests.unit.test_inpn_protected_areas_fr._write_json` |
| `metadata_path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `metadata_path.read_bytes` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `metadata["sha256"] = "0" * 64` |
| Direct parameter mutation | None directly present. |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_successful_first_and_replacement_publication`

**Purpose:** Regression invariant: successful first and replacement publication. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_successful_first_and_replacement_publication(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert second.cache_hit is False`
  - `assert second.path.read_bytes() == replacement`
  - `assert _read_json(_download_metadata_path(second))["sha256"] == second.sha256`
  - `assert not list(Path(config.cache_root).rglob("*.part"))`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_download` | `tests.unit.test_inpn_protected_areas_fr._download` |
| `_force_cache_miss` | `tests.unit.test_inpn_protected_areas_fr._force_cache_miss` |
| `_zip_bytes` | `tests.unit.test_inpn_protected_areas_fr._zip_bytes` |
| `_download_with_session` | `tests.unit.test_inpn_protected_areas_fr._download_with_session` |
| `_session` | `tests.unit.test_inpn_protected_areas_fr._session` |
| `second.path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `_read_json` | `tests.unit.test_inpn_protected_areas_fr._read_json` |
| `_download_metadata_path` | `tests.unit.test_inpn_protected_areas_fr._download_metadata_path` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `Path(config.cache_root).rglob` | `unresolved local/third-party receiver; no ownership inferred` |
| `Path` | `pathlib.Path` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `second.path.read_bytes` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_publication_failure_restores_old_pair`

**Purpose:** Regression invariant: publication failure restores old pair. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_publication_failure_restores_old_pair(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    failure_target: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("failure_target", ["archive", "metadata"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |
| `failure_target` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(InpnProtectedAreasSourceError, match="publication\|download")`
- Exact assertions:
  - `assert first.path.read_bytes() == old_archive`
  - `assert metadata_path.read_bytes() == old_metadata`
  - `assert not list(Path(config.cache_root).rglob("*.part"))`
  - `assert not list(Path(config.cache_root).rglob("*.bak"))`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_download` | `tests.unit.test_inpn_protected_areas_fr._download` |
| `_force_cache_miss` | `tests.unit.test_inpn_protected_areas_fr._force_cache_miss` |
| `first.path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_download_with_session` | `tests.unit.test_inpn_protected_areas_fr._download_with_session` |
| `_session` | `tests.unit.test_inpn_protected_areas_fr._session` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `Path(config.cache_root).rglob` | `unresolved local/third-party receiver; no ownership inferred` |
| `Path` | `pathlib.Path` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `first.path.read_bytes`<br>`metadata_path.read_bytes` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_publication_failure_restores_old_pair.fail_once`

**Purpose:** Implements `fail once` within the file role: Provides complete unit and regression coverage for the `inpn_protected_areas_fr` contracts exercised in this file.

**Exact signature**

```python
def fail_once(source: Path, target: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source` | positional-or-keyword | `Path` | `required` |
| `target` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `OSError("publication failed")` under lexical guard `source.name.endswith(".part") and target == wanted and not failed`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `source.name.endswith` | `unresolved local/third-party receiver; no ownership inferred` |
| `OSError` | `unresolved local/third-party receiver; no ownership inferred` |
| `original_replace` | `unresolved local/third-party receiver; no ownership inferred` |

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
def fail_once(source: Path, target: Path) -> None:
        nonlocal failed
        wanted = first.path if failure_target == "archive" else metadata_path
        if source.name.endswith(".part") and target == wanted and not failed:
            failed = True
            raise OSError("publication failed")
        original_replace(source, target)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_rollback_failure_preserves_recovery_material`

**Purpose:** Regression invariant: rollback failure preserves recovery material. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_rollback_failure_preserves_recovery_material(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(InpnProtectedAreasSourceError, match="rollback")`
- Exact assertions:
  - `assert archive_backup.read_bytes() == old_archive`
  - `assert metadata_backup.read_bytes() == old_metadata`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_download` | `tests.unit.test_inpn_protected_areas_fr._download` |
| `_download_metadata_path` | `tests.unit.test_inpn_protected_areas_fr._download_metadata_path` |
| `first.path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_download_with_session` | `tests.unit.test_inpn_protected_areas_fr._download_with_session` |
| `_session` | `tests.unit.test_inpn_protected_areas_fr._session` |
| `first.path.with_name` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.with_name` | `unresolved local/third-party receiver; no ownership inferred` |
| `archive_backup.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_backup.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `first.path.read_bytes`<br>`metadata_path.read_bytes`<br>`archive_backup.read_bytes`<br>`metadata_backup.read_bytes` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_rollback_failure_preserves_recovery_material.fail_publication_and_rollback`

**Purpose:** Implements `fail publication and rollback` within the file role: Provides complete unit and regression coverage for the `inpn_protected_areas_fr` contracts exercised in this file.

**Exact signature**

```python
def fail_publication_and_rollback(source: Path, target: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source` | positional-or-keyword | `Path` | `required` |
| `target` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `OSError("publication failed")` under lexical guard `source.name.endswith(".part") and target == metadata_path`.
  - `OSError("rollback failed")` under lexical guard `source.name.endswith(".bak")`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `source.name.endswith` | `unresolved local/third-party receiver; no ownership inferred` |
| `OSError` | `unresolved local/third-party receiver; no ownership inferred` |
| `original_replace` | `unresolved local/third-party receiver; no ownership inferred` |

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
def fail_publication_and_rollback(source: Path, target: Path) -> None:
        if source.name.endswith(".part") and target == metadata_path:
            raise OSError("publication failed")
        if source.name.endswith(".bak"):
            raise OSError("rollback failed")
        original_replace(source, target)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_broken_download_recovery_symlink_is_rejected`

**Purpose:** Regression invariant: broken download recovery symlink is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_broken_download_recovery_symlink_is_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    backup_role: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("backup_role", ["archive", "metadata"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |
| `backup_role` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(InpnProtectedAreasSourceError, match="backup\|recovery\|manual")`
- Exact assertions:
  - `assert not archive_path.exists()`
  - `assert not metadata_path.exists()`
  - `assert temporary_archive.read_bytes() == b"replacement archive"`
  - `assert temporary_metadata.read_bytes() == b"replacement metadata"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `temporary_archive.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `temporary_metadata.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `archive_path.with_name` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.with_name` | `unresolved local/third-party receiver; no ownership inferred` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `inpn._publish_cache_pair` | `landscout.sources.inpn_protected_areas_fr._publish_cache_pair` |
| `archive_path.exists` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.exists` | `unresolved local/third-party receiver; no ownership inferred` |
| `temporary_archive.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `temporary_metadata.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `archive_path.exists`<br>`metadata_path.exists`<br>`temporary_archive.read_bytes`<br>`temporary_metadata.read_bytes` |
| Filesystem/archive write or publication | `temporary_archive.write_bytes`<br>`temporary_metadata.write_bytes` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_broken_download_recovery_symlink_is_rejected.simulated_is_symlink`

**Purpose:** Implements `simulated is symlink` within the file role: Provides complete unit and regression coverage for the `inpn_protected_areas_fr` contracts exercised in this file.

**Exact signature**

```python
def simulated_is_symlink(path: Path) -> bool:
```

- Exact decorators: none.
- Declared return annotation: `bool`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `path == broken_link or original_is_symlink(path)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `original_is_symlink` | `unresolved local/third-party receiver; no ownership inferred` |

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
def simulated_is_symlink(path: Path) -> bool:
        return path == broken_link or original_is_symlink(path)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_existing_normal_download_recovery_backup_remains_unchanged`

**Purpose:** Regression invariant: existing normal download recovery backup remains unchanged. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_existing_normal_download_recovery_backup_remains_unchanged(
    tmp_path: Path,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(InpnProtectedAreasSourceError, match="backup\|recovery\|manual")`
- Exact assertions:
  - `assert archive_backup.read_bytes() == recovery_bytes`
  - `assert temporary_archive.read_bytes() == b"replacement archive"`
  - `assert temporary_metadata.read_bytes() == b"replacement metadata"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `archive_path.with_name` | `unresolved local/third-party receiver; no ownership inferred` |
| `temporary_archive.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `temporary_metadata.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `archive_backup.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `inpn._publish_cache_pair` | `landscout.sources.inpn_protected_areas_fr._publish_cache_pair` |
| `archive_backup.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `temporary_archive.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `temporary_metadata.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `archive_backup.read_bytes`<br>`temporary_archive.read_bytes`<br>`temporary_metadata.read_bytes` |
| Filesystem/archive write or publication | `temporary_archive.write_bytes`<br>`temporary_metadata.write_bytes`<br>`archive_backup.write_bytes` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_failed_replacement_restores_a_still_reusable_valid_download_pair`

**Purpose:** Regression invariant: failed replacement restores a still reusable valid download pair. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_failed_replacement_restores_a_still_reusable_valid_download_pair(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(InpnProtectedAreasSourceError, match="publication")`
- Exact assertions:
  - `assert first.path.read_bytes() == old_archive`
  - `assert metadata_path.read_bytes() == old_metadata`
  - `assert reused.cache_hit is True`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_download` | `tests.unit.test_inpn_protected_areas_fr._download` |
| `_download_metadata_path` | `tests.unit.test_inpn_protected_areas_fr._download_metadata_path` |
| `first.path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_download_with_session` | `tests.unit.test_inpn_protected_areas_fr._download_with_session` |
| `_session` | `tests.unit.test_inpn_protected_areas_fr._session` |
| `_Session` | `tests.unit.test_inpn_protected_areas_fr._Session` |
| `AssertionError` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `first.path.read_bytes`<br>`metadata_path.read_bytes` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_failed_replacement_restores_a_still_reusable_valid_download_pair.fail_metadata`

**Purpose:** Implements `fail metadata` within the file role: Provides complete unit and regression coverage for the `inpn_protected_areas_fr` contracts exercised in this file.

**Exact signature**

```python
def fail_metadata(source: Path, target: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source` | positional-or-keyword | `Path` | `required` |
| `target` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `OSError("publication failed")` under lexical guard `source.name.endswith(".part") and target == metadata_path`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `source.name.endswith` | `unresolved local/third-party receiver; no ownership inferred` |
| `OSError` | `unresolved local/third-party receiver; no ownership inferred` |
| `original_replace` | `unresolved local/third-party receiver; no ownership inferred` |

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
def fail_metadata(source: Path, target: Path) -> None:
        if source.name.endswith(".part") and target == metadata_path:
            raise OSError("publication failed")
        original_replace(source, target)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unsafe_zip_member_paths_are_rejected`

**Purpose:** Regression invariant: unsafe zip member paths are rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_unsafe_zip_member_paths_are_rejected(
    tmp_path: Path,
    member_name: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
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
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `member_name` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(InpnProtectedAreasSourceError, match="ZIP\|archive\|member\|path")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_zip_bytes` | `tests.unit.test_inpn_protected_areas_fr._zip_bytes` |
| `_config` | `tests.unit.test_inpn_protected_areas_fr._config` |
| `pytest.raises` | `pytest.raises` |
| `_download_with_session` | `tests.unit.test_inpn_protected_areas_fr._download_with_session` |
| `_session` | `tests.unit.test_inpn_protected_areas_fr._session` |
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
def test_unsafe_zip_member_paths_are_rejected(
    tmp_path: Path,
    member_name: str,
) -> None:
    payload = _zip_bytes([(member_name, b"bad")])
    config = _config(tmp_path, payload)
    with pytest.raises(InpnProtectedAreasSourceError, match="ZIP|archive|member|path"):
        _download_with_session(config, _session(config, payload))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_duplicate_or_colliding_zip_destinations_are_rejected`

**Purpose:** Regression invariant: duplicate or colliding zip destinations are rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_duplicate_or_colliding_zip_destinations_are_rejected(
    tmp_path: Path,
    members: list[tuple[str, bytes]],
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "members",
    [
        [("same.txt", b"a"), ("same.txt", b"b")],
        [("folder/file.txt", b"a"), (r"folder\file.txt", b"b")],
        [("folder/file.txt", b"a"), ("folder/./file.txt", b"b")],
        [("Folder/File.txt", b"a"), ("folder/file.txt", b"b")],
        [("blocked", b"a"), ("blocked/child.txt", b"b")],
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `members` | positional-or-keyword | `list[tuple[str, bytes]]` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(InpnProtectedAreasSourceError, match="duplicate\|collid\|archive")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_zip_bytes` | `tests.unit.test_inpn_protected_areas_fr._zip_bytes` |
| `_config` | `tests.unit.test_inpn_protected_areas_fr._config` |
| `pytest.raises` | `pytest.raises` |
| `_download_with_session` | `tests.unit.test_inpn_protected_areas_fr._download_with_session` |
| `_session` | `tests.unit.test_inpn_protected_areas_fr._session` |
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
def test_duplicate_or_colliding_zip_destinations_are_rejected(
    tmp_path: Path,
    members: list[tuple[str, bytes]],
) -> None:
    payload = _zip_bytes(members)
    config = _config(tmp_path, payload)
    with pytest.raises(InpnProtectedAreasSourceError, match="duplicate|collid|archive"):
        _download_with_session(config, _session(config, payload))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_zip_links_and_special_files_are_rejected`

**Purpose:** Regression invariant: zip links and special files are rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_zip_links_and_special_files_are_rejected(
    tmp_path: Path,
    mode: int,
    message: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("mode", "message"),
    [(stat.S_IFLNK | 0o777, "symbolic|link"), (stat.S_IFIFO | 0o644, "special")],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `mode` | positional-or-keyword | `int` | `required` |
| `message` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(InpnProtectedAreasSourceError, match=message)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_special_zip` | `tests.unit.test_inpn_protected_areas_fr._special_zip` |
| `_config` | `tests.unit.test_inpn_protected_areas_fr._config` |
| `pytest.raises` | `pytest.raises` |
| `_download_with_session` | `tests.unit.test_inpn_protected_areas_fr._download_with_session` |
| `_session` | `tests.unit.test_inpn_protected_areas_fr._session` |
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_complete_zip_inventory_is_validated_before_member_copy`

**Purpose:** Regression invariant: complete zip inventory is validated before member copy. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_complete_zip_inventory_is_validated_before_member_copy(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(InpnProtectedAreasSourceError)`
- Exact assertions:
  - `assert opened == 0`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_zip_bytes` | `tests.unit.test_inpn_protected_areas_fr._zip_bytes` |
| `_config` | `tests.unit.test_inpn_protected_areas_fr._config` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_download_with_session` | `tests.unit.test_inpn_protected_areas_fr._download_with_session` |
| `_session` | `tests.unit.test_inpn_protected_areas_fr._session` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_complete_zip_inventory_is_validated_before_member_copy.record_open`

**Purpose:** Implements `record open` within the file role: Provides complete unit and regression coverage for the `inpn_protected_areas_fr` contracts exercised in this file.

**Exact signature**

```python
def record_open(self: zipfile.ZipFile, *args: object, **kwargs: object) -> Any:
```

- Exact decorators: none.
- Declared return annotation: `Any`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `zipfile.ZipFile` | `required` |
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- Exact observed return expressions:
  - `original_open(self, *args, **kwargs)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `original_open` | `unresolved local/third-party receiver; no ownership inferred` |

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
def record_open(self: zipfile.ZipFile, *args: object, **kwargs: object) -> Any:
        nonlocal opened
        opened += 1
        return original_open(self, *args, **kwargs)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_extraction_validates_complete_inventory_before_copying`

**Purpose:** Regression invariant: extraction validates complete inventory before copying. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_extraction_validates_complete_inventory_before_copying(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(InpnProtectedAreasSourceError)`
- Exact assertions:
  - `assert copied == 0`
  - `assert not (download.path.parent / "x" / forged.sha256).exists()`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_download` | `tests.unit.test_inpn_protected_areas_fr._download` |
| `_zip_bytes` | `tests.unit.test_inpn_protected_areas_fr._zip_bytes` |
| `download.path.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256(payload).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `extract_inpn_protected_areas_archive` | `landscout.sources.inpn_protected_areas_fr.extract_inpn_protected_areas_archive` |
| `(download.path.parent / "x" / forged.sha256).exists` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `(download.path.parent / "x" / forged.sha256).exists` |
| Filesystem/archive write or publication | `download.path.write_bytes` |
| Hashing/byte identity | `sha256(payload).hexdigest`<br>`sha256`<br>`(download.path.parent / "x" / forged.sha256).exists` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_extraction_validates_complete_inventory_before_copying.record_copy`

**Purpose:** Implements `record copy` within the file role: Provides complete unit and regression coverage for the `inpn_protected_areas_fr` contracts exercised in this file.

**Exact signature**

```python
def record_copy(*args: object, **kwargs: object) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `original_copy` | `unresolved local/third-party receiver; no ownership inferred` |

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
def record_copy(*args: object, **kwargs: object) -> None:
        nonlocal copied
        copied += 1
        original_copy(*args, **kwargs)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_normal_nested_members_are_accepted`

**Purpose:** Regression invariant: normal nested members are accepted. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_normal_nested_members_are_accepted(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert download.path.is_file()`
  - `assert download.filename == config.archive_filename`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_download` | `tests.unit.test_inpn_protected_areas_fr._download` |
| `_zip_bytes` | `tests.unit.test_inpn_protected_areas_fr._zip_bytes` |
| `download.path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `download.path.is_file` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_normal_nested_members_are_accepted(tmp_path: Path) -> None:
    config, download, _ = _download(
        tmp_path,
        payload=_zip_bytes({"EP/docs/readme.txt": b"ok"}),
    )

    assert download.path.is_file()
    assert download.filename == config.archive_filename
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_extraction_inventory_is_complete_ordered_and_hashed`

**Purpose:** Regression invariant: extraction inventory is complete ordered and hashed. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_extraction_inventory_is_complete_ordered_and_hashed(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert extraction.cache_hit is False`
  - `assert [item.relative_path for item in extraction.files] == expected_paths`
  - `assert len(extraction.files) == len(payloads)`
  - `assert item.file_size == len(payload)`
  - `assert item.sha256 == sha256(payload).hexdigest()`
  - `assert (<br>            extraction.extraction_path.joinpath(*relative_path.split("/")).read_bytes()<br>            == payload<br>        )`
  - `assert by_path["z-last/empty.cpg"].file_size == 0`
  - `assert by_path["z-last/empty.cpg"].sha256 == sha256(b"").hexdigest()`
  - `assert metadata["schema_version"] == 1`
  - `assert metadata["archive_sha256"] == download.sha256`
  - `assert metadata["archive_size"] == download.file_size`
  - `assert not list(extraction.extraction_path.parent.glob("*.part"))`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_download` | `tests.unit.test_inpn_protected_areas_fr._download` |
| `_zip_bytes` | `tests.unit.test_inpn_protected_areas_fr._zip_bytes` |
| `extract_inpn_protected_areas_archive` | `landscout.sources.inpn_protected_areas_fr.extract_inpn_protected_areas_archive` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `payloads.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256(payload).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |
| `extraction.extraction_path.joinpath(*relative_path.split("/")).read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `extraction.extraction_path.joinpath` | `unresolved local/third-party receiver; no ownership inferred` |
| `relative_path.split` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256(b"").hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `_read_json` | `tests.unit.test_inpn_protected_areas_fr._read_json` |
| `_extraction_metadata_path` | `tests.unit.test_inpn_protected_areas_fr._extraction_metadata_path` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `extraction.extraction_path.parent.glob` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `extraction.extraction_path.joinpath(*relative_path.split("/")).read_bytes`<br>`extraction.extraction_path.parent.glob` |
| Filesystem/archive write or publication | `extraction.extraction_path.joinpath(*relative_path.split("/")).read_bytes`<br>`extraction.extraction_path.joinpath`<br>`extraction.extraction_path.parent.glob` |
| Hashing/byte identity | `sha256(payload).hexdigest`<br>`sha256`<br>`sha256(b"").hexdigest` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_valid_extraction_cache_is_reused`

**Purpose:** Regression invariant: valid extraction cache is reused. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_valid_extraction_cache_is_reused(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert second.cache_hit is True`
  - `assert second.files == first.files`
  - `assert second.extraction_path == first.extraction_path`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_download` | `tests.unit.test_inpn_protected_areas_fr._download` |
| `extract_inpn_protected_areas_archive` | `landscout.sources.inpn_protected_areas_fr.extract_inpn_protected_areas_archive` |

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
def test_valid_extraction_cache_is_reused(tmp_path: Path) -> None:
    config, download, _ = _download(tmp_path)
    first = extract_inpn_protected_areas_archive(download, config)

    second = extract_inpn_protected_areas_archive(download, config)

    assert second.cache_hit is True
    assert second.files == first.files
    assert second.extraction_path == first.extraction_path
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_invalid_extraction_cache_is_rebuilt`

**Purpose:** Regression invariant: invalid extraction cache is rebuilt. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_invalid_extraction_cache_is_rebuilt(
    tmp_path: Path,
    mutation: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
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
        "duplicate_key",
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `mutation` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert data_path.stat().st_size == len(original)`
  - `assert isinstance(file_entries, list)`
  - `assert isinstance(file_entries[0], dict)`
  - `assert refreshed.cache_hit is False`
  - `assert (refreshed.extraction_path / "EP" / "value.txt").read_bytes() == original`
  - `assert not (refreshed.extraction_path / "unexpected.txt").exists()`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_download` | `tests.unit.test_inpn_protected_areas_fr._download` |
| `_zip_bytes` | `tests.unit.test_inpn_protected_areas_fr._zip_bytes` |
| `extract_inpn_protected_areas_archive` | `landscout.sources.inpn_protected_areas_fr.extract_inpn_protected_areas_archive` |
| `_extraction_metadata_path` | `tests.unit.test_inpn_protected_areas_fr._extraction_metadata_path` |
| `_read_json` | `tests.unit.test_inpn_protected_areas_fr._read_json` |
| `data_path.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `data_path.stat` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `data_path.unlink` | `unresolved local/third-party receiver; no ownership inferred` |
| `(first.extraction_path / "unexpected.txt").write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `_write_json` | `tests.unit.test_inpn_protected_areas_fr._write_json` |
| `json.dumps` | `json.dumps` |
| `metadata_path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `encoded.replace` | `unresolved local/third-party receiver; no ownership inferred` |
| `(refreshed.extraction_path / "EP" / "value.txt").read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `(refreshed.extraction_path / "unexpected.txt").exists` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `data_path.stat`<br>`(refreshed.extraction_path / "EP" / "value.txt").read_bytes`<br>`(refreshed.extraction_path / "unexpected.txt").exists` |
| Filesystem/archive write or publication | `data_path.write_bytes`<br>`data_path.unlink`<br>`(first.extraction_path / "unexpected.txt").write_bytes`<br>`metadata_path.write_text`<br>`encoded.replace`<br>`(refreshed.extraction_path / "EP" / "value.txt").read_bytes`<br>`(refreshed.extraction_path / "unexpected.txt").exists` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `file_entries[0]["sha256"] = "0" * 64`<br>`metadata["archive_sha256"] = "0" * 64`<br>`metadata["archive_size"] = download.file_size + 1`<br>`metadata["schema_version"] = schema_values[mutation]`<br>`metadata["unexpected"] = True`<br>`file_entries[0]["file_size"] = True` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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
    elif mutation == "boolean_file_size":
        file_entries = metadata["files"]
        assert isinstance(file_entries, list)
        assert isinstance(file_entries[0], dict)
        file_entries[0]["file_size"] = True
        _write_json(metadata_path, metadata)
    else:
        encoded = json.dumps(metadata, separators=(",", ":"))
        marker = '"schema_version":1'
        metadata_path.write_text(
            encoded.replace(marker, f"{marker},{marker}", 1),
            encoding="utf-8",
        )

    refreshed = extract_inpn_protected_areas_archive(download, config)

    assert refreshed.cache_hit is False
    assert (refreshed.extraction_path / "EP" / "value.txt").read_bytes() == original
    assert not (refreshed.extraction_path / "unexpected.txt").exists()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_tree_snapshot`

**Purpose:** Implements `tree snapshot` within the file role: Provides complete unit and regression coverage for the `inpn_protected_areas_fr` contracts exercised in this file.

**Exact signature**

```python
def _tree_snapshot(root: Path) -> dict[str, bytes]:
```

- Exact decorators: none.
- Declared return annotation: `dict[str, bytes]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `root` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `{<br>        path.relative_to(root).as_posix(): path.read_bytes()<br>        for path in sorted(root.rglob("*"))<br>        if path.is_file()<br>    }`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_extraction_replacement_failure_restores_old_tree` via `_tree_snapshot`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_extraction_replacement_failure_restores_old_tree` via `_tree_snapshot`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_extraction_rollback_failure_preserves_backup` via `_tree_snapshot`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_extraction_rollback_failure_preserves_backup` via `_tree_snapshot`
- direct call: `tests.unit.test_inpn_protected_areas_fr::test_extraction_backup_move_failure_leaves_old_tree_untouched` via `_tree_snapshot`
- value/type reference: `tests.unit.test_inpn_protected_areas_fr::test_extraction_backup_move_failure_leaves_old_tree_untouched` via `_tree_snapshot`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.relative_to(root).as_posix` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.relative_to` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `root.rglob` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `path.read_bytes`<br>`path.is_file` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_first_extraction_publication_failure_leaves_no_half_root`

**Purpose:** Regression invariant: first extraction publication failure leaves no half root. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_first_extraction_publication_failure_leaves_no_half_root(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(InpnProtectedAreasSourceError, match="publication")`
- Exact assertions:
  - `assert not root.exists()`
  - `assert not root.with_name(f"{root.name}.part").exists()`
  - `assert not root.with_name(f"{root.name}.bak").exists()`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_download` | `tests.unit.test_inpn_protected_areas_fr._download` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `extract_inpn_protected_areas_archive` | `landscout.sources.inpn_protected_areas_fr.extract_inpn_protected_areas_archive` |
| `root.exists` | `unresolved local/third-party receiver; no ownership inferred` |
| `root.with_name(f"{root.name}.part").exists` | `unresolved local/third-party receiver; no ownership inferred` |
| `root.with_name` | `unresolved local/third-party receiver; no ownership inferred` |
| `root.with_name(f"{root.name}.bak").exists` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `root.exists`<br>`root.with_name(f"{root.name}.part").exists`<br>`root.with_name(f"{root.name}.bak").exists` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_first_extraction_publication_failure_leaves_no_half_root.fail_publish`

**Purpose:** Implements `fail publish` within the file role: Provides complete unit and regression coverage for the `inpn_protected_areas_fr` contracts exercised in this file.

**Exact signature**

```python
def fail_publish(source: Path, target: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source` | positional-or-keyword | `Path` | `required` |
| `target` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `OSError("publication failed")` under lexical guard `source.name.endswith(".part") and target == root`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `source.name.endswith` | `unresolved local/third-party receiver; no ownership inferred` |
| `OSError` | `unresolved local/third-party receiver; no ownership inferred` |
| `original_replace` | `unresolved local/third-party receiver; no ownership inferred` |

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
def fail_publish(source: Path, target: Path) -> None:
        if source.name.endswith(".part") and target == root:
            raise OSError("publication failed")
        original_replace(source, target)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_extraction_replacement_failure_restores_old_tree`

**Purpose:** Regression invariant: extraction replacement failure restores old tree. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_extraction_replacement_failure_restores_old_tree(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(InpnProtectedAreasSourceError, match="publication")`
- Exact assertions:
  - `assert _tree_snapshot(first.extraction_path) == before`
  - `assert not first.extraction_path.with_name(<br>        f"{first.extraction_path.name}.bak"<br>    ).exists()`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_download` | `tests.unit.test_inpn_protected_areas_fr._download` |
| `extract_inpn_protected_areas_archive` | `landscout.sources.inpn_protected_areas_fr.extract_inpn_protected_areas_archive` |
| `(first.extraction_path / "EP" / "readme.txt").write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `_tree_snapshot` | `tests.unit.test_inpn_protected_areas_fr._tree_snapshot` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `first.extraction_path.with_name(<br>        f"{first.extraction_path.name}.bak"<br>    ).exists` | `unresolved local/third-party receiver; no ownership inferred` |
| `first.extraction_path.with_name` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `first.extraction_path.with_name(<br>        f"{first.extraction_path.name}.bak"<br>    ).exists` |
| Filesystem/archive write or publication | `(first.extraction_path / "EP" / "readme.txt").write_bytes`<br>`first.extraction_path.with_name(<br>        f"{first.extraction_path.name}.bak"<br>    ).exists`<br>`first.extraction_path.with_name` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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
        if (
            source.name.endswith(".part")
            and target == first.extraction_path
            and not failed
        ):
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_extraction_replacement_failure_restores_old_tree.fail_once`

**Purpose:** Implements `fail once` within the file role: Provides complete unit and regression coverage for the `inpn_protected_areas_fr` contracts exercised in this file.

**Exact signature**

```python
def fail_once(source: Path, target: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source` | positional-or-keyword | `Path` | `required` |
| `target` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `OSError("publication failed")` under lexical guard `source.name.endswith(".part")<br>            and target == first.extraction_path<br>            and not failed`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `source.name.endswith` | `unresolved local/third-party receiver; no ownership inferred` |
| `OSError` | `unresolved local/third-party receiver; no ownership inferred` |
| `original_replace` | `unresolved local/third-party receiver; no ownership inferred` |

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
def fail_once(source: Path, target: Path) -> None:
        nonlocal failed
        if (
            source.name.endswith(".part")
            and target == first.extraction_path
            and not failed
        ):
            failed = True
            raise OSError("publication failed")
        original_replace(source, target)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_extraction_rollback_failure_preserves_backup`

**Purpose:** Regression invariant: extraction rollback failure preserves backup. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_extraction_rollback_failure_preserves_backup(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(InpnProtectedAreasSourceError, match="rollback")`
- Exact assertions:
  - `assert _tree_snapshot(backup) == before`
  - `assert not first.extraction_path.with_name(<br>        f"{first.extraction_path.name}.part"<br>    ).exists()`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_download` | `tests.unit.test_inpn_protected_areas_fr._download` |
| `extract_inpn_protected_areas_archive` | `landscout.sources.inpn_protected_areas_fr.extract_inpn_protected_areas_archive` |
| `(first.extraction_path / "EP" / "readme.txt").write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `_tree_snapshot` | `tests.unit.test_inpn_protected_areas_fr._tree_snapshot` |
| `first.extraction_path.with_name` | `unresolved local/third-party receiver; no ownership inferred` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `first.extraction_path.with_name(<br>        f"{first.extraction_path.name}.part"<br>    ).exists` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `first.extraction_path.with_name(<br>        f"{first.extraction_path.name}.part"<br>    ).exists` |
| Filesystem/archive write or publication | `(first.extraction_path / "EP" / "readme.txt").write_bytes`<br>`first.extraction_path.with_name`<br>`first.extraction_path.with_name(<br>        f"{first.extraction_path.name}.part"<br>    ).exists` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_extraction_rollback_failure_preserves_backup.fail_publish_and_rollback`

**Purpose:** Implements `fail publish and rollback` within the file role: Provides complete unit and regression coverage for the `inpn_protected_areas_fr` contracts exercised in this file.

**Exact signature**

```python
def fail_publish_and_rollback(source: Path, target: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source` | positional-or-keyword | `Path` | `required` |
| `target` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `OSError("publication failed")` under lexical guard `source.name.endswith(".part") and target == first.extraction_path`.
  - `OSError("rollback failed")` under lexical guard `source == backup and target == first.extraction_path`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `source.name.endswith` | `unresolved local/third-party receiver; no ownership inferred` |
| `OSError` | `unresolved local/third-party receiver; no ownership inferred` |
| `original_replace` | `unresolved local/third-party receiver; no ownership inferred` |

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
def fail_publish_and_rollback(source: Path, target: Path) -> None:
        if source.name.endswith(".part") and target == first.extraction_path:
            raise OSError("publication failed")
        if source == backup and target == first.extraction_path:
            raise OSError("rollback failed")
        original_replace(source, target)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_extraction_backup_move_failure_leaves_old_tree_untouched`

**Purpose:** Regression invariant: extraction backup move failure leaves old tree untouched. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_extraction_backup_move_failure_leaves_old_tree_untouched(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(InpnProtectedAreasSourceError, match="publication\|stage")`
- Exact assertions:
  - `assert first.extraction_path.is_dir()`
  - `assert _tree_snapshot(first.extraction_path) == before`
  - `assert not backup.exists()`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_download` | `tests.unit.test_inpn_protected_areas_fr._download` |
| `extract_inpn_protected_areas_archive` | `landscout.sources.inpn_protected_areas_fr.extract_inpn_protected_areas_archive` |
| `(first.extraction_path / "EP" / "readme.txt").write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `_tree_snapshot` | `tests.unit.test_inpn_protected_areas_fr._tree_snapshot` |
| `first.extraction_path.with_name` | `unresolved local/third-party receiver; no ownership inferred` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `first.extraction_path.is_dir` | `unresolved local/third-party receiver; no ownership inferred` |
| `backup.exists` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `first.extraction_path.is_dir`<br>`backup.exists` |
| Filesystem/archive write or publication | `(first.extraction_path / "EP" / "readme.txt").write_bytes`<br>`first.extraction_path.with_name`<br>`first.extraction_path.is_dir` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_extraction_backup_move_failure_leaves_old_tree_untouched.fail_backup_move`

**Purpose:** Implements `fail backup move` within the file role: Provides complete unit and regression coverage for the `inpn_protected_areas_fr` contracts exercised in this file.

**Exact signature**

```python
def fail_backup_move(source: Path, target: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source` | positional-or-keyword | `Path` | `required` |
| `target` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `OSError("cannot stage old tree")` under lexical guard `source == first.extraction_path and target == backup`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `OSError` | `unresolved local/third-party receiver; no ownership inferred` |
| `original_replace` | `unresolved local/third-party receiver; no ownership inferred` |

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
def fail_backup_move(source: Path, target: Path) -> None:
        if source == first.extraction_path and target == backup:
            raise OSError("cannot stage old tree")
        original_replace(source, target)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_extraction_rejects_wrong_download_type`

**Purpose:** Regression invariant: extraction rejects wrong download type. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_extraction_rejects_wrong_download_type(
    tmp_path: Path,
    bad_input: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("bad_input", [None, object(), True])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `bad_input` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(InpnProtectedAreasSourceError, match="download\|type")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `extract_inpn_protected_areas_archive` | `landscout.sources.inpn_protected_areas_fr.extract_inpn_protected_areas_archive` |
| `_config` | `tests.unit.test_inpn_protected_areas_fr._config` |
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_extraction_rejects_wrong_config_type`

**Purpose:** Regression invariant: extraction rejects wrong config type. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_extraction_rejects_wrong_config_type(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(InpnProtectedAreasSourceError, match="config\|type")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_download` | `tests.unit.test_inpn_protected_areas_fr._download` |
| `pytest.raises` | `pytest.raises` |
| `extract_inpn_protected_areas_archive` | `landscout.sources.inpn_protected_areas_fr.extract_inpn_protected_areas_archive` |
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
def test_extraction_rejects_wrong_config_type(tmp_path: Path) -> None:
    _, download, _ = _download(tmp_path)
    with pytest.raises(InpnProtectedAreasSourceError, match="config|type"):
        extract_inpn_protected_areas_archive(
            download,
            object(),  # type: ignore[arg-type]
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_extraction_cache_setup_failure_is_controlled`

**Purpose:** Regression invariant: extraction cache setup failure is controlled. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_extraction_cache_setup_failure_is_controlled(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(InpnProtectedAreasSourceError, match="extract\|cache")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_download` | `tests.unit.test_inpn_protected_areas_fr._download` |
| `extraction_parent.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `extract_inpn_protected_areas_archive` | `landscout.sources.inpn_protected_areas_fr.extract_inpn_protected_areas_archive` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `extraction_parent.write_bytes` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_extraction_cache_setup_failure_is_controlled(tmp_path: Path) -> None:
    config, download, _ = _download(tmp_path)
    extraction_parent = download.path.parent / "x"
    extraction_parent.write_bytes(b"not a directory")

    with pytest.raises(InpnProtectedAreasSourceError, match="extract|cache"):
        extract_inpn_protected_areas_archive(download, config)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_extraction_rejects_stale_download_bytes`

**Purpose:** Regression invariant: extraction rejects stale download bytes. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_extraction_rejects_stale_download_bytes(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        InpnProtectedAreasSourceError, match="SHA\|size\|archive\|download"<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_download` | `tests.unit.test_inpn_protected_areas_fr._download` |
| `_zip_bytes` | `tests.unit.test_inpn_protected_areas_fr._zip_bytes` |
| `download.path.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `extract_inpn_protected_areas_archive` | `landscout.sources.inpn_protected_areas_fr.extract_inpn_protected_areas_archive` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `download.path.write_bytes` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_extraction_rejects_stale_download_bytes(tmp_path: Path) -> None:
    config, download, _ = _download(tmp_path)
    replacement = _zip_bytes({"EP/readme.txt": b"forged contents"})
    download.path.write_bytes(replacement)

    with pytest.raises(
        InpnProtectedAreasSourceError, match="SHA|size|archive|download"
    ):
        extract_inpn_protected_areas_archive(download, config)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_result_dataclasses_are_frozen`

**Purpose:** Regression invariant: result dataclasses are frozen. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_result_dataclasses_are_frozen(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(FrozenInstanceError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_download` | `tests.unit.test_inpn_protected_areas_fr._download` |
| `extract_inpn_protected_areas_archive` | `landscout.sources.inpn_protected_areas_fr.extract_inpn_protected_areas_archive` |
| `pytest.raises` | `pytest.raises` |

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
| In-memory mutation | `download.cache_hit = True`<br>`extraction.cache_hit = True`<br>`extraction.files[0].sha256 = "0" * 64` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_public_api_exports_only_stable_high_level_symbols`

**Purpose:** Regression invariant: public api exports only stable high level symbols. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_public_api_exports_only_stable_high_level_symbols() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert set(inpn.__all__) == EXPECTED_EXPORTS`
  - `assert EXPECTED_EXPORTS <= set(sources.__all__)`
  - `assert all(<br>        getattr(sources, name) is getattr(inpn, name) for name in EXPECTED_EXPORTS<br>    )`
  - `assert not hasattr(sources, "_validated_zip_members")`
  - `assert not hasattr(sources, "_inventory")`
  - `assert not hasattr(sources, "validate_inpn_protected_area_geometry")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `all` | `unresolved local/third-party receiver; no ownership inferred` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `hasattr` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_public_api_exports_only_stable_high_level_symbols() -> None:
    assert set(inpn.__all__) == EXPECTED_EXPORTS
    assert EXPECTED_EXPORTS <= set(sources.__all__)
    assert all(
        getattr(sources, name) is getattr(inpn, name) for name in EXPECTED_EXPORTS
    )
    assert not hasattr(sources, "_validated_zip_members")
    assert not hasattr(sources, "_inventory")
    assert not hasattr(sources, "validate_inpn_protected_area_geometry")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_result_schemas_are_factual_inventory_only`

**Purpose:** Regression invariant: result schemas are factual inventory only. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_result_schemas_are_factual_inventory_only() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert [field.name for field in fields(InpnProtectedAreasDownload)] == [<br>        "provider",<br>        "authority",<br>        "program",<br>        "dataset_id",<br>        "dataset_name",<br>        "declared_version",<br>        "reference_page_url",<br>        "archive_url",<br>        "download_timestamp",<br>        "filename",<br>        "file_size",<br>        "sha256",<br>        "path",<br>        "cache_hit",<br>    ]`
  - `assert [field.name for field in fields(InpnProtectedAreasExtractedFile)] == [<br>        "relative_path",<br>        "file_size",<br>        "sha256",<br>    ]`
  - `assert [field.name for field in fields(InpnProtectedAreasExtraction)] == [<br>        "download",<br>        "extraction_path",<br>        "files",<br>        "cache_hit",<br>    ]`
  - `assert not any(<br>        fragment in name.casefold() for name in inpn.__all__ for fragment in forbidden<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `fields` | `dataclasses.fields` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `name.casefold` | `unresolved local/third-party receiver; no ownership inferred` |

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
        fragment in name.casefold() for name in inpn.__all__ for fragment in forbidden
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_strict_metadata_rejects_boolean_numeric_values_as_cache_hits`

**Purpose:** Regression invariant: strict metadata rejects boolean numeric values as cache hits. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_strict_metadata_rejects_boolean_numeric_values_as_cache_hits(
    tmp_path: Path,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert refreshed.cache_hit is False`
  - `assert len(session.calls) == 1`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_download` | `tests.unit.test_inpn_protected_areas_fr._download` |
| `_download_metadata_path` | `tests.unit.test_inpn_protected_areas_fr._download_metadata_path` |
| `_read_json` | `tests.unit.test_inpn_protected_areas_fr._read_json` |
| `_write_json` | `tests.unit.test_inpn_protected_areas_fr._write_json` |
| `_session` | `tests.unit.test_inpn_protected_areas_fr._session` |
| `_download_with_session` | `tests.unit.test_inpn_protected_areas_fr._download_with_session` |
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
| In-memory mutation | `metadata["file_size"] = True` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_cache_path_binds_version_and_filename`

**Purpose:** Regression invariant: cache path binds version and filename. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_cache_path_binds_version_and_filename(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert download.path.name == "EP.zip"`
  - `assert "07-2026" in download.path.parts`
  - `assert metadata["dataset_id"] == "EP"`
  - `assert metadata["declared_version"] == "07/2026"`
  - `assert metadata["filename"] == "EP.zip"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_download` | `tests.unit.test_inpn_protected_areas_fr._download` |
| `_read_json` | `tests.unit.test_inpn_protected_areas_fr._read_json` |
| `_download_metadata_path` | `tests.unit.test_inpn_protected_areas_fr._download_metadata_path` |

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
def test_cache_path_binds_version_and_filename(tmp_path: Path) -> None:
    _, download, _ = _download(tmp_path)

    assert download.path.name == "EP.zip"
    assert "07-2026" in download.path.parts
    metadata = _read_json(_download_metadata_path(download))
    assert metadata["dataset_id"] == "EP"
    assert metadata["declared_version"] == "07/2026"
    assert metadata["filename"] == "EP.zip"
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_download_uses_no_hidden_reference_page_scrape`

**Purpose:** Regression invariant: download uses no hidden reference page scrape. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_download_uses_no_hidden_reference_page_scrape(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert [url for url, _ in session.calls] == [str(config.archive_url)]`
  - `assert str(config.reference_page_url) not in [url for url, _ in session.calls]`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_config` | `tests.unit.test_inpn_protected_areas_fr._config` |
| `_session` | `tests.unit.test_inpn_protected_areas_fr._session` |
| `_download_with_session` | `tests.unit.test_inpn_protected_areas_fr._download_with_session` |
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
def test_download_uses_no_hidden_reference_page_scrape(tmp_path: Path) -> None:
    config = _config(tmp_path)
    session = _session(config)

    _download_with_session(config, session)

    assert [url for url, _ in session.calls] == [str(config.archive_url)]
    assert str(config.reference_page_url) not in [url for url, _ in session.calls]
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_exact_file_inventory_does_not_omit_unknown_suffixes`

**Purpose:** Regression invariant: exact file inventory does not omit unknown suffixes. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_exact_file_inventory_does_not_omit_unknown_suffixes(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert {item.relative_path for item in extraction.files} == set(members)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_download` | `tests.unit.test_inpn_protected_areas_fr._download` |
| `_zip_bytes` | `tests.unit.test_inpn_protected_areas_fr._zip_bytes` |
| `extract_inpn_protected_areas_archive` | `landscout.sources.inpn_protected_areas_fr.extract_inpn_protected_areas_archive` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_archive_and_extraction_cache_reuse_are_independent`

**Purpose:** Regression invariant: archive and extraction cache reuse are independent. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_archive_and_extraction_cache_reuse_are_independent(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert first_download.cache_hit is False`
  - `assert first_extraction.cache_hit is False`
  - `assert second_download.cache_hit is True`
  - `assert second_extraction.cache_hit is True`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_download` | `tests.unit.test_inpn_protected_areas_fr._download` |
| `extract_inpn_protected_areas_archive` | `landscout.sources.inpn_protected_areas_fr.extract_inpn_protected_areas_archive` |
| `_download_with_session` | `tests.unit.test_inpn_protected_areas_fr._download_with_session` |
| `_Session` | `tests.unit.test_inpn_protected_areas_fr._Session` |
| `AssertionError` | `unresolved local/third-party receiver; no ownership inferred` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_no_stale_parts_after_download_or_extraction_success`

**Purpose:** Regression invariant: no stale parts after download or extraction success. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_no_stale_parts_after_download_or_extraction_success(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert extraction.extraction_path.is_dir()`
  - `assert not list(Path(config.cache_root).rglob("*.part"))`
  - `assert not list(Path(config.cache_root).rglob("*.bak"))`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_download` | `tests.unit.test_inpn_protected_areas_fr._download` |
| `extract_inpn_protected_areas_archive` | `landscout.sources.inpn_protected_areas_fr.extract_inpn_protected_areas_archive` |
| `extraction.extraction_path.is_dir` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `Path(config.cache_root).rglob` | `unresolved local/third-party receiver; no ownership inferred` |
| `Path` | `pathlib.Path` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `extraction.extraction_path.is_dir` |
| Filesystem/archive write or publication | `extraction.extraction_path.is_dir` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_no_stale_parts_after_download_or_extraction_success(tmp_path: Path) -> None:
    config, download, _ = _download(tmp_path)
    extraction = extract_inpn_protected_areas_archive(download, config)

    assert extraction.extraction_path.is_dir()
    assert not list(Path(config.cache_root).rglob("*.part"))
    assert not list(Path(config.cache_root).rglob("*.bak"))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.


### STEP 7F.1B.1 extraction revalidation regressions

The appended tests prove that a valid extraction returns newly constructed source-bound objects; wrong types/paths and forged path/size/SHA records fail; physical missing, extra, and same-size content changes fail; and simulated links/junctions fail. These tests use only synthetic local ZIP/extraction bytes.

## 7. Test-specific regression contract

- Test functions: **56**.
- Pytest fixtures (decorator-proven): **0**.

### Per-test regression index

| Test | Parametrization | Expected exception contexts | Assertion count | Exact regression purpose |
|---|---|---|---:|---|
| `test_checked_in_config_loads_with_exact_source_identity` | none | none | 12 | Proves checked in config loads with exact source identity using the exact source reproduced in section 7. |
| `test_source_config_yaml_rejects_duplicate_keys` | none | pytest.raises(InpnProtectedAreasSourceError, match="config") | 0 | Proves source config yaml rejects duplicate keys using the exact source reproduced in section 7. |
| `test_loaded_source_config_is_immutable` | none | pytest.raises(ValidationError, match="frozen") | 0 | Proves loaded source config is immutable using the exact source reproduced in section 7. |
| `test_config_rejects_invalid_expected_snapshot_integrity` | pytest.mark.parametrize(<br>    ("field", "value"),<br>    [<br>        ("expected_archive_size_bytes", 0),<br>        ("expected_archive_size_bytes", -1),<br>        ("expected_archive_size_bytes", True),<br>        ("expected_archive_size_bytes", 1.0),<br>        ("expected_archive_size_bytes", "99835011"),<br>        ("expected_archive_size_bytes", float("nan")),<br>        ("expected_archive_size_bytes", float("inf")),<br>        ("expected_archive_size_bytes", float("-inf")),<br>        ("expected_archive_sha256", "0" * 63),<br>        ("expected_archive_sha256", "A" * 64),<br>        ("expected_archive_sha256", None),<br>    ],<br>) | pytest.raises((TypeError, ValueError)) | 0 | Proves config rejects invalid expected snapshot integrity using the exact source reproduced in section 7. |
| `test_config_rejects_noncanonical_values` | pytest.mark.parametrize(<br>    "mutation",<br>    [<br>        "unknown_key",<br>        "missing_dataset_id",<br>        "wrong_dataset_id",<br>        "empty_version",<br>        "malformed_reference_url",<br>        "malformed_archive_url",<br>        "non_https_archive_url",<br>        "wrong_archive_filename",<br>    ],<br>) | pytest.raises(InpnProtectedAreasSourceError) | 0 | Proves config rejects noncanonical values using the exact source reproduced in section 7. |
| `test_wrong_download_config_type_has_controlled_error` | none | pytest.raises(InpnProtectedAreasSourceError, match="config\|type") | 0 | Proves wrong download config type has controlled error using the exact source reproduced in section 7. |
| `test_download_timeout_is_strict_finite_positive` | pytest.mark.parametrize(<br>    "timeout",<br>    [<br>        0,<br>        -1,<br>        float("nan"),<br>        float("inf"),<br>        "30",<br>        True,<br>        pytest.param(10**10000, id="overflow-int"),<br>    ],<br>) | pytest.raises(InpnProtectedAreasSourceError, match="timeout") | 0 | Proves download timeout is strict finite positive using the exact source reproduced in section 7. |
| `test_download_api_has_no_arbitrary_http_session_injection` | none | none | 1 | Proves download api has no arbitrary http session injection using the exact source reproduced in section 7. |
| `test_download_cache_setup_failure_is_controlled` | none | pytest.raises(InpnProtectedAreasSourceError, match="download\|cache") | 0 | Proves download cache setup failure is controlled using the exact source reproduced in section 7. |
| `test_valid_zip_download_binds_exact_bytes_and_lineage` | none | none | 16 | Proves valid zip download binds exact bytes and lineage using the exact source reproduced in section 7. |
| `test_cold_download_must_match_configured_snapshot_before_publication` | pytest.mark.parametrize("mismatch", ["size", "sha256"]) | pytest.raises(<br>        InpnProtectedAreasSourceError, match="size\|SHA\|snapshot\|integrity"<br>    ) | 5 | Proves cold download must match configured snapshot before publication using the exact source reproduced in section 7. |
| `test_coordinated_cache_and_metadata_snapshot_change_is_not_a_cache_hit` | none | pytest.raises(InpnProtectedAreasSourceError) | 2 | Proves coordinated cache and metadata snapshot change is not a cache hit using the exact source reproduced in section 7. |
| `test_http_and_payload_failures_are_controlled` | pytest.mark.parametrize(<br>    ("payload", "status", "error"),<br>    [<br>        (_zip_bytes(), 300, None),<br>        (_zip_bytes(), 304, None),<br>        (_zip_bytes(), 503, None),<br>        (b"", 200, None),<br>        (b"<html>temporary failure</html>", 200, None),<br>        (b"PK not really a zip", 200, None),<br>        (_zip_bytes(), 200, OSError("network failed")),<br>    ],<br>    ids=[<br>        "http-300",<br>        "http-304",<br>        "http-error",<br>        "empty",<br>        "html",<br>        "invalid-zip",<br>        "transport-error",<br>    ],<br>) | pytest.raises(InpnProtectedAreasSourceError) | 1 | Proves http and payload failures are controlled using the exact source reproduced in section 7. |
| `test_unsupported_zip_compression_has_controlled_error` | none | pytest.raises(InpnProtectedAreasSourceError, match="ZIP\|archive") | 0 | Proves unsupported zip compression has controlled error using the exact source reproduced in section 7. |
| `test_malformed_response_headers_have_controlled_error` | none | pytest.raises(InpnProtectedAreasSourceError, match="response\|download") | 0 | Proves malformed response headers have controlled error using the exact source reproduced in section 7. |
| `test_midstream_protocol_failure_has_controlled_error` | none | pytest.raises(InpnProtectedAreasSourceError, match="response\|download") | 0 | Proves midstream protocol failure has controlled error using the exact source reproduced in section 7. |
| `test_valid_physical_and_metadata_cache_is_reused` | none | none | 3 | Proves valid physical and metadata cache is reused using the exact source reproduced in section 7. |
| `test_invalid_download_cache_is_a_miss` | pytest.mark.parametrize(<br>    "mutation",<br>    [<br>        "physical_size",<br>        "physical_sha",<br>        "metadata_sha",<br>        "metadata_size",<br>        "metadata_url",<br>        "metadata_version",<br>        "metadata_schema",<br>        "metadata_schema_bool",<br>        "metadata_schema_float",<br>        "metadata_unknown",<br>        "metadata_duplicate",<br>        "metadata_timestamp",<br>        "metadata_malformed",<br>        "invalid_cached_zip",<br>    ],<br>) | none | 3 | Proves invalid download cache is a miss using the exact source reproduced in section 7. |
| `test_successful_first_and_replacement_publication` | none | none | 4 | Proves successful first and replacement publication using the exact source reproduced in section 7. |
| `test_publication_failure_restores_old_pair` | pytest.mark.parametrize("failure_target", ["archive", "metadata"]) | pytest.raises(InpnProtectedAreasSourceError, match="publication\|download") | 4 | Proves publication failure restores old pair using the exact source reproduced in section 7. |
| `test_rollback_failure_preserves_recovery_material` | none | pytest.raises(InpnProtectedAreasSourceError, match="rollback") | 2 | Proves rollback failure preserves recovery material using the exact source reproduced in section 7. |
| `test_broken_download_recovery_symlink_is_rejected` | pytest.mark.parametrize("backup_role", ["archive", "metadata"]) | pytest.raises(InpnProtectedAreasSourceError, match="backup\|recovery\|manual") | 4 | Proves broken download recovery symlink is rejected using the exact source reproduced in section 7. |
| `test_existing_normal_download_recovery_backup_remains_unchanged` | none | pytest.raises(InpnProtectedAreasSourceError, match="backup\|recovery\|manual") | 3 | Proves existing normal download recovery backup remains unchanged using the exact source reproduced in section 7. |
| `test_failed_replacement_restores_a_still_reusable_valid_download_pair` | none | pytest.raises(InpnProtectedAreasSourceError, match="publication") | 3 | Proves failed replacement restores a still reusable valid download pair using the exact source reproduced in section 7. |
| `test_unsafe_zip_member_paths_are_rejected` | pytest.mark.parametrize(<br>    "member_name",<br>    [<br>        "../evil.txt",<br>        "nested/../../evil.txt",<br>        "/absolute/evil.txt",<br>        r"C:\evil.txt",<br>        r"\\server\share\evil.txt",<br>        r"..\mixed\evil.txt",<br>        ".",<br>        "CON.txt",<br>        "folder/NUL.data",<br>        "folder/COM¹.parquet",<br>        "folder/LPT³.dbf",<br>        "folder/bad:name.txt",<br>        "folder/trailing. ",<br>        "folder/ leading.txt",<br>        "folder/control\n.txt",<br>    ],<br>) | pytest.raises(InpnProtectedAreasSourceError, match="ZIP\|archive\|member\|path") | 0 | Proves unsafe zip member paths are rejected using the exact source reproduced in section 7. |
| `test_duplicate_or_colliding_zip_destinations_are_rejected` | pytest.mark.parametrize(<br>    "members",<br>    [<br>        [("same.txt", b"a"), ("same.txt", b"b")],<br>        [("folder/file.txt", b"a"), (r"folder\file.txt", b"b")],<br>        [("folder/file.txt", b"a"), ("folder/./file.txt", b"b")],<br>        [("Folder/File.txt", b"a"), ("folder/file.txt", b"b")],<br>        [("blocked", b"a"), ("blocked/child.txt", b"b")],<br>    ],<br>) | pytest.raises(InpnProtectedAreasSourceError, match="duplicate\|collid\|archive") | 0 | Proves duplicate or colliding zip destinations are rejected using the exact source reproduced in section 7. |
| `test_zip_links_and_special_files_are_rejected` | pytest.mark.parametrize(<br>    ("mode", "message"),<br>    [(stat.S_IFLNK \| 0o777, "symbolic\|link"), (stat.S_IFIFO \| 0o644, "special")],<br>) | pytest.raises(InpnProtectedAreasSourceError, match=message) | 0 | Proves zip links and special files are rejected using the exact source reproduced in section 7. |
| `test_complete_zip_inventory_is_validated_before_member_copy` | none | pytest.raises(InpnProtectedAreasSourceError) | 1 | Proves complete zip inventory is validated before member copy using the exact source reproduced in section 7. |
| `test_extraction_validates_complete_inventory_before_copying` | none | pytest.raises(InpnProtectedAreasSourceError) | 2 | Proves extraction validates complete inventory before copying using the exact source reproduced in section 7. |
| `test_normal_nested_members_are_accepted` | none | none | 2 | Proves normal nested members are accepted using the exact source reproduced in section 7. |
| `test_extraction_inventory_is_complete_ordered_and_hashed` | none | none | 12 | Proves extraction inventory is complete ordered and hashed using the exact source reproduced in section 7. |
| `test_valid_extraction_cache_is_reused` | none | none | 3 | Proves valid extraction cache is reused using the exact source reproduced in section 7. |
| `test_invalid_extraction_cache_is_rebuilt` | pytest.mark.parametrize(<br>    "mutation",<br>    [<br>        "same_size_content",<br>        "size",<br>        "missing",<br>        "unexpected",<br>        "file_sha",<br>        "archive_sha",<br>        "archive_size",<br>        "schema",<br>        "schema_bool",<br>        "schema_float",<br>        "unknown",<br>        "boolean_file_size",<br>        "duplicate_key",<br>    ],<br>) | none | 8 | Proves invalid extraction cache is rebuilt using the exact source reproduced in section 7. |
| `test_first_extraction_publication_failure_leaves_no_half_root` | none | pytest.raises(InpnProtectedAreasSourceError, match="publication") | 3 | Proves first extraction publication failure leaves no half root using the exact source reproduced in section 7. |
| `test_extraction_replacement_failure_restores_old_tree` | none | pytest.raises(InpnProtectedAreasSourceError, match="publication") | 2 | Proves extraction replacement failure restores old tree using the exact source reproduced in section 7. |
| `test_extraction_rollback_failure_preserves_backup` | none | pytest.raises(InpnProtectedAreasSourceError, match="rollback") | 2 | Proves extraction rollback failure preserves backup using the exact source reproduced in section 7. |
| `test_extraction_backup_move_failure_leaves_old_tree_untouched` | none | pytest.raises(InpnProtectedAreasSourceError, match="publication\|stage") | 3 | Proves extraction backup move failure leaves old tree untouched using the exact source reproduced in section 7. |
| `test_extraction_rejects_wrong_download_type` | pytest.mark.parametrize("bad_input", [None, object(), True]) | pytest.raises(InpnProtectedAreasSourceError, match="download\|type") | 0 | Proves extraction rejects wrong download type using the exact source reproduced in section 7. |
| `test_extraction_rejects_wrong_config_type` | none | pytest.raises(InpnProtectedAreasSourceError, match="config\|type") | 0 | Proves extraction rejects wrong config type using the exact source reproduced in section 7. |
| `test_extraction_cache_setup_failure_is_controlled` | none | pytest.raises(InpnProtectedAreasSourceError, match="extract\|cache") | 0 | Proves extraction cache setup failure is controlled using the exact source reproduced in section 7. |
| `test_extraction_rejects_stale_download_bytes` | none | pytest.raises(<br>        InpnProtectedAreasSourceError, match="SHA\|size\|archive\|download"<br>    ) | 0 | Proves extraction rejects stale download bytes using the exact source reproduced in section 7. |
| `test_result_dataclasses_are_frozen` | none | pytest.raises(FrozenInstanceError); pytest.raises(FrozenInstanceError); pytest.raises(FrozenInstanceError) | 0 | Proves result dataclasses are frozen using the exact source reproduced in section 7. |
| `test_public_api_exports_only_stable_high_level_symbols` | none | none | 6 | Proves public api exports only stable high level symbols using the exact source reproduced in section 7. |
| `test_result_schemas_are_factual_inventory_only` | none | none | 4 | Proves result schemas are factual inventory only using the exact source reproduced in section 7. |
| `test_strict_metadata_rejects_boolean_numeric_values_as_cache_hits` | none | none | 2 | Proves strict metadata rejects boolean numeric values as cache hits using the exact source reproduced in section 7. |
| `test_cache_path_binds_version_and_filename` | none | none | 5 | Proves cache path binds version and filename using the exact source reproduced in section 7. |
| `test_download_uses_no_hidden_reference_page_scrape` | none | none | 2 | Proves download uses no hidden reference page scrape using the exact source reproduced in section 7. |
| `test_exact_file_inventory_does_not_omit_unknown_suffixes` | none | none | 1 | Proves exact file inventory does not omit unknown suffixes using the exact source reproduced in section 7. |
| `test_archive_and_extraction_cache_reuse_are_independent` | none | none | 4 | Proves archive and extraction cache reuse are independent using the exact source reproduced in section 7. |
| `test_no_stale_parts_after_download_or_extraction_success` | none | none | 3 | Proves no stale parts after download or extraction success using the exact source reproduced in section 7. |

## 8. Public exports and package ownership

This module declares no `__all__`; no package-level public guarantee is inferred from direct importability alone.

## 9. Trust, provenance, side effects, and business boundary

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.
- Configured identity, textual lineage, byte identity, physical source reconstruction, local envelope validation, and source-complete validation remain distinct trust levels. This companion attributes only the levels implemented in the exact source.
- Filesystem, network, hashing, CRS/geometry, process, mutation, and expected-exception evidence is listed per callable; an empty category is not silently promoted to an effect.

## 10. Change impact

A source-byte change invalidates the SHA above and requires re-auditing imports/re-exports, constants/aliases/schemas, model fields/immutability, qualified callers, side effects, controlled errors, tests, source/artifact locks, and the exact full snapshot.

## 11. Exact complete current file content

This byte-bound snapshot is the complete current repository file.

```python
from __future__ import annotations

import inspect
import io
import json
import stat
import warnings
import zipfile
from contextlib import contextmanager
from dataclasses import FrozenInstanceError, fields, replace
from datetime import datetime
from hashlib import sha256
from pathlib import Path
from typing import Any, Self

import pytest
import yaml
from pydantic import ValidationError

from landscout import sources
from landscout.common import safe_http
from landscout.common.safe_http import SafeHttpsError
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
    validate_inpn_protected_areas_extraction,
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
    "validate_inpn_protected_areas_extraction",
}


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
        return (
            self.status_code in {301, 302, 303, 307, 308} and "Location" in self.headers
        )

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
    snapshot = _zip_bytes() if payload is None else payload
    config = _config(tmp_path, snapshot)
    session = _session(config, snapshot)
    result = _download_with_session(config, session)
    return config, result, session


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
    assert (
        str(config.archive_url) == "https://assets.patrinat.fr/files/donnees/ep/EP.zip"
    )
    assert config.archive_filename == "EP.zip"
    assert config.expected_archive_size_bytes == 99_835_011
    assert (
        config.expected_archive_sha256
        == "73688bc37205a5e7f59e2065a0b81fc8cf2a242bdec5d7d2786f083671c4abe5"
    )


def test_source_config_yaml_rejects_duplicate_keys(tmp_path: Path) -> None:
    path = tmp_path / "source.yaml"
    path.write_text(
        CONFIG_PATH.read_text(encoding="utf-8") + "\nprovider: PatriNat\n",
        encoding="utf-8",
    )

    with pytest.raises(InpnProtectedAreasSourceError, match="config"):
        load_inpn_protected_areas_source_config(path)


def test_loaded_source_config_is_immutable() -> None:
    config = load_inpn_protected_areas_source_config()

    with pytest.raises(ValidationError, match="frozen"):
        config.declared_version = "08/2026"


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("expected_archive_size_bytes", 0),
        ("expected_archive_size_bytes", -1),
        ("expected_archive_size_bytes", True),
        ("expected_archive_size_bytes", 1.0),
        ("expected_archive_size_bytes", "99835011"),
        ("expected_archive_size_bytes", float("nan")),
        ("expected_archive_size_bytes", float("inf")),
        ("expected_archive_size_bytes", float("-inf")),
        ("expected_archive_sha256", "0" * 63),
        ("expected_archive_sha256", "A" * 64),
        ("expected_archive_sha256", None),
    ],
)
def test_config_rejects_invalid_expected_snapshot_integrity(
    field: str,
    value: object,
) -> None:
    payload = _config_payload()
    payload[field] = value

    with pytest.raises((TypeError, ValueError)):
        InpnProtectedAreasSourceConfig.model_validate(payload)


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


def test_download_api_has_no_arbitrary_http_session_injection() -> None:
    assert (
        "session"
        not in inspect.signature(download_inpn_protected_areas_archive).parameters
    )


def test_download_cache_setup_failure_is_controlled(tmp_path: Path) -> None:
    cache_file = tmp_path / "cache-is-a-file"
    cache_file.write_bytes(b"not a directory")
    payload = _config_payload()
    payload["cache_root"] = str(cache_file)
    config = InpnProtectedAreasSourceConfig.model_validate(payload)

    with pytest.raises(InpnProtectedAreasSourceError, match="download|cache"):
        _download_with_session(config, _session(config))


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


@pytest.mark.parametrize("mismatch", ["size", "sha256"])
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

    with pytest.raises(
        InpnProtectedAreasSourceError, match="size|SHA|snapshot|integrity"
    ):
        _download_with_session(config, _session(config, downloaded))

    assert not list(Path(config.cache_root).rglob("EP.zip"))
    assert not list(Path(config.cache_root).rglob("*.metadata.json"))


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
        _download_with_session(config, session)

    assert not list(Path(config.cache_root).rglob("*.part"))


def test_unsupported_zip_compression_has_controlled_error(tmp_path: Path) -> None:
    payload = _unsupported_compression_zip()
    config = _config(tmp_path, payload)

    with pytest.raises(InpnProtectedAreasSourceError, match="ZIP|archive"):
        _download_with_session(config, _session(config, payload))


def test_malformed_response_headers_have_controlled_error(tmp_path: Path) -> None:
    config = _config(tmp_path)
    response = _Response(_zip_bytes(), url=str(config.archive_url))
    response.headers = None  # type: ignore[assignment]

    with pytest.raises(InpnProtectedAreasSourceError, match="response|download"):
        _download_with_session(config, _Session(response))


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
    elif mutation in {
        "metadata_schema",
        "metadata_schema_bool",
        "metadata_schema_float",
    }:
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


def _force_cache_miss(download: InpnProtectedAreasDownload) -> tuple[Path, bytes]:
    metadata_path = _download_metadata_path(download)
    metadata = _read_json(metadata_path)
    metadata["sha256"] = "0" * 64
    _write_json(metadata_path, metadata)
    return metadata_path, metadata_path.read_bytes()


def test_successful_first_and_replacement_publication(tmp_path: Path) -> None:
    config, first, _ = _download(tmp_path)
    _force_cache_miss(first)
    replacement = _zip_bytes()

    second = _download_with_session(config, _session(config, replacement))

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
        _download_with_session(config, _session(config))

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
        _download_with_session(config, _session(config))

    archive_backup = first.path.with_name(f"{first.path.name}.bak")
    metadata_backup = metadata_path.with_name(f"{metadata_path.name}.bak")
    assert archive_backup.read_bytes() == old_archive
    assert metadata_backup.read_bytes() == old_metadata


@pytest.mark.parametrize("backup_role", ["archive", "metadata"])
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
    payload = _zip_bytes([(member_name, b"bad")])
    config = _config(tmp_path, payload)
    with pytest.raises(InpnProtectedAreasSourceError, match="ZIP|archive|member|path"):
        _download_with_session(config, _session(config, payload))


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
    payload = _zip_bytes(members)
    config = _config(tmp_path, payload)
    with pytest.raises(InpnProtectedAreasSourceError, match="duplicate|collid|archive"):
        _download_with_session(config, _session(config, payload))


@pytest.mark.parametrize(
    ("mode", "message"),
    [(stat.S_IFLNK | 0o777, "symbolic|link"), (stat.S_IFIFO | 0o644, "special")],
)
def test_zip_links_and_special_files_are_rejected(
    tmp_path: Path,
    mode: int,
    message: str,
) -> None:
    payload = _special_zip("unsafe", mode)
    config = _config(tmp_path, payload)
    with pytest.raises(InpnProtectedAreasSourceError, match=message):
        _download_with_session(config, _session(config, payload))


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
        "duplicate_key",
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
    elif mutation == "boolean_file_size":
        file_entries = metadata["files"]
        assert isinstance(file_entries, list)
        assert isinstance(file_entries[0], dict)
        file_entries[0]["file_size"] = True
        _write_json(metadata_path, metadata)
    else:
        encoded = json.dumps(metadata, separators=(",", ":"))
        marker = '"schema_version":1'
        metadata_path.write_text(
            encoded.replace(marker, f"{marker},{marker}", 1),
            encoding="utf-8",
        )

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
        if (
            source.name.endswith(".part")
            and target == first.extraction_path
            and not failed
        ):
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

    with pytest.raises(
        InpnProtectedAreasSourceError, match="SHA|size|archive|download"
    ):
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
    assert all(
        getattr(sources, name) is getattr(inpn, name) for name in EXPECTED_EXPORTS
    )
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
        fragment in name.casefold() for name in inpn.__all__ for fragment in forbidden
    )


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

    _download_with_session(config, session)

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

    second_download = _download_with_session(
        config,
        _Session(error=AssertionError("network used")),
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


def test_extraction_revalidation_returns_fresh_source_bound_result(
    tmp_path: Path,
) -> None:
    config, download, _ = _download(tmp_path)
    extraction = extract_inpn_protected_areas_archive(download, config)

    fresh = validate_inpn_protected_areas_extraction(extraction, config)

    assert fresh == extraction
    assert fresh is not extraction
    assert fresh.download is not extraction.download
    assert fresh.files is not extraction.files


@pytest.mark.parametrize("bad_extraction", [None, object(), True])
def test_extraction_revalidation_rejects_wrong_type(
    tmp_path: Path,
    bad_extraction: object,
) -> None:
    with pytest.raises(InpnProtectedAreasSourceError, match="extraction|type"):
        validate_inpn_protected_areas_extraction(
            bad_extraction,  # type: ignore[arg-type]
            _config(tmp_path),
        )


def test_extraction_revalidation_rejects_wrong_path(tmp_path: Path) -> None:
    config, download, _ = _download(tmp_path)
    extraction = extract_inpn_protected_areas_archive(download, config)
    forged = replace(extraction, extraction_path=tmp_path / "other")

    with pytest.raises(InpnProtectedAreasSourceError, match="path|extraction"):
        validate_inpn_protected_areas_extraction(forged, config)


@pytest.mark.parametrize("mutation", ["path", "size", "sha256"])
def test_extraction_revalidation_rejects_forged_file_inventory(
    tmp_path: Path,
    mutation: str,
) -> None:
    config, download, _ = _download(tmp_path)
    extraction = extract_inpn_protected_areas_archive(download, config)
    item = extraction.files[0]
    if mutation == "path":
        forged_item = replace(item, relative_path="EP/forged.txt")
    elif mutation == "size":
        forged_item = replace(item, file_size=item.file_size + 1)
    else:
        forged_item = replace(item, sha256="0" * 64)
    forged = replace(extraction, files=(forged_item,))

    with pytest.raises(InpnProtectedAreasSourceError, match="inventory|extraction"):
        validate_inpn_protected_areas_extraction(forged, config)


@pytest.mark.parametrize("mutation", ["missing", "extra", "content"])
def test_extraction_revalidation_rejects_physical_inventory_mutation(
    tmp_path: Path,
    mutation: str,
) -> None:
    config, download, _ = _download(tmp_path)
    extraction = extract_inpn_protected_areas_archive(download, config)
    path = extraction.extraction_path.joinpath(
        *extraction.files[0].relative_path.split("/")
    )
    if mutation == "missing":
        path.unlink()
    elif mutation == "extra":
        (extraction.extraction_path / "extra.txt").write_bytes(b"extra")
    else:
        payload = path.read_bytes()
        path.write_bytes(b"x" * len(payload))

    with pytest.raises(
        InpnProtectedAreasSourceError,
        match="physical|inventory|cache|Extracted",
    ):
        validate_inpn_protected_areas_extraction(extraction, config)


def test_extraction_revalidation_rejects_link_or_junction_file(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config, download, _ = _download(tmp_path)
    extraction = extract_inpn_protected_areas_archive(download, config)
    target = extraction.extraction_path.joinpath(
        *extraction.files[0].relative_path.split("/")
    )
    original = inpn._is_link_or_junction

    def simulated_link(path: Path) -> bool:
        return path == target or original(path)

    monkeypatch.setattr(inpn, "_is_link_or_junction", simulated_link)

    with pytest.raises(InpnProtectedAreasSourceError, match="link|junction|physical"):
        validate_inpn_protected_areas_extraction(extraction, config)
```

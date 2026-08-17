# `tests/unit/test_inpn_protected_areas_fr.py`

## File identity

- Repository path: `tests/unit/test_inpn_protected_areas_fr.py`
- File type: Python test
- Primary responsibility: Provides complete unit and regression coverage for the `inpn_protected_areas_fr` contracts exercised in this file.
- Layer / domain: `unit/regression test` / `test`
- Public or internal role: Internal test support; not a production API.
- Source SHA256: `1f4561a2e58cd09b3a1d934ce0998af09d9f81eb67ae53cd47e5c830ad60366d`

## 1. Purpose

Provides complete unit and regression coverage for the `inpn_protected_areas_fr` contracts exercised in this file.

## 2. Position in LandScout architecture

This file is a `unit/regression test` artifact in the `test` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from __future__ import annotations` — required by the implementation paths and symbols documented below.
- `import io` — required by the implementation paths and symbols documented below.
- `import json` — required by the implementation paths and symbols documented below.
- `import warnings` — required by the implementation paths and symbols documented below.
- `import zipfile` — required by the implementation paths and symbols documented below.
- `from contextlib import contextmanager` — required by the implementation paths and symbols documented below.
- `from dataclasses import FrozenInstanceError, fields, replace` — required by the implementation paths and symbols documented below.
- `from datetime import datetime` — required by the implementation paths and symbols documented below.
- `from hashlib import sha256` — required by the implementation paths and symbols documented below.
- `from pathlib import Path` — required by the implementation paths and symbols documented below.
- `from typing import Any, Self` — required by the implementation paths and symbols documented below.

### Third-party

- `import inspect` — required by the implementation paths and symbols documented below.
- `import stat` — required by the implementation paths and symbols documented below.
- `import pytest` — required by the implementation paths and symbols documented below.
- `import yaml` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout import sources` — required by the implementation paths and symbols documented below.
- `from landscout.common import safe_http` — required by the implementation paths and symbols documented below.
- `from landscout.common.safe_http import SafeHttpsError` — required by the implementation paths and symbols documented below.
- `from landscout.sources import inpn_protected_areas_fr as inpn` — required by the implementation paths and symbols documented below.
- `from landscout.sources.inpn_protected_areas_fr import ( InpnProtectedAreasDownload, InpnProtectedAreasExtractedFile, InpnProtectedAreasExtraction, InpnProtectedAreasSourceConfig, InpnProtectedAreasSourceError, download_inpn_protected_areas_archive, extract_inpn_protected_areas_archive, load_inpn_pr…` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `CONFIG_PATH` | `Path("configs/sources/inpn_protected_areas_fr.yaml")` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `EXPECTED_EXPORTS` | `{ "InpnProtectedAreasDownload", "InpnProtectedAreasExtractedFile", "InpnProtectedAreasExtraction", "InpnProtectedAreasSourceConfig", "InpnProtectedAreasSourceError", "download_inpn_protected_areas_archive", "extract_inpn_protected_areas_archive", "load_inpn_protected_areas_source_config", }` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

### `_Response`

**Purpose:** Groups the `Response` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `object`.

**Model form and mutability:** class inheriting from `object`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `raw` | `not explicitly annotated` | `assigned in `__init__` from `io.BytesIO(payload)`` | `not explicitly annotated` state used by `tests/unit/test_inpn_protected_areas_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `url` | `not explicitly annotated` | `assigned in `__init__` from `url`` | Canonical HTTPS URL retained for request identity, redirects, lineage, or provenance according to the owning model. |
| `status_code` | `not explicitly annotated` | `assigned in `__init__` from `status_code`` | Exact configured or source code whose vocabulary/format is enforced by the owning validator. |
| `headers` | `not explicitly annotated` | `assigned in `__init__` from `{} if location is None else {'Location': location}`` | `not explicitly annotated` state used by `tests/unit/test_inpn_protected_areas_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `closed` | `not explicitly annotated` | `assigned in `__init__` from `False`` | `not explicitly annotated` state used by `tests/unit/test_inpn_protected_areas_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- `__init__` — `def __init__(         self,         payload: bytes,         *,         url: str,         status_code: int = 200,         location: str | None = None,     ) -> None:`; decorators `none`. The complete method algorithm appears in the function/method section.
- `is_redirect` — `def is_redirect(self) -> bool:`; decorators `property`. The complete method algorithm appears in the function/method section.
- `raise_for_status` — `def raise_for_status(self) -> None:`; decorators `none`. The complete method algorithm appears in the function/method section.
- `iter_content` — `def iter_content(self, chunk_size: int = 8192) -> Any:`; decorators `none`. The complete method algorithm appears in the function/method section.
- `close` — `def close(self) -> None:`; decorators `none`. The complete method algorithm appears in the function/method section.
- `read` — `def read(self, size: int = -1) -> bytes:`; decorators `none`. The complete method algorithm appears in the function/method section.
- `__enter__` — `def __enter__(self) -> Self:`; decorators `none`. The complete method algorithm appears in the function/method section.
- `__exit__` — `def __exit__(self, *args: object) -> None:`; decorators `none`. The complete method algorithm appears in the function/method section.

### `_Session`

**Purpose:** Groups the `Session` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `object`.

**Model form and mutability:** class inheriting from `object`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `responses` | `not explicitly annotated` | `assigned in `__init__` from `list(responses or ([] if response is None else [response]))`` | `not explicitly annotated` state used by `tests/unit/test_inpn_protected_areas_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `error` | `not explicitly annotated` | `assigned in `__init__` from `error`` | `not explicitly annotated` state used by `tests/unit/test_inpn_protected_areas_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `calls` | `list[tuple[str, dict[str, object]]]` | `assigned in `__init__` from `[]`` | `list[tuple[str, dict[str, object]]]` state used by `tests/unit/test_inpn_protected_areas_fr.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- `__init__` — `def __init__(         self,         response: _Response | None = None,         *,         responses: list[_Response] | None = None,         error: Exception | None = None,     ) -> None:`; decorators `none`. The complete method algorithm appears in the function/method section.
- `get` — `def get(self, url: str, **kwargs: object) -> _Response:`; decorators `none`. The complete method algorithm appears in the function/method section.
- `open` — `def open(         self,         url: str,         *,         timeout: float,         headers: dict[str, str] | None = None,         max_redirects: int = 10,     ) -> Any:`; decorators `contextmanager`. The complete method algorithm appears in the function/method section.

### `test_midstream_protocol_failure_has_controlled_error._FailingRaw`

**Purpose:** Groups the `FailingRaw` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `object`.

**Model form and mutability:** class inheriting from `object`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- `seek` — `def seek(self, offset: int) -> int:`; decorators `none`. The complete method algorithm appears in the function/method section.
- `read` — `def read(self, size: int = -1) -> bytes:`; decorators `none`. The complete method algorithm appears in the function/method section.

## 6. Functions and methods

### `_Response.__init__`

**Signature**

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

Implements init according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `payload` (`bytes`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `url` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `status_code` (`int`; optional/default `200`) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `location` (`str | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `self.raw` from `io.BytesIO(payload)`.
2. Computes `self.url` from `url`.
3. Computes `self.status_code` from `status_code`.
4. Computes `self.headers` from `{} if location is None else {'Location': location}`.
5. Computes `self.closed` from `False`.

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

### `_Response.is_redirect`

**Signature**

```python
def is_redirect(self) -> bool:
```

**Purpose**

Returns whether `redirect` satisfies the exact predicates and branches listed below.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bool`. Observed return expression(s): `self.status_code in {301, 302, 303, 307, 308} and 'Location' in self.headers`.

**Algorithm**

1. Returns `self.status_code in {301, 302, 303, 307, 308} and 'Location' in self.headers`.

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

### `_Response.raise_for_status`

**Signature**

```python
def raise_for_status(self) -> None:
```

**Purpose**

Implements raise for status according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `self.status_code >= 400`. When true: Raises `OSError(f'HTTP {self.status_code}')`.

**Validation and invariants**

- Rejects or diverts the path when `self.status_code >= 400` is true.

**Exceptions**

- Explicitly raises: `OSError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `OSError`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_Response.iter_content`

**Signature**

```python
def iter_content(self, chunk_size: int = 8192) -> Any:
```

**Purpose**

Implements iter content according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `chunk_size` (`int`; optional/default `8192`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `Any`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Repeats the guarded body while `(chunk := self.raw.read(chunk_size))` remains true.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `self.raw.read`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_Response.close`

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

### `_Response.read`

**Signature**

```python
def read(self, size: int = -1) -> bytes:
```

**Purpose**

Reads and validates read according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `size` (`int`; optional/default `-1`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bytes`. Observed return expression(s): `self.raw.read(size)`.

**Algorithm**

1. Returns `self.raw.read(size)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `self.raw.read`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_Response.__enter__`

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

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_Response.__exit__`

**Signature**

```python
def __exit__(self, *args: object) -> None:
```

**Purpose**

Implements exit according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

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

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_Session.__init__`

**Signature**

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

Implements init according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `response` (`_Response | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `responses` (`list[_Response] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `error` (`Exception | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `self.responses` from `list(responses or ([] if response is None else [response]))`.
2. Computes `self.error` from `error`.
3. Defines `self.calls` with annotation `list[tuple[str, dict[str, object]]]` from `[]`.

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

### `_Session.get`

**Signature**

```python
def get(self, url: str, **kwargs: object) -> _Response:
```

**Purpose**

Implements get according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `url` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `_Response`. Observed return expression(s): `response`.

**Algorithm**

1. Calls `self.calls.append((url, kwargs))` for its validation or side effect.
2. Checks `self.error is not None`. When true: Raises `self.error`.
3. Checks `not self.responses`. When true: Raises `AssertionError('No fake HTTP response was configured')`.
4. Computes `response` from `self.responses.pop(0)`.
5. Calls `response.raw.seek(0)` for its validation or side effect.
6. Returns `response`.

**Validation and invariants**

- Rejects or diverts the path when `self.error is not None` is true.
- Rejects or diverts the path when `not self.responses` is true.

**Exceptions**

- Explicitly raises: `AssertionError`, `self.error`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `AssertionError`, `response.raw.seek`, `self.calls.append`, `self.responses.pop`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_Session.open`

**Signature**

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

Implements open according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `url` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `timeout` (`float`; required) — network timeout in seconds; validation rejects unsupported or non-positive values. Nullability and accepted values are exactly those enforced by the guards listed below.
- `headers` (`dict[str, str] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `max_redirects` (`int`; optional/default `10`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `Any`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `response` from `self.get(url, timeout=timeout, headers=headers, max_redirects=max_redirects)`.
2. Checks `not 200 <= response.status_code < 300`. When true: Raises `SafeHttpsError(f'HTTP status {response.status_code}')`.
3. Runs guarded operation: Evaluates `(yield response)`. Handles no explicit exception types. Finally: Calls `response.close()` for its validation or side effect.

**Validation and invariants**

- Rejects or diverts the path when `not 200 <= response.status_code < 300` is true.

**Exceptions**

- Explicitly raises: `SafeHttpsError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `SafeHttpsError`, `response.close`, `self.get`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_zip_bytes`

**Signature**

```python
def _zip_bytes(
    members: dict[str, bytes] | list[tuple[str, bytes]] | None = None,
) -> bytes:
```

**Purpose**

Implements zip bytes according to the exact implementation and guards in this file.

**Inputs**

- `members` (`dict[str, bytes] | list[tuple[str, bytes]] | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bytes`. Observed return expression(s): `stream.getvalue()`.

**Algorithm**

1. Computes `values` from `members or {'EP/readme.txt': b'protected areas'}`.
2. Computes `entries` from `list(values.items()) if isinstance(values, dict) else values`.
3. Computes `stream` from `io.BytesIO()`.
4. Enters managed context(s) `warnings.catch_warnings()` and executes: Calls `warnings.simplefilter('ignore', UserWarning)` for its validation or side effect. Enters managed context(s) `zipfile.ZipFile(stream, 'w', compression=zipfile.ZIP_STORED)` and executes: Iterates `(name, payload)` over `entries`. For each value: Computes `info` from `zipfile.ZipInfo(name, date_time=(2026, 7, 1, 0, 0, 0))`. Computes `info.compress_type` from `zipfile.ZIP_STORED`. Calls `archive.writestr(info, payload)` for its validation or side effect.
5. Returns `stream.getvalue()`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `archive.writestr`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `archive.writestr`, `io.BytesIO`, `isinstance`, `list`, `stream.getvalue`, `values.items`, `warnings.catch_warnings`, `warnings.simplefilter`, `zipfile.ZipFile`, `zipfile.ZipInfo`.

**Known repository callers**

- `tests/unit/test_inpn_protected_areas_fr.py` — `_config`
- `tests/unit/test_inpn_protected_areas_fr.py` — `_download`
- `tests/unit/test_inpn_protected_areas_fr.py` — `_session`
- `tests/unit/test_inpn_protected_areas_fr.py` — `_unsupported_compression_zip`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_cold_download_must_match_configured_snapshot_before_publication`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_complete_zip_inventory_is_validated_before_member_copy`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_coordinated_cache_and_metadata_snapshot_change_is_not_a_cache_hit`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_duplicate_or_colliding_zip_destinations_are_rejected`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_exact_file_inventory_does_not_omit_unknown_suffixes`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_extraction_inventory_is_complete_ordered_and_hashed`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_extraction_rejects_stale_download_bytes`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_extraction_validates_complete_inventory_before_copying`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_http_and_payload_failures_are_controlled`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_invalid_download_cache_is_a_miss`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_invalid_extraction_cache_is_rebuilt`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_malformed_response_headers_have_controlled_error`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_midstream_protocol_failure_has_controlled_error`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_normal_nested_members_are_accepted`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_successful_first_and_replacement_publication`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_unsafe_zip_member_paths_are_rejected`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_valid_zip_download_binds_exact_bytes_and_lineage`

**Tests**

- `tests/unit/test_inpn_protected_areas_fr.py::test_cold_download_must_match_configured_snapshot_before_publication`
- `tests/unit/test_inpn_protected_areas_fr.py::test_complete_zip_inventory_is_validated_before_member_copy`
- `tests/unit/test_inpn_protected_areas_fr.py::test_coordinated_cache_and_metadata_snapshot_change_is_not_a_cache_hit`
- `tests/unit/test_inpn_protected_areas_fr.py::test_duplicate_or_colliding_zip_destinations_are_rejected`
- `tests/unit/test_inpn_protected_areas_fr.py::test_exact_file_inventory_does_not_omit_unknown_suffixes`
- `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_inventory_is_complete_ordered_and_hashed`
- `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_rejects_stale_download_bytes`
- `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_validates_complete_inventory_before_copying`
- `tests/unit/test_inpn_protected_areas_fr.py::test_http_and_payload_failures_are_controlled`
- `tests/unit/test_inpn_protected_areas_fr.py::test_invalid_download_cache_is_a_miss`
- `tests/unit/test_inpn_protected_areas_fr.py::test_invalid_extraction_cache_is_rebuilt`
- `tests/unit/test_inpn_protected_areas_fr.py::test_malformed_response_headers_have_controlled_error`
- `tests/unit/test_inpn_protected_areas_fr.py::test_midstream_protocol_failure_has_controlled_error`
- `tests/unit/test_inpn_protected_areas_fr.py::test_normal_nested_members_are_accepted`
- `tests/unit/test_inpn_protected_areas_fr.py::test_successful_first_and_replacement_publication`
- `tests/unit/test_inpn_protected_areas_fr.py::test_unsafe_zip_member_paths_are_rejected`
- `tests/unit/test_inpn_protected_areas_fr.py::test_valid_zip_download_binds_exact_bytes_and_lineage`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_special_zip`

**Signature**

```python
def _special_zip(name: str, mode: int) -> bytes:
```

**Purpose**

Implements special zip according to the exact implementation and guards in this file.

**Inputs**

- `name` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `mode` (`int`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bytes`. Observed return expression(s): `stream.getvalue()`.

**Algorithm**

1. Computes `stream` from `io.BytesIO()`.
2. Enters managed context(s) `zipfile.ZipFile(stream, 'w')` and executes: Computes `info` from `zipfile.ZipInfo(name)`. Computes `info.create_system` from `3`. Computes `info.external_attr` from `mode << 16`. Calls `archive.writestr(info, b'target')` for its validation or side effect.
3. Returns `stream.getvalue()`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `archive.writestr`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `archive.writestr`, `io.BytesIO`, `stream.getvalue`, `zipfile.ZipFile`, `zipfile.ZipInfo`.

**Known repository callers**

- `tests/unit/test_inpn_protected_areas_fr.py` — `test_zip_links_and_special_files_are_rejected`

**Tests**

- `tests/unit/test_inpn_protected_areas_fr.py::test_zip_links_and_special_files_are_rejected`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_unsupported_compression_zip`

**Signature**

```python
def _unsupported_compression_zip() -> bytes:
```

**Purpose**

Implements unsupported compression zip according to the exact implementation and guards in this file.

**Inputs**

- No parameters.

**Returns**

- Declared return type: `bytes`. Observed return expression(s): `bytes(payload)`.

**Algorithm**

1. Computes `payload` from `bytearray(_zip_bytes())`.
2. Computes `local` from `payload.index(b'PK\x03\x04')`.
3. Computes `central` from `payload.index(b'PK\x01\x02')`.
4. Computes `payload[local + 8:local + 10]` from `99 .to_bytes(2, 'little')`.
5. Computes `payload[central + 10:central + 12]` from `99 .to_bytes(2, 'little')`.
6. Returns `bytes(payload)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `99 .to_bytes`, `_zip_bytes`, `bytearray`, `bytes`, `payload.index`.

**Known repository callers**

- `tests/unit/test_inpn_protected_areas_fr.py` — `test_unsupported_zip_compression_has_controlled_error`

**Tests**

- `tests/unit/test_inpn_protected_areas_fr.py::test_unsupported_zip_compression_has_controlled_error`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_config_payload`

**Signature**

```python
def _config_payload() -> dict[str, object]:
```

**Purpose**

Implements config payload according to the exact implementation and guards in this file.

**Inputs**

- No parameters.

**Returns**

- Declared return type: `dict[str, object]`. Observed return expression(s): `payload`.

**Algorithm**

1. Computes `payload` from `yaml.safe_load(CONFIG_PATH.read_text(encoding='utf-8'))`.
2. Asserts `isinstance(payload, dict)`.
3. Returns `payload`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `CONFIG_PATH.read_text`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `CONFIG_PATH.read_text`, `isinstance`, `yaml.safe_load`.

**Known repository callers**

- `tests/unit/test_inpn_protected_areas_fr.py` — `_config`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_config_rejects_invalid_expected_snapshot_integrity`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_config_rejects_noncanonical_values`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_download_cache_setup_failure_is_controlled`

**Tests**

- `tests/unit/test_inpn_protected_areas_fr.py::test_config_rejects_invalid_expected_snapshot_integrity`
- `tests/unit/test_inpn_protected_areas_fr.py::test_config_rejects_noncanonical_values`
- `tests/unit/test_inpn_protected_areas_fr.py::test_download_cache_setup_failure_is_controlled`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_write_config`

**Signature**

```python
def _write_config(tmp_path: Path, payload: dict[str, object]) -> Path:
```

**Purpose**

Writes config according to the exact implementation and guards in this file.

**Inputs**

- `tmp_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `payload` (`dict[str, object]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `Path`. Observed return expression(s): `path`.

**Algorithm**

1. Computes `path` from `tmp_path / 'source.yaml'`.
2. Calls `path.write_text(yaml.safe_dump(payload, allow_unicode=True, sort_keys=False), encoding='utf-8')` for its validation or side effect.
3. Returns `path`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `path.write_text`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `path.write_text`, `yaml.safe_dump`.

**Known repository callers**

- `tests/unit/test_inpn_protected_areas_fr.py` — `test_config_rejects_noncanonical_values`

**Tests**

- `tests/unit/test_inpn_protected_areas_fr.py::test_config_rejects_noncanonical_values`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_config`

**Signature**

```python
def _config(
    tmp_path: Path,
    expected_bytes: bytes | None = None,
) -> InpnProtectedAreasSourceConfig:
```

**Purpose**

Implements config according to the exact implementation and guards in this file.

**Inputs**

- `tmp_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `expected_bytes` (`bytes | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `InpnProtectedAreasSourceConfig`. Observed return expression(s): `InpnProtectedAreasSourceConfig.model_validate(payload)`.

**Algorithm**

1. Computes `snapshot` from `_zip_bytes() if expected_bytes is None else expected_bytes`.
2. Computes `payload` from `_config_payload()`.
3. Computes `payload['cache_root']` from `str(tmp_path / 'cache')`.
4. Computes `payload['expected_archive_size_bytes']` from `len(snapshot)`.
5. Computes `payload['expected_archive_sha256']` from `sha256(snapshot).hexdigest()`.
6. Returns `InpnProtectedAreasSourceConfig.model_validate(payload)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `InpnProtectedAreasSourceConfig.model_validate`, `_config_payload`, `_zip_bytes`, `len`, `sha256`, `sha256(snapshot).hexdigest`, `str`.

**Known repository callers**

- `tests/unit/test_inpn_protected_areas_fr.py` — `_download`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_cold_download_must_match_configured_snapshot_before_publication`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_complete_zip_inventory_is_validated_before_member_copy`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_download_uses_no_hidden_reference_page_scrape`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_duplicate_or_colliding_zip_destinations_are_rejected`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_extraction_rejects_wrong_download_type`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_http_and_payload_failures_are_controlled`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_malformed_response_headers_have_controlled_error`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_midstream_protocol_failure_has_controlled_error`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_unsafe_zip_member_paths_are_rejected`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_unsupported_zip_compression_has_controlled_error`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_valid_zip_download_binds_exact_bytes_and_lineage`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_zip_links_and_special_files_are_rejected`

**Tests**

- `tests/unit/test_inpn_protected_areas_fr.py::test_cold_download_must_match_configured_snapshot_before_publication`
- `tests/unit/test_inpn_protected_areas_fr.py::test_complete_zip_inventory_is_validated_before_member_copy`
- `tests/unit/test_inpn_protected_areas_fr.py::test_download_uses_no_hidden_reference_page_scrape`
- `tests/unit/test_inpn_protected_areas_fr.py::test_duplicate_or_colliding_zip_destinations_are_rejected`
- `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_rejects_wrong_download_type`
- `tests/unit/test_inpn_protected_areas_fr.py::test_http_and_payload_failures_are_controlled`
- `tests/unit/test_inpn_protected_areas_fr.py::test_malformed_response_headers_have_controlled_error`
- `tests/unit/test_inpn_protected_areas_fr.py::test_midstream_protocol_failure_has_controlled_error`
- `tests/unit/test_inpn_protected_areas_fr.py::test_unsafe_zip_member_paths_are_rejected`
- `tests/unit/test_inpn_protected_areas_fr.py::test_unsupported_zip_compression_has_controlled_error`
- `tests/unit/test_inpn_protected_areas_fr.py::test_valid_zip_download_binds_exact_bytes_and_lineage`
- `tests/unit/test_inpn_protected_areas_fr.py::test_zip_links_and_special_files_are_rejected`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_session`

**Signature**

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

Implements session according to the exact implementation and guards in this file.

**Inputs**

- `config` (`InpnProtectedAreasSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `payload` (`bytes | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `status_code` (`int`; optional/default `200`) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `redirect_chain` (`tuple[str, ...]`; optional/default `()`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `_Session`. Observed return expression(s): `_Session(responses=responses)`; `_Session(_Response(payload if payload is not None else _zip_bytes(), url=archive_url, status_code=status_code))`.

**Algorithm**

1. Computes `archive_url` from `str(config.archive_url)`.
2. Checks `not redirect_chain`. When true: Returns `_Session(_Response(payload if payload is not None else _zip_bytes(), url=archive_url, status_code=status_code))`.
3. Defines `responses` with annotation `list[_Response]` from `[]`.
4. Computes `current_url` from `archive_url`.
5. Iterates `target_url` over `redirect_chain`. For each value: Calls `responses.append(_Response(b'', url=current_url, status_code=302, location=target_url))` for its validation or side effect. Computes `current_url` from `target_url`.
6. Calls `responses.append(_Response(payload if payload is not None else _zip_bytes(), url=current_url, status_code=status_code))` for its validation or side effect.
7. Returns `_Session(responses=responses)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_Response`, `_Session`, `_zip_bytes`, `responses.append`, `str`.

**Known repository callers**

- `tests/unit/test_inpn_protected_areas_fr.py` — `_download`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_cold_download_must_match_configured_snapshot_before_publication`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_complete_zip_inventory_is_validated_before_member_copy`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_download_cache_setup_failure_is_controlled`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_download_uses_no_hidden_reference_page_scrape`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_duplicate_or_colliding_zip_destinations_are_rejected`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_failed_replacement_restores_a_still_reusable_valid_download_pair`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_http_and_payload_failures_are_controlled`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_invalid_download_cache_is_a_miss`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_publication_failure_restores_old_pair`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_rollback_failure_preserves_recovery_material`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_strict_metadata_rejects_boolean_numeric_values_as_cache_hits`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_successful_first_and_replacement_publication`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_unsafe_zip_member_paths_are_rejected`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_unsupported_zip_compression_has_controlled_error`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_valid_zip_download_binds_exact_bytes_and_lineage`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_zip_links_and_special_files_are_rejected`

**Tests**

- `tests/unit/test_inpn_protected_areas_fr.py::test_cold_download_must_match_configured_snapshot_before_publication`
- `tests/unit/test_inpn_protected_areas_fr.py::test_complete_zip_inventory_is_validated_before_member_copy`
- `tests/unit/test_inpn_protected_areas_fr.py::test_download_cache_setup_failure_is_controlled`
- `tests/unit/test_inpn_protected_areas_fr.py::test_download_uses_no_hidden_reference_page_scrape`
- `tests/unit/test_inpn_protected_areas_fr.py::test_duplicate_or_colliding_zip_destinations_are_rejected`
- `tests/unit/test_inpn_protected_areas_fr.py::test_failed_replacement_restores_a_still_reusable_valid_download_pair`
- `tests/unit/test_inpn_protected_areas_fr.py::test_http_and_payload_failures_are_controlled`
- `tests/unit/test_inpn_protected_areas_fr.py::test_invalid_download_cache_is_a_miss`
- `tests/unit/test_inpn_protected_areas_fr.py::test_publication_failure_restores_old_pair`
- `tests/unit/test_inpn_protected_areas_fr.py::test_rollback_failure_preserves_recovery_material`
- `tests/unit/test_inpn_protected_areas_fr.py::test_strict_metadata_rejects_boolean_numeric_values_as_cache_hits`
- `tests/unit/test_inpn_protected_areas_fr.py::test_successful_first_and_replacement_publication`
- `tests/unit/test_inpn_protected_areas_fr.py::test_unsafe_zip_member_paths_are_rejected`
- `tests/unit/test_inpn_protected_areas_fr.py::test_unsupported_zip_compression_has_controlled_error`
- `tests/unit/test_inpn_protected_areas_fr.py::test_valid_zip_download_binds_exact_bytes_and_lineage`
- `tests/unit/test_inpn_protected_areas_fr.py::test_zip_links_and_special_files_are_rejected`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_download`

**Signature**

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

Downloads and validates download according to the exact implementation and guards in this file.

**Inputs**

- `tmp_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `payload` (`bytes | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[InpnProtectedAreasSourceConfig, InpnProtectedAreasDownload, _Session]`. Observed return expression(s): `(config, result, session)`.

**Algorithm**

1. Computes `snapshot` from `_zip_bytes() if payload is None else payload`.
2. Computes `config` from `_config(tmp_path, snapshot)`.
3. Computes `session` from `_session(config, snapshot)`.
4. Computes `result` from `_download_with_session(config, session)`.
5. Returns `(config, result, session)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `_download_with_session`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `_config`, `_download_with_session`, `_session`, `_zip_bytes`.

**Known repository callers**

- `tests/unit/test_inpn_protected_areas_fr.py` — `test_archive_and_extraction_cache_reuse_are_independent`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_cache_path_binds_version_and_filename`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_coordinated_cache_and_metadata_snapshot_change_is_not_a_cache_hit`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_exact_file_inventory_does_not_omit_unknown_suffixes`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_extraction_backup_move_failure_leaves_old_tree_untouched`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_extraction_cache_setup_failure_is_controlled`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_extraction_inventory_is_complete_ordered_and_hashed`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_extraction_rejects_stale_download_bytes`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_extraction_rejects_wrong_config_type`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_extraction_replacement_failure_restores_old_tree`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_extraction_rollback_failure_preserves_backup`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_extraction_validates_complete_inventory_before_copying`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_failed_replacement_restores_a_still_reusable_valid_download_pair`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_first_extraction_publication_failure_leaves_no_half_root`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_invalid_download_cache_is_a_miss`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_invalid_extraction_cache_is_rebuilt`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_no_stale_parts_after_download_or_extraction_success`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_normal_nested_members_are_accepted`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_publication_failure_restores_old_pair`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_result_dataclasses_are_frozen`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_rollback_failure_preserves_recovery_material`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_strict_metadata_rejects_boolean_numeric_values_as_cache_hits`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_successful_first_and_replacement_publication`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_valid_extraction_cache_is_reused`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_valid_physical_and_metadata_cache_is_reused`

**Tests**

- `tests/unit/test_inpn_protected_areas_fr.py::test_archive_and_extraction_cache_reuse_are_independent`
- `tests/unit/test_inpn_protected_areas_fr.py::test_cache_path_binds_version_and_filename`
- `tests/unit/test_inpn_protected_areas_fr.py::test_coordinated_cache_and_metadata_snapshot_change_is_not_a_cache_hit`
- `tests/unit/test_inpn_protected_areas_fr.py::test_exact_file_inventory_does_not_omit_unknown_suffixes`
- `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_backup_move_failure_leaves_old_tree_untouched`
- `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_cache_setup_failure_is_controlled`
- `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_inventory_is_complete_ordered_and_hashed`
- `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_rejects_stale_download_bytes`
- `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_rejects_wrong_config_type`
- `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_replacement_failure_restores_old_tree`
- `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_rollback_failure_preserves_backup`
- `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_validates_complete_inventory_before_copying`
- `tests/unit/test_inpn_protected_areas_fr.py::test_failed_replacement_restores_a_still_reusable_valid_download_pair`
- `tests/unit/test_inpn_protected_areas_fr.py::test_first_extraction_publication_failure_leaves_no_half_root`
- `tests/unit/test_inpn_protected_areas_fr.py::test_invalid_download_cache_is_a_miss`
- `tests/unit/test_inpn_protected_areas_fr.py::test_invalid_extraction_cache_is_rebuilt`
- `tests/unit/test_inpn_protected_areas_fr.py::test_no_stale_parts_after_download_or_extraction_success`
- `tests/unit/test_inpn_protected_areas_fr.py::test_normal_nested_members_are_accepted`
- `tests/unit/test_inpn_protected_areas_fr.py::test_publication_failure_restores_old_pair`
- `tests/unit/test_inpn_protected_areas_fr.py::test_result_dataclasses_are_frozen`
- `tests/unit/test_inpn_protected_areas_fr.py::test_rollback_failure_preserves_recovery_material`
- `tests/unit/test_inpn_protected_areas_fr.py::test_strict_metadata_rejects_boolean_numeric_values_as_cache_hits`
- `tests/unit/test_inpn_protected_areas_fr.py::test_successful_first_and_replacement_publication`
- `tests/unit/test_inpn_protected_areas_fr.py::test_valid_extraction_cache_is_reused`
- `tests/unit/test_inpn_protected_areas_fr.py::test_valid_physical_and_metadata_cache_is_reused`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_download_with_session`

**Signature**

```python
def _download_with_session(
    config: InpnProtectedAreasSourceConfig,
    session: _Session,
    *,
    timeout_seconds: float = 120.0,
) -> InpnProtectedAreasDownload:
```

**Purpose**

Downloads and validates with session according to the exact implementation and guards in this file.

**Inputs**

- `config` (`InpnProtectedAreasSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `session` (`_Session`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `timeout_seconds` (`float`; optional/default `120.0`) — network timeout in seconds; validation rejects unsupported or non-positive values. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `InpnProtectedAreasDownload`. Observed return expression(s): `download_inpn_protected_areas_archive(config, timeout_seconds=timeout_seconds)`.

**Algorithm**

1. Enters managed context(s) `pytest.MonkeyPatch.context()` and executes: Calls `monkeypatch.setattr(inpn, 'open_safe_https', session.open)` for its validation or side effect. Returns `download_inpn_protected_areas_archive(config, timeout_seconds=timeout_seconds)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `download_inpn_protected_areas_archive`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `download_inpn_protected_areas_archive`, `monkeypatch.setattr`, `pytest.MonkeyPatch.context`.

**Known repository callers**

- `tests/unit/test_inpn_protected_areas_fr.py` — `_download`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_archive_and_extraction_cache_reuse_are_independent`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_cold_download_must_match_configured_snapshot_before_publication`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_complete_zip_inventory_is_validated_before_member_copy`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_coordinated_cache_and_metadata_snapshot_change_is_not_a_cache_hit`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_download_cache_setup_failure_is_controlled`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_download_uses_no_hidden_reference_page_scrape`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_duplicate_or_colliding_zip_destinations_are_rejected`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_failed_replacement_restores_a_still_reusable_valid_download_pair`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_http_and_payload_failures_are_controlled`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_invalid_download_cache_is_a_miss`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_malformed_response_headers_have_controlled_error`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_midstream_protocol_failure_has_controlled_error`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_publication_failure_restores_old_pair`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_rollback_failure_preserves_recovery_material`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_strict_metadata_rejects_boolean_numeric_values_as_cache_hits`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_successful_first_and_replacement_publication`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_unsafe_zip_member_paths_are_rejected`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_unsupported_zip_compression_has_controlled_error`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_valid_zip_download_binds_exact_bytes_and_lineage`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_zip_links_and_special_files_are_rejected`

**Tests**

- `tests/unit/test_inpn_protected_areas_fr.py::test_archive_and_extraction_cache_reuse_are_independent`
- `tests/unit/test_inpn_protected_areas_fr.py::test_cold_download_must_match_configured_snapshot_before_publication`
- `tests/unit/test_inpn_protected_areas_fr.py::test_complete_zip_inventory_is_validated_before_member_copy`
- `tests/unit/test_inpn_protected_areas_fr.py::test_coordinated_cache_and_metadata_snapshot_change_is_not_a_cache_hit`
- `tests/unit/test_inpn_protected_areas_fr.py::test_download_cache_setup_failure_is_controlled`
- `tests/unit/test_inpn_protected_areas_fr.py::test_download_uses_no_hidden_reference_page_scrape`
- `tests/unit/test_inpn_protected_areas_fr.py::test_duplicate_or_colliding_zip_destinations_are_rejected`
- `tests/unit/test_inpn_protected_areas_fr.py::test_failed_replacement_restores_a_still_reusable_valid_download_pair`
- `tests/unit/test_inpn_protected_areas_fr.py::test_http_and_payload_failures_are_controlled`
- `tests/unit/test_inpn_protected_areas_fr.py::test_invalid_download_cache_is_a_miss`
- `tests/unit/test_inpn_protected_areas_fr.py::test_malformed_response_headers_have_controlled_error`
- `tests/unit/test_inpn_protected_areas_fr.py::test_midstream_protocol_failure_has_controlled_error`
- `tests/unit/test_inpn_protected_areas_fr.py::test_publication_failure_restores_old_pair`
- `tests/unit/test_inpn_protected_areas_fr.py::test_rollback_failure_preserves_recovery_material`
- `tests/unit/test_inpn_protected_areas_fr.py::test_strict_metadata_rejects_boolean_numeric_values_as_cache_hits`
- `tests/unit/test_inpn_protected_areas_fr.py::test_successful_first_and_replacement_publication`
- `tests/unit/test_inpn_protected_areas_fr.py::test_unsafe_zip_member_paths_are_rejected`
- `tests/unit/test_inpn_protected_areas_fr.py::test_unsupported_zip_compression_has_controlled_error`
- `tests/unit/test_inpn_protected_areas_fr.py::test_valid_zip_download_binds_exact_bytes_and_lineage`
- `tests/unit/test_inpn_protected_areas_fr.py::test_zip_links_and_special_files_are_rejected`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_download_metadata_path`

**Signature**

```python
def _download_metadata_path(download: InpnProtectedAreasDownload) -> Path:
```

**Purpose**

Downloads and validates metadata path according to the exact implementation and guards in this file.

**Inputs**

- `download` (`InpnProtectedAreasDownload`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `Path`. Observed return expression(s): `download.path.with_name(f'{download.filename}.metadata.json')`.

**Algorithm**

1. Returns `download.path.with_name(f'{download.filename}.metadata.json')`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `download.path.with_name`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `download.path.with_name`.

**Known repository callers**

- `tests/unit/test_inpn_protected_areas_fr.py` — `_force_cache_miss`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_cache_path_binds_version_and_filename`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_coordinated_cache_and_metadata_snapshot_change_is_not_a_cache_hit`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_failed_replacement_restores_a_still_reusable_valid_download_pair`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_invalid_download_cache_is_a_miss`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_rollback_failure_preserves_recovery_material`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_strict_metadata_rejects_boolean_numeric_values_as_cache_hits`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_successful_first_and_replacement_publication`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_valid_zip_download_binds_exact_bytes_and_lineage`

**Tests**

- `tests/unit/test_inpn_protected_areas_fr.py::test_cache_path_binds_version_and_filename`
- `tests/unit/test_inpn_protected_areas_fr.py::test_coordinated_cache_and_metadata_snapshot_change_is_not_a_cache_hit`
- `tests/unit/test_inpn_protected_areas_fr.py::test_failed_replacement_restores_a_still_reusable_valid_download_pair`
- `tests/unit/test_inpn_protected_areas_fr.py::test_invalid_download_cache_is_a_miss`
- `tests/unit/test_inpn_protected_areas_fr.py::test_rollback_failure_preserves_recovery_material`
- `tests/unit/test_inpn_protected_areas_fr.py::test_strict_metadata_rejects_boolean_numeric_values_as_cache_hits`
- `tests/unit/test_inpn_protected_areas_fr.py::test_successful_first_and_replacement_publication`
- `tests/unit/test_inpn_protected_areas_fr.py::test_valid_zip_download_binds_exact_bytes_and_lineage`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_extraction_metadata_path`

**Signature**

```python
def _extraction_metadata_path(extraction: InpnProtectedAreasExtraction) -> Path:
```

**Purpose**

Implements extraction metadata path according to the exact implementation and guards in this file.

**Inputs**

- `extraction` (`InpnProtectedAreasExtraction`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `Path`. Observed return expression(s): `candidates[0]`.

**Algorithm**

1. Computes `candidates` from `sorted((path for path in extraction.extraction_path.iterdir() if path.is_file() and path.name.startswith('.landscout') and (path.suffix == '.json')))`.
2. Asserts `len(candidates) == 1`.
3. Returns `candidates[0]`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `extraction.extraction_path.iterdir`, `len`, `path.is_file`, `path.name.startswith`, `sorted`.

**Known repository callers**

- `tests/unit/test_inpn_protected_areas_fr.py` — `test_extraction_inventory_is_complete_ordered_and_hashed`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_invalid_extraction_cache_is_rebuilt`

**Tests**

- `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_inventory_is_complete_ordered_and_hashed`
- `tests/unit/test_inpn_protected_areas_fr.py::test_invalid_extraction_cache_is_rebuilt`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_read_json`

**Signature**

```python
def _read_json(path: Path) -> dict[str, object]:
```

**Purpose**

Reads and validates json according to the exact implementation and guards in this file.

**Inputs**

- `path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[str, object]`. Observed return expression(s): `payload`.

**Algorithm**

1. Computes `payload` from `json.loads(path.read_text(encoding='utf-8'))`.
2. Asserts `isinstance(payload, dict)`.
3. Returns `payload`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `path.read_text`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `isinstance`, `json.loads`, `path.read_text`.

**Known repository callers**

- `tests/unit/test_inpn_protected_areas_fr.py` — `_force_cache_miss`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_cache_path_binds_version_and_filename`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_coordinated_cache_and_metadata_snapshot_change_is_not_a_cache_hit`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_extraction_inventory_is_complete_ordered_and_hashed`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_invalid_download_cache_is_a_miss`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_invalid_extraction_cache_is_rebuilt`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_strict_metadata_rejects_boolean_numeric_values_as_cache_hits`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_successful_first_and_replacement_publication`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_valid_zip_download_binds_exact_bytes_and_lineage`

**Tests**

- `tests/unit/test_inpn_protected_areas_fr.py::test_cache_path_binds_version_and_filename`
- `tests/unit/test_inpn_protected_areas_fr.py::test_coordinated_cache_and_metadata_snapshot_change_is_not_a_cache_hit`
- `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_inventory_is_complete_ordered_and_hashed`
- `tests/unit/test_inpn_protected_areas_fr.py::test_invalid_download_cache_is_a_miss`
- `tests/unit/test_inpn_protected_areas_fr.py::test_invalid_extraction_cache_is_rebuilt`
- `tests/unit/test_inpn_protected_areas_fr.py::test_strict_metadata_rejects_boolean_numeric_values_as_cache_hits`
- `tests/unit/test_inpn_protected_areas_fr.py::test_successful_first_and_replacement_publication`
- `tests/unit/test_inpn_protected_areas_fr.py::test_valid_zip_download_binds_exact_bytes_and_lineage`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_write_json`

**Signature**

```python
def _write_json(path: Path, payload: dict[str, object]) -> None:
```

**Purpose**

Writes json according to the exact implementation and guards in this file.

**Inputs**

- `path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `payload` (`dict[str, object]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Calls `path.write_text(json.dumps(payload, indent=2) + '\n', encoding='utf-8')` for its validation or side effect.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `path.write_text`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `json.dumps`, `path.write_text`.

**Known repository callers**

- `tests/unit/test_inpn_protected_areas_fr.py` — `_force_cache_miss`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_coordinated_cache_and_metadata_snapshot_change_is_not_a_cache_hit`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_invalid_download_cache_is_a_miss`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_invalid_extraction_cache_is_rebuilt`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_strict_metadata_rejects_boolean_numeric_values_as_cache_hits`

**Tests**

- `tests/unit/test_inpn_protected_areas_fr.py::test_coordinated_cache_and_metadata_snapshot_change_is_not_a_cache_hit`
- `tests/unit/test_inpn_protected_areas_fr.py::test_invalid_download_cache_is_a_miss`
- `tests/unit/test_inpn_protected_areas_fr.py::test_invalid_extraction_cache_is_rebuilt`
- `tests/unit/test_inpn_protected_areas_fr.py::test_strict_metadata_rejects_boolean_numeric_values_as_cache_hits`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_midstream_protocol_failure_has_controlled_error._FailingRaw.seek`

**Signature**

```python
def seek(self, offset: int) -> int:
```

**Purpose**

Implements seek according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `offset` (`int`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `int`. Observed return expression(s): `offset`.

**Algorithm**

1. Returns `offset`.

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

### `test_midstream_protocol_failure_has_controlled_error._FailingRaw.read`

**Signature**

```python
def read(self, size: int = -1) -> bytes:
```

**Purpose**

Reads and validates read according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `size` (`int`; optional/default `-1`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bytes`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Raises `OSError('connection ended mid-stream')`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `OSError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `OSError`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_valid_physical_and_metadata_cache_is_reused.fail_dns`

**Signature**

```python
def fail_dns(*args: object, **kwargs: object) -> list[tuple[Any, ...]]:
```

**Purpose**

Implements fail dns according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `list[tuple[Any, ...]]`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Raises `AssertionError('DNS used for valid cache hit')`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `AssertionError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `AssertionError`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_valid_physical_and_metadata_cache_is_reused.fail_http`

**Signature**

```python
def fail_http(*args: object, **kwargs: object) -> Any:
```

**Purpose**

Implements fail http according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `Any`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Raises `AssertionError('HTTP used for valid cache hit')`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `AssertionError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `AssertionError`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_force_cache_miss`

**Signature**

```python
def _force_cache_miss(download: InpnProtectedAreasDownload) -> tuple[Path, bytes]:
```

**Purpose**

Implements force cache miss according to the exact implementation and guards in this file.

**Inputs**

- `download` (`InpnProtectedAreasDownload`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[Path, bytes]`. Observed return expression(s): `(metadata_path, metadata_path.read_bytes())`.

**Algorithm**

1. Computes `metadata_path` from `_download_metadata_path(download)`.
2. Computes `metadata` from `_read_json(metadata_path)`.
3. Computes `metadata['sha256']` from `'0' * 64`.
4. Calls `_write_json(metadata_path, metadata)` for its validation or side effect.
5. Returns `(metadata_path, metadata_path.read_bytes())`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `_download_metadata_path`, `_read_json`, `_write_json`, `metadata_path.read_bytes`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `_download_metadata_path`, `_read_json`, `_write_json`, `metadata_path.read_bytes`.

**Known repository callers**

- `tests/unit/test_inpn_protected_areas_fr.py` — `test_publication_failure_restores_old_pair`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_successful_first_and_replacement_publication`

**Tests**

- `tests/unit/test_inpn_protected_areas_fr.py::test_publication_failure_restores_old_pair`
- `tests/unit/test_inpn_protected_areas_fr.py::test_successful_first_and_replacement_publication`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_publication_failure_restores_old_pair.fail_once`

**Signature**

```python
def fail_once(source: Path, target: Path) -> None:
```

**Purpose**

Implements fail once according to the exact implementation and guards in this file.

**Inputs**

- `source` (`Path`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `target` (`Path`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Executes `nonlocal failed`.
2. Computes `wanted` from `first.path if failure_target == 'archive' else metadata_path`.
3. Checks `source.name.endswith('.part') and target == wanted and (not failed)`. When true: Computes `failed` from `True`. Raises `OSError('publication failed')`.
4. Calls `original_replace(source, target)` for its validation or side effect.

**Validation and invariants**

- Rejects or diverts the path when `source.name.endswith('.part') and target == wanted and (not failed)` is true.

**Exceptions**

- Explicitly raises: `OSError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `original_replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `OSError`, `original_replace`, `source.name.endswith`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_rollback_failure_preserves_recovery_material.fail_publication_and_rollback`

**Signature**

```python
def fail_publication_and_rollback(source: Path, target: Path) -> None:
```

**Purpose**

Implements fail publication and rollback according to the exact implementation and guards in this file.

**Inputs**

- `source` (`Path`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `target` (`Path`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `source.name.endswith('.part') and target == metadata_path`. When true: Raises `OSError('publication failed')`.
2. Checks `source.name.endswith('.bak')`. When true: Raises `OSError('rollback failed')`.
3. Calls `original_replace(source, target)` for its validation or side effect.

**Validation and invariants**

- Rejects or diverts the path when `source.name.endswith('.part') and target == metadata_path` is true.
- Rejects or diverts the path when `source.name.endswith('.bak')` is true.

**Exceptions**

- Explicitly raises: `OSError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `original_replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `OSError`, `original_replace`, `source.name.endswith`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_broken_download_recovery_symlink_is_rejected.simulated_is_symlink`

**Signature**

```python
def simulated_is_symlink(path: Path) -> bool:
```

**Purpose**

Implements simulated is symlink according to the exact implementation and guards in this file.

**Inputs**

- `path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bool`. Observed return expression(s): `path == broken_link or original_is_symlink(path)`.

**Algorithm**

1. Returns `path == broken_link or original_is_symlink(path)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `original_is_symlink`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_failed_replacement_restores_a_still_reusable_valid_download_pair.fail_metadata`

**Signature**

```python
def fail_metadata(source: Path, target: Path) -> None:
```

**Purpose**

Implements fail metadata according to the exact implementation and guards in this file.

**Inputs**

- `source` (`Path`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `target` (`Path`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `source.name.endswith('.part') and target == metadata_path`. When true: Raises `OSError('publication failed')`.
2. Calls `original_replace(source, target)` for its validation or side effect.

**Validation and invariants**

- Rejects or diverts the path when `source.name.endswith('.part') and target == metadata_path` is true.

**Exceptions**

- Explicitly raises: `OSError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `original_replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `OSError`, `original_replace`, `source.name.endswith`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_complete_zip_inventory_is_validated_before_member_copy.record_open`

**Signature**

```python
def record_open(self: zipfile.ZipFile, *args: object, **kwargs: object) -> Any:
```

**Purpose**

Implements record open according to the exact implementation and guards in this file.

**Inputs**

- `self` (`zipfile.ZipFile`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `Any`. Observed return expression(s): `original_open(self, *args, **kwargs)`.

**Algorithm**

1. Executes `nonlocal opened`.
2. Updates `opened` using `` and `1`.
3. Returns `original_open(self, *args, **kwargs)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `original_open`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `original_open`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_extraction_validates_complete_inventory_before_copying.record_copy`

**Signature**

```python
def record_copy(*args: object, **kwargs: object) -> None:
```

**Purpose**

Implements record copy according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Executes `nonlocal copied`.
2. Updates `copied` using `` and `1`.
3. Calls `original_copy(*args, **kwargs)` for its validation or side effect.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `original_copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `original_copy`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_tree_snapshot`

**Signature**

```python
def _tree_snapshot(root: Path) -> dict[str, bytes]:
```

**Purpose**

Implements tree snapshot according to the exact implementation and guards in this file.

**Inputs**

- `root` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[str, bytes]`. Observed return expression(s): `{path.relative_to(root).as_posix(): path.read_bytes() for path in sorted(root.rglob('*')) if path.is_file()}`.

**Algorithm**

1. Returns `{path.relative_to(root).as_posix(): path.read_bytes() for path in sorted(root.rglob('*')) if path.is_file()}`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `path.read_bytes`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `path.is_file`, `path.read_bytes`, `path.relative_to`, `path.relative_to(root).as_posix`, `root.rglob`, `sorted`.

**Known repository callers**

- `tests/unit/test_inpn_protected_areas_fr.py` — `test_extraction_backup_move_failure_leaves_old_tree_untouched`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_extraction_replacement_failure_restores_old_tree`
- `tests/unit/test_inpn_protected_areas_fr.py` — `test_extraction_rollback_failure_preserves_backup`

**Tests**

- `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_backup_move_failure_leaves_old_tree_untouched`
- `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_replacement_failure_restores_old_tree`
- `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_rollback_failure_preserves_backup`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_first_extraction_publication_failure_leaves_no_half_root.fail_publish`

**Signature**

```python
def fail_publish(source: Path, target: Path) -> None:
```

**Purpose**

Implements fail publish according to the exact implementation and guards in this file.

**Inputs**

- `source` (`Path`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `target` (`Path`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `source.name.endswith('.part') and target == root`. When true: Raises `OSError('publication failed')`.
2. Calls `original_replace(source, target)` for its validation or side effect.

**Validation and invariants**

- Rejects or diverts the path when `source.name.endswith('.part') and target == root` is true.

**Exceptions**

- Explicitly raises: `OSError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `original_replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `OSError`, `original_replace`, `source.name.endswith`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_extraction_replacement_failure_restores_old_tree.fail_once`

**Signature**

```python
def fail_once(source: Path, target: Path) -> None:
```

**Purpose**

Implements fail once according to the exact implementation and guards in this file.

**Inputs**

- `source` (`Path`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `target` (`Path`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Executes `nonlocal failed`.
2. Checks `source.name.endswith('.part') and target == first.extraction_path and (not failed)`. When true: Computes `failed` from `True`. Raises `OSError('publication failed')`.
3. Calls `original_replace(source, target)` for its validation or side effect.

**Validation and invariants**

- Rejects or diverts the path when `source.name.endswith('.part') and target == first.extraction_path and (not failed)` is true.

**Exceptions**

- Explicitly raises: `OSError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `original_replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `OSError`, `original_replace`, `source.name.endswith`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_extraction_rollback_failure_preserves_backup.fail_publish_and_rollback`

**Signature**

```python
def fail_publish_and_rollback(source: Path, target: Path) -> None:
```

**Purpose**

Implements fail publish and rollback according to the exact implementation and guards in this file.

**Inputs**

- `source` (`Path`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `target` (`Path`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `source.name.endswith('.part') and target == first.extraction_path`. When true: Raises `OSError('publication failed')`.
2. Checks `source == backup and target == first.extraction_path`. When true: Raises `OSError('rollback failed')`.
3. Calls `original_replace(source, target)` for its validation or side effect.

**Validation and invariants**

- Rejects or diverts the path when `source.name.endswith('.part') and target == first.extraction_path` is true.
- Rejects or diverts the path when `source == backup and target == first.extraction_path` is true.

**Exceptions**

- Explicitly raises: `OSError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `original_replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `OSError`, `original_replace`, `source.name.endswith`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_extraction_backup_move_failure_leaves_old_tree_untouched.fail_backup_move`

**Signature**

```python
def fail_backup_move(source: Path, target: Path) -> None:
```

**Purpose**

Implements fail backup move according to the exact implementation and guards in this file.

**Inputs**

- `source` (`Path`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `target` (`Path`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `source == first.extraction_path and target == backup`. When true: Raises `OSError('cannot stage old tree')`.
2. Calls `original_replace(source, target)` for its validation or side effect.

**Validation and invariants**

- Rejects or diverts the path when `source == first.extraction_path and target == backup` is true.

**Exceptions**

- Explicitly raises: `OSError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `original_replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `OSError`, `original_replace`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_checked_in_config_loads_with_exact_source_identity`

**Signature**

```python
def test_checked_in_config_loads_with_exact_source_identity() -> None:
```

**Purpose**

Protects the `checked in config loads with exact source identity` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Computes `config` from `load_inpn_protected_areas_source_config()`.

**Action**

- Calls `load_inpn_protected_areas_source_config`, `type`.

**Expected result**

- Direct assertions: `assert type(config) is InpnProtectedAreasSourceConfig`; `assert config.provider == 'PatriNat'`; `assert config.authority == 'MNHN'`; `assert config.program == 'INPN'`; `assert config.dataset_id == 'EP'`; `assert config.dataset_name == 'Base de référence des espaces protégés français'`; `assert config.declared_version == '07/2026'`; `assert str(config.reference_page_url).startswith('https://www.patrinat.fr/')`; `assert str(config.archive_url) == 'https://assets.patrinat.fr/files/donnees/ep/EP.zip'`; `assert config.archive_filename == 'EP.zip'`; `assert config.expected_archive_size_bytes == 99835011`; `assert config.expected_archive_sha256 == '73688bc37205a5e7f59e2065a0b81fc8cf2a242bdec5d7d2786f083671c4abe5'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `checked in config loads with exact source identity` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `load_inpn_protected_areas_source_config`, `str`, `str(config.reference_page_url).startswith`, `type`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_config_rejects_invalid_expected_snapshot_integrity`

**Signature**

```python
def test_config_rejects_invalid_expected_snapshot_integrity(
    field: str,
    value: object,
) -> None:
```

**Purpose**

Protects the `config rejects invalid expected snapshot integrity` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `field`, `value`.
- Contains 3 explicit setup/context statement(s).
- Computes `payload` from `_config_payload()`.
- Computes `payload[field]` from `value`.
- Enters managed context(s) `pytest.raises((TypeError, ValueError))` and executes: Calls `InpnProtectedAreasSourceConfig.model_validate(payload)` for its validation or side effect.

**Action**

- Calls `InpnProtectedAreasSourceConfig.model_validate`, `_config_payload`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises((TypeError, ValueError)): InpnProtectedAreasSourceConfig.model_validate(payload)`.

**Regression protected**

- Protects the exact `config rejects invalid expected snapshot integrity` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `InpnProtectedAreasSourceConfig.model_validate`, `_config_payload`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_config_rejects_noncanonical_values`

**Signature**

```python
def test_config_rejects_noncanonical_values(tmp_path: Path, mutation: str) -> None:
```

**Purpose**

Protects the `config rejects noncanonical values` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `mutation`.
- Contains 2 explicit setup/context statement(s).
- Computes `payload` from `_config_payload()`.
- Enters managed context(s) `pytest.raises(InpnProtectedAreasSourceError)` and executes: Calls `load_inpn_protected_areas_source_config(_write_config(tmp_path, payload))` for its validation or side effect.

**Action**

- Calls `_config_payload`, `_write_config`, `load_inpn_protected_areas_source_config`, `payload.pop`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(InpnProtectedAreasSourceError): load_inpn_protected_areas_source_config(_write_config(tmp_path, payload))`.

**Regression protected**

- Protects the exact `config rejects noncanonical values` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_config_payload`, `_write_config`, `load_inpn_protected_areas_source_config`, `payload.pop`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_wrong_download_config_type_has_controlled_error`

**Signature**

```python
def test_wrong_download_config_type_has_controlled_error() -> None:
```

**Purpose**

Protects the `wrong download config type has controlled error` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(InpnProtectedAreasSourceError, match='config|type')` and executes: Calls `download_inpn_protected_areas_archive(object())` for its validation or side effect.

**Action**

- Calls `download_inpn_protected_areas_archive`, `object`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(InpnProtectedAreasSourceError, match='config|type'): download_inpn_protected_areas_archive(object())`.

**Regression protected**

- Protects the exact `wrong download config type has controlled error` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `download_inpn_protected_areas_archive`, `object`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_download_timeout_is_strict_finite_positive`

**Signature**

```python
def test_download_timeout_is_strict_finite_positive(timeout: object) -> None:
```

**Purpose**

Protects the `download timeout is strict finite positive` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `timeout`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(InpnProtectedAreasSourceError, match='timeout')` and executes: Calls `download_inpn_protected_areas_archive(load_inpn_protected_areas_source_config(), timeout_seconds=timeout)` for its validation or side effect.

**Action**

- Calls `download_inpn_protected_areas_archive`, `float`, `load_inpn_protected_areas_source_config`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(InpnProtectedAreasSourceError, match='timeout'): download_inpn_protected_areas_archive(load_inpn_protected_areas_source_config(), timeout_seconds=timeout)`.

**Regression protected**

- Protects the exact `download timeout is strict finite positive` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `download_inpn_protected_areas_archive`, `float`, `load_inpn_protected_areas_source_config`, `pytest.mark.parametrize`, `pytest.param`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_download_api_has_no_arbitrary_http_session_injection`

**Signature**

```python
def test_download_api_has_no_arbitrary_http_session_injection() -> None:
```

**Purpose**

Protects the `download api has no arbitrary http session injection` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 0 explicit setup/context statement(s).

**Action**

- Calls `inspect.signature`.

**Expected result**

- Direct assertions: `assert 'session' not in inspect.signature(download_inpn_protected_areas_archive).parameters`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `download api has no arbitrary http session injection` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `inspect.signature`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_download_cache_setup_failure_is_controlled`

**Signature**

```python
def test_download_cache_setup_failure_is_controlled(tmp_path: Path) -> None:
```

**Purpose**

Protects the `download cache setup failure is controlled` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 5 explicit setup/context statement(s).
- Computes `cache_file` from `tmp_path / 'cache-is-a-file'`.
- Computes `payload` from `_config_payload()`.
- Computes `payload['cache_root']` from `str(cache_file)`.
- Computes `config` from `InpnProtectedAreasSourceConfig.model_validate(payload)`.
- Enters managed context(s) `pytest.raises(InpnProtectedAreasSourceError, match='download|cache')` and executes: Calls `_download_with_session(config, _session(config))` for its validation or side effect.

**Action**

- Calls `InpnProtectedAreasSourceConfig.model_validate`, `_config_payload`, `_download_with_session`, `_session`, `cache_file.write_bytes`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(InpnProtectedAreasSourceError, match='download|cache'): _download_with_session(config, _session(config))`.

**Regression protected**

- Protects the exact `download cache setup failure is controlled` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `InpnProtectedAreasSourceConfig.model_validate`, `_config_payload`, `_download_with_session`, `_session`, `cache_file.write_bytes`, `pytest.raises`, `str`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_valid_zip_download_binds_exact_bytes_and_lineage`

**Signature**

```python
def test_valid_zip_download_binds_exact_bytes_and_lineage(tmp_path: Path) -> None:
```

**Purpose**

Protects the `valid zip download binds exact bytes and lineage` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 7 explicit setup/context statement(s).
- Computes `payload` from `_zip_bytes({'EP/data/areas.shp': b'shape', 'EP/data/areas.dbf': b'table'})`.
- Computes `config` from `_config(tmp_path, payload)`.
- Computes `session` from `_session(config, payload)`.
- Computes `result` from `_download_with_session(config, session)`.
- Computes `timestamp` from `datetime.fromisoformat(result.download_timestamp)`.
- Computes `(requested_url, request_options)` from `session.calls[0]`.
- Computes `metadata` from `_read_json(_download_metadata_path(result))`.

**Action**

- Calls `_config`, `_download_metadata_path`, `_download_with_session`, `_read_json`, `_session`, `_zip_bytes`, `datetime.fromisoformat`, `field.endswith`, `getattr`, `result.path.read_bytes`, `result.sha256.lower`, `sha256`, `sha256(payload).hexdigest`, `timestamp.utcoffset`, `timestamp.utcoffset().total_seconds`.

**Expected result**

- Direct assertions: `assert result.cache_hit is False`; `assert result.path.read_bytes() == payload`; `assert result.file_size == len(payload)`; `assert result.sha256 == sha256(payload).hexdigest()`; `assert len(result.sha256) == 64 and result.sha256 == result.sha256.lower()`; `assert timestamp.tzinfo is not None`; `assert timestamp.utcoffset() is not None`; `assert timestamp.utcoffset().total_seconds() == 0`; `assert result.filename == config.archive_filename == 'EP.zip'`; `assert len(session.calls) == 1`; `assert requested_url == str(config.archive_url)`; `assert request_options['timeout'] == pytest.approx(120.0)`; `assert metadata['schema_version'] == 1`; `assert metadata['file_size'] == len(payload)`; `assert metadata['sha256'] == result.sha256`; `assert getattr(result, field) == expected`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `valid zip download binds exact bytes and lineage` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_config`, `_download_metadata_path`, `_download_with_session`, `_read_json`, `_session`, `_zip_bytes`, `datetime.fromisoformat`, `field.endswith`, `getattr`, `len`, `pytest.approx`, `result.path.read_bytes`, `result.sha256.lower`, `sha256`, `sha256(payload).hexdigest`, `str`, `timestamp.utcoffset`, `timestamp.utcoffset().total_seconds`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_cold_download_must_match_configured_snapshot_before_publication`

**Signature**

```python
def test_cold_download_must_match_configured_snapshot_before_publication(
    tmp_path: Path,
    mismatch: str,
) -> None:
```

**Purpose**

Protects the `cold download must match configured snapshot before publication` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `mismatch`.
- Contains 3 explicit setup/context statement(s).
- Computes `expected` from `_zip_bytes()`.
- Computes `config` from `_config(tmp_path, expected)`.
- Enters managed context(s) `pytest.raises(InpnProtectedAreasSourceError, match='size|SHA|snapshot|integrity')` and executes: Calls `_download_with_session(config, _session(config, downloaded))` for its validation or side effect.

**Action**

- Calls `Path`, `Path(config.cache_root).rglob`, `_config`, `_download_with_session`, `_session`, `_zip_bytes`, `sha256`, `sha256(downloaded).digest`, `sha256(expected).digest`.

**Expected result**

- Direct assertions: `assert not list(Path(config.cache_root).rglob('EP.zip'))`; `assert not list(Path(config.cache_root).rglob('*.metadata.json'))`; `assert len(downloaded) != len(expected)`; `assert len(downloaded) == len(expected)`; `assert sha256(downloaded).digest() != sha256(expected).digest()`.
- Expected exception contexts: `with pytest.raises(InpnProtectedAreasSourceError, match='size|SHA|snapshot|integrity'): _download_with_session(config, _session(config, downloaded))`.

**Regression protected**

- Protects the exact `cold download must match configured snapshot before publication` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Path`, `Path(config.cache_root).rglob`, `_config`, `_download_with_session`, `_session`, `_zip_bytes`, `len`, `list`, `pytest.mark.parametrize`, `pytest.raises`, `sha256`, `sha256(downloaded).digest`, `sha256(expected).digest`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_coordinated_cache_and_metadata_snapshot_change_is_not_a_cache_hit`

**Signature**

```python
def test_coordinated_cache_and_metadata_snapshot_change_is_not_a_cache_hit(
    tmp_path: Path,
) -> None:
```

**Purpose**

Protects the `coordinated cache and metadata snapshot change is not a cache hit` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 8 explicit setup/context statement(s).
- Computes `(config, first, _)` from `_download(tmp_path)`.
- Computes `replacement` from `_zip_bytes({'EP/readme.txt': b'protected areaz'})`.
- Computes `metadata_path` from `_download_metadata_path(first)`.
- Computes `metadata` from `_read_json(metadata_path)`.
- Computes `metadata['file_size']` from `len(replacement)`.
- Computes `metadata['sha256']` from `sha256(replacement).hexdigest()`.
- Computes `no_network` from `_Session(error=SafeHttpsError('configured snapshot requires refresh'))`.
- Enters managed context(s) `pytest.raises(InpnProtectedAreasSourceError)` and executes: Calls `_download_with_session(config, no_network)` for its validation or side effect.

**Action**

- Calls `SafeHttpsError`, `_Session`, `_download`, `_download_metadata_path`, `_download_with_session`, `_read_json`, `_write_json`, `_zip_bytes`, `first.path.write_bytes`, `sha256`, `sha256(replacement).hexdigest`.

**Expected result**

- Direct assertions: `assert len(replacement) == first.file_size`; `assert len(no_network.calls) == 1`.
- Expected exception contexts: `with pytest.raises(InpnProtectedAreasSourceError): _download_with_session(config, no_network)`.

**Regression protected**

- Protects the exact `coordinated cache and metadata snapshot change is not a cache hit` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `SafeHttpsError`, `_Session`, `_download`, `_download_metadata_path`, `_download_with_session`, `_read_json`, `_write_json`, `_zip_bytes`, `first.path.write_bytes`, `len`, `pytest.raises`, `sha256`, `sha256(replacement).hexdigest`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_http_and_payload_failures_are_controlled`

**Signature**

```python
def test_http_and_payload_failures_are_controlled(
    tmp_path: Path,
    payload: bytes,
    status: int,
    error: Exception | None,
) -> None:
```

**Purpose**

Protects the `http and payload failures are controlled` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `payload`, `status`, `error`.
- Contains 3 explicit setup/context statement(s).
- Computes `config` from `_config(tmp_path)`.
- Computes `session` from `_Session(error=error) if error is not None else _session(config, payload, status_code=status)`.
- Enters managed context(s) `pytest.raises(InpnProtectedAreasSourceError)` and executes: Calls `_download_with_session(config, session)` for its validation or side effect.

**Action**

- Calls `OSError`, `Path`, `Path(config.cache_root).rglob`, `_Session`, `_config`, `_download_with_session`, `_session`, `_zip_bytes`.

**Expected result**

- Direct assertions: `assert not list(Path(config.cache_root).rglob('*.part'))`.
- Expected exception contexts: `with pytest.raises(InpnProtectedAreasSourceError): _download_with_session(config, session)`.

**Regression protected**

- Protects the exact `http and payload failures are controlled` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `OSError`, `Path`, `Path(config.cache_root).rglob`, `_Session`, `_config`, `_download_with_session`, `_session`, `_zip_bytes`, `list`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unsupported_zip_compression_has_controlled_error`

**Signature**

```python
def test_unsupported_zip_compression_has_controlled_error(tmp_path: Path) -> None:
```

**Purpose**

Protects the `unsupported zip compression has controlled error` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 3 explicit setup/context statement(s).
- Computes `payload` from `_unsupported_compression_zip()`.
- Computes `config` from `_config(tmp_path, payload)`.
- Enters managed context(s) `pytest.raises(InpnProtectedAreasSourceError, match='ZIP|archive')` and executes: Calls `_download_with_session(config, _session(config, payload))` for its validation or side effect.

**Action**

- Calls `_config`, `_download_with_session`, `_session`, `_unsupported_compression_zip`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(InpnProtectedAreasSourceError, match='ZIP|archive'): _download_with_session(config, _session(config, payload))`.

**Regression protected**

- Protects the exact `unsupported zip compression has controlled error` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_config`, `_download_with_session`, `_session`, `_unsupported_compression_zip`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_malformed_response_headers_have_controlled_error`

**Signature**

```python
def test_malformed_response_headers_have_controlled_error(tmp_path: Path) -> None:
```

**Purpose**

Protects the `malformed response headers have controlled error` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 4 explicit setup/context statement(s).
- Computes `config` from `_config(tmp_path)`.
- Computes `response` from `_Response(_zip_bytes(), url=str(config.archive_url))`.
- Computes `response.headers` from `None`.
- Enters managed context(s) `pytest.raises(InpnProtectedAreasSourceError, match='response|download')` and executes: Calls `_download_with_session(config, _Session(response))` for its validation or side effect.

**Action**

- Calls `_Response`, `_Session`, `_config`, `_download_with_session`, `_zip_bytes`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(InpnProtectedAreasSourceError, match='response|download'): _download_with_session(config, _Session(response))`.

**Regression protected**

- Protects the exact `malformed response headers have controlled error` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_Response`, `_Session`, `_config`, `_download_with_session`, `_zip_bytes`, `pytest.raises`, `str`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_midstream_protocol_failure_has_controlled_error`

**Signature**

```python
def test_midstream_protocol_failure_has_controlled_error(tmp_path: Path) -> None:
```

**Purpose**

Protects the `midstream protocol failure has controlled error` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 4 explicit setup/context statement(s).
- Computes `config` from `_config(tmp_path)`.
- Computes `response` from `_Response(_zip_bytes(), url=str(config.archive_url))`.
- Computes `response.raw` from `_FailingRaw()`.
- Enters managed context(s) `pytest.raises(InpnProtectedAreasSourceError, match='response|download')` and executes: Calls `_download_with_session(config, _Session(response))` for its validation or side effect.

**Action**

- Calls `OSError`, `_FailingRaw`, `_Response`, `_Session`, `_config`, `_download_with_session`, `_zip_bytes`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(InpnProtectedAreasSourceError, match='response|download'): _download_with_session(config, _Session(response))`.

**Regression protected**

- Protects the exact `midstream protocol failure has controlled error` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `OSError`, `_FailingRaw`, `_Response`, `_Session`, `_config`, `_download_with_session`, `_zip_bytes`, `pytest.raises`, `str`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_valid_physical_and_metadata_cache_is_reused`

**Signature**

```python
def test_valid_physical_and_metadata_cache_is_reused(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `valid physical and metadata cache is reused` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`.
- Contains 2 explicit setup/context statement(s).
- Computes `(config, first, _)` from `_download(tmp_path)`.
- Computes `second` from `download_inpn_protected_areas_archive(config)`.

**Action**

- Calls `AssertionError`, `_download`, `download_inpn_protected_areas_archive`, `monkeypatch.setattr`.

**Expected result**

- Direct assertions: `assert second.cache_hit is True`; `assert second.file_size == first.file_size`; `assert second.sha256 == first.sha256`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `valid physical and metadata cache is reused` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `AssertionError`, `_download`, `download_inpn_protected_areas_archive`, `monkeypatch.setattr`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_invalid_download_cache_is_a_miss`

**Signature**

```python
def test_invalid_download_cache_is_a_miss(
    tmp_path: Path,
    mutation: str,
) -> None:
```

**Purpose**

Protects the `invalid download cache is a miss` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `mutation`.
- Contains 5 explicit setup/context statement(s).
- Computes `(config, first, _)` from `_download(tmp_path)`.
- Computes `metadata_path` from `_download_metadata_path(first)`.
- Computes `metadata` from `_read_json(metadata_path)`.
- Computes `session` from `_session(config)`.
- Computes `refreshed` from `_download_with_session(config, session)`.

**Action**

- Calls `_download`, `_download_metadata_path`, `_download_with_session`, `_read_json`, `_session`, `_write_json`, `_zip_bytes`, `first.path.write_bytes`, `json.dumps`, `metadata_json.replace`, `metadata_path.write_text`, `sha256`, `sha256(invalid_zip).hexdigest`.

**Expected result**

- Direct assertions: `assert refreshed.cache_hit is False`; `assert len(session.calls) == 1`; `assert len(replacement) == first.file_size`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `invalid download cache is a miss` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_download`, `_download_metadata_path`, `_download_with_session`, `_read_json`, `_session`, `_write_json`, `_zip_bytes`, `first.path.write_bytes`, `json.dumps`, `len`, `metadata_json.replace`, `metadata_path.write_text`, `pytest.mark.parametrize`, `sha256`, `sha256(invalid_zip).hexdigest`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_successful_first_and_replacement_publication`

**Signature**

```python
def test_successful_first_and_replacement_publication(tmp_path: Path) -> None:
```

**Purpose**

Protects the `successful first and replacement publication` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 3 explicit setup/context statement(s).
- Computes `(config, first, _)` from `_download(tmp_path)`.
- Computes `replacement` from `_zip_bytes()`.
- Computes `second` from `_download_with_session(config, _session(config, replacement))`.

**Action**

- Calls `Path`, `Path(config.cache_root).rglob`, `_download`, `_download_metadata_path`, `_download_with_session`, `_force_cache_miss`, `_read_json`, `_session`, `_zip_bytes`, `second.path.read_bytes`.

**Expected result**

- Direct assertions: `assert second.cache_hit is False`; `assert second.path.read_bytes() == replacement`; `assert _read_json(_download_metadata_path(second))['sha256'] == second.sha256`; `assert not list(Path(config.cache_root).rglob('*.part'))`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `successful first and replacement publication` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Path`, `Path(config.cache_root).rglob`, `_download`, `_download_metadata_path`, `_download_with_session`, `_force_cache_miss`, `_read_json`, `_session`, `_zip_bytes`, `list`, `second.path.read_bytes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_publication_failure_restores_old_pair`

**Signature**

```python
def test_publication_failure_restores_old_pair(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    failure_target: str,
) -> None:
```

**Purpose**

Protects the `publication failure restores old pair` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`, `failure_target`.
- Contains 7 explicit setup/context statement(s).
- Computes `(config, first, _)` from `_download(tmp_path)`.
- Computes `(metadata_path, _)` from `_force_cache_miss(first)`.
- Computes `old_archive` from `first.path.read_bytes()`.
- Computes `old_metadata` from `metadata_path.read_bytes()`.
- Computes `original_replace` from `inpn._replace_file`.
- Computes `failed` from `False`.
- Enters managed context(s) `pytest.raises(InpnProtectedAreasSourceError, match='publication|download')` and executes: Calls `_download_with_session(config, _session(config))` for its validation or side effect.

**Action**

- Calls `OSError`, `Path`, `Path(config.cache_root).rglob`, `_download`, `_download_with_session`, `_force_cache_miss`, `_session`, `first.path.read_bytes`, `metadata_path.read_bytes`, `monkeypatch.setattr`, `original_replace`, `source.name.endswith`.

**Expected result**

- Direct assertions: `assert first.path.read_bytes() == old_archive`; `assert metadata_path.read_bytes() == old_metadata`; `assert not list(Path(config.cache_root).rglob('*.part'))`; `assert not list(Path(config.cache_root).rglob('*.bak'))`.
- Expected exception contexts: `with pytest.raises(InpnProtectedAreasSourceError, match='publication|download'): _download_with_session(config, _session(config))`.

**Regression protected**

- Protects the exact `publication failure restores old pair` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `OSError`, `Path`, `Path(config.cache_root).rglob`, `_download`, `_download_with_session`, `_force_cache_miss`, `_session`, `first.path.read_bytes`, `list`, `metadata_path.read_bytes`, `monkeypatch.setattr`, `original_replace`, `pytest.mark.parametrize`, `pytest.raises`, `source.name.endswith`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_rollback_failure_preserves_recovery_material`

**Signature**

```python
def test_rollback_failure_preserves_recovery_material(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `rollback failure preserves recovery material` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`.
- Contains 8 explicit setup/context statement(s).
- Computes `(config, first, _)` from `_download(tmp_path)`.
- Computes `metadata_path` from `_download_metadata_path(first)`.
- Computes `old_archive` from `first.path.read_bytes()`.
- Computes `old_metadata` from `metadata_path.read_bytes()`.
- Computes `original_replace` from `inpn._replace_file`.
- Enters managed context(s) `pytest.raises(InpnProtectedAreasSourceError, match='rollback')` and executes: Calls `_download_with_session(config, _session(config))` for its validation or side effect.
- Computes `archive_backup` from `first.path.with_name(f'{first.path.name}.bak')`.
- Computes `metadata_backup` from `metadata_path.with_name(f'{metadata_path.name}.bak')`.

**Action**

- Calls `OSError`, `_download`, `_download_metadata_path`, `_download_with_session`, `_session`, `archive_backup.read_bytes`, `first.path.read_bytes`, `first.path.with_name`, `metadata_backup.read_bytes`, `metadata_path.read_bytes`, `metadata_path.with_name`, `monkeypatch.setattr`, `original_replace`, `source.name.endswith`.

**Expected result**

- Direct assertions: `assert archive_backup.read_bytes() == old_archive`; `assert metadata_backup.read_bytes() == old_metadata`.
- Expected exception contexts: `with pytest.raises(InpnProtectedAreasSourceError, match='rollback'): _download_with_session(config, _session(config))`.

**Regression protected**

- Protects the exact `rollback failure preserves recovery material` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `OSError`, `_download`, `_download_metadata_path`, `_download_with_session`, `_session`, `archive_backup.read_bytes`, `first.path.read_bytes`, `first.path.with_name`, `metadata_backup.read_bytes`, `metadata_path.read_bytes`, `metadata_path.with_name`, `monkeypatch.setattr`, `original_replace`, `pytest.raises`, `source.name.endswith`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_broken_download_recovery_symlink_is_rejected`

**Signature**

```python
def test_broken_download_recovery_symlink_is_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    backup_role: str,
) -> None:
```

**Purpose**

Protects the `broken download recovery symlink is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`, `backup_role`.
- Contains 8 explicit setup/context statement(s).
- Computes `archive_path` from `tmp_path / 'EP.zip'`.
- Computes `metadata_path` from `tmp_path / 'EP.zip.metadata.json'`.
- Computes `temporary_archive` from `tmp_path / 'EP.zip.part'`.
- Computes `temporary_metadata` from `tmp_path / 'EP.zip.metadata.json.part'`.
- Computes `recovery_paths` from `{'archive': archive_path.with_name(f'{archive_path.name}.bak'), 'metadata': metadata_path.with_name(f'{metadata_path.name}.bak')}`.
- Computes `broken_link` from `recovery_paths[backup_role]`.
- Computes `original_is_symlink` from `Path.is_symlink`.
- Enters managed context(s) `pytest.raises(InpnProtectedAreasSourceError, match='backup|recovery|manual')` and executes: Calls `inpn._publish_cache_pair(temporary_archive, temporary_metadata, archive_path, metadata_path)` for its validation or side effect.

**Action**

- Calls `archive_path.exists`, `archive_path.with_name`, `inpn._publish_cache_pair`, `metadata_path.exists`, `metadata_path.with_name`, `monkeypatch.setattr`, `original_is_symlink`, `temporary_archive.read_bytes`, `temporary_archive.write_bytes`, `temporary_metadata.read_bytes`, `temporary_metadata.write_bytes`.

**Expected result**

- Direct assertions: `assert not archive_path.exists()`; `assert not metadata_path.exists()`; `assert temporary_archive.read_bytes() == b'replacement archive'`; `assert temporary_metadata.read_bytes() == b'replacement metadata'`.
- Expected exception contexts: `with pytest.raises(InpnProtectedAreasSourceError, match='backup|recovery|manual'): inpn._publish_cache_pair(temporary_archive, temporary_metadata, archive_path, metadata_path)`.

**Regression protected**

- Protects the exact `broken download recovery symlink is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `archive_path.exists`, `archive_path.with_name`, `inpn._publish_cache_pair`, `metadata_path.exists`, `metadata_path.with_name`, `monkeypatch.setattr`, `original_is_symlink`, `pytest.mark.parametrize`, `pytest.raises`, `temporary_archive.read_bytes`, `temporary_archive.write_bytes`, `temporary_metadata.read_bytes`, `temporary_metadata.write_bytes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_existing_normal_download_recovery_backup_remains_unchanged`

**Signature**

```python
def test_existing_normal_download_recovery_backup_remains_unchanged(
    tmp_path: Path,
) -> None:
```

**Purpose**

Protects the `existing normal download recovery backup remains unchanged` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 7 explicit setup/context statement(s).
- Computes `archive_path` from `tmp_path / 'EP.zip'`.
- Computes `metadata_path` from `tmp_path / 'EP.zip.metadata.json'`.
- Computes `temporary_archive` from `tmp_path / 'EP.zip.part'`.
- Computes `temporary_metadata` from `tmp_path / 'EP.zip.metadata.json.part'`.
- Computes `archive_backup` from `archive_path.with_name(f'{archive_path.name}.bak')`.
- Computes `recovery_bytes` from `b'manual INPN recovery archive'`.
- Enters managed context(s) `pytest.raises(InpnProtectedAreasSourceError, match='backup|recovery|manual')` and executes: Calls `inpn._publish_cache_pair(temporary_archive, temporary_metadata, archive_path, metadata_path)` for its validation or side effect.

**Action**

- Calls `archive_backup.read_bytes`, `archive_backup.write_bytes`, `archive_path.with_name`, `inpn._publish_cache_pair`, `temporary_archive.read_bytes`, `temporary_archive.write_bytes`, `temporary_metadata.read_bytes`, `temporary_metadata.write_bytes`.

**Expected result**

- Direct assertions: `assert archive_backup.read_bytes() == recovery_bytes`; `assert temporary_archive.read_bytes() == b'replacement archive'`; `assert temporary_metadata.read_bytes() == b'replacement metadata'`.
- Expected exception contexts: `with pytest.raises(InpnProtectedAreasSourceError, match='backup|recovery|manual'): inpn._publish_cache_pair(temporary_archive, temporary_metadata, archive_path, metadata_path)`.

**Regression protected**

- Protects the exact `existing normal download recovery backup remains unchanged` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `archive_backup.read_bytes`, `archive_backup.write_bytes`, `archive_path.with_name`, `inpn._publish_cache_pair`, `pytest.raises`, `temporary_archive.read_bytes`, `temporary_archive.write_bytes`, `temporary_metadata.read_bytes`, `temporary_metadata.write_bytes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_failed_replacement_restores_a_still_reusable_valid_download_pair`

**Signature**

```python
def test_failed_replacement_restores_a_still_reusable_valid_download_pair(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `failed replacement restores a still reusable valid download pair` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`.
- Contains 8 explicit setup/context statement(s).
- Computes `(config, first, _)` from `_download(tmp_path)`.
- Computes `metadata_path` from `_download_metadata_path(first)`.
- Computes `old_archive` from `first.path.read_bytes()`.
- Computes `old_metadata` from `metadata_path.read_bytes()`.
- Computes `original_load` from `inpn._load_cached_download`.
- Computes `original_replace` from `inpn._replace_file`.
- Enters managed context(s) `pytest.raises(InpnProtectedAreasSourceError, match='publication')` and executes: Calls `_download_with_session(config, _session(config))` for its validation or side effect.
- Computes `reused` from `_download_with_session(config, _Session(error=AssertionError('network used')))`.

**Action**

- Calls `AssertionError`, `OSError`, `_Session`, `_download`, `_download_metadata_path`, `_download_with_session`, `_session`, `first.path.read_bytes`, `metadata_path.read_bytes`, `monkeypatch.setattr`, `original_replace`, `source.name.endswith`.

**Expected result**

- Direct assertions: `assert first.path.read_bytes() == old_archive`; `assert metadata_path.read_bytes() == old_metadata`; `assert reused.cache_hit is True`.
- Expected exception contexts: `with pytest.raises(InpnProtectedAreasSourceError, match='publication'): _download_with_session(config, _session(config))`.

**Regression protected**

- Protects the exact `failed replacement restores a still reusable valid download pair` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `AssertionError`, `OSError`, `_Session`, `_download`, `_download_metadata_path`, `_download_with_session`, `_session`, `first.path.read_bytes`, `metadata_path.read_bytes`, `monkeypatch.setattr`, `original_replace`, `pytest.raises`, `source.name.endswith`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unsafe_zip_member_paths_are_rejected`

**Signature**

```python
def test_unsafe_zip_member_paths_are_rejected(
    tmp_path: Path,
    member_name: str,
) -> None:
```

**Purpose**

Protects the `unsafe zip member paths are rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `member_name`.
- Contains 3 explicit setup/context statement(s).
- Computes `payload` from `_zip_bytes([(member_name, b'bad')])`.
- Computes `config` from `_config(tmp_path, payload)`.
- Enters managed context(s) `pytest.raises(InpnProtectedAreasSourceError, match='ZIP|archive|member|path')` and executes: Calls `_download_with_session(config, _session(config, payload))` for its validation or side effect.

**Action**

- Calls `_config`, `_download_with_session`, `_session`, `_zip_bytes`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(InpnProtectedAreasSourceError, match='ZIP|archive|member|path'): _download_with_session(config, _session(config, payload))`.

**Regression protected**

- Protects the exact `unsafe zip member paths are rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_config`, `_download_with_session`, `_session`, `_zip_bytes`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_duplicate_or_colliding_zip_destinations_are_rejected`

**Signature**

```python
def test_duplicate_or_colliding_zip_destinations_are_rejected(
    tmp_path: Path,
    members: list[tuple[str, bytes]],
) -> None:
```

**Purpose**

Protects the `duplicate or colliding zip destinations are rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `members`.
- Contains 3 explicit setup/context statement(s).
- Computes `payload` from `_zip_bytes(members)`.
- Computes `config` from `_config(tmp_path, payload)`.
- Enters managed context(s) `pytest.raises(InpnProtectedAreasSourceError, match='duplicate|collid|archive')` and executes: Calls `_download_with_session(config, _session(config, payload))` for its validation or side effect.

**Action**

- Calls `_config`, `_download_with_session`, `_session`, `_zip_bytes`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(InpnProtectedAreasSourceError, match='duplicate|collid|archive'): _download_with_session(config, _session(config, payload))`.

**Regression protected**

- Protects the exact `duplicate or colliding zip destinations are rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_config`, `_download_with_session`, `_session`, `_zip_bytes`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_zip_links_and_special_files_are_rejected`

**Signature**

```python
def test_zip_links_and_special_files_are_rejected(
    tmp_path: Path,
    mode: int,
    message: str,
) -> None:
```

**Purpose**

Protects the `zip links and special files are rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `mode`, `message`.
- Contains 3 explicit setup/context statement(s).
- Computes `payload` from `_special_zip('unsafe', mode)`.
- Computes `config` from `_config(tmp_path, payload)`.
- Enters managed context(s) `pytest.raises(InpnProtectedAreasSourceError, match=message)` and executes: Calls `_download_with_session(config, _session(config, payload))` for its validation or side effect.

**Action**

- Calls `_config`, `_download_with_session`, `_session`, `_special_zip`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(InpnProtectedAreasSourceError, match=message): _download_with_session(config, _session(config, payload))`.

**Regression protected**

- Protects the exact `zip links and special files are rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_config`, `_download_with_session`, `_session`, `_special_zip`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_complete_zip_inventory_is_validated_before_member_copy`

**Signature**

```python
def test_complete_zip_inventory_is_validated_before_member_copy(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `complete zip inventory is validated before member copy` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`.
- Contains 5 explicit setup/context statement(s).
- Computes `payload` from `_zip_bytes([('safe-first.txt', b'safe'), ('../unsafe-last.txt', b'unsafe')])`.
- Computes `config` from `_config(tmp_path, payload)`.
- Computes `opened` from `0`.
- Computes `original_open` from `zipfile.ZipFile.open`.
- Enters managed context(s) `pytest.raises(InpnProtectedAreasSourceError)` and executes: Calls `_download_with_session(config, _session(config, payload))` for its validation or side effect.

**Action**

- Calls `_config`, `_download_with_session`, `_session`, `_zip_bytes`, `monkeypatch.setattr`, `original_open`.

**Expected result**

- Direct assertions: `assert opened == 0`.
- Expected exception contexts: `with pytest.raises(InpnProtectedAreasSourceError): _download_with_session(config, _session(config, payload))`.

**Regression protected**

- Protects the exact `complete zip inventory is validated before member copy` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_config`, `_download_with_session`, `_session`, `_zip_bytes`, `monkeypatch.setattr`, `original_open`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_extraction_validates_complete_inventory_before_copying`

**Signature**

```python
def test_extraction_validates_complete_inventory_before_copying(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `extraction validates complete inventory before copying` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`.
- Contains 6 explicit setup/context statement(s).
- Computes `(config, download, _)` from `_download(tmp_path)`.
- Computes `payload` from `_zip_bytes([('safe-first.txt', b'safe'), ('../unsafe-last.txt', b'unsafe')])`.
- Computes `forged` from `replace(download, file_size=len(payload), sha256=sha256(payload).hexdigest())`.
- Computes `copied` from `0`.
- Computes `original_copy` from `inpn.copyfileobj`.
- Enters managed context(s) `pytest.raises(InpnProtectedAreasSourceError)` and executes: Calls `extract_inpn_protected_areas_archive(forged, config)` for its validation or side effect.

**Action**

- Calls `(download.path.parent / 'x' / forged.sha256).exists`, `_download`, `_zip_bytes`, `download.path.write_bytes`, `extract_inpn_protected_areas_archive`, `monkeypatch.setattr`, `original_copy`, `replace`, `sha256`, `sha256(payload).hexdigest`.

**Expected result**

- Direct assertions: `assert copied == 0`; `assert not (download.path.parent / 'x' / forged.sha256).exists()`.
- Expected exception contexts: `with pytest.raises(InpnProtectedAreasSourceError): extract_inpn_protected_areas_archive(forged, config)`.

**Regression protected**

- Protects the exact `extraction validates complete inventory before copying` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `(download.path.parent / 'x' / forged.sha256).exists`, `_download`, `_zip_bytes`, `download.path.write_bytes`, `extract_inpn_protected_areas_archive`, `len`, `monkeypatch.setattr`, `original_copy`, `pytest.raises`, `replace`, `sha256`, `sha256(payload).hexdigest`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_normal_nested_members_are_accepted`

**Signature**

```python
def test_normal_nested_members_are_accepted(tmp_path: Path) -> None:
```

**Purpose**

Protects the `normal nested members are accepted` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 1 explicit setup/context statement(s).
- Computes `(config, download, _)` from `_download(tmp_path, payload=_zip_bytes({'EP/docs/readme.txt': b'ok'}))`.

**Action**

- Calls `_download`, `_zip_bytes`, `download.path.is_file`.

**Expected result**

- Direct assertions: `assert download.path.is_file()`; `assert download.filename == config.archive_filename`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `normal nested members are accepted` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_download`, `_zip_bytes`, `download.path.is_file`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_extraction_inventory_is_complete_ordered_and_hashed`

**Signature**

```python
def test_extraction_inventory_is_complete_ordered_and_hashed(tmp_path: Path) -> None:
```

**Purpose**

Protects the `extraction inventory is complete ordered and hashed` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 6 explicit setup/context statement(s).
- Computes `payloads` from `{'z-last/empty.cpg': b'', 'EP/data/areas.shp': b'shape', 'EP/data/areas.dbf': b'table', 'EP/metadata.xml': b'<metadata/>'}`.
- Computes `(config, download, _)` from `_download(tmp_path, payload=_zip_bytes(payloads))`.
- Computes `extraction` from `extract_inpn_protected_areas_archive(download, config)`.
- Computes `expected_paths` from `sorted(payloads)`.
- Computes `by_path` from `{item.relative_path: item for item in extraction.files}`.
- Computes `metadata` from `_read_json(_extraction_metadata_path(extraction))`.

**Action**

- Calls `_download`, `_extraction_metadata_path`, `_read_json`, `_zip_bytes`, `extract_inpn_protected_areas_archive`, `extraction.extraction_path.joinpath`, `extraction.extraction_path.joinpath(*relative_path.split('/')).read_bytes`, `extraction.extraction_path.parent.glob`, `payloads.items`, `relative_path.split`, `sha256`, `sha256(b'').hexdigest`, `sha256(payload).hexdigest`, `sorted`.

**Expected result**

- Direct assertions: `assert extraction.cache_hit is False`; `assert [item.relative_path for item in extraction.files] == expected_paths`; `assert len(extraction.files) == len(payloads)`; `assert by_path['z-last/empty.cpg'].file_size == 0`; `assert by_path['z-last/empty.cpg'].sha256 == sha256(b'').hexdigest()`; `assert metadata['schema_version'] == 1`; `assert metadata['archive_sha256'] == download.sha256`; `assert metadata['archive_size'] == download.file_size`; `assert not list(extraction.extraction_path.parent.glob('*.part'))`; `assert item.file_size == len(payload)`; `assert item.sha256 == sha256(payload).hexdigest()`; `assert extraction.extraction_path.joinpath(*relative_path.split('/')).read_bytes() == payload`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `extraction inventory is complete ordered and hashed` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_download`, `_extraction_metadata_path`, `_read_json`, `_zip_bytes`, `extract_inpn_protected_areas_archive`, `extraction.extraction_path.joinpath`, `extraction.extraction_path.joinpath(*relative_path.split('/')).read_bytes`, `extraction.extraction_path.parent.glob`, `len`, `list`, `payloads.items`, `relative_path.split`, `sha256`, `sha256(b'').hexdigest`, `sha256(payload).hexdigest`, `sorted`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_valid_extraction_cache_is_reused`

**Signature**

```python
def test_valid_extraction_cache_is_reused(tmp_path: Path) -> None:
```

**Purpose**

Protects the `valid extraction cache is reused` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 3 explicit setup/context statement(s).
- Computes `(config, download, _)` from `_download(tmp_path)`.
- Computes `first` from `extract_inpn_protected_areas_archive(download, config)`.
- Computes `second` from `extract_inpn_protected_areas_archive(download, config)`.

**Action**

- Calls `_download`, `extract_inpn_protected_areas_archive`.

**Expected result**

- Direct assertions: `assert second.cache_hit is True`; `assert second.files == first.files`; `assert second.extraction_path == first.extraction_path`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `valid extraction cache is reused` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_download`, `extract_inpn_protected_areas_archive`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_invalid_extraction_cache_is_rebuilt`

**Signature**

```python
def test_invalid_extraction_cache_is_rebuilt(
    tmp_path: Path,
    mutation: str,
) -> None:
```

**Purpose**

Protects the `invalid extraction cache is rebuilt` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `mutation`.
- Contains 7 explicit setup/context statement(s).
- Computes `original` from `b'original'`.
- Computes `(config, download, _)` from `_download(tmp_path, payload=_zip_bytes({'EP/value.txt': original}))`.
- Computes `first` from `extract_inpn_protected_areas_archive(download, config)`.
- Computes `data_path` from `first.extraction_path / 'EP' / 'value.txt'`.
- Computes `metadata_path` from `_extraction_metadata_path(first)`.
- Computes `metadata` from `_read_json(metadata_path)`.
- Computes `refreshed` from `extract_inpn_protected_areas_archive(download, config)`.

**Action**

- Calls `(first.extraction_path / 'unexpected.txt').write_bytes`, `(refreshed.extraction_path / 'EP' / 'value.txt').read_bytes`, `(refreshed.extraction_path / 'unexpected.txt').exists`, `_download`, `_extraction_metadata_path`, `_read_json`, `_write_json`, `_zip_bytes`, `data_path.stat`, `data_path.unlink`, `data_path.write_bytes`, `extract_inpn_protected_areas_archive`, `isinstance`.

**Expected result**

- Direct assertions: `assert refreshed.cache_hit is False`; `assert (refreshed.extraction_path / 'EP' / 'value.txt').read_bytes() == original`; `assert not (refreshed.extraction_path / 'unexpected.txt').exists()`; `assert data_path.stat().st_size == len(original)`; `assert isinstance(file_entries, list)`; `assert isinstance(file_entries[0], dict)`; `assert isinstance(file_entries, list)`; `assert isinstance(file_entries[0], dict)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `invalid extraction cache is rebuilt` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `(first.extraction_path / 'unexpected.txt').write_bytes`, `(refreshed.extraction_path / 'EP' / 'value.txt').read_bytes`, `(refreshed.extraction_path / 'unexpected.txt').exists`, `_download`, `_extraction_metadata_path`, `_read_json`, `_write_json`, `_zip_bytes`, `data_path.stat`, `data_path.unlink`, `data_path.write_bytes`, `extract_inpn_protected_areas_archive`, `isinstance`, `len`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_first_extraction_publication_failure_leaves_no_half_root`

**Signature**

```python
def test_first_extraction_publication_failure_leaves_no_half_root(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `first extraction publication failure leaves no half root` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`.
- Contains 4 explicit setup/context statement(s).
- Computes `(config, download, _)` from `_download(tmp_path)`.
- Computes `root` from `download.path.parent / 'x' / download.sha256`.
- Computes `original_replace` from `inpn._replace_directory`.
- Enters managed context(s) `pytest.raises(InpnProtectedAreasSourceError, match='publication')` and executes: Calls `extract_inpn_protected_areas_archive(download, config)` for its validation or side effect.

**Action**

- Calls `OSError`, `_download`, `extract_inpn_protected_areas_archive`, `monkeypatch.setattr`, `original_replace`, `root.exists`, `root.with_name`, `root.with_name(f'{root.name}.bak').exists`, `root.with_name(f'{root.name}.part').exists`, `source.name.endswith`.

**Expected result**

- Direct assertions: `assert not root.exists()`; `assert not root.with_name(f'{root.name}.part').exists()`; `assert not root.with_name(f'{root.name}.bak').exists()`.
- Expected exception contexts: `with pytest.raises(InpnProtectedAreasSourceError, match='publication'): extract_inpn_protected_areas_archive(download, config)`.

**Regression protected**

- Protects the exact `first extraction publication failure leaves no half root` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `OSError`, `_download`, `extract_inpn_protected_areas_archive`, `monkeypatch.setattr`, `original_replace`, `pytest.raises`, `root.exists`, `root.with_name`, `root.with_name(f'{root.name}.bak').exists`, `root.with_name(f'{root.name}.part').exists`, `source.name.endswith`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_extraction_replacement_failure_restores_old_tree`

**Signature**

```python
def test_extraction_replacement_failure_restores_old_tree(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `extraction replacement failure restores old tree` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`.
- Contains 6 explicit setup/context statement(s).
- Computes `(config, download, _)` from `_download(tmp_path)`.
- Computes `first` from `extract_inpn_protected_areas_archive(download, config)`.
- Computes `before` from `_tree_snapshot(first.extraction_path)`.
- Computes `original_replace` from `inpn._replace_directory`.
- Computes `failed` from `False`.
- Enters managed context(s) `pytest.raises(InpnProtectedAreasSourceError, match='publication')` and executes: Calls `extract_inpn_protected_areas_archive(download, config)` for its validation or side effect.

**Action**

- Calls `(first.extraction_path / 'EP' / 'readme.txt').write_bytes`, `OSError`, `_download`, `_tree_snapshot`, `extract_inpn_protected_areas_archive`, `first.extraction_path.with_name`, `first.extraction_path.with_name(f'{first.extraction_path.name}.bak').exists`, `monkeypatch.setattr`, `original_replace`, `source.name.endswith`.

**Expected result**

- Direct assertions: `assert _tree_snapshot(first.extraction_path) == before`; `assert not first.extraction_path.with_name(f'{first.extraction_path.name}.bak').exists()`.
- Expected exception contexts: `with pytest.raises(InpnProtectedAreasSourceError, match='publication'): extract_inpn_protected_areas_archive(download, config)`.

**Regression protected**

- Protects the exact `extraction replacement failure restores old tree` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `(first.extraction_path / 'EP' / 'readme.txt').write_bytes`, `OSError`, `_download`, `_tree_snapshot`, `extract_inpn_protected_areas_archive`, `first.extraction_path.with_name`, `first.extraction_path.with_name(f'{first.extraction_path.name}.bak').exists`, `monkeypatch.setattr`, `original_replace`, `pytest.raises`, `source.name.endswith`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_extraction_rollback_failure_preserves_backup`

**Signature**

```python
def test_extraction_rollback_failure_preserves_backup(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `extraction rollback failure preserves backup` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`.
- Contains 6 explicit setup/context statement(s).
- Computes `(config, download, _)` from `_download(tmp_path)`.
- Computes `first` from `extract_inpn_protected_areas_archive(download, config)`.
- Computes `before` from `_tree_snapshot(first.extraction_path)`.
- Computes `backup` from `first.extraction_path.with_name(f'{first.extraction_path.name}.bak')`.
- Computes `original_replace` from `inpn._replace_directory`.
- Enters managed context(s) `pytest.raises(InpnProtectedAreasSourceError, match='rollback')` and executes: Calls `extract_inpn_protected_areas_archive(download, config)` for its validation or side effect.

**Action**

- Calls `(first.extraction_path / 'EP' / 'readme.txt').write_bytes`, `OSError`, `_download`, `_tree_snapshot`, `extract_inpn_protected_areas_archive`, `first.extraction_path.with_name`, `first.extraction_path.with_name(f'{first.extraction_path.name}.part').exists`, `monkeypatch.setattr`, `original_replace`, `source.name.endswith`.

**Expected result**

- Direct assertions: `assert _tree_snapshot(backup) == before`; `assert not first.extraction_path.with_name(f'{first.extraction_path.name}.part').exists()`.
- Expected exception contexts: `with pytest.raises(InpnProtectedAreasSourceError, match='rollback'): extract_inpn_protected_areas_archive(download, config)`.

**Regression protected**

- Protects the exact `extraction rollback failure preserves backup` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `(first.extraction_path / 'EP' / 'readme.txt').write_bytes`, `OSError`, `_download`, `_tree_snapshot`, `extract_inpn_protected_areas_archive`, `first.extraction_path.with_name`, `first.extraction_path.with_name(f'{first.extraction_path.name}.part').exists`, `monkeypatch.setattr`, `original_replace`, `pytest.raises`, `source.name.endswith`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_extraction_backup_move_failure_leaves_old_tree_untouched`

**Signature**

```python
def test_extraction_backup_move_failure_leaves_old_tree_untouched(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `extraction backup move failure leaves old tree untouched` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`.
- Contains 6 explicit setup/context statement(s).
- Computes `(config, download, _)` from `_download(tmp_path)`.
- Computes `first` from `extract_inpn_protected_areas_archive(download, config)`.
- Computes `before` from `_tree_snapshot(first.extraction_path)`.
- Computes `backup` from `first.extraction_path.with_name(f'{first.extraction_path.name}.bak')`.
- Computes `original_replace` from `inpn._replace_directory`.
- Enters managed context(s) `pytest.raises(InpnProtectedAreasSourceError, match='publication|stage')` and executes: Calls `extract_inpn_protected_areas_archive(download, config)` for its validation or side effect.

**Action**

- Calls `(first.extraction_path / 'EP' / 'readme.txt').write_bytes`, `OSError`, `_download`, `_tree_snapshot`, `backup.exists`, `extract_inpn_protected_areas_archive`, `first.extraction_path.is_dir`, `first.extraction_path.with_name`, `monkeypatch.setattr`, `original_replace`.

**Expected result**

- Direct assertions: `assert first.extraction_path.is_dir()`; `assert _tree_snapshot(first.extraction_path) == before`; `assert not backup.exists()`.
- Expected exception contexts: `with pytest.raises(InpnProtectedAreasSourceError, match='publication|stage'): extract_inpn_protected_areas_archive(download, config)`.

**Regression protected**

- Protects the exact `extraction backup move failure leaves old tree untouched` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `(first.extraction_path / 'EP' / 'readme.txt').write_bytes`, `OSError`, `_download`, `_tree_snapshot`, `backup.exists`, `extract_inpn_protected_areas_archive`, `first.extraction_path.is_dir`, `first.extraction_path.with_name`, `monkeypatch.setattr`, `original_replace`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_extraction_rejects_wrong_download_type`

**Signature**

```python
def test_extraction_rejects_wrong_download_type(
    tmp_path: Path,
    bad_input: object,
) -> None:
```

**Purpose**

Protects the `extraction rejects wrong download type` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `bad_input`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(InpnProtectedAreasSourceError, match='download|type')` and executes: Calls `extract_inpn_protected_areas_archive(bad_input, _config(tmp_path))` for its validation or side effect.

**Action**

- Calls `_config`, `extract_inpn_protected_areas_archive`, `object`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(InpnProtectedAreasSourceError, match='download|type'): extract_inpn_protected_areas_archive(bad_input, _config(tmp_path))`.

**Regression protected**

- Protects the exact `extraction rejects wrong download type` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_config`, `extract_inpn_protected_areas_archive`, `object`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_extraction_rejects_wrong_config_type`

**Signature**

```python
def test_extraction_rejects_wrong_config_type(tmp_path: Path) -> None:
```

**Purpose**

Protects the `extraction rejects wrong config type` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 2 explicit setup/context statement(s).
- Computes `(_, download, _)` from `_download(tmp_path)`.
- Enters managed context(s) `pytest.raises(InpnProtectedAreasSourceError, match='config|type')` and executes: Calls `extract_inpn_protected_areas_archive(download, object())` for its validation or side effect.

**Action**

- Calls `_download`, `extract_inpn_protected_areas_archive`, `object`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(InpnProtectedAreasSourceError, match='config|type'): extract_inpn_protected_areas_archive(download, object())`.

**Regression protected**

- Protects the exact `extraction rejects wrong config type` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_download`, `extract_inpn_protected_areas_archive`, `object`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_extraction_cache_setup_failure_is_controlled`

**Signature**

```python
def test_extraction_cache_setup_failure_is_controlled(tmp_path: Path) -> None:
```

**Purpose**

Protects the `extraction cache setup failure is controlled` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 3 explicit setup/context statement(s).
- Computes `(config, download, _)` from `_download(tmp_path)`.
- Computes `extraction_parent` from `download.path.parent / 'x'`.
- Enters managed context(s) `pytest.raises(InpnProtectedAreasSourceError, match='extract|cache')` and executes: Calls `extract_inpn_protected_areas_archive(download, config)` for its validation or side effect.

**Action**

- Calls `_download`, `extract_inpn_protected_areas_archive`, `extraction_parent.write_bytes`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(InpnProtectedAreasSourceError, match='extract|cache'): extract_inpn_protected_areas_archive(download, config)`.

**Regression protected**

- Protects the exact `extraction cache setup failure is controlled` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_download`, `extract_inpn_protected_areas_archive`, `extraction_parent.write_bytes`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_extraction_rejects_stale_download_bytes`

**Signature**

```python
def test_extraction_rejects_stale_download_bytes(tmp_path: Path) -> None:
```

**Purpose**

Protects the `extraction rejects stale download bytes` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 3 explicit setup/context statement(s).
- Computes `(config, download, _)` from `_download(tmp_path)`.
- Computes `replacement` from `_zip_bytes({'EP/readme.txt': b'forged contents'})`.
- Enters managed context(s) `pytest.raises(InpnProtectedAreasSourceError, match='SHA|size|archive|download')` and executes: Calls `extract_inpn_protected_areas_archive(download, config)` for its validation or side effect.

**Action**

- Calls `_download`, `_zip_bytes`, `download.path.write_bytes`, `extract_inpn_protected_areas_archive`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(InpnProtectedAreasSourceError, match='SHA|size|archive|download'): extract_inpn_protected_areas_archive(download, config)`.

**Regression protected**

- Protects the exact `extraction rejects stale download bytes` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_download`, `_zip_bytes`, `download.path.write_bytes`, `extract_inpn_protected_areas_archive`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_result_dataclasses_are_frozen`

**Signature**

```python
def test_result_dataclasses_are_frozen(tmp_path: Path) -> None:
```

**Purpose**

Protects the `result dataclasses are frozen` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 5 explicit setup/context statement(s).
- Computes `(config, download, _)` from `_download(tmp_path)`.
- Computes `extraction` from `extract_inpn_protected_areas_archive(download, config)`.
- Enters managed context(s) `pytest.raises(FrozenInstanceError)` and executes: Computes `download.cache_hit` from `True`.
- Enters managed context(s) `pytest.raises(FrozenInstanceError)` and executes: Computes `extraction.cache_hit` from `True`.
- Enters managed context(s) `pytest.raises(FrozenInstanceError)` and executes: Computes `extraction.files[0].sha256` from `'0' * 64`.

**Action**

- Calls `_download`, `extract_inpn_protected_areas_archive`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(FrozenInstanceError): download.cache_hit = True`; `with pytest.raises(FrozenInstanceError): extraction.cache_hit = True`; `with pytest.raises(FrozenInstanceError): extraction.files[0].sha256 = '0' * 64`.

**Regression protected**

- Protects the exact `result dataclasses are frozen` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_download`, `extract_inpn_protected_areas_archive`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_public_api_exports_only_stable_high_level_symbols`

**Signature**

```python
def test_public_api_exports_only_stable_high_level_symbols() -> None:
```

**Purpose**

Protects the `public api exports only stable high level symbols` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 0 explicit setup/context statement(s).

**Action**

- Calls `all`, `getattr`, `hasattr`.

**Expected result**

- Direct assertions: `assert set(inpn.__all__) == EXPECTED_EXPORTS`; `assert EXPECTED_EXPORTS <= set(sources.__all__)`; `assert all((getattr(sources, name) is getattr(inpn, name) for name in EXPECTED_EXPORTS))`; `assert not hasattr(sources, '_validated_zip_members')`; `assert not hasattr(sources, '_inventory')`; `assert not hasattr(sources, 'validate_inpn_protected_area_geometry')`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `public api exports only stable high level symbols` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `all`, `getattr`, `hasattr`, `set`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_result_schemas_are_factual_inventory_only`

**Signature**

```python
def test_result_schemas_are_factual_inventory_only() -> None:
```

**Purpose**

Protects the `result schemas are factual inventory only` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Computes `forbidden` from `{'geometry', 'normalize', 'parcel', 'overlay', 'severity', 'score', 'reject', 'exclude', 'bess'}`.

**Action**

- Calls `any`, `fields`, `name.casefold`.

**Expected result**

- Direct assertions: `assert [field.name for field in fields(InpnProtectedAreasDownload)] == ['provider', 'authority', 'program', 'dataset_id', 'dataset_name', 'declared_version', 'reference_page_url', 'archive_url', 'download_timestamp', 'filename', 'file_size', 'sha256', 'path', 'cache_hit']`; `assert [field.name for field in fields(InpnProtectedAreasExtractedFile)] == ['relative_path', 'file_size', 'sha256']`; `assert [field.name for field in fields(InpnProtectedAreasExtraction)] == ['download', 'extraction_path', 'files', 'cache_hit']`; `assert not any((fragment in name.casefold() for name in inpn.__all__ for fragment in forbidden))`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `result schemas are factual inventory only` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `any`, `fields`, `name.casefold`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_strict_metadata_rejects_boolean_numeric_values_as_cache_hits`

**Signature**

```python
def test_strict_metadata_rejects_boolean_numeric_values_as_cache_hits(
    tmp_path: Path,
) -> None:
```

**Purpose**

Protects the `strict metadata rejects boolean numeric values as cache hits` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 6 explicit setup/context statement(s).
- Computes `(config, first, _)` from `_download(tmp_path)`.
- Computes `metadata_path` from `_download_metadata_path(first)`.
- Computes `metadata` from `_read_json(metadata_path)`.
- Computes `metadata['file_size']` from `True`.
- Computes `session` from `_session(config)`.
- Computes `refreshed` from `_download_with_session(config, session)`.

**Action**

- Calls `_download`, `_download_metadata_path`, `_download_with_session`, `_read_json`, `_session`, `_write_json`.

**Expected result**

- Direct assertions: `assert refreshed.cache_hit is False`; `assert len(session.calls) == 1`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `strict metadata rejects boolean numeric values as cache hits` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_download`, `_download_metadata_path`, `_download_with_session`, `_read_json`, `_session`, `_write_json`, `len`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_cache_path_binds_version_and_filename`

**Signature**

```python
def test_cache_path_binds_version_and_filename(tmp_path: Path) -> None:
```

**Purpose**

Protects the `cache path binds version and filename` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 2 explicit setup/context statement(s).
- Computes `(_, download, _)` from `_download(tmp_path)`.
- Computes `metadata` from `_read_json(_download_metadata_path(download))`.

**Action**

- Calls `_download`, `_download_metadata_path`, `_read_json`.

**Expected result**

- Direct assertions: `assert download.path.name == 'EP.zip'`; `assert '07-2026' in download.path.parts`; `assert metadata['dataset_id'] == 'EP'`; `assert metadata['declared_version'] == '07/2026'`; `assert metadata['filename'] == 'EP.zip'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `cache path binds version and filename` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_download`, `_download_metadata_path`, `_read_json`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_download_uses_no_hidden_reference_page_scrape`

**Signature**

```python
def test_download_uses_no_hidden_reference_page_scrape(tmp_path: Path) -> None:
```

**Purpose**

Protects the `download uses no hidden reference page scrape` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 2 explicit setup/context statement(s).
- Computes `config` from `_config(tmp_path)`.
- Computes `session` from `_session(config)`.

**Action**

- Calls `_config`, `_download_with_session`, `_session`.

**Expected result**

- Direct assertions: `assert [url for url, _ in session.calls] == [str(config.archive_url)]`; `assert str(config.reference_page_url) not in [url for url, _ in session.calls]`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `download uses no hidden reference page scrape` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_config`, `_download_with_session`, `_session`, `str`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_exact_file_inventory_does_not_omit_unknown_suffixes`

**Signature**

```python
def test_exact_file_inventory_does_not_omit_unknown_suffixes(tmp_path: Path) -> None:
```

**Purpose**

Protects the `exact file inventory does not omit unknown suffixes` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 3 explicit setup/context statement(s).
- Computes `members` from `{'EP/a.dbf': b'dbf', 'EP/a.shx': b'shx', 'EP/a.prj': b'prj', 'EP/a.cpg': b'cpg', 'EP/a.xml': b'xml', 'EP/a.csv': b'csv', 'EP/a.sqlite': b'sqlite', 'EP/a.gpkg': b'gpkg', 'EP/a.unknown': b'unknown'}`.
- Computes `(config, download, _)` from `_download(tmp_path, payload=_zip_bytes(members))`.
- Computes `extraction` from `extract_inpn_protected_areas_archive(download, config)`.

**Action**

- Calls `_download`, `_zip_bytes`, `extract_inpn_protected_areas_archive`.

**Expected result**

- Direct assertions: `assert {item.relative_path for item in extraction.files} == set(members)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `exact file inventory does not omit unknown suffixes` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_download`, `_zip_bytes`, `extract_inpn_protected_areas_archive`, `set`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_archive_and_extraction_cache_reuse_are_independent`

**Signature**

```python
def test_archive_and_extraction_cache_reuse_are_independent(tmp_path: Path) -> None:
```

**Purpose**

Protects the `archive and extraction cache reuse are independent` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 4 explicit setup/context statement(s).
- Computes `(config, first_download, _)` from `_download(tmp_path)`.
- Computes `first_extraction` from `extract_inpn_protected_areas_archive(first_download, config)`.
- Computes `second_download` from `_download_with_session(config, _Session(error=AssertionError('network used')))`.
- Computes `second_extraction` from `extract_inpn_protected_areas_archive(second_download, config)`.

**Action**

- Calls `AssertionError`, `_Session`, `_download`, `_download_with_session`, `extract_inpn_protected_areas_archive`.

**Expected result**

- Direct assertions: `assert first_download.cache_hit is False`; `assert first_extraction.cache_hit is False`; `assert second_download.cache_hit is True`; `assert second_extraction.cache_hit is True`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `archive and extraction cache reuse are independent` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `AssertionError`, `_Session`, `_download`, `_download_with_session`, `extract_inpn_protected_areas_archive`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_no_stale_parts_after_download_or_extraction_success`

**Signature**

```python
def test_no_stale_parts_after_download_or_extraction_success(tmp_path: Path) -> None:
```

**Purpose**

Protects the `no stale parts after download or extraction success` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 2 explicit setup/context statement(s).
- Computes `(config, download, _)` from `_download(tmp_path)`.
- Computes `extraction` from `extract_inpn_protected_areas_archive(download, config)`.

**Action**

- Calls `Path`, `Path(config.cache_root).rglob`, `_download`, `extract_inpn_protected_areas_archive`, `extraction.extraction_path.is_dir`.

**Expected result**

- Direct assertions: `assert extraction.extraction_path.is_dir()`; `assert not list(Path(config.cache_root).rglob('*.part'))`; `assert not list(Path(config.cache_root).rglob('*.bak'))`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `no stale parts after download or extraction success` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Path`, `Path(config.cache_root).rglob`, `_download`, `extract_inpn_protected_areas_archive`, `extraction.extraction_path.is_dir`, `list`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `archive_filename` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `archive_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `archive_size` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `archive_url` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `cache_root` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `dataset_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `declared_version` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `download_timestamp` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `expected_archive_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `expected_archive_size_bytes` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `file_size` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `filename` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `files` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `reference_page_url` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `schema_version` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `sha256` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `timeout` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `unexpected` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `z-last/empty.cpg` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |

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

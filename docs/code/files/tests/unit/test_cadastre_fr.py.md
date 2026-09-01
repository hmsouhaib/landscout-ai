# `tests/unit/test_cadastre_fr.py`

## File identity

- Repository path: `tests/unit/test_cadastre_fr.py`
- File type: Python source
- Layer: unit/regression test
- Domain: isolated contract test evidence
- Responsibility: Provides complete unit and regression coverage for the `cadastre_fr` contracts exercised in this file.
- Source SHA256: `6d0cc8419a7dc41440e8a296eb64e7c451e553f344d67e72156425faaa3e5e01`

## 1. STEP 7F.1A.4 contract delta

- Refreshes permanent STEP 7F.1A.4 regression coverage for cadastre fr; the exact fixtures, mutations, calls, controlled failures, and assertions are inventoried below.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Provides complete unit and regression coverage for the `cadastre_fr` contracts exercised in this file.

The file belongs to the **unit/regression test** layer and **isolated contract test evidence** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `import gzip`
- `import io`
- `import json`
- `from datetime import UTC, datetime, timedelta`
- `from hashlib import sha256`
- `from pathlib import Path`
- `from unittest.mock import patch`
- `from urllib.error import HTTPError`

### Third-party packages

- `import pytest`

### Internal LandScout imports

- `from landscout.sources import cadastre_fr`
- `from landscout.sources.cadastre_fr import (
    CadastreDownloadError,
    _is_valid_gzip,
    build_cadastre_parcelles_url,
    download_cadastre_parcelles,
)`

## 4. Contract taxonomy

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `COMMUNE_CODE`

- Category: module constant or closed domain.
- Exact declaration:

```python
COMMUNE_CODE = "31395"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `EXPECTED_URL`

- Category: module constant or closed domain.
- Exact declaration:

```python
EXPECTED_URL = (
    "https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes/"
    "31/31395/cadastre-31395-parcelles.json.gz"
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `ARCHIVE_CONTENT`

- Category: module constant or closed domain.
- Exact declaration:

```python
ARCHIVE_CONTENT = gzip.compress(b'{"type":"FeatureCollection","features":[]}')
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `REFRESHED_ARCHIVE_CONTENT`

- Category: module constant or closed domain.
- Exact declaration:

```python
REFRESHED_ARCHIVE_CONTENT = gzip.compress(
    b'{"type":"FeatureCollection","features":[{"type":"Feature"}]}'
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `CORRUPTED_ARCHIVE_CONTENT`

- Category: module constant or closed domain.
- Exact declaration:

```python
CORRUPTED_ARCHIVE_CONTENT = ARCHIVE_CONTENT[:-8]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

No top-level class/model/dataclass is declared.

## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `_set_cache_age`

**Purpose:** Implements `set cache age` within the file role: Provides complete unit and regression coverage for the `cadastre_fr` contracts exercised in this file.

**Exact signature**

```python
def _set_cache_age(metadata_path: Path, age: timedelta) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `metadata_path` | positional-or-keyword | `Path` | `required` |
| `age` | positional-or-keyword | `timedelta` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_cadastre_fr::test_expired_cache_is_downloaded_again` via `_set_cache_age`
- value/type reference: `tests.unit.test_cadastre_fr::test_expired_cache_is_downloaded_again` via `_set_cache_age`
- direct call: `tests.unit.test_cadastre_fr::test_failed_refresh_preserves_cached_archive` via `_set_cache_age`
- value/type reference: `tests.unit.test_cadastre_fr::test_failed_refresh_preserves_cached_archive` via `_set_cache_age`
- direct call: `tests.unit.test_cadastre_fr::test_corrupted_new_download_preserves_existing_archive` via `_set_cache_age`
- value/type reference: `tests.unit.test_cadastre_fr::test_corrupted_new_download_preserves_existing_archive` via `_set_cache_age`
- direct call: `tests.unit.test_cadastre_fr::test_metadata_publication_failure_restores_previous_cache_pair` via `_set_cache_age`
- value/type reference: `tests.unit.test_cadastre_fr::test_metadata_publication_failure_restores_previous_cache_pair` via `_set_cache_age`
- direct call: `tests.unit.test_cadastre_fr::test_publication_and_rollback_failure_preserves_recovery_backup` via `_set_cache_age`
- value/type reference: `tests.unit.test_cadastre_fr::test_publication_and_rollback_failure_preserves_recovery_backup` via `_set_cache_age`
- direct call: `tests.unit.test_cadastre_fr::test_next_run_after_double_failure_preserves_recovery_before_network` via `_set_cache_age`
- value/type reference: `tests.unit.test_cadastre_fr::test_next_run_after_double_failure_preserves_recovery_before_network` via `_set_cache_age`
- direct call: `tests.unit.test_cadastre_fr::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `_set_cache_age`
- value/type reference: `tests.unit.test_cadastre_fr::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `_set_cache_age`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `json.loads` | `json.loads` |
| `metadata_path.read_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `(datetime.now(UTC) - age).isoformat` | `unresolved local/third-party receiver; no ownership inferred` |
| `datetime.now` | `datetime.datetime.now` |
| `metadata_path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `metadata_path.read_text` |
| Filesystem/archive write or publication | `metadata_path.write_text` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `metadata["download_timestamp"] = (datetime.now(UTC) - age).isoformat()` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _set_cache_age(metadata_path: Path, age: timedelta) -> None:
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    metadata["download_timestamp"] = (datetime.now(UTC) - age).isoformat()
    metadata_path.write_text(json.dumps(metadata), encoding="utf-8")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_update_metadata_integrity`

**Purpose:** Implements `update metadata integrity` within the file role: Provides complete unit and regression coverage for the `cadastre_fr` contracts exercised in this file.

**Exact signature**

```python
def _update_metadata_integrity(metadata_path: Path, archive_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `metadata_path` | positional-or-keyword | `Path` | `required` |
| `archive_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_cadastre_fr::test_corrupted_cached_archive_triggers_fresh_download` via `_update_metadata_integrity`
- value/type reference: `tests.unit.test_cadastre_fr::test_corrupted_cached_archive_triggers_fresh_download` via `_update_metadata_integrity`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `json.loads` | `json.loads` |
| `metadata_path.read_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `archive_path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256(content).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |
| `metadata_path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `metadata_path.read_text`<br>`archive_path.read_bytes` |
| Filesystem/archive write or publication | `metadata_path.write_text` |
| Hashing/byte identity | `sha256(content).hexdigest`<br>`sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `metadata["file_size"] = len(content)`<br>`metadata["sha256"] = sha256(content).hexdigest()` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _update_metadata_integrity(metadata_path: Path, archive_path: Path) -> None:
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    content = archive_path.read_bytes()
    metadata["file_size"] = len(content)
    metadata["sha256"] = sha256(content).hexdigest()
    metadata_path.write_text(json.dumps(metadata), encoding="utf-8")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_build_cadastre_parcelles_url`

**Purpose:** Regression invariant: build cadastre parcelles url. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_build_cadastre_parcelles_url() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert build_cadastre_parcelles_url(COMMUNE_CODE) == EXPECTED_URL`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `build_cadastre_parcelles_url` | `landscout.sources.cadastre_fr.build_cadastre_parcelles_url` |

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
def test_build_cadastre_parcelles_url() -> None:
    assert build_cadastre_parcelles_url(COMMUNE_CODE) == EXPECTED_URL
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_successful_download`

**Purpose:** Regression invariant: successful download. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_successful_download(tmp_path: Path) -> None:
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
  - `assert result.path.read_bytes() == ARCHIVE_CONTENT`
  - `assert result.commune_code == COMMUNE_CODE`
  - `assert result.source_url == EXPECTED_URL`
  - `assert result.file_size == len(ARCHIVE_CONTENT)`
  - `assert result.cache_hit is False`
  - `assert metadata["schema_version"] == 1`
  - `assert metadata["commune_code"] == COMMUNE_CODE`
  - `assert metadata["download_timestamp"] == result.download_timestamp`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `patch` | `unittest.mock.patch` |
| `io.BytesIO` | `io.BytesIO` |
| `download_cadastre_parcelles` | `landscout.sources.cadastre_fr.download_cadastre_parcelles` |
| `result.path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.loads` | `json.loads` |
| `metadata_path.read_text` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `result.path.read_bytes`<br>`metadata_path.read_text` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_successful_download(tmp_path: Path) -> None:
    with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        return_value=io.BytesIO(ARCHIVE_CONTENT),
    ):
        result = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert result.path.read_bytes() == ARCHIVE_CONTENT
    assert result.commune_code == COMMUNE_CODE
    assert result.source_url == EXPECTED_URL
    assert result.file_size == len(ARCHIVE_CONTENT)
    assert result.cache_hit is False
    metadata_path = tmp_path / f"{result.filename}.metadata.json"
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    assert metadata["schema_version"] == 1
    assert metadata["commune_code"] == COMMUNE_CODE
    assert metadata["download_timestamp"] == result.download_timestamp
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_fresh_cache_is_reused`

**Purpose:** Regression invariant: fresh cache is reused. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_fresh_cache_is_reused(tmp_path: Path) -> None:
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
  - `assert opener.call_count == 1`
  - `assert first.cache_hit is False`
  - `assert second.cache_hit is True`
  - `assert second.sha256 == first.sha256`
  - `assert second.download_timestamp == first.download_timestamp`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `patch` | `unittest.mock.patch` |
| `io.BytesIO` | `io.BytesIO` |
| `download_cadastre_parcelles` | `landscout.sources.cadastre_fr.download_cadastre_parcelles` |

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
def test_fresh_cache_is_reused(tmp_path: Path) -> None:
    with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        return_value=io.BytesIO(ARCHIVE_CONTENT),
    ) as opener:
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
        second = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert opener.call_count == 1
    assert first.cache_hit is False
    assert second.cache_hit is True
    assert second.sha256 == first.sha256
    assert second.download_timestamp == first.download_timestamp
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_expired_cache_is_downloaded_again`

**Purpose:** Regression invariant: expired cache is downloaded again. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_expired_cache_is_downloaded_again(tmp_path: Path) -> None:
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
  - `assert opener.call_count == 2`
  - `assert refreshed.cache_hit is False`
  - `assert refreshed.path.read_bytes() == REFRESHED_ARCHIVE_CONTENT`
  - `assert refreshed.sha256 == sha256(REFRESHED_ARCHIVE_CONTENT).hexdigest()`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `patch` | `unittest.mock.patch` |
| `io.BytesIO` | `io.BytesIO` |
| `download_cadastre_parcelles` | `landscout.sources.cadastre_fr.download_cadastre_parcelles` |
| `_set_cache_age` | `tests.unit.test_cadastre_fr._set_cache_age` |
| `timedelta` | `datetime.timedelta` |
| `refreshed.path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256(REFRESHED_ARCHIVE_CONTENT).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `refreshed.path.read_bytes` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `sha256(REFRESHED_ARCHIVE_CONTENT).hexdigest`<br>`sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_expired_cache_is_downloaded_again(tmp_path: Path) -> None:
    with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        side_effect=[
            io.BytesIO(ARCHIVE_CONTENT),
            io.BytesIO(REFRESHED_ARCHIVE_CONTENT),
        ],
    ) as opener:
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
        metadata_path = tmp_path / f"{first.filename}.metadata.json"
        _set_cache_age(metadata_path, timedelta(hours=169))
        refreshed = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert opener.call_count == 2
    assert refreshed.cache_hit is False
    assert refreshed.path.read_bytes() == REFRESHED_ARCHIVE_CONTENT
    assert refreshed.sha256 == sha256(REFRESHED_ARCHIVE_CONTENT).hexdigest()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_failed_refresh_preserves_cached_archive`

**Purpose:** Regression invariant: failed refresh preserves cached archive. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_failed_refresh_preserves_cached_archive(tmp_path: Path) -> None:
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
  - `pytest.raises(CadastreDownloadError)`
- Exact assertions:
  - `assert first.path.read_bytes() == original_archive`
  - `assert metadata_path.is_file()`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `patch` | `unittest.mock.patch` |
| `io.BytesIO` | `io.BytesIO` |
| `download_cadastre_parcelles` | `landscout.sources.cadastre_fr.download_cadastre_parcelles` |
| `first.path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `_set_cache_age` | `tests.unit.test_cadastre_fr._set_cache_age` |
| `timedelta` | `datetime.timedelta` |
| `HTTPError` | `urllib.error.HTTPError` |
| `pytest.raises` | `pytest.raises` |
| `metadata_path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `first.path.read_bytes`<br>`metadata_path.is_file` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_failed_refresh_preserves_cached_archive(tmp_path: Path) -> None:
    with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        return_value=io.BytesIO(ARCHIVE_CONTENT),
    ):
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    original_archive = first.path.read_bytes()
    metadata_path = tmp_path / f"{first.filename}.metadata.json"
    _set_cache_age(metadata_path, timedelta(hours=169))
    error = HTTPError(EXPECTED_URL, 503, "Unavailable", hdrs=None, fp=None)

    with (
        patch("landscout.sources.cadastre_fr.open_safe_https", side_effect=error),
        pytest.raises(CadastreDownloadError),
    ):
        download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert first.path.read_bytes() == original_archive
    assert metadata_path.is_file()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_failed_http_response`

**Purpose:** Regression invariant: failed http response. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_failed_http_response(tmp_path: Path) -> None:
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
  - `pytest.raises(CadastreDownloadError)`
- Exact assertions:
  - `assert not list(tmp_path.glob("*"))`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `HTTPError` | `urllib.error.HTTPError` |
| `patch` | `unittest.mock.patch` |
| `pytest.raises` | `pytest.raises` |
| `download_cadastre_parcelles` | `landscout.sources.cadastre_fr.download_cadastre_parcelles` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `tmp_path.glob` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `tmp_path.glob` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_failed_http_response(tmp_path: Path) -> None:
    error = HTTPError(EXPECTED_URL, 404, "Not Found", hdrs=None, fp=None)

    with (
        patch("landscout.sources.cadastre_fr.open_safe_https", side_effect=error),
        pytest.raises(CadastreDownloadError),
    ):
        download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert not list(tmp_path.glob("*"))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_checksum_generation`

**Purpose:** Regression invariant: checksum generation. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_checksum_generation(tmp_path: Path) -> None:
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
  - `assert result.sha256 == sha256(ARCHIVE_CONTENT).hexdigest()`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `patch` | `unittest.mock.patch` |
| `io.BytesIO` | `io.BytesIO` |
| `download_cadastre_parcelles` | `landscout.sources.cadastre_fr.download_cadastre_parcelles` |
| `sha256(ARCHIVE_CONTENT).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `sha256(ARCHIVE_CONTENT).hexdigest`<br>`sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_checksum_generation(tmp_path: Path) -> None:
    with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        return_value=io.BytesIO(ARCHIVE_CONTENT),
    ):
        result = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert result.sha256 == sha256(ARCHIVE_CONTENT).hexdigest()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_valid_gzip_is_accepted`

**Purpose:** Regression invariant: valid gzip is accepted. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_valid_gzip_is_accepted(tmp_path: Path) -> None:
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
  - `assert _is_valid_gzip(archive_path)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `archive_path.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `_is_valid_gzip` | `landscout.sources.cadastre_fr._is_valid_gzip` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `archive_path.write_bytes` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_valid_gzip_is_accepted(tmp_path: Path) -> None:
    archive_path = tmp_path / "valid.json.gz"
    archive_path.write_bytes(ARCHIVE_CONTENT)

    assert _is_valid_gzip(archive_path)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_truncated_gzip_is_rejected`

**Purpose:** Regression invariant: truncated gzip is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_truncated_gzip_is_rejected(tmp_path: Path) -> None:
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
  - `assert not _is_valid_gzip(archive_path)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `archive_path.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `_is_valid_gzip` | `landscout.sources.cadastre_fr._is_valid_gzip` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `archive_path.write_bytes` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_truncated_gzip_is_rejected(tmp_path: Path) -> None:
    archive_path = tmp_path / "truncated.json.gz"
    archive_path.write_bytes(CORRUPTED_ARCHIVE_CONTENT)

    assert not _is_valid_gzip(archive_path)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_corrupted_cached_archive_triggers_fresh_download`

**Purpose:** Regression invariant: corrupted cached archive triggers fresh download. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_corrupted_cached_archive_triggers_fresh_download(tmp_path: Path) -> None:
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
  - `assert opener.call_count == 2`
  - `assert refreshed.cache_hit is False`
  - `assert refreshed.path.read_bytes() == REFRESHED_ARCHIVE_CONTENT`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `patch` | `unittest.mock.patch` |
| `io.BytesIO` | `io.BytesIO` |
| `download_cadastre_parcelles` | `landscout.sources.cadastre_fr.download_cadastre_parcelles` |
| `first.path.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `_update_metadata_integrity` | `tests.unit.test_cadastre_fr._update_metadata_integrity` |
| `refreshed.path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `refreshed.path.read_bytes` |
| Filesystem/archive write or publication | `first.path.write_bytes` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_corrupted_cached_archive_triggers_fresh_download(tmp_path: Path) -> None:
    with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        side_effect=[
            io.BytesIO(ARCHIVE_CONTENT),
            io.BytesIO(REFRESHED_ARCHIVE_CONTENT),
        ],
    ) as opener:
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
        metadata_path = tmp_path / f"{first.filename}.metadata.json"
        first.path.write_bytes(CORRUPTED_ARCHIVE_CONTENT)
        _update_metadata_integrity(metadata_path, first.path)
        refreshed = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert opener.call_count == 2
    assert refreshed.cache_hit is False
    assert refreshed.path.read_bytes() == REFRESHED_ARCHIVE_CONTENT
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_corrupted_new_download_preserves_existing_archive`

**Purpose:** Regression invariant: corrupted new download preserves existing archive. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_corrupted_new_download_preserves_existing_archive(tmp_path: Path) -> None:
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
  - `pytest.raises(CadastreDownloadError)`
- Exact assertions:
  - `assert first.path.read_bytes() == original_archive`
  - `assert not list(tmp_path.glob("*.part"))`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `patch` | `unittest.mock.patch` |
| `io.BytesIO` | `io.BytesIO` |
| `download_cadastre_parcelles` | `landscout.sources.cadastre_fr.download_cadastre_parcelles` |
| `first.path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `_set_cache_age` | `tests.unit.test_cadastre_fr._set_cache_age` |
| `timedelta` | `datetime.timedelta` |
| `pytest.raises` | `pytest.raises` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `tmp_path.glob` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `first.path.read_bytes`<br>`tmp_path.glob` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_corrupted_new_download_preserves_existing_archive(tmp_path: Path) -> None:
    with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        return_value=io.BytesIO(ARCHIVE_CONTENT),
    ):
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    original_archive = first.path.read_bytes()
    metadata_path = tmp_path / f"{first.filename}.metadata.json"
    _set_cache_age(metadata_path, timedelta(hours=169))

    with (
        patch(
            "landscout.sources.cadastre_fr.open_safe_https",
            return_value=io.BytesIO(CORRUPTED_ARCHIVE_CONTENT),
        ),
        pytest.raises(CadastreDownloadError),
    ):
        download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert first.path.read_bytes() == original_archive
    assert not list(tmp_path.glob("*.part"))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_corsica_cadastre_urls_are_canonical`

**Purpose:** Regression invariant: corsica cadastre urls are canonical. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_corsica_cadastre_urls_are_canonical(code: str, department: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("code", "department"),
    [("2A004", "2A"), ("2B033", "2B")],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `code` | positional-or-keyword | `str` | `required` |
| `department` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert f"/{department}/{code}/cadastre-{code}-parcelles.json.gz" in url`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `build_cadastre_parcelles_url` | `landscout.sources.cadastre_fr.build_cadastre_parcelles_url` |
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
def test_corsica_cadastre_urls_are_canonical(code: str, department: str) -> None:
    url = build_cadastre_parcelles_url(code)

    assert f"/{department}/{code}/cadastre-{code}-parcelles.json.gz" in url
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_noncanonical_commune_code_is_controlled`

**Purpose:** Regression invariant: noncanonical commune code is controlled. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_noncanonical_commune_code_is_controlled(code: object) -> None:
```

- Exact decorators: `pytest.mark.parametrize("code", [31395, "2a004", " 31395 ", "ABCDE"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `code` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises((TypeError, ValueError), match="Commune code")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `build_cadastre_parcelles_url` | `landscout.sources.cadastre_fr.build_cadastre_parcelles_url` |
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
def test_noncanonical_commune_code_is_controlled(code: object) -> None:
    with pytest.raises((TypeError, ValueError), match="Commune code"):
        build_cadastre_parcelles_url(code)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_download_timeout_is_strict_finite_positive`

**Purpose:** Regression invariant: download timeout is strict finite positive. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_download_timeout_is_strict_finite_positive(
    tmp_path: Path,
    timeout: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "timeout",
    [0, -1, float("nan"), float("inf"), "60", True],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `timeout` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValueError, match="timeout")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `download_cadastre_parcelles` | `landscout.sources.cadastre_fr.download_cadastre_parcelles` |
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
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_download_timeout_is_strict_finite_positive(
    tmp_path: Path,
    timeout: object,
) -> None:
    with pytest.raises(ValueError, match="timeout"):
        download_cadastre_parcelles(
            COMMUNE_CODE,
            tmp_path,
            timeout=timeout,  # type: ignore[arg-type]
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_cache_age_is_strict_finite_nonnegative`

**Purpose:** Regression invariant: cache age is strict finite nonnegative. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_cache_age_is_strict_finite_nonnegative(
    tmp_path: Path,
    max_age: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "max_age",
    [-1, float("nan"), float("inf"), "168", True],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `max_age` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValueError, match="max_cache_age_hours")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `download_cadastre_parcelles` | `landscout.sources.cadastre_fr.download_cadastre_parcelles` |
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
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_cache_age_is_strict_finite_nonnegative(
    tmp_path: Path,
    max_age: object,
) -> None:
    with pytest.raises(ValueError, match="max_cache_age_hours"):
        download_cadastre_parcelles(
            COMMUNE_CODE,
            tmp_path,
            max_cache_age_hours=max_age,  # type: ignore[arg-type]
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_malformed_cached_metadata_triggers_refresh`

**Purpose:** Regression invariant: malformed cached metadata triggers refresh. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_malformed_cached_metadata_triggers_refresh(
    tmp_path: Path,
    field: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("field", ["file_size", "sha256", "download_timestamp"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `field` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert opener.call_count == 2`
  - `assert refreshed.path.read_bytes() == REFRESHED_ARCHIVE_CONTENT`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `patch` | `unittest.mock.patch` |
| `io.BytesIO` | `io.BytesIO` |
| `download_cadastre_parcelles` | `landscout.sources.cadastre_fr.download_cadastre_parcelles` |
| `json.loads` | `json.loads` |
| `metadata_path.read_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `refreshed.path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `metadata_path.read_text`<br>`refreshed.path.read_bytes` |
| Filesystem/archive write or publication | `metadata_path.write_text` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `metadata[field] = {<br>            "file_size": first.file_size + 1,<br>            "sha256": "0" * 64,<br>            "download_timestamp": "not-a-timestamp",<br>        }[field]` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_malformed_cached_metadata_triggers_refresh(
    tmp_path: Path,
    field: str,
) -> None:
    with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        side_effect=[
            io.BytesIO(ARCHIVE_CONTENT),
            io.BytesIO(REFRESHED_ARCHIVE_CONTENT),
        ],
    ) as opener:
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
        metadata_path = tmp_path / f"{first.filename}.metadata.json"
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        metadata[field] = {
            "file_size": first.file_size + 1,
            "sha256": "0" * 64,
            "download_timestamp": "not-a-timestamp",
        }[field]
        metadata_path.write_text(json.dumps(metadata), encoding="utf-8")
        refreshed = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert opener.call_count == 2
    assert refreshed.path.read_bytes() == REFRESHED_ARCHIVE_CONTENT
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_cache_metadata_schema_and_size_are_strict_integers`

**Purpose:** Regression invariant: cache metadata schema and size are strict integers. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_cache_metadata_schema_and_size_are_strict_integers(
    tmp_path: Path,
    field: str,
    value: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("field", "value"),
    [
        ("schema_version", True),
        ("schema_version", 1.0),
        ("file_size", True),
        ("file_size", 1.0),
        ("file_size", "1"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `field` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert opener.call_count == 2`
  - `assert refreshed.cache_hit is False`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `patch` | `unittest.mock.patch` |
| `io.BytesIO` | `io.BytesIO` |
| `download_cadastre_parcelles` | `landscout.sources.cadastre_fr.download_cadastre_parcelles` |
| `json.loads` | `json.loads` |
| `metadata_path.read_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `metadata_path.read_text` |
| Filesystem/archive write or publication | `metadata_path.write_text` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `metadata[field] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_cache_metadata_schema_and_size_are_strict_integers(
    tmp_path: Path,
    field: str,
    value: object,
) -> None:
    with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        side_effect=[
            io.BytesIO(ARCHIVE_CONTENT),
            io.BytesIO(REFRESHED_ARCHIVE_CONTENT),
        ],
    ) as opener:
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
        metadata_path = tmp_path / f"{first.filename}.metadata.json"
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        metadata[field] = value
        metadata_path.write_text(json.dumps(metadata), encoding="utf-8")
        refreshed = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert opener.call_count == 2
    assert refreshed.cache_hit is False
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_future_cached_timestamp_triggers_refresh`

**Purpose:** Regression invariant: future cached timestamp triggers refresh. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_future_cached_timestamp_triggers_refresh(tmp_path: Path) -> None:
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
  - `assert opener.call_count == 2`
  - `assert refreshed.path.read_bytes() == REFRESHED_ARCHIVE_CONTENT`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `patch` | `unittest.mock.patch` |
| `io.BytesIO` | `io.BytesIO` |
| `download_cadastre_parcelles` | `landscout.sources.cadastre_fr.download_cadastre_parcelles` |
| `json.loads` | `json.loads` |
| `metadata_path.read_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `(<br>            datetime.now(UTC) + timedelta(hours=1)<br>        ).isoformat` | `unresolved local/third-party receiver; no ownership inferred` |
| `datetime.now` | `datetime.datetime.now` |
| `timedelta` | `datetime.timedelta` |
| `metadata_path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `refreshed.path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `metadata_path.read_text`<br>`refreshed.path.read_bytes` |
| Filesystem/archive write or publication | `metadata_path.write_text` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `metadata["download_timestamp"] = (<br>            datetime.now(UTC) + timedelta(hours=1)<br>        ).isoformat()` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_future_cached_timestamp_triggers_refresh(tmp_path: Path) -> None:
    with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        side_effect=[
            io.BytesIO(ARCHIVE_CONTENT),
            io.BytesIO(REFRESHED_ARCHIVE_CONTENT),
        ],
    ) as opener:
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
        metadata_path = tmp_path / f"{first.filename}.metadata.json"
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        metadata["download_timestamp"] = (
            datetime.now(UTC) + timedelta(hours=1)
        ).isoformat()
        metadata_path.write_text(json.dumps(metadata), encoding="utf-8")
        refreshed = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert opener.call_count == 2
    assert refreshed.path.read_bytes() == REFRESHED_ARCHIVE_CONTENT
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_strict_cadastre_cache_json_never_returns_a_cache_hit`

**Purpose:** Regression invariant: strict cadastre cache json never returns a cache hit. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_strict_cadastre_cache_json_never_returns_a_cache_hit(
    tmp_path: Path,
    invalid_metadata: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "invalid_metadata",
    [
        '{"schema_version":1,"schema_version":1}',
        '{"schema_version":1,"file_size":NaN}',
        "[]",
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `invalid_metadata` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert opener.call_count == 2`
  - `assert refreshed.cache_hit is False`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `patch` | `unittest.mock.patch` |
| `io.BytesIO` | `io.BytesIO` |
| `download_cadastre_parcelles` | `landscout.sources.cadastre_fr.download_cadastre_parcelles` |
| `metadata_path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `metadata_path.write_text` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_strict_cadastre_cache_json_never_returns_a_cache_hit(
    tmp_path: Path,
    invalid_metadata: str,
) -> None:
    with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        side_effect=[
            io.BytesIO(ARCHIVE_CONTENT),
            io.BytesIO(REFRESHED_ARCHIVE_CONTENT),
        ],
    ) as opener:
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
        metadata_path = tmp_path / f"{first.filename}.metadata.json"
        metadata_path.write_text(invalid_metadata, encoding="utf-8")
        refreshed = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert opener.call_count == 2
    assert refreshed.cache_hit is False
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_metadata_publication_failure_restores_previous_cache_pair`

**Purpose:** Regression invariant: metadata publication failure restores previous cache pair. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_metadata_publication_failure_restores_previous_cache_pair(
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
  - `pytest.raises(CadastreDownloadError, match="publication")`
- Exact assertions:
  - `assert first.path.read_bytes() == archive_before`
  - `assert metadata_path.read_bytes() == metadata_before`
  - `assert not list(tmp_path.glob("*.part"))`
  - `assert not list(tmp_path.glob("*.bak"))`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `patch` | `unittest.mock.patch` |
| `io.BytesIO` | `io.BytesIO` |
| `download_cadastre_parcelles` | `landscout.sources.cadastre_fr.download_cadastre_parcelles` |
| `_set_cache_age` | `tests.unit.test_cadastre_fr._set_cache_age` |
| `timedelta` | `datetime.timedelta` |
| `first.path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.with_suffix` | `unresolved local/third-party receiver; no ownership inferred` |
| `__import__` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `tmp_path.glob` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `first.path.read_bytes`<br>`metadata_path.read_bytes`<br>`tmp_path.glob` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_metadata_publication_failure_restores_previous_cache_pair(
    tmp_path: Path,
) -> None:
    with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        return_value=io.BytesIO(ARCHIVE_CONTENT),
    ):
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
    metadata_path = tmp_path / f"{first.filename}.metadata.json"
    _set_cache_age(metadata_path, timedelta(hours=169))
    archive_before = first.path.read_bytes()
    metadata_before = metadata_path.read_bytes()
    temporary_metadata = metadata_path.with_suffix(f"{metadata_path.suffix}.part")
    original_replace = __import__(
        "landscout.sources.cadastre_fr",
        fromlist=["_replace_file"],
    )._replace_file

    def fail_metadata_publication(source: Path, target: Path) -> None:
        if source == temporary_metadata and target == metadata_path:
            raise OSError("simulated metadata publication failure")
        original_replace(source, target)

    with (
        patch(
            "landscout.sources.cadastre_fr.open_safe_https",
            return_value=io.BytesIO(REFRESHED_ARCHIVE_CONTENT),
        ),
        patch(
            "landscout.sources.cadastre_fr._replace_file",
            side_effect=fail_metadata_publication,
        ),
        pytest.raises(CadastreDownloadError, match="publication"),
    ):
        download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert first.path.read_bytes() == archive_before
    assert metadata_path.read_bytes() == metadata_before
    assert not list(tmp_path.glob("*.part"))
    assert not list(tmp_path.glob("*.bak"))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_metadata_publication_failure_restores_previous_cache_pair.fail_metadata_publication`

**Purpose:** Implements `fail metadata publication` within the file role: Provides complete unit and regression coverage for the `cadastre_fr` contracts exercised in this file.

**Exact signature**

```python
def fail_metadata_publication(source: Path, target: Path) -> None:
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
  - `OSError("simulated metadata publication failure")` under lexical guard `source == temporary_metadata and target == metadata_path`.

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
def fail_metadata_publication(source: Path, target: Path) -> None:
        if source == temporary_metadata and target == metadata_path:
            raise OSError("simulated metadata publication failure")
        original_replace(source, target)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_first_metadata_publication_failure_leaves_no_half_pair`

**Purpose:** Regression invariant: first metadata publication failure leaves no half pair. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_first_metadata_publication_failure_leaves_no_half_pair(
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
  - `pytest.raises(CadastreDownloadError, match="publication")`
- Exact assertions:
  - `assert not expected_path.exists()`
  - `assert not metadata_path.exists()`
  - `assert not list(tmp_path.glob("*.part"))`
  - `assert not list(tmp_path.glob("*.bak"))`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `metadata_path.with_suffix` | `unresolved local/third-party receiver; no ownership inferred` |
| `__import__` | `unresolved local/third-party receiver; no ownership inferred` |
| `patch` | `unittest.mock.patch` |
| `io.BytesIO` | `io.BytesIO` |
| `pytest.raises` | `pytest.raises` |
| `download_cadastre_parcelles` | `landscout.sources.cadastre_fr.download_cadastre_parcelles` |
| `expected_path.exists` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.exists` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `tmp_path.glob` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `expected_path.exists`<br>`metadata_path.exists`<br>`tmp_path.glob` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_first_metadata_publication_failure_leaves_no_half_pair(
    tmp_path: Path,
) -> None:
    expected_path = tmp_path / "cadastre-31395-parcelles.json.gz"
    metadata_path = tmp_path / f"{expected_path.name}.metadata.json"
    temporary_metadata = metadata_path.with_suffix(f"{metadata_path.suffix}.part")
    original_replace = __import__(
        "landscout.sources.cadastre_fr",
        fromlist=["_replace_file"],
    )._replace_file

    def fail_metadata_publication(source: Path, target: Path) -> None:
        if source == temporary_metadata and target == metadata_path:
            raise OSError("simulated metadata publication failure")
        original_replace(source, target)

    with (
        patch(
            "landscout.sources.cadastre_fr.open_safe_https",
            return_value=io.BytesIO(ARCHIVE_CONTENT),
        ),
        patch(
            "landscout.sources.cadastre_fr._replace_file",
            side_effect=fail_metadata_publication,
        ),
        pytest.raises(CadastreDownloadError, match="publication"),
    ):
        download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert not expected_path.exists()
    assert not metadata_path.exists()
    assert not list(tmp_path.glob("*.part"))
    assert not list(tmp_path.glob("*.bak"))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_first_metadata_publication_failure_leaves_no_half_pair.fail_metadata_publication`

**Purpose:** Implements `fail metadata publication` within the file role: Provides complete unit and regression coverage for the `cadastre_fr` contracts exercised in this file.

**Exact signature**

```python
def fail_metadata_publication(source: Path, target: Path) -> None:
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
  - `OSError("simulated metadata publication failure")` under lexical guard `source == temporary_metadata and target == metadata_path`.

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
def fail_metadata_publication(source: Path, target: Path) -> None:
        if source == temporary_metadata and target == metadata_path:
            raise OSError("simulated metadata publication failure")
        original_replace(source, target)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_publication_and_rollback_failure_preserves_recovery_backup`

**Purpose:** Regression invariant: publication and rollback failure preserves recovery backup. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_publication_and_rollback_failure_preserves_recovery_backup(
    tmp_path: Path,
    rollback_target: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("rollback_target", ["archive", "metadata"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `rollback_target` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(CadastreDownloadError, match="rollback")`
- Exact assertions:
  - `assert useful_backups`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `patch` | `unittest.mock.patch` |
| `io.BytesIO` | `io.BytesIO` |
| `download_cadastre_parcelles` | `landscout.sources.cadastre_fr.download_cadastre_parcelles` |
| `_set_cache_age` | `tests.unit.test_cadastre_fr._set_cache_age` |
| `timedelta` | `datetime.timedelta` |
| `first.path.with_suffix` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.with_suffix` | `unresolved local/third-party receiver; no ownership inferred` |
| `patch.object` | `unittest.mock.patch.object` |
| `pytest.raises` | `pytest.raises` |
| `path.exists` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `path.exists` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_publication_and_rollback_failure_preserves_recovery_backup(
    tmp_path: Path,
    rollback_target: str,
) -> None:
    with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        return_value=io.BytesIO(ARCHIVE_CONTENT),
    ):
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
    metadata_path = tmp_path / f"{first.filename}.metadata.json"
    _set_cache_age(metadata_path, timedelta(hours=169))
    archive_backup = first.path.with_suffix(f"{first.path.suffix}.bak")
    metadata_backup = metadata_path.with_suffix(f"{metadata_path.suffix}.bak")
    temporary_metadata = metadata_path.with_suffix(f"{metadata_path.suffix}.part")
    original_replace = cadastre_fr._replace_file

    def fail_publication_and_rollback(source: Path, target: Path) -> None:
        if source == temporary_metadata and target == metadata_path:
            raise OSError("publication failure")
        if rollback_target == "archive" and source == archive_backup:
            raise OSError("archive rollback failure")
        if rollback_target == "metadata" and source == metadata_backup:
            raise OSError("metadata rollback failure")
        original_replace(source, target)

    with (
        patch(
            "landscout.sources.cadastre_fr.open_safe_https",
            return_value=io.BytesIO(REFRESHED_ARCHIVE_CONTENT),
        ),
        patch.object(
            cadastre_fr,
            "_replace_file",
            side_effect=fail_publication_and_rollback,
        ),
        pytest.raises(CadastreDownloadError, match="rollback"),
    ):
        download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    useful_backups = [
        path for path in (archive_backup, metadata_backup) if path.exists()
    ]
    assert useful_backups
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_publication_and_rollback_failure_preserves_recovery_backup.fail_publication_and_rollback`

**Purpose:** Implements `fail publication and rollback` within the file role: Provides complete unit and regression coverage for the `cadastre_fr` contracts exercised in this file.

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
  - `OSError("publication failure")` under lexical guard `source == temporary_metadata and target == metadata_path`.
  - `OSError("archive rollback failure")` under lexical guard `rollback_target == "archive" and source == archive_backup`.
  - `OSError("metadata rollback failure")` under lexical guard `rollback_target == "metadata" and source == metadata_backup`.

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
def fail_publication_and_rollback(source: Path, target: Path) -> None:
        if source == temporary_metadata and target == metadata_path:
            raise OSError("publication failure")
        if rollback_target == "archive" and source == archive_backup:
            raise OSError("archive rollback failure")
        if rollback_target == "metadata" and source == metadata_backup:
            raise OSError("metadata rollback failure")
        original_replace(source, target)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_stale_recovery_backup_rejects_cache_before_network_and_preserves_bytes`

**Purpose:** Regression invariant: stale recovery backup rejects cache before network and preserves bytes. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_stale_recovery_backup_rejects_cache_before_network_and_preserves_bytes(
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
  - `pytest.raises(CadastreDownloadError, match="backup\|recovery\|manual")`
- Exact assertions:
  - `assert recovery_path.read_bytes() == recovery_bytes`
  - `assert first.path.read_bytes() == ARCHIVE_CONTENT`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `patch` | `unittest.mock.patch` |
| `io.BytesIO` | `io.BytesIO` |
| `download_cadastre_parcelles` | `landscout.sources.cadastre_fr.download_cadastre_parcelles` |
| `first.path.with_suffix` | `unresolved local/third-party receiver; no ownership inferred` |
| `recovery_path.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `AssertionError` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `opener.assert_not_called` | `unresolved local/third-party receiver; no ownership inferred` |
| `recovery_path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `first.path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `recovery_path.read_bytes`<br>`first.path.read_bytes` |
| Filesystem/archive write or publication | `recovery_path.write_bytes` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_stale_recovery_backup_rejects_cache_before_network_and_preserves_bytes(
    tmp_path: Path,
) -> None:
    with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        return_value=io.BytesIO(ARCHIVE_CONTENT),
    ):
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
    recovery_path = first.path.with_suffix(f"{first.path.suffix}.bak")
    recovery_bytes = b"manual cadastre recovery material"
    recovery_path.write_bytes(recovery_bytes)

    with (
        patch(
            "landscout.sources.cadastre_fr.open_safe_https",
            side_effect=AssertionError("recovery state must fail before network"),
        ) as opener,
        pytest.raises(CadastreDownloadError, match="backup|recovery|manual"),
    ):
        download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    opener.assert_not_called()
    assert recovery_path.read_bytes() == recovery_bytes
    assert first.path.read_bytes() == ARCHIVE_CONTENT
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_next_run_after_double_failure_preserves_recovery_before_network`

**Purpose:** Regression invariant: next run after double failure preserves recovery before network. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_next_run_after_double_failure_preserves_recovery_before_network(
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
  - `pytest.raises(CadastreDownloadError, match="rollback")`
  - `pytest.raises(CadastreDownloadError, match="backup\|recovery\|manual")`
- Exact assertions:
  - `assert archive_backup.read_bytes() == old_archive`
  - `assert metadata_backup.read_bytes() == old_metadata`
  - `assert archive_backup.read_bytes() == archive_recovery`
  - `assert metadata_backup.read_bytes() == metadata_recovery`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `patch` | `unittest.mock.patch` |
| `io.BytesIO` | `io.BytesIO` |
| `download_cadastre_parcelles` | `landscout.sources.cadastre_fr.download_cadastre_parcelles` |
| `_set_cache_age` | `tests.unit.test_cadastre_fr._set_cache_age` |
| `timedelta` | `datetime.timedelta` |
| `first.path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.with_suffix` | `unresolved local/third-party receiver; no ownership inferred` |
| `first.path.with_suffix` | `unresolved local/third-party receiver; no ownership inferred` |
| `patch.object` | `unittest.mock.patch.object` |
| `pytest.raises` | `pytest.raises` |
| `archive_backup.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_backup.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `AssertionError` | `unresolved local/third-party receiver; no ownership inferred` |
| `opener.assert_not_called` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_next_run_after_double_failure_preserves_recovery_before_network(
    tmp_path: Path,
) -> None:
    with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        return_value=io.BytesIO(ARCHIVE_CONTENT),
    ):
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
    metadata_path = tmp_path / f"{first.filename}.metadata.json"
    _set_cache_age(metadata_path, timedelta(hours=169))
    old_archive = first.path.read_bytes()
    old_metadata = metadata_path.read_bytes()
    temporary_metadata = metadata_path.with_suffix(f"{metadata_path.suffix}.part")
    archive_backup = first.path.with_suffix(f"{first.path.suffix}.bak")
    metadata_backup = metadata_path.with_suffix(f"{metadata_path.suffix}.bak")
    original_replace = cadastre_fr._replace_file

    def fail_publication_and_rollback(source: Path, target: Path) -> None:
        if source == temporary_metadata and target == metadata_path:
            raise OSError("publication failed")
        if source == archive_backup and target == first.path:
            raise OSError("rollback failed")
        original_replace(source, target)

    with (
        patch(
            "landscout.sources.cadastre_fr.open_safe_https",
            return_value=io.BytesIO(REFRESHED_ARCHIVE_CONTENT),
        ),
        patch.object(
            cadastre_fr,
            "_replace_file",
            side_effect=fail_publication_and_rollback,
        ),
        pytest.raises(CadastreDownloadError, match="rollback"),
    ):
        download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert archive_backup.read_bytes() == old_archive
    assert metadata_backup.read_bytes() == old_metadata
    archive_recovery = archive_backup.read_bytes()
    metadata_recovery = metadata_backup.read_bytes()

    with (
        patch(
            "landscout.sources.cadastre_fr.open_safe_https",
            side_effect=AssertionError("recovery state must fail before network"),
        ) as opener,
        pytest.raises(CadastreDownloadError, match="backup|recovery|manual"),
    ):
        download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    opener.assert_not_called()
    assert archive_backup.read_bytes() == archive_recovery
    assert metadata_backup.read_bytes() == metadata_recovery
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_next_run_after_double_failure_preserves_recovery_before_network.fail_publication_and_rollback`

**Purpose:** Implements `fail publication and rollback` within the file role: Provides complete unit and regression coverage for the `cadastre_fr` contracts exercised in this file.

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
  - `OSError("publication failed")` under lexical guard `source == temporary_metadata and target == metadata_path`.
  - `OSError("rollback failed")` under lexical guard `source == archive_backup and target == first.path`.

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
def fail_publication_and_rollback(source: Path, target: Path) -> None:
        if source == temporary_metadata and target == metadata_path:
            raise OSError("publication failed")
        if source == archive_backup and target == first.path:
            raise OSError("rollback failed")
        original_replace(source, target)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_temporary_link_or_junction_cannot_modify_target_before_network`

**Purpose:** Regression invariant: temporary link or junction cannot modify target before network. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_temporary_link_or_junction_cannot_modify_target_before_network(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    temporary_role: str,
    link_kind: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("temporary_role", ["archive", "metadata"])`, `pytest.mark.parametrize("link_kind", ["symlink", "junction"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |
| `temporary_role` | positional-or-keyword | `str` | `required` |
| `link_kind` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(CadastreDownloadError, match="temporary\|link\|cache")`
- Exact assertions:
  - `assert network_calls == 0`
  - `assert sentinel.read_bytes() == sentinel_bytes`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `archive_path.with_suffix` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.with_suffix` | `unresolved local/third-party receiver; no ownership inferred` |
| `sentinel.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `download_cadastre_parcelles` | `landscout.sources.cadastre_fr.download_cadastre_parcelles` |
| `sentinel.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `sentinel.read_bytes` |
| Filesystem/archive write or publication | `sentinel.write_bytes` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_temporary_link_or_junction_cannot_modify_target_before_network(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    temporary_role: str,
    link_kind: str,
) -> None:
    archive_path = tmp_path / "cadastre-31395-parcelles.json.gz"
    metadata_path = tmp_path / f"{archive_path.name}.metadata.json"
    temporary_paths = {
        "archive": archive_path.with_suffix(f"{archive_path.suffix}.part"),
        "metadata": metadata_path.with_suffix(f"{metadata_path.suffix}.part"),
    }
    unsafe_path = temporary_paths[temporary_role]
    sentinel = tmp_path / "do-not-overwrite.txt"
    sentinel_bytes = b"irreplaceable cadastre sentinel"
    sentinel.write_bytes(sentinel_bytes)
    original_is_symlink = Path.is_symlink
    original_is_junction = Path.is_junction
    original_open = Path.open

    def simulated_is_symlink(path: Path) -> bool:
        return (link_kind == "symlink" and path == unsafe_path) or original_is_symlink(
            path
        )

    def simulated_is_junction(path: Path) -> bool:
        return (
            link_kind == "junction" and path == unsafe_path
        ) or original_is_junction(path)

    def simulated_symlink_open(path: Path, *args: object, **kwargs: object) -> object:
        if path == unsafe_path:
            return original_open(sentinel, *args, **kwargs)
        return original_open(path, *args, **kwargs)

    network_calls = 0

    def record_network(*args: object, **kwargs: object) -> io.BytesIO:
        nonlocal network_calls
        network_calls += 1
        return io.BytesIO(ARCHIVE_CONTENT)

    monkeypatch.setattr(Path, "is_symlink", simulated_is_symlink)
    monkeypatch.setattr(Path, "is_junction", simulated_is_junction)
    monkeypatch.setattr(Path, "open", simulated_symlink_open)
    monkeypatch.setattr(cadastre_fr, "open_safe_https", record_network)

    with pytest.raises(CadastreDownloadError, match="temporary|link|cache"):
        download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert network_calls == 0
    assert sentinel.read_bytes() == sentinel_bytes
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_temporary_link_or_junction_cannot_modify_target_before_network.simulated_is_symlink`

**Purpose:** Implements `simulated is symlink` within the file role: Provides complete unit and regression coverage for the `cadastre_fr` contracts exercised in this file.

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
  - `(link_kind == "symlink" and path == unsafe_path) or original_is_symlink(<br>            path<br>        )`
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
        return (link_kind == "symlink" and path == unsafe_path) or original_is_symlink(
            path
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_temporary_link_or_junction_cannot_modify_target_before_network.simulated_is_junction`

**Purpose:** Implements `simulated is junction` within the file role: Provides complete unit and regression coverage for the `cadastre_fr` contracts exercised in this file.

**Exact signature**

```python
def simulated_is_junction(path: Path) -> bool:
```

- Exact decorators: none.
- Declared return annotation: `bool`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `(<br>            link_kind == "junction" and path == unsafe_path<br>        ) or original_is_junction(path)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `original_is_junction` | `unresolved local/third-party receiver; no ownership inferred` |

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
def simulated_is_junction(path: Path) -> bool:
        return (
            link_kind == "junction" and path == unsafe_path
        ) or original_is_junction(path)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_temporary_link_or_junction_cannot_modify_target_before_network.simulated_symlink_open`

**Purpose:** Implements `simulated symlink open` within the file role: Provides complete unit and regression coverage for the `cadastre_fr` contracts exercised in this file.

**Exact signature**

```python
def simulated_symlink_open(path: Path, *args: object, **kwargs: object) -> object:
```

- Exact decorators: none.
- Declared return annotation: `object`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- Exact observed return expressions:
  - `original_open(sentinel, *args, **kwargs)`
  - `original_open(path, *args, **kwargs)`
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
def simulated_symlink_open(path: Path, *args: object, **kwargs: object) -> object:
        if path == unsafe_path:
            return original_open(sentinel, *args, **kwargs)
        return original_open(path, *args, **kwargs)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_temporary_link_or_junction_cannot_modify_target_before_network.record_network`

**Purpose:** Implements `record network` within the file role: Provides complete unit and regression coverage for the `cadastre_fr` contracts exercised in this file.

**Exact signature**

```python
def record_network(*args: object, **kwargs: object) -> io.BytesIO:
```

- Exact decorators: none.
- Declared return annotation: `io.BytesIO`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- Exact observed return expressions:
  - `io.BytesIO(ARCHIVE_CONTENT)`
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
def record_network(*args: object, **kwargs: object) -> io.BytesIO:
        nonlocal network_calls
        network_calls += 1
        return io.BytesIO(ARCHIVE_CONTENT)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_broken_recovery_symlink_is_rejected_before_network`

**Purpose:** Regression invariant: broken recovery symlink is rejected before network. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_broken_recovery_symlink_is_rejected_before_network(
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
  - `pytest.raises(CadastreDownloadError, match="backup\|recovery\|manual")`
- Exact assertions:
  - `assert network_calls == 0`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `archive_path.with_suffix` | `unresolved local/third-party receiver; no ownership inferred` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `download_cadastre_parcelles` | `landscout.sources.cadastre_fr.download_cadastre_parcelles` |

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
def test_broken_recovery_symlink_is_rejected_before_network(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    archive_path = tmp_path / "cadastre-31395-parcelles.json.gz"
    recovery_path = archive_path.with_suffix(f"{archive_path.suffix}.bak")
    original_is_symlink = Path.is_symlink

    def simulated_is_symlink(path: Path) -> bool:
        return path == recovery_path or original_is_symlink(path)

    network_calls = 0

    def fail_network(*args: object, **kwargs: object) -> io.BytesIO:
        nonlocal network_calls
        network_calls += 1
        raise AssertionError("broken recovery link must fail before network")

    monkeypatch.setattr(Path, "is_symlink", simulated_is_symlink)
    monkeypatch.setattr(cadastre_fr, "open_safe_https", fail_network)

    with pytest.raises(CadastreDownloadError, match="backup|recovery|manual"):
        download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert network_calls == 0
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_broken_recovery_symlink_is_rejected_before_network.simulated_is_symlink`

**Purpose:** Implements `simulated is symlink` within the file role: Provides complete unit and regression coverage for the `cadastre_fr` contracts exercised in this file.

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
  - `path == recovery_path or original_is_symlink(path)`
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
        return path == recovery_path or original_is_symlink(path)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_broken_recovery_symlink_is_rejected_before_network.fail_network`

**Purpose:** Implements `fail network` within the file role: Provides complete unit and regression coverage for the `cadastre_fr` contracts exercised in this file.

**Exact signature**

```python
def fail_network(*args: object, **kwargs: object) -> io.BytesIO:
```

- Exact decorators: none.
- Declared return annotation: `io.BytesIO`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `AssertionError("broken recovery link must fail before network")`.

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
def fail_network(*args: object, **kwargs: object) -> io.BytesIO:
        nonlocal network_calls
        network_calls += 1
        raise AssertionError("broken recovery link must fail before network")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_cleanup_failure_does_not_mask_double_failure_recovery_error`

**Purpose:** Regression invariant: cleanup failure does not mask double failure recovery error. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_cleanup_failure_does_not_mask_double_failure_recovery_error(
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
  - `pytest.raises(CadastreDownloadError, match="rollback")`
- Exact assertions:
  - `assert archive_backup.read_bytes() == old_archive`
  - `assert metadata_backup.read_bytes() == old_metadata`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `patch` | `unittest.mock.patch` |
| `io.BytesIO` | `io.BytesIO` |
| `download_cadastre_parcelles` | `landscout.sources.cadastre_fr.download_cadastre_parcelles` |
| `_set_cache_age` | `tests.unit.test_cadastre_fr._set_cache_age` |
| `timedelta` | `datetime.timedelta` |
| `first.path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `metadata_path.with_suffix` | `unresolved local/third-party receiver; no ownership inferred` |
| `first.path.with_suffix` | `unresolved local/third-party receiver; no ownership inferred` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
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
def test_cleanup_failure_does_not_mask_double_failure_recovery_error(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        return_value=io.BytesIO(ARCHIVE_CONTENT),
    ):
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
    metadata_path = tmp_path / f"{first.filename}.metadata.json"
    _set_cache_age(metadata_path, timedelta(hours=169))
    old_archive = first.path.read_bytes()
    old_metadata = metadata_path.read_bytes()
    temporary_metadata = metadata_path.with_suffix(f"{metadata_path.suffix}.part")
    archive_backup = first.path.with_suffix(f"{first.path.suffix}.bak")
    metadata_backup = metadata_path.with_suffix(f"{metadata_path.suffix}.bak")
    original_replace = cadastre_fr._replace_file
    original_unlink = Path.unlink
    rollback_failed = False

    def fail_publication_and_rollback(source: Path, target: Path) -> None:
        nonlocal rollback_failed
        if source == temporary_metadata and target == metadata_path:
            raise OSError("publication failed")
        if source == archive_backup and target == first.path:
            rollback_failed = True
            raise OSError("rollback failed")
        original_replace(source, target)

    def fail_temporary_cleanup(path: Path, *, missing_ok: bool = False) -> None:
        if rollback_failed and path == temporary_metadata:
            raise PermissionError("temporary cleanup failed")
        original_unlink(path, missing_ok=missing_ok)

    monkeypatch.setattr(
        cadastre_fr,
        "open_safe_https",
        lambda *args, **kwargs: io.BytesIO(REFRESHED_ARCHIVE_CONTENT),
    )
    monkeypatch.setattr(cadastre_fr, "_replace_file", fail_publication_and_rollback)
    monkeypatch.setattr(Path, "unlink", fail_temporary_cleanup)

    with pytest.raises(CadastreDownloadError, match="rollback"):
        download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert archive_backup.read_bytes() == old_archive
    assert metadata_backup.read_bytes() == old_metadata
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_cleanup_failure_does_not_mask_double_failure_recovery_error.fail_publication_and_rollback`

**Purpose:** Implements `fail publication and rollback` within the file role: Provides complete unit and regression coverage for the `cadastre_fr` contracts exercised in this file.

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
  - `OSError("publication failed")` under lexical guard `source == temporary_metadata and target == metadata_path`.
  - `OSError("rollback failed")` under lexical guard `source == archive_backup and target == first.path`.

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
def fail_publication_and_rollback(source: Path, target: Path) -> None:
        nonlocal rollback_failed
        if source == temporary_metadata and target == metadata_path:
            raise OSError("publication failed")
        if source == archive_backup and target == first.path:
            rollback_failed = True
            raise OSError("rollback failed")
        original_replace(source, target)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_cleanup_failure_does_not_mask_double_failure_recovery_error.fail_temporary_cleanup`

**Purpose:** Implements `fail temporary cleanup` within the file role: Provides complete unit and regression coverage for the `cadastre_fr` contracts exercised in this file.

**Exact signature**

```python
def fail_temporary_cleanup(path: Path, *, missing_ok: bool = False) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |
| `missing_ok` | keyword-only | `bool` | `False` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `PermissionError("temporary cleanup failed")` under lexical guard `rollback_failed and path == temporary_metadata`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `PermissionError` | `unresolved local/third-party receiver; no ownership inferred` |
| `original_unlink` | `unresolved local/third-party receiver; no ownership inferred` |

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
def fail_temporary_cleanup(path: Path, *, missing_ok: bool = False) -> None:
        if rollback_failed and path == temporary_metadata:
            raise PermissionError("temporary cleanup failed")
        original_unlink(path, missing_ok=missing_ok)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.


## 7. Test-specific regression contract

- Test functions: **27**.
- Pytest fixtures (decorator-proven): **0**.

### Per-test regression index

| Test | Parametrization | Expected exception contexts | Assertion count | Exact regression purpose |
|---|---|---|---:|---|
| `test_build_cadastre_parcelles_url` | none | none | 1 | Proves build cadastre parcelles url using the exact source reproduced in section 7. |
| `test_successful_download` | none | none | 8 | Proves successful download using the exact source reproduced in section 7. |
| `test_fresh_cache_is_reused` | none | none | 5 | Proves fresh cache is reused using the exact source reproduced in section 7. |
| `test_expired_cache_is_downloaded_again` | none | none | 4 | Proves expired cache is downloaded again using the exact source reproduced in section 7. |
| `test_failed_refresh_preserves_cached_archive` | none | pytest.raises(CadastreDownloadError) | 2 | Proves failed refresh preserves cached archive using the exact source reproduced in section 7. |
| `test_failed_http_response` | none | pytest.raises(CadastreDownloadError) | 1 | Proves failed http response using the exact source reproduced in section 7. |
| `test_checksum_generation` | none | none | 1 | Proves checksum generation using the exact source reproduced in section 7. |
| `test_valid_gzip_is_accepted` | none | none | 1 | Proves valid gzip is accepted using the exact source reproduced in section 7. |
| `test_truncated_gzip_is_rejected` | none | none | 1 | Proves truncated gzip is rejected using the exact source reproduced in section 7. |
| `test_corrupted_cached_archive_triggers_fresh_download` | none | none | 3 | Proves corrupted cached archive triggers fresh download using the exact source reproduced in section 7. |
| `test_corrupted_new_download_preserves_existing_archive` | none | pytest.raises(CadastreDownloadError) | 2 | Proves corrupted new download preserves existing archive using the exact source reproduced in section 7. |
| `test_corsica_cadastre_urls_are_canonical` | pytest.mark.parametrize(<br>    ("code", "department"),<br>    [("2A004", "2A"), ("2B033", "2B")],<br>) | none | 1 | Proves corsica cadastre urls are canonical using the exact source reproduced in section 7. |
| `test_noncanonical_commune_code_is_controlled` | pytest.mark.parametrize("code", [31395, "2a004", " 31395 ", "ABCDE"]) | pytest.raises((TypeError, ValueError), match="Commune code") | 0 | Proves noncanonical commune code is controlled using the exact source reproduced in section 7. |
| `test_download_timeout_is_strict_finite_positive` | pytest.mark.parametrize(<br>    "timeout",<br>    [0, -1, float("nan"), float("inf"), "60", True],<br>) | pytest.raises(ValueError, match="timeout") | 0 | Proves download timeout is strict finite positive using the exact source reproduced in section 7. |
| `test_cache_age_is_strict_finite_nonnegative` | pytest.mark.parametrize(<br>    "max_age",<br>    [-1, float("nan"), float("inf"), "168", True],<br>) | pytest.raises(ValueError, match="max_cache_age_hours") | 0 | Proves cache age is strict finite nonnegative using the exact source reproduced in section 7. |
| `test_malformed_cached_metadata_triggers_refresh` | pytest.mark.parametrize("field", ["file_size", "sha256", "download_timestamp"]) | none | 2 | Proves malformed cached metadata triggers refresh using the exact source reproduced in section 7. |
| `test_cache_metadata_schema_and_size_are_strict_integers` | pytest.mark.parametrize(<br>    ("field", "value"),<br>    [<br>        ("schema_version", True),<br>        ("schema_version", 1.0),<br>        ("file_size", True),<br>        ("file_size", 1.0),<br>        ("file_size", "1"),<br>    ],<br>) | none | 2 | Proves cache metadata schema and size are strict integers using the exact source reproduced in section 7. |
| `test_future_cached_timestamp_triggers_refresh` | none | none | 2 | Proves future cached timestamp triggers refresh using the exact source reproduced in section 7. |
| `test_strict_cadastre_cache_json_never_returns_a_cache_hit` | pytest.mark.parametrize(<br>    "invalid_metadata",<br>    [<br>        '{"schema_version":1,"schema_version":1}',<br>        '{"schema_version":1,"file_size":NaN}',<br>        "[]",<br>    ],<br>) | none | 2 | Proves strict cadastre cache json never returns a cache hit using the exact source reproduced in section 7. |
| `test_metadata_publication_failure_restores_previous_cache_pair` | none | pytest.raises(CadastreDownloadError, match="publication") | 4 | Proves metadata publication failure restores previous cache pair using the exact source reproduced in section 7. |
| `test_first_metadata_publication_failure_leaves_no_half_pair` | none | pytest.raises(CadastreDownloadError, match="publication") | 4 | Proves first metadata publication failure leaves no half pair using the exact source reproduced in section 7. |
| `test_publication_and_rollback_failure_preserves_recovery_backup` | pytest.mark.parametrize("rollback_target", ["archive", "metadata"]) | pytest.raises(CadastreDownloadError, match="rollback") | 1 | Proves publication and rollback failure preserves recovery backup using the exact source reproduced in section 7. |
| `test_stale_recovery_backup_rejects_cache_before_network_and_preserves_bytes` | none | pytest.raises(CadastreDownloadError, match="backup\|recovery\|manual") | 2 | Proves stale recovery backup rejects cache before network and preserves bytes using the exact source reproduced in section 7. |
| `test_next_run_after_double_failure_preserves_recovery_before_network` | none | pytest.raises(CadastreDownloadError, match="rollback"); pytest.raises(CadastreDownloadError, match="backup\|recovery\|manual") | 4 | Proves next run after double failure preserves recovery before network using the exact source reproduced in section 7. |
| `test_temporary_link_or_junction_cannot_modify_target_before_network` | pytest.mark.parametrize("temporary_role", ["archive", "metadata"]); pytest.mark.parametrize("link_kind", ["symlink", "junction"]) | pytest.raises(CadastreDownloadError, match="temporary\|link\|cache") | 2 | Proves temporary link or junction cannot modify target before network using the exact source reproduced in section 7. |
| `test_broken_recovery_symlink_is_rejected_before_network` | none | pytest.raises(CadastreDownloadError, match="backup\|recovery\|manual") | 1 | Proves broken recovery symlink is rejected before network using the exact source reproduced in section 7. |
| `test_cleanup_failure_does_not_mask_double_failure_recovery_error` | none | pytest.raises(CadastreDownloadError, match="rollback") | 2 | Proves cleanup failure does not mask double failure recovery error using the exact source reproduced in section 7. |

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
import gzip
import io
import json
from datetime import UTC, datetime, timedelta
from hashlib import sha256
from pathlib import Path
from unittest.mock import patch
from urllib.error import HTTPError

import pytest

from landscout.sources import cadastre_fr
from landscout.sources.cadastre_fr import (
    CadastreDownloadError,
    _is_valid_gzip,
    build_cadastre_parcelles_url,
    download_cadastre_parcelles,
)

COMMUNE_CODE = "31395"
EXPECTED_URL = (
    "https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes/"
    "31/31395/cadastre-31395-parcelles.json.gz"
)
ARCHIVE_CONTENT = gzip.compress(b'{"type":"FeatureCollection","features":[]}')
REFRESHED_ARCHIVE_CONTENT = gzip.compress(
    b'{"type":"FeatureCollection","features":[{"type":"Feature"}]}'
)
CORRUPTED_ARCHIVE_CONTENT = ARCHIVE_CONTENT[:-8]


def _set_cache_age(metadata_path: Path, age: timedelta) -> None:
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    metadata["download_timestamp"] = (datetime.now(UTC) - age).isoformat()
    metadata_path.write_text(json.dumps(metadata), encoding="utf-8")


def _update_metadata_integrity(metadata_path: Path, archive_path: Path) -> None:
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    content = archive_path.read_bytes()
    metadata["file_size"] = len(content)
    metadata["sha256"] = sha256(content).hexdigest()
    metadata_path.write_text(json.dumps(metadata), encoding="utf-8")


def test_build_cadastre_parcelles_url() -> None:
    assert build_cadastre_parcelles_url(COMMUNE_CODE) == EXPECTED_URL


def test_successful_download(tmp_path: Path) -> None:
    with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        return_value=io.BytesIO(ARCHIVE_CONTENT),
    ):
        result = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert result.path.read_bytes() == ARCHIVE_CONTENT
    assert result.commune_code == COMMUNE_CODE
    assert result.source_url == EXPECTED_URL
    assert result.file_size == len(ARCHIVE_CONTENT)
    assert result.cache_hit is False
    metadata_path = tmp_path / f"{result.filename}.metadata.json"
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    assert metadata["schema_version"] == 1
    assert metadata["commune_code"] == COMMUNE_CODE
    assert metadata["download_timestamp"] == result.download_timestamp


def test_fresh_cache_is_reused(tmp_path: Path) -> None:
    with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        return_value=io.BytesIO(ARCHIVE_CONTENT),
    ) as opener:
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
        second = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert opener.call_count == 1
    assert first.cache_hit is False
    assert second.cache_hit is True
    assert second.sha256 == first.sha256
    assert second.download_timestamp == first.download_timestamp


def test_expired_cache_is_downloaded_again(tmp_path: Path) -> None:
    with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        side_effect=[
            io.BytesIO(ARCHIVE_CONTENT),
            io.BytesIO(REFRESHED_ARCHIVE_CONTENT),
        ],
    ) as opener:
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
        metadata_path = tmp_path / f"{first.filename}.metadata.json"
        _set_cache_age(metadata_path, timedelta(hours=169))
        refreshed = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert opener.call_count == 2
    assert refreshed.cache_hit is False
    assert refreshed.path.read_bytes() == REFRESHED_ARCHIVE_CONTENT
    assert refreshed.sha256 == sha256(REFRESHED_ARCHIVE_CONTENT).hexdigest()


def test_failed_refresh_preserves_cached_archive(tmp_path: Path) -> None:
    with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        return_value=io.BytesIO(ARCHIVE_CONTENT),
    ):
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    original_archive = first.path.read_bytes()
    metadata_path = tmp_path / f"{first.filename}.metadata.json"
    _set_cache_age(metadata_path, timedelta(hours=169))
    error = HTTPError(EXPECTED_URL, 503, "Unavailable", hdrs=None, fp=None)

    with (
        patch("landscout.sources.cadastre_fr.open_safe_https", side_effect=error),
        pytest.raises(CadastreDownloadError),
    ):
        download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert first.path.read_bytes() == original_archive
    assert metadata_path.is_file()


def test_failed_http_response(tmp_path: Path) -> None:
    error = HTTPError(EXPECTED_URL, 404, "Not Found", hdrs=None, fp=None)

    with (
        patch("landscout.sources.cadastre_fr.open_safe_https", side_effect=error),
        pytest.raises(CadastreDownloadError),
    ):
        download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert not list(tmp_path.glob("*"))


def test_checksum_generation(tmp_path: Path) -> None:
    with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        return_value=io.BytesIO(ARCHIVE_CONTENT),
    ):
        result = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert result.sha256 == sha256(ARCHIVE_CONTENT).hexdigest()


def test_valid_gzip_is_accepted(tmp_path: Path) -> None:
    archive_path = tmp_path / "valid.json.gz"
    archive_path.write_bytes(ARCHIVE_CONTENT)

    assert _is_valid_gzip(archive_path)


def test_truncated_gzip_is_rejected(tmp_path: Path) -> None:
    archive_path = tmp_path / "truncated.json.gz"
    archive_path.write_bytes(CORRUPTED_ARCHIVE_CONTENT)

    assert not _is_valid_gzip(archive_path)


def test_corrupted_cached_archive_triggers_fresh_download(tmp_path: Path) -> None:
    with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        side_effect=[
            io.BytesIO(ARCHIVE_CONTENT),
            io.BytesIO(REFRESHED_ARCHIVE_CONTENT),
        ],
    ) as opener:
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
        metadata_path = tmp_path / f"{first.filename}.metadata.json"
        first.path.write_bytes(CORRUPTED_ARCHIVE_CONTENT)
        _update_metadata_integrity(metadata_path, first.path)
        refreshed = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert opener.call_count == 2
    assert refreshed.cache_hit is False
    assert refreshed.path.read_bytes() == REFRESHED_ARCHIVE_CONTENT


def test_corrupted_new_download_preserves_existing_archive(tmp_path: Path) -> None:
    with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        return_value=io.BytesIO(ARCHIVE_CONTENT),
    ):
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    original_archive = first.path.read_bytes()
    metadata_path = tmp_path / f"{first.filename}.metadata.json"
    _set_cache_age(metadata_path, timedelta(hours=169))

    with (
        patch(
            "landscout.sources.cadastre_fr.open_safe_https",
            return_value=io.BytesIO(CORRUPTED_ARCHIVE_CONTENT),
        ),
        pytest.raises(CadastreDownloadError),
    ):
        download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert first.path.read_bytes() == original_archive
    assert not list(tmp_path.glob("*.part"))


@pytest.mark.parametrize(
    ("code", "department"),
    [("2A004", "2A"), ("2B033", "2B")],
)
def test_corsica_cadastre_urls_are_canonical(code: str, department: str) -> None:
    url = build_cadastre_parcelles_url(code)

    assert f"/{department}/{code}/cadastre-{code}-parcelles.json.gz" in url


@pytest.mark.parametrize("code", [31395, "2a004", " 31395 ", "ABCDE"])
def test_noncanonical_commune_code_is_controlled(code: object) -> None:
    with pytest.raises((TypeError, ValueError), match="Commune code"):
        build_cadastre_parcelles_url(code)  # type: ignore[arg-type]


@pytest.mark.parametrize(
    "timeout",
    [0, -1, float("nan"), float("inf"), "60", True],
)
def test_download_timeout_is_strict_finite_positive(
    tmp_path: Path,
    timeout: object,
) -> None:
    with pytest.raises(ValueError, match="timeout"):
        download_cadastre_parcelles(
            COMMUNE_CODE,
            tmp_path,
            timeout=timeout,  # type: ignore[arg-type]
        )


@pytest.mark.parametrize(
    "max_age",
    [-1, float("nan"), float("inf"), "168", True],
)
def test_cache_age_is_strict_finite_nonnegative(
    tmp_path: Path,
    max_age: object,
) -> None:
    with pytest.raises(ValueError, match="max_cache_age_hours"):
        download_cadastre_parcelles(
            COMMUNE_CODE,
            tmp_path,
            max_cache_age_hours=max_age,  # type: ignore[arg-type]
        )


@pytest.mark.parametrize("field", ["file_size", "sha256", "download_timestamp"])
def test_malformed_cached_metadata_triggers_refresh(
    tmp_path: Path,
    field: str,
) -> None:
    with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        side_effect=[
            io.BytesIO(ARCHIVE_CONTENT),
            io.BytesIO(REFRESHED_ARCHIVE_CONTENT),
        ],
    ) as opener:
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
        metadata_path = tmp_path / f"{first.filename}.metadata.json"
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        metadata[field] = {
            "file_size": first.file_size + 1,
            "sha256": "0" * 64,
            "download_timestamp": "not-a-timestamp",
        }[field]
        metadata_path.write_text(json.dumps(metadata), encoding="utf-8")
        refreshed = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert opener.call_count == 2
    assert refreshed.path.read_bytes() == REFRESHED_ARCHIVE_CONTENT


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("schema_version", True),
        ("schema_version", 1.0),
        ("file_size", True),
        ("file_size", 1.0),
        ("file_size", "1"),
    ],
)
def test_cache_metadata_schema_and_size_are_strict_integers(
    tmp_path: Path,
    field: str,
    value: object,
) -> None:
    with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        side_effect=[
            io.BytesIO(ARCHIVE_CONTENT),
            io.BytesIO(REFRESHED_ARCHIVE_CONTENT),
        ],
    ) as opener:
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
        metadata_path = tmp_path / f"{first.filename}.metadata.json"
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        metadata[field] = value
        metadata_path.write_text(json.dumps(metadata), encoding="utf-8")
        refreshed = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert opener.call_count == 2
    assert refreshed.cache_hit is False


def test_future_cached_timestamp_triggers_refresh(tmp_path: Path) -> None:
    with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        side_effect=[
            io.BytesIO(ARCHIVE_CONTENT),
            io.BytesIO(REFRESHED_ARCHIVE_CONTENT),
        ],
    ) as opener:
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
        metadata_path = tmp_path / f"{first.filename}.metadata.json"
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        metadata["download_timestamp"] = (
            datetime.now(UTC) + timedelta(hours=1)
        ).isoformat()
        metadata_path.write_text(json.dumps(metadata), encoding="utf-8")
        refreshed = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert opener.call_count == 2
    assert refreshed.path.read_bytes() == REFRESHED_ARCHIVE_CONTENT


@pytest.mark.parametrize(
    "invalid_metadata",
    [
        '{"schema_version":1,"schema_version":1}',
        '{"schema_version":1,"file_size":NaN}',
        "[]",
    ],
)
def test_strict_cadastre_cache_json_never_returns_a_cache_hit(
    tmp_path: Path,
    invalid_metadata: str,
) -> None:
    with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        side_effect=[
            io.BytesIO(ARCHIVE_CONTENT),
            io.BytesIO(REFRESHED_ARCHIVE_CONTENT),
        ],
    ) as opener:
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
        metadata_path = tmp_path / f"{first.filename}.metadata.json"
        metadata_path.write_text(invalid_metadata, encoding="utf-8")
        refreshed = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert opener.call_count == 2
    assert refreshed.cache_hit is False


def test_metadata_publication_failure_restores_previous_cache_pair(
    tmp_path: Path,
) -> None:
    with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        return_value=io.BytesIO(ARCHIVE_CONTENT),
    ):
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
    metadata_path = tmp_path / f"{first.filename}.metadata.json"
    _set_cache_age(metadata_path, timedelta(hours=169))
    archive_before = first.path.read_bytes()
    metadata_before = metadata_path.read_bytes()
    temporary_metadata = metadata_path.with_suffix(f"{metadata_path.suffix}.part")
    original_replace = __import__(
        "landscout.sources.cadastre_fr",
        fromlist=["_replace_file"],
    )._replace_file

    def fail_metadata_publication(source: Path, target: Path) -> None:
        if source == temporary_metadata and target == metadata_path:
            raise OSError("simulated metadata publication failure")
        original_replace(source, target)

    with (
        patch(
            "landscout.sources.cadastre_fr.open_safe_https",
            return_value=io.BytesIO(REFRESHED_ARCHIVE_CONTENT),
        ),
        patch(
            "landscout.sources.cadastre_fr._replace_file",
            side_effect=fail_metadata_publication,
        ),
        pytest.raises(CadastreDownloadError, match="publication"),
    ):
        download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert first.path.read_bytes() == archive_before
    assert metadata_path.read_bytes() == metadata_before
    assert not list(tmp_path.glob("*.part"))
    assert not list(tmp_path.glob("*.bak"))


def test_first_metadata_publication_failure_leaves_no_half_pair(
    tmp_path: Path,
) -> None:
    expected_path = tmp_path / "cadastre-31395-parcelles.json.gz"
    metadata_path = tmp_path / f"{expected_path.name}.metadata.json"
    temporary_metadata = metadata_path.with_suffix(f"{metadata_path.suffix}.part")
    original_replace = __import__(
        "landscout.sources.cadastre_fr",
        fromlist=["_replace_file"],
    )._replace_file

    def fail_metadata_publication(source: Path, target: Path) -> None:
        if source == temporary_metadata and target == metadata_path:
            raise OSError("simulated metadata publication failure")
        original_replace(source, target)

    with (
        patch(
            "landscout.sources.cadastre_fr.open_safe_https",
            return_value=io.BytesIO(ARCHIVE_CONTENT),
        ),
        patch(
            "landscout.sources.cadastre_fr._replace_file",
            side_effect=fail_metadata_publication,
        ),
        pytest.raises(CadastreDownloadError, match="publication"),
    ):
        download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert not expected_path.exists()
    assert not metadata_path.exists()
    assert not list(tmp_path.glob("*.part"))
    assert not list(tmp_path.glob("*.bak"))


@pytest.mark.parametrize("rollback_target", ["archive", "metadata"])
def test_publication_and_rollback_failure_preserves_recovery_backup(
    tmp_path: Path,
    rollback_target: str,
) -> None:
    with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        return_value=io.BytesIO(ARCHIVE_CONTENT),
    ):
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
    metadata_path = tmp_path / f"{first.filename}.metadata.json"
    _set_cache_age(metadata_path, timedelta(hours=169))
    archive_backup = first.path.with_suffix(f"{first.path.suffix}.bak")
    metadata_backup = metadata_path.with_suffix(f"{metadata_path.suffix}.bak")
    temporary_metadata = metadata_path.with_suffix(f"{metadata_path.suffix}.part")
    original_replace = cadastre_fr._replace_file

    def fail_publication_and_rollback(source: Path, target: Path) -> None:
        if source == temporary_metadata and target == metadata_path:
            raise OSError("publication failure")
        if rollback_target == "archive" and source == archive_backup:
            raise OSError("archive rollback failure")
        if rollback_target == "metadata" and source == metadata_backup:
            raise OSError("metadata rollback failure")
        original_replace(source, target)

    with (
        patch(
            "landscout.sources.cadastre_fr.open_safe_https",
            return_value=io.BytesIO(REFRESHED_ARCHIVE_CONTENT),
        ),
        patch.object(
            cadastre_fr,
            "_replace_file",
            side_effect=fail_publication_and_rollback,
        ),
        pytest.raises(CadastreDownloadError, match="rollback"),
    ):
        download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    useful_backups = [
        path for path in (archive_backup, metadata_backup) if path.exists()
    ]
    assert useful_backups


def test_stale_recovery_backup_rejects_cache_before_network_and_preserves_bytes(
    tmp_path: Path,
) -> None:
    with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        return_value=io.BytesIO(ARCHIVE_CONTENT),
    ):
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
    recovery_path = first.path.with_suffix(f"{first.path.suffix}.bak")
    recovery_bytes = b"manual cadastre recovery material"
    recovery_path.write_bytes(recovery_bytes)

    with (
        patch(
            "landscout.sources.cadastre_fr.open_safe_https",
            side_effect=AssertionError("recovery state must fail before network"),
        ) as opener,
        pytest.raises(CadastreDownloadError, match="backup|recovery|manual"),
    ):
        download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    opener.assert_not_called()
    assert recovery_path.read_bytes() == recovery_bytes
    assert first.path.read_bytes() == ARCHIVE_CONTENT


def test_next_run_after_double_failure_preserves_recovery_before_network(
    tmp_path: Path,
) -> None:
    with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        return_value=io.BytesIO(ARCHIVE_CONTENT),
    ):
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
    metadata_path = tmp_path / f"{first.filename}.metadata.json"
    _set_cache_age(metadata_path, timedelta(hours=169))
    old_archive = first.path.read_bytes()
    old_metadata = metadata_path.read_bytes()
    temporary_metadata = metadata_path.with_suffix(f"{metadata_path.suffix}.part")
    archive_backup = first.path.with_suffix(f"{first.path.suffix}.bak")
    metadata_backup = metadata_path.with_suffix(f"{metadata_path.suffix}.bak")
    original_replace = cadastre_fr._replace_file

    def fail_publication_and_rollback(source: Path, target: Path) -> None:
        if source == temporary_metadata and target == metadata_path:
            raise OSError("publication failed")
        if source == archive_backup and target == first.path:
            raise OSError("rollback failed")
        original_replace(source, target)

    with (
        patch(
            "landscout.sources.cadastre_fr.open_safe_https",
            return_value=io.BytesIO(REFRESHED_ARCHIVE_CONTENT),
        ),
        patch.object(
            cadastre_fr,
            "_replace_file",
            side_effect=fail_publication_and_rollback,
        ),
        pytest.raises(CadastreDownloadError, match="rollback"),
    ):
        download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert archive_backup.read_bytes() == old_archive
    assert metadata_backup.read_bytes() == old_metadata
    archive_recovery = archive_backup.read_bytes()
    metadata_recovery = metadata_backup.read_bytes()

    with (
        patch(
            "landscout.sources.cadastre_fr.open_safe_https",
            side_effect=AssertionError("recovery state must fail before network"),
        ) as opener,
        pytest.raises(CadastreDownloadError, match="backup|recovery|manual"),
    ):
        download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    opener.assert_not_called()
    assert archive_backup.read_bytes() == archive_recovery
    assert metadata_backup.read_bytes() == metadata_recovery


@pytest.mark.parametrize("temporary_role", ["archive", "metadata"])
@pytest.mark.parametrize("link_kind", ["symlink", "junction"])
def test_temporary_link_or_junction_cannot_modify_target_before_network(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    temporary_role: str,
    link_kind: str,
) -> None:
    archive_path = tmp_path / "cadastre-31395-parcelles.json.gz"
    metadata_path = tmp_path / f"{archive_path.name}.metadata.json"
    temporary_paths = {
        "archive": archive_path.with_suffix(f"{archive_path.suffix}.part"),
        "metadata": metadata_path.with_suffix(f"{metadata_path.suffix}.part"),
    }
    unsafe_path = temporary_paths[temporary_role]
    sentinel = tmp_path / "do-not-overwrite.txt"
    sentinel_bytes = b"irreplaceable cadastre sentinel"
    sentinel.write_bytes(sentinel_bytes)
    original_is_symlink = Path.is_symlink
    original_is_junction = Path.is_junction
    original_open = Path.open

    def simulated_is_symlink(path: Path) -> bool:
        return (link_kind == "symlink" and path == unsafe_path) or original_is_symlink(
            path
        )

    def simulated_is_junction(path: Path) -> bool:
        return (
            link_kind == "junction" and path == unsafe_path
        ) or original_is_junction(path)

    def simulated_symlink_open(path: Path, *args: object, **kwargs: object) -> object:
        if path == unsafe_path:
            return original_open(sentinel, *args, **kwargs)
        return original_open(path, *args, **kwargs)

    network_calls = 0

    def record_network(*args: object, **kwargs: object) -> io.BytesIO:
        nonlocal network_calls
        network_calls += 1
        return io.BytesIO(ARCHIVE_CONTENT)

    monkeypatch.setattr(Path, "is_symlink", simulated_is_symlink)
    monkeypatch.setattr(Path, "is_junction", simulated_is_junction)
    monkeypatch.setattr(Path, "open", simulated_symlink_open)
    monkeypatch.setattr(cadastre_fr, "open_safe_https", record_network)

    with pytest.raises(CadastreDownloadError, match="temporary|link|cache"):
        download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert network_calls == 0
    assert sentinel.read_bytes() == sentinel_bytes


def test_broken_recovery_symlink_is_rejected_before_network(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    archive_path = tmp_path / "cadastre-31395-parcelles.json.gz"
    recovery_path = archive_path.with_suffix(f"{archive_path.suffix}.bak")
    original_is_symlink = Path.is_symlink

    def simulated_is_symlink(path: Path) -> bool:
        return path == recovery_path or original_is_symlink(path)

    network_calls = 0

    def fail_network(*args: object, **kwargs: object) -> io.BytesIO:
        nonlocal network_calls
        network_calls += 1
        raise AssertionError("broken recovery link must fail before network")

    monkeypatch.setattr(Path, "is_symlink", simulated_is_symlink)
    monkeypatch.setattr(cadastre_fr, "open_safe_https", fail_network)

    with pytest.raises(CadastreDownloadError, match="backup|recovery|manual"):
        download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert network_calls == 0


def test_cleanup_failure_does_not_mask_double_failure_recovery_error(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        return_value=io.BytesIO(ARCHIVE_CONTENT),
    ):
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
    metadata_path = tmp_path / f"{first.filename}.metadata.json"
    _set_cache_age(metadata_path, timedelta(hours=169))
    old_archive = first.path.read_bytes()
    old_metadata = metadata_path.read_bytes()
    temporary_metadata = metadata_path.with_suffix(f"{metadata_path.suffix}.part")
    archive_backup = first.path.with_suffix(f"{first.path.suffix}.bak")
    metadata_backup = metadata_path.with_suffix(f"{metadata_path.suffix}.bak")
    original_replace = cadastre_fr._replace_file
    original_unlink = Path.unlink
    rollback_failed = False

    def fail_publication_and_rollback(source: Path, target: Path) -> None:
        nonlocal rollback_failed
        if source == temporary_metadata and target == metadata_path:
            raise OSError("publication failed")
        if source == archive_backup and target == first.path:
            rollback_failed = True
            raise OSError("rollback failed")
        original_replace(source, target)

    def fail_temporary_cleanup(path: Path, *, missing_ok: bool = False) -> None:
        if rollback_failed and path == temporary_metadata:
            raise PermissionError("temporary cleanup failed")
        original_unlink(path, missing_ok=missing_ok)

    monkeypatch.setattr(
        cadastre_fr,
        "open_safe_https",
        lambda *args, **kwargs: io.BytesIO(REFRESHED_ARCHIVE_CONTENT),
    )
    monkeypatch.setattr(cadastre_fr, "_replace_file", fail_publication_and_rollback)
    monkeypatch.setattr(Path, "unlink", fail_temporary_cleanup)

    with pytest.raises(CadastreDownloadError, match="rollback"):
        download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert archive_backup.read_bytes() == old_archive
    assert metadata_backup.read_bytes() == old_metadata
```

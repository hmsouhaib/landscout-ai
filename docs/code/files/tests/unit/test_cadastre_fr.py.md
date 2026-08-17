# `tests/unit/test_cadastre_fr.py`

## File identity

- Repository path: `tests/unit/test_cadastre_fr.py`
- File type: Python test
- Layer: unit/regression test
- Domain: test
- Responsibility: Provides complete unit and regression coverage for the `cadastre_fr` contracts exercised in this file.
- Source SHA256: `07f5bc37cf8d7fca0fa8c1a88ab19528c0717139d5a581d52c1fe20644d74eb5`

## 1. Purpose

Provides complete unit and regression coverage for the `cadastre_fr` contracts exercised in this file.

## 2. Position in LandScout architecture

This file belongs to the **unit/regression test** layer and the **test** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

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

### A. Python constants

#### `COMMUNE_CODE`

```python
COMMUNE_CODE = "31395"
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_cadastre_fr.py::test_build_cadastre_parcelles_url` (value argument/reference), `tests/unit/test_cadastre_fr.py::test_successful_download` (value argument/reference), `tests/unit/test_cadastre_fr.py::test_fresh_cache_is_reused` (value argument/reference), `tests/unit/test_cadastre_fr.py::test_expired_cache_is_downloaded_again` (value argument/reference), `tests/unit/test_cadastre_fr.py::test_failed_refresh_preserves_cached_archive` (value argument/reference), `tests/unit/test_cadastre_fr.py::test_failed_http_response` (value argument/reference), `tests/unit/test_cadastre_fr.py::test_checksum_generation` (value argument/reference), `tests/unit/test_cadastre_fr.py::test_corrupted_cached_archive_triggers_fresh_download` (value argument/reference), `tests/unit/test_cadastre_fr.py::test_corrupted_new_download_preserves_existing_archive` (value argument/reference), `tests/unit/test_cadastre_fr.py::test_download_timeout_is_strict_finite_positive` (value argument/reference), `tests/unit/test_cadastre_fr.py::test_cache_age_is_strict_finite_nonnegative` (value argument/reference), `tests/unit/test_cadastre_fr.py::test_malformed_cached_metadata_triggers_refresh` (value argument/reference), `tests/unit/test_cadastre_fr.py::test_future_cached_timestamp_triggers_refresh` (value argument/reference), `tests/unit/test_cadastre_fr.py::test_metadata_publication_failure_restores_previous_cache_pair` (value argument/reference), `tests/unit/test_cadastre_fr.py::test_first_metadata_publication_failure_leaves_no_half_pair` (value argument/reference), `tests/unit/test_cadastre_fr.py::test_publication_and_rollback_failure_preserves_recovery_backup` (value argument/reference), `tests/unit/test_cadastre_fr.py::test_stale_recovery_backup_rejects_cache_before_network_and_preserves_bytes` (value argument/reference), `tests/unit/test_cadastre_fr.py::test_next_run_after_double_failure_preserves_recovery_before_network` (value argument/reference), `tests/unit/test_cadastre_fr.py::test_temporary_link_or_junction_cannot_modify_target_before_network` (value argument/reference), `tests/unit/test_cadastre_fr.py::test_broken_recovery_symlink_is_rejected_before_network` (value argument/reference).

#### `EXPECTED_URL`

```python
EXPECTED_URL = (
    "https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes/"
    "31/31395/cadastre-31395-parcelles.json.gz"
)
```

Configured/constructed URL component or origin constraint; it is textual identity until the transport/source validator proves bytes. Consumers include `tests/unit/test_cadastre_fr.py::test_failed_refresh_preserves_cached_archive` (value argument/reference), `tests/unit/test_cadastre_fr.py::test_failed_http_response` (value argument/reference).

#### `ARCHIVE_CONTENT`

```python
ARCHIVE_CONTENT = gzip.compress(b'{"type":"FeatureCollection","features":[]}')
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_cadastre_fr.py::test_successful_download` (value argument/reference), `tests/unit/test_cadastre_fr.py::test_successful_download` (value argument/reference), `tests/unit/test_cadastre_fr.py::test_fresh_cache_is_reused` (value argument/reference), `tests/unit/test_cadastre_fr.py::test_expired_cache_is_downloaded_again` (value argument/reference), `tests/unit/test_cadastre_fr.py::test_failed_refresh_preserves_cached_archive` (value argument/reference), `tests/unit/test_cadastre_fr.py::test_checksum_generation` (value argument/reference), `tests/unit/test_cadastre_fr.py::test_checksum_generation` (value argument/reference), `tests/unit/test_cadastre_fr.py::test_valid_gzip_is_accepted` (value argument/reference), `tests/unit/test_cadastre_fr.py::test_corrupted_cached_archive_triggers_fresh_download` (value argument/reference), `tests/unit/test_cadastre_fr.py::test_corrupted_new_download_preserves_existing_archive` (value argument/reference), `tests/unit/test_cadastre_fr.py::test_malformed_cached_metadata_triggers_refresh` (value argument/reference), `tests/unit/test_cadastre_fr.py::test_future_cached_timestamp_triggers_refresh` (value argument/reference), `tests/unit/test_cadastre_fr.py::test_metadata_publication_failure_restores_previous_cache_pair` (value argument/reference), `tests/unit/test_cadastre_fr.py::test_first_metadata_publication_failure_leaves_no_half_pair` (value argument/reference), `tests/unit/test_cadastre_fr.py::test_publication_and_rollback_failure_preserves_recovery_backup` (value argument/reference), `tests/unit/test_cadastre_fr.py::test_stale_recovery_backup_rejects_cache_before_network_and_preserves_bytes` (value argument/reference), `tests/unit/test_cadastre_fr.py::test_next_run_after_double_failure_preserves_recovery_before_network` (value argument/reference), `tests/unit/test_cadastre_fr.py::test_temporary_link_or_junction_cannot_modify_target_before_network.record_network` (value argument/reference), `tests/unit/test_cadastre_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` (value argument/reference).

#### `REFRESHED_ARCHIVE_CONTENT`

```python
REFRESHED_ARCHIVE_CONTENT = gzip.compress(
    b'{"type":"FeatureCollection","features":[{"type":"Feature"}]}'
)
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_cadastre_fr.py::test_expired_cache_is_downloaded_again` (value argument/reference), `tests/unit/test_cadastre_fr.py::test_expired_cache_is_downloaded_again` (value argument/reference), `tests/unit/test_cadastre_fr.py::test_corrupted_cached_archive_triggers_fresh_download` (value argument/reference), `tests/unit/test_cadastre_fr.py::test_malformed_cached_metadata_triggers_refresh` (value argument/reference), `tests/unit/test_cadastre_fr.py::test_future_cached_timestamp_triggers_refresh` (value argument/reference), `tests/unit/test_cadastre_fr.py::test_metadata_publication_failure_restores_previous_cache_pair` (value argument/reference), `tests/unit/test_cadastre_fr.py::test_publication_and_rollback_failure_preserves_recovery_backup` (value argument/reference), `tests/unit/test_cadastre_fr.py::test_next_run_after_double_failure_preserves_recovery_before_network` (value argument/reference), `tests/unit/test_cadastre_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` (value argument/reference).

#### `CORRUPTED_ARCHIVE_CONTENT`

```python
CORRUPTED_ARCHIVE_CONTENT = ARCHIVE_CONTENT[:-8]
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_cadastre_fr.py::test_truncated_gzip_is_rejected` (value argument/reference), `tests/unit/test_cadastre_fr.py::test_corrupted_cached_archive_triggers_fresh_download` (value argument/reference), `tests/unit/test_cadastre_fr.py::test_corrupted_new_download_preserves_existing_archive` (value argument/reference).


### B. Type aliases and closed domains

No module-level Literal/Annotated/TypeAlias declaration is present.

### C. Meaningful dunder contracts

No meaningful module-level dunder contract is declared.

### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

No class/model/dataclass is declared.

## 6. Functions and methods

### `_set_cache_age`

**Exact signature**

```python
def _set_cache_age(metadata_path: Path, age: timedelta) -> None:
```

**Purpose**

Private `test` helper for set cache age; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: `metadata_path.read_text`.
- Filesystem write: `metadata_path.write_text`.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: `metadata['download_timestamp']`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_cadastre_fr.py::test_expired_cache_is_downloaded_again` via `_set_cache_age`.
- direct call or construction: `tests/unit/test_cadastre_fr.py::test_failed_refresh_preserves_cached_archive` via `_set_cache_age`.
- direct call or construction: `tests/unit/test_cadastre_fr.py::test_corrupted_new_download_preserves_existing_archive` via `_set_cache_age`.
- direct call or construction: `tests/unit/test_cadastre_fr.py::test_metadata_publication_failure_restores_previous_cache_pair` via `_set_cache_age`.
- direct call or construction: `tests/unit/test_cadastre_fr.py::test_publication_and_rollback_failure_preserves_recovery_backup` via `_set_cache_age`.
- direct call or construction: `tests/unit/test_cadastre_fr.py::test_next_run_after_double_failure_preserves_recovery_before_network` via `_set_cache_age`.
- direct call or construction: `tests/unit/test_cadastre_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `_set_cache_age`.

**Complete source-ordered implementation**

```python
def _set_cache_age(metadata_path: Path, age: timedelta) -> None:
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    metadata["download_timestamp"] = (datetime.now(UTC) - age).isoformat()
    metadata_path.write_text(json.dumps(metadata), encoding="utf-8")
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_update_metadata_integrity`

**Exact signature**

```python
def _update_metadata_integrity(metadata_path: Path, archive_path: Path) -> None:
```

**Purpose**

Private `test` helper for update metadata integrity; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: `archive_path.read_bytes`, `metadata_path.read_text`.
- Filesystem write: `metadata_path.write_text`.
- CRS/geometry calculation: none directly visible.
- Hashing: `sha256`, `sha256(content).hexdigest`.
- Environment/process effects: none directly visible.
- In-memory mutation: `metadata['file_size']`, `metadata['sha256']`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_cadastre_fr.py::test_corrupted_cached_archive_triggers_fresh_download` via `_update_metadata_integrity`.

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

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_build_cadastre_parcelles_url`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

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
assert build_cadastre_parcelles_url(COMMUNE_CODE) == EXPECTED_URL
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_build_cadastre_parcelles_url() -> None:
    assert build_cadastre_parcelles_url(COMMUNE_CODE) == EXPECTED_URL
```

### `test_successful_download`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
metadata_path = tmp_path / f"{result.filename}.metadata.json"
metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
```

**Action**

```python
with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        return_value=io.BytesIO(ARCHIVE_CONTENT),
    ):
        result = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
```

**Expected result**

```python
assert result.path.read_bytes() == ARCHIVE_CONTENT
assert result.source_url == EXPECTED_URL
assert result.file_size == len(ARCHIVE_CONTENT)
assert result.cache_hit is False
assert metadata["download_timestamp"] == result.download_timestamp
```

**Regression protected**

Pins verified cache reuse and ensures the successful local path avoids the external operation asserted by the test.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_successful_download(tmp_path: Path) -> None:
    with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        return_value=io.BytesIO(ARCHIVE_CONTENT),
    ):
        result = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert result.path.read_bytes() == ARCHIVE_CONTENT
    assert result.source_url == EXPECTED_URL
    assert result.file_size == len(ARCHIVE_CONTENT)
    assert result.cache_hit is False
    metadata_path = tmp_path / f"{result.filename}.metadata.json"
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    assert metadata["download_timestamp"] == result.download_timestamp
```

### `test_fresh_cache_is_reused`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        return_value=io.BytesIO(ARCHIVE_CONTENT),
    ) as opener:
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
        second = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
```

**Expected result**

```python
assert opener.call_count == 1
assert first.cache_hit is False
assert second.cache_hit is True
assert second.sha256 == first.sha256
assert second.download_timestamp == first.download_timestamp
```

**Regression protected**

Pins verified cache reuse and ensures the successful local path avoids the external operation asserted by the test.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

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

### `test_expired_cache_is_downloaded_again`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        side_effect=[io.BytesIO(ARCHIVE_CONTENT), io.BytesIO(REFRESHED_ARCHIVE_CONTENT)],
    ) as opener:
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
        metadata_path = tmp_path / f"{first.filename}.metadata.json"
        _set_cache_age(metadata_path, timedelta(hours=169))
        refreshed = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
```

**Expected result**

```python
assert opener.call_count == 2
assert refreshed.cache_hit is False
assert refreshed.path.read_bytes() == REFRESHED_ARCHIVE_CONTENT
assert refreshed.sha256 == sha256(REFRESHED_ARCHIVE_CONTENT).hexdigest()
```

**Regression protected**

Pins verified cache reuse and ensures the successful local path avoids the external operation asserted by the test.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_expired_cache_is_downloaded_again(tmp_path: Path) -> None:
    with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        side_effect=[io.BytesIO(ARCHIVE_CONTENT), io.BytesIO(REFRESHED_ARCHIVE_CONTENT)],
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

### `test_failed_refresh_preserves_cached_archive`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
original_archive = first.path.read_bytes()
metadata_path = tmp_path / f"{first.filename}.metadata.json"
_set_cache_age(metadata_path, timedelta(hours=169))
error = HTTPError(EXPECTED_URL, 503, "Unavailable", hdrs=None, fp=None)
```

**Action**

```python
with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        return_value=io.BytesIO(ARCHIVE_CONTENT),
    ):
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
```

**Expected result**

```python
with (
        patch("landscout.sources.cadastre_fr.open_safe_https", side_effect=error),
        pytest.raises(CadastreDownloadError),
    ):
        download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
assert first.path.read_bytes() == original_archive
assert metadata_path.is_file()
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

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

### `test_failed_http_response`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
error = HTTPError(EXPECTED_URL, 404, "Not Found", hdrs=None, fp=None)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with (
        patch("landscout.sources.cadastre_fr.open_safe_https", side_effect=error),
        pytest.raises(CadastreDownloadError),
    ):
        download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
assert not list(tmp_path.glob("*"))
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

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

### `test_checksum_generation`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        return_value=io.BytesIO(ARCHIVE_CONTENT),
    ):
        result = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
```

**Expected result**

```python
assert result.sha256 == sha256(ARCHIVE_CONTENT).hexdigest()
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_checksum_generation(tmp_path: Path) -> None:
    with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        return_value=io.BytesIO(ARCHIVE_CONTENT),
    ):
        result = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)

    assert result.sha256 == sha256(ARCHIVE_CONTENT).hexdigest()
```

### `test_valid_gzip_is_accepted`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
archive_path = tmp_path / "valid.json.gz"
archive_path.write_bytes(ARCHIVE_CONTENT)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert _is_valid_gzip(archive_path)
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_valid_gzip_is_accepted(tmp_path: Path) -> None:
    archive_path = tmp_path / "valid.json.gz"
    archive_path.write_bytes(ARCHIVE_CONTENT)

    assert _is_valid_gzip(archive_path)
```

### `test_truncated_gzip_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
archive_path = tmp_path / "truncated.json.gz"
archive_path.write_bytes(CORRUPTED_ARCHIVE_CONTENT)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert not _is_valid_gzip(archive_path)
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_truncated_gzip_is_rejected(tmp_path: Path) -> None:
    archive_path = tmp_path / "truncated.json.gz"
    archive_path.write_bytes(CORRUPTED_ARCHIVE_CONTENT)

    assert not _is_valid_gzip(archive_path)
```

### `test_corrupted_cached_archive_triggers_fresh_download`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        side_effect=[io.BytesIO(ARCHIVE_CONTENT), io.BytesIO(REFRESHED_ARCHIVE_CONTENT)],
    ) as opener:
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
        metadata_path = tmp_path / f"{first.filename}.metadata.json"
        first.path.write_bytes(CORRUPTED_ARCHIVE_CONTENT)
        _update_metadata_integrity(metadata_path, first.path)
        refreshed = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
```

**Expected result**

```python
assert opener.call_count == 2
assert refreshed.cache_hit is False
assert refreshed.path.read_bytes() == REFRESHED_ARCHIVE_CONTENT
```

**Regression protected**

Pins verified cache reuse and ensures the successful local path avoids the external operation asserted by the test.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_corrupted_cached_archive_triggers_fresh_download(tmp_path: Path) -> None:
    with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        side_effect=[io.BytesIO(ARCHIVE_CONTENT), io.BytesIO(REFRESHED_ARCHIVE_CONTENT)],
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

### `test_corrupted_new_download_preserves_existing_archive`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
original_archive = first.path.read_bytes()
metadata_path = tmp_path / f"{first.filename}.metadata.json"
_set_cache_age(metadata_path, timedelta(hours=169))
```

**Action**

```python
with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        return_value=io.BytesIO(ARCHIVE_CONTENT),
    ):
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
```

**Expected result**

```python
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

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

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

### `test_corsica_cadastre_urls_are_canonical`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `code`, `department`.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
url = build_cadastre_parcelles_url(code)
```

**Expected result**

```python
assert f"/{department}/{code}/cadastre-{code}-parcelles.json.gz" in url
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_corsica_cadastre_urls_are_canonical(code: str, department: str) -> None:
    url = build_cadastre_parcelles_url(code)

    assert f"/{department}/{code}/cadastre-{code}-parcelles.json.gz" in url
```

### `test_noncanonical_commune_code_is_controlled`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `code`.

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
with pytest.raises((TypeError, ValueError), match="Commune code"):
        build_cadastre_parcelles_url(code)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_noncanonical_commune_code_is_controlled(code: object) -> None:
    with pytest.raises((TypeError, ValueError), match="Commune code"):
        build_cadastre_parcelles_url(code)
```

### `test_download_timeout_is_strict_finite_positive`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
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
with pytest.raises(ValueError, match="timeout"):
        download_cadastre_parcelles(
            COMMUNE_CODE,
            tmp_path,
            timeout=timeout,  # type: ignore[arg-type]
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

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

### `test_cache_age_is_strict_finite_nonnegative`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `max_age`.

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
with pytest.raises(ValueError, match="max_cache_age_hours"):
        download_cadastre_parcelles(
            COMMUNE_CODE,
            tmp_path,
            max_cache_age_hours=max_age,  # type: ignore[arg-type]
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

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

### `test_malformed_cached_metadata_triggers_refresh`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `field`.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        side_effect=[io.BytesIO(ARCHIVE_CONTENT), io.BytesIO(REFRESHED_ARCHIVE_CONTENT)],
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
```

**Expected result**

```python
assert opener.call_count == 2
assert refreshed.path.read_bytes() == REFRESHED_ARCHIVE_CONTENT
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_malformed_cached_metadata_triggers_refresh(
    tmp_path: Path,
    field: str,
) -> None:
    with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        side_effect=[io.BytesIO(ARCHIVE_CONTENT), io.BytesIO(REFRESHED_ARCHIVE_CONTENT)],
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

### `test_future_cached_timestamp_triggers_refresh`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        side_effect=[io.BytesIO(ARCHIVE_CONTENT), io.BytesIO(REFRESHED_ARCHIVE_CONTENT)],
    ) as opener:
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
        metadata_path = tmp_path / f"{first.filename}.metadata.json"
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        metadata["download_timestamp"] = (
            datetime.now(UTC) + timedelta(hours=1)
        ).isoformat()
        metadata_path.write_text(json.dumps(metadata), encoding="utf-8")
        refreshed = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
```

**Expected result**

```python
assert opener.call_count == 2
assert refreshed.path.read_bytes() == REFRESHED_ARCHIVE_CONTENT
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_future_cached_timestamp_triggers_refresh(tmp_path: Path) -> None:
    with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        side_effect=[io.BytesIO(ARCHIVE_CONTENT), io.BytesIO(REFRESHED_ARCHIVE_CONTENT)],
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

### `test_metadata_publication_failure_restores_previous_cache_pair`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
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
```

**Action**

```python
with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        return_value=io.BytesIO(ARCHIVE_CONTENT),
    ):
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
```

**Expected result**

```python
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

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

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

### `test_metadata_publication_failure_restores_previous_cache_pair.fail_metadata_publication`

**Exact signature**

```python
def fail_metadata_publication(source: Path, target: Path) -> None:
```

**Purpose**

Private `test` helper for fail metadata publication; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `source == temporary_metadata and target == metadata_path`.
- Explicit raise expressions: `OSError('simulated metadata publication failure')`.

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

- callback/function object: `tests/unit/test_cadastre_fr.py::test_metadata_publication_failure_restores_previous_cache_pair` via `patch('landscout.sources.cadastre_fr._replace_file', side_effect=fail_metadata_publication)`.
- callback/function object: `tests/unit/test_cadastre_fr.py::test_first_metadata_publication_failure_leaves_no_half_pair` via `patch('landscout.sources.cadastre_fr._replace_file', side_effect=fail_metadata_publication)`.
- callback/function object: `tests/unit/test_ign_bdtopo_fr.py::test_metadata_publication_failure_restores_previous_cache_pair` via `patch.object(ign_bdtopo_fr, '_replace_file', side_effect=fail_metadata_publication)`.
- callback/function object: `tests/unit/test_rte_odre_fr.py::test_metadata_publication_failure_restores_previous_pair` via `patch.object(rte_odre_fr, '_replace_file', side_effect=fail_metadata_publication)`.

**Complete source-ordered implementation**

```python
def fail_metadata_publication(source: Path, target: Path) -> None:
        if source == temporary_metadata and target == metadata_path:
            raise OSError("simulated metadata publication failure")
        original_replace(source, target)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_first_metadata_publication_failure_leaves_no_half_pair`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
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
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
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

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

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

### `test_first_metadata_publication_failure_leaves_no_half_pair.fail_metadata_publication`

**Exact signature**

```python
def fail_metadata_publication(source: Path, target: Path) -> None:
```

**Purpose**

Private `test` helper for fail metadata publication; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `source == temporary_metadata and target == metadata_path`.
- Explicit raise expressions: `OSError('simulated metadata publication failure')`.

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

- callback/function object: `tests/unit/test_cadastre_fr.py::test_metadata_publication_failure_restores_previous_cache_pair` via `patch('landscout.sources.cadastre_fr._replace_file', side_effect=fail_metadata_publication)`.
- callback/function object: `tests/unit/test_cadastre_fr.py::test_first_metadata_publication_failure_leaves_no_half_pair` via `patch('landscout.sources.cadastre_fr._replace_file', side_effect=fail_metadata_publication)`.
- callback/function object: `tests/unit/test_ign_bdtopo_fr.py::test_metadata_publication_failure_restores_previous_cache_pair` via `patch.object(ign_bdtopo_fr, '_replace_file', side_effect=fail_metadata_publication)`.
- callback/function object: `tests/unit/test_rte_odre_fr.py::test_metadata_publication_failure_restores_previous_pair` via `patch.object(rte_odre_fr, '_replace_file', side_effect=fail_metadata_publication)`.

**Complete source-ordered implementation**

```python
def fail_metadata_publication(source: Path, target: Path) -> None:
        if source == temporary_metadata and target == metadata_path:
            raise OSError("simulated metadata publication failure")
        original_replace(source, target)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_publication_and_rollback_failure_preserves_recovery_backup`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `rollback_target`.

**Setup**

```python
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
useful_backups = [path for path in (archive_backup, metadata_backup) if path.exists()]
```

**Action**

```python
with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        return_value=io.BytesIO(ARCHIVE_CONTENT),
    ):
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
```

**Expected result**

```python
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
assert useful_backups
```

**Regression protected**

Prevents cache publication/rollback failures from destroying the last recoverable bytes; the exact old archive/metadata or extraction tree asserted below must survive in recovery material.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

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

    useful_backups = [path for path in (archive_backup, metadata_backup) if path.exists()]
    assert useful_backups
```

### `test_publication_and_rollback_failure_preserves_recovery_backup.fail_publication_and_rollback`

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

- Guard with a raise path: `source == temporary_metadata and target == metadata_path`.
- Guard with a raise path: `rollback_target == 'archive' and source == archive_backup`.
- Guard with a raise path: `rollback_target == 'metadata' and source == metadata_backup`.
- Explicit raise expressions: `OSError('archive rollback failure')`, `OSError('metadata rollback failure')`, `OSError('publication failure')`.

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

- callback/function object: `tests/unit/test_cadastre_fr.py::test_publication_and_rollback_failure_preserves_recovery_backup` via `patch.object(cadastre_fr, '_replace_file', side_effect=fail_publication_and_rollback)`.
- callback/function object: `tests/unit/test_cadastre_fr.py::test_next_run_after_double_failure_preserves_recovery_before_network` via `patch.object(cadastre_fr, '_replace_file', side_effect=fail_publication_and_rollback)`.
- callback/function object: `tests/unit/test_cadastre_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `monkeypatch.setattr(cadastre_fr, '_replace_file', fail_publication_and_rollback)`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_publication_and_rollback_failure_preserves_exact_recovery_backups` via `monkeypatch.setattr(gpu, '_replace_file', fail_publication_and_rollback)`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `monkeypatch.setattr(gpu, '_replace_file', fail_publication_and_rollback)`.
- callback/function object: `tests/unit/test_ign_bdtopo_fr.py::test_publication_and_rollback_failure_preserves_exact_recovery_backups` via `patch.object(ign_bdtopo_fr, '_replace_file', side_effect=fail_publication_and_rollback)`.
- callback/function object: `tests/unit/test_ign_bdtopo_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `patch.object(ign_bdtopo_fr, '_replace_file', side_effect=fail_publication_and_rollback)`.
- callback/function object: `tests/unit/test_inpn_protected_areas_fr.py::test_rollback_failure_preserves_recovery_material` via `monkeypatch.setattr(inpn, '_replace_file', fail_publication_and_rollback)`.
- callback/function object: `tests/unit/test_rte_odre_fr.py::test_double_failure_preserves_recovery_and_next_run_uses_zero_network` via `monkeypatch.setattr(rte_odre_fr, '_replace_file', fail_publication_and_rollback)`.
- callback/function object: `tests/unit/test_rte_odre_fr.py::test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error` via `monkeypatch.setattr(rte_odre_fr, '_replace_file', fail_publication_and_rollback)`.

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

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_stale_recovery_backup_rejects_cache_before_network_and_preserves_bytes`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
recovery_path = first.path.with_suffix(f"{first.path.suffix}.bak")
recovery_bytes = b"manual cadastre recovery material"
recovery_path.write_bytes(recovery_bytes)
opener.assert_not_called()
```

**Action**

```python
with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        return_value=io.BytesIO(ARCHIVE_CONTENT),
    ):
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
```

**Expected result**

```python
with (
        patch(
            "landscout.sources.cadastre_fr.open_safe_https",
            side_effect=AssertionError("recovery state must fail before network"),
        ) as opener,
        pytest.raises(CadastreDownloadError, match="backup|recovery|manual"),
    ):
        download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
assert recovery_path.read_bytes() == recovery_bytes
assert first.path.read_bytes() == ARCHIVE_CONTENT
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

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

### `test_next_run_after_double_failure_preserves_recovery_before_network`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
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
archive_recovery = archive_backup.read_bytes()
metadata_recovery = metadata_backup.read_bytes()
opener.assert_not_called()
```

**Action**

```python
with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        return_value=io.BytesIO(ARCHIVE_CONTENT),
    ):
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
```

**Expected result**

```python
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
with (
        patch(
            "landscout.sources.cadastre_fr.open_safe_https",
            side_effect=AssertionError("recovery state must fail before network"),
        ) as opener,
        pytest.raises(CadastreDownloadError, match="backup|recovery|manual"),
    ):
        download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
assert archive_backup.read_bytes() == archive_recovery
assert metadata_backup.read_bytes() == metadata_recovery
```

**Regression protected**

Prevents failed cache publication and failed rollback from deleting the last recoverable backup bytes.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

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

### `test_next_run_after_double_failure_preserves_recovery_before_network.fail_publication_and_rollback`

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

- Guard with a raise path: `source == temporary_metadata and target == metadata_path`.
- Guard with a raise path: `source == archive_backup and target == first.path`.
- Explicit raise expressions: `OSError('publication failed')`, `OSError('rollback failed')`.

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

- callback/function object: `tests/unit/test_cadastre_fr.py::test_publication_and_rollback_failure_preserves_recovery_backup` via `patch.object(cadastre_fr, '_replace_file', side_effect=fail_publication_and_rollback)`.
- callback/function object: `tests/unit/test_cadastre_fr.py::test_next_run_after_double_failure_preserves_recovery_before_network` via `patch.object(cadastre_fr, '_replace_file', side_effect=fail_publication_and_rollback)`.
- callback/function object: `tests/unit/test_cadastre_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `monkeypatch.setattr(cadastre_fr, '_replace_file', fail_publication_and_rollback)`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_publication_and_rollback_failure_preserves_exact_recovery_backups` via `monkeypatch.setattr(gpu, '_replace_file', fail_publication_and_rollback)`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `monkeypatch.setattr(gpu, '_replace_file', fail_publication_and_rollback)`.
- callback/function object: `tests/unit/test_ign_bdtopo_fr.py::test_publication_and_rollback_failure_preserves_exact_recovery_backups` via `patch.object(ign_bdtopo_fr, '_replace_file', side_effect=fail_publication_and_rollback)`.
- callback/function object: `tests/unit/test_ign_bdtopo_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `patch.object(ign_bdtopo_fr, '_replace_file', side_effect=fail_publication_and_rollback)`.
- callback/function object: `tests/unit/test_inpn_protected_areas_fr.py::test_rollback_failure_preserves_recovery_material` via `monkeypatch.setattr(inpn, '_replace_file', fail_publication_and_rollback)`.
- callback/function object: `tests/unit/test_rte_odre_fr.py::test_double_failure_preserves_recovery_and_next_run_uses_zero_network` via `monkeypatch.setattr(rte_odre_fr, '_replace_file', fail_publication_and_rollback)`.
- callback/function object: `tests/unit/test_rte_odre_fr.py::test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error` via `monkeypatch.setattr(rte_odre_fr, '_replace_file', fail_publication_and_rollback)`.

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

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_temporary_link_or_junction_cannot_modify_target_before_network`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `link_kind`, `temporary_role`.

**Setup**

```python
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
        return (
            link_kind == "symlink" and path == unsafe_path
        ) or original_is_symlink(path)
def simulated_is_junction(path: Path) -> bool:
        return (
            link_kind == "junction" and path == unsafe_path
        ) or original_is_junction(path)
def simulated_symlink_open(
        path: Path, *args: object, **kwargs: object
    ) -> object:
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
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(CadastreDownloadError, match="temporary|link|cache"):
        download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
assert network_calls == 0
assert sentinel.read_bytes() == sentinel_bytes
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

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
        return (
            link_kind == "symlink" and path == unsafe_path
        ) or original_is_symlink(path)

    def simulated_is_junction(path: Path) -> bool:
        return (
            link_kind == "junction" and path == unsafe_path
        ) or original_is_junction(path)

    def simulated_symlink_open(
        path: Path, *args: object, **kwargs: object
    ) -> object:
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

### `test_temporary_link_or_junction_cannot_modify_target_before_network.simulated_is_symlink`

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
link_kind == 'symlink' and path == unsafe_path or original_is_symlink(path)
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

- callback/function object: `tests/unit/test_cadastre_fr.py::test_temporary_link_or_junction_cannot_modify_target_before_network` via `monkeypatch.setattr(Path, 'is_symlink', simulated_is_symlink)`.
- callback/function object: `tests/unit/test_cadastre_fr.py::test_broken_recovery_symlink_is_rejected_before_network` via `monkeypatch.setattr(Path, 'is_symlink', simulated_is_symlink)`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_preexisting_temporary_archive_symlink_cannot_modify_target` via `monkeypatch.setattr(Path, 'is_symlink', simulated_is_symlink)`.
- callback/function object: `tests/unit/test_inpn_protected_areas_fr.py::test_broken_download_recovery_symlink_is_rejected` via `monkeypatch.setattr(Path, 'is_symlink', simulated_is_symlink)`.
- callback/function object: `tests/unit/test_rte_odre_fr.py::test_temporary_link_or_junction_cannot_modify_target_before_rte_network` via `monkeypatch.setattr(Path, 'is_symlink', simulated_is_symlink)`.
- callback/function object: `tests/unit/test_rte_odre_fr.py::test_broken_recovery_symlink_rejects_rte_before_network` via `monkeypatch.setattr(Path, 'is_symlink', simulated_is_symlink)`.

**Complete source-ordered implementation**

```python
def simulated_is_symlink(path: Path) -> bool:
        return (
            link_kind == "symlink" and path == unsafe_path
        ) or original_is_symlink(path)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_temporary_link_or_junction_cannot_modify_target_before_network.simulated_is_junction`

**Exact signature**

```python
def simulated_is_junction(path: Path) -> bool:
```

**Purpose**

Private `test` helper for simulated is junction; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `bool`.
- Every observed return expression is reproduced without truncation:
```python
link_kind == 'junction' and path == unsafe_path or original_is_junction(path)
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

- callback/function object: `tests/unit/test_cadastre_fr.py::test_temporary_link_or_junction_cannot_modify_target_before_network` via `monkeypatch.setattr(Path, 'is_junction', simulated_is_junction)`.
- callback/function object: `tests/unit/test_rte_odre_fr.py::test_temporary_link_or_junction_cannot_modify_target_before_rte_network` via `monkeypatch.setattr(Path, 'is_junction', simulated_is_junction)`.

**Complete source-ordered implementation**

```python
def simulated_is_junction(path: Path) -> bool:
        return (
            link_kind == "junction" and path == unsafe_path
        ) or original_is_junction(path)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_temporary_link_or_junction_cannot_modify_target_before_network.simulated_symlink_open`

**Exact signature**

```python
def simulated_symlink_open(
        path: Path, *args: object, **kwargs: object
    ) -> object:
```

**Purpose**

Private `test` helper for simulated symlink open; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `object`.
- Every observed return expression is reproduced without truncation:
```python
original_open(path, *args, **kwargs)

original_open(sentinel, *args, **kwargs)
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

- callback/function object: `tests/unit/test_cadastre_fr.py::test_temporary_link_or_junction_cannot_modify_target_before_network` via `monkeypatch.setattr(Path, 'open', simulated_symlink_open)`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_preexisting_temporary_archive_symlink_cannot_modify_target` via `monkeypatch.setattr(Path, 'open', simulated_symlink_open)`.
- callback/function object: `tests/unit/test_rte_odre_fr.py::test_temporary_link_or_junction_cannot_modify_target_before_rte_network` via `monkeypatch.setattr(Path, 'open', simulated_symlink_open)`.

**Complete source-ordered implementation**

```python
def simulated_symlink_open(
        path: Path, *args: object, **kwargs: object
    ) -> object:
        if path == unsafe_path:
            return original_open(sentinel, *args, **kwargs)
        return original_open(path, *args, **kwargs)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_temporary_link_or_junction_cannot_modify_target_before_network.record_network`

**Exact signature**

```python
def record_network(*args: object, **kwargs: object) -> io.BytesIO:
```

**Purpose**

Private `test` helper for record network; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `io.BytesIO`.
- Every observed return expression is reproduced without truncation:
```python
io.BytesIO(ARCHIVE_CONTENT)
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

- callback/function object: `tests/unit/test_cadastre_fr.py::test_temporary_link_or_junction_cannot_modify_target_before_network` via `monkeypatch.setattr(cadastre_fr, 'open_safe_https', record_network)`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_preexisting_temporary_archive_symlink_cannot_modify_target` via `monkeypatch.setattr(gpu, 'open_safe_https', record_network)`.
- callback/function object: `tests/unit/test_rte_odre_fr.py::test_temporary_link_or_junction_cannot_modify_target_before_rte_network` via `monkeypatch.setattr(rte_odre_fr, 'open_safe_https', record_network)`.

**Complete source-ordered implementation**

```python
def record_network(*args: object, **kwargs: object) -> io.BytesIO:
        nonlocal network_calls
        network_calls += 1
        return io.BytesIO(ARCHIVE_CONTENT)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_broken_recovery_symlink_is_rejected_before_network`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
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
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(CadastreDownloadError, match="backup|recovery|manual"):
        download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
assert network_calls == 0
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

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

### `test_broken_recovery_symlink_is_rejected_before_network.simulated_is_symlink`

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
path == recovery_path or original_is_symlink(path)
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

- callback/function object: `tests/unit/test_cadastre_fr.py::test_temporary_link_or_junction_cannot_modify_target_before_network` via `monkeypatch.setattr(Path, 'is_symlink', simulated_is_symlink)`.
- callback/function object: `tests/unit/test_cadastre_fr.py::test_broken_recovery_symlink_is_rejected_before_network` via `monkeypatch.setattr(Path, 'is_symlink', simulated_is_symlink)`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_preexisting_temporary_archive_symlink_cannot_modify_target` via `monkeypatch.setattr(Path, 'is_symlink', simulated_is_symlink)`.
- callback/function object: `tests/unit/test_inpn_protected_areas_fr.py::test_broken_download_recovery_symlink_is_rejected` via `monkeypatch.setattr(Path, 'is_symlink', simulated_is_symlink)`.
- callback/function object: `tests/unit/test_rte_odre_fr.py::test_temporary_link_or_junction_cannot_modify_target_before_rte_network` via `monkeypatch.setattr(Path, 'is_symlink', simulated_is_symlink)`.
- callback/function object: `tests/unit/test_rte_odre_fr.py::test_broken_recovery_symlink_rejects_rte_before_network` via `monkeypatch.setattr(Path, 'is_symlink', simulated_is_symlink)`.

**Complete source-ordered implementation**

```python
def simulated_is_symlink(path: Path) -> bool:
        return path == recovery_path or original_is_symlink(path)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_broken_recovery_symlink_is_rejected_before_network.fail_network`

**Exact signature**

```python
def fail_network(*args: object, **kwargs: object) -> io.BytesIO:
```

**Purpose**

Private `test` helper for fail network; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `io.BytesIO`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `AssertionError('broken recovery link must fail before network')`.

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

- callback/function object: `tests/unit/test_cadastre_fr.py::test_broken_recovery_symlink_is_rejected_before_network` via `monkeypatch.setattr(cadastre_fr, 'open_safe_https', fail_network)`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_mutated_loaded_api_origin_is_rejected_before_discovery_network` via `monkeypatch.setattr(gpu, 'open_safe_https', fail_network)`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_download_rejects_forged_written_file_provenance_before_network` via `monkeypatch.setattr(gpu, 'open_safe_https', fail_network)`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_stale_recovery_backup_rejects_cache_before_network` via `monkeypatch.setattr(gpu, 'open_safe_https', fail_network)`.
- callback/function object: `tests/unit/test_rte_odre_fr.py::test_mutated_loaded_api_origin_is_rejected_before_metadata_network` via `monkeypatch.setattr(rte_odre_fr, 'open_safe_https', fail_network)`.
- callback/function object: `tests/unit/test_rte_odre_fr.py::test_double_failure_preserves_recovery_and_next_run_uses_zero_network` via `monkeypatch.setattr(rte_odre_fr, 'open_safe_https', fail_network)`.
- callback/function object: `tests/unit/test_rte_odre_fr.py::test_broken_recovery_symlink_rejects_rte_before_network` via `monkeypatch.setattr(rte_odre_fr, 'open_safe_https', fail_network)`.

**Complete source-ordered implementation**

```python
def fail_network(*args: object, **kwargs: object) -> io.BytesIO:
        nonlocal network_calls
        network_calls += 1
        raise AssertionError("broken recovery link must fail before network")
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_cleanup_failure_does_not_mask_double_failure_recovery_error`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
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
```

**Action**

```python
with patch(
        "landscout.sources.cadastre_fr.open_safe_https",
        return_value=io.BytesIO(ARCHIVE_CONTENT),
    ):
        first = download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
```

**Expected result**

```python
with pytest.raises(CadastreDownloadError, match="rollback"):
        download_cadastre_parcelles(COMMUNE_CODE, tmp_path)
assert archive_backup.read_bytes() == old_archive
assert metadata_backup.read_bytes() == old_metadata
```

**Regression protected**

Prevents failed cache publication and failed rollback from deleting the last recoverable backup bytes.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

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

### `test_cleanup_failure_does_not_mask_double_failure_recovery_error.fail_publication_and_rollback`

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

- Guard with a raise path: `source == temporary_metadata and target == metadata_path`.
- Guard with a raise path: `source == archive_backup and target == first.path`.
- Explicit raise expressions: `OSError('publication failed')`, `OSError('rollback failed')`.

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

- callback/function object: `tests/unit/test_cadastre_fr.py::test_publication_and_rollback_failure_preserves_recovery_backup` via `patch.object(cadastre_fr, '_replace_file', side_effect=fail_publication_and_rollback)`.
- callback/function object: `tests/unit/test_cadastre_fr.py::test_next_run_after_double_failure_preserves_recovery_before_network` via `patch.object(cadastre_fr, '_replace_file', side_effect=fail_publication_and_rollback)`.
- callback/function object: `tests/unit/test_cadastre_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `monkeypatch.setattr(cadastre_fr, '_replace_file', fail_publication_and_rollback)`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_publication_and_rollback_failure_preserves_exact_recovery_backups` via `monkeypatch.setattr(gpu, '_replace_file', fail_publication_and_rollback)`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `monkeypatch.setattr(gpu, '_replace_file', fail_publication_and_rollback)`.
- callback/function object: `tests/unit/test_ign_bdtopo_fr.py::test_publication_and_rollback_failure_preserves_exact_recovery_backups` via `patch.object(ign_bdtopo_fr, '_replace_file', side_effect=fail_publication_and_rollback)`.
- callback/function object: `tests/unit/test_ign_bdtopo_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `patch.object(ign_bdtopo_fr, '_replace_file', side_effect=fail_publication_and_rollback)`.
- callback/function object: `tests/unit/test_inpn_protected_areas_fr.py::test_rollback_failure_preserves_recovery_material` via `monkeypatch.setattr(inpn, '_replace_file', fail_publication_and_rollback)`.
- callback/function object: `tests/unit/test_rte_odre_fr.py::test_double_failure_preserves_recovery_and_next_run_uses_zero_network` via `monkeypatch.setattr(rte_odre_fr, '_replace_file', fail_publication_and_rollback)`.
- callback/function object: `tests/unit/test_rte_odre_fr.py::test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error` via `monkeypatch.setattr(rte_odre_fr, '_replace_file', fail_publication_and_rollback)`.

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

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_cleanup_failure_does_not_mask_double_failure_recovery_error.fail_temporary_cleanup`

**Exact signature**

```python
def fail_temporary_cleanup(path: Path, *, missing_ok: bool = False) -> None:
```

**Purpose**

Private `test` helper for fail temporary cleanup; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `rollback_failed and path == temporary_metadata`.
- Explicit raise expressions: `PermissionError('temporary cleanup failed')`.

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

- callback/function object: `tests/unit/test_cadastre_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `monkeypatch.setattr(Path, 'unlink', fail_temporary_cleanup)`.
- callback/function object: `tests/unit/test_gpu_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `monkeypatch.setattr(Path, 'unlink', fail_temporary_cleanup)`.
- callback/function object: `tests/unit/test_ign_bdtopo_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `patch.object(Path, 'unlink', new=fail_temporary_cleanup)`.
- callback/function object: `tests/unit/test_rte_odre_fr.py::test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error` via `monkeypatch.setattr(Path, 'unlink', fail_temporary_cleanup)`.

**Complete source-ordered implementation**

```python
def fail_temporary_cleanup(path: Path, *, missing_ok: bool = False) -> None:
        if rollback_failed and path == temporary_metadata:
            raise PermissionError("temporary cleanup failed")
        original_unlink(path, missing_ok=missing_ok)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.


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

# `tests/unit/test_inpn_protected_areas_fr.py`

## File identity

- Repository path: `tests/unit/test_inpn_protected_areas_fr.py`
- File type: Python unit/regression tests
- Domain: isolated INPN archive/extraction source authority evidence
- Source SHA256: `a5b74d0e8db4cd715231fcfa651aa0c2330f43a34c80ac5f0a74e47dcb96f1be`
- Collected cases after STEP 7F.1B.1.1: `147`

## 1. Test architecture and boundary

The test file uses local temporary archives/GeoPackages and controlled monkeypatches. It never depends on live INPN transport. It protects factual byte, archive, extraction, package, metadata, canonicality, and rebuild contracts without adding environmental semantics. Feature rows are used only to construct tiny synthetic fixture files; the production catalog path is explicitly prevented from materializing them.

## 2. Imports

```python
from __future__ import annotations
```

```python
import inspect
```

```python
import io
```

```python
import json
```

```python
import stat
```

```python
import warnings
```

```python
import zipfile
```

```python
from contextlib import contextmanager
```

```python
from dataclasses import FrozenInstanceError, fields, replace
```

```python
from datetime import datetime
```

```python
from hashlib import sha256
```

```python
from pathlib import Path
```

```python
from typing import Any, Self
```

```python
import pytest
```

```python
import yaml
```

```python
from pydantic import ValidationError
```

```python
from landscout import sources
```

```python
from landscout.common import safe_http
```

```python
from landscout.common.safe_http import SafeHttpsError
```

```python
from landscout.sources import inpn_protected_areas_fr as inpn
```

```python
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
```

## 3. Fixtures, helpers, context managers, and support classes

### `_Response`

- Kind: support class.
- Bases: `object`.
- Purpose: provides deterministic fake transport, scalar-subclass, or mutation-fixture behavior required by the tests.
- Decorators: `none`.
- Exact methods:

  - `def __init__(self, payload: bytes, *, url: str, status_code: int=200, location: str | None=None) -> None` stores deterministic payload, URL, status, headers, read/close counters, and offset.
  - `@property def is_redirect(self) -> bool` derives redirect status from the exact status code.
  - `def raise_for_status(self) -> None` raises the configured HTTP error domain for non-success status.
  - `def iter_content(self, chunk_size: int=8192) -> Any` yields deterministic byte chunks.
  - `def close(self) -> None` records closure.
  - `def read(self, size: int=-1) -> bytes` implements bounded sequential fake response reads.
  - `def __enter__(self) -> Self` and `def __exit__(self, *args: object) -> None` provide deterministic context-manager lifetime.
- Invariant protected: the production boundary cannot distinguish trust using mutable aliases, permissive scalar equality, or real network state.

### `_Session`

- Kind: support class.
- Bases: `object`.
- Purpose: provides deterministic fake transport, scalar-subclass, or mutation-fixture behavior required by the tests.
- Decorators: `none`.
- Exact methods:

  - `def __init__(self, response: _Response | None=None, *, responses: list[_Response] | None=None, error: Exception | None=None) -> None` installs ordered fake responses or a controlled failure and call history.
  - `def get(self, url: str, **kwargs: object) -> _Response` records a request and returns/raises the next deterministic response.
  - `@contextmanager def open(self, url: str, *, timeout: float, headers: dict[str, str] | None=None, max_redirects: int=10) -> Any` adapts the fake session to the source transport context-manager contract and closes responses.
- Invariant protected: the production boundary cannot distinguish trust using mutable aliases, permissive scalar equality, or real network state.

### `_zip_bytes`

- Exact signature: `def _zip_bytes(members: dict[str, bytes] | list[tuple[str, bytes]] | None=None) -> bytes`
- Decorators: `none`.
- Kind: fixture/helper.
- Purpose: Zip bytes.
- Inputs/outputs: fixed by the exact signature; returned archives, configs, extraction records, catalog records, and monkeypatch closures are local synthetic evidence only.
- Mechanisms/callees: `archive.writestr`, `io.BytesIO`, `isinstance`, `list`, `stream.getvalue`, `values.items`, `warnings.catch_warnings`, `warnings.simplefilter`, `zipfile.ZipFile`, `zipfile.ZipInfo`.
- Validation behavior: assertions and delegated production validation.
- Filesystem/network boundary: uses pytest temporary paths and fake/blocked transport where visible; no approved EP cache or external service is modified.

### `_special_zip`

- Exact signature: `def _special_zip(name: str, mode: int) -> bytes`
- Decorators: `none`.
- Kind: fixture/helper.
- Purpose: Special zip.
- Inputs/outputs: fixed by the exact signature; returned archives, configs, extraction records, catalog records, and monkeypatch closures are local synthetic evidence only.
- Mechanisms/callees: `archive.writestr`, `io.BytesIO`, `stream.getvalue`, `zipfile.ZipFile`, `zipfile.ZipInfo`.
- Validation behavior: assertions and delegated production validation.
- Filesystem/network boundary: uses pytest temporary paths and fake/blocked transport where visible; no approved EP cache or external service is modified.

### `_unsupported_compression_zip`

- Exact signature: `def _unsupported_compression_zip() -> bytes`
- Decorators: `none`.
- Kind: fixture/helper.
- Purpose: Unsupported compression zip.
- Inputs/outputs: fixed by the exact signature; returned archives, configs, extraction records, catalog records, and monkeypatch closures are local synthetic evidence only.
- Mechanisms/callees: `99 .to_bytes`, `_zip_bytes`, `bytearray`, `bytes`, `payload.index`.
- Validation behavior: assertions and delegated production validation.
- Filesystem/network boundary: uses pytest temporary paths and fake/blocked transport where visible; no approved EP cache or external service is modified.

### `_config_payload`

- Exact signature: `def _config_payload() -> dict[str, object]`
- Decorators: `none`.
- Kind: fixture/helper.
- Purpose: Config payload.
- Inputs/outputs: fixed by the exact signature; returned archives, configs, extraction records, catalog records, and monkeypatch closures are local synthetic evidence only.
- Mechanisms/callees: `CONFIG_PATH.read_text`, `isinstance`, `yaml.safe_load`.
- Validation behavior: assertions and delegated production validation.
- Filesystem/network boundary: uses pytest temporary paths and fake/blocked transport where visible; no approved EP cache or external service is modified.

### `_write_config`

- Exact signature: `def _write_config(tmp_path: Path, payload: dict[str, object]) -> Path`
- Decorators: `none`.
- Kind: fixture/helper.
- Purpose: Write config.
- Inputs/outputs: fixed by the exact signature; returned archives, configs, extraction records, catalog records, and monkeypatch closures are local synthetic evidence only.
- Mechanisms/callees: `path.write_text`, `yaml.safe_dump`.
- Validation behavior: assertions and delegated production validation.
- Filesystem/network boundary: uses pytest temporary paths and fake/blocked transport where visible; no approved EP cache or external service is modified.

### `_config`

- Exact signature: `def _config(tmp_path: Path, expected_bytes: bytes | None=None) -> InpnProtectedAreasSourceConfig`
- Decorators: `none`.
- Kind: fixture/helper.
- Purpose: Config.
- Inputs/outputs: fixed by the exact signature; returned archives, configs, extraction records, catalog records, and monkeypatch closures are local synthetic evidence only.
- Mechanisms/callees: `InpnProtectedAreasSourceConfig.model_validate`, `_config_payload`, `_zip_bytes`, `len`, `sha256`, `sha256(snapshot).hexdigest`, `str`.
- Validation behavior: assertions and delegated production validation.
- Filesystem/network boundary: uses pytest temporary paths and fake/blocked transport where visible; no approved EP cache or external service is modified.

### `_session`

- Exact signature: `def _session(config: InpnProtectedAreasSourceConfig, payload: bytes | None=None, *, status_code: int=200, redirect_chain: tuple[str, ...]=()) -> _Session`
- Decorators: `none`.
- Kind: fixture/helper.
- Purpose: Session.
- Inputs/outputs: fixed by the exact signature; returned archives, configs, extraction records, catalog records, and monkeypatch closures are local synthetic evidence only.
- Mechanisms/callees: `_Response`, `_Session`, `_zip_bytes`, `responses.append`, `str`.
- Validation behavior: assertions and delegated production validation.
- Filesystem/network boundary: uses pytest temporary paths and fake/blocked transport where visible; no approved EP cache or external service is modified.

### `_download`

- Exact signature: `def _download(tmp_path: Path, *, payload: bytes | None=None) -> tuple[InpnProtectedAreasSourceConfig, InpnProtectedAreasDownload, _Session]`
- Decorators: `none`.
- Kind: fixture/helper.
- Purpose: Download.
- Inputs/outputs: fixed by the exact signature; returned archives, configs, extraction records, catalog records, and monkeypatch closures are local synthetic evidence only.
- Mechanisms/callees: `_config`, `_download_with_session`, `_session`, `_zip_bytes`.
- Validation behavior: assertions and delegated production validation.
- Filesystem/network boundary: uses pytest temporary paths and fake/blocked transport where visible; no approved EP cache or external service is modified.

### `_download_with_session`

- Exact signature: `def _download_with_session(config: InpnProtectedAreasSourceConfig, session: _Session, *, timeout_seconds: float=120.0) -> InpnProtectedAreasDownload`
- Decorators: `none`.
- Kind: fixture/helper.
- Purpose: Download with session.
- Inputs/outputs: fixed by the exact signature; returned archives, configs, extraction records, catalog records, and monkeypatch closures are local synthetic evidence only.
- Mechanisms/callees: `download_inpn_protected_areas_archive`, `monkeypatch.setattr`, `pytest.MonkeyPatch.context`.
- Validation behavior: assertions and delegated production validation.
- Filesystem/network boundary: uses pytest temporary paths and fake/blocked transport where visible; no approved EP cache or external service is modified.

### `_download_metadata_path`

- Exact signature: `def _download_metadata_path(download: InpnProtectedAreasDownload) -> Path`
- Decorators: `none`.
- Kind: fixture/helper.
- Purpose: Download metadata path.
- Inputs/outputs: fixed by the exact signature; returned archives, configs, extraction records, catalog records, and monkeypatch closures are local synthetic evidence only.
- Mechanisms/callees: `download.path.with_name`.
- Validation behavior: assertions and delegated production validation.
- Filesystem/network boundary: uses pytest temporary paths and fake/blocked transport where visible; no approved EP cache or external service is modified.

### `_extraction_metadata_path`

- Exact signature: `def _extraction_metadata_path(extraction: InpnProtectedAreasExtraction) -> Path`
- Decorators: `none`.
- Kind: fixture/helper.
- Purpose: Extraction metadata path.
- Inputs/outputs: fixed by the exact signature; returned archives, configs, extraction records, catalog records, and monkeypatch closures are local synthetic evidence only.
- Mechanisms/callees: `extraction.extraction_path.iterdir`, `len`, `path.is_file`, `path.name.startswith`, `sorted`.
- Validation behavior: assertions and delegated production validation.
- Filesystem/network boundary: uses pytest temporary paths and fake/blocked transport where visible; no approved EP cache or external service is modified.

### `_read_json`

- Exact signature: `def _read_json(path: Path) -> dict[str, object]`
- Decorators: `none`.
- Kind: fixture/helper.
- Purpose: Read json.
- Inputs/outputs: fixed by the exact signature; returned archives, configs, extraction records, catalog records, and monkeypatch closures are local synthetic evidence only.
- Mechanisms/callees: `isinstance`, `json.loads`, `path.read_text`.
- Validation behavior: assertions and delegated production validation.
- Filesystem/network boundary: uses pytest temporary paths and fake/blocked transport where visible; no approved EP cache or external service is modified.

### `_write_json`

- Exact signature: `def _write_json(path: Path, payload: dict[str, object]) -> None`
- Decorators: `none`.
- Kind: fixture/helper.
- Purpose: Write json.
- Inputs/outputs: fixed by the exact signature; returned archives, configs, extraction records, catalog records, and monkeypatch closures are local synthetic evidence only.
- Mechanisms/callees: `json.dumps`, `path.write_text`.
- Validation behavior: assertions and delegated production validation.
- Filesystem/network boundary: uses pytest temporary paths and fake/blocked transport where visible; no approved EP cache or external service is modified.

### `_rewrite_extraction_marker_and_caller`

- Exact signature: `def _rewrite_extraction_marker_and_caller(extraction: InpnProtectedAreasExtraction) -> InpnProtectedAreasExtraction`
- Decorators: `none`.
- Kind: fixture/helper.
- Purpose: Rewrite extraction marker and caller.
- Inputs/outputs: fixed by the exact signature; returned archives, configs, extraction records, catalog records, and monkeypatch closures are local synthetic evidence only.
- Mechanisms/callees: `InpnProtectedAreasExtractedFile`, `_extraction_metadata_path`, `_read_json`, `_write_json`, `extraction.extraction_path.rglob`, `path.is_file`, `path.read_bytes`, `path.relative_to`, `path.relative_to(extraction.extraction_path).as_posix`, `path.stat`, `replace`, `sha256`, `sha256(path.read_bytes()).hexdigest`, `sorted`, `tuple`.
- Validation behavior: assertions and delegated production validation.
- Filesystem/network boundary: uses pytest temporary paths and fake/blocked transport where visible; no approved EP cache or external service is modified.

### `_force_cache_miss`

- Exact signature: `def _force_cache_miss(download: InpnProtectedAreasDownload) -> tuple[Path, bytes]`
- Decorators: `none`.
- Kind: fixture/helper.
- Purpose: Force cache miss.
- Inputs/outputs: fixed by the exact signature; returned archives, configs, extraction records, catalog records, and monkeypatch closures are local synthetic evidence only.
- Mechanisms/callees: `_download_metadata_path`, `_read_json`, `_write_json`, `metadata_path.read_bytes`.
- Validation behavior: assertions and delegated production validation.
- Filesystem/network boundary: uses pytest temporary paths and fake/blocked transport where visible; no approved EP cache or external service is modified.

### `_tree_snapshot`

- Exact signature: `def _tree_snapshot(root: Path) -> dict[str, bytes]`
- Decorators: `none`.
- Kind: fixture/helper.
- Purpose: Tree snapshot.
- Inputs/outputs: fixed by the exact signature; returned archives, configs, extraction records, catalog records, and monkeypatch closures are local synthetic evidence only.
- Mechanisms/callees: `path.is_file`, `path.read_bytes`, `path.relative_to`, `path.relative_to(root).as_posix`, `root.rglob`, `sorted`.
- Validation behavior: assertions and delegated production validation.
- Filesystem/network boundary: uses pytest temporary paths and fake/blocked transport where visible; no approved EP cache or external service is modified.

## 4. Test-by-test regression inventory

### `test_checked_in_config_loads_with_exact_source_identity`

- Exact signature: `def test_checked_in_config_loads_with_exact_source_identity() -> None`
- Parametrization/decorators: none; one collected case.
- Fixtures/inputs: none.
- Protected invariant: Checked in config loads with exact source identity.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: none directly.
- Expected controlled failures: none; this is an acceptance/output invariant.
- Calls exercised: `load_inpn_protected_areas_source_config`, `str`, `str(config.reference_page_url).startswith`, `type`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_source_config_yaml_rejects_duplicate_keys`

- Exact signature: `def test_source_config_yaml_rejects_duplicate_keys(tmp_path: Path) -> None`
- Parametrization/decorators: none; one collected case.
- Fixtures/inputs: `tmp_path`.
- Protected invariant: Source config yaml rejects duplicate keys.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: none directly.
- Expected controlled failures: `pytest.raises(InpnProtectedAreasSourceError, match='config')`.
- Calls exercised: `CONFIG_PATH.read_text`, `load_inpn_protected_areas_source_config`, `path.write_text`, `pytest.raises`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_loaded_source_config_is_immutable`

- Exact signature: `def test_loaded_source_config_is_immutable() -> None`
- Parametrization/decorators: none; one collected case.
- Fixtures/inputs: none.
- Protected invariant: Loaded source config is immutable.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: none directly.
- Expected controlled failures: `pytest.raises(ValidationError, match='frozen')`.
- Calls exercised: `load_inpn_protected_areas_source_config`, `pytest.raises`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_config_rejects_invalid_expected_snapshot_integrity`

- Exact signature: `def test_config_rejects_invalid_expected_snapshot_integrity(field: str, value: object) -> None`
- Parametrization/decorators: `pytest.mark.parametrize(('field', 'value'), [('expected_archive_size_bytes', 0), ('expected_archive_size_bytes', -1), ('expected_archive_size_bytes', True), ('expected_archive_size_bytes', 1.0), ('expected_archive_size_bytes', '99835011'), ('expected_archive_size_bytes', float('nan')), ('expected_archive_size_bytes', float('inf')), ('expected_archive_size_bytes', float('-inf')), ('expected_archive_sha256', '0' * 63), ('expected_archive_sha256', 'A' * 64), ('expected_archive_sha256', None)])`.
- Fixtures/inputs: `field`, `value`.
- Protected invariant: Config rejects invalid expected snapshot integrity.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: none directly.
- Expected controlled failures: `pytest.raises((TypeError, ValueError))`.
- Calls exercised: `InpnProtectedAreasSourceConfig.model_validate`, `_config_payload`, `float`, `pytest.mark.parametrize`, `pytest.raises`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_config_rejects_noncanonical_values`

- Exact signature: `def test_config_rejects_noncanonical_values(tmp_path: Path, mutation: str) -> None`
- Parametrization/decorators: `pytest.mark.parametrize('mutation', ['unknown_key', 'missing_dataset_id', 'wrong_dataset_id', 'empty_version', 'malformed_reference_url', 'malformed_archive_url', 'non_https_archive_url', 'wrong_archive_filename'])`.
- Fixtures/inputs: `tmp_path`, `mutation`.
- Protected invariant: Config rejects noncanonical values.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: none directly.
- Expected controlled failures: `pytest.raises(InpnProtectedAreasSourceError)`.
- Calls exercised: `_config_payload`, `_write_config`, `load_inpn_protected_areas_source_config`, `payload.pop`, `pytest.mark.parametrize`, `pytest.raises`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_wrong_download_config_type_has_controlled_error`

- Exact signature: `def test_wrong_download_config_type_has_controlled_error() -> None`
- Parametrization/decorators: none; one collected case.
- Fixtures/inputs: none.
- Protected invariant: Wrong download config type has controlled error.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: none directly.
- Expected controlled failures: `pytest.raises(InpnProtectedAreasSourceError, match='config|type')`.
- Calls exercised: `download_inpn_protected_areas_archive`, `object`, `pytest.raises`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_download_timeout_is_strict_finite_positive`

- Exact signature: `def test_download_timeout_is_strict_finite_positive(timeout: object) -> None`
- Parametrization/decorators: `pytest.mark.parametrize('timeout', [0, -1, float('nan'), float('inf'), '30', True, pytest.param(10 ** 10000, id='overflow-int')])`.
- Fixtures/inputs: `timeout`.
- Protected invariant: Download timeout is strict finite positive.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: none directly.
- Expected controlled failures: `pytest.raises(InpnProtectedAreasSourceError, match='timeout')`.
- Calls exercised: `download_inpn_protected_areas_archive`, `float`, `load_inpn_protected_areas_source_config`, `pytest.mark.parametrize`, `pytest.param`, `pytest.raises`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_download_api_has_no_arbitrary_http_session_injection`

- Exact signature: `def test_download_api_has_no_arbitrary_http_session_injection() -> None`
- Parametrization/decorators: none; one collected case.
- Fixtures/inputs: none.
- Protected invariant: Download api has no arbitrary http session injection.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: none directly.
- Expected controlled failures: none; this is an acceptance/output invariant.
- Calls exercised: `inspect.signature`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_download_cache_setup_failure_is_controlled`

- Exact signature: `def test_download_cache_setup_failure_is_controlled(tmp_path: Path) -> None`
- Parametrization/decorators: none; one collected case.
- Fixtures/inputs: `tmp_path`.
- Protected invariant: Download cache setup failure is controlled.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: none directly.
- Expected controlled failures: `pytest.raises(InpnProtectedAreasSourceError, match='download|cache')`.
- Calls exercised: `InpnProtectedAreasSourceConfig.model_validate`, `_config_payload`, `_download_with_session`, `_session`, `cache_file.write_bytes`, `pytest.raises`, `str`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_valid_zip_download_binds_exact_bytes_and_lineage`

- Exact signature: `def test_valid_zip_download_binds_exact_bytes_and_lineage(tmp_path: Path) -> None`
- Parametrization/decorators: none; one collected case.
- Fixtures/inputs: `tmp_path`.
- Protected invariant: Valid zip download binds exact bytes and lineage.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: none directly.
- Expected controlled failures: none; this is an acceptance/output invariant.
- Calls exercised: `_config`, `_download_metadata_path`, `_download_with_session`, `_read_json`, `_session`, `_zip_bytes`, `datetime.fromisoformat`, `field.endswith`, `getattr`, `len`, `pytest.approx`, `result.path.read_bytes`, `result.sha256.lower`, `sha256`, `sha256(payload).hexdigest`, `str`, `timestamp.utcoffset`, `timestamp.utcoffset().total_seconds`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_cold_download_must_match_configured_snapshot_before_publication`

- Exact signature: `def test_cold_download_must_match_configured_snapshot_before_publication(tmp_path: Path, mismatch: str) -> None`
- Parametrization/decorators: `pytest.mark.parametrize('mismatch', ['size', 'sha256'])`.
- Fixtures/inputs: `tmp_path`, `mismatch`.
- Protected invariant: Cold download must match configured snapshot before publication.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: none directly.
- Expected controlled failures: `pytest.raises(InpnProtectedAreasSourceError, match='size|SHA|snapshot|integrity')`.
- Calls exercised: `Path`, `Path(config.cache_root).rglob`, `_config`, `_download_with_session`, `_session`, `_zip_bytes`, `len`, `list`, `pytest.mark.parametrize`, `pytest.raises`, `sha256`, `sha256(downloaded).digest`, `sha256(expected).digest`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_coordinated_cache_and_metadata_snapshot_change_is_not_a_cache_hit`

- Exact signature: `def test_coordinated_cache_and_metadata_snapshot_change_is_not_a_cache_hit(tmp_path: Path) -> None`
- Parametrization/decorators: none; one collected case.
- Fixtures/inputs: `tmp_path`.
- Protected invariant: Coordinated cache and metadata snapshot change is not a cache hit.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: none directly.
- Expected controlled failures: `pytest.raises(InpnProtectedAreasSourceError)`.
- Calls exercised: `SafeHttpsError`, `_Session`, `_download`, `_download_metadata_path`, `_download_with_session`, `_read_json`, `_write_json`, `_zip_bytes`, `first.path.write_bytes`, `len`, `pytest.raises`, `sha256`, `sha256(replacement).hexdigest`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_http_and_payload_failures_are_controlled`

- Exact signature: `def test_http_and_payload_failures_are_controlled(tmp_path: Path, payload: bytes, status: int, error: Exception | None) -> None`
- Parametrization/decorators: `pytest.mark.parametrize(('payload', 'status', 'error'), [(_zip_bytes(), 300, None), (_zip_bytes(), 304, None), (_zip_bytes(), 503, None), (b'', 200, None), (b'<html>temporary failure</html>', 200, None), (b'PK not really a zip', 200, None), (_zip_bytes(), 200, OSError('network failed'))], ids=['http-300', 'http-304', 'http-error', 'empty', 'html', 'invalid-zip', 'transport-error'])`.
- Fixtures/inputs: `tmp_path`, `payload`, `status`, `error`.
- Protected invariant: Http and payload failures are controlled.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: none directly.
- Expected controlled failures: `pytest.raises(InpnProtectedAreasSourceError)`.
- Calls exercised: `OSError`, `Path`, `Path(config.cache_root).rglob`, `_Session`, `_config`, `_download_with_session`, `_session`, `_zip_bytes`, `list`, `pytest.mark.parametrize`, `pytest.raises`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_unsupported_zip_compression_has_controlled_error`

- Exact signature: `def test_unsupported_zip_compression_has_controlled_error(tmp_path: Path) -> None`
- Parametrization/decorators: none; one collected case.
- Fixtures/inputs: `tmp_path`.
- Protected invariant: Unsupported zip compression has controlled error.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: none directly.
- Expected controlled failures: `pytest.raises(InpnProtectedAreasSourceError, match='ZIP|archive')`.
- Calls exercised: `_config`, `_download_with_session`, `_session`, `_unsupported_compression_zip`, `pytest.raises`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_malformed_response_headers_have_controlled_error`

- Exact signature: `def test_malformed_response_headers_have_controlled_error(tmp_path: Path) -> None`
- Parametrization/decorators: none; one collected case.
- Fixtures/inputs: `tmp_path`.
- Protected invariant: Malformed response headers have controlled error.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: none directly.
- Expected controlled failures: `pytest.raises(InpnProtectedAreasSourceError, match='response|download')`.
- Calls exercised: `_Response`, `_Session`, `_config`, `_download_with_session`, `_zip_bytes`, `pytest.raises`, `str`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_midstream_protocol_failure_has_controlled_error`

- Exact signature: `def test_midstream_protocol_failure_has_controlled_error(tmp_path: Path) -> None`
- Parametrization/decorators: none; one collected case.
- Fixtures/inputs: `tmp_path`.
- Protected invariant: Midstream protocol failure has controlled error.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: none directly.
- Expected controlled failures: `pytest.raises(InpnProtectedAreasSourceError, match='response|download')`.
- Calls exercised: `OSError`, `_FailingRaw`, `_Response`, `_Session`, `_config`, `_download_with_session`, `_zip_bytes`, `pytest.raises`, `str`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_valid_physical_and_metadata_cache_is_reused`

- Exact signature: `def test_valid_physical_and_metadata_cache_is_reused(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None`
- Parametrization/decorators: none; one collected case.
- Fixtures/inputs: `tmp_path`, `monkeypatch`.
- Protected invariant: Valid physical and metadata cache is reused.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: `monkeypatch.setattr(inpn, "open_safe_https", fail_http)`; `monkeypatch.setattr(safe_http.socket, "getaddrinfo", fail_dns)`.
- Expected controlled failures: none; this is an acceptance/output invariant.
- Calls exercised: `AssertionError`, `_download`, `download_inpn_protected_areas_archive`, `monkeypatch.setattr`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_invalid_download_cache_is_a_miss`

- Exact signature: `def test_invalid_download_cache_is_a_miss(tmp_path: Path, mutation: str) -> None`
- Parametrization/decorators: `pytest.mark.parametrize('mutation', ['physical_size', 'physical_sha', 'metadata_sha', 'metadata_size', 'metadata_url', 'metadata_version', 'metadata_schema', 'metadata_schema_bool', 'metadata_schema_float', 'metadata_unknown', 'metadata_duplicate', 'metadata_timestamp', 'metadata_malformed', 'invalid_cached_zip'])`.
- Fixtures/inputs: `tmp_path`, `mutation`.
- Protected invariant: Invalid download cache is a miss.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: none directly.
- Expected controlled failures: none; this is an acceptance/output invariant.
- Calls exercised: `_download`, `_download_metadata_path`, `_download_with_session`, `_read_json`, `_session`, `_write_json`, `_zip_bytes`, `first.path.write_bytes`, `json.dumps`, `len`, `metadata_json.replace`, `metadata_path.write_text`, `pytest.mark.parametrize`, `sha256`, `sha256(invalid_zip).hexdigest`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_successful_first_and_replacement_publication`

- Exact signature: `def test_successful_first_and_replacement_publication(tmp_path: Path) -> None`
- Parametrization/decorators: none; one collected case.
- Fixtures/inputs: `tmp_path`.
- Protected invariant: Successful first and replacement publication.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: none directly.
- Expected controlled failures: none; this is an acceptance/output invariant.
- Calls exercised: `Path`, `Path(config.cache_root).rglob`, `_download`, `_download_metadata_path`, `_download_with_session`, `_force_cache_miss`, `_read_json`, `_session`, `_zip_bytes`, `list`, `second.path.read_bytes`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_publication_failure_restores_old_pair`

- Exact signature: `def test_publication_failure_restores_old_pair(tmp_path: Path, monkeypatch: pytest.MonkeyPatch, failure_target: str) -> None`
- Parametrization/decorators: `pytest.mark.parametrize('failure_target', ['archive', 'metadata'])`.
- Fixtures/inputs: `tmp_path`, `monkeypatch`, `failure_target`.
- Protected invariant: Publication failure restores old pair.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: `monkeypatch.setattr(inpn, "_replace_file", fail_once)`.
- Expected controlled failures: `pytest.raises(InpnProtectedAreasSourceError, match='publication|download')`.
- Calls exercised: `OSError`, `Path`, `Path(config.cache_root).rglob`, `_download`, `_download_with_session`, `_force_cache_miss`, `_session`, `first.path.read_bytes`, `list`, `metadata_path.read_bytes`, `monkeypatch.setattr`, `original_replace`, `pytest.mark.parametrize`, `pytest.raises`, `source.name.endswith`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_rollback_failure_preserves_recovery_material`

- Exact signature: `def test_rollback_failure_preserves_recovery_material(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None`
- Parametrization/decorators: none; one collected case.
- Fixtures/inputs: `tmp_path`, `monkeypatch`.
- Protected invariant: Rollback failure preserves recovery material.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: `monkeypatch.setattr(inpn, "_load_cached_download", lambda *args: None)`; `monkeypatch.setattr(inpn, "_replace_file", fail_publication_and_rollback)`.
- Expected controlled failures: `pytest.raises(InpnProtectedAreasSourceError, match='rollback')`.
- Calls exercised: `OSError`, `_download`, `_download_metadata_path`, `_download_with_session`, `_session`, `archive_backup.read_bytes`, `first.path.read_bytes`, `first.path.with_name`, `metadata_backup.read_bytes`, `metadata_path.read_bytes`, `metadata_path.with_name`, `monkeypatch.setattr`, `original_replace`, `pytest.raises`, `source.name.endswith`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_broken_download_recovery_symlink_is_rejected`

- Exact signature: `def test_broken_download_recovery_symlink_is_rejected(tmp_path: Path, monkeypatch: pytest.MonkeyPatch, backup_role: str) -> None`
- Parametrization/decorators: `pytest.mark.parametrize('backup_role', ['archive', 'metadata'])`.
- Fixtures/inputs: `tmp_path`, `monkeypatch`, `backup_role`.
- Protected invariant: Broken download recovery symlink is rejected.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: `monkeypatch.setattr(Path, "is_symlink", simulated_is_symlink)`.
- Expected controlled failures: `pytest.raises(InpnProtectedAreasSourceError, match='backup|recovery|manual')`.
- Calls exercised: `archive_path.exists`, `archive_path.with_name`, `inpn._publish_cache_pair`, `metadata_path.exists`, `metadata_path.with_name`, `monkeypatch.setattr`, `original_is_symlink`, `pytest.mark.parametrize`, `pytest.raises`, `temporary_archive.read_bytes`, `temporary_archive.write_bytes`, `temporary_metadata.read_bytes`, `temporary_metadata.write_bytes`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_existing_normal_download_recovery_backup_remains_unchanged`

- Exact signature: `def test_existing_normal_download_recovery_backup_remains_unchanged(tmp_path: Path) -> None`
- Parametrization/decorators: none; one collected case.
- Fixtures/inputs: `tmp_path`.
- Protected invariant: Existing normal download recovery backup remains unchanged.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: none directly.
- Expected controlled failures: `pytest.raises(InpnProtectedAreasSourceError, match='backup|recovery|manual')`.
- Calls exercised: `archive_backup.read_bytes`, `archive_backup.write_bytes`, `archive_path.with_name`, `inpn._publish_cache_pair`, `pytest.raises`, `temporary_archive.read_bytes`, `temporary_archive.write_bytes`, `temporary_metadata.read_bytes`, `temporary_metadata.write_bytes`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_failed_replacement_restores_a_still_reusable_valid_download_pair`

- Exact signature: `def test_failed_replacement_restores_a_still_reusable_valid_download_pair(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None`
- Parametrization/decorators: none; one collected case.
- Fixtures/inputs: `tmp_path`, `monkeypatch`.
- Protected invariant: Failed replacement restores a still reusable valid download pair.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: `monkeypatch.setattr(inpn, "_load_cached_download", lambda *args: None)`; `monkeypatch.setattr(inpn, "_load_cached_download", original_load)`; `monkeypatch.setattr(inpn, "_replace_file", fail_metadata)`; `monkeypatch.setattr(inpn, "_replace_file", original_replace)`.
- Expected controlled failures: `pytest.raises(InpnProtectedAreasSourceError, match='publication')`.
- Calls exercised: `AssertionError`, `OSError`, `_Session`, `_download`, `_download_metadata_path`, `_download_with_session`, `_session`, `first.path.read_bytes`, `metadata_path.read_bytes`, `monkeypatch.setattr`, `original_replace`, `pytest.raises`, `source.name.endswith`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_unsafe_zip_member_paths_are_rejected`

- Exact signature: `def test_unsafe_zip_member_paths_are_rejected(tmp_path: Path, member_name: str) -> None`
- Parametrization/decorators: `pytest.mark.parametrize('member_name', ['../evil.txt', 'nested/../../evil.txt', '/absolute/evil.txt', 'C:\\evil.txt', '\\\\server\\share\\evil.txt', '..\\mixed\\evil.txt', '.', 'CON.txt', 'folder/NUL.data', 'folder/COM¹.parquet', 'folder/LPT³.dbf', 'folder/bad:name.txt', 'folder/trailing. ', 'folder/ leading.txt', 'folder/control\n.txt'])`.
- Fixtures/inputs: `tmp_path`, `member_name`.
- Protected invariant: Unsafe zip member paths are rejected.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: none directly.
- Expected controlled failures: `pytest.raises(InpnProtectedAreasSourceError, match='ZIP|archive|member|path')`.
- Calls exercised: `_config`, `_download_with_session`, `_session`, `_zip_bytes`, `pytest.mark.parametrize`, `pytest.raises`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_duplicate_or_colliding_zip_destinations_are_rejected`

- Exact signature: `def test_duplicate_or_colliding_zip_destinations_are_rejected(tmp_path: Path, members: list[tuple[str, bytes]]) -> None`
- Parametrization/decorators: `pytest.mark.parametrize('members', [[('same.txt', b'a'), ('same.txt', b'b')], [('folder/file.txt', b'a'), ('folder\\file.txt', b'b')], [('folder/file.txt', b'a'), ('folder/./file.txt', b'b')], [('Folder/File.txt', b'a'), ('folder/file.txt', b'b')], [('blocked', b'a'), ('blocked/child.txt', b'b')]])`.
- Fixtures/inputs: `tmp_path`, `members`.
- Protected invariant: Duplicate or colliding zip destinations are rejected.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: none directly.
- Expected controlled failures: `pytest.raises(InpnProtectedAreasSourceError, match='duplicate|collid|archive')`.
- Calls exercised: `_config`, `_download_with_session`, `_session`, `_zip_bytes`, `pytest.mark.parametrize`, `pytest.raises`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_zip_links_and_special_files_are_rejected`

- Exact signature: `def test_zip_links_and_special_files_are_rejected(tmp_path: Path, mode: int, message: str) -> None`
- Parametrization/decorators: `pytest.mark.parametrize(('mode', 'message'), [(stat.S_IFLNK | 511, 'symbolic|link'), (stat.S_IFIFO | 420, 'special')])`.
- Fixtures/inputs: `tmp_path`, `mode`, `message`.
- Protected invariant: Zip links and special files are rejected.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: none directly.
- Expected controlled failures: `pytest.raises(InpnProtectedAreasSourceError, match=message)`.
- Calls exercised: `_config`, `_download_with_session`, `_session`, `_special_zip`, `pytest.mark.parametrize`, `pytest.raises`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_complete_zip_inventory_is_validated_before_member_copy`

- Exact signature: `def test_complete_zip_inventory_is_validated_before_member_copy(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None`
- Parametrization/decorators: none; one collected case.
- Fixtures/inputs: `tmp_path`, `monkeypatch`.
- Protected invariant: Complete zip inventory is validated before member copy.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: `monkeypatch.setattr(zipfile.ZipFile, "open", record_open)`.
- Expected controlled failures: `pytest.raises(InpnProtectedAreasSourceError)`.
- Calls exercised: `_config`, `_download_with_session`, `_session`, `_zip_bytes`, `monkeypatch.setattr`, `original_open`, `pytest.raises`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_extraction_validates_complete_inventory_before_copying`

- Exact signature: `def test_extraction_validates_complete_inventory_before_copying(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None`
- Parametrization/decorators: none; one collected case.
- Fixtures/inputs: `tmp_path`, `monkeypatch`.
- Protected invariant: Extraction validates complete inventory before copying.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: `monkeypatch.setattr(inpn, "copyfileobj", record_copy)`.
- Expected controlled failures: `pytest.raises(InpnProtectedAreasSourceError)`.
- Calls exercised: `(download.path.parent / 'x' / forged.sha256).exists`, `_download`, `_zip_bytes`, `download.path.write_bytes`, `extract_inpn_protected_areas_archive`, `len`, `monkeypatch.setattr`, `original_copy`, `pytest.raises`, `replace`, `sha256`, `sha256(payload).hexdigest`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_normal_nested_members_are_accepted`

- Exact signature: `def test_normal_nested_members_are_accepted(tmp_path: Path) -> None`
- Parametrization/decorators: none; one collected case.
- Fixtures/inputs: `tmp_path`.
- Protected invariant: Normal nested members are accepted.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: none directly.
- Expected controlled failures: none; this is an acceptance/output invariant.
- Calls exercised: `_download`, `_zip_bytes`, `download.path.is_file`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_extraction_inventory_is_complete_ordered_and_hashed`

- Exact signature: `def test_extraction_inventory_is_complete_ordered_and_hashed(tmp_path: Path) -> None`
- Parametrization/decorators: none; one collected case.
- Fixtures/inputs: `tmp_path`.
- Protected invariant: Extraction inventory is complete ordered and hashed.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: none directly.
- Expected controlled failures: none; this is an acceptance/output invariant.
- Calls exercised: `_download`, `_extraction_metadata_path`, `_read_json`, `_zip_bytes`, `extract_inpn_protected_areas_archive`, `extraction.extraction_path.joinpath`, `extraction.extraction_path.joinpath(*relative_path.split('/')).read_bytes`, `extraction.extraction_path.parent.glob`, `len`, `list`, `payloads.items`, `relative_path.split`, `sha256`, `sha256(b'').hexdigest`, `sha256(payload).hexdigest`, `sorted`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_valid_extraction_cache_is_reused`

- Exact signature: `def test_valid_extraction_cache_is_reused(tmp_path: Path) -> None`
- Parametrization/decorators: none; one collected case.
- Fixtures/inputs: `tmp_path`.
- Protected invariant: Valid extraction cache is reused.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: none directly.
- Expected controlled failures: none; this is an acceptance/output invariant.
- Calls exercised: `_download`, `extract_inpn_protected_areas_archive`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_invalid_extraction_cache_is_rebuilt`

- Exact signature: `def test_invalid_extraction_cache_is_rebuilt(tmp_path: Path, mutation: str) -> None`
- Parametrization/decorators: `pytest.mark.parametrize('mutation', ['same_size_content', 'size', 'missing', 'unexpected', 'file_sha', 'archive_sha', 'archive_size', 'schema', 'schema_bool', 'schema_float', 'unknown', 'boolean_file_size', 'duplicate_key'])`.
- Fixtures/inputs: `tmp_path`, `mutation`.
- Protected invariant: Invalid extraction cache is rebuilt.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: none directly.
- Expected controlled failures: none; this is an acceptance/output invariant.
- Calls exercised: `(first.extraction_path / 'unexpected.txt').write_bytes`, `(refreshed.extraction_path / 'EP' / 'value.txt').read_bytes`, `(refreshed.extraction_path / 'unexpected.txt').exists`, `_download`, `_extraction_metadata_path`, `_read_json`, `_write_json`, `_zip_bytes`, `data_path.stat`, `data_path.unlink`, `data_path.write_bytes`, `encoded.replace`, `extract_inpn_protected_areas_archive`, `isinstance`, `json.dumps`, `len`, `metadata_path.write_text`, `pytest.mark.parametrize`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_first_extraction_publication_failure_leaves_no_half_root`

- Exact signature: `def test_first_extraction_publication_failure_leaves_no_half_root(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None`
- Parametrization/decorators: none; one collected case.
- Fixtures/inputs: `tmp_path`, `monkeypatch`.
- Protected invariant: First extraction publication failure leaves no half root.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: `monkeypatch.setattr(inpn, "_replace_directory", fail_publish)`.
- Expected controlled failures: `pytest.raises(InpnProtectedAreasSourceError, match='publication')`.
- Calls exercised: `OSError`, `_download`, `extract_inpn_protected_areas_archive`, `monkeypatch.setattr`, `original_replace`, `pytest.raises`, `root.exists`, `root.with_name`, `root.with_name(f'{root.name}.bak').exists`, `root.with_name(f'{root.name}.part').exists`, `source.name.endswith`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_extraction_replacement_failure_restores_old_tree`

- Exact signature: `def test_extraction_replacement_failure_restores_old_tree(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None`
- Parametrization/decorators: none; one collected case.
- Fixtures/inputs: `tmp_path`, `monkeypatch`.
- Protected invariant: Extraction replacement failure restores old tree.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: `monkeypatch.setattr(inpn, "_replace_directory", fail_once)`.
- Expected controlled failures: `pytest.raises(InpnProtectedAreasSourceError, match='publication')`.
- Calls exercised: `(first.extraction_path / 'EP' / 'readme.txt').write_bytes`, `OSError`, `_download`, `_tree_snapshot`, `extract_inpn_protected_areas_archive`, `first.extraction_path.with_name`, `first.extraction_path.with_name(f'{first.extraction_path.name}.bak').exists`, `monkeypatch.setattr`, `original_replace`, `pytest.raises`, `source.name.endswith`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_extraction_rollback_failure_preserves_backup`

- Exact signature: `def test_extraction_rollback_failure_preserves_backup(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None`
- Parametrization/decorators: none; one collected case.
- Fixtures/inputs: `tmp_path`, `monkeypatch`.
- Protected invariant: Extraction rollback failure preserves backup.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: `monkeypatch.setattr(inpn, "_replace_directory", fail_publish_and_rollback)`.
- Expected controlled failures: `pytest.raises(InpnProtectedAreasSourceError, match='rollback')`.
- Calls exercised: `(first.extraction_path / 'EP' / 'readme.txt').write_bytes`, `OSError`, `_download`, `_tree_snapshot`, `extract_inpn_protected_areas_archive`, `first.extraction_path.with_name`, `first.extraction_path.with_name(f'{first.extraction_path.name}.part').exists`, `monkeypatch.setattr`, `original_replace`, `pytest.raises`, `source.name.endswith`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_extraction_backup_move_failure_leaves_old_tree_untouched`

- Exact signature: `def test_extraction_backup_move_failure_leaves_old_tree_untouched(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None`
- Parametrization/decorators: none; one collected case.
- Fixtures/inputs: `tmp_path`, `monkeypatch`.
- Protected invariant: Extraction backup move failure leaves old tree untouched.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: `monkeypatch.setattr(inpn, "_replace_directory", fail_backup_move)`.
- Expected controlled failures: `pytest.raises(InpnProtectedAreasSourceError, match='publication|stage')`.
- Calls exercised: `(first.extraction_path / 'EP' / 'readme.txt').write_bytes`, `OSError`, `_download`, `_tree_snapshot`, `backup.exists`, `extract_inpn_protected_areas_archive`, `first.extraction_path.is_dir`, `first.extraction_path.with_name`, `monkeypatch.setattr`, `original_replace`, `pytest.raises`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_extraction_rejects_wrong_download_type`

- Exact signature: `def test_extraction_rejects_wrong_download_type(tmp_path: Path, bad_input: object) -> None`
- Parametrization/decorators: `pytest.mark.parametrize('bad_input', [None, object(), True])`.
- Fixtures/inputs: `tmp_path`, `bad_input`.
- Protected invariant: Extraction rejects wrong download type.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: none directly.
- Expected controlled failures: `pytest.raises(InpnProtectedAreasSourceError, match='download|type')`.
- Calls exercised: `_config`, `extract_inpn_protected_areas_archive`, `object`, `pytest.mark.parametrize`, `pytest.raises`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_extraction_rejects_wrong_config_type`

- Exact signature: `def test_extraction_rejects_wrong_config_type(tmp_path: Path) -> None`
- Parametrization/decorators: none; one collected case.
- Fixtures/inputs: `tmp_path`.
- Protected invariant: Extraction rejects wrong config type.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: none directly.
- Expected controlled failures: `pytest.raises(InpnProtectedAreasSourceError, match='config|type')`.
- Calls exercised: `_download`, `extract_inpn_protected_areas_archive`, `object`, `pytest.raises`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_extraction_cache_setup_failure_is_controlled`

- Exact signature: `def test_extraction_cache_setup_failure_is_controlled(tmp_path: Path) -> None`
- Parametrization/decorators: none; one collected case.
- Fixtures/inputs: `tmp_path`.
- Protected invariant: Extraction cache setup failure is controlled.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: none directly.
- Expected controlled failures: `pytest.raises(InpnProtectedAreasSourceError, match='extract|cache')`.
- Calls exercised: `_download`, `extract_inpn_protected_areas_archive`, `extraction_parent.write_bytes`, `pytest.raises`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_extraction_rejects_stale_download_bytes`

- Exact signature: `def test_extraction_rejects_stale_download_bytes(tmp_path: Path) -> None`
- Parametrization/decorators: none; one collected case.
- Fixtures/inputs: `tmp_path`.
- Protected invariant: Extraction rejects stale download bytes.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: none directly.
- Expected controlled failures: `pytest.raises(InpnProtectedAreasSourceError, match='SHA|size|archive|download')`.
- Calls exercised: `_download`, `_zip_bytes`, `download.path.write_bytes`, `extract_inpn_protected_areas_archive`, `pytest.raises`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_result_dataclasses_are_frozen`

- Exact signature: `def test_result_dataclasses_are_frozen(tmp_path: Path) -> None`
- Parametrization/decorators: none; one collected case.
- Fixtures/inputs: `tmp_path`.
- Protected invariant: Result dataclasses are frozen.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: none directly.
- Expected controlled failures: `pytest.raises(FrozenInstanceError)`.
- Calls exercised: `_download`, `extract_inpn_protected_areas_archive`, `pytest.raises`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_public_api_exports_only_stable_high_level_symbols`

- Exact signature: `def test_public_api_exports_only_stable_high_level_symbols() -> None`
- Parametrization/decorators: none; one collected case.
- Fixtures/inputs: none.
- Protected invariant: Public api exports only stable high level symbols.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: none directly.
- Expected controlled failures: none; this is an acceptance/output invariant.
- Calls exercised: `all`, `getattr`, `hasattr`, `set`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_result_schemas_are_factual_inventory_only`

- Exact signature: `def test_result_schemas_are_factual_inventory_only() -> None`
- Parametrization/decorators: none; one collected case.
- Fixtures/inputs: none.
- Protected invariant: Result schemas are factual inventory only.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: none directly.
- Expected controlled failures: none; this is an acceptance/output invariant.
- Calls exercised: `any`, `fields`, `name.casefold`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_strict_metadata_rejects_boolean_numeric_values_as_cache_hits`

- Exact signature: `def test_strict_metadata_rejects_boolean_numeric_values_as_cache_hits(tmp_path: Path) -> None`
- Parametrization/decorators: none; one collected case.
- Fixtures/inputs: `tmp_path`.
- Protected invariant: Strict metadata rejects boolean numeric values as cache hits.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: none directly.
- Expected controlled failures: none; this is an acceptance/output invariant.
- Calls exercised: `_download`, `_download_metadata_path`, `_download_with_session`, `_read_json`, `_session`, `_write_json`, `len`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_cache_path_binds_version_and_filename`

- Exact signature: `def test_cache_path_binds_version_and_filename(tmp_path: Path) -> None`
- Parametrization/decorators: none; one collected case.
- Fixtures/inputs: `tmp_path`.
- Protected invariant: Cache path binds version and filename.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: none directly.
- Expected controlled failures: none; this is an acceptance/output invariant.
- Calls exercised: `_download`, `_download_metadata_path`, `_read_json`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_download_uses_no_hidden_reference_page_scrape`

- Exact signature: `def test_download_uses_no_hidden_reference_page_scrape(tmp_path: Path) -> None`
- Parametrization/decorators: none; one collected case.
- Fixtures/inputs: `tmp_path`.
- Protected invariant: Download uses no hidden reference page scrape.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: none directly.
- Expected controlled failures: none; this is an acceptance/output invariant.
- Calls exercised: `_config`, `_download_with_session`, `_session`, `str`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_exact_file_inventory_does_not_omit_unknown_suffixes`

- Exact signature: `def test_exact_file_inventory_does_not_omit_unknown_suffixes(tmp_path: Path) -> None`
- Parametrization/decorators: none; one collected case.
- Fixtures/inputs: `tmp_path`.
- Protected invariant: Exact file inventory does not omit unknown suffixes.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: none directly.
- Expected controlled failures: none; this is an acceptance/output invariant.
- Calls exercised: `_download`, `_zip_bytes`, `extract_inpn_protected_areas_archive`, `set`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_archive_and_extraction_cache_reuse_are_independent`

- Exact signature: `def test_archive_and_extraction_cache_reuse_are_independent(tmp_path: Path) -> None`
- Parametrization/decorators: none; one collected case.
- Fixtures/inputs: `tmp_path`.
- Protected invariant: Archive and extraction cache reuse are independent.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: none directly.
- Expected controlled failures: none; this is an acceptance/output invariant.
- Calls exercised: `AssertionError`, `_Session`, `_download`, `_download_with_session`, `extract_inpn_protected_areas_archive`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_no_stale_parts_after_download_or_extraction_success`

- Exact signature: `def test_no_stale_parts_after_download_or_extraction_success(tmp_path: Path) -> None`
- Parametrization/decorators: none; one collected case.
- Fixtures/inputs: `tmp_path`.
- Protected invariant: No stale parts after download or extraction success.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: none directly.
- Expected controlled failures: none; this is an acceptance/output invariant.
- Calls exercised: `Path`, `Path(config.cache_root).rglob`, `_download`, `extract_inpn_protected_areas_archive`, `extraction.extraction_path.is_dir`, `list`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_extraction_revalidation_returns_fresh_source_bound_result`

- Exact signature: `def test_extraction_revalidation_returns_fresh_source_bound_result(tmp_path: Path) -> None`
- Parametrization/decorators: none; one collected case.
- Fixtures/inputs: `tmp_path`.
- Protected invariant: Extraction revalidation returns fresh source bound result.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: none directly.
- Expected controlled failures: none; this is an acceptance/output invariant.
- Calls exercised: `_download`, `extract_inpn_protected_areas_archive`, `validate_inpn_protected_areas_extraction`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_extraction_revalidation_rejects_wrong_type`

- Exact signature: `def test_extraction_revalidation_rejects_wrong_type(tmp_path: Path, bad_extraction: object) -> None`
- Parametrization/decorators: `pytest.mark.parametrize('bad_extraction', [None, object(), True])`.
- Fixtures/inputs: `tmp_path`, `bad_extraction`.
- Protected invariant: Extraction revalidation rejects wrong type.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: none directly.
- Expected controlled failures: `pytest.raises(InpnProtectedAreasSourceError, match='extraction|type')`.
- Calls exercised: `_config`, `object`, `pytest.mark.parametrize`, `pytest.raises`, `validate_inpn_protected_areas_extraction`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_extraction_revalidation_rejects_wrong_path`

- Exact signature: `def test_extraction_revalidation_rejects_wrong_path(tmp_path: Path) -> None`
- Parametrization/decorators: none; one collected case.
- Fixtures/inputs: `tmp_path`.
- Protected invariant: Extraction revalidation rejects wrong path.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: none directly.
- Expected controlled failures: `pytest.raises(InpnProtectedAreasSourceError, match='path|extraction')`.
- Calls exercised: `_download`, `extract_inpn_protected_areas_archive`, `pytest.raises`, `replace`, `validate_inpn_protected_areas_extraction`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_extraction_revalidation_rejects_forged_file_inventory`

- Exact signature: `def test_extraction_revalidation_rejects_forged_file_inventory(tmp_path: Path, mutation: str) -> None`
- Parametrization/decorators: `pytest.mark.parametrize('mutation', ['path', 'size', 'sha256'])`.
- Fixtures/inputs: `tmp_path`, `mutation`.
- Protected invariant: Extraction revalidation rejects forged file inventory.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: none directly.
- Expected controlled failures: `pytest.raises(InpnProtectedAreasSourceError, match='inventory|extraction')`.
- Calls exercised: `_download`, `extract_inpn_protected_areas_archive`, `pytest.mark.parametrize`, `pytest.raises`, `replace`, `validate_inpn_protected_areas_extraction`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_extraction_revalidation_rejects_physical_inventory_mutation`

- Exact signature: `def test_extraction_revalidation_rejects_physical_inventory_mutation(tmp_path: Path, mutation: str) -> None`
- Parametrization/decorators: `pytest.mark.parametrize('mutation', ['missing', 'extra', 'content'])`.
- Fixtures/inputs: `tmp_path`, `mutation`.
- Protected invariant: Extraction revalidation rejects physical inventory mutation.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: none directly.
- Expected controlled failures: `pytest.raises(InpnProtectedAreasSourceError, match='physical|inventory|cache|Extracted')`.
- Calls exercised: `(extraction.extraction_path / 'extra.txt').write_bytes`, `_download`, `extract_inpn_protected_areas_archive`, `extraction.extraction_path.joinpath`, `extraction.files[0].relative_path.split`, `len`, `path.read_bytes`, `path.unlink`, `path.write_bytes`, `pytest.mark.parametrize`, `pytest.raises`, `validate_inpn_protected_areas_extraction`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_extraction_revalidation_rejects_link_or_junction_file`

- Exact signature: `def test_extraction_revalidation_rejects_link_or_junction_file(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None`
- Parametrization/decorators: none; one collected case.
- Fixtures/inputs: `tmp_path`, `monkeypatch`.
- Protected invariant: Extraction revalidation rejects link or junction file.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: `monkeypatch.setattr(inpn, "_is_link_or_junction", simulated_link)`.
- Expected controlled failures: `pytest.raises(InpnProtectedAreasSourceError, match='link|junction|physical')`.
- Calls exercised: `_download`, `extract_inpn_protected_areas_archive`, `extraction.extraction_path.joinpath`, `extraction.files[0].relative_path.split`, `monkeypatch.setattr`, `original`, `pytest.raises`, `validate_inpn_protected_areas_extraction`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_archive_derived_inventory_equals_marker_physical_and_caller`

- Exact signature: `def test_archive_derived_inventory_equals_marker_physical_and_caller(tmp_path: Path) -> None`
- Parametrization/decorators: none; one collected case.
- Fixtures/inputs: `tmp_path`.
- Protected invariant: Archive derived inventory equals marker physical and caller.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: none directly.
- Expected controlled failures: none; this is an acceptance/output invariant.
- Calls exercised: `_download`, `_extraction_metadata_path`, `_read_json`, `_zip_bytes`, `extract_inpn_protected_areas_archive`, `inpn._archive_regular_file_inventory`, `inpn._read_verified_archive_bytes`, `inpn._validated_zip_members`, `io.BytesIO`, `type`, `validate_inpn_protected_areas_extraction`, `zipfile.ZipFile`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_coordinated_marker_physical_and_caller_forgery_cannot_override_archive`

- Exact signature: `def test_coordinated_marker_physical_and_caller_forgery_cannot_override_archive(tmp_path: Path, mutation: str) -> None`
- Parametrization/decorators: `pytest.mark.parametrize('mutation', ['same-size-content', 'size-and-content', 'member-removal', 'member-path'])`.
- Fixtures/inputs: `tmp_path`, `mutation`.
- Protected invariant: Coordinated marker physical and caller forgery cannot override archive.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: none directly.
- Expected controlled failures: `pytest.raises(InpnProtectedAreasSourceError, match='archive|inventory')`.
- Calls exercised: `_download`, `_rewrite_extraction_marker_and_caller`, `_zip_bytes`, `extract_inpn_protected_areas_archive`, `pytest.mark.parametrize`, `pytest.raises`, `target.replace`, `target.stat`, `target.unlink`, `target.with_name`, `target.write_bytes`, `validate_inpn_protected_areas_extraction`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_invalid_coordinated_cache_rebuilds_from_local_archive_without_network`

- Exact signature: `def test_invalid_coordinated_cache_rebuilds_from_local_archive_without_network(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None`
- Parametrization/decorators: none; one collected case.
- Fixtures/inputs: `tmp_path`, `monkeypatch`.
- Protected invariant: Invalid coordinated cache rebuilds from local archive without network.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: `monkeypatch.setattr(inpn, "open_safe_https", forbidden_network)`.
- Expected controlled failures: none; this is an acceptance/output invariant.
- Calls exercised: `AssertionError`, `_download`, `_extraction_metadata_path`, `_read_json`, `_rewrite_extraction_marker_and_caller`, `_zip_bytes`, `extract_inpn_protected_areas_archive`, `monkeypatch.setattr`, `target.read_bytes`, `target.write_bytes`, `validate_inpn_protected_areas_extraction`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

### `test_transient_archive_path_swap_cannot_change_extracted_member_bytes`

- Exact signature: `def test_transient_archive_path_swap_cannot_change_extracted_member_bytes(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None`
- Parametrization/decorators: none; one collected case.
- Fixtures/inputs: `tmp_path`, `monkeypatch`.
- Protected invariant: Transient archive path swap cannot change extracted member bytes.
- Ordered mechanism: constructs or mutates only the local fixture state visible in the exact snapshot, invokes the production boundary, then asserts exact output or controlled rejection.
- Monkeypatch mechanism: `monkeypatch.setattr(inpn, "_validated_zip_members", swap_around_path_validation)`.
- Expected controlled failures: none; this is an acceptance/output invariant.
- Calls exercised: `(extraction.extraction_path / 'EP' / 'a.gpkg').read_bytes`, `_download`, `_zip_bytes`, `download.path.read_bytes`, `extract_inpn_protected_areas_archive`, `isinstance`, `monkeypatch.setattr`, `original`, `source.write_bytes`.
- Regression boundary: factual source/package/catalog evidence only; no category meaning, parcel operations, exclusion, score, or ranking.

## 5. STEP 7F.1B.1.1 coverage map

- Archive suite: immutable archive bytes; same-snapshot member validation/streaming; archive-derived regular-file hashes; four-way equality; coordinated marker/file mutations; archive member byte/size/path/removal mismatches; cache rebuild without network; transient archive-path swap isolation.
- Catalog suite: each package read once; identical built-in bytes supplied to `list_layers`/all `read_info`; transient swap isolation; persistent mutation rejection; required exact `GPKG` driver; schema-2 driver hash binding; schema-1 rejection; exact tuple/float bounds; exact optional CRS strings; independent physical rebuild.
- Zero materialization: production attempts to call `pyogrio.read_dataframe`, `pyogrio.read_arrow`, `geopandas.read_file`, or `geopandas.read_parquet` fail immediately in the regression.
- Semantic non-goals: no protected-area categories, Natura 2000, ZNIEFF, geometry normalization, parcel relation, exclusion, scoring, or ranking.

## 6. Exact complete current file content

This snapshot reproduces every current test line; the raw-byte SHA above is the binding authority.

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


def _rewrite_extraction_marker_and_caller(
    extraction: InpnProtectedAreasExtraction,
) -> InpnProtectedAreasExtraction:
    marker_path = _extraction_metadata_path(extraction)
    marker = _read_json(marker_path)
    files = tuple(
        InpnProtectedAreasExtractedFile(
            relative_path=path.relative_to(extraction.extraction_path).as_posix(),
            file_size=path.stat().st_size,
            sha256=sha256(path.read_bytes()).hexdigest(),
        )
        for path in sorted(extraction.extraction_path.rglob("*"))
        if path.is_file() and path != marker_path
    )
    marker["files"] = [
        {
            "relative_path": item.relative_path,
            "file_size": item.file_size,
            "sha256": item.sha256,
        }
        for item in files
    ]
    _write_json(marker_path, marker)
    return replace(extraction, files=files)


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


def test_archive_derived_inventory_equals_marker_physical_and_caller(
    tmp_path: Path,
) -> None:
    archive = _zip_bytes(
        {
            "EP/a.gpkg": b"first-package",
            "EP/nested/b.gpkg": b"second-package",
        }
    )
    config, download, _ = _download(tmp_path, payload=archive)
    extraction = extract_inpn_protected_areas_archive(download, config)

    archive_bytes = inpn._read_verified_archive_bytes(download, config)
    with zipfile.ZipFile(io.BytesIO(archive_bytes)) as opened:
        members = inpn._validated_zip_members(opened)
        archive_files = inpn._archive_regular_file_inventory(opened, members)
    fresh = validate_inpn_protected_areas_extraction(extraction, config)
    marker = _read_json(_extraction_metadata_path(extraction))

    assert type(archive_bytes) is bytes
    assert archive_files == fresh.files == extraction.files
    assert marker["files"] == [
        {
            "relative_path": item.relative_path,
            "file_size": item.file_size,
            "sha256": item.sha256,
        }
        for item in archive_files
    ]


@pytest.mark.parametrize(
    "mutation",
    ["same-size-content", "size-and-content", "member-removal", "member-path"],
)
def test_coordinated_marker_physical_and_caller_forgery_cannot_override_archive(
    tmp_path: Path,
    mutation: str,
) -> None:
    archive = _zip_bytes(
        {
            "EP/a.gpkg": b"archive-authority-a",
            "EP/b.gpkg": b"archive-authority-b",
        }
    )
    config, download, _ = _download(tmp_path, payload=archive)
    extraction = extract_inpn_protected_areas_archive(download, config)
    target = extraction.extraction_path / "EP" / "a.gpkg"
    if mutation == "same-size-content":
        target.write_bytes(b"x" * target.stat().st_size)
    elif mutation == "size-and-content":
        target.write_bytes(b"different-size")
    elif mutation == "member-removal":
        target.unlink()
    else:
        target.replace(target.with_name("renamed.gpkg"))
    forged = _rewrite_extraction_marker_and_caller(extraction)

    with pytest.raises(InpnProtectedAreasSourceError, match="archive|inventory"):
        validate_inpn_protected_areas_extraction(forged, config)


def test_invalid_coordinated_cache_rebuilds_from_local_archive_without_network(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    expected = b"archive-member-bytes"
    archive = _zip_bytes({"EP/a.gpkg": expected})
    config, download, _ = _download(tmp_path, payload=archive)
    extraction = extract_inpn_protected_areas_archive(download, config)
    target = extraction.extraction_path / "EP" / "a.gpkg"
    target.write_bytes(b"forged-member-bytes")
    _rewrite_extraction_marker_and_caller(extraction)

    def forbidden_network(*args: object, **kwargs: object) -> Any:
        raise AssertionError("network called while rebuilding from local archive")

    monkeypatch.setattr(inpn, "open_safe_https", forbidden_network)
    rebuilt = extract_inpn_protected_areas_archive(download, config)
    fresh = validate_inpn_protected_areas_extraction(rebuilt, config)

    assert rebuilt.cache_hit is False
    assert target.read_bytes() == expected
    assert fresh.files == rebuilt.files
    marker = _read_json(_extraction_metadata_path(rebuilt))
    assert marker["files"] == [
        {
            "relative_path": item.relative_path,
            "file_size": item.file_size,
            "sha256": item.sha256,
        }
        for item in fresh.files
    ]


def test_transient_archive_path_swap_cannot_change_extracted_member_bytes(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    expected_member = b"package-a"
    archive_a = _zip_bytes({"EP/a.gpkg": expected_member})
    archive_b = _zip_bytes({"EP/a.gpkg": b"package-b"})
    config, download, _ = _download(tmp_path, payload=archive_a)
    original = inpn._validated_zip_members
    path_calls = 0

    def swap_around_path_validation(
        source: Path | zipfile.ZipFile,
    ) -> tuple[inpn._ValidatedZipMember, ...]:
        nonlocal path_calls
        result = original(source)
        if isinstance(source, Path):
            path_calls += 1
            if path_calls == 1:
                source.write_bytes(archive_b)
            elif path_calls == 2:
                source.write_bytes(archive_a)
        return result

    monkeypatch.setattr(inpn, "_validated_zip_members", swap_around_path_validation)
    extraction = extract_inpn_protected_areas_archive(download, config)

    assert (
        extraction.extraction_path / "EP" / "a.gpkg"
    ).read_bytes() == expected_member
    assert download.path.read_bytes() == archive_a
```

# `tests/unit/test_cadastre_fr.py`

## File identity

- Repository path: `tests/unit/test_cadastre_fr.py`
- File type: Python test
- Primary responsibility: Provides complete unit and regression coverage for the `cadastre_fr` contracts exercised in this file.
- Layer / domain: `unit/regression test` / `test`
- Public or internal role: Internal test support; not a production API.
- Source SHA256: `07f5bc37cf8d7fca0fa8c1a88ab19528c0717139d5a581d52c1fe20644d74eb5`

## 1. Purpose

Provides complete unit and regression coverage for the `cadastre_fr` contracts exercised in this file.

## 2. Position in LandScout architecture

This file is a `unit/regression test` artifact in the `test` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `import gzip` — required by the implementation paths and symbols documented below.
- `import io` — required by the implementation paths and symbols documented below.
- `import json` — required by the implementation paths and symbols documented below.
- `from datetime import UTC, datetime, timedelta` — required by the implementation paths and symbols documented below.
- `from hashlib import sha256` — required by the implementation paths and symbols documented below.
- `from pathlib import Path` — required by the implementation paths and symbols documented below.
- `from urllib.error import HTTPError` — required by the implementation paths and symbols documented below.

### Third-party

- `from unittest.mock import patch` — required by the implementation paths and symbols documented below.
- `import pytest` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout.sources import cadastre_fr` — required by the implementation paths and symbols documented below.
- `from landscout.sources.cadastre_fr import ( CadastreDownloadError, _is_valid_gzip, build_cadastre_parcelles_url, download_cadastre_parcelles, )` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `COMMUNE_CODE` | `"31395"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `EXPECTED_URL` | `"https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes/" "31/31395/cadastre-31395-parcelles.json.gz"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `ARCHIVE_CONTENT` | `gzip.compress(b'{"type":"FeatureCollection","features":[]}')` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `REFRESHED_ARCHIVE_CONTENT` | `gzip.compress( b'{"type":"FeatureCollection","features":[{"type":"Feature"}]}' )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `CORRUPTED_ARCHIVE_CONTENT` | `ARCHIVE_CONTENT[:-8]` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

No class, model, or dataclass is declared in this file.

## 6. Functions and methods

### `_set_cache_age`

**Signature**

```python
def _set_cache_age(metadata_path: Path, age: timedelta) -> None:
```

**Purpose**

Implements set cache age according to the exact implementation and guards in this file.

**Inputs**

- `metadata_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `age` (`timedelta`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `metadata` from `json.loads(metadata_path.read_text(encoding='utf-8'))`.
2. Computes `metadata['download_timestamp']` from `(datetime.now(UTC) - age).isoformat()`.
3. Calls `metadata_path.write_text(json.dumps(metadata), encoding='utf-8')` for its validation or side effect.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `metadata_path.read_text`, `metadata_path.write_text`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `(datetime.now(UTC) - age).isoformat`, `datetime.now`, `json.dumps`, `json.loads`, `metadata_path.read_text`, `metadata_path.write_text`.

**Known repository callers**

- `tests/unit/test_cadastre_fr.py` — `test_cleanup_failure_does_not_mask_double_failure_recovery_error`
- `tests/unit/test_cadastre_fr.py` — `test_corrupted_new_download_preserves_existing_archive`
- `tests/unit/test_cadastre_fr.py` — `test_expired_cache_is_downloaded_again`
- `tests/unit/test_cadastre_fr.py` — `test_failed_refresh_preserves_cached_archive`
- `tests/unit/test_cadastre_fr.py` — `test_metadata_publication_failure_restores_previous_cache_pair`
- `tests/unit/test_cadastre_fr.py` — `test_next_run_after_double_failure_preserves_recovery_before_network`
- `tests/unit/test_cadastre_fr.py` — `test_publication_and_rollback_failure_preserves_recovery_backup`

**Tests**

- `tests/unit/test_cadastre_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error`
- `tests/unit/test_cadastre_fr.py::test_corrupted_new_download_preserves_existing_archive`
- `tests/unit/test_cadastre_fr.py::test_expired_cache_is_downloaded_again`
- `tests/unit/test_cadastre_fr.py::test_failed_refresh_preserves_cached_archive`
- `tests/unit/test_cadastre_fr.py::test_metadata_publication_failure_restores_previous_cache_pair`
- `tests/unit/test_cadastre_fr.py::test_next_run_after_double_failure_preserves_recovery_before_network`
- `tests/unit/test_cadastre_fr.py::test_publication_and_rollback_failure_preserves_recovery_backup`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_update_metadata_integrity`

**Signature**

```python
def _update_metadata_integrity(metadata_path: Path, archive_path: Path) -> None:
```

**Purpose**

Implements update metadata integrity according to the exact implementation and guards in this file.

**Inputs**

- `metadata_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `archive_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `metadata` from `json.loads(metadata_path.read_text(encoding='utf-8'))`.
2. Computes `content` from `archive_path.read_bytes()`.
3. Computes `metadata['file_size']` from `len(content)`.
4. Computes `metadata['sha256']` from `sha256(content).hexdigest()`.
5. Calls `metadata_path.write_text(json.dumps(metadata), encoding='utf-8')` for its validation or side effect.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `archive_path.read_bytes`, `metadata_path.read_text`, `metadata_path.write_text`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `archive_path.read_bytes`, `json.dumps`, `json.loads`, `len`, `metadata_path.read_text`, `metadata_path.write_text`, `sha256`, `sha256(content).hexdigest`.

**Known repository callers**

- `tests/unit/test_cadastre_fr.py` — `test_corrupted_cached_archive_triggers_fresh_download`

**Tests**

- `tests/unit/test_cadastre_fr.py::test_corrupted_cached_archive_triggers_fresh_download`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_metadata_publication_failure_restores_previous_cache_pair.fail_metadata_publication`

**Signature**

```python
def fail_metadata_publication(source: Path, target: Path) -> None:
```

**Purpose**

Implements fail metadata publication according to the exact implementation and guards in this file.

**Inputs**

- `source` (`Path`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `target` (`Path`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `source == temporary_metadata and target == metadata_path`. When true: Raises `OSError('simulated metadata publication failure')`.
2. Calls `original_replace(source, target)` for its validation or side effect.

**Validation and invariants**

- Rejects or diverts the path when `source == temporary_metadata and target == metadata_path` is true.

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

### `test_first_metadata_publication_failure_leaves_no_half_pair.fail_metadata_publication`

**Signature**

```python
def fail_metadata_publication(source: Path, target: Path) -> None:
```

**Purpose**

Implements fail metadata publication according to the exact implementation and guards in this file.

**Inputs**

- `source` (`Path`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `target` (`Path`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `source == temporary_metadata and target == metadata_path`. When true: Raises `OSError('simulated metadata publication failure')`.
2. Calls `original_replace(source, target)` for its validation or side effect.

**Validation and invariants**

- Rejects or diverts the path when `source == temporary_metadata and target == metadata_path` is true.

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

### `test_publication_and_rollback_failure_preserves_recovery_backup.fail_publication_and_rollback`

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

1. Checks `source == temporary_metadata and target == metadata_path`. When true: Raises `OSError('publication failure')`.
2. Checks `rollback_target == 'archive' and source == archive_backup`. When true: Raises `OSError('archive rollback failure')`.
3. Checks `rollback_target == 'metadata' and source == metadata_backup`. When true: Raises `OSError('metadata rollback failure')`.
4. Calls `original_replace(source, target)` for its validation or side effect.

**Validation and invariants**

- Rejects or diverts the path when `source == temporary_metadata and target == metadata_path` is true.
- Rejects or diverts the path when `rollback_target == 'archive' and source == archive_backup` is true.
- Rejects or diverts the path when `rollback_target == 'metadata' and source == metadata_backup` is true.

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

### `test_next_run_after_double_failure_preserves_recovery_before_network.fail_publication_and_rollback`

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

1. Checks `source == temporary_metadata and target == metadata_path`. When true: Raises `OSError('publication failed')`.
2. Checks `source == archive_backup and target == first.path`. When true: Raises `OSError('rollback failed')`.
3. Calls `original_replace(source, target)` for its validation or side effect.

**Validation and invariants**

- Rejects or diverts the path when `source == temporary_metadata and target == metadata_path` is true.
- Rejects or diverts the path when `source == archive_backup and target == first.path` is true.

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

### `test_temporary_link_or_junction_cannot_modify_target_before_network.simulated_is_symlink`

**Signature**

```python
def simulated_is_symlink(path: Path) -> bool:
```

**Purpose**

Implements simulated is symlink according to the exact implementation and guards in this file.

**Inputs**

- `path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bool`. Observed return expression(s): `link_kind == 'symlink' and path == unsafe_path or original_is_symlink(path)`.

**Algorithm**

1. Returns `link_kind == 'symlink' and path == unsafe_path or original_is_symlink(path)`.

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

### `test_temporary_link_or_junction_cannot_modify_target_before_network.simulated_is_junction`

**Signature**

```python
def simulated_is_junction(path: Path) -> bool:
```

**Purpose**

Implements simulated is junction according to the exact implementation and guards in this file.

**Inputs**

- `path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bool`. Observed return expression(s): `link_kind == 'junction' and path == unsafe_path or original_is_junction(path)`.

**Algorithm**

1. Returns `link_kind == 'junction' and path == unsafe_path or original_is_junction(path)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `original_is_junction`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_temporary_link_or_junction_cannot_modify_target_before_network.simulated_symlink_open`

**Signature**

```python
def simulated_symlink_open(
        path: Path, *args: object, **kwargs: object
    ) -> object:
```

**Purpose**

Implements simulated symlink open according to the exact implementation and guards in this file.

**Inputs**

- `path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `object`. Observed return expression(s): `original_open(path, *args, **kwargs)`; `original_open(sentinel, *args, **kwargs)`.

**Algorithm**

1. Checks `path == unsafe_path`. When true: Returns `original_open(sentinel, *args, **kwargs)`.
2. Returns `original_open(path, *args, **kwargs)`.

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

### `test_temporary_link_or_junction_cannot_modify_target_before_network.record_network`

**Signature**

```python
def record_network(*args: object, **kwargs: object) -> io.BytesIO:
```

**Purpose**

Implements record network according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `io.BytesIO`. Observed return expression(s): `io.BytesIO(ARCHIVE_CONTENT)`.

**Algorithm**

1. Executes `nonlocal network_calls`.
2. Updates `network_calls` using `` and `1`.
3. Returns `io.BytesIO(ARCHIVE_CONTENT)`.

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

### `test_broken_recovery_symlink_is_rejected_before_network.simulated_is_symlink`

**Signature**

```python
def simulated_is_symlink(path: Path) -> bool:
```

**Purpose**

Implements simulated is symlink according to the exact implementation and guards in this file.

**Inputs**

- `path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bool`. Observed return expression(s): `path == recovery_path or original_is_symlink(path)`.

**Algorithm**

1. Returns `path == recovery_path or original_is_symlink(path)`.

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

### `test_broken_recovery_symlink_is_rejected_before_network.fail_network`

**Signature**

```python
def fail_network(*args: object, **kwargs: object) -> io.BytesIO:
```

**Purpose**

Implements fail network according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `io.BytesIO`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Executes `nonlocal network_calls`.
2. Updates `network_calls` using `` and `1`.
3. Raises `AssertionError('broken recovery link must fail before network')`.

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

### `test_cleanup_failure_does_not_mask_double_failure_recovery_error.fail_publication_and_rollback`

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

1. Executes `nonlocal rollback_failed`.
2. Checks `source == temporary_metadata and target == metadata_path`. When true: Raises `OSError('publication failed')`.
3. Checks `source == archive_backup and target == first.path`. When true: Computes `rollback_failed` from `True`. Raises `OSError('rollback failed')`.
4. Calls `original_replace(source, target)` for its validation or side effect.

**Validation and invariants**

- Rejects or diverts the path when `source == temporary_metadata and target == metadata_path` is true.
- Rejects or diverts the path when `source == archive_backup and target == first.path` is true.

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

### `test_cleanup_failure_does_not_mask_double_failure_recovery_error.fail_temporary_cleanup`

**Signature**

```python
def fail_temporary_cleanup(path: Path, *, missing_ok: bool = False) -> None:
```

**Purpose**

Implements fail temporary cleanup according to the exact implementation and guards in this file.

**Inputs**

- `path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `missing_ok` (`bool`; optional/default `False`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `rollback_failed and path == temporary_metadata`. When true: Raises `PermissionError('temporary cleanup failed')`.
2. Calls `original_unlink(path, missing_ok=missing_ok)` for its validation or side effect.

**Validation and invariants**

- Rejects or diverts the path when `rollback_failed and path == temporary_metadata` is true.

**Exceptions**

- Explicitly raises: `PermissionError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `original_unlink`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `PermissionError`, `original_unlink`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_build_cadastre_parcelles_url`

**Signature**

```python
def test_build_cadastre_parcelles_url() -> None:
```

**Purpose**

Protects the `build cadastre parcelles url` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 0 explicit setup/context statement(s).

**Action**

- Calls `build_cadastre_parcelles_url`.

**Expected result**

- Direct assertions: `assert build_cadastre_parcelles_url(COMMUNE_CODE) == EXPECTED_URL`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `build cadastre parcelles url` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `build_cadastre_parcelles_url`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_successful_download`

**Signature**

```python
def test_successful_download(tmp_path: Path) -> None:
```

**Purpose**

Protects the `successful download` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 3 explicit setup/context statement(s).
- Enters managed context(s) `patch('landscout.sources.cadastre_fr.open_safe_https', return_value=io.BytesIO(ARCHIVE_CONTENT))` and executes: Computes `result` from `download_cadastre_parcelles(COMMUNE_CODE, tmp_path)`.
- Computes `metadata_path` from `tmp_path / f'{result.filename}.metadata.json'`.
- Computes `metadata` from `json.loads(metadata_path.read_text(encoding='utf-8'))`.

**Action**

- Calls `download_cadastre_parcelles`, `io.BytesIO`, `json.loads`, `metadata_path.read_text`, `result.path.read_bytes`.

**Expected result**

- Direct assertions: `assert result.path.read_bytes() == ARCHIVE_CONTENT`; `assert result.source_url == EXPECTED_URL`; `assert result.file_size == len(ARCHIVE_CONTENT)`; `assert result.cache_hit is False`; `assert metadata['download_timestamp'] == result.download_timestamp`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `successful download` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `download_cadastre_parcelles`, `io.BytesIO`, `json.loads`, `len`, `metadata_path.read_text`, `patch`, `result.path.read_bytes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_fresh_cache_is_reused`

**Signature**

```python
def test_fresh_cache_is_reused(tmp_path: Path) -> None:
```

**Purpose**

Protects the `fresh cache is reused` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `patch('landscout.sources.cadastre_fr.open_safe_https', return_value=io.BytesIO(ARCHIVE_CONTENT))` and executes: Computes `first` from `download_cadastre_parcelles(COMMUNE_CODE, tmp_path)`. Computes `second` from `download_cadastre_parcelles(COMMUNE_CODE, tmp_path)`.

**Action**

- Calls `download_cadastre_parcelles`, `io.BytesIO`.

**Expected result**

- Direct assertions: `assert opener.call_count == 1`; `assert first.cache_hit is False`; `assert second.cache_hit is True`; `assert second.sha256 == first.sha256`; `assert second.download_timestamp == first.download_timestamp`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `fresh cache is reused` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `download_cadastre_parcelles`, `io.BytesIO`, `patch`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_expired_cache_is_downloaded_again`

**Signature**

```python
def test_expired_cache_is_downloaded_again(tmp_path: Path) -> None:
```

**Purpose**

Protects the `expired cache is downloaded again` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `patch('landscout.sources.cadastre_fr.open_safe_https', side_effect=[io.BytesIO(ARCHIVE_CONTENT), io.BytesIO(REFRESHED_ARCHIVE_CONTENT)])` and executes: Computes `first` from `download_cadastre_parcelles(COMMUNE_CODE, tmp_path)`. Computes `metadata_path` from `tmp_path / f'{first.filename}.metadata.json'`. Calls `_set_cache_age(metadata_path, timedelta(hours=169))` for its validation or side effect. Computes `refreshed` from `download_cadastre_parcelles(COMMUNE_CODE, tmp_path)`.

**Action**

- Calls `_set_cache_age`, `download_cadastre_parcelles`, `io.BytesIO`, `refreshed.path.read_bytes`, `sha256`, `sha256(REFRESHED_ARCHIVE_CONTENT).hexdigest`, `timedelta`.

**Expected result**

- Direct assertions: `assert opener.call_count == 2`; `assert refreshed.cache_hit is False`; `assert refreshed.path.read_bytes() == REFRESHED_ARCHIVE_CONTENT`; `assert refreshed.sha256 == sha256(REFRESHED_ARCHIVE_CONTENT).hexdigest()`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `expired cache is downloaded again` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_set_cache_age`, `download_cadastre_parcelles`, `io.BytesIO`, `patch`, `refreshed.path.read_bytes`, `sha256`, `sha256(REFRESHED_ARCHIVE_CONTENT).hexdigest`, `timedelta`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_failed_refresh_preserves_cached_archive`

**Signature**

```python
def test_failed_refresh_preserves_cached_archive(tmp_path: Path) -> None:
```

**Purpose**

Protects the `failed refresh preserves cached archive` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 5 explicit setup/context statement(s).
- Enters managed context(s) `patch('landscout.sources.cadastre_fr.open_safe_https', return_value=io.BytesIO(ARCHIVE_CONTENT))` and executes: Computes `first` from `download_cadastre_parcelles(COMMUNE_CODE, tmp_path)`.
- Computes `original_archive` from `first.path.read_bytes()`.
- Computes `metadata_path` from `tmp_path / f'{first.filename}.metadata.json'`.
- Computes `error` from `HTTPError(EXPECTED_URL, 503, 'Unavailable', hdrs=None, fp=None)`.
- Enters managed context(s) `patch('landscout.sources.cadastre_fr.open_safe_https', side_effect=error), pytest.raises(CadastreDownloadError)` and executes: Calls `download_cadastre_parcelles(COMMUNE_CODE, tmp_path)` for its validation or side effect.

**Action**

- Calls `HTTPError`, `_set_cache_age`, `download_cadastre_parcelles`, `first.path.read_bytes`, `io.BytesIO`, `metadata_path.is_file`, `timedelta`.

**Expected result**

- Direct assertions: `assert first.path.read_bytes() == original_archive`; `assert metadata_path.is_file()`.
- Expected exception contexts: `with patch('landscout.sources.cadastre_fr.open_safe_https', side_effect=error), pytest.raises(CadastreDownloadError): download_cadastre_parcelles(COMMUNE_CODE, tmp_path)`.

**Regression protected**

- Protects the exact `failed refresh preserves cached archive` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `HTTPError`, `_set_cache_age`, `download_cadastre_parcelles`, `first.path.read_bytes`, `io.BytesIO`, `metadata_path.is_file`, `patch`, `pytest.raises`, `timedelta`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_failed_http_response`

**Signature**

```python
def test_failed_http_response(tmp_path: Path) -> None:
```

**Purpose**

Protects the `failed http response` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 2 explicit setup/context statement(s).
- Computes `error` from `HTTPError(EXPECTED_URL, 404, 'Not Found', hdrs=None, fp=None)`.
- Enters managed context(s) `patch('landscout.sources.cadastre_fr.open_safe_https', side_effect=error), pytest.raises(CadastreDownloadError)` and executes: Calls `download_cadastre_parcelles(COMMUNE_CODE, tmp_path)` for its validation or side effect.

**Action**

- Calls `HTTPError`, `download_cadastre_parcelles`, `tmp_path.glob`.

**Expected result**

- Direct assertions: `assert not list(tmp_path.glob('*'))`.
- Expected exception contexts: `with patch('landscout.sources.cadastre_fr.open_safe_https', side_effect=error), pytest.raises(CadastreDownloadError): download_cadastre_parcelles(COMMUNE_CODE, tmp_path)`.

**Regression protected**

- Protects the exact `failed http response` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `HTTPError`, `download_cadastre_parcelles`, `list`, `patch`, `pytest.raises`, `tmp_path.glob`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_checksum_generation`

**Signature**

```python
def test_checksum_generation(tmp_path: Path) -> None:
```

**Purpose**

Protects the `checksum generation` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `patch('landscout.sources.cadastre_fr.open_safe_https', return_value=io.BytesIO(ARCHIVE_CONTENT))` and executes: Computes `result` from `download_cadastre_parcelles(COMMUNE_CODE, tmp_path)`.

**Action**

- Calls `download_cadastre_parcelles`, `io.BytesIO`, `sha256`, `sha256(ARCHIVE_CONTENT).hexdigest`.

**Expected result**

- Direct assertions: `assert result.sha256 == sha256(ARCHIVE_CONTENT).hexdigest()`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `checksum generation` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `download_cadastre_parcelles`, `io.BytesIO`, `patch`, `sha256`, `sha256(ARCHIVE_CONTENT).hexdigest`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_valid_gzip_is_accepted`

**Signature**

```python
def test_valid_gzip_is_accepted(tmp_path: Path) -> None:
```

**Purpose**

Protects the `valid gzip is accepted` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 1 explicit setup/context statement(s).
- Computes `archive_path` from `tmp_path / 'valid.json.gz'`.

**Action**

- Calls `_is_valid_gzip`, `archive_path.write_bytes`.

**Expected result**

- Direct assertions: `assert _is_valid_gzip(archive_path)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `valid gzip is accepted` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_is_valid_gzip`, `archive_path.write_bytes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_truncated_gzip_is_rejected`

**Signature**

```python
def test_truncated_gzip_is_rejected(tmp_path: Path) -> None:
```

**Purpose**

Protects the `truncated gzip is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 1 explicit setup/context statement(s).
- Computes `archive_path` from `tmp_path / 'truncated.json.gz'`.

**Action**

- Calls `_is_valid_gzip`, `archive_path.write_bytes`.

**Expected result**

- Direct assertions: `assert not _is_valid_gzip(archive_path)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `truncated gzip is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_is_valid_gzip`, `archive_path.write_bytes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_corrupted_cached_archive_triggers_fresh_download`

**Signature**

```python
def test_corrupted_cached_archive_triggers_fresh_download(tmp_path: Path) -> None:
```

**Purpose**

Protects the `corrupted cached archive triggers fresh download` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `patch('landscout.sources.cadastre_fr.open_safe_https', side_effect=[io.BytesIO(ARCHIVE_CONTENT), io.BytesIO(REFRESHED_ARCHIVE_CONTENT)])` and executes: Computes `first` from `download_cadastre_parcelles(COMMUNE_CODE, tmp_path)`. Computes `metadata_path` from `tmp_path / f'{first.filename}.metadata.json'`. Calls `first.path.write_bytes(CORRUPTED_ARCHIVE_CONTENT)` for its validation or side effect. Calls `_update_metadata_integrity(metadata_path, first.path)` for its validation or side effect. Executes 1 additional source-ordered statement(s).

**Action**

- Calls `_update_metadata_integrity`, `download_cadastre_parcelles`, `first.path.write_bytes`, `io.BytesIO`, `refreshed.path.read_bytes`.

**Expected result**

- Direct assertions: `assert opener.call_count == 2`; `assert refreshed.cache_hit is False`; `assert refreshed.path.read_bytes() == REFRESHED_ARCHIVE_CONTENT`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `corrupted cached archive triggers fresh download` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_update_metadata_integrity`, `download_cadastre_parcelles`, `first.path.write_bytes`, `io.BytesIO`, `patch`, `refreshed.path.read_bytes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_corrupted_new_download_preserves_existing_archive`

**Signature**

```python
def test_corrupted_new_download_preserves_existing_archive(tmp_path: Path) -> None:
```

**Purpose**

Protects the `corrupted new download preserves existing archive` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 4 explicit setup/context statement(s).
- Enters managed context(s) `patch('landscout.sources.cadastre_fr.open_safe_https', return_value=io.BytesIO(ARCHIVE_CONTENT))` and executes: Computes `first` from `download_cadastre_parcelles(COMMUNE_CODE, tmp_path)`.
- Computes `original_archive` from `first.path.read_bytes()`.
- Computes `metadata_path` from `tmp_path / f'{first.filename}.metadata.json'`.
- Enters managed context(s) `patch('landscout.sources.cadastre_fr.open_safe_https', return_value=io.BytesIO(CORRUPTED_ARCHIVE_CONTENT)), pytest.raises(CadastreDownloadError)` and executes: Calls `download_cadastre_parcelles(COMMUNE_CODE, tmp_path)` for its validation or side effect.

**Action**

- Calls `_set_cache_age`, `download_cadastre_parcelles`, `first.path.read_bytes`, `io.BytesIO`, `timedelta`, `tmp_path.glob`.

**Expected result**

- Direct assertions: `assert first.path.read_bytes() == original_archive`; `assert not list(tmp_path.glob('*.part'))`.
- Expected exception contexts: `with patch('landscout.sources.cadastre_fr.open_safe_https', return_value=io.BytesIO(CORRUPTED_ARCHIVE_CONTENT)), pytest.raises(CadastreDownloadError): download_cadastre_parcelles(COMMUNE_CODE, tmp_path)`.

**Regression protected**

- Protects the exact `corrupted new download preserves existing archive` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_set_cache_age`, `download_cadastre_parcelles`, `first.path.read_bytes`, `io.BytesIO`, `list`, `patch`, `pytest.raises`, `timedelta`, `tmp_path.glob`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_corsica_cadastre_urls_are_canonical`

**Signature**

```python
def test_corsica_cadastre_urls_are_canonical(code: str, department: str) -> None:
```

**Purpose**

Protects the `corsica cadastre urls are canonical` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `code`, `department`.
- Contains 1 explicit setup/context statement(s).
- Computes `url` from `build_cadastre_parcelles_url(code)`.

**Action**

- Calls `build_cadastre_parcelles_url`.

**Expected result**

- Direct assertions: `assert f'/{department}/{code}/cadastre-{code}-parcelles.json.gz' in url`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `corsica cadastre urls are canonical` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `build_cadastre_parcelles_url`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_noncanonical_commune_code_is_controlled`

**Signature**

```python
def test_noncanonical_commune_code_is_controlled(code: object) -> None:
```

**Purpose**

Protects the `noncanonical commune code is controlled` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `code`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises((TypeError, ValueError), match='Commune code')` and executes: Calls `build_cadastre_parcelles_url(code)` for its validation or side effect.

**Action**

- Calls `build_cadastre_parcelles_url`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises((TypeError, ValueError), match='Commune code'): build_cadastre_parcelles_url(code)`.

**Regression protected**

- Protects the exact `noncanonical commune code is controlled` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `build_cadastre_parcelles_url`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_download_timeout_is_strict_finite_positive`

**Signature**

```python
def test_download_timeout_is_strict_finite_positive(
    tmp_path: Path,
    timeout: object,
) -> None:
```

**Purpose**

Protects the `download timeout is strict finite positive` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `timeout`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(ValueError, match='timeout')` and executes: Calls `download_cadastre_parcelles(COMMUNE_CODE, tmp_path, timeout=timeout)` for its validation or side effect.

**Action**

- Calls `download_cadastre_parcelles`, `float`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValueError, match='timeout'): download_cadastre_parcelles(COMMUNE_CODE, tmp_path, timeout=timeout)`.

**Regression protected**

- Protects the exact `download timeout is strict finite positive` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `download_cadastre_parcelles`, `float`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_cache_age_is_strict_finite_nonnegative`

**Signature**

```python
def test_cache_age_is_strict_finite_nonnegative(
    tmp_path: Path,
    max_age: object,
) -> None:
```

**Purpose**

Protects the `cache age is strict finite nonnegative` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `max_age`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(ValueError, match='max_cache_age_hours')` and executes: Calls `download_cadastre_parcelles(COMMUNE_CODE, tmp_path, max_cache_age_hours=max_age)` for its validation or side effect.

**Action**

- Calls `download_cadastre_parcelles`, `float`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValueError, match='max_cache_age_hours'): download_cadastre_parcelles(COMMUNE_CODE, tmp_path, max_cache_age_hours=max_age)`.

**Regression protected**

- Protects the exact `cache age is strict finite nonnegative` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `download_cadastre_parcelles`, `float`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_malformed_cached_metadata_triggers_refresh`

**Signature**

```python
def test_malformed_cached_metadata_triggers_refresh(
    tmp_path: Path,
    field: str,
) -> None:
```

**Purpose**

Protects the `malformed cached metadata triggers refresh` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `field`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `patch('landscout.sources.cadastre_fr.open_safe_https', side_effect=[io.BytesIO(ARCHIVE_CONTENT), io.BytesIO(REFRESHED_ARCHIVE_CONTENT)])` and executes: Computes `first` from `download_cadastre_parcelles(COMMUNE_CODE, tmp_path)`. Computes `metadata_path` from `tmp_path / f'{first.filename}.metadata.json'`. Computes `metadata` from `json.loads(metadata_path.read_text(encoding='utf-8'))`. Computes `metadata[field]` from `{'file_size': first.file_size + 1, 'sha256': '0' * 64, 'download_timestamp': 'not-a-timestamp'}[field]`. Executes 2 additional source-ordered statement(s).

**Action**

- Calls `download_cadastre_parcelles`, `io.BytesIO`, `json.dumps`, `json.loads`, `metadata_path.read_text`, `metadata_path.write_text`, `refreshed.path.read_bytes`.

**Expected result**

- Direct assertions: `assert opener.call_count == 2`; `assert refreshed.path.read_bytes() == REFRESHED_ARCHIVE_CONTENT`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `malformed cached metadata triggers refresh` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `download_cadastre_parcelles`, `io.BytesIO`, `json.dumps`, `json.loads`, `metadata_path.read_text`, `metadata_path.write_text`, `patch`, `pytest.mark.parametrize`, `refreshed.path.read_bytes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_future_cached_timestamp_triggers_refresh`

**Signature**

```python
def test_future_cached_timestamp_triggers_refresh(tmp_path: Path) -> None:
```

**Purpose**

Protects the `future cached timestamp triggers refresh` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `patch('landscout.sources.cadastre_fr.open_safe_https', side_effect=[io.BytesIO(ARCHIVE_CONTENT), io.BytesIO(REFRESHED_ARCHIVE_CONTENT)])` and executes: Computes `first` from `download_cadastre_parcelles(COMMUNE_CODE, tmp_path)`. Computes `metadata_path` from `tmp_path / f'{first.filename}.metadata.json'`. Computes `metadata` from `json.loads(metadata_path.read_text(encoding='utf-8'))`. Computes `metadata['download_timestamp']` from `(datetime.now(UTC) + timedelta(hours=1)).isoformat()`. Executes 2 additional source-ordered statement(s).

**Action**

- Calls `(datetime.now(UTC) + timedelta(hours=1)).isoformat`, `datetime.now`, `download_cadastre_parcelles`, `io.BytesIO`, `json.dumps`, `json.loads`, `metadata_path.read_text`, `metadata_path.write_text`, `refreshed.path.read_bytes`, `timedelta`.

**Expected result**

- Direct assertions: `assert opener.call_count == 2`; `assert refreshed.path.read_bytes() == REFRESHED_ARCHIVE_CONTENT`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `future cached timestamp triggers refresh` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `(datetime.now(UTC) + timedelta(hours=1)).isoformat`, `datetime.now`, `download_cadastre_parcelles`, `io.BytesIO`, `json.dumps`, `json.loads`, `metadata_path.read_text`, `metadata_path.write_text`, `patch`, `refreshed.path.read_bytes`, `timedelta`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_metadata_publication_failure_restores_previous_cache_pair`

**Signature**

```python
def test_metadata_publication_failure_restores_previous_cache_pair(
    tmp_path: Path,
) -> None:
```

**Purpose**

Protects the `metadata publication failure restores previous cache pair` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 7 explicit setup/context statement(s).
- Enters managed context(s) `patch('landscout.sources.cadastre_fr.open_safe_https', return_value=io.BytesIO(ARCHIVE_CONTENT))` and executes: Computes `first` from `download_cadastre_parcelles(COMMUNE_CODE, tmp_path)`.
- Computes `metadata_path` from `tmp_path / f'{first.filename}.metadata.json'`.
- Computes `archive_before` from `first.path.read_bytes()`.
- Computes `metadata_before` from `metadata_path.read_bytes()`.
- Computes `temporary_metadata` from `metadata_path.with_suffix(f'{metadata_path.suffix}.part')`.
- Computes `original_replace` from `__import__('landscout.sources.cadastre_fr', fromlist=['_replace_file'])._replace_file`.
- Enters managed context(s) `patch('landscout.sources.cadastre_fr.open_safe_https', return_value=io.BytesIO(REFRESHED_ARCHIVE_CONTENT)), patch('landscout.sources.cadastre_fr._replace_file', side_effect=fail_metadata_publication), pytest.raises(CadastreDownloadError, match='publication')` and executes: Calls `download_cadastre_parcelles(COMMUNE_CODE, tmp_path)` for its validation or side effect.

**Action**

- Calls `OSError`, `__import__`, `_set_cache_age`, `download_cadastre_parcelles`, `first.path.read_bytes`, `io.BytesIO`, `metadata_path.read_bytes`, `metadata_path.with_suffix`, `original_replace`, `timedelta`, `tmp_path.glob`.

**Expected result**

- Direct assertions: `assert first.path.read_bytes() == archive_before`; `assert metadata_path.read_bytes() == metadata_before`; `assert not list(tmp_path.glob('*.part'))`; `assert not list(tmp_path.glob('*.bak'))`.
- Expected exception contexts: `with patch('landscout.sources.cadastre_fr.open_safe_https', return_value=io.BytesIO(REFRESHED_ARCHIVE_CONTENT)), patch('landscout.sources.cadastre_fr._replace_file', side_effect=fail_metadata_publication), pytest.raises(CadastreDownloadError, match='publication'): download_cadastre_parcelles(COMMUNE_CODE, tmp_path)`.

**Regression protected**

- Protects the exact `metadata publication failure restores previous cache pair` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `OSError`, `__import__`, `_set_cache_age`, `download_cadastre_parcelles`, `first.path.read_bytes`, `io.BytesIO`, `list`, `metadata_path.read_bytes`, `metadata_path.with_suffix`, `original_replace`, `patch`, `pytest.raises`, `timedelta`, `tmp_path.glob`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_first_metadata_publication_failure_leaves_no_half_pair`

**Signature**

```python
def test_first_metadata_publication_failure_leaves_no_half_pair(
    tmp_path: Path,
) -> None:
```

**Purpose**

Protects the `first metadata publication failure leaves no half pair` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 5 explicit setup/context statement(s).
- Computes `expected_path` from `tmp_path / 'cadastre-31395-parcelles.json.gz'`.
- Computes `metadata_path` from `tmp_path / f'{expected_path.name}.metadata.json'`.
- Computes `temporary_metadata` from `metadata_path.with_suffix(f'{metadata_path.suffix}.part')`.
- Computes `original_replace` from `__import__('landscout.sources.cadastre_fr', fromlist=['_replace_file'])._replace_file`.
- Enters managed context(s) `patch('landscout.sources.cadastre_fr.open_safe_https', return_value=io.BytesIO(ARCHIVE_CONTENT)), patch('landscout.sources.cadastre_fr._replace_file', side_effect=fail_metadata_publication), pytest.raises(CadastreDownloadError, match='publication')` and executes: Calls `download_cadastre_parcelles(COMMUNE_CODE, tmp_path)` for its validation or side effect.

**Action**

- Calls `OSError`, `__import__`, `download_cadastre_parcelles`, `expected_path.exists`, `io.BytesIO`, `metadata_path.exists`, `metadata_path.with_suffix`, `original_replace`, `tmp_path.glob`.

**Expected result**

- Direct assertions: `assert not expected_path.exists()`; `assert not metadata_path.exists()`; `assert not list(tmp_path.glob('*.part'))`; `assert not list(tmp_path.glob('*.bak'))`.
- Expected exception contexts: `with patch('landscout.sources.cadastre_fr.open_safe_https', return_value=io.BytesIO(ARCHIVE_CONTENT)), patch('landscout.sources.cadastre_fr._replace_file', side_effect=fail_metadata_publication), pytest.raises(CadastreDownloadError, match='publication'): download_cadastre_parcelles(COMMUNE_CODE, tmp_path)`.

**Regression protected**

- Protects the exact `first metadata publication failure leaves no half pair` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `OSError`, `__import__`, `download_cadastre_parcelles`, `expected_path.exists`, `io.BytesIO`, `list`, `metadata_path.exists`, `metadata_path.with_suffix`, `original_replace`, `patch`, `pytest.raises`, `tmp_path.glob`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_publication_and_rollback_failure_preserves_recovery_backup`

**Signature**

```python
def test_publication_and_rollback_failure_preserves_recovery_backup(
    tmp_path: Path,
    rollback_target: str,
) -> None:
```

**Purpose**

Protects the `publication and rollback failure preserves recovery backup` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `rollback_target`.
- Contains 8 explicit setup/context statement(s).
- Enters managed context(s) `patch('landscout.sources.cadastre_fr.open_safe_https', return_value=io.BytesIO(ARCHIVE_CONTENT))` and executes: Computes `first` from `download_cadastre_parcelles(COMMUNE_CODE, tmp_path)`.
- Computes `metadata_path` from `tmp_path / f'{first.filename}.metadata.json'`.
- Computes `archive_backup` from `first.path.with_suffix(f'{first.path.suffix}.bak')`.
- Computes `metadata_backup` from `metadata_path.with_suffix(f'{metadata_path.suffix}.bak')`.
- Computes `temporary_metadata` from `metadata_path.with_suffix(f'{metadata_path.suffix}.part')`.
- Computes `original_replace` from `cadastre_fr._replace_file`.
- Enters managed context(s) `patch('landscout.sources.cadastre_fr.open_safe_https', return_value=io.BytesIO(REFRESHED_ARCHIVE_CONTENT)), patch.object(cadastre_fr, '_replace_file', side_effect=fail_publication_and_rollback), pytest.raises(CadastreDownloadError, match='rollback')` and executes: Calls `download_cadastre_parcelles(COMMUNE_CODE, tmp_path)` for its validation or side effect.
- Computes `useful_backups` from `[path for path in (archive_backup, metadata_backup) if path.exists()]`.

**Action**

- Calls `OSError`, `_set_cache_age`, `download_cadastre_parcelles`, `first.path.with_suffix`, `io.BytesIO`, `metadata_path.with_suffix`, `original_replace`, `path.exists`, `timedelta`.

**Expected result**

- Direct assertions: `assert useful_backups`.
- Expected exception contexts: `with patch('landscout.sources.cadastre_fr.open_safe_https', return_value=io.BytesIO(REFRESHED_ARCHIVE_CONTENT)), patch.object(cadastre_fr, '_replace_file', side_effect=fail_publication_and_rollback), pytest.raises(CadastreDownloadError, match='rollback'): download_cadastre_parcelles(COMMUNE_CODE, tmp_path)`.

**Regression protected**

- Protects the exact `publication and rollback failure preserves recovery backup` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `OSError`, `_set_cache_age`, `download_cadastre_parcelles`, `first.path.with_suffix`, `io.BytesIO`, `metadata_path.with_suffix`, `original_replace`, `patch`, `patch.object`, `path.exists`, `pytest.mark.parametrize`, `pytest.raises`, `timedelta`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_stale_recovery_backup_rejects_cache_before_network_and_preserves_bytes`

**Signature**

```python
def test_stale_recovery_backup_rejects_cache_before_network_and_preserves_bytes(
    tmp_path: Path,
) -> None:
```

**Purpose**

Protects the `stale recovery backup rejects cache before network and preserves bytes` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 4 explicit setup/context statement(s).
- Enters managed context(s) `patch('landscout.sources.cadastre_fr.open_safe_https', return_value=io.BytesIO(ARCHIVE_CONTENT))` and executes: Computes `first` from `download_cadastre_parcelles(COMMUNE_CODE, tmp_path)`.
- Computes `recovery_path` from `first.path.with_suffix(f'{first.path.suffix}.bak')`.
- Computes `recovery_bytes` from `b'manual cadastre recovery material'`.
- Enters managed context(s) `patch('landscout.sources.cadastre_fr.open_safe_https', side_effect=AssertionError('recovery state must fail before network')), pytest.raises(CadastreDownloadError, match='backup|recovery|manual')` and executes: Calls `download_cadastre_parcelles(COMMUNE_CODE, tmp_path)` for its validation or side effect.

**Action**

- Calls `AssertionError`, `download_cadastre_parcelles`, `first.path.read_bytes`, `first.path.with_suffix`, `io.BytesIO`, `opener.assert_not_called`, `recovery_path.read_bytes`, `recovery_path.write_bytes`.

**Expected result**

- Direct assertions: `assert recovery_path.read_bytes() == recovery_bytes`; `assert first.path.read_bytes() == ARCHIVE_CONTENT`.
- Expected exception contexts: `with patch('landscout.sources.cadastre_fr.open_safe_https', side_effect=AssertionError('recovery state must fail before network')) as opener, pytest.raises(CadastreDownloadError, match='backup|recovery|manual'): download_cadastre_parcelles(COMMUNE_CODE, tmp_path)`.

**Regression protected**

- Protects the exact `stale recovery backup rejects cache before network and preserves bytes` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `AssertionError`, `download_cadastre_parcelles`, `first.path.read_bytes`, `first.path.with_suffix`, `io.BytesIO`, `opener.assert_not_called`, `patch`, `pytest.raises`, `recovery_path.read_bytes`, `recovery_path.write_bytes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_next_run_after_double_failure_preserves_recovery_before_network`

**Signature**

```python
def test_next_run_after_double_failure_preserves_recovery_before_network(
    tmp_path: Path,
) -> None:
```

**Purpose**

Protects the `next run after double failure preserves recovery before network` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 12 explicit setup/context statement(s).
- Enters managed context(s) `patch('landscout.sources.cadastre_fr.open_safe_https', return_value=io.BytesIO(ARCHIVE_CONTENT))` and executes: Computes `first` from `download_cadastre_parcelles(COMMUNE_CODE, tmp_path)`.
- Computes `metadata_path` from `tmp_path / f'{first.filename}.metadata.json'`.
- Computes `old_archive` from `first.path.read_bytes()`.
- Computes `old_metadata` from `metadata_path.read_bytes()`.
- Computes `temporary_metadata` from `metadata_path.with_suffix(f'{metadata_path.suffix}.part')`.
- Computes `archive_backup` from `first.path.with_suffix(f'{first.path.suffix}.bak')`.
- Computes `metadata_backup` from `metadata_path.with_suffix(f'{metadata_path.suffix}.bak')`.
- Computes `original_replace` from `cadastre_fr._replace_file`.
- Enters managed context(s) `patch('landscout.sources.cadastre_fr.open_safe_https', return_value=io.BytesIO(REFRESHED_ARCHIVE_CONTENT)), patch.object(cadastre_fr, '_replace_file', side_effect=fail_publication_and_rollback), pytest.raises(CadastreDownloadError, match='rollback')` and executes: Calls `download_cadastre_parcelles(COMMUNE_CODE, tmp_path)` for its validation or side effect.
- Computes `archive_recovery` from `archive_backup.read_bytes()`.
- Computes `metadata_recovery` from `metadata_backup.read_bytes()`.
- Enters managed context(s) `patch('landscout.sources.cadastre_fr.open_safe_https', side_effect=AssertionError('recovery state must fail before network')), pytest.raises(CadastreDownloadError, match='backup|recovery|manual')` and executes: Calls `download_cadastre_parcelles(COMMUNE_CODE, tmp_path)` for its validation or side effect.

**Action**

- Calls `AssertionError`, `OSError`, `_set_cache_age`, `archive_backup.read_bytes`, `download_cadastre_parcelles`, `first.path.read_bytes`, `first.path.with_suffix`, `io.BytesIO`, `metadata_backup.read_bytes`, `metadata_path.read_bytes`, `metadata_path.with_suffix`, `opener.assert_not_called`, `original_replace`, `timedelta`.

**Expected result**

- Direct assertions: `assert archive_backup.read_bytes() == old_archive`; `assert metadata_backup.read_bytes() == old_metadata`; `assert archive_backup.read_bytes() == archive_recovery`; `assert metadata_backup.read_bytes() == metadata_recovery`.
- Expected exception contexts: `with patch('landscout.sources.cadastre_fr.open_safe_https', return_value=io.BytesIO(REFRESHED_ARCHIVE_CONTENT)), patch.object(cadastre_fr, '_replace_file', side_effect=fail_publication_and_rollback), pytest.raises(CadastreDownloadError, match='rollback'): download_cadastre_parcelles(COMMUNE_CODE, tmp_path)`; `with patch('landscout.sources.cadastre_fr.open_safe_https', side_effect=AssertionError('recovery state must fail before network')) as opener, pytest.raises(CadastreDownloadError, match='backup|recovery|manual'): download_cadastre_parcelles(COMMUNE_CODE, tmp_path)`.

**Regression protected**

- Protects the exact `next run after double failure preserves recovery before network` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `AssertionError`, `OSError`, `_set_cache_age`, `archive_backup.read_bytes`, `download_cadastre_parcelles`, `first.path.read_bytes`, `first.path.with_suffix`, `io.BytesIO`, `metadata_backup.read_bytes`, `metadata_path.read_bytes`, `metadata_path.with_suffix`, `opener.assert_not_called`, `original_replace`, `patch`, `patch.object`, `pytest.raises`, `timedelta`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_temporary_link_or_junction_cannot_modify_target_before_network`

**Signature**

```python
def test_temporary_link_or_junction_cannot_modify_target_before_network(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    temporary_role: str,
    link_kind: str,
) -> None:
```

**Purpose**

Protects the `temporary link or junction cannot modify target before network` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`, `temporary_role`, `link_kind`.
- Contains 11 explicit setup/context statement(s).
- Computes `archive_path` from `tmp_path / 'cadastre-31395-parcelles.json.gz'`.
- Computes `metadata_path` from `tmp_path / f'{archive_path.name}.metadata.json'`.
- Computes `temporary_paths` from `{'archive': archive_path.with_suffix(f'{archive_path.suffix}.part'), 'metadata': metadata_path.with_suffix(f'{metadata_path.suffix}.part')}`.
- Computes `unsafe_path` from `temporary_paths[temporary_role]`.
- Computes `sentinel` from `tmp_path / 'do-not-overwrite.txt'`.
- Computes `sentinel_bytes` from `b'irreplaceable cadastre sentinel'`.
- Computes `original_is_symlink` from `Path.is_symlink`.
- Computes `original_is_junction` from `Path.is_junction`.
- Computes `original_open` from `Path.open`.
- Computes `network_calls` from `0`.
- Enters managed context(s) `pytest.raises(CadastreDownloadError, match='temporary|link|cache')` and executes: Calls `download_cadastre_parcelles(COMMUNE_CODE, tmp_path)` for its validation or side effect.

**Action**

- Calls `archive_path.with_suffix`, `download_cadastre_parcelles`, `io.BytesIO`, `metadata_path.with_suffix`, `monkeypatch.setattr`, `original_is_junction`, `original_is_symlink`, `original_open`, `sentinel.read_bytes`, `sentinel.write_bytes`.

**Expected result**

- Direct assertions: `assert network_calls == 0`; `assert sentinel.read_bytes() == sentinel_bytes`.
- Expected exception contexts: `with pytest.raises(CadastreDownloadError, match='temporary|link|cache'): download_cadastre_parcelles(COMMUNE_CODE, tmp_path)`.

**Regression protected**

- Protects the exact `temporary link or junction cannot modify target before network` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `archive_path.with_suffix`, `download_cadastre_parcelles`, `io.BytesIO`, `metadata_path.with_suffix`, `monkeypatch.setattr`, `original_is_junction`, `original_is_symlink`, `original_open`, `pytest.mark.parametrize`, `pytest.raises`, `sentinel.read_bytes`, `sentinel.write_bytes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_broken_recovery_symlink_is_rejected_before_network`

**Signature**

```python
def test_broken_recovery_symlink_is_rejected_before_network(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `broken recovery symlink is rejected before network` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`.
- Contains 5 explicit setup/context statement(s).
- Computes `archive_path` from `tmp_path / 'cadastre-31395-parcelles.json.gz'`.
- Computes `recovery_path` from `archive_path.with_suffix(f'{archive_path.suffix}.bak')`.
- Computes `original_is_symlink` from `Path.is_symlink`.
- Computes `network_calls` from `0`.
- Enters managed context(s) `pytest.raises(CadastreDownloadError, match='backup|recovery|manual')` and executes: Calls `download_cadastre_parcelles(COMMUNE_CODE, tmp_path)` for its validation or side effect.

**Action**

- Calls `AssertionError`, `archive_path.with_suffix`, `download_cadastre_parcelles`, `monkeypatch.setattr`, `original_is_symlink`.

**Expected result**

- Direct assertions: `assert network_calls == 0`.
- Expected exception contexts: `with pytest.raises(CadastreDownloadError, match='backup|recovery|manual'): download_cadastre_parcelles(COMMUNE_CODE, tmp_path)`.

**Regression protected**

- Protects the exact `broken recovery symlink is rejected before network` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `AssertionError`, `archive_path.with_suffix`, `download_cadastre_parcelles`, `monkeypatch.setattr`, `original_is_symlink`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_cleanup_failure_does_not_mask_double_failure_recovery_error`

**Signature**

```python
def test_cleanup_failure_does_not_mask_double_failure_recovery_error(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `cleanup failure does not mask double failure recovery error` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`.
- Contains 11 explicit setup/context statement(s).
- Enters managed context(s) `patch('landscout.sources.cadastre_fr.open_safe_https', return_value=io.BytesIO(ARCHIVE_CONTENT))` and executes: Computes `first` from `download_cadastre_parcelles(COMMUNE_CODE, tmp_path)`.
- Computes `metadata_path` from `tmp_path / f'{first.filename}.metadata.json'`.
- Computes `old_archive` from `first.path.read_bytes()`.
- Computes `old_metadata` from `metadata_path.read_bytes()`.
- Computes `temporary_metadata` from `metadata_path.with_suffix(f'{metadata_path.suffix}.part')`.
- Computes `archive_backup` from `first.path.with_suffix(f'{first.path.suffix}.bak')`.
- Computes `metadata_backup` from `metadata_path.with_suffix(f'{metadata_path.suffix}.bak')`.
- Computes `original_replace` from `cadastre_fr._replace_file`.
- Computes `original_unlink` from `Path.unlink`.
- Computes `rollback_failed` from `False`.
- Enters managed context(s) `pytest.raises(CadastreDownloadError, match='rollback')` and executes: Calls `download_cadastre_parcelles(COMMUNE_CODE, tmp_path)` for its validation or side effect.

**Action**

- Calls `OSError`, `PermissionError`, `_set_cache_age`, `archive_backup.read_bytes`, `download_cadastre_parcelles`, `first.path.read_bytes`, `first.path.with_suffix`, `io.BytesIO`, `metadata_backup.read_bytes`, `metadata_path.read_bytes`, `metadata_path.with_suffix`, `monkeypatch.setattr`, `original_replace`, `original_unlink`, `timedelta`.

**Expected result**

- Direct assertions: `assert archive_backup.read_bytes() == old_archive`; `assert metadata_backup.read_bytes() == old_metadata`.
- Expected exception contexts: `with pytest.raises(CadastreDownloadError, match='rollback'): download_cadastre_parcelles(COMMUNE_CODE, tmp_path)`.

**Regression protected**

- Protects the exact `cleanup failure does not mask double failure recovery error` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `OSError`, `PermissionError`, `_set_cache_age`, `archive_backup.read_bytes`, `download_cadastre_parcelles`, `first.path.read_bytes`, `first.path.with_suffix`, `io.BytesIO`, `metadata_backup.read_bytes`, `metadata_path.read_bytes`, `metadata_path.with_suffix`, `monkeypatch.setattr`, `original_replace`, `original_unlink`, `patch`, `pytest.raises`, `timedelta`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `download_timestamp` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `file_size` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `sha256` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |

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

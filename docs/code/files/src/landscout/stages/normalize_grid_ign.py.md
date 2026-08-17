# `src/landscout/stages/normalize_grid_ign.py`

## File identity

- Repository path: `src/landscout/stages/normalize_grid_ign.py`
- File type: Python source
- Primary responsibility: Source-completely normalizes IGN electricity lines and transformation posts into stable factual proxy catalogs.
- Layer / domain: `stage` / `grid`
- Public or internal role: Module symbols without a package re-export are internal unless imported directly by repository code.
- Source SHA256: `f287bded75c93f0a451e5819c7edcd99bdeb8e7a161069dbf99cd019e35ae290`

## 1. Purpose

Source-completely normalizes IGN electricity lines and transformation posts into stable factual proxy catalogs.

## 2. Position in LandScout architecture

This file is a `stage` artifact in the `grid` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from __future__ import annotations` — required by the implementation paths and symbols documented below.
- `import re` — required by the implementation paths and symbols documented below.
- `import unicodedata` — required by the implementation paths and symbols documented below.
- `from dataclasses import dataclass` — required by the implementation paths and symbols documented below.
- `from datetime import date, datetime` — required by the implementation paths and symbols documented below.
- `from math import isfinite` — required by the implementation paths and symbols documented below.
- `from numbers import Real` — required by the implementation paths and symbols documented below.
- `from typing import Literal` — required by the implementation paths and symbols documented below.

### Third-party

- `import geopandas as gpd` — required by the implementation paths and symbols documented below.
- `import pandas as pd` — required by the implementation paths and symbols documented below.
- `from pandas.api.types import is_scalar` — required by the implementation paths and symbols documented below.
- `from pydantic import HttpUrl, TypeAdapter, ValidationError` — required by the implementation paths and symbols documented below.
- `from pyproj import CRS` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout.sources.ign_bdtopo_fr import ( DepartmentCode, EditionString, IgnBdTopoDownload, IgnBdTopoElectricityData, IgnBdTopoExtraction, IgnBdTopoLayerSummary, IgnBdTopoSourceConfig, _revalidate_ign_bdtopo_electricity_data, _validate_layer_summary_contract, )` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `SOURCE_PROVIDER` | `"IGN"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `SOURCE_PRODUCT` | `"BD_TOPO"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `SPATIAL_ROLE` | `"PROXY_GEOMETRY"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `PACKAGE_LINEAGE_COLUMNS` | `( "source_department_code", "source_edition", "source_product_version", "source_download_timestamp", "source_archive_sha256", "source_url", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `LINE_OUTPUT_COLUMNS` | `( "grid_feature_id", "grid_feature_type", "source_provider", "source_product", "source_layer", "source_feature_id", *PACKAGE_LINEAGE_COLUMNS, "voltage_raw", "voltage_status", "voltage_kv", "voltage_upper_bound_kv", "manager_name", "manager_siren", "asset_status_raw", "source_name_raw", "source_identifiers_raw", "source_created_at", "source_modified_at", "source_confirmed_at", "planimetric_acquisition_method", "planimetric_precision_m", "spatial_role", "geometry_status", "geometry", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `TRANSFORMATION_POST_OUTPUT_COLUMNS` | `( "grid_feature_id", "grid_feature_type", "source_provider", "source_product", "source_layer", "source_feature_id", *PACKAGE_LINEAGE_COLUMNS, "name", "name_status_raw", "importance_raw", "asset_status_raw", "source_name_raw", "source_identifiers_raw", "source_created_at", "source_modified_at", "source_confirmed_at", "planimetric_acquisition_method", "planimetric_precision_m", "voltage_status", "voltage_kv", "spatial_role", "geometry_status", "geometry", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `LINE_SOURCE_FIELDS` | `frozenset( { "cleabs", "voltage", "gestionnaire", "siren_gestionnaire", "etat_de_l_objet", "sources", "identifiants_sources", "date_creation", "date_modification", "date_de_confirmation", "methode_d_acquisition_planimetrique", "precision_planimetrique", "geometry", } )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `TRANSFORMATION_POST_SOURCE_FIELDS` | `frozenset( { "cleabs", "toponyme", "statut_du_toponyme", "importance", "etat_de_l_objet", "sources", "identifiants_sources", "date_creation", "date_modification", "date_de_confirmation", "methode_d_acquisition_planimetrique", "precision_planimetrique", "geometry", } )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `LINE_GEOMETRY_TYPES` | `frozenset({"LineString", "MultiLineString"})` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `TRANSFORMATION_POST_GEOMETRY_TYPES` | `frozenset({"Polygon", "MultiPolygon"})` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_EXACT_VOLTAGE_PATTERN` | `re.compile( r"^(?P<value>\d+(?:[.,]\d+)?)\s*kv$", re.IGNORECASE )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_BELOW_VOLTAGE_PATTERN` | `re.compile( r"^<\s*(?P<value>\d+(?:[.,]\d+)?)\s*kv$", re.IGNORECASE )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_UNKNOWN_VOLTAGE_TERMS` | `frozenset( {"inconnu", "inconnue", "unknown", "non renseigne", "non renseignee"} )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_DEENERGIZED_VOLTAGE_TERMS` | `frozenset({"hors tension"})` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_DEPARTMENT_CODE_VALIDATOR` | `TypeAdapter(DepartmentCode)` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_EDITION_VALIDATOR` | `TypeAdapter(EditionString)` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_HTTP_URL_VALIDATOR` | `TypeAdapter(HttpUrl)` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_SHA256_PATTERN` | `re.compile(r"^[0-9a-f]{64}$")` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_IGN_PROVIDER_IDENTITIES` | `frozenset( { "ign", "institut national de l information geographique et forestiere", "institut national de l information geographique et forestiere ign", } )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

### `IgnGridNormalizationError`

**Purpose:** Raised when IGN electricity data cannot be normalized safely.

**Inheritance:** `ValueError`.

**Model form and mutability:** class inheriting from `ValueError`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

### `_IgnGridSourceContext`

**Purpose:** Immutable source-package context persisted on every normalized row.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `source_layer` | `str` | `required` | Source lineage or source-bound object whose exact identity is checked before downstream use. |
| `department_code` | `str` | `required` | Exact configured or source code whose vocabulary/format is enforced by the owning validator. |
| `edition` | `str` | `required` | `str` state used by `src/landscout/stages/normalize_grid_ign.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `product_version` | `str | None` | `required` | `str | None` state used by `src/landscout/stages/normalize_grid_ign.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `download_timestamp` | `str` | `required` | Offset-aware source/download timestamp string preserved as lineage and validated by the owning model. |
| `archive_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `source_url` | `str` | `required` | Exact source or evidence URL; host/path/HTTPS restrictions are enforced by configuration or source validators. |

**Validators and methods:**

- None.

### `IgnVoltageNormalization`

**Purpose:** One source voltage value and its explicit normalized semantics.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `raw` | `str | None` | `required` | `str | None` state used by `src/landscout/stages/normalize_grid_ign.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `status` | `VoltageStatus` | `required` | `VoltageStatus` state used by `src/landscout/stages/normalize_grid_ign.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `voltage_kv` | `float | None` | `required` | `float | None` state used by `src/landscout/stages/normalize_grid_ign.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `voltage_upper_bound_kv` | `float | None` | `required` | `float | None` state used by `src/landscout/stages/normalize_grid_ign.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `NormalizedIgnElectricityData`

**Purpose:** Groups the `NormalizedIgnElectricityData` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `electric_lines` | `gpd.GeoDataFrame` | `required` | `gpd.GeoDataFrame` state used by `src/landscout/stages/normalize_grid_ign.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `transformation_posts` | `gpd.GeoDataFrame` | `required` | `gpd.GeoDataFrame` state used by `src/landscout/stages/normalize_grid_ign.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

## 6. Functions and methods

### `_normalized_term`

**Signature**

```python
def _normalized_term(value: str) -> str:
```

**Purpose**

Implements normalized term according to the exact implementation and guards in this file.

**Inputs**

- `value` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `' '.join(without_accents.split())`.

**Algorithm**

1. Computes `decomposed` from `unicodedata.normalize('NFKD', value.strip().casefold())`.
2. Computes `without_accents` from `''.join((character for character in decomposed if not unicodedata.combining(character)))`.
3. Returns `' '.join(without_accents.split())`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `' '.join`, `''.join`, `unicodedata.combining`, `unicodedata.normalize`, `value.strip`, `value.strip().casefold`, `without_accents.split`.

**Known repository callers**

- `src/landscout/stages/normalize_grid_ign.py` — `parse_ign_voltage`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_positive_voltage`

**Signature**

```python
def _positive_voltage(match: re.Match[str]) -> float | None:
```

**Purpose**

Implements positive voltage according to the exact implementation and guards in this file.

**Inputs**

- `match` (`re.Match[str]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `float | None`. Observed return expression(s): `value if value > 0 and isfinite(value) else None`.

**Algorithm**

1. Computes `value` from `float(match.group('value').replace(',', '.'))`.
2. Returns `value if value > 0 and isfinite(value) else None`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `match.group('value').replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `float`, `isfinite`, `match.group`, `match.group('value').replace`.

**Known repository callers**

- `src/landscout/stages/normalize_grid_ign.py` — `parse_ign_voltage`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_is_missing_scalar`

**Signature**

```python
def _is_missing_scalar(value: object) -> bool:
```

**Purpose**

Returns whether `missing scalar` satisfies the exact predicates and branches listed below.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bool`. Observed return expression(s): `bool(pd.isna(value))`; `True`; `False`.

**Algorithm**

1. Checks `value is None`. When true: Returns `True`.
2. Checks `not is_scalar(value)`. When true: Returns `False`.
3. Returns `bool(pd.isna(value))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `bool`, `is_scalar`, `pd.isna`.

**Known repository callers**

- `src/landscout/stages/normalize_grid_ign.py` — `_normalized_precision`
- `src/landscout/stages/normalize_grid_ign.py` — `parse_ign_voltage`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `parse_ign_voltage`

**Signature**

```python
def parse_ign_voltage(value: object) -> IgnVoltageNormalization:
```

**Purpose**

Parse scalar IGN voltage vocabulary without inventing precision. Unsupported list-like or array-like inputs are preserved as text and classified ``UNPARSED`` rather than reaching Pandas' ambiguous truth-value handling.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `IgnVoltageNormalization`. Observed return expression(s): `IgnVoltageNormalization(raw, 'UNPARSED', None, None)`; `IgnVoltageNormalization(str(value), 'UNPARSED', None, None)`; `IgnVoltageNormalization(None, 'UNKNOWN', None, None)`; `IgnVoltageNormalization(raw, 'UNKNOWN', None, None)`; `IgnVoltageNormalization(raw, 'DEENERGIZED', None, None)`; `IgnVoltageNormalization(raw, 'BELOW', None, upper_bound)`; `IgnVoltageNormalization(raw, 'EXACT', exact, None)`.

**Algorithm**

1. Checks `not is_scalar(value)`. When true: Returns `IgnVoltageNormalization(str(value), 'UNPARSED', None, None)`.
2. Checks `_is_missing_scalar(value)`. When true: Returns `IgnVoltageNormalization(None, 'UNKNOWN', None, None)`.
3. Computes `raw` from `value if isinstance(value, str) else str(value)`.
4. Computes `normalized` from `_normalized_term(raw)`.
5. Checks `normalized in _UNKNOWN_VOLTAGE_TERMS`. When true: Returns `IgnVoltageNormalization(raw, 'UNKNOWN', None, None)`.
6. Checks `normalized in _DEENERGIZED_VOLTAGE_TERMS`. When true: Returns `IgnVoltageNormalization(raw, 'DEENERGIZED', None, None)`.
7. Computes `below_match` from `_BELOW_VOLTAGE_PATTERN.fullmatch(normalized)`.
8. Checks `below_match is not None`. When true: Computes `upper_bound` from `_positive_voltage(below_match)`. Checks `upper_bound is not None`. When true: Returns `IgnVoltageNormalization(raw, 'BELOW', None, upper_bound)`.
9. Computes `exact_match` from `_EXACT_VOLTAGE_PATTERN.fullmatch(normalized)`.
10. Checks `exact_match is not None`. When true: Computes `exact` from `_positive_voltage(exact_match)`. Checks `exact is not None`. When true: Returns `IgnVoltageNormalization(raw, 'EXACT', exact, None)`.
11. Returns `IgnVoltageNormalization(raw, 'UNPARSED', None, None)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `IgnVoltageNormalization`, `_BELOW_VOLTAGE_PATTERN.fullmatch`, `_EXACT_VOLTAGE_PATTERN.fullmatch`, `_is_missing_scalar`, `_normalized_term`, `_positive_voltage`, `is_scalar`, `isinstance`, `str`.

**Known repository callers**

- `src/landscout/stages/normalize_grid_ign.py` — `_normalize_ign_electric_lines`
- `tests/unit/test_normalize_grid_ign.py` — `test_bounded_voltage_is_generic_finite_and_not_exact`
- `tests/unit/test_normalize_grid_ign.py` — `test_deenergized_voltage_parser`
- `tests/unit/test_normalize_grid_ign.py` — `test_exact_voltage_parser_is_generic_and_finite`
- `tests/unit/test_normalize_grid_ign.py` — `test_invalid_or_overflowing_numeric_voltage_is_unparsed`
- `tests/unit/test_normalize_grid_ign.py` — `test_unexpected_or_non_scalar_voltage_is_controlled_unparsed`
- `tests/unit/test_normalize_grid_ign.py` — `test_unknown_voltage_parser`

**Tests**

- `tests/unit/test_normalize_grid_ign.py::test_bounded_voltage_is_generic_finite_and_not_exact`
- `tests/unit/test_normalize_grid_ign.py::test_deenergized_voltage_parser`
- `tests/unit/test_normalize_grid_ign.py::test_exact_voltage_parser_is_generic_and_finite`
- `tests/unit/test_normalize_grid_ign.py::test_invalid_or_overflowing_numeric_voltage_is_unparsed`
- `tests/unit/test_normalize_grid_ign.py::test_unexpected_or_non_scalar_voltage_is_controlled_unparsed`
- `tests/unit/test_normalize_grid_ign.py::test_unknown_voltage_parser`

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validated_lambert93`

**Signature**

```python
def _validated_lambert93(crs_value: object, label: str) -> CRS:
```

**Purpose**

Validates and returns canonical lambert93 according to the exact implementation and guards in this file.

**Inputs**

- `crs_value` (`object`; required) — coordinate reference system identity. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `CRS`. Observed return expression(s): `source_crs`.

**Algorithm**

1. Checks `crs_value is None`. When true: Raises `IgnGridNormalizationError(f'{label} CRS is required')`.
2. Runs guarded operation: Computes `source_crs` from `CRS.from_user_input(crs_value)`. Handles `Exception`.
3. Computes `expected_crs` from `CRS.from_epsg(2154)`.
4. Checks `not source_crs.is_projected or not source_crs.equals(expected_crs)`. When true: Raises `IgnGridNormalizationError(f'{label} must use EPSG:2154')`.
5. Returns `source_crs`.

**Validation and invariants**

- Rejects or diverts the path when `crs_value is None` is true.
- Rejects or diverts the path when `not source_crs.is_projected or not source_crs.equals(expected_crs)` is true.

**Exceptions**

- Explicitly raises: `IgnGridNormalizationError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `CRS.from_epsg`, `CRS.from_user_input`, `IgnGridNormalizationError`, `source_crs.equals`.

**Known repository callers**

- `src/landscout/stages/normalize_grid_ign.py` — `_validate_archive_identity`
- `src/landscout/stages/normalize_grid_ign.py` — `_validate_input`
- `src/landscout/stages/normalize_grid_ign.py` — `_validate_layer_summary`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_required_exact_string`

**Signature**

```python
def _required_exact_string(value: object, label: str) -> str:
```

**Purpose**

Implements required exact string according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `value`.

**Algorithm**

1. Checks `not isinstance(value, str) or not value.strip()`. When true: Raises `IgnGridNormalizationError(f'IGN source context {label} must be a string')`.
2. Checks `value != value.strip()`. When true: Raises `IgnGridNormalizationError(f'IGN source context {label} must not contain edge whitespace')`.
3. Returns `value`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(value, str) or not value.strip()` is true.
- Rejects or diverts the path when `value != value.strip()` is true.

**Exceptions**

- Explicitly raises: `IgnGridNormalizationError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `IgnGridNormalizationError`, `isinstance`, `value.strip`.

**Known repository callers**

- `src/landscout/stages/normalize_grid_ign.py` — `_validate_source_context`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_source_context`

**Signature**

```python
def _validate_source_context(context: _IgnGridSourceContext) -> None:
```

**Purpose**

Validates and rejects malformed source context according to the exact implementation and guards in this file.

**Inputs**

- `context` (`_IgnGridSourceContext`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Calls `_required_exact_string(context.source_layer, 'source_layer')` for its validation or side effect.
2. Computes `department_code` from `_required_exact_string(context.department_code, 'department_code')`.
3. Computes `edition` from `_required_exact_string(context.edition, 'edition')`.
4. Computes `download_timestamp` from `_required_exact_string(context.download_timestamp, 'download_timestamp')`.
5. Computes `archive_sha256` from `_required_exact_string(context.archive_sha256, 'archive_sha256')`.
6. Computes `source_url` from `_required_exact_string(context.source_url, 'source_url')`.
7. Runs guarded operation: Computes `validated_department` from `_DEPARTMENT_CODE_VALIDATOR.validate_python(department_code)`. Handles `ValidationError`.
8. Checks `validated_department != department_code`. When true: Raises `IgnGridNormalizationError('IGN source context department_code must not be rewritten')`.
9. Runs guarded operation: Computes `validated_edition` from `_EDITION_VALIDATOR.validate_python(edition)`. Calls `date.fromisoformat(validated_edition)` for its validation or side effect. Handles `(ValidationError, ValueError)`.
10. Checks `validated_edition != edition`. When true: Raises `IgnGridNormalizationError('IGN source context edition must not be rewritten')`.
11. Runs guarded operation: Computes `timestamp` from `datetime.fromisoformat(download_timestamp)`. Handles `ValueError`.
12. Checks `timestamp.tzinfo is None or timestamp.utcoffset() is None`. When true: Raises `IgnGridNormalizationError('IGN source context download_timestamp must be timezone-aware')`.
13. Checks `_SHA256_PATTERN.fullmatch(archive_sha256) is None`. When true: Raises `IgnGridNormalizationError('IGN source context archive_sha256 must contain 64 hexadecimal characters')`.
14. Runs guarded operation: Calls `_HTTP_URL_VALIDATOR.validate_python(source_url)` for its validation or side effect. Handles `ValidationError`.
15. Checks `context.product_version is not None`. When true: Calls `_required_exact_string(context.product_version, 'product_version')` for its validation or side effect.

**Validation and invariants**

- Rejects or diverts the path when `validated_department != department_code` is true.
- Rejects or diverts the path when `validated_edition != edition` is true.
- Rejects or diverts the path when `timestamp.tzinfo is None or timestamp.utcoffset() is None` is true.
- Rejects or diverts the path when `_SHA256_PATTERN.fullmatch(archive_sha256) is None` is true.

**Exceptions**

- Explicitly raises: `IgnGridNormalizationError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `IgnGridNormalizationError`, `_DEPARTMENT_CODE_VALIDATOR.validate_python`, `_EDITION_VALIDATOR.validate_python`, `_HTTP_URL_VALIDATOR.validate_python`, `_SHA256_PATTERN.fullmatch`, `_required_exact_string`, `date.fromisoformat`, `datetime.fromisoformat`, `timestamp.utcoffset`.

**Known repository callers**

- `src/landscout/stages/normalize_grid_ign.py` — `_normalize_ign_electric_lines`
- `src/landscout/stages/normalize_grid_ign.py` — `_normalize_ign_transformation_posts`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_input`

**Signature**

```python
def _validate_input(
    frame: gpd.GeoDataFrame,
    required_columns: frozenset[str],
    source_layer: str,
) -> None:
```

**Purpose**

Validates and rejects malformed input according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `required_columns` (`frozenset[str]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `source_layer` (`str`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `missing` from `required_columns - set(frame.columns)`.
2. Checks `missing`. When true: Computes `formatted` from `', '.join(sorted(missing))`. Raises `IgnGridNormalizationError(f'Missing required IGN {source_layer} columns: {formatted}')`.
3. Checks `frame.active_geometry_name != 'geometry'`. When true: Raises `IgnGridNormalizationError(f'IGN {source_layer} requires an active geometry column')`.
4. Calls `_validated_lambert93(frame.crs, f'IGN {source_layer}')` for its validation or side effect.
5. Computes `identifiers` from `frame['cleabs']`.
6. Checks `identifiers.isna().any()`. When true: Raises `IgnGridNormalizationError(f'IGN {source_layer} cleabs values must not be null')`.
7. Checks `any((not isinstance(identifier, str) for identifier in identifiers.tolist()))`. When true: Raises `IgnGridNormalizationError(f'IGN {source_layer} cleabs values must be strings')`.
8. Checks `identifiers.str.strip().eq('').any()`. When true: Raises `IgnGridNormalizationError(f'IGN {source_layer} cleabs values must not be empty')`.
9. Checks `identifiers.map(lambda value: value != value.strip()).any()`. When true: Raises `IgnGridNormalizationError(f'IGN {source_layer} cleabs values must not contain edge whitespace')`.
10. Checks `identifiers.str.contains(':', regex=False).any()`. When true: Raises `IgnGridNormalizationError(f"IGN {source_layer} cleabs values must not contain ':'")`.
11. Checks `identifiers.map(lambda value: any((unicodedata.category(character) == 'Cc' for character in value))).any()`. When true: Raises `IgnGridNormalizationError(f'IGN {source_layer} cleabs values must not contain control characters')`.
12. Checks `identifiers.duplicated().any()`. When true: Raises `IgnGridNormalizationError(f'IGN {source_layer} cleabs values must be unique')`.

**Validation and invariants**

- Rejects or diverts the path when `missing` is true.
- Rejects or diverts the path when `frame.active_geometry_name != 'geometry'` is true.
- Rejects or diverts the path when `identifiers.isna().any()` is true.
- Rejects or diverts the path when `any((not isinstance(identifier, str) for identifier in identifiers.tolist()))` is true.
- Rejects or diverts the path when `identifiers.str.strip().eq('').any()` is true.
- Rejects or diverts the path when `identifiers.map(lambda value: value != value.strip()).any()` is true.
- Rejects or diverts the path when `identifiers.str.contains(':', regex=False).any()` is true.
- Rejects or diverts the path when `identifiers.map(lambda value: any((unicodedata.category(character) == 'Cc' for character in value))).any()` is true.
- Rejects or diverts the path when `identifiers.duplicated().any()` is true.

**Exceptions**

- Explicitly raises: `IgnGridNormalizationError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `', '.join`, `IgnGridNormalizationError`, `_validated_lambert93`, `any`, `identifiers.duplicated`, `identifiers.duplicated().any`, `identifiers.isna`, `identifiers.isna().any`, `identifiers.map`, `identifiers.map(lambda value: any((unicodedata.category(character) == 'Cc' for character in value))).any`, `identifiers.map(lambda value: value != value.strip()).any`, `identifiers.str.contains`, `identifiers.str.contains(':', regex=False).any`, `identifiers.str.strip`, `identifiers.str.strip().eq`, `identifiers.str.strip().eq('').any`, `identifiers.tolist`, `isinstance`, `set`, `sorted`, `unicodedata.category`, `value.strip`.

**Known repository callers**

- `src/landscout/stages/normalize_grid_ign.py` — `_normalize_ign_electric_lines`
- `src/landscout/stages/normalize_grid_ign.py` — `_normalize_ign_transformation_posts`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_geometry_status`

**Signature**

```python
def _geometry_status(geometry: gpd.GeoSeries) -> pd.Series:
```

**Purpose**

Implements geometry status according to the exact implementation and guards in this file.

**Inputs**

- `geometry` (`gpd.GeoSeries`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.Series`. Observed return expression(s): `status`.

**Algorithm**

1. Computes `status` from `pd.Series('VALID', index=geometry.index, dtype='object')`.
2. Computes `null_mask` from `geometry.isna()`.
3. Computes `empty_mask` from `~null_mask & geometry.is_empty`.
4. Computes `invalid_mask` from `~null_mask & ~geometry.is_empty & ~geometry.is_valid`.
5. Computes `status.loc[null_mask]` from `'NULL'`.
6. Computes `status.loc[empty_mask]` from `'EMPTY'`.
7. Computes `status.loc[invalid_mask]` from `'INVALID'`.
8. Returns `status`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `geometry.isna`, `pd.Series`.

**Known repository callers**

- `src/landscout/stages/normalize_grid_ign.py` — `_normalize_ign_electric_lines`
- `src/landscout/stages/normalize_grid_ign.py` — `_normalize_ign_transformation_posts`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_geometry_summary`

**Signature**

```python
def _geometry_summary(
    frame: gpd.GeoDataFrame,
) -> tuple[int, int, int, tuple[str, ...]]:
```

**Purpose**

Implements geometry summary according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[int, int, int, tuple[str, ...]]`. Observed return expression(s): `(int(null_mask.sum()), int(empty_mask.sum()), int(invalid_mask.sum()), geometry_types)`.

**Algorithm**

1. Computes `geometry` from `frame.geometry`.
2. Computes `null_mask` from `geometry.isna()`.
3. Computes `empty_mask` from `~null_mask & geometry.is_empty`.
4. Computes `invalid_mask` from `~null_mask & ~geometry.is_empty & ~geometry.is_valid`.
5. Computes `geometry_types` from `tuple(sorted((str(value) for value in geometry[~null_mask].geom_type.dropna().unique())))`.
6. Returns `(int(null_mask.sum()), int(empty_mask.sum()), int(invalid_mask.sum()), geometry_types)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `empty_mask.sum`, `geometry.isna`, `geometry[~null_mask].geom_type.dropna`, `geometry[~null_mask].geom_type.dropna().unique`, `int`, `invalid_mask.sum`, `null_mask.sum`, `sorted`, `str`, `tuple`.

**Known repository callers**

- `src/landscout/stages/normalize_grid_ign.py` — `_validate_layer_summary`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_valid_geometry_types`

**Signature**

```python
def _validate_valid_geometry_types(
    frame: gpd.GeoDataFrame,
    status: pd.Series,
    allowed_types: frozenset[str],
    source_layer: str,
) -> None:
```

**Purpose**

Validates and rejects malformed valid geometry types according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `status` (`pd.Series`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `allowed_types` (`frozenset[str]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `source_layer` (`str`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `valid_types` from `frame.loc[status == 'VALID', 'geometry'].geom_type`.
2. Computes `unsupported` from `sorted(set(valid_types.dropna()) - allowed_types)`.
3. Checks `unsupported`. When true: Raises `IgnGridNormalizationError(f'IGN {source_layer} has unsupported VALID geometry types: ' + ', '.join(unsupported))`.

**Validation and invariants**

- Rejects or diverts the path when `unsupported` is true.

**Exceptions**

- Explicitly raises: `IgnGridNormalizationError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `', '.join`, `IgnGridNormalizationError`, `set`, `sorted`, `valid_types.dropna`.

**Known repository callers**

- `src/landscout/stages/normalize_grid_ign.py` — `_normalize_ign_electric_lines`
- `src/landscout/stages/normalize_grid_ign.py` — `_normalize_ign_transformation_posts`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_normalized_precision`

**Signature**

```python
def _normalized_precision(
    source: pd.Series,
    source_layer: str,
) -> pd.Series:
```

**Purpose**

Implements normalized precision according to the exact implementation and guards in this file.

**Inputs**

- `source` (`pd.Series`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `source_layer` (`str`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.Series`. Observed return expression(s): `pd.Series(normalized, index=source.index, dtype='float64')`.

**Algorithm**

1. Defines `normalized` with annotation `list[float]` from `[]`.
2. Iterates `value` over `source.tolist()`. For each value: Checks `_is_missing_scalar(value)`. When true: Calls `normalized.append(float('nan'))` for its validation or side effect. Executes `continue` control flow. Checks `isinstance(value, bool) or not isinstance(value, Real)`. When true: Raises `IgnGridNormalizationError(f'IGN {source_layer} precision_planimetrique must be numeric or null')`. Computes `numeric` from `float(value)`. Executes 2 additional source-ordered statement(s).
3. Returns `pd.Series(normalized, index=source.index, dtype='float64')`.

**Validation and invariants**

- Rejects or diverts the path when `isinstance(value, bool) or not isinstance(value, Real)` is true.
- Rejects or diverts the path when `not isfinite(numeric) or numeric < 0` is true.

**Exceptions**

- Explicitly raises: `IgnGridNormalizationError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `IgnGridNormalizationError`, `_is_missing_scalar`, `float`, `isfinite`, `isinstance`, `normalized.append`, `pd.Series`, `source.tolist`.

**Known repository callers**

- `src/landscout/stages/normalize_grid_ign.py` — `_normalize_ign_electric_lines`
- `src/landscout/stages/normalize_grid_ign.py` — `_normalize_ign_transformation_posts`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_base_output`

**Signature**

```python
def _base_output(
    frame: gpd.GeoDataFrame,
    *,
    feature_type: str,
    context: _IgnGridSourceContext,
) -> pd.DataFrame:
```

**Purpose**

Implements base output according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `feature_type` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `context` (`_IgnGridSourceContext`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.DataFrame`. Observed return expression(s): `output`.

**Algorithm**

1. Computes `source_ids` from `frame['cleabs'].copy()`.
2. Computes `output` from `pd.DataFrame(index=frame.index.copy())`.
3. Computes `output['grid_feature_id']` from `source_ids.map(lambda identifier: f'IGN_BDTOPO:{feature_type}:{identifier}')`.
4. Computes `output['grid_feature_type']` from `feature_type`.
5. Computes `output['source_provider']` from `SOURCE_PROVIDER`.
6. Computes `output['source_product']` from `SOURCE_PRODUCT`.
7. Computes `output['source_layer']` from `context.source_layer`.
8. Computes `output['source_feature_id']` from `source_ids`.
9. Computes `output['source_department_code']` from `context.department_code`.
10. Computes `output['source_edition']` from `context.edition`.
11. Computes `output['source_product_version']` from `context.product_version`.
12. Computes `output['source_download_timestamp']` from `context.download_timestamp`.
13. Computes `output['source_archive_sha256']` from `context.archive_sha256`.
14. Computes `output['source_url']` from `context.source_url`.
15. Returns `output`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `frame.index.copy`, `frame['cleabs'].copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `frame.index.copy`, `frame['cleabs'].copy`, `pd.DataFrame`, `source_ids.map`.

**Known repository callers**

- `src/landscout/stages/normalize_grid_ign.py` — `_normalize_ign_electric_lines`
- `src/landscout/stages/normalize_grid_ign.py` — `_normalize_ign_transformation_posts`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validated_geodataframe`

**Signature**

```python
def _validated_geodataframe(
    output: pd.DataFrame,
    frame: gpd.GeoDataFrame,
    status: pd.Series,
    columns: tuple[str, ...],
) -> gpd.GeoDataFrame:
```

**Purpose**

Validates and returns canonical geodataframe according to the exact implementation and guards in this file.

**Inputs**

- `output` (`pd.DataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `frame` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `status` (`pd.Series`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `columns` (`tuple[str, ...]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `normalized`.

**Algorithm**

1. Computes `output['spatial_role']` from `SPATIAL_ROLE`.
2. Computes `output['geometry_status']` from `status`.
3. Computes `output['geometry']` from `frame.geometry.copy()`.
4. Computes `normalized` from `gpd.GeoDataFrame(output.loc[:, list(columns)], geometry='geometry', crs=frame.crs)`.
5. Computes `normalized_ids` from `normalized['grid_feature_id']`.
6. Checks `normalized_ids.isna().any() or normalized_ids.duplicated().any()`. When true: Raises `IgnGridNormalizationError('Normalized IGN grid_feature_id values must be non-null and unique')`.
7. Checks `len(normalized) != len(frame)`. When true: Raises `IgnGridNormalizationError('IGN normalization changed the row count')`.
8. Checks `not isinstance(normalized.index, pd.RangeIndex)`. When true: Raises `IgnGridNormalizationError('IGN normalized output must use a RangeIndex')`.
9. Returns `normalized`.

**Validation and invariants**

- Rejects or diverts the path when `normalized_ids.isna().any() or normalized_ids.duplicated().any()` is true.
- Rejects or diverts the path when `len(normalized) != len(frame)` is true.
- Rejects or diverts the path when `not isinstance(normalized.index, pd.RangeIndex)` is true.

**Exceptions**

- Explicitly raises: `IgnGridNormalizationError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `frame.geometry.copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `IgnGridNormalizationError`, `frame.geometry.copy`, `gpd.GeoDataFrame`, `isinstance`, `len`, `list`, `normalized_ids.duplicated`, `normalized_ids.duplicated().any`, `normalized_ids.isna`, `normalized_ids.isna().any`.

**Known repository callers**

- `src/landscout/stages/normalize_grid_ign.py` — `_normalize_ign_electric_lines`
- `src/landscout/stages/normalize_grid_ign.py` — `_normalize_ign_transformation_posts`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_normalize_ign_electric_lines`

**Signature**

```python
def _normalize_ign_electric_lines(
    lines: gpd.GeoDataFrame,
    context: _IgnGridSourceContext,
) -> gpd.GeoDataFrame:
```

**Purpose**

Normalize one discovered IGN electric-line layer.

**Inputs**

- `lines` (`gpd.GeoDataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `context` (`_IgnGridSourceContext`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `_validated_geodataframe(output, working, status, LINE_OUTPUT_COLUMNS)`.

**Algorithm**

1. Calls `_validate_source_context(context)` for its validation or side effect.
2. Calls `_validate_input(lines, LINE_SOURCE_FIELDS, context.source_layer)` for its validation or side effect.
3. Computes `working` from `lines.reset_index(drop=True).copy()`.
4. Computes `status` from `_geometry_status(working.geometry)`.
5. Calls `_validate_valid_geometry_types(working, status, LINE_GEOMETRY_TYPES, context.source_layer)` for its validation or side effect.
6. Computes `precision` from `_normalized_precision(working['precision_planimetrique'], context.source_layer)`.
7. Computes `output` from `_base_output(working, feature_type='ELECTRIC_LINE', context=context)`.
8. Computes `parsed` from `[parse_ign_voltage(value) for value in working['voltage'].tolist()]`.
9. Computes `output['voltage_raw']` from `[result.raw for result in parsed]`.
10. Computes `output['voltage_status']` from `[result.status for result in parsed]`.
11. Computes `output['voltage_kv']` from `[result.voltage_kv for result in parsed]`.
12. Computes `output['voltage_upper_bound_kv']` from `[result.voltage_upper_bound_kv for result in parsed]`.
13. Computes `output['manager_name']` from `working['gestionnaire'].copy()`.
14. Computes `output['manager_siren']` from `working['siren_gestionnaire'].copy()`.
15. Computes `output['asset_status_raw']` from `working['etat_de_l_objet'].copy()`.
16. Computes `output['source_name_raw']` from `working['sources'].copy()`.
17. Computes `output['source_identifiers_raw']` from `working['identifiants_sources'].copy()`.
18. Computes `output['source_created_at']` from `working['date_creation'].copy()`.
19. Computes `output['source_modified_at']` from `working['date_modification'].copy()`.
20. Computes `output['source_confirmed_at']` from `working['date_de_confirmation'].copy()`.
21. Computes `output['planimetric_acquisition_method']` from `working['methode_d_acquisition_planimetrique'].copy()`.
22. Computes `output['planimetric_precision_m']` from `precision`.
23. Returns `_validated_geodataframe(output, working, status, LINE_OUTPUT_COLUMNS)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `lines.reset_index(drop=True).copy`, `working['date_creation'].copy`, `working['date_de_confirmation'].copy`, `working['date_modification'].copy`, `working['etat_de_l_objet'].copy`, `working['gestionnaire'].copy`, `working['identifiants_sources'].copy`, `working['methode_d_acquisition_planimetrique'].copy`, `working['siren_gestionnaire'].copy`, `working['sources'].copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `_base_output`, `_geometry_status`, `_normalized_precision`, `_validate_input`, `_validate_source_context`, `_validate_valid_geometry_types`, `_validated_geodataframe`, `lines.reset_index`, `lines.reset_index(drop=True).copy`, `parse_ign_voltage`, `working['date_creation'].copy`, `working['date_de_confirmation'].copy`, `working['date_modification'].copy`, `working['etat_de_l_objet'].copy`, `working['gestionnaire'].copy`, `working['identifiants_sources'].copy`, `working['methode_d_acquisition_planimetrique'].copy`, `working['siren_gestionnaire'].copy`, `working['sources'].copy`, `working['voltage'].tolist`.

**Known repository callers**

- `src/landscout/stages/normalize_grid_ign.py` — `normalize_ign_electricity`
- `tests/unit/test_normalize_grid_ign.py` — `test_appropriate_multigeometry_types_are_accepted`
- `tests/unit/test_normalize_grid_ign.py` — `test_deenergized_voltage_does_not_override_source_asset_status`
- `tests/unit/test_normalize_grid_ign.py` — `test_duplicate_line_cleabs_fails`
- `tests/unit/test_normalize_grid_ign.py` — `test_internal_source_context_rejects_uppercase_sha256`
- `tests/unit/test_normalize_grid_ign.py` — `test_invalid_line_precision_fails`
- `tests/unit/test_normalize_grid_ign.py` — `test_line_geometry_quality_is_preserved_without_row_loss_or_repair`
- `tests/unit/test_normalize_grid_ign.py` — `test_line_missing_or_wrong_crs_fails`
- `tests/unit/test_normalize_grid_ign.py` — `test_line_normalization_does_not_mutate_input_and_has_stable_columns`
- `tests/unit/test_normalize_grid_ign.py` — `test_missing_required_line_field_fails`
- `tests/unit/test_normalize_grid_ign.py` — `test_normalized_voltage_never_emits_non_finite_numeric_values`
- `tests/unit/test_normalize_grid_ign.py` — `test_null_or_empty_line_cleabs_fails`
- `tests/unit/test_normalize_grid_ign.py` — `test_unsafe_source_id_is_rejected_without_rewriting`
- `tests/unit/test_normalize_grid_ign.py` — `test_unusual_duplicate_source_index_is_not_preserved_as_identity`
- `tests/unit/test_normalize_grid_ign.py` — `test_valid_line_has_stable_identity_lineage_and_range_index`
- `tests/unit/test_normalize_grid_ign.py` — `test_valid_or_null_line_precision_is_normalized_to_float`
- `tests/unit/test_normalize_grid_ign.py` — `test_valid_polygon_or_point_is_rejected_as_electric_line`
- `tests/unit/test_normalize_grid_ign.py` — `test_z_coordinates_are_preserved`

**Tests**

- `tests/unit/test_normalize_grid_ign.py::test_appropriate_multigeometry_types_are_accepted`
- `tests/unit/test_normalize_grid_ign.py::test_deenergized_voltage_does_not_override_source_asset_status`
- `tests/unit/test_normalize_grid_ign.py::test_duplicate_line_cleabs_fails`
- `tests/unit/test_normalize_grid_ign.py::test_internal_source_context_rejects_uppercase_sha256`
- `tests/unit/test_normalize_grid_ign.py::test_invalid_line_precision_fails`
- `tests/unit/test_normalize_grid_ign.py::test_line_geometry_quality_is_preserved_without_row_loss_or_repair`
- `tests/unit/test_normalize_grid_ign.py::test_line_missing_or_wrong_crs_fails`
- `tests/unit/test_normalize_grid_ign.py::test_line_normalization_does_not_mutate_input_and_has_stable_columns`
- `tests/unit/test_normalize_grid_ign.py::test_missing_required_line_field_fails`
- `tests/unit/test_normalize_grid_ign.py::test_normalized_voltage_never_emits_non_finite_numeric_values`
- `tests/unit/test_normalize_grid_ign.py::test_null_or_empty_line_cleabs_fails`
- `tests/unit/test_normalize_grid_ign.py::test_unsafe_source_id_is_rejected_without_rewriting`
- `tests/unit/test_normalize_grid_ign.py::test_unusual_duplicate_source_index_is_not_preserved_as_identity`
- `tests/unit/test_normalize_grid_ign.py::test_valid_line_has_stable_identity_lineage_and_range_index`
- `tests/unit/test_normalize_grid_ign.py::test_valid_or_null_line_precision_is_normalized_to_float`
- `tests/unit/test_normalize_grid_ign.py::test_valid_polygon_or_point_is_rejected_as_electric_line`
- `tests/unit/test_normalize_grid_ign.py::test_z_coordinates_are_preserved`

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_normalize_ign_transformation_posts`

**Signature**

```python
def _normalize_ign_transformation_posts(
    posts: gpd.GeoDataFrame,
    context: _IgnGridSourceContext,
) -> gpd.GeoDataFrame:
```

**Purpose**

Normalize one discovered IGN transformation-post proxy layer.

**Inputs**

- `posts` (`gpd.GeoDataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `context` (`_IgnGridSourceContext`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `_validated_geodataframe(output, working, status, TRANSFORMATION_POST_OUTPUT_COLUMNS)`.

**Algorithm**

1. Calls `_validate_source_context(context)` for its validation or side effect.
2. Calls `_validate_input(posts, TRANSFORMATION_POST_SOURCE_FIELDS, context.source_layer)` for its validation or side effect.
3. Computes `working` from `posts.reset_index(drop=True).copy()`.
4. Computes `status` from `_geometry_status(working.geometry)`.
5. Calls `_validate_valid_geometry_types(working, status, TRANSFORMATION_POST_GEOMETRY_TYPES, context.source_layer)` for its validation or side effect.
6. Computes `precision` from `_normalized_precision(working['precision_planimetrique'], context.source_layer)`.
7. Computes `output` from `_base_output(working, feature_type='TRANSFORMATION_POST', context=context)`.
8. Computes `output['name']` from `working['toponyme'].copy()`.
9. Computes `output['name_status_raw']` from `working['statut_du_toponyme'].copy()`.
10. Computes `output['importance_raw']` from `working['importance'].copy()`.
11. Computes `output['asset_status_raw']` from `working['etat_de_l_objet'].copy()`.
12. Computes `output['source_name_raw']` from `working['sources'].copy()`.
13. Computes `output['source_identifiers_raw']` from `working['identifiants_sources'].copy()`.
14. Computes `output['source_created_at']` from `working['date_creation'].copy()`.
15. Computes `output['source_modified_at']` from `working['date_modification'].copy()`.
16. Computes `output['source_confirmed_at']` from `working['date_de_confirmation'].copy()`.
17. Computes `output['planimetric_acquisition_method']` from `working['methode_d_acquisition_planimetrique'].copy()`.
18. Computes `output['planimetric_precision_m']` from `precision`.
19. Computes `output['voltage_status']` from `'UNKNOWN'`.
20. Computes `output['voltage_kv']` from `float('nan')`.
21. Returns `_validated_geodataframe(output, working, status, TRANSFORMATION_POST_OUTPUT_COLUMNS)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `posts.reset_index(drop=True).copy`, `working['date_creation'].copy`, `working['date_de_confirmation'].copy`, `working['date_modification'].copy`, `working['etat_de_l_objet'].copy`, `working['identifiants_sources'].copy`, `working['importance'].copy`, `working['methode_d_acquisition_planimetrique'].copy`, `working['sources'].copy`, `working['statut_du_toponyme'].copy`, `working['toponyme'].copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `_base_output`, `_geometry_status`, `_normalized_precision`, `_validate_input`, `_validate_source_context`, `_validate_valid_geometry_types`, `_validated_geodataframe`, `float`, `posts.reset_index`, `posts.reset_index(drop=True).copy`, `working['date_creation'].copy`, `working['date_de_confirmation'].copy`, `working['date_modification'].copy`, `working['etat_de_l_objet'].copy`, `working['identifiants_sources'].copy`, `working['importance'].copy`, `working['methode_d_acquisition_planimetrique'].copy`, `working['sources'].copy`, `working['statut_du_toponyme'].copy`, `working['toponyme'].copy`.

**Known repository callers**

- `src/landscout/stages/normalize_grid_ign.py` — `normalize_ign_electricity`
- `tests/unit/test_normalize_grid_ign.py` — `test_appropriate_multigeometry_types_are_accepted`
- `tests/unit/test_normalize_grid_ign.py` — `test_duplicate_post_cleabs_fails`
- `tests/unit/test_normalize_grid_ign.py` — `test_invalid_post_precision_fails`
- `tests/unit/test_normalize_grid_ign.py` — `test_null_post_geometry_and_precision_are_preserved`
- `tests/unit/test_normalize_grid_ign.py` — `test_post_geometry_crs_and_input_are_preserved`
- `tests/unit/test_normalize_grid_ign.py` — `test_valid_line_or_point_is_rejected_as_transformation_post`
- `tests/unit/test_normalize_grid_ign.py` — `test_valid_post_has_stable_lineage_and_no_voltage_inference`

**Tests**

- `tests/unit/test_normalize_grid_ign.py::test_appropriate_multigeometry_types_are_accepted`
- `tests/unit/test_normalize_grid_ign.py::test_duplicate_post_cleabs_fails`
- `tests/unit/test_normalize_grid_ign.py::test_invalid_post_precision_fails`
- `tests/unit/test_normalize_grid_ign.py::test_null_post_geometry_and_precision_are_preserved`
- `tests/unit/test_normalize_grid_ign.py::test_post_geometry_crs_and_input_are_preserved`
- `tests/unit/test_normalize_grid_ign.py::test_valid_line_or_point_is_rejected_as_transformation_post`
- `tests/unit/test_normalize_grid_ign.py::test_valid_post_has_stable_lineage_and_no_voltage_inference`

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_layer_summary`

**Signature**

```python
def _validate_layer_summary(
    frame: gpd.GeoDataFrame,
    summary: IgnBdTopoLayerSummary,
    *,
    expected_layer: str,
    expected_logical_name: str,
) -> None:
```

**Purpose**

Validates and rejects malformed layer summary according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `summary` (`IgnBdTopoLayerSummary`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `expected_layer` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `expected_logical_name` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Runs guarded operation: Calls `_validate_layer_summary_contract(summary)` for its validation or side effect. Handles `Exception`.
2. Checks `summary.source_layer_name != expected_layer`. When true: Raises `IgnGridNormalizationError(f'IGN {expected_logical_name} summary layer does not match extraction')`.
3. Checks `summary.logical_name != expected_logical_name`. When true: Raises `IgnGridNormalizationError(f'IGN {expected_logical_name} summary has the wrong logical name')`.
4. Checks `summary.feature_count != len(frame)`. When true: Raises `IgnGridNormalizationError(f'IGN {expected_logical_name} summary row count does not match frame')`.
5. Computes `observed_columns` from `tuple((str(column) for column in frame.columns))`.
6. Computes `observed_dtypes` from `tuple(((str(column), str(dtype)) for column, dtype in frame.dtypes.items()))`.
7. Checks `summary.columns != observed_columns or summary.dtypes != observed_dtypes`. When true: Raises `IgnGridNormalizationError(f'IGN {expected_logical_name} summary schema columns or dtypes do not match frame')`.
8. Checks `frame.active_geometry_name != 'geometry'`. When true: Raises `IgnGridNormalizationError(f'IGN {expected_logical_name} requires an active geometry column')`.
9. Computes `frame_crs` from `_validated_lambert93(frame.crs, f'IGN {expected_logical_name}')`.
10. Computes `summary_crs` from `_validated_lambert93(summary.crs, f'IGN {expected_logical_name} summary')`.
11. Checks `not frame_crs.equals(summary_crs)`. When true: Raises `IgnGridNormalizationError(f'IGN {expected_logical_name} summary CRS does not match frame')`.
12. Computes `observed_geometry` from `_geometry_summary(frame)`.
13. Computes `expected_geometry` from `(summary.null_geometry_count, summary.empty_geometry_count, summary.invalid_geometry_count, summary.geometry_types)`.
14. Checks `observed_geometry != expected_geometry`. When true: Raises `IgnGridNormalizationError(f'IGN {expected_logical_name} geometry summary does not match frame')`.

**Validation and invariants**

- Rejects or diverts the path when `summary.source_layer_name != expected_layer` is true.
- Rejects or diverts the path when `summary.logical_name != expected_logical_name` is true.
- Rejects or diverts the path when `summary.feature_count != len(frame)` is true.
- Rejects or diverts the path when `summary.columns != observed_columns or summary.dtypes != observed_dtypes` is true.
- Rejects or diverts the path when `frame.active_geometry_name != 'geometry'` is true.
- Rejects or diverts the path when `not frame_crs.equals(summary_crs)` is true.
- Rejects or diverts the path when `observed_geometry != expected_geometry` is true.

**Exceptions**

- Explicitly raises: `IgnGridNormalizationError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `IgnGridNormalizationError`, `_geometry_summary`, `_validate_layer_summary_contract`, `_validated_lambert93`, `frame.dtypes.items`, `frame_crs.equals`, `len`, `str`, `tuple`.

**Known repository callers**

- `src/landscout/stages/normalize_grid_ign.py` — `_validate_source_bundle`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_normalized_identity`

**Signature**

```python
def _normalized_identity(value: object, label: str) -> str:
```

**Purpose**

Implements normalized identity according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `' '.join(re.findall('[a-z0-9]+', without_accents))`.

**Algorithm**

1. Checks `not isinstance(value, str) or not value.strip()`. When true: Raises `IgnGridNormalizationError(f'IGN archive {label} must be a string')`.
2. Computes `decomposed` from `unicodedata.normalize('NFKD', value.casefold())`.
3. Computes `without_accents` from `''.join((character for character in decomposed if not unicodedata.combining(character)))`.
4. Returns `' '.join(re.findall('[a-z0-9]+', without_accents))`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(value, str) or not value.strip()` is true.

**Exceptions**

- Explicitly raises: `IgnGridNormalizationError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `' '.join`, `''.join`, `IgnGridNormalizationError`, `isinstance`, `re.findall`, `unicodedata.combining`, `unicodedata.normalize`, `value.casefold`, `value.strip`.

**Known repository callers**

- `src/landscout/stages/normalize_grid_ign.py` — `_validate_archive_identity`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_archive_identity`

**Signature**

```python
def _validate_archive_identity(source: IgnBdTopoElectricityData) -> None:
```

**Purpose**

Validates and rejects malformed archive identity according to the exact implementation and guards in this file.

**Inputs**

- `source` (`IgnBdTopoElectricityData`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `archive` from `source.extraction.archive`.
2. Computes `provider` from `_normalized_identity(archive.provider, 'provider')`.
3. Computes `product` from `_normalized_identity(archive.product, 'product')`.
4. Checks `provider not in _IGN_PROVIDER_IDENTITIES`. When true: Raises `IgnGridNormalizationError('IGN archive provider is incompatible with the IGN normalizer')`.
5. Checks `product.replace(' ', '') != 'bdtopo'`. When true: Raises `IgnGridNormalizationError('IGN archive product is incompatible with the BD TOPO normalizer')`.
6. Calls `_validated_lambert93(archive.projection, 'IGN archive projection')` for its validation or side effect.

**Validation and invariants**

- Rejects or diverts the path when `provider not in _IGN_PROVIDER_IDENTITIES` is true.
- Rejects or diverts the path when `product.replace(' ', '') != 'bdtopo'` is true.

**Exceptions**

- Explicitly raises: `IgnGridNormalizationError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `product.replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `IgnGridNormalizationError`, `_normalized_identity`, `_validated_lambert93`, `product.replace`.

**Known repository callers**

- `src/landscout/stages/normalize_grid_ign.py` — `_validate_source_bundle`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_source_bundle`

**Signature**

```python
def _validate_source_bundle(source: IgnBdTopoElectricityData) -> None:
```

**Purpose**

Validates and rejects malformed source bundle according to the exact implementation and guards in this file.

**Inputs**

- `source` (`IgnBdTopoElectricityData`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `type(source) is not IgnBdTopoElectricityData`. When true: Raises `IgnGridNormalizationError('IGN electricity source must be IgnBdTopoElectricityData')`.
2. Checks `type(source.extraction) is not IgnBdTopoExtraction`. When true: Raises `IgnGridNormalizationError('IGN electricity extraction type is invalid')`.
3. Checks `type(source.extraction.archive) is not IgnBdTopoDownload`. When true: Raises `IgnGridNormalizationError('IGN electricity archive type is invalid')`.
4. Checks `type(source.electric_lines_summary) is not IgnBdTopoLayerSummary or type(source.transformation_posts_summary) is not IgnBdTopoLayerSummary`. When true: Raises `IgnGridNormalizationError('IGN electricity summary type is invalid')`.
5. Checks `not isinstance(source.electric_lines, gpd.GeoDataFrame) or not isinstance(source.transformation_posts, gpd.GeoDataFrame)`. When true: Raises `IgnGridNormalizationError('IGN electricity layers must be GeoDataFrames')`.
6. Computes `extraction` from `source.extraction`.
7. Computes `layer_names` from `extraction.all_layer_names`.
8. Checks `type(layer_names) is not tuple or not layer_names or any((not isinstance(name, str) or not name or name != name.strip() for name in layer_names)) or (len(set(layer_names)) != len(layer_names))`. When true: Raises `IgnGridNormalizationError('IGN electricity layer inventory must be a unique non-empty tuple')`.
9. Computes `selected_layers` from `(extraction.electric_lines_layer, extraction.transformation_posts_layer)`.
10. Checks `any((layer not in layer_names for layer in selected_layers))`. When true: Raises `IgnGridNormalizationError('IGN electricity selected layer is absent from the layer inventory')`.
11. Checks `selected_layers[0] == selected_layers[1]`. When true: Raises `IgnGridNormalizationError('IGN electricity roles must use distinct layers, not the same layer')`.
12. Calls `_validate_archive_identity(source)` for its validation or side effect.
13. Computes `roles` from `(source.spatial_role, source.extraction.spatial_role, source.extraction.archive.spatial_role, source.electric_lines_summary.spatial_role, source.transformation_posts_summary.spatial_role)`.
14. Checks `any((role != SPATIAL_ROLE for role in roles))`. When true: Raises `IgnGridNormalizationError('IGN source bundle spatial roles must all be PROXY_GEOMETRY')`.
15. Calls `_validate_layer_summary(source.electric_lines, source.electric_lines_summary, expected_layer=source.extraction.electric_lines_layer, expected_logical_name='electric_lines')` for its validation or side effect.
16. Calls `_validate_layer_summary(source.transformation_posts, source.transformation_posts_summary, expected_layer=source.extraction.transformation_posts_layer, expected_logical_name='transformation_posts')` for its validation or side effect.

**Validation and invariants**

- Rejects or diverts the path when `type(source) is not IgnBdTopoElectricityData` is true.
- Rejects or diverts the path when `type(source.extraction) is not IgnBdTopoExtraction` is true.
- Rejects or diverts the path when `type(source.extraction.archive) is not IgnBdTopoDownload` is true.
- Rejects or diverts the path when `type(source.electric_lines_summary) is not IgnBdTopoLayerSummary or type(source.transformation_posts_summary) is not IgnBdTopoLayerSummary` is true.
- Rejects or diverts the path when `not isinstance(source.electric_lines, gpd.GeoDataFrame) or not isinstance(source.transformation_posts, gpd.GeoDataFrame)` is true.
- Rejects or diverts the path when `type(layer_names) is not tuple or not layer_names or any((not isinstance(name, str) or not name or name != name.strip() for name in layer_names)) or (len(set(layer_names)) != len(layer_names))` is true.
- Rejects or diverts the path when `any((layer not in layer_names for layer in selected_layers))` is true.
- Rejects or diverts the path when `selected_layers[0] == selected_layers[1]` is true.
- Rejects or diverts the path when `any((role != SPATIAL_ROLE for role in roles))` is true.

**Exceptions**

- Explicitly raises: `IgnGridNormalizationError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `IgnGridNormalizationError`, `_validate_archive_identity`, `_validate_layer_summary`, `any`, `isinstance`, `len`, `name.strip`, `set`, `type`.

**Known repository callers**

- `src/landscout/stages/normalize_grid_ign.py` — `normalize_ign_electricity`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_source_context`

**Signature**

```python
def _source_context(
    source: IgnBdTopoElectricityData,
    source_layer: str,
) -> _IgnGridSourceContext:
```

**Purpose**

Implements source context according to the exact implementation and guards in this file.

**Inputs**

- `source` (`IgnBdTopoElectricityData`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `source_layer` (`str`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `_IgnGridSourceContext`. Observed return expression(s): `_IgnGridSourceContext(source_layer=source_layer, department_code=archive.department_code, edition=archive.edition, product_version=archive.product_version, download_timestamp=archive.download_timestamp, archive_sha256=archive.sha256, source_url=archive.source_url)`.

**Algorithm**

1. Computes `archive` from `source.extraction.archive`.
2. Returns `_IgnGridSourceContext(source_layer=source_layer, department_code=archive.department_code, edition=archive.edition, product_version=archive.product_version, download_timestamp=archive.download_timestamp, archive_sha256=archive.sha256, source_url=archive.source_url)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_IgnGridSourceContext`.

**Known repository callers**

- `src/landscout/stages/normalize_grid_ign.py` — `normalize_ign_electricity`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `normalize_ign_electricity`

**Signature**

```python
def normalize_ign_electricity(
    source: IgnBdTopoElectricityData,
    config: IgnBdTopoSourceConfig,
) -> NormalizedIgnElectricityData:
```

**Purpose**

Validate and normalize a complete already-loaded IGN source bundle.

**Inputs**

- `source` (`IgnBdTopoElectricityData`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `config` (`IgnBdTopoSourceConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `NormalizedIgnElectricityData`. Observed return expression(s): `NormalizedIgnElectricityData(electric_lines=_normalize_ign_electric_lines(source.electric_lines, line_context), transformation_posts=_normalize_ign_transformation_posts(source.transformation_posts, post_context))`.

**Algorithm**

1. Runs guarded operation: Checks `type(config) is not IgnBdTopoSourceConfig`. When true: Raises `IgnGridNormalizationError('IGN electricity source config type is invalid')`. Calls `_validate_source_bundle(source)` for its validation or side effect. Calls `_revalidate_ign_bdtopo_electricity_data(source, config)` for its validation or side effect. Computes `line_context` from `_source_context(source, source.extraction.electric_lines_layer)`. Executes 2 additional source-ordered statement(s). Handles `IgnGridNormalizationError`, `Exception`.

**Validation and invariants**

- Rejects or diverts the path when `type(config) is not IgnBdTopoSourceConfig` is true.

**Exceptions**

- Explicitly raises: `IgnGridNormalizationError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `IgnGridNormalizationError`, `NormalizedIgnElectricityData`, `_normalize_ign_electric_lines`, `_normalize_ign_transformation_posts`, `_revalidate_ign_bdtopo_electricity_data`, `_source_context`, `_validate_source_bundle`, `type`.

**Known repository callers**

- `src/landscout/stages/enrich_grid_proximity.py` — `enrich_parcel_grid_proximity`
- `tests/unit/test_normalize_grid_ign.py` — `normalize_ign_electricity`
- `tests/unit/test_normalize_grid_ign.py` — `test_archive_identity_comparison_is_case_accent_and_punctuation_tolerant`

**Tests**

- `tests/unit/test_normalize_grid_ign.py::test_archive_identity_comparison_is_case_accent_and_punctuation_tolerant`

**Business interpretation**

This symbol contributes to the `grid` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `BELOW` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `DEENERGIZED` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `EMPTY` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `EXACT` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `INVALID` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `NULL` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `UNKNOWN` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `UNPARSED` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `VALID` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `asset_status_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `cleabs` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `date_creation` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `date_de_confirmation` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `date_modification` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `etat_de_l_objet` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `geometry` | Logical dtype: GeoPandas active geometry dtype. Nullability: nullable only where the source-stage geometry-status contract explicitly preserves nulls. | source or preserved spatial geometry; never itself a suitability or legal conclusion. Consumers and exact calculations are the functions that reference this column above. |
| `geometry_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `gestionnaire` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `grid_feature_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `grid_feature_type` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `identifiants_sources` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `importance` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `importance_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `manager_name` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `manager_siren` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `methode_d_acquisition_planimetrique` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `name` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `name_status_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `planimetric_acquisition_method` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `planimetric_precision_m` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | linear distance/length in metres; proxy meaning is limited by the introducing stage. Consumers and exact calculations are the functions that reference this column above. |
| `precision_planimetrique` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `siren_gestionnaire` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_archive_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `source_confirmed_at` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_created_at` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_department_code` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_download_timestamp` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_edition` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_feature_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `source_identifiers_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `source_layer` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_modified_at` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_name_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `source_product` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_product_version` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_provider` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_url` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `sources` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `spatial_role` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `statut_du_toponyme` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `toponyme` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `voltage` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `voltage_kv` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `voltage_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `voltage_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `voltage_upper_bound_kv` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |

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

This file contributes to LandScout's `grid` evidence flow as described by its purpose and public symbols. It preserves the distinction among fact, proxy evidence, policy interpretation, diagnostic status, and parcel precheck.

## 15. Explicit non-goals

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

## 16. Tests

Direct name-resolved tests appear under each symbol. Higher-level tests may exercise private helpers through a public source-complete function; companion documents for all test files describe their fixtures, actions, assertions, and boundaries.

## 17. Change impact

Changing this file requires reviewing its static callers, package exports, directly mapped tests, relevant schema/hash/version constants, source locks, persisted artifact contracts, and the corresponding pipeline/cross-cutting documents. Any byte change makes the SHA256 above stale and requires regenerating this companion.

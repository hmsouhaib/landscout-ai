# `tests/unit/test_filter_shape.py`

## File identity

- Repository path: `tests/unit/test_filter_shape.py`
- File type: Python source
- Layer: unit/regression test
- Domain: isolated contract test evidence
- Responsibility: Provides complete unit and regression coverage for the `filter_shape` contracts exercised in this file.
- Source SHA256: `2e79e0eaf5d81ce2a6f9f1257e3c3b5d5dd5405594a6c02451c4ef029ed2b70a`

## 1. STEP 7F.1A.4 contract delta

- Refreshes permanent STEP 7F.1A.4 regression coverage for filter shape; the exact fixtures, mutations, calls, controlled failures, and assertions are inventoried below.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Provides complete unit and regression coverage for the `filter_shape` contracts exercised in this file.

The file belongs to the **unit/regression test** layer and **isolated contract test evidence** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- None.

### Third-party packages

- `import geopandas as gpd`
- `import pandas as pd`
- `import pytest`
- `from geopandas.testing import assert_geodataframe_equal`
- `from shapely.geometry import Polygon`

### Internal LandScout imports

- `from landscout.config import ShapeCalibrationConfig, ShapeScreeningConfig`
- `from landscout.stages.filter_parcels import (
    ParcelFilterError,
    filter_parcels_by_shape,
)`

## 4. Contract taxonomy

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `CASE_NAMES`

- Category: module constant or closed domain.
- Exact declaration:

```python
CASE_NAMES = (
    "at-boundaries",
    "passing",
    "width-below",
    "ratio-above",
    "shape-error",
    "width-unknown",
    "ratio-unknown",
    "both-unknown",
    "ratio-unknown-width-below",
    "both-thresholds-fail",
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `at-boundaries`
  - `passing`
  - `width-below`
  - `ratio-above`
  - `shape-error`
  - `width-unknown`
  - `ratio-unknown`
  - `both-unknown`
  - `ratio-unknown-width-below`
  - `both-thresholds-fail`

### `PARCEL_IDS`

- Category: module constant or closed domain.
- Exact declaration:

```python
PARCEL_IDS = {
    name: f"313950000A{index:04d}" for index, name in enumerate(CASE_NAMES, start=1)
}
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

No top-level class/model/dataclass is declared.

## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `_shape_config`

**Purpose:** Implements `shape config` within the file role: Provides complete unit and regression coverage for the `filter_shape` contracts exercised in this file.

**Exact signature**

```python
def _shape_config(
    *,
    min_width_m: float = 15,
    max_length_width_ratio: float = 10,
    policy_version: str = "test_policy_v1",
) -> ShapeScreeningConfig:
```

- Exact decorators: none.
- Declared return annotation: `ShapeScreeningConfig`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `min_width_m` | keyword-only | `float` | `15` |
| `max_length_width_ratio` | keyword-only | `float` | `10` |
| `policy_version` | keyword-only | `str` | `'test_policy_v1'` |

**Return and exception contract**

- Exact observed return expressions:
  - `ShapeScreeningConfig(<br>        enabled=True,<br>        min_width_m=min_width_m,<br>        max_length_width_ratio=max_length_width_ratio,<br>        calibration=ShapeCalibrationConfig(<br>            policy_version=policy_version,<br>            method="unit_test",<br>            calibration_scope="test fixture",<br>            sample_size=10,<br>            calibrated_at="2026-08-11",<br>            target_retention_pct=90,<br>            observed_retention_pct=90,<br>        ),<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_filter_shape::shape_config` via `_shape_config`
- value/type reference: `tests.unit.test_filter_shape::shape_config` via `_shape_config`
- direct call: `tests.unit.test_filter_shape::test_different_configs_change_results_for_same_parcels` via `_shape_config`
- value/type reference: `tests.unit.test_filter_shape::test_different_configs_change_results_for_same_parcels` via `_shape_config`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `ShapeScreeningConfig` | `landscout.config.ShapeScreeningConfig` |
| `ShapeCalibrationConfig` | `landscout.config.ShapeCalibrationConfig` |

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
def _shape_config(
    *,
    min_width_m: float = 15,
    max_length_width_ratio: float = 10,
    policy_version: str = "test_policy_v1",
) -> ShapeScreeningConfig:
    return ShapeScreeningConfig(
        enabled=True,
        min_width_m=min_width_m,
        max_length_width_ratio=max_length_width_ratio,
        calibration=ShapeCalibrationConfig(
            policy_version=policy_version,
            method="unit_test",
            calibration_scope="test fixture",
            sample_size=10,
            calibrated_at="2026-08-11",
            target_retention_pct=90,
            observed_retention_pct=90,
        ),
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `shape_config`

**Purpose:** Implements `shape config` within the file role: Provides complete unit and regression coverage for the `filter_shape` contracts exercised in this file.

**Exact signature**

```python
def shape_config() -> ShapeScreeningConfig:
```

- Exact decorators: `pytest.fixture`.
- Declared return annotation: `ShapeScreeningConfig`.

**Inputs**

- No parameters.

**Return and exception contract**

- Exact observed return expressions:
  - `_shape_config()`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- value/type reference: `tests.unit.test_filter_shape::test_exact_width_and_ratio_boundaries_are_retained` via `shape_config`
- value/type reference: `tests.unit.test_filter_shape::test_shape_filter_revalidates_mutated_config_before_frame_work` via `shape_config`
- value/type reference: `tests.unit.test_filter_shape::test_rejected_parcel_has_expected_primary_reason` via `shape_config`
- value/type reference: `tests.unit.test_filter_shape::test_rejection_reason_precedence_is_deterministic` via `shape_config`
- value/type reference: `tests.unit.test_filter_shape::test_shape_error_precedence_does_not_inspect_metrics` via `shape_config`
- value/type reference: `tests.unit.test_filter_shape::test_enabled_outputs_record_active_policy_metadata` via `shape_config`
- value/type reference: `tests.unit.test_filter_shape::test_enabled_partition_preserves_exact_ids_and_crs` via `shape_config`
- value/type reference: `tests.unit.test_filter_shape::test_filter_does_not_mutate_input` via `shape_config`
- value/type reference: `tests.unit.test_filter_shape::test_missing_required_column_fails` via `shape_config`
- value/type reference: `tests.unit.test_filter_shape::test_null_parcel_id_fails` via `shape_config`
- value/type reference: `tests.unit.test_filter_shape::test_duplicate_parcel_id_fails` via `shape_config`
- value/type reference: `tests.unit.test_filter_shape::test_unknown_crs_fails` via `shape_config`
- value/type reference: `tests.unit.test_filter_shape::test_unexpected_or_null_shape_status_fails` via `shape_config`
- value/type reference: `tests.unit.test_filter_shape::test_non_finite_known_metric_on_valid_row_fails` via `shape_config`
- value/type reference: `tests.unit.test_filter_shape::test_valid_shape_requires_strict_positive_width` via `shape_config`
- value/type reference: `tests.unit.test_filter_shape::test_valid_shape_requires_ratio_at_least_one` via `shape_config`
- value/type reference: `tests.unit.test_filter_shape::test_negative_ratio_cannot_pass_permissive_thresholds` via `shape_config`
- value/type reference: `tests.unit.test_filter_shape::test_valid_shape_rejects_every_incomplete_metric_form` via `shape_config`
- value/type reference: `tests.unit.test_filter_shape::test_shape_filter_rejects_plain_dataframe` via `shape_config`
- value/type reference: `tests.unit.test_filter_shape::test_shape_filter_rejects_duplicate_columns` via `shape_config`
- value/type reference: `tests.unit.test_filter_shape::test_shape_filter_rejects_unreadable_crs` via `shape_config`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_shape_config` | `tests.unit.test_filter_shape._shape_config` |

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
def shape_config() -> ShapeScreeningConfig:
    return _shape_config()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `parcels`

**Purpose:** Implements `parcels` within the file role: Provides complete unit and regression coverage for the `filter_shape` contracts exercised in this file.

**Exact signature**

```python
def parcels() -> gpd.GeoDataFrame:
```

- Exact decorators: `pytest.fixture`.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

- No parameters.

**Return and exception contract**

- Exact observed return expressions:
  - `gpd.GeoDataFrame(<br>        {<br>            "parcel_id": list(PARCEL_IDS.values()),<br>            "commune_code": ["31395"] * 10,<br>            "section_prefix": ["000"] * 10,<br>            "section": ["A"] * 10,<br>            "parcel_number": [str(index) for index in range(1, 11)],<br>            "source_contenance": [None] * 10,<br>            "source_arpente": [None] * 10,<br>            "source_created_at": [None] * 10,<br>            "source_updated_at": [None] * 10,<br>            "geometry_status": ["VALID"] * 10,<br>            "area_m2": [measured_area] * 10,<br>            "geometry": [geometry] * 10,<br>            "shape_status": [<br>                "VALID",<br>                "VALID",<br>                "VALID",<br>                "VALID",<br>                "ERROR",<br>                "ERROR",<br>                "ERROR",<br>                "ERROR",<br>                "ERROR",<br>                "VALID",<br>            ],<br>            "width_m": [15.0, 20.0, 14.9, 16.0, None, None, 20.0, None, 14.0, 14.0],<br>            "length_width_ratio": [<br>                10.0,<br>                5.0,<br>                8.0,<br>                10.1,<br>                None,<br>                2.0,<br>                None,<br>                None,<br>                None,<br>                11.0,<br>            ],<br>            "compactness": [0.5] * 10,<br>        },<br>        geometry="geometry",<br>        crs="EPSG:4326",<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- value/type reference: `tests.unit.test_filter_shape::test_exact_width_and_ratio_boundaries_are_retained` via `parcels`
- value/type reference: `tests.unit.test_filter_shape::test_shape_filter_revalidates_mutated_config_before_frame_work` via `parcels`
- value/type reference: `tests.unit.test_filter_shape::test_rejected_parcel_has_expected_primary_reason` via `parcels`
- value/type reference: `tests.unit.test_filter_shape::test_rejection_reason_precedence_is_deterministic` via `parcels`
- value/type reference: `tests.unit.test_filter_shape::test_shape_error_precedence_does_not_inspect_metrics` via `parcels`
- value/type reference: `tests.unit.test_filter_shape::test_enabled_outputs_record_active_policy_metadata` via `parcels`
- value/type reference: `tests.unit.test_filter_shape::test_enabled_partition_preserves_exact_ids_and_crs` via `parcels`
- value/type reference: `tests.unit.test_filter_shape::test_filter_does_not_mutate_input` via `parcels`
- value/type reference: `tests.unit.test_filter_shape::test_missing_required_column_fails` via `parcels`
- value/type reference: `tests.unit.test_filter_shape::test_null_parcel_id_fails` via `parcels`
- value/type reference: `tests.unit.test_filter_shape::test_duplicate_parcel_id_fails` via `parcels`
- value/type reference: `tests.unit.test_filter_shape::test_unknown_crs_fails` via `parcels`
- value/type reference: `tests.unit.test_filter_shape::test_unexpected_or_null_shape_status_fails` via `parcels`
- value/type reference: `tests.unit.test_filter_shape::test_non_finite_known_metric_on_valid_row_fails` via `parcels`
- value/type reference: `tests.unit.test_filter_shape::test_valid_shape_requires_strict_positive_width` via `parcels`
- value/type reference: `tests.unit.test_filter_shape::test_valid_shape_requires_ratio_at_least_one` via `parcels`
- value/type reference: `tests.unit.test_filter_shape::test_negative_ratio_cannot_pass_permissive_thresholds` via `parcels`
- value/type reference: `tests.unit.test_filter_shape::test_disabled_policy_is_an_exact_passthrough` via `parcels`
- value/type reference: `tests.unit.test_filter_shape::test_different_configs_change_results_for_same_parcels` via `parcels`
- value/type reference: `tests.unit.test_filter_shape::test_valid_shape_requires_complete_metrics_even_when_screening_disabled` via `parcels`
- value/type reference: `tests.unit.test_filter_shape::test_valid_shape_rejects_every_incomplete_metric_form` via `parcels`
- value/type reference: `tests.unit.test_filter_shape::test_shape_filter_rejects_plain_dataframe` via `parcels`
- value/type reference: `tests.unit.test_filter_shape::test_shape_filter_rejects_duplicate_columns` via `parcels`
- value/type reference: `tests.unit.test_filter_shape::test_shape_filter_rejects_unreadable_crs` via `parcels`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `Polygon` | `shapely.geometry.Polygon` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |
| `gpd.GeoSeries([geometry], crs="EPSG:4326").to_crs` | `unresolved local/third-party receiver; no ownership inferred` |
| `gpd.GeoSeries` | `geopandas.GeoSeries` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `PARCEL_IDS.values` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `range` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `gpd.GeoSeries([geometry], crs="EPSG:4326").to_crs` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def parcels() -> gpd.GeoDataFrame:
    geometry = Polygon([(2.0, 43.0), (2.01, 43.0), (2.01, 43.01), (2.0, 43.0)])
    measured_area = float(
        gpd.GeoSeries([geometry], crs="EPSG:4326").to_crs("EPSG:2154").area.iloc[0]
    )
    return gpd.GeoDataFrame(
        {
            "parcel_id": list(PARCEL_IDS.values()),
            "commune_code": ["31395"] * 10,
            "section_prefix": ["000"] * 10,
            "section": ["A"] * 10,
            "parcel_number": [str(index) for index in range(1, 11)],
            "source_contenance": [None] * 10,
            "source_arpente": [None] * 10,
            "source_created_at": [None] * 10,
            "source_updated_at": [None] * 10,
            "geometry_status": ["VALID"] * 10,
            "area_m2": [measured_area] * 10,
            "geometry": [geometry] * 10,
            "shape_status": [
                "VALID",
                "VALID",
                "VALID",
                "VALID",
                "ERROR",
                "ERROR",
                "ERROR",
                "ERROR",
                "ERROR",
                "VALID",
            ],
            "width_m": [15.0, 20.0, 14.9, 16.0, None, None, 20.0, None, 14.0, 14.0],
            "length_width_ratio": [
                10.0,
                5.0,
                8.0,
                10.1,
                None,
                2.0,
                None,
                None,
                None,
                11.0,
            ],
            "compactness": [0.5] * 10,
        },
        geometry="geometry",
        crs="EPSG:4326",
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_exact_width_and_ratio_boundaries_are_retained`

**Purpose:** Regression invariant: exact width and ratio boundaries are retained. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_exact_width_and_ratio_boundaries_are_retained(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `shape_config` | positional-or-keyword | `ShapeScreeningConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert PARCEL_IDS["at-boundaries"] in set(retained["parcel_id"])`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `filter_parcels_by_shape` | `landscout.stages.filter_parcels.filter_parcels_by_shape` |
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
def test_exact_width_and_ratio_boundaries_are_retained(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
    retained, _ = filter_parcels_by_shape(parcels, shape_config)

    assert PARCEL_IDS["at-boundaries"] in set(retained["parcel_id"])
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_shape_filter_revalidates_mutated_config_before_frame_work`

**Purpose:** Regression invariant: shape filter revalidates mutated config before frame work. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_shape_filter_revalidates_mutated_config_before_frame_work(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `shape_config` | positional-or-keyword | `ShapeScreeningConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ParcelFilterError, match="config")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `shape_config.model_copy` | `tests.unit.test_filter_shape.shape_config.model_copy` |
| `parcels.assign` | `tests.unit.test_filter_shape.parcels.assign` |
| `pytest.raises` | `pytest.raises` |
| `filter_parcels_by_shape` | `landscout.stages.filter_parcels.filter_parcels_by_shape` |

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
def test_shape_filter_revalidates_mutated_config_before_frame_work(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
) -> None:
    tampered = shape_config.model_copy(update={"min_width_m": -1.0})
    colliding = parcels.assign(shape_rejection_reason="existing")

    with pytest.raises(ParcelFilterError, match="config"):
        filter_parcels_by_shape(colliding, tampered)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_rejected_parcel_has_expected_primary_reason`

**Purpose:** Regression invariant: rejected parcel has expected primary reason. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_rejected_parcel_has_expected_primary_reason(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
    parcel_id: str,
    expected_reason: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("parcel_id", "expected_reason"),
    [
        ("width-below", "WIDTH_BELOW_MIN"),
        ("ratio-above", "RATIO_ABOVE_MAX"),
        ("shape-error", "SHAPE_ERROR"),
        ("width-unknown", "SHAPE_ERROR"),
        ("ratio-unknown", "SHAPE_ERROR"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `shape_config` | positional-or-keyword | `ShapeScreeningConfig` | `required` |
| `parcel_id` | positional-or-keyword | `str` | `required` |
| `expected_reason` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert row["shape_rejection_reason"] == expected_reason`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `filter_parcels_by_shape` | `landscout.stages.filter_parcels.filter_parcels_by_shape` |
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
def test_rejected_parcel_has_expected_primary_reason(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
    parcel_id: str,
    expected_reason: str,
) -> None:
    _, rejected = filter_parcels_by_shape(parcels, shape_config)

    row = rejected.loc[rejected["parcel_id"] == PARCEL_IDS[parcel_id]].iloc[0]
    assert row["shape_rejection_reason"] == expected_reason
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_rejection_reason_precedence_is_deterministic`

**Purpose:** Regression invariant: rejection reason precedence is deterministic. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_rejection_reason_precedence_is_deterministic(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
    parcel_id: str,
    expected_reason: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("parcel_id", "expected_reason"),
    [
        ("shape-error", "SHAPE_ERROR"),
        ("both-unknown", "SHAPE_ERROR"),
        ("ratio-unknown-width-below", "SHAPE_ERROR"),
        ("both-thresholds-fail", "WIDTH_BELOW_MIN"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `shape_config` | positional-or-keyword | `ShapeScreeningConfig` | `required` |
| `parcel_id` | positional-or-keyword | `str` | `required` |
| `expected_reason` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert reason == expected_reason`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `filter_parcels_by_shape` | `landscout.stages.filter_parcels.filter_parcels_by_shape` |
| `rejected.set_index` | `unresolved local/third-party receiver; no ownership inferred` |
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
def test_rejection_reason_precedence_is_deterministic(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
    parcel_id: str,
    expected_reason: str,
) -> None:
    _, rejected = filter_parcels_by_shape(parcels, shape_config)

    reason = rejected.set_index("parcel_id").loc[
        PARCEL_IDS[parcel_id], "shape_rejection_reason"
    ]
    assert reason == expected_reason
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_shape_error_precedence_does_not_inspect_metrics`

**Purpose:** Regression invariant: shape error precedence does not inspect metrics. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_shape_error_precedence_does_not_inspect_metrics(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `shape_config` | positional-or-keyword | `ShapeScreeningConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert reason == "SHAPE_ERROR"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `parcels.copy` | `tests.unit.test_filter_shape.parcels.copy` |
| `with_error_payload["width_m"].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `with_error_payload[<br>        "length_width_ratio"<br>    ].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `filter_parcels_by_shape` | `landscout.stages.filter_parcels.filter_parcels_by_shape` |
| `rejected.set_index` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `with_error_payload["width_m"] = with_error_payload["width_m"].astype(object)`<br>`with_error_payload["length_width_ratio"] = with_error_payload[<br>        "length_width_ratio"<br>    ].astype(object)`<br>`with_error_payload.loc[error_row, "width_m"] = "unavailable"`<br>`with_error_payload.loc[error_row, "length_width_ratio"] = "unavailable"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_shape_error_precedence_does_not_inspect_metrics(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
    with_error_payload = parcels.copy()
    with_error_payload["width_m"] = with_error_payload["width_m"].astype(object)
    with_error_payload["length_width_ratio"] = with_error_payload[
        "length_width_ratio"
    ].astype(object)
    error_row = with_error_payload["parcel_id"] == PARCEL_IDS["shape-error"]
    with_error_payload.loc[error_row, "width_m"] = "unavailable"
    with_error_payload.loc[error_row, "length_width_ratio"] = "unavailable"

    _, rejected = filter_parcels_by_shape(with_error_payload, shape_config)

    reason = rejected.set_index("parcel_id").loc[
        PARCEL_IDS["shape-error"], "shape_rejection_reason"
    ]
    assert reason == "SHAPE_ERROR"
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_enabled_outputs_record_active_policy_metadata`

**Purpose:** Regression invariant: enabled outputs record active policy metadata. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_enabled_outputs_record_active_policy_metadata(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `shape_config` | positional-or-keyword | `ShapeScreeningConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert set(output["shape_policy_version"]) == {"test_policy_v1"}`
  - `assert set(output["shape_policy_min_width_m"]) == {15.0}`
  - `assert set(output["shape_policy_max_ratio"]) == {10.0}`
  - `assert "shape_rejection_reason" not in retained.columns`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `filter_parcels_by_shape` | `landscout.stages.filter_parcels.filter_parcels_by_shape` |
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
def test_enabled_outputs_record_active_policy_metadata(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
    retained, rejected = filter_parcels_by_shape(parcels, shape_config)

    for output in (retained, rejected):
        assert set(output["shape_policy_version"]) == {"test_policy_v1"}
        assert set(output["shape_policy_min_width_m"]) == {15.0}
        assert set(output["shape_policy_max_ratio"]) == {10.0}
    assert "shape_rejection_reason" not in retained.columns
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_enabled_partition_preserves_exact_ids_and_crs`

**Purpose:** Regression invariant: enabled partition preserves exact ids and crs. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_enabled_partition_preserves_exact_ids_and_crs(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `shape_config` | positional-or-keyword | `ShapeScreeningConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert len(parcels) == len(retained) + len(rejected)`
  - `assert retained_ids.isdisjoint(rejected_ids)`
  - `assert retained_ids \| rejected_ids == set(parcels["parcel_id"])`
  - `assert not retained["parcel_id"].duplicated().any()`
  - `assert not rejected["parcel_id"].duplicated().any()`
  - `assert retained.crs == parcels.crs`
  - `assert rejected.crs == parcels.crs`
  - `assert "compactness" in retained.columns`
  - `assert "compactness" in rejected.columns`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `filter_parcels_by_shape` | `landscout.stages.filter_parcels.filter_parcels_by_shape` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `retained_ids.isdisjoint` | `unresolved local/third-party receiver; no ownership inferred` |
| `retained["parcel_id"].duplicated().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `retained["parcel_id"].duplicated` | `unresolved local/third-party receiver; no ownership inferred` |
| `rejected["parcel_id"].duplicated().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `rejected["parcel_id"].duplicated` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `retained_ids.isdisjoint` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_enabled_partition_preserves_exact_ids_and_crs(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
    retained, rejected = filter_parcels_by_shape(parcels, shape_config)

    retained_ids = set(retained["parcel_id"])
    rejected_ids = set(rejected["parcel_id"])
    assert len(parcels) == len(retained) + len(rejected)
    assert retained_ids.isdisjoint(rejected_ids)
    assert retained_ids | rejected_ids == set(parcels["parcel_id"])
    assert not retained["parcel_id"].duplicated().any()
    assert not rejected["parcel_id"].duplicated().any()
    assert retained.crs == parcels.crs
    assert rejected.crs == parcels.crs
    assert "compactness" in retained.columns
    assert "compactness" in rejected.columns
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_filter_does_not_mutate_input`

**Purpose:** Regression invariant: filter does not mutate input. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_filter_does_not_mutate_input(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `shape_config` | positional-or-keyword | `ShapeScreeningConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `parcels.copy` | `tests.unit.test_filter_shape.parcels.copy` |
| `filter_parcels_by_shape` | `landscout.stages.filter_parcels.filter_parcels_by_shape` |
| `assert_geodataframe_equal` | `geopandas.testing.assert_geodataframe_equal` |

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
def test_filter_does_not_mutate_input(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
    original = parcels.copy(deep=True)

    filter_parcels_by_shape(parcels, shape_config)

    assert_geodataframe_equal(parcels, original)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_missing_required_column_fails`

**Purpose:** Regression invariant: missing required column fails. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_missing_required_column_fails(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
    column: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "column",
    ["parcel_id", "shape_status", "width_m", "length_width_ratio", "geometry"],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `shape_config` | positional-or-keyword | `ShapeScreeningConfig` | `required` |
| `column` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ParcelFilterError, match="Missing required shape columns")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `parcels.drop` | `tests.unit.test_filter_shape.parcels.drop` |
| `pytest.raises` | `pytest.raises` |
| `filter_parcels_by_shape` | `landscout.stages.filter_parcels.filter_parcels_by_shape` |
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
| In-memory mutation | `parcels.drop(columns=[column])` |
| Direct parameter mutation | `parcels.drop(columns=[column])` |

**Complete source-ordered implementation**

```python
def test_missing_required_column_fails(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
    column: str,
) -> None:
    missing_column = parcels.drop(columns=[column])

    with pytest.raises(ParcelFilterError, match="Missing required shape columns"):
        filter_parcels_by_shape(missing_column, shape_config)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_null_parcel_id_fails`

**Purpose:** Regression invariant: null parcel id fails. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_null_parcel_id_fails(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `shape_config` | positional-or-keyword | `ShapeScreeningConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ParcelFilterError, match="must not be null")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `parcels.copy` | `tests.unit.test_filter_shape.parcels.copy` |
| `pytest.raises` | `pytest.raises` |
| `filter_parcels_by_shape` | `landscout.stages.filter_parcels.filter_parcels_by_shape` |

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
| In-memory mutation | `invalid.loc[0, "parcel_id"] = None` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_null_parcel_id_fails(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
    invalid = parcels.copy()
    invalid.loc[0, "parcel_id"] = None

    with pytest.raises(ParcelFilterError, match="must not be null"):
        filter_parcels_by_shape(invalid, shape_config)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_duplicate_parcel_id_fails`

**Purpose:** Regression invariant: duplicate parcel id fails. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_duplicate_parcel_id_fails(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `shape_config` | positional-or-keyword | `ShapeScreeningConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ParcelFilterError, match="must be unique")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `parcels.copy` | `tests.unit.test_filter_shape.parcels.copy` |
| `pytest.raises` | `pytest.raises` |
| `filter_parcels_by_shape` | `landscout.stages.filter_parcels.filter_parcels_by_shape` |

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
| In-memory mutation | `invalid.loc[1, "parcel_id"] = invalid.loc[0, "parcel_id"]` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_duplicate_parcel_id_fails(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
    invalid = parcels.copy()
    invalid.loc[1, "parcel_id"] = invalid.loc[0, "parcel_id"]

    with pytest.raises(ParcelFilterError, match="must be unique"):
        filter_parcels_by_shape(invalid, shape_config)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unknown_crs_fails`

**Purpose:** Regression invariant: unknown crs fails. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_unknown_crs_fails(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `shape_config` | positional-or-keyword | `ShapeScreeningConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ParcelFilterError, match="known CRS")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `parcels.set_crs` | `tests.unit.test_filter_shape.parcels.set_crs` |
| `pytest.raises` | `pytest.raises` |
| `filter_parcels_by_shape` | `landscout.stages.filter_parcels.filter_parcels_by_shape` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `parcels.set_crs` |
| External process/environment | None directly present. |
| In-memory mutation | `parcels.set_crs(None, allow_override=True)` |
| Direct parameter mutation | `parcels.set_crs(None, allow_override=True)` |

**Complete source-ordered implementation**

```python
def test_unknown_crs_fails(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
    invalid = parcels.set_crs(None, allow_override=True)

    with pytest.raises(ParcelFilterError, match="known CRS"):
        filter_parcels_by_shape(invalid, shape_config)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unexpected_or_null_shape_status_fails`

**Purpose:** Regression invariant: unexpected or null shape status fails. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_unexpected_or_null_shape_status_fails(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
    status: str | None,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("status", [None, "UNKNOWN"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `shape_config` | positional-or-keyword | `ShapeScreeningConfig` | `required` |
| `status` | positional-or-keyword | `str \| None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ParcelFilterError, match="Unexpected shape_status")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `parcels.copy` | `tests.unit.test_filter_shape.parcels.copy` |
| `pytest.raises` | `pytest.raises` |
| `filter_parcels_by_shape` | `landscout.stages.filter_parcels.filter_parcels_by_shape` |
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
| In-memory mutation | `invalid.loc[0, "shape_status"] = status` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_unexpected_or_null_shape_status_fails(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
    status: str | None,
) -> None:
    invalid = parcels.copy()
    invalid.loc[0, "shape_status"] = status

    with pytest.raises(ParcelFilterError, match="Unexpected shape_status"):
        filter_parcels_by_shape(invalid, shape_config)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_non_finite_known_metric_on_valid_row_fails`

**Purpose:** Regression invariant: non finite known metric on valid row fails. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_non_finite_known_metric_on_valid_row_fails(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
    column: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("column", ["width_m", "length_width_ratio"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `shape_config` | positional-or-keyword | `ShapeScreeningConfig` | `required` |
| `column` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ParcelFilterError, match="numeric and finite")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `parcels.copy` | `tests.unit.test_filter_shape.parcels.copy` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `filter_parcels_by_shape` | `landscout.stages.filter_parcels.filter_parcels_by_shape` |
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
| In-memory mutation | `invalid.loc[0, column] = float("inf")` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_non_finite_known_metric_on_valid_row_fails(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
    column: str,
) -> None:
    invalid = parcels.copy()
    invalid.loc[0, column] = float("inf")

    with pytest.raises(ParcelFilterError, match="numeric and finite"):
        filter_parcels_by_shape(invalid, shape_config)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_valid_shape_requires_strict_positive_width`

**Purpose:** Regression invariant: valid shape requires strict positive width. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_valid_shape_requires_strict_positive_width(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
    width: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("width", [-1, 0, float("inf"), "20", True])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `shape_config` | positional-or-keyword | `ShapeScreeningConfig` | `required` |
| `width` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        ParcelFilterError,<br>        match="width_m must be (numeric and finite\|greater than zero)",<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `parcels.copy` | `tests.unit.test_filter_shape.parcels.copy` |
| `invalid["width_m"].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `filter_parcels_by_shape` | `landscout.stages.filter_parcels.filter_parcels_by_shape` |
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
| In-memory mutation | `invalid["width_m"] = invalid["width_m"].astype(object)`<br>`invalid.loc[0, "width_m"] = width` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_valid_shape_requires_strict_positive_width(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
    width: object,
) -> None:
    invalid = parcels.copy()
    invalid["width_m"] = invalid["width_m"].astype(object)
    invalid.loc[0, "width_m"] = width

    with pytest.raises(
        ParcelFilterError,
        match="width_m must be (numeric and finite|greater than zero)",
    ):
        filter_parcels_by_shape(invalid, shape_config)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_valid_shape_requires_ratio_at_least_one`

**Purpose:** Regression invariant: valid shape requires ratio at least one. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_valid_shape_requires_ratio_at_least_one(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
    ratio: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("ratio", [-1, 0, 0.999, float("inf"), "2", True])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `shape_config` | positional-or-keyword | `ShapeScreeningConfig` | `required` |
| `ratio` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        ParcelFilterError,<br>        match="length_width_ratio must be (numeric and finite\|at least one)",<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `parcels.copy` | `tests.unit.test_filter_shape.parcels.copy` |
| `invalid["length_width_ratio"].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `filter_parcels_by_shape` | `landscout.stages.filter_parcels.filter_parcels_by_shape` |
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
| In-memory mutation | `invalid["length_width_ratio"] = invalid["length_width_ratio"].astype(object)`<br>`invalid.loc[0, "length_width_ratio"] = ratio` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_valid_shape_requires_ratio_at_least_one(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
    ratio: object,
) -> None:
    invalid = parcels.copy()
    invalid["length_width_ratio"] = invalid["length_width_ratio"].astype(object)
    invalid.loc[0, "length_width_ratio"] = ratio

    with pytest.raises(
        ParcelFilterError,
        match="length_width_ratio must be (numeric and finite|at least one)",
    ):
        filter_parcels_by_shape(invalid, shape_config)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_negative_ratio_cannot_pass_permissive_thresholds`

**Purpose:** Regression invariant: negative ratio cannot pass permissive thresholds. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_negative_ratio_cannot_pass_permissive_thresholds(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `shape_config` | positional-or-keyword | `ShapeScreeningConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        ParcelFilterError, match="length_width_ratio must be at least one"<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `parcels.copy` | `tests.unit.test_filter_shape.parcels.copy` |
| `pytest.raises` | `pytest.raises` |
| `filter_parcels_by_shape` | `landscout.stages.filter_parcels.filter_parcels_by_shape` |

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
| In-memory mutation | `invalid.loc[0, "width_m"] = 20`<br>`invalid.loc[0, "length_width_ratio"] = -1` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_negative_ratio_cannot_pass_permissive_thresholds(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
) -> None:
    invalid = parcels.copy()
    invalid.loc[0, "width_m"] = 20
    invalid.loc[0, "length_width_ratio"] = -1

    with pytest.raises(
        ParcelFilterError, match="length_width_ratio must be at least one"
    ):
        filter_parcels_by_shape(invalid, shape_config)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_disabled_policy_is_an_exact_passthrough`

**Purpose:** Regression invariant: disabled policy is an exact passthrough. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_disabled_policy_is_an_exact_passthrough(parcels: gpd.GeoDataFrame) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert column not in retained.columns`
  - `assert column not in rejected.columns`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `ShapeScreeningConfig` | `landscout.config.ShapeScreeningConfig` |
| `filter_parcels_by_shape` | `landscout.stages.filter_parcels.filter_parcels_by_shape` |
| `assert_geodataframe_equal` | `geopandas.testing.assert_geodataframe_equal` |

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
def test_disabled_policy_is_an_exact_passthrough(parcels: gpd.GeoDataFrame) -> None:
    disabled = ShapeScreeningConfig(enabled=False)

    retained, rejected = filter_parcels_by_shape(parcels, disabled)

    assert_geodataframe_equal(retained, parcels)
    assert_geodataframe_equal(rejected, parcels.iloc[0:0])
    for column in (
        "shape_rejection_reason",
        "shape_policy_version",
        "shape_policy_min_width_m",
        "shape_policy_max_ratio",
    ):
        assert column not in retained.columns
        assert column not in rejected.columns
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_different_configs_change_results_for_same_parcels`

**Purpose:** Regression invariant: different configs change results for same parcels. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_different_configs_change_results_for_same_parcels(
    parcels: gpd.GeoDataFrame,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert set(permissive_retained["parcel_id"]) == {<br>        PARCEL_IDS["at-boundaries"],<br>        PARCEL_IDS["passing"],<br>        PARCEL_IDS["width-below"],<br>        PARCEL_IDS["ratio-above"],<br>        PARCEL_IDS["both-thresholds-fail"],<br>    }`
  - `assert set(restrictive_retained["parcel_id"]) == {PARCEL_IDS["passing"]}`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_shape_config` | `tests.unit.test_filter_shape._shape_config` |
| `filter_parcels_by_shape` | `landscout.stages.filter_parcels.filter_parcels_by_shape` |
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
def test_different_configs_change_results_for_same_parcels(
    parcels: gpd.GeoDataFrame,
) -> None:
    permissive = _shape_config(
        min_width_m=10,
        max_length_width_ratio=12,
        policy_version="permissive",
    )
    restrictive = _shape_config(
        min_width_m=18,
        max_length_width_ratio=6,
        policy_version="restrictive",
    )

    permissive_retained, _ = filter_parcels_by_shape(parcels, permissive)
    restrictive_retained, _ = filter_parcels_by_shape(parcels, restrictive)

    assert set(permissive_retained["parcel_id"]) == {
        PARCEL_IDS["at-boundaries"],
        PARCEL_IDS["passing"],
        PARCEL_IDS["width-below"],
        PARCEL_IDS["ratio-above"],
        PARCEL_IDS["both-thresholds-fail"],
    }
    assert set(restrictive_retained["parcel_id"]) == {PARCEL_IDS["passing"]}
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_valid_shape_requires_complete_metrics_even_when_screening_disabled`

**Purpose:** Regression invariant: valid shape requires complete metrics even when screening disabled. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_valid_shape_requires_complete_metrics_even_when_screening_disabled(
    parcels: gpd.GeoDataFrame,
    column: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("column", ["width_m", "length_width_ratio"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `column` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ParcelFilterError, match="complete\|must not be null")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `parcels.copy` | `tests.unit.test_filter_shape.parcels.copy` |
| `pytest.raises` | `pytest.raises` |
| `filter_parcels_by_shape` | `landscout.stages.filter_parcels.filter_parcels_by_shape` |
| `ShapeScreeningConfig` | `landscout.config.ShapeScreeningConfig` |
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
| In-memory mutation | `invalid.loc[0, column] = None` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_valid_shape_requires_complete_metrics_even_when_screening_disabled(
    parcels: gpd.GeoDataFrame,
    column: str,
) -> None:
    invalid = parcels.copy()
    invalid.loc[0, column] = None

    with pytest.raises(ParcelFilterError, match="complete|must not be null"):
        filter_parcels_by_shape(invalid, ShapeScreeningConfig(enabled=False))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_valid_shape_rejects_every_incomplete_metric_form`

**Purpose:** Regression invariant: valid shape rejects every incomplete metric form. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_valid_shape_rejects_every_incomplete_metric_form(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
    width: float | None,
    ratio: float | None,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("width", "ratio"),
    [
        (None, 5.0),
        (20.0, None),
        (None, None),
        (float("nan"), 5.0),
        (20.0, float("nan")),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `shape_config` | positional-or-keyword | `ShapeScreeningConfig` | `required` |
| `width` | positional-or-keyword | `float \| None` | `required` |
| `ratio` | positional-or-keyword | `float \| None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ParcelFilterError, match="complete")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `parcels.copy` | `tests.unit.test_filter_shape.parcels.copy` |
| `pytest.raises` | `pytest.raises` |
| `filter_parcels_by_shape` | `landscout.stages.filter_parcels.filter_parcels_by_shape` |
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
| In-memory mutation | `invalid.loc[0, "width_m"] = width`<br>`invalid.loc[0, "length_width_ratio"] = ratio` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_valid_shape_rejects_every_incomplete_metric_form(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
    width: float | None,
    ratio: float | None,
) -> None:
    invalid = parcels.copy()
    invalid.loc[0, "width_m"] = width
    invalid.loc[0, "length_width_ratio"] = ratio

    with pytest.raises(ParcelFilterError, match="complete"):
        filter_parcels_by_shape(invalid, shape_config)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_shape_filter_rejects_plain_dataframe`

**Purpose:** Regression invariant: shape filter rejects plain dataframe. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_shape_filter_rejects_plain_dataframe(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `shape_config` | positional-or-keyword | `ShapeScreeningConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ParcelFilterError, match="GeoDataFrame")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `filter_parcels_by_shape` | `landscout.stages.filter_parcels.filter_parcels_by_shape` |
| `pd.DataFrame` | `pandas.DataFrame` |

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
def test_shape_filter_rejects_plain_dataframe(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
    with pytest.raises(ParcelFilterError, match="GeoDataFrame"):
        filter_parcels_by_shape(
            pd.DataFrame(parcels),  # type: ignore[arg-type]
            shape_config,
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_shape_filter_rejects_duplicate_columns`

**Purpose:** Regression invariant: shape filter rejects duplicate columns. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_shape_filter_rejects_duplicate_columns(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `shape_config` | positional-or-keyword | `ShapeScreeningConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ParcelFilterError, match="columns.*unique")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `pd.concat` | `pandas.concat` |
| `pytest.raises` | `pytest.raises` |
| `filter_parcels_by_shape` | `landscout.stages.filter_parcels.filter_parcels_by_shape` |

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
def test_shape_filter_rejects_duplicate_columns(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
    duplicate = gpd.GeoDataFrame(
        pd.concat([parcels, parcels[["parcel_id"]]], axis=1),
        geometry="geometry",
        crs=parcels.crs,
    )

    with pytest.raises(ParcelFilterError, match="columns.*unique"):
        filter_parcels_by_shape(duplicate, shape_config)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_shape_filter_rejects_unreadable_crs`

**Purpose:** Regression invariant: shape filter rejects unreadable crs. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_shape_filter_rejects_unreadable_crs(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `shape_config` | positional-or-keyword | `ShapeScreeningConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ParcelFilterError, match="CRS")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `parcels.copy` | `tests.unit.test_filter_shape.parcels.copy` |
| `pytest.raises` | `pytest.raises` |
| `filter_parcels_by_shape` | `landscout.stages.filter_parcels.filter_parcels_by_shape` |

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
| In-memory mutation | `invalid.geometry.array._crs = "not-a-crs"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_shape_filter_rejects_unreadable_crs(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
    invalid = parcels.copy()
    invalid.geometry.array._crs = "not-a-crs"

    with pytest.raises(ParcelFilterError, match="CRS"):
        filter_parcels_by_shape(invalid, shape_config)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.


## 7. Test-specific regression contract

- Test functions: **24**.
- Pytest fixtures (decorator-proven): **2**.

### Fixtures

- `shape_config` — decorators: `pytest.fixture`.
- `parcels` — decorators: `pytest.fixture`.

### Per-test regression index

| Test | Parametrization | Expected exception contexts | Assertion count | Exact regression purpose |
|---|---|---|---:|---|
| `test_exact_width_and_ratio_boundaries_are_retained` | none | none | 1 | Proves exact width and ratio boundaries are retained using the exact source reproduced in section 7. |
| `test_shape_filter_revalidates_mutated_config_before_frame_work` | none | pytest.raises(ParcelFilterError, match="config") | 0 | Proves shape filter revalidates mutated config before frame work using the exact source reproduced in section 7. |
| `test_rejected_parcel_has_expected_primary_reason` | pytest.mark.parametrize(<br>    ("parcel_id", "expected_reason"),<br>    [<br>        ("width-below", "WIDTH_BELOW_MIN"),<br>        ("ratio-above", "RATIO_ABOVE_MAX"),<br>        ("shape-error", "SHAPE_ERROR"),<br>        ("width-unknown", "SHAPE_ERROR"),<br>        ("ratio-unknown", "SHAPE_ERROR"),<br>    ],<br>) | none | 1 | Proves rejected parcel has expected primary reason using the exact source reproduced in section 7. |
| `test_rejection_reason_precedence_is_deterministic` | pytest.mark.parametrize(<br>    ("parcel_id", "expected_reason"),<br>    [<br>        ("shape-error", "SHAPE_ERROR"),<br>        ("both-unknown", "SHAPE_ERROR"),<br>        ("ratio-unknown-width-below", "SHAPE_ERROR"),<br>        ("both-thresholds-fail", "WIDTH_BELOW_MIN"),<br>    ],<br>) | none | 1 | Proves rejection reason precedence is deterministic using the exact source reproduced in section 7. |
| `test_shape_error_precedence_does_not_inspect_metrics` | none | none | 1 | Proves shape error precedence does not inspect metrics using the exact source reproduced in section 7. |
| `test_enabled_outputs_record_active_policy_metadata` | none | none | 4 | Proves enabled outputs record active policy metadata using the exact source reproduced in section 7. |
| `test_enabled_partition_preserves_exact_ids_and_crs` | none | none | 9 | Proves enabled partition preserves exact ids and crs using the exact source reproduced in section 7. |
| `test_filter_does_not_mutate_input` | none | none | 0 | Proves filter does not mutate input using the exact source reproduced in section 7. |
| `test_missing_required_column_fails` | pytest.mark.parametrize(<br>    "column",<br>    ["parcel_id", "shape_status", "width_m", "length_width_ratio", "geometry"],<br>) | pytest.raises(ParcelFilterError, match="Missing required shape columns") | 0 | Proves missing required column fails using the exact source reproduced in section 7. |
| `test_null_parcel_id_fails` | none | pytest.raises(ParcelFilterError, match="must not be null") | 0 | Proves null parcel id fails using the exact source reproduced in section 7. |
| `test_duplicate_parcel_id_fails` | none | pytest.raises(ParcelFilterError, match="must be unique") | 0 | Proves duplicate parcel id fails using the exact source reproduced in section 7. |
| `test_unknown_crs_fails` | none | pytest.raises(ParcelFilterError, match="known CRS") | 0 | Proves unknown crs fails using the exact source reproduced in section 7. |
| `test_unexpected_or_null_shape_status_fails` | pytest.mark.parametrize("status", [None, "UNKNOWN"]) | pytest.raises(ParcelFilterError, match="Unexpected shape_status") | 0 | Proves unexpected or null shape status fails using the exact source reproduced in section 7. |
| `test_non_finite_known_metric_on_valid_row_fails` | pytest.mark.parametrize("column", ["width_m", "length_width_ratio"]) | pytest.raises(ParcelFilterError, match="numeric and finite") | 0 | Proves non finite known metric on valid row fails using the exact source reproduced in section 7. |
| `test_valid_shape_requires_strict_positive_width` | pytest.mark.parametrize("width", [-1, 0, float("inf"), "20", True]) | pytest.raises(<br>        ParcelFilterError,<br>        match="width_m must be (numeric and finite\|greater than zero)",<br>    ) | 0 | Proves valid shape requires strict positive width using the exact source reproduced in section 7. |
| `test_valid_shape_requires_ratio_at_least_one` | pytest.mark.parametrize("ratio", [-1, 0, 0.999, float("inf"), "2", True]) | pytest.raises(<br>        ParcelFilterError,<br>        match="length_width_ratio must be (numeric and finite\|at least one)",<br>    ) | 0 | Proves valid shape requires ratio at least one using the exact source reproduced in section 7. |
| `test_negative_ratio_cannot_pass_permissive_thresholds` | none | pytest.raises(<br>        ParcelFilterError, match="length_width_ratio must be at least one"<br>    ) | 0 | Proves negative ratio cannot pass permissive thresholds using the exact source reproduced in section 7. |
| `test_disabled_policy_is_an_exact_passthrough` | none | none | 2 | Proves disabled policy is an exact passthrough using the exact source reproduced in section 7. |
| `test_different_configs_change_results_for_same_parcels` | none | none | 2 | Proves different configs change results for same parcels using the exact source reproduced in section 7. |
| `test_valid_shape_requires_complete_metrics_even_when_screening_disabled` | pytest.mark.parametrize("column", ["width_m", "length_width_ratio"]) | pytest.raises(ParcelFilterError, match="complete\|must not be null") | 0 | Proves valid shape requires complete metrics even when screening disabled using the exact source reproduced in section 7. |
| `test_valid_shape_rejects_every_incomplete_metric_form` | pytest.mark.parametrize(<br>    ("width", "ratio"),<br>    [<br>        (None, 5.0),<br>        (20.0, None),<br>        (None, None),<br>        (float("nan"), 5.0),<br>        (20.0, float("nan")),<br>    ],<br>) | pytest.raises(ParcelFilterError, match="complete") | 0 | Proves valid shape rejects every incomplete metric form using the exact source reproduced in section 7. |
| `test_shape_filter_rejects_plain_dataframe` | none | pytest.raises(ParcelFilterError, match="GeoDataFrame") | 0 | Proves shape filter rejects plain dataframe using the exact source reproduced in section 7. |
| `test_shape_filter_rejects_duplicate_columns` | none | pytest.raises(ParcelFilterError, match="columns.*unique") | 0 | Proves shape filter rejects duplicate columns using the exact source reproduced in section 7. |
| `test_shape_filter_rejects_unreadable_crs` | none | pytest.raises(ParcelFilterError, match="CRS") | 0 | Proves shape filter rejects unreadable crs using the exact source reproduced in section 7. |

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
import geopandas as gpd
import pandas as pd
import pytest
from geopandas.testing import assert_geodataframe_equal
from shapely.geometry import Polygon

from landscout.config import ShapeCalibrationConfig, ShapeScreeningConfig
from landscout.stages.filter_parcels import (
    ParcelFilterError,
    filter_parcels_by_shape,
)

CASE_NAMES = (
    "at-boundaries",
    "passing",
    "width-below",
    "ratio-above",
    "shape-error",
    "width-unknown",
    "ratio-unknown",
    "both-unknown",
    "ratio-unknown-width-below",
    "both-thresholds-fail",
)
PARCEL_IDS = {
    name: f"313950000A{index:04d}" for index, name in enumerate(CASE_NAMES, start=1)
}


def _shape_config(
    *,
    min_width_m: float = 15,
    max_length_width_ratio: float = 10,
    policy_version: str = "test_policy_v1",
) -> ShapeScreeningConfig:
    return ShapeScreeningConfig(
        enabled=True,
        min_width_m=min_width_m,
        max_length_width_ratio=max_length_width_ratio,
        calibration=ShapeCalibrationConfig(
            policy_version=policy_version,
            method="unit_test",
            calibration_scope="test fixture",
            sample_size=10,
            calibrated_at="2026-08-11",
            target_retention_pct=90,
            observed_retention_pct=90,
        ),
    )


@pytest.fixture
def shape_config() -> ShapeScreeningConfig:
    return _shape_config()


@pytest.fixture
def parcels() -> gpd.GeoDataFrame:
    geometry = Polygon([(2.0, 43.0), (2.01, 43.0), (2.01, 43.01), (2.0, 43.0)])
    measured_area = float(
        gpd.GeoSeries([geometry], crs="EPSG:4326").to_crs("EPSG:2154").area.iloc[0]
    )
    return gpd.GeoDataFrame(
        {
            "parcel_id": list(PARCEL_IDS.values()),
            "commune_code": ["31395"] * 10,
            "section_prefix": ["000"] * 10,
            "section": ["A"] * 10,
            "parcel_number": [str(index) for index in range(1, 11)],
            "source_contenance": [None] * 10,
            "source_arpente": [None] * 10,
            "source_created_at": [None] * 10,
            "source_updated_at": [None] * 10,
            "geometry_status": ["VALID"] * 10,
            "area_m2": [measured_area] * 10,
            "geometry": [geometry] * 10,
            "shape_status": [
                "VALID",
                "VALID",
                "VALID",
                "VALID",
                "ERROR",
                "ERROR",
                "ERROR",
                "ERROR",
                "ERROR",
                "VALID",
            ],
            "width_m": [15.0, 20.0, 14.9, 16.0, None, None, 20.0, None, 14.0, 14.0],
            "length_width_ratio": [
                10.0,
                5.0,
                8.0,
                10.1,
                None,
                2.0,
                None,
                None,
                None,
                11.0,
            ],
            "compactness": [0.5] * 10,
        },
        geometry="geometry",
        crs="EPSG:4326",
    )


def test_exact_width_and_ratio_boundaries_are_retained(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
    retained, _ = filter_parcels_by_shape(parcels, shape_config)

    assert PARCEL_IDS["at-boundaries"] in set(retained["parcel_id"])


def test_shape_filter_revalidates_mutated_config_before_frame_work(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
) -> None:
    tampered = shape_config.model_copy(update={"min_width_m": -1.0})
    colliding = parcels.assign(shape_rejection_reason="existing")

    with pytest.raises(ParcelFilterError, match="config"):
        filter_parcels_by_shape(colliding, tampered)


@pytest.mark.parametrize(
    ("parcel_id", "expected_reason"),
    [
        ("width-below", "WIDTH_BELOW_MIN"),
        ("ratio-above", "RATIO_ABOVE_MAX"),
        ("shape-error", "SHAPE_ERROR"),
        ("width-unknown", "SHAPE_ERROR"),
        ("ratio-unknown", "SHAPE_ERROR"),
    ],
)
def test_rejected_parcel_has_expected_primary_reason(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
    parcel_id: str,
    expected_reason: str,
) -> None:
    _, rejected = filter_parcels_by_shape(parcels, shape_config)

    row = rejected.loc[rejected["parcel_id"] == PARCEL_IDS[parcel_id]].iloc[0]
    assert row["shape_rejection_reason"] == expected_reason


@pytest.mark.parametrize(
    ("parcel_id", "expected_reason"),
    [
        ("shape-error", "SHAPE_ERROR"),
        ("both-unknown", "SHAPE_ERROR"),
        ("ratio-unknown-width-below", "SHAPE_ERROR"),
        ("both-thresholds-fail", "WIDTH_BELOW_MIN"),
    ],
)
def test_rejection_reason_precedence_is_deterministic(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
    parcel_id: str,
    expected_reason: str,
) -> None:
    _, rejected = filter_parcels_by_shape(parcels, shape_config)

    reason = rejected.set_index("parcel_id").loc[
        PARCEL_IDS[parcel_id], "shape_rejection_reason"
    ]
    assert reason == expected_reason


def test_shape_error_precedence_does_not_inspect_metrics(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
    with_error_payload = parcels.copy()
    with_error_payload["width_m"] = with_error_payload["width_m"].astype(object)
    with_error_payload["length_width_ratio"] = with_error_payload[
        "length_width_ratio"
    ].astype(object)
    error_row = with_error_payload["parcel_id"] == PARCEL_IDS["shape-error"]
    with_error_payload.loc[error_row, "width_m"] = "unavailable"
    with_error_payload.loc[error_row, "length_width_ratio"] = "unavailable"

    _, rejected = filter_parcels_by_shape(with_error_payload, shape_config)

    reason = rejected.set_index("parcel_id").loc[
        PARCEL_IDS["shape-error"], "shape_rejection_reason"
    ]
    assert reason == "SHAPE_ERROR"


def test_enabled_outputs_record_active_policy_metadata(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
    retained, rejected = filter_parcels_by_shape(parcels, shape_config)

    for output in (retained, rejected):
        assert set(output["shape_policy_version"]) == {"test_policy_v1"}
        assert set(output["shape_policy_min_width_m"]) == {15.0}
        assert set(output["shape_policy_max_ratio"]) == {10.0}
    assert "shape_rejection_reason" not in retained.columns


def test_enabled_partition_preserves_exact_ids_and_crs(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
    retained, rejected = filter_parcels_by_shape(parcels, shape_config)

    retained_ids = set(retained["parcel_id"])
    rejected_ids = set(rejected["parcel_id"])
    assert len(parcels) == len(retained) + len(rejected)
    assert retained_ids.isdisjoint(rejected_ids)
    assert retained_ids | rejected_ids == set(parcels["parcel_id"])
    assert not retained["parcel_id"].duplicated().any()
    assert not rejected["parcel_id"].duplicated().any()
    assert retained.crs == parcels.crs
    assert rejected.crs == parcels.crs
    assert "compactness" in retained.columns
    assert "compactness" in rejected.columns


def test_filter_does_not_mutate_input(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
    original = parcels.copy(deep=True)

    filter_parcels_by_shape(parcels, shape_config)

    assert_geodataframe_equal(parcels, original)


@pytest.mark.parametrize(
    "column",
    ["parcel_id", "shape_status", "width_m", "length_width_ratio", "geometry"],
)
def test_missing_required_column_fails(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
    column: str,
) -> None:
    missing_column = parcels.drop(columns=[column])

    with pytest.raises(ParcelFilterError, match="Missing required shape columns"):
        filter_parcels_by_shape(missing_column, shape_config)


def test_null_parcel_id_fails(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
    invalid = parcels.copy()
    invalid.loc[0, "parcel_id"] = None

    with pytest.raises(ParcelFilterError, match="must not be null"):
        filter_parcels_by_shape(invalid, shape_config)


def test_duplicate_parcel_id_fails(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
    invalid = parcels.copy()
    invalid.loc[1, "parcel_id"] = invalid.loc[0, "parcel_id"]

    with pytest.raises(ParcelFilterError, match="must be unique"):
        filter_parcels_by_shape(invalid, shape_config)


def test_unknown_crs_fails(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
    invalid = parcels.set_crs(None, allow_override=True)

    with pytest.raises(ParcelFilterError, match="known CRS"):
        filter_parcels_by_shape(invalid, shape_config)


@pytest.mark.parametrize("status", [None, "UNKNOWN"])
def test_unexpected_or_null_shape_status_fails(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
    status: str | None,
) -> None:
    invalid = parcels.copy()
    invalid.loc[0, "shape_status"] = status

    with pytest.raises(ParcelFilterError, match="Unexpected shape_status"):
        filter_parcels_by_shape(invalid, shape_config)


@pytest.mark.parametrize("column", ["width_m", "length_width_ratio"])
def test_non_finite_known_metric_on_valid_row_fails(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
    column: str,
) -> None:
    invalid = parcels.copy()
    invalid.loc[0, column] = float("inf")

    with pytest.raises(ParcelFilterError, match="numeric and finite"):
        filter_parcels_by_shape(invalid, shape_config)


@pytest.mark.parametrize("width", [-1, 0, float("inf"), "20", True])
def test_valid_shape_requires_strict_positive_width(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
    width: object,
) -> None:
    invalid = parcels.copy()
    invalid["width_m"] = invalid["width_m"].astype(object)
    invalid.loc[0, "width_m"] = width

    with pytest.raises(
        ParcelFilterError,
        match="width_m must be (numeric and finite|greater than zero)",
    ):
        filter_parcels_by_shape(invalid, shape_config)


@pytest.mark.parametrize("ratio", [-1, 0, 0.999, float("inf"), "2", True])
def test_valid_shape_requires_ratio_at_least_one(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
    ratio: object,
) -> None:
    invalid = parcels.copy()
    invalid["length_width_ratio"] = invalid["length_width_ratio"].astype(object)
    invalid.loc[0, "length_width_ratio"] = ratio

    with pytest.raises(
        ParcelFilterError,
        match="length_width_ratio must be (numeric and finite|at least one)",
    ):
        filter_parcels_by_shape(invalid, shape_config)


def test_negative_ratio_cannot_pass_permissive_thresholds(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
) -> None:
    invalid = parcels.copy()
    invalid.loc[0, "width_m"] = 20
    invalid.loc[0, "length_width_ratio"] = -1

    with pytest.raises(
        ParcelFilterError, match="length_width_ratio must be at least one"
    ):
        filter_parcels_by_shape(invalid, shape_config)


def test_disabled_policy_is_an_exact_passthrough(parcels: gpd.GeoDataFrame) -> None:
    disabled = ShapeScreeningConfig(enabled=False)

    retained, rejected = filter_parcels_by_shape(parcels, disabled)

    assert_geodataframe_equal(retained, parcels)
    assert_geodataframe_equal(rejected, parcels.iloc[0:0])
    for column in (
        "shape_rejection_reason",
        "shape_policy_version",
        "shape_policy_min_width_m",
        "shape_policy_max_ratio",
    ):
        assert column not in retained.columns
        assert column not in rejected.columns


def test_different_configs_change_results_for_same_parcels(
    parcels: gpd.GeoDataFrame,
) -> None:
    permissive = _shape_config(
        min_width_m=10,
        max_length_width_ratio=12,
        policy_version="permissive",
    )
    restrictive = _shape_config(
        min_width_m=18,
        max_length_width_ratio=6,
        policy_version="restrictive",
    )

    permissive_retained, _ = filter_parcels_by_shape(parcels, permissive)
    restrictive_retained, _ = filter_parcels_by_shape(parcels, restrictive)

    assert set(permissive_retained["parcel_id"]) == {
        PARCEL_IDS["at-boundaries"],
        PARCEL_IDS["passing"],
        PARCEL_IDS["width-below"],
        PARCEL_IDS["ratio-above"],
        PARCEL_IDS["both-thresholds-fail"],
    }
    assert set(restrictive_retained["parcel_id"]) == {PARCEL_IDS["passing"]}


@pytest.mark.parametrize("column", ["width_m", "length_width_ratio"])
def test_valid_shape_requires_complete_metrics_even_when_screening_disabled(
    parcels: gpd.GeoDataFrame,
    column: str,
) -> None:
    invalid = parcels.copy()
    invalid.loc[0, column] = None

    with pytest.raises(ParcelFilterError, match="complete|must not be null"):
        filter_parcels_by_shape(invalid, ShapeScreeningConfig(enabled=False))


@pytest.mark.parametrize(
    ("width", "ratio"),
    [
        (None, 5.0),
        (20.0, None),
        (None, None),
        (float("nan"), 5.0),
        (20.0, float("nan")),
    ],
)
def test_valid_shape_rejects_every_incomplete_metric_form(
    parcels: gpd.GeoDataFrame,
    shape_config: ShapeScreeningConfig,
    width: float | None,
    ratio: float | None,
) -> None:
    invalid = parcels.copy()
    invalid.loc[0, "width_m"] = width
    invalid.loc[0, "length_width_ratio"] = ratio

    with pytest.raises(ParcelFilterError, match="complete"):
        filter_parcels_by_shape(invalid, shape_config)


def test_shape_filter_rejects_plain_dataframe(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
    with pytest.raises(ParcelFilterError, match="GeoDataFrame"):
        filter_parcels_by_shape(
            pd.DataFrame(parcels),  # type: ignore[arg-type]
            shape_config,
        )


def test_shape_filter_rejects_duplicate_columns(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
    duplicate = gpd.GeoDataFrame(
        pd.concat([parcels, parcels[["parcel_id"]]], axis=1),
        geometry="geometry",
        crs=parcels.crs,
    )

    with pytest.raises(ParcelFilterError, match="columns.*unique"):
        filter_parcels_by_shape(duplicate, shape_config)


def test_shape_filter_rejects_unreadable_crs(
    parcels: gpd.GeoDataFrame, shape_config: ShapeScreeningConfig
) -> None:
    invalid = parcels.copy()
    invalid.geometry.array._crs = "not-a-crs"

    with pytest.raises(ParcelFilterError, match="CRS"):
        filter_parcels_by_shape(invalid, shape_config)
```

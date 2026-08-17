# `src/landscout/stages/profile_shape.py`

## File identity

- Repository path: `src/landscout/stages/profile_shape.py`
- File type: Python source
- Primary responsibility: Profiles shape metrics and scenario evidence without making parcel suitability decisions.
- Layer / domain: `stage` / `cadastre`
- Public or internal role: Module symbols without a package re-export are internal unless imported directly by repository code.
- Source SHA256: `1a5e1de1f7584e49abedf963282e4cc3b7c7ab3a724333bea75cdaa6f90a24c8`

## 1. Purpose

Profiles shape metrics and scenario evidence without making parcel suitability decisions.

## 2. Position in LandScout architecture

This file is a `stage` artifact in the `cadastre` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from dataclasses import dataclass` — required by the implementation paths and symbols documented below.
- `from math import isclose, isfinite` — required by the implementation paths and symbols documented below.
- `from numbers import Real` — required by the implementation paths and symbols documented below.

### Third-party

- `import geopandas as gpd` — required by the implementation paths and symbols documented below.
- `from pyproj import CRS` — required by the implementation paths and symbols documented below.

### Internal LandScout

- None.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `PROFILE_METRICS` | `( "area_m2", "length_m", "width_m", "length_width_ratio", "compactness", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `REPRESENTATIVE_FIELDS` | `( "parcel_id", "area_m2", "length_m", "width_m", "length_width_ratio", "compactness", "centroid_lat", "centroid_lon", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `REQUIRED_COLUMNS` | `frozenset({"parcel_id", "shape_status", *REPRESENTATIVE_FIELDS})` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `PERCENTILES` | `{ "min": 0.0, "p01": 0.01, "p05": 0.05, "p10": 0.10, "p25": 0.25, "p50": 0.50, "p75": 0.75, "p90": 0.90, "p95": 0.95, "p99": 0.99, "max": 1.0, }` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

### `ShapeProfileError`

**Purpose:** Raised when shape candidates cannot be profiled safely.

**Inheritance:** `ValueError`.

**Model form and mutability:** class inheriting from `ValueError`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

### `DiagnosticScenario`

**Purpose:** Groups the `DiagnosticScenario` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `retained_count` | `int` | `required` | Strict count; Boolean coercion is rejected where the model/validator requires an exact integer. |
| `retained_percentage` | `float` | `required` | `float` state used by `src/landscout/stages/profile_shape.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `ShapeDistributionProfile`

**Purpose:** Carries deterministic diagnostic/profile statistics without changing the underlying evidence rows.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `input_count` | `int` | `required` | Strict count; Boolean coercion is rejected where the model/validator requires an exact integer. |
| `valid_count` | `int` | `required` | Strict count; Boolean coercion is rejected where the model/validator requires an exact integer. |
| `error_count` | `int` | `required` | Strict count; Boolean coercion is rejected where the model/validator requires an exact integer. |
| `distributions` | `dict[str, dict[str, float]]` | `required` | `dict[str, dict[str, float]]` state used by `src/landscout/stages/profile_shape.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `width_buckets` | `dict[str, int]` | `required` | `dict[str, int]` state used by `src/landscout/stages/profile_shape.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `ratio_buckets` | `dict[str, int]` | `required` | `dict[str, int]` state used by `src/landscout/stages/profile_shape.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `compactness_buckets` | `dict[str, int]` | `required` | `dict[str, int]` state used by `src/landscout/stages/profile_shape.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `scenarios` | `dict[str, DiagnosticScenario]` | `required` | `dict[str, DiagnosticScenario]` state used by `src/landscout/stages/profile_shape.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `median_parcels` | `list[dict[str, object]]` | `required` | Tabular/spatial evidence carried with the schema, dtype, index, geometry, and preservation contract documented in this module. |
| `extreme_parcels` | `list[dict[str, object]]` | `required` | Tabular/spatial evidence carried with the schema, dtype, index, geometry, and preservation contract documented in this module. |

**Validators and methods:**

- None.

## 6. Functions and methods

### `_records`

**Signature**

```python
def _records(frame: gpd.GeoDataFrame) -> list[dict[str, object]]:
```

**Purpose**

Implements records according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `list[dict[str, object]]`. Observed return expression(s): `frame[list(REPRESENTATIVE_FIELDS)].to_dict(orient='records')`.

**Algorithm**

1. Returns `frame[list(REPRESENTATIVE_FIELDS)].to_dict(orient='records')`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `frame[list(REPRESENTATIVE_FIELDS)].to_dict`, `list`.

**Known repository callers**

- `src/landscout/stages/profile_shape.py` — `profile_shape_distribution`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `cadastre` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

### `profile_shape_distribution`

**Signature**

```python
def profile_shape_distribution(
    parcels: gpd.GeoDataFrame,
) -> ShapeDistributionProfile:
```

**Purpose**

Profiles shape distribution according to the exact implementation and guards in this file.

**Inputs**

- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `ShapeDistributionProfile`. Observed return expression(s): `ShapeDistributionProfile(input_count=input_count, valid_count=valid_count, error_count=error_count, distributions=distributions, width_buckets=width_buckets, ratio_buckets=ratio_buckets, compactness_buckets=compactness_buckets, scenarios=scenarios, median_parcels=_records(median_frame), extreme_parcels=_records(extreme_frame))`.

**Algorithm**

1. Checks `not isinstance(parcels, gpd.GeoDataFrame)`. When true: Raises `ShapeProfileError('Shape candidates must be a GeoDataFrame')`.
2. Checks `parcels.columns.duplicated().any()`. When true: Raises `ShapeProfileError('Shape candidate columns must be unique')`.
3. Computes `missing_columns` from `REQUIRED_COLUMNS - set(parcels.columns)`.
4. Checks `missing_columns`. When true: Computes `formatted` from `', '.join(sorted(missing_columns))`. Raises `ShapeProfileError(f'Missing required shape columns: {formatted}')`.
5. Checks `parcels.crs is None`. When true: Raises `ShapeProfileError('Shape candidate CRS is required')`.
6. Runs guarded operation: Calls `CRS.from_user_input(parcels.crs)` for its validation or side effect. Handles `Exception`.
7. Computes `identifiers` from `parcels['parcel_id']`.
8. Checks `identifiers.isna().any()`. When true: Raises `ShapeProfileError('parcel_id values must not be null')`.
9. Checks `any((not isinstance(identifier, str) or not identifier or identifier != identifier.strip() for identifier in identifiers))`. When true: Raises `ShapeProfileError('parcel_id values must be exact non-empty strings')`.
10. Checks `identifiers.duplicated().any()`. When true: Raises `ShapeProfileError('parcel_id values must be unique')`.
11. Computes `statuses` from `set(parcels['shape_status'].dropna().unique())`.
12. Checks `parcels['shape_status'].isna().any() or not statuses <= {'VALID', 'ERROR'}`. When true: Computes `unexpected` from `sorted((str(status) for status in statuses - {'VALID', 'ERROR'}))`. Computes `formatted` from `', '.join(unexpected) if unexpected else 'null'`. Raises `ShapeProfileError(f'Unexpected shape_status values: {formatted}')`.
13. Computes `valid_shapes` from `parcels['shape_status'] == 'VALID'`.
14. Computes `error_shapes` from `parcels['shape_status'] == 'ERROR'`.
15. Computes `input_count` from `len(parcels)`.
16. Computes `valid_count` from `int(valid_shapes.sum())`.
17. Computes `error_count` from `int(error_shapes.sum())`.
18. Checks `input_count != valid_count + error_count`. When true: Raises `ShapeProfileError('Shape status counts do not match input count')`.
19. Checks `valid_count == 0`. When true: Raises `ShapeProfileError('At least one VALID shape row is required')`.
20. Computes `required_valid_metrics` from `[*PROFILE_METRICS, 'centroid_lat', 'centroid_lon']`.
21. Checks `parcels.loc[valid_shapes, required_valid_metrics].isna().any().any()`. When true: Raises `ShapeProfileError('VALID shape rows must have complete shape metrics')`.
22. Iterates `column` over `required_valid_metrics`. For each value: Computes `values_are_finite` from `all((isinstance(value, Real) and (not isinstance(value, bool)) and isfinite(float(value)) for value in parcels.loc[valid_shapes, column]))`. Checks `not values_are_finite`. When true: Raises `ShapeProfileError(f'VALID shape metric must be numeric and finite: {column}')`.
23. Computes `valid` from `parcels.loc[valid_shapes]`.
24. Computes `domain_contracts` from `(('area_m2', valid['area_m2'] > 0, 'area_m2 must be greater than zero'), ('length_m', valid['length_m'] > 0, 'length_m must be greater than zero'), ('width_m', valid['width_m'] > 0, 'width_m must be greater than zero'), ('length_width_ratio', valid['length_width_ratio'] >= 1, 'length_width_ratio must be at least one')…`.
25. Iterates `(_, condition, message)` over `domain_contracts`. For each value: Checks `not bool(condition.all())`. When true: Raises `ShapeProfileError(message)`.
26. Checks `not bool((valid['length_m'] >= valid['width_m']).all())`. When true: Raises `ShapeProfileError('length_m must be at least width_m')`.
27. Iterates `row` over `valid.itertuples(index=False)`. For each value: Computes `expected_ratio` from `float(row.length_m) / float(row.width_m)`. Checks `not isclose(float(row.length_width_ratio), expected_ratio, rel_tol=1e-09, abs_tol=1e-09)`. When true: Raises `ShapeProfileError('length_width_ratio must equal length_m / width_m within tolerance')`.
28. Computes `working` from `parcels.loc[valid_shapes].copy()`.
29. Computes `distributions` from `{metric: {label: float(working[metric].quantile(quantile)) for label, quantile in PERCENTILES.items()} for metric in PROFILE_METRICS}`.
30. Computes `width` from `working['width_m']`.
31. Computes `width_buckets` from `{'width < 5 m': int((width < 5).sum()), '5–10 m': int(((width >= 5) & (width < 10)).sum()), '10–15 m': int(((width >= 10) & (width < 15)).sum()), '15–20 m': int(((width >= 15) & (width < 20)).sum()), '20–25 m': int(((width >= 20) & (width < 25)).sum()), '25–30 m': int(((width >= 25) & (width < 30)).sum()), '30–40 m': …`.
32. Computes `ratio` from `working['length_width_ratio']`.
33. Computes `ratio_buckets` from `{'ratio <= 2': int((ratio <= 2).sum()), '2–3': int(((ratio > 2) & (ratio <= 3)).sum()), '3–4': int(((ratio > 3) & (ratio <= 4)).sum()), '4–5': int(((ratio > 4) & (ratio <= 5)).sum()), '5–7': int(((ratio > 5) & (ratio <= 7)).sum()), '7–10': int(((ratio > 7) & (ratio <= 10)).sum()), '10–15': int(((ratio > 10) & (ratio <…`.
34. Computes `compactness` from `working['compactness']`.
35. Computes `compactness_buckets` from `{'compactness < 0.05': int((compactness < 0.05).sum()), '0.05–0.10': int(((compactness >= 0.05) & (compactness < 0.1)).sum()), '0.10–0.20': int(((compactness >= 0.1) & (compactness < 0.2)).sum()), '0.20–0.30': int(((compactness >= 0.2) & (compactness < 0.3)).sum()), '0.30–0.40': int(((compactness >= 0.3) & (compactnes…`.
36. Checks `sum(width_buckets.values()) != valid_count`. When true: Raises `ShapeProfileError('Width buckets do not cover every VALID row')`.
37. Checks `sum(ratio_buckets.values()) != valid_count`. When true: Raises `ShapeProfileError('Ratio buckets do not cover every VALID row')`.
38. Checks `sum(compactness_buckets.values()) != valid_count`. When true: Raises `ShapeProfileError('Compactness buckets do not cover every VALID row')`.
39. Computes `scenario_masks` from `{'A': width >= 10, 'B': width >= 15, 'C': width >= 20, 'D': (width >= 15) & (ratio <= 10), 'E': (width >= 20) & (ratio <= 7), 'F': (width >= 20) & (ratio <= 5) & (compactness >= 0.2)}`.
40. Computes `scenarios` from `{name: DiagnosticScenario(retained_count=int(mask.sum()), retained_percentage=float(mask.sum() / valid_count * 100)) for name, mask in scenario_masks.items()}`.
41. Computes `working['_median_score']` from `0.0`.
42. Iterates `metric` over `PROFILE_METRICS`. For each value: Computes `median` from `working[metric].median()`. Computes `scale` from `working[metric].quantile(0.75) - working[metric].quantile(0.25)`. Checks `scale == 0`. When true: Computes `scale` from `1.0`. Executes 1 additional source-ordered statement(s).
43. Computes `median_frame` from `working.nsmallest(5, '_median_score')`.
44. Computes `working['_extreme_score']` from `working['length_width_ratio'].rank(pct=True) + (-working['width_m']).rank(pct=True) + (-working['compactness']).rank(pct=True)`.
45. Computes `extreme_pool` from `working.loc[~working['parcel_id'].isin(median_frame['parcel_id'])]`.
46. Computes `extreme_frame` from `extreme_pool.nlargest(5, '_extreme_score')`.
47. Returns `ShapeDistributionProfile(input_count=input_count, valid_count=valid_count, error_count=error_count, distributions=distributions, width_buckets=width_buckets, ratio_buckets=ratio_buckets, compactness_buckets=compactness_buckets, scenarios=scenarios, median_parcels=_records(median_frame), extreme_parcels=_records(extreme_frame))`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(parcels, gpd.GeoDataFrame)` is true.
- Rejects or diverts the path when `parcels.columns.duplicated().any()` is true.
- Rejects or diverts the path when `missing_columns` is true.
- Rejects or diverts the path when `parcels.crs is None` is true.
- Rejects or diverts the path when `identifiers.isna().any()` is true.
- Rejects or diverts the path when `any((not isinstance(identifier, str) or not identifier or identifier != identifier.strip() for identifier in identifiers))` is true.
- Rejects or diverts the path when `identifiers.duplicated().any()` is true.
- Rejects or diverts the path when `parcels['shape_status'].isna().any() or not statuses <= {'VALID', 'ERROR'}` is true.
- Rejects or diverts the path when `input_count != valid_count + error_count` is true.
- Rejects or diverts the path when `valid_count == 0` is true.
- Rejects or diverts the path when `parcels.loc[valid_shapes, required_valid_metrics].isna().any().any()` is true.
- Rejects or diverts the path when `not bool((valid['length_m'] >= valid['width_m']).all())` is true.
- Rejects or diverts the path when `sum(width_buckets.values()) != valid_count` is true.
- Rejects or diverts the path when `sum(ratio_buckets.values()) != valid_count` is true.
- Rejects or diverts the path when `sum(compactness_buckets.values()) != valid_count` is true.
- Rejects or diverts the path when `not values_are_finite` is true.
- Rejects or diverts the path when `not bool(condition.all())` is true.
- Rejects or diverts the path when `not isclose(float(row.length_width_ratio), expected_ratio, rel_tol=1e-09, abs_tol=1e-09)` is true.

**Exceptions**

- Explicitly raises: `ShapeProfileError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `parcels.loc[valid_shapes].copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `', '.join`, `((compactness >= 0.05) & (compactness < 0.1)).sum`, `((compactness >= 0.1) & (compactness < 0.2)).sum`, `((compactness >= 0.2) & (compactness < 0.3)).sum`, `((compactness >= 0.3) & (compactness < 0.4)).sum`, `((compactness >= 0.4) & (compactness < 0.5)).sum`, `((compactness >= 0.5) & (compactness < 0.6)).sum`, `((compactness >= 0.6) & (compactness < 0.7)).sum`, `((ratio > 10) & (ratio <= 15)).sum`, `((ratio > 15) & (ratio <= 25)).sum`, `((ratio > 2) & (ratio <= 3)).sum`, `((ratio > 3) & (ratio <= 4)).sum`, `((ratio > 4) & (ratio <= 5)).sum`, `((ratio > 5) & (ratio <= 7)).sum`, `((ratio > 7) & (ratio <= 10)).sum`, `((width >= 10) & (width < 15)).sum`, `((width >= 15) & (width < 20)).sum`, `((width >= 20) & (width < 25)).sum`, `((width >= 25) & (width < 30)).sum`, `((width >= 30) & (width < 40)).sum`, `((width >= 40) & (width < 50)).sum`, `((width >= 5) & (width < 10)).sum`, `(-working['compactness']).rank`, `(-working['width_m']).rank`, `(compactness < 0.05).sum`, `(compactness >= 0.7).sum`, `(ratio <= 2).sum`, `(ratio > 25).sum`, `(valid['length_m'] >= valid['width_m']).all`, `(width < 5).sum`, `(width >= 50).sum`, `(working[metric] - median).abs`, `CRS.from_user_input`, `DiagnosticScenario`, `PERCENTILES.items`, `ShapeDistributionProfile`, `ShapeProfileError`, `_records`, `all`, `any`, `bool`, `compactness_buckets.values`, `condition.all`, `error_shapes.sum`, `extreme_pool.nlargest`, `float`, `identifier.strip`, `identifiers.duplicated`, `identifiers.duplicated().any`, `identifiers.isna`, `identifiers.isna().any`, `int`, `isclose`, `isfinite`, `isinstance`, `len`, `mask.sum`, `parcels.columns.duplicated`, `parcels.columns.duplicated().any`, `parcels.loc[valid_shapes, required_valid_metrics].isna`, `parcels.loc[valid_shapes, required_valid_metrics].isna().any`, `parcels.loc[valid_shapes, required_valid_metrics].isna().any().any`, `parcels.loc[valid_shapes].copy`, `parcels['shape_status'].dropna`, `parcels['shape_status'].dropna().unique`, `parcels['shape_status'].isna`, `parcels['shape_status'].isna().any`, `ratio_buckets.values`, `scenario_masks.items`, `set`, `sorted`, `str`, `sum`, `valid.itertuples`, `valid['centroid_lat'].between`, `valid['centroid_lon'].between`, `valid_shapes.sum`, `width_buckets.values`, `working.nsmallest`, `working['length_width_ratio'].rank`; additional calls omitted from this compact list.

**Known repository callers**

- `tests/unit/test_profile_shape.py` — `test_bucket_counts_sum_to_input_count`
- `tests/unit/test_profile_shape.py` — `test_diagnostic_scenario_counts`
- `tests/unit/test_profile_shape.py` — `test_duplicate_parcel_id_fails`
- `tests/unit/test_profile_shape.py` — `test_error_rows_are_excluded_from_buckets`
- `tests/unit/test_profile_shape.py` — `test_error_rows_are_excluded_from_percentiles`
- `tests/unit/test_profile_shape.py` — `test_existing_all_valid_behavior_is_unchanged`
- `tests/unit/test_profile_shape.py` — `test_input_is_not_mutated`
- `tests/unit/test_profile_shape.py` — `test_missing_crs_fails`
- `tests/unit/test_profile_shape.py` — `test_missing_metric_fails`
- `tests/unit/test_profile_shape.py` — `test_mixed_valid_and_error_rows_are_counted`
- `tests/unit/test_profile_shape.py` — `test_non_finite_metric_on_valid_row_fails`
- `tests/unit/test_profile_shape.py` — `test_null_metric_on_valid_shape_fails`
- `tests/unit/test_profile_shape.py` — `test_null_parcel_id_fails`
- `tests/unit/test_profile_shape.py` — `test_percentile_calculation`
- `tests/unit/test_profile_shape.py` — `test_scenario_percentages_use_valid_count`
- `tests/unit/test_profile_shape.py` — `test_unexpected_shape_status_fails`
- `tests/unit/test_profile_shape.py` — `test_valid_shape_length_must_not_be_less_than_width`
- `tests/unit/test_profile_shape.py` — `test_valid_shape_metrics_reject_bool_and_numeric_strings`
- `tests/unit/test_profile_shape.py` — `test_valid_shape_metrics_require_physical_domains`
- `tests/unit/test_profile_shape.py` — `test_valid_shape_ratio_must_match_length_divided_by_width`
- `tests/unit/test_profile_shape.py` — `test_zero_valid_rows_fails_clearly`

**Tests**

- `tests/unit/test_profile_shape.py::test_bucket_counts_sum_to_input_count`
- `tests/unit/test_profile_shape.py::test_diagnostic_scenario_counts`
- `tests/unit/test_profile_shape.py::test_duplicate_parcel_id_fails`
- `tests/unit/test_profile_shape.py::test_error_rows_are_excluded_from_buckets`
- `tests/unit/test_profile_shape.py::test_error_rows_are_excluded_from_percentiles`
- `tests/unit/test_profile_shape.py::test_existing_all_valid_behavior_is_unchanged`
- `tests/unit/test_profile_shape.py::test_input_is_not_mutated`
- `tests/unit/test_profile_shape.py::test_missing_crs_fails`
- `tests/unit/test_profile_shape.py::test_missing_metric_fails`
- `tests/unit/test_profile_shape.py::test_mixed_valid_and_error_rows_are_counted`
- `tests/unit/test_profile_shape.py::test_non_finite_metric_on_valid_row_fails`
- `tests/unit/test_profile_shape.py::test_null_metric_on_valid_shape_fails`
- `tests/unit/test_profile_shape.py::test_null_parcel_id_fails`
- `tests/unit/test_profile_shape.py::test_percentile_calculation`
- `tests/unit/test_profile_shape.py::test_scenario_percentages_use_valid_count`
- `tests/unit/test_profile_shape.py::test_unexpected_shape_status_fails`
- `tests/unit/test_profile_shape.py::test_valid_shape_length_must_not_be_less_than_width`
- `tests/unit/test_profile_shape.py::test_valid_shape_metrics_reject_bool_and_numeric_strings`
- `tests/unit/test_profile_shape.py::test_valid_shape_metrics_require_physical_domains`
- `tests/unit/test_profile_shape.py::test_valid_shape_ratio_must_match_length_divided_by_width`
- `tests/unit/test_profile_shape.py::test_zero_valid_rows_fails_clearly`

**Business interpretation**

This symbol contributes to the `cadastre` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `_extreme_score` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `_median_score` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `centroid_lat` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `centroid_lon` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `compactness` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `length_m` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | linear distance/length in metres; proxy meaning is limited by the introducing stage. Consumers and exact calculations are the functions that reference this column above. |
| `length_width_ratio` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `parcel_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `shape_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `width_m` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | linear distance/length in metres; proxy meaning is limited by the introducing stage. Consumers and exact calculations are the functions that reference this column above. |

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

This file contributes to LandScout's `cadastre` evidence flow as described by its purpose and public symbols. It preserves the distinction among fact, proxy evidence, policy interpretation, diagnostic status, and parcel precheck.

## 15. Explicit non-goals

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

## 16. Tests

Direct name-resolved tests appear under each symbol. Higher-level tests may exercise private helpers through a public source-complete function; companion documents for all test files describe their fixtures, actions, assertions, and boundaries.

## 17. Change impact

Changing this file requires reviewing its static callers, package exports, directly mapped tests, relevant schema/hash/version constants, source locks, persisted artifact contracts, and the corresponding pipeline/cross-cutting documents. Any byte change makes the SHA256 above stale and requires regenerating this companion.

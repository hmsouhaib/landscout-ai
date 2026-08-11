# LandScout AI development log

## Current project state

- Current phase: French electricity-grid source ingestion
- Latest completed step: STEP 7C.1 — RTE / ODRÉ grid source ingestion
- Current branch: `main`
- Python version: `3.12.13`
- Next step waiting for review: review of the official grid-source findings

## STEP 0 — Environment check

- Status: Complete
- Implementation summary: Audited the Windows development environment and created the initial project scaffold.
- Important files: `README.md`, `.gitignore`, `.env.example`, `.python-version`, `pyproject.toml`
- Tests/checks: OS, CPU, RAM, disk, VS Code, Git, Python, uv, Docker, WSL, GitHub CLI, Codex, and Claude Code availability checked.
- Important decisions: Target Python 3.12; no packages, datasets, services, or application logic added.
- Known issues: Python, Docker, WSL, GitHub CLI, and Claude Code were not installed at this stage.

## STEP 1 — Python and Git setup

- Status: Complete
- Implementation summary: Installed uv-managed Python 3.12.13, created `.venv`, initialized local Git, and retained generated-data directories with `.gitkeep` files.
- Important files: `.python-version`, `.gitignore`, `data/**/.gitkeep`, `outputs/.gitkeep`, `uv.lock`
- Tests/checks: `uv run python --version`; Git status and ignore rules verified.
- Important decisions: Git identity is repository-local; generated data, outputs, `.env`, and `.venv` remain untracked.
- Known issues: None.

## STEP 2 — GIS dependencies

- Status: Complete
- Implementation summary: Added GeoPandas, Shapely, PyProj, Pyogrio, and PyArrow.
- Important files: `pyproject.toml`, `uv.lock`
- Tests/checks: Imported all GIS packages, transformed EPSG:4326 to EPSG:2154, calculated projected area, and completed a temporary GeoParquet write/read round trip.
- Important decisions: Metric work uses projected CRS EPSG:2154; no GIS application logic or datasets added.
- Known issues: None.

## STEP 3 — Quality tools

- Status: Complete
- Implementation summary: Added pytest, pytest-cov, Ruff, and mypy; created the minimal `landscout` package and import/version test.
- Important files: `src/landscout/__init__.py`, `tests/unit/test_package.py`, `pyproject.toml`, `uv.lock`
- Tests/checks: pytest, Ruff, and mypy passed.
- Important decisions: Tests and type checking use the `src` layout; configuration remains minimal.
- Known issues: None.

## STEP 4 — Configuration system

- Status: Complete
- Implementation summary: Added validated Pydantic YAML models and loading for scan configuration plus its referenced BESS profile.
- Important files: `src/landscout/config.py`, `configs/profiles/bess_default_fr.yaml`, `configs/scans/bess_muret.yaml`, `tests/unit/test_config.py`
- Tests/checks: Covered valid loading, invalid commune code, invalid parcel area bounds, negative minimum area, and missing profile; pytest, Ruff, and mypy passed.
- Important decisions: Relative profile paths resolve from the project layout; malformed, invalid, or missing configuration fails explicitly.
- Known issues: PyYAML has no bundled typing metadata, handled with a localized mypy annotation.

## STEP 5 — GIS geometry core

- Status: Complete
- Implementation summary: Added CRS constants, Lambert-93 reprojection, metric area/perimeter, centroid conversion, controlled geometry errors, and orientation-independent parcel shape metrics.
- Important files: `src/landscout/geo/crs.py`, `src/landscout/geo/geometry.py`, `src/landscout/geo/__init__.py`, `tests/unit/test_crs.py`, `tests/unit/test_geometry.py`
- Tests/checks: Current suite has 31 passing tests; Ruff and mypy pass.
- Important decisions: Metric calculations reject geographic or non-metre CRS values; Polygon and MultiPolygon are supported; invalid geometries are never repaired silently; dimensions use the minimum rotated rectangle; compactness uses Polsby-Popper.
- Known issues: Shapely typing metadata is absent, handled with localized mypy annotations.

## STEP 7A — French cadastre downloader

- Status: Complete
- Implementation summary: Added an official Cadastre Etalab commune-level parcel archive downloader with validated local caching and metadata.
- Important files: `src/landscout/sources/cadastre_fr.py`, `src/landscout/sources/__init__.py`, `tests/unit/test_cadastre_fr.py`
- Tests/checks: Mocked URL, download, cache-hit, HTTP-failure, and checksum cases; real Muret (`31395`) download and cache reuse verified; pytest, Ruff, and mypy pass.
- Important decisions: Uses the official `latest` compressed GeoJSON URL; validates cached gzip signature, size, URL, filename, and SHA-256; cached archives and metadata remain ignored by Git.
- Known issues: None.

## STEP 7A.1 — Package installation fix

- Status: Complete
- Implementation summary: Configured the uv build backend so the existing `src/landscout` package is installed by `uv sync`.
- Important files: `pyproject.toml`, `uv.lock`
- Tests/checks: `uv sync`, pytest, Ruff, mypy, and direct `uv run python` import/version verification.
- Important decisions: Retained the existing source layout and explicitly mapped distribution `landscout-ai` to module `landscout`.
- Known issues: None.

## STEP 7A.2 — Cadastre cache freshness

- Status: Complete
- Implementation summary: Added configurable cache expiry to prevent indefinite reuse of stale cadastre archives.
- Important files: `src/landscout/sources/cadastre_fr.py`, `tests/unit/test_cadastre_fr.py`
- Tests/checks: Covered fresh-cache reuse, expired-cache refresh, and failed-refresh preservation; pytest, Ruff, and mypy pass.
- Important decisions: Default maximum age is 168 hours; age uses the stored UTC-aware download timestamp; refresh downloads to a temporary file and preserves the prior archive on failure.
- Known issues: None.

## STEP 7A.3 — Cadastre gzip integrity

- Status: Complete
- Implementation summary: Replaced gzip-header checks with full streaming decompression validation for cached and newly downloaded archives.
- Important files: `src/landscout/sources/cadastre_fr.py`, `tests/unit/test_cadastre_fr.py`
- Tests/checks: Covered valid, truncated, corrupted-cache, and corrupted-refresh archives; pytest, Ruff, and mypy pass.
- Important decisions: Reads decompressed data in 1 MiB chunks to verify gzip structure and CRC without loading the archive into memory; invalid refreshes never replace an existing archive.
- Known issues: None.

## STEP 7B.1 — Load French cadastral parcels

- Status: Complete
- Implementation summary: Added a validated GeoPandas loader that preserves source attributes, geometries, and reported CRS.
- Important files: `src/landscout/sources/cadastre_loader_fr.py`, `tests/unit/test_cadastre_loader_fr.py`
- Tests/checks: Covered plain and gzipped GeoJSON, empty/missing/invalid datasets, missing geometry, and unsupported geometry types; real Muret archive loaded with 17,200 parcels; pytest, Ruff, and mypy pass.
- Important decisions: Accepts Polygon and MultiPolygon without reprojection or derived metrics; uses GDAL `/vsigzip/` on compressed inputs for reliable Windows loading; never invents a CRS.
- Known issues: GeoPandas and Pyogrio lack bundled typing metadata, handled with localized mypy annotations.

### Observed Muret schema (`31395`)

- Parcel count: 17,200
- Detected CRS: `EPSG:4326`
- Geometry types: Polygon 17,200; MultiPolygon 0
- Geometry health: null 0; empty 0; invalid 2

| Column | dtype | Null count | Null percentage |
| --- | --- | ---: | ---: |
| `id` | `str` | 0 | 0% |
| `commune` | `str` | 0 | 0% |
| `prefixe` | `str` | 0 | 0% |
| `section` | `str` | 0 | 0% |
| `numero` | `str` | 0 | 0% |
| `contenance` | `float64` | 1 | 0.005814% |
| `arpente` | `bool` | 0 | 0% |
| `created` | `datetime64[ms]` | 0 | 0% |
| `updated` | `datetime64[ms]` | 0 | 0% |
| `geometry` | `geometry` | 0 | 0% |

Example attribute records (geometry omitted):

| id | commune | prefixe | section | numero | contenance | arpente | created | updated |
| --- | --- | --- | --- | --- | ---: | --- | --- | --- |
| `313950000A0033` | `31395` | `000` | `A` | `33` | 7,533 | false | `2004-12-02 00:00:00` | `2017-01-31 00:00:00` |
| `313950000A0561` | `31395` | `000` | `A` | `561` | 2,081 | false | `2004-12-02 00:00:00` | `2017-01-31 00:00:00` |
| `313950000A0558` | `31395` | `000` | `A` | `558` | 125,371 | false | `2004-12-02 00:00:00` | `2017-01-31 00:00:00` |

## STEP 7B.2 — Normalize Muret parcels

- Status: Complete
- Implementation summary: Added a normalized cadastral schema and vectorized Lambert-93 area calculation while preserving source geometries in WGS84.
- Important files: `src/landscout/stages/normalize_cadastre.py`, `tests/unit/test_normalize_cadastre.py`
- Tests/checks: Covered field mapping, metric area, retained WGS84 geometry, invalid-geometry preservation, missing CRS, and duplicate IDs; pytest, Ruff, and mypy pass.
- Important decisions: Calculates area only for valid, non-empty geometries in a temporary EPSG:2154 copy; invalid geometries remain unchanged with `INVALID` status and null area; generated GeoParquet remains ignored by Git.
- Known issues: Two source geometries are invalid and intentionally remain unmodified.

### Real Muret normalization (`31395`)

- Input parcels: 17,200
- Output parcels: 17,200
- Valid geometries: 17,198
- Invalid geometries: 2
- Duplicate parcel IDs: 0
- Null `area_m2`: 2
- Minimum `area_m2`: 0.064419
- Median `area_m2`: 730.474151
- Maximum `area_m2`: 304,924.087291
- Output CRS: `EPSG:4326`
- Output GeoParquet: `data/processed/cadastre/muret_parcels.parquet`

## STEP 7B.3 — Filter BESS parcels by area

- Status: Complete
- Implementation summary: Added a lossless candidate/rejected partition using parcel-area thresholds from the validated BESS profile.
- Important files: `src/landscout/stages/filter_parcels.py`, `tests/unit/test_filter_parcels.py`
- Tests/checks: Covered inclusive boundaries, every rejection reason, lossless partitioning, retained CRS, and configuration-driven thresholds; pytest, Ruff, and mypy pass.
- Important decisions: Uses no hardcoded area thresholds; invalid geometry takes rejection precedence over unknown area; every input parcel appears in exactly one output; generated GeoParquet files remain ignored by Git.
- Known issues: None.

### Real Muret BESS area filter (`31395`)

- Profile thresholds: 2,000–15,000 m² inclusive
- Total parcels: 17,200
- Candidates: 4,013
- Rejected: 13,187
- Percentage retained: 23.331395%
- `AREA_BELOW_MIN`: 12,453
- `AREA_ABOVE_MAX`: 732
- `INVALID_GEOMETRY`: 2
- `AREA_UNKNOWN`: 0
- Candidate minimum area: 2,001.499661 m²
- Candidate median area: 3,915.028783 m²
- Candidate maximum area: 14,973.105182 m²
- Candidate CRS: `EPSG:4326`
- Candidate GeoParquet: `data/processed/cadastre/muret_bess_candidates.parquet`
- Rejected GeoParquet: `data/processed/cadastre/muret_bess_rejected.parquet`

## STEP 7B.3.1 — Strengthen parcel filter validation

- Status: Complete
- Implementation summary: Added strict parcel identity validation and exact output-partition invariants to the BESS area filter.
- Important files: `src/landscout/stages/filter_parcels.py`, `tests/unit/test_filter_parcels.py`
- Tests/checks: Covered missing, null, and duplicate parcel IDs, disjoint outputs, and exact ID preservation; pytest, Ruff, and mypy pass.
- Important decisions: Requires `parcel_id`, `geometry_status`, and `area_m2`; candidate and rejected IDs must be unique, disjoint, and have a union equal to the input ID set.
- Known issues: None.

## STEP 7B.4 — Enrich BESS parcel shape metrics

- Status: Complete
- Implementation summary: Added shape dimensions, aspect ratio, Polsby-Popper compactness, and projected centroids for area-filtered candidates.
- Important files: `src/landscout/stages/enrich_shape.py`, `tests/unit/test_enrich_shape.py`
- Tests/checks: Covered square, rectangular, rotated, elongated, failed-geometry, identity, CRS, centroid, compactness, and geometry-preservation cases; pytest, Ruff, and mypy pass.
- Important decisions: Reprojects the measurable subset once to EPSG:2154; keeps output geometry unchanged in EPSG:4326; preserves failed rows with `ERROR` and null derived metrics; applies no shape rejection thresholds.
- Known issues: None.

### Real Muret BESS shape enrichment (`31395`)

- Input parcels: 4,013
- Output parcels: 4,013
- Duplicate parcel IDs: 0
- `VALID`: 4,013
- `ERROR`: 0
- Null `length_m`: 0
- Null `width_m`: 0
- Null `length_width_ratio`: 0
- Null `compactness`: 0
- Null `centroid_lat`: 0
- Null `centroid_lon`: 0
- Centroid-null rows: 0
- `length_m` min / median / max: 45.922054 / 131.207909 / 994.057897
- `width_m` min / median / max: 5.578234 / 44.612654 / 317.221485
- `length_width_ratio` min / median / max: 1.000677 / 2.576522 / 70.334491
- `compactness` min / median / max: 0.015827 / 0.532606 / 0.883103
- Output CRS: `EPSG:4326`
- Output GeoParquet: `data/processed/cadastre/muret_bess_shape_candidates.parquet`

Highest `length_width_ratio` parcels (geometry omitted):

| parcel_id | area_m2 | length_m | width_m | length_width_ratio | compactness |
| --- | ---: | ---: | ---: | ---: | ---: |
| `313950000K1259` | 2,001.873974 | 392.342257 | 5.578234 | 70.334491 | 0.039888 |
| `313950000K1263` | 2,124.726244 | 391.903893 | 5.602324 | 69.953812 | 0.042381 |
| `31395000EC0002` | 2,075.541146 | 440.928455 | 6.370519 | 69.213904 | 0.032907 |
| `313950000K1237` | 2,182.107274 | 394.694144 | 5.845761 | 67.518010 | 0.043004 |
| `313950000K1261` | 2,152.836718 | 392.107473 | 6.035972 | 64.961776 | 0.042869 |

## STEP 7B.4.1 — Centralize parcel shape metrics

- Status: Complete
- Implementation summary: Consolidated length, width, aspect ratio, and compactness into the geometry core and made both legacy helpers and enrichment delegate to it.
- Important files: `src/landscout/geo/geometry.py`, `src/landscout/geo/__init__.py`, `src/landscout/stages/enrich_shape.py`, `tests/unit/test_geometry.py`, `tests/unit/test_enrich_shape.py`
- Tests/checks: Covered centralized square, rectangle, rotated, elongated, MultiPolygon, invalid, zero-area, and CRS cases; verified legacy APIs, enrichment equivalence, and exact ID preservation; pytest, Ruff, and mypy pass.
- Important decisions: `parcel_shape_metrics_m` performs one geometry/CRS validation, one minimum rotated rectangle, one area calculation, and one perimeter calculation; the stage retains only orchestration, centroid transformation, and per-row failure isolation.
- Known issues: None.

### Real Muret refactor verification

- Input parcels: 4,013
- Output parcels: 4,013
- Lost parcel IDs: 0
- Extra parcel IDs: 0
- `VALID`: 4,013
- `ERROR`: 0
- Output CRS: `EPSG:4326`
- Maximum absolute difference versus STEP 7B.4 for `length_m`: 0
- Maximum absolute difference versus STEP 7B.4 for `width_m`: 0
- Maximum absolute difference versus STEP 7B.4 for `length_width_ratio`: 0
- Maximum absolute difference versus STEP 7B.4 for `compactness`: 0
- Metric min / median / max values: unchanged from STEP 7B.4

## STEP 7B.5 — Profile BESS parcel shape distribution

- Status: Complete
- Implementation summary: Added a non-mutating shape profiler with percentiles, disjoint buckets, diagnostic scenarios, and representative parcel samples.
- Important files: `src/landscout/stages/profile_shape.py`, `tests/unit/test_profile_shape.py`
- Tests/checks: Covered percentiles, bucket completeness, scenario counts, immutability, required metrics, CRS, and parcel identity; pytest, Ruff, and mypy pass.
- Important decisions: Diagnostic scenarios are analysis only; no threshold was selected, persisted, or applied; median samples minimize normalized deviation across five metrics, while extreme samples emphasize high ratio, low width, and low compactness.
- Known issues: None.

### Real Muret shape distribution (4,013 candidates)

| Metric | min | p01 | p05 | p10 | p25 | p50 | p75 | p90 | p95 | p99 | max |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `area_m2` | 2,001.499661 | 2,014.733986 | 2,111.726147 | 2,257.174309 | 2,716.518957 | 3,915.028783 | 6,633.124319 | 10,238.716584 | 12,348.081108 | 14,320.736428 | 14,973.105182 |
| `length_m` | 45.922054 | 53.154294 | 63.383902 | 71.559474 | 95.609423 | 131.207909 | 180.176206 | 242.927683 | 283.324796 | 399.451809 | 994.057897 |
| `width_m` | 5.578234 | 9.487703 | 16.112164 | 19.976713 | 30.257069 | 44.612654 | 64.828342 | 88.799674 | 102.363064 | 129.745629 | 317.221485 |
| `length_width_ratio` | 1.000677 | 1.020187 | 1.107411 | 1.219572 | 1.608094 | 2.576522 | 5.040910 | 9.572230 | 14.355207 | 29.747604 | 70.334491 |
| `compactness` | 0.015827 | 0.054627 | 0.136849 | 0.202288 | 0.342403 | 0.532606 | 0.684481 | 0.756590 | 0.775246 | 0.801175 | 0.883103 |

Width buckets:

| Bucket | Count |
| --- | ---: |
| width < 5 m | 0 |
| 5–10 m | 44 |
| 10–15 m | 115 |
| 15–20 m | 245 |
| 20–25 m | 288 |
| 25–30 m | 287 |
| 30–40 m | 704 |
| 40–50 m | 648 |
| width >= 50 m | 1,682 |

Length/width ratio buckets:

| Bucket | Count |
| --- | ---: |
| ratio <= 2 | 1,487 |
| 2–3 | 786 |
| 3–4 | 438 |
| 4–5 | 283 |
| 5–7 | 357 |
| 7–10 | 287 |
| 10–15 | 189 |
| 15–25 | 120 |
| ratio > 25 | 66 |

Compactness buckets:

| Bucket | Count |
| --- | ---: |
| compactness < 0.05 | 35 |
| 0.05–0.10 | 75 |
| 0.10–0.20 | 282 |
| 0.20–0.30 | 409 |
| 0.30–0.40 | 485 |
| 0.40–0.50 | 544 |
| 0.50–0.60 | 612 |
| 0.60–0.70 | 685 |
| compactness >= 0.70 | 886 |

Diagnostic scenarios (not applied):

| Scenario | Diagnostic condition | Retained | Retained percentage |
| --- | --- | ---: | ---: |
| A | width >= 10 m | 3,969 | 98.903563% |
| B | width >= 15 m | 3,854 | 96.037877% |
| C | width >= 20 m | 3,609 | 89.932719% |
| D | width >= 15 m and ratio <= 10 | 3,638 | 90.655370% |
| E | width >= 20 m and ratio <= 7 | 3,329 | 82.955395% |
| F | width >= 20 m, ratio <= 5, and compactness >= 0.20 | 2,903 | 72.339895% |

Representative median-shape parcels (geometry omitted):

| parcel_id | area_m2 | length_m | width_m | ratio | compactness | centroid_lat | centroid_lon |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `31395000AE0107` | 3,769.752364 | 130.791396 | 49.659919 | 2.633742 | 0.532806 | 43.477477 | 1.318787 |
| `31395000CM0034` | 3,797.865646 | 119.382511 | 44.007068 | 2.712803 | 0.533889 | 43.421749 | 1.319704 |
| `313950000I0217` | 4,089.041536 | 117.704209 | 43.949066 | 2.678196 | 0.531772 | 43.400689 | 1.309433 |
| `31395000CD0009` | 3,698.472835 | 126.082728 | 48.373716 | 2.606430 | 0.543704 | 43.422481 | 1.322639 |
| `31395000BS0042` | 4,335.275483 | 124.523783 | 46.877474 | 2.656367 | 0.532606 | 43.441195 | 1.344145 |

Representative extreme/problematic parcels (geometry omitted):

| parcel_id | area_m2 | length_m | width_m | ratio | compactness | centroid_lat | centroid_lon |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `313950000K1259` | 2,001.873974 | 392.342257 | 5.578234 | 70.334491 | 0.039888 | 43.419217 | 1.303238 |
| `31395000EC0002` | 2,075.541146 | 440.928455 | 6.370519 | 69.213904 | 0.032907 | 43.464875 | 1.288404 |
| `313950000K1263` | 2,124.726244 | 391.903893 | 5.602324 | 69.953812 | 0.042381 | 43.419288 | 1.303371 |
| `313950000K1237` | 2,182.107274 | 394.694144 | 5.845761 | 67.518010 | 0.043004 | 43.418377 | 1.302782 |
| `313950000K1261` | 2,152.836718 | 392.107473 | 6.035972 | 64.961776 | 0.042869 | 43.419241 | 1.303348 |

## STEP 7B.5.1 — Explicit VALID and ERROR profiling

- Status: Complete
- Implementation summary: Made shape-status accounting explicit and restricted every statistic, bucket, scenario, and representative sample to VALID rows.
- Important files: `src/landscout/stages/profile_shape.py`, `tests/unit/test_profile_shape.py`
- Tests/checks: Covered mixed VALID/ERROR inputs, exclusion from statistics and buckets, valid-count scenario percentages, count integrity, status validation, finite metrics, zero-VALID behavior, all-VALID regression, and input immutability; pytest, Ruff, and mypy pass.
- Important decisions: Only `VALID` and `ERROR` statuses are accepted; ERROR rows contribute only to `error_count`; bucket sums must equal `valid_count`; scenario percentages use `valid_count`; inputs with zero VALID rows raise a clear `ShapeProfileError`.
- Known issues: None.

### Real Muret regression

- `input_count`: 4,013
- `valid_count`: 4,013
- `error_count`: 0
- Count integrity (`input_count == valid_count + error_count`): confirmed
- Percentile values: unchanged from STEP 7B.5
- Width bucket counts: unchanged from STEP 7B.5
- Ratio bucket counts: unchanged from STEP 7B.5
- Compactness bucket counts: unchanged from STEP 7B.5
- Diagnostic scenario counts: unchanged from STEP 7B.5

## STEP 7B.6 — Configurable calibrated BESS shape screening

- Status: Complete
- Implementation summary: Added a validated, configuration-driven shape policy and a lossless retained/rejected partition for shape-enriched parcels.
- Important files: `src/landscout/config.py`, `configs/profiles/bess_default_fr.yaml`, `src/landscout/stages/filter_parcels.py`, `src/landscout/stages/__init__.py`, `tests/unit/test_config.py`, `tests/unit/test_filter_shape.py`
- Tests/checks: Covered configuration bounds and completeness, disabled behavior, inclusive thresholds, rejection precedence, policy provenance, CRS and parcel-ID integrity, configuration-driven output changes, and input immutability; 160 tests, Ruff, and mypy pass.
- Important decisions: YAML owns all active policy values and calibration evidence; Python contains only the generic screening mechanism. Compactness is preserved but is not a rejection rule. A disabled policy is an exact pass-through without fabricated rejection or active-policy columns.
- Known issues: None.

### Active calibration

- Policy version: `muret_empirical_v1`
- Method: `empirical_distribution`
- Calibration scope: `Muret 31395`
- Sample size: 4,013
- Calibration date: `2026-08-11`
- Target retention: 90%
- Observed calibration retention: 90.655370%
- Minimum width: 15 m
- Maximum length/width ratio: 10

These thresholds are **pilot calibration parameters derived from the Muret empirical distribution**. They are not universal BESS engineering constraints and can be changed through profile configuration without modifying Python code.

### Real Muret shape screening (`31395`)

- Input parcels: 4,013
- Retained parcels: 3,638
- Rejected parcels: 375
- Retained percentage: 90.655370%
- `SHAPE_ERROR`: 0
- `WIDTH_UNKNOWN`: 0
- `RATIO_UNKNOWN`: 0
- `WIDTH_BELOW_MIN`: 159
- `RATIO_ABOVE_MAX`: 216
- Minimum retained width: 15.111883 m
- Maximum retained length/width ratio: 9.997098
- Duplicate input parcel IDs: 0
- Duplicate retained parcel IDs: 0
- Duplicate rejected parcel IDs: 0
- Overlapping retained/rejected parcel IDs: 0
- Lost parcel IDs: 0
- Extra parcel IDs: 0
- Output CRS: `EPSG:4326`
- Retained GeoParquet: `data/processed/cadastre/muret_bess_shape_filtered_candidates.parquet`
- Rejected GeoParquet: `data/processed/cadastre/muret_bess_shape_rejected.parquet`

## STEP 7C.1 — RTE / ODRÉ grid source ingestion

- Status: Complete
- Implementation summary: Added a validated ODRE source configuration and one generic adapter for official RTE site, overhead-line, and underground-line metadata and GeoJSON exports.
- Important files: `configs/sources/rte_odre_fr.yaml`, `src/landscout/sources/rte_odre_fr.py`, `src/landscout/sources/__init__.py`, `tests/unit/test_rte_odre_fr.py`
- Tests/checks: Covered strict configuration, all configured URLs, metadata extraction, successful downloads, fresh and expired caches, HTTP and content failures, preservation of a valid prior cache, JSON/GeoJSON integrity, lineage, null geometries, and temporary-file cleanup; 183 tests, Ruff, and mypy pass.
- Important decisions: Dataset identifiers and export formats live only in source YAML; a single downloader handles all three logical datasets; downloads and metadata sidecars are atomic `.part` replacements; cached files require matching lineage, age, size, SHA256, and complete GeoJSON validation.
- Known issues: The current official exports expose attributes but no non-null geometry. Grid distance analysis is therefore not possible from these versions and was not attempted.

RTE currently states that GPS access to transport-grid infrastructure has evolved for public-security reasons.

LandScout therefore does not claim that published RTE geometries represent exact infrastructure coordinates.

These datasets describe network infrastructure only. They do not establish available capacity, connection availability, BESS feasibility, or a guaranteed connection.

### Source and cache configuration

- Provider: `RTE`
- Portal: `ODRE`
- API base URL: `https://odre.opendatasoft.com/api/explore/v2.1`
- Export format: `geojson`
- Cache maximum age: 168 hours
- Cache directory: `data/cache/rte_odre/`
- Second-run cache verification: `sites`, `overhead_lines`, and `underground_lines` all returned `cache_hit = true`
- Generated cache content: ignored by Git

### `sites` — official electrical sites

- Logical name: `sites`
- Dataset ID: `postes-electriques-rte`
- Title: `Sites électriques RTE et points de piquage (au 16 juin 2026)`
- Publisher: `RTE`
- License: `Licence Ouverte v2.0 (Etalab)`
- Source modified: `2026-06-16T14:08:01+00:00`
- Source data processed: `2026-06-16T14:08:30+00:00`
- Source metadata processed: `2026-06-16T14:08:30.142000+00:00`
- Source URL: `https://odre.opendatasoft.com/api/explore/v2.1/catalog/datasets/postes-electriques-rte/exports/geojson`
- Export format: `geojson`
- Cached file: `data/cache/rte_odre/postes-electriques-rte.geojson`
- File size: 1,029,193 bytes
- SHA256: `a6cc86256c1e295c6810146077c6f8034e82e6d76f076347fb7b365a60f2a88a`
- Download timestamp: `2026-08-11T14:31:56.265051+00:00`
- Metadata record count: 5,042
- Export feature count: 5,042

Property schema and null counts:

| Property | Detected JSON types | Null count |
| --- | --- | ---: |
| `code_poste` | string | 0 |
| `nom_poste` | string | 0 |
| `fonction` | string | 0 |
| `etat` | string | 0 |
| `tension` | string | 0 |
| `departement` | string, null | 141 |

Geometry inspection:

- Geometry field present: yes, in all 5,042 features
- Null geometries: 5,042
- Non-null geometries: 0
- Geometry types: none exposed
- Top-level GeoJSON `crs` member: absent
- CRS interpretation: GeoJSON normally carries a WGS84 coordinate assumption, but this export contains no coordinates; no operational spatial CRS or exact location is claimed.
- `geometry_precision_status`: `MISSING`

The source currently exposes all inspected site fields: `code_poste`, `nom_poste`, `fonction`, `etat`, `tension`, and `departement`.

### `overhead_lines` — official overhead lines

- Logical name: `overhead_lines`
- Dataset ID: `lignes-aeriennes-rte-nv`
- Title: `Lignes aériennes RTE – nouveau découpage (au 16 juin 2026)`
- Publisher: `RTE`
- License: `Licence Ouverte v2.0 (Etalab)`
- Source modified: `2025-07-03T09:46:05+00:00`
- Source data processed: `2026-06-16T14:04:57+00:00`
- Source metadata processed: `2026-06-16T14:04:57.442000+00:00`
- Source URL: `https://odre.opendatasoft.com/api/explore/v2.1/catalog/datasets/lignes-aeriennes-rte-nv/exports/geojson`
- Export format: `geojson`
- Cached file: `data/cache/rte_odre/lignes-aeriennes-rte-nv.geojson`
- File size: 3,996,948 bytes
- SHA256: `22d9d8d8be663414601be1a22a250360baf83a543abccb7cd470dc7c3b43720e`
- Download timestamp: `2026-08-11T14:31:58.119185+00:00`
- Metadata record count: 9,221
- Export feature count: 9,221

Property schema and null counts:

| Property | Detected JSON types | Null count |
| --- | --- | ---: |
| `type_ouvrage` | string | 0 |
| `code_ligne` | string | 0 |
| `nom_ligne` | string, null | 19 |
| `etat` | string | 0 |
| `tension` | string | 0 |
| `nombre_circuit` | string | 0 |
| `source` | string | 0 |
| `identification_2` | string, null | 6,682 |
| `nom_ouvrage_2` | string, null | 6,684 |
| `identification_3` | string, null | 9,197 |
| `nom_ouvrage_3` | string, null | 9,197 |
| `identification_4` | string, null | 9,211 |
| `nom_ouvrage_4` | string, null | 9,211 |
| `identification_5` | null only | 9,221 |
| `nom_ouvrage_5` | null only | 9,221 |

Geometry inspection:

- Geometry field present: yes, in all 9,221 features
- Null geometries: 9,221
- Non-null geometries: 0
- Geometry types: none exposed
- Top-level GeoJSON `crs` member: absent
- CRS interpretation: GeoJSON normally carries a WGS84 coordinate assumption, but this export contains no coordinates; no operational spatial CRS or exact line location is claimed.
- `geometry_precision_status`: `MISSING`

The source currently exposes the inspected line fields `type_ouvrage`, `code_ligne`, `nom_ligne`, `etat`, `tension`, and `nombre_circuit`, plus optional additional line identifiers/names.

### `underground_lines` — official underground lines

- Logical name: `underground_lines`
- Dataset ID: `lignes-souterraines-rte-nv`
- Title: `Lignes souterraines RTE – nouveau découpage (au 16 juin 2026)`
- Publisher: `RTE`
- License: `Licence Ouverte v2.0 (Etalab)`
- Source modified: `2026-06-16T13:01:35+00:00`
- Source data processed: `2026-06-16T13:02:59+00:00`
- Source metadata processed: `2026-06-16T13:02:59.780000+00:00`
- Source URL: `https://odre.opendatasoft.com/api/explore/v2.1/catalog/datasets/lignes-souterraines-rte-nv/exports/geojson`
- Export format: `geojson`
- Cached file: `data/cache/rte_odre/lignes-souterraines-rte-nv.geojson`
- File size: 1,573,710 bytes
- SHA256: `ebbf9e5a2d71ec6b0fa513cd3f578c289c58bc06c781f180ec370ffafd35ed5e`
- Download timestamp: `2026-08-11T14:31:59.913470+00:00`
- Metadata record count: 3,825
- Export feature count: 3,825

Property schema and null counts:

| Property | Detected JSON types | Null count |
| --- | --- | ---: |
| `type_ouvrage` | string | 0 |
| `code_ligne` | string | 0 |
| `nom_ouvrage_1` | string, null | 185 |
| `etat` | string | 0 |
| `tension` | string | 0 |
| `nombre_circuit` | string | 0 |
| `identification_2` | null only | 3,825 |
| `nom_ouvrage_2` | null only | 3,825 |
| `identification_3` | null only | 3,825 |
| `nom_ouvrage_3` | null only | 3,825 |
| `identification_4` | null only | 3,825 |
| `nom_ouvrage_4` | null only | 3,825 |
| `identification_5` | null only | 3,825 |
| `nom_ouvrage_5` | null only | 3,825 |

Geometry inspection:

- Geometry field present: yes, in all 3,825 features
- Null geometries: 3,825
- Non-null geometries: 0
- Geometry types: none exposed
- Top-level GeoJSON `crs` member: absent
- CRS interpretation: GeoJSON normally carries a WGS84 coordinate assumption, but this export contains no coordinates; no operational spatial CRS or exact line location is claimed.
- `geometry_precision_status`: `MISSING`

The source currently exposes `type_ouvrage`, `code_ligne`, `etat`, `tension`, and `nombre_circuit`. Its primary name field is `nom_ouvrage_1`, not `nom_ligne`; no normalization was applied.

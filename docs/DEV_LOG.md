# LandScout AI development log

## Current project state

- Current phase: French urban-planning evidence structuring
- Latest completed step: STEP 7D.4B.1 — hardened regulation evidence fidelity
- Current branch: `main`
- Python version: `3.12.13`
- Next step waiting for review: evidence-based planning-rule interpretation design

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

## STEP 7C.1.1 — Strengthen RTE / ODRÉ source integrity

- Status: Complete
- Implementation summary: Added metadata/export count consistency, immutable persisted export summaries, cache-summary revalidation, and failure-safe archive/sidecar publication with rollback.
- Important files: `src/landscout/sources/rte_odre_fr.py`, `src/landscout/sources/__init__.py`, `tests/unit/test_rte_odre_fr.py`
- Tests/checks: Covered equal, larger, smaller, unavailable, and negative record counts; summary validation and lineage; cache-summary/count invalidation; null geometries; backup cleanup; and an injected archive-success/metadata-failure rollback; 195 tests, Ruff, and mypy pass.
- Important decisions: A known metadata record count must equal the parsed GeoJSON feature count. Cache lineage never overrides fresh GeoJSON validation. Existing archive and sidecar files are copied to local backups before publication and restored together if either final replacement fails.
- Known issues: The official exports still contain no non-null geometries. This integrity step makes no connection-feasibility interpretation.

### Persisted integrity model

Each `RteOdreDownload` and JSON sidecar now includes an immutable export summary with:

- `feature_count`
- `null_geometry_count`
- `non_null_geometry_count`
- `geometry_types`

All counts must be non-negative and the two geometry counts must sum exactly to `feature_count`. When source metadata supplies `records_count`, it must equal `feature_count`; `None` remains accepted without fabrication. A cached summary is deserialized and structurally validated, then compared with a fresh full GeoJSON validation before the cache can be reused.

### Transaction and rollback verification

- Publication sequence: validated `.part` archive and sidecar are published as one rollback-protected pair.
- Before replacement: existing archive and sidecar are copied to same-directory `.bak` files.
- Injected failure: archive replacement succeeded and metadata replacement persistently raised a Windows-style `PermissionError`.
- Result: the prior archive bytes and prior sidecar bytes were both restored exactly.
- Failure cleanup: no `.part` or `.bak` file remained.
- Successful refresh cleanup: no `.part` or `.bak` file remained.

### Real RTE cache regression

| Logical dataset | Metadata records | Export features | Null geometry | Non-null geometry | Geometry types | Precision status |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| `sites` | 5,042 | 5,042 | 5,042 | 0 | none | `MISSING` |
| `overhead_lines` | 9,221 | 9,221 | 9,221 | 0 | none | `MISSING` |
| `underground_lines` | 3,825 | 3,825 | 3,825 | 0 | none | `MISSING` |

- Count consistency: confirmed for all three official exports.
- Export summaries: persisted in all three metadata sidecars.
- Fresh cache revalidation: summary equality and metadata/export count equality confirmed for all three.
- First run after lineage migration: all three refreshed because the prior sidecars did not contain export summaries.
- Second run: all three returned `cache_hit = true`.
- Temporary/backup artifacts after real refresh: 0.
- Current checksums and file sizes: unchanged from STEP 7C.1.
- Refreshed `sites` timestamp: `2026-08-11T14:58:19.738310+00:00`
- Refreshed `overhead_lines` timestamp: `2026-08-11T14:58:20.821434+00:00`
- Refreshed `underground_lines` timestamp: `2026-08-11T14:58:21.404259+00:00`

The counts above are real-source regression observations, not production constants. No parcel-grid distance, coordinate inference, available-capacity inference, or connection claim was added.

## STEP 7C.2 — IGN BD TOPO electricity spatial source ingestion

- Status: Complete
- Implementation summary: Added a strictly validated, configuration-driven IGN BD TOPO source adapter for archive download/cache integrity, safe 7z extraction, unique GeoPackage discovery, electricity-layer discovery, and read-only inspection of line and transformation-post geometries.
- Important files: `configs/sources/ign_bdtopo_fr.yaml`, `src/landscout/sources/ign_bdtopo_fr.py`, `src/landscout/sources/__init__.py`, `tests/unit/test_ign_bdtopo_fr.py`, `pyproject.toml`, `uv.lock`
- Tests/checks: 31 offline IGN tests cover strict source configuration, download/cache behavior, archive and checksum validation, safe refresh and rollback, temporary cleanup, synthetic archive/GeoPackage discovery, missing and ambiguous electricity layers, CRS/geometry validation, row counts, and null/empty/invalid geometry reporting. The full suite passes with 226 tests; Ruff and mypy pass.
- Important decisions: The pinned source is the smallest official department-level GeoPackage package that contains both required electricity layers. Archive extraction uses the Python `py7zr` library rather than an external `7z.exe`. Layer names are discovered from the real GeoPackage without assuming case or accents. A short content-addressed extraction path (`x/<SHA256 prefix>`) avoids Windows legacy path-length failures while retaining IGN's internal paths. IGN electricity geometries have the explicit spatial role `PROXY_GEOMETRY` and are suitable for broad spatial screening only.
- Known issues: IGN publishes an inline MD5 in its package manifest but no checksum URL/file for this package. The archive exposes no per-member CRC through `py7zr`, so integrity is established by the exact official size and MD5 plus successful safe extraction and GeoPackage opening. `pyogrio.list_layers()` emits non-fatal warnings for several unsupported declared SQL field formats in the package metadata tables. Source lineage and confirmation dates are mixed. The transformation-post layer has no voltage attribute. These geometries do not replace exact/current RTE asset data and provide no connection-point or available-capacity evidence.

### Official source package and lineage

- Provider: `IGN`
- Portal: `Géoplateforme / cartes.gouv.fr`
- Product: `BD TOPO`
- Product version: `3.5`
- Package scope: all themes, department `D031` (Haute-Garonne)
- Edition: `2026-06-15`
- Package catalog update observed: `2026-07-09`
- Projection: Lambert-93, `EPSG:2154`
- Distribution format: GeoPackage inside a 7z archive
- Archive filename: `BDTOPO_3-5_TOUSTHEMES_GPKG_LAMB93_D031_2026-06-15.7z`
- Official source URL: `https://data.geopf.fr/telechargement/download/BDTOPO/BDTOPO_3-5_TOUSTHEMES_GPKG_LAMB93_D031_2026-06-15/BDTOPO_3-5_TOUSTHEMES_GPKG_LAMB93_D031_2026-06-15.7z`
- Official package manifest URL: `https://data.geopf.fr/telechargement/resource/BDTOPO/BDTOPO_3-5_TOUSTHEMES_GPKG_LAMB93_D031_2026-06-15?page=1&limit=50`
- Official manifest checksum: MD5 `24d4a50b7eae3c0d55bb55ffd5b525a6`
- Official checksum URL/file: absent; the checksum is supplied inline by the official package manifest
- Downloaded archive size: 494,818,677 bytes
- Local SHA256: `4fcd6d1234495c5e38f3a671159aa7c8da88c70fa1b8747c9f93f0a7a3001ab0`
- Adapter archive cache path: `data/cache/ign_bdtopo/BDTOPO_3-5_TOUSTHEMES_GPKG_LAMB93_D031_2026-06-15.7z`
- Adapter extraction cache path: `data/cache/ign_bdtopo/x/4fcd6d1234495c5e/`
- Adapter download timestamp: `2026-08-11T15:32:03.110837+00:00`
- Second-run cache result: archive `cache_hit = true`; extraction `cache_hit = true`
- Cache root: `data/cache/ign_bdtopo/`; generated archives, extraction content, and sidecars remain ignored by Git

The source URL, edition, package scope, projection, archive format, and expected official checksum are pinned in YAML. The downloaded bytes are also identified independently by SHA256. The package URL and edition are not guessed dynamically at runtime.

### Archive and GeoPackage inspection

- Archive type: 7z
- Archive integrity: official size and MD5 validated; archive safely extracted and its GeoPackage opened successfully (the official 7z exposes no per-member CRC through `py7zr`)
- GeoPackage discovery result: exactly one intended `.gpkg` found
- Internal GeoPackage filename: `BDT_3-5_GPKG_LAMB93_D031-ED2026-06-15.gpkg`
- Internal archive member path: `BDTOPO_3-5_TOUSTHEMES_GPKG_LAMB93_D031_2026-06-15/BDTOPO/1_DONNEES_LIVRAISON_2026-06-00418/BDT_3-5_GPKG_LAMB93_D031_ED2026-06-15/BDT_3-5_GPKG_LAMB93_D031-ED2026-06-15.gpkg`
- Extracted GeoPackage size: 2,955,161,600 bytes
- GeoPackage layer count: 57 discoverable layers (53 feature layers and 4 non-spatial tables)
- Selected line layer: `ligne_electrique`
- Selected transformation-post layer: `poste_de_transformation`
- Selected layer CRS: `EPSG:2154`

Complete GeoPackage layer inventory:

```text
troncon_de_route
route_numerotee_ou_nommee
itineraire_autre
troncon_de_voie_ferree
equipement_de_transport
piste_d_aerodrome
aerodrome
point_de_repere
non_communication
point_du_reseau
transport_par_cable
batiment
cimetiere
construction_lineaire
construction_ponctuelle
construction_surfacique
reservoir
ligne_orographique
pylone
terrain_de_sport
cours_d_eau
troncon_hydrographique
bassin_versant_topographique
plan_d_eau
surface_hydrographique
noeud_hydrographique
detail_hydrographique
zone_d_habitation
lieu_dit_non_habite
detail_orographique
canalisation
ligne_electrique
poste_de_transformation
erp
zone_d_activite_ou_d_interet
voie_nommee
parc_ou_reserve
foret_publique
haie
zone_de_vegetation
arrondissement
commune_associee_ou_deleguee
commune
epci
collectivite_territoriale
departement
region
adresse_ban
batiment_rnb_lien_bdtopo
canton
lien_adresse_vers_bdtopo
section_de_points_de_repere
toponymie
info_metadonnees
metadonnees_lot
metadonnees_theme
layer_styles
```

### `ligne_electrique` — electricity-line proxy geometry

- Row count: 333
- Active geometry column: `geometry`
- CRS: `EPSG:2154` (projected Lambert-93)
- Geometry types: `LineString Z` = 333
- Null geometries: 0
- Empty geometries: 0
- Invalid geometries: 0
- `spatial_role`: `PROXY_GEOMETRY`
- Usable for broad spatial screening: yes

Column schema and null diagnostics:

| Column | dtype | Null count | Null percentage |
| --- | --- | ---: | ---: |
| `cleabs` | `str` | 0 | 0.0000% |
| `voltage` | `str` | 0 | 0.0000% |
| `gestionnaire` | `str` | 52 | 15.6156% |
| `siren_gestionnaire` | `str` | 52 | 15.6156% |
| `etat_de_l_objet` | `str` | 0 | 0.0000% |
| `date_creation` | `datetime64[ms]` | 0 | 0.0000% |
| `date_modification` | `datetime64[ms]` | 9 | 2.7027% |
| `date_d_apparition` | `datetime64[ms]` | 333 | 100.0000% |
| `date_de_confirmation` | `datetime64[ms]` | 43 | 12.9129% |
| `sources` | `str` | 14 | 4.2042% |
| `identifiants_sources` | `str` | 299 | 89.7898% |
| `methode_d_acquisition_planimetrique` | `str` | 0 | 0.0000% |
| `precision_planimetrique` | `float64` | 0 | 0.0000% |
| `methode_d_acquisition_altimetrique` | `str` | 0 | 0.0000% |
| `precision_altimetrique` | `float64` | 0 | 0.0000% |
| `geometry` | `geometry` | 0 | 0.0000% |

Observed categorical values and counts:

- `voltage`: `63 kV` 223; `225 kV` 65; `400 kV` 28; `150 kV` 9; `Inconnue` 5; `<63 kV` 2; `Hors tension` 1
- `etat_de_l_objet`: `En service` 333
- `gestionnaire`: `Réseau de Transport d'Électricité` 281; null 52
- `siren_gestionnaire`: `444619258` 281; null 52
- `sources`: `RTE 2024` 281; `RTE 2022` 33; null 14; `non RTE (EDF)` 3; `RTE` 2
- `methode_d_acquisition_planimetrique`: `Photogrammétrie` 324; `BDTopo` 5; `Orthophotographie` 3; `Fichier numérique non métrique` 1
- `methode_d_acquisition_altimetrique`: `Photogrammétrie` 324; `BDTopo` 5; `Pas de Z` 3; `Z corrigé` 1

Observed date lineage:

- `date_creation`: minimum `2008-11-03T14:43:19.522`, maximum `2026-06-11T16:17:20.863`
- `date_modification`: minimum `2017-02-22T13:52:57.158`, maximum `2026-06-16T19:33:50.619`; 9 null
- `date_d_apparition`: entirely null
- `date_de_confirmation`: minimum `2014-07-01`, maximum `2024-12-18`; 43 null

### `poste_de_transformation` — transformation-post proxy geometry

- Row count: 84
- Active geometry column: `geometry`
- CRS: `EPSG:2154` (projected Lambert-93)
- Geometry types: `MultiPolygon Z` = 84
- Null geometries: 0
- Empty geometries: 0
- Invalid geometries: 0
- `spatial_role`: `PROXY_GEOMETRY`
- Usable for broad spatial screening: yes
- Voltage field: absent; no voltage value is inferred from another layer

Column schema and null diagnostics:

| Column | dtype | Null count | Null percentage |
| --- | --- | ---: | ---: |
| `cleabs` | `str` | 0 | 0.0000% |
| `toponyme` | `str` | 80 | 95.2381% |
| `statut_du_toponyme` | `str` | 80 | 95.2381% |
| `importance` | `str` | 4 | 4.7619% |
| `etat_de_l_objet` | `str` | 0 | 0.0000% |
| `date_creation` | `datetime64[ms]` | 0 | 0.0000% |
| `date_modification` | `datetime64[ms]` | 69 | 82.1429% |
| `date_d_apparition` | `datetime64[ms]` | 84 | 100.0000% |
| `date_de_confirmation` | `datetime64[ms]` | 64 | 76.1905% |
| `sources` | `str` | 83 | 98.8095% |
| `identifiants_sources` | `str` | 63 | 75.0000% |
| `methode_d_acquisition_planimetrique` | `str` | 0 | 0.0000% |
| `precision_planimetrique` | `float64` | 0 | 0.0000% |
| `methode_d_acquisition_altimetrique` | `str` | 0 | 0.0000% |
| `precision_altimetrique` | `float64` | 0 | 0.0000% |
| `geometry` | `geometry` | 0 | 0.0000% |

Observed categorical values and counts:

- `etat_de_l_objet`: `En service` 84
- `importance`: `5` 75; null 4; `4` 4; `6` 1
- `toponyme`: null 80; `Poste d'Issel` 1; `Poste Électrique de Fontenilles` 1; `Poste Électrique de Ginestous` 1; `Poste Électrique de Verfeil` 1
- `statut_du_toponyme`: null 80; `Validé` 3; `Collecté` 1
- `sources`: null 83; `RTE 2021` 1
- `methode_d_acquisition_planimetrique`: `Photogrammétrie` 77; `Orthophotographie` 6; `Fichier numérique non métrique` 1
- `methode_d_acquisition_altimetrique`: `Photogrammétrie` 78; `Pas de Z` 6

Observed date lineage:

- `date_creation`: minimum `2007-05-04T13:58:02.915`, maximum `2026-06-18T10:36:03.587`
- `date_modification`: minimum `2012-06-28T15:33:15.234`, maximum `2026-06-11T16:17:28.201`; 69 null
- `date_d_apparition`: entirely null
- `date_de_confirmation`: minimum `2006-07-01`, maximum `2025-06-17`; 64 null

### Spatial semantics and explicit limitations

Both selected IGN layers expose non-null, non-empty, valid projected geometries and can support future broad parcel-to-network spatial screening. They are recorded as `PROXY_GEOMETRY`, not as survey-grade or guaranteed-current RTE asset coordinates.

The inspection does **not**:

- replace exact or current RTE infrastructure data;
- identify an electrical connection point;
- establish available grid capacity or connection feasibility;
- calculate parcel-to-grid distances;
- match IGN objects to ODRE/RTE records;
- infer a transformation-post voltage from nearby line features;
- repair or alter any source geometry.

The package edition is recent, but individual features carry heterogeneous source labels and confirmation dates. Package recency must therefore not be interpreted as uniform feature-level recency. No scoring, filtering, nearest-feature matching, capacity inference, or business rule was added in this step.

## STEP 7C.3 — Normalize IGN electricity proxy layers

- Status: Complete
- Implementation summary: Added independent, immutable normalization for the already-loaded IGN electric-line and transformation-post layers, including strict source identity and EPSG:2154 validation, namespaced LandScout IDs, geometry-quality classification, stable output schemas, source lineage, and generic voltage parsing.
- Important files: `src/landscout/stages/normalize_grid_ign.py`, `src/landscout/stages/__init__.py`, `tests/unit/test_normalize_grid_ign.py`
- Tests/checks: 40 focused normalization tests cover generic exact and bounded voltage parsing, unknown/de-energized/unparsed vocabulary, ID failures, CRS failures, geometry-quality preservation, lineage, deterministic columns, and input immutability. The full suite passes with 266 tests; Ruff and mypy pass.
- Important decisions: Source `cleabs` is preserved as `source_feature_id`; normalized IDs use the `IGN_BDTOPO:<feature type>:<cleabs>` namespace and never use DataFrame indexes. Source geometry is neither reprojected nor repaired. Transformation-post voltage remains explicitly unknown because the real source layer contains no voltage field.
- Known issues: IGN transformation-post names are sparse and their voltage is absent. Exact numeric line voltage is source-derived only; it does not establish proximity suitability, connection feasibility, available capacity, or a connection point.

### Stable normalization semantics

Shared lineage values for every normalized feature:

- `source_provider = IGN`
- `source_product = BD_TOPO`
- `spatial_role = PROXY_GEOMETRY`
- Source CRS and output CRS: `EPSG:2154`
- Geometry states: `VALID`, `NULL`, `EMPTY`, `INVALID`

Feature types and ID formats:

- Electric line: `ELECTRIC_LINE`; `IGN_BDTOPO:ELECTRIC_LINE:<cleabs>`
- Transformation post: `TRANSFORMATION_POST`; `IGN_BDTOPO:TRANSFORMATION_POST:<cleabs>`

The generic voltage parser accepts positive numeric kV values without a fixed voltage list. `<N kV` is represented as `BELOW` with only `voltage_upper_bound_kv`; it is never converted into an exact voltage. Null or explicitly unknown vocabulary is `UNKNOWN`, `Hors tension` is `DEENERGIZED`, and any other non-null vocabulary is preserved as `UNPARSED`.

### Real D031 electric-line regression

- Input rows: 333
- Output rows: 333
- Duplicate source IDs: 0
- Duplicate normalized IDs: 0
- Lost source IDs: 0
- Extra source IDs: 0
- CRS: `EPSG:2154`
- Geometry status: `VALID` 333; `NULL` 0; `EMPTY` 0; `INVALID` 0
- Known manager: 281
- Unknown manager: 52
- Unexpected/unparsed voltage vocabulary: none

Voltage-status counts:

| Status | Count |
| --- | ---: |
| `EXACT` | 325 |
| `BELOW` | 2 |
| `UNKNOWN` | 5 |
| `DEENERGIZED` | 1 |
| `UNPARSED` | 0 |

Exact source-derived voltage counts:

| `voltage_kv` | Count |
| ---: | ---: |
| 63 | 223 |
| 150 | 9 |
| 225 | 65 |
| 400 | 28 |

- Minimum exact voltage: 63 kV
- Median exact voltage: 63 kV
- Maximum exact voltage: 400 kV
- GeoParquet: `data/processed/grid/ign_bdtopo_d031_electric_lines.parquet`
- GeoParquet size: 138,795 bytes
- Read-back verification: 333 rows, EPSG:2154

### Real D031 transformation-post regression

- Input rows: 84
- Output rows: 84
- Duplicate source IDs: 0
- Duplicate normalized IDs: 0
- Lost source IDs: 0
- Extra source IDs: 0
- CRS: `EPSG:2154`
- Geometry status: `VALID` 84; `NULL` 0; `EMPTY` 0; `INVALID` 0
- Voltage status: `UNKNOWN` 84
- Non-null `voltage_kv`: 0
- Non-null normalized names: 4
- GeoParquet: `data/processed/grid/ign_bdtopo_d031_transformation_posts.parquet`
- GeoParquet size: 38,432 bytes
- Read-back verification: 84 rows, EPSG:2154

Generated GeoParquet outputs remain ignored by Git.

### Explicit spatial interpretation

IGN geometry is `PROXY_GEOMETRY`.

Exact numeric line voltage is source-derived, but proximity to a line does not establish connection feasibility.

IGN transformation posts have no source voltage in the D031 dataset; LandScout therefore keeps their voltage `UNKNOWN`.

`TRANSFORMATION_POST` means only an IGN BD TOPO transformation-post proxy. It does not mean an RTE substation, BESS connection point, source substation, available grid node, or available-capacity location. No parcel distance, parcel rejection, source matching, voltage threshold, grid score, or capacity inference was added.

## STEP 7C.3.1 — Harden IGN grid normalization lineage, geometry semantics, and numeric integrity

- Status: Complete
- Implementation summary: Reworked IGN grid normalization around an immutable source context and the complete `IgnBdTopoElectricityData` bundle. Normalized rows now carry auditable package lineage, discovered layer names, strict feature geometry semantics, finite numeric values, authoritative source IDs, and deterministic indexes.
- Important files: `src/landscout/stages/normalize_grid_ign.py`, `src/landscout/stages/__init__.py`, `tests/unit/test_normalize_grid_ign.py`
- Tests/checks: 78 focused tests cover high-level bundle normalization, lineage, bundle-summary consistency, geometry contracts, voltage parsing, precision validation, identifier hygiene, deterministic indexes and schemas, and input immutability. The full suite passes with 304 tests; Ruff and mypy pass.
- Important decisions: The high-level bundle API is the production normalization entry point. Source layer names come from validated extraction discovery rather than constants. `cleabs` remains authoritative and unmodified. Geometry is classified and preserved without repair or reprojection. Only finite positive voltage values and finite non-negative source precision values are accepted as numeric values.
- Known issues: IGN data remains `PROXY_GEOMETRY`. Package lineage and stronger validation improve auditability but do not establish exact RTE assets, connection feasibility, capacity, proximity suitability, or a connection point.

### Lineage and bundle integrity

Every normalized row now includes:

- `source_department_code`
- `source_edition`
- `source_product_version`
- `source_download_timestamp`
- `source_archive_sha256`
- `source_url`

The normalizer validates the source, archive, extraction, and both layer summaries as one consistent bundle. It rejects mismatched spatial roles, logical or physical layer names, feature counts, CRS values, geometry-quality counts, and geometry-type summaries before producing output. Local cache paths and cache-hit state are intentionally excluded from row-level lineage.

### Geometry, numeric, and identity semantics

- Valid electric-line geometry is limited to `LineString` and `MultiLineString`.
- Valid transformation-post geometry is limited to `Polygon` and `MultiPolygon`.
- Null, empty, and invalid source geometries are preserved and classified; no geometry is silently repaired.
- Z coordinates are preserved.
- Scalar voltage values are parsed only when positive and finite. Collection-like values and numeric overflow are preserved as `UNPARSED`; infinity is never emitted.
- Source `precision_planimetrique` is exposed as `planimetric_precision_m` only when it is a finite, non-negative real value. Missing values remain missing, while negative, infinite, Boolean, and numeric-string values fail with a controlled error. Altimetric precision is not normalized in this step.
- `cleabs` must be a unique, non-null, non-empty string without leading/trailing whitespace, colons, or Unicode control characters. No arbitrary length limit is imposed.
- Output row order is stable and the output uses a deterministic zero-based `RangeIndex`, independent of the source index.

### Real D031 high-level regression

The real cached package was normalized only through `normalize_ign_electricity()` and both GeoParquets were read back successfully.

Shared package lineage:

- Department: `31`
- Edition: `2026-06-15`
- Product version: `3.5`
- Download timestamp: `2026-08-11T15:32:03.110837+00:00`
- Archive SHA256: `4fcd6d1234495c5e38f3a671159aa7c8da88c70fa1b8747c9f93f0a7a3001ab0`
- Source URL: `https://data.geopf.fr/telechargement/download/BDTOPO/BDTOPO_3-5_TOUSTHEMES_GPKG_LAMB93_D031_2026-06-15/BDTOPO_3-5_TOUSTHEMES_GPKG_LAMB93_D031_2026-06-15.7z`
- Spatial role: `PROXY_GEOMETRY`

Electric lines:

- Discovered source layer: `ligne_electrique`
- Input/output/read-back rows: 333 / 333 / 333
- Duplicate normalized IDs: 0
- Lost/extra source IDs: 0 / 0
- Geometry status: `VALID` 333
- CRS and read-back CRS: `EPSG:2154`
- Stable output columns verified: yes
- Voltage status: `EXACT` 325; `BELOW` 2; `UNKNOWN` 5; `DEENERGIZED` 1; `UNPARSED` 0
- Exact voltage counts: 63 kV = 223; 150 kV = 9; 225 kV = 65; 400 kV = 28
- GeoParquet: `data/processed/grid/ign_bdtopo_d031_electric_lines.parquet`
- GeoParquet size: 143,554 bytes

Transformation posts:

- Discovered source layer: `poste_de_transformation`
- Input/output/read-back rows: 84 / 84 / 84
- Duplicate normalized IDs: 0
- Lost/extra source IDs: 0 / 0
- Geometry status: `VALID` 84
- CRS and read-back CRS: `EPSG:2154`
- Stable output columns verified: yes
- Voltage status: `UNKNOWN` 84
- Non-null `voltage_kv`: 0
- GeoParquet: `data/processed/grid/ign_bdtopo_d031_transformation_posts.parquet`
- GeoParquet size: 43,181 bytes

The generated GeoParquets remain ignored by Git. This hardening adds no distance calculation, parcel filtering, RTE/IGN matching, voltage threshold, grid scoring, or capacity inference.

## STEP 7C.3.2 — Close IGN normalization API boundary and validate lineage context

- Status: Complete
- Implementation summary: Made `normalize_ign_electricity()` the sole public production entry point for IGN electricity normalization. Layer-specific normalizers and their immutable context are now internal implementation details.
- Important files: `src/landscout/stages/normalize_grid_ign.py`, `src/landscout/stages/__init__.py`, `tests/unit/test_normalize_grid_ign.py`
- Tests/checks: 105 focused normalization tests cover the closed public API, private context validation, archive identity, and all retained STEP 7C.3.1 behavior. The full suite passes with 331 tests; Ruff and mypy pass.
- Important decisions: Context validation preserves source values rather than trimming or canonicalizing them. The normalizer reuses the IGN adapter's department-code type and validates archive compatibility before stamping canonical `IGN` / `BD_TOPO` lineage.
- Known issues: Loading the real GeoPackage still emits existing Pyogrio warnings for unsupported declared SQL field formats; both required layers load and normalize successfully. IGN geometries remain `PROXY_GEOMETRY` and do not establish connection feasibility.

### API and lineage validation

The `landscout.stages` package continues to expose:

- `IgnGridNormalizationError`
- `IgnVoltageNormalization`
- `NormalizedIgnElectricityData`
- `parse_ign_voltage`
- `normalize_ign_electricity`

It no longer exposes the source-context class or either layer-specific normalizer. The high-level entry point alone constructs validated contexts from the complete `IgnBdTopoElectricityData` bundle and invokes the internal helpers.

Context validation now requires an exact non-empty layer name, a supported French department code, a real ISO calendar edition date, a timezone-aware ISO download timestamp, an exact 64-digit hexadecimal SHA256 value, an HTTP(S) source URL, and a non-empty edge-whitespace-free product version when present. Invalid runtime types produce controlled `IgnGridNormalizationError` failures.

Before canonical lineage is emitted, archive metadata must identify a punctuation/case/accent-normalized IGN provider and BD TOPO product and use a CRS equivalent to EPSG:2154. The discovered extraction layer names remain the authoritative `source_layer` values.

### Real D031 regression and GeoParquet read-back

- Archive and extraction cache hits: yes / yes
- Discovered electric-line layer: `ligne_electrique`
- Electric-line input/output/read-back rows: 333 / 333 / 333
- Electric-line voltage status: `EXACT` 325; `BELOW` 2; `UNKNOWN` 5; `DEENERGIZED` 1; `UNPARSED` 0
- Discovered transformation-post layer: `poste_de_transformation`
- Transformation-post input/output/read-back rows: 84 / 84 / 84
- Transformation-post voltage status: `UNKNOWN` 84
- Lost/extra IDs: 0 / 0 for both layers
- Duplicate normalized IDs: 0 for both layers
- Output and read-back CRS: `EPSG:2154`
- Package lineage, deterministic schemas, geometry statuses, and discovered layer values verified after read-back
- Electric-line GeoParquet: `data/processed/grid/ign_bdtopo_d031_electric_lines.parquet` (143,981 bytes)
- Transformation-post GeoParquet: `data/processed/grid/ign_bdtopo_d031_transformation_posts.parquet` (43,607 bytes)

Generated GeoParquets remain ignored by Git. No distance, threshold, parcel rejection, grid scoring, post-voltage inference, RTE matching, capacity data, Enedis integration, or altimetric-precision normalization was added.

## STEP 7C.4 — Parcel-to-IGN grid proxy proximity

- Status: Complete
- Implementation summary: Added validated parcel-to-proxy enrichment using Shapely spatial indexes, deterministic nearest-feature tie resolution, calculation-only 2D Lambert-93 geometries, dynamic exact-voltage proximity rows, and threshold-free profiling.
- Important files: `src/landscout/stages/enrich_grid_proximity.py`, `src/landscout/stages/__init__.py`, `tests/unit/test_enrich_grid_proximity.py`
- Tests/checks: 44 focused tests cover exact edge and polygon distances, touching geometries, CRS behavior, Z removal, ties, grid quality, voltage semantics, dynamic voltage levels, no-exact behavior, parcel integrity, immutability, profiling, and the public API. The full suite passes with 375 tests; Ruff and mypy pass.
- Important decisions: Full parcel geometry—not parcel centroids—is used. `STRtree.query_nearest` provides indexed vectorized matching. Exactly equidistant matches are counted and resolved by ascending `grid_feature_id`. Loops are limited to dynamically observed exact-voltage levels.
- Known issues: The loaded source covers IGN BD TOPO department 31 only. A nearest result means nearest inside that loaded proxy coverage and may not be the globally nearest electricity asset, especially near coverage boundaries.

### Inputs and integrity

- Shape-screened parcel count: 3,638
- Normalized electric-line count: 333
- Normalized transformation-post count: 84
- Valid exact-voltage electric-line count: 325
- Dynamically observed exact voltage levels: 63, 150, 225, and 400 kV
- Enriched parcel count: 3,638
- Voltage-level proximity rows: 14,552
- Lost parcel IDs: 0
- Extra parcel IDs: 0
- Duplicate output parcel IDs: 0
- Duplicate `(parcel_id, voltage_kv)` pairs: 0
- Parcel input CRS: `EPSG:4326`
- Parcel output/read-back CRS: `EPSG:4326`
- Calculation CRS: `EPSG:2154`
- Original parcel geometry preserved through GeoParquet read-back: yes
- Real proximity computation wall-clock duration: 1.211 seconds

Profile `tie count` means the number of parcel matches for which more than one proxy feature shared the exact nearest distance. The selected match is the lexically smallest `grid_feature_id`.

### Nearest electric-line proxy profile

| Statistic | Value (m unless count) |
| --- | ---: |
| Count | 3,638 |
| Missing count | 0 |
| Minimum | 0.000 |
| p01 | 0.000 |
| p05 | 0.000 |
| p10 | 50.142 |
| p25 | 265.121 |
| p50 | 746.824 |
| p75 | 1,339.712 |
| p90 | 2,866.724 |
| p95 | 4,397.159 |
| p99 | 6,064.828 |
| Maximum | 6,417.713 |
| Zero-distance count | 224 |
| Tie count | 62 |

The nearest-any-line calculation includes every `VALID` line regardless of whether its voltage status is `EXACT`, `BELOW`, `UNKNOWN`, `DEENERGIZED`, or `UNPARSED`; the selected feature's status and raw voltage remain explicit in the enriched dataset.

### Nearest exact-voltage electric-line proxy profile

| Statistic | Value (m unless count) |
| --- | ---: |
| Count | 3,638 |
| Missing count | 0 |
| Minimum | 0.000 |
| p01 | 0.000 |
| p05 | 0.000 |
| p10 | 50.142 |
| p25 | 265.121 |
| p50 | 746.824 |
| p75 | 1,339.712 |
| p90 | 2,866.724 |
| p95 | 4,397.159 |
| p99 | 6,064.828 |
| Maximum | 6,417.713 |
| Zero-distance count | 224 |
| Tie count | 62 |

For this pinned D031 observation, nearest-any-line and nearest-exact-line profiles are identical because none of the eight non-exact-status lines is the nearest line for these parcels. This is an observation, not a production assumption.

### Nearest transformation-post proxy profile

| Statistic | Value (m unless count) |
| --- | ---: |
| Count | 3,638 |
| Missing count | 0 |
| Minimum | 0.000 |
| p01 | 210.743 |
| p05 | 488.496 |
| p10 | 806.727 |
| p25 | 1,527.617 |
| p50 | 2,643.274 |
| p75 | 3,942.982 |
| p90 | 5,493.856 |
| p95 | 5,953.047 |
| p99 | 6,503.975 |
| Maximum | 6,972.433 |
| Zero-distance count | 5 |
| Tie count | 0 |

### Exact-voltage proximity profiles

#### 63 kV

- Source line features: 223
- Parcel proximity rows: 3,638
- Count/missing: 3,638 / 0
- Min/p01/p05/p10: 0.000 / 0.000 / 0.000 / 64.527 m
- p25/p50/p75: 292.591 / 746.824 / 1,339.712 m
- p90/p95/p99/max: 2,866.724 / 4,397.159 / 6,064.828 / 6,417.713 m
- Zero-distance count: 196
- Tie count: 56

#### 150 kV

- Source line features: 9
- Parcel proximity rows: 3,638
- Count/missing: 3,638 / 0
- Min/p01/p05/p10: 68,210.960 / 69,196.820 / 69,925.882 / 70,306.798 m
- p25/p50/p75: 71,324.540 / 73,299.982 / 75,227.244 m
- p90/p95/p99/max: 76,635.219 / 77,056.775 / 77,764.933 / 78,170.390 m
- Zero-distance count: 0
- Tie count: 0

#### 225 kV

- Source line features: 65
- Parcel proximity rows: 3,638
- Count/missing: 3,638 / 0
- Min/p01/p05/p10: 0.000 / 16.488 / 557.396 / 1,005.906 m
- p25/p50/p75: 2,162.172 / 3,990.063 / 5,388.479 m
- p90/p95/p99/max: 6,718.453 / 7,308.618 / 8,278.292 / 9,192.183 m
- Zero-distance count: 34
- Tie count: 0

#### 400 kV

- Source line features: 28
- Parcel proximity rows: 3,638
- Count/missing: 3,638 / 0
- Min/p01/p05/p10: 2,919.575 / 3,708.506 / 4,479.750 / 5,499.350 m
- p25/p50/p75: 7,133.889 / 8,631.311 / 9,892.190 m
- p90/p95/p99/max: 11,093.324 / 11,708.181 / 12,535.949 / 12,960.288 m
- Zero-distance count: 0
- Tie count: 0

### Outputs and semantics

- Enriched GeoParquet: `data/processed/grid/muret_bess_grid_proximity.parquet` (1,228,383 bytes)
- Long-form Parquet: `data/processed/grid/muret_bess_grid_voltage_proximity.parquet` (176,469 bytes)
- Both outputs were read back successfully with row counts, IDs, schemas, lineage, finite non-negative distances, and CRS verified.
- Matched line and post source departments are `31`; matched source edition is `2026-06-15`.

All distances are 2D planar proxy distances calculated in EPSG:2154. IGN Z values are not used in horizontal proximity.

IGN BD TOPO geometry is `PROXY_GEOMETRY`.

Distance to an IGN electric line or transformation post does not establish grid connection feasibility, capacity, connection cost, or an RTE/DSO connection point.

Nearest distance means nearest feature inside the loaded proxy-source coverage. It does not prove that the feature is the globally nearest electricity asset outside that coverage.

No BESS grid-distance threshold was selected in STEP 7C.4. No parcel was rejected and no grid score or suitability category was created.

## STEP 7C.4.1 — Harden grid-proximity integrity contracts

- Status: Complete
- Implementation summary: Hardened parcel identity and geometry validation, nearest-match state validation, tie-count validation, dynamic voltage coverage, the complete parcel-by-voltage invariant, and defensive validation in the public profiler without changing the established STRtree distance algorithm.
- Important files: `src/landscout/stages/enrich_grid_proximity.py`, `tests/unit/test_enrich_grid_proximity.py`
- Tests/checks: 144 focused proximity tests pass. The full suite passes with 475 tests; Ruff and mypy pass.
- Important decisions: Valid parcel identifiers are preserved exactly rather than stripped or rewritten. Only valid `Polygon` and `MultiPolygon` parcel geometries enter proximity calculation. Every matched row has a complete, finite, internally consistent match state; an unavailable exact-voltage class has a wholly null state with stable numeric dtypes. Profiling revalidates the complete mutable result before producing statistics.
- Known issues: Source coverage remains limited to the loaded IGN BD TOPO D031 proxy dataset. The hardening deliberately adds no grid threshold, suitability rule, or connection-feasibility inference.

### Integrity contracts

- `parcel_id` must be a unique, non-null, non-empty string with no leading or trailing whitespace; valid values are preserved exactly.
- Parcel geometry must be non-null, non-empty, valid `Polygon` or `MultiPolygon`. Z-enabled parcel polygons remain accepted, while calculation-only copies continue to be reduced to planar XY.
- Required nearest-line and nearest-post matches now require a finite non-negative distance, non-null grid/source feature IDs, and a numeric finite integer tie count of at least one.
- Exact-line matches obey the same contract and require a finite positive voltage represented by the dynamic source coverage. When no eligible exact-voltage line exists, all exact-match fields remain null; distance and voltage columns remain float-compatible and tie count remains nullable `Int64`.
- Voltage coverage must contain unique positive finite voltage levels in ascending order with positive integer line counts.
- The long table must be exactly the input parcel set multiplied by the dynamic voltage-level set. Every level contains each input parcel exactly once and in input order; pairs are unique and every row retains matched IDs and source lineage.
- `profile_grid_proximity()` now revalidates parcel IDs and geometry, all main match states, coverage, and every long-table row before calculating percentiles. Tests deliberately corrupt IDs, distances, ties, coverage, match fields, and Cartesian rows to prove that misleading partial profiles are rejected with `GridProximityError`.
- Large or non-finite numeric values are rejected through controlled validation rather than leaking conversion exceptions.
- The existing full-parcel `STRtree.query_nearest(..., all_matches=True)` algorithm, force-to-2D calculation copies, Lambert-93 calculation CRS, and lexical `grid_feature_id` tie resolution are unchanged.

### Real Muret/D031 regression and read-back

- Input parcels / lines / posts / valid exact lines: 3,638 / 333 / 84 / 325
- Dynamic exact-voltage levels: 63, 150, 225, and 400 kV
- Enriched parcel rows / voltage proximity rows: 3,638 / 14,552
- Lost IDs / extra IDs / duplicate parcel IDs / duplicate parcel-voltage pairs: 0 / 0 / 0 / 0
- Parcel input, output, and GeoParquet read-back CRS: `EPSG:4326`; calculation CRS: `EPSG:2154`
- Nearest line / exact line / post p50: 746.824 m / 746.824 m / 2,643.274 m
- All STEP 7C.4 distance distributions, zero-distance counts, and tie counts remained numerically unchanged.
- Real proximity computation wall-clock duration: 1.264 seconds
- GeoParquet read-back: 3,638 rows, original parcel order/IDs and geometry preserved, distance dtypes `float64`, tie-count dtypes `int64`, source lineage complete
- Long Parquet read-back: 14,552 rows, exact Cartesian coverage, no duplicate pair, voltage/distance dtypes `float64`, tie-count dtype `int64`, matched IDs and source lineage complete
- Rewritten GeoParquet: `data/processed/grid/muret_bess_grid_proximity.parquet` (1,227,955 bytes)
- Rewritten long-form Parquet: `data/processed/grid/muret_bess_grid_voltage_proximity.parquet` (176,469 bytes)

Generated outputs remain ignored by Git.

IGN geometry is `PROXY_GEOMETRY`.

All distances remain 2D planar proxy distances calculated in EPSG:2154 from full parcel geometry. IGN Z values are not used in horizontal proximity.

Distance to an IGN electric line or transformation post does not establish grid connection feasibility, capacity, connection cost, or an RTE/DSO connection point.

No BESS grid-distance threshold is selected here.

## STEP 7D.5A — Resolve official CNIG meanings for planning-feature codes

- Status: Complete
- Test-first proof: the new focused suite was collected before production implementation and failed on the absent `landscout.stages.resolve_planning_feature_codes` module; after implementation, all 29 focused tests pass.
- Quality gate: `uv run pytest -q` = 1,108 passed; `uv run ruff check .` and `uv run mypy src` pass.
- Standard lock: `CNIG PLU v2017`
- Planning document: `33edb4c9f6943c88d8d92518bff20bec`
- GPU archive SHA256: `9d6677cd6634b56b712311042f0cc714d5ca42a38f82a417b27dd473255d7d93`
- Offline profile: `cnig_plu_2017_muret_observed_pairs_v1`
- Profile schema / result-hash schema: `1` / `1`
- Retrieval date: 2026-08-12
- Canonical records SHA256: `ef00219f39632708de401e9446322dfdce0044ae006de209a983042f5c955cca`
- Complete profile SHA256: `ee2509ee4d28923bf598c265cf4d01ee85a6b78d287acc47034141665751fa28`

The official prescription and information tables were inspected once at the GPU CNIG PLU 2017 endpoints and normalized into `configs/planning/cnig_plu_2017_feature_codes.yaml`. Production resolution is offline and performs one exact lookup on `(feature_family, type_code, subtype_code)`; it never calls an API per feature, falls back to a type-only record, or applies prefix/fuzzy matching. The checked-in source URLs are:

- `https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/PrescriptionUrbaType`
- `https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/InformationUrbaType`

The current line catalog contains the additional factual prescription pair `15/01`, which was not included in the ticket's abbreviated observation list. It is retained and resolved from its own official pair record; it is not inferred from `15/00`.

### Observed pairs and official labels

| Logical layer | Family | Pair | Official CNIG label | Features | Parcel relations |
| --- | --- | --- | --- | ---: | ---: |
| information_surface | INFORMATION | `02/00` | Zone d'aménagement concerté | 1 | 43 |
| information_surface | INFORMATION | `14/00` | Périmètre de voisinage d'infrastructure de transport terrestre (secteur affecté par le bruit) | 3 | 989 |
| information_surface | INFORMATION | `27/00` | Plan d'exposition au bruit des aérodromes | 4 | 178 |
| information_surface | INFORMATION | `99/00` | Autre  périmètre, secteur, plan, document, site, projet, espace. | 141 | 127 |
| prescription_surface | PRESCRIPTION | `01/00` | Espace boisé classé | 127 | 619 |
| prescription_surface | PRESCRIPTION | `05/00` | Emplacement réservé | 185 | 321 |
| prescription_surface | PRESCRIPTION | `07/04` | Éléments de paysage, (sites et secteurs) à préserver pour des motifs d'ordre écologique | 1 | 4 |
| prescription_surface | PRESCRIPTION | `17/00` | Secteur à programme de logements mixité sociale en zone U et AU | 1 | 6 |
| prescription_surface | PRESCRIPTION | `18/00` | Périmètre comportant des orientations d’aménagement et de programmation (OAP) | 6 | 117 |
| prescription_line | PRESCRIPTION | `15/00` | Règles d’implantation des constructions | 4 | 8 |
| prescription_line | PRESCRIPTION | `15/01` | Implantation des constructions par rapport aux voies et aux emprises publiques | 1 | 0 |
| prescription_point | PRESCRIPTION | `07/00` | Patrimoine bâti, paysager ou éléments de paysages à protéger pour des motifs d'ordre culturel, historique, architectural ou écologique | 5 | 2 |

All 479 feature rows and all 2,414 parcel/feature relation rows are `RESOLVED_OFFICIAL`; `UNKNOWN_CODE_PAIR` counts are 0 and 0. Lost/extra feature IDs are 0/0, and lost/extra relation rows are 0/0. Leading-zero type and subtype strings remain unchanged throughout the catalogs and relation table.

### Integrity and outputs

| Component | Rows | Content SHA256 | Output bytes |
| --- | ---: | --- | ---: |
| Code dictionary | 12 | `371ee59bf7baca62eb559f69933b35317e948d375baf3ff5c9fb8cf00fa75225` | 9,658 |
| Surface features | 469 | `2f40e9959c2b70199a798472635cc2fa2d1c98ff96e68f8ee182d725868b2808` | 355,140 |
| Line features | 5 | `a3735f06815d4f3906a459b2af4153333ad15e3f3fc786460038324efb0ab309` | 37,208 |
| Point features | 5 | `b2e056473b53c077728851944335a9dc888d99206cc52f2916b98afde517c4ae` | 33,727 |
| Parcel/feature relations | 2,414 | `0d64738cb284787bc66e415c6bbfb9f8956796841e13e9da9dabcd41ed7a2bcc` | 158,661 |

Complete result SHA256: `894e6225dc9622ee45b3a847de104fb59b94f664c26d3fd87e37d8d290d9b2a6`.

Resolution and source-complete validation took 0.906 seconds with the validated GPU archive and extraction caches. All five outputs were read back, reconstructed into the immutable result, and passed the public source-complete validator. Feature IDs, source IDs, row order, index, geometry, CRS, raw attributes, source lineage, relation types, and every geometry-derived metric remained unchanged.

Generated outputs:

- `data/processed/planning/muret_cnig_plu_2017_feature_codes.parquet`
- `data/processed/planning/muret_gpu_surface_features_coded.parquet`
- `data/processed/planning/muret_gpu_line_features_coded.parquet`
- `data/processed/planning/muret_gpu_point_features_coded.parquet`
- `data/processed/planning/muret_bess_planning_feature_relations_coded.parquet`

These official labels are factual CNIG code meanings only. No BESS impact, compatibility, severity, rejection, or planning score is assigned.

## STEP 7D.5A.1 — Harden CNIG snapshot fidelity and public coding contracts

- Status: Complete
- Test-first proof: the expanded contract suite produced 27 failures against the former schema-v1 implementation, including acceptance of an in-memory profile whose canonical-record hash had been corrupted with `model_copy(update=...)`.
- Focused regression suite: 94 tests pass.
- Quality gate: `uv run pytest -q` = 1,173 passed; `uv run ruff check .` and `uv run mypy src` pass.
- Profile / result schemas: `2` / `2`; schema version 1 is unsupported.
- Profile: `cnig_plu_2017_muret_observed_pairs_v2`
- Official-text normalization: `GPU_DISPLAY_TEXT_NFC_WHITESPACE_V1`
- Retrieval date: 2026-08-12
- Canonical records SHA256: `5990552a681a9e50c072eb207bf88d25c876f61c89eeb88618e74d905487672c`
- Complete profile SHA256: `5611b814eb4bc057578b908c6505094f9df5d2c2bf4ca126629b1362983c47ee`

The two CNIG source-table identities are now exact, family-specific constants. Alternate official-host paths, endpoint swaps, query strings, fragments, credentials, ports, HTTP, host changes, and trailing-path variants are rejected. A supplied in-memory Pydantic profile is serialized and fully revalidated rather than trusted, closing `model_construct` and `model_copy` bypasses for schema, endpoint, record order, duplicate pair, nested record, and canonical-hash integrity.

Official display text must already be Unicode NFC with edge whitespace removed and every internal Unicode-whitespace run represented by one ASCII space. Loading never rewrites malformed profile text. The approved snapshot therefore corrects two display artifacts while preserving the official words, case, accents, and punctuation:

- INFORMATION `99/00`: `Autre périmètre, secteur, plan, document, site, projet, espace.`
- PRESCRIPTION `15/00` legal reference: `L151-17 et L151-18`

The complete ordered 12-record snapshot, all labels/references, both endpoint identities, retrieval date, normalization profile, canonical records hash, and complete profile hash are pinned by an offline regression test.

### Catalog, relation, and public contracts

Every catalog now requires unique columns, an active `geometry` column, a known parseable CRS, exact non-null source identity strings, valid non-null/non-empty geometry, and its geometry-specific layer contract. Surface, line, and point inputs accept their matching single/multi geometry types; logical layer determines PRESCRIPTION versus INFORMATION. Planning feature IDs are globally unique across all three catalogs. Properly typed empty optional catalogs retain their deterministic schema and CRS and remain valid.

Relations require unique columns, exact parcel and feature IDs, unique `(parcel_id, planning_feature_id)` pairs, a feature present in exactly one catalog, exact catalog/source agreement, and geometry-compatible relation vocabulary. No geometry metric is recalculated. The six stable profile, error, result, loader, resolver, and source-complete validator symbols are exported from both the module and `landscout.stages`; private lookup/hash/DataFrame helpers remain unexported.

### Real Muret regression and read-back

- Document ID: `33edb4c9f6943c88d8d92518bff20bec`
- Archive SHA256: `9d6677cd6634b56b712311042f0cc714d5ca42a38f82a417b27dd473255d7d93`
- Configured/observed pairs: 12/12
- Features: 479 input / 479 output / 479 `RESOLVED_OFFICIAL` / 0 `UNKNOWN_CODE_PAIR`
- Relations: 2,414 input / 2,414 output / 2,414 `RESOLVED_OFFICIAL` / 0 `UNKNOWN_CODE_PAIR`
- Lost/extra feature IDs: 0/0
- Lost/extra relation rows: 0/0
- PRESCRIPTION `15/00` and `15/01`: independently resolved and unchanged
- Resolution plus source-complete validation runtime: 0.908 seconds

| Component | Rows | Schema-v2 content SHA256 | Output bytes |
| --- | ---: | --- | ---: |
| Code dictionary | 12 | `ee93bfb6b768ffa223775b2821762afc7384d74db8745009a5983494c281c45f` | 9,642 |
| Surface features | 469 | `72f598aaa606cd8eb3e2ec1de0570f3cdb520c4e4e5d9aaad506231da748e5ac` | 355,137 |
| Line features | 5 | `f19166784d09b073901d82758d8d768fb8ee3b3a006a869ede31696f5a3f8b84` | 37,194 |
| Point features | 5 | `dab480976d1506a18469a00fd1f8af4c54668481b9cdfd77b04b030fa94a4c5c` | 33,727 |
| Parcel/feature relations | 2,414 | `0c7a5b657c2bb6e8b468be29cc1df4125b869531d1e9db341412d1fec54d59fa` | 158,650 |

Complete result SHA256: `a39099534ee1f8f1675ec6cd07fcc44c08994540e8b5087b9c39d850c20db912`.

All five ignored outputs were rewritten and read back. The reconstructed schema-v2 result passed the exported source-complete validator against the validated GPU planning document, all four original factual inputs, and the checked-in profile. IDs, order, index, geometries, CRS, raw attributes, source lineage, relation types, and geometry-derived metrics are unchanged.

No BESS impact or severity is assigned. No parcel is rejected. No planning score or legal interpretation is produced.

## STEP 7D.5A.2 — Close normalized planning-feature input contracts

- Status: Complete
- Test-first proof: the first focused collection failed because the reusable factual validator did not exist. The new stripped-catalog and provenance/metric regressions therefore failed at the former STEP 7D.5A.1 boundary before production integration.
- Focused regression suite: 207 tests pass across STEP 7D.3.1 and STEP 7D.5A coding.
- Quality gate: `uv run pytest -q` = 1,206 passed; `uv run ruff check .` and `uv run mypy src` pass.
- CNIG profile / result schemas remain `2` / `2`; the approved official snapshot and exact pair lookup are unchanged.

### One factual contract

`validate_normalized_planning_feature_inputs(...)` is the single reusable contract used by both the STEP 7D.3.1 result validator and the STEP 7D.5A resolver. The coding stage no longer owns a second partial copy of catalog schemas, geometry rules, identity rules, relation schemas, or relation semantics. Its remaining checks are specific to the loaded planning-document lineage, CNIG two-character code format, and official-code enrichment.

The contract requires the exact deterministic factual columns and order for each catalog and the relation table. Empty and populated catalogs now use the same kind-specific schema. All catalogs require canonical `EPSG:2154`, valid non-null and non-empty geometries, and their stored source metric:

- surface `feature_area_m2` is finite, positive, and agrees with polygon area;
- line `feature_length_m` is finite, positive, and agrees with line length;
- point `point_member_count` is a strict positive integer equal to the Point/MultiPoint member count.

Metric comparisons reuse `technical_overlay_tolerance(...)`; no new threshold was introduced and no stored metric is repaired or replaced.

Identity provenance is exact. `CNIG_ATTRIBUTE` requires `LIB_IDPSC` for prescriptions and `LIB_IDINFO` for information. `ARCHIVE_SCOPED_OGR_FID` remains limited to `prescription_surface`, requires `OGR_FID`, and requires an `OGR_FID:` source-ID prefix. Source feature IDs are unique inside each logical layer and LandScout planning feature IDs remain globally unique.

Relations require the complete STEP 7D.3.1 schema, unique `(parcel_id, planning_feature_id)` pairs, exact null-safe catalog agreement for raw facts and lineage, and exact agreement with the relevant source feature metric. Area, length, percentage, and point-member semantics are independently revalidated; irrelevant geometry-kind metrics must remain null. This stage does not recompute spatial intersections.

### Real Muret regression and read-back

- Features: 469 surface + 5 line + 5 point = 479; all catalogs passed the complete schema, identity, geometry, metric, and canonical CRS contracts.
- Relations: 2,414; duplicate pairs 0; all rows passed complete catalog agreement and geometry-specific semantics.
- Configured/observed official pairs: 12/12; `UNKNOWN_CODE_PAIR` features/relations: 0/0.
- PRESCRIPTION `15/00` and `15/01` remain separate exact pairs.
- Lost/extra feature IDs: 0/0; lost/extra relation rows: 0/0.
- Offline cache inspection, resolution, rewrite, and source-complete read-back runtime: 3.947 seconds.

All schema-v2 integrity hashes are unchanged, proving that valid serialized coding results did not change:

- dictionary: `ee93bfb6b768ffa223775b2821762afc7384d74db8745009a5983494c281c45f`;
- surface / line / point: `72f598aaa606cd8eb3e2ec1de0570f3cdb520c4e4e5d9aaad506231da748e5ac` / `f19166784d09b073901d82758d8d768fb8ee3b3a006a869ede31696f5a3f8b84` / `dab480976d1506a18469a00fd1f8af4c54668481b9cdfd77b04b030fa94a4c5c`;
- coded relations: `0c7a5b657c2bb6e8b468be29cc1df4125b869531d1e9db341412d1fec54d59fa`;
- complete result: `a39099534ee1f8f1675ec6cd07fcc44c08994540e8b5087b9c39d850c20db912`.

The five ignored outputs were rewritten and read back (12 dictionary rows, 469 surface features, 5 line features, 5 point features, and 2,414 relations). A reconstructed immutable result passed the exported source-complete validator against the original factual inputs, checked-in profile, and verified local GPU planning document.

No planning code is interpreted as favorable, restrictive, compatible, or blocking. No BESS severity, parcel rejection, score, live production call, or legal interpretation is introduced.

## STEP 7D.5A.3 — Bind normalized planning facts to GPU and parcel identity

- Status: Complete
- Test-first proof: against the former STEP 7D.5A.2 boundary, 32 feature-stage regressions failed on the old context-free validator/export/source-binding behavior, and all 11 new resolver API/hash regressions failed on the old six-argument coding contract. After implementation, 120 feature-stage and 135 coding-stage focused tests pass.
- Quality gate: `uv run pytest -q` = 1,254 passed; `uv run ruff check .` and `uv run mypy src` pass.
- CNIG profile schema: `2` (unchanged); result-hash and ignored-manifest schemas: `3` / `3`. Results claiming schema 1 or 2 are unsupported.
- Profile and exact official pair lookup: `cnig_plu_2017_muret_observed_pairs_v2`; unchanged.
- Planning document / archive: `33edb4c9f6943c88d8d92518bff20bec` / `9d6677cd6634b56b712311042f0cc714d5ca42a38f82a417b27dd473255d7d93`.

### Source-complete factual boundary

`validate_normalized_planning_feature_inputs(planning_document, parcels, surface_features, line_features, point_features, relations)` is now the only public factual-input contract. STEP 7D.3.1 and CNIG coding both use the same private normalization implementation; no weaker public overload remains. The validator rebuilds the three catalogs from the inspected GPU related layers and exact-compares schema, dtypes, row count/order, index, every raw attribute, deterministic identifiers, provenance, geometry WKB, CRS, and stored geometry metrics.

Every feature ID must equal `GPU:{source_document_id}:{logical_layer}:{source_feature_id}`. Catalog provenance must equal the current GPU provider, portal, commune, document type, archive name/SHA256, logical IDURBA archive identity, standard model, physical source layer, and inspected source CRS. A populated catalog cannot be supplied for an absent GPU layer. Current inspected layers remain:

| Logical layer | Source rows | Inspected source CRS | Normalized catalog |
| --- | ---: | --- | --- |
| `prescription_surface` | 320 | `IGNF:LAMB93` | surface, EPSG:2154, canonical 2D |
| `prescription_line` | 5 | `EPSG:2154` | line, EPSG:2154, canonical 2D |
| `prescription_point` | 5 | `EPSG:2154` | point, EPSG:2154, canonical 2D |
| `information_surface` | 149 | `IGNF:LAMB93` | surface, EPSG:2154, canonical 2D |
| `information_line` | absent | n/a | empty deterministic line catalog |
| `information_point` | absent | n/a | empty deterministic point catalog |

Supplied normalized Polygon/MultiPolygon, LineString/MultiLineString, and Point/MultiPoint geometries must have coordinate dimension exactly two. Only source normalization may create the canonical 2D copy; validation never hides a Z/M ordinate with `force_2d`.

The unchanged 3,638-parcel source is EPSG:4326. Parcel IDs are exact and unique; order, index, CRS, and geometry WKB are bound by the parcel-input hash. Parcel area is independently measured on a calculation-only EPSG:2154 copy and every relation's stored `parcel_metric_area_m2` must agree using only `technical_overlay_tolerance(...)`. All 2,414 relations resolve to a real source parcel and exact source feature. The parcel input is never reprojected or rewritten.

### Schema-v3 source and result integrity

Four new canonical UTF-8 JSON hashes bind the complete source context before official columns are appended:

- planning-document context: `fd15de370fdbbbc6688cb9211fc5b09058797ded9184263566e2ebee0dc7caa9`;
- parcel identity input: `100cf574d4f965153626cfcea57106b189498c36a1686d968ce980b272bf451f`;
- normalized catalogs input: `07bcfc3c1afb168b72e6711164874f5af56995c0b0f329dee25d929a9d505ade`;
- normalized relations input: `e9616edb6e09a7fd901774270a11ba717aa8c97dd7427dd14e445b661bc71097`.

The document payload excludes machine-local cache paths and operational cache state, while binding official document metadata, archive identity, standard lineage, physical/logical layer mapping, inspected summaries, and complete loaded source-layer facts. Every output component hash includes all four input hashes.

### Real Muret regression, outputs, and read-back

- Source parcels / features / relations: 3,638 / 479 / 2,414.
- Surface / line / point catalogs: 469 / 5 / 5; all EPSG:2154 and canonical 2D.
- Configured/observed pairs: 12/12; leading-zero strings unchanged; PRESCRIPTION `15/00` and `15/01` remain distinct.
- Resolved feature/relation rows: 479 / 2,414; unknown pairs: 0 / 0.
- Lost/extra parcel IDs, feature IDs, and relation rows: 0/0, 0/0, and 0/0.
- Offline reconstruction, resolution, source-complete validation, persistence, and read-back runtime: 5.158 seconds.

| Component | Rows | Schema-v3 content SHA256 | Output bytes |
| --- | ---: | --- | ---: |
| Code dictionary | 12 | `4238f069d84c6641e90702ebace797ec0d84a391ebf80c071858684b66b02355` | 9,642 |
| Surface features | 469 | `bb8df32392fc271bd28aaf481a1235ab2ecc417f1a7757f6f1747424d6024540` | 355,137 |
| Line features | 5 | `15be09bd8d7dd42682cb536bd4aad59621d058df7a7e3af3995171bcf0eced4b` | 37,194 |
| Point features | 5 | `21814ad5d006097c2b83e189a63dcb708a19416b85cfeccfc81bbcbc6894a875` | 33,727 |
| Parcel/feature relations | 2,414 | `f5d1ea58be9cd780b1d8d4d3238c8d896f5df1db1265da9aacd3fe7d76f3e48c` | 158,650 |

Complete result SHA256: `14cc65fff65cf135f2f672c1a04a6fd66a52e396c36326bedab11770b595e148`.

All five ignored Parquets were rewritten. The new ignored schema-v3 manifest is `data/processed/planning/muret_cnig_plu_2017_feature_codes.json` (2,788 bytes). Read-back reconstructed every immutable result scalar from the manifest rather than reusing the in-memory envelope, loaded all five frames from disk, checked exact filenames/row counts/diagnostics, and passed the public source-complete validator against the original GPU document, parcels, factual catalogs, relations, and checked-in profile.

Official CNIG mappings and coded DataFrame facts remain unchanged. No BESS impact or severity is assigned. No parcel is rejected. No score or legal interpretation is produced. No new dataset is downloaded and no parcel/feature spatial intersection is recomputed in this step.

## STEP 7D.4C.4 — Enforce unique chapter-scoped evidence occurrences

- Status: Complete
- Policy/result/output-manifest schemas: 5 / 5 / 5. Versions 1 through 4 are rejected; the checked-in profile is `muret_bess_written_zoning_v5`.
- Test-first regression: schema v4 accepted two evidence IDs with identical chapter, section/page fragment, and excerpt offsets when both were linked under the same compatible route. The dedicated regression failed before the correction and now passes.
- Occurrence contract: `(resolved_zone_chapter_label, section_id, page_number, section_page_fragment_sha256, excerpt_start, excerpt_end)` identifies exactly one evidence ID, kind, and direction. Duplicate entries fail explicitly rather than being deduplicated.
- Legitimate reuse remains factual: one evidence ID may support several compatible routes; identical literal text at different offsets remains distinct; and the same exact GENERAL occurrence may be represented once for each different chapter.
- Persistence boundary: the public source-complete result validator independently checks occurrence-key uniqueness on the supplied evidence catalog before comparing rebuilt frames and hashes. A coordinated duplicate plus recomputed hashes is rejected; Parquet read-back retains 26 unique keys.

### Real Muret regression and read-back

- Regulation chapter labels / unique labels: 13 / 13
- Routes / evidence rows / unique chapter-scoped occurrences / evidence-route links: 13 / 26 / 26 / 26
- Unlinked decision evidence / context-only evidence: 0 / 0
- Chapter status/confidence: 13 `CONDITIONAL_REVIEW` / `LOW`
- Raw GPU labels: 29, all `CONDITIONAL_REVIEW`
- Parcels: 3,638 input and output; lost / extra IDs = 0 / 0; prior fields, geometry, order, index, and CRS unchanged
- Runtime, including build-time source-complete validation: 24.392 seconds

Schema-v5 hashes:

- policy: `64cd30a13f4a46a2181236cc381e5b8a890f5d5d30bf15225289e4b3dc58c79d`
- evidence / links / routes: `193d480adc1fe01cf9aa71261c809746643e23f5debd645d1163ba46fb5a8f45` / `47634f59d0165299e690e55ed6fe8a87dc2dcab30ecaca8f0e84b7a9b6144029` / `ba01df262d6cffd3abe68dc7cb561dd821194a133bc41969ac3e4a510c181797`
- chapter / source-zone / parcel-zone: `d3fde89925c8f31ffa323373143faaa6ee04ee066f3e9cb9aa74e7f8bc8301c8` / `42b9339c2652e13bff9b3e284553719951e90268ac152ebab692d83f945ff0a7` / `de792d669fa06e0e6fd01faef270459b989ba96c80933f1be1be5f513560ae69`
- parcel output / complete result: `f5a4be8f729deeab257ade80500b10aa1d1f21979cfc51c1c349d7d39a7091db` / `288c2a70e8bd889a5dd7f3e5060642e1e632f3b62a999f354a9deaea16b1e650`

All eight ignored outputs were rewritten and read back. The reconstructed immutable schema-v5 result passed the public source-complete validator with the original factual inputs and policy.

The precheck remains conservative and documentary. It is not an authorization, permit decision, or legal opinion. No prescription or environmental interpretation, parcel rejection, score, LLM, or authorization claim is introduced.

## STEP 7D.4C.3 — Close evidence-to-route coverage and chapter identity

- Status: Complete
- Policy/result/output-manifest schemas: 4 / 4 / 4. Versions 1, 2, and 3 are rejected; no migration is inferred.
- Test-first regression: before the production correction, the new unlinked-difficulty test failed because schema v3 accepted a second `SUPPORTS_DIFFICULTY` occurrence that appeared in no route. Schema v4 now rejects every unlinked positive, difficulty, or condition occurrence.
- Evidence closure: each decision direction must occur in one or more explicit route arrays under its matching `POSITIVE`, `CONDITION`, or `DIFFICULTY` role. `CONTEXT_ONLY` evidence must occur in no route. One occurrence may support several routes only under the same compatible role.
- Normalized audit link: `muret_bess_zoning_evidence_route_links.parquet` contains one deterministic row per `(route_id, evidence_id)`. The public source-complete validator reconstructs this table from every route array and independently reconstructs each evidence row's sorted `linked_route_ids`, aligned `linked_route_roles`, and `decision_linked` flag.
- Output semantics: `evidence_ids` retains all chapter evidence. `decision_evidence_ids` and `context_evidence_ids` are separate on chapter, raw-zone, and parcel/zone outputs. Parcel `zoning_precheck_evidence_ids` is decision-only; `zoning_precheck_context_evidence_ids` preserves context without allowing it to influence status.
- Chapter identity: every factual `ZONE_CHAPTER` now requires an exact non-null unique chapter label and a unique section ID before policy completeness is evaluated. Duplicate labels are rejected even when no current GPU zone refers to them.

### Real Muret regression and integrity

- Regulation chapter sections / unique chapter labels: 13 / 13
- Routes / evidence rows / normalized route links: 13 / 26 / 26
- Decision-linked / context-only / unlinked decision evidence: 26 / 0 / 0
- Route kinds: 11 `CONDITIONAL_ROUTE`; 2 `RESTRICTION_EXCEPTION_ROUTE`
- Chapter status/confidence: 13 `CONDITIONAL_REVIEW` / `LOW`
- Raw GPU labels: 29, all `CONDITIONAL_REVIEW`
- Parcels: 3,638 input and output; 3,638 `CONDITIONAL_REVIEW`; lost / extra IDs = 0 / 0
- Parcel/zone interpretation rows: 5,095; touch-only factual rows: 0
- Original parcel fields, count, IDs, order, index, geometry, and CRS: unchanged
- Runtime, including the public build-time validation: 24.411 seconds

Integrity hashes:

- policy: `55b98fcc27cfb002c580338a38c4b9da1979ae4ab061db217945b7f018ccf45e`
- evidence catalog: `3d267d87938422167deaaf9fbb82bb11980e4e633943c09ed0d7b6a3dcf80433`
- evidence-route links: `236ed3a0d490789515b1b85cd449501efe4ed5ab9b8ce323669cd99966853e9c`
- route assessments: `85bd6bb6f4726bb269330cd717ce2a91ba2375a430838a8cd99929d297a0ed74`
- chapter / source-zone / parcel-zone: `84f0fd168d64df4315ba0e49014d728308a74b92b1aa940612f49ba882cfb45d` / `02cd77b5abbe6115702d1436b289705f15f44e7baf72217ba80d2f6c5524369c` / `46a673dc5c3fa133ce3e2c80d3d3a7d49ebbfb1e2e0ba4d399449dd1ea630f20`
- parcel output / complete result: `2bbe8d055b6c1c2219b9104c4a4610c1b48d46582b656c20d617d173810ce43c` / `4252a40036363235cc0eca0be1e8dd9ba9db3a09aeb34e914fda8466f3095590`

All eight ignored outputs were rewritten. Their persisted Parquet tables and schema-v4 JSON envelope were read back, the immutable result was reconstructed from persisted scalars and frames, and the public source-complete validator passed against the original index, structure/config, 221-zone catalog, 5,095 factual relations, 3,638-parcel input, and checked-in policy.

This remains a conservative LandScout preliminary written-zoning precheck, not an authorization, permit decision, or legal opinion. Prescription and information features remain uninterpreted. No parcel is rejected and no score is created.

## STEP 7D.4C.2 — Link BESS zoning evidence into coherent decision routes

- Status: Complete
- Policy schema / result-hash schema / ignored manifest schema: `3` / `3` / `3`; versions 1 and 2 are rejected rather than migrated.
- A required red-first regression demonstrated the prior defect: positive and condition evidence placed in one chapter, but not linked to a common route, still produced `CONDITIONAL_REVIEW`. The test failed against schema v2 and now passes only because route membership is explicit.

### Route and review semantics

The precheck retains `planning_precheck_scope = WRITTEN_ZONING_REGULATION_ONLY` and now separately records:

```text
review_scope = CONFIGURED_USE_CONTROL_ARTICLES_ONLY
```

The source-family scope and the reviewed-portion scope are not interchangeable. Every complete chapter is now `COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES`; an `INCOMPLETE` chapter may use an empty reviewed-section list, omit required articles, and must remain `UNKNOWN / LOW`. The normalized chapter table stores the exact deterministic `missing_required_section_ids` tuple.

Chapter statuses are derived from explicit route assessments and must equal the YAML declaration:

- `DIRECT_ROUTE`: positive evidence only, yielding `POTENTIALLY_COMPATIBLE` only when no unresolved difficulty route exists;
- `CONDITIONAL_ROUTE`: positive evidence and its linked condition, yielding `CONDITIONAL_REVIEW`;
- `RESTRICTION_EXCEPTION_ROUTE`: positive exception evidence and linked difficulty evidence, yielding `CONDITIONAL_REVIEW`;
- `DIFFICULTY_ONLY`: difficulty evidence with no coherent positive route, yielding `LIKELY_DIFFICULT`;
- incomplete review, no coherent route, or only unlinked condition/context evidence yields `UNKNOWN`.

No association is inferred from evidence order or mere chapter membership. Every route ID is globally unique; every referenced evidence ID must belong to that chapter and have the direction required by its route role. An unrelated condition cannot affect another route.

### Complete exact source-rule context

All 26 evidence occurrences still identify a short exact effect excerpt. They now also retain one of 17 complete exact source-rule occurrences using `source_rule_id`, raw source-rule text, SHA256, and 0-based half-open offsets in the same validated section-page fragment. The evidence offsets must lie wholly inside the source-rule offsets. One source-rule ID always resolves to one occurrence; identical occurrences use one ID; partial source-rule overlaps are rejected.

The real Muret policy was re-reviewed from the complete retained rules:

- UA, UB, UC, UD, UF, AU, and AUf use the full ICPE conditional sentence, including `ne sont autorisées qu’à`, its connector, compatibility qualification, and local-necessity qualification.
- UP and AUp preserve the full restriction/exception frame around public or collective-interest equipment, rather than treating the category phrase as unconditional permission.
- AU0 and AUf0 preserve the full prohibition/exception sentence for collective-interest networks and public infrastructure, with the separate PLU-modification condition linked in the same route assessment.
- A and N preserve one complete restriction-and-exception rule occurrence; their restriction and infrastructure-exception excerpts are linked as one explicit conflict.

The evidence-kind/direction matrix is exhaustive for all eight configured evidence kinds. Generic access, network, risk, nuisance, and other conditions cannot serve as positive route evidence. Contradiction detection keys the exact occurrence identity—section, page, fragment hash, and offsets—so identical text at different offsets remains distinct.

The factual structure API now validates the complete structure and returns its section-page fragments from the same rebuild. One precheck `_build_result()` therefore performs exactly one factual-structure rebuild; the independent public result validator still performs its own source-complete rebuild.

### Real Muret regression

The resulting distribution was not used as a target. It remains unchanged only because each chapter independently satisfies the schema-v3 route contract:

| Result | Count |
| --- | ---: |
| Complete / incomplete chapter reviews | 13 / 0 |
| Normalized routes | 13 |
| `CONDITIONAL_ROUTE` / `RESTRICTION_EXCEPTION_ROUTE` | 11 / 2 |
| Evidence occurrences / unique source rules | 26 / 17 |
| Linked / unlinked conditions | 11 / 0 |
| `CONDITIONAL_REVIEW` chapters / raw zone labels / parcels | 13 / 29 / 3,638 |
| Positive parcel-zone rows / touch-only rows | 5,095 / 0 |
| Mixed / `UNKNOWN` parcels | 0 / 0 |
| Chapters without explicit BESS wording | 13 |
| Lost / extra parcel IDs | 0 / 0 |

All chapter confidences remain `LOW`. Evidence directions remain 13 positive-route, 11 condition, and 2 difficulty occurrences. These are preliminary category-route assessments; they do not establish that a BESS falls within the cited categories or satisfies their conditions.

### Integrity, outputs, and read-back

- Policy config SHA256: `504997abd09f5a9ef4719a8e987fa04357c37b02247d29835082bf6d0a981c8a`
- Factual structure input SHA256: `055d43ba51af64ba3829244a894ecd3f32f0d196b58af1eee80722875476d628`
- Zone-map / zoning-relation SHA256: `718d4721d54a76b8a28d152ba6535b3c948e606b3c4fc8d9f4fe9742c8e99453` / `547614f20eba5ba493d50c0162e498ffa0e7345cce65eb072537f0caf7e7a94b`
- Evidence catalog SHA256: `caf47c6d8176d480a63ef05a245b0fbb9c02bd0c5b473753cfaa4ae44a41dfcf`
- Route table SHA256: `e56d248e08e2738837c23d71053d1679da78dfd9bc2a35412aff79bcb5f56838`
- Chapter / raw-zone / parcel-zone SHA256: `4961654d26c7b9125a5b7a37604d91a7e218bed0d0cdcca574c24cee3a5d2e53` / `91af7742ae385cb363ac7a7aeab01bbf840ac580275c341ebb62dd259df4a65d` / `94c9eef80612a6d2ccfbe91dc2efcaa6bf6ccc80502b859f9fb1dc74852e6f6f`
- Parcel output / complete result SHA256: `7533cc8654d9bd555c2a423b5d4ada0af05e569397f6157bf8cc34642e799e16` / `c6c059e87d8c50e1abe98ea10f5022eecfb92ccc79fe1606e7917fdedf7839f5`
- Complete build plus persisted source-complete read-back validation runtime: 23.926 seconds
- Evidence catalog: 26 rows, 27,102 bytes
- Route table: 13 rows, 15,202 bytes
- Chapter policy: 13 rows, 20,074 bytes
- Raw-zone policy: 29 rows, 14,222 bytes
- Parcel-zone policy: 5,095 rows, 137,006 bytes
- Parcel GeoParquet: 3,638 rows, 1,588,167 bytes
- JSON manifest: 4,144 bytes

All seven ignored outputs were read back. The immutable schema-v3 result was reconstructed, including the route table and evidence catalog, and accepted by the public source-complete validator using the original factual index, structure config/result, zones, intersections, parcels, and checked-in policy. Parcel IDs, order, index, geometry, CRS, and every prior field remained identical.

This is not planning authorization or a legal opinion.

No prescription or information feature is interpreted.

No parcel is rejected.

No score is created.

## STEP 7D.4C.1 — Harden BESS zoning-policy semantics and evidence auditability

- Status: Complete
- Policy schema / result-hash schema / output-manifest schema: `2` / `2` / `2`
- The public interpretation and validation APIs now receive the schema-v2 factual-structure configuration and invoke the existing source-complete `validate_planning_regulation_structure(...)` contract before applying policy. The precheck no longer carries a parallel private copy of the structure-stage schemas or hashing rules.
- A red-first regression test demonstrated the former defect: a chapter containing only `CONDITION` evidence was accepted as `CONDITIONAL_REVIEW`. The test failed against the prior implementation, and now passes because that status requires an explicit positive route plus a condition, or an explicit positive/difficulty conflict.

### Review and evidence contracts

Every chapter records `review_completeness`, an explicit ordered `reviewed_section_ids` list, and a review note. The checked-in policy requires review of existing zone Articles 1 and 2; all 13 real chapters are recorded as `COMPLETE_FOR_WRITTEN_ZONING_PRECHECK`, with both relevant articles listed. Evidence must belong to one of those reviewed sections, except that a relied-upon `GENERAL` section may be listed explicitly. A section from another zone chapter is rejected.

The status rules are now deterministic:

- `POTENTIALLY_COMPATIBLE` requires a complete review and positive route evidence without unresolved difficulty or conditions.
- `CONDITIONAL_REVIEW` requires a complete review, positive route evidence, and either a condition or explicit conflicting difficulty evidence.
- `LIKELY_DIFFICULT` requires difficulty evidence without a defensible positive route.
- `UNKNOWN / LOW` is mandatory for incomplete review; condition-only or contextual-only evidence cannot establish a route.

Evidence-kind/direction combinations are checked explicitly. In particular, a restriction cannot support potential compatibility, a permission cannot support difficulty, and an access/network condition cannot be used as positive route evidence.

Each evidence row now identifies one exact occurrence within a validated section-page fragment using a fragment SHA256 and 0-based half-open `excerpt_start` / `excerpt_end` offsets. The exact excerpt must equal that fragment slice and retain the source accents and punctuation. Tests cover duplicate text, wrong page, wrong fragment hash, and wrong offsets. The new 26-row evidence catalog is the sole ID authority for chapter, raw-zone, parcel-zone, and parcel evidence references and is included in the complete result envelope.

All positive-area zoning relations now require both factual denominators and both percentages: `parcel_metric_area_m2`, `zone_area_m2`, `parcel_share_pct`, and `zone_share_pct`. Percentages are recomputed from the measured intersection area and checked using only the shared technical overlay tolerance.

### Real Muret re-review

The real regulation still contains no explicit BESS or battery wording. All 13 chapters therefore remain `LOW` confidence and require formal review; that distribution was not used as a target. The evidentiary basis changed materially:

| Chapters | Reviewed sections | Evidence route |
| --- | --- | --- |
| UA, UB, UC, UD, UF | each chapter's Articles 1 and 2 | separate positive ICPE-route excerpt plus separate condition excerpt |
| UP | `SECTION-0080`, `SECTION-0081` | public/collective-interest route plus condition |
| AU | `SECTION-0095`, `SECTION-0096` | ICPE route plus condition; infrastructure prerequisites alone are not treated as a route |
| AUp | `SECTION-0110`, `SECTION-0111` | public-interest route plus condition |
| AUf | `SECTION-0125`, `SECTION-0126` | ICPE route plus condition; infrastructure prerequisites alone are not treated as a route |
| AU0, AUf0 | Articles 1 and 2 (`SECTION-0140/0141`, `SECTION-0155/0156`) | separate infrastructure exception and prior-PLU-modification condition |
| A, N | Articles 1 and 2 (`SECTION-0170/0171`, `SECTION-0184/0185`) | separate restrictive and technical-infrastructure exception excerpts, recorded as an explicit conflict |

Observed status and evidence counts:

| Result | Count |
| --- | ---: |
| Chapter policies / raw-zone policies | 13 / 29 |
| Evidence catalog rows | 26 |
| Positive parcel/zone interpretation rows | 5,095 |
| Input/output parcels | 3,638 / 3,638 |
| `CONDITIONAL_REVIEW` chapters / raw labels / parcels | 13 / 29 / 3,638 |
| `MIXED_REVIEW_REQUIRED` parcels | 0 |
| `UNKNOWN` parcels | 0 |
| Chapters without explicit route evidence | 0 |
| Chapters without explicit BESS wording | 13 |
| Lost / extra parcel IDs | 0 / 0 |

Evidence directions are 13 `SUPPORTS_POTENTIAL_COMPATIBILITY`, 11 `CONDITION`, and 2 `SUPPORTS_DIFFICULTY`. Evidence kinds are 16 `ICPE_RULE`, 4 `TECHNICAL_EQUIPMENT_RULE`, 2 `PUBLIC_INTEREST_EXCEPTION`, 2 `USE_RESTRICTION`, and 2 `OTHER_RELEVANT_RULE`.

### Integrity, outputs, and read-back

- Policy config SHA256: `ac8932d2ade74dd88d1647181ca9b8e930582cf61a9ee3c7da7c3721276c1094`
- Factual structure input SHA256: `055d43ba51af64ba3829244a894ecd3f32f0d196b58af1eee80722875476d628`
- Zone-map input SHA256: `718d4721d54a76b8a28d152ba6535b3c948e606b3c4fc8d9f4fe9742c8e99453`
- Zoning-relation input SHA256: `547614f20eba5ba493d50c0162e498ffa0e7345cce65eb072537f0caf7e7a94b`
- Evidence catalog SHA256: `dfa7fa078ef75696cee2f6c9677e072d8cd2ebf89cf4104b6cc7c81cdc39bbd4`
- Chapter / raw-zone / parcel-zone SHA256: `ae011df49884b861747b23de0ee65555eb379016c73f9c2e18be571771b247fa` / `524814ad0846d8419875293b6246e82b37a54a1e160d0e09e9f8e2c45c0407ce` / `a04bb860e711d74b9a9031e4a5abb86d2c5e229879ea907c75d6999aa529e878`
- Parcel-output SHA256: `9748d06e630f014be946cdb65c9722132299e32d588a7abe719dab8930f5b726`
- Complete result SHA256: `73395cf098b4139fc0f6a11cbe7bb0e1b50f5b4f19920d7e30191769bbbc6778`
- Source-complete build plus persisted read-back validation runtime: 41.260 seconds
- `muret_bess_zoning_evidence.parquet`: 26 rows, 20,096 bytes
- `muret_bess_zoning_chapter_policy.parquet`: 13 rows, 18,592 bytes
- `muret_bess_zoning_source_policy.parquet`: 29 rows, 13,532 bytes
- `muret_bess_zoning_policy_relations.parquet`: 5,095 rows, 136,308 bytes
- `muret_bess_zoning_precheck.parquet`: 3,638 rows, 1,587,466 bytes; original GeoParquet CRS, geometry, index, order, and all prior columns preserved
- `muret_bess_zoning_precheck.json`: 4,594 bytes

All six outputs were read back, the immutable schema-v2 result was reconstructed from persisted data, and the public source-complete validator passed with the original index, factual structure configuration/result, zone catalog, zoning intersections, parcels, and checked-in policy.

This is a conservative LandScout preliminary screening status.

It is not an authorization, permit decision, or legal opinion. Formal review of the complete planning document, prescriptions, servitudes, and project design remains required.

No prescription or information feature is interpreted.

No parcel is rejected.

## STEP 7D.4A — Extract and index the Muret PLU written regulation

- Status: Complete
- Implementation summary: Added a factual page-level text index for the one validated Muret written-regulation PDF in the current GPU extraction inventory. The stage validates current-document/archive lineage, containment, regular-file status, inventory classification, byte size, and SHA256 before using `pypdf`; it keeps raw extracted text separate from accent/case/whitespace-normalized search text and isolates an extraction failure to its page.
- Important files: `src/landscout/stages/index_planning_regulation.py`, `tests/unit/test_index_planning_regulation.py`, `src/landscout/stages/__init__.py`, `pyproject.toml`, `uv.lock`
- Tests/checks: 31 focused offline tests and the complete 787-test suite pass. They cover exact-target API scope, discovery, ambiguity, path/link integrity, size/SHA mismatch, page states and numbering, per-page and reader failures, search normalization, determinism, corrupted-index rejection, and input immutability. Ruff and mypy pass.
- Important decisions: `pypdf` is the sole added extraction dependency; no OCR dependency or OCR processing is used. Search is literal after Unicode decomposition, accent removal, case folding, and whitespace normalization. A hit is a retrieval fact only and carries no legal or BESS meaning. Complete regulation text is stored only in ignored processed data, not this log or Git.
- Known issues: Poppler rendering tools were unavailable locally, but all 142 pages yielded deterministic embedded text with no extraction error, replacement character, or NUL character. This step indexes text; it does not claim layout fidelity or interpret the regulation.

### Validated source and extraction

- Document ID: `33edb4c9f6943c88d8d92518bff20bec`
- Archive SHA256: `9d6677cd6634b56b712311042f0cc714d5ca42a38f82a417b27dd473255d7d93`
- PDF relative path: `31395_PLU_20240215/Pieces_ecrites/3_Reglement/31395_reglement_20240215.pdf`
- PDF size: 2,162,501 bytes
- PDF SHA256: `5358ebad6b0cda6de681ba3536e29b8b6291fb701c7d3711f4ee1d6fdb85c6fb`
- Extractor: `pypdf 6.15.0`
- Pages: 142; `TEXT` 142, `EMPTY` 0, `ERROR` 0
- Total raw extracted characters: 325,851
- First real extraction/index runtime: 7.621 seconds
- A second independent extraction produced an identical page table.

### Factual diagnostic searches

Search counts below are page-hit rows / literal normalized occurrences; page numbers are 1-based.

| Runtime term | Hit pages / occurrences | Page numbers |
| --- | ---: | --- |
| `batterie` | 0 / 0 | — |
| `stockage` | 29 / 35 | 8, 11, 22, 24, 25, 26, 36, 38, 39, 40, 48, 51, 52, 63, 64, 65, 74, 75, 81, 84, 85, 95, 96, 106, 107, 127, 128, 137, 138 |
| `énergie` | 12 / 22 | 4, 11, 25, 39, 51, 63, 74, 84, 95, 106, 127, 138 |
| `poste électrique` | 0 / 0 | — |
| `transformateur` | 10 / 10 | 11, 16, 30, 43, 54, 74, 87, 95, 128, 138 |
| `ouvrage technique` | 0 / 0 | — |
| `équipement d'intérêt collectif` | 0 / 0 | — |
| `service public` | 1 / 1 | 6 |
| `installation classée` | 0 / 0 | — |
| `ICPE` | 0 / 0 | — |
| `risque` | 25 / 58 | 5, 8, 9, 22, 23, 35, 36, 37, 48, 49, 60, 61, 71, 72, 80, 81, 82, 94, 104, 114, 125, 126, 134, 135, 136 |
| `nuisance` | 11 / 11 | 8, 22, 35, 36, 48, 71, 80, 81, 101, 125, 136 |

Zero hits mean only that the exact normalized runtime phrase was absent; variants or different wording are not inferred.

### Outputs and read-back

- `data/processed/planning/muret_plu_regulation_pages.parquet`: 142 rows, 258,518 bytes
- `data/processed/planning/muret_plu_regulation_search_hits.parquet`: 88 rows, 7,292 bytes
- `data/processed/planning/muret_plu_regulation_index.json`: 740 bytes

Read-back verified document/archive/PDF lineage, PDF hash, page count, unique ordered page numbers, exact text/status/character fields, deterministic repeat extraction, and valid search-hit page references. Generated outputs remain ignored by Git.

No legal or BESS conclusion is produced. No zone is classified, and no parcel is rejected.

## STEP 7D.4A.1 — Generalize and harden planning-regulation indexing

- Status: Complete
- Implementation summary: Removed the Muret PDF filename constant. Automatic selection now derives the one primary regulation filename from the loaded zoning layer's exact `NOMFIC` values and requires one matching official `written_files` entry plus exactly one matching validated extraction-inventory file. A caller may select explicitly only among filenames that satisfy all three source checks.
- Search normalization: `fr_literal_v1` applies Unicode compatibility normalization, case and accent folding, whitespace collapsing, canonical apostrophes and dashes, `œ`/`æ` expansion, and soft-hyphen removal. It is literal retrieval only: there is no stemming, synonym expansion, semantic matching, OCR, or legal interpretation. Raw page text is unchanged.
- Integrity model: each page has a canonical UTF-8 JSON `page_content_sha256` binding its number, extraction state, raw and normalized text, character count, error, and normalization profile. The immutable index carries `pages_content_sha256` over the complete ordered page table. Search results use an immutable lineage envelope and `hits_content_sha256`; validators recompute page text, hashes, source-derived raw/normalized contexts, ordering, counts, page references, and lineage before use.
- Tests/checks: 62 focused offline tests and the complete 818-test suite pass. They cover generic and explicit source selection, all three source cross-checks, French normalization, raw-context mapping, coordinated mutation, page and envelope hashes, dependency-version failure, search-result lineage/integrity, stable empty results, determinism, and input immutability. Full Ruff and mypy checks pass.

### Real Muret regression

- Source-derived filename: `31395_reglement_20240215.pdf`
- Unique zoning `NOMFIC` values: 1; official `written_files` matches: 1; extraction-inventory basename matches: 1
- PDF relative path: `31395_PLU_20240215/Pieces_ecrites/3_Reglement/31395_reglement_20240215.pdf`
- PDF size / SHA256: 2,162,501 bytes / `5358ebad6b0cda6de681ba3536e29b8b6291fb701c7d3711f4ee1d6fdb85c6fb`
- Document ID / archive SHA256: `33edb4c9f6943c88d8d92518bff20bec` / `9d6677cd6634b56b712311042f0cc714d5ca42a38f82a417b27dd473255d7d93`
- Extractor / profile: `pypdf 6.15.0` / `fr_literal_v1`; OCR was not used
- Pages: 142 (`TEXT` 142, `EMPTY` 0, `ERROR` 0); raw extracted characters: 325,851
- All 142 page hashes validate. Complete ordered page-table SHA256: `928e7e59c45e27c38e39d3f28f3eb10bd2590886416df57efc4ac8e5d8901ec9`
- Two independent real extractions produced the same page-table hash. Index plus diagnostic search runtime: 6.558 seconds for the recorded output run.
- Search-result rows / occurrences: 88 / 137. Complete ordered search-result SHA256: `17b069bbd6142ac4452dc806094e75f21340ef0da929f5c3d3f8b1d356ecd890`

| Runtime term | Hit-page rows | Literal occurrences |
| --- | ---: | ---: |
| `batterie` | 0 | 0 |
| `stockage` | 29 | 35 |
| `énergie` | 12 | 22 |
| `poste électrique` | 0 | 0 |
| `transformateur` | 10 | 10 |
| `ouvrage technique` | 0 | 0 |
| `équipement d'intérêt collectif` | 0 | 0 |
| `service public` | 1 | 1 |
| `installation classée` | 0 | 0 |
| `ICPE` | 0 | 0 |
| `risque` | 25 | 58 |
| `nuisance` | 11 | 11 |

The improved normalization did not change these real literal counts. Each hit now carries document/archive/PDF lineage plus both a source-derived `raw_context` and a separately labelled `normalized_context`; normalized context is not presented as a source quote.

### Outputs and read-back

- `data/processed/planning/muret_plu_regulation_pages.parquet`: 142 rows, 267,275 bytes
- `data/processed/planning/muret_plu_regulation_search_hits.parquet`: 88 rows, 15,946 bytes
- `data/processed/planning/muret_plu_regulation_index.json`: schema version 2, 1,728 bytes

The JSON manifest records source selection, document/archive/PDF lineage, extractor/version, normalization profile, page count, page-table hash, search-result hash, and output row counts. After writing, both Parquet files and the JSON manifest were read back; the strengthened index and search-result validators accepted the reconstructed envelopes with identical hashes and row counts.

No legal or BESS conclusion is produced.
No zone is classified.
No parcel is rejected.

## STEP 7D.4A.2 — Seal regulation-source selection and index lineage

- Status: Complete
- Implementation summary: Before trusting zoning `NOMFIC`, the indexer now resolves the zoning dataset under the verified extraction root, rejects links/junctions, checks every relevant source-family member against extraction-inventory path, byte size, and SHA256, re-reads the actual source layer with GeoPandas/pyogrio, and compares row count/order, source layer, CRS, every source attribute (including `LIB_IDZONE` and `NOMFIC`), and geometry WKB against the loaded zoning frame. Both ESRI Shapefile families and GeoPackage layers are covered offline.
- Source selection: automatic selection is explicitly `ZONING_NOMFIC`. The selected filename, actual zoning layer/driver and ordered source-file integrity, exact official `written_files` entry, and selected PDF inventory record are bound by canonical UTF-8 JSON in `source_selection_sha256`.
- Complete lineage envelopes: schema version 1 is persisted and strictly enforced independently for page hashes, the complete index hash, and search hashes. `index_content_sha256` binds every immutable index metadata field plus the page-table envelope. Search results bind and must match that exact index hash; sharing a PDF hash alone is insufficient.
- Raw Unicode contexts: normalized characters now map to source spans rather than single positions. Zero-context retrieval preserves exact source substrings for precomposed and decomposed accents, `œ`/`æ` expansion, typographic apostrophes, and ignored soft hyphens at either match boundary. Raw text remains untouched and normalized context remains separately labelled.
- Controlled failures: malformed schema values, mutable search-term lists, malformed Pandas cells, inconsistent source metadata, and canonical JSON serialization failures all surface as `PlanningRegulationIndexError`; serialization failures retain the chained cause.
- Tests/checks: 114 focused offline tests and the complete 870-test suite pass. Full Ruff and mypy checks pass.

### Real Muret regression

- Zoning source: `31395_ZONE_URBA_20240215`, ESRI Shapefile, 221 rows
- Revalidated source family: 7 files (`.cpg`, `.dbf`, `.prj`, `.qix`, `.qmd`, `.shp`, `.shx`); containment, sizes, and SHA256 values all matched the verified GPU extraction inventory
- Loaded/source zoning comparison: exact row count/order, CRS, complete attribute table, `LIB_IDZONE`, `NOMFIC`, and geometry WKB passed
- Selected regulation: `31395_reglement_20240215.pdf` via `ZONING_NOMFIC`
- Source-selection SHA256: `1b4c1cdb9c12cf6bb9a5bcdb97bf9c972fb9f007472dbf0aae37acb376d5eb32`
- Page / index / search hash schema versions: 1 / 1 / 1
- Pages: 142 (`TEXT` 142, `EMPTY` 0, `ERROR` 0); raw characters: 325,851; OCR was not used
- Pages-content SHA256: `928e7e59c45e27c38e39d3f28f3eb10bd2590886416df57efc4ac8e5d8901ec9`
- Complete index-content SHA256: `6a0009228ca17128c0a8bb329d9c2277a1b6638708a67b913b72ee93063e42cd`
- Search rows / occurrences: 88 / 137, unchanged; search-result SHA256: `00428db8cf07767ba0705953a5fda760b6ae97971e3e41b521117501f3a14b95`
- Two independent real index runs produced identical page-table and complete-index hashes
- Recorded source revalidation + extraction + diagnostic-search runtime: 11.635 seconds

### Outputs and read-back

- `data/processed/planning/muret_plu_regulation_pages.parquet`: 142 rows, 267,275 bytes
- `data/processed/planning/muret_plu_regulation_search_hits.parquet`: 88 rows, 15,946 bytes
- `data/processed/planning/muret_plu_regulation_index.json`: manifest schema 3, 4,374 bytes

The JSON manifest now persists the complete zoning/PDF source-selection evidence, all three hash schema versions, page/index/search hashes, document/archive/PDF lineage, requested terms, and output row counts. Both Parquet files and the JSON manifest were read back into immutable models; both public validators passed, and the persisted source-selection evidence reproduced the recorded selection hash.

SHA256 integrity detects inconsistent or accidental mutation. Official source authenticity remains grounded in the verified GPU archive and extraction inventory.

No OCR.
No legal interpretation.
No zone classification.
No parcel rejection.

## STEP 7D.4B — Build factual regulation structure and zone evidence

- Status: Complete
- Implementation summary: Added a document-locked, configuration-driven parser that turns the validated 142-page regulation index into ordered factual sections, maps every raw GPU zoning label using exact headings or explicit aliases, and retrieves literal topic evidence inside the resulting sections. No Muret heading, alias, or topic vocabulary is embedded in Python.
- Important files: `configs/planning/muret_plu_structure.yaml`, `src/landscout/stages/structure_planning_regulation.py`, `tests/unit/test_structure_planning_regulation.py`, and the four ignored outputs under `data/processed/planning/`.
- Tests/checks: 19 focused offline tests cover document locks, strict YAML and regex validation, alias cycles, repeated table-of-contents headings, hierarchy, multi-page articles, exact/alias/unmapped/ambiguous mappings, absence of fuzzy matching, mutation detection, page references, input immutability, and the dominant-candidate mapping gate. The complete 889-test suite passes; Ruff and mypy pass.

### Real document-structure inspection

The rules below were derived from the current Muret page index before the YAML grammar was written:

- The extracted 142-page regulation has no separate table-of-contents section. Page 3 contains a factual enumeration of zones inside general article 3, but not a duplicate chapter index.
- Page 1 is the cover. General provisions use five uppercase headings: `ARTICLE 1 - ...` through `ARTICLE 5 - ...`, starting on pages 2, 2, 3, 3, and 4 respectively and continuing through page 6.
- Zone chapters use an anchored `ZONE <label>` heading. The 13 observed body chapters begin on pages 7, 21, 35, 47, 59, 70, 80, 92, 101, 113, 119, 124, and 134 for `UA`, `UB`, `UC`, `UD`, `UF`, `UP`, `AU`, `AUp`, `AUf`, `AU 0`, `AUf 0`, `A`, and `N`.
- Zone articles use `ARTICLE <zone> <number> - <title>` with both hyphen and en-dash separators. Titles can continue over subsequent uppercase lines. The source also contains compact forms such as `ARTICLE UC 10–...` and an uppercase `AUF0` spelling in one article; matching preserves the chapter's raw canonical label while comparing this source spelling case-insensitively.
- The repeated page header is `Muret-12ème modification du PLU`; the footer is the standalone page number. Both ignored patterns are explicit in YAML. Ordinary mixed-case Code de l'urbanisme citations such as `Article R.111.2.` are not body headings.
- Article numbering restarts within each zone. Some source chapters omit article numbers rather than presenting a complete 1–14 sequence; the parser records what exists and does not fabricate missing articles.

The YAML source lock binds document ID `33edb4c9f6943c88d8d92518bff20bec`, PDF SHA256 `5358ebad6b0cda6de681ba3536e29b8b6291fb701c7d3711f4ee1d6fdb85c6fb`, page-table SHA256 `928e7e59c45e27c38e39d3f28f3eb10bd2590886416df57efc4ac8e5d8901ec9`, complete index SHA256 `6a0009228ca17128c0a8bb329d9c2277a1b6638708a67b913b72ee93063e42cd`, and normalization profile `fr_literal_v1`. Unknown YAML fields, duplicate YAML keys, bad regexes, blank terms, duplicate normalized terms, and alias cycles fail before parsing.

### Real sections and zone mapping

| Structural result | Count |
| --- | ---: |
| All sections | 196 |
| `OTHER` cover sections | 1 |
| General sections/articles | 5 |
| Zone chapters | 13 |
| Zone articles | 177 |
| Unique raw GPU zone labels | 29 |
| `EXACT` mappings | 12 |
| `CONFIG_ALIAS` mappings | 17 |
| `UNMAPPED` mappings | 0 |
| `AMBIGUOUS` mappings | 0 |
| Candidate parcels affected by unmapped/ambiguous labels | 0 |

Exact chapter matches are `A`, `AU`, `AU0`, `AUf`, `AUp`, `N`, `UA`, `UB`, `UC`, `UD`, `UF`, and `UP`. The 17 explicit aliases map source sub-zone labels only through YAML: `UAa`/`UAb` to `UA`; `UBa`/`UBb` to `UB`; `UFa`/`UFc`/`UFd` to `UF`; `AUa` to `AU`; `AUfa`/`AUfb`/`AUfc`/`AUfd` to `AUf`; `AUfo` to the actual `AUf0` chapter; and `NL`/`Ne`/`Nh`/`Nr` to `N`. Prefix similarity is never a mapping method.

All 3,638 current candidate parcels and 5,095 factual parcel/zone relations were represented in the coverage counts. Every raw label used as the deterministic dominant zone by at least one candidate is `EXACT` or `CONFIG_ALIAS`; the stage would stop on any dominant unresolved label.

### Factual topic evidence

Literal terms are configured by retrieval topic and reuse `fr_literal_v1`; they are not synonyms, rules, or severity labels. One evidence row represents a topic/term/section/page combination and preserves both raw and normalized context.

| Topic | Evidence rows | Literal occurrences |
| --- | ---: | ---: |
| `access` | 65 | 188 |
| `classified_installation` | 17 | 20 |
| `destination_and_use` | 29 | 30 |
| `electricity` | 34 | 37 |
| `energy` | 12 | 22 |
| `fire_safety` | 36 | 57 |
| `networks` | 62 | 277 |
| `nuisance` | 22 | 22 |
| `public_interest_equipment` | 25 | 25 |
| `risk` | 49 | 73 |
| `setbacks` | 133 | 196 |
| `technical_equipment` | 16 | 27 |
| `transformer` | 10 | 10 |

| Location | Evidence rows | Literal occurrences |
| --- | ---: | ---: |
| General provisions / cover | 13 | 19 |
| `UA` | 50 | 93 |
| `UB` | 46 | 90 |
| `UC` | 44 | 90 |
| `UD` | 43 | 87 |
| `UF` | 34 | 73 |
| `UP` | 43 | 84 |
| `AU` | 50 | 86 |
| `AUp` | 39 | 78 |
| `AUf` | 39 | 84 |
| `AU0` | 21 | 27 |
| `AUf0` | 16 | 23 |
| `A` | 38 | 78 |
| `N` | 34 | 72 |

`GENERAL_RULE` and `ZONE_SPECIFIC_RULE` describe only where the literal text occurs. Both are retained; neither states legal priority or effect.

### Integrity, outputs, and read-back

- Section hash schema version: 1
- Structure-config SHA256: `709d63c89d6aa5d668930303e900f655abd83c8a348120c7c2a4d73f8c30a029`
- Ordered sections SHA256: `df6f9489ee017962637243e0eef851a8e7b15b5853c98511e83de1933973c099`
- Ordered zone-map SHA256: `1df96ff62d83283c1adf3ceced845fb066fedbcb04434041f65d8e98d60902a5`
- Ordered topic-evidence SHA256: `09be72cba6d43be2cfbfff1cff75e315f747a58564c9b24aa4fc2b47d577f0d8`
- Real structure runtime: 8.212 seconds
- Sections Parquet: `muret_plu_regulation_sections.parquet`, 196 rows, 280,570 bytes
- Zone-map Parquet: `muret_plu_zone_section_map.parquet`, 29 rows, 11,117 bytes
- Topic-evidence Parquet: `muret_plu_topic_evidence.parquet`, 510 rows, 50,865 bytes
- Structure manifest: `muret_plu_structure_index.json`, 2,394 bytes

All ignored outputs were read back. The public validator accepted the reconstructed immutable result, source page references remained valid, and all three ordered-content hashes reproduced exactly. Coordinated mutable-DataFrame changes are rejected by the outer content envelopes.

No legal conclusion is produced.
No BESS compatibility status is assigned.
No parcel is rejected.
No score is calculated.

## STEP 7D.4B.1 — Harden regulation structure and evidence fidelity

- Status: Complete
- Implementation summary: Closed the parser's remaining trust boundaries without changing its factual section hierarchy or zoning aliases. French literal normalization and raw-span reconstruction now live in one shared `planning_text` module used by both regulation stages. The public validator receives and revalidates the complete index, strict config, ordered zone catalog, ordered zoning relations, and result; it independently rebuilds the expected sections, mapping, evidence, and hashes before accepting a result.
- Important files: `src/landscout/common/planning_text.py`, `src/landscout/stages/index_planning_regulation.py`, `src/landscout/stages/structure_planning_regulation.py`, `configs/planning/muret_plu_structure.yaml`, and both regulation test modules.
- Tests/checks: 178 focused index/structure tests pass. They retain the complete `fr_literal_v1` Unicode suite and add positional page filtering, mandatory regex captures, lossless record partitioning, strict hierarchy/mapping contracts, source-complete rebuild validation, area bounds, token boundaries, longest-match overlap handling, match provenance, and coordinated mutation rejection. The complete 934-test suite passes; Ruff and mypy pass.

### Positional source fidelity

Header/footer regexes now operate only at page edges. The parser removes contiguous configured header lines from the leading page region and configured footer lines from the trailing page region, with deterministic surrounding-blank handling. An identical header-looking string or numeric string inside body text is retained. In the current PDF the repeated title and page number are consecutive leading page-header records, so both are configured as headers; the footer list is correctly empty.

Every retained line now has a sequential `record_id`, original page number, original 1-based page-line number, and untouched raw text. Section rows bind their inclusive record boundaries, record count, and ordered record SHA256. The real result is an exact partition:

| Record invariant | Real result |
| --- | ---: |
| Retained source records | 6,490 |
| Omitted retained records | 0 |
| Duplicated retained records | 0 |
| Reordered retained records | 0 |

There is no table-of-contents page in the current Muret regulation. The config nevertheless makes TOC page recognition explicit: retained TOC text remains an auditable `OTHER` section, while topic retrieval from configured TOC pages is disabled unless explicitly enabled.

Section IDs are required to be exactly sequential in source order. Pages must be strictly ascending and agree with record boundaries. Each of the 177 `ARTICLE` rows has an earlier `ZONE_CHAPTER` parent with the same canonical label and non-empty number/title; all 13 zone chapters, five general articles, and one cover section satisfy their type-specific null/parent rules. The section totals remain unchanged at 196.

### Complete input and result integrity

Canonical UTF-8 JSON hashes now bind every source used by this step:

- Config schema / SHA256: 1 / `8b324fb6b01486ed82c0660257b401622f7217b4bc95b7ed1e85ae2275a82a8b`
- Ordered zone-input SHA256: `f9bfcd9d225c4dec964b3b17bf701323e0bc1873a3ad4483b983fc351f189b21`
- Ordered zoning-intersection SHA256: `f9c2b7a13d5d7c57e250e38ac0286d515f979c0e50cba54b8c2efe90e7e8ce91`
- Retained source-record SHA256: `5507ec145593dc40d620515304062e2d052658bf89302fce0f95e520a56fdfdb`
- Ordered sections SHA256: `21b73d967c11ef138ad370642196a2c7512fd1ff49b5e1459cbad6d9656920ad`
- Ordered zone-map SHA256: `b4bac92e5b97c3470d55d4744df0d6c494e2375d278efe46463617c6ec121ebd`
- Ordered topic-evidence SHA256: `31bda1efafb75d4e48f42d560de66db8eb8dafe88d2f4aa233444d56c965b158`
- Complete structure-result SHA256: `d3c7759a56cc38769362fc3c68a81524e5eea992ebd37c05daab7a4b4aaa9200`

Zone identity is now cross-checked through both `planning_zone_id` and authoritative `source_zone_id`, plus raw label and document/archive lineage. When metric denominators are present, intersection area cannot exceed parcel or zone area beyond the existing `1e-6 m²` technical geometry tolerance. Counts are rebuilt from the 221-zone catalog and 5,095 relations. Mapping semantics remain 12 `EXACT`, 17 `CONFIG_ALIAS`, 0 `UNMAPPED`, and 0 `AMBIGUOUS`; all 3,638 candidates remain represented and dominant unresolved candidates remain zero.

### Corrected literal topic evidence

The configured policy is `boundary_mode: token` plus `overlap_resolution: longest_match`. Matches must have token boundaries. Within one topic/section/page, all candidate spans are compared; the longest overlapping term wins, configuration order breaks an equal-length tie, and each retained source span is counted once. This corrects duplicate counting from singular/plural pairs and nested phrases such as `risque`/`risques`, `réseau`/`réseaux`, `intérêt collectif` inside `équipement d'intérêt collectif`, and `incendie` inside `défense contre l'incendie`. It is still literal retrieval: no stemming, synonyms, fuzzy match, LLM, or legal interpretation is used.

Evidence rows now retain the match-policy identifier and first normalized/raw span boundaries. Validators reconstruct matches and contexts from retained source text and require exact topic, configured term, section/page, zone/article, scope, count, provenance, raw context, and normalized context.

| Topic | Corrected rows | Unique retained occurrences |
| --- | ---: | ---: |
| `access` | 57 | 174 |
| `classified_installation` | 17 | 20 |
| `destination_and_use` | 29 | 30 |
| `electricity` | 34 | 35 |
| `energy` | 12 | 22 |
| `fire_safety` | 31 | 37 |
| `networks` | 50 | 177 |
| `nuisance` | 11 | 11 |
| `public_interest_equipment` | 25 | 25 |
| `risk` | 46 | 58 |
| `setbacks` | 130 | 183 |
| `technical_equipment` | 16 | 27 |
| **Total** | **458** | **799** |

The former 510 evidence rows and 984 literal occurrences included overlapping configured terms. The new 458 rows and 799 unique retained occurrences are a retrieval-integrity correction; source text, the 196 sections, zone aliases, and parcel/zone facts did not change.

### Outputs and read-back

- Real source-complete structure runtime: 8.975 seconds
- `muret_plu_regulation_sections.parquet`: 196 rows, 299,138 bytes
- `muret_plu_zone_section_map.parquet`: 29 rows, 11,117 bytes
- `muret_plu_topic_evidence.parquet`: 458 rows, 59,411 bytes
- `muret_plu_structure_index.json`: manifest schema 2, 3,185 bytes

The manifest now persists config schema/hash, both factual input hashes, source-record hash/counts, all result component hashes, complete result hash, match policy, and output counts. All four ignored outputs were rewritten and read back. The source-complete public validator rebuilt the result from the original real index, zones, intersections, and YAML config and accepted the persisted frames with identical hashes.

No legal conclusion.
No BESS compatibility status.
No parcel rejection.
No score.

## STEP 7D.4B.2 — Finalize structure schema and deterministic edge handling

- Status: Complete
- Implementation summary: Versioned the incompatible factual-structure grammar and hash format, made topic ordering independent of YAML mapping order, preserved blank-only source prefixes, isolated explicitly configured table-of-contents blocks at any document position, reused the shared planning-overlay tolerance, and made the table-of-contents evidence flag a strict boolean. Parsing, aliases, factual topic terms, and the real Muret hierarchy remain unchanged.
- Important files: `configs/planning/muret_plu_structure.yaml`, `src/landscout/stages/structure_planning_regulation.py`, `tests/unit/test_structure_planning_regulation.py`, and the four ignored structure outputs under `data/processed/planning/`.
- Tests/checks: 86 focused structure tests cover the v2 contracts and deterministic edge cases. The complete 956-test suite passes; repository-wide Ruff and `mypy src` checks pass.

### Versioned and deterministic contracts

The configuration schema is now version 2 and the section/source-record/component/result hash schema is version 2. Schema 1 is not migrated or interpreted under the new rules, and unknown schema versions fail explicitly. The outer ignored output manifest is version 3 and records both supported versions. The new schema version is bound into the complete source-record hash, every per-section hash, all ordered component hashes, and the complete result hash.

Topic names are processed in canonical ascending order. Reordering only the YAML topic keys produces the same config hash, row order, component hashes, and complete result hash. Configured term order inside a topic is deliberately preserved: it remains the final deterministic tie-breaker when equal-length literal spans overlap.

`include_table_of_contents_in_topic_evidence` now accepts only actual YAML/Python booleans; numeric and string lookalikes are rejected. Blank-only records before the first heading attach to that first factual section while leaving its real heading unchanged. Each contiguous configured table-of-contents page block becomes a separate factual `OTHER` section wherever it occurs, remains in the exact one-time source-record partition, and is included in topic retrieval only when the strict option is true. The current Muret config identifies no table-of-contents pages, so its real section hierarchy is unchanged.

Area upper-bound validation now calls the same `technical_overlay_tolerance(reference)` helper used by the factual zoning and planning-feature overlays. Its absolute/relative floating-point guard is a shared technical geometry tolerance, not a planning rule or business threshold.

### Real Muret regression

| Factual result | Count |
| --- | ---: |
| Retained source records | 6,490 |
| Omitted records | 0 |
| Duplicated records | 0 |
| Reordered records | 0 |
| Sections | 196 |
| `OTHER` sections | 1 |
| General sections | 5 |
| Zone chapters | 13 |
| Articles | 177 |
| Zone-map rows | 29 |
| `EXACT` mappings | 12 |
| `CONFIG_ALIAS` mappings | 17 |
| `UNMAPPED` mappings | 0 |
| `AMBIGUOUS` mappings | 0 |
| Dominant unresolved candidates | 0 |
| Topic-evidence rows | 458 |
| Unique retained topic occurrences | 799 |

The corrected per-topic evidence counts remain exactly those recorded in STEP 7D.4B.1. The factual frames are unchanged; the integrity hashes legitimately changed because both the config and structure/hash schemas changed:

- Config schema / SHA256: 2 / `13d028fe4b58d30929ff9fdedae90e2cc95983a3296f2f83c2817d0da381107a`
- Section/hash schema: 2
- Retained source-record SHA256: `c031c2a9157ff6cf3ae5fea1a63d3ab1c7b4137d6fadd742addf0d5ca9415ecb`
- Ordered sections SHA256: `7485fa0423dd8ffaf5066dae7cb2047743e5837afeaf6a3561fc35642031323a`
- Ordered zone-map SHA256: `140de4dbd097ffa00252333348d81d265493180b204fac20a56702df2c2268a3`
- Ordered topic-evidence SHA256: `a79e449f3318425822ea2d89a710577e323b26bc1c585965c3cf5c02373c597c`
- Complete structure-result SHA256: `56db5da3923f0e6405a256e9a1de5f6ba262d4575fd0921b126d8df4e558502d`
- Real source-complete structure runtime: 8.844 seconds

### Outputs and read-back

- `muret_plu_regulation_sections.parquet`: 196 rows, 298,888 bytes
- `muret_plu_zone_section_map.parquet`: 29 rows, 11,117 bytes
- `muret_plu_topic_evidence.parquet`: 458 rows, 59,064 bytes
- `muret_plu_structure_index.json`: manifest schema 3, 3,184 bytes

All four ignored artifacts were rewritten. The immutable result was reconstructed from the three persisted Parquet tables and the schema-v3 manifest, then accepted by the source-complete public validator using the original validated page index, 221-zone catalog, 5,095 parcel/zone relations, and schema-v2 YAML configuration.

No legal conclusion.
No BESS compatibility status.
No parcel rejection.
No score.

## STEP 7D.4B.3 — Finalize factual structure edge integrity

- Status: Complete
- Implementation summary: Closed the final factual structure edges by deriving evidence scope from section type, preserving blank-only configured TOC blocks, retaining ordinary blank gaps and document tails deterministically, validating every configured layout page against the indexed document, and binding every intersection metric actually used by the stage into the source-complete result envelope.
- Important files: `src/landscout/stages/structure_planning_regulation.py`, `tests/unit/test_structure_planning_regulation.py`, and the four ignored structure outputs under `data/processed/planning/`.
- Tests/checks: 105 focused structure tests cover the schema-v3, page-layout, evidence-scope, blank-partition, and optional-metric hash contracts. The complete 975-test suite passes; repository-wide Ruff and `mypy src` checks pass.

### Scope, page, and source-record fidelity

Evidence scope now describes exact factual location: `GENERAL` maps to `GENERAL_RULE`; `ZONE_CHAPTER` and `ARTICLE` map to `ZONE_SPECIFIC_RULE`; and cover, preamble, or configured table-of-contents `OTHER` sections map to `OTHER_TEXT`. The current Muret cover has no configured topic hit, so its real evidence remains 13 `GENERAL_RULE` rows and 445 `ZONE_SPECIFIC_RULE` rows; no current row required an `OTHER_TEXT` value.

Forced TOC boundaries are now distinct from ordinary blank-gap boundaries. A configured TOC block made only of retained whitespace remains a separate `OTHER` section with its exact blank records and an empty factual heading; no heading is invented. Several contiguous TOC pages remain one block. Ordinary blank records before a later real heading attach to that following section, while a blank tail at the end of the document remains attached to the preceding factual section. A TOC block followed only by blank tail records remains the preceding factual TOC `OTHER` section. All cases retain exact order with no omitted or duplicated source record.

After validating the regulation index, the stage now requires `body_start_page` and every configured TOC page to reference a real indexed page. Page zero, a page above the page count, and any nonexistent indexed page fail with a controlled structure error. A real indexed `EMPTY` page remains a valid page reference even though it has no topic evidence and may contain no retained line records.

### Complete intersection-input lineage

The real ordered intersection hash columns are persisted as:

```text
parcel_id
planning_zone_id
source_zone_id
zone_label_raw
relation_type
intersection_area_m2
source_document_id
source_archive_sha256
parcel_metric_area_m2
zone_area_m2
```

The first eight columns are always required. The two metric upper bounds are appended in that fixed order only when present. This exact list is bound into the intersection-input hash, every component hash, the complete result hash, and the manifest. A still-geometrically-valid change to either optional metric invalidates the prior result instead of passing under a hash that omitted a used input.

The configuration remains schema 2 because its YAML shape is unchanged. The changed evidence vocabulary and source-input semantics use section/hash schema 3; schema versions 1 and 2 are rejected. The ignored structure manifest is schema 4.

### Real Muret regression and read-back

| Factual result | Count |
| --- | ---: |
| Retained source records | 6,490 |
| Omitted / duplicated / reordered records | 0 / 0 / 0 |
| Sections | 196 |
| `OTHER` / `GENERAL` / `ZONE_CHAPTER` / `ARTICLE` | 1 / 5 / 13 / 177 |
| `EXACT` / `CONFIG_ALIAS` mappings | 12 / 17 |
| `UNMAPPED` / `AMBIGUOUS` mappings | 0 / 0 |
| Dominant unresolved candidates | 0 |
| Topic-evidence rows | 458 |
| Unique retained topic occurrences | 799 |
| `GENERAL_RULE` / `ZONE_SPECIFIC_RULE` / `OTHER_TEXT` rows | 13 / 445 / 0 |

- Config schema / SHA256: 2 / `13d028fe4b58d30929ff9fdedae90e2cc95983a3296f2f83c2817d0da381107a`
- Section/hash schema: 3
- Intersection-input SHA256: `0ab84c4c2832a41901b9392e0ed1b91aa33c6e7cacf639bc4c39196f2597ebe2`
- Retained source-record SHA256: `2e931b945484ff07728ad4d64a3c9c358809f72c30c60144dba03eb342a41517`
- Ordered sections SHA256: `cad93569d2cf75b9560d7bfcbf0fcc0b8896b49a2f5357572c88344a3f5e9b64`
- Ordered zone-map SHA256: `0f39c06ffddc9c7bf0a81e6eac963a9e1247ee0ff478f6be8a2f8e7324172605`
- Ordered topic-evidence SHA256: `67acf8dbb4010a4702f84be148f3e93973c0d537f7d1c1a73f46cd7138a6452a`
- Complete structure-result SHA256: `16f8a9edfff0d330f69579310da085f804f4641de973d98e0046bff5ea96b03c`
- Real source-complete runtime: 8.864 seconds
- `muret_plu_regulation_sections.parquet`: 196 rows, 299,178 bytes
- `muret_plu_zone_section_map.parquet`: 29 rows, 11,117 bytes
- `muret_plu_topic_evidence.parquet`: 458 rows, 59,071 bytes
- `muret_plu_structure_index.json`: manifest schema 4, 3,577 bytes

All ignored outputs were rewritten. The immutable schema-v3 result was reconstructed from the three Parquet tables and manifest, including the ordered intersection hash-column tuple, then accepted by the source-complete public validator using the original validated regulation index, zone catalog, 5,095 zoning intersections, and schema-v2 configuration.

No legal conclusion.
No BESS compatibility status.
No parcel rejection.
No score.

## STEP 7D.4B.4 — Reject ambiguous structural heading matches

- Status: Complete
- Implementation summary: Replaced structural first-pattern precedence with one ambiguity-aware classifier that evaluates every configured zone-chapter, general-section, and article pattern for each retained source line. Zero matches remain factual body text, exactly one match creates a heading event, and every multiple match fails with `PlanningRegulationStructureError`.
- Important files: `src/landscout/stages/structure_planning_regulation.py` and `tests/unit/test_structure_planning_regulation.py`.
- Tests/checks: 114 focused structure tests cover unique headings, non-heading text, within-group and cross-category ambiguity, duplicate cross-group regex configuration, ambiguous continuation candidates, source-complete rebuilding under changed grammar, and deterministic normal parsing. The complete 984-test suite passes; repository-wide Ruff and `mypy src` checks pass.

### Heading ambiguity contract

The parser no longer assigns priority by either pattern order or structural category. It evaluates all configured structural regular expressions with the existing exact `fullmatch` semantics. Two distinct patterns in the same group are ambiguous even when their named captures agree; overlaps between `ZONE_CHAPTER`, `GENERAL`, and `ARTICLE` are equally ambiguous. Reusing an identical regex string across structural groups is rejected while loading the configuration, while runtime classification remains necessary for distinct expressions whose accepted languages overlap.

Controlled runtime diagnostics identify the retained record ID, indexed page number, page line number, matching categories, and zero-based pattern indexes. They deliberately omit source text because an unbroken extracted record could contain a complete PDF page. Continuation collection uses this same classifier: one structural match ends the preceding continued heading, while multiple matches fail instead of becoming a silent continuation boundary.

The existing Muret schema-v2 grammar required no YAML change. All 195 structural heading records were uniquely classified: 13 zone chapters, 5 general sections, and 177 articles; ambiguous heading records were 0.

### Real Muret regression and read-back

The live source-complete rebuild took 8.860 seconds and remained identical to the persisted schema-v3 result:

| Factual result | Count |
| --- | ---: |
| Retained source records | 6,490 |
| Sections | 196 |
| `OTHER` / `GENERAL` / `ZONE_CHAPTER` / `ARTICLE` | 1 / 5 / 13 / 177 |
| `EXACT` / `CONFIG_ALIAS` mappings | 12 / 17 |
| `UNMAPPED` / `AMBIGUOUS` mappings | 0 / 0 |
| Topic-evidence rows | 458 |
| Unique retained topic occurrences | 799 |

No output schema or factual row changed, so the ignored processed artifacts were not rewritten. The existing Parquet tables and schema-v4 manifest were read back, reconstructed into the immutable result, and accepted by the public source-complete validator using the original validated page index, 221-zone catalog, 5,095 zoning intersections, and current schema-v2 configuration.

All component and envelope hashes remain unchanged:

- Config: `13d028fe4b58d30929ff9fdedae90e2cc95983a3296f2f83c2817d0da381107a`
- Zones: `f9bfcd9d225c4dec964b3b17bf701323e0bc1873a3ad4483b983fc351f189b21`
- Intersections: `0ab84c4c2832a41901b9392e0ed1b91aa33c6e7cacf639bc4c39196f2597ebe2`
- Source records: `2e931b945484ff07728ad4d64a3c9c358809f72c30c60144dba03eb342a41517`
- Sections: `cad93569d2cf75b9560d7bfcbf0fcc0b8896b49a2f5357572c88344a3f5e9b64`
- Zone map: `0f39c06ffddc9c7bf0a81e6eac963a9e1247ee0ff478f6be8a2f8e7324172605`
- Topic evidence: `67acf8dbb4010a4702f84be148f3e93973c0d537f7d1c1a73f46cd7138a6452a`
- Complete result: `16f8a9edfff0d330f69579310da085f804f4641de973d98e0046bff5ea96b03c`

No legal conclusion.
No BESS compatibility status.
No parcel rejection.
No score.

## STEP 7D.4C — Evidence-backed BESS zoning precheck

- Status: Complete
- Implementation summary: Added a strict, checked-in, source-locked YAML policy and a source-complete interpretation stage that converts only validated written-zoning evidence into conservative chapter, raw-zone, parcel/zone, and parcel-level precheck facts. No runtime LLM, semantic classifier, fuzzy inheritance, or parcel filtering is used.
- Important files: `configs/planning/muret_bess_zoning_policy.yaml`, `src/landscout/stages/interpret_bess_zoning.py`, `tests/unit/test_interpret_bess_zoning.py`, and the five ignored precheck outputs under `data/processed/planning/`.
- Tests/checks: 36 focused offline tests cover source locks, strict YAML and duplicate keys, policy completeness, exact evidence excerpts, contradictory-direction rejection, status/evidence prerequisites, exact and configured-alias inheritance, independently recomputed factual mapping counters, mixed-zone aggregation, touch-only handling, input immutability, coordinated mutations, and persisted read-back. The complete 1,020-test suite passes; repository-wide Ruff and `mypy src` checks pass.

### Scope and policy semantics

Every output carries:

```text
planning_precheck_scope = WRITTEN_ZONING_REGULATION_ONLY
```

The stage does not interpret `TYPEPSC`, `STYPEPSC`, `TYPEINF`, or `STYPEINF`. Existing prescription/information relation counts remain unchanged, and every parcel explicitly records `non_zoning_planning_features_interpreted = false`. It also does not interpret environmental constraints, permit procedure, grid capacity, or project design.

The policy locks document ID, archive SHA256, PDF SHA256, complete index SHA256, complete factual-structure SHA256, structure profile, and policy schema. It contains exactly one entry for each of the 13 resolved regulation chapters. The source mapping is the only inheritance path: 12 raw labels use `EXACT`, 17 use `CONFIG_ALIAS`, and no label is inferred from a prefix.

The current regulation contains no explicit occurrence of `batterie` and does not classify an electricity-storage installation as one of its planning-use categories. Accordingly, the checked-in policy does not use absence of a prohibition as positive evidence. Each chapter remains `CONDITIONAL_REVIEW / LOW`: the cited text provides an explicit conditional category route or exception, but formal review must determine whether the actual BESS design belongs to that category and meets every condition.

| Chapter | Section / page | Factual evidence used | Status / confidence |
| --- | --- | --- | --- |
| UA | `SECTION-0009` / 8 | Conditional ICPE rule | `CONDITIONAL_REVIEW` / `LOW` |
| UB | `SECTION-0022` / 22 | Conditional ICPE rule | `CONDITIONAL_REVIEW` / `LOW` |
| UC | `SECTION-0037` / 36 | Conditional ICPE rule | `CONDITIONAL_REVIEW` / `LOW` |
| UD | `SECTION-0052` / 48 | Conditional ICPE rule | `CONDITIONAL_REVIEW` / `LOW` |
| UF | `SECTION-0066` / 60 | Conditional ICPE rule | `CONDITIONAL_REVIEW` / `LOW` |
| UP | `SECTION-0080` / 71 | Public/collective-interest equipment exception | `CONDITIONAL_REVIEW` / `LOW` |
| AU | `SECTION-0096` / 81 | Access, road, and network prerequisites | `CONDITIONAL_REVIEW` / `LOW` |
| AUp | `SECTION-0111` / 93 | Access, road, and network prerequisites | `CONDITIONAL_REVIEW` / `LOW` |
| AUf | `SECTION-0126` / 102 | Road and network prerequisites | `CONDITIONAL_REVIEW` / `LOW` |
| AU0 | `SECTION-0141` / 114 | Prior PLU-modification requirement | `CONDITIONAL_REVIEW` / `LOW` |
| AUf0 | `SECTION-0156` / 120 | Prior PLU-modification requirement | `CONDITIONAL_REVIEW` / `LOW` |
| A | `SECTION-0170` / 125 | Broad restriction with technical-infrastructure exception | `CONDITIONAL_REVIEW` / `LOW` |
| N | `SECTION-0184` / 135 | Technical-infrastructure/public-service exceptions | `CONDITIONAL_REVIEW` / `LOW` |

All 13 excerpts are exact source substrings, 600 characters or fewer, with individual SHA256 values. Interpretation is confined to separate `interpretation_note`, `rationale`, and `missing_information` fields. Evidence directions are all `CONDITION`: ICPE rule 5, public-interest exception 1, access/network condition 3, other relevant rule 2, and technical-equipment rule 2. All 13 chapters lack explicit BESS wording.

### Integrity and parcel aggregation

The stage independently revalidates the factual structure component hashes, per-section hashes, and complete envelope. It also recomputes the exact zone and intersection input hashes used by STEP 7D.4B before applying policy. The public validator receives the index, factual structure, zone catalog, zoning relations, complete STEP 7D.3 parcel frame, policy, and result; it rebuilds all four outputs and compares every row, scalar, lineage field, and hash.

Positive-area zones alone control parcel aggregation. One status across all positive zones is retained; differing statuses would produce `MIXED_REVIEW_REQUIRED`; no positive-area zone produces `UNKNOWN`. The dominant zone is retained as a separate factual view and never suppresses a non-dominant conflict. `TOUCH_ONLY` remains counted but cannot control status. No geometric area threshold is introduced.

### Real Muret regression

| Result | Count |
| --- | ---: |
| Input/output parcels | 3,638 / 3,638 |
| Chapter policies | 13 |
| Raw-zone policies | 29 |
| Positive parcel/zone policy relations | 5,095 |
| Factual touch-only relations | 0 |
| `CONDITIONAL_REVIEW` chapters / raw labels / parcels | 13 / 29 / 3,638 |
| `MIXED_REVIEW_REQUIRED` parcels | 0 |
| `UNKNOWN` parcels | 0 |
| Lost / extra parcel IDs | 0 / 0 |

- Policy SHA256: `201bbd8e0a8538f0ecc8ed077290e41f25b2c57723721d69183ab31d0b0be153`
- Factual structure input SHA256: `e407cb12ef6e2d051dd1929d1dcd56cb3599ea04ece4d92fb036fd73f4405a09`
- Zone-mapping input SHA256: `718d4721d54a76b8a28d152ba6535b3c948e606b3c4fc8d9f4fe9742c8e99453`
- Parcel/zoning relation input SHA256: `547614f20eba5ba493d50c0162e498ffa0e7345cce65eb072537f0caf7e7a94b`
- Chapter/source-zone/parcel-zone hashes: `d77b74d0412fa1772a64cc46f5dc2af7cb457d9ca4823538c3fe5092ead65d6e` / `1447db9885e2c7a9ff3c0399416c442aa9c3bed8be504af9b99b3edad6f56cf5` / `40a88adb1e137d61bfcdd8d991a6b6e897ede86822ab319119c6e034dca236fa`
- Parcel-output SHA256: `2213be8c264fba06cbb6db16041125c985781122bf0522951c47c093b380c498`
- Complete result SHA256: `a51146520780e4e4e3b2c8ee89e47230c4164e438ca13a9edc3a3167222cff06`
- Source-complete runtime: 13.677 seconds

### Outputs and read-back

- `muret_bess_zoning_chapter_policy.parquet`: 13 rows, 15,973 bytes
- `muret_bess_zoning_source_policy.parquet`: 29 rows, 13,391 bytes
- `muret_bess_zoning_policy_relations.parquet`: 5,095 rows, 134,757 bytes
- `muret_bess_zoning_precheck.parquet`: 3,638 rows, 1,585,871 bytes; GeoParquet in the original parcel CRS
- `muret_bess_zoning_precheck.json`: manifest schema 1, 3,283 bytes

All files were read back. The immutable result was reconstructed from the four persisted Parquet outputs and JSON manifest, then accepted by the public source-complete validator with the original validated inputs. Parcel IDs/order/index, all prior fields, geometry, and CRS were unchanged.

This is a conservative LandScout preliminary screening status.

It is not an authorization, permit decision or legal opinion.

Formal review of the complete planning document, prescriptions, servitudes and project design remains required.

No parcel is rejected in this step.

## STEP 7D.2 — Normalize GPU zoning and intersect Muret parcels

- Status: Complete
- Implementation summary: Added one high-level factual zoning stage that validates the loaded GPU bundle, normalizes the authoritative zoning catalog to EPSG:2154, uses a spatial index plus vectorized full-polygon intersections, and returns copied parcel, zone, and long-form relation frames. It does not interpret zoning or reject parcels.
- Important files: `src/landscout/stages/enrich_planning_zoning.py`, `tests/unit/test_enrich_planning_zoning.py`, `src/landscout/stages/__init__.py`
- Tests/checks: 66 focused offline zoning tests pass. The full suite passes with 675 tests; Ruff and mypy pass.
- Important decisions: `LIB_IDZONE` is the authoritative source identity and becomes `GPU:<document_id>:ZONE:<LIB_IDZONE>`. Raw GPU values are copied exactly. `IDURBA` must equal the logical archive identity derived from the loaded document. Metric work uses planar EPSG:2154 geometry; parcel storage geometry and CRS remain unchanged. `AREA_OVERLAP` means strictly positive measured intersection area, while zero-area intersections remain explicit `TOUCH_ONLY` relations. Dominance uses the greatest positive intersection area and lexical `planning_zone_id` for an exact tie.
- Known issues: The current result describes source zoning geometry only; prescription layers and written regulation are not interpreted. A `1e-6 m²` technical comparison tolerance guards floating-point area invariants. Positive residues below that tolerance are reported separately and are not treated as material source overlap.

### Real inputs and lineage

| Item | Observed value |
| --- | --- |
| Parcel input | `data/processed/grid/muret_bess_grid_proximity_coverage.parquet` |
| Parcel count | 3,638 |
| Parcel CRS | `EPSG:4326` |
| GPU zoning zones | 221 |
| Source zoning CRS | `IGNF:LAMB93` |
| Normalized/calculation CRS | `EPSG:2154` |
| Source layer | `31395_ZONE_URBA_20240215` |
| Document ID | `33edb4c9f6943c88d8d92518bff20bec` |
| Document type | `PLU` |
| Archive | `31395_PLU_20240215` |
| Archive SHA256 | `9d6677cd6634b56b712311042f0cc714d5ca42a38f82a417b27dd473255d7d93` |
| Standard model | `CNIG PLU v2017` |

All 221 source geometries remain valid polygons. The normalized zone catalog has 221 unique `planning_zone_id` values and retains the exact source `TYPEZONE`, `LIBELLE`, `LIBELONG`, `NOMFIC`, `URLFIC`, `IDURBA`, and `DATVALID` values.

### Integrity and performance

- Input/output parcels: 3,638 / 3,638
- Lost / extra parcel IDs: 0 / 0
- Duplicate normalized zone IDs: 0
- Duplicate parcel/zone pairs: 0
- Invalid or non-finite calculations: 0
- Original parcel order, WKB geometry, all prior grid fields, and `EPSG:4326` CRS: preserved
- Normalized zone CRS: canonical `EPSG:2154`
- Real intersection wall-clock duration: 2.104 seconds

The raw intersection sum and covered-union area are recorded separately. Coverage and gap use the covered union, while overlap excess is the raw sum minus that union. No area was calculated in EPSG:4326.

### Factual zoning results

- Parcel/zone relation rows: 5,095
- `AREA_OVERLAP`: 5,095
- `TOUCH_ONLY`: 0 (the relation remains covered by synthetic tests)
- Parcels with 0 / 1 / multiple positive-area zones: 0 / 2,324 / 1,314
- Detailed positive-area zone counts: 1 zone = 2,324; 2 = 1,178; 3 = 129; 4 = 7
- Zoning coverage min / p50 / max: 99.983493067% / 100% / 100%
- Zoning gap min / p50 / max: 0 / 0 / 0.684117101 m²
- Parcels with material source-overlap excess above `1e-6 m²`: 0
- Positive floating-point overlap residues: 1,587; maximum `4.82542e-08 m²`, all below the technical tolerance

Dominant raw `TYPEZONE` counts:

| Raw `TYPEZONE` | Parcels |
| --- | ---: |
| `A` | 1,946 |
| `AUc` | 134 |
| `AUs` | 105 |
| `N` | 398 |
| `U` | 1,055 |

Dominant raw `LIBELLE` counts:

| Raw labels | Parcel counts |
| --- | --- |
| `A`; `AU`; `AU0`; `AUa`; `AUf` | 1,946; 4; 42; 2; 20 |
| `AUfa`; `AUfb`; `AUfc`; `AUfd`; `AUfo`; `AUp` | 29; 29; 23; 19; 63; 8 |
| `N`; `NL`; `Ne`; `Nh`; `Nr` | 127; 30; 2; 124; 115 |
| `UA`; `UAa`; `UAb`; `UB`; `UBa`; `UBb` | 3; 19; 2; 53; 19; 9 |
| `UC`; `UD`; `UF`; `UFc`; `UFd`; `UP` | 266; 447; 148; 7; 4; 78 |

Ten deterministic representative multi-zone parcels, ordered by descending zone count then `parcel_id`:

| Parcel | Area (m²) | Zones | Dominant `TYPEZONE` | Dominant `LIBELLE` | Dominant share | Coverage |
| --- | ---: | ---: | --- | --- | ---: | ---: |
| `31395000AS0325` | 4,061.821 | 4 | `U` | `UBb` | 93.997295% | 100.000000% |
| `31395000CH0151` | 8,646.473 | 4 | `A` | `A` | 84.720485% | 100.000000% |
| `31395000CM0028` | 8,821.617 | 4 | `A` | `A` | 92.086894% | 100.000000% |
| `31395000CR0007` | 10,844.189 | 4 | `U` | `UD` | 62.837576% | 100.000000% |
| `31395000CY0006` | 2,616.574 | 4 | `U` | `UD` | 99.998189% | 100.000000% |
| `31395000CY0207` | 2,266.731 | 4 | `U` | `UC` | 92.344287% | 100.000000% |
| `31395000IE0287` | 3,484.755 | 4 | `U` | `UB` | 60.839179% | 100.000000% |
| `313950000A0392` | 5,821.807 | 3 | `A` | `A` | 94.977689% | 100.000000% |
| `313950000K0012` | 2,623.994 | 3 | `A` | `A` | 99.996608% | 100.000000% |
| `313950000K0013` | 2,369.380 | 3 | `N` | `Nh` | 99.962334% | 100.000000% |

### Outputs and read-back

- Zone GeoParquet: `data/processed/planning/muret_gpu_zones.parquet` (221 rows, 306,703 bytes, `EPSG:2154`)
- Parcel GeoParquet: `data/processed/planning/muret_bess_zoning.parquet` (3,638 rows, 1,440,942 bytes, `EPSG:4326`)
- Relation Parquet: `data/processed/planning/muret_bess_zoning_intersections.parquet` (5,095 rows, 224,907 bytes)
- Read-back verified exact parcel IDs/order and WKB geometry, both CRSs, unique zone IDs and parcel/zone pairs, source lineage, unchanged raw vocabulary, relation types, and finite non-negative areas and percentages.

Generated outputs remain ignored by Git.

GPU zoning is an official source fact.

Dominant zone means the source zone covering the largest measured part of the parcel. It does not mean the only legally relevant zone.

No zoning value is interpreted as BESS-compatible or BESS-incompatible in STEP 7D.2.

No parcel is rejected.

## STEP 7D.3 — Normalize and intersect GPU planning features

- Status: Complete
- Implementation summary: Added one factual high-level stage for GPU prescription and information layers. It validates the immutable source bundle, normalizes surface/line/point catalogs to EPSG:2154, generates candidate relations through spatial indexing, and applies vectorized geometry-specific measurements. Existing cadastre, shape, grid, coverage, and zoning parcel facts remain unchanged.
- Important files: `src/landscout/stages/enrich_planning_features.py`, `tests/unit/test_enrich_planning_features.py`, `src/landscout/stages/__init__.py`
- Tests/checks: 47 focused offline tests pass. The full suite passes with 722 tests; Ruff and mypy pass.
- Important decisions: Raw codes and text are preserved without interpretation. Surface relations use positive area versus zero-area touch; line relations use positive in-parcel length versus zero-length touch; point relations distinguish interior members from boundary members. Surface coverage is calculated from a union so overlapping source features are not double-counted. The same `1e-6 m²` technical area-comparison tolerance established in STEP 7D.2 is reused and is not a planning threshold.
- Known issues: The official prescription-surface Shapefile omits `LIB_IDPSC`. For that layer only, LandScout reopens the immutable archive-derived Shapefile, validates row attributes/geometries against the inspected frame, and uses namespaced, archive-and-layer-scoped OGR FIDs such as `OGR_FID:0`; an OGR FID is not an official CNIG attribute identity and is stable only with that immutable archive/layer lineage. It never uses the mutable GeoDataFrame index. The current document contains no information-line or information-point layer.

### Real schemas and source identities

| Logical layer | Source layer | Features | Source CRS | Geometry | Source identity mechanism |
| --- | --- | ---: | --- | --- | --- |
| `prescription_surface` | `31395_PRESCRIPTION_SURF_20240215` | 320 | `IGNF:LAMB93` | Polygon 320 | `ARCHIVE_SCOPED_OGR_FID` / `OGR_FID` because the DBF omits `LIB_IDPSC`; not a CNIG identity |
| `prescription_line` | `31395_PRESCRIPTION_LIN_20240215` | 5 | `EPSG:2154` | LineString 5 | `LIB_IDPSC` |
| `prescription_point` | `31395_PRESCRIPTION_PCT_20240215` | 5 | `EPSG:2154` | Point 5 | `LIB_IDPSC` |
| `information_surface` | `31395_INFO_SURF_20240215` | 149 | `IGNF:LAMB93` | Polygon 148, MultiPolygon 1 | `LIB_IDINFO` |
| `information_line` | absent | 0 | — | — | — |
| `information_point` | absent | 0 | — | — | — |

Exact prescription-surface fields:

```text
LIBELLE, TXT, TYPEPSC, STYPEPSC, NOMFIC, URLFIC, IDURBA, DATVALID, geometry
```

Exact prescription-line and prescription-point fields:

```text
LIBELLE, TXT, TYPEPSC, STYPEPSC, NOMFIC, URLFIC, IDURBA, DATVALID, LIB_IDPSC, geometry
```

Exact information-surface fields:

```text
LIBELLE, TXT, TYPEINF, STYPEINF, NOMFIC, URLFIC, IDURBA, DATVALID, LIB_IDINFO, geometry
```

All loaded geometries are non-null, non-empty, valid, and retained without repair. Every source `IDURBA` is `31395_PLU_20240215` and was validated against the loaded archive identity rather than a production constant. Document lineage remains:

- document ID: `33edb4c9f6943c88d8d92518bff20bec`;
- archive SHA256: `9d6677cd6634b56b712311042f0cc714d5ca42a38f82a417b27dd473255d7d93`;
- standard: `CNIG PLU v2017`;
- calculation and normalized catalog CRS: `EPSG:2154`.

### Raw source-code diagnostics

| Logical layer | Raw source code counts |
| --- | --- |
| Prescription surface | `TYPEPSC`: `01` 127, `05` 185, `07` 1, `17` 1, `18` 6; `STYPEPSC`: `00` 319, `04` 1 |
| Prescription line | `TYPEPSC`: `15` 5; `STYPEPSC`: `00` 4, `01` 1 |
| Prescription point | `TYPEPSC`: `07` 5; `STYPEPSC`: `00` 5 |
| Information surface | `TYPEINF`: `02` 1, `14` 3, `27` 4, `99` 141; `STYPEINF`: `00` 149 |

Parcel relation rows by raw logical layer/type/subtype:

| Logical layer and raw code | Relations |
| --- | ---: |
| Information surface `02/00` | 43 |
| Information surface `14/00` | 989 |
| Information surface `27/00` | 178 |
| Information surface `99/00` | 127 |
| Prescription surface `01/00` | 619 |
| Prescription surface `05/00` | 321 |
| Prescription surface `07/04` | 4 |
| Prescription surface `17/00` | 6 |
| Prescription surface `18/00` | 117 |
| Prescription line `15/00` | 8 |
| Prescription point `07/00` | 2 |

These counts are source and geometric facts only. They do not assign priority, severity, authorization, or prohibition.

### Real relations, metrics, and integrity

- Input/output parcels: 3,638 / 3,638
- Lost / extra parcel IDs: 0 / 0
- Normalized surface / line / point features: 469 / 5 / 5
- Total unique parcel/feature relations: 2,414
- Duplicate parcel/feature pairs: 0
- Relation types: `AREA_OVERLAP` 2,404; `LENGTH_OVERLAP` 8; `INSIDE` 2; `TOUCH_ONLY` 0; `BOUNDARY_TOUCH` 0
- Relations by layer: prescription surface 1,067; prescription line 8; prescription point 2; information surface 1,337
- Affected parcels by layer: prescription surface 975; prescription line 8; prescription point 2; information surface 1,261
- All-planning-surface covered percentage min / p50 / max: 0% / 0.000168550% / 100%
- Prescription-surface covered percentage min / p50 / max: 0% / 0% / 100%
- Information-surface covered percentage min / p50 / max: 0% / 0% / 100%
- In-parcel line-length sum among the 8 affected parcels, min / p50 / max: 15.341 m / 29.489 m / 96.601 m
- Point members inside / on parcel boundary: 2 / 0
- Non-finite or negative calculations: 0
- Real intersection wall-clock duration: 0.936 seconds

The parcel output retains exactly the original 3,638 IDs, order, RangeIndex, WKB geometry, `EPSG:4326` CRS, and every prior field. Catalog lineage, raw codes, relation references, and metric/summary consistency were verified after serialization.

### Outputs and read-back

| Output | Rows | Size | Semantics |
| --- | ---: | ---: | --- |
| `data/processed/planning/muret_gpu_surface_features.parquet` | 469 | 343,778 bytes | GeoParquet, `EPSG:2154` |
| `data/processed/planning/muret_gpu_line_features.parquet` | 5 | 29,168 bytes | GeoParquet, `EPSG:2154` |
| `data/processed/planning/muret_gpu_point_features.parquet` | 5 | 25,303 bytes | GeoParquet, `EPSG:2154` |
| `data/processed/planning/muret_bess_planning_features.parquet` | 3,638 | 1,551,346 bytes | GeoParquet, original `EPSG:4326` parcel geometry |
| `data/processed/planning/muret_bess_planning_feature_relations.parquet` | 2,414 | 132,166 bytes | regular long-form Parquet |

Read-back verified feature IDs, source lineage, raw codes, geometry types, catalog CRSs, parcel IDs/order/prior columns/WKB/CRS, unique relation pairs, known references, nullable geometry-specific metrics, and finite non-negative values. Generated files remain ignored by Git.

Prescription and information codes remain official GPU source facts.

Geometric intersection does not by itself prove that a prescription prohibits or authorizes a BESS project.

No parcel is rejected in STEP 7D.3.

No urban-planning score is calculated.

## STEP 7D.3.1 — Harden GPU planning-feature identity and result contracts

- Status: Complete
- Implementation summary: Kept the factual STEP 7D.3 spatial result unchanged while closing its trust boundaries. Present-but-empty optional related layers are valid inputs; feature and relation records carry explicit source-identity provenance; result validation cross-checks relations against catalogs and parcel summaries; geometry-specific semantics and strict count types are enforced; and geospatial failures become controlled `PlanningFeaturesError` exceptions with chained causes.
- Important files: `src/landscout/stages/enrich_planning_features.py`, `src/landscout/stages/enrich_planning_zoning.py`, `src/landscout/stages/planning_overlay.py`, `tests/unit/test_enrich_planning_features.py`, `tests/unit/test_enrich_planning_zoning.py`
- Tests/checks: 147 focused planning-feature/zoning tests and the complete 756-test suite pass. Ruff and mypy pass.
- Important decisions: `CNIG_ATTRIBUTE` identifies values from `LIB_IDPSC` or `LIB_IDINFO`. `ARCHIVE_SCOPED_OGR_FID` labels the prescription-surface fallback from `OGR_FID`; it is not a CNIG identity and is meaningful only with the namespaced document, logical layer, archive SHA256, and actual source layer. A zero-row prescription-surface layer does not reopen OGR merely to manufacture IDs. Both overlay stages use one shared `1e-6 m²` absolute / `1e-12` relative floating-point comparison tolerance; this is technical, not a planning or BESS threshold.
- Known issues: The current document has no information-line or information-point source layer. No source code is legally interpreted here.

### Strengthened contracts

- Every normalized feature and relation contains `source_identity_kind` and `source_identity_field`.
- Counts are finite, non-negative integers and reject booleans, strings, fractions, infinities, and negatives. Point covered-member counts cannot exceed source members.
- Surface, line, and point relation labels agree exactly with their area, length, and member metrics. Percentages are recomputed; line overlap cannot exceed source length beyond the shared technical tolerance.
- Relations are null-safely cross-validated against catalogs for ID/provenance, logical layer/family/kind, raw type/subtype/label/text, document/archive/layer lineage, validity date, regulation filename, and source geometry metric.
- `planning_feature_id` is globally unique across catalogs. Parcel counts, sums, family counts, covered-union bounds, and percentages are independently reconciled with relations and calculation geometries.
- GeoPandas joins and Shapely intersection, union, member, area, and length operations are wrapped with controlled errors and exception chaining.

### Real Muret regression and read-back

- Parcels: 3,638 input / 3,638 output; lost / extra IDs: 0 / 0.
- Features: 469 surface, 5 line, 5 point; duplicate global feature IDs: 0.
- Catalog identity provenance: `ARCHIVE_SCOPED_OGR_FID` 320; `CNIG_ATTRIBUTE` 159.
- Relations: 2,414; duplicate parcel/feature pairs: 0; `AREA_OVERLAP` 2,404, `LENGTH_OVERLAP` 8, `INSIDE` 2.
- Relation identity provenance: `ARCHIVE_SCOPED_OGR_FID` 1,067; `CNIG_ATTRIBUTE` 1,347.
- Wall-clock computation and strengthened validation: 7.289 seconds.

All five processed outputs were rewritten and read back through the hardened validator. IDs, provenance, lineage, raw facts, geometry, CRS, nullable metric schema, strict counts, relation semantics, and parcel summaries passed. Output sizes: surface 345,126 bytes; line 30,446; point 26,581; parcels 1,572,298; relations 134,375. Generated data remains ignored by Git.

Prescription and information codes remain official GPU source facts. An intersection does not itself prove authorization or prohibition.

No parcel is rejected in STEP 7D.3.1. No urban-planning score is calculated.

## STEP 7D.1.1 — Harden GPU source and extraction integrity

- Status: Complete
- Implementation summary: Closed every remaining GPU source trust boundary before parcel-to-zoning work. Current state is now revalidated across listing and details; document identity is checked against strict source configuration before cache or network access; archive names are treated as hostile metadata; immutable download size/SHA/format/filename are verified against real bytes before extraction; ZIP destinations are collision-checked; and extraction reuse requires a versioned per-file SHA256 manifest.
- Important files: `src/landscout/sources/gpu_fr.py`, `tests/unit/test_gpu_fr.py`
- Tests/checks: 93 focused offline GPU tests pass, including independent same-size modification, deletion, addition, and rename attacks against the extraction cache. Full suite: 609 passed; Ruff and mypy passed.
- Important decisions: The official ZIP remains the sole source of truth. A corrupt derived extraction is regenerated locally only after the ZIP object and bytes pass size, SHA256, filename, format, and full ZIP CRC validation. The raw GPU `archive_name` remains unchanged in lineage; only the local filename normalizes one optional case-insensitive `.zip` suffix to exactly one `.zip`.
- Known issues: None for this ticket. This integrity work does not interpret zoning or planning rules.

### Listing/details and document/config identity

The discovery listing still requires `document.production`, `APPROVED`, and `EN_VIGUEUR`. The selected details response must independently repeat those states and exactly match the listing document ID, raw archive name, requested commune, partition, and supplied document type. Any race or mismatch raises `GpuDiscoveryError`; it is never resolved by filename order or guesswork.

Before cache lookup or network access, the immutable document must match:

- configured provider and portal;
- configured five-digit pilot commune;
- the partition generated from that commune;
- the `DU` document family and current legal/effective state;
- the exact official GPU partition URL on `www.geoportail-urbanisme.gouv.fr` with no credentials, query, or fragment.

Cross-platform local archive naming rejects empty/dot/path/drive/control/edge-whitespace names, Windows device names, forbidden characters, trailing dot/space, repeated `.zip`, Unicode-normalized unsafe components, and oversized Windows components. No unsafe name is stripped into a different basename.

### Archive, ZIP-target, and extraction-manifest integrity

Every `GpuArchiveDownload` is revalidated before extraction:

- path is a regular non-link/non-junction file;
- real size equals immutable `file_size`;
- streaming SHA256 equals immutable `sha256`;
- format is `zip`;
- filename equals both `path.name` and the safe filename derived from source lineage;
- full ZIP integrity remains valid.

ZIP validation rejects exact duplicate names, normalized/case-insensitive Windows destination collisions, slash/backslash and dot-path equivalence, ancestor file/directory collisions, traversal, absolute/drive paths, controls, reserved names, links/special files, and any collision with LandScout's extraction manifest.

The former count-only marker was replaced by schema version 2:

```json
{
  "schema_version": 2,
  "archive_sha256": "<official cached archive SHA256>",
  "files": [
    {
      "relative_path": "<deterministically sorted source path>",
      "size_bytes": 123,
      "sha256": "<source-file SHA256>"
    }
  ]
}
```

The marker is not a source file. Cache reuse inventories the complete source tree and requires the exact same path set, size, and SHA256 for every source file. A same-size byte change, missing file, additional file, rename, malformed marker, or archive-lineage mismatch forces a safe local regeneration. Extraction is completed and revalidated under `<hash>.part` before directory publication; an existing extraction is backed up and rollback-protected during replacement.

### Real Muret regression

- Document ID: `33edb4c9f6943c88d8d92518bff20bec`
- Archive: `31395_PLU_20240215`
- State: `document.production` / `APPROVED` / `EN_VIGUEUR`
- Source URL: `https://www.geoportail-urbanisme.gouv.fr/api/document/download-by-partition/DU_31395`
- Download timestamp retained: `2026-08-11T20:27:22.943318+00:00`
- Archive SHA256 retained: `9d6677cd6634b56b712311042f0cc714d5ca42a38f82a417b27dd473255d7d93`
- Archive acquisition: cache hit after complete revalidation
- First hardened extraction: safe offline regeneration from the valid ZIP (old marker migration)
- Second hardened extraction: cache hit after checking 73 paths, sizes, and file hashes
- Extraction manifest: schema 2, archive SHA matches, 73 entries, exact inventory match
- Zoning / prescription surface / line / point: 221 / 320 / 5 / 5
- Written PDFs: 35
- Detected standard: `CNIG PLU v2017`

Raw zoning vocabulary is unchanged:

- `TYPEZONE`: `A` 6, `AUc` 9, `AUs` 7, `N` 143, `U` 56.
- `LIBELLE`: `A`, `AU`, `AU0`, `AUa`, `AUf`, `AUfa`, `AUfb`, `AUfc`, `AUfd`, `AUfo`, `AUp`, `N`, `NL`, `Ne`, `Nh`, `Nr`, `UA`, `UAa`, `UAb`, `UB`, `UBa`, `UBb`, `UC`, `UD`, `UF`, `UFa`, `UFc`, `UFd`, `UP`.

No BESS urban-planning suitability rule is selected.

## STEP 7D.1 — GPU Muret urban-planning source ingestion

- Status: Complete
- Implementation summary: Added strict official-GPU configuration, metadata-driven current-document discovery, partition download, transactional cache publication, complete ZIP integrity/path/link validation, content-addressed safe extraction, deterministic inventory, config-driven CNIG layer discovery, and read-only schema/geometry inspection. No parcel or zoning interpretation is performed.
- Important files: `configs/sources/gpu_fr.yaml`, `src/landscout/sources/gpu_fr.py`, `tests/unit/test_gpu_fr.py`
- Tests/checks: 27 focused offline tests cover strict configuration, status-aware discovery, download/cache/expiry/failure preservation, lineage sidecars, archive corruption/traversal/symlinks, extraction caching, and spatial inspection without geometry repair. Full suite: 543 passed; Ruff and mypy passed.
- Important decisions: A document is current only when GPU reports `document.production`, `APPROVED`, and `EN_VIGUEUR` for the configured partition and commune. Selection is never based on filename order. Physical layer names are matched from configured normalized tokens, including CNIG commune/date prefixes and suffixes. Missing API metadata remains null rather than being fabricated.
- Known issues: The current API does not expose the ticket's observed numeric version `10`; LandScout records `version = null`. The embedded ISO metadata does expose `CNIG PLU v2017`. GPU publication is authoritative source evidence, but does not itself establish BESS authorization, buildability, permit acceptance, or grid permission.

### Current official document and archive lineage

| Field | Observed value |
| --- | --- |
| Provider / portal | Géoportail de l'Urbanisme |
| Commune / partition | Muret `31395` / `DU_31395` |
| Document ID | `33edb4c9f6943c88d8d92518bff20bec` |
| Family / type | `DU` / `PLU` |
| Title | Plan Local d'Urbanisme (PLU) de la commune de MURET |
| Processing status | `document.production` |
| Legal / effective status | `APPROVED` / `EN_VIGUEUR` |
| Archive | `31395_PLU_20240215.zip` |
| API version | Not exposed (`null`) |
| Publication / update | `26/03/2024 08:52:34` / `26/03/2024 08:52:34` |
| Revision/reference date | API: not exposed; current `DOC_URBA` approval date: `20240215` (`MC1`) |
| Producer | Mairie de Muret |
| Standard/model | Embedded ISO metadata: `CNIG PLU v2017` |
| API projection | `EPSG:2154` |
| Metadata identifier | `fr-000031395-plu20240215` |
| Download source | `https://www.geoportail-urbanisme.gouv.fr/api/document/download-by-partition/DU_31395` |
| Archive format / size | ZIP / 261,401,471 bytes |
| SHA256 | `9d6677cd6634b56b712311042f0cc714d5ca42a38f82a417b27dd473255d7d93` |
| Download timestamp | `2026-08-11T20:27:22.943318+00:00` |
| Second acquisition | Cache hit after full ZIP and lineage revalidation |
| Extraction | 73 source files at ignored `data/cache/gpu/x/9d6677cd6634b56b` |

The API returned exactly one current approved/in-force document. Three older Muret PLU documents were returned as `document.deleted` / `ARCHIVE` and were not selected.

### Complete extracted-file inventory

The inventory below is `relative path | type | bytes`. Shapefile components are spatial data, the XML is metadata, and PDFs are written-document attachments.

```text
31395_PLU_20240215/31395_DOC_URBA_20240215.dbf | dbf | 21900
31395_PLU_20240215/31395_DOC_URBA_COM_20240215.dbf | dbf | 134
31395_PLU_20240215/Donnees_geographiques/31395_INFO_SURF_20240215.cpg | cpg | 5
31395_PLU_20240215/Donnees_geographiques/31395_INFO_SURF_20240215.dbf | dbf | 101791
31395_PLU_20240215/Donnees_geographiques/31395_INFO_SURF_20240215.prj | prj | 464
31395_PLU_20240215/Donnees_geographiques/31395_INFO_SURF_20240215.qix | qix | 7740
31395_PLU_20240215/Donnees_geographiques/31395_INFO_SURF_20240215.qmd | qmd | 2091
31395_PLU_20240215/Donnees_geographiques/31395_INFO_SURF_20240215.shp | shp | 155288
31395_PLU_20240215/Donnees_geographiques/31395_INFO_SURF_20240215.shx | shx | 1292
31395_PLU_20240215/Donnees_geographiques/31395_PRESCRIPTION_LIN_20240215.cpg | cpg | 5
31395_PLU_20240215/Donnees_geographiques/31395_PRESCRIPTION_LIN_20240215.dbf | dbf | 3727
31395_PLU_20240215/Donnees_geographiques/31395_PRESCRIPTION_LIN_20240215.prj | prj | 452
31395_PLU_20240215/Donnees_geographiques/31395_PRESCRIPTION_LIN_20240215.qix | qix | 80
31395_PLU_20240215/Donnees_geographiques/31395_PRESCRIPTION_LIN_20240215.qmd | qmd | 2091
31395_PLU_20240215/Donnees_geographiques/31395_PRESCRIPTION_LIN_20240215.shp | shp | 2284
31395_PLU_20240215/Donnees_geographiques/31395_PRESCRIPTION_LIN_20240215.shx | shx | 140
31395_PLU_20240215/Donnees_geographiques/31395_PRESCRIPTION_PCT_20240215.cpg | cpg | 5
31395_PLU_20240215/Donnees_geographiques/31395_PRESCRIPTION_PCT_20240215.dbf | dbf | 3727
31395_PLU_20240215/Donnees_geographiques/31395_PRESCRIPTION_PCT_20240215.prj | prj | 452
31395_PLU_20240215/Donnees_geographiques/31395_PRESCRIPTION_PCT_20240215.qix | qix | 80
31395_PLU_20240215/Donnees_geographiques/31395_PRESCRIPTION_PCT_20240215.qmd | qmd | 2091
31395_PLU_20240215/Donnees_geographiques/31395_PRESCRIPTION_PCT_20240215.shp | shp | 240
31395_PLU_20240215/Donnees_geographiques/31395_PRESCRIPTION_PCT_20240215.shx | shx | 140
31395_PLU_20240215/Donnees_geographiques/31395_PRESCRIPTION_SURF_20240215.cpg | cpg | 5
31395_PLU_20240215/Donnees_geographiques/31395_PRESCRIPTION_SURF_20240215.dbf | dbf | 205410
31395_PLU_20240215/Donnees_geographiques/31395_PRESCRIPTION_SURF_20240215.prj | prj | 464
31395_PLU_20240215/Donnees_geographiques/31395_PRESCRIPTION_SURF_20240215.qix | qix | 13044
31395_PLU_20240215/Donnees_geographiques/31395_PRESCRIPTION_SURF_20240215.qmd | qmd | 658
31395_PLU_20240215/Donnees_geographiques/31395_PRESCRIPTION_SURF_20240215.shp | shp | 255244
31395_PLU_20240215/Donnees_geographiques/31395_PRESCRIPTION_SURF_20240215.shx | shx | 2660
31395_PLU_20240215/Donnees_geographiques/31395_ZONE_URBA_20240215.cpg | cpg | 5
31395_PLU_20240215/Donnees_geographiques/31395_ZONE_URBA_20240215.dbf | dbf | 151012
31395_PLU_20240215/Donnees_geographiques/31395_ZONE_URBA_20240215.prj | prj | 464
31395_PLU_20240215/Donnees_geographiques/31395_ZONE_URBA_20240215.qix | qix | 9524
31395_PLU_20240215/Donnees_geographiques/31395_ZONE_URBA_20240215.qmd | qmd | 677
31395_PLU_20240215/Donnees_geographiques/31395_ZONE_URBA_20240215.shp | shp | 377460
31395_PLU_20240215/Donnees_geographiques/31395_ZONE_URBA_20240215.shx | shx | 1868
31395_PLU_20240215/fr-000031395-plu20240215.xml | xml | 26263
31395_PLU_20240215/Pieces_ecrites/0_Procedure/31395_procedure_20240215.pdf | pdf | 2949459
31395_PLU_20240215/Pieces_ecrites/1_Rapport_de_presentation/31395_rapport_0_20240215.pdf | pdf | 34431
31395_PLU_20240215/Pieces_ecrites/1_Rapport_de_presentation/31395_rapport_1_20240215.pdf | pdf | 11543672
31395_PLU_20240215/Pieces_ecrites/1_Rapport_de_presentation/31395_rapport_10_20240215.pdf | pdf | 1657190
31395_PLU_20240215/Pieces_ecrites/1_Rapport_de_presentation/31395_rapport_11_20240215.pdf | pdf | 5578080
31395_PLU_20240215/Pieces_ecrites/1_Rapport_de_presentation/31395_rapport_12_20240215.pdf | pdf | 6191659
31395_PLU_20240215/Pieces_ecrites/1_Rapport_de_presentation/31395_rapport_13_20240215.pdf | pdf | 1778722
31395_PLU_20240215/Pieces_ecrites/1_Rapport_de_presentation/31395_rapport_14_20240215.pdf | pdf | 9346087
31395_PLU_20240215/Pieces_ecrites/1_Rapport_de_presentation/31395_rapport_15_20240215.pdf | pdf | 5309159
31395_PLU_20240215/Pieces_ecrites/1_Rapport_de_presentation/31395_rapport_16_20240215.pdf | pdf | 9756075
31395_PLU_20240215/Pieces_ecrites/1_Rapport_de_presentation/31395_rapport_17_20240215.pdf | pdf | 7037066
31395_PLU_20240215/Pieces_ecrites/1_Rapport_de_presentation/31395_rapport_5_20240215.pdf | pdf | 3611788
31395_PLU_20240215/Pieces_ecrites/1_Rapport_de_presentation/31395_rapport_6_20240215.pdf | pdf | 5215130
31395_PLU_20240215/Pieces_ecrites/1_Rapport_de_presentation/31395_rapport_7_20240215.pdf | pdf | 7119987
31395_PLU_20240215/Pieces_ecrites/1_Rapport_de_presentation/31395_rapport_8_20240215.pdf | pdf | 2139816
31395_PLU_20240215/Pieces_ecrites/1_Rapport_de_presentation/31395_rapport_9_20240215.pdf | pdf | 6070479
31395_PLU_20240215/Pieces_ecrites/2_PADD/31395_padd_20240215.pdf | pdf | 8238141
31395_PLU_20240215/Pieces_ecrites/3_Reglement/31395_prescription_surf_05_00_20240215.pdf | pdf | 758810
31395_PLU_20240215/Pieces_ecrites/3_Reglement/31395_reglement_20240215.pdf | pdf | 2162501
31395_PLU_20240215/Pieces_ecrites/3_Reglement/31395_reglement_graphique_0_20240215.pdf | pdf | 1537350
31395_PLU_20240215/Pieces_ecrites/3_Reglement/31395_reglement_graphique_1_20240215.pdf | pdf | 21284814
31395_PLU_20240215/Pieces_ecrites/3_Reglement/31395_reglement_graphique_2_20240215.pdf | pdf | 8483008
31395_PLU_20240215/Pieces_ecrites/3_Reglement/31395_reglement_graphique_3_20240215.pdf | pdf | 10994632
31395_PLU_20240215/Pieces_ecrites/3_Reglement/31395_reglement_graphique_4_20240215.pdf | pdf | 22472095
31395_PLU_20240215/Pieces_ecrites/3_Reglement/31395_reglement_graphique_5_20240215.pdf | pdf | 15115257
31395_PLU_20240215/Pieces_ecrites/3_Reglement/31395_reglement_graphique_6_20240215.pdf | pdf | 18170061
31395_PLU_20240215/Pieces_ecrites/3_Reglement/31395_reglement_graphique_7_20240215.pdf | pdf | 16646544
31395_PLU_20240215/Pieces_ecrites/4_Annexes/31395_arrete_sonor_20240215.pdf | pdf | 8517904
31395_PLU_20240215/Pieces_ecrites/4_Annexes/31395_DUP_20240215.pdf | pdf | 33557433
31395_PLU_20240215/Pieces_ecrites/4_Annexes/31395_info_surf_16_00_20240215.pdf | pdf | 18138691
31395_PLU_20240215/Pieces_ecrites/4_Annexes/31395_info_surf_27_00_20240215.pdf | pdf | 4254234
31395_PLU_20240215/Pieces_ecrites/4_Annexes/31395_liste_annexes_2040215.pdf | pdf | 233035
31395_PLU_20240215/Pieces_ecrites/4_Annexes/31395_liste_sup_20240215.pdf | pdf | 359529
31395_PLU_20240215/Pieces_ecrites/4_Annexes/31395_plan_sonor_20240215.pdf | pdf | 429888
31395_PLU_20240215/Pieces_ecrites/5_Orientations_amenagement/31395_orientations_amenagement_20240215.pdf | pdf | 8790094
```

### Spatial layer inventory and geometry evidence

The real package contains five Shapefile layers and no GeoPackage:

| Actual source layer | Features | Source CRS | Geometry | Null / empty / invalid |
| --- | ---: | --- | --- | ---: |
| `31395_ZONE_URBA_20240215` | 221 | `IGNF:LAMB93` | Polygon 221 | 0 / 0 / 0 |
| `31395_PRESCRIPTION_SURF_20240215` | 320 | `IGNF:LAMB93` | Polygon 320 | 0 / 0 / 0 |
| `31395_PRESCRIPTION_LIN_20240215` | 5 | `EPSG:2154` | LineString 5 | 0 / 0 / 0 |
| `31395_PRESCRIPTION_PCT_20240215` | 5 | `EPSG:2154` | Point 5 | 0 / 0 / 0 |
| `31395_INFO_SURF_20240215` | 149 | `IGNF:LAMB93` | Polygon 148, MultiPolygon 1 | 0 / 0 / 0 |

`IGNF:LAMB93` is the source's authority label for Lambert-93; it was recorded as reported and not relabelled in the inspection output. No geometry was repaired or reprojected. No information-line or information-point layer exists in this archive.

Authoritative zoning schema:

| Column | dtype | nulls |
| --- | --- | ---: |
| `LIB_IDZONE` | str | 0 |
| `LIBELLE` | str | 0 |
| `LIBELONG` | str | 0 |
| `TYPEZONE` | str | 0 |
| `NOMFIC` | str | 0 |
| `URLFIC` | object | 221 |
| `IDURBA` | str | 0 |
| `DATVALID` | str | 0 |
| `geometry` | geometry | 0 |

The real identity fields are `IDURBA` (`31395_PLU_20240215`) and the commune-linked `DOC_URBA_COM` record (`INSEE=31395`). The raw zoning vocabulary is preserved exactly:

| Source field | Raw value counts |
| --- | --- |
| `TYPEZONE` | `A` 6; `AUc` 9; `AUs` 7; `N` 143; `U` 56 |
| `LIBELLE` | `A` 6; `AU` 1; `AU0` 6; `AUa` 1; `AUf` 1; `AUfa` 1; `AUfb` 1; `AUfc` 1; `AUfd` 1; `AUfo` 1; `AUp` 2; `N` 2; `NL` 4; `Ne` 1; `Nh` 124; `Nr` 12; `UA` 2; `UAa` 3; `UAb` 8; `UB` 5; `UBa` 2; `UBb` 2; `UC` 7; `UD` 8; `UF` 2; `UFa` 1; `UFc` 1; `UFd` 1; `UP` 14 |
| `NOMFIC` | `31395_reglement_20240215.pdf` 221 |
| `DATVALID` | `20221215` 218; `20231005` 2; `20240215` 1 |
| `URLFIC` | null 221 |

No zoning value is mapped to BESS suitability in this step.

Prescription/information classification evidence:

| Layer | Key source codes |
| --- | --- |
| Prescription surface | `TYPEPSC`: `01` 127, `05` 185, `07` 1, `17` 1, `18` 6; `STYPEPSC`: `00` 319, `04` 1 |
| Prescription line | `TYPEPSC`: `15` 5; `STYPEPSC`: `00` 4, `01` 1 |
| Prescription point | `TYPEPSC`: `07` 5; `STYPEPSC`: `00` 5 |
| Information surface | `TYPEINF`: `02` 1, `14` 3, `27` 4, `99` 141; `STYPEINF`: `00` 149 |

The source `LIBELLE`, `TXT`, `NOMFIC`, `IDURBA`, and validity-date fields remain unmodified and available for later evidence-based interpretation. These codes are source facts only; no exclusion/pass meaning is assigned here.

### Written regulation inventory

The archive and `/files` endpoint agree on 35 PDFs. The extracted paths above preserve their source relation: one procedure, fourteen presentation-report parts, one PADD, ten regulation files (written regulation, reserved-site attachment, and eight graphic sheets), seven annexes, and one OAP. Key files are:

- written regulation: `31395_reglement_20240215.pdf`;
- graphic regulation: `31395_reglement_graphique_0_20240215.pdf` through `_7_`;
- annexes/SUP evidence: `31395_liste_annexes_2040215.pdf`, `31395_liste_sup_20240215.pdf`, DUP, noise, archaeological-site, and airport-noise attachments;
- prescription evidence: `31395_prescription_surf_05_00_20240215.pdf`;
- planning context: procedure, PADD, OAP, and presentation-report parts.

No OCR or regulation interpretation was performed.

No BESS urban-planning suitability rule was selected in STEP 7D.1.

Source zoning classification is preserved independently from later LandScout interpretation.

## STEP 7C.5 — Diagnose IGN grid proxy coverage boundaries

- Status: Complete
- Implementation summary: Added config-driven loading of the authoritative D031 department geometry and a separate immutable stage that diagnoses whether each existing nearest-proxy result could be limited by the loaded package boundary.
- Important files: `configs/sources/ign_bdtopo_fr.yaml`, `src/landscout/sources/ign_bdtopo_fr.py`, `src/landscout/stages/assess_grid_coverage.py`, `tests/unit/test_ign_bdtopo_fr.py`, `tests/unit/test_assess_grid_coverage.py`
- Tests/checks: 61 focused IGN-source and coverage tests pass. The full suite passes with 516 tests; Ruff and mypy pass.
- Important decisions: Physical coverage-layer discovery and its department identity field are configuration-driven. Parcels touching, crossing, or lying outside the selected coverage are handled conservatively and receive a deterministic boundary distance of `0 m`. For strictly internal parcels, full parcel geometry—not the centroid—is measured against the full coverage boundary in planar EPSG:2154.
- Known issues: The existing Pyogrio warnings for unsupported declared GeoPackage field formats remain; layer discovery and loading succeed. This diagnostic does not measure source completeness inside D031.

### Real department-layer inspection

- Actual source layer: `departement`
- Source feature count: 7
- CRS: `EPSG:2154`
- Geometry types: `MultiPolygon` 7
- Null / empty / invalid geometries: 0 / 0 / 0
- Columns and dtypes:
  - `cleabs`: `str`
  - `nom_officiel`: `str`
  - `code_insee`: `str`
  - `code_insee_de_la_region`: `str`
  - `code_siren`: `str`
  - `date_creation`: `datetime64[ms]`
  - `date_modification`: `datetime64[ms]`
  - `date_d_apparition`: `datetime64[ms]`
  - `date_de_confirmation`: `datetime64[ms]`
  - `liens_vers_autorite_administrative`: `str`
  - `geometry`: `geometry`
- Authoritative identity field: `code_insee`
- Selected feature: exactly one row with `code_insee = "31"` and `nom_officiel = "Haute-Garonne"`
- Selected geometry: valid `MultiPolygon`; no union or row-position inference was used

The coverage source result preserves provider, product, department, edition, product version, archive SHA256, actual source layer, and `SOURCE_COVERAGE_BOUNDARY` spatial role. All original source attributes remain available on the selected feature.

### Diagnostic semantics

For strictly internal parcels, `grid_source_boundary_distance_m` is the minimum planar XY distance from the full parcel geometry to the selected D031 boundary. A matched proxy is `NOT_BOUNDARY_LIMITED` only when its distance is strictly smaller than that boundary distance. Equality remains `BOUNDARY_LIMITED`, because an outside feature could tie. Matched parcels that are not strictly internal are `OUTSIDE_OR_CROSSING_COVERAGE`; a legitimately absent proximity class is `NO_MATCH`.

The stage returns new parcel and voltage frames. Parcel count, parcel IDs/order, geometry, storage CRS, parcel-voltage pairs/order, distances, selected features, tie counts, voltages, and existing lineage remain unchanged. Coverage provenance is added explicitly to both outputs. The long-form voltage vocabulary remains dynamic.

### Real Muret/D031 results

- Input/output parcels: 3,638 / 3,638
- Voltage proximity rows: 14,552
- Fully covered parcels: 3,638
- Outside or crossing parcels: 0
- Assessment wall-clock duration: 16.667 seconds

Main proximity status counts:

| Proximity class | NOT_BOUNDARY_LIMITED | BOUNDARY_LIMITED | OUTSIDE_OR_CROSSING_COVERAGE | NO_MATCH |
| --- | ---: | ---: | ---: | ---: |
| Nearest line | 3,638 | 0 | 0 | 0 |
| Nearest exact-voltage line | 3,638 | 0 | 0 | 0 |
| Nearest transformation post | 3,638 | 0 | 0 | 0 |

Dynamic exact-voltage results:

| Voltage | Parcels | NOT_BOUNDARY_LIMITED | BOUNDARY_LIMITED | OUTSIDE_OR_CROSSING_COVERAGE |
| ---: | ---: | ---: | ---: | ---: |
| 63 kV | 3,638 | 3,638 | 0 | 0 |
| 150 kV | 3,638 | 0 | 3,638 | 0 |
| 225 kV | 3,638 | 3,638 | 0 | 0 |
| 400 kV | 3,638 | 3,638 | 0 | 0 |

The observed 150 kV proximity distribution is therefore boundary-limited for every current Muret candidate. This is a coverage diagnostic, not a distance or voltage suitability judgment.

Boundary-distance distribution:

| Statistic | Distance (m) |
| --- | ---: |
| Minimum | 8,450.250 |
| p01 | 9,183.982 |
| p05 | 9,859.522 |
| p10 | 10,903.477 |
| p25 | 12,494.960 |
| p50 | 14,003.103 |
| p75 | 14,961.993 |
| p90 | 15,660.464 |
| p95 | 16,074.718 |
| p99 | 16,418.363 |
| Maximum | 16,712.165 |

### Outputs and read-back

- Coverage GeoParquet: `data/processed/grid/muret_bess_grid_proximity_coverage.parquet` (1,272,692 bytes)
- Coverage long-form Parquet: `data/processed/grid/muret_bess_grid_voltage_proximity_coverage.parquet` (221,705 bytes)
- Read-back rows: 3,638 parcels and 14,552 parcel-voltage rows
- Duplicate parcel-voltage pairs: 0
- Parcel CRS: `EPSG:4326`
- Original geometry and every prior proximity value: unchanged
- Coverage statuses, boundary distances, dynamic Cartesian product, and coverage lineage: verified after read-back

Generated outputs remain ignored by Git.

`NOT_BOUNDARY_LIMITED` does not prove that IGN contains every real electrical asset.

It only means an asset outside the loaded D031 geographic coverage cannot be geometrically closer than the selected in-coverage proxy.

IGN infrastructure geometry is `PROXY_GEOMETRY`.

The department geometry is `SOURCE_COVERAGE_BOUNDARY`, not infrastructure geometry.

No BESS distance or voltage suitability threshold is selected.

## STEP 7C.4.2 — Cross-validate exact-line proximity representations

- Status: Complete
- Implementation summary: Added a result-contract check that reconstructs the deterministic global nearest EXACT-voltage line from each parcel's long-form per-voltage winners and rejects any contradiction before enrichment returns or profiling begins.
- Important files: `src/landscout/stages/enrich_grid_proximity.py`, `tests/unit/test_enrich_grid_proximity.py`
- Tests/checks: 155 focused proximity tests pass. The full suite passes with 486 tests; Ruff and mypy pass.
- Important decisions: The validator uses exact distance equality because both representations are produced independently from the same calculation-only Lambert-93 geometries. Expected winners are ordered explicitly by parcel input position, distance, then lexical `grid_feature_id`; incidental DataFrame row order is never used.
- Known issues: The source remains a department-31 IGN proxy dataset. Cross-representation consistency proves internal mathematical and lineage agreement, not connection feasibility or completeness beyond the loaded coverage.

### Exact representation contract

For every parcel with exact-voltage coverage, the global nearest EXACT match must equal the deterministic minimum across its voltage-level proximity rows. The validator cross-checks:

- proxy distance;
- grid feature ID;
- source feature ID;
- voltage;
- manager and raw asset status using null-safe equality;
- source department, edition, and archive SHA256;
- global tie count.

The existing long-table schema is sufficient to reconstruct the global tie count exactly. Each voltage row retains its within-level tie count; for every voltage level whose winner shares the exact global minimum distance, those tie counts are summed. This captures both same-voltage and cross-voltage ties without inventing a weaker proxy invariant or adding columns. Lexical selection among tied per-voltage winners reproduces the production `grid_feature_id` tie breaker.

When exact-voltage coverage is absent, the existing invariant is unchanged: the voltage table is empty and every `nearest_exact_*` field is null with stable nullable numeric dtypes.

`profile_grid_proximity()` invokes the complete cross-representation check before calculating statistics. Tests prove rejection of contradictory global distances, IDs, voltages, optional metadata, source lineage, and otherwise valid but incorrect tie counts. A synthetic 110/275 kV cross-voltage tie confirms lexical selection of `A-LINE-275` over `Z-LINE-110`; existing same-voltage tie behavior remains unchanged.

### Real Muret/D031 regression and read-back

- Enriched parcels: 3,638
- Voltage-level proximity rows: 14,552
- Dynamic exact-voltage levels: 63, 150, 225, and 400 kV
- Exact representation mismatches: 0
- Lost IDs / extra IDs / duplicate parcel IDs / duplicate parcel-voltage pairs: 0 / 0 / 0 / 0
- Nearest exact-line p50: 746.824 m
- Nearest line / post p50: 746.824 m / 2,643.274 m
- Distance profiles and tie counts remain numerically unchanged from STEP 7C.4.1.
- Real enrichment wall-clock duration: 1.300 seconds
- Rewritten GeoParquet: `data/processed/grid/muret_bess_grid_proximity.parquet` (1,227,955 bytes)
- Rewritten long-form Parquet: `data/processed/grid/muret_bess_grid_voltage_proximity.parquet` (176,469 bytes)
- Read-back cross-validation: passed with the original 3,638 parcel IDs and order, exact Cartesian voltage coverage, `EPSG:4326` parcel CRS, preserved geometry, complete lineage, finite distances, and integer tie counts

Generated outputs remain ignored by Git.

IGN geometry is `PROXY_GEOMETRY`.

All distances remain 2D planar proxy distances calculated in EPSG:2154 from full parcel geometry. IGN Z values are not used in horizontal proximity.

Distance to an IGN electric line or transformation post does not establish grid connection feasibility, capacity, connection cost, or an RTE/DSO connection point.

No BESS grid-distance threshold is selected here.

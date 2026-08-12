# LandScout AI development log

## Current project state

- Current phase: French urban-planning evidence structuring
- Latest completed step: STEP 7D.4B — factual regulation structure and zone evidence
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

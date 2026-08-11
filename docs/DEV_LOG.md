# LandScout AI development log

## Current project state

- Current phase: French cadastral data ingestion
- Latest completed step: STEP 7B.4.1 — centralize parcel shape metrics
- Current branch: `main`
- Python version: `3.12.13`
- Next step waiting for review: next LandScout implementation step, not yet specified

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

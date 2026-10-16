# Cadastre area/shape screening

`DEV.CADASTRE.RUN.1` integrates one FR/BESS commune through verified cadastral
loading, normalization, and the existing area and shape filters. The result is
`RETAINED_BY_EXECUTED_FILTERS`, a preliminary geometric selection. Grid, roads,
planning, environment, scoring and owners are recorded as `NOT_RUN`. Their
presence elsewhere in the library does not imply execution by this command.

## Command and paths

From the repository root, using the existing environment:

```powershell
.venv\Scripts\python.exe -B -X utf8 -m landscout scan `
  --scan configs/scans/bess_muret.yaml `
  --cache-dir data/cache/cadastre `
  --output outputs/muret-premier-run `
  --offline
```

The CLI defaults to offline. `--offline` and `--allow-download` are mutually
exclusive. The latter permits only the configured commune's acquisition through
the cadastral adapter; development tests simulate that transport. Cache hits
still verify identity, UTC age, size, SHA256 and gzip. The optional
`--max-cache-age-hours` defaults to 168 and uses the adapter's existing strict
finite nonnegative-number validation. Offline never refreshes or accepts an
invalid/expired cache, prepares temporary files, or removes recovery material.
The adapter's new keyword-only `allow_download` requires an exact bool and
defaults to True for existing library callers; the workflow defaults to False.

Configuration layout follows `load_scan_config`: the root is
`scan_path.resolve().parents[2]`, normally `PROJECT/configs/scans/scan.yaml`.
Relative profile, cache and output paths resolve against that root, irrespective
of the current working directory. Absolute paths are retained after validation.
Without `--cache-dir`, the root-relative directory is `data/cache/cadastre`.
Without `--output`, a new `cadastre-COMMUNE-UUID` directory is selected beneath
the loaded scan's output directory. Multiple communes and identities other than
FR/BESS are explicitly rejected before acquisition or writing; the common
configuration models retain their wider scope.

The scan/profile supply all filter values. The current checked-in Muret profile
contains area 2,000–15,000 m², width 15 m, ratio 10, enabled shape screening and
`muret_empirical_v1` calibration; the runner does not duplicate those thresholds.
Shape enrichment still runs when shape screening is disabled, and the existing
disabled filter retains all area candidates without new shape exclusions.

`--help` performs no run or write. Exit 0 requires complete publication, usage
errors return 2, and controlled run errors return 1 with the cause on stderr.
An existing output directory is always refused. Output links/junctions, cache
collisions, configuration collisions and tracked-path collisions are rejected.

## Library API and execution

```python
from pathlib import Path
from landscout.workflows import run_cadastre_screening

result = run_cadastre_screening(
    Path("configs/scans/bess_muret.yaml"),
    cache_dir=Path("data/cache/cadastre"),
    output_dir=Path("outputs/new-cadastre-run"),
    allow_download=False,
)
```

`CadastreScreeningRunResult` is a frozen result with output paths and effective
normalized/area-rejected/shape-rejected/retained counts. Failures raise
`CadastreScreeningRunError`. The API loads configuration itself and executes:

1. `load_scan_config`;
2. `download_cadastre_parcelles(..., allow_download=...)`;
3. `load_cadastre_parcels`;
4. `normalize_cadastre_parcels`, including fresh physical source revalidation;
5. `filter_parcels_by_area`, returning candidates then rejected;
6. `enrich_parcel_shapes` on area candidates;
7. `filter_parcels_by_shape`, returning retained then rejected;
8. exact ID partition checks and exports.

The stages retain their own validation, metrics and reasons. Geometry stays in
EPSG:4326, with metric computations in EPSG:2154. There is no repair or dimensional
coercion. A-001's intrinsic normalized boundary now uses Shapely coordinate
dimension to reject non-null XYZ/XYM/XYZM Polygon/MultiPolygon. Ordinary XY
null/empty/invalid geometries retain their existing INVALID/null-area contract.
The in-memory dimension tests do not establish preservation of M by an official
GeoJSON reader. Centroids are geometric measurements, not addresses/access points.

## Output schema 1

Four files are created in a new run directory. Presentation sorts both CSVs and
GeoJSON features by `parcel_id`; intermediate stage frames keep their own order.
The two CSVs have this exact column order:

```text
parcel_id,commune_code,section_prefix,section,parcel_number,geometry_status,area_m2,shape_status,length_m,width_m,length_width_ratio,compactness,centroid_lat,centroid_lon,screening_status,screening_stage,rejection_reason
```

Identifiers remain strings, including leading zeroes. CSV nulls are empty cells;
GeoJSON nulls are JSON null. Source attributes outside this selection are excluded.
Rows rejected at AREA have no shape metrics/status or invented centroid; their
area is also null for INVALID geometry. Available metrics keep the stages' values.

| File | Contract |
|---|---|
| `candidates.csv` | Retained IDs and available metrics; status `RETAINED_BY_EXECUTED_FILTERS`, stage `AREA_SHAPE` or `AREA` when shape screening is disabled, null reason. |
| `rejections.csv` | All other IDs, status `REJECTED_BY_EXECUTED_FILTERS`, originating `AREA`/`SHAPE` stage and the exact filter reason. |
| `candidates.geojson` | Same ordered IDs/properties as the candidate CSV and preserved WGS84 geometries in a FeatureCollection. |
| `run.json` | Completion marker, written last; `schema_version=1`, `status=COMPLETE`, scope `CADASTRE_AREA_SHAPE_ONLY`. |

Area reasons are supplied by `rejection_reason`; shape reasons by
`shape_rejection_reason`. The runner does not rewrite them. It checks uniqueness,
disjointness and full closure: normalized = AREA rejected + SHAPE rejected +
retained, and rereads exported IDs to verify CSV/GeoJSON correspondence. Zero
retained parcels is a success: CSVs keep their headers and GeoJSON has an empty
features list. A source reading error, including a physically empty dataset, fails.

The manifest records commune, UTC start/completion timestamps, absolute scan and
profile paths/sizes/SHA256, actual loaded filter settings, download permission and
age threshold, archive/source URL/size/SHA256/timestamp/cache_hit, counts and exact
reason frequencies, three data-file sizes/SHA256, presentation order and NOT_RUN
domains. JSON is strict, without NaN/Infinity or generic `default=str`. These are
local byte digests, not publisher-supplied checksums. No circular run.json hash is
included. Data rows repeat for identical inputs; timestamps, paths and run metadata
can vary.

Scan/profile fingerprints are captured around public loading and checked before
publication. The source is physically reread and compared again after data export.
These checks reject persistent changes; they are not an immutable snapshot or a
guarantee against all transient/concurrent changes. On a write/verification failure,
the newly created directory is preserved and named in the error. Data and possibly
`run.json.part` may remain, with no COMPLETE marker. `run.json` is published after
the temporary manifest closes successfully. This is a final-marker protocol, not
an atomic multi-file transaction. Pre-existing output/cache bytes are not removed.

## Evidence from this ticket

`SYNTHETIC_END_TO_END`: physical synthetic gzip, real public loading/revalidation,
normalization, metrics, filters and exports pass with transport forbidden. A saved
synthetic example is at `C:\souhaib\dcr1-synthetic-example\outputs\cadastre-run`:
8 normalized, 4 AREA rejections, 2 SHAPE rejections, 2 retained; CLI exit 0. It is
explicitly a test dataset, not a result for the official Muret parcels.

`REAL_MURET_OFFLINE_RUN`: attempted with the command above, native exit 1 and no
output directory. The local pre-schema sidecar lacks `schema_version` and
`commune_code` and records `2026-08-11T12:03:56.900678+00:00`; it does not satisfy
the current fresh-cache contract. Neither archive nor metadata changed; no
download occurred. Real parcel counts/selection are therefore unavailable.

The exact [ticket](../project/tickets/DEV.CADASTRE.RUN.1.md) and
[DEV_LOG](../DEV_LOG.md#devcadastrerun1--first-executable-cadastre-screening-slice)
record execution evidence. A-001's implementation awaits independent review;
A-002/A-003/A-004 remain open. Global documentation remains PARTIAL and deferred
by the user, with stale bindings queued for reconciliation on resumption.

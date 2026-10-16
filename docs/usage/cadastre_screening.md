# Cadastre area/shape screening

`DEV.CADASTRE.RUN.1` integrates one FR/BESS commune through verified cadastral
loading, normalization, and the existing area and shape filters. The result is
`RETAINED_BY_EXECUTED_FILTERS`, a preliminary geometric selection. Without
either `--with-grid` or `--with-roads`, grid, roads,
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

The exact historical [cadastre ticket](../project/tickets/DEV.CADASTRE.RUN.1.md) and
[DEV_LOG](../DEV_LOG.md#devcadastrerun1--first-executable-cadastre-screening-slice)
record that ticket's execution evidence. The successor review supplied in
[DEV.GRID.RUN.1 section 1](../project/tickets/DEV.GRID.RUN.1.md) accepts the cadastre
slice and A-001 within its reviewed scope;
A-002/A-003/A-004 remain open. Global documentation remains PARTIAL and deferred
by the user, with stale bindings queued for reconciliation on resumption.

## Optional IGN grid proximity and coverage — schema 2

```powershell
.venv\Scripts\python.exe -B -X utf8 -m landscout scan `
  --scan configs/scans/bess_muret.yaml `
  --cache-dir data/cache/cadastre `
  --output outputs/muret-cadastre-grid `
  --with-grid `
  --ign-config configs/sources/ign_bdtopo_fr.yaml `
  --offline
```

The API adds keyword-only `with_grid=False`, `ign_config_path=None`,
`ign_cache_dir=None` and `ign_extraction_dir=None`. `with_grid` requires an exact
bool. IGN paths without either grid or roads enabled are rejected (CLI usage exit 2, API controlled
run error). The CLI accepts `--ign-cache-dir` and `--ign-extraction-dir` for existing
sources. Relative paths use the scan root above. Without overrides the adapter's
public default config/cache paths are root-relative; the extractor selects its
own default extraction from the verified download, without a duplicated archive
filename in the workflow. Configured department must match the canonical commune
department, including supported Corsican and overseas codes.

IGN consumption is **reuse only**: the workflow always passes
`allow_download=False` and `allow_extract=False`. `--allow-download` remains a
cadastre-only permission. The two IGN adapter flags are keyword-only, exact bools,
default True for historical callers. An unusable archive cache fails before
mkdir/.part preparation/cleanup/network/publication; an unusable extraction fails
before directory preparation/cleanup/extraction/replacement. Existing age,
checksum, role, recovery and extraction-inventory checks remain effective.

The cadastral calculation and partitions execute once. For nonempty retained
parcels, the workflow loads verified electricity then calls public
`assess_grid_coverage` once. That API owns its public proximity call, source-complete
normalization and configured department-coverage load. The workflow does not call
the private frame-computation helpers or recalculate distances. Line/post geometry
remains an IGN proxy, and `nearest_exact_line` means **exact voltage**, not surveyed
or certified geometry. There is no distance threshold or change to selection.

The producer resets the parcel index. As clarified by the user, integration first
checks count, ID presence/uniqueness and exact ID sequence; permutation/loss cannot
be masked. It restores `retained.index.copy(deep=True)` on a new parcel-frame copy,
then compares the complete pre-existing prefix (columns/order, values/dtypes,
index class/values/names, active geometry, CRS, WKB and frame attributes). Both input
frames remain unchanged. The voltage table keeps its own pair structure/index.
Frozen result dataclasses containing DataFrames are not deeply immutable.

With grid enabled, the manifest has `schema_version=2` and
`scope=CADASTRE_AREA_SHAPE_WITH_GRID_PROXIES`. It closes only this executed slice.
Five files are published:

- `candidates.csv` and GeoJSON properties retain the exact schema-1 prefix, followed
  by the explicit `NEAREST_COLUMNS` allowlist (nearest line, nearest exact-voltage
  line, nearest post), `PARCEL_DIAGNOSTIC_COLUMNS`, then `COVERAGE_LINEAGE_COLUMNS`.
  The full ordered export declarations are in
  [grid_screening.py](../../src/landscout/workflows/grid_screening.py); producer
  schemas are confronted in the integration tests. Unknown source columns are not
  exported through a wildcard.
- `rejections.csv` keeps the cadastral schema and original AREA/SHAPE reasons.
  Grid is computed only for retained parcels.
- `voltage_proximity.csv` uses `VOLTAGE_PROXIMITY_COLUMNS`,
  `VOLTAGE_DIAGNOSTIC_COLUMNS`, then `COVERAGE_LINEAGE_COLUMNS`, without duplicates.
  Export copies sort by `(parcel_id, voltage_kv)`. Its complete unique pair domain
  uses exact voltage levels dynamically observed in `voltage_level_coverage`.
- `run.json` is still the last completion marker, covering the four data-file
  sizes and SHA256 digests.

Integers such as tie counts remain integers in JSON and integer CSV lexemes.
Finite numbers, source text and true nulls are preserved explicitly; missing
evidence is not converted to zero. Boolean distances and NaN/Infinity serialization
are refused. Status strings remain `NOT_BOUNDARY_LIMITED`, `BOUNDARY_LIMITED`,
`OUTSIDE_OR_CROSSING_COVERAGE` and `NO_MATCH`. A package boundary can limit the
nearest-feature evidence; these statuses are not suitability decisions. NO_MATCH
for the exact-voltage view does not mean absence of electricity across France.

Schema 2 adds the IGN YAML binding, verified archive identity/cache_hit, extraction
identity/cache_hit/marker binding, GPKG size/hash, configured physical roles/layer
inventory, source edition/department/projection, selected source coverage and
observed exact-voltage counts. Provenance is extracted explicitly, without
recursive `asdict` over frames. A selected IGN post does not establish RTE capacity,
a connection point, cost, availability or connection feasibility.

After data export, the final checks validate archive integrity against the retained
download, publicly reload both electricity layers and compare their complete
frames and typed summaries, and publicly reload/compare the department coverage
from the same extraction. The electrical revalidator is internal in the existing
adapter; the user expressly authorized public loading plus complete comparisons
in the workflow instead of a private alias. Marker and YAML byte bindings are
also checked. Persistent source/configuration changes fail with preserved causes
and no COMPLETE marker. These are fresh physical reads, not a second distance
calculation or a universal concurrency/snapshot guarantee.

With no retained parcel, configuration/options are still validated but IGN
archive/extraction/distance APIs are not invoked. Schema 2 has empty extended
candidate/voltage headers, `grid.status=NOT_RUN`,
`grid.reason=NO_RETAINED_PARCELS` and no invented acquisition provenance. In contrast,
a valid nonempty source with no exact voltage has `grid.status=COMPLETE`, an empty
voltage table and NO_MATCH exact-voltage fields. An unusable requested source is a
controlled error, never a silent cadastral success. When grid completes, only grid
leaves `not_run`; roads/planning/environment/scoring/owners remain NOT_RUN.

`SYNTHETIC_END_TO_END` example:
`C:\souhaib\dgr1-synthetic-example\outputs\grid-run`, real CLI subprocess exit 0
with DNS/network boundaries forbidden. Counts stay 8 = 4 AREA rejected + 2 SHAPE
rejected + 2 retained. There are four voltage rows for 63 and 132.5 kV. Parcel
`31395000AA0001` has line distance 10 m/tie_count 2 and post distance 0; parcel
`31395000AA0008` has nearest line distance 0 with BELOW evidence, exact-voltage line
distance 5,930 m/BOUNDARY_LIMITED, and post distance 10 m. These are synthetic
geometries, not official Muret findings. Tests separately exercise unknown voltage,
no exact levels, unusable geometry and near/touching/outside coverage.

`REAL_MURET_OFFLINE_RUN`: not executed for this grid ticket because prerequisites
are not fresh valid caches. The cadastral sidecar has the pre-schema deficiencies
reported above; IGN records `2026-08-11T15:32:03.110837+00:00`, older than the
configured 168 h. Official extraction usability was not freshly asserted after
that archive-cache blocker. No official acquisition/re-extraction, freshness
adjustment or real parcel-distance count is claimed. The earlier cadastre-only
exit 1 remains its separate historical execution.

## Optional IGN road proximity by class and coverage — schema 3

```powershell
.venv\Scripts\python.exe -B -X utf8 -m landscout scan `
  --scan configs/scans/bess_muret.yaml `
  --cache-dir data/cache/cadastre `
  --output outputs/muret-cadastre-grid-roads `
  --with-grid --with-roads `
  --ign-config configs/sources/ign_bdtopo_fr.yaml `
  --road-policy configs/access/ign_bdtopo_vehicle_proxy_policy.yaml `
  --offline
```

This is a target command, not evidence of an official Muret execution. Omit
`--with-grid` for roads alone. The API adds only keyword-only `with_roads=False`
(exact bool) and `road_policy_path=None`; a policy option without roads is an
error (CLI 2, controlled API error). The result appends compatible optional
`road_proximity_csv` and `roads_status` fields. Existing no-option schema 1 and
grid-only schema 2 remain unchanged.

The new workflow explicitly chooses the default policy at
`scan_root / "configs/access/ign_bdtopo_vehicle_proxy_policy.yaml"`. It passes
one validated absolute path to the public loader and assessment; this does not
redefine the historical policy loader's own default. Policy bytes are captured
before loading, compared afterwards with the compiled `config_sha256`, and
checked again before COMPLETE. Policy/configuration/path validation precedes
cadastre acquisition even with zero retained parcels.

Nonempty runs obtain one shared archive/extraction context with the same strict
False/False IGN permissions. Combined grid/roads use the exact same extraction
and the same original cadastral `retained`, not each other's enriched frame.
Roads alone never load or assess electricity, even when its geometry is unusable;
the adapter still requires discovery of all four physical roles. Source/stage
revalidations remain active. One public `assess_road_proximity_coverage` call owns
the complete road proximity → policy application → normalization/revalidation
chain and department load. The workflow adds no second distance calculation.

Unlike grid, road assessment preserves the original sparse/named parcel index.
Integration strictly compares every original column/value/dtype, index metadata,
active geometry, CRS, WKB and frame attributes, without restoring, sorting or
reindexing it. Roads do not add scalar nearest-road fields to candidates or
GeoJSON. Cadastral selections, AREA/SHAPE reasons and geometries are unchanged.

| Requested analyses | Manifest scope | Data files plus final run.json |
|---|---|---|
| Roads alone | `CADASTRE_AREA_SHAPE_WITH_ROAD_PROXIES` | Three cadastral exports + `road_proximity.csv` + marker (5 files) |
| Grid and roads | `CADASTRE_AREA_SHAPE_WITH_GRID_AND_ROAD_PROXIES` | Same + `voltage_proximity.csv` + marker (6 files) |

Both use schema 3. `road_proximity.csv` has the exact public
`CLASS_PROXIMITY_COLUMNS` prefix, followed by these explicit columns:

```text
road_source_boundary_distance_m
road_source_coverage_position
road_proximity_coverage_status
road_source_coverage_provider
road_source_coverage_product
road_source_coverage_department_code
road_source_coverage_edition
road_source_coverage_product_version
road_source_coverage_archive_sha256
road_source_coverage_layer
road_source_coverage_spatial_role
```

The full fixed declaration is in
[road_screening.py](../../src/landscout/workflows/road_screening.py). Before export
it validates the complete ordered schema, RangeIndex, unique parcel/class pairs,
exact ordered parcel × distance-eligible-class domain and all six class counts.
Only scalar export copies sort by parcel ID then loaded policy class order;
the original public table keeps its index, types and values. All written cells
and the header are reread and compared, not just IDs.

Policy `ign_bdtopo_general_vehicle_proxy_v2`, schema 2, config SHA256
`2092bc620063ec1176b2abebaefafcc108a42793992dd18f869d44fdb07ca166` supplies
the class order and outcomes. Five classes have distance rows: general, limited,
restricted-review, not-general and unknown-review. `NOT_DISTANCE_PROXY` is the
sixth inventory class and never gets distance rows. Empty eligible classes keep
one NO_MATCH row per parcel with null selected evidence, distance and tie count.
All roads in NOT_DISTANCE_PROXY is valid COMPLETE evidence with five NO_MATCH
rows per parcel, not an acquisition error or proof of no roads nationally.

Finite numeric distances/widths and integer ties never coerce booleans. Nullable
toll evidence writes `true`/`false`/empty. Private facts keep booleans, numeric
facts or unresolved original TEXT; no truthiness conversion. True nulls write
empty cells; text, whitespace, status/reasons and JSON-text traces are unchanged,
without parsing/re-encoding JSON strings or generic `default=str`.

Distances use full parcel Polygon/MultiPolygon calculation copies in XY
EPSG:2154, not centroids. Exact ties and their lexical representative are the
stage's existing result. A fully covered matched parcel is NOT_BOUNDARY_LIMITED
only when road distance is strictly below its boundary margin; equality and
greater distances are BOUNDARY_LIMITED. Touching/crossing/outside means zero
margin and OUTSIDE_OR_CROSSING_COVERAGE. NO_MATCH remains separate and takes
precedence over position. No acceptable distance or preference between classes
is introduced.

The manifest explicitly binds the policy (ID/schema/hash/scope/vehicle scope and
heavy_vehicle_access), IGN archive, extraction marker, GPKG and physical roles,
used department coverage, and six `{road_proxy_class, feature_count,
distance_eligible}` entries. Combined branches retain explicit provenance for
each use of the shared extraction. Four or five actual data-file sizes/SHA256
digests are recorded; run.json has no self-hash. Only successfully assessed
domains leave `not_run`.

After exports the archive is publicly validated, roads are publicly reloaded
and full-compared with their typed summary and same extraction/spatial role;
department coverage is publicly reloaded and compared with the actual branch's
frame, full typed summary and lineage. Combined mode also keeps the separate
electrical coverage comparison. Marker, scan/profile/IGN/policy byte bindings
are checked before the final marker. Failures preserve causes and an explicitly
incomplete directory, never a silent cadastral COMPLETE. This is persistent
mutation detection, not a guarantee against all transient races or an atomic
multi-file snapshot.

Zero retained parcels still validate configuration and policy, but never acquire
IGN, load a layer or assess distances. The road CSV contains only its header;
roads is NOT_RUN/NO_RETAINED_PARCELS with validated policy evidence but no invented
physical provenance or class counts. Grid keeps its existing empty behavior.

Saved `SYNTHETIC_END_TO_END` example:
`C:\souhaib\drr1-synthetic-example-final\outputs\grid-roads-run`, actual CLI exit 0
under child DNS/connection sentinels. Eight parcels partition as 4 AREA rejected,
2 SHAPE rejected and 2 retained; four voltage rows and ten road rows. Seven road
objects have class counts 2/1/1/1/1/1 in policy order (the fifth is ineligible).
Parcel `31395000AA0001` has GENERAL distance 10 m, tie count 2, selected ID A,
toll true; LIMITED distance 5,960 m is BOUNDARY_LIMITED. Parcel
`31395000AA0008` has LIMITED distance 0 and GENERAL distance 5,930 m with two
ties/BOUNDARY_LIMITED. Restricted rights/private and unresolved private evidence
remain explicit. These are synthetic fixtures, not official Muret conclusions.

`REAL_MURET_ROADS_RUN=NOT_RUN`: inspected existing sidecars still fail prerequisites
(pre-schema cadastral metadata and August timestamp; IGN August timestamp older
than 168 h). No timestamp/checksum/age rewrite, official download or extraction
was performed; official extraction usability was not freshly certified beyond
the archive-cache blocker. Historical attempts remain historical.

Road evidence establishes neither legal access/easement, parcel entrance,
route practicability, nor heavy-truck/construction/BESS access. Every row keeps
`heavy_vehicle_access=NOT_PROVEN`. No road/parcel score, ranking, threshold,
new rejection, planning or environmental decision is added.

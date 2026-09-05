# Testing strategy

## Organization

Most tracked tests are under `tests/unit`; many of those exercise multi-function source-complete boundaries with real Pandas/GeoPandas/Shapely behavior, temporary archives, Parquets, PDFs, GeoPackages, and deterministic result rebuilds. `tests/integration/test_gpu_planning_end_to_end.py` is the deliberate physical end-to-end exception: it keeps the complete GPU spatial/written planning chain visible as one integration contract.

Every test file has a mirrored companion under `docs/code/files/tests/`. Each test function section records its fixtures, source-derived setup statements, called functions, direct assertions/expected exceptions, regression purpose, and whether it uses temporary filesystem, geometry, synthetic GeoPackage, mocks, or blocked/fake network.

## Test categories

### Pure contracts and configuration

Configuration/policy tests load checked-in YAML or synthetic mutations, reject nested duplicate keys/extra fields/coercion/version drift, prove nested structures cannot be mutated, and verify exact identities/domains. Shared strict-serialization tests also cover duplicate JSON keys, malformed UTF-8, non-finite/overflow numbers, and non-object payloads. Byte or canonical-config hashes are asserted only for loaders/compilers whose current source actually computes them; `load_scan_config`, for example, parses and validates the scan and referenced profile YAML without hashing their bytes.

### Geometry and frame contracts

Tests create real Shapely geometries and GeoDataFrames to exercise CRS, validity, geometry kind, area/distance/intersection, preservation, index/dtype/order, WKB, null/empty handling, and no-repair behavior. Missing-CRS fixtures intentionally produce the small pyogrio warnings visible in full-suite output.

### Synthetic physical sources

Cadastre tests use real gzip GeoJSON sources to prove `CadastreParcelSource` binds official download identity and normalization consumes a fresh exact physical reread. IGN/GPU tests write temporary archives/GeoPackages and use physical alternate layers, globally colliding roles, inventories, summaries, marker files, recovery states, and byte tampering. INPN tests prove controlled ZIP-constructor errors, same-snapshot archive validation/member hashing/extraction, archive-marker-physical-caller equality, canonical download lineage, offline extraction rebuild, and effective transient/persistent archive swaps with explicit hook-execution assertions. They also mutate cold and extraction publication seams to prove pre/post return conditions. Synthetic spatial, non-spatial, empty, multilayer, and multipackage sources prove one immutable byte snapshot per package, byte-only metadata/attribute calls, transient/persistent mutation handling, exact `GPKG` driver, schema-2 catalog and schema-1 attribute-profile hashes, Unicode identity collision rejection, strict count/CRS/bounds/frame/FID/scalar domains, exact final scalar types, complete distinct-value frequencies, narrowly suppressed known extension warnings, visible unrelated warnings, and independent physical rebuild. One shared 11-row package-path corpus covers `CON`, `NUL`, colon, both component-edge-whitespace forms, trailing-dot components, controls, fullwidth reserved names/slashes, valid nesting, and uppercase `.GPKG`; a single parity test requires extraction, catalog, and profile decisions to agree row-for-row, including chained error causes. Attribute-profile-only forgeries additionally prove path/position bijection, lexical package grouping, contiguous layer positions, repeated package-evidence equality, exact/NFKC/casefold layer and field identity uniqueness, direct impossible capacity `(3, 1, 2)`, valid sparse capacity `(3, 1, 4)`, and deterministic empty hashes. Catalog-bound profile mismatches are instrumented to fail before `read_dataframe`, while a valid profile must reach the physical rebuild. Catalog tests patch all feature readers to fail; attribute tests allow only the exact non-geometry `read_dataframe` contract and patch geometry-capable readers to fail.

### INPN geometry byte-snapshot and measured-dimension evidence

The geometry suite constructs deterministic synthetic GeoPackages and writes explicit Standard GeoPackageBinary plus XY/XYZ/XYM/XYZM WKB using SQLite during fixture construction. It does not pass measured geometries through Pyogrio: the locked Pyogrio 0.13.0 geometry reader drops M. Permanent real-Shapely parser regressions retain point ordinate values, dimension/Z/M flags, WKB roundtrips, and EMPTY M/ZM evidence. Header cases cover both byte orders, every valid/invalid envelope code, magic/version/reserved/extended flags, truncation, SRS, and empty-state disagreement. Metadata cases enforce feature tables, exact geometry columns, rowid-alias INTEGER PRIMARY KEYs, safe identifiers, and prohibited/mandatory/optional Z/M declarations.

Fatal sentinels forbid Pyogrio and GeoPandas geometry readers, attribute projections, repairs, and reprojection. Instrumented SQLite connections prove exact immutable package bytes enter `deserialize`, layers share their package snapshot, different packages have separate snapshots, feature reads are query-only, and only FID plus geometry BLOB are selected. Tests preserve sparse FIDs, NULL versus EMPTY, valid versus invalid topology with exact reasons, finite XY/Z/M/ZM, and canonical domain/count/bounds evidence. Raw full-BLOB hashes and parser-derived WKB hashes are tested independently: header-only raw changes, coordinate/Z/M/FID/structural changes, portable repeats, cache-hit independence, temporary path replacement, persistent mutation, and coordinated profile/hash forgery exercise their distinct meanings. Intrinsic and cheap fresh-catalog checks remain separate from independent physical rebuild.

Real EP verification is an explicitly controlled offline check after synthetic cases pass. It blocks network, Pyogrio/GeoPandas feature readers, repairs, and reprojection; it reads no environmental attribute. The complete per-layer geometry evidence and exact toolchain/hash results are historical validation evidence in `docs/DEV_LOG.md`, not inferred environmental meaning.

The geometry suite contains 273 collected cases; the combined INPN suites contain 672 (399 existing + 273 geometry). The focused geometry and combined runs report zero unhandled warnings. One all-NULL mandatory Z/M metadata fixture explicitly expects eight Pyogrio measured-type metadata warnings; real geometry rows still bypass Pyogrio entirely.

### Safe network boundary

`test_safe_http.py` installs fake resolver/socket/TLS/HTTP behavior. It proves URL rejection before DNS, case-insensitive header uniqueness, rejection of credential and caller-owned hop-by-hop headers before DNS, all-address public DNS validation, numeric socket binding without re-resolution, peer checks, original Host/SNI/certificate identity, redirect revalidation/loops/limits, safe ordinary-header forwarding, and proxy independence without live network.

Source-adapter tests patch the adapter-local `open_safe_https` symbol with in-memory responses. They verify adapter-specific URL/config identity, payload validation, hashes, cache hits/misses, and controlled errors rather than retesting TLS internals.

### Cache and recovery fault injection

Tests monkeypatch `Path.replace`, link/junction predicates, open/unlink calls, and publication helpers to inject first-publish failure, replacement failure, rollback success/failure, stale `.bak`, unsafe `.part`, and cleanup failure. IGN/GPU extraction regressions prove stale backups stop the next run, double-failure recovery bytes survive, temporary roots cannot redirect through links/junctions, and archive destination inventories are complete before extraction. Assertions include exact old/recovery bytes and zero-network behavior on the next run.

### Determinism and immutability

Tests reorder rows/input mappings, deep-copy source objects, mutate coordinated hashes/manifests, and compare exact output frames. Frozen dataclass/Pydantic structures are recursively walked to reject reachable built-in mutable collections; tuple, immutable-mapping, and frozenset tests require append/item/update/delete/set mutations to fail immediately, and caller-owned nested payload aliases are mutated after validation. Artifact-integrity tests reject mutable/custom leaves, collection views, sets, NumPy objects, non-finite floats, cycles, and non-string mapping keys; they also prove immutable mapping copy/deep-copy identity, Pydantic deep-copy safety, unchanged canonical JSON dumps, and retained physical schema/CRS comparison. Deterministic tie handling, JSON ordering, pair ordering, section partitioning, and hash payload order receive permanent regressions.

### Lightweight versus source-complete validation

Planning tests instrument heavy validators and physical reads. Malformed local result/manifests must fail before source-complete calls. Artifact loaders validate exact upstream envelopes, rebuild once, and perform zero heavy physical validation; independent public source-complete validators are tested separately.

Planning completeness tests remove each zoning-summary family, mutate reconstructed values, omit/duplicate/cross-chapter required articles, inject body-page extraction errors, and retain blank successful pages. One complete synthetic physical test exercises GPU archive/extraction, configured inspection, zoning intersection, PDF indexing, regulation structure, source-locked policy, interpretation, and final validation without monkeypatching the zoning validator.

## Fixtures and helpers

Test helpers are not production APIs. Companion documents list each helper and meaningful nested callback. Common patterns include:

- `tmp_path` for isolated filesystem/cache state;
- `monkeypatch`/`unittest.mock.patch` for DNS, HTTPS, filesystem failure, validator call counts, and source-bound seams;
- frozen dataclass `replace` for coherent mutation;
- Pydantic revalidation rather than unchecked model-copy mutation where the test requires a valid alternative;
- GeoDataFrame equality/WKB snapshots for nonmutation;
- canonical hash/manifest rebuilding so a test isolates the intended semantic gap instead of failing on a cheap stale hash;
- synthetic GPKGs containing both configured physical layer A and structurally compatible alternate B.

## Regression proof standard

A strong regression demonstrates the old fail-open path and isolates the corrected boundary. For example, a wrong physical layer must be a real layer in the same verified package with a coherent summary; an artifact mutation must update its physical Parquet and manifest hashes; a rollback test starts from a valid reusable pair and byte-compares recovery copies; a network rejection asserts the unsafe destination was never requested.

## Full-suite and focused validation

Tickets normally run focused files first for fast causal feedback, then the explicitly required full suite. Repository gates are:

```text
uv run pytest -q
uv run ruff check .
uv run ruff format --check .
uv run mypy src
uv lock --check
uv pip check
uv run python -m compileall -q src tests
git diff --check
```

Tests must remain offline unless a ticket explicitly authorizes real acquisition. Current source suites use fake transport or verified cache paths; a unit test name is not evidence that live external access occurred.

On this Windows environment, every Pytest invocation supplies a fresh unique `--basetemp` under `%LOCALAPPDATA%\LandScout\pytest-runs`; the broken default `pytest-current` path is not reused. STEP 7F.1B.3 runs the 399-case existing INPN baseline first, then the new geometry suite, combined INPN suites, and the complete repository (starting baseline 3,394 plus the exact new geometry cases).

Ruff checks and formats production/test Python, while `pyproject.toml` excludes `docs/code/files`. Those companions embed byte-bound exact source snapshots whose formatting must follow the documented source rather than a second formatter pass; the companion SHA/content audit is their integrity gate.

## Limits

Passing tests prove the encoded contract for the exercised source/synthetic inputs. They do not establish legal correctness, current external-source truth, grid capacity, road rights/heavy access, environmental suitability, owner identity, or a global BESS decision.

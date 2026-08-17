# Testing strategy

## Organization

All tracked tests are under `tests/unit`. Despite that directory name, many tests exercise multi-function source-complete boundaries with real Pandas/GeoPandas/Shapely behavior, temporary archives, Parquets, PDFs, GeoPackages, and deterministic result rebuilds. No separate tracked integration-test directory exists.

Every test file has a companion under `docs/code/files/tests/unit/`. Each test function section records its fixtures, source-derived setup statements, called functions, direct assertions/expected exceptions, regression purpose, and whether it uses temporary filesystem, geometry, synthetic GeoPackage, mocks, or blocked/fake network.

## Test categories

### Pure contracts and configuration

Configuration/policy tests load checked-in YAML or synthetic mutations, reject duplicate keys/extra fields/coercion/version drift, and verify exact identities/domains. Byte or canonical-config hashes are asserted only for loaders/compilers whose current source actually computes them; `load_scan_config`, for example, parses and validates the scan and referenced profile YAML without hashing their bytes.

### Geometry and frame contracts

Tests create real Shapely geometries and GeoDataFrames to exercise CRS, validity, geometry kind, area/distance/intersection, preservation, index/dtype/order, WKB, null/empty handling, and no-repair behavior. Missing-CRS fixtures intentionally produce the small pyogrio warnings visible in full-suite output.

### Synthetic physical sources

IGN/GPU tests write temporary ZIPs/GeoPackages and use physical alternate layers, layer inventories, summaries, marker files, and byte tampering. These tests are stronger than coordinated in-memory frame mutations because public revalidators must reproduce configured roles and reread verified physical bytes.

### Safe network boundary

`test_safe_http.py` installs fake resolver/socket/TLS/HTTP behavior. It proves URL rejection before DNS, all-address public DNS validation, numeric socket binding without re-resolution, peer checks, original Host/SNI/certificate identity, redirect revalidation/loops/limits, and proxy independence without live network.

Source-adapter tests patch the adapter-local `open_safe_https` symbol with in-memory responses. They verify adapter-specific URL/config identity, payload validation, hashes, cache hits/misses, and controlled errors rather than retesting TLS internals.

### Cache and recovery fault injection

Tests monkeypatch `Path.replace`, link/junction predicates, open/unlink calls, and publication helpers to inject first-publish failure, replacement failure, rollback success/failure, stale `.bak`, unsafe `.part`, and cleanup failure. Assertions include exact old/recovery bytes and zero-network behavior on the next run.

### Determinism and immutability

Tests reorder rows/input mappings, deep-copy source objects, mutate coordinated hashes/manifests, and compare exact output frames. Frozen dataclass/Pydantic structures are tested for immutability. Deterministic tie handling, JSON ordering, pair ordering, section partitioning, and hash payload order receive permanent regressions.

### Lightweight versus source-complete validation

Planning tests instrument heavy validators and physical reads. Malformed local result/manifests must fail before source-complete calls. Artifact loaders validate exact upstream envelopes, rebuild once, and perform zero heavy physical validation; independent public source-complete validators are tested separately.

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
uv run mypy src
uv lock --check
uv pip check
git diff --check
```

Tests must remain offline unless a ticket explicitly authorizes real acquisition. Current source suites use fake transport or verified cache paths; a unit test name is not evidence that live external access occurred.

## Limits

Passing tests prove the encoded contract for the exercised source/synthetic inputs. They do not establish legal correctness, current external-source truth, grid capacity, road rights/heavy access, environmental suitability, owner identity, or a global BESS decision.

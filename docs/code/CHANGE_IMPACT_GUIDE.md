# Change impact guide

Use the relevant file companions first: they list exact callers, tests, constants, fields, raises, and algorithms for the current source SHA.

## Changing a source adapter

Review the adapter config YAML/model, package exports, shared safe HTTPS boundary, cache sidecar/result dataclasses, archive/extraction validation, physical-source consumers, and all adapter tests. Preserve the ordering of cache checks versus network, before/after hashing, controlled errors, and source-complete consumers. Cadastre changes affect normalization; IGN changes affect grid/road/coverage; GPU changes affect every planning branch; INPN changes affect both fresh extraction authority and the physical metadata catalog; RTE changes affect its source envelopes.

## Changing the INPN metadata catalog

Review controlled ZIP snapshot opening, immutable archive reads, same-snapshot ZIP validation/member inventory/extraction, archive-marker-physical-caller equality, archive-path postconditions before/after publication and return, canonical download lineage reconstruction, safe package containment, one verified built-in byte snapshot per package, byte-only Pyogrio metadata calls, the exact local `/vsimem` warning filter, package/layer/field physical ordering, exact `GPKG` driver, exact metadata keys, feature-count forcing, geometry-type agreement, raw/canonical CRS, exact final optional-string and bounds types, empty/populated/non-spatial bounds rules, portable catalog hash schema, aggregate counts, final full-extraction validation, and independent rebuild comparison. Use only metadata APIs; feature readers and environmental category/parcel-policy semantics remain outside this layer. A catalog hash payload change requires an explicit schema decision and real-cache evidence must remain zero-network.

## Changing the INPN attribute profile

Review exact extraction/config/catalog runtime types, fresh catalog reconstruction, canonical relative package paths, package path/position bijection, lexical contiguous package/layer grouping, repeated package-evidence equality, exact/NFKC/casefold identity uniqueness, contiguous layer/field positions, FID extrema/capacity, package-byte helper ownership, the shared narrow Pyogrio warning context, exact `read_dataframe` options, Pandas-only frame/type/column/order/count rules, integer FID preservation and sorting, null detection, the closed text/Boolean/integer/float-hex/Base64 scalar representation, unsupported composite/temporal/geometry failures, complete distinct domains/frequencies, FID/column/row/profile canonical JSON hashes, deterministic empty-component hashes, aggregate closure, the cheap fresh-catalog preflight before attribute reads, final extraction/catalog postconditions, and independent physical rebuild. Column hashes bind only ordered FID-addressed canonical cells; field identity/dtypes are separate complete-profile facts. Intrinsic validation checks non-empty component-SHA syntax but physical validation reconstructs those hashes. EP remains distinct from Natura 2000 and ZNIEFF; category meaning, geometry loading, parcel relations, exclusions, and scores remain outside this layer.

## Changing source configuration

Review strict Pydantic fields/validators, recursively copied tuple/frozenset/immutable-mapping values at every depth, input-alias isolation, duplicate/extra-key handling, URL origin/path locks, exact provider/product identities, strict finite numeric fields, expected size/SHA/checksum, cache identity, logical-role uniqueness, source lineage copied to frames/results, immediate mutation-operation regressions, and any persisted source/result hashes. Explicit field serializers must preserve the established plain JSON/Python shape used by canonical hashes. Public operations must still reconstruct/revalidate configuration at the trust boundary. GPU config changes also change its canonical config SHA and every planning document that retains it.

## Changing strict serialization

Review every trust-bearing YAML/JSON reader, not only source config files. YAML mappings must reject duplicate keys at any depth. JSON must use strict UTF-8, reject duplicate keys/non-finite or overflow numbers, and require an object where the schema expects one. Re-run config/policy, HTTP-response, cache/marker, and planning-manifest regressions; deterministic writers and existing valid bytes should remain unchanged.

For immutable artifact-integrity mappings, review both parser input and in-memory model construction. Recursively accepted values are only null, exact strings, booleans, integers, finite floats, exact-string-keyed mappings, and ordered lists/tuples. Unsupported leaves, collection views, cycles, sets, binary values, and NumPy objects fail validation; they are never retained or stringified. Re-run copy/deep-copy identity, Pydantic deep-copy, plain JSON dump, physical schema/CRS comparison, schema-version, and canonical-hash locks together.

## Changing `safe_http`

Review all five adapter call sites and `test_safe_http.py`. Preserve HTTPS-only identity, localhost/numeric-IP handling, all-address DNS validation, no re-resolution, numeric socket endpoint, peer verification, default TLS verification, original SNI/Host, case-insensitive header uniqueness, pre-DNS rejection of credentials/caller-owned hop-by-hop headers, safe ordinary-header redirect behavior, proxy independence, redirect ownership, 2xx-only completion, streaming, and response/connection cleanup. Run every source-adapter suite because transport error translation occurs there.

## Changing CRS or geometry logic

Review `geo/crs.py`, `geo/geometry.py`, all normalization stages, both proximity/coverage pairs, planning zoning/features, aggregation parcel-area checks, and geometry tests. Distinguish stored versus calculation copies. Check CRS equality/canonical-representation expectations, force-2D location, Z preservation, valid geometry kinds, null/empty/invalid behavior, WKB preservation, units, minimum rotated rectangle, centroid semantics, overlay tolerance, and boundary equality.

## Changing a normalized schema

Search for the exact ordered column constants and dtype maps. Review builders, intrinsic validators, source-complete validators, code resolver, policy application, aggregation, hashes/schema signatures, Parquet manifests, empty-frame builders, and every test that removes/reorders/retypes a column. A validation-only change must not cast malformed loaded artifacts or alter valid output hashes.

For parcel zoning, `PARCEL_ZONING_OUTPUT_COLUMNS` is a complete required summary contract even when unrelated pass-through parcel columns exist. Any addition/removal requires builder, reconstruction, validator, public export, interpretation, and one-missing-column-family regressions to move together.

## Changing DataFrame columns

Review introduction, exact dtype/nullability/domain, index/CRS/geometry preservation, relation-to-feature comparisons, canonical frame hashing, artifact schema signatures, selectors/profilers, package exports, and companion data-contract tables. Search exact string occurrences across `src` and `tests`; do not rely only on Python imports.

## Changing a public stage signature

Review `src/landscout/stages/__init__.py`, all direct tests/callers, source-complete ownership, call-count regressions, mocks patched at the consuming module, and documentation flows. Do not reintroduce weaker overloads accepting arbitrary normalized frames, caller proximity results, caller coverage, or compiled policy objects where current APIs own those sources.

## Changing planning source locks

Review canonical GPU config identity/hash, document/archive/extraction/spatial-role/written-file identity, planning index/structure locks, exact source excerpts/page/offset/fragment hashes, complete zoning summaries, configured required articles per chapter, body-page extraction status, policy config source locks, complete result hashes, artifact manifests, and source-complete rebuild tests. Source locks describe approved evidence; changing them requires independent source verification, not only updated expected values.

## Changing policy YAML

Review the relevant compiler's strict model, evidence sources, exact pair/chapter/route completeness, precedence, official meaning agreement, applicability/context, interpretation/legal flags, policy byte hash, result hashes, downstream application/aggregation, ignored generated artifacts, and permanent source-excerpt tests. Do not update expected hashes merely to silence a semantic failure.

## Changing a policy schema

Review Pydantic schema-version Literals/validators, checked-in YAML, result schema/hash versions, artifact manifest source locks, loaders, compatibility validators, older-version rejection tests, docs, and migration strategy. A new schema version is a compatibility contract and must not be used for validation-only hardening without need.

## Changing a hash schema

Review canonicalization, null/geometry/index/dtype serialization, component ordering, complete-result closure, manifest roles, source lock comparison, artifact loaders, exact pinned hashes, and all coordinated-mutation tests. Keep physical-byte hashes distinct from canonical frame/content hashes.

## Changing cache metadata

Review strict schema/version/type validation, duplicate-key handling, timestamp rules, source/config identity, size/SHA equality, current physical validation, cache-hit reconstruction, invalid-cache refresh tests, and compatibility with existing verified caches. Cache metadata cannot authorize bytes that fail current physical checks.

## Changing recovery logic

Review final/archive/metadata existence combinations, `.part` link/junction/directory handling, exclusive creation, stale `.bak` fail-closed behavior, first publication, replacement, partial publication, rollback success, rollback failure, useful backup byte preservation, next-run zero-network behavior, cleanup precedence, and recovery-state tests for Cadastre/RTE/IGN/GPU/INPN.

## Changing tests

Preserve the contract being tested, not only pass status. Ensure a mutation is otherwise coherent when it is meant to isolate a semantic/source gap. Keep network fully fake/blocked unless authorized. Avoid tests that pass for a cheaper stale hash/schema/summary defect. Update the companion test section and rerun focused plus required full/static gates.

Planning integration changes must retain at least one real synthetic physical chain without monkeypatching `validate_normalized_planning_zoning_inputs`; isolated monkeypatched unit tests remain useful but cannot replace the source-complete chain.

## Changing package exports or version metadata

Review the exact `__all__` contract for `landscout.sources` and `landscout.stages`; source-bound Cadastre and factual zoning high-level results/errors must not be replaced by raw-path helpers. Verify `landscout.__version__` equals `project.version` in `pyproject.toml`, not merely that both values are present.

## Changing documentation

Recompute companion SHA256 after any source/project-file byte change. Re-run file/symbol/test completeness audits, verify links/Mermaid/Markdown conflict markers, and remember that `docs/DEV_LOG.md` is historical evidence rather than current implementation authority. `docs/code/files` is deliberately excluded from Ruff because companions reproduce exact source snapshots; do not format those embedded bytes independently of their source.

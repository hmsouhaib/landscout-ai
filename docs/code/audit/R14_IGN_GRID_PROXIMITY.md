# R14 — IGN electricity proximity documentation

Local bounded documentary lot complete; independent R14 review **PENDING**, global audit **PARTIAL**. This receipt does not approve a functional step, connection feasibility or a parcel score. The [exact R14 instruction](../../project/tickets/DOCS.CONTINUITY.1.R14.txt) is the authority for this seven-path change. Final commit identity is resolved through Git after publication, not embedded as a future self-SHA.

## Readiness and ownership actually observed

Repository C:/souhaib/landscout-ai; branch recovery/docs-continuity-1-partial; clean starting HEAD/local tracking/actual server recovery ref 8afba19df0f6748bf0d5927668b5114e36bb8fb3. Local main, origin/main and actual server main were aa4ebc7063f2abdfcbae95154ba89b5b1a0dba02. Root, empty index/worktree diff, no unmerged entries or active Git operation were checked before editing. A network Git attempt first failed; a subsequent command exposed the actual dubious-ownership error. Only the authorized per-command safe.directory exception for this exact repository was used for the successful remote query; no persistent trust/ACL/security change occurred.

The original matrix and every review fragment identify foundations.json as the sole owner. There are **two explicit file rows**, not four: the two companion units use their source/test row's embedded documentation status. No transferred-to intention is counted as another owner.

| Original unit | Actual initial state | Final local state | Original symbols |
|---|---|---|---:|
| src/landscout/stages/enrich_grid_proximity.py | READ; read_complete=true | CHECKED; true | 64 |
| tests/unit/test_enrich_grid_proximity.py | READ; read_complete=true | CHECKED; true | 77 |
| docs/code/files/src/landscout/stages/enrich_grid_proximity.py.md | Embedded READ; documentation_read_complete=true | Embedded CORRECTED; true | 0 |
| docs/code/files/tests/unit/test_enrich_grid_proximity.py.md | Embedded NOT_READ; documentation_read_complete=false | Embedded CORRECTED; true | 0 |

All existing symbol notes were read. The 29 acquired production-function explanations were reused where accurate; prior generic class/field/test READ notes are replaced with source-specific notes, not treated as previous semantic closure. Prior row metadata and canonical symbol-list SHA are retained with the starting commit under r14_prior_evidence. Companion hashes bind exact Git-content bytes; only these two owner objects change.

## Files and identity

- `docs/code/files/src/landscout/stages/enrich_grid_proximity.py.md`
- `docs/code/files/tests/unit/test_enrich_grid_proximity.py.md`
- `docs/code/audit/reviews/foundations.json`
- `docs/code/audit/R14_IGN_GRID_PROXIMITY.md`
- `docs/project/tickets/DOCS.CONTINUITY.1.R14.txt`
- `docs/code/audit/DOCUMENTATION_AUDIT.md`
- `docs/project/CURRENT_STATE.md`

| Binding | Git OID at start | SHA256 |
|---|---|---|
| src/landscout/stages/enrich_grid_proximity.py (unchanged) | `cdc98d5da0b58e420beff08175c2f67ac71e2070` | `7131d0b980dad7b5c73a4c7cf2d0bd6f9fe5572c089ad39c4a592c02098c9015` |
| tests/unit/test_enrich_grid_proximity.py (unchanged) | `151b6bc7df1aeeab6bbdb653dc5b2ebfbeddc196` | `436de7dd475f09b28356502b0b4eaed66ead17253da7bf6d3869aaf8bbcee728` |
| docs/code/files/src/landscout/stages/enrich_grid_proximity.py.md (corrected companion) | Not a source binding | `fe1ab0f83c66805ac47c2f6aa6d3af9be9ea37fddad5b796bdc9d583e92020d4` |
| docs/code/files/tests/unit/test_enrich_grid_proximity.py.md (corrected companion) | Not a source binding | `9cf3e33155a3bcc0f8f4e1858668ac6d83ef84c8da8eb142eadf33f8992c6054` |

No application signature, hash/schema version or business rule changed. The component declares neither an artifact loader nor its own manifest/hash domain. Its source module has no __all__; stages re-exports six classes and two functions.

## Actual reading, not dependency closure

Read production 1–1092 and tests 1–1470 completely. Read every unique explanation/table/interface in the starting companions (869 unique nonblank nonfenced source-prose lines and 1,067 test-prose lines, with occurrence locations), rereading useful truncated spans. All 238 original fenced blocks remain and are mechanically matched to already-read source content; two full snapshots match exact source bytes. Repeated snapshots are not claimed as another independent semantic read.

Read AGENTS.md, WORKING_RULES, RESUME, CURRENT_STATE, BACKLOG_AND_GAPS, DOCUMENTATION_AUDIT, preservation authority, R13 receipt and this exact ticket. Unchanged historical STEP_INDEX, DECISIONS, BACKLOG and code README were reused only after exact Git-byte identity checks against their previously read versions. The supplied R13 approval is recorded successorily in CURRENT_STATE by reference to R14 section 1, without rewriting historical PENDING receipts or awarding coverage.

Contextual dependencies read, with no file/symbol closure credit:

- normalize_grid_ign.py: 1–160, 164–795 (the public normalization/revalidation chain, exact frame comparisons, source context, factual output and summaries).
- ign_bdtopo_fr.py: 149–215, 242–319, 396–473, 1034–1654, 1936–2003, 2019–2148, 2329–2365 (config/source envelopes, metadata/extraction validation, loader and physical postconditions).
- assess_grid_coverage.py: 770–816 (public consumer calling the source-complete proximity API before its own separate coverage flow).
- stages/__init__.py: 49–58 plus AST membership of the eight names in package __all__. No full package-init semantic audit is claimed.
- All fourteen fixture/helper definitions are local to the fully read test file. No imported application is run outside the single authorized pytest invocation; static checks parse source without application import.

## Reconciled contracts and documentary corrections

R14-D01 — Public, private and profiling boundaries are explicit. Public enrichment checks parcel GeoDataFrame and exact source/config types, validates parcels and collisions, calls the normalizer once, checks its exact result type and delegates computation. GridProximityError is preserved; every other Exception is wrapped. The normalizer call is followed through actual local extraction/GPKG/inventory hashing, configured-role rediscovery, physical reads and comparison/postconditions. Archive metadata validation is not a reread of .7z archive bytes; a malformed input can fail earlier. One call is not one file read.

R14-D02 — The numerical helper requires usable line and polygonal-post catalogs; only the exact-voltage branch is optional. Calculation copies use EPSG:2154 and force_2d, while output keeps original geometry/CRS/columns/order on a reset RangeIndex. There is no special zero-parcel early return in _nearest_feature_rows. All equidistant nearest matches are requested; stable parcel-position/distance/lexical-ID ordering chooses the representative with exact tie counts and no invented epsilon. Unknown/bounded voltage never becomes exact voltage. The eleven-column level table is level-major with ascending levels and original parcel order.

R14-D03 — Frozen dataclasses do not freeze their DataFrames or validate annotated constructor values. Twenty-nine field notices now give required/default/type/null/unit semantics. Numeric validators reject bool, unsupported/nonfinite/overflowing values where implemented; tie counts admit integral finite Real values while coverage counts require Integral excluding bool. Result/profile validation reconciles retained evidence locally, without source reacquisition or proof of arbitrary metadata truth. Profiling builds level profiles before constructing broad/exact/post summaries. Nine quantiles plus min/max describe present distances; summary tie_count counts tied rows, not tied features.

R14-D04 — All 77 helper/test notices identify the actual called boundary and concrete setup/assertions. In the tests the short enrich_parcel_grid_proximity alias names the private helper; public_enrich_parcel_grid_proximity names the public entry point. Package call references now name the defining owner. SOURCE_CONFIG reads YAML at import; argument-or-default helpers do not construct empty frames from empty lists. Temporary GPKG writes/layer reads are attributed correctly, and string/null/list comparisons no longer masquerade as hashing or spatial calculations. Existing exact decorators, signatures, parameter tables, raises/assertions, call evidence and code blocks remain.

## Test-evidence limits retained

- **R14-T01 — Public mocked orchestration.** The once-normalizer test supplies a return_value, not a delegating spy; its bundle contains placeholder extraction/summaries. The failure test raises a ValueError sentinel. Wrong-type/collision cases assert the mock was uncalled. None of these establishes physical verification or disk-read counts.
- **R14-T02 — Physical fixture is synthetic.** Real temporary six-layer GeoPackages have consistent extraction hashes/inventory, but no named archive bytes. Alternate roles are a rejection scenario; eleven altered archive/config lineage cases can fail before extraction reads and assert no private computation. This is not successful official-source enrichment.
- **R14-T03 — Local result checks.** Mutable main/long tables and coverage are altered, then the public profiler checks its local contract. Missing/invalid data may fail earlier than cross-representation reconciliation; bad coverage values precede the incidental table-size mismatch. No hash resealing or fresh IGN query occurs. Optional manager/state nulls can consistently agree.
- **R14-T04 — Geometry/order assertions are bounded.** Zero-tolerance XY predicates and has_z do not prove every Z/M ordinate or WKB byte. Parcel rows/ID order survive, but indices reset. The nonvalid-line test checks one retained parcel and chosen VALID feature, not preservation of the distance-catalog line rows. The multi-geometry test asserts row count only.
- **R14-T05 — Numerical assertions are bounded.** The all-status test checks copied status, not raw parsing or a populated upper bound. The Cartesian test checks per-level order, not the entire inter-level sequence separately. The profile example asserts min/median/max, not every quantile. Seven invalid tie values exclude bool, while the coverage-count cases include True. No exact voltage means one parcel with missing exact evidence, not an empty parcel fixture.

These are documentary proof limits, not newly demonstrated application defects. BACKLOG_AND_GAPS is unchanged; no A-005 or production repair is invented. Preserve A-001..A-004, the five historical limits, R3-T01..04, R9-T01..04, R10-T01..04, R11-T01..05, R12-T01..05, R13-T01..05 and OPEN R5-D01. Independent/cold-start/visual/global acceptance and exhaustive 7F.1C.1 semantic review remain pending. Last approved functional boundary remains 7F.1B.4, with the original receipt gap retained.

## Unique focused execution

Executed once in the installed environment, with authorized access to the user uv cache and isolated LOCALAPPDATA directory:

```powershell
uv run --no-sync pytest -q tests/unit/test_enrich_grid_proximity.py --basetemp "C:\Users\souha\AppData\Local\LandScout\pytest-runs\r14-ecc3f0bf"
```

Observed **174 passed in 9.96s; native exit 0 after cleanup**. No warning/skip/xfail was reported; stderr is empty. No retry, full suite, other test, uv sync/install, source download, Muret pipeline or actual-source profiling was run. Synthetic GPKG I/O is the authorized test behavior. No claim is made that every process file access is confined to basetemp or that all old temporary directories were removed.

- Local log `C:/souhaib/r14-pytest.stdout.txt`: 530 bytes, SHA256 `f921cfea818d245cea7d5d315380728e0e45c16be701a18e5c373f2f043e7401`.
- Local log `C:/souhaib/r14-pytest.stderr.txt`: 0 bytes, SHA256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

## Static reconciliation and preservation

Temporary tooling stays outside the repository. Bounded checks pass for 141 symbol/qualified-owner/signature/range/unique-anchor/note mappings (64 production: six classes, 29 fields, 29 functions; 77 tests/helpers: fourteen helpers and 63 tests), exact source SHA/basis, companion hashes, JSON strictness, Markdown tables/IDs/links/incoming links/qualified references, Unicode and two complete snapshots. All 238 original code blocks and old anchors remain. Before continuity records, checks observed 141 explicit IDs, 196 headings, 64 local links, two incoming companion links, 1,019 qualified references with zero unresolved, 2,468 table lines and thirteen strict JSON files; these are scoped pre-record counts, not the full-auditor totals. Final staged checks repeat the bounded invariants.

All 106 protected files retain main/start/index OIDs and authoritative checkout hashes. Of 310 starting tracked paths, **305 outside this seven-path authorization** remain unchanged. Distinguish Git bytes, index bytes and checkout bytes: the two historical EOL exceptions remain exactly recorded, not normalized:

| Exception | Git-content SHA256 | Checkout SHA256 |
|---|---|---|
| configs/planning/muret_bess_zoning_policy.yaml | c736ea8901997f4852fd1f72a3f6f34282452f18dcd9abc0ccbce8255adaad45 | 879d50627c063bb10096950d004cf4d4e446ff04ef9a1178b3e3fb28e2ffdae3 |
| docs/project/tickets/DOCS.CONTINUITY.1.RESUME.2026-09-17.txt | b5a0fa80569fbc0b11d28718c0037f9e8ba23caac5dadca6fd60c05c7cc64a5b | 9e18c25d571c5cfe34391d1f35833634bb4c3672087781360752fa0fba7243ed |

The thirteen inherited main-to-start whitespace observations remain byte-identical; the new diff passes git diff --check. No source/test/config/auditor/dependency/cache/data/old receipt/backlog/matrix/coverage bytes are committed as changes. No visual renderer was exercised; inherited renderer availability limits remain PENDING, not a Markdown visual pass.

## Recount, single INDEX candidate and receipt delta

Actual deduplicated recount: 103 → **107/245** closed files, 2,834 → **2,975/4,769** closed symbols. Gain four original units/141 original symbols. Files CHECKED44/CORRECTED63/READ136/NOT_READ2; symbols CHECKED2,974/CORRECTED1/READ1,794/NOT_READ0. Remaining **138 files / 1,794 symbols**. Dependencies, module constants/imports, ticket/receipt and R13 approval award no credit. No global coverage/matrix regeneration or merge occurred.

After staging only the seven explicit paths, run the unchanged full auditor once. This subsection's placeholder is the only intended post-candidate change; compare receipt prefix/suffix and every path/mode/OID, not a fictional second full audit. The actual available R13 stdout/stderr and manifest provide the comparison baseline; 10,218 is historical, not a target.

The single full run finished with **native exit 1 / completed=true / 10,217 findings**. This is completed execution with global PARTIAL findings, not timeout/exit2 or a green global audit. Candidate manifest (sorted path/mode/OID, compact JSON UTF-8 SHA256) is **`7e880ed6dd97d41d32f7bfc85b7c2c9c7698224fd9b23c7e41a8b392285f6546`**: 312 paths, 309 unique blobs, 27,595,284 bytes; 94 Python files / 94 AST parses / 4863 actual symbols, historical coverage denominator 245 files / 4769 symbols, 5 Git processes. The tool and index remained unchanged during that run.

Compared by finding-line multiplicity to actual R13 logs: **10,215 occurrences unchanged, 3 removed, 2 added** (10,218 → 10,217). Removed: ambiguous companion line-ending basis for each of the two Python files, plus the old inventory-mismatch line. Added: the inventory line now also lists the new R14 ticket, and stale file fingerprint for the modified test companion. coverage.json still stores its original 86847a03c0cc45e48b936a78cba50628542644fe6ec8a9d2ebd02d2b75dc7539 fingerprint; it is deliberately unchanged/unmerged. The current foundations owner correctly stores 9cf3e33155a3bcc0f8f4e1858668ac6d83ef84c8da8eb142eadf33f8992c6054. This is a real stale global-ledger binding, not a stale active-owner note, and not a reason to modify the forbidden ledger. The source companion fingerprint was already stale in the baseline.

Candidate categories: ambiguous basis84; bad local link3; DEV_LOG companion parser findings2; export inventory mismatch24; inventory mismatch1; missing companion exception131; missing documented anchor4,769; missing exact source snapshot8; semantic-ledger-not-COMPLETE1; stale fingerprint124; unfinished history1; unresolved qualified reference54; unresolved file review245; unresolved symbol review4,769; unchanged checkout/EOL diagnostic1. Most closure diagnostics read the unmerged global ledger, not the current review fragments. Existing unresolved references, links, export/exception/snapshot issues remain global work; known literal-domain reference false positives stay documented in their earlier receipts and their exact domain strings are not removed. No unresolved qualified-reference finding names this proximity lot. The 10,215 common occurrences were not silently relabeled as all harmless or all repaired.

The exact R13 comparator is its candidate, before its later receipt completion: manifest f1e37d11bf6e99e14a690d7726399baf52b8e72e82cec7b1859b6d37952b073b, completed=true, exit1, 10,218 findings. R14's starting committed tree instead has manifest 5b465eb512bd2b30b461e5e61bc3f1ab0eda316eb26dd46def8d5b30047936af. This distinction is retained.

Local immutable evidence files (outside Git):

- `C:/souhaib/r14-candidate.stdout.txt`: 2,300,022 bytes; SHA256 `bf55d589877a34da0d7aef8d6728b1efc5406936d4590c8009eb8b1c9d5a9be1`.
- `C:/souhaib/r14-candidate.stderr.txt`: 64,100 bytes; SHA256 `51acd78090a8e866f5419998bf4ec6ecd1143c7d3b239335101d75144b506766`.
- `C:/souhaib/r14-candidate.manifest.json`: 80,238 bytes; SHA256 `ec2b401c9a43acbb8c8749dfe24db468d45e1caa8abaea9d3e853391984a869a`.
- `C:/souhaib/r14-compare.json`: 10,370 bytes; SHA256 `ba7668d1635057990ef6daf01d070880749b5087ff161f8fd5922434a285f669`.
- `C:/souhaib/r14-static-index.json`: 4,426 bytes; SHA256 `c9c4e401684cd01f9d021d5527bf53712764fc61673ea71a135b59cb840f6017`.
- `C:/souhaib/r13-candidate.stdout.txt`: 2,300,086 bytes; SHA256 `9acb8bc66c0eab0debb01b8216354fd80cb2f758b0f1b189aeb51884dde58054`.
- `C:/souhaib/r13-candidate.stderr.txt`: 63,988 bytes; SHA256 `eedb9d4e97c1229d2690b107ff20881579ecefce50a1b91766e87678fdacb612`.
- `C:/souhaib/r13-candidate.manifest.json`: 79,732 bytes; SHA256 `29ca2f9ea60f579cbe5d61cc598c00bd9f3a6ea584f2be38c376267918285e75`.

Candidate receipt before completion: OID `b2f20739833d60cfec4173bbaf631ba453ae3f6b`, 15,329 bytes, SHA256 `81e1f02d39855efa92367863dd4c000ab57777c2b212d27751991e58bd586bdd`. Only the dedicated auditor placeholder is replaced after the run. Bounded post-completion verification checks the unchanged prefix/suffix, single changed receipt path and all other exact candidate path/mode/OIDs; its observed delta and final manifest are stored outside the receipt to avoid self-hashing circularity. No second full auditor is run and no final-tree finding count is invented. The final report supplies the actual publication SHA and verified clean/tracking/server/main result after those operations.

## Publication and stop boundary

Publish only this completed documentary lot on recovery/docs-continuity-1-partial, message `docs: audit IGN grid proximity reference`, then verify clean status, HEAD/local tracking/actual server equality and unchanged main. R14 independent review remains PENDING. The first sorted remaining NOT_READ unit is docs/code/files/tests/unit/test_ign_bdtopo_fr.py.md, identified only, not started or automatically authorized. Do not start normalization/coverage/road work or another functional step.

# R15 — IGN BD TOPO source documentation

Local bounded documentary lot complete; independent R15 review **PENDING**, global audit **PARTIAL**. The [exact received instruction](../../project/tickets/DOCS.CONTINUITY.1.R15.txt) authorizes this eight-path documentation change, not a new functional step. Publication identity must be read from Git after commit; this receipt contains no future self-SHA or claim of independent self-approval.

## Readiness and actual ownership

Repository C:/souhaib/landscout-ai; authorized branch recovery/docs-continuity-1-partial. Clean starting HEAD, local tracking and actual server recovery ref: 8bef62ab9b6eef185bab526a046b4a7dbbea42a1. Local main, origin/main and server main: aa4ebc7063f2abdfcbae95154ba89b5b1a0dba02. Root, index/worktree, unmerged entries and Git-operation markers were checked before editing. An initial escalated remote query failed; a diagnostic exposed the actual dubious-ownership error. The successful query then used only the authorized per-command safe.directory=C:/souhaib/landscout-ai exception. No persistent trust, ACL, security, environment or dependency change occurred.

Original matrix and all review fragments establish foundations.json as sole actual owner. There are two explicit source/test rows; their companion units are represented by embedded documentation fields, not two extra rows. No transferred-to intention or duplicate declaration grants credit.

| Original IGN unit | Actual initial state | Final local state | Original symbols |
|---|---|---|---:|
| src/landscout/sources/ign_bdtopo_fr.py | READ; read_complete=true | CHECKED; true | 250 |
| tests/unit/test_ign_bdtopo_fr.py | READ; read_complete=true | CHECKED; true | 105 |
| docs/code/files/src/landscout/sources/ign_bdtopo_fr.py.md | Embedded READ; documentation_read_complete=true | Embedded CORRECTED; true | 0 |
| docs/code/files/tests/unit/test_ign_bdtopo_fr.py.md | Embedded NOT_READ; documentation_read_complete=false | Embedded CORRECTED; true | 0 |

All 355 original symbols were READ, not previously closed. Production has 26 classes, 157 fields and 67 functions; tests have one class and 104 functions, including 76 top-level tests. Generic class/field/test notes were reconciled with concrete bodies rather than promoted automatically. The 67 prior production-function explanations were reused where accurate, with the cache rollback and cleanup limits corrected. r15_prior_evidence retains exact prior nonsymbol row values and the canonical prior-symbol-list fingerprint tied to the starting commit. The two existing source hashes and exact signatures/ranges remain unchanged.

## Files and bindings

- `docs/code/files/src/landscout/sources/ign_bdtopo_fr.py.md`
- `docs/code/files/tests/unit/test_ign_bdtopo_fr.py.md`
- `docs/code/files/tests/unit/test_enrich_grid_proximity.py.md`
- `docs/code/audit/reviews/foundations.json`
- `docs/code/audit/R15_IGN_BDTOPO_SOURCE.md`
- `docs/project/tickets/DOCS.CONTINUITY.1.R15.txt`
- `docs/code/audit/DOCUMENTATION_AUDIT.md`
- `docs/project/CURRENT_STATE.md`

| Binding | Starting Git OID | Current SHA256 |
|---|---|---|
| src/landscout/sources/ign_bdtopo_fr.py, unchanged | `876207e3b1b0ac4c1a245c01fdad91e72e5bb4d3` | `598df901cd8dfe543595f22ff511b511a196f345474acd6355d7929a7a512101` |
| tests/unit/test_ign_bdtopo_fr.py, unchanged | `560c3ec1774ec514e77f58e1f9a63ec6599de2db` | `39d0e303aec55a24866a2c41b32bdb215203b4280fb748421454120eae24f078` |
| tests/unit/test_enrich_grid_proximity.py, unchanged | `151b6bc7df1aeeab6bbdb653dc5b2ebfbeddc196` | `436de7dd475f09b28356502b0b4eaed66ead17253da7bf6d3869aaf8bbcee728` |
| docs/code/files/src/landscout/sources/ign_bdtopo_fr.py.md, corrected prose | Not a source binding | `6a4c441fac22a6d71171e84bf42e2b0a5c2da0e8e5574a18fb089f5f9a6b894b` |
| docs/code/files/tests/unit/test_ign_bdtopo_fr.py.md, corrected prose | Not a source binding | `f4ac55a98498fcac75098f9cb05116ffd57068a854145e7d2979d6aa18613f83` |
| docs/code/files/tests/unit/test_enrich_grid_proximity.py.md, corrected prose | Not a source binding | `92041d7deea354cd23cd3c89d40c5b52d338a82aa2e5f21232ffb14ff4eb55ff` |

For these source/test/companion files, exact Git/index/checkout bytes agree after staging; hashes use Git-content bytes. The separate protected-file manifest retains the historical checkout-vs-Git EOL distinction, not normalized bytes substituted for a source binding. No application API, metadata schema, canonical hash or business rule changes. Download metadata remains schema 1, extraction metadata schema 3; no INPN/GPU protocol is substituted.

## Read method and contextual dependencies

Read production 1–2484 and tests 1–2209 completely at the starting version. Read every unique companion explanation/table/interface with source context: 1,965 nonblank nonfenced unique production-prose lines and 1,309 test-prose lines, occurrence locations retained during inspection; truncated output spans were reread. Existing 182 production and 217 test fenced blocks are retained and matched to already-read source content; the two full snapshots equal exact source bytes. Repeated code is mechanically compared, not presented as a second independent semantic reading.

Read AGENTS, WORKING_RULES, RESUME, CURRENT_STATE, BACKLOG_AND_GAPS, DOCUMENTATION_AUDIT, R14 receipt, preservation authority and this ticket. STEP_INDEX, DECISIONS, BACKLOG_AND_GAPS and code README historical readings were reused only after exact-byte comparison with the recorded earlier base. No prior PENDING receipt is rewritten.

Contextual reading only: complete shared safe_http/strict_json/strict_yaml definitions; sources package imports/__all__; electricity/road normalizer public revalidation paths; grid proximity public orchestration and grid coverage loader call; road policy application/proximity/coverage call chains. This follows the actual transport, strict parser and physical source owners, not another adapter's rules. It grants no dependency closure or new application execution.

## Concrete documentary corrections

- R15-D01 — Sequential cache publication and asymmetric rollback: archive replacement can be rolled back; old metadata remains in place if metadata replacement fails. There is no metadata_backup-to-primary restore call. Backup cleanup inside the publisher can raise; the outer temporary-file cleanup preserves active primary errors for its caught OSErrors. No general atomicity/concurrency-lock guarantee.
- R15-D02 — Explicitly separate HttpUrl/model validation from shared DNS-to-socket HTTPS transport, optional pins from local SHA, UTC cache age from lineage timestamp parsing, physical archive validation from current GPKG/tree pre/post checks, and path-based reads from immutable-byte snapshots. Cache hits avoid transport but not disk/CRC/hash work; size checking follows streaming, not an early download budget.
- R15-D03 — Complete class/field ownership and defaults; frozen Pydantic tuples versus frozen dataclasses containing mutable frames/files. _ExtractedEntryMetadata has no kind/size/hash cross-validator or path grammar: the inventory builder and physical comparison supply that consistency. Coverage summary versus selected frame and the two currently uncalled coverage helpers are distinguished. No application defect is inferred from that local model description alone.
- R15-D04 — Replace generic test titles with 105 concrete class/helper/callback/test notices and linked scenarios for the 76 top-level tests. Preserve direct assertion counts without confusing assertion-helper calls, fixtures or nested callbacks with new tests. Record first possible rejection and limits of mocked transport, fake headers, predicate-simulated links, stale hashes and selected geometry equality.
- R15-D05 — Correct inherited Pydantic model method ownership and the strict-JSON helper's defining module; source_config parameters are injected model values, not fixture-callable methods. Exact package imports/__all__ expose 29 IGN names; the module itself has no __all__, and the untrusted reader/AccessConfig/private revalidators are not package exports.
- R15-D06 — Correct side-effect descriptions: pyogrio.write_dataframe and archive.write do write synthetic files; read_text and with_name do not; bytes.replace is in-memory, write_bytes changes disk; py7zr is in-process, not a subprocess. Original source code and snapshots are unchanged.

The raw reader and electricity/road loaders preserve NULL/EMPTY/nonempty-invalid geometries without repair or VALID-only filtering. Department selection instead requires exactly one valid nonempty polygonal feature and appends lineage to a copy. Physical loaded-object revalidation compares schema/dtypes/index/CRS/nongeometry values/WKB/attrs and summaries against fresh reads. None of this proves available electrical capacity, a guaranteed RTE connection point, legal/heavy-truck access, BESS authorization or parcel suitability/scoring.

## New bounded test-evidence limits, not production findings

- R15-T01 — IGN tests replace open_safe_https with nondelegating byte streams or raising sentinels; no live DNS/TLS/redirect or official archive acquisition is exercised. Shared transport reading is not a transport regression execution.
- R15-T02 — Appending a layer changes GPKG bytes, so the changed-inventory test fails the size/SHA gate before isolated inventory equality. Same-size text replacement keeps stale hash evidence; it is not isolated semantic attribute validation. The layer parameter in the three-consumer tamper test is unused and no post-mutation layer listing is asserted.
- R15-T03 — _FakeArchive tests inspect artificial member metadata; link/junction cases simulate predicates rather than create OS links. The .part-link test returns precomputed integrity from a mock, asserts validation call arguments and protected removal counts, but does not delegate that patched validation or prove real-link deletion safety end to end.
- R15-T04 — Geometry tests preserve selected counts/invalidity and compare line/multiline GeoDataFrames; they do not independently prove all Z/M ordinates or exact WKB. Coverage positive test checks one selected feature and summary facts, not electrical reach. Schema-3 inventory test checks at least one entry, not independent enumeration of every entry/hash.
- R15-T05 — Double-failure tests prove specified recovery backup bytes and controlled errors for injected seams, not universal cleanup or atomicity. Negative checksum case is SHA256 only; no positive official MD5 acquisition is asserted. Post-read tamper rejection is a path-based postcondition, not a race-free immutable snapshot proof.

No new concrete application finding was established; BACKLOG_AND_GAPS remains unchanged. Preserve A-001..A-004, five original limitations, R3-T01..04, R9-T01..04, R10-T01..04, R11-T01..05, R12-T01..05, R13-T01..05, R14-T01..05 and OPEN R5-D01. Cold-start independent acceptance, visual rendering, global finalization, exhaustive 7F.1C.1 semantic review and original 7F.1B.4 review-receipt gap remain unresolved. Last approved functional boundary remains 7F.1B.4; no functional continuation is authorized here.

## Two bounded R14 retouches and supplied review

The exact R15 ticket section 1 archives the supplied ChatGPT **APPROVED — documentary R14**, with minor nonblocking R14-REV01/REV02, at 8bef62ab9b6eef185bab526a046b4a7dbbea42a1. Its source-reading, remote-reference and omitted-check limits are a reviewer declaration, not this Codex execution, a signature, full Windows-state attestation or global/functional certification. The short successor link in CURRENT_STATE supersedes review state only within that supplied scope; the historical R14 PENDING receipt remains byte-identical.

Locally read both actual foundations notes before editing; both reproduced their companion's error, neither was already exact:

| Reservation | Exact protected test range | Local correction |
|---|---|---|
| R14-REV01 | test_epsg2154_parcel_input_remains_epsg2154, 688–692 | Only asserts non-null output CRS and EPSG 2154 after the private calculator; remove invented 100 m assertion. |
| R14-REV02 | test_supported_parcel_polygon_geometry_is_preserved, 743–747 | Name scalar equals_exact(geometry, tolerance=0) and has_z equality; retain Z/M/WKB proof limit. |

Only these two purpose paragraphs and matching notes change, plus the single companion fingerprint and compact r15_editorial_provenance. Protected test bytes, exact code/assertion blocks, every other paragraph/note, signatures, anchors, prior proofs and CHECKED/CORRECTED states remain unchanged. R14 gains zero files/symbols; its 174-test historical run is not rerun or reported as a new execution. Independent acceptance of these local corrections remains pending R15 review.

## Deduplicated progress and preservation

From actual matrix-to-owner reconciliation: 107/245 files and 2,975/4,769 symbols before; **111/245 files and 3,330/4,769 symbols after**, gain **four original files / 355 original symbols**, remaining **134 files / 1,439 symbols**. Final file labels: CHECKED 46, CORRECTED 65, READ 133, NOT_READ 1. Symbol labels: CHECKED 3,329, CORRECTED 1, READ 1,439. Dependencies, ticket/receipt, two R14 retouches and supplied approval add no credit. Global coverage.json and original matrix remain deliberately unchanged/unmerged.

Initial tracked inventory is 312 paths. Eight allowed output paths comprise six existing and two new paths, so all **306 initial paths outside scope** are compared, not the historical 305. All **106 protected files** retain manifest-authoritative Git OIDs, Git SHA256 and starting-checkout SHA256, also equal to preserved main Git OIDs. The two historical EOL exceptions remain untouched: written-zoning YAML and DOCS.CONTINUITY.1.RESUME.2026-09-17 ticket. The exact thirteen inherited whitespace observations remain byte-for-byte equal in main-to-start versus main-to-candidate diagnostics; new diff --check passes. No reset/restore/clean/stash/rebase/merge/amend/force-push or broad cleanup occurs.

First sorted remaining NOT_READ is docs/code/files/tests/unit/test_rte_odre_fr.py.md, identified only. READ units also remain unfinished; identifying that companion does not authorize the next lot.

## Unique focused execution and static checks

Only one application test invocation, installed environment unchanged:

```powershell
uv run --no-sync pytest -q tests/unit/test_ign_bdtopo_fr.py --basetemp "C:\Users\souha\AppData\Local\LandScout\pytest-runs\r15-6c546818"
```

Actual result: **125 passed in 9.02s**, final native **exit 0 after cleanup**; wrapper elapsed 9.4238553 seconds. No warning, skip or xfail reported; stderr is empty. LOCALAPPDATA/uv-cache access used the authorized escalation, without installation, sync, dependency/environment/security change or retry. No full suite, R14 suite, other pytest, pipeline, official archive download or official GPKG read occurred.

- `C:/souhaib/r15-pytest.stdout.txt`: 368 bytes, SHA256 `daf4e612496079196d2346c8fbfa95bb9b849cce7f06471f76e8552b83f84d39`.
- `C:/souhaib/r15-pytest.stderr.txt`: 0 bytes, SHA256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

Bounded static checks, without application imports: 355 exact signature/range/qualified-owner/anchor/note mappings; 399 original fenced blocks retained; two complete exact source snapshots; class field defaults and ordered call/return/exception contracts confronted with bodies; 29 package exports; strict JSON, unique anchors, local/incoming links, table shape, UTF-8 and source/companion SHA bases. The R14 delta is proven to be precisely the two allowed paragraph substitutions and matching two notes, with every other R14 owner field unchanged except fingerprint/provenance. Initial pre-record check found 432 explicit IDs, 519 heading IDs, 140 local links, four incoming companion links, 2,760 qualified-reference occurrences with zero unresolved, 5,809 table lines and 13 strict JSON files; these are that bounded check's scope, not a visual pass. Final staged static check and its exact metrics are retained outside Git below after the auditor run.

No usable local visual renderer was exercised; visual rendering remains **PENDING**, not inferred from Markdown parsing. No permanent tool is added. Temporary inspection/authoring/check/evidence scripts and all logs stay outside the repository.

## Single INDEX candidate and bounded completion

Only the eight explicit authorized paths are staged. One unchanged full auditor invocation on that candidate:

```powershell
.venv\Scripts\python.exe -B -X utf8 tools/audit_documentation.py --check --progress > C:\souhaib\r15-candidate.stdout.txt 2> C:\souhaib\r15-candidate.stderr.txt
```

The single full run finished with **native exit 1 / completed=true / 10,209 findings**, wrapper elapsed **2.0366161 seconds**. This is completed execution with global PARTIAL findings, not timeout/exit2 or a green global audit. Candidate manifest (sorted path/mode/OID, compact JSON UTF-8 SHA256) is **`a54db5d82f6b18bbee8bc0254ab4be173405fad0077feb5de8fc21306df2ebe6`**: 314 paths, 311 unique blobs, 27,790,876 bytes; 94 Python files / 94 AST parses / 4863 actual symbols, historical coverage denominator 245 files / 4769 symbols, 5 Git processes. The tool and index remained unchanged during the run.

Compared by finding-line multiplicity to actual R14 candidate logs: **10,207 occurrences unchanged, 10 removed, 2 added** (10,217 → 10,209). Removed: two ambiguous companion line-ending-basis findings for the IGN source/tests, seven incorrectly qualified inherited-method references in the two IGN companions, and the old inventory-mismatch line. Added: the inventory line now also lists the new R15 ticket, and a stale file fingerprint for the changed IGN test companion. coverage.json still stores its original 4ab36a80a52c85f96ee67e92e85e0f3baded2bcaf01b0b885443b74495e5fe5d fingerprint; the current foundations owner correctly stores f4ac55a98498fcac75098f9cb05116ffd57068a854145e7d2979d6aa18613f83. This is a real stale global-ledger binding, not a stale active-owner note, and does not authorize changing that forbidden ledger. The production companion fingerprint was already stale in the comparator.

Candidate categories: ambiguous basis82; bad local link3; DEV_LOG companion parser findings2; export inventory mismatch24; inventory mismatch1; missing companion exception131; missing documented anchor4,769; missing exact source snapshot8; semantic-ledger-not-COMPLETE1; stale fingerprint125; unfinished history1; unresolved qualified reference47; unresolved file review245; unresolved symbol review4,769; unchanged checkout/EOL diagnostic1. Most closure diagnostics read the unmerged global ledger, not the current review fragments. Existing unresolved links, references, export/exception/snapshot issues remain global work; the common findings are not relabeled as all harmless or all repaired. No unresolved qualified-reference finding names either IGN companion. Known literal-domain reference limitations from earlier receipts remain unchanged.

The exact R14 comparator is its candidate before its later receipt completion: manifest 7e880ed6dd97d41d32f7bfc85b7c2c9c7698224fd9b23c7e41a8b392285f6546, completed=true, exit1, 10,217 findings. R15's starting committed tree instead has manifest 9a99bae46fe6ac911e31edd0ac418557d142e8f5813b16c2bb95792dbb511e8b. These are not conflated.

The pre-run staged bounded static check passed with 432 explicit IDs, 544 heading IDs, 198 local links, four incoming companion links, 2,760 qualified-reference occurrences and zero unresolved, 5,827 table lines and 13 strict JSON files. It also reconfirmed the 355 mappings, two exact snapshots, 399 preserved fenced blocks, all 106 protected files, 306 initial outside-scope paths and thirteen unchanged inherited whitespace observations. This remains static checking, not visual or independent acceptance.

Local evidence files retained outside Git:

- `C:/souhaib/r15-candidate.stdout.txt`: 2,297,868 bytes; SHA256 `f5b60b351bde41de756bc10331c441e2d5a56366ddd6ecf5208f589061542d10`.
- `C:/souhaib/r15-candidate.stderr.txt`: 64,204 bytes; SHA256 `709b60b5242dd0e6de11e1c5589290aa0b64876a3495ea8dcea40044e629bffa`.
- `C:/souhaib/r15-candidate.manifest.json`: 80,742 bytes; SHA256 `ad2009f26a26d91e38ced7afe03bebd18bb5f03dbc5750ee97c73727226bb0a9`.
- `C:/souhaib/r15-compare.json`: 12,720 bytes; SHA256 `4122b7c1615cb40cec45ccdadb12ba136c0fec0c437450771a9d51c257cdbdc9`.
- `C:/souhaib/r15-static-index.json`: 4,534 bytes; SHA256 `eae2f0799f288810492c5c4e80946fa2578af419e1cd3a420ead17546b64670a`.
- `C:/souhaib/r14-candidate.stdout.txt`: 2,300,022 bytes; SHA256 `bf55d589877a34da0d7aef8d6728b1efc5406936d4590c8009eb8b1c9d5a9be1`.
- `C:/souhaib/r14-candidate.stderr.txt`: 64,100 bytes; SHA256 `51acd78090a8e866f5419998bf4ec6ecd1143c7d3b239335101d75144b506766`.
- `C:/souhaib/r14-candidate.manifest.json`: 80,238 bytes; SHA256 `ec2b401c9a43acbb8c8749dfe24db468d45e1caa8abaea9d3e853391984a869a`.

Candidate receipt before completion: OID `55376102cf3f5cf8ffd72aae56b3ef479a10c615`, 17,368 bytes, SHA256 `32b8787a50a0bf7341633888b3d7a72ab52ff1380b5ba653566d88f05f9c5620`. Only the dedicated auditor placeholder is replaced after the run. Bounded post-completion verification checks the unchanged prefix/suffix, single changed receipt path and all other exact candidate path/mode/OIDs; its observed delta and final manifest are stored outside the receipt to avoid self-hashing circularity. No second full auditor is run and no final-tree finding count is invented. The final report supplies the actual publication SHA and verified clean/tracking/server/main result after those operations.

After the single run, only this dedicated receipt placeholder may be completed. The sorted exact path/mode/OID candidate manifest and logs remain immutable local evidence; the post-run check must prove unchanged prefix/suffix, only this receipt path changed and every other path/mode/OID equal. No second full auditor, final=candidate equivalence or invented final-tree finding count. Commit/push on recovery only, then verify native publication result, clean index/worktree, matching tracking/server recovery SHA and unchanged local/tracking/server main. STOP; review pending.

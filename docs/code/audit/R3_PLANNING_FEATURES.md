# DOCS.CONTINUITY.1.R3 — planning-feature documentation review

Status: four-row semantic documentation review complete; candidate integration
and publication gates recorded below. Independent R3 review **PENDING**;
global DOCS.CONTINUITY.1 **PARTIAL**. No application correction or approval.

## Authority and preserved starting state

Authority: [exact supplied R3 ticket](../../project/tickets/DOCS.CONTINUITY.1.R3.txt),
attachment `2748cd3b-2d5e-4960-9b79-d853fcfaaa76/pasted-text.txt`.
Attachment and archived raw bytes have identical SHA256:
`8d381c265a96e0a789c363c36a4f738bc9f59a5a82e60ed954b2e0023af159de`.
Section 1 is the supplied read-only reviewer receipt, not a newly executed test
or a separate signed/full transcript.

Clean starting branch `recovery/docs-continuity-1-partial`, local HEAD and
local/actual remote recovery `fd4d87b973be9e6842a6b1934077b61ad6c70f93`;
local/actual remote main `aa4ebc7063f2abdfcbae95154ba89b5b1a0dba02`.
No unmerged entries or Git-operation markers. Sandbox remote access failed;
native explicit-root inspection reproduced the known ownership mismatch before
the authorized command-only `-c safe.directory=C:/souhaib/landscout-ai` remote
query succeeded. No fetch, persistent trust/security/dependency change or reset.

The supplied reviewer **APPROVED R2.1 only within subprocess-test stabilization**
at the starting SHA, parent `64787a28bd5801dcc88f8e2107cd230fe263d476`.
It reports byte-verified unchanged Linux copies: Python 3.13.5, Git 2.47.3,
pytest 9.0.2; selected eight passed/128 deselected in 2.36 s and whole file
136 passed in 6.79 s, exits 0, no reported warnings/skips/xfails. This is supplied
review evidence, not fresh R3 execution. Exact tool/test blob IDs and hashes remain
in the archived ticket. It does not approve global prose/application correctness,
the Windows candidate, EP research or cold-start acceptance. The historical
[R2](R2_DIAGNOSTICS.md) and [R2.1](R2_1_DIAGNOSTICS.md) receipts stay unchanged.

## Reading, semantic corrections and evidence limits

Read the entire unchanged source (2,057 lines) and test (2,287 lines), all unique
explanatory prose/signatures/field tables/test descriptions in both retained
companions, then compared repeated code blocks to those already read source bytes.
The prior source companion contained 830 unique nonblank prose lines; test companion
1,668. Repeated generic call/effect tables were deduplicated for display, not treated
as semantic evidence. All 250 test code blocks matched source substrings; 155 of
175 source blocks matched exact substrings, while 20 were AST-formatted return
expressions individually compared to source. The old test companion contained an
exact full snapshot; the old source companion had matching excerpts but no exact
complete-file block. R3 supplies exact complete snapshots for both.
R3 replaces generic name-based descriptions and duplicate assertion dumps with
individual explanations, exact signatures/case decorators and one exact full
snapshot per companion. It does not derive algorithm prose from AST names.

Reviewed all five public names and every private definition/field: source 84,
test 122 (98 test definitions, 20 top-level helpers, four nested substitutes).
Constants, empty cases, accepted families/identities, raw optional values, CRS,
units, dtype/index schemas, copy/mutability, errors, physical effects, caller
boundaries and both canonical hash payloads are explained independently of the
snapshots. No code/schema/hash bytes changed.

Concrete corrections/clarifications:

- Physical revalidation is a delegated filesystem effect of both public paths,
  not absent merely because the module has no open()/HTTP calls. GPU reads paths
  with pre/post checks, not immutable archive byte snapshots.
- Builder's private `source_inputs_already_rebuilt=True` skips independent
  catalog/relation validation, not source reconstruction. The public validator
  physically rebuilds before checking supplied catalog strings (A-003 below).
- Frozen result envelopes contain mutable DataFrames. The independence test
  checks saved relations against selected original inputs, not every output or
  the fresh document-held source frame.
- Full source area/length differ from parcel-clipped metrics. Surface union
  avoids duplicate covered area; raw area/line sums do not. Point summaries count
  members, while relation counts count feature/parcel pairs.
- Label/date/standard-model catalog dtype is str, not arbitrary str/object;
  only three optional text/file/URL columns have specified all-null variants.
  Original parcels retain CRS/WKB; metric copies and catalogs force XY2154.
- Exact helper returns and order are documented: _active_geometry and numeric/
  integer validation helpers return None; _validate_parcels returns CRS;
  _canonical_catalog_dtypes mutates/returns its argument; _project_geometry
  returns a new positional GeoSeries. Scalar tolerance uses the actual common
  reference magnitude, not an invented geometric buffer.
- Synthetic fixtures use real GPKG/Shapefile IO and schema-2 extraction markers
  but a fabricated ZIP envelope; no official acquisition or prevalence proof.

Retained bounded test-evidence findings (details per test in the companion):

| ID | Exact limitation, not a new application defect |
|---|---|
| R3-T01 | `test_strict_relation_integer_counts_are_enforced` and seven cases of `test_corrupted_relation_semantics_are_rejected` cast columns to object, so canonical dtype rejection precedes scalar/semantic checks. Parcel-summary cases actually reach strict scalar checks. Source summary True equals 1 at GPU dataclass equality and reaches stage strict checking; the other four bad-count values fail earlier. |
| R3-T02 | `test_feature_ids_are_globally_unique_across_catalogs` and two `test_source_complete_contract_rejects_coherently_renamed_feature_identity` cases break deterministic IDs first; they do not isolate global uniqueness or fully coherent source-ID forgery. |
| R3-T03 | `test_source_complete_contract_rejects_missing_expected_relation` keeps RangeIndex start 1 and fails canonical index validation. Extra false relation reaches reconstruction but fails index equality before explicit count guard; reversed/reset rows do exercise ordered cell comparison. |
| R3-T04 | Absent logical layer/outside reference/.prj inventory/.shx deletion/.cpg or GPKG byte attacks often fail configured discovery or whole-extraction manifest checks before selected-dataset containment/core/family checks. Exact mutation and earlier gate are recorded, not credited to an unvisited branch. |

Related positive limits are explicit: ordered-column equality is not all-schema
equality; Z cases are not M/ZM coverage; a fake link-detector answer is not an OS
symlink; patched returned FIDs are not rewritten disk FIDs; selected sidecars are
not every suffix. Missing dedicated A-003/tolerance-edge/zero-parcel regressions
remain limitations. Tests are unchanged. These bounded clarifications need no new
application backlog entry; the existing backlog and five INPN/roads test-evidence
limitations remain untouched/open.

Rejection-site distinctions come from the ordered source and exact fixture/attack
reading, reconciled with the one passing run; no separate branch instrumentation
or extra test invocation was performed. Broad exception regexes alone do not prove
that a later branch ran.

### A-003 remains OPEN

Read the [archived exact synthetic reproduction](RECOVERY_STATUS_2026-09-17.md#application-findings)
and affected bodies; no repeat was needed. Physical LIBELLE `" Label "` is copied
unchanged by _optional_values/_normalize_layer into catalog and relation label_raw.
Builder returns it because its optimized _validate_result path does not call
_validate_catalog_identity. Public validation first rebuilds physical catalogs,
then _validate_optional_exact_strings/_strict_string rejects the supplied label
with `Feature catalog label raw must be a non-empty exact string`, before catalog
comparison, relation reconstruction and integrity-record return. This refines the
old report's ambiguous “before downstream physical source completion” wording
without rewriting that historical receipt. Intended raw preservation is retained;
no trimming/fix, official prevalence claim or acquisition attestation. A-001 and
A-002 likewise remain open for separate corrective authority/review.

### Dependency read boundary (no ownership/status expansion)

- Complete `common/planning_feature_schema.py`, `planning_feature_contract.py`,
  `planning_overlay.py`, `frame_integrity.py`: exact frame schema/dtype/index,
  intrinsic formulas/nulls, tolerance and deterministic schema-signature owners.
- `sources/gpu_fr.py`: config/layer models and loaders/reconstruction/hash
  (149–403); metadata/config identity, SHA/link helpers (686–792);
  extraction inventory/manifest validation (1245–1370, with adjacent cleanup
  context read but not audited); spatial discovery/configured role checks
  (1517–1744); physical dataset-family/containment/hash/read/compare/revalidation
  and summaries (1738–2285). These reads do not close the GPU inventory row.
- `stages/__init__.py` imports 59–65 and export declaration 161–254; actual
  reference search identified `resolve_planning_feature_codes.py`:
  `_build_result` 886–968 and public caller 1121–end, including transfer of both
  validation digests. No full CNIG-policy review or test execution claimed.
- `tests/unit/test_resolve_planning_feature_codes.py` 598–683:
  `_integration_inputs`, `_integration_parcels` and `_inputs` pass this builder's
  actual returned fields onward. No audit of that whole test file.

## Exact four-row reconciliation

Basis: unchanged [original recovery matrix](recovery_file_matrix_2026-09-17.json)
and updated operational owner [extension](reviews/inpn_roads_extension.json).
Prior planning-fragment duplicates remain historical transfer evidence, not
second closures. Deduplicate by path and (path, kind, qualified_name).

| Original row | Before | After | Symbols closed in R3 |
|---|---|---|---:|
| src/landscout/stages/enrich_planning_features.py | NOT_READ | CHECKED | 84 |
| tests/unit/test_enrich_planning_features.py | NOT_READ | CHECKED | 122 |
| docs/code/files/src/landscout/stages/enrich_planning_features.py.md | NOT_READ | CORRECTED | 0 |
| docs/code/files/tests/unit/test_enrich_planning_features.py.md | NOT_READ | CORRECTED | 0 |

All four are in the original 178 pending paths and were read_complete=false.
Their current records bind exact Git-content SHA, each signature/range, companion
anchor, manual behavioral notes and real test references/explicit missing direct
regressions. Closure means documentation fidelity, not A-003 fixed or independent
approval. The 241 other original matrix rows receive no delta.

Original-scope arithmetic only: 67+4 = **71/245 files**;
1,388+84+122 = **1,594/4,769 symbols**. Remaining **174 files / 3,175 symbols**.
File totals become CHECKED 26, CORRECTED 45, READ 141, NOT_READ 33;
symbol totals CHECKED 1,593, CORRECTED 1, READ 2,078, NOT_READ 1,097.
New receipts/tickets and the 94-symbol auditor/test addition do not enter these
original denominators. Global coverage.json stays the original unmerged inventory.

## Actual focused execution

Inspected fixture/callee paths before running: local synthetic physical IO and
config reads, no HTTP acquisition calls. No blanket network block was injected.
Using the existing native environment and explicit repository location:

```text
uv run pytest -q tests/unit/test_enrich_planning_features.py --basetemp C:\Users\souha\AppData\Local\LandScout\pytest-runs\r3a27
```

**183 collected/passed, 2 warnings, 64.14 s, native process exit 0 including
cleanup**. Zero failures/skips/xfails/deselections. Exactly one unchanged-file run;
no full application suite, real GPU/EP rebuild, download or acquisition.

Warnings, both retained rather than suppressed:

1. `test_null_or_empty_source_geometry_is_rejected[geometry1]`,
   `gpu_fr.py:2228`: UserWarning about GeoSeries.notna no longer treating empty
   geometries as missing; historical behavior differs for the synthetic empty.
2. `test_missing_crs_is_rejected[source]`,
   `.venv/Lib/site-packages/pyogrio/geopandas.py:948`: UserWarning that crs was not
   provided for output dataset during the synthetic missing-CRS write.

## Preservation and documentation validation

Pre-staging comparison passed all **106 original protected paths** against base
main Git identities, current index hashes and recorded raw-checkout hashes.
All **275 starting tracked paths outside the five existing allowed edits** match
their starting bytes (with only the two already-recorded raw/Git EOL distinctions:
Muret YAML and the old resume ticket). New ticket/receipt are the other two allowed
paths. No BACKLOG, executable, config, dependency, tool, old fragment/matrix/archive,
cache, research-pair or source snapshot change is authorized or included.

Unchanged source SHA256:
`01a56b482a3c956d1f8a7069b94c69518758ea3937c3d98ef8ae5d74615d6148`.
Unchanged test SHA256:
`f742a30c7921e83fd28114c7419ba0d4c2ca36aa0aed5d04c8881cad1feaef57`.
Unchanged auditor SHA256:
`5b5aae765c6c32225496d7830e17e83a9bfac89e007949b032b75b13eda3029f`.
Unchanged global coverage SHA256:
`5ae2a994effb59947b0dbe4af97b777bc17fb13998a8ba5b8110f2c42052036c`.

Exact source snapshots, all 206 signatures and explicit symbol anchors have been
checked. Targeted static checks passed four exact fragment identities/ranges,
206 matching manual notes/signatures/anchors, 196 local links and changed Markdown
fences/table delimiter widths. Current companion Git-content SHA256 values:

- Source companion: `227e99c83b96bd7e5c3aa9a3746fb82830ca7716365b47629dcaecaf22c60f23`.
- Test companion: `5b41259990b4c50f3c37d62a7edffc9355b44965a0e0b86f69cd5d4af2847fd7`.

The protection-check preparation initially used an incomplete AuditRun constructor
and then an abbreviated old resume-ticket filename; both probes stopped on explicit
errors, without edits. Correct constructor/recorded exact filename passed all
106/275 comparisons above. These were scoped checks, not full checker invocations.
Final indexed-byte checks and one full staged INDEX execution are recorded below.
The full checker does not consume this fragment as a merged global coverage ledger.

Local rendering discovery: pandoc/markdown/marked/node are absent from PATH and
the existing Python environment lacks markdown/markdown_it/mistune/docutils.
Previously discovered VS Code Markdown extension supplies no inspected standalone
renderer entry; native-app UI control is unavailable. No document was visually
rendered, no dependency installed and no private content uploaded. Static checks
are not a visual pass; visual acceptance stays pending.

### Staged candidate integration

The seven explicit paths were staged; new-delta `git diff --check` and
`git diff --cached --check` both exited 0. The existing full INDEX checker ran
**once**, in the owning context, stdout outside Git:

```text
.venv\Scripts\python.exe -X utf8 tools/audit_documentation.py --check --progress > C:\souhaib\r3-candidate.stdout.txt
```

**Native exit 1**, `completed=true`, normal PARTIAL findings, no interruption or
exit 2. Exact candidate manifest SHA256:
`6ac0d1ae9a692da210ec6177859be6e935246f5b1063b0cb14ec6e7e1896ac30`.
282 paths, 279 distinct blobs, 29,048,158 per-path content bytes; 94 Python files,
94 AST parses, 4,863 enumerated symbols (4,769 original + 94 auditor/test symbols).
Five Git processes, non-shallow history and unchanged final index enumeration.
Native tool wall time 2.0770757 s includes launcher/output overhead; no benchmark
claim. Phase seconds: index 0.182501, coverage-input 0.010431, Python 0.801365,
checkout-Markdown 0.272171, coverage 0.112421, references 0.145645, history
0.073265, index-postcondition 0.026328.

**10,264 observed sorted unique findings**: coverage/staleness 5,033, mechanical
215, pending recorded acceptance 5,016. The original global ledger is still
unmerged, so it continues reporting its original NOT_READ rows/missing recorded
anchors; this is not a rejection of the separate four-row reconciliation.
Compared with retained R2.1 output, two ambiguous companion-basis findings, the
source's missing exact full snapshot and one Pydantic dynamic-method qualified
reference disappear; the inventory line gains this ticket archive. Two new
qualified-reference diagnostics name the source companion's **literal hash-domain
strings**, `landscout.planning_features.verified_gpu_sources.v1` and
`landscout.planning_features.expected_relations.v2`. They exactly match source
payload strings at lines 1050/1083, not Python API claims. The diagnostic scanner
does not distinguish that prose context. They remain reported: no checker change,
suppression, exception entry or claim that all mechanical findings passed.

Detailed stdout: `C:\souhaib\r3-candidate.stdout.txt`, PowerShell UTF-16,
2,314,932 bytes, SHA256
`3ace1c81d28280e94fb4dc4ae01cca3671cf5845ddbc561e077d9f146b394823`.
Exact sorted path/mode/blob entries remain outside Git in
`C:\souhaib\r3-candidate.manifest.json` (UTF-8); compact ASCII-safe JSON without
terminal newline reproduces the manifest digest above.

The candidate included this receipt's preparation version. **Only this receipt
changes after that full run**, to record outcomes and clarify the old source
snapshot limitation; those later bytes are not retroactively part of the checked
candidate. Scoped final checks cover the later receipt's links/fences, exact
one-path manifest delta, seven-path scope, all protected bytes and both companion
bindings. No second full checker run, global coverage regeneration or new test run.

The cumulative main-to-candidate whitespace check exits 2 with exactly the same
13 inherited observations as main-to-start: twelve original cold-start Markdown
hard breaks and the original ticket's final blank line. Stdout/stderr are identical;
new R3 delta is clean. One diagnostic printer initially raised a Windows cp1252
UnicodeEncodeError after those comparisons passed; a UTF-8 scoped rerun completed
with exit 0 and confirmed all 13. No archive rewrite or whitespace suppression.

## Stop and remaining queue

Publish this bounded batch only on the recovery branch with
`docs: complete planning feature companion review`, verify clean tree and actual
remote recovery equality/main preservation, then stop for independent R3 review.
Final SHA is resolved after commit, not embedded as its own future identity.

First remaining NOT_READ path in the preserved sorted queue:
`configs/planning/cnig_plu_2017_feature_codes.yaml`. No implementation or new review
of that item is authorized here. Global semantic coverage, original five test
limitations, A-001/A-002/A-003, final cold-start acceptance
(`REPORTED_EXECUTED_PENDING_REVIEW`), visual rendering and final full application
validation remain open. Last approved functional boundary is 7F.1B.4; 7F.1C.1
remains research with exhaustive independent semantic review pending.

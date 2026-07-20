# Obstruction and Gluing Analysis

## Method

This engineering ledger treats each repository or component as a local capability section and each versioned contract as a gluing map. A composition is considered supported only when shared fixtures or receipts demonstrate that adjacent components agree on identity, schema, authority, status, evidence, revocation, and recovery semantics.

This is a practical compatibility analysis, not a claim of completed mathematical homology computation.

## Material obstructions

| ID | Obstruction | Affected edge | Consequence | Lowest-scope repair candidate |
|---|---|---|---|---|
| JFM-O1 | `host` is a short hostname, not an authenticated device identity | JusticeForMe → Repository `0`/`1` | A report cannot be safely bound to the intended device | Wrap schema `1.0` in a separate evidence envelope with approved device identity |
| JFM-O2 | `root_complete` is global and boolean while checks can individually fail, timeout, or be unsupported | Collector → dashboard | Zero counts may be mistaken for verified absence | Define per-check status outside schema `1.0`, then version deliberately if promoted |
| JFM-O3 | Dashboard thresholds are fixed heuristics, not signed host baselines | Dashboard → operator or policy | `ok` can be confused with compliant or trusted | Keep thresholds informational and compare through Repository `1` baseline policy |
| JFM-O4 | Artifact names are listed without hashes in `report.json` | Report → evidence directory | Dashboard cannot verify that displayed metrics and artifacts belong together | Bind report and manifest hashes in an evidence envelope |
| JFM-O5 | Manifest is locally generated but unsigned and mutable with the report directory | Evidence directory → long-term evidence | Later modification may be difficult to distinguish | Preserve an independent hash/receipt through an approved evidence authority |
| JFM-O6 | Package verification output can contain errors, timeouts, or findings under one count | Package tool → metric | Result semantics are ambiguous | Record command, exit/timeout state, verifier identity, and categorized output |
| JFM-O7 | Permission and read errors are often suppressed | Host → collector | Missing evidence can look like a clean result | Produce explicit skipped/error status per collection domain |
| JFM-O8 | No operating-system, kernel, package-manager, shell, Python, or utility versions are in the report | Collector → replay/review | Results are not fully reproducible or comparable | Add execution provenance to a separate envelope |
| JFM-O9 | No freshness, replay, nonce, or prior-run relationship exists | JusticeForMe → Repository `1` | A valid old report could be replayed as current | Repository `1` validates issued request, time window, nonce, and device generation |
| JFM-O10 | Raw evidence may contain sensitive local identity and configuration data | Evidence → transport/storage | Public CI, issues, or Pages could expose host details | Default to local storage; approve minimization, encryption, retention, and private transfer |
| JFM-O11 | JusticeForMe is Linux-only while Repositories `0` and `1` are portable-device foundations | Portable baseline → collector | Portfolio may imply coverage on unsupported platforms | Publish a platform capability matrix and mark unsupported controls `UNKNOWN` |
| JFM-O12 | No accepted proposal/capability/receipt package ownership exists | Repository `0` → Repository `1` | Integration implementations may invent incompatible envelopes | Assign one contract owner and pin shared fixtures |
| JFM-O13 | Collection and remediation are intentionally separate but no approved adapter boundary exists | JusticeForMe → Repository `0` | Observations could be converted into changes without explicit review | Define a read-only observation adapter and separate remediation proposal contract |
| JFM-O14 | Evidence preservation and emergency-stop ownership are external and unnamed | Incident → recovery | A serious finding may not have a coherent escalation path | Name human security, evidence, incident, and recovery owners in portfolio governance |

## Pairwise gluing requirements

### JusticeForMe collector ↔ local dashboard

- schema `1.0` accepted fixture;
- unsupported-version rejection fixture;
- missing metrics and malformed types rejection fixture;
- extreme-value rendering fixture;
- local-only resource and no-network validation;
- text-safe rendering of host, notice, and artifact names.

### JusticeForMe ↔ Repository `0`

- exact collector source and invocation identity;
- authorized device and output scope;
- report and manifest hash binding;
- complete, partial, failed, unsupported, and timed-out statuses;
- privacy classification and allowed evidence destinations;
- transformation receipt when observations become a proposal.

### Repository `0` ↔ Repository `1`

- versioned proposal envelope;
- expected canonical head and device generation;
- freshness and replay protection;
- policy and human-approval requirements;
- narrowly scoped capability issuance;
- execution, rollback, and resulting-state receipts;
- revocation and emergency-stop propagation.

## Triple-overlap witnesses

### Collector → Repository `0` → Repository `1`

The same device identity, report hash, policy version, and collection status must survive collection, proposal transformation, and quarantine admission. A mismatch at any edge fails closed.

### Repository `1` → Repository `0` → host remediation adapter

The capability's device, pre-state, operation, target resources, duration, and rollback requirements must agree across authority decision, orchestration, and execution. Successful command execution is not automatic canonical acceptance.

### JusticeForMe → evidence store → human review interface

The report, manifest, redaction state, classification, and evidence identity must remain bound. Public presentation must not expose raw private host evidence.

### Incident freeze → Repository `1` → replacement-device bootstrap

Revoked device identity and capabilities must not silently transfer to the replacement device. The new device requires a new identity, baseline comparison, and recovery checkpoint.

## Priority repair sequence

1. Keep the current collector and dashboard behavior unchanged while documenting semantics.
2. Approve JusticeForMe's role as a Linux observation adapter under Repository `0`.
3. Assign the evidence-envelope and proposal-contract owner.
4. Define device identity, request freshness, per-check status, and execution provenance.
5. Create shared fail-closed fixtures at immutable commits.
6. Define privacy, retention, encryption, incident, and recovery ownership.
7. Only then consider collector schema or adapter implementation changes.

## Architectural clarification required

Formal approval is still required for:

- JusticeForMe's portfolio owner and whether it is a standalone tool or Repository `0` adapter;
- the device-identity authority and replacement-device lifecycle;
- evidence-envelope, proposal, capability, receipt, and revocation contract ownership;
- privacy classification, retention, transport, and publication policy;
- the human security, evidence, incident, emergency-stop, and recovery owners;
- whether schema `1.0` remains stable and is wrapped, or is replaced by a versioned report schema after fixtures exist.

# Release Plan

## Current decision

Status: `BLOCKED — DOCUMENTATION VALIDATION, PRODUCT ROLE, EVIDENCE SEMANTICS, PRIVACY, AND CONTRACT OWNERSHIP REQUIRED`

The current repository contains a bounded read-only Linux collector and local static dashboard. This documentation candidate does not alter either implementation. It establishes the review material required to decide whether JusticeForMe remains a standalone local audit tool, becomes a Repository `0` observation adapter, or supports both roles under distinct contracts.

## Versioning

- Current report schema: `1.0`.
- First eligible documentation candidate: `0.1.0-docs` after exact-head validation and approval.
- A documentation version does not imply forensic correctness, supported-platform completeness, Repository `0`/`1` integration, publication approval, or remediation capability.
- A breaking report semantic change requires a new schema version and migration fixtures.
- Evidence-envelope, proposal, capability, receipt, and revocation versions remain separate from `report.json`.

## Candidate scope

The documentation candidate may include:

- polished project overview and portfolio role;
- architecture, data flow, trust boundaries, and failure model;
- report schema and evidence-contract documentation;
- local dashboard usage and threshold interpretation;
- onboarding, development, validation, and review guidance;
- operations, privacy, evidence preservation, incident freeze, recovery, and rollback guidance;
- obstruction/gluing analysis and compatibility requirements;
- aligned task chain, punch list, changelog, and exact-head documentation validation.

It may not activate remote collection, report transport, credential access, scheduled enforcement, host modification, remediation, capability issuance, Pages deployment, package release, or production authority.

## Acceptance gates

| Gate | Status | Requirement |
|---|---|---|
| Documentation completeness | REVIEW | All required guidance and coordination files are present and internally consistent. |
| Exact-head validation | PENDING | Shell, JavaScript, HTML, required documentation, and links pass at the immutable submitted head. |
| Implementation boundary | PASS FOR CURRENT SOURCE | Collector is read-only with respect to audited configuration and dashboard parses locally; future changes require renewed review. |
| Product role | BLOCKED | Approve standalone, Repository `0` adapter, or dual-role identity. |
| Report semantics | PARTIAL | Schema `1.0` is documented; per-check failure and provenance semantics remain absent. |
| Privacy and retention | BLOCKED | Classification, minimization, encryption, transport, retention, deletion, and disclosure policy are approved. |
| Contract ownership | BLOCKED | Report, evidence-envelope, device-identity, proposal, capability, receipt, revocation, and recovery owners are assigned. |
| Shared fixtures | NO EVIDENCE | Repository `0`/`1` gluing fixtures pass at pinned commits. |
| Publication | NOT AUTHORIZED | Documentation Pages deployment requires separate approval; raw reports are prohibited from public publication. |
| Approval | PENDING | Human approval records exact candidate head and scope. |

## Required release evidence

- exact source commit and clean-checkout assertion;
- shell and JavaScript syntax results;
- static HTML and local-resource validation;
- required documentation and local-link validation;
- workflow permission and deployment-prohibition checks;
- rendered or archived documentation evidence;
- SHA-256 manifest tied to the submitted head;
- limitations, privacy statement, rollback instructions, and approval record.

## Rollback

Withdraw the candidate if documentation implies unsupported coverage, findings are represented as proof, privacy boundaries are weakened, report schema semantics diverge from implementation, links or validation fail, workflow permissions expand, or integration language silently authorizes Repository `0`/`1` behavior. Restore the previous reviewed source, retain failed-candidate evidence, and record the reason in `changelog.md`.

## Unresolved blockers

- JusticeForMe's final portfolio role and owner are not approved.
- Exact-head validation for this documentation candidate has not yet passed.
- The current report lacks per-check status, authenticated device identity, execution provenance, and replay protection.
- Raw evidence privacy, transport, and retention policy is not approved.
- No accepted Repository `0`/`1` shared contract or fixture set exists.
- Public Pages deployment remains intentionally absent.

## Release log

- 2026-07-20 — Prepared a documentation-only portfolio-integration candidate. No implementation, publication, credential, transport, remediation, or authority change was approved.

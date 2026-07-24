# Release Plan

## Current decision

Status: `BLOCKED — DESCENDANT VALIDATION, MANUAL ACCESSIBILITY EVIDENCE, PRODUCT ROLE, EVIDENCE SEMANTICS, PRIVACY, AND CONTRACT OWNERSHIP REQUIRED`

The current repository contains a bounded read-only Linux collector and local static dashboard. This documentation candidate does not alter either implementation. It establishes the review material required to decide whether JusticeForMe remains a standalone local audit tool, becomes a Repository `0` observation adapter, or supports both roles under distinct contracts.

Accessibility status is `DOCUMENTED_NOT_CERTIFIED`. The review protocol is documented, but no universal accessibility claim, conformance certification, publication approval, or release approval follows from automated source checks.

## Versioning

- Current report schema: `1.0`.
- First eligible documentation candidate: `0.1.0-docs` after exact-head validation and approval.
- A documentation version does not imply forensic correctness, supported-platform completeness, Repository `0`/`1` integration, accessibility certification, publication approval, or remediation capability.
- A breaking report semantic change requires a new schema version and migration fixtures.
- Evidence-envelope, proposal, capability, receipt, revocation, accessibility-review-record, and correction-record versions remain separate from `report.json`.

## Candidate scope

The documentation candidate may include:

- polished project overview and portfolio role;
- architecture, data flow, trust boundaries, and failure model;
- report schema and evidence-contract documentation;
- local dashboard usage and threshold interpretation;
- onboarding, development, validation, and review guidance;
- exact-artifact accessibility review protocol and non-certification boundary;
- operations, privacy, evidence preservation, incident freeze, recovery, and rollback guidance;
- obstruction/gluing analysis and compatibility requirements;
- aligned task chain, punch list, changelog, and exact-head documentation validation.

It may not activate remote collection, report transport, credential access, scheduled enforcement, host modification, remediation, capability issuance, accessibility certification, Pages deployment, package release, or production authority.

## Acceptance gates

| Gate | Status | Requirement |
|---|---|---|
| Documentation completeness | REVIEW | All required guidance and coordination files are present and internally consistent. |
| Exact-head validation | REVALIDATE DESCENDANT | Shell, JavaScript, HTML, required documentation, links, accessibility markers, and source identity pass at the immutable submitted head. Historical passes apply only to their recorded generations. |
| Implementation boundary | PASS FOR CURRENT SOURCE | Collector is read-only with respect to audited configuration and dashboard parses locally; future changes require renewed review. |
| Accessibility protocol | DOCUMENTED_NOT_CERTIFIED | Review surfaces, states, exact-artifact evidence, manual procedures, privacy, correction, and fail-closed rules are documented. |
| Manual accessibility evidence | BLOCKED | Retained keyboard, focus, 200%/400% zoom and reflow, contrast, reduced-motion, screen-reader, cognitive-access, and error-recovery evidence exists for the exact rendered artifact. |
| Product role | BLOCKED | Approve standalone, Repository `0` adapter, or dual-role identity. |
| Report semantics | PARTIAL | Schema `1.0` is documented; per-check failure and provenance semantics remain absent. |
| Privacy and retention | BLOCKED | Classification, minimization, encryption, transport, retention, deletion, and disclosure policy are approved. |
| Contract ownership | BLOCKED | Report, evidence-envelope, device-identity, proposal, capability, receipt, revocation, recovery, accessibility-review, and correction owners are assigned. |
| Shared fixtures | NO EVIDENCE | Repository `0`/`1` gluing fixtures pass at pinned commits. |
| Publication | NOT AUTHORIZED | Documentation Pages deployment requires separate approval; raw reports are prohibited from public publication. |
| Approval | PENDING | Human approval records exact candidate head, artifact, scope, limitations, and authority boundary. |

## Required release evidence

- exact source commit and clean-checkout assertion;
- shell and JavaScript syntax results;
- static HTML and local-resource validation;
- required documentation and local-link validation;
- accessibility-protocol semantic checks;
- workflow permission and deployment-prohibition checks;
- rendered or archived documentation evidence and digest;
- manual accessibility evidence for the exact rendered artifact;
- browser, operating system, viewport, zoom, input-method, assistive-technology, and reviewer records;
- SHA-256 manifest tied to the submitted head;
- limitations, privacy statement, correction links, rollback instructions, and approval record.

## Accessibility claim boundary

Automated validation may verify source identity, required HTML structure, labels, local links, local resources, required text markers, and absence of deployment authority. It cannot certify screen-reader usability, comprehension, adequate contrast in every environment, 400% reflow, cognitive accessibility, or conformance to every applicable standard.

A later certification claim requires an approved standard and scope, named reviewer authority, exact rendered artifact, retained manual evidence, supported environment matrix, correction and withdrawal policy, and explicit human approval.

## Rollback

Withdraw the candidate if documentation implies unsupported coverage, findings are represented as proof, privacy boundaries are weakened, report schema semantics diverge from implementation, accessibility source checks are represented as certification, links or validation fail, workflow permissions expand, or integration language silently authorizes Repository `0`/`1` behavior. Restore the previous reviewed source, retain failed-candidate evidence, preserve the original record, and record the correction, withdrawal, or supersession reason in `changelog.md`.

## Unresolved blockers

- JusticeForMe's final portfolio role and owner are not approved.
- Exact-head validation must pass for the current documentation descendant.
- Manual accessibility evidence for an exact rendered artifact is not complete.
- The current report lacks per-check status, authenticated device identity, execution provenance, and replay protection.
- Raw evidence privacy, transport, and retention policy is not approved.
- No accepted Repository `0`/`1` shared contract or fixture set exists.
- Public Pages deployment remains intentionally absent.

## Release log

- 2026-07-20 — Prepared a documentation-only portfolio-integration candidate. No implementation, publication, credential, transport, remediation, or authority change was approved.
- 2026-07-23 — Added an exact-artifact accessibility and review-evidence protocol, preserved `DOCUMENTED_NOT_CERTIFIED`, and kept manual review, certification, publication, collector execution, and release authority separate.

# Task Chain

## Purpose

This task chain keeps documentation, validation, and release work aligned with the repository's implemented scope. A checked documentation task means the material exists; it does not imply that runtime, security, or release evidence has been accepted.

## Current state

JusticeForMe currently provides a read-only Linux audit collector, a local evidence bundle, a `report.json` summary contract at schema version `1.0`, and a static browser dashboard deployed from `docs/`.

The repository is **not release-approved** merely because these components exist or because documentation is complete.

## Phase 1 — Scope and documentation baseline

- [x] Define the project as a read-only Linux privilege and configuration audit tool.
- [x] Document authorized-use and evidentiary limits.
- [x] Document implemented collector scope and explicit non-goals.
- [x] Document collector, evidence-bundle, dashboard, and Pages boundaries.
- [x] Document schema `1.0` fields and current dashboard thresholds.
- [x] Add developer onboarding and contribution guidance.
- [x] Add security, privacy, evidence-preservation, and live-system caveats.
- [x] Add Pages project documentation and architecture diagrams.
- [x] Add release-readiness and changelog records.

## Phase 2 — Baseline reproduction

- [ ] Record the exact `main` commit used for acceptance testing.
- [ ] Run `bash -n` on the collector and retain output.
- [ ] Run ShellCheck with a recorded version and retain output.
- [ ] Exercise root and non-root collection on approved test hosts.
- [ ] Record tested Linux distributions, versions, filesystems, and package managers.
- [ ] Verify the collector terminates safely when optional directories or tools are absent.
- [ ] Verify output-directory behavior, permissions, and disk-space failure handling.
- [ ] Verify every declared artifact is generated or intentionally empty with an explanation.
- [ ] Verify `REPORT-SHA256SUMS.txt` covers the intended top-level files.

## Phase 3 — Contract and dashboard validation

- [ ] Create sanitized synthetic fixtures for normal, warning, priority, incomplete, and malformed reports.
- [ ] Verify schema `1.0` acceptance and unsupported-version rejection.
- [ ] Verify missing and non-numeric metric handling.
- [ ] Verify threshold boundaries exactly match `DESIGN.md`.
- [ ] Verify local-only behavior with browser network inspection.
- [ ] Verify keyboard operation, focus visibility, heading order, contrast, responsive layout, and status announcements.
- [ ] Verify the Pages guide and dashboard links from a clean deployment artifact.
- [ ] Decide whether a formal JSON Schema is required before the first tagged release.

## Phase 4 — Security and privacy review

- [ ] Review every collector command for mutation, traversal, quoting, race, and privilege hazards.
- [ ] Review temporary/output path handling for symlink and unsafe-directory risks.
- [ ] Confirm generated artifacts do not capture unnecessary file contents or secrets.
- [ ] Review browser parsing for injection, denial-of-service, and oversized-input behavior.
- [ ] Review Pages dependencies and pinning policy.
- [ ] Define report retention, redaction, transfer, and deletion guidance.
- [ ] Establish a private vulnerability-reporting path.
- [ ] Record reviewer identity, date, exact commit, findings, and dispositions.

## Phase 5 — Compatibility and operational evidence

- [ ] Define supported Linux families and explicit exclusions.
- [ ] Define supported Bash and Python versions.
- [ ] Define package-verifier semantics per supported distribution.
- [ ] Test interrupted collection and partial output recovery.
- [ ] Test dashboard rollback to the previous Pages artifact.
- [ ] Test collector rollback to the previous approved commit.
- [ ] Document how operators preserve original evidence and analyze a copy.
- [ ] Confirm no generated report is included in repository or Pages artifacts.

## Phase 6 — Governance and release decision

- [ ] Confirm repository license and redistribution terms.
- [ ] Confirm maintainer, security-review, documentation, and release ownership.
- [ ] Approve support status and communication policy.
- [ ] Approve schema stability and compatibility policy.
- [ ] Approve the release checklist in `release.md` against retained evidence.
- [ ] Create a signed or otherwise approved release record only after all mandatory gates pass.
- [ ] Publish Pages only from the accepted documentation commit.
- [ ] Record rollback target, artifact digest, and final human approval.

## Architectural clarification triggers

Stop implementation and request architectural clarification when a proposal introduces or materially changes:

- remote collection or command execution;
- automated remediation or containment;
- continuous monitoring or fleet management;
- network transmission, hosted storage, or collaboration;
- evidence signing, timestamping, or identity claims;
- malware classification or attribution;
- collection of file contents, credentials, secrets, or personal data;
- schema meaning, metric units, or dashboard thresholds;
- supported-platform commitments; or
- production, compliance, or forensic-certification claims.

## Definition of a substantial documentation milestone

A substantial documentation milestone is complete when a coherent documentation area is added or materially improved, links and terminology are reconciled, diagrams and text agree with the implementation, scope boundaries are explicit, and `taskchain.md`, `release.md`, and `changelog.md` remain aligned.
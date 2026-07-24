# Punch List

Accessibility status: `DOCUMENTED_NOT_CERTIFIED`.

## P0 documentation milestone

- [x] Clarify current collector and dashboard purpose.
- [x] Document implemented surfaces and explicit non-capabilities.
- [x] Add architecture and trust-boundary model.
- [x] Document report schema `1.0`, artifacts, and dashboard thresholds.
- [x] Add developer and reviewer onboarding.
- [x] Add operations, evidence preservation, incident freeze, recovery, and rollback guidance.
- [x] Add obstruction and gluing ledger.
- [x] Add exact-artifact accessibility and review-evidence protocol.
- [x] Align `taskchain.md`, `release.md`, and `changelog.md`.
- [ ] Validate the current descendant exact head and retain evidence.
- [ ] Produce manual keyboard, focus, 200%/400% zoom and reflow, contrast, reduced-motion, screen-reader, cognitive-access, and error-recovery evidence.
- [ ] Review the retained rendered artifact rather than relying only on source inspection.

## Product and ownership decisions

- [ ] Approve JusticeForMe as a standalone Linux audit tool, a Repository `0` observation adapter, or both with distinct release identities.
- [ ] Name repository product, security, evidence, privacy, incident, recovery, accessibility-review, and correction owners.
- [ ] Approve supported Linux distributions and minimum tool assumptions.
- [ ] Define whether public Pages publication is allowed for documentation only.
- [ ] Define the accessibility standard, scope, supported browser/assistive-technology matrix, and certification authority, if certification is pursued.

## Contract ownership

- [ ] Assign owner for report schema `1.0`.
- [ ] Assign owner for the future evidence envelope.
- [ ] Assign owners for device identity, proposal, capability, execution receipt, revocation, and recovery contracts.
- [ ] Define semantic-versioning and compatibility policy.
- [ ] Record expected-head and immutable-fixture requirements.

## Evidence correctness

- [ ] Define per-check `complete`, `partial`, `failed`, `unsupported`, and `timed_out` semantics.
- [ ] Separate package findings from package-verifier errors.
- [ ] Record collector commit, script hash, effective identity, platform, kernel, shell, Python, and utility versions.
- [ ] Bind `report.json`, supporting artifacts, and manifest in one evidence envelope.
- [ ] Define clock, freshness, nonce, replay, and prior-run semantics.
- [ ] Define independent evidence preservation or attestation.

## Accessibility evidence

- [x] Define `NOT_REVIEWED`, `PARTIAL`, `PASS`, `FAIL`, `BLOCKED`, `UNKNOWN`, `SUPERSEDED`, `WITHDRAWN`, and `CORRECTED` states.
- [x] Separate automated structural validation from accessibility certification.
- [x] Define exact source, rendered artifact, environment, reviewer, limitation, correction, and supersession bindings.
- [x] Define privacy rules requiring synthetic or minimized fixtures.
- [ ] Retain exact rendered dashboard and guide artifacts for manual review.
- [ ] Test keyboard-only navigation and visible focus.
- [ ] Test screen-reader names, roles, states, live status, table/card comprehension, and errors.
- [ ] Test 200% and 400% zoom, narrow viewport reflow, long hashes, paths, commands, and tables.
- [ ] Test text and control contrast, forced-colors behavior, reduced motion, and non-color severity communication.
- [ ] Test cognitive comprehension of partial, failed, unsupported, timed-out, unknown, heuristic, and authority states.
- [ ] Link defects to correction, withdrawal, or accepted-risk records without overwriting history.

## Privacy and security

- [ ] Classify report fields and artifacts.
- [ ] Define minimization and redaction requirements.
- [ ] Define allowed local, encrypted, private, and prohibited public destinations.
- [ ] Define retention and deletion policy.
- [ ] Add negative tests blocking raw report publication to public CI or Pages.
- [ ] Document evidence access and disclosure incident handling.
- [ ] Treat screenshots, recordings, browser logs, and assistive-technology transcripts as potentially sensitive.

## Platform and baseline integration

- [ ] Publish a platform capability matrix.
- [ ] Mark unsupported platforms and checks as `UNKNOWN`.
- [ ] Define Repository `0` invocation and observation adapter boundary.
- [ ] Define Repository `1` baseline comparison and quarantine boundary.
- [ ] Create shared fixtures for identity mismatch, stale/replayed reports, unsupported schema, partial collection, and manifest mismatch.
- [ ] Define clean-room reinstall and replacement-device workflows.

## Deferred implementation

- [ ] Consider report schema evolution only after contract fixtures are approved.
- [ ] Consider additional Linux surfaces only through separately reviewed scope.
- [ ] Consider remediation proposals only after observation, authority, rollback, and recovery contracts pass independent review.

## Release blockers

A release remains blocked while current-descendant exact-head validation is absent, manual rendered accessibility evidence is incomplete, product/portfolio identity is unresolved, evidence semantics can treat missing data as clean, privacy policy is unapproved, and no shared Repository `0`/`1` compatibility fixtures exist.

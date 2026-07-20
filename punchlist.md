# Punch List

## P0 documentation milestone

- [x] Clarify current collector and dashboard purpose.
- [x] Document implemented surfaces and explicit non-capabilities.
- [x] Add architecture and trust-boundary model.
- [x] Document report schema `1.0`, artifacts, and dashboard thresholds.
- [x] Add developer and reviewer onboarding.
- [x] Add operations, evidence preservation, incident freeze, recovery, and rollback guidance.
- [x] Add obstruction and gluing ledger.
- [x] Align `taskchain.md`, `release.md`, and `changelog.md`.
- [ ] Validate exact submitted head and retain evidence.
- [ ] Review Pages guide for accessibility, local-only behavior, and privacy language.

## Product and ownership decisions

- [ ] Approve JusticeForMe as a standalone Linux audit tool, a Repository `0` observation adapter, or both with distinct release identities.
- [ ] Name repository product, security, evidence, privacy, incident, and recovery owners.
- [ ] Approve supported Linux distributions and minimum tool assumptions.
- [ ] Define whether public Pages publication is allowed for documentation only.

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

## Privacy and security

- [ ] Classify report fields and artifacts.
- [ ] Define minimization and redaction requirements.
- [ ] Define allowed local, encrypted, private, and prohibited public destinations.
- [ ] Define retention and deletion policy.
- [ ] Add negative tests blocking raw report publication to public CI or Pages.
- [ ] Document evidence access and disclosure incident handling.

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

A release remains blocked while exact-head documentation validation is absent, product/portfolio identity is unresolved, evidence semantics can treat missing data as clean, privacy policy is unapproved, and no shared Repository `0`/`1` compatibility fixtures exist.

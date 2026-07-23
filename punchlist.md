# JusticeForMe Punch List

Status: `DOCUMENTATION_ONLY — PUBLICATION AND DEPLOYMENT BLOCKED`

## Documentation baseline

- [x] Add a project overview with users, scope, non-goals, privacy, and release posture.
- [x] Add an architecture guide with a diagram and equivalent prose.
- [x] Add safe operator and maintainer onboarding.
- [x] Add developer change controls and rollback guidance.
- [x] Document report schema `1.0` and compatibility rules.
- [x] Add security, privacy, and evidence-handling guidance.
- [x] Add a local documentation front door.
- [x] Align `README.md`, `taskchain.md`, `release.md`, `punchlist.md`, and `changelog.md`.
- [ ] Obtain exact-head workflow evidence for the complete baseline.

## Validation

- [ ] Validate every internal Markdown and HTML route.
- [ ] Verify the dashboard and guide use local assets only.
- [ ] Verify one `<main>` and one `<h1>` on each HTML entry point.
- [ ] Verify diagrams carry equivalent prose.
- [ ] Verify planning files share the same status and schema version.
- [ ] Verify workflow permissions remain `contents: read`.
- [ ] Retain deterministic source hashes and a validation artifact.

## Next bounded work

- [ ] Add synthetic valid and invalid report fixtures.
- [ ] Add parser regressions for malformed, incomplete, future, and type-confused reports.
- [ ] Document distribution-specific package-verifier semantics.
- [ ] Document threshold provenance and calibration before changing any dashboard threshold.
- [ ] Add an evidence-export/redaction design without implementing upload or sharing.

## Blocked decisions

- [ ] GitHub Pages publication approval.
- [ ] License selection.
- [ ] Named documentation, security, accessibility, schema, and release owners.
- [ ] Retention guidance for real report directories.
- [ ] Distribution baseline ownership and review cadence.
- [ ] Formal forensic or compliance claims, which remain out of scope without independent standards and legal review.

## Prohibited shortcuts

Do not treat a passing workflow, report hash, root-complete flag, package-verifier line, dashboard severity, or documentation milestone as proof of compromise, chain of custody, compliance, publication approval, or operational authority.

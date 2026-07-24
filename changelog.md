# JusticeForMe Changelog

All notable product, documentation, validation, release, and authority-boundary changes are recorded here.

## Unreleased

### Added

- 2026-07-23 — Added a project overview describing intended users, bounded questions, components, privacy model, documentation routes, and release posture.
- 2026-07-23 — Added an architecture guide with a collector-to-report-to-dashboard diagram and equivalent prose, component responsibilities, trust boundaries, failure modes, and extension rules.
- 2026-07-23 — Added authorized-use onboarding for collection, local report review, evidence preservation, maintainer setup, and stop conditions.
- 2026-07-23 — Added a developer guide covering repository structure, design invariants, collector and dashboard changes, schema versioning, validation, review, and rollback.
- 2026-07-23 — Added report schema `1.0` documentation, a synthetic example, compatibility rules, and browser-input security requirements.
- 2026-07-23 — Added security, privacy, threat-model, chain-of-custody, disclosure, workflow, interpretation, correction, and rollback guidance.
- 2026-07-23 — Added a local HTML documentation front door alongside the dashboard.
- 2026-07-23 — Added `taskchain.md`, `punchlist.md`, and `release.md` with explicit publication, licensing, ownership, synthetic-test, and evidence gates.
- 2026-07-23 — Added a separate read-only resulting-main workflow so exact default-branch documentation heads receive retained validation without adding Pages deployment authority.
- 2026-07-23 — Added focused regressions for per-command failure aggregation, per-push evidence identity, always-retained failure evidence, repository-wide workflow scanning, and local-only dashboard assets.

### Changed

- 2026-07-24 — Bound pull-request validation concurrency to each immutable submitted head, disabled cancellation of superseded runs, and added regression coverage so every reviewed generation can retain terminal evidence.
- 2026-07-23 — Expanded README navigation and repository layout to include the complete documentation and planning surface.
- 2026-07-23 — Expanded pull-request validation to cover documentation links, HTML navigation, planning alignment, diagram prose alternatives, and the unchanged deployment prohibition.
- 2026-07-23 — Clarified that GitHub Pages content is prepared for local review but publication remains unauthorized.
- 2026-07-23 — Separated pull-request validation in `pages.yml` from resulting-default-head validation so the Pages workflow remains structurally incapable of push, manual, OIDC, or deployment actions.
- 2026-07-23 — Hardened resulting-main validation so shell, JavaScript, dashboard, regression, and integrity failures are tracked independently; each pushed `main` SHA receives its own validation generation; and workflow changes always trigger repository-wide deployment-authority checks.

### Security

- 2026-07-23 — Required real host reports to remain outside public Git, CI, issues, and documentation artifacts.
- 2026-07-23 — Documented hostname, user/group, path, package, privilege, and persistence disclosure risks.
- 2026-07-23 — Preserved read-only workflow permissions, exact-head checkout, pinned actions, local-only assets, and no OIDC or deployment authority.
- 2026-07-23 — Required indicators, hashes, timestamps, package-verifier lines, and dashboard severities to remain distinct from proof, attribution, legal conclusions, and compliance decisions.
- 2026-07-23 — Required retained evidence even when integrity checks fail and prohibited remote dashboard scripts/styles or deployment authority in any repository workflow.

### Release

- 2026-07-23 — Recorded status `BLOCKED_PUBLICATION_NOT_AUTHORIZED`; no Pages publication, package release, remote execution, credentials, telemetry, report upload, or deployment is included.

## Historical baseline

- 2026-07-20 — Removed stale deployed-Pages instructions and aligned the README with local dashboard use and validation-only workflow policy.
- 2026-07-20 — Replaced automatic Pages deployment with exact-head, read-only pull-request validation and retained evidence.

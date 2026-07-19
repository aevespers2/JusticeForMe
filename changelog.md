# Changelog

All notable repository changes should be recorded here. Entries describe repository changes; they do not by themselves establish release approval.

## Unreleased

### Documentation

- Expanded the README into a complete project overview with quick start, architecture summary, scope boundaries, documentation map, and support-status caution.
- Added architecture documentation covering system context, components, data flow, trust boundaries, report contract, failure modes, deployment, and non-goals.
- Added design documentation covering collection semantics, dashboard thresholds, compatibility expectations, evidence integrity, privacy, accessibility, and change classification.
- Expanded contributor guidance with developer onboarding, synthetic fixtures, change categories, validation steps, and review checklists.
- Added security and evidence-handling guidance for authorized use, elevated execution, sensitive outputs, live-system limitations, browser review, Pages publication, and vulnerability reporting.
- Added an evidence-driven task chain and explicit architectural clarification triggers.
- Added release-readiness gates with evidence-record requirements and prohibited unsupported claims.
- Added a GitHub Pages project guide with architecture, report contract, onboarding, operations, and incident-response material.
- Improved Pages navigation and shared styling without changing collector or dashboard interpretation behavior.

### Scope

- No collector command, scan root, artifact, metric, threshold, schema meaning, network behavior, credential behavior, remediation authority, or publication authority is changed by this documentation milestone.

## 2026-07-19 — Initial audit dashboard baseline

### Added

- Read-only Linux privilege and configuration audit collector.
- `/etc` metadata and SHA-256 inventories.
- World-writable and executable `/etc` findings.
- Setuid/setgid binary and Linux file-capability inventories.
- Administrative-access, persistence, loader, and package-integrity artifacts.
- `report.json` summary using schema version `1.0`.
- SHA-256 manifest for generated report files.
- Static browser dashboard with local file loading and heuristic review priorities.
- GitHub Pages deployment workflow.
- Initial safety, scope, and contribution guidance.

### Clarified

- Findings are indicators requiring human validation and are not proof of malicious activity.
- The dashboard parses reports locally and does not upload selected files.

## Changelog policy

Future entries should identify:

- user-visible behavior changes;
- collector scope changes;
- report schema and metric changes;
- dashboard threshold or interpretation changes;
- security and privacy changes;
- compatibility changes;
- workflow and publication changes;
- documentation milestones; and
- release or rollback decisions.

Breaking schema changes must include migration guidance and an explicit compatibility decision.
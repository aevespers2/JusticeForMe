# JusticeForMe

JusticeForMe is a read-only Linux configuration and privilege auditing project. It inventories `/etc`, privileged binaries, file capabilities, administrative access paths, persistence locations, and package-integrity deviations, then renders a local report schema `1.0` in a browser-based static dashboard.

Status: `DOCUMENTATION_ONLY — LOCAL USE; PUBLICATION NOT AUTHORIZED`

## Start here

- [Project overview](docs/project-overview.md)
- [Architecture and trust boundaries](docs/architecture.md)
- [Safe onboarding](docs/onboarding.md)
- [Developer guide](docs/developer-guide.md)
- [Report schema 1.0](docs/report-schema.md)
- [Security and evidence handling](docs/security-and-evidence.md)
- [Accessibility and review evidence](docs/accessibility-and-review-evidence.md)
- [Local documentation guide](docs/guide.html)
- [Task chain](taskchain.md)
- [Punch list](punchlist.md)
- [Release plan](release.md)
- [Changelog](changelog.md)

## Safety and evidentiary limits

The collector does not modify the audited system outside the chosen output directory or transmit reports. Findings are indicators that require validation against trusted package metadata, known-good hashes, documented administrative changes, and preserved chain-of-custody records. A configuration difference, report hash, package-verifier line, timestamp, or dashboard severity is not by itself proof of malicious activity, attribution, legal responsibility, or compliance failure.

Use this project only on systems you own or are authorized to inspect. Real report directories may expose hostnames, users, groups, local paths, package changes, privileged binaries, capabilities, and persistence mechanisms; keep them out of public Git, CI artifacts, and issues.

## Run the collector

```bash
chmod +x audit/linux-privilege-audit.sh
sudo ./audit/linux-privilege-audit.sh
```

To choose a destination:

```bash
sudo ./audit/linux-privilege-audit.sh /secure/path/justiceforme-case-001
```

The script creates a timestamped report directory containing:

- `report.json` for the dashboard;
- `/etc` metadata and SHA-256 inventories;
- world-writable and executable `/etc` findings;
- setuid/setgid binaries and Linux file capabilities;
- administrative groups and sudo metadata;
- persistence and dynamic-loader indicators;
- package-manager integrity results; and
- `REPORT-SHA256SUMS.txt` for collected-file identity checks.

## Use the dashboard

Open `docs/index.html` locally, choose the generated `report.json`, and review the prioritized indicators. Parsing occurs entirely in the browser; the dashboard does not upload the selected file. Read [onboarding](docs/onboarding.md), [security and evidence handling](docs/security-and-evidence.md), and [accessibility and review evidence](docs/accessibility-and-review-evidence.md) before reviewing sensitive host data.

GitHub Pages publication is not authorized by the repository workflow. The workflow validates pull-request source only, uses read-only repository permissions, and does not deploy, publish, request an OIDC token, change credentials, or run remote collection.

## Accessibility evidence boundary

The repository records accessibility review status as `DOCUMENTED_NOT_CERTIFIED`. Automated checks may validate source identity, landmarks, labels, local routes, local assets, diagram alternatives, and the absence of deployment authority. They do not certify screen-reader usability, comprehension, contrast in every environment, 400% reflow, cognitive accessibility, or conformance to every applicable standard.

## Repository layout

```text
audit/linux-privilege-audit.sh       Read-only audit collector
docs/index.html                      Local static dashboard
docs/guide.html                      Local documentation front door
docs/*.md                            Overview, architecture, onboarding, schema, evidence, and accessibility guidance
tests/                               Documentation and governance regressions
.github/workflows/pages.yml          Pull-request validation only
taskchain.md                         Ordered work and dependencies
punchlist.md                         Bounded completion items
release.md                           Release and publication gates
changelog.md                         Notable changes
```

## Validation boundary

Collector, dashboard, and documentation changes must pass exact-head validation for shell and JavaScript syntax, required HTML landmarks and controls, local-only assets, internal routes, prose-equivalent diagrams, planning alignment, clean checkout identity, and absence of Pages deployment authority. Passing validation does not establish forensic correctness, accessibility certification, compliance, publication approval, or proof of malicious activity.

## FYSA-120 capability map

This documentation baseline applies CAT-011, CAT-012, CAT-017, CAT-018, CAT-019, CAT-031, CAT-040, CAT-052, CAT-054, CAT-056, and CAT-064. Proposed subdivisions `056-F — Forensic-tool documentation and interpretation-boundary engineering` and `019-Q — Exact-artifact accessibility evidence for local security-review interfaces` are non-authoritative taxonomy gaps; they do not certify competence or expand project authority.

## Scope

The project supports authorized internal security reviews, incident-response preparation, compliance validation inputs, and forensic preservation. Remote scanning, automated remediation, production incident command, public report hosting, accessibility certification, and legal or compliance conclusions remain outside scope.
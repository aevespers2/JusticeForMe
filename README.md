# JusticeForMe

JusticeForMe is a **read-only Linux configuration and privilege auditing project**. It inventories selected `/etc` state, privileged binaries, file capabilities, administrative access paths, persistence locations, and package-integrity output, then renders a local `report.json` in a browser-based static dashboard.

Within the A.L.I.S.T.A.I.R.E. portfolio, JusticeForMe is a candidate **Linux host-observation adapter** for the Repository `0`/`1` portable first-install security foundation. Repository `0` may supervise an approved local collection and prepare a remediation proposal; Repository `1` may compare the evidence with an approved device baseline and decide whether a narrow capability is authorized. That integration is documentation-only and is not active.

## Safety and evidentiary limits

The collector does not modify the audited system or transmit reports. Findings are indicators that require validation against trusted package metadata, known-good hashes, documented administrative changes, and preserved chain-of-custody records. A configuration difference, dashboard severity, or package-verifier line is not by itself proof of malicious activity, attribution, compromise, or compliance failure.

The current report schema does not provide authenticated device identity, per-check completion state, full execution provenance, or replay protection. Missing or suppressed evidence must not be interpreted as verified absence.

## Documentation

- [Pages dashboard](docs/index.html)
- [Pages project and architecture guide](docs/guide.html)
- [Project overview](docs/reference/project-overview.md)
- [Architecture and trust boundaries](docs/reference/architecture.md)
- [Report and evidence contract](docs/reference/report-contract.md)
- [Developer onboarding](docs/reference/developer-onboarding.md)
- [Operations and recovery](docs/reference/operations-and-recovery.md)
- [Obstruction and gluing analysis](docs/reference/obstruction-and-gluing.md)
- [Task chain](taskchain.md)
- [Punch list](punchlist.md)
- [Release plan](release.md)
- [Changelog](changelog.md)

## Run the collector

```bash
chmod +x audit/linux-privilege-audit.sh
sudo ./audit/linux-privilege-audit.sh
```

The script creates a timestamped report directory containing:

- `report.json` for the dashboard;
- `/etc` metadata and SHA-256 inventories;
- world-writable and executable `/etc` findings;
- setuid/setgid binaries and Linux file capabilities;
- administrative groups and sudo metadata;
- persistence and dynamic-loader indicators;
- package-manager integrity output;
- a SHA-256 manifest for the collected report files.

## Use the dashboard

Open `docs/index.html` locally, choose the generated `report.json`, and review the prioritized indicators. Parsing occurs entirely in the browser; the dashboard does not upload the selected file.

GitHub Pages publication is not authorized by the repository workflow. The workflow validates pull-request source only, uses read-only repository permissions, and does not deploy, publish, request an OIDC token, or change credentials.

## Architecture boundary

```text
Authorized operator
        |
        v
Read-only Linux collector
        |
        +--> timestamped evidence directory
                 |-- report.json
                 |-- supporting artifacts
                 `-- REPORT-SHA256SUMS.txt
        |
        v
Local browser dashboard

Proposed only:
JusticeForMe evidence -> Repository 0 proposal -> Repository 1 quarantine/baseline decision
```

JusticeForMe does not issue capabilities, approve remediation, modify host state, control remote devices, or establish a canonical baseline.

## Repository layout

```text
audit/linux-privilege-audit.sh     Read-only audit collector
docs/index.html                    Local static dashboard
docs/guide.html                    Pages project and architecture guide
docs/reference/                    Detailed repository documentation
.github/workflows/pages.yml        Pull-request validation only
taskchain.md                       Sequenced work and evidence rules
punchlist.md                       Documentation and integration blockers
release.md                         Release scope and gates
changelog.md                       Product and documentation history
```

## Validation boundary

Dashboard or collector changes must pass exact-head validation for shell syntax, JavaScript syntax, required HTML landmarks and controls, local assets, documentation presence and links, clean checkout identity, and absence of Pages deployment authority. Passing validation does not establish forensic correctness, compliance, publication approval, integration readiness, or proof of malicious activity.

## Scope

This project is intended for systems you own or are authorized to inspect, including internal security reviews, incident response, compliance validation, recovery preparation, and forensic preservation. Raw audit evidence may contain sensitive host information and must not be placed in public issues, pull requests, Pages content, or public CI artifacts.

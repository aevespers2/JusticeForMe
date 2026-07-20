# JusticeForMe

JusticeForMe is a read-only Linux configuration and privilege auditing project. It inventories `/etc`, privileged binaries, file capabilities, administrative access paths, persistence locations, and package-integrity deviations, then renders a local `report.json` in a browser-based static dashboard.

## Safety and evidentiary limits

The collector does not modify the audited system or transmit reports. Findings are indicators that require validation against trusted package metadata, known-good hashes, documented administrative changes, and preserved chain-of-custody records. A configuration difference is not by itself proof of malicious activity.

## Run the collector

```bash
chmod +x audit/linux-privilege-audit.sh
sudo ./audit/linux-privilege-audit.sh
```

The script creates a timestamped report directory containing:

- `report.json` for the dashboard
- `/etc` metadata and SHA-256 inventories
- world-writable and executable `/etc` findings
- setuid/setgid binaries and Linux file capabilities
- administrative groups and sudo metadata
- persistence and dynamic-loader indicators
- package-manager integrity results
- a SHA-256 manifest for the collected report files

## Use the dashboard

Open `docs/index.html` locally, choose the generated `report.json`, and review the prioritized indicators. Parsing occurs entirely in the browser; the dashboard does not upload the selected file.

GitHub Pages publication is not authorized by the repository workflow. The workflow validates pull-request source only, uses read-only repository permissions, and does not deploy, publish, request an OIDC token, or change credentials.

## Repository layout

```text
audit/linux-privilege-audit.sh   Read-only audit collector
docs/                            Local static dashboard
.github/workflows/pages.yml      Pull-request validation only
```

## Validation boundary

Dashboard or collector changes must pass exact-head validation for shell syntax, JavaScript syntax, required HTML landmarks and controls, local assets, clean checkout identity, and absence of Pages deployment authority. Passing validation does not establish forensic correctness, compliance, publication approval, or proof of malicious activity.

## Scope

This project is intended for systems you own or are authorized to inspect, including internal security reviews, incident response, compliance validation, and forensic preservation.

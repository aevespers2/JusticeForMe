# JusticeForMe Project Overview

Status: `DOCUMENTATION_ONLY — LOCAL AUDIT TOOL; PUBLICATION NOT AUTHORIZED`

JusticeForMe is a read-only Linux configuration and privilege-audit project. It collects local system metadata into a timestamped directory, generates a compact `report.json`, and renders that report in a browser-based dashboard without uploading the selected file.

## Intended users

- system owners validating administrative and persistence exposure;
- incident responders preserving an initial configuration snapshot;
- security engineers comparing a host against a trusted baseline;
- auditors reviewing package-integrity and privileged-access indicators; and
- maintainers improving the collector or dashboard under exact-head validation.

## Problem boundary

The project helps answer four bounded questions:

1. Which privileged binaries, capabilities, administrative groups, and persistence locations are observable on this host?
2. Which `/etc` files are writable, executable, recently changed, or different from package-manager expectations?
3. Was the collection root-complete, and which artifacts were produced?
4. Which indicators deserve manual review against trusted package metadata and documented operational changes?

It does **not** determine intent, attribute activity, establish compromise, prove misconduct, certify compliance, or replace a forensic examiner. Thresholds in the dashboard are prioritization aids rather than universal security baselines.

## Current components

| Component | Responsibility | Authority boundary |
|---|---|---|
| `audit/linux-privilege-audit.sh` | Read-only collection and report generation | May read authorized local system state and write only to the selected output directory |
| `docs/index.html` | Local dashboard entry point | Loads user-selected JSON in the browser; does not transmit it |
| `docs/app.js` | Schema validation and indicator rendering | Accepts report schema `1.0`; does not make forensic conclusions |
| `docs/styles.css` | Accessible visual presentation | Presentation only |
| `.github/workflows/pages.yml` | Pull-request validation and evidence retention | Read-only repository access; no Pages deployment or credential authority |

## Data and privacy model

Generated reports can reveal hostnames, administrative groups, local paths, package-integrity deviations, and persistence locations. Treat the report directory as sensitive operational evidence. Do not commit real host reports to GitHub, attach them to public issues, or load them into an untrusted browser context.

## Documentation routes

- [Architecture](architecture.md)
- [Onboarding](onboarding.md)
- [Developer guide](developer-guide.md)
- [Report schema](report-schema.md)
- [Security and evidence handling](security-and-evidence.md)
- [Local dashboard guide](guide.html)

## Release posture

The repository remains a validation-only, local-use project. GitHub Pages publication, package distribution, automated collection, remote execution, privileged deployment, credential use, and production incident-response authority remain blocked until separately reviewed and approved.

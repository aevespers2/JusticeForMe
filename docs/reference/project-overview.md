# JusticeForMe Project Overview

## Purpose

JusticeForMe is a read-only Linux configuration and privilege auditing component. It collects a bounded local inventory of security-relevant configuration and privileged execution surfaces, writes evidence into a timestamped local directory, and renders the summary report in a browser without uploading it.

Within the A.L.I.S.T.A.I.R.E. portfolio, JusticeForMe is a candidate **Linux host-observation adapter** for the portable first-install security workflow shared by Repository `0` and Repository `1`:

- Repository `0` may invoke or supervise the collector under an approved local inspection task;
- JusticeForMe produces observations and a local evidence bundle;
- Repository `0` may transform those observations into a versioned remediation proposal;
- Repository `1` may compare the proposal and evidence with an approved device baseline and decide whether a narrowly scoped capability should be issued.

No integration is active merely because this responsibility is documented.

## Current implemented surface

The current collector:

- inventories `/etc` metadata and SHA-256 hashes;
- identifies world-writable and executable entries under `/etc`;
- enumerates setuid/setgid binaries in standard executable roots;
- records Linux file capabilities when `getcap` is available;
- records UID-0 accounts, selected administrative groups, and sudo configuration metadata;
- records local systemd units, cron entries, and `/etc/ld.so.preload` state;
- runs a bounded package verification command for `dpkg`, `rpm`, or `pacman` when available;
- generates `report.json`, supporting text artifacts, and `REPORT-SHA256SUMS.txt`;
- provides a local static dashboard for report schema `1.0`.

## Explicit limits

JusticeForMe does not currently:

- modify, quarantine, repair, delete, or disable host configuration;
- transmit reports or provide a remote service;
- establish device identity or ownership;
- prove that an indicator is malicious;
- compare results with a signed, host-specific approved baseline;
- cover macOS, Windows, Android, iOS, firmware, routers, or cloud control planes;
- inspect all Linux persistence, namespace, container, kernel, boot, network, or credential surfaces;
- issue capabilities, approve remediation, merge code, release packages, or deploy infrastructure.

Unsupported or incomplete observations must be represented as unknown or partial, not silently treated as secure.

## Users

Primary users are:

- an owner or administrator inspecting a Linux system they control;
- an incident responder preserving a first-pass local configuration snapshot;
- a developer validating the collector and dashboard contract;
- a reviewer assessing whether the output can safely glue into the Repository `0`/`1` device-trust workflow.

## Evidence classes

| Class | Example | Meaning |
|---|---|---|
| Observation | `/etc` metadata, package verification output | Raw local information requiring interpretation |
| Summary | Metrics in `report.json` | Derived counts for triage, not proof |
| Manifest | `REPORT-SHA256SUMS.txt` | Integrity aid for files in one report directory |
| Review decision | Human or policy evaluation | Outside JusticeForMe's current authority |
| Canonical baseline | Approved Repository `1` record | Not produced by JusticeForMe |
| Remediation receipt | Verified result of an approved change | Not produced by the current collector |

## Success criteria for the documentation milestone

- The repository's current behavior and non-capabilities are unambiguous.
- The report schema, collection flow, trust boundaries, and failure semantics are documented.
- New contributors can run, inspect, validate, and safely extend documentation.
- `taskchain.md`, `punchlist.md`, `release.md`, and `changelog.md` reflect the same scope.
- Cross-repository obstructions are identified without silently changing the collector contract.

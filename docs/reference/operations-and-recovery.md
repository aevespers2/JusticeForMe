# Operations, Evidence Preservation, and Recovery

## Supported operating mode

JusticeForMe currently supports local, read-only collection on an authorized Linux host and local browser review. There is no daemon, remote API, scheduled remediation, credential service, or deployment authority.

## Pre-collection checklist

- Confirm ownership or written authorization for the device.
- Decide whether the goal is baseline review, incident triage, compliance evidence, or recovery preparation.
- Minimize network exposure when compromise is suspected.
- Record date, operator, device location, and visible system state.
- Choose a protected output destination with sufficient space.
- Preserve volatile evidence first when required by an incident-response plan.
- Do not reboot, update packages, or clean findings merely to make the report look normal.

## Collection procedure

```bash
sudo ./audit/linux-privilege-audit.sh /protected/path/justiceforme-run
```

After completion:

```bash
cd /protected/path/justiceforme-run
sha256sum -c REPORT-SHA256SUMS.txt
```

Record the command result, exact collector commit, script hash, operating-system version, shell version, package-manager version, and whether any command timed out or was unavailable.

## Triage order

1. Confirm whether collection was root-complete.
2. Verify the evidence manifest before opening or copying files.
3. Review package-integrity output for errors versus actual deviations.
4. Review UID-0 accounts, administrative groups, sudo metadata, setuid/setgid binaries, and file capabilities.
5. Review world-writable or executable configuration entries.
6. Review systemd, cron, and dynamic-loader persistence indicators.
7. Compare against a known-good, host-specific baseline and documented administrative changes.
8. Escalate uncertain or high-impact differences for independent review.

Dashboard severity is only a review-order aid.

## Evidence handling

- Keep the original evidence directory immutable where practical.
- Create working copies for annotation or redaction.
- Hash copies after transfer and record source and destination hashes.
- Encrypt sensitive evidence at rest and in transit.
- Restrict access to authorized reviewers.
- Do not upload raw evidence to GitHub Pages, public issues, public pull requests, or public CI artifacts.
- Preserve unsuccessful and partial runs when they may explain later state.

## Incident freeze

Freeze further automated changes when any of these are observed:

- unexplained privileged accounts or access paths;
- package verification indicating broad or uncertain modification;
- unknown dynamic-loader configuration;
- evidence-manifest mismatch;
- collector source or runtime identity cannot be established;
- host identity conflicts with the expected device;
- Repository `0` proposes changes without an approved Repository `1` capability;
- audit evidence would be overwritten by a subsequent run.

A freeze is not proof of compromise. It is a stop condition for preserving evidence and obtaining review.

## Recovery paths

### Collector or dashboard defect

- Stop relying on affected derived metrics.
- Preserve the report and exact source identity.
- reproduce in a disposable environment;
- correct through a reviewable change;
- regenerate only when the new run can be distinguished from the original.

### Evidence corruption or manifest mismatch

- Do not rewrite the original manifest.
- Preserve the directory and storage metadata.
- locate an independently preserved copy;
- document transfer history;
- rerun only as a separate evidence set if the host is still available.

### Suspected host compromise

- Follow the approved incident plan.
- isolate rather than retaliate;
- preserve volatile and persistent evidence as required;
- revoke or rotate credentials through their actual authorities;
- use a trusted recovery or reinstallation path;
- reinstall Repositories `0` and `1` before restoring higher-level services;
- compare restored state with the approved baseline.

### Lost or stolen device

JusticeForMe cannot remotely control or revoke a missing device. Repository `1` or the relevant external identity providers must record the device as lost and revoke supported sessions, certificates, or capabilities. A replacement device should be bootstrapped from trusted media and audited before ordinary use.

## Rollback

Documentation changes are reverted by restoring the last reviewed commit. Collector or dashboard changes require preservation of the affected exact-head evidence, restoration of the last accepted source, and a new validation run. Never erase failed-run evidence as part of rollback.

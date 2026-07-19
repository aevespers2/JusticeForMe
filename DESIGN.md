# Design

## Design intent

JusticeForMe is designed as a small, auditable bridge between Linux host inspection and human review. The collector favors transparent operating-system commands and plain-text artifacts. The dashboard favors local parsing and a compact, versioned summary contract.

The design does not attempt to infer intent or attribution from configuration differences.

## Core principles

### Read host state; do not repair it

Collection commands inspect files, permissions, accounts, capabilities, persistence locations, and package metadata. The collector does not change permissions, delete files, disable accounts, restart services, install packages, or quarantine a host.

Writing the evidence directory is the only intended mutation. Operators should choose a destination that does not overwrite prior evidence and that has appropriate access controls.

### Preserve detailed artifacts alongside summaries

`report.json` is intentionally compact. It records counts and artifact names, not every finding. Detailed text artifacts remain necessary for interpretation, independent verification, and later comparison.

### Keep interpretation visibly heuristic

The dashboard uses fixed thresholds to order attention. These thresholds are not vulnerability scores, compliance verdicts, or compromise probabilities.

| Metric | Baseline-review range | Review recommended | Priority review |
| --- | ---: | ---: | ---: |
| World-writable `/etc` entries | 0 | 1 or more | 1 or more |
| Executable files in `/etc` | 0–5 | 6–19 | 20 or more |
| Setuid/setgid binaries | 0–20 | 21–59 | 60 or more |
| File capabilities | 0–5 | 6–19 | 20 or more |
| Package-integrity findings | 0 | 1–9 | 10 or more |
| Recent `/etc` changes within 30 days | 0–25 | 26–99 | 100 or more |

The first row has the same review and priority boundary in the current implementation because any world-writable regular file or directory under `/etc` deserves prompt validation. The dashboard labels it `high` when the count is at least one.

Thresholds are display policy embedded in `docs/app.js`. Changing them alters interpretation behavior and should be reviewed as a product decision, not treated as a documentation-only edit.

## Collection design

### Filesystem scope

The collector limits privileged-binary and capability enumeration to existing roots from:

- `/bin`
- `/sbin`
- `/usr/bin`
- `/usr/sbin`
- `/usr/local/bin`
- `/usr/local/sbin`

Each `find` invocation uses `-xdev`, so it does not cross filesystem boundaries from the selected root. That keeps scans bounded but may omit relevant paths mounted elsewhere.

### `/etc` inventory

The collector produces:

- a sorted metadata inventory containing type, mode, owner, group, size, timestamp, path, and link target;
- a SHA-256 inventory of regular files;
- world-writable regular files and directories; and
- executable regular files.

Metadata and hash files can be large. They may contain sensitive path and account information and should not be committed to the repository or uploaded to public issue threads.

### Administrative access

The administrative-access artifact records:

- accounts with UID 0;
- selected groups commonly associated with administrative or sensitive host access; and
- metadata for `/etc/sudoers` and files below `/etc/sudoers.d`.

It does not fully evaluate sudo policy, nested identity providers, PAM configuration, SSH authorization, polkit rules, or every distribution-specific privilege mechanism.

### Persistence indicators

The collector records local systemd units, conventional cron locations, and `/etc/ld.so.preload`. This is a bounded indicator set, not a comprehensive persistence framework.

### Package verification

Exactly one available package verifier is selected in this order:

1. `dpkg --verify`
2. `rpm -Va`
3. `pacman -Qkk`

Verifier output and exit status are distribution-specific. The collector retains output and continues so that deviations can be interpreted manually.

## Summary contract design

`schema_version` is currently `1.0`. The dashboard rejects reports with another version or without a `metrics` object.

Compatibility expectations:

- additions to the JSON object should be backward-compatible when the dashboard can ignore them;
- removing or renaming a metric is incompatible with current display logic;
- changing the meaning or unit of a metric requires a new schema version;
- artifact filenames are part of the human-facing handoff and should remain stable unless migration guidance is provided; and
- schema evolution must be documented in `changelog.md` and reviewed against `release.md`.

A formal JSON Schema, fixture suite, and migration mechanism are not currently implemented. They are appropriate future tasks after the existing contract is validated, but this document does not add them to runtime scope.

## Evidence integrity model

`REPORT-SHA256SUMS.txt` is generated after the other top-level report files. It supports later detection of accidental or unauthorized changes when compared from a trusted environment.

It does not provide:

- signer identity;
- trusted collection time;
- protection against an attacker who can replace both files and manifest;
- a complete disk image;
- memory capture; or
- chain-of-custody documentation.

Operators should preserve the original directory, record collection context separately, verify the manifest before analysis, and work from a copy.

## Privacy model

The Pages dashboard receives only a local file selected by the user and does not implement upload or persistence. The deployed site remains public static content, so operators should never commit generated reports to `docs/` or any public branch.

Browser extensions, local malware, screenshots, copied text, and developer tools remain outside the dashboard's control. Sensitive review should occur on a trusted workstation.

## Accessibility and usability

The dashboard uses native file input, buttons, headings, lists, and text status. Documentation changes should preserve keyboard access, visible focus, readable contrast, responsive layout, and meaningful text alternatives for diagrams.

## Change classification

The following are documentation-only when they accurately describe current behavior:

- clarifying scope and non-goals;
- explaining evidence handling;
- adding diagrams;
- improving onboarding; and
- documenting existing fields and thresholds.

The following are implementation changes and require separate review:

- changing collector commands or scan roots;
- adding collected data;
- changing thresholds;
- changing schema semantics;
- adding network behavior;
- adding remediation;
- adding storage, authentication, or collaboration; and
- changing Pages publication authority.
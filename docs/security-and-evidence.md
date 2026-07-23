# Security and Evidence Handling

Status: `DOCUMENTATION_ONLY — LOCAL, AUTHORIZED, HUMAN-REVIEWED USE`

## Threat model

JusticeForMe observes sensitive privilege and configuration state. Primary risks are:

- unauthorized collection from a system outside the operator's scope;
- accidental disclosure of hostnames, usernames, paths, package changes, or persistence mechanisms;
- modification of a live host during evidence collection;
- false confidence caused by incomplete privileges or unavailable tools;
- overinterpreting dashboard thresholds as proof of compromise;
- tampering with report files after collection;
- browser or extension access to a locally opened report; and
- workflow changes that silently introduce publication, credentials, telemetry, or remote execution.

## Collection controls

- Obtain explicit authorization before running the collector.
- Prefer a trusted administrative environment and an output directory with restrictive permissions.
- Do not alter system configuration to make a result appear cleaner or more complete.
- Record whether collection was root-complete.
- Preserve command errors and empty artifacts as evidence of limitations.
- Do not run the collector when doing so could disrupt a fragile system or overwrite higher-value forensic evidence.

## Report preservation

The generated SHA-256 manifest supports later file-identity checks:

```bash
cd /secure/path/justiceforme-case-001
sha256sum -c REPORT-SHA256SUMS.txt
```

A successful check means the listed bytes match the manifest. It does not prove who collected them, whether the host clock was correct, whether the live system changed during collection, or whether an artifact is truthful or complete.

For formal evidence handling, separately record:

- case or review identifier;
- operator and authorization source;
- host identity and acquisition context;
- collection start and completion times;
- time-source reliability;
- original output path and storage media;
- every transfer, copy, redaction, or transformation;
- independent verification results; and
- retention, access, and destruction decisions.

## Privacy and disclosure

Real reports should be treated as confidential operational data. Before sharing even within an authorized team, review whether the recipient needs:

- hostnames and domain details;
- user and group membership;
- local paths and service names;
- privileged binary and capability inventories;
- package-integrity output; and
- persistence and loader configuration.

Use synthetic fixtures for public documentation. Redaction creates a new derived artifact and must receive a new hash and transformation record.

## Dashboard security

The dashboard is intentionally local-only and dependency-free. It does not fetch remote scripts or transmit the selected report. Review reports in a trusted browser profile with unnecessary extensions disabled. Report strings must be rendered as text, not interpreted as HTML.

## Workflow security

The validation workflow must retain:

- `permissions: contents: read`;
- exact submitted-head checkout;
- `persist-credentials: false`;
- pinned action commit identifiers;
- absence of `pages: write`, `id-token: write`, deployment actions, push publication, and manual deployment triggers; and
- deterministic retained evidence.

Any change that introduces write authority, secrets, OIDC, deployment, remote upload, or unattended collection requires separate security and governance approval.

## Interpretation discipline

A finding is an observation requiring validation. The project must never claim that a count, hash, package-verifier line, recent timestamp, privilege bit, or dashboard severity proves malicious activity, attribution, legal responsibility, or compliance failure.

## Correction and rollback

When documentation, thresholds, schema meaning, or collection behavior is found to be wrong:

1. preserve the affected version and exact commit;
2. identify report generations and users that relied on it;
3. publish a bounded correction without exposing real host data;
4. update every controlled documentation and planning route;
5. verify the corrected exact head; and
6. restore a supported prior interpretation or mark the affected generation withdrawn.

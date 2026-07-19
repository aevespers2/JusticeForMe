# Contributing to JusticeForMe

Thank you for helping improve this public-interest Linux audit project.

## Scope first

JusticeForMe is a bounded defensive auditing tool. Contributions should improve the existing read-only collector, local report contract, static dashboard, documentation, or validation evidence without silently expanding the project into remote administration, surveillance, remediation, fleet management, malware attribution, or hosted report storage.

When a proposal changes what data is collected, how findings are interpreted, or where reports move, treat it as an architecture and security change rather than a small implementation detail.

## Ways to contribute

- Test the collector on Linux systems you own or are authorized to inspect.
- Report false positives, missing controls, portability issues, or unclear explanations.
- Propose safer collection methods, stronger provenance, improved accessibility, or clearer dashboard semantics.
- Improve architecture, design, onboarding, security, release, and operations documentation.
- Fork the repository and create specialized versions while preserving attribution and safety notices.

## Developer onboarding

### 1. Clone and inspect

```bash
git clone https://github.com/aevespers2/JusticeForMe.git
cd JusticeForMe
```

Read, in order:

1. `README.md`
2. `ARCHITECTURE.md`
3. `DESIGN.md`
4. `SECURITY.md`
5. `taskchain.md`
6. `release.md`
7. `changelog.md`

### 2. Review the collector

The collector is a single Bash script:

```text
audit/linux-privilege-audit.sh
```

Before running it, inspect every command and choose a disposable or explicitly authorized test host. Do not use a production system as the first validation environment.

### 3. Run a bounded local check

```bash
bash -n audit/linux-privilege-audit.sh
chmod +x audit/linux-privilege-audit.sh
./audit/linux-privilege-audit.sh ./tmp-audit-output
```

A non-root run is useful for smoke testing but is expected to be incomplete. Review the generated output, then remove it securely when no longer needed. Never commit generated evidence.

When available, run ShellCheck separately:

```bash
shellcheck audit/linux-privilege-audit.sh
```

ShellCheck is recommended but is not currently enforced by the repository workflow.

### 4. Review the Pages site

Serve the static files locally:

```bash
python3 -m http.server 8000 --directory docs
```

Open `http://localhost:8000`, load demonstration data, and then load a synthetic `report.json` fixture. Do not use sensitive host reports for routine frontend testing.

### 5. Validate documentation

Confirm that:

- the dashboard links to the project guide;
- every guide section is keyboard reachable;
- repository links resolve;
- headings follow a logical hierarchy;
- diagrams have equivalent text explanations; and
- no generated report or host-specific detail appears in the change.

## Synthetic dashboard fixture

```json
{
  "schema_version": "1.0",
  "generated_at": "2026-01-01T00:00:00Z",
  "host": "synthetic-host",
  "root_complete": false,
  "metrics": {
    "world_writable_etc": 0,
    "executable_files_etc": 4,
    "privileged_binaries": 18,
    "file_capabilities": 2,
    "package_integrity_findings": 0,
    "recent_etc_changes_30d": 12
  },
  "artifacts": [
    "etc-metadata.txt",
    "etc-sha256.txt",
    "privileged-binaries.txt",
    "package-integrity.txt"
  ],
  "notice": "Synthetic test data only."
}
```

## Testing reports

Never attach secrets, credentials, private keys, full `/etc` archives, personal data, or live investigative evidence to a public issue. Share only minimized, redacted examples that are safe for public disclosure.

When reporting a result, include:

1. distribution and version;
2. whether the collector ran with `sudo`;
3. the relevant metric or artifact name;
4. expected and observed behavior; and
5. a redacted reproduction case when possible.

## Change categories

### Documentation-only

- correct descriptions of current behavior;
- architecture diagrams;
- onboarding improvements;
- evidence-handling guidance;
- accessibility improvements that do not change interpretation; and
- release-evidence templates.

### Collector behavior

- new commands or scan roots;
- changed filesystem traversal;
- changed error handling;
- new artifacts;
- changed package-verifier selection; or
- changed summary metrics.

These require shell validation, distribution testing, security review, and updated design documentation.

### Dashboard behavior

- changed thresholds;
- changed schema acceptance;
- new parsing behavior;
- new persistence or network access;
- new third-party scripts; or
- new claims about findings.

These require browser tests, security/privacy review, accessibility review, and explicit release evidence.

## Pull request checklist

- [ ] The change has a single, clear purpose.
- [ ] Current scope and non-goals remain accurate.
- [ ] `taskchain.md`, `release.md`, and `changelog.md` are updated when applicable.
- [ ] Collector changes pass `bash -n` and ShellCheck where available.
- [ ] Dashboard changes are tested with valid, invalid, incomplete, and synthetic reports.
- [ ] No real host report, credential, personal data, or environment-specific secret is included.
- [ ] Documentation distinguishes indicators from proof.
- [ ] New diagrams include text descriptions.
- [ ] Security, privacy, accessibility, compatibility, and rollback impacts are described.
- [ ] No release gate is marked complete without retained evidence.

## Review expectations

Reviewers should challenge:

- unsupported forensic or security claims;
- scope expansion hidden as convenience work;
- collection of unnecessary sensitive data;
- assumptions that one distribution represents all Linux systems;
- threshold changes without evidence;
- report contract changes without migration guidance; and
- publication or release claims without reproducible validation.

## Generated files

Do not commit collector output. Suggested local exclusions include:

```text
justiceforme-audit-*/
tmp-audit-output/
report.json
REPORT-SHA256SUMS.txt
```

Repository ignore rules should be changed only after confirming they do not hide intentional fixtures or documentation examples.

## Contact

For collaboration inquiries, contact Jacob at Jacob@vespersinc.com.

JusticeForMe is independent and is not affiliated with organizations linked from its resource directory unless an affiliation is expressly documented.
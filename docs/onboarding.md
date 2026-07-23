# JusticeForMe Onboarding

Status: `DOCUMENTATION_ONLY — AUTHORIZED LOCAL USE`

This guide is for maintainers and authorized operators. It does not authorize inspection of systems you do not own or administer.

## Before running the collector

1. Confirm written or otherwise explicit authorization for the target host.
2. Choose an output location with enough space and access controls appropriate for sensitive host metadata.
3. Record the host, operator, purpose, date, time source, and expected package baseline outside the generated report directory.
4. Decide whether root-complete collection is necessary. Running without root is supported, but the report will be marked incomplete.
5. Do not use a production host as a public demonstration target.

## First local run

```bash
chmod +x audit/linux-privilege-audit.sh
sudo ./audit/linux-privilege-audit.sh
```

To choose a destination explicitly:

```bash
sudo ./audit/linux-privilege-audit.sh /secure/path/justiceforme-case-001
```

The script prints the output directory when collection finishes.

## Review the report safely

1. Preserve the report directory before opening or transforming files.
2. Verify `REPORT-SHA256SUMS.txt` from inside the report directory:

   ```bash
   sha256sum -c REPORT-SHA256SUMS.txt
   ```

3. Open `docs/index.html` from a trusted local checkout.
4. Select the generated `report.json` using the file control.
5. Treat dashboard priorities as prompts for review, not findings of compromise.
6. Compare detailed artifacts with trusted package metadata, known-good host baselines, and documented administrative changes.

## Evidence-handling minimums

- Keep the original report directory read-only after collection where practical.
- Record any copies, exports, redactions, or transformations.
- Hash transformed copies separately; do not overwrite the original manifest.
- Avoid public issue attachments, chat uploads, or cloud synchronization unless separately authorized.
- Redact hostnames, usernames, group memberships, paths, and package details before preparing public examples.
- Use synthetic demonstration data for documentation and tests.

## Maintainer setup

The repository has no package installation step. Validation requires tools available on a standard Ubuntu GitHub runner:

- Bash
- Python 3
- Node.js

Run local syntax checks:

```bash
bash -n audit/linux-privilege-audit.sh
node --check docs/app.js
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

## Safe first contribution

A good first change is a documentation correction, a synthetic fixture improvement, or an accessibility refinement. Keep the change focused and update all affected planning files:

- `taskchain.md`
- `punchlist.md`
- `release.md`
- `changelog.md`

Do not add Pages deployment, push-triggered publication, OIDC, write permissions, telemetry, remote report upload, unattended remote collection, or privileged execution without separate approval.

## When to stop

Stop and preserve the current state when:

- authorization is uncertain;
- the collector would affect availability or evidence preservation;
- sensitive data would leave the approved environment;
- the host is changing too quickly for a meaningful snapshot;
- package metadata cannot be trusted; or
- a finding requires specialist forensic handling beyond this tool's scope.

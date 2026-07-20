# Developer and Reviewer Onboarding

## Prerequisites

Use a disposable or authorized Linux environment for collector testing. Required tools are:

- Bash;
- Python 3;
- Node.js for dashboard syntax validation;
- standard GNU/Linux utilities used by the collector;
- one supported package manager (`dpkg`, `rpm`, or `pacman`) for package-integrity coverage;
- optional `getcap` for Linux file-capability inventory.

Do not test against a device you do not own or have explicit permission to inspect.

## Local documentation and dashboard review

```bash
git clone https://github.com/aevespers2/JusticeForMe.git
cd JusticeForMe

bash -n audit/linux-privilege-audit.sh
node --check docs/app.js
python3 -m http.server --directory docs 8000
```

Open `http://127.0.0.1:8000/` and use demonstration data or a locally generated report. The dashboard can also be opened directly from the filesystem.

## Collector run

```bash
chmod +x audit/linux-privilege-audit.sh
sudo ./audit/linux-privilege-audit.sh /path/to/authorized-output
```

Before sharing or moving evidence:

1. record the exact JusticeForMe commit;
2. preserve the generated directory without editing files;
3. verify `REPORT-SHA256SUMS.txt` from inside the report directory;
4. record operating-system and tool versions separately;
5. classify the report's privacy sensitivity;
6. avoid public repository, issue, log, or artifact upload.

## Change workflow

1. Read `README.md`, `taskchain.md`, `punchlist.md`, `release.md`, and `changelog.md`.
2. Identify whether the change affects documentation, dashboard presentation, collector observations, report semantics, or portfolio integration.
3. Keep implementation and documentation changes separately reviewable where practical.
4. For report-contract changes, add compatibility fixtures before changing field semantics.
5. For collector changes, document command availability, timeout, partial-result, privilege, privacy, and false-positive behavior.
6. Run exact-head validation in a pull request.
7. Record limitations and rollback instructions.

## Review checklist

### Collector

- Does the change remain read-only with respect to the audited host?
- Are paths quoted and null-delimited where required?
- Are optional files and commands handled without turning absence into success?
- Are timeouts bounded?
- Are permission errors or partial results represented honestly?
- Does output avoid secrets and unnecessary content?
- Does it work when standard scan roots are absent?

### Dashboard

- Does parsing remain local?
- Are all inserted values treated as text rather than trusted HTML?
- Is an unsupported schema rejected clearly?
- Are thresholds described as heuristics?
- Is accessibility preserved?
- Are scripts and styles local and pinned to repository source?

### Documentation and governance

- Are implemented, proposed, validated, approved, released, and deployed states distinguished?
- Are Repository `0` and Repository `1` roles described as proposed integration unless accepted?
- Are findings described as indicators rather than proof or attribution?
- Are privacy, evidence preservation, rollback, and authority boundaries explicit?

## Safe test strategy

Use synthetic fixtures and disposable containers or virtual machines for ordinary development. Avoid manufacturing suspicious privileged state on a production host merely to test dashboard thresholds. Negative fixtures should include malformed JSON, wrong schema versions, missing metrics, extreme values, unexpected artifact names, stale timestamps, and partial collection status once an envelope exists.

## Reporting security concerns

Do not place live credentials, raw private audit reports, personally identifying host data, or exploit instructions in public issues. Report the minimum reproducible metadata and preserve sensitive evidence through an approved private channel.

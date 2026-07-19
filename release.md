# Release Readiness

## Status

**Release status: blocked pending validation, governance, and retained evidence.**

The repository contains an implemented collector and static dashboard, but no tagged release, production-readiness claim, forensic-certification claim, or support commitment should be inferred from source availability or documentation completeness.

## Implemented baseline

The current baseline includes:

- a Bash collector for selected Linux configuration and privilege indicators;
- timestamped local output;
- a compact `report.json` summary with `schema_version: "1.0"`;
- detailed plain-text artifacts;
- a SHA-256 manifest for generated top-level report files;
- a static browser dashboard with fixed heuristic thresholds; and
- GitHub Pages deployment of the static `docs/` directory.

## Mandatory release gates

### 1. Scope and claims

- [ ] Release notes describe only implemented behavior.
- [ ] Indicators are never described as proof of compromise, misconduct, or attribution.
- [ ] Read-only scope is verified against the exact release commit.
- [ ] Non-goals and unsupported platforms are explicit.
- [ ] No production, compliance, or forensic-certification claim exceeds the evidence.

### 2. Collector verification

- [ ] `bash -n` passes on the exact release commit.
- [ ] ShellCheck passes or every retained finding has an approved disposition.
- [ ] Root and non-root behavior are tested.
- [ ] Optional-tool and missing-directory behavior are tested.
- [ ] Output-path safety, quoting, interruption, disk-space, and partial-output behavior are tested.
- [ ] All declared artifacts are reconciled with actual output.
- [ ] The checksum manifest is independently verified.

### 3. Platform compatibility

- [ ] Supported distributions and versions are named.
- [ ] Supported Bash and Python versions are named.
- [ ] `dpkg`, `rpm`, and `pacman` verifier semantics are documented for supported platforms.
- [ ] Filesystem and mount-boundary limitations are documented.
- [ ] Known container, namespace, chroot, and immutable-system limitations are documented.

### 4. Report contract

- [ ] Schema `1.0` fields, types, meanings, and units are approved.
- [ ] Sanitized valid, boundary, incomplete, and malformed fixtures are retained.
- [ ] Compatibility behavior for unknown and missing fields is tested.
- [ ] A decision is recorded on formal JSON Schema publication.
- [ ] Schema-change and migration policy is approved.

### 5. Dashboard quality

- [ ] Threshold boundaries match `DESIGN.md` exactly.
- [ ] Unsupported schemas are rejected as documented.
- [ ] Oversized, malformed, and adversarial local files are tested.
- [ ] Browser network inspection confirms no report transmission.
- [ ] Keyboard, focus, contrast, responsive layout, and status behavior are reviewed.
- [ ] The exact Pages artifact is tested, not only a local working tree.

### 6. Security, privacy, and evidence handling

- [ ] Collector commands receive security review.
- [ ] Elevated-execution and output-directory risks receive security review.
- [ ] Browser parsing receives security review.
- [ ] Generated-data sensitivity and redaction guidance are approved.
- [ ] Retention, transfer, deletion, and chain-of-custody guidance are approved.
- [ ] Private vulnerability reporting is available.
- [ ] No real host report, credential, personal data, or investigative evidence exists in release artifacts.

### 7. Documentation

- [ ] README, architecture, design, security, onboarding, task chain, release, and changelog documents agree.
- [ ] GitHub Pages navigation and repository links are validated.
- [ ] Diagrams match current implementation and include text explanations.
- [ ] Commands are tested from a clean clone.
- [ ] Documentation distinguishes current behavior from proposals.

### 8. Supply chain and provenance

- [ ] Exact source commit is recorded.
- [ ] Workflow action-resolution policy is approved.
- [ ] Pages artifact digest is retained.
- [ ] Validation-tool versions and environments are retained.
- [ ] Reviewers and approval dates are recorded.
- [ ] License and redistribution terms are confirmed.

### 9. Operations and rollback

- [ ] Collector rollback target is recorded and tested.
- [ ] Pages rollback target is recorded and tested.
- [ ] Partial collection recovery is documented.
- [ ] Incident procedure covers accidental report publication.
- [ ] Release withdrawal and correction procedures are documented.
- [ ] Maintainer and security-review ownership are confirmed.

### 10. Human approval

- [ ] Technical review approved.
- [ ] Security/privacy review approved.
- [ ] Documentation review approved.
- [ ] Release owner approved the exact commit and artifact.
- [ ] Remaining risks and limitations are accepted in writing.

## Evidence record template

For every gate, retain:

| Field | Required value |
| --- | --- |
| Gate | Checklist item identifier |
| Result | Pass, fail, blocked, or not applicable |
| Exact commit | Full Git SHA |
| Environment | Distribution, version, architecture, browser, and relevant tools |
| Procedure | Reproducible command or test steps |
| Evidence | Log, screenshot, fixture, report, or artifact digest |
| Reviewer | Named human reviewer |
| Date | UTC date and time |
| Notes | Limitations, deviations, and disposition |

A checkbox must not be marked complete solely because work was attempted. The evidence must be reviewable and tied to the exact candidate.

## Release-blocking architectural decisions

Release remains blocked until the repository has explicit decisions for:

- license and redistribution;
- supported Linux scope;
- maintainer and security-review ownership;
- schema stability and compatibility;
- support status;
- data-retention guidance; and
- publication and release authority.

## Prohibited release claims without additional evidence

Do not describe the current project as:

- a certified forensic acquisition tool;
- a compromise detector;
- a malware scanner;
- a complete persistence detector;
- a compliance certification system;
- tamper-proof or court-admissible by default;
- safe for unattended production deployment; or
- supported across all Linux distributions.
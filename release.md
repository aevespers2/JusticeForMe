# JusticeForMe Release Plan

## Current decision

Status: `BLOCKED_PUBLICATION_NOT_AUTHORIZED`

JusticeForMe is currently a local-use, documentation-and-validation candidate. The collector and dashboard may be reviewed from source, but GitHub Pages publication, packaged distribution, remote execution, telemetry, report upload, production deployment, credentials, OIDC, and automated incident-response authority are excluded.

## Candidate scope

The bounded documentation candidate includes:

- read-only collector source;
- local dependency-free dashboard;
- report schema `1.0` documentation;
- project overview, architecture, onboarding, developer, security, and evidence guidance;
- task chain, punch list, release plan, and changelog;
- exact-head pull-request validation; and
- retained deterministic validation evidence.

## Acceptance gates

| Gate | Status | Requirement |
|---|---|---|
| Scope | REVIEW | Local read-only auditing and human interpretation only |
| Documentation | REVIEW | All reader and maintainer routes are complete and consistent |
| Links and navigation | PENDING | Internal Markdown and HTML routes pass at the final exact head |
| Accessibility | PENDING | Semantic structure, labels, keyboard access, focus, non-color meaning, and prose-equivalent diagrams pass |
| Report schema | REVIEW | Schema `1.0` fields, types, compatibility, and rejection behavior are documented |
| Synthetic tests | INCOMPLETE | Valid and hostile report fixtures are still required |
| Security and privacy | REVIEW | Real reports remain local and excluded from public Git, CI, and issues |
| Evidence provenance | PENDING | Exact source, deterministic hashes, artifact identity, and expiration are retained |
| Workflow least privilege | REVIEW | `contents: read`, pinned actions, exact-head checkout, and no deployment authority |
| License | BLOCKED | No license decision has been recorded |
| Ownership | BLOCKED | Documentation, accessibility, schema, security, release, and correction owners are unnamed |
| Publication | BLOCKED | Explicit approval and a separately reviewed deployment design are absent |

## Artifact requirements

A review-ready documentation candidate should retain:

- exact repository and submitted commit;
- workflow run and attempt;
- collector and JavaScript syntax results;
- HTML and documentation-route results;
- planning-alignment results;
- action and tool versions;
- SHA-256 identities for validated inputs; and
- artifact expiration.

Validation evidence is not operational evidence from an audited host and must not include real reports.

## Versioning

- Current report interface: `1.0`.
- Documentation changes remain unreleased until an explicit release decision.
- Incompatible report changes require a new schema version and migration/rollback guidance.
- Dashboard threshold changes require provenance, calibration evidence, and a changelog entry.

## Rollback criteria

Rollback is required when a candidate introduces report disclosure, state-changing collection, unsupported schema reinterpretation, inaccessible controls, broken routes, misleading forensic claims, workflow write authority, unpinned external execution, or documentation contradictions. The rollback must restore a supported prior state or explicitly mark the affected guidance and report generation withdrawn.

## Publication rule

A passing workflow does not authorize Pages publication. Publication requires a separate review of privacy, sensitive-data risk, licensing, accessibility, security headers and dependencies, correction and withdrawal propagation, named ownership, release approval, and resulting deployed-state verification.

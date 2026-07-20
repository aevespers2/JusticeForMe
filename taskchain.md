# Task Chain

## Product directive

JusticeForMe provides read-only Linux host observations and local evidence review. Its immediate objective is to preserve the current collector/dashboard scope while defining the contracts, evidence semantics, and governance required for safe integration with the Repository `0`/`1` portable device-security foundation.

## Current priority

**P0 — Documentation, evidence semantics, and integration-boundary review.**

No collector remediation, remote transport, credential use, scheduled enforcement, or production authority is authorized.

## Success criteria

- Current collector behavior and non-capabilities are documented accurately.
- Report schema `1.0`, supporting artifacts, thresholds, and failure semantics are explicit.
- GitHub Pages exposes a safe project and architecture guide without publishing private audit evidence.
- The Repository `0` observation boundary and Repository `1` baseline/capability boundary are proposed without activation.
- Material gluing obstructions and required shared fixtures are recorded.
- Release, punch-list, changelog, validation, privacy, rollback, and recovery guidance agree.

## Active chain

| Priority | Task | Depends on | Status | Acceptance criteria |
|---|---|---|---|---|
| P0A | Complete Pages and repository documentation | — | REVIEW | Overview, architecture, contract, onboarding, operations, obstruction analysis, diagrams, and coordination files are present and internally linked. |
| P0B | Validate documentation and existing implementation boundary at exact head | P0A | READY | Shell, JavaScript, HTML, documentation links, required files, and absence of deployment authority pass against the submitted head. |
| P0C | Approve JusticeForMe portfolio role | P0A, Architect approval | BLOCKED | Standalone-tool versus Repository `0` observation-adapter role, owner, supported platform, and non-goals are accepted. |
| P1 | Assign evidence-envelope and cross-repository contract ownership | P0C, Repository `0`/`1` governance | PROPOSED | Device identity, provenance, per-check status, freshness, privacy, proposal, capability, receipt, revocation, and recovery schemas have one owner and version policy. |
| P2 | Specify deterministic compatibility fixtures | P1 | PROPOSED | Valid, partial, failed, unsupported, stale, replayed, malformed, identity-mismatched, rollback, and privacy-negative fixtures are approved at immutable commits. |
| P3 | Decide report schema evolution | P2 | PROPOSED | Schema `1.0` remains wrapped or a new version is accepted with compatibility and migration evidence. |
| P4 | Implement a bounded Repository `0` observation adapter | P3 | PROPOSED | Adapter is local, read-only, least-privilege, off by default, evidence-preserving, and accepted by shared fixtures. |
| P5 | Exercise Repository `1` quarantine and baseline comparison | P4 | PROPOSED | No remediation occurs; identity, freshness, evidence, policy, replay, and expected-head checks fail closed. |
| P6 | Consider narrowly scoped remediation proposals | P5, independent security review, explicit approval | PROPOSED | Observation remains separate from remediation; capabilities are device-bound, reversible, expiring, audited, and human-reviewable. |

## Builder rules

Builders may work only on `READY` tasks. Documentation, local validation, synthetic fixtures, and evidence-preserving contract proposals are permitted. Changes that inspect additional sensitive surfaces, modify the host, transmit reports, use credentials, create remote services, issue capabilities, or remediate configuration require separately approved tasks.

## Evidence rules

Every material task records:

- exact source commit and changed files;
- implemented versus proposed behavior;
- commands and tool versions;
- positive, negative, and partial results;
- privacy and evidence-handling effects;
- unsupported platforms or checks;
- limitations and residual risks;
- rollback and incident paths;
- approval status.

## Builder log

- 2026-07-20 — Prepared a Pages and portfolio-integration documentation candidate defining JusticeForMe as a read-only Linux observation component, documenting schema `1.0`, architecture, onboarding, operations, recovery, and fourteen gluing obstructions without changing collector or dashboard behavior.

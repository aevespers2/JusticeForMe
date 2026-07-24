# JusticeForMe Task Chain

Repository status: `DOCUMENTATION_ONLY — LOCAL USE; PUBLICATION NOT AUTHORIZED`

Accessibility review status: `DOCUMENTED_NOT_CERTIFIED`

States: `PROPOSED` · `IN PROGRESS` · `REVIEW` · `BLOCKED` · `DONE`

## Repository role

JusticeForMe is a bounded, read-only Linux privilege and configuration auditing tool. It produces local evidence for human review and does not operate a remote scanner, forensic conclusion engine, compliance authority, accessibility-certification authority, or publication service.

## Active chain

| Priority | Task | Depends on | Status | Acceptance criteria |
|---|---|---|---|---|
| P0 | Establish a complete documentation and planning baseline | — | REVIEW | Project overview, architecture, onboarding, developer guide, schema, security/evidence guidance, accessibility-review protocol, local documentation front door, and planning files agree. |
| P0.1 | Preserve local-only collection and dashboard boundaries | P0 | REVIEW | Collector writes only to the chosen output directory; dashboard loads explicit local JSON; no telemetry or remote upload exists. |
| P0.2 | Validate report schema `1.0` and interpretation limits | P0 | REVIEW | Fields, types, metrics, compatibility, rejection behavior, and non-proof language are documented and tested. |
| P0.3 | Validate accessibility and documentation routes | P0 | REVIEW | HTML landmarks, labels, keyboard-accessible controls, local assets, prose-equivalent diagrams, local links, exact-artifact evidence states, and certification denials pass exact-head validation. |
| P0.4 | Preserve workflow least privilege and retained evidence | P0-P0.3 | REVIEW | Read-only permissions, exact-head checkout, pinned actions, deployment prohibition, deterministic hashes, artifact retention, and clean-tree checks pass. |
| P0.5 | Perform rendered accessibility review | P0.3-P0.4 and approved scope | BLOCKED | Exact non-deploying artifact, reviewer, browser/assistive-technology matrix, manual evidence, limitations, correction route, and certification boundary are approved and retained. |
| P1 | Add synthetic schema fixtures and parser regressions | P0.2-P0.4 | PROPOSED | Accepted, rejected, incomplete, and future-schema fixtures remain synthetic and receive deterministic validation. |
| P2 | Define distribution-specific baseline profiles | P1 | BLOCKED | Baselines have named owners, evidence, versioning, false-positive analysis, migration, and rollback; dashboard thresholds do not silently become standards. |
| P3 | Evaluate optional Pages publication | P0-P2 and explicit approval | BLOCKED | Privacy, licensing, accessibility, security, release, correction, withdrawal, and deployment ownership are approved separately. |

## Invariants

- Authorized systems only.
- Read-only collection outside the chosen output directory.
- Real reports remain outside public Git and CI.
- Indicators remain distinct from findings, attribution, legal conclusions, and compliance decisions.
- Automated accessibility checks remain distinct from rendered review and certification.
- Schema meaning is versioned and never silently reinterpreted.
- Historical accessibility evidence never validates a moved source head or changed renderer.
- Passing CI does not authorize publication, release, remote execution, privileged deployment, or accessibility certification.

## FYSA-120 capability map

Applied categories: CAT-011, CAT-012, CAT-017, CAT-018, CAT-019, CAT-031, CAT-040, CAT-052, CAT-054, CAT-056, and CAT-064.

Proposed non-authoritative subdivisions:

- `056-F — Forensic-tool documentation and interpretation-boundary engineering`, covering collector scope narration, completeness signaling, indicator-versus-conclusion separation, chain-of-custody guidance, synthetic evidence examples, and rollback-safe correction propagation.
- `019-Q — Exact-artifact accessibility evidence for local security-review interfaces`, covering source/artifact binding, manual-environment evidence, accessibility-state vocabulary, correction-linked review, and certification separation.

Taxonomy mapping does not certify competence, appoint a reviewer, approve publication, or expand project authority.
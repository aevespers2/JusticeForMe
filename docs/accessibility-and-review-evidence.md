# Accessibility and Review Evidence

Status: `DOCUMENTED_NOT_CERTIFIED`

JusticeForMe documents an accessibility review protocol for its static dashboard, local project guide, repository documentation, and any retained rendered artifact. This protocol does not certify accessibility, authorize GitHub Pages publication, approve collector execution, or convert a documentation check into forensic, security, privacy, or release approval.

This page preservation-safely carries forward the unique accessibility-review material developed on historical documentation candidate `docs/portfolio-integration-20260720@33db861320c29e71059ec390cbdafe04c8f8793d` while using the current default-branch documentation layout. The historical branch remains intact and is not treated as current validation evidence.

## Review surfaces

Each surface is reviewed and recorded separately.

| Surface | Current form | Primary accessibility risks | Evidence boundary |
|---|---|---|---|
| Audit dashboard | `docs/index.html`, `docs/app.js`, `docs/styles.css` | File-input labeling, focus order, status announcements, dense metric interpretation, error recovery, zoom, and reflow | Exact source plus the exact non-deploying rendered artifact |
| Project guide | `docs/guide.html`, `docs/styles.css` | Heading order, navigation, long procedures, links, zoom, and reflow | Exact source plus the exact non-deploying rendered artifact |
| Repository Markdown | README and `docs/*.md` | Link clarity, heading hierarchy, diagram alternatives, tables, and code-block comprehension | Exact source commit and rendered repository view |
| Generated audit evidence | Local reports and report directories | Sensitive data, dense technical output, ambiguous missing-state semantics | Excluded from public review artifacts; synthetic or minimized fixtures only |
| Future portfolio adapters | Not implemented | Authority-state comprehension, identity, provenance, correction, and error communication | Separate review after an approved interface exists |

A pass for one surface is not transferable to another surface, browser, viewport, operating system, input method, rendering engine, or assistive technology.

## Review-state vocabulary

Use exactly one of these states for every reviewed surface and check set:

- `NOT_REVIEWED` — no qualifying review evidence exists.
- `PARTIAL` — some required checks were completed and the remainder is listed.
- `PASS` — the named checks passed for the exact artifact and environment.
- `FAIL` — one or more named checks failed.
- `BLOCKED` — an artifact, environment, tool, permission, or reviewer was unavailable.
- `UNKNOWN` — evidence is insufficient or contradictory.
- `SUPERSEDED` — a later artifact or correction replaced the reviewed target.
- `WITHDRAWN` — the evidence or claim was intentionally retracted.
- `CORRECTED` — a defect was repaired and linked to a new evidence generation.

`PASS` means only that the recorded checks passed. It does not mean universal conformance, certification, security approval, publication approval, or release readiness.

## Evidence flow

```mermaid
flowchart LR
    S[Exact source commit] --> B[Non-deploying rendered artifact]
    B --> A[Automated structural checks]
    B --> M[Manual keyboard, zoom, contrast, screen-reader, and comprehension review]
    A --> R[Accessibility evidence record]
    M --> R
    R --> D{Bounded disposition}
    D -->|named checks satisfied| P[Documented review result]
    D -->|defect or missing evidence| F[Fail, block, unknown, or partial]
    F --> C[Correction or withdrawal]
    C --> S2[New exact source generation]
```

**Equivalent prose:** bind the review to one exact source generation, render a non-deploying artifact, run automated structural checks, perform the required manual reviews, record successes and limitations, and issue only a bounded disposition. A defect, moved head, changed renderer, or missing check requires a failed, blocked, unknown, partial, superseded, withdrawn, or corrected record instead of silent reuse of earlier evidence.

## Required evidence fields

Every accessibility review record must include:

- repository and full source commit;
- reviewed paths and surface identifiers;
- workflow run and rendered-artifact identifier, when applicable;
- artifact digest and creation time;
- browser, operating system, viewport, zoom level, display scaling, and rendering method;
- input methods used;
- assistive technology and version, when used;
- automated checks and tool versions;
- manual procedures and observed results;
- defects, limitations, unsupported combinations, and blocked checks;
- reviewer identity or approved review role;
- correction, withdrawal, and supersession links; and
- publication, release, collector, remediation, certification, and authority status.

Example documentation-only record:

```yaml
schema: justiceforme.accessibility-review.v1
status: PARTIAL
source:
  repository: aevespers2/JusticeForMe
  commit: FULL_COMMIT_SHA
surface:
  id: static-dashboard
  paths:
    - docs/index.html
    - docs/app.js
    - docs/styles.css
artifact:
  id: NON_DEPLOYING_ARTIFACT_ID
  sha256: ARTIFACT_DIGEST
environment:
  browser: NAME_AND_VERSION
  operating_system: NAME_AND_VERSION
  viewport: 1280x720
  zoom: 200-percent
checks:
  keyboard: PASS
  focus_visibility: PASS
  screen_reader: NOT_REVIEWED
  contrast: PARTIAL
  reflow_200: PASS
  reflow_400: NOT_REVIEWED
  reduced_motion: PASS
  error_recovery: PARTIAL
limitations:
  - Manual screen-reader review remains pending.
authority:
  accessibility_certification: denied
  pages_publication: denied
  collector_execution: denied
  host_inspection: denied
  remediation: denied
  release: denied
```

This template is synthetic and non-executable. It contains no host report, credential, device identity, or private evidence.

## Review protocol

### Keyboard and focus

- Reach every interactive control using the keyboard alone.
- Confirm a logical focus order and visible focus indicator.
- Confirm the file input has a programmatically associated label.
- Confirm every demonstration or reset control is reachable and operable.
- Confirm status changes are announced without moving focus unexpectedly.
- Confirm errors leave a usable recovery path.
- Confirm no keyboard trap exists.

### Screen-reader and semantic structure

- Confirm one clear page title and one primary `h1`.
- Confirm landmarks, headings, lists, tables, labels, and status regions expose meaningful names and roles.
- Confirm metric names, values, and severity are understandable without visual position or color.
- Confirm report errors and unsupported-schema messages are announced.
- Confirm every architecture or evidence-flow diagram has complete prose equivalence.
- Confirm link text remains understandable outside its surrounding sentence.

### Zoom, reflow, and responsive use

- Review at 200% and 400% zoom.
- Confirm controls, status text, metrics, navigation, tables, code blocks, and guidance reflow without information loss or two-dimensional scrolling except where intrinsically necessary.
- Confirm touch targets and spacing remain usable on narrow viewports.
- Confirm long paths, hashes, and commands wrap or scroll without obscuring adjacent content.

### Contrast and non-color communication

- Check text, controls, borders, focus indicators, links, and status elements against the rendered background.
- Confirm `ok`, `warn`, and `high` states include text and do not depend on border color alone.
- Confirm selected, current, failed, blocked, partial, and unknown states remain distinguishable in forced-colors or high-contrast modes where available.

### Motion and timing

- Confirm the site works with `prefers-reduced-motion` enabled.
- Do not add essential timed interactions, auto-advancing content, or animation-dependent meaning.
- Confirm large local files and parsing errors do not leave the interface in an unexplained busy state.

### Cognitive access and risk communication

- Keep procedures stepwise and state prerequisites before commands.
- Distinguish observation, heuristic severity, evidence, interpretation, proposal, approval, and remediation.
- Explain partial, unsupported, timed-out, failed, and unknown collection states without representing them as verified absence.
- Keep the warning that findings are indicators rather than proof near the relevant output.
- Use synthetic examples for public documentation and routine review.

### Privacy and local-only behavior

- Use only synthetic or minimized fixtures during accessibility review.
- Confirm the dashboard makes no network request while loading a report.
- Do not include real hostnames, usernames, file paths, privilege relationships, credentials, or raw audit output in public evidence.
- Treat screenshots, recordings, browser logs, and assistive-technology transcripts as potentially sensitive review artifacts.

## Automated checks versus certification

Automated validation may verify source identity, required landmarks, labels, local links, local scripts and styles, deployment prohibition, and required documentation markers. It cannot establish screen-reader usability, comprehension, sufficient contrast in every environment, 400% reflow, cognitive accessibility, or conformance to every applicable standard.

The repository therefore records `DOCUMENTED_NOT_CERTIFIED`. A later certification claim requires an approved standard, scope, reviewer, exact rendered artifact, retained manual evidence, correction policy, and explicit human approval.

## Correction, withdrawal, and supersession

- A moved source head invalidates currentness until the descendant is reviewed.
- A rendering, stylesheet, JavaScript, content, browser, workflow, or assistive-technology change requires impact analysis and renewed checks.
- A discovered defect changes the affected record to `FAIL`, `PARTIAL`, `UNKNOWN`, `CORRECTED`, or `WITHDRAWN` as appropriate.
- Preserve the original record and link the correction; do not rewrite history as though the defect never existed.
- Withdraw any claim that cannot be reproduced from the recorded source and artifact.

## Fail-closed stop conditions

Stop review or publication disposition when:

- the exact source or rendered artifact cannot be identified;
- a public artifact contains real audit evidence or sensitive host data;
- keyboard access, focus, labeling, status announcement, or error recovery is materially broken;
- critical meaning depends on color, motion, pointer use, or visual layout alone;
- automated checks are represented as accessibility certification;
- a historical pass is presented as evidence for a moved head; or
- publication, collector execution, remediation, release, or operational authority is implied by the review record.

## Reviewer onboarding

1. Read the README, project overview, architecture, report schema, security/evidence guide, and release plan.
2. Confirm the exact source generation and obtain the non-deploying rendered artifact.
3. Use synthetic fixtures only.
4. Perform automated and manual checks independently.
5. Record limitations and unsupported combinations explicitly.
6. Link every defect to a correction, withdrawal, accepted-risk, or blocked disposition.
7. Keep accessibility review separate from security, privacy, forensic correctness, publication, integration, and release approval.

## FYSA-120 capability map

Applied capabilities: `CAT-011-B/E`, `CAT-012-A/B/D/E`, `CAT-018-B/E`, `CAT-019-B/C/D`, `CAT-031-A/D/E`, and `CAT-040-E`.

Proposed non-authoritative refinement: `019-Q — Exact-artifact accessibility evidence for local security-review interfaces`.

The capability map does not certify a reviewer, appoint an owner, grant publication authority, or alter implementation scope.
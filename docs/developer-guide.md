# JusticeForMe Developer Guide

Status: `DOCUMENTATION_ONLY — CONTRIBUTION AND VALIDATION GUIDE`

## Repository layout

```text
.github/workflows/pages.yml      Exact-head pull-request validation
audit/linux-privilege-audit.sh   Read-only Linux collector
docs/index.html                  Local dashboard
docs/app.js                      Report parser and renderer
docs/styles.css                  Dashboard presentation
docs/guide.html                  Human-readable documentation front door
docs/*.md                        Architecture, onboarding, schema, and evidence guidance
tests/                           Documentation and contract regressions
taskchain.md                     Ordered work and dependencies
punchlist.md                     Bounded completion items
release.md                       Release and publication gates
changelog.md                     Notable documentation and behavior changes
```

## Design invariants

Every change must preserve these invariants unless a separately approved design decision replaces them:

1. Collection is local and read-only outside the chosen output directory.
2. Real host reports and operational secrets never enter public Git or CI.
3. The dashboard processes explicitly selected local JSON and performs no upload or telemetry.
4. Schema version and interpretation rules are explicit.
5. An indicator is never presented as proof of compromise, misconduct, attribution, or compliance.
6. Validation is tied to the submitted pull-request head.
7. Workflow permissions remain `contents: read` and deployment authority remains absent.
8. Passing CI does not authorize publication, release, privileged execution, or operational use.

## Collector changes

When adding a collection step:

- document why the data is necessary and how sensitive it is;
- avoid state-changing commands;
- restrict filesystem traversal with appropriate boundaries such as `-xdev` where needed;
- handle absent commands, paths, and permissions without misrepresenting completeness;
- keep output deterministic enough for review;
- add the artifact to `report.json` only when the file is always created; and
- update evidence-handling and privacy guidance.

## Report schema changes

Schema `1.0` is consumed by `docs/app.js`. Any incompatible change requires a new schema version, a migration note, synthetic fixtures for both supported and rejected forms, and explicit dashboard behavior for older reports. Do not silently reinterpret an existing field.

See [Report schema](report-schema.md).

## Dashboard changes

- Use semantic HTML and one primary `<main>` landmark.
- Preserve a single descriptive `<h1>`.
- Label every form control.
- Maintain keyboard access and visible focus.
- Do not convey severity only through color.
- Keep external scripts, fonts, trackers, and remote assets out of the dashboard.
- Treat all report strings as untrusted data and render them with text-safe DOM APIs.
- Provide equivalent prose when adding diagrams or complex visualizations.

## Documentation changes

Documentation is part of the validated product surface. Update links, terminology, status labels, scope boundaries, and planning controls together. The workflow checks local Markdown links and required alignment markers.

## Local validation

```bash
bash -n audit/linux-privilege-audit.sh
node --check docs/app.js
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

The pull-request workflow additionally checks exact source identity, deployment prohibition, HTML structure, documentation routes, planning consistency, deterministic hashes, and a clean source tree.

## Review checklist

- [ ] Scope and non-goals remain explicit.
- [ ] Sensitive data is absent.
- [ ] Collection remains read-only.
- [ ] Schema compatibility is preserved or versioned.
- [ ] Dashboard content remains accessible and local-only.
- [ ] Documentation and planning files agree.
- [ ] Workflow permissions remain least privilege.
- [ ] Exact-head evidence is retained.
- [ ] No release or publication authority is inferred from validation.

## Rollback

A documentation or code revert is not enough when a report schema or evidence-handling instruction has already been used. Rollback planning must identify affected report generations, local copies, published guidance, and downstream users, then restore either a supported prior state or a clearly withdrawn state.

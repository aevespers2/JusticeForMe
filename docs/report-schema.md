# JusticeForMe Report Schema 1.0

Status: `DOCUMENTATION_ONLY — CURRENT LOCAL INTERFACE`

`report.json` is the only structured interface consumed by the dashboard. The collector writes UTF-8 JSON with a trailing newline.

## Top-level object

| Field | Type | Required | Meaning |
|---|---|---:|---|
| `schema_version` | string | yes | Exact interface version; currently `1.0` |
| `generated_at` | RFC 3339 UTC string | yes | Collector generation time |
| `host` | string | yes | Short hostname observed by the collector |
| `root_complete` | boolean | yes | Whether the collector ran with root privileges |
| `metrics` | object | yes | Six integer review metrics |
| `artifacts` | array of strings | yes | Detailed files expected in the report directory |
| `notice` | string | yes | Human-review and non-proof warning |

## Metrics

| Field | Source | Interpretation limit |
|---|---|---|
| `world_writable_etc` | world-writable files and directories under `/etc` | Count alone does not establish exploitability |
| `executable_files_etc` | executable regular files under `/etc` | Some environments may have legitimate executable configuration helpers |
| `privileged_binaries` | setuid or setgid binaries in scanned executable roots | Compare with distribution and local policy baselines |
| `file_capabilities` | `getcap` output in scanned roots | Empty can mean no capabilities or unavailable/incomplete collection |
| `package_integrity_findings` | non-empty package-verifier lines | Output semantics vary by package manager |
| `recent_etc_changes_30d` | regular files under `/etc` modified within 30 days | Timestamps are mutable and not proof of who changed a file |

All metric values are non-negative integers. Dashboard thresholds are prioritization policy and are not part of the evidence semantics.

## Example

```json
{
  "schema_version": "1.0",
  "generated_at": "2026-07-23T12:00:00Z",
  "host": "synthetic-host",
  "root_complete": true,
  "metrics": {
    "world_writable_etc": 0,
    "executable_files_etc": 3,
    "privileged_binaries": 21,
    "file_capabilities": 4,
    "package_integrity_findings": 0,
    "recent_etc_changes_30d": 18
  },
  "artifacts": [
    "etc-metadata.txt",
    "etc-sha256.txt",
    "etc-world-writable.txt",
    "etc-executable-files.txt",
    "privileged-binaries.txt",
    "file-capabilities.txt",
    "admin-access.txt",
    "persistence-and-loader.txt",
    "package-integrity.txt"
  ],
  "notice": "Indicators require human review and are not proof of malicious activity."
}
```

The example is synthetic and must not be replaced with data from a real host.

## Compatibility rules

- Consumers must reject unsupported `schema_version` values rather than guessing.
- New optional fields may be introduced only when old consumers can safely ignore them.
- Renaming, removing, changing the type, or changing the meaning of an existing field requires a new schema version.
- A new schema version must document migration, coexistence, rollback, and dashboard rejection behavior.
- Schema success does not establish collection completeness, evidence authenticity, chain of custody, or forensic correctness.

## Security rules

Treat every string and number as untrusted input. Browser code must avoid injecting report values as HTML. Reports should remain local, access-controlled, and excluded from public Git and CI artifacts.

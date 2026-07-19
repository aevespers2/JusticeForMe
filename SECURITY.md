# Security and Evidence Handling

## Authorized use

Use JusticeForMe only on systems you own or are explicitly authorized to inspect. The project is intended for defensive administration, internal security review, incident response, compliance validation, and forensic preservation.

Do not use the collector to bypass access controls, inspect third-party systems without permission, or publish sensitive host data.

## Security posture

JusticeForMe currently consists of:

- a local Bash collector;
- a local evidence directory;
- a static browser dashboard; and
- a GitHub Pages deployment workflow for the dashboard and documentation.

There is no remote agent, backend API, account system, report upload endpoint, telemetry service, or automated remediation mechanism.

## Collector privileges

Running with `sudo` improves visibility into protected paths. It also means the collector executes with elevated privileges. Before use:

1. inspect the script from the exact commit you intend to run;
2. verify the repository and commit source;
3. select a protected output destination with adequate free space;
4. avoid running from an untrusted writable directory; and
5. preserve the exact script and commit identifier with the evidence record.

A non-root run is supported but can be incomplete. The report records this as `root_complete: false`.

## Sensitive data

Generated artifacts may disclose:

- hostnames;
- usernames and administrative group membership;
- ownership and permission relationships;
- local unit and cron paths;
- package-integrity deviations;
- configuration file names and timestamps;
- privileged executable locations; and
- evidence of local administrative practices.

Treat the entire output directory as confidential security material. Do not attach it to public GitHub issues, commit it to the repository, publish it through Pages, or paste it into public chat systems.

## Evidence preservation

Recommended handling:

1. collect to a new directory;
2. record operator, authorization, host, time source, command, script commit, and destination;
3. preserve the original directory as read-only evidence;
4. verify `REPORT-SHA256SUMS.txt` from a trusted environment;
5. analyze a copy rather than the original; and
6. document every transfer or transformation.

The generated checksum manifest is not a signature and does not replace formal chain-of-custody controls.

## Live-system limitations

The collector reads a running host. Results can be affected by concurrent changes, mount namespaces, containers, chroots, permission errors, rootkits, compromised userland tools, time manipulation, or an attacker altering files during collection.

For high-assurance investigations, combine this project with approved forensic acquisition methods, trusted external tooling, memory capture where appropriate, and professional incident-response procedures.

## Browser dashboard threat model

The dashboard parses a user-selected JSON file locally. It writes report values into text nodes for the current schema, reducing HTML-injection exposure. It does not verify the checksum manifest or authenticate report origin.

Use the dashboard on a trusted workstation. Browser extensions, compromised local software, screenshots, clipboard history, and other local processes can still expose report content.

## Pages publication boundary

The Pages workflow publishes the repository's `docs/` directory. Generated reports must never be placed there. Documentation contributors should inspect changes for accidental evidence, credentials, hostnames, personal data, and environment-specific paths before merge.

## Dependency and supply-chain considerations

The collector relies on the host's Bash, Python 3, and standard command-line utilities. Package-verification results are only as trustworthy as the invoked package database and binaries. The dashboard relies on the user's browser and contains no third-party runtime library in the current implementation.

GitHub Actions are referenced by tagged major versions in the Pages workflow. Release review should record the exact resolved workflow revisions or otherwise establish an approved supply-chain policy before making strong reproducibility claims.

## Reporting a vulnerability

Use the repository's private security-advisory mechanism when available. Do not include real host reports, credentials, personal data, or exploit-ready details in a public issue. If private reporting is unavailable, open a minimal public issue requesting a secure contact path without disclosing the vulnerability.

## Security non-goals

The project does not currently claim to provide:

- malware detection or attribution;
- tamper-proof acquisition;
- cryptographic signing;
- trusted timestamping;
- endpoint containment;
- secrets discovery;
- comprehensive persistence detection;
- fleet monitoring; or
- compliance certification.
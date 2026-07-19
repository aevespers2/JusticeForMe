# Contributing to JusticeForMe

Thank you for helping improve this public-interest Linux audit project.

## Ways to contribute

- Test the collector on Linux systems you own or are authorized to inspect.
- Report false positives, missing controls, portability issues, or unclear explanations.
- Propose safer collection methods, stronger provenance, improved accessibility, or clearer dashboard semantics.
- Fork the repository and create specialized versions while preserving attribution and safety notices.

## Testing reports

Never attach secrets, credentials, private keys, full `/etc` archives, personal data, or live investigative evidence to a public issue. Share only minimized, redacted examples that are safe for public disclosure.

When reporting a result, include:

1. Distribution and version.
2. Whether the collector ran with `sudo`.
3. The relevant metric or artifact name.
4. The expected behavior and observed behavior.
5. A redacted reproduction case when possible.

## Pull requests

- Create a focused branch.
- Keep collection read-only by default.
- Do not add telemetry, automatic uploads, remote command execution, credential collection, or exploit automation.
- Explain the security purpose and validation performed.
- Update documentation and the report schema when behavior changes.

## Contact

For collaboration inquiries, contact Jacob at Jacob@vespersinc.com.

JusticeForMe is independent and is not affiliated with organizations linked from its resource directory unless an affiliation is expressly documented.

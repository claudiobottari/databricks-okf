---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4e57f4effd545035ae3dfb746ca59678c2038bfab056a2978c87617a713eaa64
  pageDirectory: concepts
  sources:
    - migrate-to-databricks-connect-for-python-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-version-pinning-with-dot-asterisk-notation
    - DCVPWDN
  citations:
    - file: migrate-to-databricks-connect-for-python-databricks-on-aws.md
title: Databricks Connect Version Pinning with Dot-Asterisk Notation
description: The recommended practice of specifying databricks-connect versions using X.Y.* notation to ensure the latest patch version is installed.
tags:
  - databricks
  - python
  - package-management
  - best-practice
timestamp: "2026-06-19T19:34:29.316Z"
---

##Databricks Connect Version Pinning with Dot-Asterisk Notation

**Databricks Connect Version Pinning with Dot-Asterisk Notation** is a recommended practice when installing the Databricks Connect client for Python. Instead of specifying an exact version (e.g., `databricks-connect==14.0`), you specify a version range using the dot-asterisk pattern `X.Y.*` (e.g., `databricks-connect==14.0.*`). This allows the package manager to install the most recent patch release within that major.minor series while still pinning to a specific Databricks Runtime version. ^[migrate-to-databricks-connect-for-python-databricks-on-aws.md]

## Rationale

When upgrading your existing Python project to Databricks Connect for Databricks Runtime 13.3 LTS and above, the migration instructions include a step to install the new Databricks Connect client. Databricks recommends appending `.*` to the version specifier to make sure that the latest supported features and bug fixes for that runtime version are automatically obtained. While this notation is not a requirement, using `X.Y.*` helps you stay up-to-date with the most recent package improvements without accidentally jumping to a different runtime major.minor version. ^[migrate-to-databricks-connect-for-python-databricks-on-aws.md]

## Example

The following command installs Databricks Connect for runtime version 14.0, with the dot-asterisk notation:

```bash
pip3 install --upgrade "databricks-connect==14.0.*"
```

Adjust `X.Y` to match your cluster’s Databricks Runtime version (e.g., `13.3.*`, `14.1.*`). The exact version pattern is `X.Y.*`, where `X` is the major version and `Y` is the minor version. ^[migrate-to-databricks-connect-for-python-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The tool that enables connecting IDEs, notebook servers, and custom applications to Databricks clusters.
- Databricks Runtime Versions — The runtime version determines which `databricks-connect` package version you should target.
- [Python Virtual Environment](/concepts/python-virtual-environment-for-databricks-connect.md) — The recommended environment in which to install Databricks Connect.
- [Installation Requirements for Databricks Connect](/concepts/databricks-connect-setup-and-requirements.md) — Prerequisites such as matching Python versions.

## Sources

- migrate-to-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [migrate-to-databricks-connect-for-python-databricks-on-aws.md](/references/migrate-to-databricks-connect-for-python-databricks-on-aws-5b63ea6f.md)

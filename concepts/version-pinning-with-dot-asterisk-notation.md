---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6e3092a25cce34e2971d0430dc100e9d048b85c49844d05da1ddba1c6e7b706d
  pageDirectory: concepts
  sources:
    - install-databricks-connect-for-python-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - version-pinning-with-dot-asterisk-notation
    - VPWDN
  citations:
    - file: install-databricks-connect-for-python-databricks-on-aws.md
title: Version Pinning with Dot-Asterisk Notation
description: Databricks recommends using 'X.Y.*' (pip) to pin the major.minor version while allowing the latest patch version of databricks-connect to be installed.
tags:
  - versioning
  - pip
  - databricks
timestamp: "2026-06-19T19:10:03.010Z"
---

# Version Pinning with Dot-Asterisk Notation

**Version Pinning with Dot-Asterisk Notation** is a package installation strategy for `databricks-connect` that uses the `==X.Y.*` syntax (e.g., `databricks-connect==17.3.*`) to specify a major-minor version while allowing the latest patch release within that version range to be installed. ^[install-databricks-connect-for-python-databricks-on-aws.md]

## Overview

When installing the [Databricks Connect](/concepts/databricks-connect.md) client for Python, Databricks recommends using dot-asterisk notation instead of exact version pinning (e.g., `==17.3`). The dot-asterisk pattern `==X.Y.*` ensures that the most recent patch release for the specified major.minor version is installed, rather than a specific patch version. ^[install-databricks-connect-for-python-databricks-on-aws.md]

## Usage

### With pip and venv

When using `pip` with a venv virtual environment, run the following command, replacing `17.3` with your cluster's Databricks Runtime version: ^[install-databricks-connect-for-python-databricks-on-aws.md]

```bash
pip3 install --upgrade "databricks-connect==17.3.*"
```

The `--upgrade` option upgrades any existing client installation to the specified version. The quotation marks are required to prevent shell expansion of the asterisk. ^[install-databricks-connect-for-python-databricks-on-aws.md]

### Corresponding Poetry Notation

The equivalent in Poetry uses the at-tilde notation (`@~X.Y`) rather than dot-asterisk: ^[install-databricks-connect-for-python-databricks-on-aws.md]

```bash
poetry add databricks-connect@~17.3
```

## Benefits

While not a strict requirement, using dot-asterisk notation helps ensure that users can access the latest supported features for their cluster version. If an exact version is pinned (e.g., `databricks-connect==17.3`), the installation will not automatically receive patch updates that may include bug fixes, security patches, or new features compatible with that major.minor release. ^[install-databricks-connect-for-python-databricks-on-aws.md]

## Pre-installation Requirements

Before installing, PySpark must be uninstalled if present, as the `databricks-connect` package conflicts with PySpark installations. Use `pip3 show pyspark` to check for PySpark, and `pip3 uninstall pyspark` to remove it. ^[install-databricks-connect-for-python-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The client library for connecting local development environments to Databricks clusters
- Version Pinning — General strategies for specifying package versions
- [Databricks Runtime Versioning](/concepts/databricks-runtime-version-compatibility.md) — How Databricks Runtime versions map to Connect client versions
- Python Virtual Environments — Recommended isolation for Databricks Connect installations
- Conflicting PySpark Installations — Troubleshooting guidance for version conflicts

## Sources

- install-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [install-databricks-connect-for-python-databricks-on-aws.md](/references/install-databricks-connect-for-python-databricks-on-aws-fe510d11.md)

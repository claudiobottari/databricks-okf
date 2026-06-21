---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0312c9083c07277b6822597664339ec5a8e460738ec36b896fa271ea8f86e09d
  pageDirectory: concepts
  sources:
    - install-databricks-connect-for-python-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - poetry-tilde-notation-for-databricks-connect
    - PTNFDC
  citations:
    - file: install-databricks-connect-for-python-databricks-on-aws.md
title: Poetry Tilde Notation for Databricks Connect
description: When using Poetry, the '~X.Y' (tilde) notation is recommended to pin the major.minor version while allowing the latest patch of databricks-connect.
tags:
  - versioning
  - poetry
  - databricks
timestamp: "2026-06-19T19:10:06.686Z"
---

# Poetry Tilde Notation for Databricks Connect

The **Poetry Tilde Notation for Databricks Connect** refers to the recommended syntax for specifying the `databricks-connect` package version when installing it via Poetry. The notation uses a tilde (`~`) followed by a version specifier to ensure compatibility with a specific Databricks Runtime version while allowing the installation of the most recent compatible package release.

## Overview

When installing the Databricks Connect client using Poetry, the recommended approach is to use the "at-tilde" notation (`@~`) rather than an exact version pin (`==`). This notation ensures that you install the most recent version of Databricks Connect that is compatible with your target Databricks Runtime cluster while still maintaining the correct version constraints. ^[install-databricks-connect-for-python-databricks-on-aws.md]

## Syntax

The standard command uses the following syntax:

```bash
poetry add databricks-connect@~X.Y
```

Where `X.Y` represents your Databricks Runtime version. For example, to install Databricks Connect for Databricks Runtime 13.3and above:

```bash
poetry add databricks-connect@~13.3
```

Or for Runtime 17.3:

```bash
poetry add databricks-connect@~17.3
```

^[install-databricks-connect-for-python-databricks-on-aws.md]

## Comparison with Other Installation Methods

The Poetry tilde notation is analogous to the "dot-asterisk" notation (`==X.Y.*`) used when installing with `pip3`:

| Package Manager | Recommended Syntax | Example |
|-----------------|-------------------|---------|
| Poetry | `@~X.Y` | `poetry add databricks-connect@~17.3` |
| pip3 | `==X.Y.*` | `pip3 install "databricks-connect==17.3.*"` |

Both notations serve the same purpose: they allow installation of the latest compatible patch version while ensuring the major and minor versions match your cluster. ^[install-databricks-connect-for-python-databricks-on-aws.md]

## Why Not Use Exact Pinning

Using exact version pinning such as `databricks-connect==13.3` is not recommended because it may result in installing an older package version that lacks the latest supported features for that cluster release. The tilde notation ensures you automatically receive the most up-to-date package within the specified version range. ^[install-databricks-connect-for-python-databricks-on-aws.md]

## Prerequisites

Before running the `poetry add` command, you must:

1. **Activate a Python virtual environment** — Poetry manages environments automatically, but Databricks recommends having a virtual environment activated.
2. **Remove PySpark if installed** — The `databricks-connect` package conflicts with PySpark. First check if PySpark is installed using `poetry show pyspark`, then remove it with `poetry remove pyspark` if necessary.

^[install-databricks-connect-for-python-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The client library for connecting local development environments to Databricks clusters.
- Poetry Dependency Management — Python dependency management tool used with Databricks Connect.
- venv Virtual Environment — Alternative to Poetry for managing Python environments.
- [Databricks Runtime Version Compatibility](/concepts/databricks-runtime-version-compatibility.md) — Ensuring correct version matching between client and cluster.
- Conflicting PySpark Installations — A common issue when installing Databricks Connect.

## Sources

- install-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [install-databricks-connect-for-python-databricks-on-aws.md](/references/install-databricks-connect-for-python-databricks-on-aws-fe510d11.md)

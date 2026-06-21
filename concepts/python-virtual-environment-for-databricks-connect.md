---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c0f40793e6266489280b5a681f0dbb9831e35b3393600a915cf4e3034b1bc6f3
  pageDirectory: concepts
  sources:
    - install-databricks-connect-for-python-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - python-virtual-environment-for-databricks-connect
    - PVEFDC
    - Python Virtual Environment
    - Python virtual environments
  citations:
    - file: install-databricks-connect-for-python-databricks-on-aws.md
title: Python Virtual Environment for Databricks Connect
description: Databricks strongly recommends using a Python virtual environment (venv or Poetry) to isolate the correct versions of Python and Databricks Connect.
tags:
  - python
  - virtual-environments
  - databricks
timestamp: "2026-06-19T19:09:48.391Z"
---

# Python Virtual Environment for Databricks Connect

A **Python virtual environment for Databricks Connect** is an isolated Python environment that Databricks strongly recommends using when developing with Databricks Connect on a local machine. Virtual environments ensure that the correct versions of Python and the `databricks-connect` package are used together, avoiding version conflicts with other Python packages such as PySpark. ^[install-databricks-connect-for-python-databricks-on-aws.md]

## Why Use a Virtual Environment

Databricks Connect requires the `databricks-connect` package, which **conflicts with PySpark**. If PySpark is already installed in the same environment, the two packages cannot coexist. A virtual environment isolates `databricks-connect` and its dependencies, allowing you to manage separate environments for different clusters or Python versions without interfering with system‑wide or other project packages. ^[install-databricks-connect-for-python-databricks-on-aws.md]

Using a dedicated virtual environment helps guarantee that:

- The correct Python version for the cluster runtime is used.
- The `databricks-connect` version matches the target Databricks Runtime (e.g., 13.3 LTS and above).
- No pre‑existing PySpark installation conflicts with the client library.

## Recommended Tools

Databricks recommends two tools for creating and managing virtual environments:

- **[venv]** – A built‑in Python module (`python -m venv`) that creates lightweight virtual environments.
- **[Poetry]** – A dependency management and packaging tool that handles virtual environments and version pinning.

Both tools can be used to activate an environment before installing `databricks-connect`. ^[install-databricks-connect-for-python-databricks-on-aws.md]

## Installation Steps

The following steps assume a virtual environment is already activated.

### Using venv

1. **Uninstall PySpark** if it is present in the environment (check with `pip3 show pyspark`):
   ```bash
   pip3 uninstall pyspark
   ```
2. **Install the Databricks Connect client**:
   ```bash
   pip3 install --upgrade "databricks-connect==17.3.*"
   ```
   Databricks recommends using the `X.Y.*` notation (e.g., `17.3.*`) instead of a fixed version like `17.3` to ensure the latest supported patch release is installed. ^[install-databricks-connect-for-python-databricks-on-aws.md]

### Using Poetry

1. **Remove PySpark** if it is present (check with `poetry show pyspark`):
   ```bash
   poetry remove pyspark
   ```
2. **Add the Databricks Connect client**:
   ```bash
   poetry add databricks-connect@~17.3
   ```
   Use the `~X.Y` (tilde) notation to allow compatible version updates while staying within the same minor version. ^[install-databricks-connect-for-python-databricks-on-aws.md]

### Version Matching

The installed `databricks-connect` version must correspond to the Databricks Runtime version of the target cluster. For example, `17.3.*` or `~17.3` matches Databricks Runtime 13.3 LTS and above. Always confirm the runtime version of your cluster before installation. ^[install-databricks-connect-for-python-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The client‑server framework that links local IDEs to Databricks clusters.
- venv – Python’s built‑in virtual environment tool.
- Poetry – Dependency management tool that can create and manage virtual environments.
- PySpark – The Python API for Apache Spark; must be uninstalled before installing `databricks-connect`.
- Databricks Runtime – The versioned environment running on Databricks clusters; the `databricks-connect` client version must match it.

## Sources

- install-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [install-databricks-connect-for-python-databricks-on-aws.md](/references/install-databricks-connect-for-python-databricks-on-aws-fe510d11.md)

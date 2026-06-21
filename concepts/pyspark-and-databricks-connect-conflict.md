---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3202f0986c1c1d1c1154fda77278a052b999f8b84429115fa4ed8e09807c3d59
  pageDirectory: concepts
  sources:
    - install-databricks-connect-for-python-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pyspark-and-databricks-connect-conflict
    - Databricks Connect Conflict and PySpark
    - PADCC
    - PySpark and Databricks Connect conflicts
    - PySpark vs Databricks Connect
  citations:
    - file: install-databricks-connect-for-python-databricks-on-aws.md
title: PySpark and Databricks Connect Conflict
description: The databricks-connect package conflicts with PySpark, requiring PySpark to be uninstalled before installing Databricks Connect.
tags:
  - pyspark
  - databricks
  - compatibility
timestamp: "2026-06-19T19:09:58.238Z"
---

# PySpark and Databricks Connect Conflict

The **PySpark and Databricks Connect Conflict** refers to a known package incompatibility where the `databricks-connect` package and the `pyspark` package cannot be installed in the same Python environment simultaneously. This conflict requires users to uninstall PySpark before installing Databricks Connect, and vice versa when switching between local PySpark development and Databricks Connect workflows. ^[install-databricks-connect-for-python-databricks-on-aws.md]

## Cause

The `databricks-connect` package and the `pyspark` package have conflicting dependencies and cannot coexist in the same Python virtual environment. Attempting to install both will result in installation errors or unpredictable runtime behavior. ^[install-databricks-connect-for-python-databricks-on-aws.md]

## Resolution

### When Installing Databricks Connect

Before installing the Databricks Connect client, you must first uninstall PySpark if it is already present in your environment. This is enforced regardless of the package manager being used. ^[install-databricks-connect-for-python-databricks-on-aws.md]

**Using venv:**

1. Check if PySpark is already installed:
   ```bash
   pip3 show pyspark
   ```

2. Uninstall PySpark:
   ```bash
   pip3 uninstall pyspark
   ```

3. Install Databricks Connect:
   ```bash
   pip3 install --upgrade "databricks-connect==17.3.*"
   ```

^[install-databricks-connect-for-python-databricks-on-aws.md]

**Using Poetry:**

1. Check if PySpark is already installed:
   ```bash
   poetry show pyspark
   ```

2. Uninstall PySpark:
   ```bash
   poetry remove pyspark
   ```

3. Install Databricks Connect:
   ```bash
   poetry add databricks-connect@~17.3
   ```

^[install-databricks-connect-for-python-databricks-on-aws.md]

### When Switching Back to PySpark

If you need to use PySpark instead of Databricks Connect, you must uninstall Databricks Connect first and then install PySpark. The same mutual exclusivity applies in both directions.

## Best Practices

- Use [Python virtual environments](/concepts/python-virtual-environment-for-databricks-connect.md) to isolate Databricks Connect and PySpark installations. Databricks strongly recommends activating a separate virtual environment for each tool. ^[install-databricks-connect-for-python-databricks-on-aws.md]
- Maintain separate virtual environments for Databricks Connect development and local PySpark development to avoid repeated uninstall/reinstall cycles.

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The client library that connects local development environments to Databricks clusters.
- PySpark — The Python API for Apache Spark.
- venv — Python's built-in virtual environment tool.
- Poetry — A dependency management tool for Python.
- [Databricks Connect Troubleshooting](/concepts/databricks-connect-troubleshooting.md) — Guide for resolving common Databricks Connect issues, including conflicting PySpark installations.

## Sources

- install-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [install-databricks-connect-for-python-databricks-on-aws.md](/references/install-databricks-connect-for-python-databricks-on-aws-fe510d11.md)

---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e8c3d2bf3f278c24ec8215f6ec72ddd1b425b9f826ba8c2a0417f6335d1fb2d1
  pageDirectory: concepts
  sources:
    - databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - python-environment-compatibility-for-databricks-connect
    - PECFDC
  citations:
    - file: databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md
title: Python Environment Compatibility for Databricks Connect
description: The requirement that the minor version of Python on the development machine must match the minor Python version of the Databricks cluster, with recommended use of virtual environments.
tags:
  - python
  - compatibility
  - environments
timestamp: "2026-06-19T18:09:02.036Z"
---

# Python Environment Compatibility for Databricks Connect

**Python Environment Compatibility for Databricks Connect** refers to the requirements and constraints for the Python version used on the local development machine when connecting to a Databricks cluster via Databricks Connect. Proper version matching between the client and cluster is essential for successful connectivity and operation.

## Python Version Requirements

The minor version of the Python installation on the development machine must match the minor Python version installed on the Databricks cluster. For example, Python 3.9 on the client requires Python 3.9 on the cluster. Minor differences in patch versions (e.g., 3.9.15 versus 3.9.16) are acceptable. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

The following table shows the Python version installed with each supported Databricks Runtime version:

| Databricks Runtime | Available Python Versions |
|-------------------|--------------------------|
| 12.2 LTS, 12.2 LTS ML | Python 3.9 |
| 11.3 LTS, 11.3 LTS ML | Python 3.9 |
| 10.4 LTS, 10.4 LTS ML | Python 3.9 |
| 9.1 LTS, 9.1 LTS ML | Python 3.8 |
| 7.3 LTS | Python 3.7 |

Databricks strongly recommends using a Python **virtual environment** for each Python version used with Databricks Connect. Virtual environments help ensure the correct versions of Python and Databricks Connect are used together, reducing time spent resolving compatibility issues. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Setting Up a Compatible Python Environment

### Using venv

If using `venv` on a development machine and the cluster runs Python 3.9, create a `venv` environment with Python 3.9:

```bash
# Linux and macOS
python3.9 -m venv ./.venv
# Windows
python3.9 -m venv .\.venv
```

### Using Conda

If using Conda and the cluster runs Python 3.9, create a Conda environment with that version:

```bash
conda create --name dbconnect python=3.9
conda activate dbconnect
```

^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Verifying and Troubleshooting Python Version Mismatch

If you have multiple Python versions installed locally, ensure Databricks Connect uses the correct one by setting the `PYSPARK_PYTHON` environment variable:

```bash
export PYSPARK_PYTHON=python3
```

^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

Check the Python version used locally has at least the same minor release as the version on the cluster. For example, local `3.9.16` versus cluster `3.9.15` is acceptable, but `3.9` versus `3.8` is not. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — Overview and setup of the client library
- Python Virtual Environments — Best practices for managing Python dependencies
- Databricks Runtime Versions — Matrix of supported runtime versions and Python compatibility
- Cluster Configuration Best Practices — Guidelines for configuring Databricks clusters

## Sources

- databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md

# Citations

1. [databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md](/references/databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws-4be394af.md)

---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 34a7743e7d65de60d89317cb6d67492c43b69f8603f92719d482b5d4d602cc06
  pageDirectory: concepts
  sources:
    - troubleshooting-databricks-connect-for-python-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - python-version-compatibility-in-databricks-connect
    - PVCIDC
  citations:
    - file: troubleshooting-databricks-connect-for-python-databricks-on-aws.md
title: Python Version Compatibility in Databricks Connect
description: Databricks Connect requires the local Python version to match at least the same minor release as the cluster's Python version, configurable via the PYSPARK_PYTHON environment variable.
tags:
  - databricks-connect
  - python
  - troubleshooting
  - versioning
timestamp: "2026-06-19T23:14:34.459Z"
---

# Python Version Compatibility in [Databricks Connect](/concepts/databricks-connect.md)

**Python Version Compatibility in Databricks Connect** refers to the requirement that the Python version used locally for [Databricks Connect](/concepts/databricks-connect.md) must be compatible with the Python version running on the connected Databricks cluster. This is a critical configuration consideration when using [Databricks Connect](/concepts/databricks-connect.md) for Python development with Databricks Runtime 13.3 LTS and above.

## Version Requirements

The local Python version must have at least the same minor release as the Python version on the cluster. For example, Python 3.10.11 locally is compatible with Python 3.10.10 on the cluster, but Python 3.10 is **not** compatible with Python 3.9. For the full list of supported versions, consult the version support matrix. ^[troubleshooting-databricks-connect-for-python-databricks-on-aws.md]

## Checking and Setting the Correct Version

If you have multiple Python versions installed locally, ensure that [Databricks Connect](/concepts/databricks-connect.md) uses the correct one by setting the `PYSPARK_PYTHON` environment variable. For example: ^[troubleshooting-databricks-connect-for-python-databricks-on-aws.md]

```bash
PYSPARK_PYTHON=python3
```

## Common Symptoms of Mismatch

When a Python version mismatch occurs, you may encounter errors containing strings such as: ^[troubleshooting-databricks-connect-for-python-databricks-on-aws.md]

- `StatusCode.UNAVAILABLE`
- `StatusCode.UNKNOWN`
- `DNS resolution failed`
- `Received http2 header with status: 500`

These errors indicate that [Databricks Connect](/concepts/databricks-connect.md) cannot reach your cluster, often due to version incompatibility.

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The framework for connecting IDEs and applications to Databricks clusters
- Databricks Runtime — The runtime environment on Databricks clusters
- [PySpark Compatibility](/concepts/apache-spark-compatibility.md) — Understanding potential conflicts between PySpark and [Databricks Connect](/concepts/databricks-connect.md)
- [Environment Variables for Databricks Connect](/concepts/environment-variable-configuration-for-databricks-connect.md) — Configuration settings including `PYSPARK_PYTHON`

## Sources

- troubleshooting-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [troubleshooting-databricks-connect-for-python-databricks-on-aws.md](/references/troubleshooting-databricks-connect-for-python-databricks-on-aws-bb4d5efd.md)

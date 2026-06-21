---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fd508a7b632d5614f60806b352184dd83cc93d99d9a3c097a0d81d5d8e836ee5
  pageDirectory: concepts
  sources:
    - troubleshooting-databricks-connect-for-python-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - cluster-connectivity-troubleshooting-for-databricks-connect
    - CCTFDC
  citations:
    - file: troubleshooting-databricks-connect-for-python-databricks-on-aws.md
title: Cluster Connectivity Troubleshooting for Databricks Connect
description: Common connectivity failures when Databricks Connect cannot reach a cluster, indicated by errors like StatusCode.UNAVAILABLE, DNS resolution failure, or HTTP 500 status codes.
tags:
  - databricks-connect
  - troubleshooting
  - networking
timestamp: "2026-06-19T23:14:28.850Z"
---

# Cluster Connectivity Troubleshooting for [Databricks Connect](/concepts/databricks-connect.md)

This page provides common cluster connectivity issues and their solutions when using **Databricks Connect** for Python. [Databricks Connect](/concepts/databricks-connect.md) allows you to connect popular IDEs, notebook servers, and custom applications to Databricks clusters. For the Scala version, see [Troubleshooting Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md). ^[troubleshooting-databricks-connect-for-python-databricks-on-aws.md]

## General Connectivity Errors

**Error indicators**: Messages containing `StatusCode.UNAVAILABLE`, `StatusCode.UNKNOWN`, `DNS resolution failed`, or `Received http2 header with status: 500`.

**Possible cause**: [Databricks Connect](/concepts/databricks-connect.md) cannot reach your cluster.

**Recommended solutions**:

- Verify that your **workspace instance name** is correct. If using environment variables, confirm the variable is set correctly on your local development machine.
- Verify that your **cluster ID** is correct and the environment variable is accurate.
- Ensure your cluster uses a Databricks Runtime version compatible with [Databricks Connect](/concepts/databricks-connect.md). ^[troubleshooting-databricks-connect-for-python-databricks-on-aws.md]

## Python Version Mismatch

The Python version on your local machine must have at least the same **minor release** as the Python version on the cluster (for example, `3.10.11` vs `3.10.10` is acceptable; `3.10` vs `3.9` is not). See the version support matrix in [Databricks Connect for Python requirements](/concepts/databricks-connect-requirements.md). ^[troubleshooting-databricks-connect-for-python-databricks-on-aws.md]

If you have multiple Python versions installed, ensure [Databricks Connect](/concepts/databricks-connect.md) uses the correct one by setting the `PYSPARK_PYTHON` environment variable (e.g., `PYSPARK_PYTHON=python3`). ^[troubleshooting-databricks-connect-for-python-databricks-on-aws.md]

## Conflicting PySpark Installations

The `databricks-connect` package conflicts with `pyspark`. Having both installed can cause “stream corrupted” or “class not found” errors when initializing the Spark context. ^[troubleshooting-databricks-connect-for-python-databricks-on-aws.md]

**Fix**: Uninstall PySpark and then re-install the [Databricks Connect](/concepts/databricks-connect.md) package:

```bash
pip3 uninstall pyspark
pip3 uninstall databricks-connect
pip3 install --upgrade "databricks-connect==14.0.*"  # or X.Y.* matching your cluster version
```

[Databricks Connect](/concepts/databricks-connect.md) and PySpark are mutually exclusive. While you can use Python virtual environments to keep them separate (e.g., `databricks-connect` in an IDE, `pyspark` in a terminal), Databricks recommends using [Databricks Connect](/concepts/databricks-connect.md) with [serverless compute](/concepts/serverless-gpu-compute.md) for all testing because:

- Databricks Runtime includes features unavailable in open-source `pyspark`.
- Testing with [Databricks Connect](/concepts/databricks-connect.md) and serverless is faster.
- [Unity Catalog](/concepts/unity-catalog.md) integrations are not available in `pyspark`, so permissions are not enforced locally.
- End-to-end integration tests are preferable to local unit tests for external dependencies. ^[troubleshooting-databricks-connect-for-python-databricks-on-aws.md]

If you still need to connect to a local Spark cluster, use a connection string:

```python
connection_string = "sc://localhost"
[[databrickssession|DatabricksSession]].builder.remote(connection_string).getOrCreate()
``` ^[troubleshooting-databricks-connect-for-python-databricks-on-aws.md]

## Errors Connecting to an Open-Source Apache Spark Server

[Databricks Connect](/concepts/databricks-connect.md) is built against Databricks Runtime, which has different dependencies than open-source Apache Spark. Attempting to connect to an open-source [Spark Connect](/concepts/spark-connect.md) server (e.g., a local Apache Spark 3.5.x instance at `sc://localhost`) can cause class not found errors, API mismatches, or serialization failures. In particular, [Databricks Connect](/concepts/databricks-connect.md) 15.4 and 16.4 are incompatible with Apache Spark 3.5.x because they use a different version of the `json4s` library. ^[troubleshooting-databricks-connect-for-python-databricks-on-aws.md]

**Solution**: Always use a Databricks cluster or serverless compute instead of an open-source Spark server. See [Compute configuration for Databricks Connect](/concepts/compute-configuration-for-databricks-connect.md). ^[troubleshooting-databricks-connect-for-python-databricks-on-aws.md]

## Conflicting or Missing `PATH` Entry for Binaries

Commands like `spark-shell` may inadvertently run a previously installed binary instead of the one provided by [Databricks Connect](/concepts/databricks-connect.md). Ensure that the [Databricks Connect](/concepts/databricks-connect.md) binaries take precedence in your `PATH`, or remove conflicting installations. ^[troubleshooting-databricks-connect-for-python-databricks-on-aws.md]

If commands like `spark-shell` cannot be found, the `pip3 install` might not have added the installation `bin` directory to your `PATH` automatically. Add it manually. IDEs can still work without this PATH setup. ^[troubleshooting-databricks-connect-for-python-databricks-on-aws.md]

## Windows Path Issue (Spaces in Directory Name)

On Windows, if you see:

```
The filename, directory name, or volume label syntax is incorrect.
```

This occurs when [Databricks Connect](/concepts/databricks-connect.md) is installed into a directory whose path contains a space (e.g., `C:\Program Files`). Two workarounds:

- Install into a directory path without spaces.
- Configure your `PATH` using the short‑name form (e.g., `C:\PROGRA~1`). ^[troubleshooting-databricks-connect-for-python-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md)
- Databricks Runtime
- [Serverless compute](/concepts/serverless-gpu-compute.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Compute configuration for Databricks Connect](/concepts/compute-configuration-for-databricks-connect.md)
- [Databricks Connect for Python requirements](/concepts/databricks-connect-requirements.md)
- [Troubleshooting Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md)

## Sources

- troubleshooting-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [troubleshooting-databricks-connect-for-python-databricks-on-aws.md](/references/troubleshooting-databricks-connect-for-python-databricks-on-aws-bb4d5efd.md)

---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 47cca5d1394beae25c8229cecf62e43d47fa257ac0787d90101fa8d47a0c3d67
  pageDirectory: concepts
  sources:
    - databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-troubleshooting
    - DCT
    - Databricks Connect for Python troubleshooting
  citations:
    - file: databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md
title: Databricks Connect Troubleshooting
description: Common issues encountered when using Databricks Connect such as Python version mismatches, conflicting PySpark installations, SPARK_HOME conflicts, serialization settings, and Windows-specific problems.
tags:
  - troubleshooting
  - errors
  - debugging
timestamp: "2026-06-19T18:09:12.726Z"
---

# Databricks Connect Troubleshooting

This page describes common issues encountered when using [Databricks Connect](/concepts/databricks-connect.md) (legacy, for Databricks Runtime 12.2 LTS and below) and how to resolve them. Run `databricks-connect test` to check for connectivity issues. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Python Version Mismatch

The minor Python version on your development machine must match the minor Python version on the Databricks cluster. For example, Python 3.9 locally and Python 3.8 on the cluster is not compatible. If you have multiple Python versions installed locally, set the `PYSPARK_PYTHON` environment variable (e.g., `PYSPARK_PYTHON=python3`) to ensure Databricks Connect uses the correct one. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Server Not Enabled

The cluster must have the Spark server enabled with the configuration `spark.databricks.service.server.enabled true`. Check the driver log for lines like `Set spark config:spark.databricks.service.server.enabled -> true` and `Starting Spark Service RPC Server` to confirm the server is active. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Conflicting PySpark Installations

The `databricks-connect` package conflicts with PySpark. Having both installed can cause errors such as "stream corrupted" or "class not found" when initializing the Spark context. To resolve, uninstall PySpark and re-install Databricks Connect:

```bash
pip3 uninstall pyspark
pip3 uninstall databricks-connect
pip3 install --upgrade "databricks-connect==12.2.*"
```

Replace `12.2.*` with the version matching your Databricks Runtime. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Conflicting `SPARK_HOME`

If the `SPARK_HOME` environment variable points to a Spark installation other than the one bundled with Databricks Connect, you may see "stream corrupted" or "class not found" errors. Unset `SPARK_HOME` and restart your IDE. Check your `.bashrc`, `.zshrc`, `.bash_profile`, and IDE environment variable settings. You should not need to set `SPARK_HOME` to a new value; unsetting it is sufficient. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Conflicting or Missing `PATH` Entry for Binaries

If commands like `spark-shell` run a previously installed binary instead of the one provided by Databricks Connect, `databricks-connect test` may fail. Ensure the Databricks Connect `bin` directory takes precedence in your `PATH` or remove conflicting installations. If you cannot run `spark-shell` at all, your `PATH` was not automatically set up by `pip3 install` — add the installation `bin` directory manually. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Conflicting Serialization Settings on the Cluster

If you see "stream corrupted" errors during `databricks-connect test`, incompatible cluster serialization configuration (e.g., `spark.io.compression.codec`) may be the cause. Remove or adjust these configs from the cluster settings, or set the same configuration in the Databricks Connect client. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Cannot Find `winutils.exe` on Windows

On Windows, if you see the error:

```
ERROR Shell: Failed to locate the winutils binary in the hadoop binary path
java.io.IOException: Could not locate executable null\bin\winutils.exe in the Hadoop binaries.
```

Follow the instructions to configure the Hadoop path on Windows as described in the [Hadoop Windows documentation](https://cwiki.apache.org/confluence/display/HADOOP2/Hadoop2OnWindows). ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## The Filename, Directory Name, or Volume Label Syntax Is Incorrect on Windows

If you encounter this error on Windows, either Java or Databricks Connect was installed into a directory path containing spaces. Install into a path without spaces, or use the short name form (e.g., `C:\PROGRA~1` instead of `C:\Program Files`). ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – Overview and setup
- Databricks Connect for Databricks Runtime 12.2 LTS and below – Full setup guide for legacy versions
- PySpark Environment Variables – `PYSPARK_PYTHON` and other relevant settings
- Hadoop Windows Configuration – Setting up `winutils.exe`

## Sources

- databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md

# Citations

1. [databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md](/references/databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws-4be394af.md)

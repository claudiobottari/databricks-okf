---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b5c2da4903931398b75a80edb23a9a1c3a635c294f19bf8d76fbcbf08d957d24
  pageDirectory: concepts
  sources:
    - user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - python-version-compatibility-for-udfs
    - PVCFU
  citations:
    - file: user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md
title: Python Version Compatibility for UDFs
description: The Python version on the Databricks Connect client must exactly match the Python version on the Databricks compute cluster for UDF serialization and deserialization to work correctly.
tags:
  - databricks-connect
  - udf
  - compatibility
timestamp: "2026-06-19T23:23:18.442Z"
---

# Python Version Compatibility for UDFs

**Python Version Compatibility for UDFs** refers to the requirement that the Python version on the client machine must exactly match the Python version running on the Databricks compute when using [Databricks Connect for Python](/concepts/databricks-connect-for-python.md). This constraint arises because user-defined functions (UDFs) are serialized on the client and deserialized on the server. ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

## Overview

When a DataFrame operation that includes UDFs is executed through [Databricks Connect](/concepts/databricks-connect.md), the UDFs are serialized by the client and sent to the server as part of the request. ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md] Because the serialized function must be deserialized on the server side, the Python version on the client must match the Python version on the Databricks compute. ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

## Determining Python Versions

For specific supported version combinations, see the [Databricks Connect version support matrix](/concepts/databricks-connect-version-compatibility.md). ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

### Cluster Compute

For clusters, the base Python environment is the Python environment of the Databricks Runtime version running on the cluster. The Python version and the list of packages in this base environment are found under the *System environment* and *Installed Python libraries* sections of the Databricks Runtime release notes. ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

### Serverless Compute

For serverless compute, the base Python environment corresponds to the serverless environment version. The specific Python versions are documented in the serverless environment version tables on Databricks. ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

## Automatic Dependency Management

The automatic dependency management feature (`withAutoDependencies()`) requires Python 3.12 on the local machine and a cluster running Databricks Runtime 18.1 or above. ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect for Python](/concepts/databricks-connect-for-python.md)
- User-Defined Functions (UDFs)
- Databricks Runtime Release Notes
- Serverless Environment Version
- UDF Dependencies Management

## Sources

- user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md](/references/user-defined-functions-in-databricks-connect-for-python-databricks-on-aws-d446d035.md)

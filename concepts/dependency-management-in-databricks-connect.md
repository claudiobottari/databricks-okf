---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d9d66e4a1c682ea207901d88b16f02820e8982b3db494e3f6d90763e0e13c7ea
  pageDirectory: concepts
  sources:
    - databricks-connect-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dependency-management-in-databricks-connect
    - DMIDC
    - Dependency Management in Databricks
  citations:
    - file: databricks-connect-databricks-on-aws.md
    - file: databricks-connect-databricks-on-aws.md
      start: 64
      end: 70
title: Dependency Management in Databricks Connect
description: The dual dependency model where application dependencies are installed locally while UDF dependencies must be managed separately on the Databricks cluster.
tags:
  - dependencies
  - udf
  - databricks
  - packaging
timestamp: "2026-06-19T14:45:12.705Z"
---

# Dependency Management in Databricks Connect

**Dependency Management in Databricks Connect** refers to the process of installing and managing software libraries required by code that runs in a Databricks Connect application. Because Databricks Connect uses a client-server architecture where different parts of the code execute in different environments, dependencies fall into two categories: **local dependencies** (for code that runs on the client machine) and **UDF dependencies** (for code that runs on the remote Databricks compute). ^[databricks-connect-databricks-on-aws.md]

## Overview

Databricks Connect is built on [Spark Connect](/concepts/spark-connect.md), which decouples the client from the Spark cluster. General Python and Scala code (e.g., orchestration logic, data post-processing, or calls to non-Spark libraries) runs on the local client machine. User-Defined Functions (UDFs) and similar APIs (`foreach`, `foreachBatch`, `transformWithState`) are serialized and sent to the Databricks cluster for execution. This separation means that libraries needed for local code must be installed on the client, while libraries needed for UDF execution must be available on the cluster. ^[databricks-connect-databricks-on-aws.md]

## Local Dependencies

Local dependencies are libraries that your development project requires on your local machine. They include packages used for interactive debugging, data visualisation, or any non-Spark logic that runs in the client process. These dependencies are installed as part of the project's environment, for example within a Python virtual environment. Common tools such as `pip` or `conda` are used to manage them. ^[databricks-connect-databricks-on-aws.md]

Because all general code runs locally, you can debug interactively using your IDE's native debugging features (e.g., breakpoints in Visual Studio Code or PyCharm). Libraries that are only needed locally should be added to your project's `requirements.txt` or equivalent.

## UDF Dependencies

UDF dependencies are libraries required by user-defined functions that execute on the Databricks cluster. When you define a UDF locally that imports external packages (e.g., `pandas`, `numpy`, or custom modules), those packages must also be installed on the cluster nodes. Databricks Connect does not automatically synchronise local environments with the cluster, so you must manage UDF dependencies separately. ^[databricks-connect-databricks-on-aws.md]

Databricks provides guidance on how to install UDF dependencies on the cluster. See the Manage UDF Dependencies page for detailed instructions. ^[databricks-connect-databricks-on-aws.md:64-70]

The following table summarises the two dependency categories:

| Category | Where code runs | Where dependencies must be installed | Example |
|----------|----------------|--------------------------------------|---------|
| **Local dependencies** | Client machine (local) | Local project environment (e.g., Python virtual environment) | `plotly`, `requests`, `pytest` |
| **UDF dependencies** | Databricks cluster | On the cluster (e.g., cluster libraries or init scripts) | `pandas`, `scikit-learn`, custom modules |

## Best Practices

- **Keep local and UDF dependencies separate** in your documentation and installation scripts to avoid confusion.
- **Test UDF dependencies** by running a small UDF on the cluster after installing new packages.
- **Use consistent versions** of libraries across local and cluster environments to avoid serialisation or behaviour mismatches.
- **Leverage the Databricks Visual Studio Code extension** which uses Databricks Connect and automates some dependency setup; see [Databricks VS Code Extension](/concepts/databricks-visual-studio-code-extension.md).

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md)
- [Spark Connect](/concepts/spark-connect.md)
- User-Defined Functions (UDFs)
- [Databricks Visual Studio Code Extension](/concepts/databricks-visual-studio-code-extension.md)
- Manage UDF Dependencies

## Sources

- databricks-connect-databricks-on-aws.md

# Citations

1. [databricks-connect-databricks-on-aws.md](/references/databricks-connect-databricks-on-aws-65545eb5.md)
2. [databricks-connect-databricks-on-aws.md:64-70](/references/databricks-connect-databricks-on-aws-65545eb5.md)

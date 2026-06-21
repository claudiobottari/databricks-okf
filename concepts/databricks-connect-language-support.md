---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9ad941fe4156f189d1e156729d6cfaff460b117d446da6d60c0a08f8600b7514
  pageDirectory: concepts
  sources:
    - databricks-connect-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-language-support
    - DCLS
  citations:
    - file: databricks-connect-databricks-on-aws.md
title: Databricks Connect Language Support
description: Databricks Connect is available for Python, R, and Scala, allowing developers to write code using Spark APIs in their preferred language and run it remotely on Databricks compute.
tags:
  - languages
  - python
  - scala
  - r
timestamp: "2026-06-18T15:02:43.714Z"
---

# Databricks Connect Language Support

**Databricks Connect Language Support** refers to the programming languages for which the [Databricks Connect](/concepts/databricks-connect.md) client library is available, enabling remote execution of Spark workloads on Databricks compute from local IDEs, notebooks, and custom applications.

## Overview

Databricks Connect is available for three languages: Python, R, and Scala. For each language, the library provides a thin client that communicates with a remote Databricks cluster via the open-source [Spark Connect](/concepts/spark-connect.md) protocol (gRPC-based) using unresolved logical plans and Apache Arrow. This design allows developers to write code using Spark APIs in their preferred language and execute DataFrame transformations on Databricks compute while running non-Spark logic locally. ^[databricks-connect-databricks-on-aws.md]

Databricks Connect is supported on Databricks Runtime 13.3 LTS and above across all three languages. ^[databricks-connect-databricks-on-aws.md]

## Supported Languages

### Python

The Python client for Databricks Connect is the most commonly used variant. It enables interactive development with PySpark inside IDEs like Visual Studio Code and PyCharm, as well as within custom applications. Tutorials are available for both classic compute clusters and serverless compute. ^[databricks-connect-databricks-on-aws.md]

### R

Databricks Connect for R provides a similar experience for R users, allowing them to run SparkR or sparklyr code remotely. A dedicated tutorial is available for getting started with R. ^[databricks-connect-databricks-on-aws.md]

### Scala

The Scala client supports both classic and serverless compute environments. It is particularly useful for developers building JVM-based data applications or working in IntelliJ IDEA. Tutorials cover classic compute and JAR compilation for serverless compute. ^[databricks-connect-databricks-on-aws.md]

## Language‑Agnostic Behavior

Regardless of the chosen language, Databricks Connect follows the same execution model:

- **General code** (non‑Spark logic) runs locally on the client machine, enabling native debugging. ^[databricks-connect-databricks-on-aws.md]
- **DataFrame API calls** are converted into Spark plans and executed on the remote Databricks cluster. Results are materialized locally when commands like `collect()`, `show()`, or `toPandas()` are called. ^[databricks-connect-databricks-on-aws.md]
- **User‑defined functions (UDFs)** and other user code (e.g., `foreach`, `foreachBatch`, `transformWithState`) are serialized and transmitted to the cluster for execution. ^[databricks-connect-databricks-on-aws.md]

## Dependency Management

Dependencies are managed separately for local and remote execution:

- **Application dependencies** (libraries used by client‑side code) must be installed locally, for example in a Python virtual environment or a Scala project configuration. ^[databricks-connect-databricks-on-aws.md]
- **UDF dependencies** must be installed on the Databricks cluster. See the documentation on Manage UDF dependencies for details. ^[databricks-connect-databricks-on-aws.md]

## Related Concepts

- [Spark Connect](/concepts/spark-connect.md)
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- UDFs
- [Databricks Visual Studio Code Extension](/concepts/databricks-visual-studio-code-extension.md)

## Sources

- databricks-connect-databricks-on-aws.md

# Citations

1. [databricks-connect-databricks-on-aws.md](/references/databricks-connect-databricks-on-aws-65545eb5.md)

---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c7914a89aa4fcd85d63a201a31f55449eb3c688f60d1ee9ead250dc9111aa759
  pageDirectory: concepts
  sources:
    - databricks-connect-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - language-support-for-databricks-connect
    - LSFDC
  citations:
    - file: databricks-connect-databricks-on-aws.md
title: Language Support for Databricks Connect
description: Databricks Connect is available for Python, R, and Scala, with each language having its own dedicated documentation and tutorials.
tags:
  - python
  - scala
  - r
  - multi-language
timestamp: "2026-06-19T14:45:43.556Z"
---

# Language Support for Databricks Connect

**Language Support for Databricks Connect** refers to the programming languages that the Databricks Connect client library supports for connecting to Databricks compute from IDEs, notebooks, and custom applications. Databricks Connect is built on open-source [Spark Connect](/concepts/spark-connect.md) and is available for Databricks Runtime 13.3 LTS and above. ^[databricks-connect-databricks-on-aws.md]

## Supported Languages

Databricks Connect supports three languages: Python, R, and Scala. Each language has its own dedicated library and documentation. ^[databricks-connect-databricks-on-aws.md]

### Python

The [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) library is the most commonly used variant. It provides the full expressiveness of Python through PySpark, eliminating SQL programming language impedance mismatch and enabling all data transformations with Spark on Databricks serverless scalable compute. ^[databricks-connect-databricks-on-aws.md]

### R

[Databricks Connect for R](/concepts/databricks-connect-for-r.md) provides R users with the ability to connect to Databricks compute and run Spark workloads remotely. ^[databricks-connect-databricks-on-aws.md]

### Scala

[Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) supports both classic compute and serverless compute tutorials, including JAR compilation workflows. ^[databricks-connect-databricks-on-aws.md]

## How Language Execution Works

With Databricks Connect, the execution model varies by code type: ^[databricks-connect-databricks-on-aws.md]

- **General code runs locally**: Python, R, and Scala code that is not Spark-related runs on the client side, enabling interactive debugging. All code is executed locally, while all Spark code continues to run on the remote cluster.
- **DataFrame APIs are executed on Databricks compute**: All data transformations are converted to Spark plans and run on the Databricks compute through the remote Spark session. They are materialized on your local client when you use commands such as `collect()`, `show()`, or `toPandas()`.
- **UDF code runs on Databricks compute**: User-defined functions (UDFs) defined locally are serialized and transmitted to the cluster where they execute. APIs that run user code on Databricks include User-Defined Functions (UDFs), `foreach`, `foreachBatch`, and `transformWithState`.

## Dependency Management

Language support also encompasses dependency management considerations: ^[databricks-connect-databricks-on-aws.md]

- **Application dependencies** must be installed on your local machine as part of your project, such as within a Python virtual environment. These run locally.
- **UDF dependencies** must be installed on Databricks. See the documentation on [Managing UDF Dependencies](/concepts/udf-dependency-sources.md) for details.

## Next Steps

Tutorials are available for each supported language: ^[databricks-connect-databricks-on-aws.md]

- [Databricks Connect for Python classic compute tutorial](/concepts/databricks-connect-with-classic-compute.md)
- Databricks Connect for Python serverless compute tutorial
- Databricks Connect for Scala classic compute tutorial
- Databricks Connect for Scala serverless compute tutorial
- [Databricks Connect for R tutorial](/concepts/databricks-connect-for-r.md)

The GitHub examples repository provides sample applications including a simple ETL application, an interactive data application based on Plotly, and an interactive data application based on Plotly and PySpark AI. ^[databricks-connect-databricks-on-aws.md]

## Related Concepts

- [Spark Connect](/concepts/spark-connect.md) — The open-source gRPC-based protocol underlying Databricks Connect
- [Databricks Visual Studio Code Extension](/concepts/databricks-visual-studio-code-extension.md) — Uses Databricks Connect for built-in debugging
- [Unity Catalog](/concepts/unity-catalog.md) — Supported through Databricks Connect extensions
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — Compatible runtime for Databricks Connect workloads

## Sources

- databricks-connect-databricks-on-aws.md

# Citations

1. [databricks-connect-databricks-on-aws.md](/references/databricks-connect-databricks-on-aws-65545eb5.md)

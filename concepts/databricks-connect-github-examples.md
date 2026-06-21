---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fd095163c9d32880c6816e7079f16fac0a7321314d73a952b3efa25133e069a2
  pageDirectory: concepts
  sources:
    - code-examples-for-databricks-connect-for-python-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-github-examples
    - DCGE
  citations:
    - file: code-examples-for-databricks-connect-for-python-databricks-on-aws.md
title: Databricks Connect GitHub Examples
description: A GitHub repository by Databricks containing example applications demonstrating Databricks Connect usage, including ETL, Plotly visualizations, and PySpark AI.
tags:
  - databricks
  - examples
  - github
  - python
timestamp: "2026-06-19T17:45:29.822Z"
---

```yaml
---
title: Databricks Connect GitHub Examples
summary: A set of reference example applications in the Databricks Connect GitHub repository demonstrating ETL, interactive Plotly applications, and Plotly with PySpark AI integration.
sources:
  - code-examples-for-databricks-connect-for-python-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T09:15:13.692Z"
updatedAt: "2026-06-19T09:15:13.692Z"
tags:
  - databricks
  - examples
  - github
aliases:
  - databricks-connect-github-examples
  - DCGE
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Databricks Connect GitHub Examples

**Databricks Connect GitHub Examples** are a collection of sample applications hosted in the [Databricks Connect GitHub repository](https://github.com/databricks-demos/dbconnect-examples) that demonstrate how to use [[Databricks Connect]] for Python. These examples show patterns for building ETL pipelines, interactive data visualizations, and AI-powered data applications using the Databricks Connect client library. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

## Repository Location

The examples are available in the public GitHub repository [`databricks-demos/dbconnect-examples`](https://github.com/databricks-demos/dbconnect-examples). The repository contains separate directories for Python and Scala implementations. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

## Available Examples

The repository includes the following Python examples (for Databricks Runtime 13.3 LTS and above): ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

| Example | Description |
|---------|-------------|
| **Simple ETL application** | Demonstrates a basic extract, transform, load workflow using Databricks Connect. Located at `python/ETL`. |
| **Interactive data application based on Plotly** | Shows how to build an interactive visualization dashboard using Plotly connected to a Databricks cluster. Located at `python/Plotly`. |
| **Interactive data application based on Plotly and PySpark AI** | Extends the Plotly example by incorporating PySpark AI capabilities for AI-enhanced data exploration. Located at `python/Plotly-AI`. |

## Portable SparkSession Pattern

A common pattern shown in the Databricks Connect documentation — and applicable to the GitHub examples — is writing code that works both with and without Databricks Connect. The following snippet attempts to use `DatabricksSession` and falls back to a standard `SparkSession` when the `databricks.connect` module is not available: ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

```python
from pyspark.sql import SparkSession, DataFrame

def get_spark() -> SparkSession:
    try:
        from databricks.connect import [DatabricksSession](/concepts/databrickssession.md)
        return [DatabricksSession](/concepts/databrickssession.md).builder.getOrCreate()
    except ImportError:
        return SparkSession.builder.getOrCreate()

def get_taxis(spark: SparkSession) -> DataFrame:
    return spark.read.table("samples.nyctaxi.trips")

get_taxis(get_spark()).show(5)
```

This pattern is used in the repository examples to ensure compatibility across different environments. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The core client library for connecting external applications to Databricks clusters.
- [DatabricksSession](/concepts/databrickssession.md) – The entry point for creating a SparkSession via Databricks Connect.
- PySpark AI – AI extensions for PySpark used in the Plotly-AI example.
- Plotly – The visualization library used in the interactive data examples.
- [Code examples for Databricks Connect for Python](/concepts/databricks-connect-for-python.md) – The documentation page that references these GitHub examples.

## Sources

- code-examples-for-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [code-examples-for-databricks-connect-for-python-databricks-on-aws.md](/references/code-examples-for-databricks-connect-for-python-databricks-on-aws-43e94551.md)

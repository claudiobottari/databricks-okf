---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fec75f6c140f4b8313cb8e5160994c8e131b0e4a8f2c6ecffacf59a7068993c1
  pageDirectory: concepts
  sources:
    - code-examples-for-databricks-connect-for-python-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - portable-spark-session-pattern
    - PSSP
  citations:
    - file: code-examples-for-databricks-connect-for-python-databricks-on-aws.md
title: Portable Spark Session Pattern
description: A try/except pattern for writing code that works in environments both with and without the DatabricksSession class, falling back to standard SparkSession.
tags:
  - pattern
  - python
  - compatibility
timestamp: "2026-06-19T14:13:35.803Z"
---

```markdown
# Portable Spark Session Pattern

**Portable Spark Session Pattern** refers to a coding technique that makes Spark applications written in Python compatible with both [[Databricks Connect]] (remote cluster execution) and standard SparkSession environments without code changes. The pattern detects whether the `DatabricksSession` class is available at import time and, if not, falls back to the standard `SparkSession.builder.getOrCreate()` method. This allows the same code to run inside a Databricks workspace, on a local machine connected to a Databricks cluster via Databricks Connect, or entirely offline with a local Spark installation.^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

## How it works

The pattern consists of a single helper function that attempts to import `DatabricksSession` from `databricks.connect`. If the import succeeds (meaning the environment has Databricks Connect installed and configured, typically with the `SPARK_REMOTE` environment variable set), the function returns a `DatabricksSession` instance. If the import fails with `ImportError`, the function falls back to creating a plain `SparkSession` via `SparkSession.builder.getOrCreate()`.^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

The `SPARK_REMOTE` environment variable is used by Databricks Connect to specify the remote cluster endpoint; when present and correctly configured, `DatabricksSession.builder.getOrCreate()` automatically picks it up. In the fallback case, `SparkSession.builder.getOrCreate()` uses whatever local Spark configuration is available (e.g., a `spark-defaults.conf` file or embedded Spark).^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

## Code example

The following example defines a reusable `get_spark()` function and then uses it to query a table:^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

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

## Usage

This pattern is useful when:

- Developing locally with an IDE or notebook where Databricks Connect is optionally installed.
- Sharing notebook or application code between team members who may or may not use Databricks Connect.
- Writing tests that can run both against a remote Databricks cluster (when connected) and against a local Spark instance (when offline).

The pattern applies to Databricks Connect for Databricks Runtime 13.3 LTS and above.^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

## Related concepts

- [[Databricks Connect]] — The client library that allows remote execution on Databricks clusters.
- SparkSession — The entry point for Spark DataFrame and SQL APIs.
- [[DatabricksSession]] — A Databricks-specific subclass of SparkSession used with Databricks Connect.
- [[Spark Connect|SPARK_REMOTE]] — An environment variable that configures the remote cluster endpoint for Databricks Connect.

## Sources

- code-examples-for-databricks-connect-for-python-databricks-on-aws.md
```

# Citations

1. [code-examples-for-databricks-connect-for-python-databricks-on-aws.md](/references/code-examples-for-databricks-connect-for-python-databricks-on-aws-43e94551.md)

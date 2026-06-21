---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7f149fa968642d83fc463a596ab1dafe4105712ad1d516df1e1bff1c9c52ae86
  pageDirectory: concepts
  sources:
    - code-examples-for-databricks-connect-for-python-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - portable-sparksession-pattern
    - PSP
    - portable-sparksession-pattern-for-databricks-connect
    - PSPFDC
  citations:
    - file: code-examples-for-databricks-connect-for-python-databricks-on-aws.md
title: Portable SparkSession Pattern
description: A coding pattern that gracefully falls back from DatabricksSession to a regular SparkSession when Databricks Connect is not available, enabling portable PySpark code.
tags:
  - databricks
  - python
  - pattern
  - portability
timestamp: "2026-06-19T17:45:40.422Z"
---

# Portable SparkSession Pattern

The **Portable SparkSession Pattern** is a coding pattern for writing PySpark code that can run both with [Databricks Connect](/concepts/databricks-connect.md) (using `DatabricksSession`) and in environments where the `DatabricksSession` class is unavailable (falling back to a standard `SparkSession`). ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

## Overview

When developing applications that may execute in different Spark environments, the `DatabricksSession` class may not always be available. The Portable SparkSession pattern gracefully falls back to the standard `SparkSession` when `DatabricksSession` cannot be imported, allowing the same code to work in both contexts without modification. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

This pattern is designed for [Databricks Connect](/concepts/databricks-connect.md) for Databricks Runtime 13.3 LTS and above. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

## Implementation

The pattern uses a `try`/`except ImportError` block to attempt importing `DatabricksSession` from `databricks.connect`. If the import fails (because the `databricks-connect` package is not installed), it falls back to the standard `SparkSession` from `pyspark.sql`. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

### Basic Pattern

```python
from pyspark.sql import SparkSession, DataFrame

def get_spark() -> SparkSession:
    try:
        from databricks.connect import [[databrickssession|DatabricksSession]]
        return [[databrickssession|DatabricksSession]].builder.getOrCreate()
    except ImportError:
        return SparkSession.builder.getOrCreate()
```

^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

### Usage Example

The following example demonstrates the pattern in a complete workflow that queries a table and displays results: ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

```python
from pyspark.sql import SparkSession, DataFrame

def get_spark() -> SparkSession:
    try:
        from databricks.connect import [[databrickssession|DatabricksSession]]
        return [[databrickssession|DatabricksSession]].builder.getOrCreate()
    except ImportError:
        return SparkSession.builder.getOrCreate()

def get_taxis(spark: SparkSession) -> DataFrame:
    return spark.read.table("samples.nyctaxi.trips")

get_taxis(get_spark()).show(5)
```

This code queries the `samples.nyctaxi.trips` table and returns the first 5 rows, working identically whether running through [Databricks Connect](/concepts/databricks-connect.md) or a local Spark session. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

## Authentication

When using the Portable SparkSession pattern, authentication for [Databricks Connect](/concepts/databricks-connect.md) connections is handled through the `SPARK_REMOTE` environment variable. The `DatabricksSession.builder.getOrCreate()` method reads this variable to establish the remote connection to the Databricks cluster. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

## Best Practices

- **Use the pattern in library code** that may be consumed by both Databricks notebooks and external applications.
- **Wrap the import attempt** in a dedicated factory function (like `get_spark()`) to keep the fallback logic in one place.
- **Return a `SparkSession` type hint** from the factory function, since both `DatabricksSession` and `SparkSession` share the same API surface for most operations.
- **Set the `SPARK_REMOTE` environment variable** when running outside a Databricks cluster to enable remote connectivity.
- **Use the `except ImportError` clause** specifically, rather than a broad exception handler, to only catch cases where the `databricks.connect` module is not installed.

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The client library that enables remote Spark execution from IDEs and custom applications
- [DatabricksSession](/concepts/databrickssession.md) — The Databricks-specific session class for remote connections
- SparkSession — The standard PySpark entry point for Spark functionality
- SPARK_REMOTE Environment Variable — Configuration for Databricks Connect remote connections
- Code Portability Patterns — General approaches for writing environment-agnostic Spark code
- PySpark — The Python API for Apache Spark

## Sources

- code-examples-for-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [code-examples-for-databricks-connect-for-python-databricks-on-aws.md](/references/code-examples-for-databricks-connect-for-python-databricks-on-aws-43e94551.md)

---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e907d0581c5381e91ba6308abd2d6b0f4a8508d4e1fe7823b79cc9cad892a6a4
  pageDirectory: concepts
  sources:
    - code-examples-for-databricks-connect-for-python-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - portable-sparksession-pattern-for-databricks-connect
    - PSPFDC
  citations:
    - file: code-examples-for-databricks-connect-for-python-databricks-on-aws.md
title: Portable SparkSession pattern for Databricks Connect
description: A code pattern that falls back from DatabricksSession to SparkSession when Databricks Connect is unavailable, enabling portable code
tags:
  - databricks
  - python
  - portability
timestamp: "2026-06-18T14:37:29.393Z"
---

# Portable SparkSession pattern for Databricks Connect

The **Portable SparkSession pattern for Databricks Connect** is a code pattern that allows a single Python script to work both when connected to a remote Databricks cluster via [Databricks Connect](/concepts/databricks-connect.md) and when running directly in a local SparkSession environment. This pattern enables code portability across different execution contexts without manual configuration changes. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

## Overview

When developing Spark applications, code may need to run in multiple environments: locally with a standalone PySpark installation, or remotely through [Databricks Connect](/concepts/databricks-connect.md) connected to a Databricks cluster. The portable SparkSession pattern handles both cases by attempting to create a [DatabricksSession](/concepts/databrickssession.md) first, and falling back to a standard SparkSession if the Databricks Connect client libraries are not available. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

## Implementation

The pattern uses a `try-except` block to import the `DatabricksSession` class. If the import succeeds (meaning the Databricks Connect client is installed), it creates a `DatabricksSession`. If the import fails with `ImportError`, it falls back to a standard `SparkSession`. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

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

### Complete Example

The following example demonstrates the full pattern, combining the portable session creation with a query function:

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

^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

## Authentication

When using Databricks Connect, this pattern assumes that authentication is configured through the `SPARK_REMOTE` environment variable or through the default [Databricks authentication](/concepts/databricks-authentication-type.md) setup. In the fallback scenario (local SparkSession), standard local Spark configuration applies. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

## Use Cases

- **Development workstations**: Developers can write and test code locally with PySpark, then deploy the same code to run against Databricks clusters. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]
- **CI/CD pipelines**: The same test scripts can run in environments that may or may not have Databricks Connect installed. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]
- **Notebooks and scripts**: Code can be shared between local development notebooks and Databricks notebooks without manual session creation logic changes. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

## Return Type Note

The function signature declares `SparkSession` as the return type, even when `DatabricksSession` is returned. This is valid because `DatabricksSession` extends `SparkSession`, maintaining type compatibility. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The client library for connecting IDEs and applications to Databricks clusters
- [DatabricksSession](/concepts/databrickssession.md) — The Databricks-specific SparkSession subclass used with Databricks Connect
- SparkSession — The entry point to PySpark functionality
- SPARK_REMOTE Environment Variable|SPARK_REMOTE environment variable — Configuration variable for Databricks Connect authentication
- [Databricks authentication](/concepts/databricks-authentication-type.md) — Authentication methods for Databricks API access

## Sources

- code-examples-for-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [code-examples-for-databricks-connect-for-python-databricks-on-aws.md](/references/code-examples-for-databricks-connect-for-python-databricks-on-aws-43e94551.md)

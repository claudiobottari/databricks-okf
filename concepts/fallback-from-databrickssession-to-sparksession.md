---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 581b5b17faffb22078c98e9edf5dbf2181f42ae7bdbd920cb0846da551ee6abc
  pageDirectory: concepts
  sources:
    - code-examples-for-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - fallback-from-databrickssession-to-sparksession
    - FFDTS
  citations:
    - file: code-examples-for-databricks-connect-for-scala-databricks-on-aws.md
title: Fallback from DatabricksSession to SparkSession
description: The pattern of using SparkSession.builder().getOrCreate() directly when the DatabricksSession class is unavailable, relying on the SPARK_REMOTE environment variable for authentication.
tags:
  - databricks
  - scala
  - fallback
  - authentication
timestamp: "2026-06-19T14:15:15.354Z"
---

# Fallback from [DatabricksSession](/concepts/databrickssession.md) to SparkSession

**Fallback from [DatabricksSession](/concepts/databrickssession.md) to SparkSession** refers to the technique of using `SparkSession.builder().getOrCreate()` directly instead of `DatabricksSession.builder().getOrCreate()` in [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) when the `DatabricksSession` class is unavailable. This approach enables applications to maintain compatibility with standard Spark APIs while still connecting to Databricks clusters.

## Overview

When writing Scala applications with [Databricks Connect](/concepts/databricks-connect.md), the recommended practice is to use `DatabricksSession.builder().getOrCreate()` to establish a connection to a Databricks cluster. However, in scenarios where the `DatabricksSession` class is not available — such as when the application must work in environments where Databricks-specific dependencies are not included — developers can fall back to the standard `SparkSession.builder().getOrCreate()` method. ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

## Usage

### When to Use Fallback

The fallback is appropriate when:
- The application needs to be portable across environments that may or may not have Databricks Connect installed.
- The `DatabricksSession` class is not part of the classpath.
- You want to minimize dependencies on Databricks-specific libraries.

### How It Works

When using `SparkSession.builder().getOrCreate()` as a fallback, authentication is typically handled through the `SPARK_REMOTE` environment variable rather than through [DatabricksSession](/concepts/databrickssession.md)'s built-in authentication mechanisms. ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

## Code Example

The following example demonstrates the fallback pattern. It queries the `samples.nyctaxi.trips` table and returns the first 5 rows using a standard `SparkSession`:

```scala
import org.apache.spark.sql.{DataFrame, SparkSession}

object Main {
  def main(args: Array[String]): Unit = {
    getTaxis(getSpark()).show(5)
  }

  private def getSpark(): SparkSession = {
    SparkSession.builder().getOrCreate()
  }

  private def getTaxis(spark: SparkSession): DataFrame = {
    spark.read.table("samples.nyctaxi.trips")
  }
}
```

^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

### Key Differences

| Aspect | [DatabricksSession](/concepts/databrickssession.md) | SparkSession (Fallback) |
|--------|------------------|------------------------|
| Dependency | Requires Databricks Connect library | Standard Spark dependency |
| Authentication | Built-in Databricks authentication | Requires `SPARK_REMOTE` environment variable or other config |
| API Surface | Includes Databricks-specific extensions | Standard Spark API only |

## Best Practices

- **Use [DatabricksSession](/concepts/databrickssession.md) by default** when your application is designed exclusively for Databricks Connect and you have the library available.
- **Implement the fallback** when you need code that works in multiple environments, such as sharing code between local development and Databricks-connected execution.
- **Configure `SPARK_REMOTE`** when using the fallback approach, as the automatic authentication provided by `DatabricksSession` will not be available.

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The client library that enables remote connection to Databricks clusters
- [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) — Scala-specific implementation of Databricks Connect
- [DatabricksSession](/concepts/databrickssession.md) — The Databricks-specific session class for establishing connections
- [SPARK_REMOTE](/concepts/spark-connect.md) — Environment variable for configuring remote Spark connections
- SparkSession — The standard entry point for Spark functionality

## Sources

- code-examples-for-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [code-examples-for-databricks-connect-for-scala-databricks-on-aws.md](/references/code-examples-for-databricks-connect-for-scala-databricks-on-aws-383843cd.md)

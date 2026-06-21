---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 694d97699c85959beb8b7cd5ef649f40a47cb2397043cb48d5ad627d15fcb656
  pageDirectory: concepts
  sources:
    - code-examples-for-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sparksession-with-spark_remote-authentication
    - SWSA
  citations:
    - file: code-examples-for-databricks-connect-for-scala-databricks-on-aws.md
title: SparkSession with SPARK_REMOTE authentication
description: An alternative approach to connecting to Databricks clusters using the standard SparkSession class together with the SPARK_REMOTE environment variable for authentication, useful when DatabricksSession is unavailable.
tags:
  - databricks
  - spark
  - authentication
timestamp: "2026-06-18T10:59:04.711Z"
---

# SparkSession with SPARK_REMOTE authentication

**SparkSession with SPARK_REMOTE authentication** refers to the pattern of creating a SparkSession in a [Databricks Connect](/concepts/databricks-connect.md) client application by relying on the `SPARK_REMOTE` environment variable for authentication, rather than using the `DatabricksSession` builder class. This approach is useful when `DatabricksSession` is unavailable or when you prefer environment-based configuration.^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

## Overview

Databricks Connect enables you to connect popular IDEs, notebook servers, and custom applications to Databricks clusters. While the recommended approach uses `DatabricksSession.builder().getOrCreate()`, you can also create a standard `SparkSession` that reads authentication configuration from the `SPARK_REMOTE` environment variable.^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

## Usage

To use `SparkSession` with `SPARK_REMOTE` authentication, set the `SPARK_REMOTE` environment variable with the appropriate connection string before launching your application. Then create a `SparkSession` using the standard builder pattern:^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

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

## How it works

When `SparkSession.builder().getOrCreate()` is called without explicitly setting configuration, the Spark session reads the `SPARK_REMOTE` environment variable to determine how to connect to the remote Databricks cluster. This environment variable contains the connection endpoint and authentication credentials required to establish the remote session.^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

## Comparison with [DatabricksSession](/concepts/databrickssession.md)

The `DatabricksSession` class provides a higher-level API that handles authentication configuration automatically, including reading from default Databricks authentication profiles. Using `SparkSession` with `SPARK_REMOTE` gives you more direct control over the connection configuration but requires you to manage the environment variable yourself.^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

## Prerequisites

Before using this pattern, you must [set up the Databricks Connect client](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/scala/install) and configure the `SPARK_REMOTE` environment variable with valid connection details for your Databricks workspace.^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

## Related concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The client library that enables remote Spark session connections
- [DatabricksSession](/concepts/databrickssession.md) — The recommended builder class for Databricks Connect
- SparkSession — The entry point for Spark DataFrame and SQL functionality
- SPARK_REMOTE Environment Variable|SPARK_REMOTE environment variable — Configuration variable for remote Spark connections
- [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) — Scala-specific setup and usage of Databricks Connect

## Sources

- code-examples-for-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [code-examples-for-databricks-connect-for-scala-databricks-on-aws.md](/references/code-examples-for-databricks-connect-for-scala-databricks-on-aws-383843cd.md)

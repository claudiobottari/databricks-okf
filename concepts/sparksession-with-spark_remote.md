---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 859fc1cb857f12e9836d4e1cd7cf81bea8f92a9fe9826751f3a3130fafcbd755
  pageDirectory: concepts
  sources:
    - code-examples-for-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sparksession-with-spark_remote
    - SWS
    - SparkSession management
    - sparksession-with-spark_remote-authentication
    - SWSA
  citations:
    - file: code-examples-for-databricks-connect-for-scala-databricks-on-aws.md
title: SparkSession with SPARK_REMOTE
description: Alternative pattern to connect to Databricks clusters using the standard SparkSession builder when DatabricksSession is unavailable, relying on the SPARK_REMOTE environment variable
tags:
  - databricks
  - scala
  - spark-session
  - authentication
timestamp: "2026-06-19T17:45:27.664Z"
---

# SparkSession with SPARK_REMOTE

**SparkSession with SPARK_REMOTE** refers to using the standard Apache Spark `SparkSession` builder in a [Databricks Connect](/concepts/databricks-connect.md) client for Scala, with authentication handled via the `SPARK_REMOTE` environment variable instead of the `DatabricksSession` helper class. This approach is useful when the `DatabricksSession` class is unavailable or when a project already relies on the core Spark API. ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

## Usage

In a Databricks Connect client, calling `SparkSession.builder().getOrCreate()` reads the `SPARK_REMOTE` environment variable to determine the remote cluster endpoint and authentication credentials. The client must be [set up](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/scala/install) before this call. ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

## Example

The following Scala code queries the `samples.nyctaxi.trips` table and shows the first five rows, using `SparkSession` with the `SPARK_REMOTE` environment variable for authentication:

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

This pattern is equivalent to using `DatabricksSession.builder().getOrCreate()` when the `SPARK_REMOTE` environment variable is properly configured. ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The remote execution framework that this pattern uses.
- [DatabricksSession](/concepts/databrickssession.md) – The recommended convenience wrapper for Databricks Connect clients.
- SPARK_REMOTE Environment Variable|SPARK_REMOTE environment variable – The environment variable that supplies the remote cluster connection string.
- Code examples for Databricks Connect for Scala – The source article containing this example.

## Sources

- code-examples-for-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [code-examples-for-databricks-connect-for-scala-databricks-on-aws.md](/references/code-examples-for-databricks-connect-for-scala-databricks-on-aws-383843cd.md)

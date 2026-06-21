---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 82b60d9ebd3d0c99d76253593c4e85aef0230f674def33d31fd9382382d5276f
  pageDirectory: concepts
  sources:
    - code-examples-for-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - sparksession-based-databricks-connect
    - SDC
  citations:
    - file: code-examples-for-databricks-connect-for-scala-databricks-on-aws.md
title: SparkSession-based Databricks Connect
description: A fallback pattern for using Databricks Connect with the standard SparkSession class when DatabricksSession is unavailable, relying on SPARK_REMOTE for authentication.
tags:
  - databricks
  - scala
  - patterns
timestamp: "2026-06-18T14:38:27.470Z"
---

# SparkSession-based Databricks Connect

**SparkSession-based Databricks Connect** refers to using a plain `SparkSession` — rather than the `DatabricksSession` wrapper — to connect a local or remote application to a Databricks cluster via the Databricks Connect client. This approach is useful when the `DatabricksSession` class is unavailable or when an existing Spark application already constructs its own `SparkSession`. ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

## Overview

Databricks Connect allows you to connect popular IDEs, notebook servers, and custom applications to Databricks clusters. While the recommended entry point is `DatabricksSession` (provided by the `com.databricks.connect` package), you can also use the standard `SparkSession.builder()` — provided that the client library and required environment variables are correctly configured. ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

The `SparkSession`-based pattern is especially relevant for Scala applications that already manage their own Spark session or that need to avoid a dependency on the Databricks-specific session class. ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

## Requirements

Before using any Databricks Connect client, you must:

- Set up the client library and authentication as described in the [Install the Databricks Connect client](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/scala/install) guide.
- Ensure the client version matches the Databricks Runtime version (13.3 LTS or above). ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

## Authentication via the `SPARK_REMOTE` Environment Variable

When using `SparkSession.builder().getOrCreate()`, Databricks Connect looks for the `SPARK_REMOTE` environment variable to resolve the cluster endpoint and authentication tokens. This variable must be set before the session is created; otherwise, the connection will fail or fall back to a local Spark session. ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

## Example: Reading a Table with SparkSession

The following example demonstrates how to read a table from a Databricks cluster using a plain `SparkSession` and the `SPARK_REMOTE` environment variable for authentication. It queries the `samples.nyctaxi.trips` table and prints the first five rows.

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

## Using `SparkSession` When `DatabricksSession` Is Unavailable

The `DatabricksSession` class provides additional convenience features, such as automatic authentication discovery. If `DatabricksSession` is not available in your classpath, or if you prefer to avoid it, you can fall back to `SparkSession.builder().getOrCreate()` and rely on environment variables or other Spark configuration sources for connection details. ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

## Additional Resources

- DatabricksSession-based Databricks Connect – The recommended approach using the `DatabricksSession` builder.
- [Databricks Connect Client Setup](/concepts/databricks-connect-client-setup.md) – Prerequisites for installing and configuring the client.
- [Databricks Connect Authentication](/concepts/databricks-connect-authentication.md) – Methods for authenticating with a Databricks cluster.
- Code Examples for Databricks Connect for Scala – The source article containing full examples.

Databricks also provides example applications in the [Databricks Connect GitHub repository](https://github.com/databricks-demos/dbconnect-examples), including a simple ETL application and chart visualizations with JFreeChart. ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

## Sources

- code-examples-for-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [code-examples-for-databricks-connect-for-scala-databricks-on-aws.md](/references/code-examples-for-databricks-connect-for-scala-databricks-on-aws-383843cd.md)

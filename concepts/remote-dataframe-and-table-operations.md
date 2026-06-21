---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5a63b5d2444d88d1a5ccf5cfa2909033fb43c9b377a88fddb9dcff434d24c0c2
  pageDirectory: concepts
  sources:
    - code-examples-for-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - remote-dataframe-and-table-operations
    - table operations and Remote DataFrame
    - RDATO
  citations:
    - file: code-examples-for-databricks-connect-for-scala-databricks-on-aws.md
title: Remote DataFrame and table operations
description: Patterns for creating, reading, writing, and querying DataFrames and tables on a remote Databricks cluster using Databricks Connect
tags:
  - databricks
  - scala
  - dataframe
  - sql
timestamp: "2026-06-19T17:45:40.211Z"
---

# Remote DataFrame and table operations

**Remote DataFrame and table operations** refers to the ability to run Spark DataFrame and SQL table operations on a remote Databricks cluster from a local IDE, notebook server, or custom application using [Databricks Connect](/concepts/databricks-connect.md). This enables interactive development with full access to cluster resources without requiring a local Spark cluster. ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

## Overview

[Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) allows you to submit [Spark DataFrame](/concepts/spark-dataframe-evaluation-pattern.md) transformations and Spark SQL queries to a Databricks cluster. The client application uses either `DatabricksSession` or a plain `SparkSession` configured with the `SPARK_REMOTE` environment variable to connect. Once connected, the remote cluster executes the operations and returns results to the client. ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

## Common operations

### Reading a table

You can read a Databricks-managed table remotely. The example below reads the `samples.nyctaxi.trips` table and displays the first five rows:

```scala
import com.databricks.connect.[[databrickssession|DatabricksSession]]
import org.apache.spark.sql.SparkSession

object Main {
  def main(args: Array[String]): Unit = {
    val spark = [[databrickssession|DatabricksSession]].builder().getOrCreate()
    val df = spark.read.table("samples.nyctaxi.trips")
    df.limit(5).show()
  }
}
```

^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

### Creating a DataFrame and saving to a table

You can create an in-memory DataFrame locally and write it to a remote table:

1. Use `createDataFrame` with a defined schema.
2. Drop any existing table with the same name.
3. Save the DataFrame using `saveAsTable`.
4. Query the remote table with `spark.sql` and display the results.
5. Clean up by dropping the table.

A complete example creates a temperature DataFrame with airport codes, dates, and high/low temperatures, stores it as `zzz_demo_temps_table`, runs a filtered query, and shows the output. ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

### Using SparkSession instead of [DatabricksSession](/concepts/databrickssession.md)

When the `DatabricksSession` class is unavailable, you can use a standard `SparkSession` configured via the `SPARK_REMOTE` environment variable. The following example reads the same `samples.nyctaxi.trips` table and shows five rows:

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

## Additional examples

Databricks provides a repository with more examples, including a simple ETL application and charts visualizations using JFreeChart. These demonstrate how to use Databricks Connect for remote ETL tasks and reporting. ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

## Requirements

- Databricks Connect for Databricks Runtime 13.3 LTS and above.
- The client must be set up with default authentication or the `SPARK_REMOTE` environment variable. ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

## Related concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The framework enabling remote client-cluster connectivity.
- [Spark DataFrame](/concepts/spark-dataframe-evaluation-pattern.md) – The core data abstraction used in remote operations.
- Spark SQL – For running SQL queries on remote tables.
- [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) – The Python equivalent of the Scala examples.

## Sources

- code-examples-for-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [code-examples-for-databricks-connect-for-scala-databricks-on-aws.md](/references/code-examples-for-databricks-connect-for-scala-databricks-on-aws-383843cd.md)

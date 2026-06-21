---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7d978256b1b6eb31a04c07af6b51ffd22c19d887a0d88bd35e327403e3c47f98
  pageDirectory: concepts
  sources:
    - code-examples-for-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-table-operations
    - DCTO
  citations:
    - file: code-examples-for-databricks-connect-for-scala-databricks-on-aws.md
title: Databricks Connect Table Operations
description: Code patterns for reading, creating, and managing tables in Databricks using Databricks Connect for Scala, including CRUD operations and SQL queries.
tags:
  - databricks
  - scala
  - data-operations
timestamp: "2026-06-18T14:38:02.985Z"
---

# Databricks Connect Table Operations

**Databricks Connect Table Operations** refers to the basic set of actions you can perform on Databricks-managed tables from a remote client using [Databricks Connect](/concepts/databricks-connect.md) for Scala (or Python). These operations include reading, creating, writing, querying, and deleting tables, all through familiar Apache Spark APIs.

## Overview

Databricks Connect allows you to connect an IDE, notebook server, or custom application to a Databricks cluster. Once connected, you can operate on tables stored in the Databricks environment as if they were local Spark DataFrames. The examples in this article assume default authentication for the Databricks Connect client. ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

## Reading a Table

To read a table, use the `spark.read.table("catalog.schema.table")` method. The following simple example queries the `samples.nyctaxi.trips` table and displays its first five rows:

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

## Creating and Writing a Table

You can create an in-memory DataFrame and write it to a new table on the cluster. The example below builds a schema and data for airport temperature records, drops any existing table named `zzz_demo_temps_table` in the `default` schema, and then saves the DataFrame using `saveAsTable`.

```scala
val temps = spark.createDataFrame(data).toDF(schema.fieldNames: _*)
spark.sql("USE default")
spark.sql("DROP TABLE IF EXISTS zzz_demo_temps_table")
temps.write.saveAsTable("zzz_demo_temps_table")
```

If a table with the same name already exists, it must be deleted first (with `DROP TABLE IF EXISTS`) before `saveAsTable` can succeed, unless you specify an overwrite mode. ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

## Querying a Table

After a table is created, you can submit SQL queries against it using `spark.sql()`. The following query filters rows, groups results, and orders them by temperature:

```scala
val df_temps = spark.sql(
  """SELECT * FROM zzz_demo_temps_table
     WHERE AirportCode != 'BLI' AND Date > '2021-04-01'
     GROUP BY AirportCode, Date, TempHighF, TempLowF
     ORDER BY TempHighF DESC"""
)
df_temps.show()
```

The query runs entirely on the remote cluster, and only the result set is returned to the client. ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

## Deleting a Table

To clean up, use `spark.sql("DROP TABLE <table_name>")`. This removes the table metadata and data from the Databricks cluster.

```scala
spark.sql("DROP TABLE zzz_demo_temps_table")
```

^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

## Using SparkSession vs. [DatabricksSession](/concepts/databrickssession.md)

The `DatabricksSession` class (from the `com.databricks.connect` package) is the recommended entry point for Databricks Connect. If it is unavailable, you can use the standard `SparkSession` class as long as the `SPARK_REMOTE` environment variable is set for authentication.

```scala
import org.apache.spark.sql.{DataFrame, SparkSession}

object Main {
  def main(args: Array[String]): Unit = {
    val spark = SparkSession.builder().getOrCreate()
    val df = spark.read.table("samples.nyctaxi.trips")
    df.show(5)
  }
}
```

^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The underlying remote connectivity framework.
- [DatabricksSession](/concepts/databrickssession.md) – The Scala entry point for Databricks Connect.
- SparkSession – The standard Spark entry point (works with `SPARK_REMOTE`).
- DataFrame – The primary abstraction for table data in Spark.
- Databricks Runtime – The cluster runtime that hosts the tables.

## Sources

- code-examples-for-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [code-examples-for-databricks-connect-for-scala-databricks-on-aws.md](/references/code-examples-for-databricks-connect-for-scala-databricks-on-aws-383843cd.md)

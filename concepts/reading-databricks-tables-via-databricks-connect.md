---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 38932c1d8f600aa64ac7ae0cc4bb45630b78208b0d424b1a49ed8fe872c03762
  pageDirectory: concepts
  sources:
    - code-examples-for-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - reading-databricks-tables-via-databricks-connect
    - RDTVDC
  citations:
    - file: code-examples-for-databricks-connect-for-scala-databricks-on-aws.md
title: Reading Databricks Tables via Databricks Connect
description: The pattern of using spark.read.table() through Databricks Connect to query and display remote Databricks tables from a local Scala application.
tags:
  - databricks
  - scala
  - data-access
timestamp: "2026-06-19T09:16:21.984Z"
---

# Reading Databricks Tables via Databricks Connect

**Databricks Connect** enables you to connect popular IDEs, notebook servers, and custom applications to Databricks clusters, allowing you to read and process data stored in Databricks tables using familiar Spark APIs from a remote client. ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

## Using `DatabricksSession` (Recommended)

The simplest approach to read a table is to create a `DatabricksSession` (available for Databricks Runtime 13.3 LTS and above) and use the `.read.table()` method. The following Scala example queries the `samples.nyctaxi.trips` table and displays the first five rows: ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

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

After obtaining a DataFrame via `spark.read.table()`, you can perform any standard Spark SQL operation – filtering, aggregations, joins – and materialize results locally or write them back to the cluster. ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

## Using `SparkSession` Directly

In environments where the `DatabricksSession` class is unavailable, you can use the standard `SparkSession.builder().getOrCreate()` instead, provided you have configured the `SPARK_REMOTE` environment variable or set connection properties through other authentication methods. The following example reads the same table and returns the first five rows: ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

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

## Creating a Table and Reading It Back

A more complete example demonstrates reading data after creating a table. The pattern is: drop the table if it exists (to avoid conflicts), create a temporary DataFrame, save it as a managed table, then read that table with SQL or the DataFrame reader. ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

```scala
import com.databricks.connect.[[databrickssession|DatabricksSession]]
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.types._
import java.time.LocalDate

object Main {
  def main(args: Array[String]): Unit = {
    val spark = [[databrickssession|DatabricksSession]].builder().getOrCreate()

    // Create schema and data
    val schema = StructType(Seq(
      StructField("AirportCode", StringType, false),
      StructField("Date", DateType, false),
      StructField("TempHighF", IntegerType, false),
      StructField("TempLowF", IntegerType, false)
    ))
    val data = Seq(...) // airport temperature data
    val temps = spark.createDataFrame(data).toDF(schema.fieldNames: _*)

    // Save as table
    spark.sql("USE default")
    spark.sql("DROP TABLE IF EXISTS zzz_demo_temps_table")
    temps.write.saveAsTable("zzz_demo_temps_table")

    // Read the table back with a query
    val df_temps = spark.sql(
      "SELECT * FROM zzz_demo_temps_table " +
      "WHERE AirportCode != 'BLI' AND Date > '2021-04-01' " +
      "GROUP BY AirportCode, Date, TempHighF, TempLowF " +
      "ORDER BY TempHighF DESC"
    )
    df_temps.show()

    // Clean up
    spark.sql("DROP TABLE zzz_demo_temps_table")
  }
}
```

Reading tables via Databricks Connect is transparent: the remote client sends Spark operations to the Databricks cluster, which executes them and returns results to the client. The API surface is identical to running Spark jobs locally on a cluster. ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

## Prerequisites

Before reading tables, you must [set up the Databricks Connect client](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/scala/install). The examples above assume default authentication is configured. ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The framework that enables remote Spark client connections to Databricks clusters
- SparkSession – The entry point for reading data and executing SQL queries
- [DatabricksSession](/concepts/databrickssession.md) – A Databricks‑specific wrapper around SparkSession with additional integration features
- DataFrame – The primary data abstraction in Spark used to represent tabular data
- Spark SQL – The SQL interface for querying structured data within Spark

## Sources

- code-examples-for-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [code-examples-for-databricks-connect-for-scala-databricks-on-aws.md](/references/code-examples-for-databricks-connect-for-scala-databricks-on-aws-383843cd.md)

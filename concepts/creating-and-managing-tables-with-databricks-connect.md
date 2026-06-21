---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3dacf96497872c79f0ba732c5350ad92431d042d53aae1e782678446f408077a
  pageDirectory: concepts
  sources:
    - code-examples-for-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - creating-and-managing-tables-with-databricks-connect
    - Managing Tables with Databricks Connect and Creating
    - CAMTWDC
  citations:
    - file: code-examples-for-databricks-connect-for-scala-databricks-on-aws.md
title: Creating and Managing Tables with Databricks Connect
description: The pattern of creating in-memory DataFrames locally, saving them as managed tables on a remote Databricks cluster, querying them, and cleaning up via Databricks Connect for Scala.
tags:
  - databricks
  - scala
  - etl
timestamp: "2026-06-19T09:15:34.179Z"
---

# Creating and Managing Tables with Databricks Connect

**Creating and Managing Tables with Databricks Connect** refers to the process of using the Databricks Connect client to create, populate, query, and delete tables on a remote Databricks cluster from a local Scala or Python application. Databricks Connect enables you to connect popular IDEs, notebook servers, and custom applications to Databricks clusters, allowing you to manage tables programmatically without working directly in the Databricks workspace. ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

## Overview

When using Databricks Connect, you interact with tables on a remote Databricks cluster through a local SparkSession or [DatabricksSession](/concepts/databrickssession.md) object. The workflow typically involves creating a DataFrame locally, saving it as a table on the cluster, running SQL queries against that table, and optionally cleaning up by dropping the table. ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

## Prerequisites

Before you can create and manage tables with Databricks Connect, you must [set up the Databricks Connect client](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/scala/install). The examples in this article assume you are using default authentication for Databricks Connect client setup. ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

## Creating a Table

To create a table using Databricks Connect, you first create a DataFrame in your local application, then save it as a table on the remote Databricks cluster using the `saveAsTable()` method. ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

### Step 1: Create a DataFrame

Define a schema and populate a DataFrame with data. The following example creates a DataFrame of airport temperature data: ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

```scala
import com.databricks.connect.[[databrickssession|DatabricksSession]]
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.types._
import java.time.LocalDate

val spark = [[databrickssession|DatabricksSession]].builder().getOrCreate()

val schema = StructType(
  Seq(
    StructField("AirportCode", StringType, false),
    StructField("Date", DateType, false),
    StructField("TempHighF", IntegerType, false),
    StructField("TempLowF", IntegerType, false)
  )
)

val data = Seq(
  ( "BLI", LocalDate.of(2021, 4, 3), 52, 43 ),
  ( "BLI", LocalDate.of(2021, 4, 2), 50, 38),
  ( "BLI", LocalDate.of(2021, 4, 1), 52, 41),
  ( "PDX", LocalDate.of(2021, 4, 3), 64, 45),
  ( "PDX", LocalDate.of(2021, 4, 2), 61, 41),
  ( "PDX", LocalDate.of(2021, 4, 1), 66, 39),
  ( "SEA", LocalDate.of(2021, 4, 3), 57, 43),
  ( "SEA", LocalDate.of(2021, 4, 2), 54, 39),
  ( "SEA", LocalDate.of(2021, 4, 1), 56, 41)
)

val temps = spark.createDataFrame(data).toDF(schema.fieldNames: _*)
```

### Step 2: Drop Existing Table (Optional)

If a table with the target name already exists, drop it first to avoid conflicts: ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

```scala
spark.sql("USE default")
spark.sql("DROP TABLE IF EXISTS zzz_demo_temps_table")
```

### Step 3: Save the DataFrame as a Table

Use the `saveAsTable()` method to write the DataFrame's contents to a table on the Databricks cluster: ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

```scala
temps.write.saveAsTable("zzz_demo_temps_table")
```

## Querying a Table

After creating a table, you can query it using standard Spark SQL through the `spark.sql()` method. The following example queries the temperature table, filtering for specific airports and dates, then ordering by high temperature: ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

```scala
val df_temps = spark.sql("SELECT * FROM zzz_demo_temps_table " +
  "WHERE AirportCode != 'BLI' AND Date > '2021-04-01' " +
  "GROUP BY AirportCode, Date, TempHighF, TempLowF " +
  "ORDER BY TempHighF DESC")

df_temps.show()
```

This query returns:

```
+------------+-----------+---------+--------+
| AirportCode|       Date|TempHighF|TempLowF|
+------------+-----------+---------+--------+
|        PDX | 2021-04-03|      64 |     45 |
|        PDX | 2021-04-02|      61 |     41 |
|        SEA | 2021-04-03|      57 |     43 |
|        SEA | 2021-04-02|      54 |     39 |
+------------+-----------+---------+--------+
```

## Reading an Existing Table

To read an existing table from the Databricks cluster, use the `spark.read.table()` method: ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

```scala
val df = spark.read.table("samples.nyctaxi.trips")
df.limit(5).show()
```

## Deleting a Table

After you finish working with a table, you can clean up by dropping it from the Databricks cluster: ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

```scala
spark.sql("DROP TABLE zzz_demo_temps_table")
```

## Using [DatabricksSession](/concepts/databrickssession.md) vs. SparkSession

Databricks Connect provides two session classes for connecting to a remote cluster: ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

- **DatabricksSession**: The recommended session class for Databricks Connect. Use `DatabricksSession.builder().getOrCreate()` to create the session. ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]
- **SparkSession**: Can be used as an alternative when `DatabricksSession` is unavailable. This approach uses the `SPARK_REMOTE` environment variable for authentication. ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

```scala
// Using SparkSession as an alternative
import org.apache.spark.sql.{DataFrame, SparkSession}

val spark = SparkSession.builder().getOrCreate()
val df = spark.read.table("samples.nyctaxi.trips")
df.show(5)
```

## Best Practices

- **Drop tables before recreating**: Use `DROP TABLE IF EXISTS` to avoid errors when re-running table creation code. ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]
- **Use a schema**: Always specify the target schema (e.g., `default`) before creating tables to ensure they are placed in the correct location. ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]
- **Clean up resources**: Drop temporary tables after use to avoid cluttering the cluster with test data. ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]
- **Use descriptive table names**: Prefix test tables with identifiers like `zzz_demo_` to distinguish them from production tables. ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The client library for connecting local applications to Databricks clusters
- [DatabricksSession](/concepts/databrickssession.md) — The recommended session class for Databricks Connect
- SparkSession — The alternative session class for Databricks Connect
- DataFrame — The primary data structure for creating and manipulating tabular data
- Spark SQL — The SQL interface for querying tables on Databricks clusters
- Code Examples for Databricks Connect for Scala — Additional examples including ETL applications and visualizations

## Sources

- code-examples-for-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [code-examples-for-databricks-connect-for-scala-databricks-on-aws.md](/references/code-examples-for-databricks-connect-for-scala-databricks-on-aws-383843cd.md)

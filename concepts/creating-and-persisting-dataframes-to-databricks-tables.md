---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b8971f83f9b5955fdda7817e6fef3f2659f9d2c55b300095c0673fb9c49a5e55
  pageDirectory: concepts
  sources:
    - code-examples-for-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - creating-and-persisting-dataframes-to-databricks-tables
    - persisting DataFrames to Databricks tables and Creating
    - CAPDTDT
  citations:
    - file: code-examples-for-databricks-connect-for-scala-databricks-on-aws.md
title: Creating and persisting DataFrames to Databricks tables
description: The end-to-end workflow of creating in-memory Spark DataFrames, saving them as managed tables via saveAsTable(), querying them with Spark SQL, and cleaning up with DROP TABLE.
tags:
  - databricks
  - scala
  - etl
  - data-management
timestamp: "2026-06-18T11:00:26.444Z"
---

# Creating and persisting DataFrames to Databricks tables

**Creating and persisting DataFrames to Databricks tables** is a fundamental data engineering workflow where you construct a DataFrame in-memory (or from an existing data source) and write its contents to a managed or external table within the [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md). After persisting, the data can be queried by any workload that has access to the table — notebooks, jobs, Databricks SQL, or external tools via [Databricks Connect](/concepts/databricks-connect.md).^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

## Overview of the workflow

The typical workflow involves three steps:
1. Create or obtain a DataFrame (e.g., from a query, a file, or programmatically constructed data).
2. Write the DataFrame to a table using the DataFrame writer API.
3. (Optional) Query the persisted table and, if needed, clean up by dropping the table.^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

Databricks supports both Scala and PySpark for these operations. The following sections use Scala examples via [Databricks Connect](/concepts/databricks-connect.md), but the same pattern applies in notebooks and jobs.^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

## Creating a DataFrame in-memory

You can create a DataFrame programmatically by defining a schema and supplying data rows. In Scala, use `StructType` and `StructField` to define the schema, then pass a sequence of rows and the schema to `spark.createDataFrame`.^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

The following example creates a DataFrame of airport weather data with columns `AirportCode` (string), `Date` (date), `TempHighF` (integer), and `TempLowF` (integer):^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

```scala
import org.apache.spark.sql.types._
import java.time.LocalDate

val schema = StructType(Seq(
  StructField("AirportCode", StringType, false),
  StructField("Date", DateType, false),
  StructField("TempHighF", IntegerType, false),
  StructField("TempLowF", IntegerType, false)
))

val data = Seq(
  ("BLI", LocalDate.of(2021, 4, 3), 52, 43),
  ("BLI", LocalDate.of(2021, 4, 2), 50, 38),
  ("BLI", LocalDate.of(2021, 4, 1), 52, 41),
  ("PDX", LocalDate.of(2021, 4, 3), 64, 45),
  ("PDX", LocalDate.of(2021, 4, 2), 61, 41),
  ("PDX", LocalDate.of(2021, 4, 1), 66, 39),
  ("SEA", LocalDate.of(2021, 4, 3), 57, 43),
  ("SEA", LocalDate.of(2021, 4, 2), 54, 39),
  ("SEA", LocalDate.of(2021, 4, 1), 56, 41)
)

val temps = spark.createDataFrame(data).toDF(schema.fieldNames: _*)
```

^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

## Persisting a DataFrame to a table

To persist the DataFrame, use the `saveAsTable` method on the DataFrame writer. Before writing, you may want to drop an existing table with the same name to avoid conflicts.^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

```scala
spark.sql("USE default")
spark.sql("DROP TABLE IF EXISTS zzz_demo_temps_table")
temps.write.saveAsTable("zzz_demo_temps_table")
```

^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

The `write.saveAsTable` method creates a managed table in the specified schema (here, `default`). The table is registered in the [Metastore](/concepts/metastore.md), and the data is stored in the workspace's root bucket or the location defined by the catalog or schema.^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

## Reading a persisted table

Once persisted, you can query the table using Spark SQL or the DataFrame reader:^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

```scala
val df_temps = spark.sql("""
  SELECT * FROM zzz_demo_temps_table
  WHERE AirportCode != 'BLI' AND Date > '2021-04-01'
  GROUP BY AirportCode, Date, TempHighF, TempLowF
  ORDER BY TempHighF DESC
""")
df_temps.show()
```

^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

The result filters, groups, and orders the persisted data:^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

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

## Cleaning up

After you finish working with the table, you can delete it to free storage and [Metastore](/concepts/metastore.md) resources:^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

```scala
spark.sql("DROP TABLE zzz_demo_temps_table")
```

^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

## Using Databricks Connect for remote execution

When using [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md), the DataFrame operations execute remotely on the configured Databricks cluster. You obtain the `SparkSession` through `DatabricksSession.builder().getOrCreate()`, which automatically handles authentication and cluster connection. All `write.saveAsTable` and `spark.sql` calls run on the remote Spark driver.^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

If the `DatabricksSession` class is unavailable in your environment, you can fall back to the standard `SparkSession.builder().getOrCreate()`, provided the `SPARK_REMOTE` environment variable is set for authentication:^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

```scala
import org.apache.spark.sql.{DataFrame, SparkSession}

val spark = SparkSession.builder().getOrCreate()
val df = spark.read.table("samples.nyctaxi.trips")
df.show(5)
```

^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

## Additional considerations

- **Table naming:** Use three-level names (`catalog.schema.table`) when working with Unity Catalog. The `default` schema used in the examples is part of the `hive_metastore` catalog in legacy workspaces.^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]
- **Write modes:** By default, `saveAsTable` uses the `errorifexists` mode, which fails if the table already exists. Use `.mode("overwrite")` to replace the table, or `.mode("append")` to add rows.^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]
- **Partitioning and bucketing:** For large tables, consider adding `.partitionBy("column")` or `.bucketBy(numBuckets, "column")` before `saveAsTable` to optimize query performance.^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]
- **Reading existing tables:** Use `spark.read.table("table_name")` to load a DataFrame from an existing table without rewriting it.^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

## Related concepts

- DataFrame — The core distributed data structure in Spark
- [Databricks Connect](/concepts/databricks-connect.md) — Client library for running Spark code on remote Databricks clusters
- [Unity Catalog](/concepts/unity-catalog.md) — Data governance layer for managing tables and permissions
- [Managed tables vs External tables](/concepts/managed-vs-external-tables-in-unity-catalog.md) — Storage management differences in Databricks
- Spark SQL — SQL interface for querying DataFrames and tables
- ETL Patterns on Databricks — Common data engineering workflows

## Sources

- code-examples-for-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [code-examples-for-databricks-connect-for-scala-databricks-on-aws.md](/references/code-examples-for-databricks-connect-for-scala-databricks-on-aws-383843cd.md)

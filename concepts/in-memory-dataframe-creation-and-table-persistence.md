---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5d285b0453c6436fcec4ecea8308e045c5026fdee9b692658d7a0ddcae6a7c66
  pageDirectory: concepts
  sources:
    - code-examples-for-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - in-memory-dataframe-creation-and-table-persistence
    - table persistence and In-memory DataFrame creation
    - IDCATP
  citations:
    - file: code-examples-for-databricks-connect-for-scala-databricks-on-aws.md
title: In-memory DataFrame creation and table persistence
description: The workflow of creating a Spark DataFrame from in-memory Scala data, defining a schema with StructType, saving it as a managed table, and querying it on the remote cluster.
tags:
  - databricks
  - scala
  - dataframe
  - etl
timestamp: "2026-06-19T14:14:32.559Z"
---

# In-memory DataFrame creation and table persistence

**In-memory DataFrame creation and table persistence** is a common pattern in [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) that involves constructing a [Spark DataFrame](/concepts/spark-dataframe-evaluation-pattern.md) from programmatic data, saving it as a managed table on a Databricks cluster, querying the table, and cleaning up afterwards. This pattern is useful for prototyping, testing, and small-scale ETL tasks where data originates from application code rather than external storage. ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

## Workflow overview

The typical workflow consists of four steps:

1. **Define a schema** – Specify the column names, types, and nullability using `StructType` and `StructField`.
2. **Create an in-memory DataFrame** – Populate the schema with a sequence of row values and call `spark.createDataFrame()`.
3. **Persist as a table** – Write the DataFrame to a named table using `DataFrame.write.saveAsTable()`, optionally dropping a pre-existing table first.
4. **Query and clean up** – Run SQL statements against the table, then drop it when it is no longer needed.

The following sections walk through each step using code from the standard [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) example. ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

## Defining the schema

The schema is declared as a `StructType` containing `StructField` entries. Each field specifies a name, a Spark SQL data type, and a nullable flag. ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

```scala
import org.apache.spark.sql.types._
import java.time.LocalDate

val schema = StructType(Seq(
  StructField("AirportCode", StringType, false),
  StructField("Date", DateType, false),
  StructField("TempHighF", IntegerType, false),
  StructField("TempLowF", IntegerType, false)
))
```

## Creating the in-memory DataFrame

The data is provided as a sequence of tuples matching the schema. `spark.createDataFrame(data).toDF(schema.fieldNames: _*)` converts the sequence into a DataFrame. ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

```scala
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

## Persisting the DataFrame as a table

The DataFrame is saved to the `default` schema under a chosen table name. It is a best practice to drop any existing table with the same name before writing to avoid conflicts. The `saveAsTable` method creates a managed table on the Databricks cluster. ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

```scala
spark.sql("USE default")
spark.sql("DROP TABLE IF EXISTS zzz_demo_temps_table")
temps.write.saveAsTable("zzz_demo_temps_table")
```

## Querying and cleaning up

Once the table exists, standard SQL queries can be executed against it. After querying, the table is dropped to leave the cluster in a clean state. ^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

```scala
val df_temps = spark.sql("""
  SELECT * FROM zzz_demo_temps_table
  WHERE AirportCode != 'BLI' AND Date > '2021-04-01'
  GROUP BY AirportCode, Date, TempHighF, TempLowF
  ORDER BY TempHighF DESC
""")
df_temps.show()

// Clean up
spark.sql("DROP TABLE zzz_demo_temps_table")
```

## Related concepts

- [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) — The client library that enables remote Spark session execution.
- [Spark DataFrame](/concepts/spark-dataframe-evaluation-pattern.md) — The core distributed data structure used.
- [Managed Tables in Databricks](/concepts/managed-tables-in-databricks.md) — Tables whose data and metadata are managed by the Hive [Metastore](/concepts/metastore.md).
- In-memory data processing — Patterns for working with data that resides in application memory.

## Sources

- code-examples-for-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [code-examples-for-databricks-connect-for-scala-databricks-on-aws.md](/references/code-examples-for-databricks-connect-for-scala-databricks-on-aws-383843cd.md)

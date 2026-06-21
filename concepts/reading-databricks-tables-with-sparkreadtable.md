---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f3e78b88ede61676f4d58d6cc6629071490c1c249e37860a5b9aa94e3f052c82
  pageDirectory: concepts
  sources:
    - code-examples-for-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - reading-databricks-tables-with-sparkreadtable
    - RDTWS
  citations:
    - file: code-examples-for-databricks-connect-for-scala-databricks-on-aws.md
title: Reading Databricks tables with Spark.read.table
description: The pattern of using SparkSession.read.table() via Databricks Connect to query existing tables on a Databricks cluster and display results.
tags:
  - databricks
  - scala
  - query
timestamp: "2026-06-19T14:14:25.108Z"
---

# Reading Databricks tables with Spark.read.table

**`Spark.read.table`** is a method in Apache Spark that reads the contents of a table registered in the Hive [Metastore](/concepts/metastore.md) (or Unity Catalog) and returns a DataFrame. On Databricks, this is the primary way to load production tables for analysis or transformation, whether running in a notebook, a job, or through [Databricks Connect](/concepts/databricks-connect.md).

## Usage with Databricks Connect

When using Databricks Connect (for Scala or Python), you obtain a `SparkSession` (or `DatabricksSession`) and call `spark.read.table("catalog.schema.table")` to reference a table stored on the remote Databricks cluster. The returned DataFrame can then be transformed or shown as usual.

```scala
import com.databricks.connect.[[databrickssession|DatabricksSession]]
import org.apache.spark.sql.SparkSession

val spark = [[databrickssession|DatabricksSession]].builder().getOrCreate()
val df = spark.read.table("samples.nyctaxi.trips")
df.limit(5).show()
```

^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

### In a reusable function

You can encapsulate the read in a helper method that returns a DataFrame:

```scala
def getTaxis(spark: SparkSession): DataFrame = {
  spark.read.table("samples.nyctaxi.trips")
}
```

^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

## Best practices

- Always verify that the table exists and that you have the necessary permissions.
- Use the fully qualified table name (catalog.schema.table) to avoid ambiguity.
- When working with Databricks Connect, ensure your client is properly authenticated and the remote cluster is accessible.

## Related concepts

- [Databricks Connect](/concepts/databricks-connect.md) — Remotely connect IDEs and applications to Databricks clusters.
- SparkSession — The entry point for reading data and creating DataFrames.
- DataFrame — The primary data abstraction in Spark.

## Sources

- code-examples-for-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [code-examples-for-databricks-connect-for-scala-databricks-on-aws.md](/references/code-examples-for-databricks-connect-for-scala-databricks-on-aws-383843cd.md)

---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b57915d5292cbdd40d34975fb204d997886cd8386b32bae02a698cfbcbf33f7e
  pageDirectory: concepts
  sources:
    - limitations-with-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - create-table-as-select-workaround
    - CTASW
    - CTAS
  citations:
    - file: limitations-with-databricks-connect-for-scala-databricks-on-aws.md
title: CREATE TABLE AS SELECT Workaround
description: The CREATE TABLE AS SELECT statement is not supported in Databricks Connect for Scala; the recommended alternative is spark.sql(...).write.saveAsTable(...).
tags:
  - databricks-connect
  - sql
  - workaround
  - scala
timestamp: "2026-06-19T19:12:37.669Z"
---

# CREATE TABLE AS SELECT Workaround

The **CREATE TABLE AS SELECT Workaround** refers to the recommended alternative for the unsupported `CREATE TABLE <table-name> AS SELECT` syntax in [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md). When this syntax is unavailable, users must replace it with a two-step write operation using the DataFrame API.

## Overview

In [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) (Databricks Runtime 13.3 LTS and above), the `CREATE TABLE ... AS SELECT` (CTAS) syntax is not supported. Attempting to use this SQL statement will result in an error. The workaround involves first executing the `SELECT` query to obtain a DataFrame, then writing that DataFrame to a table using the `.write.saveAsTable()` method. ^[limitations-with-databricks-connect-for-scala-databricks-on-aws.md]

## Workaround Syntax

Instead of running:

```sql
CREATE TABLE my_table AS SELECT * FROM source_table WHERE condition = 'value'
```

Use the equivalent DataFrame API approach:

```scala
spark.sql("SELECT * FROM source_table WHERE condition = 'value'")
  .write.saveAsTable("my_table")
```

^[limitations-with-databricks-connect-for-scala-databricks-on-aws.md]

## How It Works

1. **Execute the SELECT query**: Use `spark.sql("SELECT ...")` to create a DataFrame containing the desired data.
2. **Write the DataFrame to a table**: Chain `.write.saveAsTable("table_name")` on the DataFrame to persist it as a managed table in the [Hive metastore](/concepts/built-in-hive-metastore.md).

This workaround achieves the same result as the CTAS syntax — creating a table populated with the results of a query — but uses the DataFrame write API instead of direct SQL.

## Related Concepts

- [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) — The client library that enables connecting IDEs and custom applications to Databricks compute resources.
- [Databricks Connect Limitations](/concepts/databricks-connect-limitations.md) — The full list of unsupported features, including streaming, UDFs, and RDDs.
- DataFrame Writer — The API used to persist DataFrames to tables.
- [CREATE TABLE AS SELECT (CTAS)](/concepts/create-table-as-select-ctas-for-migration.md) — The standard SQL syntax that is not available in this context.
- [Managed Tables](/concepts/managed-tables-in-databricks.md) — Tables whose data and metadata are managed by the [Metastore](/concepts/metastore.md).

## Sources

- limitations-with-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [limitations-with-databricks-connect-for-scala-databricks-on-aws.md](/references/limitations-with-databricks-connect-for-scala-databricks-on-aws-8e97ac24.md)

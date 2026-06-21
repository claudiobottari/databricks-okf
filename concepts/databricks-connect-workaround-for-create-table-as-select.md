---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ca54b06dca68a21b5691a50a62422c8b0b3467308b60c5b720826fbccf0e0338
  pageDirectory: concepts
  sources:
    - limitations-with-databricks-connect-for-python-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-workaround-for-create-table-as-select
    - DCWFCTAS
  citations:
    - file: limitations-with-databricks-connect-for-python-databricks-on-aws.md
title: Databricks Connect Workaround for CREATE TABLE AS SELECT
description: In Databricks Connect, CREATE TABLE AS SELECT is not supported; the workaround is to use spark.sql('SELECT ...').write.saveAsTable('table') instead.
tags:
  - databricks
  - workaround
  - sql
timestamp: "2026-06-19T19:12:23.587Z"
---

# Databricks Connect Workaround for CREATE TABLE AS SELECT

The **Databricks Connect Workaround for CREATE TABLE AS SELECT** refers to the alternative method required when using [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) to create a table from a query result, because the standard SQL `CREATE TABLE ... AS SELECT` syntax is not supported in this environment. ^[limitations-with-databricks-connect-for-python-databricks-on-aws.md]

## Limitation

In Databricks Connect for Python, the `CREATE TABLE <table-name> AS SELECT` statement is not available. This limitation applies across all supported Databricks Runtime versions covered by Databricks Connect. ^[limitations-with-databricks-connect-for-python-databricks-on-aws.md]

## Workaround

Instead of using the SQL `CREATE TABLE ... AS SELECT` syntax, use the DataFrame API method `write.saveAsTable()`. The recommended approach is:

1. Execute the query using `spark.sql()` to create a DataFrame.
2. Call `.write.saveAsTable("table")` on the resulting DataFrame to persist it as a table.

```python
spark.sql("SELECT ...").write.saveAsTable("table")
```

This achieves the same result as `CREATE TABLE <table-name> AS SELECT` while working within the constraints of Databricks Connect. ^[limitations-with-databricks-connect-for-python-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) — The client library that enables connecting IDEs and custom applications to Databricks clusters
- [Databricks Connect Limitations](/concepts/databricks-connect-limitations.md) — Full list of unsupported features in Databricks Connect
- saveAsTable — The DataFrame API method used to persist query results as tables
- Spark DataFrame API — The programmatic interface for working with structured data in Spark

## Sources

- limitations-with-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [limitations-with-databricks-connect-for-python-databricks-on-aws.md](/references/limitations-with-databricks-connect-for-python-databricks-on-aws-334fca41.md)

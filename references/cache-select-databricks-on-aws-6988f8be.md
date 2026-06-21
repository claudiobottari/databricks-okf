---
title: CACHE SELECT | Databricks on AWS
source: https://docs.databricks.com/aws/en/sql/language-manual/delta-cache
ingestedAt: "2026-06-18T08:18:39.202Z"
---

Caches the data accessed by the specified simple `SELECT` query in the [disk cache](https://docs.databricks.com/aws/en/optimizations/disk-cache). You can choose a subset of columns to be cached by providing a list of column names and choose a subset of rows by providing a predicate. This enables subsequent queries to avoid scanning the original files as much as possible. This construct is applicable only to Delta tables and Parquet tables. Views are also supported, but the expanded queries are restricted to the simple queries, as described above.

    CACHE SELECT column_name [, ...] FROM table_name [ WHERE boolean_expression ]

---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 27742f341101eee3a071d364e864a41b6043b205b0584e431c504239e084631d
  pageDirectory: concepts
  sources:
    - archival-support-in-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - early-failure-and-error-reporting-for-archived-queries
    - error reporting for archived queries and Early failure
    - EFAERFAQ
  citations:
    - file: archival-support-in-databricks-databricks-on-aws.md
title: Early failure and error reporting for archived queries
description: Archival support enables queries that need archived files to fail early with descriptive errors, reducing wasted compute.
tags:
  - databricks
  - delta-lake
  - archival
  - error-handling
timestamp: "2026-06-19T22:07:54.668Z"
---

# Early failure and error reporting for archived queries

**Early failure and error reporting for archived queries** is a feature of [archival support](/concepts/archival-support-in-databricks.md) for [Delta Lake](/concepts/delta-lake.md) tables that ensures queries requiring access to archived files fail quickly and provide clear error messages, enabling users to adapt and re-run queries efficiently.^[archival-support-in-databricks-databricks-on-aws.md]

## Overview

When archival support is configured on a Delta table, Databricks optimizes queries to avoid scanning archived files whenever possible. For queries that cannot return correct results without accessing archived data, the system provides two key behaviors: early failure and informative error messages.^[archival-support-in-databricks-databricks-on-aws.md]

Configuring archival support for Delta Lake ensures the following:

- Queries fail early if they attempt to access archived files, reducing wasted compute and allowing users to adapt and re-run queries quickly.
- Error messages inform users that a query has failed because it attempted to access archived files.^[archival-support-in-databricks-databricks-on-aws.md]

## Importance

Without archival support, operations against Delta tables might break because data files or transaction log files have moved to archived locations and become unavailable when queried. Archival support introduces optimizations to avoid querying archived data when possible, and adds new syntax to identify files that must be restored from archival storage to complete queries.^[archival-support-in-databricks-databricks-on-aws.md]

Databricks never returns results for queries that require archived files to return the correct result.^[archival-support-in-databricks-databricks-on-aws.md]

## The LIMIT query error

A specific error case occurs with `LIMIT` queries. If you get the error `Not enough files to satisfy LIMIT`, your table does not have enough data rows in unarchived files to satisfy the number of records specified by `LIMIT`. Lower the `LIMIT` clause to find enough unarchived rows to meet the specified limit.^[archival-support-in-databricks-databricks-on-aws.md]

`LIMIT` queries on tables with archival support enabled do not trigger How does Databricks sample for restored data?|sampling for restored data. If a table's data is restored, most queries succeed when querying restored data, but a `LIMIT` query returns a `DELTA_ARCHIVED_FILES_IN_LIMIT` error.^[archival-support-in-databricks-databricks-on-aws.md]

## Identifying files to restore

Users can generate a report of files that must be restored using the `SHOW ARCHIVED FILES` syntax:

```sql
SHOW ARCHIVED FILES FOR table_name [ WHERE predicate ];
```

This operation returns URIs for archived files as a Spark DataFrame. After restoring the necessary files in your cloud provider storage, you can query your table. Archival support automatically recognizes the restored files.^[archival-support-in-databricks-databricks-on-aws.md]

## Related concepts

- [Archival Support in Databricks](/concepts/archival-support-in-databricks.md)
- [Delta Lake](/concepts/delta-lake.md)
- [SHOW ARCHIVED FILES](/concepts/show-archived-files-syntax.md)
- Restore archived files
- How does Databricks sample for restored data?

## Sources

- archival-support-in-databricks-databricks-on-aws.md

# Citations

1. [archival-support-in-databricks-databricks-on-aws.md](/references/archival-support-in-databricks-databricks-on-aws-d64d2061.md)

---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 41e0297d56391086c3a87b55543e16991357536da79fe1efe498e8d910aa1a19
  pageDirectory: concepts
  sources:
    - archival-support-in-databricks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - early-failure-on-archived-queries
    - EFOAQ
  citations:
    - file: archival-support-in-databricks-databricks-on-aws.md
title: Early Failure on Archived Queries
description: An optimization where queries that must scan archived files fail early with clear error messages instead of running into missing-data issues, reducing wasted compute.
tags:
  - databricks
  - archival
  - error-handling
  - performance
timestamp: "2026-06-19T14:03:14.178Z"
---

# Early Failure on Archived Queries

**Early Failure on Archived Queries** is a feature of [Archival Support in Databricks](/concepts/archival-support-in-databricks.md) that causes queries requiring access to archived files to fail immediately at the start of execution, rather than after scanning through available data. This behavior reduces wasted compute and allows users to quickly identify when they need to restore archived files. ^[archival-support-in-databricks-databricks-on-aws.md]

## Overview

When [archival support](/concepts/delta-lake-archival-support.md) is configured for a [Delta table](/concepts/delta-lake-table.md), Databricks tracks which files have been moved to archival storage tiers such as S3 Glacier Deep Archive or Glacier Flexible Retrieval. For any query that must scan these archived files to produce correct results, Databricks fails early instead of attempting to read the inaccessible data. ^[archival-support-in-databricks-databricks-on-aws.md]

This early failure mechanism ensures that Databricks never returns results for queries that require archived files to return the correct result. ^[archival-support-in-databricks-databricks-on-aws.md]

## Error Messages

When a query fails due to attempting to access archived files, the error message informs users that the query has failed because it attempted to access archived files. ^[archival-support-in-databricks-databricks-on-aws.md]

### LIMIT Queries

A specific error, `DELTA_ARCHIVED_FILES_IN_LIMIT`, occurs for `LIMIT` queries on tables with archival support enabled:

```
Not enough files to satisfy LIMIT
```

This error indicates the table does not have enough data rows in unarchived files to satisfy the number of records specified by `LIMIT`. Users should lower the `LIMIT` clause to find enough unarchived rows to meet the specified limit. ^[archival-support-in-databricks-databricks-on-aws.md]

## How Early Failure Works

For queries that must scan archived files to generate correct results, configuring archival support for Delta Lake ensures: ^[archival-support-in-databricks-databricks-on-aws.md]

1. **Queries fail early** if they attempt to access archived files, reducing wasted compute and allowing users to adapt and re-run queries quickly.
2. **Error messages inform users** that a query has failed because it attempted to access archived files.

## Identifying Archived Files

Users can generate a report of files that must be restored using the `SHOW ARCHIVED FILES` syntax:

```sql
SHOW ARCHIVED FILES FOR table_name [ WHERE predicate ];
```

This operation returns URIs for archived files as a Spark DataFrame, enabling users to identify exactly which files require restoration before re-running the query. ^[archival-support-in-databricks-databricks-on-aws.md]

## Related Concepts

- [Archival Support in Databricks](/concepts/archival-support-in-databricks.md) — The overall feature for lifecycle policy integration with Delta tables
- [Delta table](/concepts/delta-lake-table.md) — The table format that supports archival configuration
- S3 Glacier storage tiers — Cloud storage tiers compatible with archival support
- [Delta transaction log](/concepts/delta-transaction-log.md) — Files that must never be archived to maintain table accessibility

## Sources

- archival-support-in-databricks-databricks-on-aws.md

# Citations

1. [archival-support-in-databricks-databricks-on-aws.md](/references/archival-support-in-databricks-databricks-on-aws-d64d2061.md)

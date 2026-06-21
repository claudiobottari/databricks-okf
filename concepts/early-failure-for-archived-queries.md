---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c00c6bc23ccf908aafa7bb847a1974e1e468fc246dd25c10697599089e8dcf80
  pageDirectory: concepts
  sources:
    - archival-support-in-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - early-failure-for-archived-queries
    - EFFAQ
  citations:
    - file: archival-support-in-databricks-databricks-on-aws.md
title: Early failure for archived queries
description: A behavior where queries requiring archived data fail immediately with clear error messages, avoiding wasted compute and enabling rapid recovery via file restoration.
tags:
  - delta-lake
  - query-execution
  - error-handling
timestamp: "2026-06-18T14:27:04.925Z"
---

# Early Failure for Archived Queries

**Early failure for archived queries** is a feature of [Archival Support in Databricks](/concepts/archival-support-in-databricks.md) that causes queries requiring access to archived files to fail immediately, rather than attempting to scan unavailable data and potentially wasting compute resources. ^[archival-support-in-databricks-databricks-on-aws.md]

## Overview

When archival support is enabled for a [Delta table](/concepts/delta-lake-table.md), Databricks tracks which data files have been moved to archived cloud storage, such as S3 Glacier Deep Archive or Glacier Flexible Retrieval. For queries that must scan these archived files to produce correct results, Databricks fails the query early and returns a clear error message explaining the failure. ^[archival-support-in-databricks-databricks-on-aws.md]

Databricks never returns results for queries that require archived files to return the correct result. This ensures data integrity and prevents users from receiving incomplete or misleading query responses. ^[archival-support-in-databricks-databricks-on-aws.md]

## Benefits

Early failure provides two primary advantages:

- **Reduced wasted compute**: Queries terminate quickly rather than hanging or timing out while attempting to access unavailable archived files. ^[archival-support-in-databricks-databricks-on-aws.md]
- **Clear error messaging**: Users receive informative error messages explaining that the query failed because it attempted to access archived files, allowing them to take corrective action. ^[archival-support-in-databricks-databricks-on-aws.md]

## Error Resolution

### Identifying Archived Files

When a query fails due to archived files, users can generate a report of which files need restoration using the `SHOW ARCHIVED FILES` syntax:

```sql
SHOW ARCHIVED FILES FOR table_name [ WHERE predicate ];
```

This operation returns URIs for archived files as a Spark DataFrame. ^[archival-support-in-databricks-databricks-on-aws.md]

### LIMIT Queries

If you receive the error `Not enough files to satisfy LIMIT`, the table does not have enough data rows in unarchived files to satisfy the number of records specified by `LIMIT`. Lowering the `LIMIT` clause can allow the query to succeed by finding enough unarchived rows. ^[archival-support-in-databricks-databricks-on-aws.md]

## Query Types That Succeed Without Archived Data

Archival support only allows queries that can be answered correctly without touching archived files. These include:

- Queries that scan metadata only
- Queries with filters that do not require scanning any archived files

^[archival-support-in-databricks-databricks-on-aws.md]

## Supported Query Optimizations

Databricks optimizes the following queries against Delta tables with archival support enabled. Queries that must scan archived files for any reason will fail early.

## Related Concepts

- [Archival Support in Databricks](/concepts/archival-support-in-databricks.md)
- [Delta Lake](/concepts/delta-lake.md)
- [SHOW ARCHIVED FILES](/concepts/show-archived-files-syntax.md)
- Archived File Restoration
- Lifecycle Management Policies
- S3 Glacier Storage Classes

## Sources

- archival-support-in-databricks-databricks-on-aws.md

# Citations

1. [archival-support-in-databricks-databricks-on-aws.md](/references/archival-support-in-databricks-databricks-on-aws-d64d2061.md)

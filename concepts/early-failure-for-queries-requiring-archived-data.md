---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 37ea590b526f2d1d2cf003d3fdbf459598837cb649a71ec25195e6c9190accd3
  pageDirectory: concepts
  sources:
    - archival-support-in-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - early-failure-for-queries-requiring-archived-data
    - EFFQRAD
  citations:
    - file: archival-support-in-databricks-databricks-on-aws.md
title: Early Failure for Queries Requiring Archived Data
description: A Databricks optimization that causes queries needing archived files to fail immediately with clear error messages, rather than waiting for unavailable data.
tags:
  - archival
  - error-handling
  - query-optimization
  - databricks
timestamp: "2026-06-19T09:02:16.080Z"
---

# Early Failure for Queries Requiring Archived Data

**Early Failure for Queries Requiring Archived Data** refers to the behavior of [Delta Lake](/concepts/delta-lake.md) tables with [archival support](/concepts/delta-lake-archival-support.md) enabled: any query that cannot be answered correctly without scanning archived files is terminated immediately, rather than attempting to read unavailable data and potentially returning incorrect results or hanging. ^[archival-support-in-databricks-databricks-on-aws.md]

## Overview

When archival support is configured on a Delta table via the `delta.timeUntilArchived` table property, Databricks treats files older than the specified interval as archived. Queries that require data from those archived files to produce a correct result are failed early. This early-failure mechanism reduces wasted compute time and lets users quickly identify that they need to restore files or adjust their query. ^[archival-support-in-databricks-databricks-on-aws.md]

Databricks never returns results for queries that require archived files. Only queries that can be answered without touching archived files succeed—those that either query only metadata or have filters that avoid scanning archived data. ^[archival-support-in-databricks-databricks-on-aws.md]

## Error Messages

When a query fails due to archived data, the error message informs the user that the query attempted to access archived files. A specific error condition also exists for `LIMIT` clauses:

- If you receive the error `Not enough files to satisfy LIMIT`, the table does not have enough non-archived data rows to satisfy the specified `LIMIT`. The solution is to reduce the `LIMIT` value so that enough unarchived rows exist to meet the requested count. ^[archival-support-in-databricks-databricks-on-aws.md]

## Related Concepts

- [Archival Support in Databricks](/concepts/archival-support-in-databricks.md) – The parent feature that enables early failure and other optimizations.
- [SHOW ARCHIVED FILES](/concepts/show-archived-files-syntax.md) – A command to list files that must be restored to complete a query.
- [delta.timeUntilArchived](/concepts/deltatimeuntilarchived.md) – The table property that specifies the archival interval.
- [Delta Lake](/concepts/delta-lake.md) – The storage engine underlying this feature.

## Sources

- archival-support-in-databricks-databricks-on-aws.md

# Citations

1. [archival-support-in-databricks-databricks-on-aws.md](/references/archival-support-in-databricks-databricks-on-aws-d64d2061.md)

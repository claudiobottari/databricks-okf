---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 22d663974316c3287d949f1c7993f7fdb78f15d0422143331f727ef35c29567c
  pageDirectory: concepts
  sources:
    - archival-support-in-databricks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mergeupdatedelete-restrictions-on-archived-delta-data
    - MROADD
  citations:
    - file: archival-support-in-databricks-databricks-on-aws.md
title: Merge/Update/Delete restrictions on archived Delta data
description: MERGE, UPDATE, and DELETE operations fail if they impact data in archived files; files must be restored first.
tags:
  - delta-lake
  - archival
  - dml
timestamp: "2026-06-19T17:35:05.301Z"
---

# Merge/Update/Delete restrictions on archived Delta data

**Merge/Update/Delete restrictions on archived Delta data** refers to the limitation that `MERGE`, `UPDATE`, and `DELETE` operations fail when they would impact data stored in archived files within a [Delta Lake](/concepts/delta-lake.md) table that has archival support enabled.

## Overview

When archival support is enabled on a Delta table, the system prevents write operations that would modify data in archived files. This restriction exists because archived files reside in cost-optimized storage tiers (such as S3 Glacier Deep Archive or Glacier Flexible Retrieval) that do not support the random access and modification required for these operations. ^[archival-support-in-databricks-databricks-on-aws.md]

## Behavior

Any `MERGE`, `UPDATE`, or `DELETE` operation that would impact data in archived files fails with an error. Databricks never returns results for queries that require archived files to produce the correct result. ^[archival-support-in-databricks-databricks-on-aws.md]

## Required action: Restore archived files

To run `MERGE`, `UPDATE`, or `DELETE` operations on data that has been archived, you must first restore the affected files to a storage tier that supports fast retrieval. ^[archival-support-in-databricks-databricks-on-aws.md]

The recommended workflow is:

1. Use the `SHOW ARCHIVED FILES` syntax to identify which files must be restored for the operation you intend to run. ^[archival-support-in-databricks-databricks-on-aws.md]

   ```sql
   SHOW ARCHIVED FILES FOR table_name [ WHERE predicate ];
   ```

2. Restore the identified files using your cloud provider's restore APIs. For AWS, use the S3 restore object APIs to restore files to a fast retrieval storage tier. ^[archival-support-in-databricks-databricks-on-aws.md]

3. After restoration is complete, the system automatically recognizes the restored files, and the write operation can proceed. ^[archival-support-in-databricks-databricks-on-aws.md]

## How Databricks detects restored files

When preparing a scan over a table with archival support enabled, Databricks samples files older than the specified retention period to determine whether files have been restored. If the sampled files are available, Databricks assumes all files for the query have been restored and processes the query, including data from the previously archived files. ^[archival-support-in-databricks-databricks-on-aws.md]

## Limitations

- `REORG TABLE APPLY PURGE` makes a best-effort attempt on disk-resident data but cannot delete archived deletion vector files. ^[archival-support-in-databricks-databricks-on-aws.md]
- `DROP COLUMN` is not supported on tables with archived files. ^[archival-support-in-databricks-databricks-on-aws.md]

## Related Concepts

- [Archival Support in Databricks](/concepts/archival-support-in-databricks.md) — The feature that enables cloud-based lifecycle policies for Delta tables.
- [Show archived files](/concepts/show-archived-files-syntax.md) — Syntax for identifying which files must be restored.
- [Delta Lake](/concepts/delta-lake.md) — The storage layer underlying these restrictions.
- S3 Glacier Deep Archive — A common archival storage tier affected by these restrictions.
- S3 Glacier Flexible Retrieval — Another archival storage tier for Delta data.

## Sources

- archival-support-in-databricks-databricks-on-aws.md

# Citations

1. [archival-support-in-databricks-databricks-on-aws.md](/references/archival-support-in-databricks-databricks-on-aws-d64d2061.md)

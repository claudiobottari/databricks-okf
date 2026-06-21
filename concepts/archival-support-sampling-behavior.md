---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 338aafddf018ffb98510e425ee2a76185c937540d3d74e0c535657c658c1d47f
  pageDirectory: concepts
  sources:
    - archival-support-in-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - archival-support-sampling-behavior
    - ASSB
  citations:
    - file: archival-support-in-databricks-databricks-on-aws.md
title: Archival support sampling behavior
description: The mechanism by which Databricks samples files older than the retention period to determine if restored data is available before scanning a table.
tags:
  - delta-lake
  - archival
  - query-optimization
timestamp: "2026-06-18T14:26:55.171Z"
---

# Archival Support Sampling Behavior

**Archival support sampling behavior** refers to the mechanism by which Databricks determines whether previously archived files have been restored from cold storage before allowing a query to proceed against a Delta table with archival support enabled.

## How Sampling Works

When Databricks prepares a scan over a table with archival support enabled, it samples files older than the specified retention period to determine whether those files have been restored from archival storage. If the sampling results indicate that the presumed-archived files have been restored, Databricks assumes that all files for the query have been restored and proceeds with the query. The results include data from the previously archived files. ^[archival-support-in-databricks-databricks-on-aws.md]

This sampling process is separate from the cloud provider's own lifecycle policies. Setting `delta.timeUntilArchived` on a Delta table tells Databricks to ignore files older than that threshold, but it does not create or alter the underlying cloud lifecycle policies. ^[archival-support-in-databricks-databricks-on-aws.md]

## When Sampling Applies

Sampling may not apply to all queries. Specifically, `LIMIT` queries on tables with archival support enabled do not trigger sampling for restored data. If a table's data is restored, most queries succeed when querying restored data, but a `LIMIT` query returns a `DELTA_ARCHIVED_FILES_IN_LIMIT` error. ^[archival-support-in-databricks-databricks-on-aws.md]

## Sampling and Restored Data

After restoring archived files using your cloud provider's APIs (such as the S3 restore object API), archival support automatically recognizes the restored files. Databricks checks for restored data through its sampling mechanism when preparing scans. ^[archival-support-in-databricks-databricks-on-aws.md]

## Relationship to `SHOW ARCHIVED FILES`

The `SHOW ARCHIVED FILES` operation provides information about which files must be restored to complete a given query. During this operation, Delta Lake only has access to the data statistics contained in the transaction log—specifically minimum values, maximum values, null counts, and the total number of records, collected on the first 32 columns. ^[archival-support-in-databricks-databricks-on-aws.md]

## Best Practices

To minimize the number of files that must be restored, provide predicates that include fields on which data is partitioned, Z-ordered, or clustered. This reduces the set of files that the sampling mechanism considers. ^[archival-support-in-databricks-databricks-on-aws.md]

## Related Concepts

- [Archival Support in Databricks](/concepts/archival-support-in-databricks.md) — The overall feature enabling cloud-based lifecycle policies on Delta tables
- [Delta timeUntilArchived](/concepts/deltatimeuntilarchived.md) — The table property that sets the archival threshold
- Restore archived files — The process of restoring files from cold storage
- [Show archived files](/concepts/show-archived-files-syntax.md) — Syntax for identifying files that require restoration
- Lifecycle management policies — Cloud storage policies that govern file archiving

## Sources

- archival-support-in-databricks-databricks-on-aws.md

# Citations

1. [archival-support-in-databricks-databricks-on-aws.md](/references/archival-support-in-databricks-databricks-on-aws-d64d2061.md)

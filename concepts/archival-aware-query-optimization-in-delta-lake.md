---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 40a5d5b9faa202e3c08eba55a59143fc3c864db84693bfe1f80464658c733851
  pageDirectory: concepts
  sources:
    - archival-support-in-databricks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - archival-aware-query-optimization-in-delta-lake
    - AQOIDL
  citations:
    - file: archival-support-in-databricks-databricks-on-aws.md
title: Archival-aware query optimization in Delta Lake
description: Optimizations that allow queries to succeed without touching archived files by using metadata-only queries or filters that avoid archived data.
tags:
  - delta-lake
  - query-optimization
  - archival
timestamp: "2026-06-19T17:34:58.977Z"
---

# Archival-aware query optimization in Delta Lake

**Archival-aware query optimization in Delta Lake** is a feature in Databricks that enables Delta tables to work correctly with cloud-based lifecycle policies that move older data files to archival storage tiers. When enabled, the query engine can answer certain queries without touching archived files, while failing early and with clear error messages for queries that require archived data.

## Overview

Archival support in Databricks allows you to use cloud-based lifecycle policies on cloud object storage containing Delta tables. Enabling archival support on a [Delta Lake Table](/concepts/delta-lake-table.md) tells Databricks to ignore files that are older than the specified period in the table. ^[archival-support-in-databricks-databricks-on-aws.md]

Without archival support, operations against Delta tables might break because data files or transaction log files have moved to archived locations and are unavailable when queried. Archival support introduces optimizations to avoid querying archived data when possible, and adds new syntax to identify files that must be restored from archival storage to complete queries. ^[archival-support-in-databricks-databricks-on-aws.md]

This feature is in Public Preview for Databricks Runtime 13.3 LTS and above. ^[archival-support-in-databricks-databricks-on-aws.md]

## Requirements

Archival support requires S3 Glacier Deep Archive or Glacier Flexible Retrieval. Amazon S3 Glacier Instant Retrieval does not require configuring archival support, though Databricks recommends using views to restrict queries against tables stored in Glacier Instant Retrieval with lifecycle policies configured. ^[archival-support-in-databricks-databricks-on-aws.md]

Amazon S3 Intelligent-Tiering optional asynchronous archive access tiers is not compatible with archival support because it archives based on access time rather than file creation time. ^[archival-support-in-databricks-databricks-on-aws.md]

## How query optimization works

Archival support only allows queries that can be answered correctly without touching archived files. These queries include those that either query metadata only, or have filters that do not require scanning any archived files. All queries that require data in archived files fail. ^[archival-support-in-databricks-databricks-on-aws.md]

Databricks never returns results for queries that require archived files to return the correct result. ^[archival-support-in-databricks-databricks-on-aws.md]

### Early failure and error messages

For queries that must scan archived files to generate correct results, configuring archival support ensures:

- Queries fail early if they attempt to access archived files, reducing wasted compute and allowing users to adapt and re-run queries quickly.
- Error messages inform users that a query has failed because it attempted to access archived files.

If you get the error `Not enough files to satisfy LIMIT`, your table does not have enough data rows in unarchived files to satisfy the number of records specified by `LIMIT`. Lower the `LIMIT` clause to find enough unarchived rows. ^[archival-support-in-databricks-databricks-on-aws.md]

## Enabling archival support

You enable archival support for Delta tables by manually specifying the archival interval configured in the underlying cloud lifecycle management policy:

```sql
ALTER TABLE <table_name> SET TBLPROPERTIES(delta.timeUntilArchived = 'X days');
```

Setting a `timeUntilArchived` time tells Databricks to ignore files in your [Delta Lake Table](/concepts/delta-lake-table.md) that are older than the specified time period. This setting is separate from your cloud account's lifecycle policies — changes to one do not affect the other. If you update the lifecycle policy in your cloud account, you must also update the archival setting on your [Delta Lake Table](/concepts/delta-lake-table.md). ^[archival-support-in-databricks-databricks-on-aws.md]

If you enable this setting without lifecycle policies set for your cloud object storage, archival support allows queries to succeed, and results include data from the files marked for archival. ^[archival-support-in-databricks-databricks-on-aws.md]

Your cloud lifecycle policy must not archive the Delta transaction log (`_delta_log/` directory). ^[archival-support-in-databricks-databricks-on-aws.md]

## Identifying archived files

To identify files that must be restored to complete a given query, use `SHOW ARCHIVED FILES`:

```sql
SHOW ARCHIVED FILES FOR table_name [ WHERE predicate ];
```

This operation returns URIs for archived files as a Spark DataFrame. The files returned include all archived files that must be read to determine whether or not records fulfilling a predicate exist in the file. Databricks recommends providing predicates that include fields on which data is partitioned, z-ordered, or clustered to reduce the number of files that must be restored. ^[archival-support-in-databricks-databricks-on-aws.md]

## Restoring archived files

After identifying files using `SHOW ARCHIVED FILES`, use the S3 restore object APIs to restore your files to a fast retrieval storage tier. After restoring the files, you can query your table — archival support automatically recognizes the restored files. ^[archival-support-in-databricks-databricks-on-aws.md]

## Sampling for restored data

When Databricks prepares a scan over a table with archival support enabled, it samples files older than the specified retention period required by the query to determine whether or not files have been restored. If the results indicate the sampled files presumed to be archived have been restored, Databricks assumes all files for the query have been restored and the query processes. Results include data from the files marked for archival. ^[archival-support-in-databricks-databricks-on-aws.md]

## Limitations

The following limitations exist:

- Archival support applies only to data files. If any files in the Delta transaction log (`_delta_log/` directory) are moved to an archived storage tier, the table becomes entirely inaccessible and all queries against the table fail.
- No support exists for lifecycle management policies that are not based on file creation time, including access-time-based policies and tag-based policies.
- You cannot use `DROP COLUMN` on a table with archived files.
- `REORG TABLE APPLY PURGE` makes a best-effort attempt, but only works on deletion vector files and referenced data files that are not archived.
- Extending the lifecycle management transition rule results in unexpected behavior.
- `LIMIT` queries on tables with archival support enabled do not trigger sampling for restored data. If a table's data is restored, most queries succeed when querying restored data, but a `LIMIT` query returns a `DELTA_ARCHIVED_FILES_IN_LIMIT` error.

^[archival-support-in-databricks-databricks-on-aws.md]

## Related concepts

- [Delta Lake](/concepts/delta-lake.md) — The open-source storage layer that provides ACID transactions and scalable metadata handling.
- [Delta transaction log](/concepts/delta-transaction-log.md) — The `_delta_log/` directory that must not be archived.
- Cloud lifecycle policies — Cloud provider mechanisms for transitioning data to archival storage tiers.
- [Data skipping in Delta Lake](/concepts/z-ordering-delta-lake.md) — Optimization technique that reduces the number of files scanned during queries.
- [Z-ordering in Delta Lake](/concepts/z-ordering-delta-lake.md) — Data layout optimization that improves file pruning for filtered queries.

## Sources

- archival-support-in-databricks-databricks-on-aws.md

# Citations

1. [archival-support-in-databricks-databricks-on-aws.md](/references/archival-support-in-databricks-databricks-on-aws-d64d2061.md)

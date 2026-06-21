---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2e518482f1966b8e3d562a97edb4f566b7d12ef53c964890b48fcc0c51cadcde
  pageDirectory: concepts
  sources:
    - archival-support-in-databricks-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - archival-support-for-delta-tables
    - ASFDT
    - Archival Support in Delta Lake
  citations:
    - file: archival-support-in-databricks-databricks-on-aws.md
title: Archival support for Delta tables
description: A Databricks feature enabling Delta tables to coexist with cloud object lifecycle policies by ignoring archived files during queries.
tags:
  - databricks
  - delta-lake
  - archival
  - optimization
timestamp: "2026-06-19T22:07:35.462Z"
---

# Archival support for Delta tables

**Archival support for Delta tables** is a Databricks feature that enables cloud-based lifecycle policies on object storage containing Delta tables. When enabled, Databricks ignores files older than a specified period, allowing queries that can be answered without accessing archived files to succeed while preventing queries that require archived data from returning incorrect results. ^[archival-support-in-databricks-databricks-on-aws.md]

## Overview

Archival support is in Public Preview for Databricks Runtime 13.3 LTS and above. It works with [Delta Lake](/concepts/delta-lake.md) tables stored on Amazon S3 using S3 Glacier Deep Archive or Glacier Flexible Retrieval storage tiers. ^[archival-support-in-databricks-databricks-on-aws.md]

S3 Glacier Instant Retrieval does not require configuring archival support, though Databricks recommends using views to restrict queries against tables stored in this tier with lifecycle policies configured. S3 Intelligent-Tiering optional asynchronous archive access tiers are not compatible because they archive based on access time rather than file creation time. ^[archival-support-in-databricks-databricks-on-aws.md]

## Why enable archival support?

Without archival support, operations against Delta tables may break when data files or transaction log files move to archived locations and become unavailable. Archival support introduces optimizations to avoid querying archived data when possible and adds syntax to identify files that must be restored. ^[archival-support-in-databricks-databricks-on-aws.md]

Enabling archival support only allows queries that can be answered correctly without touching archived files. These include queries that query metadata only or have filters that do not require scanning any archived files. All queries that require data in archived files fail. Databricks never returns results for queries that require archived files to return the correct result. ^[archival-support-in-databricks-databricks-on-aws.md]

## Enabling archival support

Enable archival support by setting the `delta.timeUntilArchived` table property to match the archival interval configured in your cloud lifecycle management policy:

```sql
ALTER TABLE <table_name> SET TBLPROPERTIES(delta.timeUntilArchived = 'X days');
```

^[archival-support-in-databricks-databricks-on-aws.md]

Setting this property tells Databricks to ignore files older than the specified period. This setting is separate from your cloud account's lifecycle policies — changes to one do not affect the other. If you update the lifecycle policy, you must also update the table property. ^[archival-support-in-databricks-databricks-on-aws.md]

If you enable this setting without lifecycle policies configured, queries succeed and include data from files marked for archival. ^[archival-support-in-databricks-databricks-on-aws.md]

## Query behavior

For queries that must scan archived files, configuring archival support ensures early failure with informative error messages, reducing wasted compute. If you encounter the error `Not enough files to satisfy LIMIT`, your table does not have enough unarchived rows to satisfy the specified `LIMIT` clause. ^[archival-support-in-databricks-databricks-on-aws.md]

## Identifying archived files

Use `SHOW ARCHIVED FILES` to identify files that must be restored to complete a given query:

```sql
SHOW ARCHIVED FILES FOR table_name [ WHERE predicate ];
```

This returns URIs for archived files as a Spark DataFrame. During this operation, Delta Lake only has access to data statistics from the transaction log — minimum values, maximum values, null counts, and total record counts for the first 32 columns. Databricks recommends providing predicates on partitioned, z-ordered, or clustered fields to reduce the number of files that must be restored. ^[archival-support-in-databricks-databricks-on-aws.md]

## Restoring archived files

After identifying files with `SHOW ARCHIVED FILES`, use the S3 restore object APIs to restore files to a fast retrieval storage tier. Archival support automatically recognizes restored files. ^[archival-support-in-databricks-databricks-on-aws.md]

## Updating or deleting archived data

`MERGE`, `UPDATE`, or `DELETE` operations fail if they impact data in archived files. You must restore data to a storage tier supporting fast retrieval before running these operations. ^[archival-support-in-databricks-databricks-on-aws.md]

## Sampling for restored data

When Databricks prepares a scan over a table with archival support enabled, it samples files older than the specified retention period to determine whether files have been restored. If sampled files presumed to be archived have been restored, Databricks assumes all files for the query have been restored and processes the query, including data from the restored files. ^[archival-support-in-databricks-databricks-on-aws.md]

## Limitations

- Archival support applies only to data files. If any files in the `_delta_log/` directory are archived, the table becomes entirely inaccessible. Configure your lifecycle policy to exclude this path. ^[archival-support-in-databricks-databricks-on-aws.md]
- No support exists for lifecycle policies not based on file creation time, including access-time-based and tag-based policies. ^[archival-support-in-databricks-databricks-on-aws.md]
- `DROP COLUMN` cannot be used on a table with archived files. ^[archival-support-in-databricks-databricks-on-aws.md]
- `REORG TABLE APPLY PURGE` makes a best-effort attempt but cannot delete archived deletion vector files. ^[archival-support-in-databricks-databricks-on-aws.md]
- Extending the lifecycle management transition rule can lead to unexpected behavior. ^[archival-support-in-databricks-databricks-on-aws.md]
- `LIMIT` queries do not trigger sampling for restored data and return a `DELTA_ARCHIVED_FILES_IN_LIMIT` error if data is restored. ^[archival-support-in-databricks-databricks-on-aws.md]

## Changing the lifecycle management transition rule

If you change the time interval for your cloud lifecycle management transition rule, update `delta.timeUntilArchived` to the same interval. Shortening the interval (less time before archival) works normally after updating the property. ^[archival-support-in-databricks-databricks-on-aws.md]

### Extending the transition rule

Extending the interval (adding more time before archival) can lead to errors because cloud providers do not automatically restore files when retention policies change. Never set `delta.timeUntilArchived` to a value greater than the actual age of the most recently archived data. ^[archival-support-in-databricks-databricks-on-aws.md]

During the lag period between old and new archival thresholds, you can either leave the setting at the old threshold until enough time passes for all files to be archived, or update the setting daily to reflect the current interval. ^[archival-support-in-databricks-databricks-on-aws.md]

## Related concepts

- [Delta Lake](/concepts/delta-lake.md) — The storage layer underlying Delta tables
- Amazon S3 lifecycle policies — Cloud storage policies for archiving data
- [Delta transaction log](/concepts/delta-transaction-log.md) — The `_delta_log/` directory that must not be archived
- Table properties — Configuration options for Delta tables
- Data archiving strategies — Broader approaches to managing cold data

## Sources

- archival-support-in-databricks-databricks-on-aws.md

# Citations

1. [archival-support-in-databricks-databricks-on-aws.md](/references/archival-support-in-databricks-databricks-on-aws-d64d2061.md)

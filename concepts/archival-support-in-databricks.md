---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ea1e6779d5ad6f295cc1bed5161341f16f2f78415e6ce16ea497572457b44779
  pageDirectory: concepts
  sources:
    - archival-support-in-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - archival-support-in-databricks
    - ASID
  citations:
    - file: archival-support-in-databricks-databricks-on-aws.md
title: Archival Support in Databricks
description: A Databricks feature that enables cloud-based lifecycle policies on Delta tables, allowing queries to safely coexist with archived cloud object storage data.
tags:
  - databricks
  - delta-lake
  - archival
  - cloud-storage
timestamp: "2026-06-19T09:01:17.357Z"
---

# Archival Support in Databricks

**Archival Support in Databricks** is a Public Preview feature (Databricks Runtime 13.3 LTS and above) that enables Delta tables to work with cloud-based lifecycle policies on object storage. When enabled, Databricks treats files older than a configurable interval as archived, skipping them during query execution unless they have been restored.^[archival-support-in-databricks-databricks-on-aws.md]

## Overview

Without archival support, queries against Delta tables may fail when underlying data files or transaction log files have been transitioned to an archived storage tier by a cloud lifecycle policy. Archival support introduces optimizations that avoid touching archived files when possible, provides early failure for queries that require archived data, and offers syntax to identify files that must be restored.^[archival-support-in-databricks-databricks-on-aws.md]

## Requirements

- **Storage tiers**: Amazon S3 Glacier Deep Archive or Glacier Flexible Retrieval are supported. Amazon S3 Glacier Instant Retrieval does **not** require configuring archival support, but when queried all scanned files are retrieved; Databricks recommends using views to restrict queries on tables stored in Glacier Instant Retrieval with lifecycle policies.^[archival-support-in-databricks-databricks-on-aws.md]
- **Incompatible**: Amazon S3 Intelligent-Tiering optional asynchronous archive access tiers are not compatible because they archive based on access time rather than file creation time.^[archival-support-in-databricks-databricks-on-aws.md]
- **Transaction log**: The cloud lifecycle policy **must not** archive the Delta transaction log (`_delta_log/` directory). If any files in `_delta_log/` are archived, the table becomes entirely inaccessible.^[archival-support-in-databricks-databricks-on-aws.md]

## Why Enable Archival Support?

Enabling archival support allows only queries that can be answered correctly without scanning archived files, such as:

- Queries that read metadata only.
- Queries whose filters allow the engine to avoid scanning archived files.

All queries that require archived data to produce correct results will fail with a clear error, preventing wasted compute.^[archival-support-in-databricks-databricks-on-aws.md]

## Enabling Archival Support

Use the `ALTER TABLE` statement to set the archival interval as a table property:

```sql
ALTER TABLE <table_name> SET TBLPROPERTIES(delta.timeUntilArchived = 'X days');
```

The `timeUntilArchived` property tells Databricks to ignore files older than the specified period. This setting is independent of the cloud lifecycle policy. Changes to one do not affect the other. If you update the cloud lifecycle policy, you must also update this table property.^[archival-support-in-databricks-databricks-on-aws.md]

If you enable this setting without a corresponding lifecycle policy, queries succeed and include data from files that would otherwise be considered archived (sampling behavior applies).^[archival-support-in-databricks-databricks-on-aws.md]

## Query Optimizations

Archival support optimizes queries that can be satisfied without scanning archived files. For queries that must access archived files, the system fails early and produces error messages pointing the user to restore necessary files.^[archival-support-in-databricks-databricks-on-aws.md]

## Showing Archived Files

To identify which files must be restored for a given query, use:

```sql
SHOW ARCHIVED FILES FOR table_name [ WHERE predicate ];
```

This returns URIs of archived files as a Spark DataFrame. Providing predicates that include partition columns or columns used for Z-ordering or clustering reduces the number of files returned.^[archival-support-in-databricks-databricks-on-aws.md]

## Restoring Archived Files

1. Run `SHOW ARCHIVED FILES` to list URIs.
2. Use the [S3 restore object APIs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/restoring-objects.html) to restore files to a fast retrieval tier.
3. After restoration, Databricks automatically detects restored files through a sampling mechanism (see below) and queries proceed normally.^[archival-support-in-databricks-databricks-on-aws.md]

## Update, Delete, or Merge Operations

`MERGE`, `UPDATE`, or `DELETE` operations that affect archived files will fail. You must restore the relevant files before running these commands. Use `SHOW ARCHIVED FILES` to determine which files to restore.^[archival-support-in-databricks-databricks-on-aws.md]

## Sampling for Restored Data

When preparing a scan, Databricks samples files older than the retention period required by the query. If the sampled files (presumed archived) have been restored, Databricks assumes all files for the query have been restored and processes the query, including data from the archived files. This sampling may not apply to all queries—see Limitations.^[archival-support-in-databricks-databricks-on-aws.md]

## Limitations

- Archival support applies **only to data files**, not the [Delta transaction log](/concepts/delta-transaction-log.md) (`_delta_log/` directory). Archiving transaction log files makes the table entirely inaccessible.^[archival-support-in-databricks-databricks-on-aws.md]
- Lifecycle policies based on access time or tags are not supported; only creation‑time‑based policies work.^[archival-support-in-databricks-databricks-on-aws.md]
- `DROP COLUMN` cannot be used on tables with archived files.^[archival-support-in-databricks-databricks-on-aws.md]
- `REORG TABLE APPLY PURGE` makes a best‑effort attempt but cannot purge archived deletion vector files.^[archival-support-in-databricks-databricks-on-aws.md]
- Extending the lifecycle management transition rule can cause errors (see section below).^[archival-support-in-databricks-databricks-on-aws.md]
- `LIMIT` queries do not trigger sampling for restored data. If data has been restored, a `LIMIT` query still returns a `DELTA_ARCHIVED_FILES_IN_LIMIT` error. If you encounter `Not enough files to satisfy LIMIT`, lower the `LIMIT` value to find unarchived rows.^[archival-support-in-databricks-databricks-on-aws.md]

## Changing the Lifecycle Management Transition Rule

If you change the cloud lifecycle policy interval, update `delta.timeUntilArchived` to match. Shortening the interval (less time before archival) works normally after updating the property. **Extending** the interval (adding more time before archival) can lead to errors because the cloud provider does not automatically restore already‑archived files. To avoid errors during the lag period:

- Option 1: Keep the old `timeUntilArchived` value until all files that were previously archived become eligible for the new threshold (i.e., the lag period ends), then update.
- Option 2: Update `timeUntilArchived` daily to reflect the actual age of the oldest archived data during the lag period.^[archival-support-in-databricks-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) – The table format that archival support works with.
- [Delta transaction log](/concepts/delta-transaction-log.md) – The metadata directory that must never be archived.
- S3 Lifecycle Policies – Cloud‑side mechanism that transitions objects to archival tiers.
- Databricks Runtime – Compute environment required for archival support (13.3 LTS+).
- Amazon S3 Glacier storage classes – Supported archival tiers.
- [SHOW ARCHIVED FILES](/concepts/show-archived-files-syntax.md) – SQL command to list archived files.
- Partition pruning and Z-ordering – Techniques to reduce the number of files that must be restored.

## Sources

- archival-support-in-databricks-databricks-on-aws.md

# Citations

1. [archival-support-in-databricks-databricks-on-aws.md](/references/archival-support-in-databricks-databricks-on-aws-d64d2061.md)

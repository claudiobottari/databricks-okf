---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f98414bd5252f8adc488d9192544689d64098f72512e618b13926f2dbbcba836
  pageDirectory: concepts
  sources:
    - archival-support-in-databricks-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - limitations-of-delta-archival-support
    - LODAS
  citations:
    - file: archival-support-in-databricks-databricks-on-aws.md
title: Limitations of Delta archival support
description: "Key constraints include: transaction log must never be archived, no support for access-time or tag-based policies, DROP COLUMN and PURGE restrictions, and LIMIT query incompatibility."
tags:
  - databricks
  - delta-lake
  - archival
  - limitations
timestamp: "2026-06-19T22:07:47.158Z"
---

# Limitations of Delta Archival Support

Delta Archival Support in Databricks enables query optimization when cloud lifecycle policies archive older data files to cold storage tiers. However, several important limitations constrain its use and behavior. Understanding these limitations is critical to avoiding query failures and data access issues.

## Core Limitations

### Transaction Log Must Remain Accessible

Archival support applies only to **data files**. If any files in the Delta transaction log (`_delta_log/` directory) are moved to an archived storage tier, the table becomes entirely inaccessible and all queries against the table fail. You must configure your cloud lifecycle policy so that the `_delta_log/` path is excluded from archival. ^[archival-support-in-databricks-databricks-on-aws.md]

### Only Creation-Time-Based Policies Supported

No support exists for lifecycle management policies that are not based on file creation time. This includes access-time-based policies and tag-based policies. Archive policies that evaluate criteria such as last access time or object tags are incompatible with Delta archival support. ^[archival-support-in-databricks-databricks-on-aws.md]

### No Support for Amazon S3 Intelligent-Tiering Archive Access Tiers

Amazon S3 Intelligent-Tiering optional asynchronous archive access tiers are not compatible with archival support in Databricks because they archive based on access time rather than file creation time. ^[archival-support-in-databricks-databricks-on-aws.md]

## Query and Operation Limitations

### `DROP COLUMN` Not Available

You cannot use `DROP COLUMN` on a table with archived files. To modify the schema by removing a column, you must first restore the archived files or remove the archival configuration. ^[archival-support-in-databricks-databricks-on-aws.md]

### `REORG TABLE APPLY PURGE` Limited Functionality

`REORG TABLE APPLY PURGE` makes only a best-effort attempt to purge archived data. It works on deletion vector files and referenced data files that are **not** archived, but `PURGE` cannot delete archived deletion vector files. ^[archival-support-in-databricks-databricks-on-aws.md]

### `LIMIT` Queries Fail on Archived Tables

`LIMIT` queries on tables with archival support enabled do not trigger sampling for restored data. If a table's archived data has been restored, most queries succeed when querying restored data — but a `LIMIT` query returns a `DELTA_ARCHIVED_FILES_IN_LIMIT` error. ^[archival-support-in-databricks-databricks-on-aws.md]

### `MERGE`, `UPDATE`, and `DELETE` Require Restored Data

The operation fails if you run a `MERGE`, `UPDATE`, or `DELETE` operation that impacts data in archived files. You must restore data to a storage tier that supports fast retrieval to run these operations. Use `SHOW ARCHIVED FILES` to determine which files must be restored. ^[archival-support-in-databricks-databricks-on-aws.md]

### Partial Sampling for Restored Data

When Databricks prepares a scan over a table with archival support enabled, it samples files older than the specified retention period to determine whether files have been restored. If the sampled files are restored, Databricks assumes **all** files for the query have been restored and proceeds. This sampling may not apply to all queries, which can lead to unexpected behavior. ^[archival-support-in-databricks-databricks-on-aws.md]

## Lifecycle Policy Change Limitations

### Extending the Archival Interval Causes Errors

If you extend the time interval before archival (adding more time before archival is triggered), updating the property `delta.timeUntilArchived` to the new value can lead to errors. Cloud providers do not automatically restore files from archived storage when data retention policies are changed. This means that files previously eligible for archival — but now not considered eligible — remain archived.

**Important:** To avoid errors, never set the property `delta.timeUntilArchived` to a value greater than the actual age of the most recently archived data. ^[archival-support-in-databricks-databricks-on-aws.md]

For example, if the time interval for archival is changed from 60 days to 90 days:

1. All records between 60 and 90 days old are archived when the policy changes.
2. For 30 days, no new files are archived (the oldest non-archived files are 60 days old).
3. After 30 days, the lifecycle policy correctly describes all archived data.

During this lag period, you can either leave `delta.timeUntilArchived` at the old threshold (treating some restorable data as archived) or update it daily to reflect the current actual interval. ^[archival-support-in-databricks-databricks-on-aws.md]

### Updating the Property Does Not Change Archival Behavior

Updating the value for `delta.timeUntilArchived` does **not** change which data is actually archived. It only changes which data Databricks treats as if it were archived. The table property must match the cloud lifecycle policy to operate correctly. ^[archival-support-in-databricks-databricks-on-aws.md]

## Compatibility Limitations

### Only Compatible with Databricks Compute

Archival support relies entirely on compatible Databricks compute environments and only works for Delta tables. Configuring archival support does **not** change behavior, compatibility, or support in OSS Delta Lake clients or Databricks Runtime 12.2 LTS and below. ^[archival-support-in-databricks-databricks-on-aws.md]

### Glacier Instant Retrieval Requires Manual Restriction

Amazon S3 Glacier Instant Retrieval does not require configuring archival support. However, when you run a query, **all scanned files are retrieved** from this storage tier. Databricks recommends using views to restrict queries against tables stored in Glacier Instant Retrieval with lifecycle policies configured. ^[archival-support-in-databricks-databricks-on-aws.md]

## Related Concepts

- [Delta Archival Support](/concepts/delta-lake-archival-support.md) — Overview of enabling archival for Delta tables
- [delta.timeUntilArchived table property](/concepts/deltatimeuntilarchived-table-property.md) — The configuration property for archival intervals
- Lifecycle Policy Configuration — Cloud-side lifecycle management setup
- Archived File Restoration — Restoring files from archived storage
- [SHOW ARCHIVED FILES syntax](/concepts/show-archived-files-syntax.md) — Identifying files that must be restored

## Sources

- archival-support-in-databricks-databricks-on-aws.md

# Citations

1. [archival-support-in-databricks-databricks-on-aws.md](/references/archival-support-in-databricks-databricks-on-aws-d64d2061.md)

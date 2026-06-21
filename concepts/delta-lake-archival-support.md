---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c081a92febaf1cf12bc187be8cc9efe3d306535beda693f94698db0db8005ad3
  pageDirectory: concepts
  sources:
    - archival-support-in-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-archival-support
    - DLAS
    - Delta Archival Support
    - archival support
  citations:
    - file: archival-support-in-databricks-databricks-on-aws.md
title: Delta Lake Archival Support
description: A Databricks feature that enables Delta Lake tables to work with cloud-based lifecycle policies by ignoring files older than a specified threshold, preventing query failures against archived data.
tags:
  - databricks
  - delta-lake
  - archival
  - data-management
timestamp: "2026-06-19T14:03:00.181Z"
---

# Delta Lake Archival Support

**Delta Lake archival support** is a public preview feature introduced in Databricks Runtime 13.3 LTS and above that enables the use of cloud-based lifecycle policies on object storage containing [Delta Lake](/concepts/delta-lake.md) tables. When enabled, the feature tells Databricks to ignore data files older than a specified retention period, allowing queries to avoid scanning archived data when possible. ^[archival-support-in-databricks-databricks-on-aws.md]

## Requirements

Archival support requires Amazon S3 Glacier Deep Archive or Glacier Flexible Retrieval. S3 Glacier Instant Retrieval does not require configuring archival support, but every query that scans the table retrieves all files – Databricks recommends using [views](/concepts/shared-views-in-databricks-to-databricks-sharing.md) to restrict queries against such tables. Amazon S3 Intelligent-Tiering optional asynchronous archive access tiers are **not** compatible because they archive based on access time rather than file creation time. ^[archival-support-in-databricks-databricks-on-aws.md]

## Why Enable Archival Support?

Enabling archival support allows only queries that can be answered correctly without touching archived files. These include metadata‑only queries and queries with filters that do not require scanning any archived files. All other queries fail early, reducing wasted compute and providing clear error messages. Users can generate a list of files that must be restored using `SHOW ARCHIVED FILES`. ^[archival-support-in-databricks-databricks-on-aws.md]

> **Important:** Databricks never returns results for queries that require archived files to produce the correct answer. ^[archival-support-in-databricks-databricks-on-aws.md]

Enabling archival support does **not** create or alter lifecycle policies on your cloud object storage. You must configure those separately and keep the table property `delta.timeUntilArchived` in sync with the cloud policy. ^[archival-support-in-databricks-databricks-on-aws.md]

## Enable Archival Support

Use the following SQL command to set the archival interval:

```sql
ALTER TABLE <table_name> SET TBLPROPERTIES(delta.timeUntilArchived = 'X days');
```

This setting tells Databricks to ignore files older than the specified time period. It is independent of your cloud account’s lifecycle policies – changing one does not change the other. If you update the cloud lifecycle policy, you must also update `delta.timeUntilArchived` on the table. ^[archival-support-in-databricks-databricks-on-aws.md]

> **Warning:** Your cloud lifecycle policy must **not** archive files in the `_delta_log/` directory. Archiving the [Delta transaction log](/concepts/delta-transaction-log.md) makes the table entirely inaccessible. ^[archival-support-in-databricks-databricks-on-aws.md]

## Show Archived Files

To identify which files must be restored to complete a given query, use:

```sql
SHOW ARCHIVED FILES FOR table_name [ WHERE predicate ];
```

This returns URIs of archived files as a Spark DataFrame. Providing predicates on the first 32 columns – especially partition, Z‑order, or clustering columns – reduces the number of files returned because Delta Lake uses statistics from the transaction log (min, max, null counts, record counts). ^[archival-support-in-databricks-databricks-on-aws.md]

## Restore Archived Files

After obtaining the file list from `SHOW ARCHIVED FILES`, restore the files using the S3 restore object API to a fast retrieval tier. Databricks automatically recognizes restored files through a sampling mechanism (see below). ^[archival-support-in-databricks-databricks-on-aws.md]

## Update or Delete Archived Data

`MERGE`, `UPDATE`, or `DELETE` operations that affect data in archived files fail. You must first restore the affected files using the restore process described above, then run the operation. ^[archival-support-in-databricks-databricks-on-aws.md]

## How Does Databricks Sample for Restored Data?

When preparing a scan over a table with archiving enabled, Databricks samples files older than the specified retention period to check whether they have been restored. If the sampled files are found to be restored, Databricks assumes all files for the query have been restored and proceeds with the query, including data from those files. ^[archival-support-in-databricks-databricks-on-aws.md]

Sampling does **not** apply to `LIMIT` queries. If a `LIMIT` query encounters archived data, it returns a `DELTA_ARCHIVED_FILES_IN_LIMIT` error instructing you to lower the `LIMIT` or restore more files. ^[archival-support-in-databricks-databricks-on-aws.md]

## Limitations

- Archival support applies **only to data files**. If any files in the `_delta_log/` directory are moved to an archived storage tier, the table becomes entirely inaccessible. ^[archival-support-in-databricks-databricks-on-aws.md]
- Lifecycle management policies based on access time or tags are not supported. ^[archival-support-in-databricks-databricks-on-aws.md]
- `DROP COLUMN` cannot be used on a table with archived files. ^[archival-support-in-databricks-databricks-on-aws.md]
- `REORG TABLE APPLY PURGE` makes a best‑effort attempt but cannot delete archived deletion vector files. ^[archival-support-in-databricks-databricks-on-aws.md]
- Extending the lifecycle management transition rule can cause errors if not handled carefully (see below). ^[archival-support-in-databricks-databricks-on-aws.md]

## Changing the Lifecycle Management Transition Rule

If you shorten the time before archival (e.g., from 90 to 60 days), update `delta.timeUntilArchived` to the new interval. The table continues working normally. ^[archival-support-in-databricks-databricks-on-aws.md]

If you **extend** the time before archival (e.g., from 60 to 90 days), cloud providers do **not** automatically restore already‑archived files. During the lag period (30 days in this example), you must either:

1. Keep `delta.timeUntilArchived` at the old threshold until enough time passes for all files to be archived under the new policy, then update; or  
2. Incrementally update `delta.timeUntilArchived` each day to match the actual age of the most recently archived data.

> **Critical:** Never set `delta.timeUntilArchived` to a value greater than the actual age of the most recently archived data. ^[archival-support-in-databricks-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) – The foundational storage layer for the feature
- [Delta transaction log](/concepts/delta-transaction-log.md) – Must not be archived to maintain table accessibility
- S3 Glacier storage classes – The supported archival tiers
- Lifecycle policies in cloud storage – Required to archive data
- Table properties in Delta Lake – How `delta.timeUntilArchived` is set
- [SHOW ARCHIVED FILES command](/concepts/show-archived-files-syntax.md) – Syntax for listing archived files

## Sources

- archival-support-in-databricks-databricks-on-aws.md

# Citations

1. [archival-support-in-databricks-databricks-on-aws.md](/references/archival-support-in-databricks-databricks-on-aws-d64d2061.md)

---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d8b9a034af96b3ce43502c44ff6609079b30bda2710fbcca514c1cee54a80fb2
  pageDirectory: concepts
  sources:
    - archival-support-in-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deltatimeuntilarchived
    - Delta Time Until Archived
    - Delta timeUntilArchived
    - deltatimeuntilarchived-table-property
    - DTP
    - delta.timeUntilArchived Property
  citations:
    - file: archival-support-in-databricks-databricks-on-aws.md
title: delta.timeUntilArchived
description: A Delta table property that specifies the archival interval, telling Databricks to ignore files older than the given time period when querying.
tags:
  - delta-lake
  - configuration
  - table-properties
timestamp: "2026-06-18T14:26:52.864Z"
---

# delta.timeUntilArchived

**`delta.timeUntilArchived`** is a [Delta Lake](/concepts/delta-lake.md) table property that controls how Databricks treats files older than a specified age. When set, Databricks ignores data files whose creation timestamp (as recorded in the Delta transaction log) exceeds the configured duration, enabling query acceleration on tables whose cold data has been moved to archival cloud storage tiers such as Amazon S3 Glacier Deep Archive or S3 Glacier Flexible Retrieval. ^[archival-support-in-databricks-databricks-on-aws.md]

## Setting the Property

You enable archival support for a Delta table by manually setting the `delta.timeUntilArchived` property to match the retention period defined in your cloud object storage lifecycle policy:

```sql
ALTER TABLE <table_name> SET TBLPROPERTIES(delta.timeUntilArchived = 'X days');
```

The value `X days` tells Databricks to ignore files in the table that are older than `X` days. This setting is **independent** of your cloud account’s lifecycle policies — changing one does not automatically update the other. If you modify the lifecycle policy in your cloud account, you must also update the `delta.timeUntilArchived` property on the Delta table to the same interval. ^[archival-support-in-databricks-databricks-on-aws.md]

### Requirements

- The property is available in **Public Preview** for Databricks Runtime 13.3 LTS and above.
- The cloud storage tier must be Amazon S3 Glacier Deep Archive or S3 Glacier Flexible Retrieval. S3 Glacier Instant Retrieval does not require this property, but Databricks recommends using views to restrict queries on tables stored in that tier.
- Amazon S3 Intelligent-Tiering optional asynchronous archive access tiers are **not compatible** because they archive based on access time rather than file creation time. ^[archival-support-in-databricks-databricks-on-aws.md]

## How It Works

When `delta.timeUntilArchived` is set, Databricks uses the file creation time recorded in the Delta transaction log to determine which files are considered archived. Files older than the specified duration are treated as “archived” for query planning purposes — the engine will skip them when possible and fail fast with a clear error if a query must scan archived files to produce a correct result.

If archival support is not enabled, operations against a Delta table might break when underlying data files or transaction log files have been moved to archival storage and become unavailable. Enabling the property introduces optimizations to avoid querying archived data and provides syntax to identify files that must be restored. ^[archival-support-in-databricks-databricks-on-aws.md]

### Queries Optimized for Archived Data

Databricks allows queries that can be answered correctly without touching archived files, such as:

- Queries that read only metadata.
- Queries with filters that do not require scanning any archived files (e.g., partition pruning, Z-order filtering).

Queries that require data from archived files **fail** and return an error indicating that archived files must be restored. ^[archival-support-in-databricks-databricks-on-aws.md]

### Early Failure and Error Messages

If a query must scan archived files, it fails early with a message informing the user that archived files were accessed. This reduces wasted compute and permits quick reruns after restoration. If you encounter the error `Not enough files to satisfy LIMIT`, it means the table lacks unarchived rows to meet the specified `LIMIT` — lowering the `LIMIT` may help. ^[archival-support-in-databricks-databricks-on-aws.md]

## Interaction with Cloud Lifecycle Policies

The `delta.timeUntilArchived` property must be kept in sync with the actual retention period of your cloud lifecycle policy. ^[archival-support-in-databricks-databricks-on-aws.md]

### Shortening the Retention Interval

If the lifecycle policy is changed to archive files sooner (shorter time before archival), you can safely reduce the `delta.timeUntilArchived` value. Archival support continues to function normally after the table property is updated. ^[archival-support-in-databricks-databricks-on-aws.md]

### Extending the Retention Interval

If the lifecycle policy is changed to archive files later (longer time before archival), you must take care: cloud providers do not automatically restore already‑archived files when the retention period is extended. Therefore, **never set `delta.timeUntilArchived` to a value greater than the actual age of the most recently archived data**. Doing so can cause queries to incorrectly assume files are available when they are still archived.

During the transition period, you can either leave the old setting until the new policy takes full effect (knowing that some accessible files will be ignored), or update the setting incrementally each day to reflect the real‑time archive threshold. ^[archival-support-in-databricks-databricks-on-aws.md]

### Important: Transaction Log Must Not Be Archived

Your cloud lifecycle policy **must not** archive the Delta transaction log directory (`_delta_log/`). If any transaction log files are moved to archival storage, the entire table becomes inaccessible and all queries fail. ^[archival-support-in-databricks-databricks-on-aws.md]

## Restoring Archived Files

To identify files that need restoration, use the `SHOW ARCHIVED FILES` command:

```sql
SHOW ARCHIVED FILES FOR table_name [ WHERE predicate ];
```

This returns the URIs of archived files as a Spark DataFrame. After restoring the files using the S3 restore API, Databricks automatically recognizes them through a sampling mechanism — when a query needs to scan archived files, the engine samples to check if any files have been restored; if so, it assumes all required files are restored and proceeds. ^[archival-support-in-databricks-databricks-on-aws.md]

## Limitations

- **Data files only:** Archival support applies solely to data files. The `_delta_log/` must remain on fast storage.
- **Time‑based policies only:** Lifecycle policies based on access time or tags are not supported.
- **`DROP COLUMN` not supported** on tables with archived files.
- **`REORG TABLE APPLY PURGE`** makes a best‑effort attempt but cannot delete archived deletion vector files.
- **`LIMIT` queries:** If a table’s data is restored, `LIMIT` queries do not trigger sampling and may return a `DELTA_ARCHIVED_FILES_IN_LIMIT` error.
- **Compatibility:** Archival support works only on Databricks compute with Delta Lake; it does not change behavior in OSS Delta Lake clients or Databricks Runtime 12.2 LTS and below. ^[archival-support-in-databricks-databricks-on-aws.md]

## Related Concepts

- [Archival Support in Databricks](/concepts/archival-support-in-databricks.md)
- [Delta Lake table properties](/concepts/delta-lake-reader-table-features.md)
- Cloud lifecycle policies
- [SHOW ARCHIVED FILES](/concepts/show-archived-files-syntax.md)
- [Delta transaction log](/concepts/delta-transaction-log.md)
- Table maintenance operations

## Sources

- archival-support-in-databricks-databricks-on-aws.md

# Citations

1. [archival-support-in-databricks-databricks-on-aws.md](/references/archival-support-in-databricks-databricks-on-aws-d64d2061.md)

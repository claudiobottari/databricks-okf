---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 48a1b56d4ee674e34b1cd989bd9d37d45a306a77f7015815f7e276b2feb20519
  pageDirectory: concepts
  sources:
    - archival-support-in-databricks-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - archival-support-for-delta-tables-in-databricks
    - ASFDTID
  citations:
    - file: archival-support-in-databricks-databricks-on-aws.md
title: Archival support for Delta tables in Databricks
description: A Databricks feature that allows Delta tables to use cloud lifecycle policies on object storage, enabling queries to ignore files older than a specified period and fail early when archived files must be scanned.
tags:
  - databricks
  - delta-lake
  - storage-optimization
timestamp: "2026-06-18T10:48:07.920Z"
---



# Archival support for Delta tables in Databricks

**Archival support** for Delta tables enables you to use cloud-based lifecycle policies on cloud object storage containing [Delta Lake](/concepts/delta-lake.md) tables. When enabled, Databricks is informed to ignore files that are older than the specified period in the table, effectively treating them as archived.^[archival-support-in-databricks-databricks-on-aws.md]

## Overview

Archival support is in **Public Preview** for Databricks Runtime 13.3 LTS and above.^[archival-support-in-databricks-databricks-on-aws.md]

Enabling archival support for a table in Databricks does not create or alter lifecycle policies defined for your cloud object storage. You must manage those policies separately in your cloud provider.^[archival-support-in-databricks-databricks-on-aws.md]

Without archival support, operations against Delta tables might break because data files or transaction log files have moved to archived locations and are unavailable when queried. Archival support introduces optimizations to avoid querying archived data when possible and adds new syntax to identify files that must be restored from archival storage.^[archival-support-in-databricks-databricks-on-aws.md]

## Requirements

Archival support requires S3 Glacier Deep Archive or Glacier Flexible Retrieval. See the AWS documentation on [working with archived objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/archived-objects.html).^[archival-support-in-databricks-databricks-on-aws.md]

Amazon S3 Glacier Instant Retrieval does not require configuring archival support; however, when you run a query, all scanned files are retrieved. Databricks recommends using views to restrict queries against tables stored in Glacier Instant Retrieval with lifecycle policies configured.^[archival-support-in-databricks-databricks-on-aws.md]

**Important**: Amazon S3 Intelligent-Tiering optional asynchronous archive access tiers is **not** compatible with archival support in Databricks because it archives based on access time rather than file creation time.^[archival-support-in-databricks-databricks-on-aws.md]

## Why enable archival support?

Archival support only allows queries that can be answered correctly without touching archived files. These include queries that either:
- Query metadata only.
- Have filters that do not require scanning any archived files.

All queries that require data in archived files fail. Databricks **never** returns results for queries that require archived files to return the correct result.^[archival-support-in-databricks-databricks-on-aws.md]

## Queries optimized for archived data

Archival support in Databricks optimizes queries against Delta tables with archived data. For queries that must scan archived files to generate correct results, configuring archival support ensures:
- Queries fail early if they attempt to access archived files, reducing wasted compute and allowing users to adapt and re-run queries quickly.
- Error messages inform users that a query has failed because it attempted to access archived files.^[archival-support-in-databricks-databricks-on-aws.md]

Users can generate a report of files that must be restored using the `SHOW ARCHIVED FILES` syntax. See the [Show archived files](#show-archived-files) section.^[archival-support-in-databricks-databricks-on-aws.md]

**Note**: If you get the error `Not enough files to satisfy LIMIT`, your table does not have enough data rows in unarchived files to satisfy the `LIMIT` clause. Lower the `LIMIT` clause to find enough unarchived rows. See [Limitations](#limitations).^[archival-support-in-databricks-databricks-on-aws.md]

## Enable archival support

You enable archival support for Delta tables by manually specifying the archival interval configured in the underlying cloud lifecycle management policy:

```sql
ALTER TABLE <table_name> SET TBLPROPERTIES(delta.timeUntilArchived = 'X days');
```

Setting `timeUntilArchived` tells Databricks to ignore files in your [Delta Lake Table](/concepts/delta-lake-table.md) that are older than the specified time period. This setting is separate from your cloud account's lifecycle policies. Changes to one do not affect the other. If you update the lifecycle policy in your cloud account, you must also update the archival setting on your [Delta Lake Table](/concepts/delta-lake-table.md).^[archival-support-in-databricks-databricks-on-aws.md]

**Warning**: Your cloud lifecycle policy must **not** archive the Delta transaction log (`_delta_log/` directory). See [Limitations](#limitations).^[archival-support-in-databricks-databricks-on-aws.md]

**Important**: Archival support relies entirely on compatible Databricks compute environments and only works for Delta tables. Configuring archival support does not change behavior, compatibility, or support in OSS Delta Lake clients or Databricks Runtime 12.2 LTS and below.^[archival-support-in-databricks-databricks-on-aws.md]

## Show archived files

To identify files that must be restored to complete a given query:

```sql
SHOW ARCHIVED FILES FOR table_name [ WHERE predicate ];
```

This operation returns URIs for archived files as a Spark DataFrame. Restore the necessary archived files following documented instructions from your object storage provider. See [Restore archived files](#restore-archived-files).^[archival-support-in-databricks-databricks-on-aws.md]

During this operation, Delta Lake only has access to the data statistics contained in the transaction log. By default, these include:
- Minimum values
- Maximum values
- Null counts
- Total number of records

The files returned include all archived files that must be read to determine whether records fulfilling a predicate exist in the file. Databricks recommends providing predicates that include fields on which data is partitioned, z-ordered, or clustered to reduce the number of files that must be restored.^[archival-support-in-databricks-databricks-on-aws.md]

## Restore archived files

Use `SHOW ARCHIVED FILES` to view the list of archived files that require restoration. Then use the S3 restore object APIs to restore files to a fast retrieval storage tier. See [Restoring an archived object](https://docs.aws.amazon.com/AmazonS3/latest/userguide/restoring-objects.html).^[archival-support-in-databricks-databricks-on-aws.md]

After restoring files in your cloud provider storage, you can query your table. Archival support automatically recognizes the restored files. See [How does Databricks sample for restored data?](#how-does-databricks-sample-for-restored-data).^[archival-support-in-databricks-databricks-on-aws.md]

## Update or delete archived data

Running `MERGE`, `UPDATE`, or `DELETE` operations that impact data in archived files fails. You must restore data to a storage tier that supports fast retrieval to run these operations. Use `SHOW ARCHIVED FILES` to determine the files you must restore.^[archival-support-in-databricks-databricks-on-aws.md]

## How does Databricks sample for restored data?

When Databricks prepares a scan over a table with archival support enabled, it samples files older than the specified retention period required by the query to determine whether files have been restored. If the results indicate the sampled files have been restored, Databricks assumes all files for the query have been restored and processes the query. Results include data from the files marked for archival.^[archival-support-in-databricks-databricks-on-aws.md]

## Limitations

The following limitations exist:

- **Archival support applies only to data files.** If any files in the Delta transaction log (`_delta_log/` directory) are moved to an archived storage tier, the table becomes entirely inaccessible and all queries fail. You must configure your cloud lifecycle policy so that `_delta_log/` is not included in archival. See [AWS S3 Lifecycle configuration examples](https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-configuration-examples.html).^[archival-support-in-databricks-databricks-on-aws.md]
- **No support exists for lifecycle management policies not based on file creation time.** This includes access-time-based policies and tag-based policies.^[archival-support-in-databricks-databricks-on-aws.md]
- **You cannot use `DROP COLUMN`** on a table with archived files.^[archival-support-in-databricks-databricks-on-aws.md]
- **`REORG TABLE APPLY PURGE`** makes a best-effort attempt but only works on deletion vector files and referenced data files that are not archived. `PURGE` cannot delete archived deletion vector files.^[archival-support-in-databricks-databricks-on-aws.md]
- **Extending the lifecycle management transition rule** results in unexpected behavior. See [Extend the lifecycle management transition rule](#extend-the-lifecycle-management-transition-rule).^[archival-support-in-databricks-databricks-on-aws.md]
- **`LIMIT` queries** on tables with archival support enabled do not trigger sampling for restored data. If a table's data is restored, most queries succeed, but a `LIMIT` query returns a `DELTA_ARCHIVED_FILES_IN_LIMIT` error. See [How does Databricks sample for restored data?](#how-does-databricks-sample-for-restored-data).^[archival-support-in-databricks-databricks-on-aws.md]

## Change the lifecycle management transition rule

If you change the time interval for your cloud lifecycle management transition rule, you must update the property `delta.timeUntilArchived` to the same interval. If the time interval before archival is shortened (less time since file creation), archival support continues functioning normally after the table property is updated.^[archival-support-in-databricks-databricks-on-aws.md]

### Extend the lifecycle management transition rule

If the time interval before archival is extended (to add more time before archival is triggered), updating `delta.timeUntilArchived` to the new value can lead to errors. Cloud providers do not automatically restore files from archived storage when data retention policies are changed. Files previously eligible for archival but now not considered eligible are still archived.^[archival-support-in-databricks-databricks-on-aws.md]

**Important**: To avoid errors, never set `delta.timeUntilArchived` to a value greater than the actual age of the most recently archived data.^[archival-support-in-databricks-databricks-on-aws.md]

Consider a scenario where the time interval for archival is changed from 60 days to 90 days:
1. All records between 60 and 90 days old are archived when the policy changes.
2. For 30 days, no new files are archived (the oldest non-archived files are 60 days old when the policy is extended).
3. After 30 days, the lifecycle policy correctly describes all archived data.

During the lag period, you can take one of the following approaches:
1. Leave `delta.timeUntilArchived` with the old threshold until enough time has passed for all files to be archived. Each day for the first 30 days, another day's worth of data would be considered archived by Databricks but still needs to be archived by the cloud provider. After 30 days, update to `90 days`.
2. Update `delta.timeUntilArchived` each day to reflect the current interval during the lag period. For example, after 7 days, setting `delta.timeUntilArchived` to `67 days` accurately reflects the age of all archived data files. This approach is only necessary if you must access all data in hot tiers.^[archival-support-in-databricks-databricks-on-aws.md]

**Note**: Updating the value for `delta.timeUntilArchived` does not change which data is archived. It only changes which data Databricks treats as if it were archived.^[archival-support-in-databricks-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The underlying storage format for Delta tables
- [Delta transaction log](/concepts/delta-transaction-log.md) — The `_delta_log/` directory that must not be archived
- [Unity Catalog](/concepts/unity-catalog.md) — Governance layer for managing Delta tables and archival policies
- Cloud lifecycle policies — Policies managed in your cloud provider for archiving objects
- S3 Glacier — AWS storage tiers compatible with archival support

## Sources

- archival-support-in-databricks-databricks-on-aws.md

# Citations

1. [archival-support-in-databricks-databricks-on-aws.md](/references/archival-support-in-databricks-databricks-on-aws-d64d2061.md)

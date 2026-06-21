---
title: Archival support in Databricks | Databricks on AWS
source: https://docs.databricks.com/aws/en/optimizations/archive-delta
ingestedAt: "2026-06-18T08:18:31.202Z"
---

Preview

This feature is in Public Preview for Databricks Runtime 13.3 LTS and above.

Archival support in Databricks enables you to use cloud-based lifecycle policies on cloud object storage containing Delta tables. Enabling archival support on a Delta Lake table effectively tells Databricks to ignore files that are older than the specified period in the table.

## Requirements[​](#requirements "Direct link to Requirements")

Archival support requires S3 Glacier Deep Archive or Glacier Flexible Retrieval. See [AWS docs on working with archived objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/archived-objects.html).

Amazon S3 Glacier Instant Retrieval does not require configuring archival support. However, when you run a query, all scanned files are retrieved. Databricks recommends using views to restrict queries against tables stored in Glacier Instant Retrieval with lifecycle policies configured.

warning

Amazon S3 Intelligent-Tiering optional asynchronous archive access tiers is not compatible with archival support in Databricks because it archives based on access time rather than file creation time.

## Why should you enable archival support?[​](#why-should-you-enable-archival-support "Direct link to Why should you enable archival support?")

Archival support only allows queries that can be answered correctly without touching archived files. These queries include those that either:

*   Query metadata only.
*   Have filters that do not require scanning any archived files.

All queries that require data in archived files fail.

important

Databricks never returns results for queries that require archived files to return the correct result.

Enabling archival support for a table in Databricks does not create or alter lifecycle policies defined for your cloud object storage. See [Change the lifecycle management transition rule](#change-rule).

Without archival support, operations against Delta tables might break because data files or transaction log files have moved to archived locations and are unavailable when queried. Archival support introduces optimizations to avoid querying archived data when possible. It also adds new syntax to identify files that must be restored from archival storage to complete queries.

## Queries optimized for archived data[​](#queries-optimized-for-archived-data "Direct link to Queries optimized for archived data")

Archival support in Databricks optimizes the following queries against Delta tables.

## Early failure and error messages[​](#early-failure-and-error-messages "Direct link to Early failure and error messages")

For queries that must scan archived files to generate correct results, configuring archival support for Delta Lake ensures the following:

*   Queries fail early if they attempt to access archived files, reducing wasted compute and allowing users to adapt and re-run queries quickly.
*   Error messages inform users that a query has failed because the query attempted to access archived files.

Users can generate a report of files that must be restored using the `SHOW ARCHIVED FILES` syntax. See [Show archived files](#show).

important

If you get the error `Not enough files to satisfy LIMIT`, your table does not have enough data rows in unarchived files to satisfy the number of records specified by `LIMIT`. Lower the `LIMIT` clause to find enough unarchived rows to meet the specified `LIMIT`. See [Limitations](#limitations).

## Enable archival support[​](#enable-archival-support "Direct link to Enable archival support")

You enable archival support for Delta tables by manually specifying the archival interval configured in the underlying cloud lifecycle management policy.

SQL

    ALTER TABLE <table_name> SET TBLPROPERTIES(delta.timeUntilArchived = 'X days');

Setting a `timeUntilArchived` time tells Databricks to ignore files in your Delta Lake table that are older than the specified time period. This setting is separate from your cloud account’s lifecycle policies. Changes to one do not affect the other. If you update the lifecycle policy in your cloud account, you must also update the archival setting on your Delta Lake table. See [Change the lifecycle management transition rule](#change-rule).

When you set a new lifecycle policy in your cloud account, you might see a delay before the policy is fully propagated to all S3 systems. See [Setting lifecycle configuration](https://docs.aws.amazon.com/AmazonS3/latest/userguide/how-to-set-lifecycle-configuration-intro.html).

If you enable this setting without lifecycle policies set for your cloud object storage, archival support allows queries to succeed, and results include data from the files marked for archival. See [How does Databricks sample for restored data?](#sampling).

warning

Your cloud lifecycle policy must not archive the Delta transaction log (`_delta_log/` directory). See [Limitations](#limitations).

important

Archival support relies entirely on compatible Databricks compute environments and only works for Delta tables. Configuring archival support does not change behavior, compatibility, or support in OSS Delta Lake clients or Databricks Runtime 12.2 LTS and below.

## Show archived files[​](#show-archived-files "Direct link to show-archived-files")

To identify files that must be restored to complete a given query, use `SHOW ARCHIVED FILES`.

SQL

    SHOW ARCHIVED FILES FOR table_name [ WHERE predicate ];

This operation returns URIs for archived files as a Spark DataFrame. Restore the necessary archived files following documented instructions from your object storage provider. See [Restore archived files](#restore).

For information on how Databricks checks for restored data, see [How does Databricks sample for restored data?](#sampling).

note

During this operation, Delta Lake only has access to the data statistics contained in the transaction log. By default, these are the following statistics collected on the first 32 columns in the table:

*   Minimum values
*   Maximum values
*   Null counts
*   Total number of records

The files returned include all archived files that must be read to determine whether or not records fulfilling a predicate exist in the file. Databricks recommends providing predicates that include fields on which data is partitioned, z-ordered, or clustered to reduce the number of files that must be restored.

## Restore archived files[​](#restore-archived-files "Direct link to restore-archived-files")

To identify all files that require restoration, use `SHOW ARCHIVED FILES` to view the list of archived files.

Use the S3 restore object APIs to restore your files to a fast retrieval storage tier. See [Restoring an archived object](https://docs.aws.amazon.com/AmazonS3/latest/userguide/restoring-objects.html).

After restoring the files in your cloud provider storage, you can query your table. Archival support automatically recognizes the restored files. For information on how Databricks checks for restored data, see [How does Databricks sample for restored data?](#sampling).

## Update or delete archived data[​](#update-or-delete-archived-data "Direct link to Update or delete archived data")

The operation fails if you run a `MERGE`, `UPDATE`, or `DELETE` operation that impacts data in archived files. You must restore data to a storage tier that supports fast retrieval to run these operations. Use `SHOW ARCHIVED FILES` to determine the files that you must restore (see [Restore archived files](#restore)).

## How does Databricks sample for restored data?[​](#how-does-databricks-sample-for-restored-data "Direct link to how-does-databricks-sample-for-restored-data")

When Databricks prepares a scan over a table with archival support enabled, it samples files older than the specified retention period required by the query to determine whether or not files have been restored. If the results indicate the sampled files presumed to be archived have been restored, Databricks assumes all files for the query have been restored and the query processes. Results include data from the files marked for archival.

Sampling may not apply to all queries, see [Limitations](#limitations).

## Limitations[​](#limitations "Direct link to Limitations")

The following limitations exist:

*   Archival support applies only to data files. If any files in the Delta transaction log (`_delta_log/` directory) are moved to an archived storage tier, the table becomes entirely inaccessible and all queries against the table fail. You must configure your cloud lifecycle policy so that the `_delta_log/` path is not included in archival. See [examples of S3 Lifecycle configurations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-configuration-examples.html).
*   No support exists for lifecycle management policies that are not based on file creation time. This includes access-time-based policies and tag-based policies.
*   You cannot use `DROP COLUMN` on a table with archived files.
*   `REORG TABLE APPLY PURGE` makes a best-effort attempt, but only works on deletion vector files and referenced data files that are not archived. `PURGE` cannot delete archived deletion vector files.
*   Extending the lifecycle management transition rule results in unexpected behavior. See [Extend the lifecycle management transition rule](#extend-rule).
*   `LIMIT` queries on tables with archival support enabled do not trigger sampling for restored data. If a table's data is restored, most queries succeed when querying restored data, but a `LIMIT` query returns a `DELTA_ARCHIVED_FILES_IN_LIMIT` error. See [How does Databricks sample for restored data?](#sampling).

## Change the lifecycle management transition rule[​](#change-the-lifecycle-management-transition-rule "Direct link to change-the-lifecycle-management-transition-rule")

If you change the time interval for your cloud lifecycle management transition rule, you must update the property `delta.timeUntilArchived` to the same interval.

If the time interval before archival is shortened (less time since file creation), archival support for the Delta table continues functioning normally after the table property is updated.

### Extend the lifecycle management transition rule[​](#extend-the-lifecycle-management-transition-rule "Direct link to extend-the-lifecycle-management-transition-rule")

If the time interval before archival is extended (to add more time before archival is triggered), updating the property `delta.timeUntilArchived` to the new value can lead to errors. Cloud providers do not automatically restore files from archived storage when data retention policies are changed. This means that files previously eligible for archival but now not considered eligible for archival are still archived.

important

To avoid errors, never set the property `delta.timeUntilArchived` to a value greater than the actual age of the most recently archived data.

Consider a scenario in which the time interval for archival is changed from 60 days to 90 days:

1.  All records between 60 and 90 days old are archived when the policy changes.
2.  For 30 days, no new files are archived (the oldest non-archived files are 60 days old when the policy is extended).
3.  After 30 days, the lifecycle policy correctly describes all archived data.

The `delta.timeUntilArchived` setting tracks the set time interval against the file creation time recorded by the Delta transaction log. It does not have explicit knowledge of the underlying policy. During the lag period between the old archival threshold and the new archival threshold, you can take one of the following approaches to avoid querying archived files:

1.  You can leave the setting `delta.timeUntilArchived` with the old threshold until enough time has passed for all files to be archived.
    *   Following the example above, each day for the first 30 days, another day's worth of data would be considered archived by Databricks but still needs to be archived by the cloud provider. This does not result in an error but ignores some data files that could be queried.
    *   After 30 days, update the `delta.timeUntilArchived` to `90 days`.
2.  You can update the setting `delta.timeUntilArchived` each day to reflect the current interval during the lag period.
    *   While the cloud policy is set to 90 days, the actual age of archived data changes in real-time. For example, after 7 days, setting `delta.timeUntilArchived` to `67 days` accurately reflects the age of all archived data files.
    *   This approach is only necessary if you must access all data in hot tiers.

note

Updating the value for `delta.timeUntilArchived` does not change which data is archived. It only changes which data Databricks treats as if it were archived.

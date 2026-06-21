---
title: Delta Lake limitations on S3 | Databricks on AWS
source: https://docs.databricks.com/aws/en/delta/s3-limitations
ingestedAt: "2026-06-18T08:05:05.503Z"
---

Delta Lake on Databricks has specific limitations when storing tables in Amazon S3, including bucket versioning constraints, multi-cluster write restrictions, and risks from deleting files directly.

## Bucket versioning and Delta Lake[​](#bucket-versioning-and-delta-lake "Direct link to bucket-versioning-and-delta-lake")

Databricks recommends that you don't turn on bucket versioning for buckets that store Delta Lake data, including Unity Catalog managed tables. Delta Lake implements its own versioning and garbage collection.

When you turn on bucket versioning, S3 retains copies of metadata and data files that manual and automated processes on Databricks consider deleted. This includes data files that `VACUUM` would permanently delete and transaction logs cleaned up automatically during regular Delta Lake table operations.

important

If you choose to use bucket versioning, Databricks recommends retaining three versions and implementing a lifecycle management policy that retains versions for 7 days or less for all S3 buckets with versioning enabled.

If you encounter performance slowdown on tables stored in buckets with versioning enabled, mention that bucket versioning is enabled when contacting Databricks support.

## Multi-cluster write limitations[​](#multi-cluster-write-limitations "Direct link to Multi-cluster write limitations")

warning

To avoid potential data corruption and data loss issues, Databricks recommends that you don't modify the same Delta Lake table stored in S3 from different workspaces.

The _eventually consistent_ model used in Amazon S3 can lead to potential problems when multiple systems or clusters modify data in the same table simultaneously.

Databricks and Delta Lake support multi-cluster writes by default, meaning that queries writing to a table from multiple clusters at the same time won't corrupt the table. For Delta Lake tables stored on S3, this guarantee is limited to a single Databricks workspace.

The following features are not supported when running in this mode:

*   [Server-Side Encryption with Customer-Provided Encryption Keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html)
*   S3 paths with credentials in a cluster that cannot access [AWS Security Token Service](https://docs.aws.amazon.com/STS/latest/APIReference/Welcome.html)

You can turn off multi-cluster writes by setting `spark.databricks.delta.multiClusterWrites.enabled` to `false`. If they are turned off, writes to a single table _must_ originate from a single cluster.

warning

Turning off `spark.databricks.delta.multiClusterWrites.enabled` and modifying the same Delta Lake table from _multiple_ clusters concurrently might cause data loss or data corruption.

For more information on multi-cluster writes in Databricks, see [Configure Databricks S3 commit service-related settings](https://docs.databricks.com/aws/en/security/network/classic/s3-commit-service).

## Stale data after deleting files with `rm -rf`[​](#stale-data-after-deleting-files-with-rm--rf "Direct link to stale-data-after-deleting-files-with-rm--rf")

Don't use `rm -rf` to drop a Delta Lake table. See [Drop or replace a table](https://docs.databricks.com/aws/en/tables/operations/drop-table).

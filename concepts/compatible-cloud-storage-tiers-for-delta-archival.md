---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fc25b02d06ef39d44c4aa00d08c2258ba2700861b7e7e5609035817c08cb8c21
  pageDirectory: concepts
  sources:
    - archival-support-in-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - compatible-cloud-storage-tiers-for-delta-archival
    - CCSTFDA
  citations:
    - file: archival-support-in-databricks-databricks-on-aws.md
title: Compatible Cloud Storage Tiers for Delta Archival
description: "The specific AWS S3 storage tiers compatible with Databricks archival support: S3 Glacier Deep Archive and Glacier Flexible Retrieval; excluding Glacier Instant Retrieval (no config needed) and Intelligent-Tiering asynchronous archive tiers."
tags:
  - databricks
  - aws
  - s3
  - archival
  - compatibility
timestamp: "2026-06-19T14:03:17.150Z"
---

# Compatible Cloud Storage Tiers for Delta Archival

**Compatible Cloud Storage Tiers for Delta Archival** refers to the specific Amazon S3 storage classes that are supported when using Databricks' archival support feature for Delta tables. Archival support enables cloud-based lifecycle policies on object storage containing Delta tables, allowing Databricks to ignore files older than a specified period. ^[archival-support-in-databricks-databricks-on-aws.md]

## Supported Storage Tiers

Archival support requires one of the following S3 storage tiers: ^[archival-support-in-databricks-databricks-on-aws.md]

- **S3 Glacier Deep Archive** — The lowest-cost storage class designed for long-term retention of data that is accessed rarely.
- **S3 Glacier Flexible Retrieval** — A low-cost storage class for archival data that can be retrieved in minutes to hours.

## Unsupported Storage Tiers

### S3 Glacier Instant Retrieval

Amazon S3 Glacier Instant Retrieval does **not** require configuring archival support. However, when you run a query against a table stored in Glacier Instant Retrieval, all scanned files are retrieved. Databricks recommends using views to restrict queries against tables stored in Glacier Instant Retrieval with lifecycle policies configured. ^[archival-support-in-databricks-databricks-on-aws.md]

### S3 Intelligent-Tiering

Amazon S3 Intelligent-Tiering optional asynchronous archive access tiers are **not compatible** with archival support in Databricks. This is because Intelligent-Tiering archives based on access time rather than file creation time, which conflicts with Databricks' file creation time-based approach. ^[archival-support-in-databricks-databricks-on-aws.md]

## Lifecycle Policy Requirements

When configuring lifecycle policies on your cloud object storage for use with Databricks archival support, the following requirements apply: ^[archival-support-in-databricks-databricks-on-aws.md]

- **Lifecycle policies must be based on file creation time.** Tag-based policies and access-time-based policies are not supported.
- **The Delta transaction log (`_delta_log/` directory) must not be archived.** If any files in the transaction log are moved to an archived storage tier, the table becomes entirely inaccessible and all queries fail. You must configure your cloud lifecycle policy to exclude the `_delta_log/` path from archival.

## Configuring Compatible Storage

To use archival support with compatible storage tiers: ^[archival-support-in-databricks-databricks-on-aws.md]

1. Configure your cloud lifecycle policy to transition data files to Glacier Deep Archive or Glacier Flexible Retrieval after a specified period.
2. Set the `delta.timeUntilArchived` table property on your Delta table to match the archival interval:

```sql
ALTER TABLE <table_name> SET TBLPROPERTIES(delta.timeUntilArchived = 'X days');
```

If you change the time interval for your lifecycle management transition rule, you must update `delta.timeUntilArchived` to the same interval. ^[archival-support-in-databricks-databricks-on-aws.md]

## Restoring Archived Files

To query data in archived files, you must restore them to a fast retrieval storage tier using the S3 restore object APIs. After restoration, archival support automatically recognizes the restored files. ^[archival-support-in-databricks-databricks-on-aws.md]

Use `SHOW ARCHIVED FILES` to identify which files need restoration before running queries that require archived data. ^[archival-support-in-databricks-databricks-on-aws.md]

## Related Concepts

- [Archival Support in Databricks](/concepts/archival-support-in-databricks.md) — The main feature enabling lifecycle policy integration with Delta tables.
- [Delta Lake](/concepts/delta-lake.md) — The open-source storage layer that archival support is built upon.
- S3 Lifecycle Policies — Cloud storage policies that define when files transition to archival tiers.
- [Delta transaction log](/concepts/delta-transaction-log.md) — The `_delta_log/` directory that must be excluded from archival policies.

## Sources

- archival-support-in-databricks-databricks-on-aws.md

# Citations

1. [archival-support-in-databricks-databricks-on-aws.md](/references/archival-support-in-databricks-databricks-on-aws-d64d2061.md)

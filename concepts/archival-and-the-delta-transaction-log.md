---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8c49a6e32975870398f28a90bdcb40a19efa51eb57c9b0b5ae4964cbf112cbd5
  pageDirectory: concepts
  sources:
    - archival-support-in-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - archival-and-the-delta-transaction-log
    - the Delta Transaction Log and Archival
    - AATDTL
  citations:
    - file: archival-support-in-databricks-databricks-on-aws.md
title: Archival and the Delta Transaction Log
description: The critical constraint that the Delta transaction log directory (_delta_log/) must never be archived, as doing so makes the entire table inaccessible.
tags:
  - delta-lake
  - archival
  - transaction-log
  - limitations
timestamp: "2026-06-19T09:02:36.752Z"
---

# Archival and the Delta Transaction Log

**Archival and the Delta Transaction Log** refers to the critical relationship between cloud-based data archival lifecycle policies and the Delta transaction log (`_delta_log/` directory). When archival support is enabled for a [Delta Lake](/concepts/delta-lake.md) table, the transaction log must never be moved to an archived storage tier, as doing so renders the entire table inaccessible.

## Overview

[Archival Support in Databricks](/concepts/archival-support-in-databricks.md) enables the use of cloud-based lifecycle policies on object storage containing Delta tables. When configured, Databricks ignores files older than a specified period. However, this feature has a critical dependency on the integrity of the Delta transaction log.^[archival-support-in-databricks-databricks-on-aws.md]

## The Transaction Log Restriction

If any files in the Delta transaction log (`_delta_log/` directory) are moved to an archived storage tier, the table becomes entirely inaccessible and all queries against the table fail.^[archival-support-in-databricks-databricks-on-aws.md]

### Configuration Requirement

You must configure your cloud lifecycle policy so that the `_delta_log/` path is not included in archival. This is a mandatory requirement for archival support to function correctly.^[archival-support-in-databricks-databricks-on-aws.md]

## Why the Transaction Log Must Remain Accessible

The Delta transaction log is the foundation of Delta Lake Architecture, containing metadata about all data files, transactions, and table state. Without access to the transaction log, Databricks cannot:

- Determine which files belong to the table
- Read file statistics and metadata
- Identify which files are archived versus available
- Execute queries that avoid archived files

Archival support relies entirely on the information in the transaction log to identify files that can be safely ignored (those older than the `delta.timeUntilArchived` threshold) versus files that must be accessed.^[archival-support-in-databricks-databricks-on-aws.md]

## Consequences of Archived Transaction Log

When the transaction log is archived:

- **Complete table inaccessibility**: All queries against the table fail immediately
- **No partial recovery**: Unlike archived data files (which can be restored individually), an archived transaction log leaves the table in an unrecoverable state
- **No error reporting**: The table cannot even report which files need restoration

This contrasts with archived data files, where queries that can be answered without accessing archived data succeed, and `SHOW ARCHIVED FILES` can identify files needing restoration.^[archival-support-in-databricks-databricks-on-aws.md]

## Best Practices

### Lifecycle Policy Configuration

Configure S3 lifecycle policies to exclude the `_delta_log/` prefix. See AWS documentation on [examples of S3 Lifecycle configurations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-configuration-examples.html).^[archival-support-in-databricks-databricks-on-aws.md]

### Monitoring

Regularly verify that lifecycle policies have not inadvertently archived transaction log files. This is especially important when modifying existing lifecycle rules.

### Supported Archival Tiers

Archival support requires Amazon S3 Glacier Deep Archive or Glacier Flexible Retrieval. S3 Glacier Instant Retrieval does not require configuring archival support, though Databricks recommends using views to restrict queries against tables stored in Glacier Instant Retrieval with lifecycle policies configured.^[archival-support-in-databricks-databricks-on-aws.md]

## Unsupported Lifecycle Policies

Lifecycle management policies that are not based on file creation time are not supported. This includes:

- Access-time-based policies
- Tag-based policies

Amazon S3 Intelligent-Tiering optional asynchronous archive access tiers is also not compatible, as it archives based on access time rather than file creation time.^[archival-support-in-databricks-databricks-on-aws.md]

## Related Concepts

- [Delta transaction log](/concepts/delta-transaction-log.md) — The metadata foundation of Delta Lake
- [Archival Support in Databricks](/concepts/archival-support-in-databricks.md) — The broader archival feature
- [Delta Time Until Archived](/concepts/deltatimeuntilarchived.md) — The table property that controls archival behavior
- Restore archived files — Process for recovering archived data
- [Delta Lake table properties](/concepts/delta-lake-reader-table-features.md) — Configuration options for Delta tables

# Citations

1. [archival-support-in-databricks-databricks-on-aws.md](/references/archival-support-in-databricks-databricks-on-aws-d64d2061.md)

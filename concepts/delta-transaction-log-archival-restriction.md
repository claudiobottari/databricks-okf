---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ed474e1285d13274edaf8974d231c4f836632a3bb088f56456396890053de6ed
  pageDirectory: concepts
  sources:
    - archival-support-in-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-transaction-log-archival-restriction
    - DTLAR
  citations:
    - file: archival-support-in-databricks-databricks-on-aws.md
title: Delta transaction log archival restriction
description: The Delta transaction log (_delta_log/ directory) must never be archived; doing so makes the entire table inaccessible.
tags:
  - delta-lake
  - archival
  - transaction-log
  - limitations
timestamp: "2026-06-19T17:35:06.925Z"
---

# Delta Transaction Log Archival Restriction

**Delta Transaction Log Archival Restriction** refers to the critical rule that the Delta transaction log (`_delta_log/` directory) must never be moved to an archived storage tier when using cloud‑based lifecycle policies with Delta tables. Archiving the transaction log renders the entire table inaccessible and causes all queries to fail.^[archival-support-in-databricks-databricks-on-aws.md]

## Overview

Databricks provides [Archival support for Delta tables](/concepts/archival-support-for-delta-tables.md), allowing cloud lifecycle policies (e.g., S3 Glacier Deep Archive or Glacier Flexible Retrieval) to move old data files to cost‑efficient storage. This feature is in Public Preview for Databricks Runtime 13.3 LTS and above. Archival support helps reduce storage costs while still enabling queries that can be answered without scanning archived data files.^[archival-support-in-databricks-databricks-on-aws.md]

However, the Delta transaction log — the directory `_delta_log/` that records all table changes — is **not** covered by this support. The restriction is explicit: archival applies only to data files (e.g., Parquet files containing table rows).^[archival-support-in-databricks-databricks-on-aws.md]

## Critical Constraint

> **If any files in the Delta transaction log are moved to an archived storage tier, the table becomes entirely inaccessible and all queries against the table fail.**^[archival-support-in-databricks-databricks-on-aws.md]

This behavior is a hard limitation of the Delta Lake protocol on Databricks. Because the transaction log contains the metadata required to read the table — including schema, file listings, and version information — its unavailability breaks all read and write operations.

## Configuration Requirement

To avoid the restriction, you must configure your cloud lifecycle policy so that the `_delta_log/` path is **excluded** from archival. For AWS S3, this is done by setting appropriate rules in the S3 Lifecycle configuration (see [AWS documentation on lifecycle configuration examples](https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-configuration-examples.html)).^[archival-support-in-databricks-databricks-on-aws.md]

The archival support setting `delta.timeUntilArchived` on the table itself only controls how Databricks treats **data files** older than a specified interval. It does not affect the transaction log. The cloud‑side exclusion is separate and mandatory.^[archival-support-in-databricks-databricks-on-aws.md]

## Impact of Violating the Restriction

If the transaction log is accidentally archived:

- All queries against the table fail immediately.
- The table is effectively lost until the log files are restored from archival storage.
- Restoration requires using cloud provider APIs (e.g., S3 `RestoreObject`) to bring the log files back to a fast‑retrieval tier.

Databricks recommends carefully auditing lifecycle policies to ensure `_delta_log/` is never included in archival transitions.^[archival-support-in-databricks-databricks-on-aws.md]

## Related Concepts

- [Archival support for Delta tables](/concepts/archival-support-for-delta-tables.md) — The overall feature that enables cloud lifecycle policies on Delta data files.
- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md) — The metadata directory that must stay in hot storage.
- Lifecycle policies on object storage — Cloud provider rules for moving objects to cheaper tiers.
- S3 Glacier Deep Archive — One of the archival storage classes supported by Databricks.

## Sources

- archival-support-in-databricks-databricks-on-aws.md

# Citations

1. [archival-support-in-databricks-databricks-on-aws.md](/references/archival-support-in-databricks-databricks-on-aws-d64d2061.md)

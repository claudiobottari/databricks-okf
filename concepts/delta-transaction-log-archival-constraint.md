---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0823ffc811df9b76dbed373e2aa0cace92d0061af00816cbddb7b9d95ff9b773
  pageDirectory: concepts
  sources:
    - archival-support-in-databricks-databricks-on-aws.md
  confidence: 0.99
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-transaction-log-archival-constraint
    - DTLAC
  citations:
    - file: archival-support-in-databricks-databricks-on-aws.md
title: Delta transaction log archival constraint
description: Archiving any files in the _delta_log/ directory makes the entire Delta table inaccessible; cloud lifecycle policies must exclude the transaction log path from archival rules.
tags:
  - databricks
  - delta-lake
  - limitations
timestamp: "2026-06-18T10:47:34.059Z"
---

# Delta transaction log archival constraint

**Delta transaction log archival constraint** is a critical limitation of [Archival Support in Databricks](/concepts/archival-support-in-databricks.md): the Delta transaction log directory (`_delta_log/`) must never be moved to an archived storage tier. If any files in the transaction log are archived, the table becomes entirely inaccessible and all queries against the table fail.^[archival-support-in-databricks-databricks-on-aws.md]

## Why the constraint exists

Archival support in Databricks enables cloud-based lifecycle policies on object storage containing [Delta Lake](/concepts/delta-lake.md) tables. When enabled, Databricks ignores data files older than the specified `delta.timeUntilArchived` period. However, this optimization only applies to data files. The Delta transaction log contains the metadata required to read the table — including the list of data files, schema information, and transaction history. Without access to the transaction log, Databricks cannot determine the table's structure or which data files belong to it.^[archival-support-in-databricks-databricks-on-aws.md]

## Consequences of archiving the transaction log

If the `_delta_log/` directory is archived:

- **All queries fail**: Every operation against the table — including reads, writes, and metadata queries — becomes impossible.
- **No error recovery**: Unlike archived data files, which can be restored and automatically recognized by Databricks, an archived transaction log makes the table completely inaccessible until the log files are restored.
- **No partial access**: Even queries that only need metadata (such as `SHOW COLUMNS` or `SELECT COUNT(*)`) fail because they require the transaction log.^[archival-support-in-databricks-databricks-on-aws.md]

## Configuring lifecycle policies to avoid the constraint

When setting up cloud lifecycle management policies for object storage containing Delta tables, you must explicitly exclude the `_delta_log/` path from archival rules. For Amazon S3, this is done by configuring lifecycle rules that apply only to specific prefixes or by adding an exclusion filter for the `_delta_log/` directory.^[archival-support-in-databricks-databricks-on-aws.md]

Databricks provides examples of S3 lifecycle configurations that demonstrate how to exclude the transaction log path from archival policies.^[archival-support-in-databricks-databricks-on-aws.md]

## Relationship to data file archival

The transaction log archival constraint is separate from the archival of data files. Data files older than the `delta.timeUntilArchived` threshold can be safely archived, and Databricks will optimize queries to avoid scanning them when possible. Archived data files can also be restored using cloud provider APIs, and Databricks will automatically recognize the restored files. However, the transaction log must always remain in a fast-retrieval storage tier.^[archival-support-in-databricks-databricks-on-aws.md]

## Best practices

- **Always exclude `_delta_log/`** from cloud lifecycle archival policies.
- **Test lifecycle policies** on non-production tables first to verify the exclusion is working correctly.
- **Monitor archival status** using `SHOW ARCHIVED FILES` to identify any files that may have been incorrectly archived.
- **Set `delta.timeUntilArchived`** to match your cloud lifecycle policy's archival interval, but never set it to a value greater than the actual age of the most recently archived data.^[archival-support-in-databricks-databricks-on-aws.md]

## Related concepts

- [Archival Support in Databricks](/concepts/archival-support-in-databricks.md) — The broader feature for managing archived Delta table data
- [Delta Lake](/concepts/delta-lake.md) — The storage layer that uses the transaction log for metadata management
- [Delta transaction log](/concepts/delta-transaction-log.md) — The metadata directory that must remain accessible
- Delta table properties — Table properties including `delta.timeUntilArchived`
- Cloud lifecycle policies — Cloud provider policies for transitioning objects to archival storage

## Sources

- archival-support-in-databricks-databricks-on-aws.md

# Citations

1. [archival-support-in-databricks-databricks-on-aws.md](/references/archival-support-in-databricks-databricks-on-aws-d64d2061.md)

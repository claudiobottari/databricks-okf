---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ede313fff52ff760f368f41ef023c55a9517691c4f02a3fe4a03483adee0ce2d
  pageDirectory: concepts
  sources:
    - archival-support-in-databricks-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - archival-compatible-s3-storage-tiers
    - ASST
  citations:
    - file: archival-support-in-databricks-databricks-on-aws.md
title: Archival-compatible S3 storage tiers
description: Archival support requires S3 Glacier Deep Archive or Glacier Flexible Retrieval; Glacier Instant Retrieval works without configuration, and Amazon S3 Intelligent-Tiering async archive tiers are incompatible due to access-time-based archiving.
tags:
  - aws
  - s3
  - storage-tiers
  - databricks
timestamp: "2026-06-18T10:47:50.690Z"
---

# Archival-compatible S3 storage tiers

**Archival-compatible S3 storage tiers** are Amazon S3 storage classes that can be used with Databricks archival support for Delta tables. This feature is in **Public Preview** on Databricks Runtime 13.3 LTS and above. Archival support works by instructing Databricks to ignore files older than a specified period in a Delta table, enabling queries that can be answered without touching archived data. It requires that the underlying cloud lifecycle policy moves data to specific archival tiers based on file creation time. ^[archival-support-in-databricks-databricks-on-aws.md]

Only S3 Glacier Deep Archive and Glacier Flexible Retrieval are supported. Lifecycle policies that use other archival‑oriented tiers are either incompatible or require special handling. ^[archival-support-in-databricks-databricks-on-aws.md]

## Supported storage tiers

| S3 tier | Compatible with archival support? | Notes |
|---|---|---|
| S3 Glacier Deep Archive | Yes | Fully supported; queries fail early if they need archived files. |
| S3 Glacier Flexible Retrieval | Yes | Fully supported; same behavior as Glacier Deep Archive. |
| S3 Glacier Instant Retrieval | No special configuration needed | Archival support is not required because files are immediately retrievable. However, querying scans all files; Databricks recommends using views to restrict queries when lifecycle policies are configured. |
| S3 Intelligent‑Tiering (optional asynchronous archive access) | **No** | Incompatible because it archives based on access time, not file creation time. |

^[archival-support-in-databricks-databricks-on-aws.md]

## Requirements

To use archival-support with S3 Glacier Deep Archive or Glacier Flexible Retrieval:

- The cloud lifecycle policy must move data to one of these tiers **exclusively based on file creation time**. Access-time‑based or tag‑based policies are **not** supported. ^[archival-support-in-databricks-databricks-on-aws.md]
- The Delta transaction log (`_delta_log/` directory) must **never** be archived. If any files in the transaction log are moved to an archival tier, the table becomes completely inaccessible. ^[archival-support-in-databricks-databricks-on-aws.md]
- You must set the table property `delta.timeUntilArchived` to match the archival interval in your lifecycle policy (e.g., `ALTER TABLE t SET TBLPROPERTIES(delta.timeUntilArchived = '90 days')`). This tells Databricks to ignore files older than that interval. ^[archival-support-in-databricks-databricks-on-aws.md]

## How archival support interacts with these tiers

When archival support is enabled, Databricks optimizes queries to avoid scanning archived files:

- Queries that only need metadata or that filter on partition/ordering columns can succeed without touching archived files. ^[archival-support-in-databricks-databricks-on-aws.md]
- Queries that must scan archived files fail early with an error message. ^[archival-support-in-databricks-databricks-on-aws.md]
- Users can run `SHOW ARCHIVED FILES FOR table_name [ WHERE predicate ]` to identify which files must be restored from the archival tier. ^[archival-support-in-databricks-databricks-on-aws.md]
- After restoring files (using the S3 restore API), Databricks automatically detects the restored data through a sampling mechanism when preparing a scan. ^[archival-support-in-databricks-databricks-on-aws.md]

## Best practices

- **Do not mix archival policies with other tiers.** Using a supported archival tier alongside other tiers for the same table may cause unexpected results because Databricks treats all files older than `delta.timeUntilArchived` as archived, even if they are in a fast‑retrieval tier.
- **Never extend the lifecycle interval** after data has already been archived. If you change the policy to archive data later (e.g., from 60 days to 90 days), files that are already archived will remain in the archival tier, and Databricks will treat them as hot data, causing errors. Follow the guidelines in [Archival Support in Databricks](/concepts/archival-support-in-databricks.md) to handle interval changes safely.
- **Use Glacier Instant Retrieval only when necessary.** Because it does not require archival support, Databricks can query files directly, but the performance cost of scanning all files may be high. Use views to restrict query scope. ^[archival-support-in-databricks-databricks-on-aws.md]

## Limitations

- Only S3 Glacier Deep Archive and Glacier Flexible Retrieval are compatible. S3 Glacier Instant Retrieval does not require archival support, and S3 Intelligent‑Tiering asynchronous archive access is incompatible. ^[archival-support-in-databricks-databricks-on-aws.md]
- Lifecycle policies must be based on file **creation time**; access‑time or tag‑based policies are not supported. ^[archival-support-in-databricks-databricks-on-aws.md]
- `DROP COLUMN` is not allowed on tables with archived files. ^[archival-support-in-databricks-databricks-on-aws.md]
- `REORG TABLE APPLY PURGE` makes a best‑effort attempt but cannot delete archived deletion vector files. ^[archival-support-in-databricks-databricks-on-aws.md]
- `LIMIT` queries on tables with archival support enabled may return `DELTA_ARCHIVED_FILES_IN_LIMIT` errors if the table does not have enough unarchived rows. ^[archival-support-in-databricks-databricks-on-aws.md]

## Related concepts

- [Archival Support in Databricks](/concepts/archival-support-in-databricks.md) — The full feature overview, including enabling, querying, and restoring archived data.
- [Delta Lake](/concepts/delta-lake.md) — The storage layer that archival support works with.
- S3 Glacier Deep Archive — The lowest‑cost archival storage class supported.
- S3 Glacier Flexible Retrieval — A retrieval‑optimized archival tier supported by archival support.
- Lifecycle management — Configuring cloud lifecycle policies to move data to archival tiers.

## Sources

- archival-support-in-databricks-databricks-on-aws.md

# Citations

1. [archival-support-in-databricks-databricks-on-aws.md](/references/archival-support-in-databricks-databricks-on-aws-d64d2061.md)

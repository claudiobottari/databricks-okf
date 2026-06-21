---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b82287004bf0a5e088999561fa30f4ac685ccd91fe72de574d90947356866759
  pageDirectory: concepts
  sources:
    - reorg-table-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - idempotency-of-reorg-table
    - IORT
  citations:
    - file: reorg-table-databricks-on-aws.md
      start: 25
      end: 27
    - file: reorg-table-databricks-on-aws.md
      start: 49
      end: 51
    - file: reorg-table-databricks-on-aws.md
      start: 56
      end: 58
    - file: reorg-table-databricks-on-aws.md
      start: 28
      end: 29
title: Idempotency of REORG TABLE
description: The REORG TABLE command is idempotent, meaning running it twice on the same dataset has no effect on the second run.
tags:
  - delta-lake
  - idempotency
  - sql-command
timestamp: "2026-06-19T20:13:25.726Z"
---

# Idempotency of REORG TABLE

**Idempotency of REORG TABLE** is a property of the `REORG TABLE` command in [Delta Lake](/concepts/delta-lake.md) on Databricks. It guarantees that running the command multiple times on the same dataset produces the same result as running it once — the second and subsequent runs have no additional effect.^[reorg-table-databricks-on-aws.md#L25-L27]

## How Idempotency Applies to Each Operation

`REORG TABLE` supports three operations: `PURGE`, `UPGRADE UNIFORM`, and `CHECKPOINT`. Each operation is idempotent for its specific purpose.

- **`APPLY (PURGE)`** – Rewrites only files that contain soft‑deleted data (e.g., columns dropped by `ALTER TABLE DROP COLUMN`). If no soft‑deleted data is present, the operation does nothing. Running it a second time on the same dataset has no effect because the soft‑deleted data is already purged from the rewritten files.^[reorg-table-databricks-on-aws.md#L25-L27]
- **`APPLY (UPGRADE UNIFORM (ICEBERG_COMPAT_VERSION = version))`** – Rewrites files to upgrade the table to the specified Apache Iceberg version (1 or 2). Once the upgrade is complete, re‑running the same command has no effect because the table is already at the target version.^[reorg-table-databricks-on-aws.md#L49-L51]
- **`APPLY (CHECKPOINT)`** – Performs Delta checkpointing on the table’s latest Delta version. If the checkpoint is already up‑to‑date, a second run has no effect.^[reorg-table-databricks-on-aws.md#L56-L58]

## Relationship with VACUUM

Idempotency of `REORG TABLE` does not guarantee immediate physical deletion of old data. After running `APPLY (PURGE)`, the soft‑deleted data may still exist in old files until the VACUUM command is run to physically delete them. Running `REORG` again on the same data would have no effect, but VACUUM is a separate operation.^[reorg-table-databricks-on-aws.md#L28-L29]

## Use Cases

The idempotent nature of `REORG TABLE` makes it safe to schedule or retry without risk of side effects. Common use cases include:

- Automating the cleanup of dropped columns in a periodic maintenance job.
- Ensuring a table is always upgraded to a specific Iceberg version after schema changes.
- Lightweight checkpointing for metadata management.

Because the command has no effect on the second run, it can be triggered unconditionally in pipelines and workflows.

## Related Concepts

- [REORG TABLE](/concepts/reorg-table.md) – Full command reference, syntax, and parameters.
- [Delta Lake](/concepts/delta-lake.md) – Storage layer that supports `REORG TABLE`.
- VACUUM – Physical deletion of old data files after `APPLY (PURGE)`.
- Checkpoint V2 – Required for `APPLY (CHECKPOINT)` to avoid race conditions.
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) – Compatibility upgrade target for `APPLY (UPGRADE UNIFORM)`.

## Sources

- reorg-table-databricks-on-aws.md

# Citations

1. [reorg-table-databricks-on-aws.md:25-27](/references/reorg-table-databricks-on-aws-58d61683.md)
2. [reorg-table-databricks-on-aws.md:49-51](/references/reorg-table-databricks-on-aws-58d61683.md)
3. [reorg-table-databricks-on-aws.md:56-58](/references/reorg-table-databricks-on-aws-58d61683.md)
4. [reorg-table-databricks-on-aws.md:28-29](/references/reorg-table-databricks-on-aws-58d61683.md)

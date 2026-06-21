---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c8a81d050a1753a2d12f47ac85aff87310c81e55ed848b379e02cb6c7f471fc6
  pageDirectory: concepts
  sources:
    - reorg-table-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - vacuum-after-purge
    - VAP
  citations:
    - file: reorg-table-databricks-on-aws.md
title: VACUUM after PURGE
description: After running APPLY (PURGE), old files containing soft-deleted data may still exist and VACUUM should be used to physically delete them.
tags:
  - vacuum
  - delta-lake
  - data-purging
  - file-management
timestamp: "2026-06-19T20:13:52.672Z"
---

# VACUUM after PURGE

**VACUUM after PURGE** refers to the recommended workflow of running the `REORG TABLE ... APPLY (PURGE)` command followed by `VACUUM` to physically remove old files that still contain soft-deleted data. This two-step process is necessary because `REORG ... PURGE` only rewrites the active files to exclude the soft-deleted data (such as columns removed via `ALTER TABLE DROP COLUMN`) but does not delete the original files from storage. ^[reorg-table-databricks-on-aws.md]

## Overview

`REORG TABLE` with `APPLY (PURGE)` reorganizes a [Delta Lake Table](/concepts/delta-lake-table.md) by rewriting only the files that contain soft-deleted data. After this operation, the table’s logical state no longer includes the deleted data, but the old files remain on disk. Running `VACUUM` after `PURGE` physically deletes those old files, reclaiming storage space. ^[reorg-table-databricks-on-aws.md]

## Workflow

1. Run `REORG TABLE <table_name> APPLY (PURGE);` to rewrite files and purge soft-deleted data.
2. Then, run `VACUUM <table_name>;` to delete the old, unreferenced files.

The `REORG` command is idempotent — running it again on the same dataset has no effect. Similarly, `VACUUM` only removes files that are no longer needed by the Delta transaction log, so running it after `PURGE` safely and permanently eliminates the old data. ^[reorg-table-databricks-on-aws.md]

## Additional Notes

- `REORG ... APPLY (PURGE)` only rewrites files that contain soft-deleted data; it does not rewrite the entire table.
- The `WHERE` predicate option allows you to restrict the rewrite to specific partition(s) for `PURGE`, further optimizing the operation.
- After running `PURGE`, the old files still exist until `VACUUM` is explicitly called. This means storage is not freed until the second step is performed. ^[reorg-table-databricks-on-aws.md]

## Related Concepts

- [REORG TABLE](/concepts/reorg-table.md) – The command that performs the file rewrite for purging or upgrading.
- [PURGE](/concepts/apply-purge.md) – The operation that removes metadata-only deletes by rewriting files.
- VACUUM – The command that physically deletes unreferenced Delta Lake files.
- [Delta Lake](/concepts/delta-lake.md) – The storage layer that supports these operations.
- Soft-delete – Data that is logically removed but remains in old files until physically purged.

## Sources

- reorg-table-databricks-on-aws.md

# Citations

1. [reorg-table-databricks-on-aws.md](/references/reorg-table-databricks-on-aws-58d61683.md)

---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fc96f4c646f5b89da7c93c55193ae3c32df0ce3806157a3b5784f001c9d23ed5
  pageDirectory: concepts
  sources:
    - delta_concurrent_delete_delete-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - partitioned-table-merge-conflicts-in-delta-lake
    - PTMCIDL
    - PARTITIONED_TABLE_WITHOUT_MERGE_SOURCE
  citations:
    - file: delta_concurrent_delete_delete-error-condition-databricks-on-aws.md
title: Partitioned table merge conflicts in Delta Lake
description: A specific conflict sub-error (PARTITIONED_TABLE_WITHOUT_MERGE_SOURCE) that occurs when row-level conflict detection cannot be performed on a partitioned table during a MERGE operation.
tags:
  - delta-lake
  - partitioning
  - merge
timestamp: "2026-06-19T10:04:19.493Z"
---

# Partitioned table merge conflicts in Delta Lake

**Partitioned table merge conflicts in Delta Lake** occur when a concurrent transaction modifies data that a running `MERGE` operation on a partitioned table attempts to modify. Delta Lake uses [optimistic concurrency control](/concepts/delta-lake-optimistic-concurrency-control.md) and [row-level conflict detection](/concepts/delta-lake-row-level-conflict-detection.md) to resolve such conflicts, but in certain cases the conflict detector cannot analyze the partitioned table and returns a specific sub‑error of the `DELTA_CONCURRENT_DELETE_DELETE` error class.

## Error condition: `PARTITIONED_TABLE_WITHOUT_MERGE_SOURCE`

The `PARTITIONED_TABLE_WITHOUT_MERGE_SOURCE` sub‑error is raised when row-level conflict detection cannot be performed on a partitioned table during a `MERGE` operation. The full error message is:

```
Row-level conflict detection could not be performed on this partitioned table. Please retry the operation.
```

^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

### Cause

The error indicates that the table is partitioned, but the conflict detection mechanism was unable to use the merge source to identify which rows are affected. The exact reason is not detailed in the source material, but the error name *without merge source* suggests that the merge statement does not provide enough partition information for Delta Lake to narrow the conflict check. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

### Resolution

The documented resolution is to retry the operation. A subsequent attempt may succeed if the conflicting concurrent transaction has completed. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Related concepts

- [Delta Lake](/concepts/delta-lake.md) – The underlying storage engine that provides ACID transactions and conflict detection.
- [Merge (Delta Lake)](/concepts/merge-into-delta-lake.md) – The `MERGE` SQL command that upserts data.
- Partitioning (Delta Lake) – How tables are split into directories to improve performance and how it affects conflict detection.
- [Row-level conflict detection](/concepts/delta-lake-row-level-conflict-detection.md) – The mechanism Delta Lake uses to detect conflicts at the row level rather than the file level.
- DELTA_CONCURRENT_DELETE_DELETE Error Class|DELTA_CONCURRENT_DELETE_DELETE error class – The parent error class that includes all concurrent delete‑delete conflict sub‑errors.

## Sources

- delta_concurrent_delete_delete-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_delete_delete-error-condition-databricks-on-aws.md](/references/delta_concurrent_delete_delete-error-condition-databricks-on-aws-6fcec7a7.md)

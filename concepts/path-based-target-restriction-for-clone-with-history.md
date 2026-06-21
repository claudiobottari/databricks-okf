---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7b6958717df01dfd218c62d5c9da48804ca3caa1fba78923dfe0e4e6e40e6831
  pageDirectory: concepts
  sources:
    - delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - path-based-target-restriction-for-clone-with-history
    - PTRFCWH
  citations:
    - file: delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md
title: Path-based target restriction for clone with history
description: Cloning a Delta table with history to a path-based target table is not supported in Databricks.
tags:
  - databricks
  - delta-lake
  - restrictions
timestamp: "2026-06-18T15:17:45.247Z"
---

# Path-based target restriction for clone with history

**Path-based target restriction for clone with history** is an error condition that occurs when attempting to clone a Delta table with history enabled to a path-based target location. The DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_TARGET error class prevents users from using `CLONE` with `WITH HISTORY` when the target is specified as a file path rather than a registered table in the [Metastore](/concepts/metastore.md). ^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

## Error Details

- **SQLSTATE:** 0AKDC
- **Error class:** `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_TARGET`
- **Subclass:** `PATH_BASED` ^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

## Error Message

When this restriction is triggered, Databricks returns the following error:

```
Path-based target table is not supported.
```

^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

## Cause

The error occurs when a [Delta table clone](/concepts/delta-table-cloning.md) operation includes the `WITH HISTORY` clause (which preserves the full commit history of the source table) and specifies the target as a file path rather than as a table registered in the [Unity Catalog](/concepts/unity-catalog.md) or [Hive metastore](/concepts/built-in-hive-metastore.md). Path-based targets are not supported for clones that preserve history. ^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

## Related Error Conditions

The `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_TARGET` error class includes two additional error conditions for other unsupported target types: ^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

- **NON_DELTA:** Occurs when the target table is of a non-Delta format. ^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]
- **SESSION_TEMPORARY:** Occurs when the target is a session temporary table. ^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

## Solution

To clone a Delta table with its history, specify the target as a registered table name in the [Metastore](/concepts/metastore.md) instead of a file path. For example:

```sql
-- This will fail (path-based target)
CREATE OR REPLACE TABLE '/path/to/target' CLONE source_table WITH HISTORY;

-- This will succeed (metastore-registered target)
CREATE OR REPLACE TABLE catalog.schema.target_table CLONE source_table WITH HISTORY;
```

## Related Concepts

- [Delta table clone](/concepts/delta-table-cloning.md) — The operation that creates a copy of a Delta table
- [Clone with history](/concepts/delta-clone-with-history.md) — Cloning that preserves the source table's commit history
- [Delta Lake](/concepts/delta-lake.md) — The storage layer underlying Delta tables
- [Unity Catalog](/concepts/unity-catalog.md) — The [Metastore](/concepts/metastore.md) for registering tables
- DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_TARGET — The parent error class for unsupported target types

## Sources

- delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md

# Citations

1. [delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md](/references/delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws-797521da.md)

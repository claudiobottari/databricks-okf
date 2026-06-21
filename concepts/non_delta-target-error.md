---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9cb5ea3ca008c24303b0ee795255dd05e33171ed0d37a16fc4e84ca6f25e3c71
  pageDirectory: concepts
  sources:
    - delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - non_delta-target-error
    - NTE
  citations:
    - file: delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md
title: NON_DELTA target error
description: A subtype of DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_TARGET indicating the target table is not a Delta format table.
tags:
  - databricks
  - error-subtype
  - delta-lake
timestamp: "2026-06-18T11:51:00.480Z"
---

# NON_DELTA Target Error

**NON_DELTA target error** is an error condition that occurs when attempting to clone a Delta table with history to a target table that is not in the Delta format. The operation requires the target to also be a Delta table to preserve the commit history and time travel capabilities.

## Error Details

- **Error class:** `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_TARGET`
- **Error condition:** `NON_DELTA`
- **SQLSTATE:** `0AKDC` (Feature not supported)

## Message

```
Target table of non-delta format is not supported.
```

^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

## Cause

The `CLONE WITH HISTORY` operation requires both the source and target tables to be Delta tables. If the target table is in a non-Delta format (such as Parquet, CSV, JSON, or another format), the operation fails because non-Delta formats cannot maintain the commit history, versioning, and time travel metadata that the clone-with-history operation requires.

## Affected Operations

The error occurs when running `[CLONE](/concepts/deep-clone.md)` or `CREATE OR REPLACE TABLE ... [CLONE WITH HISTORY](/concepts/delta-clone-with-history.md)` where the target is an existing table that is not a Delta table, or when specifying a non-Delta format for the target.

## Solutions

### Convert the Target to Delta

If the target is an existing non-Delta table, convert it to Delta format before cloning:

```sql
CONVERT TO DELTA target_table;
```

Then retry the clone operation.

### Target a New Delta Table

Specify a target that does not already exist or explicitly creates a Delta table:

```sql
CREATE OR REPLACE TABLE new_target
CLONE WITH HISTORY source_table;
```

This creates a new Delta table as the target.

### Use a Different Location

Write the clone to a new location that will automatically create a Delta table:

```sql
CLONE WITH HISTORY source_table
TO LOCATION '/path/to/new/delta/target';
```

### Use Regular Clone (Without History)

If preserving history is not required and the target must remain in a non-Delta format, use a regular `CLONE` operation without the `WITH HISTORY` clause:

```sql
CREATE OR REPLACE TABLE non_delta_target
CLONE source_table;
```

## Related Error Conditions

The `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_TARGET` error class also includes the following related conditions:

| Condition | Description |
|-----------|-------------|
| `NON_DELTA` | Target table of non-Delta format is not supported |
| `PATH_BASED` | Path-based target table is not supported |
| `SESSION_TEMPORARY` | Session temporary target table is not supported |

See PATH_BASED target error and SESSION_TEMPORARY target error for details.

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The underlying storage format for Delta tables
- [CLONE](/concepts/deep-clone.md) — The Delta table cloning operation
- [Time Travel](/concepts/delta-lake-time-travel.md) — Delta Lake feature requiring history metadata
- [CONVERT TO DELTA](/concepts/convert-to-delta.md) — Converting non-Delta formats to Delta
- Table Formats in Unity Catalog — Supported table formats and their capabilities

## Sources

- delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md

# Citations

1. [delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md](/references/delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws-797521da.md)

---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 691e1587890973219ccb238be8baab50ab71faf19925e735c6ad7f4a07b52264
  pageDirectory: concepts
  sources:
    - delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - time_travelled_by_timestamp-error-sub-condition
    - TES
  citations:
    - file: delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md
title: TIME_TRAVELLED_BY_TIMESTAMP error sub-condition
description: A specific error sub-condition under DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE, raised when the source table uses timestamp-based time travel.
tags:
  - databricks
  - error-messages
  - delta-lake
  - time-travel
timestamp: "2026-06-18T11:50:51.901Z"
---

# TIME_TRAVELLED_BY_TIMESTAMP error sub-condition

The **TIME_TRAVELLED_BY_TIMESTAMP** error is a sub-condition of the DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE error class|DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE error class (SQLSTATE: 0AKDC) that occurs when attempting a `DEEP CLONE` with history from a source table that uses time travel based on a timestamp. The operation fails because the source table's timestamp-based time travel is not supported as a source for `DEEP CLONE` with history. ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

## Error Message

When this error occurs, Databricks returns the following message:

```
Source table time travelled by timestamp is not supported.
```

^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

## Cause

The error is triggered when you execute a `DEEP CLONE` with history operation on a [Delta table](/concepts/delta-lake-table.md) that is referenced at a specific point in time using a timestamp-based time travel query. The `DEEP CLONE` with history operation requires the source table to be a [Delta table](/concepts/delta-lake-table.md) that supports version-based time travel, but the operation encounters a source table that was accessed using timestamp-based time travel instead. ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

## Affected Operations

- [Deep Clone](/concepts/deep-clone.md) operations that include the `WITH HISTORY` clause
- [Delta table](/concepts/delta-lake-table.md) cloning operations that attempt to preserve source table history

## Solution

To resolve this error, use version-based time travel instead of timestamp-based time travel for the source table when performing a `DEEP CLONE` with history. Specify the source table using a version number rather than a timestamp. For example, instead of:

```sql
-- This will cause the error
CREATE OR REPLACE DEEP CLONE target_table WITH HISTORY FROM source_table TIMESTAMP AS OF '2024-01-01'
```

Use:

```sql
-- This will work correctly
CREATE OR REPLACE DEEP CLONE target_table WITH HISTORY FROM source_table VERSION AS OF 42
```

^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

## Related Sub-Conditions

The DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE error class|DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE error class also includes the NON_DELTA sub-condition, which occurs when the source table is not a Delta table format. ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

## Related Concepts

- [Deep Clone](/concepts/deep-clone.md) — The operation that creates a full copy of a Delta table including data files
- [Time travel](/concepts/delta-lake-time-travel.md) — The ability to query Delta tables as they existed at a previous point in time
- [Delta table](/concepts/delta-lake-table.md) — The storage format that supports ACID transactions and time travel
- [SQLSTATE 0AKDC](/concepts/sqlstate-0akdc.md) — The SQL state code for feature not supported errors

## Sources

- delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md](/references/delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws-0e0c9b78.md)

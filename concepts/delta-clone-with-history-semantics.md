---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 66d93b00ca74e749ae8e1a42a716092d38d30d552243f796e1efe7b72639f1aa
  pageDirectory: concepts
  sources:
    - delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md
  confidence: 0.8
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - delta-clone-with-history-semantics
    - DCWHS
  citations:
    - file: delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md
title: Delta CLONE WITH HISTORY semantics
description: The broader Databricks/Delta Lake feature of cloning a table including its full change history, which imposes restrictions on source format and access methods.
tags:
  - databricks
  - delta-lake
  - cloning
  - sql
timestamp: "2026-06-19T10:02:50.638Z"
---

# Delta CLONE WITH HISTORY semantics

**Delta CLONE WITH HISTORY** is a feature in [Delta Lake](/concepts/delta-lake.md) that creates a deep copy of a Delta table including its complete version history. Unlike a regular `CLONE` operation which creates a snapshot, `CLONE WITH HISTORY` preserves the source table's commit history in the target, enabling time travel and audit capabilities on the cloned table.

## Overview

The `CLONE WITH HISTORY` operation creates a full copy of a Delta table that includes not just the current data snapshot, but the complete lineage of changes. This allows the target table to support time travel queries (`VERSION AS OF`, `TIMESTAMP AS OF`) identical to the source. ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

## Restriction: Delta Format Required

`CLONE WITH HISTORY` only supports source tables in the **Delta format**. Attempting to clone a table in any other format (such as Parquet, CSV, JSON, or ORC) with the `WITH HISTORY` clause will fail. ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

### Error: NON_DELTA

When the source table is not a Delta table, the operation raises the `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE` error with the `NON_DELTA` condition:

> Source table of `<format>` format is not supported. ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

For non-Delta sources, use the standard `CLONE` (without `WITH HISTORY`) to create a snapshot-only copy.

## Restriction: Time Travel by Timestamp Not Supported

`CLONE WITH HISTORY` does **not** support source tables that are specified using time travel by timestamp. If you attempt to clone a table where the source is versioned using `TIMESTAMP AS OF`, the operation will fail. ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

### Error: TIME_TRAVELLED_BY_TIMESTAMP

When the source table is accessed via timestamp-based time travel, the operation raises the `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE` error with the `TIME_TRAVELLED_BY_TIMESTAMP` condition:

> Source table time travelled by timestamp is not supported. ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

### Workaround

Use version-based time travel (`VERSION AS OF`) instead of timestamp-based time travel when the source is a Delta table. For example: ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

```sql
-- Supported
CREATE OR REPLACE TABLE target_table
CLONE source_table VERSION AS OF 42
WITH HISTORY;

-- Not supported
CREATE OR REPLACE TABLE target_table
CLONE source_table TIMESTAMP AS OF '2026-01-19T10:00:00Z'
WITH HISTORY;  -- Will fail with TIME_TRAVELLED_BY_TIMESTAMP
```

## SQLSTATE

The error condition `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE` maps to SQLSTATE class **0AKDC**, which falls under the **Class 0A — Feature Not Supported** category. ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

## Best Practices

- **Verify source format**: Ensure the source table is a Delta table before using `CLONE WITH HISTORY`. Check the table format with `DESCRIBE EXTENDED <table_name>`.
- **Prefer version-based time travel**: When you need to clone a specific historical version with its history, use `VERSION AS OF` rather than `TIMESTAMP AS OF`.
- **Consider storage costs**: `CLONE WITH HISTORY` duplicates the entire table history, which can be significantly larger than a snapshot clone. Evaluate whether you need the full history versus just the current state.
- **Use for auditing and compliance**: Clone with history is ideal for creating isolated copies of tables for audit trails, compliance requirements, or testing environments where full version history must be preserved.

## Related Concepts

- Delta CLONE semantics — The standard clone operation without history
- [Delta Lake Time Travel](/concepts/delta-lake-time-travel.md) — Querying historical versions of Delta tables
- [Delta Lake versioning](/concepts/delta-table-versioning.md) — How Delta table versions are managed
- [Delta Lake DEEP CLONE vs SHALLOW CLONE](/concepts/delta-table-cloning.md) — Differences between clone types
- Delta Lake SQLSTATE error classes — Error classification system

## Sources

- delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md](/references/delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws-0e0c9b78.md)

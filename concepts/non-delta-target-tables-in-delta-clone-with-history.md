---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a11d25f464a3175dec79e49cf828d36528e66490f66fd3f40edf23e326539db9
  pageDirectory: concepts
  sources:
    - delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - non-delta-target-tables-in-delta-clone-with-history
    - NTTIDCWH
  citations:
    - file: delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md
title: Non-Delta target tables in Delta Clone with History
description: An error sub-condition (NON_DELTA) where the target table for a Delta Clone with History operation is not in Delta format
tags:
  - databricks
  - delta-lake
  - error-messages
timestamp: "2026-06-19T10:02:59.818Z"
---

# Non-Delta target tables in Delta Clone with History

**Non-Delta target tables in Delta Clone with History** refers to a specific error condition that occurs when attempting to use the `CLONE WITH HISTORY` operation on a target table that is not a Delta table. The operation requires the target to be a Delta table, and any other format will result in a `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_TARGET` error. ^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

## Error Details

When a `CLONE WITH HISTORY` operation targets a non-Delta table, the system returns the following error:

- **SQLSTATE**: 0AKDC (Feature Not Supported)
- **Error class**: `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_TARGET`
- **Subtype**: `NON_DELTA`

The error message states: "Target table of non-delta format is not supported." ^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

## Cause

The `CLONE WITH HISTORY` operation in [Delta Lake](/concepts/delta-lake.md) is designed to create a full copy of a source Delta table, including its complete version history. This operation requires the target to also be a Delta table to properly maintain the metadata, transaction log, and versioning information. Non-Delta table formats (such as Parquet, CSV, JSON, or other storage formats) cannot store this history information. ^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

## Related Error Subtypes

The `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_TARGET` error class includes two additional subtypes for other unsupported target scenarios:

- **`PATH_BASED`**: Path-based target tables are not supported for clone with history operations.
- **`SESSION_TEMPORARY`**: Session temporary target tables are not supported for clone with history operations.

## Solution

Ensure that the target table for a `CLONE WITH HISTORY` operation is a [Delta table](/concepts/delta-lake-table.md). If you need to clone data to a non-Delta format, consider using alternative approaches such as:

- Using a standard `CLONE` operation (without history) if history preservation is not required
- Performing an ETL operation to convert the data to the desired format after cloning to a Delta target
- Using CREATE TABLE AS SELECT or INSERT INTO operations to move data to non-Delta formats

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The underlying storage format that supports versioned data
- [Delta Clone](/concepts/delta-clone.md) — The operation for creating copies of Delta tables
- [Clone with History](/concepts/delta-clone-with-history.md) — The specific clone variant that preserves table history
- [Delta table](/concepts/delta-lake-table.md) — The required target format for clone with history operations
- Error classes in Databricks — The error handling framework that includes this error class

## Sources

- delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md

# Citations

1. [delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md](/references/delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws-797521da.md)

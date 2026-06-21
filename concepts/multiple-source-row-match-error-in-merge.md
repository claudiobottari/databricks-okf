---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c360baf77a842f033e4e7eff74d5479e1fef79046b184a4b4f5877d03734512f
  pageDirectory: concepts
  sources:
    - merge-into-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multiple-source-row-match-error-in-merge
    - MSRMEIM
    - DELTA_MULTIPLE_SOURCE_ROW_MATCHING_TARGET_ROW_IN_MERGE
  citations:
    - file: merge-into-databricks-on-aws.md
title: Multiple Source Row Match Error in MERGE
description: A MERGE operation fails with DELTA_MULTIPLE_SOURCE_ROW_MATCHING_TARGET_ROW_IN_MERGE error if more than one source row matches the same target row, requiring preprocessing of the source table to eliminate ambiguity.
tags:
  - delta-lake
  - error-handling
  - merge
timestamp: "2026-06-19T19:31:44.717Z"
---

# Multiple Source Row Match Error in MERGE

The **Multiple Source Row Match Error in MERGE** occurs when a `MERGE INTO` operation fails because more than one row in the source table matches the same row in the target table, based on the conditions specified in the `ON` and `WHEN MATCHED` clauses.

## Error Class

This error is returned as `DELTA_MULTIPLE_SOURCE_ROW_MATCHING_TARGET_ROW_IN_MERGE`. ^[merge-into-databricks-on-aws.md]

## Cause

According to SQL semantics, a `MERGE` operation is ambiguous when multiple source rows match a single target row, because it is unclear which source row should be used to update or delete the matched target row. Databricks Delta Lake enforces this constraint and raises the error when it detects such a condition. ^[merge-into-databricks-on-aws.md]

### Example Scenario

Consider a target table with a key column and a source table that contains multiple rows with the same key value. If the `MERGE` statement uses that key in the `ON` clause, each target row may match multiple source rows, causing the error. ^[merge-into-databricks-on-aws.md]

## Resolution

To resolve this error, preprocess the source table to eliminate the possibility of multiple matches. The recommended approach is to deduplicate the source data before applying the merge, retaining only the most recent or most relevant row for each key. ^[merge-into-databricks-on-aws.md]

### Change Data Capture Example

A common use case where this error arises is in Change Data Capture (CDC) workflows. The typical solution involves preprocessing the change dataset (the source) to retain only the latest change for each key before merging it into the target Delta table. ^[merge-into-databricks-on-aws.md]

For example, you can use a window function with `ROW_NUMBER()` to select only the most recent record for each key in the source dataset, then perform the `MERGE` using the deduplicated result. ^[merge-into-databricks-on-aws.md]

## Important Notes

- In Databricks Runtime 15.4 LTS and below, `MERGE` only considers conditions in the `ON` clause before evaluating multiple matches. ^[merge-into-databricks-on-aws.md]
- Unconditional `DELETE` actions in `WHEN MATCHED` clauses are an exception: Databricks allows multiple matches when matches are unconditionally deleted, because an unconditional delete is not ambiguous even with multiple matches. ^[merge-into-databricks-on-aws.md]

## Related Concepts

- [MERGE INTO](/concepts/merge-into-delta-lake.md) — The Delta Lake statement that performs upserts, updates, and deletes.
- Change Data Capture (CDC) — A pattern where this error frequently occurs.
- [Delta Lake](/concepts/delta-lake.md) — The storage layer that supports `MERGE` operations.
- [DELTA_MULTIPLE_SOURCE_ROW_MATCHING_TARGET_ROW_IN_MERGE](/concepts/multiple-source-row-match-error-in-merge.md) — The specific error class returned.

## Sources

- merge-into-databricks-on-aws.md

# Citations

1. [merge-into-databricks-on-aws.md](/references/merge-into-databricks-on-aws-b9eee097.md)

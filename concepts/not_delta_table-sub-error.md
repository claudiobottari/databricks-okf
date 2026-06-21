---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 96bf2f9df5b068ab270e7b05c7de55ed1c9c91a58f14de82d0d9756f7608728e
  pageDirectory: concepts
  sources:
    - delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - not_delta_table-sub-error
    - NOT_DELTA_TABLE sub-error
    - not_delta_table-error-reason
    - NER
    - Delta Lake Error Messages
  citations:
    - file: delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
title: NOT_DELTA_TABLE sub-error
description: A specific cause of DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED where the view does not reference a Delta table
tags:
  - error-messages
  - delta-lake
timestamp: "2026-06-19T10:08:30.841Z"
---

# NOT_DELTA_TABLE sub-error

The **NOT_DELTA_TABLE sub-error** is a specific error condition that occurs when using the `table_changes` function on a view that does not reference a [Delta table](/concepts/delta-lake-table.md). It is part of the `DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED` error class.

## Error Message

When this error occurs, the system returns the following message:

```
table_changes on view '<viewName>' is not supported.
```

The sub-error is reported as:

```
NOT_DELTA_TABLE: The view does not reference a Delta table.
```

^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Cause

The `table_changes` function requires the underlying data source to be a Delta table. If the view provided to `table_changes` is based on a non-Delta source — such as a Parquet file, a JDBC source, or any other format — the operation fails with this sub-error. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Solution

Ensure that the view passed to `table_changes` references a Delta table. This may involve:

- Recreating the view to query a Delta table instead of a non-Delta source.
- Converting the underlying data to [Delta Lake](/concepts/delta-lake.md) format using `CONVERT TO DELTA`.
- Verifying that all tables referenced by the view are Delta tables.

## Related Concepts

- DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED error class — The parent error class containing this sub-error
- table_changes function — The function that triggers this error when used on unsupported views
- [Delta Lake](/concepts/delta-lake.md) — The storage format required by `table_changes`
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) — The feature that enables `table_changes` functionality on Delta tables

## Sources

- delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md

# Citations

1. [delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md](/references/delta_table_changes_view_unsupported-error-condition-databricks-on-aws-c5e200eb.md)

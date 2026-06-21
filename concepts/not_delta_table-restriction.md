---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b477676f51d571e0b278a51e4c63901c6948ab57194c082ff17881658c789d16
  pageDirectory: concepts
  sources:
    - delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - not_delta_table-restriction
  citations:
    - file: delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
title: NOT_DELTA_TABLE restriction
description: A restriction that table_changes requires the target to be a Delta table; views referencing non-Delta tables are rejected.
tags:
  - delta-lake
  - restriction
  - error-subcondition
timestamp: "2026-06-19T18:27:24.776Z"
---

# NOT_DELTA_TABLE Restriction

The **NOT_DELTA_TABLE restriction** is an error condition that occurs when using the `table_changes` function on a view that does not reference a [Delta Table](/concepts/delta-lake-table.md). This restriction is part of the `DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED` error class in Databricks. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Error Message

When this restriction is triggered, Databricks returns the following error:

```
table_changes on view '<viewName>' is not supported.
NOT_DELTA_TABLE: The view does not reference a Delta table.
```

^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Cause

The `table_changes` function requires that the underlying data source be a [Delta Table](/concepts/delta-lake-table.md). If a view is defined on top of a non-Delta source — such as a Parquet file, JDBC source, or another non-Delta format — the `NOT_DELTA_TABLE` error is raised. The view must ultimately reference a Delta table for `table_changes` to work. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Related Restrictions

The `DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED` error class includes several other restrictions that can also prevent `table_changes` from working on views:

- MULTIPLE_RELATIONS error reason|MULTIPLE_RELATIONS restriction — The view references more than one relation.
- NON_DETERMINISTIC_EXPRESSIONS restriction — The view contains non-deterministic expressions.
- NOT_SHARED_VIEW error reason|NOT_SHARED_VIEW restriction — The view is not an OpenSharing view.
- SUBQUERY restriction — The view contains a subquery.
- UNSUPPORTED_OPERATOR constraint for table_changes|UNSUPPORTED_OPERATOR restriction — The view contains an operator that is not allowed.

## Resolution

To resolve the `NOT_DELTA_TABLE` restriction, ensure that the view referenced in the `table_changes` call ultimately points to a Delta table. This may involve:

1. Recreating the view to reference a Delta table instead of a non-Delta source.
2. Converting the underlying data source to [Delta Lake format](/concepts/delta-lake.md).
3. Using `table_changes` directly on the Delta table rather than through a view.

## Related Concepts

- table_changes function — The function used to read change data feed from Delta tables.
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) — The feature that tracks row-level changes in Delta tables.
- [Delta Lake](/concepts/delta-lake.md) — The storage layer that supports change data capture.
- [SQLSTATE 0AKDC](/concepts/sqlstate-0akdc.md) — The SQL state associated with feature not supported errors.

## Sources

- delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md

# Citations

1. [delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md](/references/delta_table_changes_view_unsupported-error-condition-databricks-on-aws-c5e200eb.md)

---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 22ab23fe99b8cfac88d6ebfe89c86b6ba7ba029776373ee8b9a8a162d03b65be
  pageDirectory: concepts
  sources:
    - delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta_table_changes_view_unsupported-error
    - DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED error condition
  citations:
    - file: delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
title: DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED error
description: A Databricks error raised when the table_changes function is used on a view instead of a Delta table.
tags:
  - error-message
  - databricks
  - delta-lake
timestamp: "2026-06-19T18:27:18.624Z"
---

# DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED Error

The **`DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED`** error occurs when the `table_changes` function is applied to a view that is not eligible for change data capture. The error message is: `table_changes on view '<viewName>' is not supported.` This error belongs to SQL state class `0AKDC` (Feature not supported). ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Common Causes

The error is raised because the view fails one or more requirements for use with `table_changes`. The error includes a sub‑reason that identifies the specific violation: ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

| Sub‑reason | Description |
|---|---|
| `MULTIPLE_RELATIONS` | The view references more than one underlying relation. `table_changes` can only track changes from a single Delta table. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md] |
| `NON_DETERMINISTIC_EXPRESSIONS` | The view contains non‑deterministic expressions (e.g., `rand()`, `current_timestamp()`), making it impossible to reliably map rows to the source table’s changes. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md] |
| `NOT_DELTA_TABLE` | The view does not reference a Delta table. `table_changes` is only defined for Delta Lake tables. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md] |
| `NOT_SHARED_VIEW` | The view is not an Open Sharing view. `table_changes` on views is supported only through the Delta Sharing protocol. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md] |
| `SUBQUERY` | The view contains a subquery, which prevents a direct lineage to the source Delta table. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md] |
| `UNSUPPORTED_OPERATOR` | The view uses an operator (e.g., aggregation, join) that is not allowed for change tracking. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md] |

## Resolution

To resolve the error, ensure the view meets all of the following criteria:

1. The view references exactly one Delta table.
2. The view contains only deterministic expressions.
3. The view is an [Open Sharing view](/concepts/opensharing-views.md) (Delta Sharing).
4. The view does not contain subqueries.
5. The view uses only operators that are supported by `table_changes`.

If you need change data capture on a view that does not satisfy these constraints, consider using `table_changes` directly on the underlying Delta table, or redesigning your data pipeline to produce a compliant view. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Related Concepts

- table_changes function – The SQL function that raises this error.
- [Delta Sharing](/concepts/delta-sharing.md) – The protocol that enables change data capture on shared views.
- [Delta table](/concepts/delta-lake-table.md) – The underlying storage format required by `table_changes`.
- Error conditions in Databricks – General information on error handling.

## Sources

- delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md

# Citations

1. [delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md](/references/delta_table_changes_view_unsupported-error-condition-databricks-on-aws-c5e200eb.md)

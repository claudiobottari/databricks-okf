---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b8731bb4c9976bdf16844fd93b11a36b98a4060f91fe3be798b7298bdc20bffe
  pageDirectory: concepts
  sources:
    - delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta_table_changes_view_unsupported-error-class
    - DEC
    - DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED error class
    - DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED|DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED error class
  citations:
    - file: delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
title: DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED error class
description: A Databricks error indicating that the table_changes function cannot be applied to views, with multiple specific sub-reasons.
tags:
  - databricks
  - error-messages
  - delta-lake
timestamp: "2026-06-18T15:22:41.547Z"
---

# DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED Error Class

The **DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED** error class occurs when using `table_changes` on a view, which is not supported. The error message states: `table_changes on view '<viewName>' is not supported.` This error is associated with SQLSTATE 0AKDC (Feature Not Supported). ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Error Subtypes

The `DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED` error class includes several specific sub-conditions that describe why the view is incompatible with `table_changes`. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

### MULTIPLE_RELATIONS

The view references more than one relation. `table_changes` requires the view to be based on a single [Delta table](/concepts/delta-lake-table.md). ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

### NON_DETERMINISTIC_EXPRESSIONS

The view contains non-deterministic expressions, which are not supported by `table_changes`. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

### NOT_DELTA_TABLE

The view does not reference a [Delta table](/concepts/delta-lake-table.md). `table_changes` can only operate on Delta tables. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

### NOT_SHARED_VIEW

The view is not an OpenSharing view. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

### SUBQUERY

The view contains a subquery, which is not supported by `table_changes`. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

### UNSUPPORTED_OPERATOR

The view contains an operator that is not allowed for use with `table_changes`. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Cause

The `table_changes` function is designed to retrieve change data feed (CDF) records from [Delta tables](/concepts/delta-lake-table.md) directly. When applied to a view, it fails because the view may contain constructs that prevent Databricks from determining the underlying change stream. Common causes include views referencing multiple tables, containing subqueries, using non-deterministic expressions, or not being backed by a Delta table at all.

## Solution

To resolve this error, restructure the query to apply `table_changes` directly to the underlying [Delta table](/concepts/delta-lake-table.md) rather than to a view. Instead of querying the view with `table_changes`, apply the function to the source Delta table and then apply any filtering or transformations needed.

For example, replace:
```sql
SELECT * FROM table_changes('my_view', ...);
```

With:
```sql
SELECT * FROM table_changes('my_delta_table', ...);
```

If the view logic is required, consider applying it as a subsequent transformation on the results of the `table_changes` call.

## Related Concepts

- [Delta table](/concepts/delta-lake-table.md) — The underlying table type required by `table_changes`
- [Change Data Feed (CDF)](/concepts/delta-change-data-feed-cdf.md) — The feature that `table_changes` uses to track row-level changes
- [SQLSTATE 0AKDC](/concepts/sqlstate-0akdc.md) — The SQLSTATE class for feature not supported errors
- [OpenSharing view](/concepts/opensharing-views.md) — A view type that may be compatible with `table_changes`

## Sources

- delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md

# Citations

1. [delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md](/references/delta_table_changes_view_unsupported-error-condition-databricks-on-aws-c5e200eb.md)

---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0833ac8857bea14e203a8dcb1b151e14fc545708673a95c1fa232ed6c249e05a
  pageDirectory: concepts
  sources:
    - delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - subquery-constraint-for-table_changes
    - SCFT
    - SUBQUERY constraint for table_changes
    - SUBQUERY constraint for table_changes|SUBQUERY
  citations:
    - file: delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
title: SUBQUERY constraint for table_changes
description: A validation rule requiring that views used with table_changes must not contain subqueries
tags:
  - databricks
  - validation
  - view-constraints
timestamp: "2026-06-19T15:07:49.480Z"
---

# SUBQUERY constraint for table_changes

The **SUBQUERY constraint for `table_changes`** is one of the reasons the `table_changes` function fails on a view. When a view contains a subquery, Databricks raises a `DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED` error with the subreason `SUBQUERY`. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Error details

The full error message is:

```
table_changes on view '<viewName>' is not supported.
```

The error belongs to SQLSTATE class `0AKDC` (feature not supported). ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Reason

The specific subreason `SUBQUERY` indicates that the view definition contains a subquery. `table_changes` requires the underlying relation to be a direct Delta table reference, and any subquery in the view makes it ineligible for change data capture. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Other constraints in the same error class

`DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED` can also occur for the following additional reasons, each with its own subreason:

| Subreason | Meaning |
|-----------|---------|
| `MULTIPLE_RELATIONS` | The view references more than one table or relation. |
| `NON_DETERMINISTIC_EXPRESSIONS` | The view contains non-deterministic expressions. |
| `NOT_DELTA_TABLE` | The view does not reference a [Delta Lake](/concepts/delta-lake.md) table. |
| `NOT_SHARED_VIEW` | The view is not an [OpenSharing](/concepts/opensharing.md) view. |
| `UNSUPPORTED_OPERATOR` | The view uses an operator that is not allowed. |

^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

To use `table_changes`, the view must be a simple, deterministic projection of a single Delta table that also participates in Delta Sharing. Any subquery or other unsupported construct will cause the error. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Related concepts

- table_changes function — the function that reads change data from Delta tables or views
- [Delta Lake](/concepts/delta-lake.md) — the underlying storage format required by `table_changes`
- VIEW (Delta Sharing) — shared views that can be used with `table_changes` if they meet the constraints
- Subquery — SQL subquery construct that triggers this error when present in a view definition
- [SQLSTATE 0AKDC](/concepts/sqlstate-0akdc.md) — the SQLSTATE class for feature not supported errors

## Sources

- delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md

# Citations

1. [delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md](/references/delta_table_changes_view_unsupported-error-condition-databricks-on-aws-c5e200eb.md)

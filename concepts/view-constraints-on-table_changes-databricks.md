---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2a1ae91f2539ccf0accbb20d14814e84d812678d618841e07da251a1eab2ff3e
  pageDirectory: concepts
  sources:
    - delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - view-constraints-on-table_changes-databricks
    - VCOT(
  citations:
    - file: delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
title: View constraints on table_changes (Databricks)
description: "Databricks enumerates specific view features that make a view incompatible with the table_changes function: multiple relations, non-deterministic expressions, non-Delta tables, non-shared views, subqueries, and unsupported operators."
tags:
  - databricks
  - views
  - delta-lake
  - constraints
timestamp: "2026-06-18T15:22:33.158Z"
---

Here is the wiki page for "View constraints on table_changes (Databricks)", written based solely on the provided source material.

---

## View constraints on `table_changes` (Databricks)

**View constraints on `table_changes`** refers to the restrictions that Databricks enforces when using the `table_changes` function on a view rather than a Delta table. The function `table_changes` is designed to read the change data feed of a Delta table, and when applied to a view, the view must meet strict requirements. If the view does not satisfy these constraints, Databricks raises the `DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED` error. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

### Error Condition

The error message is:

```
table_changes on view '<viewName>' is not supported.
```

This error belongs to SQLSTATE class `0AKDC` (Feature not supported). ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

### Specific Constraint Violations

The `DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED` error class includes several sub-conditions that describe why the view is incompatible with `table_changes`:

| Sub-condition | Description |
|---|---|
| `MULTIPLE_RELATIONS` | The view references more than one relation (table or view). |
| `NON_DETERMINISTIC_EXPRESSIONS` | The view contains non-deterministic expressions. |
| `NOT_DELTA_TABLE` | The view does not reference a Delta table. |
| `NOT_SHARED_VIEW` | The view is not an OpenSharing view. |
| `SUBQUERY` | The view contains a subquery. |
| `UNSUPPORTED_OPERATOR` | The view contains an operator that is not allowed. |

^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

### Requirements for a Valid View

To use `table_changes` on a view, the view must:

- Reference exactly one relation (a single Delta table).
- Contain only deterministic expressions.
- Reference a Delta table (not a non-Delta table or another view type).
- Be an OpenSharing view.
- Contain no subqueries.
- Contain only supported operators.

If any of these conditions are violated, the `DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED` error is raised with the corresponding sub-condition. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

### Related Concepts

- [Change Data Feed (Databricks)](/concepts/change-data-feed-metadata-conflict.md) — The underlying feature that `table_changes` reads from.
- [Delta table](/concepts/delta-lake-table.md) — The required underlying table type for the view.
- [OpenSharing](/concepts/opensharing.md) — The sharing protocol required for the view.
- table_changes function — The function that reads change data from Delta tables.
- SQLSTATE error classes — The error classification system used by Databricks.

### Sources

- delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md

# Citations

1. [delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md](/references/delta_table_changes_view_unsupported-error-condition-databricks-on-aws-c5e200eb.md)

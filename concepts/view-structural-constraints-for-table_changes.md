---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bf03f48d499ad6039b859fb72e11cbaf5964a2864c0574c761640f2607f9c993
  pageDirectory: concepts
  sources:
    - delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - view-structural-constraints-for-table_changes
    - VSCFT
    - View limitations for table_changes
  citations:
    - file: delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
title: View structural constraints for table_changes
description: Views used with table_changes must reference a single relation, avoid subqueries, and avoid unsupported operators.
tags:
  - view
  - structural-constraints
  - error-subcondition
timestamp: "2026-06-19T18:27:31.433Z"
---

# View Structural Constraints for `table_changes`

The **`table_changes`** function in Databricks imposes specific structural constraints on the views it can operate on. When a view does not meet these constraints, the system raises the `DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED` error with a detailed sub-reason explaining which constraint was violated. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Error Overview

The error message `table_changes on view '<viewName>' is not supported` indicates that the view referenced in a `table_changes` query does not satisfy the required structural properties. The error class provides several sub-reasons that identify the specific violation. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Constraint Types

### MULTIPLE_RELATIONS

The view references more than one relation. `table_changes` requires that the view be based on a single underlying table or view. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

### NON_DETERMINISTIC_EXPRESSIONS

The view contains non-deterministic expressions, such as `rand()`, `now()`, or `current_timestamp()`. These expressions produce different results on each evaluation, which is incompatible with the change tracking semantics of `table_changes`. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

### NOT_DELTA_TABLE

The view does not reference a [Delta Table](/concepts/delta-lake-table.md). `table_changes` only supports views that ultimately resolve to a Delta table as their data source. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

### NOT_SHARED_VIEW

The view is not an [Open Sharing](/concepts/opensharing.md) view. `table_changes` requires that the view be shared using the Delta Sharing protocol. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

### SUBQUERY

The view contains a subquery. `table_changes` does not support views that include subqueries in their definition. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

### UNSUPPORTED_OPERATOR

The view contains an operator that is not allowed. This is a catch-all for operators or SQL constructs that are incompatible with `table_changes` beyond the specific cases listed above. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Related Concepts

- table_changes function — The function that reads change data from Delta tables
- [Delta Table](/concepts/delta-lake-table.md) — The underlying storage format required by `table_changes`
- Change Data Capture (CDC) — The broader pattern that `table_changes` supports
- [Open Sharing](/concepts/opensharing.md) — The sharing protocol required for shared views
- [Delta Sharing](/concepts/delta-sharing.md) — The data sharing platform that enables shared views

## Sources

- delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md

# Citations

1. [delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md](/references/delta_table_changes_view_unsupported-error-condition-databricks-on-aws-c5e200eb.md)

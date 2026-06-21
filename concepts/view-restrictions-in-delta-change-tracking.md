---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 22a346faf5582a49208ad1df0669e4ec525d48c489e20373001b5a8bcc4ca5f0
  pageDirectory: concepts
  sources:
    - delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - view-restrictions-in-delta-change-tracking
    - VRIDCT
  citations:
    - file: delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
title: View Restrictions in Delta Change Tracking
description: Constraints that prevent using table_changes on views, including multi-relation references, non-deterministic expressions, subqueries, unsupported operators, and non-Delta/non-shared views
tags:
  - databricks
  - delta-lake
  - views
  - restrictions
timestamp: "2026-06-18T11:55:54.684Z"
---

# View Restrictions in Delta Change Tracking

**View Restrictions in Delta Change Tracking** describes the conditions under which the `table_changes` function cannot be used on a view. When `table_changes` is called on a view that does not meet specific requirements, the system throws a `DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED` error (SQLSTATE: 0AKDC). ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Error

```
DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED
table_changes on view '<viewName>' is not supported.
```

The error is accompanied by the SQLSTATE class **0A — Feature not supported**. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Restrictions

The following restrictions apply to views used with `table_changes`. If any condition is true, the operation is rejected.

### MULTIPLE_RELATIONS
The view references more than one underlying relation (for example, it joins multiple tables). `table_changes` requires a one-to-one mapping between the view and a single Delta table. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

### NON_DETERMINISTIC_EXPRESSIONS
The view contains non-deterministic expressions (for example, `rand()` or `current_timestamp()`). Change tracking requires deterministic column semantics to correctly identify row changes. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

### NOT_DELTA_TABLE
The view does not reference a [Delta table](/concepts/delta-lake-table.md). `table_changes` is a Delta Lake feature that works only on Delta tables. If the view points to a non-Delta source (e.g., a Parquet table or a view on top of external data), the operation fails. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

### NOT_SHARED_VIEW
The view is not an Open Sharing view. `table_changes` on a shared view requires the view to be defined using the Open Sharing protocol. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

### SUBQUERY
The view contains a subquery. Only a direct, flat projection against a single Delta table is allowed. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

### UNSUPPORTED_OPERATOR
The view contains an operator that is not allowed in the context of change tracking (for example, aggregation, window functions, `DISTINCT`, or other non-projection operations). ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Related Concepts

- Delta Change Tracking — The feature that captures row-level changes in Delta tables
- table_changes function — The SQL function that retrieves change data
- [Delta table](/concepts/delta-lake-table.md) — The underlying storage format required for change tracking
- [Views in Unity Catalog](/concepts/views-in-unity-catalog.md) — How views interact with Delta functionality
- [Open Sharing](/concepts/opensharing.md) — The protocol required for shared views
- SQLSTATE error classes — Databricks error classification system

## Sources

- delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md

# Citations

1. [delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md](/references/delta_table_changes_view_unsupported-error-condition-databricks-on-aws-c5e200eb.md)

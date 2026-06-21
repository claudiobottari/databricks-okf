---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8243cef145f9edec513fd3be218ddabd86e44b4524d205c3fecc0f2627980c74
  pageDirectory: concepts
  sources:
    - delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - table_changes-function-databricks
    - TF(
  citations:
    - file: delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
title: table_changes function (Databricks)
description: A Databricks function used to retrieve change data feed (CDF) records from Delta tables, which is unsupported on views.
tags:
  - databricks
  - delta-lake
  - change-data-feed
timestamp: "2026-06-18T15:22:31.782Z"
---

---
title: table_changes function (Databricks)
summary: A Delta Lake SQL function that returns change data feed records. When called on a view, it may fail with the DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED error if the view does not satisfy strict requirements.
sources:
  - delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
kind: concept
createdAt: "2026-06-17T08:00:00.000Z"
updatedAt: "2026-06-17T08:00:00.000Z"
tags:
  - databricks
  - delta-lake
  - change-data-feed
  - sql-functions
  - error
aliases:
  - table-changes-function-databricks
  - delta-table-changes-view-unsupported
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# table_changes function (Databricks)

The `table_changes` function is a [Delta Lake](/concepts/delta-lake.md) SQL function in Databricks that returns records from the [change data feed](/concepts/delta-change-data-feed-cdf.md) of a Delta table. It allows users to query the set of inserted, updated, and deleted rows that occurred after a specified starting version or timestamp. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

While `table_changes` can be invoked directly on a Delta table, it can also be called on a view — provided the view satisfies a strict set of constraints. When the view does not meet these constraints, the function raises the **DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED** error (SQLSTATE: 0AKDC). ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Error: DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED

The error message states: `table_changes on view '<viewName>' is not supported.` It occurs when the view references more than one relation, contains non‑deterministic expressions, includes subqueries or disallowed operators, does not reference a Delta table, or is not an [Open Sharing](/concepts/opensharing.md) view. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

### Sub‑conditions

Each sub‑condition uses a specific reason code that refines the underlying problem:

| Sub‑condition | Meaning |
|---------------|---------|
| `MULTIPLE_RELATIONS` | The view references more than one relation (e.g., multiple tables or views). ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md] |
| `NON_DETERMINISTIC_EXPRESSIONS` | The view contains non‑deterministic expressions (e.g., `rand()`, `current_timestamp()`). ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md] |
| `NOT_DELTA_TABLE` | The view does not reference a Delta table (e.g., it references a Parquet, CSV, or other non‑Delta source). ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md] |
| `NOT_SHARED_VIEW` | The view is not an Open Sharing view. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md] |
| `SUBQUERY` | The view contains a subquery. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md] |
| `UNSUPPORTED_OPERATOR` | The view contains an operator that is not allowed (e.g., `EXCEPT`, `INTERSECT`, certain aggregations). ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md] |

## Requirements for views

To use `table_changes` on a view successfully, the view must:

1. Reference exactly one Delta table (no joins, unions, or other multi‑relation structures).
2. Contain only deterministic expressions.
3. Contain no subqueries.
4. Contain no unsupported operators.
5. Be defined as an Open Sharing view (i.e., created with the `SHARE` clause or otherwise marked as shareable).

If the view meets all these conditions, `table_changes` can operate on it just as it would on the underlying Delta table. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Related concepts

- [Change data feed](/concepts/delta-change-data-feed-cdf.md) – The mechanism that records row-level changes in Delta tables.
- [Delta table](/concepts/delta-lake-table.md) – The source format required for `table_changes`.
- [Open Sharing](/concepts/opensharing.md) – The protocol that allows Delta tables and views to be shared across platforms.
- SQLSTATE error classes – The error classification system used by Databricks SQL.

## Sources

- delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md

# Citations

1. [delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md](/references/delta_table_changes_view_unsupported-error-condition-databricks-on-aws-c5e200eb.md)

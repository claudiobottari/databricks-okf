---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cb907b13b47b064e313ba4a1535c22cb381fc8084c2ef021506e23ebf751b03d
  pageDirectory: concepts
  sources:
    - delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - view-determinism-requirement-for-table_changes
    - VDRFT
  citations:
    - file: delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
title: View determinism requirement for table_changes
description: Views used with table_changes must be deterministic; non-deterministic expressions cause a NON_DETERMINISTIC_EXPRESSIONS error.
tags:
  - view
  - determinism
  - error-subcondition
timestamp: "2026-06-19T18:27:31.998Z"
---

# View Determinism Requirement for `table_changes`

The **view determinism requirement for `table_changes`** is one of several conditions that a view must satisfy for the `table_changes` function to be supported on it. The function `table_changes` is designed to work directly on Delta tables, but it can also be applied to views if the view is a simple, deterministic projection of a single Delta table. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

When a view violates the determinism requirement — or any of the other supported-view requirements — the engine raises the `DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED` error with a sub‑error indicating the specific cause. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

---

## Determinism Requirement (NON_DETERMINISTIC_EXPRESSIONS)

A view must not contain non‑deterministic expressions. Functions such as `rand()`, `uuid()`, `current_timestamp()`, or any expression that does not always return the same result for the same input make the view non‑deterministic. Because `table_changes` needs to produce consistent, repeatable change tracking results over a series of queries, non‑deterministic expressions are prohibited. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

---

## Other Requirements

In addition to determinism, a view must meet all of the following conditions to be eligible for `table_changes`:

### Single‑Relation Restriction (MULTIPLE_RELATIONS)

The view must reference **exactly one** base relation (one Delta table). A view that joins, unions, or otherwise combines multiple tables is not supported. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

### Underlying Table Must Be a Delta Table (NOT_DELTA_TABLE)

The single relation that the view references must be a [Delta Lake](/concepts/delta-lake.md) table. Views over non‑Delta sources (e.g., CSV, Parquet, or external systems) are not allowed. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

### View Must Be an Open Sharing View (NOT_SHARED_VIEW)

Only views that are defined as **Open Sharing views** are eligible. Non‑shared or restricted views cannot be used with `table_changes`. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

### Subquery Prohibition (SUBQUERY)

The view must not contain any subqueries. Subqueries introduce additional complexity and potential ambiguity that the change‑tracking mechanism cannot handle. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

### Operator Restriction (UNSUPPORTED_OPERATOR)

The view must not use operators that are not explicitly allowed. This includes, but is not limited to, aggregations, window functions, `DISTINCT`, `ORDER BY`, `LIMIT`, set operations (`UNION`, `INTERSECT`, `EXCEPT`) on top of the single Delta table, as well as certain logical transformations that break the direct lineage to the source Delta table. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

---

## Practical Guidance

To use `table_changes` on a view, the view should be a simple, deterministic `SELECT` of columns from a single Delta table, with no filters, joins, subqueries, non‑deterministic functions, or unsupported operators. The view must be created as an Open Sharing view. Even simple projections are acceptable as long as they preserve the one‑to‑one correspondence with the underlying Delta table’s row‑level changes.

If any of the conditions above is violated, the engine returns the `DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED` error with the corresponding sub‑cause. Users can inspect the sub‑error message to identify which requirement was not met and adjust the view definition accordingly. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

---

## Related Concepts

- table_changes function|table_changes – The function that provides change‑data‑capture on Delta tables and eligible views.
- [Delta Lake Change Data Feed](/concepts/delta-lake-change-data-feed-cdf.md) – The underlying feature that records row‑level changes.
- [Delta Lake Views](/concepts/delta-lake.md) – General use and limitations of views over Delta tables.
- DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED – The error class raised when a view does not meet the requirements.

## Sources

- delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md

# Citations

1. [delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md](/references/delta_table_changes_view_unsupported-error-condition-databricks-on-aws-c5e200eb.md)

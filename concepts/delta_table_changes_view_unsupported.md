---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e737476858eec896ad1776b9f77b6bf23da9f11d88d6bd2c05de90b96208d8a4
  pageDirectory: concepts
  sources:
    - delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta_table_changes_view_unsupported
    - DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED
    - delta_table_changes_view_unsupported-error-class
    - DEC
    - DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED error class
    - DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED|DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED error class
    - delta_table_changes_view_unsupported-error
    - DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED error condition
  citations:
    - file: delta-table-changes-view-unsupported-error-condition-databricks-on-aws.md
title: DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED
description: An error class in Databricks that occurs when table_changes is called on a view that does not meet the required criteria (single relation, deterministic, references a Delta table, etc.)
tags:
  - databricks
  - error-class
  - delta-lake
timestamp: "2026-06-19T15:07:41.737Z"
---

# DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED error condition

**DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED** is an error class that occurs when the `table_changes` function is invoked on a view that does not meet the required criteria for reading [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) from a [Delta table](/concepts/delta-lake-table.md). The function is designed to read change data from Delta tables, but the target object is an unsupported view. ^[delta-table-changes-view-unsupported-error-condition-databricks-on-aws.md]

## SQLSTATE

The error has [SQLSTATE class 0A (feature not supported)](https://docs.databricks.com/aws/en/error-messages/sqlstates#class-0a-feature-not-supported). ^[delta-table-changes-view-unsupported-error-condition-databricks-on-aws.md]

## Error Message

The error message takes the form:

```
table_changes on view '<viewName>' is not supported.
```

where `<viewName>` is the name of the view that caused the error. ^[delta-table-changes-view-unsupported-error-condition-databricks-on-aws.md]

## Sub‑reasons

The error class includes several sub‑reasons that describe why the view is unsupported:

| Sub‑reason | Description |
|------------|-------------|
| `MULTIPLE_RELATIONS` | The view references more than one relation. |
| `NON_DETERMINISTIC_EXPRESSIONS` | The view contains non‑deterministic expressions. |
| `NOT_DELTA_TABLE` | The view does not reference a Delta table. |
| `NOT_SHARED_VIEW` | The view is not an [Open Sharing](/concepts/opensharing.md) view. |
| `SUBQUERY` | The view contains a subquery. |
| `UNSUPPORTED_OPERATOR` | The view contains an operator that is not allowed. |

^[delta-table-changes-view-unsupported-error-condition-databricks-on-aws.md]

## Cause

The `table_changes` function (also known as delta table changes) can only read change data from a Delta table or from a view that is a simple, deterministic, single‑relation, Delta‑backed, and Open‑Sharing view. When the view violates any of these requirements, Databricks raises this error with the corresponding sub‑reason. ^[delta-table-changes-view-unsupported-error-condition-databricks-on-aws.md]

## Resolution

To resolve the error, modify the view definition to meet all of the following conditions:

- The view must reference exactly one relation (no joins, unions, etc.).
- The view must contain only deterministic expressions.
- The view must reference a Delta table.
- The view must be an Open‑Sharing view.
- The view must not contain subqueries.
- The view must not use any unsupported operators.

Alternatively, use `table_changes` directly on the underlying Delta table instead of on a view. ^[delta-table-changes-view-unsupported-error-condition-databricks-on-aws.md]

## Related Concepts

- table_changes function
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md)
- [Delta table](/concepts/delta-lake-table.md)
- [Open Sharing](/concepts/opensharing.md)
- [Views in Databricks](/concepts/open-sharing-views-in-databricks.md)
- SQLSTATE error classes

## Sources

- delta-table-changes-view-unsupported-error-condition-databricks-on-aws.md

# Citations

1. delta-table-changes-view-unsupported-error-condition-databricks-on-aws.md

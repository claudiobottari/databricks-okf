---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6c71c7ce26bedb5e6ad620a1fd3f61778b81ed5bd9db942278bdacb63fcb07d0
  pageDirectory: concepts
  sources:
    - delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sqlstate-class-0a-feature-not-supported
    - SC0(NS
  citations:
    - file: delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
title: SQLSTATE class 0A (Feature not supported)
description: A SQLSTATE error class indicating a feature is not supported, which is the parent class of the DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED error.
tags:
  - databricks
  - sqlstate
  - error-messages
timestamp: "2026-06-18T15:22:47.926Z"
---

# SQLSTATE class 0A (Feature not supported)

**SQLSTATE class 0A** is the SQL standard error class for **Feature not supported**. In Databricks, an error with class `0A` (typically denoted as `0AKDC` in practice) indicates that a particular SQL operation cannot be performed because the required feature is not supported on the target object or configuration. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED

One specific error in this class is **`DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED`**, which occurs when attempting to use the `table_changes` function on a view. The full error message reads:

```
table_changes on view '<viewName>' is not supported.
```

^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

This error indicates that the target object is a view rather than a Delta table, and `table_changes` (which tracks [Delta table](/concepts/delta-lake-table.md) change data) cannot operate on views due to their dynamic nature.

## Subconditions and Causes

The error is further categorized into several subconditions that explain why the view is incompatible with `table_changes`:

| Subcondition | Meaning |
|-------------|---------|
| `MULTIPLE_RELATIONS` | The view references more than one relation. `table_changes` requires a single underlying table. |
| `NON_DETERMINISTIC_EXPRESSIONS` | The view contains non‑deterministic expressions (e.g., `rand()`, `current_timestamp()`). |
| `NOT_DELTA_TABLE` | The view does not reference a Delta table. |
| `NOT_SHARED_VIEW` | The view is not an [OpenSharing](/concepts/opensharing.md) view. |
| `SUBQUERY` | The view contains a subquery. |
| `UNSUPPORTED_OPERATOR` | The view contains an operator that is not allowed. |

^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

Each subcondition provides a specific reason why `table_changes` is unsupported on the given view.

## Resolution

To use `table_changes`, the target must be a [Delta table](/concepts/delta-lake-table.md) rather than a view. Ensure that the object queried is a Delta table stored in [Unity Catalog](/concepts/unity-catalog.md) or in the Hive [Metastore](/concepts/metastore.md), and that it does not contain any of the disallowed features listed above.

## Related Concepts

- Delta table changes — The CDC‑like functionality that triggers this error when misapplied.
- [Views in Databricks](/concepts/open-sharing-views-in-databricks.md) — Temporary or permanent virtual tables that often block feature support.
- SQLSTATE error classes — The overarching error classification system used by Databricks.
- [Feature not supported](/concepts/sqlstate-0akdc-feature-not-supported.md) — General guidance on handling unsupported‑feature errors.

## Sources

- delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md

# Citations

1. [delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md](/references/delta_table_changes_view_unsupported-error-condition-databricks-on-aws-c5e200eb.md)

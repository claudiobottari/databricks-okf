---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dc1b876f5c572f1505653ef0f147d445583a2981555a9510e8bd6ef88c6ef2b1
  pageDirectory: concepts
  sources:
    - delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
  confidence: 0.8
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - delta-lake-change-data-feed-cdf
    - DLCDF(
    - Delta Lake Change Data Feed
    - Delta Lake change data feed
  citations:
    - file: delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
title: Delta Lake Change Data Feed (CDF)
description: The underlying Delta Lake feature that table_changes relies on, which only works on Delta tables, not views.
tags:
  - delta-lake
  - change-data-feed
  - feature
timestamp: "2026-06-19T18:27:30.227Z"
---

# Delta Lake Change Data Feed (CDF)

**Delta Lake Change Data Feed (CDF)** is a feature that tracks row-level changes (inserts, updates, deletes) in a [Delta Lake](/concepts/delta-lake.md) table. The `table_changes` function allows users to query these changes. However, there are restrictions on using `table_changes` on views. This page documents the `DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED` error class, which occurs when `table_changes` is invoked on a view that does not meet the required conditions. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED error class

When `table_changes` is called on a view, Databricks returns the following error if the view is not supported:

```
table_changes on view '<viewName>' is not supported.
```

The error has SQLSTATE `0AKDC`. The error class includes several sub‑conditions that describe why the view is rejected. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

### Sub‑conditions

| Sub‑condition | Description |
|---|---|
| `MULTIPLE_RELATIONS` | The view references more than one relation. |
| `NON_DETERMINISTIC_EXPRESSIONS` | The view contains non‑deterministic expressions. |
| `NOT_DELTA_TABLE` | The view does not reference a Delta table. |
| `NOT_SHARED_VIEW` | The view is not an OpenSharing view. |
| `SUBQUERY` | The view contains a subquery. |
| `UNSUPPORTED_OPERATOR` | The view contains an operator that is not allowed. |

All conditions must be absent for `table_changes` to succeed on a view. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Related concepts

- table_changes function – The SQL function used to read change data.
- [Change Data Feed (CDF)](/concepts/delta-change-data-feed-cdf.md) – The underlying feature that records row‑level changes.
- Delta Lake views – Views that can wrap Delta tables but may not support CDF queries.
- [OpenSharing view](/concepts/opensharing-views.md) – A Delta Sharing view that is supported by `table_changes`.

## Sources

- delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md

# Citations

1. [delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md](/references/delta_table_changes_view_unsupported-error-condition-databricks-on-aws-c5e200eb.md)

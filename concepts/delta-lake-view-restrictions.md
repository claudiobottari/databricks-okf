---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c2bf999d7040b1917ec7d90678d79365df2ca85cd95a43f73a90086267b6fe30
  pageDirectory: concepts
  sources:
    - delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-view-restrictions
    - DLVR
  citations:
    - file: delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
title: Delta Lake view restrictions
description: Constraints on which views can be used with table_changes, including requiring single-relation, deterministic, Delta-based views without subqueries
tags:
  - delta-lake
  - views
  - restrictions
timestamp: "2026-06-19T10:08:33.629Z"
---

# Delta Lake View Restrictions

**Delta Lake view restrictions** refer to the limitations that prevent the `table_changes` function from being applied to certain views in Databricks. The `table_changes` function is designed to read change data feed records from Delta tables, but it does not support views in several specific cases. When an unsupported view is used, Databricks raises the `DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED` error class with a SQLSTATE `0AKDC`. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Error Overview

The error message is:

```
table_changes on view '<viewName>' is not supported.
```

This error occurs when `table_changes` is called on a view that violates one or more of the following restrictions. Each restriction corresponds to a distinct sub‑reason encoded in the error. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Restriction Categories

### Multiple Relations

The view references more than one relation (e.g., it joins multiple tables or views). `table_changes` requires a single underlying Delta table to identify row-level changes. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

### Non‑Deterministic Expressions

The view contains non‑deterministic expressions (e.g., `rand()`, `now()`, `current_timestamp`). Such expressions produce different results on repeated evaluations, making change tracking inconsistent. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

### Not a Delta Table

The view does not reference a Delta table. `table_changes` only works for tables that support the Change Data Feed (CDF), which is a Delta Lake feature. Views over non‑Delta sources (e.g., Parquet, CSV, JDBC) are not eligible. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

### Not a Shared View

The view is not an OpenSharing view. Delta Sharing views must be of the OpenSharing type for change data feed queries to succeed. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

### Subquery

The view contains a subquery. Views with subqueries are not supported by `table_changes` because the underlying logical plan becomes too complex for change data propagation. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

### Unsupported Operator

The view contains an operator that is not allowed. This catch‑all category covers any query operator (e.g., `UNION`, `EXCEPT`, `GROUP BY`) that the Delta Lake engine cannot handle when resolving change data feed records. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Workaround

To use `table_changes`, operate directly on the underlying Delta table instead of the view. If the view logic is required, consider restructuring it as an inline query or materializing the data into a Delta table and reading from there.

## Related Concepts

- table_changes function
- [Change Data Feed (CDF)](/concepts/delta-change-data-feed-cdf.md)
- Delta Lake views
- [OpenSharing views](/concepts/opensharing-views.md)
- [Delta Sharing](/concepts/delta-sharing.md)

## Sources

- delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md

# Citations

1. [delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md](/references/delta_table_changes_view_unsupported-error-condition-databricks-on-aws-c5e200eb.md)

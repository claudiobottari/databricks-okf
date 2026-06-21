---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 308ef9582bf32e659d274e338a7d5ec6807dacc8468c72196ec89e1520c8ca04
  pageDirectory: concepts
  sources:
    - delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - opensharing-view-compatibility
    - OVC
  citations:
    - file: delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
title: OpenSharing view compatibility
description: table_changes on views is only supported for OpenSharing views; non-OpenSharing views trigger NOT_SHARED_VIEW.
tags:
  - delta-sharing
  - view
  - compatibility
timestamp: "2026-06-19T18:27:31.866Z"
---

# OpenSharing View Compatibility

**OpenSharing view compatibility** refers to the set of constraints and requirements that a view must satisfy to be used with the `table_changes` function in Databricks. Views that do not meet these compatibility requirements trigger the `DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED` error condition. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Overview

The `table_changes` function on Databricks supports operating on views, but only under specific conditions. When a view fails to meet these compatibility requirements, Databricks raises the `DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED` error with a specific reason code indicating why the view is not supported. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Compatibility Requirements

### OpenSharing Views Only

Only **OpenSharing views** are supported by `table_changes`. If a view is not a shared view, Databricks raises the `NOT_SHARED_VIEW` error. This means the view must be created using [Delta Sharing](/concepts/delta-sharing.md) or a similar sharing mechanism that makes it available as an OpenSharing view. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

### Delta Table References

The view must reference a [Delta table](/concepts/delta-lake-table.md). If the underlying relation is not a Delta table, Databricks raises the `NOT_DELTA_TABLE` error. The view must ultimately resolve to a Delta table as its data source. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

### Single Relation Requirement

The view must reference **exactly one** relation. If the view references more than one table or view, Databricks raises the `MULTIPLE_RELATIONS` error. The view cannot perform joins, unions, or other operations that combine multiple data sources. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

### Deterministic Expressions

All expressions in the view must be **deterministic**. If the view contains non-deterministic expressions — such as `rand()`, `current_timestamp()`, or `uuid()` — Databricks raises the `NON_DETERMINISTIC_EXPRESSIONS` error. The view must produce the same results given the same input data. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

### No Subqueries

The view must not contain any subqueries. If a subquery is present, Databricks raises the `SUBQUERY` error. The view definition must be a straightforward selection from a single Delta table without nested queries. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

### Allowed Operators Only

The view must use only operators that are explicitly allowed. If the view contains an operator that is not permitted, Databricks raises the `UNSUPPORTED_OPERATOR` error. The specific set of allowed operators is defined by the Databricks platform. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Error Conditions Summary

The `DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED` error provides the following reason codes:

| Reason Code | Description |
|---|---|
| `MULTIPLE_RELATIONS` | The view references more than one relation |
| `NON_DETERMINISTIC_EXPRESSIONS` | The view contains non-deterministic expressions |
| `NOT_DELTA_TABLE` | The view does not reference a Delta table |
| `NOT_SHARED_VIEW` | The view is not an OpenSharing view |
| `SUBQUERY` | The view contains a subquery |
| `UNSUPPORTED_OPERATOR` | The view contains an operator that is not allowed |

^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The sharing mechanism for creating OpenSharing views
- [Delta table](/concepts/delta-lake-table.md) — The required underlying table type for compatible views
- table_changes function — The function that consumes compatible views
- DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED error|DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED error condition — The error raised for incompatible views

## Sources

- delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md

# Citations

1. [delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md](/references/delta_table_changes_view_unsupported-error-condition-databricks-on-aws-c5e200eb.md)

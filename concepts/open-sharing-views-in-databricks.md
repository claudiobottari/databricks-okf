---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 17354c70c6d459a4db011ef585402f3266e1a7d80b578c03f9e623056dac02ec
  pageDirectory: concepts
  sources:
    - delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
  confidence: 0.8
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - open-sharing-views-in-databricks
    - OSVID
    - Views in Databricks
  citations:
    - file: delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
title: Open Sharing views in Databricks
description: A view type in Databricks that supports Open Sharing protocol, required by table_changes (views that are not Open Sharing views trigger the NOT_SHARED_VIEW error)
tags:
  - databricks
  - delta-sharing
  - views
timestamp: "2026-06-19T15:07:54.356Z"
---

# Open Sharing Views in Databricks

**Open Sharing views** (also referred to as *OpenSharing views*) are views that support the `table_changes` function. When a view is not an Open Sharing view, Databricks raises the `DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED` error with the sub‑condition `NOT_SHARED_VIEW`. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## The `NOT_SHARED_VIEW` Error

The error message for a non‑Open Sharing view is:

> The view is not a OpenSharing view.

^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

This sub‑condition indicates that the view must be published as an Open Sharing view for `table_changes` to operate. Other sub‑conditions in the same error class describe additional reasons a view may not support change tracking, such as `NON_DETERMINISTIC_EXPRESSIONS`, `MULTIPLE_RELATIONS`, `NOT_DELTA_TABLE`, `SUBQUERY`, or `UNSUPPORTED_OPERATOR`. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Related Concepts

- table_changes function|table_changes — The function used to read row‑level changes from Delta tables and Open Sharing views.
- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol commonly used to share views across workspaces.
- [Views in Databricks](/concepts/open-sharing-views-in-databricks.md) — Standard and shared views in [Unity Catalog](/concepts/unity-catalog.md).
- DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED error|DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED error condition — The full error class that includes the `NOT_SHARED_VIEW` sub‑condition.

## Sources

- delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md

# Citations

1. [delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md](/references/delta_table_changes_view_unsupported-error-condition-databricks-on-aws-c5e200eb.md)

---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d1a2a76bf25d0a66baf980f4365c2925df3bf2a10981534d26cf7fafdf2422ba
  pageDirectory: concepts
  sources:
    - delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - opensharing-views
    - Open Sharing view
    - OpenSharing Events
    - OpenSharing events
    - OpenSharing view
    - Delta Sharing view
    - Shared Views
    - Shared views
    - creating OpenSharing views
    - dynamic views
  citations:
    - file: delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
title: OpenSharing views
description: A specific type of view in Databricks that supports open sharing protocols; referenced as a requirement for table_changes on views
tags:
  - databricks
  - views
  - sharing
timestamp: "2026-06-19T10:08:28.896Z"
---

# OpenSharing Views

**OpenSharing views** are a type of view in Databricks that are specifically designed for use with the Delta Sharing protocol. They enable secure, cross-platform sharing of data while preserving the ability to perform change-data-capture operations (such as `table_changes`) on the shared data. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Error Context

When a user attempts to call `table_changes` on a view that is not an OpenSharing view, Databricks returns the error `DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED` with subclass `NOT_SHARED_VIEW`. The error message states: "The view is not a OpenSharing view." ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

To successfully use `table_changes` on a view, the view must be an OpenSharing view; otherwise the operation is unsupported.

## Requirements

An OpenSharing view must meet certain conditions to be eligible for change-data capture:
- It must reference a single relational object (no `MULTIPLE_RELATIONS`). ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]
- It must not contain non‑deterministic expressions. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]
- It must reference a Delta table (`NOT_DELTA_TABLE`). ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]
- It must be a shared view (`NOT_SHARED_VIEW`). ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]
- It must not contain subqueries. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]
- It must not contain unsupported operators. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

If any of these conditions are violated, the `DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED` error is raised.

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) – The open protocol for sharing data across platforms.
- [Delta table](/concepts/delta-lake-table.md) – The underlying storage format required by an OpenSharing view.
- table_changes function – A function that returns row-level changes on Delta tables or OpenSharing views.
- [Views in Databricks](/concepts/open-sharing-views-in-databricks.md) – General documentation on view creation and management.

## Sources

- delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md

# Citations

1. [delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md](/references/delta_table_changes_view_unsupported-error-condition-databricks-on-aws-c5e200eb.md)

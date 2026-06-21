---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0d65f2d94e1322afa43152e56f496a63e4160c415995d9c7c58ef238e3ebe048
  pageDirectory: concepts
  sources:
    - delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multiple_relations-sub-error
    - multiple_relations-error-reason
    - MER
    - MULTIPLE_RELATIONS restriction
  citations:
    - file: delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
title: MULTIPLE_RELATIONS sub-error
description: A specific cause of DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED where the view references more than one relation
tags:
  - error-messages
  - delta-lake
timestamp: "2026-06-19T10:08:26.650Z"
---

# MULTIPLE_RELATIONS sub-error

The **MULTIPLE_RELATIONS** sub-error occurs when using the `table_changes` function on a view that references more than one relation. This is a specific error condition within the `DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED` error class. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Error Message

When this error occurs, Databricks returns the following message:

```
table_changes on view '<viewName>' is not supported.
```

With the sub-error indicating:

```
MULTIPLE_RELATIONS: The view references more than one relation.
```

^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Cause

The `table_changes` function in Databricks is designed to track changes on a single [Delta table](/concepts/delta-lake-table.md). When applied to a view that joins, unions, or otherwise references multiple underlying tables or views, the operation fails because the change tracking mechanism cannot resolve which source relation's changes to return. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Solution

To resolve this error, ensure that the view passed to `table_changes` references only a single [Delta table](/concepts/delta-lake-table.md). If you need to track changes across multiple tables, consider one of the following approaches:

- Apply `table_changes` directly to each individual Delta table rather than through a multi-relation view.
- Restructure the view to reference only one Delta table.
- Use alternative change data capture (CDC) mechanisms for multi-table scenarios.

## Related Sub-errors

The `DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED` error class includes several other sub-errors that may occur in similar contexts:

- NON_DETERMINISTIC_EXPRESSIONS sub-error – The view contains non-deterministic expressions.
- NOT_DELTA_TABLE sub-error – The view does not reference a Delta table.
- NOT_SHARED_VIEW error reason|NOT_SHARED_VIEW sub-error – The view is not an OpenSharing view.
- SUBQUERY sub-error – The view contains a subquery.
- UNSUPPORTED_OPERATOR constraint for table_changes|UNSUPPORTED_OPERATOR sub-error – The view contains an operator that is not allowed.

## Related Concepts

- [Delta table](/concepts/delta-lake-table.md) – The underlying storage format required for `table_changes`
- table_changes function – The function that triggers this error
- Change Data Capture (CDC) – Alternative approaches for tracking data changes
- [Views in Databricks](/concepts/open-sharing-views-in-databricks.md) – Understanding view limitations with change tracking

## Sources

- delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md

# Citations

1. [delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md](/references/delta_table_changes_view_unsupported-error-condition-databricks-on-aws-c5e200eb.md)

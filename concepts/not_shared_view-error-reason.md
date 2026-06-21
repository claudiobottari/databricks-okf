---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7cb515c0c80c43313e473fc1e05404cca776192f2bb72ac93b29c09354466d68
  pageDirectory: concepts
  sources:
    - delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - not_shared_view-error-reason
    - NER
    - NOT_SHARED_VIEW restriction
    - NOT_SHARED_VIEW sub-error
  citations:
    - file: delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
title: NOT_SHARED_VIEW error reason
description: A sub-reason of DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED indicating the view is not an OpenSharing view.
tags:
  - databricks
  - error-messages
  - delta-sharing
timestamp: "2026-06-18T15:22:29.059Z"
---

# NOT_SHARED_VIEW Error Reason

The **`NOT_SHARED_VIEW`** error reason is a sub-error of the [`DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED` error class](https://docs.databricks.com/aws/en/error-messages/delta-table-changes-view-unsupported-error-class) that occurs when attempting to use the `table_changes` function on a view that is not an OpenSharing view. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Error Details

When this error occurs, the full error message is:

```
table_changes on view '<viewName>' is not supported.
NOT_SHARED_VIEW: The view is not a OpenSharing view.
```

^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Cause

The `table_changes` function in Delta Lake requires that the target view be an [OpenSharing view](/concepts/opensharing-views.md). If the view was created as a standard view rather than as an OpenSharing-compatible view, the operation fails with this error. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Solution

Ensure that the view you are querying with `table_changes` is created as an OpenSharing view. Refer to the documentation on [creating OpenSharing views](/concepts/opensharing-views.md) for details on how to create compatible views. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Related Error Reasons

The `DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED` error class includes several other reasons for why `table_changes` on a view may be unsupported:

| Error Reason | Description |
|---|---|
| `MULTIPLE_RELATIONS` | The view references more than one relation |
| `NON_DETERMINISTIC_EXPRESSIONS` | The view contains non-deterministic expressions |
| `NOT_DELTA_TABLE` | The view does not reference a [Delta table](/concepts/delta-lake-table.md) |
| `NOT_SHARED_VIEW` | The view is not an OpenSharing view |
| `SUBQUERY` | The view contains a subquery |
| `UNSUPPORTED_OPERATOR` | The view contains an operator that is not allowed |

^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Related Concepts

- table_changes function — The Delta Lake function for reading change data feeds
- [OpenSharing views](/concepts/opensharing-views.md) — Views that support Delta Sharing
- [Delta table](/concepts/delta-lake-table.md) — The underlying table type required for change data feed operations
- [SQLSTATE 0AKDC](/concepts/sqlstate-0akdc.md) — The feature-not-supported SQL state associated with this error

## Sources

- delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md

# Citations

1. [delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md](/references/delta_table_changes_view_unsupported-error-condition-databricks-on-aws-c5e200eb.md)

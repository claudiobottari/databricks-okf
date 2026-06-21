---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d6ef438f8df8a305af4ff16d2afd14d71715b3f05c869c259d5e716fb904e64e
  pageDirectory: concepts
  sources:
    - delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - non_deterministic_expressions-constraint-for-table_changes
    - NCFT
    - NON_DETERMINISTIC_EXPRESSIONS constraint for table_changes
    - NON_DETERMINISTIC_EXPRESSIONS constraint for table_changes|NON_DETERMINISTIC_EXPRESSIONS
  citations:
    - file: delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
title: NON_DETERMINISTIC_EXPRESSIONS constraint for table_changes
description: A validation rule requiring that views used with table_changes must not contain non-deterministic expressions
tags:
  - databricks
  - validation
  - view-constraints
timestamp: "2026-06-19T15:07:44.001Z"
---

# NON_DETERMINISTIC_EXPRESSIONS constraint for `table_changes`

The **NON_DETERMINISTIC_EXPRESSIONS** constraint is one of several conditions that cause the `DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED` error when using the `table_changes` function on a view. This constraint specifically applies when the view definition includes non-deterministic expressions, which are not allowed for change data capture queries. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Error Message

When triggered, the error appears as:

```
table_changes on view '<viewName>' is not supported.
```

The error class `DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED` includes a reason string `NON_DETERMINISTIC_EXPRESSIONS`. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Cause

The view contains non-deterministic expressions. Non-deterministic expressions produce different results for the same input at different times (e.g., random functions, current timestamp, or similar volatile functions). Because `table_changes` requires a deterministic and stable mapping between the view and the underlying Delta table, such expressions are prohibited. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Resolution

To resolve the constraint, ensure that the view definition does not include any non-deterministic expressions. Only deterministic expressions should be used in views that are intended for use with `table_changes`. Replace volatile functions with static values or remove them from the view definition. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Related Constraints

The same error class (`DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED`) also covers several other conditions that can prevent `table_changes` on a view:
- MULTIPLE_RELATIONS constraint for table_changes – The view references more than one relation. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]
- NOT_DELTA_TABLE constraint for table_changes – The view does not reference a Delta table. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]
- NOT_SHARED_VIEW constraint for table_changes – The view is not an OpenSharing view. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]
- SUBQUERY constraint for table_changes – The view contains a subquery. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]
- UNSUPPORTED_OPERATOR constraint for table_changes – The view contains an operator that is not allowed. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Related Concepts

- table_changes function – The function that reads change data from a Delta table or view.
- [Delta table](/concepts/delta-lake-table.md) – The underlying table type required for `table_changes`.
- View – The logical abstraction over one or more tables.
- [Deterministic vs non-deterministic expressions](/concepts/deterministic-and-error-safe-expressions-in-policy-udfs.md) – Key distinction for query stability.
- Change Data Capture – The broader pattern that `table_changes` supports.

## Sources

- delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md

# Citations

1. [delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md](/references/delta_table_changes_view_unsupported-error-condition-databricks-on-aws-c5e200eb.md)

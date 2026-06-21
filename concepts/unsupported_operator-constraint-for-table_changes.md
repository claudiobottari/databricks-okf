---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ba72f9767b1f587043f6dd40c952690d5fe662dcb7d512052cc0b1c4f19f66ff
  pageDirectory: concepts
  sources:
    - delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unsupported_operator-constraint-for-table_changes
    - UCFT
    - UNSUPPORTED_OPERATOR constraint for table_changes
    - UNSUPPORTED_OPERATOR constraint for table_changes|UNSUPPORTED_OPERATOR
    - UNSUPPORTED_OPERATOR restriction
    - UNSUPPORTED_OPERATOR sub-error
  citations:
    - file: delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
title: UNSUPPORTED_OPERATOR constraint for table_changes
description: A validation rule requiring that views used with table_changes must not contain operators that are not allowed for change data capture
tags:
  - databricks
  - validation
  - view-constraints
timestamp: "2026-06-19T15:08:10.327Z"
---

# UNSUPPORTED_OPERATOR constraint for table_changes

The **UNSUPPORTED_OPERATOR constraint** is one of several conditions that can cause the DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED error|DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED error condition when calling `table_changes` on a view in Databricks. This error occurs when the view definition contains an operator that is not allowed for change data capture queries. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Overview

`table_changes` is a Databricks function used to retrieve change data from Delta tables. When applied to a view rather than a direct table reference, the system validates the view's definition against a set of constraints. The `UNSUPPORTED_OPERATOR` constraint triggers when the view contains any operator that the system does not permit in the context of change data capture. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Error Message

```
table_changes on view '<viewName>' is not supported.
```

The SQLSTATE for this error class is `0AKDC`. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Related Constraints

The `UNSUPPORTED_OPERATOR` constraint is one of several validation checks that apply to views used with `table_changes`. The full set of constraints includes:

- MULTIPLE_RELATIONS constraint for table_changes — The view references more than one relation.
- NON_DETERMINISTIC_EXPRESSIONS constraint for table_changes — The view contains non-deterministic expressions.
- NOT_DELTA_TABLE constraint for table_changes — The view does not reference a Delta table.
- NOT_SHARED_VIEW constraint for table_changes — The view is not an OpenSharing view.
- SUBQUERY constraint for table_changes — The view contains a subquery.

## Resolution

To resolve the `UNSUPPORTED_OPERATOR` error, restructure the view definition to remove any unsupported operators. This typically involves simplifying the view query or replacing the unsupported operator with an equivalent construct that the change data capture system supports. Consider using a direct [Delta table](/concepts/delta-lake-table.md) reference instead of a view if the view's logic cannot be simplified. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta table](/concepts/delta-lake-table.md) — The underlying data format that supports change data capture.
- table_changes function — The Databricks function for retrieving incremental changes from Delta tables.
- Change Data Capture (CDC) — The broader pattern of tracking and consuming data changes.
- [OpenSharing view](/concepts/opensharing-views.md) — A view type that supports sharing across workspaces.

## Sources

- delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md

# Citations

1. [delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md](/references/delta_table_changes_view_unsupported-error-condition-databricks-on-aws-c5e200eb.md)

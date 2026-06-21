---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 355d4b2d15ce7b26374449d7c7f25579e4acf41dbade21a44c80fa9b9ad70a62
  pageDirectory: concepts
  sources:
    - delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - not_delta_table-constraint-for-table_changes
    - NCFT
    - NOT_DELTA_TABLE constraint for table_changes
    - NOT_DELTA_TABLE constraint for table_changes|NOT_DELTA_TABLE
  citations:
    - file: delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
title: NOT_DELTA_TABLE constraint for table_changes
description: A validation rule requiring that views used with table_changes must ultimately reference a Delta table
tags:
  - databricks
  - validation
  - view-constraints
timestamp: "2026-06-19T15:07:55.240Z"
---

# NOT_DELTA_TABLE constraint for table_changes

The **NOT_DELTA_TABLE** constraint is one of several error conditions that can occur when using the `table_changes` function on a view in Databricks. This specific error indicates that the view referenced in the `table_changes` call does not reference a Delta table.

## Error Details

When you attempt to use `table_changes` on a view, and that view does not reference a Delta table, you will encounter the `NOT_DELTA_TABLE` error. The full error message falls under the `DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED` error class with SQLSTATE 0AKDC (feature not supported). ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

The error message format is:
```
table_changes on view '<viewName>' is not supported.
```
with the specific reason: `NOT_DELTA_TABLE`

## Requirements

For `table_changes` to work on a view, the underlying source must be a Delta table. This means the view must be defined on top of one or more Delta tables to successfully use the `table_changes` function. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Related Constraints

The `NOT_DELTA_TABLE` constraint is part of a family of constraints that can prevent `table_changes` from working on views:

- **MULTIPLE_RELATIONS** - The view references more than one relation
- **NON_DETERMINISTIC_EXPRESSIONS** - The view contains non-deterministic expressions
- **NOT_DELTA_TABLE** - The view does not reference a Delta table (current constraint)
- **NOT_SHARED_VIEW** - The view is not an OpenSharing view
- **SUBQUERY** - The view contains a subquery
- **UNSUPPORTED_OPERATOR** - The view contains an operator that is not allowed

## Resolution

To resolve the `NOT_DELTA_TABLE` error, ensure that the view you are using with `table_changes` is defined on top of Delta tables. If the view is currently based on non-Delta sources (such as external tables, other file formats, or views), you will need to either:

1. Convert the underlying source to a Delta table
2. Create a new view that directly references Delta tables
3. Use the Delta table directly instead of through the view

## Related Concepts

- table_changes function - The function used to query change data feed from Delta tables
- [Delta table](/concepts/delta-lake-table.md) - The native table format required for change data tracking
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) - The mechanism for capturing changes in Delta tables
- DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED - The broader error class for view-related constraints
- [SQLSTATE 0AKDC](/concepts/sqlstate-0akdc.md) - The feature not supported SQL state code

## Sources

- delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md

# Citations

1. [delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md](/references/delta_table_changes_view_unsupported-error-condition-databricks-on-aws-c5e200eb.md)

---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ff1aaf2147461280bae50a02783b44ee4abc0236a99c5febe5b597ea719904e6
  pageDirectory: concepts
  sources:
    - delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - non_deterministic_expressions-sub-error
    - NON_DETERMINISTIC_EXPRESSIONS sub-error
  citations:
    - file: delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
title: NON_DETERMINISTIC_EXPRESSIONS sub-error
description: A specific cause of DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED where the view contains non-deterministic expressions
tags:
  - error-messages
  - delta-lake
timestamp: "2026-06-19T10:08:30.977Z"
---

# NON_DETERMINISTIC_EXPRESSIONS sub-error

The **NON_DETERMINISTIC_EXPRESSIONS** sub-error is a specific error condition that occurs when using the `table_changes` function on a view that contains non-deterministic expressions. This error is part of the `DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED` error class.

## Error Message

When this error occurs, the system returns the following message:

```
table_changes on view '<viewName>' is not supported.
```

With the sub-error identifier:

```
NON_DETERMINISTIC_EXPRESSIONS
```

^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Cause

The `table_changes` function requires that the underlying view definition be deterministic — meaning it must produce the same output for the same input every time it is evaluated. If the view contains non-deterministic expressions (such as functions that return different values on each invocation, like `rand()`, `current_timestamp()`, or `uuid()`), the system cannot reliably track changes to the underlying Delta table, and this error is raised. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Affected Operations

This error specifically applies to the `table_changes` function when used with views. The `table_changes` function is designed to read change data feed (CDF) information from [Delta tables](/concepts/delta-lake-table.md), but it cannot operate on views that contain non-deterministic expressions. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Resolution

To resolve this error, modify the view definition to remove any non-deterministic expressions. Alternatively, consider using `table_changes` directly on the underlying [Delta table](/concepts/delta-lake-table.md) rather than on a view that wraps it. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Related Concepts

- DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED error class — The parent error class containing this sub-error
- table_changes function — The function that triggers this error when used on unsupported views
- [Change Data Feed (CDF)](/concepts/delta-change-data-feed-cdf.md) — The feature that enables tracking row-level changes in Delta tables
- [Delta tables](/concepts/delta-lake-table.md) — The table format required for `table_changes` to work
- Deterministic vs Non-deterministic expressions — The distinction that determines whether a view is supported

## Sources

- delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md

# Citations

1. [delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md](/references/delta_table_changes_view_unsupported-error-condition-databricks-on-aws-c5e200eb.md)

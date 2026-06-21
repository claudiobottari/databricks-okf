---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 793530dc29ba2cbcd8e5dd32b1b0354f79d7871b64159098a03d54494b273eee
  pageDirectory: concepts
  sources:
    - delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - not_delta_table-error-reason
    - NER
    - Delta Lake Error Messages
  citations:
    - file: delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
title: NOT_DELTA_TABLE error reason
description: A sub-reason of DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED indicating the underlying view does not reference a Delta table.
tags:
  - databricks
  - error-messages
  - delta-lake
  - views
timestamp: "2026-06-18T15:22:25.934Z"
---

# NOT_DELTA_TABLE Error Reason

The **NOT_DELTA_TABLE** error reason occurs as a sub‑condition of the broader `DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED` error class. It indicates that the `table_changes` operation was attempted on a view that does not reference a [Delta table](/concepts/delta-lake-table.md). ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Error Context

When you call `table_changes` on a view, Databricks checks whether the view’s underlying source is a single Delta table. If the view is based on non‑Delta sources (e.g., Parquet files, external tables, or other non‑Delta formats), the operation fails with this error.

The full error message typically appears as:

```
table_changes on view '<viewName>' is not supported.
```

followed by one of several sub‑reasons, among which `NOT_DELTA_TABLE` is a possible cause. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Root Cause

The view does not reference a Delta table. Delta’s change‑data‑feed (`table_changes`) only works on tables that use the Delta Lake format; it cannot track changes on views that resolve to other storage formats or multiple sources. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

Other sub‑reasons in the same error class include:

- `MULTIPLE_RELATIONS` – The view references more than one relation.
- `NON_DETERMINISTIC_EXPRESSIONS` – The view contains non‑deterministic expressions.
- `NOT_SHARED_VIEW` – The view is not an OpenSharing view.
- `SUBQUERY` – The view contains a subquery.
- `UNSUPPORTED_OPERATOR` – The view contains an operator that is not allowed.

## Resolution

To resolve a `NOT_DELTA_TABLE` error, ensure that the view on which you are calling `table_changes` ultimately resolves to a single Delta table. This may involve:

- Replacing the view definition to point directly to a Delta table.
- Removing intermediate non‑Delta transformations.
- Using `table_changes` on the Delta table itself instead of a view that references it indirectly.

## Related Concepts

- [Delta table](/concepts/delta-lake-table.md) – The required underlying storage format for `table_changes`.
- table_changes function – The function that reads the change‑data feed.
- DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED error class – The parent error class containing this sub‑reason.
- [Change Data Feed (CDF)](/concepts/delta-change-data-feed-cdf.md) – The mechanism that tracks row‑level changes in Delta tables.

## Sources

- delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md

# Citations

1. [delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md](/references/delta_table_changes_view_unsupported-error-condition-databricks-on-aws-c5e200eb.md)

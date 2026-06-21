---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 803cfa6ca276a24abd56892f1331a0216b982d0e016cd248077fc332688238ca
  pageDirectory: concepts
  sources:
    - delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-reconciliation-queries
    - DLRQ
    - Delta Reconciliation Queries
    - Reconciliation Queries
    - Reconciliation Query
    - reconciliation query
  citations:
    - file: delta_external_metadata_unsupported_source_error_condition.md
title: Delta Lake Reconciliation Queries
description: Queries used to compare or reconcile data between sources in Delta Lake, with restrictions on projections and column aliasing when external metadata is involved.
tags:
  - delta-lake
  - queries
  - data-validation
timestamp: "2026-06-18T15:19:32.013Z"
---

# Delta Lake Reconciliation Queries

**Delta Lake Reconciliation Queries** are specialized SQL-based operations that compare the state of a Delta table with an external source or reference. They are used to detect, report, and optionally resolve data inconsistencies between the Delta Lake and another data system.

## Overview

Reconciliation queries in Delta Lake enable users to compare data between a Delta table and an external metadata source. These queries help identify discrepancies such as missing records, mismatched values, or structural differences between the two systems. ^[delta_external_metadata_unsupported_source_error_condition.md]

## Common Use Cases

- **Data integrity validation** – Comparing a Delta table with an upstream source to ensure all records have been properly ingested.
- **Migration verification** – Confirming that data transferred between systems matches exactly.
- **Change data capture (CDC) auditing** – Validating that CDC operations are correctly reflected in the target table.
- **Periodic reconciliation** – Scheduled checks to detect drift between systems over time.

## Requirements and Limitations

To use a reconciliation query, the source table must be a streaming table or [materialized view](/concepts/materialized-views-in-databricks.md). Other table types are not supported for this operation. ^[delta_external_metadata_unsupported_source_error_condition.md]

### Column Masking

Tables with column mask policies applied are not supported for reconciliation queries. ^[delta_external_metadata_unsupported_source_error_condition.md]

### Column Renaming

When using an alias in a reconciliation query, column mapping must first be enabled. ^[delta_external_metadata_unsupported_source_error_condition.md]

### Projection Support

Only certain projection types are supported in reconciliation query expressions. Queries containing unsupported projections will fail with a `PROJECTION_NOT_SUPPORTED` error. ^[delta_external_metadata_unsupported_source_error_condition.md]

### Row-Level Security

Tables with [row filter](/concepts/row-filter-policies.md) policies (row-level security) are not supported for reconciliation queries. ^[delta_external_metadata_unsupported_source_error_condition.md]

## Error Conditions

The following error conditions can occur when working with reconciliation queries:

| Error Condition | Description |
|-----------------|-------------|
| `COLUMN_MASK` | Tables with column mask policies are not supported |
| `COLUMN_RENAME_WITHOUT_COLUMN_MAPPING` | Column mapping must be enabled before using aliases |
| `PROJECTION_NOT_SUPPORTED` | The specified projection cannot be used in a reconciliation query |
| `ROW_FILTER` | Tables with row-level security policies are not supported |
| `TABLE_TYPE` | Only supported for streaming tables and materialized views |

If any of these conditions occur, the query will fail with an appropriate error message from the `DELTA_EXTERNAL_METADATA_UNSUPPORTED_SOURCE` error class. ^[delta_external_metadata_unsupported_source_error_condition.md]

## Best Practices

- Verify the table type before writing a reconciliation query – only streaming tables and [materialized views](/concepts/materialized-views-in-databricks.md) are supported.
- Ensure [column mapping](/concepts/column-mapping-in-delta-lake.md) is enabled before using aliases or renamed columns.
- Use Temporal queries to compare data at specific points in time.
- Test reconciliation queries on a subset of data before running at scale.

## Related Concepts

- [Delta Lake change data feed](/concepts/delta-lake-change-data-feed-cdf.md)
- Streaming tables
- [Materialized views](/concepts/materialized-views-in-databricks.md)
- Temporal queries in Delta Lake
- [Column mapping in Delta](/concepts/column-mapping-in-delta-lake.md)
- [Row Filters and Column Masks](/concepts/row-filters-and-column-masks.md)

## Sources

- delta_external_metadata_unsupported_source_error_condition.md

# Citations

1. delta_external_metadata_unsupported_source_error_condition.md

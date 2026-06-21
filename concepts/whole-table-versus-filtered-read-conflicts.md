---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 732ff72ee827452232393d14a3980666008d04fd20bd03729c7b1ed56dfb5b3c
  pageDirectory: concepts
  sources:
    - delta_concurrent_delete_read-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - whole-table-versus-filtered-read-conflicts
    - WVFRC
  citations:
    - file: delta_concurrent_delete_read-error-condition-databricks-on-aws.md
title: Whole-table versus filtered read conflicts
description: A class of Delta Lake concurrency conflicts where reading an entire table (without filters) collides with concurrent delete operations, with solutions involving narrowing the read scope via predicates or partition hints.
tags:
  - delta-lake
  - concurrency
  - query-optimization
timestamp: "2026-06-19T10:04:19.098Z"
---

# Whole-table versus filtered read conflicts

**Whole-table versus filtered read conflicts** are a category of transaction conflict that occurs in [Delta Lake](/concepts/delta-lake.md) when a read operation scans an entire table while a concurrent write operation deletes data from that same table. These conflicts are reported through the DELTA_CONCURRENT_DELETE_READ Error|DELTA_CONCURRENT_DELETE_READ error condition and have distinct sub-types depending on whether the read was truly unfiltered or whether partition hints were involved.

## Overview

Delta Lake uses [optimistic concurrency control](/concepts/delta-lake-optimistic-concurrency-control.md) to manage concurrent reads and writes. When a transaction reads data that a concurrent transaction deletes, a conflict is detected. The severity and resolution of the conflict depend on whether the read operation applied any filters or partition hints to narrow its data scope. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## WHOLE_TABLE_READ

The `WHOLE_TABLE_READ` sub-type occurs when a transaction attempts to read the entire table without any filters, conflicting with a concurrent deletion operation. The error message advises adding filters to the query to narrow the data scope and retrying the operation. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

This is the most common form of whole-table read conflict. It typically arises in analytical queries or ETL jobs that scan full tables without partition pruning or predicate pushdown. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## WHOLE_TABLE_REPLACE

The `WHOLE_TABLE_REPLACE` sub-type occurs when a concurrent operation replaces all data in the table. Unlike `WHOLE_TABLE_READ`, which involves a read conflicting with a delete, this sub-type involves a read conflicting with a full table replacement (for example, an `INSERT OVERWRITE` or a full table delete followed by a write). The recommended action is to retry the operation. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## WITHOUT_HINT

The `WITHOUT_HINT` sub-type occurs when a concurrent operation deletes data that was read by this operation, but no partition hint was used. This is a general conflict that does not fall into the more specific categories. The recommended action is to retry the operation. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## WITH_PARTITION_HINT

The `WITH_PARTITION_HINT` sub-type occurs when a concurrent operation deletes data in a specific partition that was read by this operation. The error message includes the partition values that caused the conflict. Unlike `WHOLE_TABLE_READ`, the read operation did use a partition hint, but the concurrent deletion targeted the same partition. The recommended action is to retry the operation. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Comparison of sub-types

| Sub-type | Read scope | Concurrent operation | Recommended action |
|----------|------------|---------------------|-------------------|
| `WHOLE_TABLE_READ` | Entire table (no filters) | Delete | Add filters and retry |
| `WHOLE_TABLE_REPLACE` | Entire table | Full table replacement | Retry |
| `WITHOUT_HINT` | Unspecified scope | Delete | Retry |
| `WITH_PARTITION_HINT` | Specific partition | Delete in same partition | Retry |

## Prevention and mitigation

- **Add filters to read queries.** The most effective way to avoid `WHOLE_TABLE_READ` conflicts is to include WHERE clauses that narrow the data scope, enabling Delta Lake to perform row-level conflict detection rather than table-level conflict detection. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]
- **Use partition hints.** When reading from partitioned tables, specifying partition hints can help Delta Lake narrow the conflict detection scope, reducing the likelihood of `WHOLE_TABLE_READ` conflicts. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]
- **Retry on conflict.** For most sub-types, retrying the operation is the recommended resolution, as the conflicting transaction will have completed by the time of the retry. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Related concepts

- DELTA_CONCURRENT_DELETE_READ Error|DELTA_CONCURRENT_DELETE_READ error condition — The parent error class containing all sub-types
- [Row-Level Conflict Resolution](/concepts/row-level-conflict-resolution.md) — The mechanism that allows Delta Lake to resolve conflicts at the row level rather than the table level
- [Optimistic concurrency control in Delta Lake](/concepts/delta-lake-optimistic-concurrency-control.md) — The underlying concurrency model
- Partition pruning — A technique to reduce the data scanned by queries
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) — A feature that can conflict with row-level conflict detection when tables contain a `_change_type` column

## Sources

- delta_concurrent_delete_read-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_delete_read-error-condition-databricks-on-aws.md](/references/delta_concurrent_delete_read-error-condition-databricks-on-aws-d0015916.md)

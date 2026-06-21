---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b3a4fb5c6c97066ccb05786991a241e69d5fa18bebca6178fcee706f0381b3e6
  pageDirectory: concepts
  sources:
    - drop-bloom-filter-index-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-table-name-restrictions-for-index-commands
    - DTNRFIC
  citations:
    - file: drop-bloom-filter-index-databricks-on-aws.md
title: Delta table name restrictions for index commands
description: The table name in DROP BLOOM FILTER INDEX must not include temporal or options specifications
tags:
  - delta-table
  - sql-syntax
  - databricks
timestamp: "2026-06-18T15:35:23.000Z"
---

# Delta Table Name Restrictions for Index Commands

**Delta table name restrictions for index commands** are constraints on the table identifier that must be satisfied when executing [CREATE BLOOM FILTER INDEX](/concepts/create-bloom-filter-index.md) or [DROP BLOOM FILTER INDEX](/concepts/drop-bloom-filter-index-syntax.md) commands on a [Delta table](/concepts/delta-lake-table.md). These restrictions ensure that the table name references an existing table and does not include certain optional specifications that are incompatible with index operations.

## Syntax

```sql
DROP BLOOMFILTER INDEX ON [TABLE] table_name
  [FOR COLUMNS (columnName1 [, ...] )]
```

^[drop-bloom-filter-index-databricks-on-aws.md]

## Name Restriction

The `table_name` parameter must identify an existing Delta table. The name must **not** include a temporal specification or options specification. These specifications are part of the table name syntax for some queries but are disallowed in index commands. ^[drop-bloom-filter-index-databricks-on-aws.md]

## Behavior

- The command fails if the table does not exist. ^[drop-bloom-filter-index-databricks-on-aws.md]
- The command fails if a specified column does not exist. ^[drop-bloom-filter-index-databricks-on-aws.md]
- All Bloom filter related metadata is removed from the specified columns. ^[drop-bloom-filter-index-databricks-on-aws.md]
- When a table has no Bloom filters, the underlying index files are cleaned during table vacuum. ^[drop-bloom-filter-index-databricks-on-aws.md]

## Related Topics

- [CREATE BLOOM FILTER INDEX](/concepts/create-bloom-filter-index.md)
- [Bloom filter indexes (deprecated)](/concepts/bloom-filter-index-deprecated.md)
- Delta table naming conventions
- Table name syntax in Databricks SQL

## Sources

- drop-bloom-filter-index-databricks-on-aws.md

# Citations

1. [drop-bloom-filter-index-databricks-on-aws.md](/references/drop-bloom-filter-index-databricks-on-aws-7a6d5bf4.md)

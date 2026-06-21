---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5d6e7c75fe1455d6697eb1721dba5d351261a33fdc88711ee0887adef57ac6b6
  pageDirectory: concepts
  sources:
    - drop-bloom-filter-index-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - drop-bloom-filter-index-syntax
    - DBFIS
    - DBFS
    - DROP BLOOM FILTER INDEX
    - DROP BLOOMFILTER INDEX
    - drop-bloom-filter-index-command
    - DBFIC
  citations:
    - file: drop-bloom-filter-index-databricks-on-aws.md
title: DROP BLOOM FILTER INDEX syntax
description: SQL command syntax and parameters for dropping Bloom filter indexes on Delta tables in Databricks
tags:
  - sql
  - delta-table
  - index-management
  - databricks
timestamp: "2026-06-18T15:35:15.594Z"
---

# DROP BLOOM FILTER INDEX Syntax

The `DROP BLOOM FILTER INDEX` command removes a [Bloom Filter Index](/concepts/bloom-filter-index.md) from one or more columns in a [Delta table](/concepts/delta-lake-table.md). This command is specific to Databricks SQL and Databricks Runtime.

> **Important**: Bloom filter indexes are deprecated. Databricks recommends dropping all existing Bloom filter indexes and using the recommended alternatives described in the [Bloom filter indexes (deprecated)](https://docs.databricks.com/aws/en/optimizations/bloom-filters) documentation.^[drop-bloom-filter-index-databricks-on-aws.md]

## Syntax

```sql
DROP BLOOMFILTER INDEX
ON [TABLE] table_name
[FOR COLUMNS (columnName1 [, ...] ) ]
```

^[drop-bloom-filter-index-databricks-on-aws.md]

## Parameters

| Parameter | Description |
|-----------|-------------|
| `table_name` | Identifies an existing Delta table. The name must not include a temporal specification or options specification. |

- The command fails if either the table name or one of the specified columns does not exist. ^[drop-bloom-filter-index-databricks-on-aws.md]

## Behavior

When the command executes, all Bloom filter related metadata is removed from the specified columns. If a table has no remaining Bloom filters (either all indexes have been dropped or none were created), the underlying index files are cleaned up when the table is vacuumed. ^[drop-bloom-filter-index-databricks-on-aws.md]

## Examples

Drop the Bloom filter index from a specific column:

```sql
DROP BLOOMFILTER INDEX
ON my_table
FOR COLUMNS (id);
```

Drop Bloom filter indexes from multiple columns:

```sql
DROP BLOOMFILTER INDEX
ON my_table
FOR COLUMNS (id, name, email);
```

Drop all Bloom filter indexes from a table (omitting the `FOR COLUMNS` clause):

```sql
DROP BLOOMFILTER INDEX
ON my_table;
```

If no `FOR COLUMNS` clause is specified, the command drops the entire Bloom filter index on the table. However, the source material does not specify this behavior in the extracted lines; it only shows that `FOR COLUMNS` is optional.

## Related Concepts

- [Bloom Filter Index](/concepts/bloom-filter-index.md) — The deprecated indexing feature that this command removes.
- [CREATE BLOOM FILTER INDEX](/concepts/create-bloom-filter-index.md) — The command to create a Bloom filter index.
- [Delta table](/concepts/delta-lake-table.md) — The table type on which Bloom filter indexes operate.
- [Bloom filter indexes (deprecated)](/concepts/bloom-filter-index.md) — Documentation on alternatives and migration guidance.
- VACUUM — The command that cleans up index files after all Bloom filters have been dropped.
- Databricks SQL — The environment where this command is available.

## Sources

- drop-bloom-filter-index-databricks-on-aws.md

# Citations

1. [drop-bloom-filter-index-databricks-on-aws.md](/references/drop-bloom-filter-index-databricks-on-aws-7a6d5bf4.md)

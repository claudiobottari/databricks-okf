---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5ea3f367a99ea0b080d839b660390103ac3aeba567ae03b323f88c41294bed2e
  pageDirectory: concepts
  sources:
    - drop-bloom-filter-index-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - drop-bloom-filter-index-command
    - DBFIC
  citations:
    - file: drop-bloom-filter-index-databricks-on-aws.md
title: DROP BLOOM FILTER INDEX Command
description: SQL syntax and parameters for dropping a Bloom filter index on a Delta table column in Databricks
tags:
  - sql
  - command
  - delta-table
  - index
timestamp: "2026-06-19T18:38:50.174Z"
---

# DROP BLOOM FILTER INDEX Command

The **`DROP BLOOMFILTER INDEX`** command removes one or all [Bloom filter](/concepts/bloom-filter-index.md) indexes from an existing [Delta table](/concepts/delta-lake-table.md). Bloom filter indexes are deprecated; Databricks recommends dropping all existing Bloom filter indexes and migrating to alternative approaches. ^[drop-bloom-filter-index-databricks-on-aws.md]

## Applies To[​](#applies-to)

This command is available in Databricks SQL and Databricks Runtime. ^[drop-bloom-filter-index-databricks-on-aws.md]

## Syntax[​](#syntax)

```sql
DROP BLOOMFILTER INDEX ON [TABLE] table_name
  [FOR COLUMNS ( columnName1 [, ...] ) ]
```

^[drop-bloom-filter-index-databricks-on-aws.md]

## Parameters[​](#parameters)

- **`table_name`**  
  Identifies an existing Delta table. The name must not include a temporal specification or options specification.  
  The command fails if the table does not exist. ^[drop-bloom-filter-index-databricks-on-aws.md]

- **`FOR COLUMNS ( columnName1 [, ...] )`**  
  An optional clause that limits the drop to bloom filter indexes on the specified columns.  
  The command fails if a column name specified does not exist in the table or does not have a bloom filter index.  
  If this clause is omitted, all bloom filter indexes on the table are dropped. ^[drop-bloom-filter-index-databricks-on-aws.md]

## Behavior[​](#behavior)

- The command removes all bloom filter related metadata from the specified columns. ^[drop-bloom-filter-index-databricks-on-aws.md]
- When a table no longer has any bloom filter indexes, the underlying index files are cleaned during the next VACUUM operation on the table. ^[drop-bloom-filter-index-databricks-on-aws.md]

## Related Concepts[​](#related-concepts)

- [Bloom filter indexes (deprecated)](/concepts/bloom-filter-index-deprecated.md) — Detailed documentation and recommended alternatives.
- [CREATE BLOOM FILTER INDEX](/concepts/create-bloom-filter-index.md) — The command to create a bloom filter index (deprecated).
- VACUUM — Operation that cleans up leftover index files after dropping all bloom filters.
- [Delta table](/concepts/delta-lake-table.md) — The table type on which bloom filter indexes are created.
- Deprecated features — General guidance on handling deprecated functionality.

## Sources[​](#sources)

- drop-bloom-filter-index-databricks-on-aws.md

# Citations

1. [drop-bloom-filter-index-databricks-on-aws.md](/references/drop-bloom-filter-index-databricks-on-aws-7a6d5bf4.md)

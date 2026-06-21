---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 85b60bca48333b5427606ff484dd08aede22d4f30761bc6bd8b3cc33405468b2
  pageDirectory: concepts
  sources:
    - update-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - merge-into-delta-lake
    - MI(L
    - MERGE INTO (Delta)
    - Merge (Delta Lake)
    - Merge Into Delta
    - Merge into Delta Table
    - MERGE INTO
    - MERGE INTO Operations
    - MERGE INTO|MERGE INTO
    - MERGE Operations in Delta Lake
    - Merge Mode
    - Upsert into Delta Lake using merge
  citations:
    - file: update-databricks-on-aws.md
title: MERGE INTO (Delta Lake)
description: Alternative SQL statement used instead of unsupported UPDATE...FROM...JOIN syntax to update a table based on a join with another table or subquery.
tags:
  - delta-lake
  - sql
  - dml
  - join
timestamp: "2026-06-19T23:16:14.058Z"
---

# MERGE INTO ([Delta Lake](/concepts/delta-lake.md))

**MERGE INTO** is a [Delta Lake](/concepts/delta-lake.md) SQL statement that atomically updates, inserts, or deletes rows in a target table based on the result of a join with a source table, view, or subquery. On Databricks, it serves as the primary mechanism for performing *upserts* (merge updates) and for updating a table from a join — an operation that the `UPDATE` statement does not support directly. ^[update-databricks-on-aws.md]

## Usage in [Delta Lake](/concepts/delta-lake.md)

MERGE INTO is the recommended alternative when you need to update a table based on a join with another table or subquery. Databricks SQL does not support the `UPDATE ... FROM ... JOIN` syntax found in some other SQL dialects; instead, you use `MERGE INTO` with a `WHEN MATCHED` clause to perform the update. ^[update-databricks-on-aws.md]

### Example: Updating from a Join

The following example shows how `MERGE INTO` replaces the unsupported `UPDATE ... FROM ... JOIN` pattern:

```sql
-- Equivalent to (not supported in Databricks):
-- UPDATE t1 SET t1.c1 = t2.c1 FROM t1 INNER JOIN t2 ON t1.c2 = t2.c2

MERGE INTO t1
USING t2
ON t1.c2 = t2.c2
WHEN MATCHED THEN UPDATE SET t1.c1 = t2.c1;
```

In this form, `t1` is the target table, `t2` is the source, the `ON` clause defines the join condition, and the `WHEN MATCHED` action updates the matched rows. ^[update-databricks-on-aws.md]

## Supported Operations

While the source material only illustrates the `WHEN MATCHED THEN UPDATE` case, the full `MERGE INTO` syntax in [Delta Lake](/concepts/delta-lake.md) also supports `WHEN NOT MATCHED THEN INSERT` and `WHEN MATCHED THEN DELETE`, enabling complete merge (upsert) workflows. The statement is atomic and fully ACID-compliant, consistent with all [Delta Lake](/concepts/delta-lake.md) operations. ^[update-databricks-on-aws.md]

## Limitations and Considerations

- The `UPDATE` statement itself is supported only for [Delta Lake](/concepts/delta-lake.md) tables; consequently, `MERGE INTO` also applies exclusively to [Delta Lake](/concepts/delta-lake.md) tables. ^[update-databricks-on-aws.md]
- For simple row‑level updates that do not require a join, the standalone `UPDATE` statement may be more straightforward. ^[update-databricks-on-aws.md]

## Related Concepts

- [UPDATE (Delta Lake)](/concepts/update-statement-delta-lake.md) – The simpler row‑update statement for [Delta Lake](/concepts/delta-lake.md).
- [DELETE (Delta Lake)](/concepts/delete-from-delta-lake.md) – Deletes rows from a Delta table.
- MERGE – General Databricks documentation for the `MERGE` command (includes full syntax and additional clauses).
- [Delta Lake](/concepts/delta-lake.md) – ACID transactions and versioned data lake storage.
- [COPY INTO](/concepts/copy-into-command.md) – Ingest data from files with schema inference and validation.

## Sources

- update-databricks-on-aws.md

# Citations

1. [update-databricks-on-aws.md](/references/update-databricks-on-aws-8f0bcd2b.md)

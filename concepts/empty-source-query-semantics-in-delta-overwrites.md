---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c3e02c3067d142c088fef229bfd3976c4ce8b6493d6ff525808b3385d2dc65cb
  pageDirectory: concepts
  sources:
    - selectively-overwrite-data-with-delta-lake-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - empty-source-query-semantics-in-delta-overwrites
    - ESQSIDO
  citations:
    - file: selectively-overwrite-data-with-delta-lake-databricks-on-aws.md
      start: 18
      end: 21
    - file: selectively-overwrite-data-with-delta-lake-databricks-on-aws.md
      start: 79
      end: 80
    - file: selectively-overwrite-data-with-delta-lake-databricks-on-aws.md
      start: 101
      end: 102
    - file: selectively-overwrite-data-with-delta-lake-databricks-on-aws.md
      start: 35
      end: 36
    - file: selectively-overwrite-data-with-delta-lake-databricks-on-aws.md
      start: 23
      end: 23
title: Empty Source Query Semantics in Delta Overwrites
description: Behavioral differences between REPLACE WHERE (may delete data), REPLACE USING (no deletion), and REPLACE ON (no deletion) when the source query produces zero rows.
tags:
  - delta-lake
  - data-engineering
  - edge-cases
timestamp: "2026-06-19T23:02:06.968Z"
---

# Empty Source Query Semantics in Delta Overwrites

**Empty Source Query Semantics in Delta Overwrites** refers to the behavior of [Delta Lake](/concepts/delta-lake.md) overwrite operations when the source query (the data being written) produces zero rows. The effect on existing target table data depends on which selective overwrite method is used: `REPLACE WHERE` may delete data, while `REPLACE USING` and `REPLACE ON` do not.

## Overview

When performing a selective overwrite in [Delta Lake](/concepts/delta-lake.md), users can choose among three primary methods: `REPLACE WHERE`, `REPLACE USING`, and `REPLACE ON`. If the source query returns an empty result set, the outcome differs significantly:

- `REPLACE USING` and `REPLACE ON` **do not delete** any rows from the target table.
- `REPLACE WHERE` **might delete** rows from the target table that match the specified predicate.

This distinction is critical for incremental or streaming workflows where the source data may occasionally be empty. Accidentally using `REPLACE WHERE` with an empty source can cause unintended data loss. ^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md#L18-L21]

## Behavior by Method

### `REPLACE USING`

`REPLACE USING` replaces rows in the target table when the specified key columns compare equal under equality. When the source query is empty, no rows are matched for replacement, and therefore **no table rows are deleted**. The target table remains unchanged. ^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md#L79-L80]

### `REPLACE ON`

`REPLACE ON` uses a user-defined condition (including NULL-safe matching) to determine which rows to replace. Similar to `REPLACE USING`, an empty source query results in **no deletion** of any table rows. ^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md#L101-L102]

### `REPLACE WHERE`

`REPLACE WHERE` overwrites data that matches an arbitrary boolean expression. When the source query is empty, the operation still evaluates the predicate against the target table. Because there is no source data to write, the overwrite effectively **deletes all rows that satisfy the predicate**. This behavior can lead to accidental removal of large portions of the table. ^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md#L35-L36]

## Implications

- **Safer for empty sources**: Use `REPLACE USING` or `REPLACE ON` when the source might be empty, to avoid unintended deletion.
- **Risk with `REPLACE WHERE`**: Ensure the source is never empty when using `REPLACE WHERE`, or guard the operation with a conditional check.
- **Recovery**: If data has been accidentally overwritten or deleted, Delta Lake’s `RESTORE` command can undo the change, provided the table history has not been vacuumed. ^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md#L23-L23]

## Related Concepts

- [Delta Lake selective overwrite](/concepts/replace-where-selective-overwrite.md) – Overview of all selective overwrite methods.
- REPLACE WHERE – The overwrite method that can delete data on empty source.
- REPLACE USING – Dynamic data overwrite method safe for empty sources.
- [REPLACE ON](/concepts/create-or-replace-clone.md) – Condition-based overwrite method safe for empty sources.
- Delta Lake history and restore – Mechanism to revert accidental overwrites.

## Sources

- selectively-overwrite-data-with-delta-lake-databricks-on-aws.md

# Citations

1. [selectively-overwrite-data-with-delta-lake-databricks-on-aws.md:18-21](/references/selectively-overwrite-data-with-delta-lake-databricks-on-aws-3465bfbb.md)
2. [selectively-overwrite-data-with-delta-lake-databricks-on-aws.md:79-80](/references/selectively-overwrite-data-with-delta-lake-databricks-on-aws-3465bfbb.md)
3. [selectively-overwrite-data-with-delta-lake-databricks-on-aws.md:101-102](/references/selectively-overwrite-data-with-delta-lake-databricks-on-aws-3465bfbb.md)
4. [selectively-overwrite-data-with-delta-lake-databricks-on-aws.md:35-36](/references/selectively-overwrite-data-with-delta-lake-databricks-on-aws-3465bfbb.md)
5. [selectively-overwrite-data-with-delta-lake-databricks-on-aws.md:23-23](/references/selectively-overwrite-data-with-delta-lake-databricks-on-aws-3465bfbb.md)

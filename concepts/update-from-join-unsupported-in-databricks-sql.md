---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 87191ccd4881be0a11e59ae388dd16d8506b628308e5d6334aec523d73850f5a
  pageDirectory: concepts
  sources:
    - update-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - update-from-join-unsupported-in-databricks-sql
    - UFJ(IDS
  citations:
    - file: update-databricks-on-aws.md
title: UPDATE FROM JOIN (Unsupported in Databricks SQL)
description: Databricks SQL does not support the UPDATE...FROM...JOIN syntax used in other SQL dialects; users must use MERGE INTO instead.
tags:
  - sql
  - syntax-differences
  - databricks-sql
timestamp: "2026-06-19T23:16:33.510Z"
---

## UPDATE FROM JOIN (Unsupported in Databricks SQL)

**UPDATE FROM JOIN** refers to a SQL syntax pattern used in some database systems where a table is updated based on a join with another table or subquery using the `UPDATE ... FROM ... JOIN` clause. This syntax is **not supported** in Databricks SQL. ^[update-databricks-on-aws.md]

### Syntax Limitation

Databricks SQL does not allow the `UPDATE...FROM...JOIN` construct. If you attempt to write an `UPDATE` statement that directly joins another table — for example, `UPDATE t1 SET t1.c1 = t2.c1 FROM t1 INNER JOIN t2 ON t1.c2 = t2.c2` — Databricks SQL will reject it. The platform's `UPDATE` statement is only supported for [Delta Lake](/concepts/delta-lake.md) tables and can only reference the target table directly, optionally with subqueries in the `WHERE` clause (subject to certain restrictions on nested subqueries and `NOT IN` inside `OR`). ^[update-databricks-on-aws.md]

### Alternative Using MERGE INTO

To update a table based on a join with another table or subquery, use [MERGE INTO](/concepts/merge-into-delta-lake.md) instead. `MERGE INTO` provides the same logic as an `UPDATE FROM JOIN` and is the recommended replacement. The `MERGE` statement matches rows between the target table and a source (which can be a table, view, or subquery) and performs updates on the matched rows. ^[update-databricks-on-aws.md]

### Examples

The following example demonstrates the equivalent of an unsupported `UPDATE FROM JOIN` using `MERGE INTO`:

```sql
-- Not supported in Databricks SQL:
-- UPDATE t1 SET t1.c1 = t2.c1 FROM t1 INNER JOIN t2 ON t1.c2 = t2.c2

-- Equivalent using MERGE INTO:
MERGE INTO t1
USING t2 ON t1.c2 = t2.c2
WHEN MATCHED THEN UPDATE SET t1.c1 = t2.c1;
```

^[update-databricks-on-aws.md]

Using `MERGE` instead of the unsupported `UPDATE...FROM...JOIN` ensures compatibility with Databricks SQL and leverages the full transactional guarantees of [Delta Lake](/concepts/delta-lake.md). For more complex join-based updates, `MERGE INTO` can also handle multiple `WHEN MATCHED` and `WHEN NOT MATCHED` clauses.

### Related Concepts

- [MERGE INTO](/concepts/merge-into-delta-lake.md) — The recommended replacement for `UPDATE FROM JOIN`.
- UPDATE — The standard `UPDATE` statement on [Delta Lake](/concepts/delta-lake.md) tables.
- [Delta Lake](/concepts/delta-lake.md) — The storage layer that supports transactional `UPDATE` operations.
- DELETE and INSERT — Other DML statements with similar pattern restrictions.

### Sources

- update-databricks-on-aws.md

# Citations

1. [update-databricks-on-aws.md](/references/update-databricks-on-aws-8f0bcd2b.md)

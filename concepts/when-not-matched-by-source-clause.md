---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8c9c49093438a452d61ff6f59373bdf69a948c82c9615a5bbb8b1ecf9b7f1a22
  pageDirectory: concepts
  sources:
    - merge-into-databricks-on-aws.md
    - upsert-into-a-delta-lake-table-using-merge-databricks-on-aws.md
  confidence: 1
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - when-not-matched-by-source-clause
    - WNMBSC
    - WHEN NOT MATCHED BY SOURCE (UPDATE/DELETE) Clause
  citations:
    - file: merge-into-databricks-on-aws.md
    - file: upsert-into-a-delta-lake-table-using-merge-databricks-on-aws.md
title: WHEN NOT MATCHED BY SOURCE Clause
description: A merge clause that acts on target rows that have no match in the source table, supporting DELETE and UPDATE actions (Databricks Runtime 12.2 LTS+), with conditions limited to target table columns.
tags:
  - delta-lake
  - sql
  - merge
timestamp: "2026-06-19T19:31:46.038Z"
---

# WHEN NOT MATCHED BY SOURCE Clause

The **WHEN NOT MATCHED BY SOURCE** clause is an extension of the [MERGE INTO](/concepts/merge-into-delta-lake.md) statement for [Delta Lake](/concepts/delta-lake.md) tables. It defines actions to perform on rows in the target table that do **not** match any row in the source table based on the merge condition. This clause is supported in Databricks SQL and Databricks Runtime 12.2 LTS and above. ^[merge-into-databricks-on-aws.md]

## Syntax

```sql
WHEN NOT MATCHED BY SOURCE [ AND not_matched_by_source_condition ] THEN not_matched_by_source_action
```

Where `not_matched_by_source_action` can be:

- `DELETE` – deletes the unmatched target row.
- `UPDATE SET { column = { expr | DEFAULT } } [, ...]` – updates specified columns of the unmatched target row. ^[merge-into-databricks-on-aws.md]

## Behavior

A `WHEN NOT MATCHED BY SOURCE` clause is evaluated for each target row that does not satisfy the `ON merge_condition` with any source row. If an optional `not_matched_by_source_condition` is provided, the action is executed only when that condition evaluates to true for the target row. ^[merge-into-databricks-on-aws.md]

The `not_matched_by_source_condition` must be a Boolean expression that only references columns from the target table; source columns are not available because no source row matched. ^[merge-into-databricks-on-aws.md]

In the `UPDATE` action, each `expr` may only reference columns from the target table. Attempting to reference source columns causes an analysis error. ^[merge-into-databricks-on-aws.md]

## Allowed Actions

### `DELETE`

Deletes the unmatched target row. For example, to remove records from the target that no longer exist in the source:

```sql
MERGE INTO target AS t
USING source AS s
ON t.key = s.key
WHEN NOT MATCHED BY SOURCE THEN DELETE
```

^[merge-into-databricks-on-aws.md]

### `UPDATE`

Updates specified columns of the unmatched target row. Because there is no matching source row, new values must be literals, expressions on target columns, or `DEFAULT`. Example:

```sql
WHEN NOT MATCHED BY SOURCE THEN UPDATE SET t.status = 'inactive'
```

You can use `DEFAULT` to set a column to its default value:

```sql
WHEN NOT MATCHED BY SOURCE THEN UPDATE SET t.value = DEFAULT
```

^[merge-into-databricks-on-aws.md]

## Multiple `WHEN NOT MATCHED BY SOURCE` Clauses

Multiple such clauses are allowed and are evaluated in the order they are specified. Each clause except the last **must** have a `not_matched_by_source_condition`. If the last clause omits the condition, it acts as a default action. If a target row satisfies no condition, it is left unchanged. ^[merge-into-databricks-on-aws.md]

```sql
WHEN NOT MATCHED BY SOURCE AND t.marked_for_deletion THEN DELETE
WHEN NOT MATCHED BY SOURCE THEN UPDATE SET t.value = DEFAULT
```

^[merge-into-databricks-on-aws.md]

## Performance Considerations

Adding a `WHEN NOT MATCHED BY SOURCE` clause can cause a large number of target rows to be modified because it applies to every target row that does not match any source row. For best performance, always attach a `not_matched_by_source_condition` to limit the scope—for example, only process rows within a recent time window. ^[merge-into-databricks-on-aws.md]

## Incremental Sync Pattern

A common use case is incrementally synchronising a target table with a source table that sees late-arriving changes or deletes. By restricting both the source and the target to a recent time window, you can atomically apply updates, inserts, and deletes without rewriting the entire table:

```sql
MERGE INTO target AS t
USING (SELECT * FROM source WHERE created_at >= current_date() - INTERVAL '5' DAY) AS s
ON t.key = s.key
WHEN MATCHED THEN UPDATE SET *
WHEN NOT MATCHED THEN INSERT *
WHEN NOT MATCHED BY SOURCE AND t.created_at >= current_date() - INTERVAL '5' DAY THEN DELETE
```

^[upsert-into-a-delta-lake-table-using-merge-databricks-on-aws.md]

## Programmatic API

In the [Python](/concepts/python-wheel-task.md) and Scala APIs for Delta Lake, the clause is expressed using `.whenNotMatchedBySourceDelete()` and `.whenNotMatchedBySourceUpdate(...)` methods:

```python
(targetDF
  .merge(sourceDF, "source.key = target.key")
  .whenMatchedUpdateAll()
  .whenNotMatchedInsertAll()
  .whenNotMatchedBySourceDelete()
  .execute())
```

For conditional updates:

```python
.whenNotMatchedBySourceUpdate(
    condition="target.lastSeen >= (current_date() - INTERVAL '5' DAY)",
    set = {"target.status": "'inactive'"}
)
```

^[upsert-into-a-delta-lake-table-using-merge-databricks-on-aws.md]

## Error Conditions

- If a `WHEN NOT MATCHED BY SOURCE` clause (other than the last) has no condition, the query fails with a `NON_LAST_NOT_MATCHED_BY_SOURCE_CLAUSE_OMIT_CONDITION` error. ^[merge-into-databricks-on-aws.md]

## Related Concepts

- [MERGE INTO](/concepts/merge-into-delta-lake.md) – The complete DML statement that contains the `WHEN NOT MATCHED BY SOURCE` clause.
- [WHEN MATCHED Clause](/concepts/when-matched-clause.md) – Actions for rows that match.
- [WHEN NOT MATCHED Clause](/concepts/when-not-matched-insert-clause.md) – Actions for source rows without a target match.
- [Delta Lake](/concepts/delta-lake.md) – The storage layer that supports `MERGE`.
- Change Data Capture (CDC) – A pattern that often relies on `WHEN NOT MATCHED BY SOURCE` for deletes.

## Sources

- merge-into-databricks-on-aws.md
- upsert-into-a-delta-lake-table-using-merge-databricks-on-aws.md

# Citations

1. [merge-into-databricks-on-aws.md](/references/merge-into-databricks-on-aws-b9eee097.md)
2. [upsert-into-a-delta-lake-table-using-merge-databricks-on-aws.md](/references/upsert-into-a-delta-lake-table-using-merge-databricks-on-aws-8ae26349.md)

---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d0ec36e788d870d7f5cbaec19e178456687b496e5880559624567a868cd8d841
  pageDirectory: concepts
  sources:
    - delete-from-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - common-table-expressions-cte-in-dml
    - CTE(ID
    - Common Table Expression (CTE)
    - Common Table Expressions
    - Common Table Expressions (CTE)
    - CTE (Common Table Expressions)
    - Common Table Expression
    - common table expression
    - common_table_expression
  citations:
    - file: delete-from-databricks-on-aws.md
title: Common Table Expressions (CTE) in DML
description: Use of named CTE queries within DELETE statements on Delta Lake to improve readability and avoid repeated computation.
tags:
  - sql
  - cte
  - delta-lake
timestamp: "2026-06-19T14:58:53.375Z"
---

# Common Table Expressions (CTE) in DML

**Common Table Expressions (CTE) in DML** refers to the use of named, temporary result sets within data modification statements such as `DELETE`, `INSERT`, `UPDATE`, and `MERGE`. A CTE is defined once and can be referenced multiple times inside the enclosing DML statement, reducing repetitive subqueries and improving readability of complex logic.

## Overview

In Databricks SQL and Databricks Runtime, a CTE is one or more named queries that can be reused multiple times within the main query block. This reuse helps avoid repeated computations and makes nested, multi-step transformations easier to follow. CTEs in DML follow the same syntax rules as CTEs in `SELECT` statements. ^[delete-from-databricks-on-aws.md]

## Syntax in DELETE FROM

The `DELETE FROM` statement for Delta Lake tables supports an optional CTE clause placed before the `DELETE FROM` keyword. The general syntax is:

```sql
[ common_table_expression ]
DELETE FROM table_name [table_alias]
[WHERE predicate]
```

The CTE can define one or more named queries, and the `WHERE` predicate in the `DELETE` can reference those names. ^[delete-from-databricks-on-aws.md]

### Example

The following example uses a CTE to find the minimum session time from a reference table before deleting older events:

```sql
WITH min_time AS (
  SELECT min(session_time) AS min_st
  FROM good_events
)
DELETE FROM all_events
WHERE session_time < (SELECT min_st FROM min_time);
```

While the source documentation only provides a syntax example that includes CTE in `DELETE FROM`, the CTE construct is expected to work similarly in other DML statements (`INSERT`, `UPDATE`, `MERGE`) where a subquery or a named result set is allowed. ^[delete-from-databricks-on-aws.md]

## Benefits

- **Reusability**: A single CTE can be referenced multiple times in the same DML statement, eliminating redundant subquery definitions.
- **Readability**: Complex filtering logic can be broken into named, self-describing steps.
- **Performance**: Because the CTE is evaluated once and its result can be reused, repeated computations are avoided.

## Related Concepts

- Common Table Expression (CTE) in SELECT – The foundational use of CTEs in queries.
- [DELETE FROM](/concepts/delete-from-delta-lake.md) – Delta Lake `DELETE` syntax and predicate rules.
- INSERT INTO – DML statement that can also incorporate CTEs.
- [MERGE INTO](/concepts/merge-into-delta-lake.md) – Combines insert, update, and delete logic with potential CTE usage.
- [UPDATE statement](/concepts/update-statement-delta-lake.md) – DML modification that supports CTEs.
- [Delta Lake](/concepts/delta-lake.md) – The table format for which these DML statements are supported.

## Sources

- delete-from-databricks-on-aws.md

# Citations

1. [delete-from-databricks-on-aws.md](/references/delete-from-databricks-on-aws-ab1d0768.md)

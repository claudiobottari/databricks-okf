---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 73bbd02cfdba08755eb2aabf42a8de1b16e07a86fa3a42d09a697d99e5569b0f
  pageDirectory: concepts
  sources:
    - row-filters-and-column-masks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-type-mismatch-in-row-filters-and-column-masks
    - column masks and Data type mismatch in row filters
    - DTMIRFACM
  citations:
    - file: row-filters-and-column-masks-databricks-on-aws.md
title: Data type mismatch in row filters and column masks
description: Risks and unexpected behavior when UDF parameter types do not match table column types, including silent NULL conversion with ANSI mode disabled.
tags:
  - data-governance
  - unity-catalog
  - troubleshooting
  - best-practices
timestamp: "2026-06-19T20:16:34.344Z"
---

# Data type mismatch in row filters and column masks

**Data type mismatch in row filters and column masks** occurs when a table column passed to a row filter or column mask UDF has a different data type than the corresponding function parameter. Databricks performs implicit casting in such cases, which can lead to silent data corruption or incorrect filtering behavior.

## Behavior

When you create a row filter or column mask, the data type of each table column passed to the function must match the corresponding parameter type in the UDF. If there is a type mismatch—such as a `STRING` column passed to an `INT` parameter—Databricks implicitly casts the column value to the parameter type. This can cause unexpected behavior when the column contains values that cannot be converted. ^[row-filters-and-column-masks-databricks-on-aws.md]

### ANSI mode disabled (default)

With ANSI mode disabled (`spark.sql.ansi.enabled = false`), uncastable values are silently converted to `NULL`. No error is raised, and the UDF receives `NULL` instead of the actual column value. This can produce incorrect results, such as a row filter that returns all rows instead of filtering them, or a column mask that masks the wrong values. ^[row-filters-and-column-masks-databricks-on-aws.md]

### ANSI mode enabled

Databricks recommends enabling ANSI mode (`spark.sql.ansi.enabled = true`), which raises an error when a cast fails, making the problem immediately visible instead of silently returning `NULL`. ^[row-filters-and-column-masks-databricks-on-aws.md]

## Example: Row filter with a type mismatch

Consider a table with a `STRING` column (`department`) and a row filter whose parameter is accidentally declared as `INT` instead of `STRING`: ^[row-filters-and-column-masks-databricks-on-aws.md]

```sql
SET spark.sql.ansi.enabled = false;

CREATE TABLE employees (
  id INT,
  salary INT,
  department STRING
);

INSERT INTO employees VALUES
  (91, 200000, null),
  (1, 200000, 'exec'),
  (2, 50000, 'engineering'),
  (3, 150000, 'exec');

-- Bug: parameter type is INT, but the column is STRING
CREATE FUNCTION salary_filter(dept INT) RETURNS BOOLEAN
RETURN dept IS NULL;

ALTER TABLE employees SET ROW FILTER salary_filter ON (department);
```

When queried, the `department` values `'exec'` and `'engineering'` cannot be cast to `INT`, so they are silently converted to `NULL`. Because the filter returns `true` when the input is `NULL`, all rows are returned instead of only the rows where `department` is actually `NULL`. ^[row-filters-and-column-masks-databricks-on-aws.md]

The correct UDF definition uses `STRING` as the parameter type to match the column: ^[row-filters-and-column-masks-databricks-on-aws.md]

```sql
CREATE FUNCTION salary_filter(dept STRING) RETURNS BOOLEAN
RETURN dept IS NULL;
```

With this fix, the query returns only the row where `department` is `NULL`. ^[row-filters-and-column-masks-databricks-on-aws.md]

## Prevention

To avoid data type mismatches: ^[row-filters-and-column-masks-databricks-on-aws.md]

- Ensure that each UDF parameter type matches the corresponding table column type exactly.
- Enable ANSI mode (`spark.sql.ansi.enabled = true`) to surface casting errors immediately.
- Test row filters and column masks with representative data before applying them to production tables.

## Related Concepts

- [Row filters](/concepts/row-filter-policies.md) — SQL UDFs that restrict which rows a user can see in a table.
- [Column masks](/concepts/column-mask-policies.md) — SQL UDFs that control what values a user sees for specific columns.
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that enforces these access controls.
- SQL UDFs — User-defined functions used to implement filtering and masking logic.
- ABAC policies — An alternative approach for consistent filtering and masking across many tables.

## Sources

- row-filters-and-column-masks-databricks-on-aws.md

# Citations

1. [row-filters-and-column-masks-databricks-on-aws.md](/references/row-filters-and-column-masks-databricks-on-aws-f091f827.md)

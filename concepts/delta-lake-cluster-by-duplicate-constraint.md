---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cb9719942aa54ca8de5ec5eff3ebd07999ff89aa8446b54791f9a28440cc220c
  pageDirectory: concepts
  sources:
    - delta_duplicate_columns_found-error-condition-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-cluster-by-duplicate-constraint
    - DLCBDC
  citations:
    - file: delta_duplicate_columns_found-error-condition-databricks-on-aws.md
title: Delta Lake CLUSTER BY Duplicate Constraint
description: A constraint in Delta Lake that the CLUSTER BY clause must not contain duplicate column references, enforced by the CLUSTER_BY sub-reason of DELTA_DUPLICATE_COLUMNS_FOUND.
tags:
  - delta-lake
  - clustering
  - schema-constraints
timestamp: "2026-06-19T15:04:28.205Z"
---

Here is the wiki page for "Delta Lake CLUSTER BY Duplicate Constraint".

---

## Delta Lake CLUSTER BY Duplicate Constraint

The **Delta Lake CLUSTER BY Duplicate Constraint** is an error condition that occurs when a [Delta Lake Table](/concepts/delta-lake-table.md)'s `CLUSTER BY` clause contains duplicate column references. It is a specific subclass of the more general `DELTA_DUPLICATE_COLUMNS_FOUND` error class. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]

### Error Details

The error is raised with the SQLSTATE code `42711`. When triggered, the error message includes the duplicate column or columns found in the statement. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]

### Specific Subtype: CLUSTER_BY

The `CLUSTER_BY` sub-type of `DELTA_DUPLICATE_COLUMNS_FOUND` is raised specifically when duplicates are found in the `CLUSTER BY` clause. This occurs when a column name appears more than once in the `CLUSTER BY` specification during table creation or alteration. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]

For example, the following would trigger this error:

```sql
CREATE TABLE example (
  id INT,
  category STRING,
  value INT
) USING DELTA
CLUSTER BY (id, category, id);
```

### Related Error Subtypes

The `DELTA_DUPLICATE_COLUMNS_FOUND` error class includes several other subtypes that cover duplicate column issues in different contexts: ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]

| Subtype | Context |
|---------|---------|
| `ADDING_COLUMNS` | Duplicates found when adding columns |
| `CONVERT_TO_DELTA` | Duplicates found during conversion to Delta |
| `DATA` | Duplicates found in the data being saved |
| `EXISTING_SCHEMA` | Duplicates found in the existing table schema or metadata update |
| `PARTITION_COLUMNS` | Duplicates found in partition columns |
| `PARTITION_SCHEMA` | Duplicates found in the partition schema |
| `READ_SCHEMA` | Duplicates found in the schema of the data being read |
| `REPLACING_COLUMNS` | Duplicates found while replacing columns |
| `SPECIFIED_COLUMNS` | Duplicates found in specified columns |
| `TABLE_SCHEMA` | Duplicates found in the table schema |

### Best Practices

To avoid this error:
- Ensure each column appears only once in any `CLUSTER BY` clause.
- Validate the column list before executing `CREATE TABLE` or `ALTER TABLE` statements that include `CLUSTER BY`.

### Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The storage layer that enforces this constraint.
- [Liquid Clustering](/concepts/liquid-clustering.md) — The feature that uses the `CLUSTER BY` clause to organize data.
- DELTA_DUPLICATE_COLUMNS_FOUND — The parent error class for all duplicate column errors.
- [Delta Lake Error Conditions](/concepts/delta-error-sub-conditions.md) — General reference for Delta Lake error handling.

### Sources

- delta_duplicate_columns_found-error-condition-databricks-on-aws.md

# Citations

1. [delta_duplicate_columns_found-error-condition-databricks-on-aws.md](/references/delta_duplicate_columns_found-error-condition-databricks-on-aws-42950ac1.md)

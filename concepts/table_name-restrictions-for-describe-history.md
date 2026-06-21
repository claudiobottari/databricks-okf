---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ae11e5cf782272918e7c2c527f3fbc2c211d4b37c5ac0862c3b62817565c8101
  pageDirectory: concepts
  sources:
    - describe-history-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - table_name-restrictions-for-describe-history
    - TRFDH
  citations:
    - file: describe-history-databricks-on-aws.md
title: table_name restrictions for DESCRIBE HISTORY
description: The table name used with DESCRIBE HISTORY must not include a temporal specification or options specification.
tags:
  - sql
  - syntax
  - restrictions
timestamp: "2026-06-18T15:27:13.497Z"
---

# table_name restrictions for DESCRIBE HISTORY

**table_name restrictions for DESCRIBE HISTORY** specifies the constraints on the `table_name` parameter used in the `DESCRIBE HISTORY` SQL command. The command returns provenance information—such as the operation, user, and timestamp—for each write to a Delta table. Table history is retained for 30 days. ^[describe-history-databricks-on-aws.md]

## Restriction

The `table_name` parameter must identify an existing Delta table. **The name must not include a temporal specification or options specification.** ^[describe-history-databricks-on-aws.md]

In other words, you cannot use time-travel syntax (e.g., `@v1`, `TIMESTAMP AS OF …`) or table options (e.g., `VERSION AS OF …`) when specifying the table for `DESCRIBE HISTORY`. Only the bare table identifier (with optional schema and catalog qualifiers) is allowed. ^[describe-history-databricks-on-aws.md]

## Example

The following is a valid invocation:

```sql
DESCRIBE HISTORY my_table;
```

The following are **invalid** because they include temporal or options specifications:

- `DESCRIBE HISTORY my_table@v1;`
- `DESCRIBE HISTORY my_table TIMESTAMP AS OF '2024-01-01';`

## Related Concepts

- [DESCRIBE HISTORY](/concepts/describe-history.md) – Full command reference.
- [Delta table](/concepts/delta-lake-table.md) – The table type to which `DESCRIBE HISTORY` applies.
- Work with table history – More details on the history output.
- temporal specification – Syntax for time-travel queries, which is disallowed here.
- options specification – Syntax for table options, also disallowed.

## Sources

- describe-history-databricks-on-aws.md

# Citations

1. [describe-history-databricks-on-aws.md](/references/describe-history-databricks-on-aws-c4aeec74.md)

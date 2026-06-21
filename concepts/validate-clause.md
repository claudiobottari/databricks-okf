---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8c792f58e04f2d528afb18cc16a66c2ed96e5c32a1022ed25b3bd3cdc0637290
  pageDirectory: concepts
  sources:
    - copy-into-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - validate-clause
  citations:
    - file: copy-into-databricks-on-aws.md
title: VALIDATE Clause
description: A validation clause in COPY INTO that checks data can be parsed, schema matches, and constraints are met without writing to the table
tags:
  - databricks
  - data-quality
  - validation
timestamp: "2026-06-19T09:25:24.269Z"
---

# VALIDATE Clause

The **VALIDATE clause** is an optional parameter of the [COPY INTO](/concepts/copy-into-command.md) command that validates data before loading it into a [Delta table](/concepts/delta-lake-table.md). When specified, the command checks whether the source data can be parsed, whether the schema matches the target table, and whether all constraints are satisfied — but does not write any data to the table. ^[copy-into-databricks-on-aws.md]

## Syntax

```sql
COPY INTO target_table
FROM source
FILEFORMAT = data_source
VALIDATE [ ALL | num_rows ROWS ]
```

The `VALIDATE` clause appears after the `FILEFORMAT` specification and before other optional clauses such as `FILES`, `PATTERN`, `FORMAT_OPTIONS`, or `COPY_OPTIONS`. ^[copy-into-databricks-on-aws.md]

## Parameters

- **`ALL`** (default): Validates all data that would be loaded by the `COPY INTO` command. This is the default behavior when `VALIDATE` is specified without a row count. ^[copy-into-databricks-on-aws.md]
- **`num_rows ROWS`**: Validates only the specified number of rows from the source data. For example, `VALIDATE 15 ROWS` checks the first 15 rows. When a number less than 50 is used, the command returns a preview of up to 50 rows of data. ^[copy-into-databricks-on-aws.md]

## Validations Performed

The `VALIDATE` clause checks the following conditions on the source data: ^[copy-into-databricks-on-aws.md]

- **Parsability**: Whether the data can be parsed according to the specified file format and format options.
- **Schema compatibility**: Whether the schema of the source data matches the schema of the target Delta table, or whether schema evolution is needed.
- **Constraint compliance**: Whether all nullability and check constraints on the target table are satisfied.

## Behavior

When `VALIDATE` is used, the `COPY INTO` command returns a preview of the validated data but does not modify the target table. This makes it useful for: ^[copy-into-databricks-on-aws.md]

- Testing whether new data sources are compatible with an existing table schema.
- Debugging parsing or schema mismatch issues before committing a full load.
- Previewing a sample of incoming data to verify correctness.

## Applicability

The `VALIDATE` clause applies to Databricks SQL and Databricks Runtime 10.4 LTS and above. ^[copy-into-databricks-on-aws.md]

## Related Concepts

- [COPY INTO](/concepts/copy-into-command.md) — The parent command that loads data into Delta tables.
- [Delta table](/concepts/delta-lake-table.md) — The target table format for `COPY INTO` operations.
- Schema evolution — How `COPY INTO` handles schema changes via the `mergeSchema` copy option.
- Data ingestion patterns — Common patterns for loading data into Databricks.

## Sources

- copy-into-databricks-on-aws.md

# Citations

1. [copy-into-databricks-on-aws.md](/references/copy-into-databricks-on-aws-02102312.md)

---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0ff8152d391a306acb7f50337de079eaceea58013e2c0a06bba79150b773f2da
  pageDirectory: concepts
  sources:
    - copy-into-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - copy-into-validate-mode
    - CIVM
  citations:
    - file: copy-into-databricks-on-aws.md
title: COPY INTO VALIDATE Mode
description: A validation mode that checks parseability, schema compatibility, and constraints without writing data; supports row-limited previews.
tags:
  - databricks
  - data-validation
  - sql
timestamp: "2026-06-19T17:53:27.961Z"
---

```markdown
---
title: COPY INTO VALIDATE Mode
summary: A validation mode that parses and checks source data against table constraints without writing to the table.
sources:
  - copy-into-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:11:43.910Z"
updatedAt: "2026-06-18T14:45:23.140Z"
tags:
  - databricks
  - data-validation
  - sql
aliases:
  - copy-into-validate-mode
  - CIVM
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# COPY INTO VALIDATE Mode

**COPY INTO VALIDATE mode** is a subclause of the `COPY INTO` command in Databricks SQL and Databricks Runtime that validates data before loading, without committing it to the target Delta table. It is a retryable and idempotent operation that skips files in the source location that have already been loaded. ^[copy-into-databricks-on-aws.md]

## Syntax

`VALIDATE` is used as part of the `COPY INTO` statement, placed after the `FILEFORMAT` clause:^[copy-into-databricks-on-aws.md]

```sql
COPY INTO target_table
  FROM source_clause
  FILEFORMAT = data_source
  VALIDATE [ ALL | num_rows ROWS ]
  [ other_options ]
```

## How VALIDATE works

When `VALIDATE` is specified, the command inspects the incoming data but does **not** write it to the table. The following checks are performed:^[copy-into-databricks-on-aws.md]

- Whether the data can be parsed.
- Whether the schema matches that of the table or if the schema needs to be evolved.
- Whether all nullability and check constraints are met.

By default, `VALIDATE` without a row count validates **all** of the data that is to be loaded.^[copy-into-databricks-on-aws.md]

### Limiting validation to a sample of rows

You can provide a specific number of rows to validate using the `ROWS` keyword:^[copy-into-databricks-on-aws.md]

```sql
COPY INTO target_table
  FROM ...
  FILEFORMAT = data_source
  VALIDATE 15 ROWS
```

When a number less than 50 is specified with `ROWS`, the `COPY INTO` statement returns a preview of the data of **50 rows or fewer**.^[copy-into-databricks-on-aws.md]

## Use cases

`VALIDATE` mode is useful for:^[copy-into-databricks-on-aws.md]

- **Testing data compatibility** – Before a full load, you can verify that the source files match the target table's schema and constraints.
- **Debugging schema errors** – When a `COPY INTO` operation fails, use `VALIDATE` to determine whether the data is malformed or the schema does not align.
- **Previewing incoming data** – With a small row count (e.g., `VALIDATE 5 ROWS`), you can inspect a sample of the data to confirm its structure.

## Related concepts

- [[COPY INTO Command|COPY INTO]] – The full command that loads data into a Delta table; `VALIDATE` is a subclause that skips the actual write.
- [[Delta Lake Table|Delta table]] – The target table for `COPY INTO` operations; `VALIDATE` checks schema compatibility against this table.
- Auto Loader – An alternative incremental ingestion tool recommended for very large directories with many files.
- File metadata column – How to access metadata for file-based data sources when using `COPY INTO`.
- Schema evolution – Controlled via the `mergeSchema` option in `COPY_OPTIONS`; `VALIDATE` can detect whether evolution is needed without applying it.

## Sources

- copy-into-databricks-on-aws.md
```

# Citations

1. [copy-into-databricks-on-aws.md](/references/copy-into-databricks-on-aws-02102312.md)

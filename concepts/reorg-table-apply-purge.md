---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: df66ea51bebef8d11ff976fd98362ae2d03b51ab460e87db26bd5c1a72e9e2ac
  pageDirectory: concepts
  sources:
    - delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - reorg-table-apply-purge
    - RTA(
    - reorg-table-apply-purge-command
    - RTA(C
  citations:
    - file: delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md
title: REORG TABLE APPLY (PURGE)
description: A Delta Lake SQL command to purge deletion vectors from a table, enabling compatibility with symlink manifest generation.
tags:
  - delta-lake
  - sql-commands
  - data-maintenance
timestamp: "2026-06-19T15:09:57.781Z"
---

```markdown
---
title: REORG TABLE APPLY (PURGE)
summary: A Delta Lake command used to purge deletion vectors from a table, enabling compatibility with unsupported features like symlink manifest generation
sources:
  - delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:58:20.726Z"
updatedAt: "2026-06-19T10:11:13.080Z"
tags:
  - delta-lake
  - commands
  - data-engineering
aliases:
  - reorg-table-apply-purge
  - RTA(
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 1
---

# REORG TABLE APPLY (PURGE)

**REORG TABLE APPLY (PURGE)** is a [[Delta Lake]] SQL command that produces a version of a [[Delta Lake Table|Delta table]] without [[deletion vectors]]. It is the recommended resolution when deletion vectors prevent the use of features such as incremental symlink manifest generation. ^[delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md]

## Syntax

```sql
REORG TABLE <table_name> APPLY (PURGE)
```

Replace `table_name` with the fully qualified table name (for example, `catalog.schema.table`).

## When to Use

The DELTA_VIOLATE_TABLE_PROPERTY_VALIDATION_FAILED error class reports table property conflicts. The source material explicitly recommends `REORG TABLE APPLY (PURGE)` for one specific sub‑condition:

### EXISTING_DELETION_VECTORS_WITH_INCREMENTAL_MANIFEST_GENERATION

symlink_format_manifest|Symlink manifest generation is unsupported while deletion vectors are present in the table. To produce a version of the table without deletion vectors, run `REORG TABLE <table> APPLY (PURGE)`. ^[delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md]

### Other Related Error Sub‑conditions

The source material lists two additional sub‑conditions that also involve deletion vectors, but does **not** specify `REORG TABLE APPLY (PURGE)` as a resolution for them:

- **PERSISTENT_DELETION_VECTORS_IN_NON_PARQUET_TABLE** – Persistent deletion vectors are supported only on Parquet‑based Delta tables.
- **PERSISTENT_DELETION_VECTORS_WITH_INCREMENTAL_MANIFEST_GENERATION** – Persistent deletion vectors and incremental symlink manifest generation are mutually exclusive. ^[delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md]

## Behavior

After executing the command, the table no longer maintains deletion vectors. This enables features that are incompatible with deletion vectors, such as incremental symlink manifest generation. The command is part of [[delta-lake-table|Delta Lake Table]] maintenance and restructuring.

## Related Concepts

- [[Deletion Vectors]] – The mechanism for tracking logically deleted rows without physical removal.
- [[Symlink Manifest Generation|Symlink Manifest]] – The manifest format used for incremental manifest generation.
- [[Delta Lake Table|Delta Table]] – The underlying table format.
- DELTA_VIOLATE_TABLE_PROPERTY_VALIDATION_FAILED – The error class that reports the property conflicts.
- [[Incremental Symlink Manifest Generation|Incremental Manifest Generation]] – A feature that conflicts with deletion vectors.

## Sources

- delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md
```

# Citations

1. [delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md](/references/delta_violate_table_property_validation_failed-error-condition-databricks-on-aws-8e86a725.md)

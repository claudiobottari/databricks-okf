---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 241020e2230e4a0a003dc2772780754ab60bc1d319b12216a2c6396019f1e0d7
  pageDirectory: concepts
  sources:
    - archival-support-in-databricks-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - show-archived-files-syntax
    - SAFS
    - SHOW ARCHIVED FILES
    - Show archived files
    - SHOW ARCHIVED FILES command
    - Show archived files (Delta Lake)
  citations:
    - file: archival-support-in-databricks-databricks-on-aws.md
title: SHOW ARCHIVED FILES syntax
description: A SQL command that returns URIs of archived files required to satisfy a given query, enabling targeted restoration.
tags:
  - databricks
  - delta-lake
  - sql
  - archival
timestamp: "2026-06-19T22:07:39.063Z"
---

```markdown
---
title: SHOW ARCHIVED FILES syntax
summary: A SQL command to identify which files in a Delta table must be restored from archival storage to complete a given query.
sources:
  - archival-support-in-databricks-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:48:04.185Z"
updatedAt: "2026-06-19T17:35:05.392Z"
tags:
  - delta-lake
  - sql
  - archival
aliases:
  - show-archived-files-syntax
  - SAFS
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 1
---

# SHOW ARCHIVED FILES syntax

**`SHOW ARCHIVED FILES`** is a SQL statement in Databricks that returns the URIs of archived files in a [[Delta Lake Table|Delta table]] that must be restored to complete a given query. This command helps you identify exactly which files need to be restored from archival storage so that the query can succeed. ^[archival-support-in-databricks-databricks-on-aws.md]

## Syntax

```sql
SHOW ARCHIVED FILES FOR table_name [ WHERE predicate ];
```

^[archival-support-in-databricks-databricks-on-aws.md]

## Parameters

- **`table_name`**: The name of the Delta table to inspect for archived files. Supports the three-level namespace (`catalog.schema.table`). ^[archival-support-in-databricks-databricks-on-aws.md]
- **`WHERE predicate`** (optional): A filter condition that narrows the results to only those archived files whose data would be needed to satisfy the given predicate. Databricks recommends providing predicates that include fields on which data is partitioned, Z-ordered, or clustered to reduce the number of files that must be restored. ^[archival-support-in-databricks-databricks-on-aws.md]

## Return value

The command returns a [[Spark DataFrame Evaluation Pattern|Spark DataFrame]] containing URIs for all archived files that must be read to determine whether or not records fulfilling a predicate exist in those files. Each row represents one archived file that requires restoration. ^[archival-support-in-databricks-databricks-on-aws.md]

## How it works

During this operation, Delta Lake only has access to the data statistics contained in the transaction log. By default, these are the following statistics collected on the first 32 columns in the table: ^[archival-support-in-databricks-databricks-on-aws.md]

- Minimum values
- Maximum values
- Null counts
- Total number of records

The files returned include all archived files that must be read to determine whether or not records fulfilling the predicate exist in the file. ^[archival-support-in-databricks-databricks-on-aws.md]

## Example

```sql
-- Identify all archived files in the table
SHOW ARCHIVED FILES FOR sales_data;

-- Identify archived files that would be needed for a filtered query
SHOW ARCHIVED FILES FOR sales_data WHERE order_date > '2024-01-01';
```

^[archival-support-in-databricks-databricks-on-aws.md]

## Related operations

### Restore archived files

After identifying the archived files with `SHOW ARCHIVED FILES`, use the S3 restore object APIs to restore your files to a fast retrieval storage tier. After restoring the files, queries against the table automatically recognize the restored data. ^[archival-support-in-databricks-databricks-on-aws.md]

### Update or delete archived data

`MERGE`, `UPDATE`, or `DELETE` operations fail if they impact data in archived files. Use `SHOW ARCHIVED FILES` to determine the files that you must restore before running these operations. ^[archival-support-in-databricks-databricks-on-aws.md]

## Requirements

- Databricks Runtime 13.3 LTS and above (Public Preview). ^[archival-support-in-databricks-databricks-on-aws.md]
- Archival support must be enabled on the Delta table via the `delta.timeUntilArchived` table property. ^[archival-support-in-databricks-databricks-on-aws.md]
- The Delta transaction log (`_delta_log/` directory) must not be archived — only data files can be moved to archival storage. ^[archival-support-in-databricks-databricks-on-aws.md]

## Related Concepts

- [[Archival support in Databricks]] — Overview of the archival support feature
- [[Delta Lake]] — The underlying storage format
- ALTER TABLE SET TBLPROPERTIES — For configuring `delta.timeUntilArchived`
- S3 Lifecycle Policies — For configuring cloud-side archival rules

## Sources

- archival-support-in-databricks-databricks-on-aws.md
```

# Citations

1. [archival-support-in-databricks-databricks-on-aws.md](/references/archival-support-in-databricks-databricks-on-aws-d64d2061.md)

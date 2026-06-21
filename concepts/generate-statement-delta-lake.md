---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7339b890dc439d98203be4a0dbf7d97ef47bee8bbb3a4c16a13340749709dc5f
  pageDirectory: concepts
  sources:
    - generate-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - generate-statement-delta-lake
    - GS(L
    - DELETE Statement (Delta Lake)
  citations:
    - file: generate-databricks-on-aws.md
title: GENERATE statement (Delta Lake)
description: SQL command to generate manifest files for Delta tables, enabling external query engines to read Delta Lake data.
tags:
  - delta-lake
  - sql-reference
  - databricks
timestamp: "2026-06-19T10:42:25.998Z"
---

# GENERATE statement (Delta Lake)

The **GENERATE** statement produces manifest files for an existing Delta table. These manifest files enable external query engines, such as Presto and Athena, to read data from a Delta table without native Delta Lake support. ^[generate-databricks-on-aws.md]

## Syntax

```sql
GENERATE mode FOR TABLE table_name
```

^[generate-databricks-on-aws.md]

## Parameters

- **mode** – The only supported mode is `symlink_format_manifest`. This generates manifest files that list the files composing the Delta table. These can be used by Presto and Athena to discover and read the data. ^[generate-databricks-on-aws.md]
- **table_name** – The identifer of an existing Delta table. The name must not include a temporal specification or options specification. ^[generate-databricks-on-aws.md] (See Table name resolution).

## Usage notes

- The GENERATE statement is available in Databricks SQL and Databricks Runtime. ^[generate-databricks-on-aws.md]
- Manifest files are written to a `_symlink_format_manifest` directory inside the table’s storage location. For details on the generated file format and how to configure readers, see the Delta Lake documentation on [generating a manifest file](https://docs.delta.io/latest/delta-utility.html#generate-a-manifest-file). ^[generate-databricks-on-aws.md]

## Example

```sql
GENERATE symlink_format_manifest FOR TABLE my_delta_table;
```

This example generates a manifest file for the Delta table `my_delta_table`. The manifest can then be used by Presto or Athena to query the table. ^[generate-databricks-on-aws.md]

## Related concepts

- [Delta Lake](/concepts/delta-lake.md) – The storage layer that enables ACID transactions on data lakes.
- Presto – A distributed SQL query engine that can read Delta tables via manifest files.
- Athena – AWS’s serverless query service that supports Delta table manifests.
- [Manifest files](/concepts/delta-lake-manifest-files.md) – The `_symlink_format_manifest` directory holding symlink-based file lists.
- SQL statements on Delta Lake – Other Delta Lake-specific SQL commands.

## Sources

- generate-databricks-on-aws.md

# Citations

1. [generate-databricks-on-aws.md](/references/generate-databricks-on-aws-7753d696.md)

---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f1a7e70fd42f9886afa1ff2565ad02b90bac0c21a0d27e7dcc7b2eb9904ffb4a
  pageDirectory: concepts
  sources:
    - generate-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - symlink_format_manifest-mode
  citations:
    - file: generate-databricks-on-aws.md
title: symlink_format_manifest mode
description: A mode for the GENERATE command that produces manifest files enabling Presto and Athena to read Delta tables.
tags:
  - delta-lake
  - manifest
  - presto
  - athena
timestamp: "2026-06-18T12:28:29.021Z"
---

# symlink_format_manifest mode

**symlink_format_manifest mode** is a parameter of the `GENERATE` statement in Databricks SQL and Databricks Runtime that creates manifest files for a [Delta table](/concepts/delta-lake-table.md). These manifest files contain a list of data file paths and can be used to read Delta tables from external query engines such as Presto and Amazon Athena. ^[generate-databricks-on-aws.md]

## Syntax

```sql
GENERATE symlink_format_manifest FOR TABLE table_name
```

- **mode**: Must be the string `symlink_format_manifest`.
- **table_name**: Identifies an existing Delta table. The name must not include a temporal specification or options specification. ^[generate-databricks-on-aws.md]

## Usage

When this mode is specified, Databricks generates manifest files in the Delta table’s directory. These files act as a snapshot of the table's current data files, allowing Presto and Athena to read Delta tables without direct Delta Lake support. ^[generate-databricks-on-aws.md]

For full details of the manifest generation process, see the [Delta Lake documentation on generating a manifest file](https://docs.delta.io/latest/delta-utility.html#generate-a-manifest-file). ^[generate-databricks-on-aws.md]

## Related concepts

- [Delta table](/concepts/delta-lake-table.md) – The underlying storage format for which manifests are generated.
- Presto – A distributed SQL query engine that can consume symlink manifests.
- Amazon Athena – A serverless query service that can use symlink manifests to query Delta tables.
- [GENERATE command](/concepts/generate-command-delta-lake.md) – The Databricks SQL statement that accepts this mode.
- [Manifest file](/concepts/delta-lake-manifest-files.md) – The files produced by this mode.

## Sources

- generate-databricks-on-aws.md

# Citations

1. [generate-databricks-on-aws.md](/references/generate-databricks-on-aws-7753d696.md)

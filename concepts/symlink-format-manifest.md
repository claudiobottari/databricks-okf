---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 483008cf025e8c566edd012ee6c8a108100bd388706997061d4210ff764e354c
  pageDirectory: concepts
  sources:
    - generate-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - symlink-format-manifest
    - SFM
  citations:
    - file: generate-databricks-on-aws.md
title: Symlink format manifest
description: A manifest format that uses symlinks to allow Presto/Athena to read Delta tables by generating a list of Parquet files.
tags:
  - delta-lake
  - manifest
  - file-format
timestamp: "2026-06-19T10:42:41.450Z"
---

Here is the wiki page for "Symlink format manifest".

---

## Symlink Format Manifest

A **symlink format manifest** is a set of files generated for a [Delta table](/concepts/delta-lake-table.md) that lists the underlying data files (parquet files) that comprise the table's current snapshot. These manifest files act as a bridge between Delta Lake and external query engines such as Presto and Athena that do not natively understand the [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md). ^[generate-databricks-on-aws.md]


### Overview

Delta Lake manages table metadata and ACID transactions through a transaction log, but external engines read data files directly. The symlink format manifest provides a static directory of the current data files that an external engine can consume, enabling it to query the Delta table without needing to read the transaction log. ^[generate-databricks-on-aws.md]


### Generating the Manifest

To generate a symlink format manifest for an existing Delta table, use the `GENERATE` command with the mode `symlink_format_manifest`: ^[generate-databricks-on-aws.md]

```
GENERATE symlink_format_manifest FOR TABLE table_name
```

The `table_name` parameter must identify an existing Delta table and must not include a temporal specification or options specification. ^[generate-databricks-on-aws.md]


### Output

When run, the command produces manifest files in a subdirectory of the Delta table's storage location (typically `_symlink_format_manifest/`). These files contain the absolute paths to the parquet files that make up the current version of the table. ^[generate-databricks-on-aws.md]

> **Note:** The generated manifest is a point-in-time snapshot. Once generated, the file list may become stale if the Delta table receives subsequent writes, updates, or deletes. After any change to the Delta table, the manifest must be regenerated before the external engine will see the updated data. ^[generate-databricks-on-aws.md]


### Use Cases

- **Presto and Athena**: Symlink format manifests allow these SQL engines to read Delta tables without additional connectors or custom integration work.
- **Incremental snapshot sharing**: The manifest can be generated and distributed to provide a static view of the table for downstream systems that do not support the Delta protocol.
- **Migration and bulk export**: When moving data to environments that do not run Spark, the manifest identifies the exact set of files to transfer or copy. ^[generate-databricks-on-aws.md]


### Related Concepts

- [Generate a manifest file — Delta Lake docs](/concepts/delta-lake-manifest-files.md) – Detailed documentation from the Delta Lake project.
- [Delta table](/concepts/delta-lake-table.md) – The table type for which manifests are generated.
- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md) – The core metadata that the manifest replaces for external readers.
- Delta Lake utility commands – Other administrative commands for managing Delta tables.


### Sources

- generate-databricks-on-aws.md

# Citations

1. [generate-databricks-on-aws.md](/references/generate-databricks-on-aws-7753d696.md)

---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 30bcb7d16ee9d3e0dc417f5af4d0b4a97fa079af0c5a3d2cbf8d46fe893a17ff
  pageDirectory: concepts
  sources:
    - read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - reorg-for-upgrading-iceberg-read-support
    - RFUIRS
  citations:
    - file: read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md
title: REORG for Upgrading Iceberg Read Support
description: A SQL command (REORG TABLE ... APPLY UPGRADE UNIFORM) used to enable Iceberg reads on tables with deletion vectors, upgrade from IcebergCompatV1, or rewrite data for compatibility with Hive-style Parquet readers.
tags:
  - delta-lake
  - iceberg
  - sql-commands
timestamp: "2026-06-19T20:11:30.873Z"
---

# REORG for Upgrading Iceberg Read Support

**REORG for Upgrading Iceberg Read Support** is a SQL command used on Databricks to enable or upgrade [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) read support on an existing [Delta Lake Table](/concepts/delta-lake-table.md) while also rewriting underlying data files. It is the recommended approach when a table has features that are incompatible with the standard `ALTER TABLE` method. ^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md]

## Overview

The `REORG` command with the `UPGRADE UNIFORM(ICEBERG_COMPAT_VERSION=2)` clause performs two actions simultaneously:

1. It enables the `IcebergCompatV2` table feature, which allows Iceberg clients to read the [Delta Lake Table](/concepts/delta-lake-table.md).
2. It rewrites the underlying Parquet data files to ensure compatibility with the target Iceberg version.

This operation is synchronous and may take time proportional to the table size, as it involves rewriting data. ^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md]

## When to Use REORG

You should use `REORG` instead of the simpler `ALTER TABLE SET TBLPROPERTIES` approach if any of the following conditions apply:

- Your table has **deletion vectors** enabled. Deletion vectors are incompatible with `IcebergCompatV2`. `REORG` disables and purges deletion vectors while enabling Iceberg reads. ^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md]
- You previously enabled the **`IcebergCompatV1`** version of UniForm (the legacy format). Upgrading to `IcebergCompatV2` requires `REORG` to rewrite metadata and data files. ^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md]
- You need to read from **Iceberg engines that do not support Hive-style Parquet files**, such as Athena or Redshift. `REORG` rewrites the data using Zstandard compression and the column‑mapping mode required by `IcebergCompatV2`. ^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md]

## Using REORG

The SQL syntax is:

```sql
REORG TABLE table_name APPLY (UPGRADE UNIFORM(ICEBERG_COMPAT_VERSION=2));
```

Replace `table_name` with the fully qualified three‑level name (`catalog.schema.table`). The command must be run on a compute that supports Databricks Runtime 14.3 LTS or above. ^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md]

After `REORG` completes, the table will have:

- `delta.enableIcebergCompatV2 = true`
- `delta.universalFormat.enabledFormats = iceberg`
- Column mapping enabled (mode `name` is required for tables that previously had deletion vectors, but `REORG` handles this automatically).
- No deletion vectors.

You can verify that Iceberg reads are enabled by running `DESCRIBE EXTENDED table_name` and looking for the **Delta Uniform Iceberg** section, or by checking the table properties with `SHOW TBLPROPERTIES`. ^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md]

## Important Considerations

- **Zstandard compression**: Tables with Iceberg reads enabled use Zstandard instead of Snappy for Parquet data files. `REORG` rewrites existing files to this codec. ^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md]
- **Resource usage**: The rewrite operation increases driver and storage I/O load. Plan accordingly for large tables.
- **Read‑only for Iceberg clients**: Once enabled, external Iceberg clients can only read the table; writes must continue through Delta Lake on Databricks. ^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md]
- **Metadata generation**: After `REORG`, Iceberg metadata is generated automatically on subsequent Delta Lake write transactions. You can also manually trigger it with `MSCK REPAIR TABLE ... SYNC METADATA`. ^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md]

## Related Concepts

- [Delta Lake Universal Format (UniForm)](/concepts/delta-lake-universal-format-uniform.md)
- [IcebergCompatV2](/concepts/icebergcompatv2.md)
- [Column Mapping](/concepts/delta-table-column-mapping.md)
- [Deletion Vectors](/concepts/deletion-vectors.md)
- Zstandard Compression
- [MSCK REPAIR TABLE](/concepts/fsck-repair-table.md)
- [Unity Catalog](/concepts/unity-catalog.md)

## Sources

- read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md

# Citations

1. [read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md](/references/read-delta-lake-tables-with-iceberg-clients-databricks-on-aws-ae1b1933.md)

---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1c33b58a508c4d766e2c4329a18bd25ab8dde003b73445deec69c553dbe6e2e8
  pageDirectory: concepts
  sources:
    - unity-catalog-requirements-and-limitations-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-file-format-support
    - UCFFS
  citations:
    - file: unity-catalog-requirements-and-limitations-databricks-on-aws.md
title: Unity Catalog File Format Support
description: Managed tables in Unity Catalog require Delta or Iceberg format; external tables support Delta, CSV, JSON, Avro, Parquet, ORC, or text.
tags:
  - unity-catalog
  - file-formats
  - tables
timestamp: "2026-06-19T23:15:06.597Z"
---

# [Unity Catalog](/concepts/unity-catalog.md) File Format Support

**Unity Catalog File Format Support** defines which data file formats can be used for tables registered in [Unity Catalog](/concepts/unity-catalog.md). The supported formats differ based on whether the table is managed or external.

## Managed Tables

[Managed tables](/concepts/managed-tables-in-databricks.md) must use either **Delta Lake** or **Apache Iceberg** as their underlying file format. No other formats are permitted for managed tables because [Unity Catalog](/concepts/unity-catalog.md) requires full ownership and management of the underlying data for these tables. ^[unity-catalog-requirements-and-limitations-databricks-on-aws.md]

- **Delta Lake** – the default and most feature‑rich format, providing ACID transactions, schema enforcement, and time travel.
- **Apache Iceberg** – an open table format that offers similar capabilities and cross‑engine compatibility.

## External Tables

[External tables](/concepts/unity-catalog-external-table-conversion.md) have broader format support and can use any of the following formats: ^[unity-catalog-requirements-and-limitations-databricks-on-aws.md]

- **Delta Lake** – recommended for full [Unity Catalog](/concepts/unity-catalog.md) integration.
- **CSV** – comma‑separated values, commonly used for ingestion.
- **JSON** – line‑delimited JSON or standard JSON.
- **Avro** – a binary row‑oriented format.
- **Parquet** – a columnar storage format optimized for analytical queries.
- **ORC** – Optimized Row Columnar format, similar to Parquet.
- **Text** – plain text files (e.g., `.txt`).

External tables reference data stored outside Unity Catalog’s [Managed storage location](/concepts/managed-storage-location.md), so the user is responsible for the lifecycle of the underlying files. The supported formats reflect the most commonly used data interchange and storage formats in the Apache Spark ecosystem.

## Considerations

- [Unity Catalog](/concepts/unity-catalog.md) does not support file formats other than those listed above; for example, table formats like Hudi are not supported.
- When creating tables, the format must be specified either explicitly (e.g., `USING DELTA`) or implicitly via file discovery; unsupported formats will result in errors.
- The format support applies to both batch and streaming reads and writes, subject to the usual compute access mode requirements.

## Related Concepts

- [Managed tables](/concepts/managed-tables-in-databricks.md)
- [External tables](/concepts/unity-catalog-external-table-conversion.md)
- [Delta Lake](/concepts/delta-lake.md)
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md)
- Unity Catalog requirements and limitations

## Sources

- unity-catalog-requirements-and-limitations-databricks-on-aws.md

# Citations

1. [unity-catalog-requirements-and-limitations-databricks-on-aws.md](/references/unity-catalog-requirements-and-limitations-databricks-on-aws-0188dbe0.md)

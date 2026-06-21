---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: afbb7cc354a8a1d42a0ae8913a8c2613e174296d696e015fc5aad0ed01c0958c
  pageDirectory: concepts
  sources:
    - delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-external-metadata-support-for-streaming-tables-and-materialized-views
    - Materialized Views and Delta External Metadata Support for Streaming Tables
    - DEMSFSTAMV
  citations:
    - file: delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md
title: Delta External Metadata Support for Streaming Tables and Materialized Views
description: Only streaming tables and materialized views are supported sources for Delta external metadata operations; other table types trigger an error.
tags:
  - databricks
  - delta-lake
  - streaming
  - materialized-views
timestamp: "2026-06-19T15:04:50.909Z"
---

Here is the wiki page for "Delta External Metadata Support for Streaming Tables and Materialized Views", written solely from the provided source material.

---

## Delta External Metadata Support for Streaming Tables and Materialized Views

**Delta External Metadata** is a feature that allows external systems to read and reconcile metadata about certain Delta table types. Support for Delta External Metadata is currently limited to **_streaming tables_** and **_materialized views_** only. Attempting to use it with other table types will produce an error. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

### Supported Table Types

When Delta External Metadata reconciliation queries are run, only the following table types are accepted:

- **Streaming Table** – Tables that are continuously updated by Delta Live Tables (DLT) pipelines.
- **[Materialized View](/concepts/materialized-views-in-databricks.md)** – Tables that are incrementally refreshed by DLT pipelines.

All other table types are unsupported and will result in a `DELTA_EXTERNAL_METADATA_UNSUPPORTED_SOURCE` error with the SQLSTATE class `0A` (Feature Not Supported). The error message specifically states:

> `<tableType>` table, only streaming table and materialized view are supported.

^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

### Unsupported Features and Error Conditions

The following features are not supported under Delta External Metadata and will trigger specific error conditions when encountered:

- **COLUMN_MASK** – External metadata does not support tables that have [Column Mask (CM) policies](/concepts/column-mask-policies.md) applied. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]
- **ROW_FILTER** – External metadata does not support tables that have [Row-Level Security (RLS) Policies](/concepts/row-level-security-rls-policies.md) applied. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]
- **COLUMN_RENAME_WITHOUT_COLUMN_MAPPING** – If a column rename is attempted without first enabling [Column Mapping](/concepts/delta-table-column-mapping.md), the reconciliation query cannot use the alias and will fail. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]
- **PROJECTION_NOT_SUPPORTED** – The projection SQL clause used in the reconciliation query is not in a supported format. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

### Error Message Format

When an unsupported source or table type is encountered, Databricks returns an error with the class `DELTA_EXTERNAL_METADATA_UNSUPPORTED_SOURCE`. The message includes the specific unsupported element, such as the table type, the projection SQL, or the security policy that caused the failure. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

### Related Concepts

- [Delta Lake](/concepts/delta-lake.md) – The open-source storage layer that powers Delta tables.
- Delta Live Tables – The framework for building streaming tables and materialized views.
- [Column Mapping](/concepts/delta-table-column-mapping.md) – Required when using column aliases in reconciliation queries.
- [Column Mask CM](/concepts/column-mask-policies.md) – A security feature not supported with external metadata.
- [Row Level Security RLS](/concepts/row-level-security-rls-policies.md) – A security feature not supported with external metadata.

### Sources

- delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md](/references/delta_external_metadata_unsupported_source-error-condition-databricks-on-aws-478fcc27.md)

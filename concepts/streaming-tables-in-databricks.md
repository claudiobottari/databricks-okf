---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3862b237dc7c56bda1c28a55dc8b3ffcafb034d63d95af35bed7fc5e51fa706e
  pageDirectory: concepts
  sources:
    - delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - streaming-tables-in-databricks
    - STID
    - Streaming Tables|Streaming tables
    - Streaming on Databricks
  citations:
    - file: delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md
title: Streaming tables in Databricks
description: Incrementally updated Delta tables that ingest streaming data, one of the two table types supported for external metadata.
tags:
  - databricks
  - streaming
  - delta-lake
timestamp: "2026-06-19T18:24:51.244Z"
---

# Streaming Tables in Databricks

**Streaming tables** are a type of Delta table in Databricks that continuously ingest and process data as it arrives. They are commonly built using Delta Live Tables (DLT) and support incremental processing, making them suitable for real-time or near-real-time data pipelines.

## Supported Table Type for External Metadata

In the context of the `DELTA_EXTERNAL_METADATA_UNSUPPORTED_SOURCE` error condition, the Databricks error message explicitly states that for the sub‑error `TABLE_TYPE`, only **streaming tables** and **materialized views** are supported as table types. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

This means that when configuring external metadata (for example, when using Unity Catalog with a third-party catalog), only streaming tables and materialized views are valid target table types; other table types will raise the unsupported‑source error.

## Related Concepts

- Delta Live Tables – The primary framework for defining and maintaining streaming tables.
- [Materialized Views](/concepts/materialized-views-in-databricks.md) – Another supported table type for external metadata.
- [Unity Catalog](/concepts/unity-catalog.md) – The catalog system that can integrate with external metadata sources.
- [Delta Lake](/concepts/delta-lake.md) – The underlying storage format used by streaming tables.
- Incremental Processing – The core processing paradigm that streaming tables enable.

## Sources

- delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md](/references/delta_external_metadata_unsupported_source-error-condition-databricks-on-aws-478fcc27.md)

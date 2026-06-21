---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dabf7179e108778ac7be28fca143ee859f6687c05682cb49ca08a76155a3b199
  pageDirectory: concepts
  sources:
    - read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md
  confidence: 0.99
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - prerequisites-and-limitations-for-uniform-iceberg-reads
    - Limitations for UniForm Iceberg Reads and Prerequisites
    - PALFUIR
  citations:
    - file: read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md
title: Prerequisites and Limitations for UniForm Iceberg Reads
description: Enabling Iceberg reads requires Unity Catalog registration, column mapping, specific Delta protocol versions (minReaderVersion >= 2, minWriterVersion >= 7), and Databricks Runtime 14.3+ — with limitations including no deletion vectors, read-only Iceberg client access, and no support for materialized views or streaming tables.
tags:
  - delta-lake
  - iceberg
  - requirements
  - limitations
timestamp: "2026-06-19T20:11:48.198Z"
---

# Prerequisites and Limitations for UniForm Iceberg Reads

**UniForm Iceberg Reads** (formerly known as Delta Lake Universal Format) enables Iceberg clients to read Delta Lake tables by automatically generating Iceberg metadata asynchronously. This page describes the prerequisites required to enable this feature and the limitations that apply.

## Prerequisites

The following prerequisites must be met to enable Iceberg reads on a [Delta Lake Table](/concepts/delta-lake-table.md): The table must be registered to Unity Catalog (both managed and external tables are supported).^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md] The table must have [column mapping](/concepts/column-mapping-in-delta-lake.md) enabled.^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md] The [Delta Lake Table](/concepts/delta-lake-table.md) must have a `minReaderVersion` >= 2 and `minWriterVersion` >= 7.^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md] Writes to the table must use Databricks Runtime 14.3 LTS or above.^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md] You cannot enable [Deletion Vectors](/concepts/deletion-vectors.md) on a table with Iceberg reads enabled; you can use `REORG` to disable and purge deletion vectors on an existing table while upgrading to Iceberg read support.^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md] Tables with Iceberg reads enabled use Zstandard (ZSTD) instead of Snappy as the compression codec for underlying Parquet data files.^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md] Iceberg metadata generation runs asynchronously on the compute used to write data to the [Delta Lake Table](/concepts/delta-lake-table.md), which might increase driver resource usage.^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md]

## Limitations

The following limitations apply to all tables with Iceberg reads enabled:

Iceberg v2 reads do not work on tables with deletion vectors enabled. (Apache Iceberg v3 supports deletion vectors; see Use Apache Iceberg v3 features and [Deletion vectors in Databricks](/concepts/deletion-vectors-in-delta-lake.md).)^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md] The [Delta Lake Table](/concepts/delta-lake-table.md) must be accessed by name (not by path) to automatically trigger Iceberg metadata generation.^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md] Iceberg reads cannot be enabled on materialized views or streaming tables.^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md] Delta Lake tables with Iceberg reads enabled do not support `VOID` types.^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md] Iceberg client support is read‑only; writes are not supported.^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md] Iceberg reader clients may have individual limitations regardless of Databricks support for Iceberg reads; refer to the documentation for your chosen client.^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md] Recipients of OpenSharing can read Delta Lake tables with Iceberg reads enabled as Iceberg tables using the Iceberg REST Catalog API (Public Preview), but some [Delta Lake Table](/concepts/delta-lake-table.md) features used by Iceberg reads are not supported by some OpenSharing reader clients.^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md] [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) works for Delta clients when Iceberg reads are enabled but does not have support in Iceberg.^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md]

## Related Concepts

- Delta Lake feature compatibility and protocols
- Rename and drop columns with Delta Lake column mapping
- [Deletion vectors in Databricks](/concepts/deletion-vectors-in-delta-lake.md)
- Use Apache Iceberg v3 features
- [What is OpenSharing?](/concepts/opensharing.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Iceberg REST Catalog API](/concepts/iceberg-rest-catalog-irc-protocol.md)

## Sources

- read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md

# Citations

1. [read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md](/references/read-delta-lake-tables-with-iceberg-clients-databricks-on-aws-ae1b1933.md)

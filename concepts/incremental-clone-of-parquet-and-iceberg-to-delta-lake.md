---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0563df931a162aa9a3adc9c61960a2abdc728ea773b66ce48c8615690a92578d
  pageDirectory: concepts
  sources:
    - convert-to-delta-lake-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - incremental-clone-of-parquet-and-iceberg-to-delta-lake
    - Iceberg to Delta Lake and Incremental Clone of Parquet
    - ICOPAITDL
    - Incremental clone (Parquet/Iceberg to Delta)
    - Incremental clone of Parquet and Iceberg tables
    - Incrementally Clone Parquet and Apache Iceberg Tables to Delta Lake
    - Incrementally Clone Parquet and Iceberg Tables to Delta Lake
    - Incrementally clone Parquet and Apache Iceberg tables to Delta Lake
  citations:
    - file: convert-to-delta-lake-databricks-on-aws.md
title: Incremental Clone of Parquet and Iceberg to Delta Lake
description: Alternative approach to incrementally clone Parquet or Iceberg tables to Delta Lake instead of one-time conversion.
tags:
  - delta-lake
  - migration
  - cloning
timestamp: "2026-06-19T17:52:48.595Z"
---

# Incremental Clone of Parquet and Iceberg to Delta Lake

**Incremental Clone of Parquet and Iceberg to Delta Lake** is a method for continuously synchronizing Parquet or Apache Iceberg tables into Delta Lake, as opposed to a one-time conversion. The [CONVERT TO DELTA](/concepts/convert-to-delta.md) SQL command performs a single batch conversion; for ongoing, incremental replication, Databricks directs users to a separate guide on incremental cloning. ^[convert-to-delta-lake-databricks-on-aws.md]

## Relationship to CONVERT TO DELTA

The `CONVERT TO DELTA` command is designed for one-time conversion of Parquet and Iceberg tables. It does not handle subsequent changes to the source data. For use cases where the source table continues to receive new records or updates, an incremental clone approach is recommended. The Databricks documentation includes a dedicated page titled *Incrementally clone Parquet and Apache Iceberg tables to Delta Lake* that describes this process. ^[convert-to-delta-lake-databricks-on-aws.md]

## Where to Learn More

The referenced guide for incremental cloning is available at:

- [Incrementally clone Parquet and Apache Iceberg tables to Delta Lake](https://docs.databricks.com/aws/en/ingestion/data-migration/clone-parquet) (external link, not part of this source)

## Related Concepts

- [CONVERT TO DELTA](/concepts/convert-to-delta.md) – One-time conversion of Parquet or Iceberg to Delta Lake.
- [Delta Lake](/concepts/delta-lake.md) – The target format for the conversion or clone.
- Parquet – A common columnar storage format that can be converted or cloned.
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) – Another open table format that can be converted or cloned.
- [External Tables in Unity Catalog](/concepts/external-tables-in-unity-catalog.md) – Where converted/cloned tables can be registered.

## Sources

- convert-to-delta-lake-databricks-on-aws.md

# Citations

1. [convert-to-delta-lake-databricks-on-aws.md](/references/convert-to-delta-lake-databricks-on-aws-85c3b3fb.md)

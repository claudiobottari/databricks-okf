---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8259bbd707a7626ec4b3b9dd7dc6f7e6f88055dfd9395bd21f7cc1e24bac226e
  pageDirectory: concepts
  sources:
    - convert-to-delta-lake-databricks-on-aws.md
  confidence: 0.8
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - incremental-cloning-to-delta-lake
    - ICTDL
    - Incremental Clone to Delta Lake
    - Incrementally clone to Delta Lake
    - Incremental Clone
    - Incremental Cloning
    - Incremental clone
    - incremental clone
  citations:
    - file: convert-to-delta-lake-databricks-on-aws.md
title: Incremental Cloning to Delta Lake
description: An alternative to one-time CONVERT TO DELTA for incrementally cloning Parquet and Apache Iceberg tables to Delta Lake.
tags:
  - delta-lake
  - incremental
  - cloning
  - data-migration
timestamp: "2026-06-18T11:10:54.269Z"
---

# Incremental Cloning to Delta Lake

**Incremental cloning to Delta Lake** is a method for continuously converting Parquet or Apache Iceberg tables to [Delta Lake](/concepts/delta-lake.md) format by cloning the source data incrementally, rather than performing a one-time conversion. This approach is useful when you need to maintain a Delta Lake copy of a source table that is being updated over time.^[convert-to-delta-lake-databricks-on-aws.md]

## Overview

The `CONVERT TO DELTA` SQL command performs a one-time conversion for Parquet and Apache Iceberg tables to Delta Lake tables. For incremental conversion of Parquet or Iceberg tables to Delta Lake, Databricks recommends using the incremental clone approach instead.^[convert-to-delta-lake-databricks-on-aws.md]

Incremental cloning allows you to:

- Continuously synchronize changes from a source Parquet or Iceberg table to a [Delta Lake Table](/concepts/delta-lake-table.md)
- Avoid reprocessing the entire dataset on each run
- Maintain a Delta Lake copy that stays up-to-date with the source

## When to Use Incremental Cloning

Use incremental cloning when:

- Your source Parquet or Iceberg table receives ongoing updates and you need to maintain a Delta Lake copy
- A one-time `CONVERT TO DELTA` conversion is insufficient because the source data continues to change
- You need to minimize reprocessing overhead for large datasets

## Related Concepts

- [CONVERT TO DELTA](/concepts/convert-to-delta.md) — The one-time conversion command for Parquet and Iceberg tables
- [Delta Lake](/concepts/delta-lake.md) — The storage format that provides ACID transactions and other lakehouse features
- Parquet tables — A common source format for conversion to Delta Lake
- Apache Iceberg tables — Another table format that can be converted to Delta Lake
- [External Tables in Unity Catalog](/concepts/external-tables-in-unity-catalog.md) — Tables stored in external locations managed by Unity Catalog

## Sources

- convert-to-delta-lake-databricks-on-aws.md

# Citations

1. [convert-to-delta-lake-databricks-on-aws.md](/references/convert-to-delta-lake-databricks-on-aws-85c3b3fb.md)

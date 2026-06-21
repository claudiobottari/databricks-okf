---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b8b5c104dcaa58a17df11c2d3b5eb156d50f882f2e14f96b588f78da4045c90b
  pageDirectory: concepts
  sources:
    - convert-to-delta-lake-databricks-on-aws.md
  confidence: 0.7
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - incremental-cloning-of-parquet-and-iceberg-to-delta-lake
    - Iceberg to Delta Lake and Incremental Cloning of Parquet
    - ICOPAITDL
    - Incremental Cloning of Parquet and Iceberg Tables
    - Incremental cloning from Iceberg to Delta Lake
    - Incremental cloning of Parquet and Iceberg tables
  citations:
    - file: convert-to-delta-lake-databricks-on-aws.md
title: Incremental Cloning of Parquet and Iceberg to Delta Lake
description: An alternative approach to CONVERT TO DELTA for incremental, ongoing conversion of Parquet or Iceberg tables to Delta Lake tables.
tags:
  - incremental-loading
  - delta-lake
  - data-migration
  - cloning
timestamp: "2026-06-18T14:45:09.746Z"
---

# Incremental Cloning of Parquet and Iceberg to Delta Lake

**Incremental Cloning of Parquet and Iceberg to Delta Lake** refers to the process of continuously migrating data from existing Parquet or [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) tables into [Delta Lake](/concepts/delta-lake.md) while preserving the history of changes. This contrasts with the one‑time bulk conversion offered by the `CONVERT TO DELTA` SQL command. ^[convert-to-delta-lake-databricks-on-aws.md]

## Overview

The `CONVERT TO DELTA` SQL command performs a **one‑time conversion** for Parquet and Iceberg tables to Delta Lake tables. For scenarios that require ongoing or incremental migration, Databricks provides a separate mechanism: **incrementally clone** Parquet and Iceberg tables to Delta Lake. ^[convert-to-delta-lake-databricks-on-aws.md]

The official Databricks documentation directs users who need incremental conversion to the dedicated guide *Incrementally clone Parquet and Apache Iceberg tables to Delta Lake*.^[convert-to-delta-lake-databricks-on-aws.md]

## Distinction from One‑Time Conversion

| Method | Behavior |
|--------|----------|
| `CONVERT TO DELTA` | One‑time, batch conversion of existing Parquet or Iceberg data to Delta Lake. |
| Incremental cloning | Ongoing synchronization that captures new data and changes while preserving the source table’s format history. See the CLONE command and the incremental cloning documentation. |

Because the source material does not describe the technical details of incremental cloning, this page serves only as a pointer to the separate documentation set.

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md)
- Parquet
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md)
- [CONVERT TO DELTA](/concepts/convert-to-delta.md)
- CLONE command
- [Incremental Cloning](/concepts/incremental-cloning-to-delta-lake.md)

## Sources

- convert-to-delta-lake-databricks-on-aws.md

# Citations

1. [convert-to-delta-lake-databricks-on-aws.md](/references/convert-to-delta-lake-databricks-on-aws-85c3b3fb.md)

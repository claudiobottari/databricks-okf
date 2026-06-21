---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ce5533d013a1dcb00173557e30b5d76d8fb939cca47e6ac64c2cd1e4777e20a0
  pageDirectory: concepts
  sources:
    - delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md
  confidence: 0.7
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - delta-uniform-delta-universal-format
    - DU(UF
  citations:
    - file: delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md
title: Delta UniForm (Delta Universal Format)
description: A Databricks feature that enables Delta Lake tables to be read by Iceberg, Hudi, and other formats through automatic metadata conversion and refresh operations.
tags:
  - databricks
  - delta-lake
  - lakehouse
  - interoperability
timestamp: "2026-06-19T18:28:00.063Z"
---

# Delta UniForm (Delta Universal Format)

**Delta UniForm (Delta Universal Format)** is a feature of [Delta Lake](/concepts/delta-lake.md) that enables reading Delta tables with non-Delta Lake clients by automatically generating and maintaining metadata in formats those clients can understand. It bridges the gap between Delta Lake's transactional storage layer and broader open-source ecosystem tools.

## Overview

Delta UniForm allows Delta tables to be read by Apache Iceberg and Apache Hudi clients without requiring those clients to natively understand the Delta Lake protocol. When UniForm is enabled on a Delta table, Delta Lake automatically generates Iceberg and Hudi metadata alongside the Delta metadata, so tools integrated with those formats can discover and read the table data. ^[delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md]

## Supported Formats

Delta UniForm currently supports automatic metadata generation for:

- **Apache Iceberg** – Enables Iceberg-compatible readers (e.g., Trino, Presto, Spark with Iceberg catalog) to read Delta tables.
- **Apache Hudi** – Enables Hudi-compatible readers to access Delta tables.

Both formats can be enabled independently on the same Delta table. ^[delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md]

## How It Works

When UniForm is enabled on a Delta table, write operations to the table trigger automatic generation or refresh of the corresponding Iceberg or Hudi metadata. This ensures that external readers always see the latest committed data without manual synchronization steps. ^[delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) – The underlying storage layer providing ACID transactions and schema enforcement.
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) – An open table format supported by UniForm.
- Apache Hudi – An open table format supported by UniForm.
- [Delta Sharing](/concepts/delta-sharing.md) – Another Databricks technology for cross-platform data access.
- Delta Live Tables – A framework for building reliable data pipelines on Delta Lake.

## Sources

- delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md](/references/delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws-592e817e.md)

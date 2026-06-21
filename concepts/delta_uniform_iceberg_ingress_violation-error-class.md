---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7e51aa680f615396a87d2e9406341a05cce9f1693588eb3fba632e0d2e408c1e
  pageDirectory: concepts
  sources:
    - delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta_uniform_iceberg_ingress_violation-error-class
    - DEC
  citations:
    - file: delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md
title: DELTA_UNIFORM_ICEBERG_INGRESS_VIOLATION error class
description: A Databricks error class (SQLSTATE KD00E) that occurs when reading an Apache Iceberg table via Delta Uniform fails, typically due to metadata parsing failures or misconfigured table properties.
tags:
  - error-messages
  - delta-uniform
  - databricks
timestamp: "2026-06-19T18:27:46.821Z"
---

# DELTA_UNIFORM_ICEBERG_INGRESS_VIOLATION error class

The **DELTA_UNIFORM_ICEBERG_INGRESS_VIOLATION error class** occurs when reading an Apache Iceberg table enabled with [Delta Uniform](/concepts/delta-uniform.md) fails due to internal consistency checks not being satisfied. This error belongs to the [SQLSTATE error classes|SQLSTATE class `KD00E`](/concepts/delta-error-sqlstate-codes.md) (Datasource-specific errors). ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

## Error Message

The primary error message states:

> Read Apache Iceberg with Delta Uniform has failed.
> Failed to parse version from existing metadata location `<existingLocation>` or current metadata location `<currentLocation>`;

This indicates that the version information embedded in the Iceberg metadata locations could not be extracted. The recommended action is to verify the file naming convention used by the Apache Iceberg writer. ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

## Sub‑error Conditions

The error class includes two distinct sub‑error conditions, each with its own cause and guidance.

### MISSING_UNIFORM_TBL_PROPERTIES

This subtype is triggered when at least one of the following required [Delta Uniform table properties](/concepts/delta-uniform.md) is missing from the Delta table: `tableId`, `snapshotId`, or `metadataLocation`. The error message includes the missing identifiers. The most likely cause is a manual modification to the `_delta_log` directory that removed or corrupted these properties. ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

### MUST_REFRESH_SAME_TABLE

This subtype occurs when attempting to refresh an existing Apache Iceberg table UUID (`<existingId>`) with metadata that belongs to a different Iceberg table UUID (`<currentId>`). Refreshing across different table UUIDs is not supported.

Additionally, the metadata location used for the refresh must have a higher version number than the existing metadata location. The error message lists both the existing and current metadata locations for debugging. ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Uniform](/concepts/delta-uniform.md) – The feature that provides a unified metadata layer for Delta Lake and Apache Iceberg.
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) – The open table format being read through Delta Uniform.
- SQLSTATE error classes – The classification system for Databricks error messages.
- Delta table properties – The metadata properties that drive Delta Uniform behavior.
- [Delta Lake](/concepts/delta-lake.md) – The storage layer underlying Delta Uniform.

## Sources

- delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md](/references/delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws-37d8ed72.md)

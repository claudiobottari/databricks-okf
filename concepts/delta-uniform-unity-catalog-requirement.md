---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 64495fa69ba762e34cce352dc8dc73efa396b6ad3b0f49241de41efd1debd3f5
  pageDirectory: concepts
  sources:
    - delta_uniform_ingress_violation-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-uniform-unity-catalog-requirement
    - DUUCR
  citations:
    - file: delta_uniform_ingress_violation-error-condition-databricks-on-aws.md
title: Delta Uniform Unity Catalog Requirement
description: Unity Catalog must be enabled to read Apache Iceberg tables using Delta Uniform; absence triggers the UNITY_CATALOG_NOT_ENABLED error.
tags:
  - databricks
  - unity-catalog
  - delta-uniform
timestamp: "2026-06-19T18:27:53.804Z"
---

# Delta Uniform Unity Catalog Requirement

The **Delta Uniform Unity Catalog Requirement** is a mandatory prerequisite for using Delta Uniform to read Apache Iceberg tables. When this requirement is not met, the system raises the `UNITY_CATALOG_NOT_ENABLED` error condition, preventing read operations on Iceberg tables through Delta Uniform. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Error Condition

When Unity Catalog is not enabled for a workspace, attempting to read Apache Iceberg tables with Delta Uniform fails with the following error:

```
UNITY_CATALOG_NOT_ENABLED: Unity Catalog is required for Read Apache Iceberg with Delta Uniform.
```

^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

This error belongs to the `DELTA_UNIFORM_INGRESS_VIOLATION` error class, which has SQLSTATE `KD00E` (a datasource-specific error code). ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Cause

The error occurs because Delta Uniform's Iceberg ingress functionality depends on [Unity Catalog](/concepts/unity-catalog.md) for metadata management and access control. Without Unity Catalog enabled, the system cannot perform the necessary metadata conversion from Iceberg format to Delta format. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Resolution

To resolve this error, enable [Unity Catalog](/concepts/unity-catalog.md) on the Databricks workspace. Once Unity Catalog is active, Delta Uniform can perform the metadata conversion required to read Apache Iceberg tables. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Related Error Conditions

The `DELTA_UNIFORM_INGRESS_VIOLATION` error class includes several other conditions that may occur when working with Delta Uniform:

- **`DELTA_LOG_LOCATION_NOT_FOUND`** — The delta log location is missing for the specified table.
- **`NOT_UNIFORM_INGRESS_TABLE`** — The table is not configured as a uniform ingress table.
- **`OPERATION_NOT_SUPPORTED`** — Only `CREATE` and `REFRESH` operations are supported on Uniform Apache Iceberg Ingress Tables.
- **`UNEXPECTED_DELTA_LOG_LOCATION`** — An unexpected delta log location was found for the table.

^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Uniform](/concepts/delta-uniform.md) — The feature enabling interoperability between Delta Lake and Apache Iceberg
- [Unity Catalog](/concepts/unity-catalog.md) — Databricks' unified governance solution for data and AI assets
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) — An open table format for large analytic datasets
- [Delta Lake](/concepts/delta-lake.md) — The foundational storage layer for Databricks
- Metadata Conversion — The process of translating between different table formats

## Sources

- delta_uniform_ingress_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_ingress_violation-error-condition-databricks-on-aws.md](/references/delta_uniform_ingress_violation-error-condition-databricks-on-aws-1bfee206.md)

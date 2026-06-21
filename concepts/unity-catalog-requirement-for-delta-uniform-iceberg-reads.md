---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 598dea93b0c12811af2979b4b227aebe9c36c7f34138e830c52ebaab891e9bfd
  pageDirectory: concepts
  sources:
    - delta_uniform_ingress_violation-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-requirement-for-delta-uniform-iceberg-reads
    - UCRFDUIR
  citations:
    - file: delta_uniform_ingress_violation-error-condition-databricks-on-aws.md
title: Unity Catalog requirement for Delta Uniform Iceberg reads
description: Unity Catalog must be enabled for reading Apache Iceberg tables through Delta Uniform; the UNITY_CATALOG_NOT_ENABLED error is raised when this prerequisite is not met.
tags:
  - unity-catalog
  - delta-lake
  - iceberg
  - prerequisites
timestamp: "2026-06-18T15:24:02.676Z"
---

## Unity Catalog Requirement for Delta Uniform Iceberg Reads

The **Unity Catalog requirement for Delta Uniform Iceberg reads** refers to the condition that the [Unity Catalog](/concepts/unity-catalog.md) must be enabled on the workspace before a read operation against an [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) table using [Delta Uniform](/concepts/delta-uniform.md) can succeed. This requirement is enforced by the `DELTA_UNIFORM_INGRESS_VIOLATION` error class. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

### Error Class

When a read against a Delta Uniform table fails because Unity Catalog is not enabled, the engine raises an error with:

- **Error class**: `DELTA_UNIFORM_INGRESS_VIOLATION`
- **SQL state**: `KD00E` (Datasource-specific error)
- **General message pattern**: `Read Delta Uniform fails: Metadata conversion from <format> to Delta failed, <errorMessage>.`
- **Specific sub-error**: `UNITY_CATALOG_NOT_ENABLED`

The sub-error message is:

> Unity Catalog is required for Read Apache Iceberg with Delta Uniform.

^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

This means that any workspace or [Metastore](/concepts/metastore.md) that does not have Unity Catalog activated cannot query Iceberg tables through the Delta Uniform compatibility layer.

### Related Sub-Errors

The `DELTA_UNIFORM_INGRESS_VIOLATION` class includes several other conditions that can also cause the read to fail: ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

| Sub-error | Meaning |
|-----------|---------|
| `DELTA_LOG_LOCATION_NOT_FOUND` | The `_delta_log` location is missing for the table. |
| `NOT_UNIFORM_INGRESS_TABLE` | The table is not a Uniform Ingress table. |
| `OPERATION_NOT_SUPPORTED` | Only `CREATE` and `REFRESH` are supported on Uniform Ingress tables. |
| `UNEXPECTED_DELTA_LOG_LOCATION` | The delta log location does not match expectations. |

These conditions are independent of the Unity Catalog requirement; even if Unity Catalog is enabled, one of these other errors may occur if the table metadata is misconfigured.

### Resolution

To resolve the `UNITY_CATALOG_NOT_ENABLED` error, ensure that the workspace and [Metastore](/concepts/metastore.md) are configured to use [Unity Catalog](/concepts/unity-catalog.md) and that the catalog containing the Iceberg table is managed by Unity Catalog. See the documentation on [Enable Unity Catalog](/concepts/unity-catalog.md) for setup steps.

### Related Concepts

- [Delta Uniform](/concepts/delta-uniform.md) – The feature that enables Delta Lake to read Iceberg tables.
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) – The open table format read by Delta Uniform.
- [Unity Catalog](/concepts/unity-catalog.md) – The required [Metastore](/concepts/metastore.md) for this read path.
- DELTA_UNIFORM_INGRESS_VIOLATION Error Class|DELTA_UNIFORM_INGRESS_VIOLATION error class – Full error class reference.

### Sources

- delta_uniform_ingress_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_ingress_violation-error-condition-databricks-on-aws.md](/references/delta_uniform_ingress_violation-error-condition-databricks-on-aws-1bfee206.md)

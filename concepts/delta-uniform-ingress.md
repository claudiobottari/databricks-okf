---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 184e655bb9e89719225893169273509a92e4aa9378cdfe1ddc2193a04cdce1f3
  pageDirectory: concepts
  sources:
    - delta_uniform_ingress_violation-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-uniform-ingress
    - DUI
    - delta-uniform-ingress-table
    - DUIT
  citations:
    - file: delta_uniform_ingress_violation-error-condition-databricks-on-aws.md
title: Delta Uniform Ingress
description: The pattern of reading or importing Apache Iceberg tables through Delta Uniform on Databricks, supporting only CREATE and REFRESH operations.
tags:
  - delta-uniform
  - ingress
  - apache-iceberg
  - databricks
timestamp: "2026-06-19T10:09:07.125Z"
---

# Delta Uniform Ingress

**Delta Uniform Ingress** refers to a Databricks integration pattern that allows reading Apache Iceberg tables through the Delta Lake protocol using [Unity Catalog](/concepts/unity-catalog.md). When a table is registered as a Uniform Ingress table, metadata conversion from Iceberg to Delta is performed automatically, enabling Delta-compatible tools and clients to read Iceberg data without direct Iceberg support. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Overview

Delta Uniform Ingress provides interoperability between the Apache Iceberg and Delta Lake formats. By maintaining a Delta log alongside the Iceberg metadata, Databricks allows Delta readers to access data stored in Iceberg format. This capability is enabled and managed through Unity Catalog, which is a prerequisite for using this feature. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Supported Operations

Only two operations are supported on Uniform Apache Iceberg Ingress tables: ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

- **`CREATE`** — Registering a new Uniform Ingress table
- **`REFRESH`** — Updating the Delta metadata to reflect changes in the Iceberg table

Any other operation on a Uniform Ingress table will result in an error. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Error Conditions

When operations on Uniform Ingress tables fail, the system raises a `DELTA_UNIFORM_INGRESS_VIOLATION` error. The following sub-conditions describe specific failure modes: ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

### DELTA_LOG_LOCATION_NOT_FOUND

The Delta log directory is missing for the specified table. Delta Uniform Ingress requires a valid Delta log location to perform metadata conversion. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

### NOT_UNIFORM_INGRESS_TABLE

The target table is not registered as a Uniform Ingress table. This error occurs when attempting to perform Uniform Ingress operations on a standard Delta or Iceberg table. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

### OPERATION_NOT_SUPPORTED

An unsupported operation was attempted on a Uniform Ingress table. Only `CREATE` and `REFRESH` are permitted. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

### UNEXPECTED_DELTA_LOG_LOCATION

The Delta log location contains an unexpected path for the specified table. This indicates a mismatch between the expected and actual metadata location. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

### UNITY_CATALOG_NOT_ENABLED

Unity Catalog is not enabled in the workspace. Delta Uniform Ingress requires Unity Catalog to be active. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Requirements

- [Unity Catalog](/concepts/unity-catalog.md) must be enabled in the Databricks workspace
- The table must be properly registered as a Uniform Ingress table
- Valid Delta log metadata must exist at the expected location

## Related Concepts

- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) — The underlying table format for Uniform Ingress
- [Delta Lake](/concepts/delta-lake.md) — The read protocol used by Delta Uniform Ingress
- [Delta Uniform](/concepts/delta-uniform.md) — The broader interoperability feature between Delta and Iceberg
- Metadata Conversion — The process of translating between Iceberg and Delta formats

## Sources

- delta_uniform_ingress_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_ingress_violation-error-condition-databricks-on-aws.md](/references/delta_uniform_ingress_violation-error-condition-databricks-on-aws-1bfee206.md)

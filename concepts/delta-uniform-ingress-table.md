---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2ffbcc90c2c9c00d542f0b0b181027dbb367161e052638dd95b821da2946c71a
  pageDirectory: concepts
  sources:
    - delta_uniform_ingress_violation-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-uniform-ingress-table
    - DUIT
  citations:
    - file: delta_uniform_ingress_violation-error-condition-databricks-on-aws.md
title: Delta Uniform Ingress Table
description: A Databricks table concept that supports reading Apache Iceberg metadata via Delta Uniform, requiring Unity Catalog and supporting only CREATE and REFRESH operations.
tags:
  - databricks
  - delta-uniform
  - apache-iceberg
timestamp: "2026-06-19T18:28:00.617Z"
---

# Delta Uniform Ingress Table

A **Delta Uniform Ingress Table** is a [Delta Uniform](/concepts/delta-uniform.md) table that is designated to read [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) data by converting the source metadata into the Delta format. This enables queries and operations on Iceberg tables through Delta Lake interfaces while relying on [Unity Catalog](/concepts/unity-catalog.md) for governance. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Overview

The Delta Uniform Ingress Table acts as a bridge that allows Databricks to read Apache Iceberg tables using Delta Lake protocols. The system performs a metadata conversion from the source format (e.g., Iceberg) to Delta. If this conversion fails, the `DELTA_UNIFORM_INGRESS_VIOLATION` error is raised, with a specific subtype describing the root cause. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Required Conditions

- **Unity Catalog must be enabled** – The table cannot be created or used without Unity Catalog. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]
- **Table must be designated as a uniform ingress table** – Not every Delta table qualifies; it must explicitly be a Uniform Apache Iceberg Ingress Table. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]
- **Delta log location must exist and be correct** – The metadata path must be properly defined and match the expected location. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Supported Operations

Only two operations are allowed on a Delta Uniform Ingress Table: `CREATE` and `REFRESH`. Any other operation (e.g., `DROP`, `ALTER`, `INSERT`) will trigger the `OPERATION_NOT_SUPPORTED` error. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Error Subtypes

The `DELTA_UNIFORM_INGRESS_VIOLATION` error condition has the following subtypes:

| Subtype | Meaning |
|---|---|
| `DELTA_LOG_LOCATION_NOT_FOUND` | The Delta log directory is missing for the specified table. |
| `NOT_UNIFORM_INGRESS_TABLE` | The table is not a uniform ingress table. |
| `OPERATION_NOT_SUPPORTED` | The attempted operation is not supported; only `CREATE` and `REFRESH` are valid. |
| `UNEXPECTED_DELTA_LOG_LOCATION` | The Delta log path does not match the expected location for the table. |
| `UNITY_CATALOG_NOT_ENABLED` | Unity Catalog is required but is not enabled. |

All subtypes share the SQLSTATE code **KD00E** (Datasource-specific error). ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Uniform](/concepts/delta-uniform.md) – The framework that provides interoperability between Delta Lake and Apache Iceberg.
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) – The open table format that can be read through the Delta Uniform Ingress Table.
- [Unity Catalog](/concepts/unity-catalog.md) – The required [Metastore](/concepts/metastore.md) for managing uniform ingress tables.
- [Delta Lake](/concepts/delta-lake.md) – The storage layer that the ingress table exposes data in.
- Metadata conversion – The process that transforms Iceberg metadata to Delta format.

## Sources

- delta_uniform_ingress_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_ingress_violation-error-condition-databricks-on-aws.md](/references/delta_uniform_ingress_violation-error-condition-databricks-on-aws-1bfee206.md)

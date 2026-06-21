---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fe9918bd29acadc62ee7602d6d14b535e6e06779267ceb6965a5f43f60f734fc
  pageDirectory: concepts
  sources:
    - delta_uniform_ingress_violation-error-condition-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - delta-uniform-metadata-conversion
    - DUMC
    - Delta Lake to Iceberg Metadata Conversion
  citations:
    - file: delta_uniform_ingress_violation-error-condition-databricks-on-aws.md
title: Delta Uniform Metadata Conversion
description: The process of converting metadata between source formats and Delta Lake during Delta Uniform ingress operations, which is the central failure point for the DELTA_UNIFORM_INGRESS_VIOLATION error.
tags:
  - delta-uniform
  - metadata
  - data-lakehouse
timestamp: "2026-06-19T10:09:34.250Z"
---

# Delta Uniform Metadata Conversion

**Delta Uniform Metadata Conversion** is a specific operation within the [Delta Uniform](/concepts/delta-uniform.md) framework that transforms metadata from an underlying table format (such as [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md)) into the [Delta Lake](/concepts/delta-lake.md) format. This conversion enables systems that read [Delta Lake](/concepts/delta-lake.md) tables to access data originally written in other formats, providing interoperability across different open table formats. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Overview

When a table is created or updated using [Delta Uniform](/concepts/delta-uniform.md) with [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) as the underlying format, the system must perform a metadata conversion step. This process reads the Iceberg metadata and translates it into the Delta Lake metadata format, making the table accessible to Delta Lake readers. The conversion is triggered automatically during supported operations on uniform ingress tables. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Supported Operations

Metadata conversion is only supported on specific [Delta Lake](/concepts/delta-lake.md) operations:

- **CREATE** – When a new uniform ingress table is created, the system converts the initial metadata to Delta format.
- **REFRESH** – When an existing uniform ingress table is refreshed, the system re-converts the metadata to ensure it is up to date with the current state of the underlying table.

Other operations are not supported and will raise an error if attempted. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Failure Conditions

Metadata conversion can fail under several conditions, each corresponding to a specific error in the `DELTA_UNIFORM_INGRESS_VIOLATION` error class:

### DELTA_LOG_LOCATION_NOT_FOUND

The delta log location is missing for the table. This occurs when the Delta log directory or its metadata files cannot be found at the expected path, preventing the system from reading the metadata needed for conversion. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

### NOT_UNIFORM_INGRESS_TABLE

The table is not a [Uniform Ingress Table](/concepts/uniform-ingress-table.md) – that is, it was not initially created as a [Delta Uniform](/concepts/delta-uniform.md) table with [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) as the underlying format. Only tables explicitly designated as uniform ingress tables can undergo metadata conversion. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

### OPERATION_NOT_SUPPORTED

The requested operation is not supported. Only `CREATE` and `REFRESH` operations are permitted on uniform ingress tables. All other operations (such as `UPDATE`, `DELETE`, or `MERGE`) are not supported. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

### UNEXPECTED_DELTA_LOG_LOCATION

An unexpected delta log location is found for the table. This occurs when the system discovers a Delta log at a path that does not match the expected location for the [Uniform Ingress Table](/concepts/uniform-ingress-table.md), suggesting a mismatch between the Iceberg and Delta metadata. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

### UNITY_CATALOG_NOT_ENABLED

[Unity Catalog](/concepts/unity-catalog.md) is required for reading [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) tables with [Delta Uniform](/concepts/delta-uniform.md). Metadata conversion cannot proceed unless [Unity Catalog](/concepts/unity-catalog.md) is enabled on the workspace. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Uniform](/concepts/delta-uniform.md) – The framework for providing Delta Lake compatibility on non-Delta table formats.
- Delta Lake Metadata Conversion – The process of transforming metadata between table formats.
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) – An open table format that can be read via Delta Uniform.
- [Uniform Ingress Table](/concepts/uniform-ingress-table.md) – A table that provides Delta Lake compatibility on an Iceberg format.
- Delta Log – The transaction log for Delta Lake tables.
- [Unity Catalog](/concepts/unity-catalog.md) – The metadata and governance layer for Databricks.
- Read Delta Uniform – The capability of reading Iceberg tables through Delta Uniform.
- [SQLSTATE KD00E](/concepts/sqlstate-kd00e.md) – The SQL state classification for datasource-specific errors, including this error class.

## Sources

- delta_uniform_ingress_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_ingress_violation-error-condition-databricks-on-aws.md](/references/delta_uniform_ingress_violation-error-condition-databricks-on-aws-1bfee206.md)

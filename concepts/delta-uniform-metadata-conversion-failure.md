---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8052c0cb1111499952015f3a3f31d45396752833a67a368c3efbcc5d2d9fc430
  pageDirectory: concepts
  sources:
    - delta_uniform_ingress_violation-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-uniform-metadata-conversion-failure
    - DUMCF
  citations:
    - file: delta_uniform_ingress_violation-error-condition-databricks-on-aws.md
title: Delta Uniform Metadata Conversion Failure
description: A failure scenario where converting source format metadata to Delta format fails during a Delta Uniform read operation, reported under the DELTA_UNIFORM_INGRESS_VIOLATION error class.
tags:
  - databricks
  - delta-uniform
  - metadata
timestamp: "2026-06-19T18:28:01.986Z"
---

# Delta Uniform Metadata Conversion Failure

**Delta Uniform Metadata Conversion Failure** is an error condition (SQLSTATE: KD00E) that occurs when Databricks attempts to read a [Delta Uniform](/concepts/delta-uniform.md) table – specifically, when converting metadata from an existing format (such as Apache Iceberg) to the Delta format – and the conversion fails. The general error message is:

> Read Delta Uniform fails: Metadata conversion from `<format>` to Delta failed, `<errorMessage>`.

^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

This error is classified under the `DELTA_UNIFORM_INGRESS_VIOLATION` error class and covers several specific failure reasons.

## Sub‑Error Conditions

### DELTA_LOG_LOCATION_NOT_FOUND

The `_delta_log` directory is missing for the table.

- Error message: `The delta_log location is missing for table <tableName>.`
- Additional message: `Cannot find metadata path for table <tableName>.`

This indicates that the table's Delta log directory does not exist or cannot be located, which prevents metadata conversion. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

### NOT_UNIFORM_INGRESS_TABLE

The target table is not configured as a [Uniform Ingress](/concepts/uniform-ingress-table.md) table.

- Error message: `Table <tableName> is not a uniform ingress table.`

Only tables explicitly set up for uniform ingress (i.e., tables that expose their metadata in a format readable by Delta) can be used with Delta Uniform. This error occurs when the table is not registered as an ingress table. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

### OPERATION_NOT_SUPPORTED

The attempted operation is not allowed on a [Uniform Iceberg Ingress Table](/concepts/uniform-ingress-table.md).

- Error message: `Operation is not supported. Only CREATE and REFRESH are supported on Uniform Apache Iceberg Ingress Table.`

Delta Uniform ingress tables support only `CREATE` and `REFRESH` operations. Any other operation (e.g., `UPDATE`, `DELETE`) will trigger this error. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

### UNEXPECTED_DELTA_LOG_LOCATION

The Delta log location does not match the expected path for the table.

- Error message: `Unexpected delta_log location <tablePath> for table <tableName>.`

This occurs when the Delta log is found at a location that is inconsistent with the table's metadata, indicating a possible misconfiguration or inconsistency. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

### UNITY_CATALOG_NOT_ENABLED

[Unity Catalog](/concepts/unity-catalog.md) is not enabled, which is a prerequisite for reading Apache Iceberg tables with Delta Uniform.

- Error message: `Unity Catalog is required for Read Apache Iceberg with Delta Uniform.`

Delta Uniform ingress requires Unity Catalog to be configured in the workspace. If Unity Catalog is not enabled, metadata conversion will fail with this error. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Uniform](/concepts/delta-uniform.md) – The feature that provides unified metadata for tables in multiple formats.
- [Uniform Ingress](/concepts/uniform-ingress-table.md) – The mechanism for converting table metadata from an external format (e.g., Iceberg) to Delta.
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) – An open table format that can be read via Delta Uniform.
- [Unity Catalog](/concepts/unity-catalog.md) – The required catalog for Delta Uniform ingress workloads.
- Delta Log – The transaction log that stores Delta table metadata.

## Sources

- delta_uniform_ingress_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_ingress_violation-error-condition-databricks-on-aws.md](/references/delta_uniform_ingress_violation-error-condition-databricks-on-aws-1bfee206.md)

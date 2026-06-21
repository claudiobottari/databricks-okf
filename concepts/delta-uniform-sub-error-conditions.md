---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d87a17fe919f39f55f9cd12bb791891d0bdf88f0ef9f979f25a3b260e8c53727
  pageDirectory: concepts
  sources:
    - delta_uniform_ingress_violation-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-uniform-sub-error-conditions
    - DUSC
  citations:
    - file: delta_uniform_ingress_violation-error-condition-databricks-on-aws.md
title: Delta Uniform Sub-Error Conditions
description: "A set of specific sub-errors under DELTA_UNIFORM_INGRESS_VIOLATION: DELTA_LOG_LOCATION_NOT_FOUND, NOT_UNIFORM_INGRESS_TABLE, OPERATION_NOT_SUPPORTED, UNEXPECTED_DELTA_LOG_LOCATION, and UNITY_CATALOG_NOT_ENABLED."
tags:
  - databricks
  - error-handling
  - delta-uniform
timestamp: "2026-06-19T18:27:56.943Z"
---

# Delta Uniform Sub-Error Conditions

**Delta Uniform Sub-Error Conditions** are specific error types under the `DELTA_UNIFORM_INGRESS_VIOLATION` error class that occur when reading [Delta Uniform](/concepts/delta-uniform.md) tables or performing operations on [Uniform Apache Iceberg Ingress Tables](/concepts/uniform-apache-iceberg-ingress-table.md). These errors indicate various failures during metadata conversion, table discovery, or operation validation.

## Overview

The `DELTA_UNIFORM_INGRESS_VIOLATION` error class (SQLSTATE: KD00E) contains multiple sub-error conditions that report different failure scenarios. The general error message format is: "Metadata conversion from `<format>` to Delta failed, `<errorMessage>`." The root cause varies depending on the specific sub-error triggered. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Sub-Error Conditions

### DELTA_LOG_LOCATION_NOT_FOUND

This sub-error occurs when the delta log location is missing for a table. The system reports:

- `The delta_log location is missing for table <tableName>.`
- `Cannot find metadata path for table <tableName>.`

This error indicates that the Delta Log directory, which contains transaction metadata, cannot be located for the specified table. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

### NOT_UNIFORM_INGRESS_TABLE

This sub-error occurs when an operation is attempted on a table that is not configured as a uniform ingress table. The system reports: `Table <tableName> is not a uniform ingress table.`

This error indicates that the table lacks the proper configuration to participate in the Delta Uniform ingress workflow. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

### OPERATION_NOT_SUPPORTED

This sub-error occurs when an unsupported operation is attempted on a Uniform Apache Iceberg Ingress Table. The system reports: `Operation is not supported. Only CREATE and REFRESH are supported on Uniform Apache Iceberg Ingress Table.`

The only valid operations for these tables are creating them or refreshing their metadata. Any other operation will trigger this error. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

### UNEXPECTED_DELTA_LOG_LOCATION

This sub-error occurs when the delta log location is found but at an unexpected path. The system reports: `Unexpected delta_log location <tablePath> for table <tableName>.`

This indicates that the Delta Log directory exists but is not located where the system expects it to be for the specified table. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

### UNITY_CATALOG_NOT_ENABLED

This sub-error occurs when attempting to read Apache Iceberg with Delta Uniform without [Unity Catalog](/concepts/unity-catalog.md) enabled. The system reports: `Unity Catalog is required for Read Apache Iceberg with Delta Uniform.`

This error indicates that the necessary Unity Catalog integration is not available, which is a prerequisite for reading Apache Iceberg tables through Delta Uniform. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Uniform](/concepts/delta-uniform.md) — The feature enabling interoperability between Delta Lake and Apache Iceberg
- [Uniform Apache Iceberg Ingress Tables](/concepts/uniform-apache-iceberg-ingress-table.md) — Tables configured for two-way metadata synchronization
- Delta Log — The transaction log that tracks all changes to a Delta table
- [Unity Catalog](/concepts/unity-catalog.md) — Required for reading Apache Iceberg with Delta Uniform
- Error Conditions — General framework for error handling in Databricks

## Sources

- delta_uniform_ingress_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_ingress_violation-error-condition-databricks-on-aws.md](/references/delta_uniform_ingress_violation-error-condition-databricks-on-aws-1bfee206.md)

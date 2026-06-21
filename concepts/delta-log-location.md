---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 33460173d800fe2ae9cb1b7f02a897aa1502c497f1904cf0f114f3dfbda946db
  pageDirectory: concepts
  sources:
    - delta_uniform_ingress_violation-error-condition-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - delta-log-location
    - DLL
  citations:
    - file: delta_uniform_ingress_violation-error-condition-databricks-on-aws.md
title: Delta Log Location
description: The metadata directory (_delta_log) for a Delta table; errors occur when this location is missing or unexpected during Uniform Ingress operations.
tags:
  - delta-lake
  - metadata
timestamp: "2026-06-19T15:08:49.132Z"
---

# Delta Log Location

**Delta Log Location** refers to the directory path where a Delta table stores its transaction log—the ordered sequence of delta files that track all changes to the table. This location is critical for Delta Lake operations because it determines how the table's metadata is accessed, managed, and maintained.

## Overview

The Delta log is a fundamental component of the [Delta Lake](/concepts/delta-lake.md) architecture. It resides in a dedicated `_delta_log` directory within the table's storage location and contains transaction logs that record all changes made to the table, including operations like writes, deletes, and schema changes. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Delta Log Location Issues

**DELTA_LOG_LOCATION_NOT_FOUND** is an error condition that occurs when the delta_log location is missing for a specified table. This is part of the broader `DELTA_UNIFORM_INGRESS_VIOLATION` error class, which handles various failure scenarios related to [Delta Uniform](/concepts/delta-uniform.md) ingress operations. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

### Error Messages

The system returns the following error messages when the delta log location is not found:

- `The delta_log location is missing for table <tableName>.`
- `Cannot find metadata path for table <tableName>.`

These errors typically occur when:
- The table's `_delta_log` directory has been deleted or corrupted
- The table is being accessed without proper Delta Lake metadata
- The table was not created using Delta Lake format

## Related Error Conditions

The `DELTA_UNIFORM_INGRESS_VIOLATION` error class includes several related conditions:

### NOT_UNIFORM_INGRESS_TABLE
Occurs when the specified table is not a uniform ingress table—a table that allows uniform access through [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) compatibility. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

### UNEXPECTED_DELTA_LOG_LOCATION
Happens when the delta_log location contains an unexpected path for the specified table. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

### UNITY_CATALOG_NOT_ENABLED
Indicates that [Unity Catalog](/concepts/unity-catalog.md) is required for reading Apache Iceberg tables with Delta Uniform. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Best Practices

To avoid delta log location issues:

1. **Maintain consistent storage paths**: Ensure the `_delta_log` directory is always present in the table's storage location
2. **Use proper table creation**: Create tables using Delta Lake format to ensure proper metadata setup
3. **Enable Unity Catalog**: For operations requiring Apache Iceberg compatibility, ensure Unity Catalog is enabled
4. **Handle ingress properly**: Only `CREATE` and `REFRESH` operations are supported on uniform ingress tables ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) – The foundational storage layer for Delta tables
- [Delta Uniform](/concepts/delta-uniform.md) – Enables uniform access to Delta tables through standard formats like Apache Iceberg
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) – A table format for large analytic datasets
- [Unity Catalog](/concepts/unity-catalog.md) – Databricks' unified governance solution for data assets
- [Transaction Log](/concepts/delta-transaction-log.md) – The core component of Delta Lake's ACID transactions

## Sources

- delta_uniform_ingress_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_ingress_violation-error-condition-databricks-on-aws.md](/references/delta_uniform_ingress_violation-error-condition-databricks-on-aws-1bfee206.md)

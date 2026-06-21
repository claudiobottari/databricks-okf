---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a5da56c572b199d4fe4233be1d6309abb16a9af96faf2aa15b32dd2f74c41135
  pageDirectory: concepts
  sources:
    - delta_uniform_ingress_violation-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta_uniform_ingress_violation
    - DELTA_UNIFORM_INGRESS_VIOLATION
  citations:
    - file: delta_uniform_ingress_violation-error-condition-databricks-on-aws.md
title: DELTA_UNIFORM_INGRESS_VIOLATION
description: An error class in Databricks raised when reading Delta Uniform tables fails due to metadata conversion or configuration issues.
tags:
  - error-handling
  - delta-uniform
  - databricks
timestamp: "2026-06-19T10:09:27.912Z"
---

# DELTA_UNIFORM_INGRESS_VIOLATION

**DELTA_UNIFORM_INGRESS_VIOLATION** (SQLSTATE: KD00E) is an error class in Databricks that occurs when reading Delta Uniform fails due to metadata conversion issues. The error is triggered when metadata conversion from a source format to Delta format fails with a specific error message. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Error Subtypes

The error class includes several specific subtypes that identify the exact nature of the violation:

### DELTA_LOG_LOCATION_NOT_FOUND
This error occurs when the delta_log location is missing for the specified table. The system cannot find the metadata path required to process the table. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

- **Error message**: "The delta_log location is missing for table `<tableName>`." / "Cannot find metadata path for table `<tableName>`."

### NOT_UNIFORM_INGRESS_TABLE
This error indicates that the specified table is not configured as a uniform ingress table. Only tables set up with uniform ingress capabilities can be processed through this workflow. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

- **Error message**: "Table `<tableName>` is not a uniform ingress table."

### OPERATION_NOT_SUPPORTED
This error occurs when an unsupported operation is attempted on a uniform Apache Iceberg ingress table. Only `CREATE` and `REFRESH` operations are supported for these tables. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

- **Error message**: "Operation is not supported. Only `CREATE` and `REFRESH` are supported on Uniform Apache Iceberg Ingress Table."

### UNEXPECTED_DELTA_LOG_LOCATION
This error occurs when the system encounters a delta_log location that doesn't match expectations for the specified table. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

- **Error message**: "Unexpected delta_log location `<tablePath>` for table `<tableName>`."

### UNITY_CATALOG_NOT_ENABLED
This error indicates that Unity Catalog is required but not enabled for reading Apache Iceberg tables with Delta Uniform. The operation cannot proceed without Unity Catalog being properly configured. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

- **Error message**: "Unity Catalog is required for Read Apache Iceberg with Delta Uniform."

## Common Causes

The DELTA_UNIFORM_INGRESS_VIOLATION error typically occurs when:
- The Delta log directory or metadata path is missing or inaccessible
- The table is not properly configured for uniform ingress
- An unsupported operation (other than CREATE or REFRESH) is attempted
- The Delta log location doesn't match expected parameters for the table
- Unity Catalog is not enabled when required for the operation

## Resolution

To resolve this error, verify:
1. The table is properly configured as a uniform ingress table
2. Only supported operations (`CREATE` or `REFRESH`) are being used
3. Unity Catalog is enabled when accessing [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) tables
4. The delta_log location exists and is accessible at the expected path

## Related Concepts

- [Delta Uniform](/concepts/delta-uniform.md) - The underlying technology for uniform data access
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) - The table format being accessed through Delta Uniform
- [Unity Catalog](/concepts/unity-catalog.md) - Required catalog service for certain operations
- [Delta Lake](/concepts/delta-lake.md) - The storage layer providing Delta format capabilities
- SQLSTATE - Databricks SQL error state classification system

## Sources

- delta_uniform_ingress_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_ingress_violation-error-condition-databricks-on-aws.md](/references/delta_uniform_ingress_violation-error-condition-databricks-on-aws-1bfee206.md)

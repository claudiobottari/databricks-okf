---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8de5aa268a342e1a3f201a213bf06e246b7f55914edaa6a79a11cd3296acb32c
  pageDirectory: concepts
  sources:
    - delta_uniform_ingress_violation-error-condition-databricks-on-aws.md
  confidence: 0.7
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - delta-uniform-delta-lake-uniform
    - DU(LU
    - Uniform (Delta Lake)
  citations:
    - file: delta_uniform_ingress_violation-error-condition-databricks-on-aws.md
title: Delta Uniform (Delta Lake Uniform)
description: A Databricks feature that provides interoperability between Delta Lake and Apache Iceberg formats, allowing tables to be read using Iceberg readers while maintaining Delta Lake as the primary format.
tags:
  - delta-lake
  - iceberg
  - interoperability
  - databricks
timestamp: "2026-06-18T15:23:38.415Z"
---

# Delta Uniform (Delta Lake Uniform)

**Delta Uniform** (also referred to as **Delta Lake Uniform**) is a Databricks feature that enables reading [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) tables using the [Delta Lake](/concepts/delta-lake.md) format. It relies on [Unity Catalog](/concepts/unity-catalog.md) to perform metadata conversion between the two table formats. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Overview

Delta Uniform allows users to read tables that are physically stored in the Apache Iceberg format as if they were Delta tables. The feature performs an automatic metadata conversion from the source format (Iceberg) to Delta. When this conversion fails, the system raises a `DELTA_UNIFORM_INGRESS_VIOLATION` error. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

The error message associated with this condition is:

```
Read Delta Uniform fails:
Metadata conversion from <format> to Delta failed, <errorMessage>.
```

## Prerequisites

- **Unity Catalog** must be enabled on the workspace. Delta Uniform for reading Apache Iceberg tables is only supported when Unity Catalog is active. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Error Conditions

When a Delta Uniform read operation fails, the system returns one of the following specific error types as part of the `DELTA_UNIFORM_INGRESS_VIOLATION` error class.

### DELTA_LOG_LOCATION_NOT_FOUND

The Delta log directory is missing for the target table. This error occurs when the `_delta_log` location cannot be found for the specified table name. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

```
The delta_log location is missing for table <tableName>.
Cannot find metadata path for table <tableName>.
```

### NOT_UNIFORM_INGRESS_TABLE

The table is not configured as a Uniform ingress table. Delta Uniform ingress reads only work on tables that are explicitly designated as uniform ingress tables. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

```
Table <tableName> is not a uniform ingress table.
```

### OPERATION_NOT_SUPPORTED

The attempted operation is not supported for Uniform Apache Iceberg ingress tables. Only `CREATE` and `REFRESH` operations are allowed on such tables. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

```
Operation is not supported. Only `CREATE` and `REFRESH` are supported on Uniform Apache Iceberg Ingress Table.
```

### UNEXPECTED_DELTA_LOG_LOCATION

The Delta log location found for the table is not the expected location, causing the read to fail. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

```
Unexpected delta_log location <tablePath> for table <tableName>.
```

### UNITY_CATALOG_NOT_ENABLED

Unity Catalog is required for reading Apache Iceberg tables with Delta Uniform, but it is not enabled in the workspace. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

```
Unity Catalog is required for Read Apache Iceberg with Delta Uniform.
```

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md)
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- Table Ingress
- Metadata Conversion

## Sources

- delta_uniform_ingress_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_ingress_violation-error-condition-databricks-on-aws.md](/references/delta_uniform_ingress_violation-error-condition-databricks-on-aws-1bfee206.md)

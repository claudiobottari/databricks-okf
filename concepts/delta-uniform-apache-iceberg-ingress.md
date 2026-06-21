---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9ef603cc58ad4395be629f72f4ebd38d0191a7daef0bd41a6253a94eff90475b
  pageDirectory: concepts
  sources:
    - delta_uniform_ingress_violation-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - delta-uniform-apache-iceberg-ingress
    - DU(II
    - Delta-Iceberg Bridge
  citations:
    - file: delta_uniform_ingress_violation-error-condition-databricks-on-aws.md
title: Delta Uniform (Apache Iceberg Ingress)
description: A Databricks feature that allows reading Apache Iceberg tables using Delta Lake via a uniform ingress table configuration
tags:
  - delta-lake
  - apache-iceberg
  - databricks
  - lakehouse
timestamp: "2026-06-18T11:57:08.256Z"
---

# Delta Uniform (Apache Iceberg Ingress)

**Delta Uniform (Apache Iceberg Ingress)** is a Databricks feature that enables reading Apache Iceberg tables through the Delta Lake protocol by converting Iceberg metadata to Delta format. This allows users to query Iceberg tables using Delta Lake readers without requiring changes to existing Iceberg workloads.

## Overview

Delta Uniform provides a bridge between Apache Iceberg and Delta Lake by performing metadata conversion at read time. When a user queries an Iceberg table through the Delta Uniform interface, the system converts the Iceberg metadata to Delta format, enabling Delta Lake-compatible readers to access the data. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Common Error: DELTA_UNIFORM_INGRESS_VIOLATION

The `DELTA_UNIFORM_INGRESS_VIOLATION` error condition (SQLSTATE: KD00E) occurs when Delta Uniform encounters a problem reading an Iceberg table. The general error message format is:

```
Read Delta Uniform fails:
Metadata conversion from <format> to Delta failed, <errorMessage>.
```

^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

### Specific Error Subtypes

#### DELTA_LOG_LOCATION_NOT_FOUND

This error occurs when the Delta log location is missing for the specified table. The error messages are:

```
The delta_log location is missing for table <tableName>.
Cannot find metadata path for table <tableName>.
```

^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

This indicates that the Delta Uniform conversion process cannot locate the Delta log directory that should contain the converted metadata for the Iceberg table.

#### NOT_UNIFORM_INGRESS_TABLE

This error occurs when a table is not configured as a Uniform Ingress table:

```
Table <tableName> is not a uniform ingress table.
```

^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

Only tables explicitly set up for Uniform Ingress can be accessed through this feature. Regular Delta or Iceberg tables that have not been configured for Uniform Ingress will trigger this error.

#### OPERATION_NOT_SUPPORTED

This error occurs when an unsupported operation is attempted on a Uniform Ingress table:

```
Operation is not supported. Only `CREATE` and `REFRESH` are supported on Uniform Apache Iceberg Ingress Table.
```

^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

Delta Uniform Ingress tables only support two operations:
- **CREATE**: Creating a new Uniform Ingress table
- **REFRESH**: Refreshing the metadata conversion for an existing Uniform Ingress table

Operations such as DELETE, UPDATE, or MERGE are not supported on Uniform Ingress tables.

#### UNEXPECTED_DELTA_LOG_LOCATION

This error occurs when the Delta log location for a table does not match the expected location:

```
Unexpected delta_log location <tablePath> for table <tableName>.
```

^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

This typically indicates a misconfiguration or corruption in the metadata path mapping between the Iceberg table and its corresponding Delta log.

#### UNITY_CATALOG_NOT_ENABLED

This error occurs when Unity Catalog is not enabled, which is a requirement for Delta Uniform:

```
Unity Catalog is required for Read Apache Iceberg with Delta Uniform.
```

^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

Delta Uniform requires [Unity Catalog](/concepts/unity-catalog.md) to manage the metadata conversion process. Workspaces without Unity Catalog cannot use this feature.

## Requirements

- The workspace must have [Unity Catalog](/concepts/unity-catalog.md) enabled ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]
- Tables must be explicitly configured as Uniform Ingress tables ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]
- Only `CREATE` and `REFRESH` operations are supported ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — Required for Delta Uniform functionality
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) — The open table format being bridged through Delta Uniform
- [Delta Lake](/concepts/delta-lake.md) — The target format for metadata conversion
- [ABAC GRANT Policy](/concepts/abac-grant-policy.md) — Access control policies applicable to tables in Unity Catalog
- [Delta Sharing](/concepts/delta-sharing.md) — Alternative mechanism for cross-platform data access

## Sources

- delta_uniform_ingress_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_ingress_violation-error-condition-databricks-on-aws.md](/references/delta_uniform_ingress_violation-error-condition-databricks-on-aws-1bfee206.md)

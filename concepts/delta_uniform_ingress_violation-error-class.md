---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4069b0be8b75680494572c31892adc89431e88d92699b01fdb3fbc2bdd49580f
  pageDirectory: concepts
  sources:
    - delta_uniform_ingress_violation-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta_uniform_ingress_violation-error-class
    - DEC
    - DELTA_UNIFORM_INGRESS_VIOLATION error class
  citations:
    - file: delta_uniform_ingress_violation-error-condition-databricks-on-aws.md
title: DELTA_UNIFORM_INGRESS_VIOLATION Error Class
description: A Databricks error class (SQLSTATE KD00E) raised when reading a Delta Uniform table fails due to metadata conversion or ingress configuration issues.
tags:
  - error-handling
  - databricks
  - delta-uniform
timestamp: "2026-06-19T18:28:00.015Z"
---

# DELTA_UNIFORM_INGRESS_VIOLATION Error Class

**DELTA_UNIFORM_INGRESS_VIOLATION** (SQLSTATE: KD00E) is a Databricks error class that is raised when a Delta Lake operation fails during the ingress of data from an Apache Iceberg table into Delta format. The error indicates that metadata conversion from the source format to Delta failed, or that a required precondition for the ingress was not met. All errors in this class follow the pattern:

```
Read Delta Uniform fails:
Metadata conversion from <format> to Delta failed, <errorMessage>.
```

The placeholder `<format>` specifies the source format (typically Apache Iceberg), and `<errorMessage>` provides the specific detail from one of the sub-errors described below. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Error Conditions

### DELTA_LOG_LOCATION_NOT_FOUND

This sub-error occurs when the Delta log location is missing for a table. The possible messages are:

- `The delta_log location is missing for table <tableName>.`
- `Cannot find metadata path for table <tableName>.`

These messages indicate that the Delta Lake metadata directory (`_delta_log`) cannot be located for the specified table, which is required for the uniform ingress operation. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

### NOT_UNIFORM_INGRESS_TABLE

This sub-error occurs when a table is not configured as a uniform ingress table. The message is:

- `Table <tableName> is not a uniform ingress table.`

Only tables specifically designated as [Uniform Apache Iceberg Ingress](/concepts/uniform-apache-iceberg-ingress-table.md) tables can participate in this operation. Tables created or managed through other mechanisms will trigger this error. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

### OPERATION_NOT_SUPPORTED

This sub-error occurs when an unsupported operation is attempted on a Uniform Apache Iceberg Ingress Table. The message is:

- `Operation is not supported. Only CREATE and REFRESH are supported on Uniform Apache Iceberg Ingress Table.`

The only allowed operations on these tables are `CREATE` (to create a new uniform ingress table) and `REFRESH` (to refresh metadata). Any other operation triggers this error. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

### UNEXPECTED_DELTA_LOG_LOCATION

This sub-error occurs when the Delta log location does not match the expected path for the table. The message is:

- `Unexpected delta_log location <tablePath> for table <tableName>.`

This indicates that the Delta log directory exists at a path that does not correspond to the expected location for the specified table, suggesting a misconfiguration or inconsistency in the table's metadata. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

### UNITY_CATALOG_NOT_ENABLED

This sub-error occurs when [Unity Catalog](/concepts/unity-catalog.md) is not enabled for the workspace. The message is:

- `Unity Catalog is required for Read Apache Iceberg with Delta Uniform.`

Unity Catalog is a prerequisite for reading Apache Iceberg tables using [Delta Uniform](/concepts/delta-uniform.md) functionality. Attempting this operation without Unity Catalog enabled results in this error. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Uniform](/concepts/delta-uniform.md) — Feature enabling interoperability between Delta Lake and Apache Iceberg.
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) — Open table format for large analytic datasets.
- [SQLSTATE KD00E](/concepts/sqlstate-kd00e.md) — SQLSTATE class for datasource-specific errors.
- [Unity Catalog](/concepts/unity-catalog.md) — Databricks' unified governance solution.

## Sources

- delta_uniform_ingress_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_ingress_violation-error-condition-databricks-on-aws.md](/references/delta_uniform_ingress_violation-error-condition-databricks-on-aws-1bfee206.md)

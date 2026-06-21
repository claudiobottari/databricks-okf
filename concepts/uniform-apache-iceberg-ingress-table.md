---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f9fa91bb8a74c0a3a1c50ef5e1d501c24b4478c7b004df8567f8345d8c2f3fac
  pageDirectory: concepts
  sources:
    - delta_uniform_ingress_violation-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - uniform-apache-iceberg-ingress-table
    - UAIIT
    - Uniform Apache Iceberg Ingress
    - Uniform Apache Iceberg Ingress Tables
  citations:
    - file: delta_uniform_ingress_violation-error-condition-databricks-on-aws.md
title: Uniform Apache Iceberg Ingress Table
description: A Databricks table type that allows ingesting Iceberg metadata into Delta format, supporting only CREATE and REFRESH operations.
tags:
  - databricks
  - delta-lake
  - apache-iceberg
timestamp: "2026-06-19T15:09:31.491Z"
---

# Uniform Apache Iceberg Ingress Table

**Uniform Apache Iceberg Ingress Table** is a Databricks table type that allows reading Apache Iceberg formatted data through the [Delta Lake](/concepts/delta-lake.md) protocol by providing a Delta-compatible metadata layer over Iceberg tables. It enables Unity Catalog to manage and serve Iceberg tables using Delta Lake's catalog and query engine capabilities. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Overview

A Uniform Apache Iceberg Ingress Table bridges the Delta Lake and Apache Iceberg formats by storing data in Iceberg format while making it readable through Delta Lake readers. The system performs metadata conversion from Iceberg to Delta format when reading, allowing Unity Catalog to treat the table as a Delta table for catalog operations. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Supported Operations

Only two operations are supported on Uniform Apache Iceberg Ingress Tables:

- **CREATE**: Creates a new Uniform Apache Iceberg Ingress Table
- **REFRESH**: Refreshes the metadata conversion to reflect the latest state of the underlying Iceberg table

Any other operations will result in an `OPERATION_NOT_SUPPORTED` error. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Prerequisites

### Unity Catalog Requirement

To read Apache Iceberg tables through Delta Uniform, [Unity Catalog](/concepts/unity-catalog.md) must be enabled. Without Unity Catalog, operations will fail with a `UNITY_CATALOG_NOT_ENABLED` error. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

### Table Requirements

The table must be a valid uniform ingress table, meaning it must have been properly created as a Uniform Apache Iceberg Ingress Table. Attempting to read a standard table through this mechanism will result in a `NOT_UNIFORM_INGRESS_TABLE` error. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Common Errors

The following error conditions can occur when working with Uniform Apache Iceberg Ingress Tables:

### DELTA_LOG_LOCATION_NOT_FOUND

Occurs when the Delta log location is missing for the specified table. The system cannot find the metadata path required to read the Iceberg data through Delta format. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

### NOT_UNIFORM_INGRESS_TABLE

Raised when attempting to read a table that is not a Uniform Apache Iceberg Ingress Table through the uniform ingress interface. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

### OPERATION_NOT_SUPPORTED

Indicates that an unsupported operation was attempted. Only `CREATE` and `REFRESH` are valid operations. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

### UNEXPECTED_DELTA_LOG_LOCATION

Occurs when the Delta log location does not match the expected path for the given table. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

### UNITY_CATALOG_NOT_ENABLED

Raised when Unity Catalog is not enabled in the workspace. This is a prerequisite for using Uniform Apache Iceberg Ingress Tables. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## How Metadata Conversion Works

When reading a Uniform Apache Iceberg Ingress Table, Databricks performs metadata conversion from the Iceberg format to Delta format. If this conversion fails, the system reports a generic metadata conversion failure with both the source format and the specific error message. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The storage layer providing ACID transactions and metadata management
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) — The open table format underlying the uniform ingress table
- [Unity Catalog](/concepts/unity-catalog.md) — Required catalog for managing uniform ingress tables
- [Delta Uniform](/concepts/delta-uniform.md) — The mechanism for reading Iceberg tables through Delta protocol
- [SQLSTATE KD00E](/concepts/sqlstate-kd00e.md) — The error class for datasource-specific errors related to Delta Uniform operations

## Sources

- delta_uniform_ingress_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_ingress_violation-error-condition-databricks-on-aws.md](/references/delta_uniform_ingress_violation-error-condition-databricks-on-aws-1bfee206.md)

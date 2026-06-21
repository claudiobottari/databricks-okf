---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3cf8c241b7950d20d4d57c8b220059af76bbd04cca0f5fa1fab2447e1805ccf7
  pageDirectory: concepts
  sources:
    - delta_uniform_ingress_violation-error-condition-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - uniform-iceberg-ingress-table
    - UIIT
    - Iceberg Ingress Table
  citations:
    - file: delta_uniform_ingress_violation-error-condition-databricks-on-aws.md
title: Uniform Iceberg Ingress Table
description: A Delta Uniform table that ingests Apache Iceberg data, supporting only CREATE and REFRESH operations; violations of this constraint raise the OPERATION_NOT_SUPPORTED error.
tags:
  - delta-lake
  - iceberg
  - ingress
  - databricks
timestamp: "2026-06-18T15:23:44.978Z"
---

# Uniform Iceberg Ingress Table

**Uniform Iceberg Ingress Table** is a type of [Delta Lake](/concepts/delta-lake.md) table that enables reading [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) data through Delta Uniform. It requires [Unity Catalog](/concepts/unity-catalog.md) and supports only `CREATE` and `REFRESH` operations.

## Overview

A Uniform Iceberg Ingress Table is a Delta table that has been configured to allow Iceberg clients to read underlying data using the Iceberg format. The term "Uniform Ingress" indicates that the table is set up to accept Iceberg-compatible reads by maintaining a synchronized Iceberg metadata layer alongside the Delta metadata. This capability is part of Databricks' Delta Uniform feature.

## Error Conditions

The following error conditions can occur when working with Uniform Iceberg Ingress Tables. They are grouped under the `DELTA_UNIFORM_INGRESS_VIOLATION` error class (SQLSTATE: KD00E).

### DELTA_LOG_LOCATION_NOT_FOUND

The Delta log location is missing for the table. The error message indicates that the metadata path for the table cannot be found. This typically means the `_delta_log` directory does not exist or is inaccessible for the specified table.^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

### NOT_UNIFORM_INGRESS_TABLE

The operation was attempted on a table that is not a Uniform Ingress table. Only tables specifically configured as Uniform Ingress tables support the related operations.^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

### OPERATION_NOT_SUPPORTED

Only `CREATE` and `REFRESH` operations are supported on a Uniform Apache Iceberg Ingress Table. Any other operation (e.g., `ALTER`, `INSERT`) will raise this error.^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

### UNEXPECTED_DELTA_LOG_LOCATION

The Delta log location points to an unexpected path for the given table. This indicates a mismatch between where the system expects the Delta log to reside and where it actually is.^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

### UNITY_CATALOG_NOT_ENABLED

Unity Catalog is required to read Apache Iceberg with Delta Uniform. If the workspace or [Metastore](/concepts/metastore.md) does not have Unity Catalog enabled, this error is raised.^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Uniform](/concepts/delta-uniform.md) – The feature that allows Iceberg clients to read Delta tables.
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) – The open table format used for Iceberg ingress.
- [Delta Lake](/concepts/delta-lake.md) – The underlying storage format of the table.
- [Unity Catalog](/concepts/unity-catalog.md) – Required for reading Iceberg data with Delta Uniform.
- Iceberg Ingress Table – Another term for a table that supports Iceberg reads via Delta Uniform.
- [SQLSTATE KD00E](/concepts/sqlstate-kd00e.md) – Datasource-specific error class for Delta Uniform violations.

## Sources

- delta_uniform_ingress_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_ingress_violation-error-condition-databricks-on-aws.md](/references/delta_uniform_ingress_violation-error-condition-databricks-on-aws-1bfee206.md)

---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c282151d4780f484059191e3eee34f8796cfe6cf923dc0128bbc17847d6a87dc
  pageDirectory: concepts
  sources:
    - delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - delta-uniform
    - Delta Lake Uniform
    - Read Delta Uniform
    - CREAT TABLE ... UNIFORM
    - Iceberg Reads (UniForm)
    - Uniform
    - delta-uniform-delta-lake-uniform
    - DU(LU
    - Uniform (Delta Lake)
    - delta-uniform-uniform
    - DU(
    - Delta Sharing Uniform Format
    - Delta UniForm documentation
    - Uniform (UniForm)
    - Uniform Format
    - uniform-delta-uniform
  citations:
    - file: delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md
    - file: delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md
title: Delta Uniform
description: A Databricks feature that enables Delta Lake tables to be readable as Apache Iceberg tables, requiring specific table properties like tableId, snapshotId, and metadataLocation.
tags:
  - delta-lake
  - iceberg
  - databricks
  - interoperability
timestamp: "2026-06-19T18:27:46.798Z"
---

# Delta UniForm

**Delta UniForm** is a Databricks feature that enables reading [Delta Lake](/concepts/delta-lake.md) tables through the [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) protocol. It works by generating Iceberg-compatible metadata alongside the Delta transaction log, allowing Iceberg-native tools and engines to query Delta tables without modifying the tables themselves. ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md, delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md]

## How It Works

Delta UniForm maintains Iceberg metadata files that reflect the state of the Delta table. When a Delta table has the required table properties (`tableId`, `snapshotId`, `metadataLocation`), the Delta engine can serve Iceberg read requests. The Iceberg metadata is kept in sync with the Delta transaction log, enabling Iceberg readers to discover and read the table as if it were a native Iceberg table. ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

A refresh operation updates the exposed Iceberg metadata to point to a newer version of the Delta table. The refreshed metadata location must have a higher version than the existing one; refreshing with a lower or equal version is not supported. ^[delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md]

## Error Conditions

Delta UniForm produces specific errors when the Iceberg metadata or Delta table properties are inconsistent or corrupted.

### DELTA_UNIFORM_ICEBERG_INGRESS_VIOLATION

This error occurs when reading an Iceberg table through Delta UniForm fails. The error message includes a failed parse of the version from the existing or current metadata location. ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

The root cause is often a malformed file name in the Iceberg writer. Check that the Iceberg writer follows the correct Iceberg file naming convention. ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

#### Sub‑conditions

**MISSING_UNIFORM_TBL_PROPERTIES**  
At least one of the required Delta table properties (`tableId`, `snapshotId`, `metadataLocation`) is missing. This can happen if the Delta transaction log (`_delta_log/`) has been manually edited or corrupted. ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

**MUST_REFRESH_SAME_TABLE**  
A refresh operation attempted to replace the existing Iceberg metadata UUID with a metadata UUID from a different Iceberg table. Refreshing is only allowed when the existing and new metadata belong to the same Iceberg table (same UUID). Additionally, the new metadata location must have a higher version than the existing one. ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

### DELTA_UNIFORM_REFRESH_INVALID_ARGUMENT

This error is raised when the arguments supplied to a Delta UniForm refresh operation are invalid. The exact message details are defined in the error class specification. ^[delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md]

## Best Practices

- **Ensure consistent Iceberg writers** – Use writers that produce correctly formatted metadata file names and follow the Iceberg specification.
- **Do not manually edit `_delta_log/`** – Avoid modifying the Delta transaction log outside of Delta Lake operations, as this can strip required table properties.
- **Refresh only when needed** – When refreshing the Iceberg metadata, confirm that the new metadata belongs to the same table UUID and has a strictly higher version number.

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) – The underlying storage format for Delta UniForm
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) – The external table format that Delta UniForm exposes
- Iceberg file naming convention – The standard Iceberg uses for metadata files
- Table properties – Delta table configuration that enables UniForm

## Sources

- delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md
- delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md](/references/delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws-37d8ed72.md)
2. [delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md](/references/delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws-592e817e.md)

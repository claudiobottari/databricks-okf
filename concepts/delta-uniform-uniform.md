---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 21358e8fdf943474ee2051128e42b51009e8f6d3600b9188ce8d283263c59aa3
  pageDirectory: concepts
  sources:
    - delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - delta-uniform-uniform
    - DU(
    - Delta Sharing Uniform Format
    - Delta UniForm documentation
    - Uniform (UniForm)
    - Uniform Format
  citations:
    - file: delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md
title: Delta Uniform (UniForm)
description: A Databricks feature that allows Delta Lake tables to be read natively as Apache Iceberg or Apache Hudi tables without conversion.
tags:
  - databricks
  - delta-lake
  - iceberg
  - feature
timestamp: "2026-06-19T10:09:07.701Z"
---

# Delta Uniform (UniForm)

**Delta Uniform (UniForm)** is a Databricks feature that enables reading [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) tables through the [Delta Lake](/concepts/delta-lake.md) engine. When reading an Iceberg table with Delta Uniform, the system may encounter a specific error class if the metadata is inconsistent or improperly formatted. ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

## Error: DELTA_UNIFORM_ICEBERG_INGRESS_VIOLATION

The `DELTA_UNIFORM_ICEBERG_INGRESS_VIOLATION` error occurs when a read operation of an Apache Iceberg table via Delta Uniform fails. This error has a SQLSTATE of `KD00E` (Datasource-specific error). ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

### Common Cause: Metadata Location Parsing Failure

The engine fails to parse the version from either the existing metadata location or the current metadata location. This typically indicates a problem with the file name convention used by the [Apache Iceberg writer](/concepts/uniform-apache-iceberg-format.md). ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

## Sub-Errors

### MISSING_UNIFORM_TBL_PROPERTIES

This sub-error occurs when at least one of the following required Delta table properties is missing: `tableId`, `snapshotId`, or `metadataLocation`. The presence of this error suggests a manual change may have been made to the `_delta_log` directory, corrupting the metadata linkage between Delta and Iceberg. ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

### MUST_REFRESH_SAME_TABLE

This sub-error occurs when attempting to refresh an existing Apache Iceberg table’s metadata (UUID `<existingId>`) with metadata from a different Iceberg table (UUID `<currentId>`). The refresh operation is only supported when both UUIDs match. Additionally, the metadata location being refreshed must have a higher version number than the existing metadata location; if the version is not greater, the refresh fails. ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

## Troubleshooting

- **Check the Apache Iceberg writer’s file naming convention** – Ensure that metadata files follow the correct versioning scheme. ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]
- **Verify Delta table properties** – Confirm that `tableId`, `snapshotId`, and `metadataLocation` are present in the Delta table properties and have not been altered. ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]
- **Ensure table identity consistency** – When refreshing metadata, use the UUID of the existing Iceberg table and provide a metadata location with a strictly higher version. ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md)
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md)
- [Delta Uniform Refresh](/concepts/delta-uniform-refresh.md)
- Iceberg Metadata
- Delta table properties

## Sources

- delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md](/references/delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws-37d8ed72.md)

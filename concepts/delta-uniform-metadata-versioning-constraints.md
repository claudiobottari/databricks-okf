---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e76c8eb72e304f097e6d8dfbf81048490c365c811725de7503fdd3d652d519f1
  pageDirectory: concepts
  sources:
    - delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-uniform-metadata-versioning-constraints
    - DUMVC
  citations:
    - file: delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md
title: Delta Uniform metadata versioning constraints
description: The requirement that Iceberg metadata locations being refreshed must have a strictly higher version number than the existing metadata location.
tags:
  - databricks
  - delta-uniform
  - versioning
  - apache-iceberg
timestamp: "2026-06-19T15:08:28.986Z"
---

# Delta Uniform Metadata Versioning Constraints

**Delta Uniform Metadata Versioning Constraints** refer to the set of rules and error conditions that govern how metadata versions are managed when reading or refreshing [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) tables through [Delta Uniform](/concepts/delta-uniform.md). These constraints ensure consistency between Delta and Iceberg metadata representations and prevent incompatible operations.

## Overview

When Delta Uniform is used to read Iceberg tables or refresh existing Iceberg metadata, the system enforces strict versioning rules on metadata locations. Violations of these constraints result in specific error conditions that indicate problems with metadata file naming, table properties, or version ordering. ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

## Error Conditions

### MISSING_UNIFORM_TBL_PROPERTIES

This error occurs when at least one of the required Delta table properties is missing: `tableId`, `snapshotId`, or `metadataLocation`. The error message includes the specific missing property and its expected value. This condition typically indicates manual changes to the `_delta_log` that removed or altered the Uniform metadata tracking properties. ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

### MUST_REFRESH_SAME_TABLE

This error occurs when attempting to refresh an existing Apache Iceberg table with metadata from a different Iceberg table UUID. The refresh operation requires that the metadata location being refreshed has a higher version than the existing metadata location. The error message includes both the existing metadata location and the current (attempted) metadata location. ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

### Version Parsing Failure

The system may fail to parse the version from either the existing metadata location or the current metadata location. This typically indicates that the file name convention used by the Apache Iceberg writer does not match the expected format. Users should check the file naming convention on the Apache Iceberg writer to resolve this issue. ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Uniform](/concepts/delta-uniform.md) — The feature that enables reading Delta tables through Iceberg-compatible clients
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) — The open table format that Delta Uniform provides compatibility with
- [Delta Lake](/concepts/delta-lake.md) — The underlying storage format for Delta tables
- Delta Log — The transaction log that tracks table metadata changes
- Iceberg Metadata — The metadata files that Iceberg uses to track table snapshots

## Sources

- delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md](/references/delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws-37d8ed72.md)

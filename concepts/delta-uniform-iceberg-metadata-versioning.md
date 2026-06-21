---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0615a14c37afe61ae17327a6058d9e1f29ac99827cce693155d4fadc9fd01fb3
  pageDirectory: concepts
  sources:
    - delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - delta-uniform-iceberg-metadata-versioning
    - DUIMV
  citations:
    - file: delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md
title: Delta Uniform Iceberg metadata versioning
description: The requirement that Iceberg metadata locations for a Delta Uniform table must follow a monotonically increasing version sequence, and refreshes must point to a higher version than the existing metadata.
tags:
  - delta-uniform
  - iceberg
  - versioning
  - metadata
timestamp: "2026-06-19T18:27:51.973Z"
---

# Delta Uniform Iceberg Metadata Versioning

**Delta Uniform Iceberg Metadata Versioning** refers to the conventions and constraints governing how metadata versions are tracked, parsed, and refreshed when a [Delta Lake](/concepts/delta-lake.md) table is configured with [Delta Uniform](/concepts/delta-uniform.md) to produce an [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) compatible metadata layer. The versioning system ensures that Iceberg metadata locations follow a consistent naming convention and that refresh operations only move forward to higher version numbers.

## Metadata Location Version Parsing

When Delta Uniform reads an Iceberg metadata location, it parses the version number from the file path. If the system cannot parse a valid version from either the existing metadata location or the current metadata location, it raises a `DELTA_UNIFORM_ICEBERG_INGRESS_VIOLATION` error. This typically occurs when the file name convention used by the Apache Iceberg writer does not match the expected format. ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

## Version Constraints for Refresh Operations

When refreshing an existing Apache Iceberg table, the metadata location to be refreshed must have a **higher version** than the existing metadata location. Attempting to refresh with a metadata location that has an equal or lower version number is not supported. ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

The system also enforces that the refresh must target the same Apache Iceberg table. If the existing metadata references a table with UUID `<existingId>` and the incoming metadata references a different table with UUID `<currentId>`, the refresh is rejected with a `MUST_REFRESH_SAME_TABLE` error. ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

## Required Table Properties for Versioning

Delta Uniform relies on three table properties to track Iceberg metadata versioning: `tableId`, `snapshotId`, and `metadataLocation`. If any of these properties is missing from the Delta table properties — for example, due to manual changes to the `_delta_log` — the system raises a `MISSING_UNIFORM_TBL_PROPERTIES` error. These properties are essential for correlating Delta Lake snapshots with their corresponding Iceberg metadata versions. ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Uniform](/concepts/delta-uniform.md) — The feature that enables Delta Lake tables to be read as Iceberg tables
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) — The open table format that Delta Uniform provides compatibility with
- [Delta Lake](/concepts/delta-lake.md) — The underlying storage format for Delta Uniform tables
- DELTA_UNIFORM_ICEBERG_INGRESS_VIOLATION — The error condition raised when versioning constraints are violated
- Delta table properties — Configuration properties stored in the Delta transaction log

## Sources

- delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md](/references/delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws-37d8ed72.md)

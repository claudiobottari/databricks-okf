---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 24f7cd7379e8f9faed118388a5d728068dab356827fa11f0831531926427c8a9
  pageDirectory: concepts
  sources:
    - delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - must_refresh_same_table-error
  citations:
    - file: delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md
title: MUST_REFRESH_SAME_TABLE error
description: A sub-error of DELTA_UNIFORM_ICEBERG_INGRESS_VIOLATION that occurs when attempting to refresh an existing Apache Iceberg table UUID with metadata from a different Iceberg table UUID, or when the refresh metadata location has a lower version than the existing location.
tags:
  - error-messages
  - delta-uniform
  - iceberg-refresh
timestamp: "2026-06-19T18:27:51.597Z"
---

# MUST_REFRESH_SAME_TABLE error

The **MUST_REFRESH_SAME_TABLE error** is a condition in the DELTA_UNIFORM_ICEBERG_INGRESS_VIOLATION error class that occurs when attempting to refresh the metadata of an existing Apache Iceberg table using metadata from a different Iceberg table. The refresh operation is only permitted when the source metadata belongs to the same logical table and has a strictly higher version number. ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

## Error Message

The full error text includes a UUID comparison and a version requirement:

```
Refresh existing Apache Iceberg table UUID <existingId>, with metadata from different Apache Iceberg table UUID <currentId> is not supported.
Metadata location to be refreshed must have a higher version than existing metadata location.
Existing metadata location <existingLocation>; current metadata location <currentLocation>.
```

^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

## Cause

The error is raised when the [Delta Uniform](/concepts/delta-uniform.md) ingress logic detects a mismatch between the existing Iceberg table's UUID and the UUID of the metadata file being applied. This indicates that an attempt was made to refresh a table with metadata belonging to a different table, which is not supported. Additionally, even if the UUIDs match, the version of the new metadata location must be higher than the version of the existing metadata location; otherwise, the refresh also fails. ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

## Common Scenarios

- Manually copying metadata files from one Iceberg table to another.
- Applying an outdated or equal-version metadata location to an existing table.
- Misconfiguring the Delta Uniform table properties so that the metadata location points to a different table.

## Resolution

Ensure that the metadata location being used for the refresh originates from the same Apache Iceberg table (i.e., has the same UUID) and that its version (often indicated by a version number in the file name or directory structure) is strictly higher than the current metadata location. Check the file name convention used by the Apache Iceberg writer to confirm correct versioning. ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Uniform](/concepts/delta-uniform.md) – The feature that enables reading Delta tables using Apache Iceberg and vice versa.
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) – The open table format used in the Delta Uniform integration.
- DELTA_UNIFORM_ICEBERG_INGRESS_VIOLATION – The parent error class containing this and other related conditions such as `MISSING_UNIFORM_TBL_PROPERTIES`.
- Delta table properties – Table properties that must include `tableId`, `snapshotId`, and `metadataLocation` for Uniform to function correctly.

## Sources

- delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md](/references/delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws-37d8ed72.md)

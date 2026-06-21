---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 07562e72ab8aef984306e5d77328bd488826730808714280276b3afbc67a9761
  pageDirectory: concepts
  sources:
    - delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - must_refresh_same_table
    - MUST_REFRESH_SAME_TABLE
    - refresh the table
  citations:
    - file: delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md
title: MUST_REFRESH_SAME_TABLE
description: A sub-error of DELTA_UNIFORM_ICEBERG_INGRESS_VIOLATION that occurs when attempting to refresh an Iceberg table with metadata from a different table UUID where the version must increase monotonically.
tags:
  - databricks
  - error-messages
  - delta-uniform
  - table-refresh
timestamp: "2026-06-19T15:08:25.111Z"
---

# MUST_REFRESH_SAME_TABLE

**MUST_REFRESH_SAME_TABLE** is a sub-error of the `DELTA_UNIFORM_ICEBERG_INGRESS_VIOLATION` error class (SQLSTATE KD00E). It occurs when an attempt to refresh an existing Apache Iceberg table uses metadata that belongs to a **different** Iceberg table (different UUID) or when the new metadata location does not have a strictly higher version number than the existing metadata location. ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

## Error Message

The error displays the following message:

```
Refresh existing Apache Iceberg table UUID <existingId>, with metadata from different Apache Iceberg table UUID <currentId> is not supported.
```

In addition, the error reports:

- Metadata location to be refreshed must have a higher version than existing metadata location.
- Existing metadata location `<existingLocation>`
- Current metadata location `<currentLocation>` ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

## Cause

This error is raised when [Delta Uniform](/concepts/delta-uniform.md) attempts to refresh an Iceberg table that was previously registered with a specific UUID. The refresh operation expects the incoming metadata to correspond to the **same** Iceberg table (same UUID) and to point to a version that is strictly greater than the currently stored version. Supplying metadata from a different table UUID, or from a lower or equal version, violates the refresh contract. ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

## Resolution

To resolve this error:

- Ensure the metadata location provided for the refresh operation belongs to the same Apache Iceberg table (identical UUID) that is already registered.
- Verify that the new metadata location has a version number higher than the existing metadata location.
- Check that the metadata file name follows the expected Apache Iceberg naming convention (for example, `00001-<uuid>.metadata.json`) so that the version number can be correctly parsed. If parsing fails, an earlier part of the error class reports a different sub-error about version parsing. ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]
- Review the configuration of the Apache Iceberg writer to ensure it is generating metadata files compatible with Delta Uniform.

## Related Concepts

- [Delta Uniform](/concepts/delta-uniform.md) – The feature that enables reading Apache Iceberg tables as Delta tables.
- MISSING_UNIFORM_TBL_PROPERTIES – A sibling sub-error of the same error class, related to missing Delta table properties.
- DELTA_UNIFORM_ICEBERG_INGRESS_VIOLATION – The parent error class.
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) – The open table format used in this workflow.
- [SQLSTATE KD00E](/concepts/sqlstate-kd00e.md) – The SQL state code associated with this error.

## Sources

- delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md](/references/delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws-37d8ed72.md)

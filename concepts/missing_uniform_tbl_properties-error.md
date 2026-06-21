---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 085f8a5b52c4127cca60d54cc8031f8aa1d810b3ac6c5d6e9c1d087dedaa080d
  pageDirectory: concepts
  sources:
    - delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - missing_uniform_tbl_properties-error
  citations:
    - file: delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md
title: MISSING_UNIFORM_TBL_PROPERTIES error
description: A sub-error of DELTA_UNIFORM_ICEBERG_INGRESS_VIOLATION indicating that one or more required Delta Uniform properties (tableId, snapshotId, metadataLocation) are missing from the Delta table properties, possibly due to manual changes to _delta_log.
tags:
  - error-messages
  - delta-uniform
  - table-properties
timestamp: "2026-06-19T18:27:45.950Z"
---

# MISSING_UNIFORM_TBL_PROPERTIES Error

The **MISSING_UNIFORM_TBL_PROPERTIES error** is a [Delta Uniform](/concepts/delta-uniform.md) error condition that occurs when reading an [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) table through [Delta Uniform](/concepts/delta-uniform.md) fails because required table properties are missing from the Delta table's metadata.

## Error Message

When this error occurs, the system returns the following message:

```
At least one of tableId <tableId>, snapshotId <snapshotId>, metadataLocation <location> is missing from Delta table properties; Is there manual change to the _delta_log?
```

^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

## Cause

The error indicates that one or more of the following required properties is missing from the Delta table's properties:

- `tableId` — The unique identifier for the Iceberg table
- `snapshotId` — The current snapshot identifier
- `metadataLocation` — The location of the Iceberg metadata file

^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

The error message suggests checking whether there has been a manual change to the `_delta_log` directory, which could have caused these properties to be removed or corrupted. ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

## Troubleshooting

To resolve this error:

1. **Check for manual modifications** — Verify that no manual changes have been made to the `_delta_log` directory that could have removed or altered the required table properties.
2. **Verify Delta table properties** — Inspect the Delta table's properties to confirm that `tableId`, `snapshotId`, and `metadataLocation` are all present and correctly set.
3. **Review Iceberg writer configuration** — Ensure that the [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) writer follows the correct file naming conventions, as the error is part of the broader `DELTA_UNIFORM_ICEBERG_INGRESS_VIOLATION` error class which also includes issues with metadata location parsing. ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Uniform](/concepts/delta-uniform.md) — The feature that enables reading Delta tables as Iceberg tables
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) — The open table format being read through Delta UniForm
- [Delta Lake](/concepts/delta-lake.md) — The underlying storage format for the Delta table
- DELTA_UNIFORM_ICEBERG_INGRESS_VIOLATION — The parent error class containing this error condition
- MUST_REFRESH_SAME_TABLE — Another error condition in the same error class

## Sources

- delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md](/references/delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws-37d8ed72.md)

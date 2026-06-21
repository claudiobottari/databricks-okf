---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 22ece04fddfb7ef7ee0ec1d3ca5e9209e2b2de531a13da033c66999d3c7155fc
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - missing_required_table_feature
    - MISSING_REQUIRED_TABLE_FEATURE
    - disabling_required_table_feature-delta-iceberg-error
    - D(IE
    - disabling_required_table_feature-error
    - disabling_required_table_feature
    - DISABLING_REQUIRED_TABLE_FEATURE
    - missing_required_table_feature-delta-iceberg-error
    - M(IE
  citations:
    - file: delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md
title: MISSING_REQUIRED_TABLE_FEATURE
description: Error sub-type indicating a required table feature for IcebergCompatV1 is not supported or enabled
tags:
  - error-messages
  - table-features
  - delta-lake
timestamp: "2026-06-19T18:25:04.603Z"
---

# MISSING_REQUIRED_TABLE_FEATURE error

The **MISSING_REQUIRED_TABLE_FEATURE** error occurs when the [IcebergCompatV1](/concepts/icebergcompatv.md) protocol is enabled on a [Delta Lake](/concepts/delta-lake.md) table, but a required Delta table feature is not supported or enabled. It is a sub‑error of the DELTA_ICEBERG_COMPAT_V1_VIOLATION error class. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Error Message

The error returns with SQLSTATE `KD00E` and displays the following message:

```
IcebergCompatV1 requires feature <feature> to be supported and enabled.
```

The placeholder `<feature>` is replaced with the name of the missing Delta table feature (e.g., `changeDataFeed`, `appendOnly`, or another reader/writer feature required by Iceberg compatibility). ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Cause

The `IcebergCompatV1` table property requires specific Delta table features to be both supported by the Delta Lake protocol and actively enabled on the table. If a required feature is not present — either because the table protocol version does not support it or because it was explicitly dropped — the validation fails with this error. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Resolution

To resolve the error, ensure that the missing Delta table feature is enabled on the table. This can be done by:

- Upgrading the Delta table protocol to a version that supports the required feature.
- Adding the feature explicitly (e.g., using `ALTER TABLE ... SET TBLPROPERTIES` if the feature is configurable).
- If you do not need Iceberg compatibility, disabling `IcebergCompatV1` by setting the table property `delta.enableIcebergCompatV1` to `false`.

For more details, see the documentation on [Delta Lake table features](/concepts/delta-lake-reader-table-features.md) and [IcebergCompatV1 configuration](/concepts/icebergcompatv-versioning.md).

## Related Concepts

- DELTA_ICEBERG_COMPAT_V1_VIOLATION error class — The parent error class that contains this sub‑error and others.
- DISABLING_REQUIRED_TABLE_FEATURE — A related sub‑error that occurs when trying to drop a feature that IcebergCompatV1 requires.
- WRONG_REQUIRED_TABLE_PROPERTY — Another sub‑error covering incorrect table property values.
- Delta Lake protocol versioning — Determines which features are supported.

## Sources

- delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md](/references/delta_iceberg_compat_v1_violation-error-class-databricks-on-aws-da04bc25.md)

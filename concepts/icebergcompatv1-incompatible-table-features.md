---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dae24d74dd65a8bb2a209f6cc2446c33e543f06ef3a386dd65f08baf8cd8fd3e
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - icebergcompatv1-incompatible-table-features
    - IITF
  citations:
    - file: delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md
title: IcebergCompatV1 Incompatible Table Features
description: Some Delta table features cannot coexist with IcebergCompatV1 and will cause a validation failure if present.
tags:
  - table-features
  - delta-lake
  - iceberg
  - compatibility
timestamp: "2026-06-18T15:19:46.049Z"
---

# IcebergCompatV1 Incompatible Table Features

**IcebergCompatV1 Incompatible Table Features** refers to a validation error that occurs when a [Delta Lake](/concepts/delta-lake.md) table attempts to enable or use a Delta table feature that is not compatible with the `IcebergCompatV1` reader/writer protocol. This error is classified under the `DELTA_ICEBERG_COMPAT_V1_VIOLATION` error class (SQLSTATE: KD00E). ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Error Message

When the validation fails, Apache Spark returns the following message:

```
IcebergCompatV1 is incompatible with feature <feature>.
```

The `<feature>` placeholder indicates the specific Delta table feature that conflicts with IcebergCompatV1. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Cause

`IcebergCompatV1` is a compatibility mode that allows Delta tables to be read by Apache Iceberg readers. To maintain this compatibility, certain Delta table features — such as advanced indexing, column mapping, or other non‑Iceberg‑conformant capabilities — must not be enabled. Attempting to enable such a feature on a table that already uses `IcebergCompatV1`, or trying to enable `IcebergCompatV1` on a table that already has an incompatible feature, raises this error. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Related Sub‑Errors

The `DELTA_ICEBERG_COMPAT_V1_VIOLATION` error class includes several other validation failures that may occur alongside the incompatible feature error:

| Sub‑error | Description |
|-----------|-------------|
| `DISABLING_REQUIRED_TABLE_FEATURE` | Try to drop a feature that IcebergCompatV1 requires. You must disable IcebergCompatV1 first. |
| `MISSING_REQUIRED_TABLE_FEATURE` | A feature needed by IcebergCompatV1 is not currently enabled on the table. |
| `WRONG_REQUIRED_TABLE_PROPERTY` | A required table property is set to an incorrect value. |
| `UNSUPPORTED_DATA_TYPE` | The schema contains `MapType`, `ArrayType`, or `NullType`, which IcebergCompatV1 does not support. |
| `REPLACE_TABLE_CHANGE_PARTITION_NAMES` | A `REPLACE TABLE` operation changes partition column names, which is not supported. |

^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Resolution

To resolve the `INCOMPATIBLE_TABLE_FEATURE` error, either:

- **Remove the incompatible feature** from the table (if possible via `ALTER TABLE ... DROP FEATURE`), or  
- **Disable IcebergCompatV1** on the table before enabling the feature that conflicts with it.

Which approach is appropriate depends on whether the incompatible feature is required for the workload and whether Iceberg‑read compatibility is needed. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Best Practices

- Review the [Delta Lake feature compatibility matrix](/concepts/delta-lake-table-features-compatibility.md) before enabling `IcebergCompatV1` on a table.
- Enable `IcebergCompatV1` only after ensuring that all existing and planned table features are compatible.
- Use the `DESCRIBE DETAIL` command to inspect the current set of enabled table features and properties.

## Related Concepts

- [Delta Lake table features](/concepts/delta-lake-reader-table-features.md)
- [IcebergCompatV1 protocol](/concepts/icebergcompatv1.md)
- Delta Lake error classes
- Apache Iceberg interoperability with Delta Lake

## Sources

- delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md](/references/delta_iceberg_compat_v1_violation-error-class-databricks-on-aws-da04bc25.md)

---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fb22b00101f2106b8c608648d446c4b4a278b3452a1dd58df3112fd27e2b05d0
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - missing_required_table_feature-delta-iceberg-error
    - M(IE
  citations:
    - file: delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md
title: MISSING_REQUIRED_TABLE_FEATURE (Delta Iceberg error)
description: A sub-error of DELTA_ICEBERG_COMPAT_V1_VIOLATION that occurs when a required table feature for IcebergCompatV1 is not enabled
tags:
  - delta-lake
  - error-subtype
  - iceberg-compatibility
timestamp: "2026-06-19T15:05:18.103Z"
---

# MISSING_REQUIRED_TABLE_FEATURE (Delta Iceberg error)

The **MISSING_REQUIRED_TABLE_FEATURE** error is a sub-error of the DELTA_ICEBERG_COMPAT_V1_VIOLATION error class (SQLSTATE: KD00E). It occurs when a Delta table has [IcebergCompatV1](/concepts/icebergcompatv1.md) enabled but is missing a table feature that IcebergCompatV1 requires. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Error Message

The full error message is:

```
IcebergCompatV1 requires feature <feature> to be supported and enabled.
```

The placeholder `<feature>` is replaced with the name of the required Delta table feature (e.g., `appendOnly`, `invariants`, `columnMapping`). ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Cause

IcebergCompatV1 imposes a set of mandatory table features that must be present and active on the Delta table. If any of these required features is missing (not yet enabled) or is not supported by the current Delta Lake protocol version, this error is raised. Typical scenarios include:

- Attempting to enable IcebergCompatV1 on a table that does not yet have all the prerequisite features.
- Running operations that accidentally remove or downgrade a required feature.
- Using an older Delta Lake runtime that does not support one of the required features.

## Resolution

To fix this error, ensure that the missing feature is both supported by your Delta Lake version and enabled on the table. You can enable a table feature using `ALTER TABLE ... SET TBLPROPERTIES` with the appropriate Delta feature property key.

If enabling the missing feature is not desirable, the alternative is to disable IcebergCompatV1 on the table first, as indicated by the related DISABLING_REQUIRED_TABLE_FEATURE sub‑error. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md] (This resolution is inferred from the overall error class context.)

## Related Sub‑Errors

The same error class includes these other sub‑errors, which may appear in related scenarios: ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

- **DISABLING_REQUIRED_TABLE_FEATURE** – Occurs when trying to drop a feature that IcebergCompatV1 requires; advises to disable IcebergCompatV1 first.
- **INCOMPATIBLE_TABLE_FEATURE** – IcebergCompatV1 is incompatible with a feature present on the table.
- **REPLACE_TABLE_CHANGE_PARTITION_NAMES** – IcebergCompatV1 does not support renaming partition columns.
- **UNSUPPORTED_DATA_TYPE** – IcebergCompatV1 does not allow `MapType`, `ArrayType`, or `NullType` in the schema.
- **WRONG_REQUIRED_TABLE_PROPERTY** – A required table property has an incorrect value.

## Related Concepts

- [IcebergCompatV1](/concepts/icebergcompatv1.md)
- [Delta Lake table features](/concepts/delta-lake-reader-table-features.md)
- DELTA_ICEBERG_COMPAT_V1_VIOLATION error class
- MISSING_REQUIRED_TABLE_FEATURE (this page)
- DISABLING_REQUIRED_TABLE_FEATURE
- WRONG_REQUIRED_TABLE_PROPERTY

## Sources

- delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md](/references/delta_iceberg_compat_v1_violation-error-class-databricks-on-aws-da04bc25.md)

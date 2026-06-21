---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8abb52c6d54045d6dad54236b9584e8365e18bd27b5909a8c4c42ff07f77f9a9
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - type-widening-indelta-iceberg-compatibility
    - TWIC
  citations:
    - file: delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
title: Type Widening inDelta-Iceberg Compatibility
description: Type changes applied to a Delta table's schema (e.g., changing a column type) can be incompatible with IcebergCompatV and trigger a violation.
tags:
  - delta-lake
  - apache-iceberg
  - schema-evolution
  - type-system
timestamp: "2026-06-18T15:20:45.787Z"
---

# Type Widening in Delta-Iceberg Compatibility

**Type widening** refers to changing a column’s data type from a narrower type to a wider type (for example, `INT` to `BIGINT` or `FLOAT` to `DOUBLE`). While Delta Lake supports type widening as part of schema evolution, the IcebergCompatV feature imposes restrictions on which schema changes are allowed. When a type‑widening change is applied to a table that has IcebergCompatV enabled, the operation is rejected, and the `DELTA_ICEBERG_COMPAT_VIOLATION` error class is raised with the `UNSUPPORTED_TYPE_WIDENING` sub‑condition.

## Error Condition

The `UNSUPPORTED_TYPE_WIDENING` error occurs when an attempt is made to change the type of a column on a table that has an active IcebergCompatV version, and that type change is considered a widening that is incompatible with the Apache Iceberg specification. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### Error Message

The full error message includes the version of IcebergCompat that is active, the field path, the previous type, and the new type:

```
IcebergCompatV<version> is incompatible with a type change applied to this table:
Field <fieldPath> was changed from <prevType> to <newType>.
```

^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### Example

If a table with `IcebergCompatV2` enabled has a column `age` changed from `INT` to `BIGINT`, the error would appear as:

```
IcebergCompatV2 is incompatible with a type change applied to this table:
Field age was changed from INT to BIGINT.
```

This example is illustrative; the error message structure is taken directly from the source.

## Cause

IcebergCompatV requires all files in the table to be Apache Iceberg compatible. Iceberg has a stricter schema evolution model than Delta Lake and does not support all type changes, particularly widening operations that can alter the on‑disk representation of data. When a table is already writing files in an Iceberg‑compatible format, applying a type‑widening schema change would break that compatibility. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Resolution

The source material does not provide a direct resolution for the `UNSUPPORTED_TYPE_WIDENING` error. To restore compatibility, you may need to:

- Revert the schema change that introduced the type widening.
- Disable the IcebergCompatV feature on the table (which will also require rewriting or migrating the table).

No automated fix or command is documented in the available sources for this specific sub‑condition.

## Related Concepts

- [IcebergCompatV](/concepts/icebergcompatv.md) — The Delta Lake feature that enforces Apache Iceberg compatibility.
- [Delta-Iceberg Compatibility](/concepts/delta-iceberg-table-feature-compatibility.md) — The broader set of features and constraints for running Delta tables as Apache Iceberg tables.
- Schema Evolution — The ability to change a table’s schema over time.
- UNSUPPORTED_DATA_TYPE — Another sub‑condition of `DELTA_ICEBERG_COMPAT_VIOLATION` for unsupported data types.
- DELTA_ICEBERG_COMPAT_V1_VIOLATION|DELTA_ICEBERG_COMPAT_VIOLATION — The parent error class for Iceberg compatibility violations.

## Sources

- delta_iceberg_compat_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_violation-error-condition-databricks-on-aws.md](/references/delta_iceberg_compat_violation-error-condition-databricks-on-aws-206a4feb.md)

---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cbbeb7810055747f1319833419ce37748491f8cf6131e3c88bf0157ca77a57ab
  pageDirectory: concepts
  sources:
    - delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-iceberg-map-key-struct-restriction
    - DMKSR
  citations:
    - file: delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md
title: Delta-Iceberg Map Key Struct Restriction
description: A restriction enforced by IcebergWriterCompatV that prevents changing map keys that are structs, because Iceberg does not support struct-typed map keys.
tags:
  - delta-lake
  - apache-iceberg
  - schema
  - data-types
timestamp: "2026-06-18T15:20:59.664Z"
---

# Delta-Iceberg Map Key Struct Restriction

**Delta-Iceberg Map Key Struct Restriction** is a specific error condition that occurs when a transaction attempts to change map keys that are structs in a Delta table operating under an `IcebergWriterCompatV` compatibility mode. The error belongs to the `DELTA_ICEBERG_WRITER_COMPAT_VIOLATION` error class. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

## Error Message

The error is reported with a `SQLSTATE: KD00E` code and the following diagnostic message:

```
CANNOT_CHANGE_MAP_STRUCT_KEY
IcebergWriterCompatV<version> disallows changing map keys that are structs. This transaction changes the key for maps: <map_names>.
```

The `<version>` placeholder indicates the specific version of the IcebergWriterCompat requirement that is being enforced, and `<map_names>` lists the map columns where the key type change was attempted. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

## Cause

When a Delta table is configured to use `IcebergWriterCompatV` — a compatibility mode that ensures Delta writes can be read correctly by [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) — certain schema evolution operations are restricted because Iceberg does not support them. Specifically, Iceberg does not allow mutating the key type of a Map column when the key is a StructType. Any attempt to alter such a map key’s schema (e.g., adding, removing, or reordering fields in the struct key) will be rejected. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

## Context

The restriction is one of several validation checks enforced by `IcebergWriterCompatV<version>`. Other checks in the same error class include prohibitions on unsupported data types, incompatible table features, and required configuration values. The map key struct restriction specifically preserves the structural integrity of map columns that Apache Iceberg cannot represent after modification. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

## Resolution

To avoid this error, ensure that any map column with a struct key type is not altered after the table is created while the IcebergWriterCompatV mode is active. Schema design for such tables should finalize the struct key fields before setting the compatibility mode. If a change to the map key is necessary, consider removing the IcebergWriterCompatV requirement (if compatibility is not essential) or redesigning the schema to avoid struct keys in map columns. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

## Related Concepts

- [IcebergWriterCompat](/concepts/icebergwritercompatv.md) — The compatibility mode that enforces the restriction
- DELTA_ICEBERG_WRITER_COMPAT_VIOLATION — The parent error class containing this condition
- [Apache Iceberg compatibility in Delta Lake](/concepts/delta-lake-table-features-and-iceberg-compatibility.md)
- Map type in Delta Lake
- StructType in Delta Lake
- Schema evolution in Delta Lake

## Sources

- delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md](/references/delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws-02e8eab9.md)

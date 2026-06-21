---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a748c9f0fcfb34678fc2b30f95d0a50fb2500a17ebb193c31435e30f121b1aa8
  pageDirectory: concepts
  sources:
    - delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-iceberg-map-key-constraints
    - DLMKC
  citations:
    - file: delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md
title: Delta Lake-Iceberg map key constraints
description: IcebergWriterCompatV prohibits changing map keys that are structs, enforced via the CANNOT_CHANGE_MAP_STRUCT_KEY condition
tags:
  - schema
  - data-types
  - compatibility
timestamp: "2026-06-18T11:55:13.102Z"
---

---
title: Delta Lake-Iceberg Map Key Constraints
summary: IcebergWriterCompatV2 disallows changing map keys that are structs, enforcing compatibility between Delta Lake and Apache Iceberg when writing to an Iceberg-compatible table via Delta Lake.
sources:
  - delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:15:00.000Z"
updatedAt: "2026-06-18T14:15:00.000Z"
tags:
  - delta-lake
  - iceberg
  - compatibility
  - error
  - schema
aliases:
  - delta-lake-iceberg-map-key-constraints
  - DLIMKC
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 1
---

# Delta Lake-Iceberg Map Key Constraints

**Delta Lake-Iceberg map key constraints** refer to a validation rule enforced by the `IcebergWriterCompatV2` compatibility mode (and later versions) in Delta Lake: **map keys that are structs cannot be changed**. This restriction ensures forward compatibility between tables written by Delta Lake and the Apache Iceberg format. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

## Constraint Description

When `IcebergWriterCompatV<version>` is enabled on a Delta table, the engine validates that the table schema does not contain maps with struct keys. If a transaction attempts to change the keys of maps that have struct types, it fails with the following error:

```
CANNOT_CHANGE_MAP_STRUCT_KEY
IcebergWriterCompatV<version> disallows changing map keys that are structs.
This transaction changes the key for maps: <map_names>.
```

^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

## Why the Constraint Exists

Apache Iceberg does not support struct types as map keys. To ensure that a Delta table can be read by Iceberg readers — and to enable the table to be written in a format compatible with Iceberg's writer specification — Delta Lake prevents schema evolutions that introduce or alter struct-typed map keys. This preemptive validation avoids silent data corruption or read failures when the table is later accessed through an Iceberg-compatible reader. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

## How the Constraint is Enforced

The `IcebergWriterCompatV<version>` protocol enforces this constraint at transaction time. When a write or schema evolution operation would change the key type of a map column from its current type to a struct (or modify an existing struct key), the engine aborts the operation and returns the `CANNOT_CHANGE_MAP_STRUCT_KEY` error. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

## Relationship to Other IcebergWriterCompatV2 Constraints

The map key constraint is one of several validation rules that `IcebergWriterCompatV<version>` imposes. Other constraints include:

- FIELD_ID_DOES_NOT_MATCH_PHYSICAL_NAME — Column mapping field physical names must equal `col-[fieldId]`.
- UNSUPPORTED_DATA_TYPE — The table schema cannot contain data types unsupported by Iceberg.
- WRONG_REQUIRED_TABLE_PROPERTY — Certain table properties must be set to specific values.
- CONFIG_NOT_ENABLED — Required configurations must be enabled.
- MISSING_REQUIRED_TABLE_FEATURE / DISABLING_REQUIRED_TABLE_FEATURE — Required table features must be supported and enabled.
- UNSUPPORTED_ICEBERG_TABLE_PROPERTY — Unsupported Iceberg table properties are not allowed.
- INCOMPATIBLE_TABLE_FEATURE — Incompatible table features are prohibited.

All of these constraints are grouped under the umbrella `DELTA_ICEBERG_WRITER_COMPAT_VIOLATION` error class with SQLSTATE `KD00E`. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

## Best Practices

- **Avoid struct-typed map keys** when designing schemas for tables that will use `IcebergWriterCompatV2` or later.
- **Use simple scalar types (STRING, INT, etc.) as map keys** instead of structs.
- If you must use struct keys in maps, disable `IcebergWriterCompatV<version>` for the table, but be aware that the table will not be compatible with Iceberg readers.
- Review all existing tables that enable Iceberg compatibility to ensure no map columns have struct keys.

## Related Concepts

- [Delta Lake-Iceberg Compatibility](/concepts/delta-lake-table-features-and-iceberg-compatibility.md) — The overall framework for making Delta tables readable by Iceberg
- [IcebergWriterCompatV2](/concepts/icebergwritercompatv.md) — The compatibility protocol version that enforces these constraints
- Delta Lake Table Features — Features that must be enabled or disabled for compatibility
- Schema Evolution in Delta Lake — How schema changes are validated against compatibility rules
- [Delta-Iceberg Bridge](/concepts/delta-uniform-apache-iceberg-ingress.md) — Connectors and protocols for cross-format table access

## Sources

- delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md](/references/delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws-02e8eab9.md)

---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 20f9b18e9bfda4117bc8b645ab8d66df21b163f097ef249209f25ddfe6bb3ad7
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md
  confidence: 0.9
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - icebergcompatv1
    - IcebergCompatV1 protocol
  citations:
    - file: delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md
title: IcebergCompatV1
description: A Delta Lake table compatibility feature that enforces Apache Iceberg compatibility requirements
tags:
  - delta-lake
  - iceberg
  - compatibility
  - databricks
timestamp: "2026-06-19T18:25:08.040Z"
---

```markdown
---
title: IcebergCompatV1
summary: A validation layer for Delta Lake tables that enforces constraints to enable compatibility with Apache Iceberg readers (Iceberg‑Spark 1.1.0), covering table features, schema types, partitioning, and table properties.
sources:
  - delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T15:40:00.000Z"
updatedAt: "2026-06-19T15:40:00.000Z"
tags:
  - delta-lake
  - iceberg
  - databricks
  - table-features
aliases:
  - icebergcompatv1
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# IcebergCompatV1

IcebergCompatV1 is a [[Delta Lake]] table feature that enforces compatibility rules for Delta tables so they can be read by Apache Iceberg readers — specifically Iceberg‑Spark 1.1.0. When enabled, the table must satisfy a set of constraints on table features, schema types, partitioning, and table properties. If any constraint is violated, the system raises a `DELTA_ICEBERG_COMPAT_V1_VIOLATION` error (SQLSTATE: KD00E). ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Required Table Features

IcebergCompatV1 requires certain [[Delta Lake Reader Table Features|Delta Lake table features]] to be both supported and enabled on the table. You cannot drop a required feature while IcebergCompatV1 is active; attempting to do so triggers the `DISABLING_REQUIRED_TABLE_FEATURE` error subtype. To remove a required feature, you must first disable IcebergCompatV1. If a required feature is not present at all, the `MISSING_REQUIRED_TABLE_FEATURE` error subtype is raised. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Incompatible Table Features

Some table features are incompatible with IcebergCompatV1. If an incompatible feature is present, validation fails with the `INCOMPATIBLE_TABLE_FEATURE` error subtype. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Required Table Properties

IcebergCompatV1 requires specific table properties to be set to particular values. When a required property has an incorrect value, the `WRONG_REQUIRED_TABLE_PROPERTY` error subtype is raised, indicating both the expected value and the current value. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Partition Spec Constraints

IcebergCompatV1 does not support replacing a partitioned table with a differently‑named partition spec. This restriction exists because Iceberg‑Spark 1.1.0 does not support this operation. The `REPLACE_TABLE_CHANGE_PARTITION_NAMES` error subtype includes both the previous and new partition specs. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Unsupported Data Types

Schemas containing `MapType`, `ArrayType`, or `NullType` columns are not allowed. If any of these types appear in the table schema, validation fails with the `UNSUPPORTED_DATA_TYPE` error subtype, which displays the offending schema. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Error Subtypes

The `DELTA_ICEBERG_COMPAT_V1_VIOLATION` error class includes the following subtypes:

| Error Subtype | Description |
|---------------|-------------|
| `DISABLING_REQUIRED_TABLE_FEATURE` | Attempting to drop a feature that IcebergCompatV1 requires |
| `INCOMPATIBLE_TABLE_FEATURE` | An incompatible table feature is present |
| `MISSING_REQUIRED_TABLE_FEATURE` | A required table feature is not supported or enabled |
| `REPLACE_TABLE_CHANGE_PARTITION_NAMES` | Replacing a partitioned table with a differently‑named partition spec |
| `UNSUPPORTED_DATA_TYPE` | Schema contains MapType, ArrayType, or NullType |
| `WRONG_REQUIRED_TABLE_PROPERTY` | A required table property has an incorrect value |

^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Related Concepts

- [[Delta Lake]] — The storage layer that provides the IcebergCompatV1 feature.
- [[Uniform (Apache Iceberg) Format|Apache Iceberg]] — The open table format that IcebergCompatV1 enables compatibility with.
- Table Features — Delta Lake features that can be enabled or disabled on tables.
- Partitioning — How data is organized in Delta tables, subject to IcebergCompatV1 constraints.
- [[Delta error SQLSTATE codes|Delta Lake SQLSTATE Error Codes]] — System error codes including datasource‑specific errors.

## Sources

- delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md
```

# Citations

1. [delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md](/references/delta_iceberg_compat_v1_violation-error-class-databricks-on-aws-da04bc25.md)

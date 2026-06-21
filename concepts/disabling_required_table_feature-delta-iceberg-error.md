---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4c3bdc0bda09b8d50decc90dac16d4f03683cb483d0d748398389c614e3a7175
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - disabling_required_table_feature-delta-iceberg-error
    - D(IE
  citations:
    - file: delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md:L9-L13
    - file: delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md:L1-L13
title: DISABLING_REQUIRED_TABLE_FEATURE (Delta Iceberg error)
description: A sub-error of DELTA_ICEBERG_COMPAT_V1_VIOLATION that occurs when attempting to drop a table feature required by IcebergCompatV1
tags:
  - delta-lake
  - error-subtype
  - iceberg-compatibility
timestamp: "2026-06-19T15:05:06.890Z"
---

# DISABLING_REQUIRED_TABLE_FEATURE (Delta Iceberg error)

The **DISABLING_REQUIRED_TABLE_FEATURE** sub-error occurs when you attempt to drop a table feature that [IcebergCompatV1](/concepts/icebergcompatv1.md) requires to be enabled. The operation is rejected because the table feature in question is mandatory for the Iceberg compatibility mode.

## Error Message

The full error belongs to the `DELTA_ICEBERG_COMPAT_V1_VIOLATION` error class (SQLSTATE: KD00E). The DISABLING_REQUIRED_TABLE_FEATURE sub-error provides the following description:

> IcebergCompatV1 requires feature `<feature>` to be supported and enabled. You cannot drop it from the table. Instead, please disable IcebergCompatV1 first.

The placeholder `<feature>` is replaced with the name of the table feature that cannot be removed (e.g., `appendOnly`, `columnMapping`, etc.). ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md:L9-L13]

## Cause

[IcebergCompatV1](/concepts/icebergcompatv1.md) is a Delta table compatibility mode that enforces a specific set of Delta table features (protocol features) to align with Apache Iceberg’s requirements. When a user attempts to drop one of those required features from the table’s protocol metadata — for example, by running an `ALTER TABLE ... DROP FEATURE` operation — the validation fails because IcebergCompatV1 cannot function without that feature. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md:L1-L13]

## Resolution

To resolve the error, you must **not** try to drop the required feature directly. Instead, first disable [IcebergCompatV1](/concepts/icebergcompatv1.md) on the table. Once IcebergCompatV1 is disabled, the table is no longer bound by the mandatory feature set, and you can then drop the feature if needed. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md:L9-L13]

The recommended workflow:

1. Disable IcebergCompatV1 on the table (e.g., by setting the appropriate table property).
2. After disabling, drop the desired table feature.
3. Re-enable IcebergCompatV1 only if still required and compatible with the remaining feature set.

Refer to the [IcebergCompatV1](/concepts/icebergcompatv1.md) documentation for the exact steps to enable or disable the mode.

## Related Concepts

- [IcebergCompatV1](/concepts/icebergcompatv1.md) — The Delta compatibility mode that enforces the feature requirements.
- DELTA_ICEBERG_COMPAT_V1_VIOLATION error class — The parent error class containing this sub-error.
- Delta table features — The protocol-level features that define a Delta table’s capabilities.
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) — The open table format that IcebergCompatV1 targets.
- ALTER TABLE DROP FEATURE — The Delta command that triggers this error when used with a required feature.
- DISABLING_REQUIRED_TABLE_FEATURE — This sub-error, covered on this page.

## Sources

- delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md (lines 1–13)

# Citations

1. delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md:L9-L13
2. delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md:L1-L13

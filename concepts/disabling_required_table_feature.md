---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 468966de27546ead34963ff658f581c41de7749b553bf9f5efbf9a8a9dd8a781
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - disabling_required_table_feature
    - DISABLING_REQUIRED_TABLE_FEATURE
  citations:
    - file: delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md
title: DISABLING_REQUIRED_TABLE_FEATURE
description: Error sub-type indicating a required table feature for IcebergCompatV1 cannot be dropped without first disabling IcebergCompatV1
tags:
  - error-messages
  - table-features
  - delta-lake
timestamp: "2026-06-19T18:24:59.004Z"
---

## DISABLING_REQUIRED_TABLE_FEATURE

**DISABLING_REQUIRED_TABLE_FEATURE** is a specific error subtype under the DELTA_ICEBERG_COMPAT_V1_VIOLATION error class in Databricks. It indicates that a user attempted to drop or disable a Table Features (Delta Lake)|table feature that is required for [IcebergCompatV1](/concepts/icebergcompatv1.md) to function correctly. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

### Cause

IcebergCompatV1 depends on certain Delta table features being both supported by the table format and enabled on the table. If a user executes an `ALTER TABLE ... DROP FEATURE` command or otherwise attempts to remove a required feature, the system raises this error. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

### Error Message

The error message includes a placeholder for the specific feature that cannot be dropped, for example:

```
IcebergCompatV1 requires feature <feature> to be supported and enabled. You cannot drop it from the table. Instead, please disable IcebergCompatV1 first.
```

### Solution

The error explicitly recommends the correct remediation: disable IcebergCompatV1 on the table before attempting to drop the required feature. Once IcebergCompatV1 is disabled, the feature can be dropped if desired. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

### Related Concepts

- DELTA_ICEBERG_COMPAT_V1_VIOLATION – The parent error class containing additional subtypes (e.g., `INCOMPATIBLE_TABLE_FEATURE`, `MISSING_REQUIRED_TABLE_FEATURE`).
- [IcebergCompatV1](/concepts/icebergcompatv1.md) – The compatibility mode that enforces these feature requirements.
- Table Features (Delta Lake) – Delta Lake's mechanism for tracking which capabilities a table uses.
- [Delta Lake](/concepts/delta-lake.md) – The underlying storage format.

### Sources

- delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md](/references/delta_iceberg_compat_v1_violation-error-class-databricks-on-aws-da04bc25.md)

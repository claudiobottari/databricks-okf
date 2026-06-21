---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bef7bcce3df5fc0c6d485459251aabcc51335d93ec0d869d14cef87ea3fe4936
  pageDirectory: concepts
  sources:
    - delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - missing_uniform_tbl_properties
    - MISSING_UNIFORM_TBL_PROPERTIES
  citations:
    - file: delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md
title: MISSING_UNIFORM_TBL_PROPERTIES
description: A sub-error of DELTA_UNIFORM_ICEBERG_INGRESS_VIOLATION indicating required Delta table properties (tableId, snapshotId, metadataLocation) are missing, possibly due to manual changes to the _delta_log.
tags:
  - databricks
  - error-messages
  - delta-uniform
  - table-properties
timestamp: "2026-06-19T15:08:30.191Z"
---

```yaml
---
title: MISSING_UNIFORM_TBL_PROPERTIES
summary: A sub-error of DELTA_UNIFORM_ICEBERG_INGRESS_VIOLATION indicating that required Delta table properties (tableId, snapshotId, metadataLocation) are missing from Delta table properties, possibly due to manual changes to _delta_log.
sources:
  - delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T10:09:02.596Z"
updatedAt: "2026-06-19T10:09:02.596Z"
tags:
  - error-message
  - databricks
  - table-properties
  - delta-log
aliases:
  - missing_uniform_tbl_properties
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# MISSING_UNIFORM_TBL_PROPERTIES

**MISSING_UNIFORM_TBL_PROPERTIES** is a specific error condition under the `DELTA_UNIFORM_ICEBERG_INGRESS_VIOLATION` error class (SQLSTATE: KD00E) in Databricks. It is raised when [[Delta Uniform]] attempts to read an [[Uniform (Apache Iceberg) Format|Apache Iceberg]] table but cannot find one or more required properties in the Delta table’s metadata. ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

## Error Message

When this error occurs, the following message is returned:

```
MISSING_UNIFORM_TBL_PROPERTIES: At least one of tableId <tableId>, snapshotId <snapshotId>, metadataLocation <location> is missing from Delta table properties; Is there manual change to the _delta_log?
```

The placeholders (`<tableId>`, `<snapshotId>`, `<location>`) are replaced with the actual identifiers that could not be found. ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

## Cause

The error occurs when at least one of the following Delta table properties is absent:

- `tableId` – a unique identifier for the table
- `snapshotId` – the identifier for the current snapshot
- `metadataLocation` – the path to the metadata location

The error message explicitly asks whether there has been a manual change to the `_delta_log`, suggesting that unintended modifications to the Delta transaction log are the most likely root cause. ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

## Related Error Conditions

This error is part of the DELTA_UNIFORM_ICEBERG_INGRESS_VIOLATION error class. A closely related condition is:

- MUST_REFRESH_SAME_TABLE – occurs when refreshing an existing Iceberg table with metadata from a different Iceberg table UUID.

## Related Concepts

- [[Delta Uniform]] – The feature enabling Iceberg compatibility on Delta tables.
- [[Uniform (Apache Iceberg) Format|Apache Iceberg]] – The open table format being read through Delta Uniform.
- _delta_log – The Delta transaction log that may have been manually altered.
- Table properties – Metadata properties stored in the Delta log.

## Sources

- delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md
```

# Citations

1. [delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md](/references/delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws-37d8ed72.md)

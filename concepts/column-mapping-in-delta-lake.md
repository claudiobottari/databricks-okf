---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cf5735eb4a26fc07e7616b3ca3d1fb2d2c513fb8b66817aa8294db041d5a6c7d
  pageDirectory: concepts
  sources:
    - delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - column-mapping-in-delta-lake
    - CMIDL
    - Column mapping in Delta
    - Column mapping
    - column mapping
  citations:
    - file: delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md
title: Column mapping in Delta Lake
description: A Delta Lake feature enabling column aliasing and rename without breaking existing data files, required for alias-based reconciliation queries.
tags:
  - delta-lake
  - schema-evolution
timestamp: "2026-06-19T18:24:49.897Z"
---

---  
title: Column Mapping in Delta Lake  
summary: A Delta Lake feature required for using column aliases in reconciliation queries with external metadata  
sources:  
  - delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md  
kind: concept  
createdAt: "2026-06-18T15:19:24.103Z"  
updatedAt: "2026-06-19T10:05:39.102Z"  
tags:  
  - databricks  
  - delta-lake  
  - schemas  
aliases:  
  - column-mapping-in-delta-lake  
  - CMIDL  
confidence: 0.99  
provenanceState: extracted  
inferredParagraphs: 0  
---

# Column Mapping in Delta Lake

**Column mapping** is a Delta Lake feature that must be enabled to use a column alias in a reconciliation query for [Delta Lake External Metadata](/concepts/delta-lake-external-metadata.md) operations. Without column mapping enabled, attempting such an alias fails with a specific error condition. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## Error Condition

The `DELTA_EXTERNAL_METADATA_UNSUPPORTED_SOURCE` error class includes a sub‑condition named `COLUMN_RENAME_WITHOUT_COLUMN_MAPPING`. This sub‑condition occurs when a reconciliation query uses a column alias but the target Delta table does not have column mapping enabled. The error message states: **Column mapping must be enabled to use an alias in the reconciliation query.** ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## Usage Context

Column mapping is a prerequisite for the [Delta Lake external metadata](https://docs.databricks.com/aws/en/error-messages/delta-external-metadata-unsupported-source-error-class) feature, which reconciles changes between Delta Lake and external systems. When external metadata reconciliation queries reference columns by alias, the underlying Delta table must have column mapping turned on; otherwise the `COLUMN_RENAME_WITHOUT_COLUMN_MAPPING` error is raised. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

The source material does not describe the mechanics of enabling column mapping (e.g., setting the `delta.columnMapping.mode` [Delta Lake table properties|table property](/concepts/delta-lake-table.md)), nor does it list other uses of column mapping such as column renaming.

## Related Concepts

- [Delta Lake External Metadata](/concepts/delta-lake-external-metadata.md) — The broader feature that triggers this error when column mapping is absent.
- [Delta Lake Reconciliation Queries](/concepts/delta-lake-reconciliation-queries.md) — Queries that compare or synchronize Delta table state with external systems.
- [Delta Lake table properties](/concepts/delta-lake-reader-table-features.md) — Including the `delta.columnMapping.mode` property that controls mapping mode.

## Sources

- delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md](/references/delta_external_metadata_unsupported_source-error-condition-databricks-on-aws-478fcc27.md)

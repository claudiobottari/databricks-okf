---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3d13c02a16a33a554e2d9b3b8c2cc118196bac69d87b4533b53bb9f046b24953
  pageDirectory: concepts
  sources:
    - delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - column-mask-cm-policies-in-delta-lake
    - CM(PIDL
  citations:
    - file: delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md
    - file: delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md
      start: 8
      end: 10
title: Column Mask (CM) policies in Delta Lake
description: A Delta table security feature that masks column values at query time, unsupported by external metadata sources.
tags:
  - delta-lake
  - security
  - data-governance
timestamp: "2026-06-19T18:24:44.622Z"
---

## Column Mask (CM) Policies in Delta Lake

**Column Mask (CM) policies** are a Delta Lake security feature that allows fine-grained control over column-level visibility at query time. However, when a table that has CM policies is used as a source for [External Metadata](/concepts/external-metadata-api.md), the operation fails with the `DELTA_EXTERNAL_METADATA_UNSUPPORTED_SOURCE` error. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

### Error Condition

The error is raised with SQLSTATE `0AKDC` and the following message:

```
COLUMN_MASK: <tableType> with Column Mask (CM) policies.
```

This indicates that External Metadata does not support reading from a table that has active column mask policies. Any attempt to use such a table in an External Metadata workload will be rejected. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md:8-10]

### Impact

The restriction applies regardless of the table type (`<tableType>` is a placeholder that can refer to any Delta table type). Only tables without CM policies, [Row-Level Security (RLS) Policies](/concepts/row-level-security-rls-policies.md), or unsupported projections can be used with External Metadata. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

### Workaround

To use a table that requires column-level protection in conjunction with External Metadata, you must remove the column mask policies from the table before using it as a source. Alternatively, avoid using External Metadata for such tables and rely on native Delta Lake query engines that do support column masks.

### Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The underlying storage format that supports column masks.
- [External Metadata](/concepts/external-metadata-api.md) — The Databricks feature that requires tables without CM policies.
- [Row-Level Security (RLS) Policies](/concepts/row-level-security-rls-policies.md) — Another security feature not supported by External Metadata.
- DELTA_EXTERNAL_METADATA_UNSUPPORTED_SOURCE — The broader error class covering unsupported source configurations.

### Sources

- delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md](/references/delta_external_metadata_unsupported_source-error-condition-databricks-on-aws-478fcc27.md)
2. [delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md:8-10](/references/delta_external_metadata_unsupported_source-error-condition-databricks-on-aws-478fcc27.md)

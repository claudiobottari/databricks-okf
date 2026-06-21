---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3be151026d4c9f3a6eeb3b9a7e11b7af0b5df5210622e62a9d5b5575dee7f2f7
  pageDirectory: concepts
  sources:
    - delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-column-mask-cm-policies
    - DLCM(P
  citations:
    - file: delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md
title: Delta Lake Column Mask (CM) Policies
description: A column-level security feature in Delta Lake that restricts visibility of sensitive columns, and is unsupported for external metadata operations.
tags:
  - delta-lake
  - security
  - column-level-security
timestamp: "2026-06-18T15:19:25.924Z"
---

# Delta Lake Column Mask (CM) Policies

**Delta Lake Column Mask (CM) Policies** are data security features that control how column values are presented to users at query time by applying masking functions to sensitive data. When a table has column mask policies defined, certain operations may not be supported by external metadata sources.

## Overview

Column Mask (CM) policies in Delta Lake allow organizations to implement dynamic data masking, where the underlying data remains intact in storage but masked values are returned to users based on policy rules. These policies are part of Delta Lake's broader security framework alongside [Row-Level Security (RLS) Policies](/concepts/row-level-security-rls-policies.md). ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## External Metadata Limitation

A key constraint exists when using column mask policies with external metadata systems: the `DELTA_EXTERNAL_METADATA_UNSUPPORTED_SOURCE` error condition indicates that external metadata sources do not support tables with Column Mask policies. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

### Error Condition

The specific error message for this scenario is:

```
COLUMN_MASK: <tableType> with Column Mask (CM) policies.
```

^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

This means that if a Delta table has column mask policies applied, external metadata systems cannot read or reconcile metadata from that table. The `<tableType>` placeholder indicates the specific type of table encountering the issue.

## Related Concepts

- [Row-Level Security (RLS) Policies](/concepts/row-level-security-rls-policies.md) — Another security feature with similar external metadata limitations
- [Column mapping in Delta Lake](/concepts/column-mapping-in-delta-lake.md) — A related feature that must be enabled for certain reconciliation operations
- External Metadata Support — The broader framework that determines which Delta Lake features are compatible with external metadata sources
- Delta Lake Security Features — The complete set of data protection mechanisms in Delta Lake

## Sources

- delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md](/references/delta_external_metadata_unsupported_source-error-condition-databricks-on-aws-478fcc27.md)

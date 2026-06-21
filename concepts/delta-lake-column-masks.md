---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 55ef5c3203d70d854dadcd507175667f349d3f796edac592be5c8d33ed64940c
  pageDirectory: concepts
  sources:
    - delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-column-masks
    - DLCM
    - column masks
  citations:
    - file: delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md
title: Delta Lake column masks
description: A Delta Lake table feature that restricts column visibility; incompatible with REFRESH SYNC UNIFORM.
tags:
  - databricks
  - delta-lake
  - security
timestamp: "2026-06-19T15:09:45.038Z"
---

# Delta Lake Column Masks

**Delta Lake column masks** are a security feature that allows you to apply masking rules to specific columns in a [Delta Lake](/concepts/delta-lake.md) table. When a column mask is defined, queries against the table automatically transform the masked column's values according to the masking policy, without modifying the underlying data.

## Overview

Column masks are a table-level feature that controls how column data is presented to query users. When a mask is applied to a column, any query that reads that column sees the masked version of the data rather than the raw values. This is implemented as part of Delta Lake's table features system, which tracks enabled capabilities on a per-table basis. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

## Compatibility Considerations

Column masks interact with other Delta Lake features in important ways. Notably, column masks are not supported by the `REFRESH` identifier `SYNC UNIFORM` operation. Attempting to use `REFRESH SYNC UNIFORM` on a table that has column masks defined will result in a `DELTA_UNIFORM_REFRESH_NOT_SUPPORTED` error with the `COLUMN_MASK` reason code. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

This limitation means that tables with column masks cannot be synchronized using the uniform refresh mechanism. If you need to use uniform refresh, you must remove column masks from the table first. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

## Related Features

Column masks share similar compatibility limitations with [row-level security](/concepts/row-level-security-rls-policies.md) features. Both are reader-level security controls that transform data at query time, and neither is supported by the `REFRESH SYNC UNIFORM` operation. Other unsupported reader features are also collectively identified by the `UNSUPPORTED_READER_FEATURES` error subtype. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

## Error Handling

When attempting operations that are incompatible with column masks, the system returns the `DELTA_UNIFORM_REFRESH_NOT_SUPPORTED` error class. The specific subtype `COLUMN_MASK` indicates that a column mask is preventing the operation. The full error message provides context about which column mask is causing the issue. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

## Related Concepts

- Delta Lake security features – Overview of security controls available in Delta Lake
- [Row-level security](/concepts/row-level-security-rls-policies.md) – Related security feature that filters rows rather than masking columns
- Table features in Delta Lake – System for tracking enabled capabilities on tables
- [Delta Lake uniform refresh](/concepts/delta-uniform-refresh.md) – Feature for synchronizing Delta tables with external formats
- Data masking strategies – Broader approaches to protecting sensitive data

## Sources

- delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md](/references/delta_uniform_refresh_not_supported-error-condition-databricks-on-aws-9dd3f333.md)

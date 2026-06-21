---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 74b90931a336d3e21b410f37aa39c3584a10c0b579e67dfb9d7a663880db111d
  pageDirectory: concepts
  sources:
    - delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - row-level-security-with-delta-uniform
    - RSWDU
    - Row filters with Delta Uniform
  citations:
    - file: delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md
title: Row-level security with Delta Uniform
description: Row-level security features on Delta tables prevent REFRESH SYNC UNIFORM from succeeding
tags:
  - databricks
  - delta-uniform
  - row-level-security
timestamp: "2026-06-19T18:28:16.073Z"
---

# Row-level Security with Delta Uniform

**Row-level security** is a [Delta Lake Table](/concepts/delta-lake-table.md) feature that restricts which rows a user can read based on a filter condition. When a Delta table has row-level security enabled, the `REFRESH SYNC UNIFORM` operation — which synchronizes the table’s [Uniform](/concepts/delta-uniform.md) format metadata — cannot be executed. The system returns a `DELTA_UNIFORM_REFRESH_NOT_SUPPORTED` error with the reason `ROW_LEVEL_SECURITY`. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

## Error Behavior

Attempting to run `REFRESH SYNC UNIFORM` on a table that has row-level security enabled produces the following error condition:

```
DELTA_UNIFORM_REFRESH_NOT_SUPPORTED: Row level security is not supported by REFRESH identifier SYNC UNIFORM.
```

^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

## Context

The `DELTA_UNIFORM_REFRESH_NOT_SUPPORTED` error class covers multiple incompatibilities between [Delta Lake](/concepts/delta-lake.md) table features and the `REFRESH SYNC UNIFORM` command. Row-level security is one of several features that block the refresh operation. Other blocked features include Column Masking, missing compatibility settings (`COMPATIBILITY_NOT_ENABLED`), unsupported reader features, and unsupported source types. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

## Workaround

To use `REFRESH SYNC UNIFORM` on a table that requires row-level security, you must first remove the row-level security filter from the table. If the security requirement is permanent, [Delta Uniform](/concepts/delta-uniform.md) refresh cannot be applied; consider alternative methods for making the table readable by non-Delta clients.

## Related Concepts

- [Delta Uniform](/concepts/delta-uniform.md) — The Universal Format (UniForm) feature that allows Delta tables to be read by Iceberg or Hudi clients.
- [REFRESH SYNC UNIFORM](/concepts/refresh-sync-uniform.md) — The SQL command that refreshes Uniform metadata for a Delta table.
- [Row-Level Security](/concepts/row-level-security-rls-policies.md) — A [Delta Lake Table](/concepts/delta-lake-table.md) feature that enforces per-row access controls.
- Column Masking — Another table feature that is incompatible with `REFRESH SYNC UNIFORM`.

## Sources

- delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md](/references/delta_uniform_refresh_not_supported-error-condition-databricks-on-aws-9dd3f333.md)

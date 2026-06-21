---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 00492603164b47ecbfa5b87d3b3176cb088343192fd5cd7fbe9cd26f8a16e362
  pageDirectory: concepts
  sources:
    - delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-row-level-security
    - DLRS
  citations:
    - file: delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md
title: Delta Lake row-level security
description: A Delta Lake table feature that restricts row visibility; incompatible with REFRESH SYNC UNIFORM.
tags:
  - databricks
  - delta-lake
  - security
timestamp: "2026-06-19T15:09:18.056Z"
---

# Delta Lake Row-Level Security

**Delta Lake row-level security** is a [Delta Lake](/concepts/delta-lake.md) feature that restricts which rows a user can access in a table. On Databricks, row-level security is implemented through column masks or row filters.

## Interaction with Uniform Refresh

Row-level security is not supported by the `REFRESH` identifier `SYNC UNIFORM` operation. Attempting to run `REFRESH SYNC UNIFORM` on a table that has row-level security enabled will result in a `DELTA_UNIFORM_REFRESH_NOT_SUPPORTED` error with the reason `ROW_LEVEL_SECURITY`. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

## Related Concepts

- DELTA_UNIFORM_REFRESH_NOT_SUPPORTED error class|DELTA_UNIFORM_REFRESH_NOT_SUPPORTED error condition – the error class that reports this limitation.
- SYNC UNIFORM – the refresh identifier that cannot be used with row-level security.
- [Column masks](/concepts/column-mask-policies.md) – one mechanism to enforce row-level security.
- [Delta Lake](/concepts/delta-lake.md) – the open‑source storage layer that provides row‑level security.

## Sources

- delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md](/references/delta_uniform_refresh_not_supported-error-condition-databricks-on-aws-9dd3f333.md)

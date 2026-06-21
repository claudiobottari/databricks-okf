---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 08892d0fde3d9a56fe39e9978b268e93291286b3aa02cfeb762c2ce2f89e431e
  pageDirectory: concepts
  sources:
    - delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - deltauniversalformatenabledformats-configuration
    - Delta Universal Format (Uniform) Configuration
  citations:
    - file: delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md
title: delta.universalFormat.enabledFormats configuration
description: A Spark configuration that controls which UniForm formats (Iceberg, Hudi) are enabled for a Delta table.
tags:
  - databricks
  - configuration
  - delta-lake
timestamp: "2026-06-19T15:09:14.658Z"
---

```markdown
---
title: "`delta.universalFormat.enabledFormats` Configuration"
summary: A Databricks Spark configuration that controls which UniForm protocols (e.g., `delta.uniform`) are enabled for a table.
sources:
  - delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T20:30:00.000Z"
updatedAt: "2026-06-19T20:30:00.000Z"
tags:
  - databricks
  - configuration
  - delta-lake
aliases:
  - delta.universalFormat.enabledFormats
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# `delta.universalFormat.enabledFormats` Configuration

The **`delta.universalFormat.enabledFormats`** configuration specifies which output formats are enabled when writing Delta tables using the [[Delta Universal Format (UniForm)]] feature. This configuration is required for UniForm to generate metadata in other formats, such as Apache Iceberg, alongside the Delta log. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

## Purpose

UniForm allows Delta tables to be readable by other table formats by generating additional metadata files. The `delta.universalFormat.enabledFormats` configuration determines which formats are actively generated during writes. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

## Required Value for SYNC UNIFORM

For the `REFRESH SYNC UNIFORM` operation to succeed, the configuration must include the value `"compatibility"` in the `enabledFormats` list. If `compatibility` is not present, the operation fails with the `COMPATIBILITY_NOT_ENABLED` error condition. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

The error message states:

> `REFRESH` identifier `SYNC UNIFORM` requires compatibility to be included in delta.universalFormat.enabledFormats. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

## Error Condition

When `compatibility` is missing from the enabled formats, the `DELTA_UNIFORM_REFRESH_NOT_SUPPORTED` error class is raised with `COMPATIBILITY_NOT_ENABLED` as the sub-reason. This error blocks the synchronization of UniForm metadata for the table. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

## Configuration Details

The `delta.universalFormat.enabledFormats` configuration is typically set as a table property on Delta tables. The only documented value for this configuration in the source material is `"compatibility"`. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

## Related Concepts

- [[Delta Universal Format (UniForm)]] — The feature that enables multi-format table access
- [[REFRESH SYNC UNIFORM]] — The command that synchronizes UniForm metadata
- COMPATIBILITY_NOT_ENABLED error — The specific error when compatibility is not configured
- [[Delta Lake Reader Table Features|Delta Lake table properties]] — The broader set of Delta-specific configurations

## Sources

- delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md
```

# Citations

1. [delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md](/references/delta_uniform_refresh_not_supported-error-condition-databricks-on-aws-9dd3f333.md)

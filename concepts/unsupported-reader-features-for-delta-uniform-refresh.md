---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e2a17e5180dafbb97e081b615190c19c5c04e768d44dc4b3b055fa6a7cc3d69a
  pageDirectory: concepts
  sources:
    - delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unsupported-reader-features-for-delta-uniform-refresh
    - URFFDUR
    - UNSUPPORTED_READER_FEATURES
  citations:
    - file: delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md
title: Unsupported reader features for Delta Uniform refresh
description: Some reader table features are incompatible with REFRESH SYNC UNIFORM and cause the UNSUPPORTED_READER_FEATURES sub-error
tags:
  - databricks
  - delta-uniform
  - reader-features
timestamp: "2026-06-19T18:28:19.472Z"
---

# Unsupported Reader Features for Delta Uniform Refresh

**Unsupported reader features for Delta Uniform refresh** is a specific error condition under the DELTA_UNIFORM_REFRESH_NOT_SUPPORTED error class|DELTA_UNIFORM_REFRESH_NOT_SUPPORTED error class. It occurs when a Delta table uses one or more reader table features that are incompatible with the `REFRESH SYNC UNIFORM` command. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

## Error Message

When this error is triggered, Databricks returns the following message:

```
The reader table feature(s) <readerFeatures> are not supported by REFRESH identifier SYNC UNIFORM.
```

Where `<readerFeatures>` lists the incompatible reader features found on the table. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

## Cause

The `REFRESH SYNC UNIFORM` command is used to synchronize a Delta table’s metadata with its [Delta Uniform](/concepts/delta-uniform.md) representation (e.g., Apache Iceberg or Apache Hudi). Certain Delta reader table features, such as [Column Mapping](/concepts/delta-table-column-mapping.md) or [Deletion Vectors](/concepts/deletion-vectors.md), are not yet supported by the UniForm reader and therefore prevent the refresh operation from succeeding. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

## Resolution

To resolve this error, you must identify which reader features are causing the incompatibility and take one of the following actions:

- Remove the unsupported reader feature from the table (if possible).
- Consider an alternative method to convert the table to UniForm without using `REFRESH SYNC UNIFORM`.

Consult the [Delta UniForm documentation](/concepts/delta-uniform-uniform.md) for the current list of supported reader features. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Uniform](/concepts/delta-uniform.md)
- [REFRESH SYNC UNIFORM](/concepts/refresh-sync-uniform.md)
- [Delta table reader features](/concepts/delta-lake-reader-table-features.md)
- [Column Mapping](/concepts/delta-table-column-mapping.md)
- [Deletion Vectors](/concepts/deletion-vectors.md)
- DELTA_UNIFORM_REFRESH_NOT_SUPPORTED error class|DELTA_UNIFORM_REFRESH_NOT_SUPPORTED (parent error class)

## Sources

- delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md](/references/delta_uniform_refresh_not_supported-error-condition-databricks-on-aws-9dd3f333.md)

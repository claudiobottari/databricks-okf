---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 63d65f49e033860b59030ecc54cc1f1cb26a3b2660e49c87b4eed91c5287a5e6
  pageDirectory: concepts
  sources:
    - delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - delta-lake-reader-table-features
    - DLRTF
    - Delta Lake Table Features
    - Delta Lake table features
    - Delta reader table features
    - Delta Lake Table Features|table feature
    - Delta Lake table properties
    - Delta table reader features
    - Reader Table Features
    - reader table features
  citations:
    - file: delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md
title: Delta Lake Reader Table Features
description: Extensibility features in Delta Lake that affect how a table is read, and can cause incompatibility with UniForm metadata refresh.
tags:
  - delta-lake
  - table-features
  - compatibility
timestamp: "2026-06-19T10:10:13.086Z"
---

```markdown
---
title: Delta Lake Reader Table Features
summary: The set of Delta Lake protocol features that reader engines must support. When a Delta table uses reader features not supported by the Iceberg format, the `SYNC UNIFORM` operation fails with the `UNSUPPORTED_READER_FEATURES` error.
sources:
  - delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T15:00:00.000Z"
updatedAt: "2026-06-18T15:00:00.000Z"
tags:
  - delta-lake
  - delta-table
  - uniform
  - reader-features
aliases:
  - reader-table-features
  - delta-reader-table-features
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 1
---

# Delta Lake Reader Table Features

**Delta Lake Reader Table Features** are a class of capabilities in the [[Delta Lake]] protocol that a table can declare. Reader features are listed in table metadata to indicate what readers must understand to correctly interpret the stored data. The concept appears in the DELTA_UNIFORM_REFRESH_NOT_SUPPORTED error class, specifically when using the SYNC UNIFORM command to synchronise [[Uniform (Apache Iceberg) Format|Uniform (Iceberg)]] metadata. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

## Interaction with SYNC UNIFORM

When a Delta table has reader features enabled that are not supported by the Iceberg format, the `REFRESH` identifier `SYNC UNIFORM` command fails with the sub-error `UNSUPPORTED_READER_FEATURES`. The error message is:

> The reader table feature(s) `<readerFeatures>` are not supported by `REFRESH` identifier `SYNC UNIFORM`. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

The exact reader features that cause this condition are listed in the error placeholder `<readerFeatures>`. This error prevents the Uniform metadata synchronisation from completing.

## Related Concepts

- [[Delta Lake Table Protocol Changes|Delta Table Protocol]] – The versioning and feature flag system of Delta Lake.
- [[Uniform (Apache Iceberg) Format|Uniform (Iceberg)]] – Feature that exposes a Delta table as an Iceberg table.
- SYNC UNIFORM – Command to refresh Uniform metadata.
- DELTA_UNIFORM_REFRESH_NOT_SUPPORTED error class – Error class containing `UNSUPPORTED_READER_FEATURES`.

## Sources

- delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md
```

# Citations

1. [delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md](/references/delta_uniform_refresh_not_supported-error-condition-databricks-on-aws-9dd3f333.md)

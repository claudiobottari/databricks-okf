---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fb09615e2c13758e782f6e64c30d22e3000b22e42610eadddc961468227904b6
  pageDirectory: concepts
  sources:
    - delta_clone_incompatible_source-error-condition-databricks-on-aws.md
  confidence: 0.7
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - delta-clone
    - DELTA_CLONE
    - Delta CLONE command
    - Delta Lake CLONE
    - Delta Lake Clone
    - Delta Lake clone
    - delta-clone-databricks
    - DC(
  citations:
    - file: delta_clone_incompatible_source-error-condition-databricks-on-aws.md
title: Delta Clone
description: A Databricks operation to clone an existing table (including Iceberg or other formats) into a Delta table, with specific compatibility constraints.
tags:
  - delta-lake
  - databricks
  - cloning
  - etl
timestamp: "2026-06-19T10:02:37.621Z"
---

Here is the wiki page for "Delta Clone", written based solely on the provided source material.

***

## Delta Clone

**Delta Clone** is an operation that creates a copy of a source table using the Delta Lake format. While the source table may be in a valid format, the clone operation requires the source to be compatible with the Delta Lake protocol and features. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

## Error Conditions

When a source table is in a valid format but has features unsupported by Delta Lake, the DELTA_CLONE_INCOMPATIBLE_SOURCE error condition may occur. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

### HAS_INDEXES

This error occurs when the source table `<tableName>` has indexes `<indexNames>`. The indexes must be dropped before the clone operation can proceed. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

### ICEBERG_MISSING_PARTITION_SPECS

This error occurs when the source [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) table has no partition specs in the table. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

### ICEBERG_UNDERGONE_PARTITION_EVOLUTION

This error occurs when the source [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) table has undergone partition evolution. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md)
- DELTA_CLONE_INCOMPATIBLE_SOURCE
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md)

## Sources

- delta_clone_incompatible_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_clone_incompatible_source-error-condition-databricks-on-aws.md](/references/delta_clone_incompatible_source-error-condition-databricks-on-aws-b63ca67d.md)

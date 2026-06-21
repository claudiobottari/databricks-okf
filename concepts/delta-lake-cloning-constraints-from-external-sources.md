---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a648a01ee6fd2c41431666b39f118058ea6cf511714a5cc11c27701914df48c6
  pageDirectory: concepts
  sources:
    - delta_clone_incompatible_source-error-condition-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - delta-lake-cloning-constraints-from-external-sources
    - DLCCFES
  citations:
    - file: delta_clone_incompatible_source-error-condition-databricks-on-aws.md
title: Delta Lake Cloning Constraints from External Sources
description: The concept that Delta Lake imposes specific compatibility constraints when cloning from external table formats like Iceberg or tables with database indexes, requiring certain conditions to be met.
tags:
  - databricks
  - delta-lake
  - cloning
  - compatibility
timestamp: "2026-06-19T18:22:27.214Z"
---

Here is the wiki page for "Delta Lake Cloning Constraints from External Sources", based solely on the provided source material.

---

## Delta Lake Cloning Constraints from External Sources

**Delta Lake Cloning Constraints from External Sources** refers to specific conditions that prevent a [CLONE](/concepts/deep-clone.md) operation from completing when the source data originates from a non-Delta format, even if that source is valid. The DELTA_CLONE_INCOMPATIBLE_SOURCE error condition signals that the source has a recognized format but includes features that are unsupported by Delta Lake's clone functionality. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

### Source Constraints

When cloning from a table that has indexes defined, Delta Lake raises the following error:

**`HAS_INDEXES`**: `Table <tableName> has indexes: <indexNames>. Drop the indexes before cloning.`

This constraint requires that all indexes on the source table be removed before the clone operation can proceed. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

### Apache Iceberg Constraints

When cloning from an [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) source, Delta Lake enforces two specific constraints:

- **`ICEBERG_MISSING_PARTITION_SPECS`**: The source Apache Iceberg table has no partition specs in the table. Delta Lake requires partition specifications to be present in the source table. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

- **`ICEBERG_UNDERGONE_PARTITION_EVOLUTION`**: The source Apache Iceberg table has undergone partition evolution. Delta Lake does not support cloning from Iceberg tables that have changed their partitioning scheme over time. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

### Related Concepts

- DELTA_CLONE_INCOMPATIBLE_SOURCE Error|DELTA_CLONE_INCOMPATIBLE_SOURCE error condition — The error class raised when clone constraints are violated.
- [CLONE](/concepts/deep-clone.md) — The Delta Lake operation for creating a copy of a table.
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) — A table format that may serve as a clone source but has specific constraints.
- [Delta Lake](/concepts/delta-lake.md) — The underlying storage format for the clone target.

### Sources

- delta_clone_incompatible_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_clone_incompatible_source-error-condition-databricks-on-aws.md](/references/delta_clone_incompatible_source-error-condition-databricks-on-aws-b63ca67d.md)

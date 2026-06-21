---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ae4cb3645c8ae05166f15c4c7d3b367cbae01aeba300cd986536e6dc7bcf7466
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deletion-vectors-in-delta-iceberg-compatibility
    - DVIDC
  citations:
    - file: delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
title: Deletion Vectors in Delta-Iceberg Compatibility
description: Deletion Vectors must be purged or disabled before enabling IcebergCompatV on a Delta table, as they are incompatible with the Iceberg read protocol.
tags:
  - delta-lake
  - apache-iceberg
  - deletion-vectors
  - compatibility
timestamp: "2026-06-18T15:20:12.451Z"
---

---
title: Deletion Vectors in Delta-Iceberg Compatibility
summary: Deletion Vectors are a Delta Lake feature that must be disabled and purged before enabling IcebergCompatV<version> on a table. The `DELTΑ_ICEBERG_COMPAT_VIOLATION` error class includes two sub‑errors that guide the required cleanup steps.
sources:
  - delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
kind: concept
createdAt: 2026-06-18T08:07:24.485Z
tags:
  - delta-lake
  - iceberg-compat
  - deletion-vectors
  - uniform
aliases:
  - deletion-vectors-in-delta-iceberg-compatibility
  - DVDIC
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Deletion Vectors in Delta-Iceberg Compatibility

**Deletion Vectors** are a [Delta Lake Table](/concepts/delta-lake-table.md) feature used to optimize merge, update, and delete operations. When a table uses [Deletion Vectors](/concepts/deletion-vectors.md), metadata (deletion vectors) tracks which rows have been logically removed, avoiding physical data rewrites. However, this feature is incompatible with IcebergCompat (Uniform Iceberg) because Apache Iceberg does not natively support the Delta Lake deletion vector mechanism. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Error Conditions

When trying to enable IcebergCompatV`<version>` on a table that uses Deletion Vectors, Databricks raises a `DELTA_ICEBERG_COMPAT_VIOLATION` error with one of two sub‑conditions:

| Sub‑condition | Message | Action required |
|---------------|---------|-----------------|
| `DELETION_VECTORS_NOT_PURGED` | IcebergCompatV`<version>` requires Deletion Vectors to be completely purged from the table. | Run `REORG TABLE APPLY (PURGE)`. |
| `DELETION_VECTORS_SHOULD_BE_DISABLED` | IcebergCompatV`<version>` requires Deletion Vectors to be disabled on the table first. Then run `REORG PURGE` command to purge the Deletion Vectors on the table. | Disable Deletion Vectors on the table, then run `REORG TABLE APPLY (PURGE)`. |

^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Resolution Steps

The appropriate command depends on the current state of Deletion Vectors on the table:

1. **If Deletion Vectors are already enabled but not yet disabled:**  
   The error `DELETION_VECTORS_SHOULD_BE_DISABLED` indicates that Deletion Vectors must be **disabled first**. After disabling the feature, run `REORG TABLE APPLY (PURGE)` to physically remove all remaining deletion‑vector tracking data.

2. **If Deletion Vectors have already been disabled but residual metadata remains:**  
   The error `DELETION_VECTORS_NOT_PURGED` indicates that the table still contains leftover deletion‑vector metadata that needs to be cleaned. Running `REORG TABLE APPLY (PURGE)` is sufficient.

After purging, you can then enable IcebergCompat on the table (e.g., via `REORG TABLE APPLY (UPGRADE UNIFORM ...)`).

## Related Concepts

- [Deletion Vectors](/concepts/deletion-vectors.md) – The Delta Lake feature that tracks logical row deletions.
- IcebergCompat – The compatibility mode that enables Delta tables to be read by Apache Iceberg readers.
- [REORG TABLE](/concepts/reorg-table.md) – The command used to rewrite table data and purge obsolete metadata.
- [Uniform](/concepts/delta-uniform.md) – Databricks’ feature for making Delta tables interoperable with Apache Iceberg and Delta Sharing.
- DELTA_ICEBERG_COMPAT_V1_VIOLATION|DELTA_ICEBERG_COMPAT_VIOLATION – The error class that captures all Iceberg compatibility validation failures.

## Sources

- delta_iceberg_compat_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_violation-error-condition-databricks-on-aws.md](/references/delta_iceberg_compat_violation-error-condition-databricks-on-aws-206a4feb.md)

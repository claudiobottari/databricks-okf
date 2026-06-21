---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ef97ed646f634175a1e9e99cb68aad9313484ff3256cef211c99845b72cbd7ac
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deletion-vectors-and-icebergcompat-conflict
    - IcebergCompat conflict and Deletion Vectors
    - DVAIC
  citations:
    - file: delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
title: Deletion Vectors and IcebergCompat conflict
description: IcebergCompatV requires Deletion Vectors to be either disabled or completely purged from a Delta table before enabling Iceberg compatibility, with specific REORG TABLE APPLY (PURGE) commands needed.
tags:
  - delta-lake
  - deletion-vectors
  - iceberg
  - compatibility
timestamp: "2026-06-19T18:25:36.961Z"
---

# Deletion Vectors and IcebergCompat conflict

The **deletion vectors and IcebergCompat conflict** occurs when attempting to enable or upgrade IcebergCompat (e.g., IcebergCompatV1, IcebergCompatV2) on a [Delta Lake](/concepts/delta-lake.md) table that has active or residual [Deletion Vectors](/concepts/deletion-vectors.md). IcebergCompat requires that deletion vectors be completely removed from the table before the compatibility mode can be activated. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Error Subconditions

The `DELTA_ICEBERG_COMPAT_VIOLATION` error class includes two subconditions related to deletion vectors:

### DELETION_VECTORS_SHOULD_BE_DISABLED

This error is raised when the table currently has deletion vectors **enabled**. IcebergCompat requires deletion vectors to be disabled first. The error message reads: "IcebergCompatV`<version>` requires Deletion Vectors to be disabled on the table first. Then run `REORG PURGE` command to purge the Deletion Vectors on the table." ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### DELETION_VECTORS_NOT_PURGED

This error is raised when deletion vectors have already been disabled on the table, but residual deletion vector data still exists (i.e., they have not been physically purged). IcebergCompat requires that deletion vectors be **completely purged** from the table. The error message reads: "IcebergCompatV`<version>` requires Deletion Vectors to be completely purged from the table. Please run the `REORG TABLE APPLY (PURGE)` command." ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Resolution

To resolve either error, follow these steps in order:

1. **Disable deletion vectors** on the table if they are currently enabled (this resolves the `DELETION_VECTORS_SHOULD_BE_DISABLED` subcondition).
2. **Purging deletion vectors**: Run `REORG TABLE APPLY (PURGE)` to physically remove all deletion vector files from the table (this resolves the `DELETION_VECTORS_NOT_PURGED` subcondition).
3. After purging is complete, re-attempt the operation that enables or upgrades IcebergCompat.

If the table has deletion vectors enabled, both conditions must be addressed sequentially. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Applicability

This conflict applies to all IcebergCompat versions currently supported (V1, V2, etc.). The error messages refer to the specific version being enabled (`IcebergCompatV<version>`). The resolution is version-agnostic. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Related Concepts

- [Deletion Vectors](/concepts/deletion-vectors.md) – A Delta Lake feature for soft deletions and updates.
- IcebergCompat – Compatibility modes that allow Delta tables to be read by Apache Iceberg clients.
- [REORG TABLE](/concepts/reorg-table.md) – The command used to purge deletion vectors and upgrade Uniform compatibility.
- [Uniform Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) – The broader feature enabling Iceberg reading of Delta tables.
- DELTA_ICEBERG_COMPAT_VIOLATION error class – The parent error class containing all IcebergCompat validation failures.

## Sources

- delta_iceberg_compat_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_violation-error-condition-databricks-on-aws.md](/references/delta_iceberg_compat_violation-error-condition-databricks-on-aws-206a4feb.md)

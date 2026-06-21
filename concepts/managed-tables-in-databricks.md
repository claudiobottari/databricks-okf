---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 18c2ab138c0128dc68793a6ff720f8f3e1a3ce7b02aa402779717eff486ff246
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - managed-tables-in-databricks
    - MTID
    - Managed Iceberg Tables on Databricks
    - Managed Tables
    - Managed Tables | managed table
    - Managed Tables|managed table
    - Managed Tables|managed tables
    - Managed Table|managed
    - Managed table (Delta Lake)
    - Managed tables
    - Managed vs External Tables in Databricks
    - managed tables
  citations:
    - file: delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
title: Managed Tables in Databricks
description: A table type requirement for enabling IcebergCompatV; the feature can only be enabled on managed tables, not external or unmanaged tables.
tags:
  - delta-lake
  - databricks
  - table-types
timestamp: "2026-06-19T15:05:57.898Z"
---

# Managed Tables in Databricks

**Managed Tables in Databricks** are tables where Databricks manages both the metadata and the underlying data files. When a managed table is created, Databricks takes full ownership of the data lifecycle, including storage location and cleanup.

## Overview

Managed tables are stored in the Databricks [Metastore](/concepts/metastore.md), and their data files are managed entirely by Databricks. Unlike external tables, where you manage the underlying data location and retention, managed tables store data within the Databricks-managed storage location, typically in the workspace's root S3 bucket (on AWS), Azure Data Lake Storage Gen2 container, or Google Cloud Storage bucket, depending on the cloud provider.^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Key Characteristics

- **Full lifecycle management**: Databricks controls the data location, file format, and cleanup. Dropping a managed table deletes both the metadata and the underlying data files.
- **No external dependencies**: The table does not rely on external storage paths that you must maintain separately.
- **Self-contained**: All table data resides in Databricks-controlled storage, simplifying governance and data lifecycle policies.

## Relationship with Uniform and IcebergCompat

Managed tables are required for enabling certain advanced table features, such as [Uniform](/concepts/delta-uniform.md) (UniForm) with [IcebergCompatV2](/concepts/icebergcompatv2.md). The `ICEBERG_COMPAT_VIOLATION` error condition includes the `REQUIRE_MANAGED_TABLE` subcondition, which explicitly states: "The feature can be enabled only on Managed Tables."^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

This means that if you attempt to enable IcebergCompatV2 or other Uniform features on an external table, Databricks will reject the operation with a `DELTA_ICEBERG_COMPAT_VIOLATION` error, specifically the `REQUIRE_MANAGED_TABLE` variant.^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Error When Using Non-Managed Tables

The `DELTA_ICEBERG_COMPAT_VIOLATION` error message for the `REQUIRE_MANAGED_TABLE` subcondition is:

```
The feature can be enabled only on Managed Tables.
```

^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

This error occurs when you try to enable a feature (such as IcebergCompat) that requires managed table ownership on a table that is externally managed. To resolve this, you must either:
1. Create the table as a managed table before enabling the feature.
2. Convert the external table to a managed table.

## When to Use Managed Tables

Managed tables are the recommended choice for most Databricks workloads because:
- They simplify data management by automating file cleanup and storage location.
- They are required for advanced features like [Uniform (UniForm)](/concepts/delta-uniform.md) and Apache Iceberg compatibility.
- They integrate seamlessly with [Delta Lake](/concepts/delta-lake.md) table features.

However, external tables may be preferred when you need to share data across multiple systems or maintain data in a specific location outside Databricks control.

## Limitations

- Managed tables cannot be directly shared with external systems outside Databricks unless you use [Delta Sharing](/concepts/delta-sharing.md).
- The underlying data is stored in Databricks-managed storage, which may not be directly accessible from other tools without proper permissions.
- Changing a managed table to an external table requires data migration or recreation.

## Related Concepts

- External Tables in Databricks – Tables where you manage the underlying data location.
- [IcebergCompatV2](/concepts/icebergcompatv2.md) – A Uniform compatibility version that requires managed tables.
- [Uniform (UniForm)](/concepts/delta-uniform.md) – Feature enabling Apache Iceberg reader compatibility.
- DELTA_ICEBERG_COMPAT_V1_VIOLATION|DELTA_ICEBERG_COMPAT_VIOLATION – Error class covering managed table requirements.
- [Delta Lake](/concepts/delta-lake.md) – The underlying storage format for managed tables.
- Databricks Metastore – The metadata catalog for managed and external tables.

## Sources

- delta_iceberg_compat_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_violation-error-condition-databricks-on-aws.md](/references/delta_iceberg_compat_violation-error-condition-databricks-on-aws-206a4feb.md)

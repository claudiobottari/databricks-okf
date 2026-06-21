---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c1012f168ba9981da73fb75841cfa287e0a6fc067beffae43ef73408bda29c06
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - managed-table-requirement-for-uniform-iceberg
    - MTRFUI
  citations:
    - file: delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
title: Managed table requirement for Uniform Iceberg
description: The IcebergCompatV feature can only be enabled on Managed Tables in Databricks, not on external or unmanaged tables.
tags:
  - delta-lake
  - iceberg-compatibility
  - table-types
timestamp: "2026-06-19T10:06:09.556Z"
---

---  
title: Managed table requirement for Uniform Iceberg  
summary: Uniform Iceberg (IcebergCompatV1/V2) can only be enabled on managed tables in Databricks; attempting to enable it on an external table raises the `REQUIRE_MANAGED_TABLE` error.  
sources:  
  - delta_iceberg_compat_violation-error-condition-databricks-on-aws.md  
kind: concept  
createdAt: "2026-06-19T09:30:00.000Z"  
updatedAt: "2026-06-19T09:30:00.000Z"  
tags:  
  - uniform-iceberg  
  - managed-tables  
  - error-messages  
  - delta-lake  
aliases:  
  - managed-table-requirement-for-uniform-iceberg  
  - MTRUI  
confidence: 1  
provenanceState: extracted  
inferredParagraphs: 0  
---

# Managed table requirement for Uniform Iceberg

**Uniform Iceberg** (also referred to as the IcebergCompatV1 or IcebergCompatV2 table feature) can only be enabled on [Managed Table|managed tables](/concepts/unity-catalog-managed-tables.md) in Databricks. Attempting to enable Uniform Iceberg on an external (unmanaged) table results in a `DELTA_ICEBERG_COMPAT_VIOLATION` error with the sub‑condition `REQUIRE_MANAGED_TABLE`. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Error message

When the error occurs, Databricks returns:

```
The feature can be enabled only on Managed Tables.
```

This is the sole description provided for the `REQUIRE_MANAGED_TABLE` sub‑condition of the `DELTA_ICEBERG_COMPAT_VIOLATION` error class. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Cause

Uniform Iceberg relies on the Delta Lake transaction log to generate Iceberg metadata, and this integration is supported only for tables whose data is fully managed by Databricks (i.e., managed tables). External tables, where Databricks does not control the data lifecycle, cannot be converted to Uniform format. The feature is intentionally restricted to managed tables.

## Resolution

To enable Uniform Iceberg, ensure the target table is a managed table. If you need to use an external table, you must first convert it to a managed table (for example, by creating a new managed table and copying the data into it) before applying the IcebergCompat upgrade.

## Related concepts

- [Uniform Iceberg](/concepts/uniform-apache-iceberg-format.md) – Overview of the Databricks feature that makes Delta tables readable as Apache Iceberg tables.
- [IcebergCompatV1](/concepts/icebergcompatv1.md) / [IcebergCompatV2](/concepts/icebergcompatv2.md) – The specific table features that enable Uniform Iceberg.
- [Managed Table](/concepts/unity-catalog-managed-tables.md) – A table whose data is stored in the Databricks file system and whose lifecycle is managed by the [Metastore](/concepts/metastore.md).
- External Table – A table whose data is stored outside the Databricks file system and is not managed by the [Metastore](/concepts/metastore.md).
- DELTA_ICEBERG_COMPAT_VIOLATION error class – The parent error class containing all sub‑conditions for Iceberg compatibility failures.

## Sources

- delta_iceberg_compat_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_violation-error-condition-databricks-on-aws.md](/references/delta_iceberg_compat_violation-error-condition-databricks-on-aws-206a4feb.md)

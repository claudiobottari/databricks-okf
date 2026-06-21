---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0427bd3f74ba2c37f62c049e5549534b1a96875440003201e28cbfb47f82b1ca
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - managed-tables-requirement-for-icebergcompat
    - MTRFI
    - managed-table-requirement-for-uniform-iceberg
    - MTRFUI
  citations:
    - file: delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
title: Managed Tables requirement for IcebergCompat
description: IcebergCompatV can only be enabled on managed Delta tables, not external or unmanaged tables.
tags:
  - delta-lake
  - table-types
  - databricks
timestamp: "2026-06-18T11:54:06.283Z"
---

# Managed Tables requirement for IcebergCompat

The **Managed Tables requirement for IcebergCompat** is a prerequisite enforced by Delta Lake when enabling Unified Iceberg ([Uniform](/concepts/delta-uniform.md)): the table must be a **managed table** in Unity Catalog or the Hive [Metastore](/concepts/metastore.md). If the table is external (i.e., defined using a `LOCATION` that points to a path not managed by the [Metastore](/concepts/metastore.md)), the `REQUIRE_MANAGED_TABLE` error condition is raised.^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Why managed tables are required

IcebergCompat relies on the Delta transaction log to produce Iceberg metadata. When the table is managed, Databricks can guarantee that the underlying data files and the transaction log are co-located and under platform control, which simplifies the generation and maintenance of Iceberg metadata views. External tables, by contrast, allow data to reside outside the platform’s lifecycle, which can break the contract that Uniform must maintain between Delta files and the Iceberg manifest.

## Error condition

If you attempt to enable IcebergCompat on an external table, the operation fails with the following sub‑condition of the `DELTA_ICEBERG_COMPAT_VIOLATION` error class:

**REQUIRE\_MANAGED\_TABLE** – “The feature can be enabled only on Managed Tables.”^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## How to check whether a table is managed

- In the Databricks Catalog Explorer, look at the **Table Type** property: a managed table displays as `MANAGED`.  
- Use the SQL command `DESCRIBE EXTENDED <table_name>` and inspect the `Type` field.  
- In Python with `spark.sql("SHOW TBLPROPERTIES <table_name>")`, check the `delta.uniform` property.

## Resolving the error

If your table is external and you need to use IcebergCompat, you have two options:

1. **Re‑create the table as a managed table** – Use `CREATE TABLE ... AS` or migrate the data to a new managed location.  
2. **Change the external table’s location to a location managed by Unity Catalog** – This is only possible if you convert the table to a managed table by removing the external location dependency (requires moving data into the metastore’s default root).

## Related concepts

- IcebergCompat – The Delta table feature that enables Unified Iceberg compatibility.  
- [Uniform](/concepts/delta-uniform.md) – The capability that allows Delta tables to be read as Iceberg and Hudi tables.  
- [Managed Table](/concepts/unity-catalog-managed-tables.md) – A table whose data and metadata are fully managed by Unity Catalog.  
- External Table – A table whose data resides at a user‑specified location outside the metastore’s control.  
- DELTA_ICEBERG_COMPAT_VIOLATION error class – The error class that contains all IcebergCompat validation failures.

## Sources

- delta_iceberg_compat_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_violation-error-condition-databricks-on-aws.md](/references/delta_iceberg_compat_violation-error-condition-databricks-on-aws-206a4feb.md)

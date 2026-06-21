---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 14795e2411eaad899ddcb04b95d0516006825850a54d4ee76ca7a59a450c77bd
  pageDirectory: concepts
  sources:
    - data-lineage-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - lineage-limitations-and-edge-cases
    - Edge Cases and Lineage Limitations
    - LLAEC
    - Data lineage limitations
  citations:
    - file: data-lineage-in-unity-catalog-databricks-on-aws.md
title: Lineage Limitations and Edge Cases
description: Known gaps in Unity Catalog lineage capture including renamed objects, Spark SQL checkpointing, RDDs, global temp views, path-referenced tables, UDFs, and Jobs API runs_submit workflows.
tags:
  - limitations
  - lineage
  - edge-cases
timestamp: "2026-06-19T09:42:02.778Z"
---

# Lineage Limitations and Edge Cases

**Lineage Limitations and Edge Cases** documents the known gaps, unsupported scenarios, and behavioral nuances of [data lineage](/concepts/data-lineage-in-unity-catalog.md) capture in [Unity Catalog](/concepts/unity-catalog.md). These constraints affect the completeness, accuracy, and availability of lineage information for tables, views, columns, and related assets across Databricks workspaces.

## Data Capture Window

Lineage data captured before **September 1, 2024** is not available in Catalog Explorer or system tables. For older metastores, the available lineage history starts from that date. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Unsupported Workflow Types

Certain job execution patterns do not appear in lineage views, even though table and column-level lineage may still be captured:

- **Jobs API `runs submit` requests** — Jobs submitted via `runs submit` do not have their lineage linked to a specific job run in the lineage graph. Table and column-level lineage is still captured, but the link to the job run is missing. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]
- **`spark submit` task type** — Jobs that use the `spark submit` task type also lack the job-run link in the lineage view. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Renamed Objects

Lineage is **not preserved** for renamed catalogs, schemas, tables, views, or columns. If an object is renamed, the historical lineage connections to its prior name are lost. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Spark SQL Dataset Checkpointing

If you use Spark SQL dataset checkpointing, lineage is **not captured** for those operations. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Lakeflow Spark Declarative Pipelines

[Lakeflow Spark Declarative Pipelines](/concepts/lakeflow-spark-declarative-pipelines.md) capture lineage in most cases, but coverage is **incomplete** for pipelines that use PRIVATE tables. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Resilient Distributed Datasets (RDDs)

Resilient Distributed Datasets (RDDs) are not captured in lineage. Only DataFrame-based and SQL-based operations are tracked. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Global Temp Views

Global temp views are not captured in lineage. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## `system.information_schema` Tables

Tables under `system.information_schema` are not captured in lineage. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Column-Level Lineage Gaps

Column-level lineage cannot be captured in certain scenarios:

- **Path-based references** — If the source or target is referenced by path (e.g., `SELECT * FROM delta."s3://<bucket>/<path>"`), column lineage is not captured. Column lineage is supported only when both source and target are referenced by table name (e.g., `SELECT * FROM <catalog>.<schema>.<table>`). ^[data-lineage-in-unity-catalog-databricks-on-aws.md]
- **User-defined functions (UDFs)** — The use of UDFs can obscure the mapping between source and target columns, preventing column-level lineage from being tracked. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Transaction Rollbacks

[Transactions](/concepts/delta-acid-transactions.md) emit lineage as each read and write occurs. However, lineage events **persist** even if the transaction is rolled back. This means that rolled-back operations may still appear in the lineage graph. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Permissions and Cross-Workspace Visibility

### Masked Nodes

Lineage graphs share the same permission model as Unity Catalog. If a user does not have `BROWSE` or `SELECT` privilege on a table, they cannot explore its lineage. Downstream tables that the user lacks permission to access appear as **masked** nodes and cannot be expanded. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

### Cross-Workspace Detail Masking

Lineage is aggregated across all workspaces attached to a Unity Catalog [Metastore](/concepts/metastore.md). However, detailed information about workspace-level objects (notebooks, jobs, dashboards) created in other workspaces is **masked**. Users can only see full details for objects in their current workspace. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Retention

Lineage data in Catalog Explorer is retained indefinitely for data captured after September 1, 2024. The lineage system tables (`system.access.table_lineage` and `system.access.column_lineage`) retain a rolling **1-year** window of data. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Data Lineage in Unity Catalog](/concepts/data-lineage-in-unity-catalog.md) — Overview and general usage
- [External Lineage](/concepts/external-lineage.md) — Extending lineage beyond Databricks
- [Lineage System Tables](/concepts/lineage-system-tables.md) — Programmatic querying of lineage data
- [Permissions in Unity Catalog](/concepts/manage-permission-in-unity-catalog.md) — Access control model for lineage visibility
- [Lakeflow Spark Declarative Pipelines](/concepts/lakeflow-spark-declarative-pipelines.md) — Pipeline type with partial lineage support
- Spark SQL dataset checkpointing — Unsupported lineage scenario

## Sources

- data-lineage-in-unity-catalog-databricks-on-aws.md

# Citations

1. [data-lineage-in-unity-catalog-databricks-on-aws.md](/references/data-lineage-in-unity-catalog-databricks-on-aws-84f84dd2.md)

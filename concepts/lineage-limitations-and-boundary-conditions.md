---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0296ecef5d211f03dda60685eb7aa22816294855041ec8e6db537464340f96ff
  pageDirectory: concepts
  sources:
    - data-lineage-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - lineage-limitations-and-boundary-conditions
    - Boundary Conditions and Lineage Limitations
    - LLABC
  citations:
    - file: data-lineage-in-unity-catalog-databricks-on-aws.md
title: Lineage Limitations and Boundary Conditions
description: Notable gaps in lineage capture including renamed objects, RDDs, global temp views, path-referenced tables, UDFs, Jobs API runs_submit workflows, Spark SQL checkpointing, and incomplete coverage for PRIVATE tables in Lakeflow pipelines.
tags:
  - limitations
  - lineage
  - troubleshooting
timestamp: "2026-06-19T18:04:45.978Z"
---

# Lineage Limitations and Boundary Conditions

**Lineage Limitations and Boundary Conditions** describes the known constraints, edge cases, and data retention policies that apply to [Data Lineage in Unity Catalog](/concepts/data-lineage-in-unity-catalog.md) on Databricks. These limitations affect the completeness and availability of lineage information displayed in Catalog Explorer and queried via system tables.

## Data Retention and Availability

Lineage data captured before September 1, 2024 is not available. For metastores created after that date, Catalog Explorer includes an **All time** option in the lineage time-range dropdown. For older metastores, the dropdown includes an **All available** option that starts from September 1, 2024. The default selection is **1 year**. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

Lineage system tables (`system.access.table_lineage` and `system.access.column_lineage`) retain a rolling 1-year window of data. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Job and Workflow Coverage Gaps

Jobs that use the Jobs API `runs submit` request or the `spark submit` task type are unavailable in lineage views. Table and column level lineage is still captured for these workflows, but the link to the job run is not captured. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Renamed Objects

Lineage is not preserved for renamed catalogs, schemas, tables, views, or columns. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Unsupported Operations and Features

The following operations and features do not produce lineage data:

- Spark SQL Dataset Checkpointing — If used, lineage is not captured. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]
- Resilient Distributed Datasets (RDDs) — RDDs are not captured in lineage. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]
- Global Temp Views — Global temp views are not captured in lineage. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]
- Tables under `system.information_schema` — Not captured in lineage. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Partial Lineage Coverage

Unity Catalog captures lineage from [Lakeflow Spark Declarative Pipelines](/concepts/lakeflow-spark-declarative-pipelines.md) in most cases, but coverage is incomplete for pipelines that use PRIVATE tables. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Column-Level Lineage Constraints

Column-level lineage cannot be captured if the source or the target is referenced as a path (for example, `select * from delta."s3://<bucket>/<path>"`). Column lineage is supported only when both the source and target are referenced by table name (for example, `select * from <catalog>.<schema>.<table>`). ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

Use of user-defined functions (UDFs) can obscure the mapping between source and target columns, preventing column-level lineage capture. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Transaction Behavior

[Transactions](/concepts/delta-acid-transactions.md) emit lineage as each read and write occurs. Lineage events persist even if the transaction is rolled back. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Cross-Workspace Visibility Limitations

Lineage is aggregated across all workspaces attached to a [Unity Catalog Metastore](/concepts/unity-catalog-metastore.md), so lineage captured in one workspace is visible in any other workspace that shares that [Metastore](/concepts/metastore.md). However, detailed information about workspace-level objects like notebooks and dashboards in other workspaces is masked. Users must have at least the `BROWSE` privilege on the parent catalog of the table or view to view lineage. If a user does not have the `BROWSE` or `SELECT` privilege on a table, they cannot explore its lineage. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Data Lineage in Unity Catalog](/concepts/data-lineage-in-unity-catalog.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Catalog Explorer](/concepts/catalog-explorer.md)
- System Tables
- [Permissions in Unity Catalog](/concepts/manage-permission-in-unity-catalog.md)
- [Lakeflow Spark Declarative Pipelines](/concepts/lakeflow-spark-declarative-pipelines.md)
- Transactions on Databricks

## Sources

- data-lineage-in-unity-catalog-databricks-on-aws.md

# Citations

1. [data-lineage-in-unity-catalog-databricks-on-aws.md](/references/data-lineage-in-unity-catalog-databricks-on-aws-84f84dd2.md)

---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b7c44a17d0ce2da243ac38488bffe5792c0873f43b63bf4618fe2eb4f8357706
  pageDirectory: concepts
  sources:
    - data-lineage-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - lineage-graph-in-catalog-explorer
    - LGICE
  citations:
    - file: data-lineage-in-unity-catalog-databricks-on-aws.md
title: Lineage Graph in Catalog Explorer
description: Interactive visual interface in Databricks Catalog Explorer for browsing upstream and downstream dependencies of tables, jobs, pipelines, and dashboards with expandable nodes and edge details.
tags:
  - ui
  - catalog-explorer
  - lineage
timestamp: "2026-06-19T09:43:07.677Z"
---

# Lineage Graph in Catalog Explorer

**Lineage Graph in Catalog Explorer** is the interactive visual interface in [Catalog Explorer](/concepts/catalog-explorer.md) that displays the [Data Lineage](/concepts/data-lineage.md) of tables and views registered in [Unity Catalog](/concepts/unity-catalog.md). It shows how data flows through Databricks — which queries and files populate a table, which jobs and notebooks transform it, and which dashboards or downstream assets consume the results — all within a single, navigable graph. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## What Lineage Shows

The lineage graph aggregates metadata from all workspaces attached to the [Unity Catalog Metastore](/concepts/unity-catalog-metastore.md) and captures it automatically for queries run on Databricks, down to the column level. Nodes in the graph can represent:

- Tables and views (registered in Unity Catalog)
- copy_model_version API|ML model versions
- External assets (entities added via [External Lineage](/concepts/external-lineage.md))
- File paths

^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## How to View Lineage in Catalog Explorer

1. In the Databricks workspace, click the **Catalog** icon (data icon).
2. Search or browse for the table you want to investigate.
3. Select the **Lineage** tab — the lineage panel appears and displays related tables.
4. Click **See Lineage Graph** to open the interactive graph. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

By default, the graph shows one level of connections. You can expand nodes by clicking the **Plus** icon on a node to reveal more connections if they are available. Click the icon on a connecting edge to open the **Lineage details** panel, which shows the source and target tables, and details about the relationship. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

### Viewing Job and Dashboard Lineage

To view job lineage, go to a table's **Lineage** tab, select **Jobs**, and select **Downstream** — the job name appears under **Job Name** as a consumer of the table. To view dashboard lineage, go to the **Lineage** tab and click **Dashboards** — the dashboard name appears under **Dashboard Name** as a consumer of the table. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

### Column-Level Lineage

To view column-level lineage, click a column in the graph to show links to related columns. For example, clicking on the `revenue` column shows upstream columns from which it was derived. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Use Cases

The lineage graph in Catalog Explorer supports several common workflows:

- **Impact analysis**: Before changing or deleting a table or column, identify downstream tables, jobs, and dashboards that depend on it. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]
- **Root cause investigation**: When a downstream report shows unexpected results, trace upstream sources to find where the data diverged. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]
- **Sensitive data flow tracking**: For compliance audits, see where regulated data originates, how it is transformed, and which downstream assets consume it. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]
- **Cross-team dependency discovery**: Identify which teams own the upstream sources you rely on, or which teams consume your tables. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Permissions

Lineage graphs share the same permission model as Unity Catalog. Tables and other data objects registered in the [Metastore](/concepts/metastore.md) are visible only to users who have at least `BROWSE` permissions on those objects. If a user does not have `BROWSE` or `SELECT` privilege on a table, they cannot explore its lineage. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

Lineage is aggregated across all workspaces, so lineage captured in one workspace is visible in any other workspace that shares the same [Metastore](/concepts/metastore.md), as long as the user has adequate object permissions. However, detailed information about workspace-level objects (like notebooks and dashboards) in other workspaces is masked — nodes from other workspaces appear as `masked` in the graph. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

Users must also have specific permissions to view workspace objects like notebooks, jobs, and dashboards. For more information, see Manage privileges in Unity Catalog and [Access control lists](/concepts/table-access-control-tacl.md). ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Requirements

- Tables must be registered in a Unity Catalog [Metastore](/concepts/metastore.md). ^[data-lineage-in-unity-catalog-databricks-on-aws.md]
- External assets must be added as external metadata objects with configured relationships. See [External Lineage](/concepts/external-lineage.md). ^[data-lineage-in-unity-catalog-databricks-on-aws.md]
- Queries must use the Spark DataFrame or Databricks SQL interfaces (notebooks or the SQL query editor). ^[data-lineage-in-unity-catalog-databricks-on-aws.md]
- Users must have `BROWSE` privilege on the parent catalog of the table or view. The parent catalog must also be accessible from the workspace (see [Workspace-Catalog Binding](/concepts/workspace-catalog-binding.md)). ^[data-lineage-in-unity-catalog-databricks-on-aws.md]
- For notebooks, jobs, or dashboards, users must have appropriate permissions as defined by workspace access control settings. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

### Compute and Network Requirements

- Lineage tracking for streaming between Delta tables requires Databricks Runtime 11.3 LTS or above. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]
- Column-level lineage tracking for [Lakeflow Spark Declarative Pipelines](/concepts/lakeflow-spark-declarative-pipelines.md) requires Databricks Runtime 13.3 LTS or above. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]
- You may need to update outbound firewall rules to allow connectivity to the Amazon Kinesis endpoint in the Databricks control plane. See Kinesis addresses and Configure a customer-managed VPC. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Getting Lineage with Genie Code

[Genie Code](/concepts/genie-code.md) can answer lineage questions in natural language. To use it:

1. In the workspace sidebar, click the **Catalog** icon.
2. Browse or search for the catalog, click the catalog name, and click the **Genie Code** icon.
3. At the prompt, use:
   - `/getTableLineages` to view upstream and downstream dependencies.
   - `/getTableInsights` to access metadata-driven insights like user activity and query patterns.

^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Querying Lineage with System Tables

To programmatically query lineage data, use the [Lineage System Tables](/concepts/lineage-system-tables.md) (`system.access.table_lineage` and `system.access.column_lineage`). These tables retain a rolling 1-year window of data. See [Lineage system tables reference](/concepts/lineage-system-tables.md). ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Retention

Lineage data displayed in Catalog Explorer is retained indefinitely. All lineage data captured after September 1, 2024 is available. For metastores created after that date, an **All time** option is available in the lineage time-range dropdown. For older metastores, an **All available** option starts from September 1, 2024. The default selection is **1 year**. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Limitations

- Lineage data captured before September 1, 2024 is not available. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]
- Jobs using the Jobs API `runs submit` request or `spark submit` task type are unavailable in lineage views (though table and column-level lineage is still captured). ^[data-lineage-in-unity-catalog-databricks-on-aws.md]
- Lineage is not preserved for renamed catalogs, schemas, tables, views, or columns. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]
- Spark SQL dataset checkpointing does not capture lineage. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]
- Resilient Distributed Datasets (RDDs) are not captured. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]
- Global temp views are not captured. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]
- Tables under `system.information_schema` are not captured. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]
- Column-level lineage cannot be captured when the source or target is referenced as a path (e.g., `select * from delta."s3://<bucket>/<path>"`). It is supported only when both are referenced by table name. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]
- Use of user-defined functions (UDFs) can obscure the mapping between source and target columns. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Data Lineage](/concepts/data-lineage.md) — The underlying metadata that powers the graph.
- [Catalog Explorer](/concepts/catalog-explorer.md) — The UI where the lineage graph is displayed.
- [Unity Catalog](/concepts/unity-catalog.md) — The governance system that manages the lineage metadata.
- [External Lineage](/concepts/external-lineage.md) — Extends the graph with assets outside Databricks.
- ML model lineage — Track lineage for machine learning models.
- Table insights — Usage trends for a table, shown in the **Insights** tab.
- [Lineage System Tables](/concepts/lineage-system-tables.md) — Programmatic access to lineage data.

## Sources

- data-lineage-in-unity-catalog-databricks-on-aws.md

# Citations

1. [data-lineage-in-unity-catalog-databricks-on-aws.md](/references/data-lineage-in-unity-catalog-databricks-on-aws-84f84dd2.md)

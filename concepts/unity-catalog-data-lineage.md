---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a784b6acb51bdca53856adedf6cdbb69287758e5043b5ea892c0e8f88b9b160f
  pageDirectory: concepts
  sources:
    - data-lineage-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-data-lineage
    - UCDL
  citations:
    - file: data-lineage-in-unity-catalog-databricks-on-aws.md
title: Unity Catalog Data Lineage
description: Automatically captured metadata showing where data in Databricks originated, how it was transformed, and which downstream assets consume it, down to the column level.
tags:
  - data-governance
  - lineage
  - unity-catalog
timestamp: "2026-06-19T18:05:56.309Z"
---

# Unity Catalog Data Lineage

**Unity Catalog Data Lineage** is a feature within [Unity Catalog](/concepts/unity-catalog.md) that automatically captures the origin and transformation of data across Databricks workspaces. It shows where data came from, which queries and files populate a table, which jobs and notebooks transform it, and which dashboards consume the results. Lineage is captured at the column level and aggregated across all workspaces attached to the same [Metastore](/concepts/metastore.md). ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Capabilities

Lineage in Unity Catalog enables several use cases:

- **Impact analysis**: Before changing or deleting a table or column, users can identify downstream tables, jobs, and dashboards that depend on it.
- **Root cause investigation**: When a downstream report shows unexpected results, users can trace upstream sources to find where the data diverged.
- **Tracking sensitive data flow**: For compliance audits, users can see where regulated data originates, how it is transformed, and which downstream assets consume it.
- **Understanding cross-team dependencies**: Users can discover which teams own the upstream sources they rely on or which teams consume their tables. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

External lineage extends the graph beyond Databricks by registering upstream sources (e.g., Salesforce, MySQL) and downstream tools (e.g., Tableau, Power BI) as external assets in Unity Catalog. See [External Lineage](/concepts/external-lineage.md). ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Requirements

To capture data lineage using Unity Catalog:

- Tables must be registered in a Unity Catalog [Metastore](/concepts/metastore.md).
- External assets must be added as external metadata objects in Unity Catalog, with relationships configured to other securable objects.
- Queries must use the Spark DataFrame interface (e.g., Spark SQL functions that return a DataFrame) or Databricks SQL interfaces such as notebooks or the SQL query editor. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

To view data lineage, users need:

- At least the `BROWSE` privilege on the parent catalog of the table or view. The parent catalog must also be accessible from the workspace (see [Workspace-Catalog Binding](/concepts/workspace-catalog-binding.md)).
- For notebooks, jobs, or dashboards, permissions defined by the workspace access control settings.
- For a Unity Catalog-enabled pipeline, `CAN VIEW` permission on the pipeline. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

Compute requirements:

- Lineage tracking of streaming between Delta tables requires Databricks Runtime 11.3 LTS or above.
- Column lineage tracking for Lakeflow Spark Declarative Pipelines requires Databricks Runtime 13.3 LTS or above. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

Networking requirements may include updating outbound firewall rules to allow connectivity to the Amazon Kinesis endpoint in the Databricks control plane, especially if the workspace is deployed in a customer-managed VPC or uses AWS PrivateLink. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Viewing Lineage in Catalog Explorer

To view table lineage in [Catalog Explorer](/concepts/catalog-explorer.md):

1. In the workspace sidebar, click **Catalog**.
2. Search or browse for the table.
3. Select the **Lineage** tab. The lineage panel displays related tables.
4. To view an interactive graph, click **See Lineage Graph**. By default, one level is displayed. Click the plus sign icon on a node to reveal more connections if available.
5. Click the icon on a connecting edge to open the **Lineage details** panel, which shows source and target tables.
6. To view an asset (notebook, job, pipeline, query) associated with a table, select the asset in the **Lineage details** panel.
7. To view column-level lineage, click a column in the graph to show links to related columns. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

### Viewing Job and Dashboard Lineage

To view job lineage, go to a table's **Lineage** tab, select **Jobs**, then **Downstream**. The job name appears under **Job Name** as a consumer of the table. Similarly, to view dashboard lineage, go to the **Lineage** tab and click **Dashboards**. The dashboard appears under **Dashboard Name** as a consumer of the table. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Getting Lineage Using Genie Code

Genie Code can answer lineage questions in natural language. To use it:

1. In the workspace sidebar, click **Catalog**.
2. Browse or search for the catalog, click the catalog name, then click the Genie Code icon in the upper-right corner.
3. At the Genie Code prompt, type:
   - `/getTableLineages` to view upstream and downstream dependencies.
   - `/getTableInsights` to access metadata-driven insights, such as user activity and query patterns.

These queries enable Genie Code to answer questions like "show me downstream lineages" or "who queries this table most often." ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Querying Lineage with System Tables

Lineage data can also be queried programmatically using lineage system tables. For detailed instructions, see the System Tables Reference and [Lineage System Tables Reference](/concepts/lineage-system-tables.md). ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Permissions

Lineage graphs share the same permission model as Unity Catalog. Tables and other data objects are visible only to users who have at least `BROWSE` permissions on those objects. If a user lacks `BROWSE` or `SELECT` privilege on a table, they cannot explore its lineage. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

Lineage is aggregated across all workspaces attached to a Unity Catalog [Metastore](/concepts/metastore.md). Lineage captured in one workspace is visible in any other workspace sharing that [Metastore](/concepts/metastore.md), as long as the user has adequate object permissions. Detailed information about workspace-level objects (notebooks, dashboards) in other workspaces is masked. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

For example, if `userA` is granted `SELECT` on `lineage_data.lineagedemo.menu`, they see the `menu` table in the lineage graph but cannot see associated tables like `dinner` (which appears as a masked node). Granting `BROWSE` on the parent catalog or schema allows users to view the lineage graph for any table in that schema. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

Lineage users must also have specific permissions to view workspace objects like notebooks, jobs, and dashboards. Detailed information about these objects is visible only in the workspace where they were created. See Manage Privileges in Unity Catalog and Access Control Lists. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Retention

Lineage data displayed in Catalog Explorer is retained indefinitely. All lineage data captured after September 1, 2024 is available. For metastores created after that date, Catalog Explorer includes an **All time** option in the lineage time-range dropdown. For older metastores, the dropdown includes an **All available** option starting from September 1, 2024. The default selection is **1 year**. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

Lineage system tables (`system.access.table_lineage` and `system.access.column_lineage`) retain a rolling 1-year window of data. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Limitations

Data lineage has the following limitations (which also apply to lineage system tables):

- Lineage data captured before September 1, 2024 is not available.
- Jobs that use the Jobs API `runs submit` request or the `spark submit` task type are unavailable in lineage views. Table and column level lineage is still captured for these workflows, but the link to the job run is not captured.
- Lineage is not preserved for renamed catalogs, schemas, tables, views, or columns.
- If Spark SQL dataset checkpointing is used, lineage is not captured.
- Unity Catalog captures lineage from Lakeflow Spark Declarative Pipelines in most cases, but coverage is incomplete for pipelines that use PRIVATE tables.
- Resilient Distributed Datasets (RDDs) are not captured in lineage.
- Global temp views are not captured in lineage.
- Transactions emit lineage as each read and write occurs. Lineage events persist even if the transaction is rolled back.
- Tables under `system.information_schema` are not captured in lineage.
- Column-level lineage cannot be captured in some cases: when the source or target is referenced as a path (e.g., `delta."s3://<bucket>/<path>"`), or when user-defined functions (UDFs) obscure the mapping between source and target columns. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [External Lineage](/concepts/external-lineage.md)
- [Catalog Explorer](/concepts/catalog-explorer.md)
- System Tables
- [Workspace-Catalog Binding](/concepts/workspace-catalog-binding.md)
- Manage Privileges in Unity Catalog
- ML Model Lineage
- Table Insights and Popularity

## Sources

- data-lineage-in-unity-catalog-databricks-on-aws.md

# Citations

1. [data-lineage-in-unity-catalog-databricks-on-aws.md](/references/data-lineage-in-unity-catalog-databricks-on-aws-84f84dd2.md)

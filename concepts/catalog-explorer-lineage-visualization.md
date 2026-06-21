---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 218a203bec334794bd829dffeef21a6faf8b8db0d24f8d04533e48be00b20d75
  pageDirectory: concepts
  sources:
    - data-lineage-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - catalog-explorer-lineage-visualization
    - CELV
  citations:
    - file: data-lineage-in-unity-catalog-databricks-on-aws.md
title: Catalog Explorer Lineage Visualization
description: Interactive graph interface in Databricks Catalog Explorer showing table, job, dashboard, and column-level lineage with expandable nodes and a Lineage details panel.
tags:
  - ui
  - visualization
  - catalog-explorer
  - lineage
timestamp: "2026-06-19T18:05:01.180Z"
---

# Catalog Explorer Lineage Visualization

**Catalog Explorer Lineage Visualization** refers to the interactive graph and details panel in Databricks Catalog Explorer that shows where data comes from and where it goes — tracking tables, views, ML model versions, external assets, and file paths across all workspaces attached to a Unity Catalog [Metastore](/concepts/metastore.md). ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Use Cases

Lineage visualization supports impact analysis (identifying downstream dependencies before changing a table), root‑cause investigation (tracing unexpected results upstream), sensitive‑data tracking for compliance, and understanding cross‑team dependencies. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Viewing Lineage in Catalog Explorer

1. In the workspace sidebar, click **Catalog**, then search or browse for the table and select it.
2. Open the **Lineage** tab to see related tables in a summary panel.
3. Click **See Lineage Graph** to display an interactive graph. By default, one level of connections is shown; click the **+** icon on any node to expand further.
4. Click the icon on a connecting edge to open the **Lineage details** panel, which shows source/target tables and associated assets.
5. In the **Lineage details** panel, filter by notebooks, jobs, pipelines, or queries to view specific asset types. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

### Column‑Level Lineage

Inside the lineage graph, clicking a column name reveals links to related upstream and downstream columns. This helps trace how individual columns are derived or consumed. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

### Job and Dashboard Lineage

To see which jobs consume a table, go to the **Lineage** tab, select **Jobs**, then **Downstream**. To see consuming dashboards, select **Dashboards**. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Permissions and Visibility

Lineage graphs respect Unity Catalog permissions. A user must have at least `BROWSE` on the parent catalog to view lineage for a table. Tables the user cannot access appear as masked nodes in the graph. Detailed information about workspace objects (notebooks, dashboards, jobs) is visible only in the workspace where they were created. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Retention

Lineage data displayed in Catalog Explorer is retained indefinitely for events captured after September 1, 2024. The time‑range dropdown offers an **All time** option (for metastores created after that date) or **All available** (starting from September 1, 2024). The default selection is **1 year**. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Limitations Relevant to Catalog Explorer

- Lineage data before September 1, 2024 is not available.
- Jobs submitted via `runs submit` or using `spark submit` task type appear without job‑run links.
- Renamed catalogs, schemas, tables, views, or columns lose their lineage history.
- Column‑level lineage may be incomplete when sources or targets are referenced by path (e.g., `delta."s3://bucket/path"`) or when user‑defined functions (UDFs) are used. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Data Lineage in Unity Catalog](/concepts/data-lineage-in-unity-catalog.md) – Overview of lineage capture and external lineage.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer that powers lineage.
- [Catalog Explorer](/concepts/catalog-explorer.md) – The UI for browsing and managing Unity Catalog objects.
- [Column-Level Lineage](/concepts/column-level-lineage.md) – Detailed tracing of data movement at the column level.
- [External Lineage](/concepts/external-lineage.md) – Integrating assets outside Databricks into the lineage graph.
- Table Insights – Usage trends and query patterns visible from the Insights tab.

## Sources

- data-lineage-in-unity-catalog-databricks-on-aws.md

# Citations

1. [data-lineage-in-unity-catalog-databricks-on-aws.md](/references/data-lineage-in-unity-catalog-databricks-on-aws-84f84dd2.md)

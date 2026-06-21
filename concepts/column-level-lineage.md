---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 88a21afff904702f112e713fb0a36b6900e44ba87350671d3e7ddf8bb0cbf907
  pageDirectory: concepts
  sources:
    - data-lineage-in-unity-catalog-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - column-level-lineage
    - Column‑Level Lineage
  citations:
    - file: data-lineage-in-unity-catalog-databricks-on-aws.md
title: Column-Level Lineage
description: Granular tracking of data at the column level within Unity Catalog, showing how specific columns in downstream tables derive from upstream columns, with limitations for path-based references and UDFs.
tags:
  - data-lineage
  - column-tracking
  - granularity
timestamp: "2026-06-19T14:41:03.790Z"
---

```yaml
---
title: Column-level Lineage
summary: Fine-grained tracking of how individual columns in a table are derived from upstream source columns, displayed interactively in the lineage graph.
sources:
  - data-lineage-in-unity-catalog-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T09:41:49.223Z"
updatedAt: "2026-06-19T09:41:49.223Z"
tags:
  - lineage
  - columns
  - data-governance
aliases:
  - column-level-lineage
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Column-level Lineage

**Column-level lineage** shows how individual columns in a table or view derive from upstream source columns, enabling detailed impact analysis, root‑cause investigation, and compliance tracking at the attribute level. Unity Catalog automatically captures column‑level lineage for queries run on Databricks and aggregates it across all workspaces attached to the [[metastore|Metastore]]. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Overview

While table-level lineage maps dependencies between entire tables, column‑level lineage traces the flow of each column through transformations such as `SELECT`, `JOIN`, and `UNION`. This granular view helps answer questions like “Which source column feeds the `revenue` column in this report?” or “If I drop this source column, which downstream columns will break?” ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

Column‑level lineage is a core feature of [[Data Lineage in Unity Catalog]], which also supports lineage for notebooks, jobs, pipelines, dashboards, and external assets. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Viewing Column-level Lineage in Catalog Explorer

To inspect column‑level relationships for a Unity Catalog table:

1. In your Databricks workspace, click **Catalog** and browse or search for the table.
2. Select the **Lineage** tab, then click **See Lineage Graph** to open the interactive graph.
3. Click any column in the graph. Links appear to the upstream columns from which it was derived (or to downstream columns that depend on it). ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

![Column-level lineage example showing a `revenue` column and its upstream columns.](https://docs.databricks.com/aws/en/assets/images/uc-column-lineage-c8dfa626d400501fd428b1606ad74e7c.png) ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

The **Lineage details** panel, opened by clicking a connecting edge, shows the source and target tables and can be filtered to view notebooks, jobs, pipelines, or queries associated with the connection. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Requirements

- Tables must be registered in a [[Unity Catalog]] [[metastore|Metastore]].
- Queries must use the Spark DataFrame interface or Databricks SQL (notebooks, SQL query editor, etc.).
- Column lineage tracking for [[Lakeflow Spark Declarative Pipelines]] workloads requires Databricks Runtime 13.3 LTS or above. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]
- To view column‑level lineage, users need at least the `BROWSE` privilege on the parent catalog of the table or view. For notebooks, jobs, or dashboards, workspace‑level permissions apply. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Limitations

Unity Catalog captures column‑level lineage as completely as possible, but the following cases are not supported: ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

- Column lineage cannot be captured when the source or target is referenced by file path (e.g., `SELECT * FROM delta."s3://bucket/path"`). Column lineage is only supported when both source and target are referenced by table name (e.g., `SELECT * FROM catalog.schema.table`).
- Use of [[ABAC User-Defined Functions (UDFs)|user‑defined functions (UDFs)]] can obscure the mapping between source and target columns, preventing column‑level lineage from being recorded.

Other general lineage limitations also apply: lineage data before September 1, 2024 is not available; jobs that use the Jobs API `runs submit` or `spark submit` task type do not appear in lineage views; lineage is not preserved for renamed catalogs, schemas, tables, views, or columns; and certain operations like Spark SQL dataset checkpointing or RDD usage are not captured. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Additional Resources

- For programmatic access, query the [[Lineage System Tables]] (`system.access.column_lineage` and `system.access.table_lineage`), which retain a rolling one‑year window of data.
- For ML model lineage, see [[Data Lineage in Unity Catalog|Track data lineage of a model in Unity Catalog]].

## Sources

- data-lineage-in-unity-catalog-databricks-on-aws.md
```

# Citations

1. [data-lineage-in-unity-catalog-databricks-on-aws.md](/references/data-lineage-in-unity-catalog-databricks-on-aws-84f84dd2.md)

---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: eaeeb8b01e3986e46255e98760250384b90ae4ae36442e96472d64d2cd8ce6d6
  pageDirectory: concepts
  sources:
    - data-lineage-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - lineage-system-tables
    - LST
    - Lineage System Tables Reference
    - Lineage system tables reference
  citations:
    - file: data-lineage-in-unity-catalog-databricks-on-aws.md
title: Lineage System Tables
description: Programmatic access to lineage data via system.access.table_lineage and system.access.column_lineage tables, which retain a rolling one-year window of lineage events.
tags:
  - system-tables
  - query
  - lineage
timestamp: "2026-06-19T18:05:12.100Z"
---

# Lineage System Tables

**Lineage system tables** are Databricks system tables that store data lineage information captured by [Unity Catalog](/concepts/unity-catalog.md), enabling programmatic querying of upstream and downstream dependencies for tables, views, and columns across all workspaces attached to a [Metastore](/concepts/metastore.md). ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Overview

Lineage system tables provide a structured, queryable interface for accessing the same lineage data displayed in the [Catalog Explorer](/concepts/catalog-explorer.md) lineage graph. They allow you to perform impact analysis, investigate root causes of data issues, track sensitive data flow for compliance audits, and understand cross-team dependencies through SQL queries or programmatic access. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Available System Tables

The lineage system tables are available under the `system.access` schema and include: ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

| Table Name | Description |
|------------|-------------|
| `table_lineage` | Records upstream and downstream relationships between tables |
| `column_lineage` | Records column-level lineage showing how columns are derived from source columns |

## Data Retention

Lineage system tables retain a rolling **1-year window** of data for both `system.access.table_lineage` and `system.access.column_lineage`. In contrast, lineage data displayed in Catalog Explorer is retained indefinitely. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Querying Lineage Data

You can use standard SQL queries against the lineage system tables to programmatically retrieve lineage information. For detailed instructions on querying these tables, see the [System tables reference](/concepts/data-classification-system-table.md) and [Lineage system tables reference](/concepts/lineage-system-tables.md) documentation. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

### Common Query Patterns

- **Upstream dependencies**: Find all source tables and columns that feed into a given table.
- **Downstream dependencies**: Identify all tables, notebooks, jobs, and dashboards that consume data from a given table.
- **Column-level trace**: Trace how a specific column is derived from upstream source columns.
- **Cross-workspace lineage**: View lineage aggregated across all workspaces attached to the [Metastore](/concepts/metastore.md) (with appropriate permissions).

## Permissions

Lineage system tables share the same permission model as Unity Catalog securable objects. Tables and other data objects registered in the Unity Catalog [Metastore](/concepts/metastore.md) are visible only to users who have at least `BROWSE` permissions on those objects. If a user does not have the `BROWSE` or `SELECT` privilege on a table, that table does not appear in lineage query results — it is effectively masked, consistent with the behavior in Catalog Explorer. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

To query lineage system tables, users must have:
- At least `BROWSE` permission on the parent catalog of the table or view
- Appropriate `SELECT` privileges on the lineage system tables themselves

## Limitations

Lineage system tables share the same limitations as the [Catalog Explorer](/concepts/catalog-explorer.md) lineage graph: ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

- **Data availability**: Lineage data captured before September 1, 2024 is not available.
- **Job linking**: Jobs that use the Jobs API `runs submit` request or the `spark submit` task type are unavailable in lineage views. Table and column level lineage is still captured for these workflows, but the link to the job run is not captured.
- **Renamed objects**: Lineage is not preserved for renamed catalogs, schemas, tables, views, or columns.
- **Spark SQL checkpointing**: If you use Spark SQL dataset checkpointing, lineage is not captured.
- **Column-level gaps**: Column lineage cannot be captured if the source or target is referenced as a file path rather than a table name, or if user-defined functions (UDFs) obscure the mapping between source and target columns.
- **Lakeflow pipelines**: Coverage is incomplete for pipelines that use PRIVATE tables.
- **Other exclusions**: Resilient Distributed Datasets (RDDs), global temp views, and tables under `system.information_schema` are not captured in lineage.
- **Rolled-back transactions**: Lineage events persist even if the transaction is rolled back.

## Comparison with Catalog Explorer

Both the Catalog Explorer lineage graph and lineage system tables draw from the same underlying lineage data. The key difference is the interface: ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

| Feature | Catalog Explorer | Lineage System Tables |
|---------|------------------|----------------------|
| Interface | Visual graph with drill-down | SQL queries |
| Automation | Manual exploration | Programmatic access |
| Retention | Indefinite display | Rolling 1-year window |
| Column-level | Click-to-explore | Queryable |

## Use Cases

- **Impact analysis in CI/CD pipelines**: Before deploying schema changes, programmatically check which downstream assets depend on the target tables.
- **Compliance automation**: Generate periodic reports showing where sensitive data flows across the data estate.
- **Custom data catalogs**: Ingest lineage data into external cataloging tools or data quality platforms.
- **Root cause investigation**: When a downstream report shows unexpected results, trace upstream sources programmatically across large numbers of tables.

## Related Concepts

- [Unity Catalog Data Lineage](/concepts/unity-catalog-data-lineage.md) — The overall lineage feature in Unity Catalog
- [Catalog Explorer Lineage](/concepts/catalog-explorer-lineage-tab.md) — Visual lineage exploration
- System Tables — The broader system tables framework
- [External Lineage](/concepts/external-lineage.md) — Registering lineage for assets outside Databricks
- Access Control in Unity Catalog — Permissions model governing lineage visibility
- [Column-Level Lineage](/concepts/column-level-lineage.md) — Tracing individual column dependencies

## Sources

- data-lineage-in-unity-catalog-databricks-on-aws.md

# Citations

1. [data-lineage-in-unity-catalog-databricks-on-aws.md](/references/data-lineage-in-unity-catalog-databricks-on-aws-84f84dd2.md)

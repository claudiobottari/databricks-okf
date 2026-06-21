---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a0ebe9b073b395d8ee860a271ca666ece1fd28e08c85d1946c1c1c747f59c0f4
  pageDirectory: concepts
  sources:
    - external-lineage-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - external-lineage-in-unity-catalog
    - ELIUC
  citations:
    - file: external-lineage-databricks-on-aws.md
title: External Lineage in Unity Catalog
description: A feature in Databricks Unity Catalog that allows users to add lineage metadata for workloads running outside Databricks (e.g., ETL tools, BI tools) to augment automatically captured runtime lineage.
tags:
  - data-lineage
  - unity-catalog
  - databricks
  - data-governance
timestamp: "2026-06-19T18:46:57.224Z"
---

# External Lineage in Unity Catalog

**External Lineage** in Unity Catalog allows you to augment Databricks’ automatically captured runtime data lineage with metadata about workloads that run outside of Databricks. This provides an end-to-end lineage view that includes upstream sources (such as Salesforce or MySQL) before data is ingested into Unity Catalog, and downstream consumers (such as Tableau or Power BI) after data leaves Databricks. ^[external-lineage-databricks-on-aws.md]

## Overview

Unity Catalog automatically captures data lineage for queries executed on Databricks. However, many data pipelines involve external systems — first‑mile ETL tools that feed data into Databricks, or last‑mile BI tools that consume Databricks data. External lineage fills this gap by letting you manually register external entities and define their relationships to Unity Catalog objects. ^[external-lineage-databricks-on-aws.md]

You can add external lineage in two ways:

- **Manually**, using the Catalog Explorer UI, the External Metadata and External Lineage APIs, or the Databricks SDK for Python.
- **Automatically**, using Lakeflow Connect managed ingestion pipelines, which record source lineage from source tables to destination tables in Unity Catalog. ^[external-lineage-databricks-on-aws.md]

## Requirements

To add external lineage metadata, you need specific privileges depending on the task: ^[external-lineage-databricks-on-aws.md]

| Task | Required Privilege |
|------|-------------------|
| Create an external metadata securable object | `CREATE EXTERNAL METADATA` on the [Metastore](/concepts/metastore.md) |
| Specify lineage relationships from an external metadata object | `MODIFY` on the external metadata object |
| Specify a downstream lineage relationship to a Unity Catalog object | Read privileges on the object (e.g., `SELECT` on a table) |
| Specify an upstream lineage relationship to a Unity Catalog object | Write privileges on the object (e.g., `MODIFY` on a table) |

## Workflow

Adding external lineage involves two steps: ^[external-lineage-databricks-on-aws.md]

1. **Create an external metadata securable object** in Unity Catalog. This object represents an entity in an external system, such as a dashboard in Tableau or a table in MySQL.
2. **Configure a lineage relationship** between the external metadata object and another Unity Catalog object — such as a table, model, path, or another external metadata object.

Once lineage relationships are created, the external metadata object appears in the lineage graph view alongside Databricks objects. ^[external-lineage-databricks-on-aws.md]

### Creating external metadata objects

#### Using Catalog Explorer

1. In your Databricks workspace, click **Catalog**.
2. Click the **External data** button, go to the **External Metadata** tab, and click **Create external metadata**.
3. Specify the metadata details:
   - **Required**: Name (human‑readable, no spaces), System type (select from common systems or choose **Custom**), Entity type (e.g., "table" or "dashboard").
   - **Optional**: URL (for click‑through access to the external asset), Description.
   - **Advanced**: Columns (for column‑level lineage mapping), Properties (JSON key‑value pairs for additional tracking).
4. Click **Create**. ^[external-lineage-databricks-on-aws.md]

#### Using the API

You can also create external metadata objects using the [External Metadata API](/concepts/external-metadata-api.md). ^[external-lineage-databricks-on-aws.md]

### Creating lineage relationships

#### Using Catalog Explorer

1. Find the external metadata object in Catalog Explorer (under **External data > External Metadata** tab).
2. Click **Create lineage relationship**.
3. Select whether the relationship is **upstream** (external object feeds into Unity Catalog) or **downstream** (Unity Catalog feeds into external object).
4. Enter the **Object type** to connect to:
   - **Table**: Select using the search dialog.
   - **Model**: Select the model, then choose the model version.
   - **Path**: For volumes or external locations, enter the path.
   - **External metadata**: Select from the drop‑down menu.
5. (Optional) Under **Advanced**, add column mappings between the external metadata object and the source/target object, or other metadata as JSON key‑value pairs (e.g., the query text that created the relationship).
6. Click **Create**. ^[external-lineage-databricks-on-aws.md]

#### Using the API or SDK

Lineage relationships can also be created using the [External Lineage API](/concepts/external-lineage-api.md) or the Databricks SDK for Python. ^[external-lineage-databricks-on-aws.md]

## Modeling complex lineage patterns

When adding external lineage manually, use these patterns for more complex scenarios: ^[external-lineage-databricks-on-aws.md]

- **Connect two Unity Catalog tables**: Create an external metadata object that sits between them. Specify one table as upstream and the other as downstream so they appear connected in the lineage graph.
- **Add multiple levels of lineage**: Create multiple external metadata objects and configure lineage relationships between each of them to annotate data passing through multiple systems before entering Databricks.
- **Add column‑level lineage**: Specify column names when creating the external metadata object, then map source and target columns when configuring the lineage relationship.

## Limitations

- External lineage is **not recorded** in the lineage system tables (`system.access.table_lineage` and `system.access.column_lineage`). ^[external-lineage-databricks-on-aws.md]
- You can create up to **10,000 external metadata objects** and **100,000 external lineage relationships** per [Metastore](/concepts/metastore.md). See Resource limits. ^[external-lineage-databricks-on-aws.md]

## Related concepts

- [Data Lineage in Unity Catalog](/concepts/data-lineage-in-unity-catalog.md) — Automatically captured runtime lineage for Databricks workloads
- Lakeflow Connect — Managed ingestion pipelines that automatically record source lineage
- [External Metadata API](/concepts/external-metadata-api.md) — REST API for creating external metadata objects
- [External Lineage API](/concepts/external-lineage-api.md) — REST API for creating lineage relationships
- Databricks SDK for Python — Programmatic access to external lineage features
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance platform providing lineage capabilities

## Sources

- external-lineage-databricks-on-aws.md

# Citations

1. [external-lineage-databricks-on-aws.md](/references/external-lineage-databricks-on-aws-d8bef4f2.md)

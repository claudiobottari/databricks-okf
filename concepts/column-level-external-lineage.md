---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c2c5221e9de92027a9c36e90b34c56e737a2deb2fc2c3780efd15886dc00a34b
  pageDirectory: concepts
  sources:
    - external-lineage-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - column-level-external-lineage
    - CEL
  citations:
    - file: external-lineage-databricks-on-aws.md
title: Column-Level External Lineage
description: The ability to map columns between external metadata objects and Unity Catalog objects when configuring lineage relationships, enabling fine-grained field-level lineage tracking.
tags:
  - lineage
  - columns
  - data-governance
timestamp: "2026-06-19T10:28:52.745Z"
---

# Column-Level External Lineage

**Column-Level External Lineage** is a feature of [Unity Catalog](/concepts/unity-catalog.md) that enables you to capture and visualize the flow of data at the column granularity between external systems and Databricks. While Unity Catalog automatically captures runtime column lineage for queries running on Databricks, column-level external lineage extends this to include columns from external sources (e.g., a MySQL table) or external consumers (e.g., a Tableau dashboard), providing a complete end‑to‑end column‑level view. ^[external-lineage-databricks-on-aws.md]

## How It Works

To add column‑level external lineage, you must first create an [External Metadata Object](/concepts/external-metadata-object.md) that represents the entity in the external system (for example, a table in Salesforce or a dashboard in Power BI). When creating this object, you can optionally specify the columns that belong to it, either one at a time or as a comma‑delimited list. ^[external-lineage-databricks-on-aws.md]

Once the external metadata object exists, you configure a lineage relationship between it and another Unity Catalog object (table, model, path, or another external metadata object). In the relationship, you can include **column mappings** that define how source columns map to target columns. These mappings are applied when you click **Advanced** in the Create lineage relationship dialog. ^[external-lineage-databricks-on-aws.md]

The resulting lineage graph shows the column‑level connections between the external object and Unity Catalog objects, allowing users to trace data provenance or consumption down to individual columns.

## Requirements

To create, modify, or view column‑level external lineage, you need the following privileges on the [Metastore](/concepts/metastore.md) and related objects:

| Privilege | Required for |
|-----------|--------------|
| `CREATE EXTERNAL METADATA` on the [Metastore](/concepts/metastore.md) | Creating an external metadata object |
| `MODIFY` on the external metadata object | Specifying lineage relationships involving that object |
| Read privileges on a Unity Catalog object (e.g., `SELECT` on a table) | Creating a downstream relationship from that object |
| Write privileges on a Unity Catalog object (e.g., `MODIFY` on a table) | Creating an upstream relationship to that object |

^[external-lineage-databricks-on-aws.md]

## Adding Column-Level External Lineage (Manual Methods)

You can add column‑level external lineage using any of the following interfaces:

### Using Catalog Explorer

1. Create an external metadata object:
   - Navigate to **Catalog** > **External data** > **External Metadata** > **Create external metadata**.
   - Fill in the required fields (Name, System type, Entity type).
   - In the **Columns** field (Advanced section), enter the column names. You can use **UI** to enter them one at a time or **Text Input** to provide a comma‑delimited list.
   - Click **Create**.
2. Create a lineage relationship for that object:
   - Select the external metadata object from the **External Metadata** tab.
   - Click **Create lineage relationship**.
   - Choose upstream or downstream.
   - Select the target object type and enter its identifier.
   - Click **Advanced** to add column mappings between the external object and the source/target object. You can also enter other metadata as JSON key‑value pairs.
   - Click **Create**.

### Using the External Lineage API or Databricks SDK for Python

The API and SDK allow programmatic creation of external metadata objects and lineage relationships, including column mappings. See the [External Metadata API](https://docs.databricks.com/api/workspace/externalmetadata) and [External Lineage API](https://docs.databricks.com/api/workspace/externallineage) for details.

## Modeling More Complex Column-Level Lineage

The following patterns help capture realistic data flows with column‑level detail:

- **Connect two Unity Catalog tables with column mappings**: Create an external metadata object that sits between two Unity Catalog tables. Specify one table as upstream and the other as downstream, then define column mappings on both sides so the lineage graph shows how columns flow through the intermediate external system. ^[external-lineage-databricks-on-aws.md]
- **Multiple levels of lineage**: If data passes through several external systems before reaching Databricks, create multiple external metadata objects and link them sequentially, each with its own column mappings. ^[external-lineage-databricks-on-aws.md]
- **Column mappings across object types**: You can map columns between external metadata objects and Unity Catalog tables, models, or paths, as well as between two external metadata objects.

## Limitations

- Column‑level external lineage is **not** recorded in the lineage system tables (`system.access.table_lineage` and `system.access.column_lineage`). It appears only in the lineage graph views within Catalog Explorer. ^[external-lineage-databricks-on-aws.md]
- There are resource limits: up to 10,000 external metadata objects and 100,000 external lineage relationships per [Metastore](/concepts/metastore.md). ^[external-lineage-databricks-on-aws.md]

## Related Concepts

- [External Lineage](/concepts/external-lineage.md) – The parent concept for all non‑Databricks lineage.
- [External Metadata Object](/concepts/external-metadata-object.md) – The securable object that represents an external entity.
- [Data Lineage in Unity Catalog](/concepts/data-lineage-in-unity-catalog.md) – The automatic lineage captured for Databricks queries.
- [Lakeflow Connect Source Lineage](/concepts/lakeflow-connect-source-lineage.md) – Automatic external lineage for managed ingestion pipelines.

## Sources

- external-lineage-databricks-on-aws.md

# Citations

1. [external-lineage-databricks-on-aws.md](/references/external-lineage-databricks-on-aws-d8bef4f2.md)

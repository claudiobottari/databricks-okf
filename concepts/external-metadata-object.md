---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 671e952522f20871f7846ca89b7e9a4dade81a4b90044bfa73c3d70a4b38941e
  pageDirectory: concepts
  sources:
    - external-lineage-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - external-metadata-object
    - EMO
  citations:
    - file: external-lineage-databricks-on-aws.md
title: External Metadata Object
description: A securable object in Unity Catalog that represents an entity in an external system (e.g., a Tableau dashboard, MySQL table, or Power BI report), which can be connected to Unity Catalog objects via lineage relationships.
tags:
  - unity-catalog
  - metadata
  - external-systems
timestamp: "2026-06-19T18:47:07.758Z"
---

```markdown
---
title: External Metadata Object
summary: A securable object in Unity Catalog that represents an entity in an external system, such as a dashboard, table, or report, enabling lineage tracking across system boundaries.
sources:
  - external-lineage-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:17:30.996Z"
updatedAt: "2026-06-19T10:28:22.996Z"
tags:
  - unity-catalog
  - metadata
  - lineage
  - databricks
aliases:
  - external-metadata-object
  - EMO
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# External Metadata Object

An **External Metadata Object** is a securable entity in [[Unity Catalog]] that represents a data asset or system component located outside of Databricks — for example, a Tableau dashboard, a MySQL table, or a Salesforce report. It serves as a placeholder in the Unity Catalog lineage graph, allowing you to connect external sources and sinks to Databricks-managed objects and create an end-to-end view of data flow. ^[external-lineage-databricks-on-aws.md]

## Purpose

Databricks automatically captures runtime data lineage for queries executed inside the platform. However, many data pipelines include upstream systems (such as first-mile ETL tools) and downstream consumers (such as BI dashboards) that run outside Databricks. External metadata objects fill this gap by representing those external assets, so that lineage graphs in Unity Catalog show the complete journey of data — from ingestion to consumption. ^[external-lineage-databricks-on-aws.md]

## Requirements

To create or manage external metadata objects you need the following [[Unity Catalog Privilege Management|Unity Catalog Privileges]]:

| Action | Required privilege |
|--------|-------------------|
| Create an external metadata object | `CREATE EXTERNAL METADATA` on the [[metastore|Metastore]] |
| Specify lineage relationships from an external metadata object to any other Unity Catalog object | `MODIFY` on the external metadata object |
| Specify a downstream lineage relationship *to* a Unity Catalog object (e.g., a table that reads from the external metadata) | Read privilege on the target object (e.g., `SELECT` on a table) |
| Specify an upstream lineage relationship *from* a Unity Catalog object (e.g., a table that is written to the external metadata) | Write privilege on the source object (e.g., `MODIFY` on a table) |

^[external-lineage-databricks-on-aws.md]

## Creating an External Metadata Object

You can create an external metadata object using either the Catalog Explorer UI or the [[External Metadata API]].

### Using Catalog Explorer

1. In your Databricks workspace, click **Catalog**.
2. Go to **External data** → **External Metadata** tab → **Create external metadata**.
3. Fill in the required fields:
   - **Name**: A human-readable name (no spaces).
   - **System type**: Choose from common external systems (e.g., Tableau, MySQL) or select **Custom**.
   - **Entity type**: The kind of object, such as "table" or "dashboard".
4. (Optional) Provide:
   - **URL**: A click-through link to the external asset.
   - **Description**: Free‑text notes.
   - **Columns**: Column names for column‑level lineage mapping.
   - **Properties**: Arbitrary JSON key‑value pairs (e.g., query text, annotations).
5. Click **Create**.

After creation, you are prompted to optionally create lineage relationships. ^[external-lineage-databricks-on-aws.md]

### Using the API

You can also create external metadata objects via the [[External Metadata API]] (endpoint `POST /api/2.1/unity-catalog/external-metadata`), which accepts the same fields as the UI. ^[external-lineage-databricks-on-aws.md]

## Creating Lineage Relationships

Once an external metadata object exists, you can attach it to the lineage graph by creating relationships with other Unity Catalog objects. Relationships can be **upstream** (the external object is a source of data) or **downstream** (the external object consumes data).

To create a relationship in Catalog Explorer:

1. Open the external metadata object (via **Catalog** → **External data** → **External Metadata**).
2. Click **Create lineage relationship**.
3. Select the direction (upstream or downstream).
4. Choose the target object type:
   - **Table** – select from a search dialog.
   - **Model** – select the model and version.
   - **Path** – enter a volume or external location path.
   - **External metadata** – choose another external metadata object.
5. (Optional) Under **Advanced**, add column mappings and JSON metadata.
6. Click **Create**.

After creation, the relationship appears in the **Lineage** tab of all related objects. ^[external-lineage-databricks-on-aws.md]

## Modeling Complex Lineage

- **Connect two Unity Catalog tables**: Create an external metadata object that sits between them. Declare one table as upstream and the other as downstream to the external metadata.
- **Multiple hops**: Create a chain of external metadata objects, each linked through lineage relationships.
- **Column‑level lineage**: When you create the external metadata object, specify column names. Then, when configuring a lineage relationship, map source and target columns. ^[external-lineage-databricks-on-aws.md]

## Limitations

- External lineage is **not recorded** in the lineage system tables (`system.access.table_lineage` and `system.access.column_lineage`). ^[external-lineage-databricks-on-aws.md]
- Per [[metastore|Metastore]] limits: up to **10,000 external metadata objects** and **100,000 external lineage relationships**. See Resource Limits. ^[external-lineage-databricks-on-aws.md]

## Related Concepts

- [[External Lineage]] — The overall mechanism for adding non-Databricks data flow information
- [[Data Lineage in Unity Catalog]] — Captured automatically for queries inside Databricks
- Lakeflow Connect — Automated source lineage for managed ingestion pipelines
- [[External Metadata API]] — REST API for creating and managing external metadata objects
- [[External Lineage API]] — REST API for creating lineage relationships
- [[Unity Catalog Privilege Management|Unity Catalog Privileges]] — Required permissions for management operations
- Resource Limits — Unity Catalog capacity constraints

## Sources

- external-lineage-databricks-on-aws.md
```

# Citations

1. [external-lineage-databricks-on-aws.md](/references/external-lineage-databricks-on-aws-d8bef4f2.md)

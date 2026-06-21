---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5e720d518d70d2392479ead638fd195881d3da4f1612388819012ab6f29b1557
  pageDirectory: concepts
  sources:
    - create-shares-for-opensharing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - schema-level-sharing
    - Schema Sharing
  citations:
    - file: create-shares-for-opensharing-databricks-on-aws.md
title: Schema-Level Sharing
description: Sharing an entire schema in Unity Catalog so recipients automatically gain access to all current and future tables, views, volumes, and models within that schema.
tags:
  - delta-sharing
  - unity-catalog
  - schema-management
timestamp: "2026-06-19T09:37:58.718Z"
---

```yaml
---
title: Schema-Level Sharing
summary: Sharing an entire Unity Catalog schema so recipients automatically get access to all current and future tables, views, volumes, and models within that schema.
sources:
  - create-shares-for-opensharing-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:24:09.031Z"
updatedAt: "2026-06-18T14:55:10.826Z"
tags:
  - delta-sharing
  - unity-catalog
  - data-governance
aliases:
  - schema-level-sharing
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Schema-Level Sharing

**Schema-Level Sharing** is a method of sharing data assets in [[OpenSharing]] where a provider shares an entire schema (database) with one or more recipients. When a schema is added to a share, recipients gain access to all current tables, views, and other supported assets in that schema, plus any future assets added to the schema. This approach simplifies management compared to sharing individual tables. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Overview

A **share** is a securable object in Unity Catalog used to share data with one or more recipients. A share can contain data and AI assets from only one Unity Catalog [[metastore|Metastore]]. ^[create-shares-for-opensharing-databricks-on-aws.md]

When you share an entire schema, recipients can access all of the following at the time of sharing, as well as any such assets added later:

- Tables and table partitions
- Streaming tables
- Managed Iceberg tables
- Views (including dynamic views)
- Materialized views
- Volumes
- Notebooks
- AI models
- Python UDFs
- Genie Spaces
- FeatureSpecs

^[create-shares-for-opensharing-databricks-on-aws.md]

Tables shared this way always include full history. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Requirements and Prerequisites

### Compute Requirements

To add a schema to a share using SQL, you must use a SQL warehouse or compute running Databricks Runtime 13.3 LTS or above. Using Catalog Explorer has no compute requirements. ^[create-shares-for-opensharing-databricks-on-aws.md]

### Permission Requirements

If you are a workspace admin who inherited `USE SCHEMA` and `USE CATALOG` permissions from the workspace admin group, you cannot add a schema to a share until you grant yourself those permissions explicitly. ^[create-shares-for-opensharing-databricks-on-aws.md]

## How to Share a Schema

### Using Catalog Explorer

1. In your Databricks workspace, click **Catalog**.
2. At the top of the **Catalog** pane, select **OpenSharing** from the gear icon menu.
3. On the **Shared by me** tab, find the share and click its name.
4. Click **Manage assets > Edit assets**.
5. On the **Edit assets** page, select an entire schema by first selecting the catalog and then the schema. ^[create-shares-for-opensharing-databricks-on-aws.md]

### Using SQL

**Schema-Level Sharing** requires that the share already exists. Add a schema using the `ALTER SHARE` command:

```sql
ALTER SHARE share_name
ADD SCHEMA schema_name
```
^[create-shares-for-opensharing-databricks-on-aws.md]

### Using the CLI

Use the Databricks Unity Catalog CLI to add schemas to a share. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Limitations

- **Unsupported data assets** are filtered out and not shared. These include tables with liquid clustering and partition filtering, R2 tables with V2 checkpoint, tables with collations enabled, tables with row filters or column masks, `SHALLOW CLONE` tables, and foreign key constraints in shared tables. ^[create-shares-for-opensharing-databricks-on-aws.md]
- **Aliases and partitions are not available** when sharing an entire schema. If you previously created aliases or partitions for any assets in the schema, they are removed when the entire schema is added to the share. ^[create-shares-for-opensharing-databricks-on-aws.md]
- **Schema-level aliasing is not supported.** Schemas with the same name from different catalogs cannot be added to the same share. To work around this, share individual tables with aliased schema names. ^[create-shares-for-opensharing-databricks-on-aws.md]
- If you need to specify advanced options (like aliases or partitions) for a specific table or volume inside a schema, you must share that object individually using SQL and give it an alias with a different schema name. ^[create-shares-for-opensharing-databricks-on-aws.md]

## ABAC and Schema Sharing

When a schema is secured by [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies, the share owner must be a *privileged user* — both the share owner and a user who is excluded from the ABAC policies applied to the data asset. The policy does not govern the recipient's access; recipients have full access to the shared asset. Standard ABAC limitations apply. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Related Concepts

- Share — A securable object in Unity Catalog for sharing data assets
- [OpenSharing](/concepts/opensharing.md) — The framework for sharing data across Databricks and open-source platforms
- [Recipient](/concepts/data-recipient.md) — The entity that receives access to shared data
- [ABAC GRANT Policy](/concepts/abac-grant-policy.md) — Attribute-based access control for granular permissions
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance layer that provides sharing capabilities

## Sources

- create-shares-for-opensharing-databricks-on-aws.md

# Citations

1. [create-shares-for-opensharing-databricks-on-aws.md](/references/create-shares-for-opensharing-databricks-on-aws-1ead08f8.md)

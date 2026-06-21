---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ea768f5197e33e32c5cf2976eb399cf3f1399ccbda1dce093c100fe2fba505b5
  pageDirectory: concepts
  sources:
    - create-shares-for-opensharing-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - schema-level-sharing-in-opensharing
    - SSIO
  citations:
    - file: create-shares-for-opensharing-databricks-on-aws.md
title: Schema-level Sharing in OpenSharing
description: Sharing an entire schema (database) so recipients automatically access all current and future tables, views, models, and volumes within it, with specific limitations on unsupported asset types.
tags:
  - delta-sharing
  - schema
  - data-governance
timestamp: "2026-06-19T14:38:14.195Z"
---

# Schema-level Sharing in OpenSharing

**Schema-level Sharing in OpenSharing** refers to the ability to share an entire schema (database) from Unity Catalog with one or more recipients, granting them access to all current and future data assets within that schema. This approach simplifies data sharing by eliminating the need to manage individual asset permissions.

## Overview

When you share an entire schema, the recipient gains access to all tables, streaming tables, views, materialized views, models, and volumes in the schema at the moment you share it. Additionally, any data and AI assets added to the schema in the future are automatically included in the share. ^[create-shares-for-opensharing-databricks-on-aws.md]

A share can contain data and AI assets from only one Unity Catalog [Metastore](/concepts/metastore.md). You can add or remove data and AI assets from a share at any time. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Requirements

To add a schema to a share using SQL statements, you must use a SQL warehouse or compute running Databricks Runtime 13.3 LTS or above. Using Catalog Explorer to add a schema has no compute requirements. ^[create-shares-for-opensharing-databricks-on-aws.md]

## How to Add a Schema to a Share

You can add a schema to a share using Catalog Explorer, the Databricks Unity Catalog CLI, or SQL commands. The process follows the same steps as adding tables to a share, with the key difference being that you select an entire schema rather than individual tables. ^[create-shares-for-opensharing-databricks-on-aws.md]

When using Catalog Explorer:

1. Navigate to the **OpenSharing** section.
2. Select the share you want to modify.
3. Click **Manage assets > Edit assets**.
4. Select the catalog, then the schema you want to share.
5. Click **Save**.

## Behavior and Features

### Automatic Inclusion of Future Assets

Any tables, views, volumes, and other supported assets added to the schema after the share is created are automatically shared with recipients. This includes all tables, views, and volumes in the schema. ^[create-shares-for-opensharing-databricks-on-aws.md]

### Full History by Default

Tables shared as part of a schema always include full history. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Limitations

Schema-level sharing has several important limitations to consider:

- **Unsupported assets are filtered out**: Schemas can be shared even if they include unsupported data assets. These assets are filtered out and not shared with recipients. Unsupported assets include:
  - Tables that use liquid clustering with partition filtering
  - R2 tables with V2 checkpoint
  - Tables with collations enabled
  - Tables with row filters or column masks
  - `SHALLOW CLONE` tables
  - Foreign key constraints in shared tables ^[create-shares-for-opensharing-databricks-on-aws.md]

- **No aliases or partitions**: Table aliases, partitions, and volume aliases are not available when sharing an entire schema. If you have created aliases or partitions for any assets in the schema, these are removed when you add the entire schema to the share. ^[create-shares-for-opensharing-databricks-on-aws.md]

- **Advanced options require individual sharing**: If you want to specify advanced options for a table or volume in the schema, you must share the table or volume using SQL and give it an alias with a different schema name. ^[create-shares-for-opensharing-databricks-on-aws.md]

- **No schema-level aliasing**: Schemas with the same name from different catalogs cannot be added to the same share. Instead, share individual tables with aliased schema names. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Comparison with Individual Asset Sharing

| Feature | Schema-level Sharing | Individual Asset Sharing |
|---------|---------------------|-------------------------|
| Future assets | Automatically included | Must be added manually |
| Aliases | Not supported | Supported |
| Partitions | Not supported | Supported |
| Advanced options | Not available per asset | Available per asset |
| Management overhead | Lower | Higher |

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) — The overall data sharing framework in Databricks
- [Shares, Providers, and Recipients](/concepts/recipient-and-share-concepts.md) — The core sharing model
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that manages schemas and shares
- [Dynamic Views in OpenSharing](/concepts/databricks-opensharing.md) — Fine-grained access control within shared schemas
- [Recipient Properties](/concepts/recipient-properties.md) — Parameterized partition sharing for data boundaries

## Sources

- create-shares-for-opensharing-databricks-on-aws.md

# Citations

1. [create-shares-for-opensharing-databricks-on-aws.md](/references/create-shares-for-opensharing-databricks-on-aws-1ead08f8.md)

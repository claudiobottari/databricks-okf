---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4540eba5347e39a0e0ce59d99b13848b17a6f0c621b572c32856a3794d2f9ac0
  pageDirectory: concepts
  sources:
    - create-shares-for-opensharing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - schema-level-data-sharing
    - SDS
  citations:
    - file: create-shares-for-opensharing-databricks-on-aws.md
title: Schema-Level Data Sharing
description: "Sharing an entire schema (database) in a share, which provides recipients access to all current and future tables, streaming tables, views, materialized views, models, and volumes in that schema. Tables shared this way always include full history. Has limitations: unsupported assets are filtered out, aliases/partitions are removed, and schema-level aliasing is not supported."
tags:
  - delta-sharing
  - unity-catalog
  - data-governance
timestamp: "2026-06-19T18:02:12.222Z"
---

# Schema-Level Data Sharing

**Schema-Level Data Sharing** is a feature of [OpenSharing](/concepts/opensharing.md) in [Unity Catalog](/concepts/unity-catalog.md) that allows a data provider to share an entire schema (database) with one or more recipients. When a schema is shared, the recipient automatically gains access to all current data assets in the schema, as well as any assets added to the schema in the future. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Overview

A share is a securable object in Unity Catalog used for sharing data assets with recipients. A share can contain data and AI assets from only one Unity Catalog [Metastore](/concepts/metastore.md). Assets can be added or removed from a share at any time. ^[create-shares-for-opensharing-databricks-on-aws.md]

When you share an entire schema, the recipient can access all of the tables, streaming tables, views, materialized views, models, and volumes in the schema at the moment you share it, along with any data and AI assets added to the schema in the future. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Included Assets

Sharing a schema provides recipients with access to the following asset types contained within that schema:

- Tables
- Streaming tables
- Views
- Materialized views
- Models
- Volumes

Tables shared this way always include full history. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Requirements

To add, update, or remove a schema using SQL, you must use a SQL warehouse or compute running Databricks Runtime 13.3 LTS or above. Using Catalog Explorer for the same operations has no compute requirements. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Limitations

Schema-level sharing has several important limitations:

- **Unsupported assets**: You can share schemas even if they include unsupported data assets. These assets are filtered out and not shared with recipients. Unsupported data assets include:
  - Tables that use liquid clustering with partition filtering
  - R2 tables with V2 checkpoint
  - Tables with collations enabled
  - Tables with row filters or column masks
  - `SHALLOW CLONE` tables
  - Foreign key constraints in shared tables

- **No aliases or partitions**: Table aliases, partitions, and volume aliases are not available if you share an entire schema. If you have created aliases or partitions for any assets in the schema, these are removed when you add the entire schema to the share.

- **Advanced options**: If you want to specify advanced options for a table or volume in the schema, you must share the table or volume using SQL and give the table or volume an alias with a different schema name.

- **No schema-level aliasing**: Schemas with the same name from different catalogs cannot be added to the same share. Instead, share individual tables with aliased schema names.

^[create-shares-for-opensharing-databricks-on-aws.md]

## Adding a Schema to a Share

To add a schema to a share, follow the same procedure as adding tables, but select the schema (database) rather than individual tables. The schema can be selected from Catalog Explorer, using SQL commands, or via the Databricks Unity Catalog CLI. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) — The sharing protocol that enables schema-level data sharing
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that manages shares and schemas
- Share — The securable object used for sharing data assets
- [Recipient](/concepts/data-recipient.md) — The entity that receives access to shared data
- [Table Sharing](/concepts/delta-sharing.md) — Sharing individual tables rather than entire schemas
- Dynamic Views — Views that can restrict access at the row and column level using recipient properties

## Sources

- create-shares-for-opensharing-databricks-on-aws.md

# Citations

1. [create-shares-for-opensharing-databricks-on-aws.md](/references/create-shares-for-opensharing-databricks-on-aws-1ead08f8.md)

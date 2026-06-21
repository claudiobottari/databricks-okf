---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 36c0a240ec23e62f00c82e3bb81a84945c0cf30b96eb5eaaa2996525273a68e9
  pageDirectory: concepts
  sources:
    - manage-unity-catalog-metastores-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-metastore-deletion
    - UCMD
  citations:
    - file: manage-unity-catalog-metastores-databricks-on-aws.md
title: Unity Catalog Metastore Deletion
description: Permanent deletion of a Unity Catalog metastore that makes all managed objects inaccessible, auto-deletes managed table data and metadata after 30 days, but does not affect external table data in cloud storage.
tags:
  - unity-catalog
  - metastore
  - administration
timestamp: "2026-06-19T19:28:57.269Z"
---

#Unity Catalog [Metastore](/concepts/metastore.md) Deletion

**Unity Catalog [Metastore](/concepts/metastore.md) Deletion** is the process of permanently removing a [Unity Catalog Metastore](/concepts/unity-catalog-metastore.md) from a Databricks account. This action makes all objects cataloged by the [Metastore](/concepts/metastore.md) inaccessible through Databricks workspaces and cannot be undone. ^[manage-unity-catalog-metastores-databricks-on-aws.md]

## Prerequisites

Only a [Metastore admin](/concepts/metastore-admin-role.md) can delete a [Metastore](/concepts/metastore.md). The deletion must be performed from the Account console. ^[manage-unity-catalog-metastores-databricks-on-aws.md]

## Consequences

- All objects managed by the [Metastore](/concepts/metastore.md) become inaccessible using Databricks workspaces. ^[manage-unity-catalog-metastores-databricks-on-aws.md]
- [Managed table](/concepts/unity-catalog-managed-tables.md) data and metadata undergo automatic deletion after 30 days. ^[manage-unity-catalog-metastores-databricks-on-aws.md]
- Data in External table|external tables residing in your cloud storage is **not** affected by [Metastore](/concepts/metastore.md) deletion. ^[manage-unity-catalog-metastores-databricks-on-aws.md]

## Procedure

1. As a [Metastore](/concepts/metastore.md) admin, log in to the [account console](https://accounts.cloud.databricks.com/).
2. Click the **Catalog** icon to open the Catalog pane.
3. Click the [Metastore](/concepts/metastore.md) name.
4. On the **Configuration** tab, click the three‑button menu at the far upper right and select **Delete**.
5. On the confirmation dialog, enter the name of the [Metastore](/concepts/metastore.md) and click **Delete**.

^[manage-unity-catalog-metastores-databricks-on-aws.md]

## Important Notes

- The action cannot be undone. ^[manage-unity-catalog-metastores-databricks-on-aws.md]
- Managed table data is not deleted immediately; it is auto‑deleted after 30 days, giving a limited window for recovery. ^[manage-unity-catalog-metastores-databricks-on-aws.md]
- External table data remains untouched because it is stored outside the metastore’s control. ^[manage-unity-catalog-metastores-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog Metastore](/concepts/unity-catalog-metastore.md) – The top‑level container for metadata and security policies.
- [Metastore admin](/concepts/metastore-admin-role.md) – The role required to perform deletion.
- Account console – The management interface for account‑level operations.
- [Managed table](/concepts/unity-catalog-managed-tables.md) – Tables whose data is managed by Unity Catalog and will be auto‑deleted.
- External table – Tables whose data resides in your own cloud storage and is unaffected by deletion.
- [Workspace assignment](/concepts/workspace-metastore-assignment.md) – The relationship between workspaces and a [Metastore](/concepts/metastore.md), which is severed on deletion.

## Sources

- manage-unity-catalog-metastores-databricks-on-aws.md

# Citations

1. [manage-unity-catalog-metastores-databricks-on-aws.md](/references/manage-unity-catalog-metastores-databricks-on-aws-6a5c164f.md)

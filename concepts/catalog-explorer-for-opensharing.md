---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7d4fe117eb8fd8e23395e5546012754cfbaf06d6dac1e103cb7d30d7ba4a5969
  pageDirectory: concepts
  sources:
    - manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - catalog-explorer-for-opensharing
    - CEFO
  citations:
    - file: manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md
title: Catalog Explorer for OpenSharing
description: The Databricks UI tool used to visually manage OpenSharing shares, recipients, and grants through the Catalog pane.
tags:
  - delta-sharing
  - databricks
  - user-interface
timestamp: "2026-06-19T19:23:29.941Z"
---

# Catalog Explorer for OpenSharing

**Catalog Explorer for OpenSharing** is a user interface within Databricks Catalog Explorer that enables data providers to manage access to [OpenSharing](/concepts/opensharing.md) data shares. It provides a graphical way to grant, revoke, and view recipients’ access to shares, as an alternative to using SQL commands or the Databricks CLI. ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

## Accessing the Interface

To open Catalog Explorer for OpenSharing:

1. In your Databricks workspace, click the **Catalog** icon.
2. At the top of the **Catalog** pane, click the gear icon and select **OpenSharing**.  
   Alternatively, in the upper-right corner, click **Share > OpenSharing**.

The OpenSharing view is divided into the **Shared by me** tab, which displays the provider’s shares, and a **Recipients** sub-tab. ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

## Prerequisites

To use Catalog Explorer for OpenSharing, you must meet the following requirements:

- The workspace must have a [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md) attached.
- You must use a SQL warehouse or cluster with a Unity-Catalog-capable cluster access mode.
- Shares and recipients must already be defined.

Additionally, you must be one of the following:

- [Metastore](/concepts/metastore.md) admin.
- A user with delegated permissions or ownership on both the share and the recipient objects — specifically, (`USE SHARE` + `SET SHARE PERMISSION`) or share owner **AND** (`USE RECIPIENT`) or recipient owner.

The share owner must also have sufficient permissions on all assets in the share for recipients to access them. ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

## Managing Access

### Adding Recipients to a Share

1. On the **Shared by me** tab, find and select the share.
2. Click **Add recipient**.
3. On the **Add recipient** dialog, type or select the recipient name from the drop-down menu.
4. Click **Add**. ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

### Granting a Share to a Recipient (Starting from the Recipient)

1. On the **Shared by me** tab, click **Recipients** and select the recipient.
2. Click **Grant share**.
3. On the **Grant share** dialog, select the shares to grant.
4. Click **Grant**. ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

### Viewing Recipients of a Share

1. On the **Shared by me** tab, select the share.
2. Go to the **Recipients** tab to see all recipients who have access. ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

### Viewing Shares Granted to a Recipient

1. On the **Shared by me** tab, click **Recipients** and select the recipient.
2. Go to the **Shares** tab to see all shares the recipient can access. ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

### Revoking Access

You can revoke a recipient’s access to a share either from the share or from the recipient.

**Revoking from the share:**

1. On the **Shared by me** tab, select the share.
2. On the **Recipients** tab, find the recipient.
3. Click the kebab menu and select **Revoke**.
4. Confirm revocation.

**Revoking from the recipient:**

1. On the **Shared by me** tab, click **Recipients** and select the recipient.
2. On the **Shares** tab, find the share.
3. Click the kebab menu on the share row and select **Revoke**.
4. Confirm revocation. ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

## Required Permissions for Each Operation

| Operation | Required permission |
|-----------|---------------------|
| Add recipient to share / Grant share | [Metastore](/concepts/metastore.md) admin, or (`USE SHARE` + `SET SHARE PERMISSION` or share owner) AND (`USE RECIPIENT` or recipient owner) |
| View recipients of a share | [Metastore](/concepts/metastore.md) admin, or `USE SHARE` privilege, or share owner |
| View shares granted to a recipient | [Metastore](/concepts/metastore.md) admin, or `USE RECIPIENT` privilege, or recipient owner |
| Revoke access | [Metastore](/concepts/metastore.md) admin, or `USE SHARE` privilege, or share owner |

^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) – The data sharing protocol used.
- [Unity Catalog](/concepts/unity-catalog.md) – The [Metastore](/concepts/metastore.md) that underpins OpenSharing.
- [Data Sharing](/concepts/delta-sharing.md) – Broader concept of sharing data across workspaces and organizations.
- [Catalog Explorer](/concepts/catalog-explorer.md) – General overview of the Databricks Catalog Explorer UI.
- [Delta Sharing](/concepts/delta-sharing.md) – The open standard on which OpenSharing is based.

## Sources

- manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md

# Citations

1. [manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md](/references/manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws-738fc31c.md)

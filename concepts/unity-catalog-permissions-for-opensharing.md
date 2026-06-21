---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7034ccdf981d199abd7ad31eb9703f00e40664d41e38f1074124fbcdb9d38985
  pageDirectory: concepts
  sources:
    - manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-permissions-for-opensharing
    - UCPFO
    - Unity Catalog Permissions for Sharing
  citations:
    - file: manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md
title: Unity Catalog Permissions for OpenSharing
description: The required permissions (metastore admin, USE SHARE, SET SHARE PERMISSION, USE RECIPIENT, and ownership) needed to manage shares and recipients.
tags:
  - delta-sharing
  - unity-catalog
  - access-control
  - permissions
timestamp: "2026-06-19T19:23:19.814Z"
---

# Unity Catalog Permissions for OpenSharing

**Unity Catalog Permissions for OpenSharing** defines the access control model that governs how data providers grant, view, and revoke a recipient's access to an OpenSharing share. Permissions are managed through [Unity Catalog](/concepts/unity-catalog.md) using a combination of metastore-level privileges, object ownership, and delegated permissions on both the share and recipient objects. ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

## Requirements

To share data with recipients, the workspace must have a Unity Catalog [Metastore](/concepts/metastore.md) attached, and the compute resource (SQL warehouse or cluster) must use a Unity-Catalog-capable cluster access mode. Shares and recipients must already be defined before access can be granted. ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

## Required Permissions

Granting share access to recipients requires one of the following: ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

- **Metastore admin** — Full administrative access to the [Metastore](/concepts/metastore.md).
- **Delegated permissions or ownership on both the share and the recipient objects** — The user must have (`USE SHARE` + `SET SHARE PERMISSION`) or be the share owner, **AND** (`USE RECIPIENT`) or be the recipient owner.

As the share owner, you must have sufficient permissions on all assets in the share for recipients to access them. Object creators must grant you access to any new assets added to the schema. ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

## Granting Access

Access can be granted using Catalog Explorer, SQL commands, or the Databricks Unity Catalog CLI. ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

### Using Catalog Explorer (from the share)

1. In your Databricks workspace, click the **Catalog** icon.
2. At the top of the **Catalog** pane, click the gear icon and select **OpenSharing** (or click **Share > OpenSharing** in the upper-right corner).
3. On the **Shared by me** tab, find and select the share.
4. Click **Add recipient**.
5. On the **Add recipient** dialog, start typing the recipient name or click the drop-down menu to select the recipients you want to add.
6. Click **Add**.

### Using Catalog Explorer (from the recipient)

1. Navigate to **Catalog > OpenSharing**.
2. On the **Shared by me** tab, click **Recipients** and select the recipient.
3. Click **Grant share**.
4. On the **Grant share** dialog, start typing the share name or click the drop-down menu to select the shares you want to grant.
5. Click **Grant**.

## Revoking Access

Revoking a recipient's access to a share requires one of the following: [Metastore](/concepts/metastore.md) admin, user with the `USE SHARE` privilege, or share object owner. ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

### Using Catalog Explorer (from the share)

1. Navigate to **Catalog > OpenSharing**.
2. On the **Shared by me** tab, find and select the share.
3. On the **Recipients** tab, find the recipient.
4. Click the kebab menu and select **Revoke**.
5. On the confirmation dialog, click **Revoke**.

### Using Catalog Explorer (from the recipient)

1. Navigate to **Catalog > OpenSharing**.
2. On the **Shared by me** tab, click **Recipients** and select the recipient.
3. On the **Shares** tab, find the share.
4. Click the kebab menu on the share row and select **Revoke**.
5. On the confirmation dialog, click **Revoke**.

## Viewing Current Grants

### Viewing recipients with access to a share

Requires [Metastore](/concepts/metastore.md) admin, `USE SHARE` privilege, or share object owner. ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

1. Navigate to **Catalog > OpenSharing**.
2. On the **Shared by me** tab, find and select the share.
3. Go to the **Recipients** tab to view all recipients who have access to the share.

### Viewing shares granted to a recipient

Requires [Metastore](/concepts/metastore.md) admin, `USE RECIPIENT` privilege, or recipient object owner. ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

1. Navigate to **Catalog > OpenSharing**.
2. On the **Shared by me** tab, click **Recipients** and select the recipient.
3. Go to the **Shares** tab to view all shares that the recipient has access to.

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) — The data sharing protocol used by Databricks
- [Unity Catalog](/concepts/unity-catalog.md) — The underlying governance layer for permissions
- [Delta Sharing](/concepts/delta-sharing.md) — The broader data sharing framework
- Managing Shares for OpenSharing — Creating and configuring shares
- Accessing Shared Data as a Recipient — Recipient-side access workflow
- Auditing and Monitoring Data Sharing — Tracking sharing activity

## Sources

- manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md

# Citations

1. [manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md](/references/manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws-738fc31c.md)

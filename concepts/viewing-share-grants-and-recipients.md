---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cf83f43ce8c87f80e6dbd43e35432dc9ce146e0066e76adf283450d5f92d3509
  pageDirectory: concepts
  sources:
    - manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - viewing-share-grants-and-recipients
    - Recipients and Viewing Share Grants
    - VSGAR
    - Viewing Share Grants
  citations:
    - file: manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md
title: Viewing Share Grants and Recipients
description: Inspecting which recipients have access to a share or which shares a recipient can access using Catalog Explorer, SQL, or CLI.
tags:
  - delta-sharing
  - audit
  - data-sharing
timestamp: "2026-06-19T19:23:17.313Z"
---

# Viewing Share Grants and Recipients

**Viewing Share Grants and Recipients** refers to the process of inspecting which recipients have access to an [OpenSharing](/concepts/opensharing.md) Share and which shares a particular [Recipient](/concepts/data-recipient.md) has been granted. This is a read-only operation that helps data providers audit and monitor data sharing permissions within [Unity Catalog](/concepts/unity-catalog.md). ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

## Viewing Recipients with Access to a Share

To see all recipients that have been granted access to a specific share, you can use [Catalog Explorer](/concepts/catalog-explorer.md), a SQL command, or the Databricks Unity Catalog CLI.

**Permissions required**: You must be a [Metastore](/concepts/metastore.md) admin, a user with the `USE SHARE` privilege, or the share object owner. ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

### Using Catalog Explorer

1. In your Databricks workspace, click the **Catalog** icon.
2. At the top of the Catalog pane, click the gear icon and select **OpenSharing**.
3. On the **Shared by me** tab, find and select the share.
4. Go to the **Recipients** tab to view all recipients who have access to the share. ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

### Using SQL

Run the `SHOW GRANTS ON SHARE` command in a Databricks notebook or the Databricks SQL query editor. For example: ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

```sql
SHOW GRANTS ON SHARE <share-name>;
```

The result lists all principals (recipients) that have been granted access to the share.

### Using the CLI

The Databricks Unity Catalog CLI also supports viewing share grants. Refer to the CLI documentation for the specific command syntax. ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

## Viewing Shares Granted to a Recipient

To see which shares a particular recipient has been granted access to, you can use Catalog Explorer, a SQL command, or the CLI.

**Permissions required**: You must be a [Metastore](/concepts/metastore.md) admin, a user with the `USE RECIPIENT` privilege, or the recipient object owner. ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

### Using Catalog Explorer

1. In your Databricks workspace, click the **Catalog** icon.
2. At the top of the Catalog pane, click the gear icon and select **OpenSharing**.
3. On the **Shared by me** tab, click **Recipients** and select the recipient.
4. Go to the **Shares** tab to view all shares that the recipient has access to. ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

### Using SQL

Run the `SHOW GRANTS TO RECIPIENT` command in a Databricks notebook or the Databricks SQL query editor. For example: ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

```sql
SHOW GRANTS TO RECIPIENT <recipient-name>;
```

The result lists all shares granted to that recipient.

### Using the CLI

The Databricks Unity Catalog CLI provides commands to view shares granted to a recipient. Consult the CLI documentation for exact usage. ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) — The data sharing protocol used for sharing data across Databricks workspaces.
- Share — A logical container for data assets shared with recipients.
- [Recipient](/concepts/data-recipient.md) — A consumer entity that receives access to a share.
- [Unity Catalog](/concepts/unity-catalog.md) — The central governance layer for managing data permissions.
- [Catalog Explorer](/concepts/catalog-explorer.md) — The UI tool for managing shares, recipients, and grants.
- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol underlying OpenSharing.
- [Granting Share Access](/concepts/granting-share-access-to-recipients.md) — The process of adding recipients to a share.
- [Revoking Share Access](/concepts/revoking-share-access-from-recipients.md) — The process of removing a recipient's access to a share.

## Sources

- manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md

# Citations

1. [manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md](/references/manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws-738fc31c.md)

---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 11b8a091de4e77ea01655ca84e1c13cdf417149ea9d872746c1208c69a0904bb
  pageDirectory: concepts
  sources:
    - manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md
    - manage-data-recipients-for-opensharing-databricks-on-aws.md
  confidence: 0.98
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - granting-share-access-to-recipients
    - GSATR
    - Grant Access to Shares
    - Grant access to shares for a recipient
    - Grant and manage share access
    - Granting Share Access
  citations:
    - file: manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md
title: Granting Share Access to Recipients
description: The process of adding a data recipient to an OpenSharing share so they can access the shared data assets.
tags:
  - delta-sharing
  - access-control
  - data-sharing
timestamp: "2026-06-19T19:23:06.833Z"
---

---

title: Granting Share Access to Recipients
summary: How to grant, view, and revoke a recipient’s access to an OpenSharing share on Databricks.
kind: concept
createdAt: "2026-06-19T22:00:00.000Z"
updatedAt: "2026-06-19T22:00:00.000Z"
tags:
  - delta-sharing
  - opensharing
  - data-sharing
aliases:
  - grant-share-access
  - share-permissions
confidence: 1
provenanceState: extracted

---

# Granting Share Access to Recipients

**Granting Share Access to Recipients** is the process of associating a [Recipient (OpenSharing)](/concepts/data-recipient-opensharing.md) object with a [Share (OpenSharing)](/concepts/opensharing.md) so that the recipient can read the shared data. In Databricks OpenSharing, access is managed through Unity Catalog permissions on the share and recipient objects, and can be performed via Catalog Explorer, SQL commands, or the Databricks CLI. ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

## Requirements

Before granting access, the following must be in place:

- A Databricks workspace with a Unity Catalog [Metastore](/concepts/metastore.md) attached.
- A SQL warehouse or cluster using a Unity‑Catalog‑capable access mode.
- Both the [Share (OpenSharing)](/concepts/opensharing.md) and the [Recipient (OpenSharing)](/concepts/data-recipient-opensharing.md) must already exist.
- The user must have one of the following permission sets:
  - [Metastore](/concepts/metastore.md) admin.
  - Delegated permissions or ownership on both the share and the recipient objects — that is, (`USE SHARE` + `SET SHARE PERMISSION`) or share owner, **and** (`USE RECIPIENT`) or recipient owner.

As the share owner, you must also have sufficient permissions on all assets in the share for recipients to access them. ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

## Granting Access

You can grant share access to recipients using any of three interfaces: Catalog Explorer, SQL, or the CLI.

### Using Catalog Explorer

**Starting from the share:**

1. In your Databricks workspace, click **Catalog**.
2. Click the gear icon and select **OpenSharing** (or click **Share > OpenSharing** in the upper‑right corner).
3. On the **Shared by me** tab, find and select the share.
4. Click **Add recipient**.
5. In the dialog, type the recipient name or select from the dropdown, then click **Add**. ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

**Starting from the recipient:**

1. Navigate to **Catalog > OpenSharing > Shared by me > Recipients**.
2. Select the recipient.
3. Click **Grant share**.
4. In the dialog, type the share name or select from the dropdown, then click **Grant**. ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

### Using SQL

Use the `GRANT ON SHARE` statement:

```sql
GRANT ON SHARE <share_name> TO RECIPIENT <recipient_name>;
```

You can run this command in a Databricks notebook or the Databricks SQL query editor. ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

### Using the CLI

Use the Databricks Unity Catalog CLI. The exact command syntax is documented in the Databricks CLI reference. The process follows the same permission requirements. ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

## Viewing Current Grants

You can view which recipients have access to a share, or which shares a recipient can access.

### Viewing Recipients of a Share

**Permissions required:** [Metastore](/concepts/metastore.md) admin, `USE SHARE` privilege, or share owner.

- **Catalog Explorer:** Open the share and go to the **Recipients** tab.
- **SQL:** `SHOW GRANTS ON SHARE <share_name>;`
- **CLI:** Available via `databricks shares ...` commands. ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

### Viewing Shares Granted to a Recipient

**Permissions required:** [Metastore](/concepts/metastore.md) admin, `USE RECIPIENT` privilege, or recipient owner.

- **Catalog Explorer:** Open the recipient detail page and go to the **Shares** tab.
- **SQL:** `SHOW GRANTS TO RECIPIENT <recipient_name>;`
- **CLI:** Available via `databricks recipients ...` commands. ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

## Revoking Access

To remove a recipient’s access to a share, you must be a [Metastore](/concepts/metastore.md) admin, have the `USE SHARE` privilege, or be the share owner.

### Starting from the Share

1. Navigate to the share’s page in Catalog Explorer.
2. Go to the **Recipients** tab.
3. Find the recipient, click the kebab menu, and select **Revoke**.
4. Confirm in the dialog. ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

### Starting from the Recipient

1. Open the recipient detail page.
2. Go to the **Shares** tab.
3. Find the share, click the kebab menu, and select **Revoke**.
4. Confirm in the dialog. ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

### Using SQL

```sql
REVOKE ON SHARE <share_name> FROM RECIPIENT <recipient_name>;
```

Remove the share permission by dropping it from the recipient. ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) — The Databricks Delta Sharing protocol for sharing data outside your organization.
- Create a Share (OpenSharing) — Steps to define a share object.
- [Create a Recipient (OpenSharing)](/concepts/data-recipient-opensharing.md) — Steps to define a recipient object.
- [Manage Recipients (OpenSharing)](/concepts/data-recipient-opensharing.md) — Updating, viewing details, and deleting recipients.
- [Unity Catalog Permissions](/concepts/unity-catalog-permissions-model.md) — How permissions like `USE SHARE` and `USE RECIPIENT` work.

## Sources

- manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md
- manage-data-recipients-for-opensharing-databricks-on-aws.md

# Citations

1. [manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md](/references/manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws-738fc31c.md)

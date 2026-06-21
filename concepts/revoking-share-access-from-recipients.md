---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 60eb0c2491acd8af49a9e854cbc4987aea7f2763b136f4d95643da593bb5fe42
  pageDirectory: concepts
  sources:
    - manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - revoking-share-access-from-recipients
    - RSAFR
    - Revoking Share Access
  citations:
    - file: manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md
title: Revoking Share Access from Recipients
description: The process of removing a recipient's access to an OpenSharing share using Catalog Explorer, SQL, or CLI.
tags:
  - delta-sharing
  - access-control
  - data-sharing
timestamp: "2026-06-19T19:23:03.284Z"
---

# Revoking Share Access from Recipients

**Revoking Share Access from Recipients** is the process of removing a recipient's access to an [OpenSharing](/concepts/opensharing.md) data share in Databricks. This operation can be performed using Catalog Explorer, SQL commands, or the Databricks Unity Catalog CLI.

## Overview

When a data provider needs to stop sharing data with a recipient, they can revoke the recipient's access to a specific share. This action removes the recipient's ability to query or access the shared data assets. ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

## Permissions Required

To revoke a recipient's access to a share, you must be one of the following:

- [Metastore](/concepts/metastore.md) admin
- User with the `USE SHARE` privilege
- Share object owner

^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

## Methods for Revoking Access

### Using Catalog Explorer

You can revoke access starting from either the share or the recipient.

**Starting from the share:**

1. In your Databricks workspace, click the **Catalog** icon.
2. At the top of the **Catalog** pane, click the gear icon and select **OpenSharing**.
3. On the **Shared by me** tab, find and select the share.
4. On the **Recipients** tab, find the recipient.
5. Click the kebab menu and select **Revoke**.
6. On the confirmation dialog, click **Revoke**.

**Starting from the recipient:**

1. In your Databricks workspace, click the **Catalog** icon.
2. At the top of the **Catalog** pane, click the gear icon and select **OpenSharing**.
3. On the **Shared by me** tab, click **Recipients** and select the recipient.
4. On the **Shares** tab, find the share.
5. Click the kebab menu on the share row and select **Revoke**.
6. On the confirmation dialog, click **Revoke**.

^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

### Using SQL

Use the `REVOKE ON SHARE` SQL command in a Databricks notebook or the Databricks SQL query editor. ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

### Using the CLI

The Databricks Unity Catalog CLI also supports revoking share access from recipients. ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) — The data sharing protocol used for sharing data between Databricks workspaces
- [Managing OpenSharing Shares](/concepts/opensharing-share.md) — Creating and managing shares for data providers
- [Granting Share Access to Recipients](/concepts/granting-share-access-to-recipients.md) — The process of adding recipients to a share
- [Viewing Share Grants](/concepts/viewing-share-grants-and-recipients.md) — Checking which recipients have access to a share
- [Unity Catalog](/concepts/unity-catalog.md) — The [Metastore](/concepts/metastore.md) that manages data sharing permissions
- [Delta Sharing](/concepts/delta-sharing.md) — The underlying technology for OpenSharing

## Sources

- manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md

# Citations

1. [manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md](/references/manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws-738fc31c.md)

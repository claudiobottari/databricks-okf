---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e5f7288dc422ece07fa6cc167310782aa2f4e65eb6c3c0c211cb0a3ffc9cadca
  pageDirectory: concepts
  sources:
    - manage-shares-for-opensharing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - share-viewing-interfaces
    - SVI
  citations:
    - file: manage-shares-for-opensharing-databricks-on-aws.md
title: Share Viewing Interfaces
description: "Three interfaces for viewing OpenSharing shares and their details: Catalog Explorer (UI), Databricks Unity Catalog CLI, and SQL commands in notebooks or SQL query editor."
tags:
  - catalog-explorer
  - cli
  - sql
  - delta-sharing
timestamp: "2026-06-19T19:28:44.636Z"
---

# Share Viewing Interfaces

**Share Viewing Interfaces** refers to the tools and methods available in Databricks for viewing OpenSharing shares, their details, and the recipients who have access to them. A *share* is a securable object in Unity Catalog that bundles tables, views, volumes, notebooks, AI models, and other data assets for sharing with one or more recipients. ^[manage-shares-for-opensharing-databricks-on-aws.md]

## Available Interfaces

Users can view shares and share details using three primary interfaces: Catalog Explorer, SQL commands, and the Databricks Unity Catalog CLI. ^[manage-shares-for-opensharing-databricks-on-aws.md]

### Catalog Explorer

To view shares in Catalog Explorer:

1. In your Databricks workspace, click the **Catalog** icon.
2. At the top of the **Catalog** pane, click the gear icon and select **OpenSharing**.
3. Open the **Shares** tab to view a list of shares.
4. View share details on the **Details** tab. ^[manage-shares-for-opensharing-databricks-on-aws.md]

### SQL

Use SQL commands in a Databricks notebook or the Databricks SQL query editor to view shares and their details. ^[manage-shares-for-opensharing-databricks-on-aws.md]

### CLI

Use the Databricks Unity Catalog CLI to view shares and share details. ^[manage-shares-for-opensharing-databricks-on-aws.md]

## Share Details

Share details include the following information:

- The share's owner, creator, creation timestamp, updater, updated timestamp, and comments.
- Data assets in the share.
- Recipients with access to the share. ^[manage-shares-for-opensharing-databricks-on-aws.md]

## Viewing Recipients

To view the list of shares that a recipient has been granted access to, use Catalog Explorer, the Databricks Unity Catalog CLI, or the `SHOW GRANTS TO RECIPIENT` SQL command. ^[manage-shares-for-opensharing-databricks-on-aws.md]

In Catalog Explorer:

1. Click the **Catalog** icon.
2. Click the gear icon and select **OpenSharing**.
3. On the **Shared by me** tab, find and select the recipient.
4. Go to the **Recipients** tab to view the list of recipients who can access the share. ^[manage-shares-for-opensharing-databricks-on-aws.md]

## Requirements

Before viewing shares and share details, users must meet the same requirements as those for creating shares for OpenSharing. ^[manage-shares-for-opensharing-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) — The data sharing protocol used by Databricks.
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that manages shares as securable objects.
- Create shares for OpenSharing — How to create new shares or add data assets to existing shares.
- Manage access to OpenSharing data shares — How to grant recipient access to shares.
- [Manage data recipients for OpenSharing](/concepts/data-recipient-opensharing.md) — How to manage the data recipients you share with.
- [Shares, providers, and recipients](/concepts/recipient-and-share-concepts.md) — The sharing model that underpins OpenSharing.

## Sources

- manage-shares-for-opensharing-databricks-on-aws.md

# Citations

1. [manage-shares-for-opensharing-databricks-on-aws.md](/references/manage-shares-for-opensharing-databricks-on-aws-a4962f9a.md)

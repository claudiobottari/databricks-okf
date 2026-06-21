---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 415661a8ec60e59858c2521a63c0f21ab54597893e87a0ec7d14324bce6f4fd5
  pageDirectory: concepts
  sources:
    - manage-shares-for-opensharing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - share-details-and-metadata
    - Metadata and Share Details
    - SDAM
  citations:
    - file: manage-shares-for-opensharing-databricks-on-aws.md
title: Share Details and Metadata
description: Information associated with a share including owner, creator, creation/update timestamps, comments, contained data assets, and associated recipients.
tags:
  - unity-catalog
  - delta-sharing
  - metadata
timestamp: "2026-06-19T19:28:46.046Z"
---

# Share Details and Metadata

**Share Details and Metadata** refers to the information displayed about an existing OpenSharing share in Databricks. A _share_ is a securable object in [Unity Catalog](/concepts/unity-catalog.md) that bundles tables, views, volumes, notebooks, AI models, and other data assets for sharing with one or more recipients. ^[manage-shares-for-opensharing-databricks-on-aws.md]

## Overview

Share details include the share's owner, creator, creation timestamp, updater, updated timestamp, and comments. Additionally, the details page lists the data assets contained in the share and the recipients who have been granted access to the share. ^[manage-shares-for-opensharing-databricks-on-aws.md]

## Viewing Share Details

To view a list of shares or details about a specific share, use [Catalog Explorer](/concepts/catalog-explorer.md), the Databricks Unity Catalog CLI, or SQL commands in a Databricks notebook or the Databricks SQL query editor. Before viewing share details, you must meet the same requirements as for creating shares. ^[manage-shares-for-opensharing-databricks-on-aws.md]

### Viewing via Catalog Explorer

1. In your Databricks workspace, click the **Catalog** icon.
2. At the top of the **Catalog** pane, click the gear icon and select **OpenSharing**. Alternatively, from the **Quick access** page, click the **OpenSharing >** button.
3. Open the **Shares** tab to view a list of shares.
4. Select a share to view its details on the **Details** tab.

## Viewing Recipients of a Share

To view the list of recipients who can access a share, use Catalog Explorer, the Databricks Unity Catalog CLI, or the `SHOW GRANTS TO RECIPIENT` SQL command. ^[manage-shares-for-opensharing-databricks-on-aws.md]

### Viewing Recipients via Catalog Explorer

1. In your Databricks workspace, click the **Catalog** icon.
2. At the top of the **Catalog** pane, click the gear icon and select **OpenSharing**.
3. On the **Shared by me** tab, find and select the recipient.
4. Go to the **Recipients** tab to view the list of recipients who can access the share.

## Updating Share Details

You can update a share by renaming it, removing tables/views/volumes/schemas, adding or updating comments, renaming a table's alias, enabling or disabling access to a table's history data, adding/updating/removing partition definitions, or changing the share owner. Use Catalog Explorer, the Databricks Unity Catalog CLI, or SQL commands. Note that you cannot use Catalog Explorer to rename the share. ^[manage-shares-for-opensharing-databricks-on-aws.md]

## Important Security Consideration

Who the share owner is affects how authorization and security features, such as [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies, are evaluated. Transferring share ownership to an over-privileged user allows recipients to have over-privileged access if you have a table or schema secured by ABAC policies. ^[manage-shares-for-opensharing-databricks-on-aws.md]

## Deleting a Share

When you delete a share, recipients can no longer access the shared data. To delete a share, use Catalog Explorer, the Databricks Unity Catalog CLI, or the `DELETE SHARE` SQL command. You must be an owner of the share. ^[manage-shares-for-opensharing-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) — The sharing protocol for secure data collaboration
- [Recipients](/concepts/data-recipient.md) — Entities who receive access to shares
- Providers — Entities that create and manage shares
- [Delta Sharing](/concepts/delta-sharing.md) — The underlying open protocol for data sharing
- [Catalog Explorer](/concepts/catalog-explorer.md) — The UI tool for browsing and managing Unity Catalog objects

## Sources

- manage-shares-for-opensharing-databricks-on-aws.md

# Citations

1. [manage-shares-for-opensharing-databricks-on-aws.md](/references/manage-shares-for-opensharing-databricks-on-aws-a4962f9a.md)

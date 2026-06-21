---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2b57c5a56b9dfbd5081d5e37d950b7c0a39624225e16ea7e8a05990c3131ceb0
  pageDirectory: concepts
  sources:
    - manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - opensharing-databricks-delta-sharing
    - O(DS
    - Databricks Delta Sharing
  citations:
    - file: manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md
title: OpenSharing (Databricks Delta Sharing)
description: Databricks' implementation of the Delta Sharing protocol for sharing data across workspaces and platforms using Unity Catalog.
tags:
  - delta-sharing
  - databricks
  - data-sharing
timestamp: "2026-06-19T19:23:32.591Z"
---

Here is the wiki page for "OpenSharing (Databricks Delta Sharing)".

---

## OpenSharing (Databricks Delta Sharing)

**OpenSharing** is the Databricks implementation of the [Delta Sharing](/concepts/delta-sharing.md) protocol for reading and exchanging data across platforms. It is the name used in the Databricks workspace UI and documentation to refer to the Delta Sharing feature set for managing shared data assets. ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

### Overview

OpenSharing enables data providers to share data assets with recipients inside and outside of a Databricks environment. Recipients can access shared data using any Delta Sharing-compatible client, including Databricks, Apache Spark™, pandas, and other tools. ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

### Prerequisites

To share data using OpenSharing, a provider must meet the following requirements:

- Use a Databricks workspace with a [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md) attached.
- Use a SQL warehouse or cluster that uses a Unity-Catalog-capable cluster access mode.
- Have existing **Shares** (the logical grouping of data assets to be shared) and **Recipients** (the users or organizations that receive access) already defined.
- Possess the necessary permissions—typically being a [Metastore](/concepts/metastore.md) admin, or having delegated `USE SHARE` and `SET SHARE PERMISSION` privileges (or share ownership) combined with `USE RECIPIENT` (or recipient ownership). ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

### Granting Access to a Share

To add a recipient to a share, use Catalog Explorer, SQL commands, or the Databricks Unity Catalog CLI.

**Using Catalog Explorer:**

1.  Open the **Catalog** pane and click the gear icon, then select **OpenSharing**.
2.  On the **Shared by me** tab, select the share.
3.  Click **Add recipient**.
4.  Select the recipient from the drop-down and click **Add**. ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

Alternatively, you can start from the **Recipients** page: find the recipient, click **Grant share**, select the share, and click **Grant**. ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

### Revoking Access

To revoke access, use the **Revoke** option from the share's **Recipients** tab or from the recipient's **Shares** tab. The required permission is either being a [Metastore](/concepts/metastore.md) admin, having `USE SHARE` privilege, or being the share owner. ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

### Viewing Grants and Shares

- To see **which recipients** have access to a share, go to the share's **Recipients** tab.
- To see **which shares** a recipient has access to, go to the recipient's **Shares** tab.
- Use `SHOW GRANTS ON SHARE` or `SHOW GRANTS TO RECIPIENT` SQL commands for programmatic inspection. ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

### Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) – The open protocol on which OpenSharing is built.
- [Unity Catalog](/concepts/unity-catalog.md) – The central metadata and governance layer for Databricks data assets.
- [Data Recipient](/concepts/data-recipient.md) – The consumer of a shared data asset.
- Data Provider – The organization or user that owns and shares data.
- Apache Spark – A common engine for consuming Delta Shared data.

### Sources

- manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md

# Citations

1. [manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md](/references/manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws-738fc31c.md)

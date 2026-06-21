---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3bfe12608592d23ac4ab24c695d5f4dfa8bd69082977bb86311eb58be45aae77
  pageDirectory: concepts
  sources:
    - manage-shares-for-opensharing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - share-deletion-implications
    - SDI
  citations:
    - file: manage-shares-for-opensharing-databricks-on-aws.md
title: Share Deletion Implications
description: Deleting an OpenSharing share immediately revokes recipient access to all shared data; only the share owner can perform deletion.
tags:
  - delta-sharing
  - share-management
  - security
timestamp: "2026-06-19T19:28:46.914Z"
---

## Share Deletion Implications

**Share Deletion Implications** refer to the consequences and requirements associated with permanently removing an [OpenSharing](/concepts/opensharing.md) share in Databricks. Deleting a share is an irreversible action that immediately revokes recipient access to all data assets bundled in that share. ^[manage-shares-for-opensharing-databricks-on-aws.md]

### Overview

A share is a [Unity Catalog](/concepts/unity-catalog.md) securable object that groups tables, views, volumes, notebooks, AI models, and other assets for distribution to one or more recipients. When a share is deleted, the underlying data assets are **not** deleted — only the share object itself is removed. Recipients lose the ability to query or read any data that was part of the share. ^[manage-shares-for-opensharing-databricks-on-aws.md]

### Implications for Recipients

*Upon deletion:* recipients can no longer access any of the shared data. ^[manage-shares-for-opensharing-databricks-on-aws.md] The share’s catalog entry is removed from the provider’s side, and any existing recipient tokens or URLs that referenced the share become invalid. There is no graceful degradation; access is cut off immediately after the deletion operation completes. ^[manage-shares-for-opensharing-databricks-on-aws.md]

### Ownership and Authorization Considerations

Only the **owner** of the share may delete it. ^[manage-shares-for-opensharing-databricks-on-aws.md] Ownership also affects how [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies are evaluated for the share’s data assets. If the share owner is an over‑privileged user, recipients may have had over‑privileged access to tables or schemas secured by ABAC policies. Deleting the share eliminates that risk, but it also severs all legitimate access. ^[manage-shares-for-opensharing-databricks-on-aws.md]

### Requirements Before Deletion

Before deleting a share, confirm that:
- You are the share owner (or have been granted ownership).
- All recipients have been notified, or you intend to permanently revoke their access.
- You have reviewed any downstream dependencies (e.g., dashboards, pipelines) that consume the shared data. ^[manage-shares-for-opensharing-databricks-on-aws.md]

### How to Delete a Share

A share can be deleted using:
- **Catalog Explorer** – navigate to the share, open the kebab menu, and select **Delete**; confirm in the dialog. ^[manage-shares-for-opensharing-databricks-on-aws.md]
- **SQL** – `DELETE SHARE <share_name>` command in a Databricks notebook or SQL editor. ^[manage-shares-for-opensharing-databricks-on-aws.md]
- **Databricks CLI** – Unity Catalog CLI commands. ^[manage-shares-for-opensharing-databricks-on-aws.md]

All methods require the caller to be the share owner. ^[manage-shares-for-opensharing-databricks-on-aws.md]

### Related Concepts

- [Share (OpenSharing)](/concepts/opensharing.md)
- Manage Shares for OpenSharing
- [Recipient (OpenSharing)](/concepts/data-recipient-opensharing.md)
- Grant Access to OpenSharing Shares
- [Unity Catalog](/concepts/unity-catalog.md)
- [Delta Sharing](/concepts/delta-sharing.md)
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md)

### Sources

- manage-shares-for-opensharing-databricks-on-aws.md

# Citations

1. [manage-shares-for-opensharing-databricks-on-aws.md](/references/manage-shares-for-opensharing-databricks-on-aws-a4962f9a.md)

---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c1df897ebd3114253ce6561c42479e3ee594c8d3008a543dbff91d73517e4741
  pageDirectory: concepts
  sources:
    - manage-shares-for-opensharing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - opensharing-share-unity-catalog
    - OS(C
  citations:
    - file: manage-shares-for-opensharing-databricks-on-aws.md
title: OpenSharing Share (Unity Catalog)
description: A securable object in Unity Catalog that bundles data assets (tables, views, volumes, notebooks, AI models) for sharing with recipients via Delta Sharing / OpenSharing.
tags:
  - unity-catalog
  - delta-sharing
  - open-sharing
timestamp: "2026-06-19T19:28:14.755Z"
---

---
title: OpenSharing Share (Unity Catalog)
summary: A securable object in Unity Catalog that bundles data assets such as tables, views, volumes, notebooks, and AI models for controlled sharing with recipients.
sources:
  - manage-shares-for-opensharing-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T20:00:00.000Z"
updatedAt: "2026-06-19T20:00:00.000Z"
tags:
  - delta-sharing
  - unity-catalog
  - data-sharing
  - opensharing
aliases:
  - OpenSharing share
  - Share (OpenSharing)
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# OpenSharing Share (Unity Catalog)

An **OpenSharing share** is a securable object in [Unity Catalog](/concepts/unity-catalog.md) that bundles data assets — such as tables, views, volumes, notebooks, AI models, and other catalog objects — for distribution to one or more recipients. Shares are the fundamental mechanism for sharing data using the OpenSharing protocol (formerly Delta Sharing) on Databricks. ^[manage-shares-for-opensharing-databricks-on-aws.md]

## Requirements

All operations on shares — viewing, updating, or deleting — require that you meet the same prerequisites as those listed for creating a share. These typically include the necessary Unity Catalog permissions and the ability to access the **OpenSharing** section in Catalog Explorer, the Databricks CLI, or use SQL commands in a notebook or the SQL query editor. ^[manage-shares-for-opensharing-databricks-on-aws.md]

## Viewing Shares and Share Details

You can list all shares and inspect the details of a specific share using Catalog Explorer, the Databricks Unity Catalog CLI, or SQL commands (such as `SHOW SHARES` or `DESCRIBE SHARE`). ^[manage-shares-for-opensharing-databricks-on-aws.md]

Share details include:
- The share's owner, creator, creation timestamp, last updater, updated timestamp, and any comments.
- The list of data assets (e.g., tables, views, volumes, notebooks, models) that the share contains.
- The recipients who have been granted access to the share. ^[manage-shares-for-opensharing-databricks-on-aws.md]

To see which shares a particular recipient can access, use Catalog Explorer, the CLI, or the `SHOW GRANTS TO RECIPIENT` SQL command. ^[manage-shares-for-opensharing-databricks-on-aws.md]

## Updating a Share

You can modify an existing share in several ways. Supported updates include:
- Renaming the share (not available in Catalog Explorer).
- Removing tables, views, volumes, or schemas from the share.
- Adding or updating a comment.
- Renaming a table alias (the name displayed to the recipient).
- Enabling or disabling access to a table's history data, allowing recipients to perform [Time Travel Queries](/concepts/delta-lake-time-travel.md) or Streaming Reads.
- Adding, updating, or removing partition definitions.
- Changing the share owner. ^[manage-shares-for-opensharing-databricks-on-aws.md]

Ownership of a share affects how authorization and attribute-based access control (ABAC) policies are evaluated. Transferring ownership to an over‑privileged user could allow recipients to gain over‑privileged access if any table or schema in the share is secured by ABAC policies. ^[manage-shares-for-opensharing-databricks-on-aws.md]

## Deleting a Share

When you delete a share, all recipients lose access to the shared data. You must be an owner of the share to delete it. Deletion can be performed using Catalog Explorer, the Databricks Unity Catalog CLI, or the `DELETE SHARE` SQL command. ^[manage-shares-for-opensharing-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The [Metastore](/concepts/metastore.md) that secures and governs shares.
- [OpenSharing](/concepts/opensharing.md) — The protocol used for sharing data across workspaces or platforms.
- [Data Recipient](/concepts/data-recipient.md) — A user or organization that receives a share.
- [Catalog Explorer](/concepts/catalog-explorer.md) — The UI used to manage shares and recipients.
- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol underlying OpenSharing.
- [Share, Provider, Recipient Model](/concepts/recipient-and-share-model.md) — The conceptual model for the sharing topology.

## Sources

- manage-shares-for-opensharing-databricks-on-aws.md

# Citations

1. [manage-shares-for-opensharing-databricks-on-aws.md](/references/manage-shares-for-opensharing-databricks-on-aws-a4962f9a.md)

---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 35b6b81dfcfb0ebb8fd06bfc7c8262d3ad3385cac265f32a2b0688cf1c819ce1
  pageDirectory: concepts
  sources:
    - share-a-genie-space-using-opensharing-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - genie-space-sharing-recipient-management
    - GSSRM
    - OpenSharing Recipient Management
  citations:
    - file: share-a-genie-space-using-opensharing-databricks-on-aws.md
title: Genie Space Sharing Recipient Management
description: The ability to add additional recipients to an existing shared Genie Space snapshot, but inability to modify data assets in the share after creation.
tags:
  - genie-space
  - recipients
  - access-control
timestamp: "2026-06-19T23:04:15.100Z"
---

# Genie Space Sharing Recipient Management

**Genie Space Sharing Recipient Management** refers to the process of granting, managing, and modifying access for recipients who receive shared Genie Space snapshots through [OpenSharing](/concepts/opensharing.md) ([Databricks-to-Databricks Sharing](/concepts/databricks-to-databricks-sharing.md)). This involves selecting recipients, adding new ones after initial sharing, and understanding the limitations around asset modification.

## Overview

When you share a Genie Space using [OpenSharing](/concepts/opensharing.md), Databricks creates a point-in-time snapshot of the space's data assets, instructions, curated SQL examples, SQL functions, and other configuration, then grants access to your selected recipients. Recipients can mount the share to create a local Genie Space pre-loaded with your data and instructions. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]

The snapshot is captured at the moment you click **Share** and does not update when you modify the original space. All recipients see the same fixed snapshot. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]

## Prerequisites

To manage recipients for a shared Genie Space, you must meet the following requirements:

- Have the **Genie Agent Sharing** preview enabled at the account level (see Manage Databricks previews).
- Have [OpenSharing](/concepts/opensharing.md) set up for your account.
- Possess `CREATE SHARE` privilege on the [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md) where the Genie Space's data is registered.
- Have `CAN EDIT` or higher permission on the Genie Space (see [Access control lists](/concepts/table-access-control-tacl.md)).
- Have `SELECT` on all data assets in the space — you must retain this privilege, or recipients cannot access the shared data.
- Have at least one recipient created (see [Create data recipients for OpenSharing](/concepts/data-recipient-opensharing.md)).

^[share-a-genie-space-using-opensharing-databricks-on-aws.md]

## Initial Sharing with Recipients

To share a Genie Space with recipients for the first time:

1. In your Databricks workspace, navigate to the Genie Space you want to share.
2. In the upper-right corner, click **Share**, then click the **External** tab.
3. In the **Select recipients to share with** field, search for and select the recipients with whom you want to share the space.
4. Click **Share**.

If no recipients exist yet, click **Create new recipient** to create them first. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]

## Adding More Recipients

After the initial share is created, you can share the same snapshot with additional recipients:

1. Go to the Genie Space and in the upper-right corner, click **Share**, then click the **External** tab.
2. Search for and select the additional recipients with whom you want to share the space.
3. Click **Add recipients**.

You cannot modify the data assets in the share after you create it. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]

## Managing the Share

The share appears in the **Shared by me** list. The share's asset list is read-only. You can manage recipients and delete the share, but you cannot add or remove data assets manually. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]

For more details, see Manage shares for OpenSharing.

## Limitations

The following limitations apply to Genie Space sharing and recipient management:

- **Snapshot only:** The share captures the Genie Space at the time you click **Share** and does not update when you change the space. All recipients see the same snapshot.
- **Size limit:** The Genie Space configuration must be less than 256 KB when compressed. Spaces that exceed this limit return an error when you attempt to share them. To reduce the size, shorten instructions or descriptions, then try again.
- **Metric views:** Genie Spaces that include metric views cannot be shared.

^[share-a-genie-space-using-opensharing-databricks-on-aws.md]

## Related Concepts

- Genie Space — The conversational AI interface for data analysis.
- [OpenSharing](/concepts/opensharing.md) — The [Databricks-to-Databricks Sharing](/concepts/databricks-to-databricks-sharing.md) protocol.
- [Mount a Shared Genie Space](/concepts/mount-a-shared-genie-space.md) — How recipients access and use the shared space.
- [Create data recipients for OpenSharing](/concepts/data-recipient-opensharing.md) — How to create recipients before sharing.
- Manage shares for OpenSharing — Managing shares after creation.
- [Unity Catalog](/concepts/unity-catalog.md) — The [Metastore](/concepts/metastore.md) where Genie Space data is registered.
- [Access control lists](/concepts/table-access-control-tacl.md) — Permission levels for Genie Space editing.
- [Delta Sharing](/concepts/delta-sharing.md) — The underlying sharing framework.

## Sources

- share-a-genie-space-using-opensharing-databricks-on-aws.md

# Citations

1. [share-a-genie-space-using-opensharing-databricks-on-aws.md](/references/share-a-genie-space-using-opensharing-databricks-on-aws-d29bfca3.md)

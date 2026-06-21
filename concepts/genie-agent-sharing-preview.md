---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 07e6e80fd6983ecb4bdb73b81f39398e24f63925565c32d3c67041ad65118877
  pageDirectory: concepts
  sources:
    - share-a-genie-space-using-opensharing-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - genie-agent-sharing-preview
    - GASP
  citations:
    - file: share-a-genie-space-using-opensharing-databricks-on-aws.md
title: Genie Agent Sharing Preview
description: An account-level preview feature that must be enabled for Genie Space sharing via OpenSharing to work.
tags:
  - genie-space
  - preview
  - account-settings
timestamp: "2026-06-19T23:04:32.634Z"
---

# Genie Agent Sharing Preview

**Genie Agent Sharing Preview** is a Beta feature on Databricks that allows users to share [Genie Spaces](/concepts/genie-space-snapshot.md) with recipients outside their organization using [OpenSharing](/concepts/opensharing.md). When a Genie Space is shared, Databricks creates a point-in-time snapshot of the space's data assets and instructions and makes it available to selected recipients. Recipients can then mount the share to create a local Genie Space pre-loaded with the shared data and instructions. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]

## Requirements

To share a Genie Space using [OpenSharing](/concepts/opensharing.md), the following prerequisites must be met:

- The **Genie Agent Sharing** preview must be enabled at the account level. See Manage Databricks previews for instructions. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]
- [OpenSharing](/concepts/opensharing.md) must be set up for the account. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]
- The user must have the `CREATE SHARE` privilege on the [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md) where the Genie Space's data is registered. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]
- The user must have `CAN EDIT` or higher permission on the Genie Space. See [Access control lists](/concepts/table-access-control-tacl.md). ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]
- The user must have `SELECT` privilege on all data assets in the space. This privilege must be retained; if lost, recipients cannot access the shared data. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]
- At least one recipient must exist. See [Create data recipients for OpenSharing](/concepts/data-recipient-opensharing.md). ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]

## Sharing a Genie Space

To share a Genie Space:

1. In your Databricks workspace, navigate to the Genie Space you want to share. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]
2. In the upper-right corner, click **Share**, then click the **External** tab. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]
3. In the **Select recipients to share with** field, search for and select the recipients with whom you want to share the space. If no recipients exist yet, click **Create new recipient**. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]
4. Click **Share**. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]

Databricks exports a snapshot of the Genie Space, creates a share containing all of the space's tables, instructions, curated SQL examples, SQL functions, and other configuration, and grants the selected recipients access. The snapshot is captured at the time you click **Share**. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]

## Adding More Recipients

After the initial share is created, you can share the same snapshot with additional recipients:

1. Go to the Genie Space and click **Share**, then click the **External** tab. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]
2. Search for and select the additional recipients, then click **Add recipients**. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]

You cannot modify the data assets in the share after you create it. The share appears in the **Shared by me** list. The share's asset list is read-only. You can manage recipients and delete the share, but you cannot add or remove data assets manually. See Manage shares for OpenSharing. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]

## Limitations

- **Snapshot only:** The share captures the Genie Space at the time you click **Share** and does not update when you change the space. All recipients see the same snapshot. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]
- **Size limit:** The Genie Space configuration must be less than 256 KB when compressed. Spaces that exceed this limit return an error when you attempt to share them. To reduce the size, shorten instructions or descriptions, then try again. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]
- **Metric views:** Genie Spaces that include metric views cannot be shared. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]

## Related Concepts

- [Genie Spaces](/concepts/genie-space-snapshot.md)
- [OpenSharing](/concepts/opensharing.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Mount a Shared Genie Space](/concepts/mount-a-shared-genie-space.md)
- Manage shares for OpenSharing
- [Create data recipients for OpenSharing](/concepts/data-recipient-opensharing.md)
- [Access control lists](/concepts/table-access-control-tacl.md)
- Manage Databricks previews

## Sources

- share-a-genie-space-using-opensharing-databricks-on-aws.md

# Citations

1. [share-a-genie-space-using-opensharing-databricks-on-aws.md](/references/share-a-genie-space-using-opensharing-databricks-on-aws-d29bfca3.md)

---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0023f81054c3c3d5e4285b0947c184a63cf28d2c66fd19e3be7cd249cf90b9d7
  pageDirectory: concepts
  sources:
    - share-a-genie-space-using-opensharing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - genie-space-opensharing
    - GSO
    - Share a Genie Space using OpenSharing
  citations:
    - file: share-a-genie-space-using-opensharing-databricks-on-aws.md
title: Genie Space OpenSharing
description: A feature that allows sharing a Genie Space with users outside your organization via a point-in-time snapshot of data assets and instructions.
tags:
  - delta-sharing
  - genie-space
  - collaboration
timestamp: "2026-06-19T23:04:33.951Z"
---

# Genie Space [OpenSharing](/concepts/opensharing.md)

**Genie Space OpenSharing** is a [Beta](https://docs.databricks.com/aws/en/release-notes/release-types) feature on Databricks that allows users to share a Genie Space with recipients outside their organization using [OpenSharing](/concepts/opensharing.md). When a Genie Space is shared, Databricks creates a point-in-time snapshot of the space's data assets, instructions, curated SQL examples, SQL functions, and other configuration, and makes it available to selected recipients. Recipients can then mount the share to create a local Genie Space pre-loaded with the shared data and instructions. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]

## Requirements

To share a Genie Space via [OpenSharing](/concepts/opensharing.md), the following prerequisites must be met:

- The **Genie Agent Sharing** preview must be enabled at the account level. See Manage Databricks previews. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]
- [OpenSharing](/concepts/opensharing.md) must be set up for your account. See [Set up OpenSharing](/concepts/opensharing.md). ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]
- The user must have `CREATE SHARE` privilege on the [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md) where the Genie Space's data is registered. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]
- The user must have `CAN EDIT` or higher on the Genie Space. See [Access control lists](/concepts/table-access-control-tacl.md). ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]
- The user must have `SELECT` on all data assets in the space. This privilege must be retained; if it is lost, recipients cannot access the shared data. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]
- At least one recipient must exist. See [Create data recipients for OpenSharing](/concepts/data-recipient-opensharing.md). ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]

## Process

### Sharing a Genie Space

1. In your Databricks workspace, navigate to the Genie Space you want to share. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]
2. In the upper-right corner, click **Share**, then click the **External** tab. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]
3. In the **Select recipients to share with** field, search for and select the recipients with whom you want to share the space. If no recipients exist yet, click **Create new recipient**. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]
4. Click **Share**. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]

Databricks exports a snapshot of the Genie Space at the moment **Share** is clicked, creates a share containing all the space's tables, instructions, curated SQL examples, SQL functions, and other configuration, and grants the selected recipients access. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]

### Adding More Recipients

After the initial share is created, you can share the same snapshot with additional recipients:

1. Go to the Genie Space and click **Share**, then click the **External** tab. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]
2. Search for and select the additional recipients, then click **Add recipients**. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]

You cannot modify the data assets in the share after it is created. The share appears in the **Shared by me** list, where the asset list is read-only. You can manage recipients and delete the share, but you cannot add or remove data assets manually. See Manage shares for OpenSharing. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]

## Limitations

- **Snapshot only:** The share captures the Genie Space at the time **Share** is clicked and does not update when the space is changed. All recipients see the same snapshot. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]
- **Size limit:** The Genie Space configuration must be less than 256 KB when compressed. Spaces exceeding this limit return an error when attempting to share. To reduce the size, shorten instructions or descriptions, then try again. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]
- **Metric views:** Genie Spaces that include metric views cannot be shared. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]

## Next Steps

- [Mount a Shared Genie Space](/concepts/mount-a-shared-genie-space.md) — Instructions for recipients to mount the shared space
- Manage shares — Managing shares in [OpenSharing](/concepts/opensharing.md)
- [Grant and manage share access](/concepts/granting-share-access-to-recipients.md) — Controlling access to shared shares

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) — The underlying sharing framework for Databricks-to-Databricks data sharing
- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol that powers [OpenSharing](/concepts/opensharing.md)
- Genie Space — The AI-powered conversational analytics tool that can be shared
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer where data assets are registered

## Sources

- share-a-genie-space-using-opensharing-databricks-on-aws.md

# Citations

1. [share-a-genie-space-using-opensharing-databricks-on-aws.md](/references/share-a-genie-space-using-opensharing-databricks-on-aws-d29bfca3.md)

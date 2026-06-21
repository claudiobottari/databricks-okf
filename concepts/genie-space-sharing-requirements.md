---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9b81bceac6e7dbe9659e27bf0421e8b8d66ebf7e9add476fce137f4c918dd353
  pageDirectory: concepts
  sources:
    - share-a-genie-space-using-opensharing-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - genie-space-sharing-requirements
    - GSSR
  citations:
    - file: share-a-genie-space-using-opensharing-databricks-on-aws.md
title: Genie Space Sharing Requirements
description: Prerequisites for sharing a Genie Space, including Genie Agent Sharing preview, OpenSharing setup, CREATE SHARE privilege, CAN EDIT permission, SELECT on data assets, and at least one recipient.
tags:
  - genie-space
  - prerequisites
  - permissions
timestamp: "2026-06-19T23:04:21.434Z"
---

# Genie Space Sharing Requirements

**Genie Space Sharing Requirements** define the prerequisites and constraints for sharing a Genie Space with users outside an organization using [OpenSharing (Delta Sharing)](/concepts/opensharing-delta-sharing.md). When a Genie Space is shared, Databricks captures a point-in-time snapshot of the space’s data assets and instructions and makes it available to selected recipients. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]

## Prerequisites

To share a Genie Space, you must satisfy requirements at the account, [Metastore](/concepts/metastore.md), workspace, data, and recipient levels.

### Account-level requirement

The **Genie Agent Sharing** preview must be enabled at the account level. This preview feature is managed in the Databricks account console under previews. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]

### [OpenSharing](/concepts/opensharing.md) setup

Your account must have [OpenSharing](/concepts/opensharing.md) set up for [Delta Sharing](/concepts/delta-sharing.md). This is the underlying sharing protocol that enables cross-organization sharing. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]

### [Metastore](/concepts/metastore.md) privilege

You need the `CREATE SHARE` privilege on the [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md) where the Genie Space’s data is registered. This privilege allows you to create the share object that represents the exported snapshot. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]

### Genie Space permission

You must have **CAN EDIT** or higher permission on the Genie Space. This is controlled by access control lists (ACLs) for workspace objects. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]

### Data access

You must have `SELECT` privilege on all data assets contained in the space. This privilege must be retained: if you lose it after sharing, recipients will be unable to access the shared data. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]

### Recipients

At least one [recipient (OpenSharing)](/concepts/data-recipient-opensharing.md) must exist before sharing. Recipients are created using the [Databricks-to-Databricks Sharing](/concepts/databricks-to-databricks-sharing.md) workflow. See [Create data recipients for OpenSharing](/concepts/data-recipient-opensharing.md). ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]

## Snapshot behavior

When you click **Share**, Databricks exports a point-in-time snapshot of the Genie Space. This snapshot includes all tables, instructions, curated SQL examples, SQL functions, and other configuration. The share is created and access is granted to the selected recipients. The snapshot is captured at the moment of sharing and does not update automatically when you later modify the Genie Space. All recipients see the same frozen snapshot. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]

After the initial share is created, you can add more recipients, but you cannot modify the data assets in the share. The share appears in the **Shared by me** list; its asset list is read-only. You can manage recipients and delete the share, but you cannot add or remove data assets manually. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]

## Limitations

- **Snapshot only:** The share does not reflect subsequent changes to the Genie Space. To share an updated version, you must create a new share. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]
- **Size limit:** The Genie Space configuration must be less than 256 KB when compressed. Spaces exceeding this limit return an error when you attempt to share them. To reduce size, shorten instructions or descriptions. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]
- **Metric views:** Genie Spaces that include metric views cannot be shared. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]

## Related Concepts

- [Mount a Shared Genie Space](/concepts/mount-a-shared-genie-space.md) – How recipients consume a shared Genie Space.
- Manage shares for OpenSharing – Managing share objects after creation.
- [Grant and manage share access](/concepts/granting-share-access-to-recipients.md) – Controlling recipient permissions on shares.
- Genie Space – The product being shared.

## Sources

- share-a-genie-space-using-opensharing-databricks-on-aws.md

# Citations

1. [share-a-genie-space-using-opensharing-databricks-on-aws.md](/references/share-a-genie-space-using-opensharing-databricks-on-aws-d29bfca3.md)

---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dda438387c8eaeff3f27a8318c5f1b725f269a262a381e4d8c2cb6478c535481
  pageDirectory: concepts
  sources:
    - share-a-genie-space-using-opensharing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - genie-space-snapshot
    - GSS
    - Genie Spaces
  citations:
    - file: share-a-genie-space-using-opensharing-databricks-on-aws.md
title: Genie Space Snapshot
description: A point-in-time capture of a Genie Space's tables, instructions, curated SQL examples, SQL functions, and configuration, created when the Share button is clicked.
tags:
  - genie-space
  - snapshot
  - delta-sharing
timestamp: "2026-06-19T23:03:54.280Z"
---

# Genie Space Snapshot

A **Genie Space Snapshot** is a point-in-time export of a Genie Space’s data assets, instructions, curated SQL examples, SQL functions, and other configuration, created automatically when the space is shared with external recipients using [OpenSharing (Delta Sharing)](/concepts/opensharing-delta-sharing.md). The snapshot allows recipients to mount the share and create a local Genie Space pre-loaded with the original space’s content. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]

## How a Snapshot Is Created

When a user with the required privileges clicks **Share** in a Genie Space and selects recipients on the **External** tab, Databricks exports a snapshot of the current state of the space. This snapshot includes all tables (and their data), instructions, curated SQL examples, SQL functions, and any other configuration that defines the space. The snapshot is captured at the moment of sharing; it does not update automatically when the original space is later changed. The snapshot is then made available to the selected recipients. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]

Additional recipients can be added after the initial share, but they receive the same static snapshot. The share’s asset list is read-only – recipients cannot modify the data assets, and the original sharer cannot add or remove assets manually except by re-sharing the space. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]

## Requirements

To create a Genie Space snapshot, the user must have:

- **Genie Agent Sharing** preview enabled at the account level.
- [OpenSharing](/concepts/opensharing.md) set up for the account.
- `CREATE SHARE` privilege on the [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md) where the space’s data is registered.
- `CAN EDIT` or higher permission on the Genie Space.
- `SELECT` privilege on all data assets in the space (retained for the snapshot to remain accessible).

Additionally, at least one recipient must already exist in [OpenSharing](/concepts/opensharing.md). ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]

## Limitations

- **Snapshot only:** The share is a static snapshot; it does not reflect subsequent changes to the original space. All recipients see the same snapshot for the lifetime of the share.
- **Size limit:** The compressed configuration of the Genie Space must be less than 256 KB. Spaces exceeding this limit return an error when sharing. To reduce the size, shorten instructions or descriptions.
- **Metric views:** Genie Spaces that include metric views cannot be shared, and therefore no snapshot can be created for such spaces. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]

## Related Concepts

- Genie Space
- [OpenSharing (Delta Sharing)](/concepts/opensharing-delta-sharing.md)
- [Delta Sharing](/concepts/delta-sharing.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Mount a Shared Genie Space](/concepts/mount-a-shared-genie-space.md)
- Manage shares for OpenSharing

## Sources

- share-a-genie-space-using-opensharing-databricks-on-aws.md

# Citations

1. [share-a-genie-space-using-opensharing-databricks-on-aws.md](/references/share-a-genie-space-using-opensharing-databricks-on-aws-d29bfca3.md)

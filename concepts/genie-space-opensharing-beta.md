---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1cd323454dd2d92a0112a80786bed9234998200ab90406057402169fddb0671d
  pageDirectory: concepts
  sources:
    - mount-a-shared-genie-space-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - genie-space-opensharing-beta
    - GSO(
  citations:
    - file: mount-a-shared-genie-space-databricks-on-aws.md
title: Genie Space OpenSharing (Beta)
description: A Databricks feature (currently in Beta) that allows data providers to share Genie Spaces with recipients across workspaces using the OpenSharing protocol.
tags:
  - databricks
  - delta-sharing
  - genie
timestamp: "2026-06-19T19:47:08.845Z"
---

#Genie Space OpenSharing (Beta)

**Genie Space OpenSharing (Beta)** is a feature that allows a data provider to share a Genie Space with a recipient in a different Databricks workspace using the [OpenSharing](/concepts/opensharing.md) protocol. The recipient can then mount the shared space locally, creating a full copy in their own workspace that comes pre-loaded with the provider’s data assets, instructions, and curated SQL examples. ^[mount-a-shared-genie-space-databricks-on-aws.md]

## How It Works

When a provider shares a Genie Space via OpenSharing, the recipient receives a share that contains the space’s configuration, data references, and instructions. The recipient mounts the share to their own [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md). Databricks rewrites all table references in the instructions and SQL examples to point to the recipient’s mounted catalog, so the space works immediately without manual reconfiguration. ^[mount-a-shared-genie-space-databricks-on-aws.md]

The recipient gains full ownership of the local space. They can add their own tables and views, edit or extend the instructions, reconfigure the SQL warehouse, and share the space with other users in their workspace. Changes made to the local copy do **not** affect the provider’s original space. ^[mount-a-shared-genie-space-databricks-on-aws.md]

## Requirements

To [Mount a Shared Genie Space](/concepts/mount-a-shared-genie-space.md), the recipient must have: ^[mount-a-shared-genie-space-databricks-on-aws.md]

- `USE PROVIDER` privilege on the Unity Catalog [Metastore](/concepts/metastore.md) (or ownership of the provider object).
- `CREATE CATALOG` privilege on the Unity Catalog [Metastore](/concepts/metastore.md).
- Access to a **Pro** or **Serverless** SQL warehouse in the recipient’s workspace.

## Mounting a Shared Genie Space

The mounting process is performed from the **Catalog** section of the Databricks workspace: ^[mount-a-shared-genie-space-databricks-on-aws.md]

1. Click the **Catalog** icon.
2. At the top of the pane, click the gear icon and select **OpenSharing** (or click **Share → OpenSharing** in the upper-right corner).
3. Find and select the provider that shared the Genie Space.
4. Locate the share containing the Genie Space and click **Mount as Genie agent**.
5. (Optional) Expand **Advanced options** to specify a custom catalog name, SQL warehouse, and workspace folder. Databricks provides sensible defaults.
6. Click **Mount**.

After mounting, the new Genie Space appears in the standard Genie Spaces list in the workspace. The mounted catalog is visible in Catalog Explorer under the specified name.

## What You Get

A mounted Genie Space includes: ^[mount-a-shared-genie-space-databricks-on-aws.md]

- **All of the provider’s data assets** – available through a catalog in the recipient’s Unity Catalog [Metastore](/concepts/metastore.md). The tables and views are **read-only**; the recipient can query them but cannot write.
- **The provider’s instructions, curated SQL examples, and SQL functions** – rewritten automatically to reference the recipient’s mounted catalog, so they work immediately.

## Limitations

- **External sharing restriction**: The recipient cannot share the mounted Genie Space outside their organization using OpenSharing. OpenSharing recipients are not allowed to re‑share data assets received from a provider. ^[mount-a-shared-genie-space-databricks-on-aws.md]

## Related Concepts

- Genie Space – The AI‑powered analytics workspace being shared.
- [Delta Sharing](/concepts/delta-sharing.md) – The underlying open protocol for secure data sharing.
- [OpenSharing](/concepts/opensharing.md) – Databricks’ implementation of Delta Sharing.
- [Unity Catalog](/concepts/unity-catalog.md) – The [Metastore](/concepts/metastore.md) that manages permissions and catalogs.
- [Share a Genie Space using OpenSharing](/concepts/genie-space-opensharing.md) – The provider‑side workflow (referenced in the source).

## Sources

- mount-a-shared-genie-space-databricks-on-aws.md

# Citations

1. [mount-a-shared-genie-space-databricks-on-aws.md](/references/mount-a-shared-genie-space-databricks-on-aws-3f0ef05b.md)

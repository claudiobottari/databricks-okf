---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 45446997003cb739e5023379cbe0110bd4a3866991c4c32f26456b240e3fc9f5
  pageDirectory: concepts
  sources:
    - mount-a-shared-genie-space-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mounted-genie-space-ownership-and-isolation
    - Isolation and Mounted Genie Space Ownership
    - MGSOAI
  citations:
    - file: mount-a-shared-genie-space-databricks-on-aws.md
title: Mounted Genie Space Ownership and Isolation
description: The recipient has full ownership of the mounted Genie Space — changes made locally do not affect the provider's original space, and the recipient can add data, modify instructions, and reconfigure freely.
tags:
  - databricks
  - genie
  - ownership
timestamp: "2026-06-19T19:47:15.101Z"
---

# Mounted Genie Space Ownership and Isolation

**Mounted Genie Space Ownership and Isolation** describes the security and data-access model that applies when a data recipient mounts a shared Genie Space using [OpenSharing](/concepts/opensharing.md). The recipient gains full ownership of the local copy of the space, while the provider’s original space remains completely unaffected. Any modifications the recipient makes are isolated to the local mount and are not reflected back to the provider. ^[mount-a-shared-genie-space-databricks-on-aws.md]

## Full Ownership of the Mounted Space

When a user mounts a shared Genie Space, the resulting local Genie Space is owned entirely by the recipient’s workspace. The recipient can:

- Add their own tables and views to the space.
- Edit or extend the instructions and SQL examples that came with the share.
- Share the space with other users *within* their own workspace.
- Reconfigure or change the SQL warehouse assigned to the space.

The provider has no control over the mounted copy. Changes made by the recipient do not alter the provider’s original Genie Space or any other copies mounted by other recipients. ^[mount-a-shared-genie-space-databricks-on-aws.md]

## Data Isolation and Read-Only Provider Tables

All data assets received from the provider are mounted into a catalog in the recipient’s [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md). These tables are **read-only**—the recipient can query them but cannot write to them. This ensures that the provider’s original data is never modified by the mounting process or by subsequent recipient operations. ^[mount-a-shared-genie-space-databricks-on-aws.md]

The mounting process rewrites all table references in the provider’s instructions, curated SQL examples, and SQL functions to point to the recipient’s mounted catalog. This isolation means the local Genie Space operates as a self-contained copy that references only the recipient’s catalog. ^[mount-a-shared-genie-space-databricks-on-aws.md]

## No External Re-Sharing

A significant isolation limitation is that the recipient **cannot** share the mounted Genie Space with users outside their organization using OpenSharing. OpenSharing recipients are explicitly prohibited from re-sharing data assets received from a provider. This prevents the provider’s data from propagating beyond the intended recipient workspace. ^[mount-a-shared-genie-space-databricks-on-aws.md]

## Related Concepts

- Genie Space – The AI-powered analytics assistant that can be shared and mounted.
- [OpenSharing](/concepts/opensharing.md) – The Delta Sharing protocol used to share Genie Spaces.
- [Unity Catalog](/concepts/unity-catalog.md) – The [Metastore](/concepts/metastore.md) where mounted catalogs are created.
- [Delta Sharing](/concepts/delta-sharing.md) – The underlying technology for sharing data assets across workspaces.
- Read-Only Tables in Delta Sharing – Provider tables are always read-only for recipients.
- Re-sharing Restrictions – OpenSharing recipients cannot re-share received assets.

## Sources

- mount-a-shared-genie-space-databricks-on-aws.md

# Citations

1. [mount-a-shared-genie-space-databricks-on-aws.md](/references/mount-a-shared-genie-space-databricks-on-aws-3f0ef05b.md)

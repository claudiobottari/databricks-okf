---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 89f7ebd299f93f81bf0fbabe53d5f4827099dd1ea874f0405d5ecb442f05a2b7
  pageDirectory: concepts
  sources:
    - mount-a-shared-genie-space-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - genie-space-mount-prerequisites
    - GSMP
  citations:
    - file: mount-a-shared-genie-space-databricks-on-aws.md
title: Genie Space Mount Prerequisites
description: To mount a shared Genie Space, a user needs the USE PROVIDER privilege, CREATE CATALOG privilege on the Unity Catalog metastore, and access to a pro or serverless SQL warehouse.
tags:
  - databricks
  - genie
  - requirements
timestamp: "2026-06-19T19:47:18.715Z"
---

# Genie Space Mount Prerequisites

**Genie Space Mount Prerequisites** are the permissions and infrastructure requirements that a user must satisfy before they can mount a shared Genie Space in their Databricks workspace using [OpenSharing](/concepts/opensharing.md). When a data provider shares a Genie Space via OpenSharing, the recipient can mount that share to create a local Genie Space pre-loaded with the provider’s data assets and instructions. The prerequisites ensure the recipient has the necessary Unity Catalog privileges and a suitable SQL warehouse to complete the mount. ^[mount-a-shared-genie-space-databricks-on-aws.md]

## Requirements

To [Mount a Shared Genie Space](/concepts/mount-a-shared-genie-space.md), you must have the following:

- `USE PROVIDER` privilege on the [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md) in your workspace, **or** ownership of the provider object.
- `CREATE CATALOG` privilege on your Unity Catalog [Metastore](/concepts/metastore.md).
- Access to a **pro** or **serverless** SQL warehouse in your workspace.

These requirements are enforced at mount time. Without them, the mount operation will fail. ^[mount-a-shared-genie-space-databricks-on-aws.md]

## Additional Notes

- The Genie Space sharing feature using OpenSharing is in **Beta**. ^[mount-a-shared-genie-space-databricks-on-aws.md]
- After mounting, the local Genie Space is fully owned by the recipient. The recipient can add their own tables, modify instructions, change the SQL warehouse, and share the space with other users in the same workspace. The provider’s original tables remain read-only. ^[mount-a-shared-genie-space-databricks-on-aws.md]
- The mounted Genie Space cannot be re-shared outside the organization using OpenSharing; recipients cannot re-share data assets received from a provider. ^[mount-a-shared-genie-space-databricks-on-aws.md]

## Related Concepts

- [Mount a Shared Genie Space](/concepts/mount-a-shared-genie-space.md) – The complete workflow for mounting a Genie Space.
- [Share a Genie Space using OpenSharing](/concepts/genie-space-opensharing.md) – How providers share Genie Spaces.
- [Unity Catalog](/concepts/unity-catalog.md) – The metastore-level authorization layer required for the mount.
- SQL warehouse – The compute resource needed to query the mounted space.
- Privileges in Unity Catalog – Details on `USE PROVIDER`, `CREATE CATALOG`, and other permissions.

## Sources

- mount-a-shared-genie-space-databricks-on-aws.md

# Citations

1. [mount-a-shared-genie-space-databricks-on-aws.md](/references/mount-a-shared-genie-space-databricks-on-aws-3f0ef05b.md)

---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 21496ddd8d64775604dc0468811b0112dc71432cef0e0b2ea978c5ef4c3cb4f9
  pageDirectory: concepts
  sources:
    - mount-a-shared-genie-space-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - external-sharing-restriction-for-mounted-genie-spaces
    - ESRFMGS
  citations:
    - file: mount-a-shared-genie-space-databricks-on-aws.md
title: External Sharing Restriction for Mounted Genie Spaces
description: Mounted Genie Spaces cannot be shared with users outside the recipient's organization using OpenSharing; OpenSharing recipients cannot re-share data assets received from a provider.
tags:
  - databricks
  - genie
  - limitations
timestamp: "2026-06-19T19:47:16.868Z"
---

# External Sharing Restriction for Mounted Genie Spaces

The **External Sharing Restriction for Mounted Genie Spaces** is a limitation that prevents users from sharing a mounted Genie Space with recipients outside their organization using [OpenSharing](/concepts/opensharing.md). When a data provider shares a Genie Space via OpenSharing and a recipient mounts it in their own workspace, the resulting local Genie Space cannot be re-shared externally. ^[mount-a-shared-genie-space-databricks-on-aws.md]

## Cause

This restriction stems from a fundamental rule of OpenSharing: recipients of shared data assets cannot re-share those assets with other parties. Even though the mounted Genie Space is a fully owned copy in the recipient’s workspace—allowing modifications to data, instructions, and configuration—the provider’s original data tables remain read-only, and the sharing agreement does not grant redistribution rights beyond the immediate recipient’s organization. ^[mount-a-shared-genie-space-databricks-on-aws.md]

## What You *Can* Do

While external sharing is blocked, you can still:

- Share the mounted space with other users **inside your workspace**.
- Add your own tables and views.
- Edit or extend the provider's instructions and SQL examples.
- Reconfigure the SQL warehouse or workspace folder.
- Query the provider’s tables (read-only). ^[mount-a-shared-genie-space-databricks-on-aws.md]

These capabilities are detailed in the [Mount a Shared Genie Space](/concepts/mount-a-shared-genie-space.md) workflow.

## Related Concepts

- Genie Space – The AI-powered analytics agent that can be shared and mounted.
- [Delta Sharing](/concepts/delta-sharing.md) – The open protocol that enables data sharing across platforms.
- [OpenSharing](/concepts/opensharing.md) – The sharing mechanism used to receive Genie Spaces from providers.
- [Mount a Shared Genie Space](/concepts/mount-a-shared-genie-space.md) – The process of creating a local copy of a shared Genie Space.
- [Unity Catalog](/concepts/unity-catalog.md) – The [Metastore](/concepts/metastore.md) where the mounted catalog is created.

## Sources

- mount-a-shared-genie-space-databricks-on-aws.md

# Citations

1. [mount-a-shared-genie-space-databricks-on-aws.md](/references/mount-a-shared-genie-space-databricks-on-aws-3f0ef05b.md)

---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9dfef5cd0fc9ea9432c21c65ad0e03ab9394b531df5e610f836d03fc2132751f
  pageDirectory: concepts
  sources:
    - share-a-genie-space-using-opensharing-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mount-a-shared-genie-space
    - MASGS
  citations:
    - file: share-a-genie-space-using-opensharing-databricks-on-aws.md
title: Mount a Shared Genie Space
description: The process by which recipients of a shared Genie Space can mount the share to create a local Genie Space pre-loaded with the provider's data and instructions.
tags:
  - genie-space
  - mounting
  - delta-sharing
timestamp: "2026-06-19T23:04:30.873Z"
---

# Mount a Shared Genie Space

**Mount a Shared Genie Space** is the process by which a recipient of a Genie Space shared via [OpenSharing](/concepts/opensharing.md) creates a local copy of that space in their own workspace. The mounted space is pre-loaded with the provider’s data assets and instructions, allowing the recipient to use and modify it as if it were their own. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]

## Overview

When a data provider uses [OpenSharing](/concepts/opensharing.md) to share a Genie Space, recipients can mount the resulting share. Mounting creates a local Genie Space that includes all of the provider’s tables, instructions, curated SQL examples, SQL functions, and other configuration captured in the snapshot. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]

This is the only documented step for recipients; the provider is responsible for initiating the share. For detailed mounting instructions, see the dedicated topic [Mount a Shared Genie Space](/concepts/mount-a-shared-genie-space.md) (which covers prerequisites, the mounting workflow, and limitations). ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) – The sharing protocol used for Genie Space sharing.
- Genie Space – The AI-powered data analysis interface on Databricks.
- [Share a Genie Space using OpenSharing](/concepts/genie-space-opensharing.md) – The provider-side workflow for creating the share.
- [Unity Catalog](/concepts/unity-catalog.md) – The [Metastore](/concepts/metastore.md) where data assets are registered.

## Sources

- share-a-genie-space-using-opensharing-databricks-on-aws.md

# Citations

1. [share-a-genie-space-using-opensharing-databricks-on-aws.md](/references/share-a-genie-space-using-opensharing-databricks-on-aws-d29bfca3.md)

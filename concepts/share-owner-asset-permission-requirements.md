---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8f0c89fc142fe8bcc308fc9dded0803c43affa425376f19a72ecee65c1f10428
  pageDirectory: concepts
  sources:
    - manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - share-owner-asset-permission-requirements
    - SOAPR
  citations:
    - file: manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md
title: Share Owner Asset Permission Requirements
description: The requirement that share owners must have sufficient permissions on all assets in the share for recipients to access them, and object creators must grant access to new assets.
tags:
  - delta-sharing
  - unity-catalog
  - permissions
timestamp: "2026-06-19T19:23:26.600Z"
---

# Share Owner Asset Permission Requirements

**Share Owner Asset Permission Requirements** refers to the permissions that a share owner must hold on all assets within a share in order for data recipients to successfully access those assets. This requirement ensures that the share owner has the authority to share each asset before recipients can view or query it.

## Overview

When a user acts as the share owner for an [OpenSharing](/concepts/opensharing.md) data share, they must have sufficient permissions on every asset included in the share. If the share owner lacks the necessary permissions on any asset, recipients will be unable to access that asset. ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

## Required Permissions

The share owner must hold the appropriate privileges on each shared data asset. Object creators must grant the share owner access to any new assets added to the schema. For a complete list of required permissions on each type of shared data asset, see the [Delta Sharing](/concepts/delta-sharing.md) requirements documentation. ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

## Impact on Recipients

If the share owner does not have sufficient permissions on all assets in the share, recipients will not be able to access those assets. This means that even after a recipient has been granted access to a share, they may encounter errors or missing data if the share owner's permissions are incomplete. ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) — The data sharing protocol used for sharing data across Databricks workspaces.
- [Delta Sharing](/concepts/delta-sharing.md) — The underlying technology for secure data sharing.
- Share Owner — The user who owns and manages a share object.
- [Data Recipient](/concepts/data-recipient.md) — The user or organization that receives access to shared data.
- [Unity Catalog](/concepts/unity-catalog.md) — The [Metastore](/concepts/metastore.md) system that manages permissions for shared assets.

## Sources

- manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md

# Citations

1. [manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md](/references/manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws-738fc31c.md)

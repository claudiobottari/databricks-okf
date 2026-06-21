---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 46db3f6d8782e481a93123a1aa68ff3cf3f79e87735473da462e30535ba954cb
  pageDirectory: concepts
  sources:
    - delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - databricks-clean-rooms
    - DCR
    - Clean Room
    - Clean Rooms
    - Clean Room|clean rooms
    - Clean rooms|clean room
    - clean room
    - clean rooms
  citations:
    - file: delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md
title: Databricks Clean Rooms
description: Secure collaboration environments within Databricks that allow multiple parties to share and jointly analyze data, which can cause deletion blocks on shared securables.
tags:
  - databricks
  - clean-rooms
  - collaboration
timestamp: "2026-06-19T10:07:59.456Z"
---

# Databricks Clean Rooms

**Databricks Clean Rooms** are a secure data collaboration feature in [Unity Catalog](/concepts/unity-catalog.md) that enables organizations to share and collaborate on data without exposing the underlying raw data to each other. Clean rooms provide a controlled environment where multiple parties can jointly analyze data while maintaining data privacy and governance controls. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

## Overview

Clean rooms allow organizations to collaborate on sensitive data by creating a shared workspace where each party retains ownership and control over their data. Data within a clean room can be queried and analyzed, but participants cannot extract or copy raw data from other participants. This enables use cases such as joint customer analytics, advertising attribution, and supply chain optimization without compromising data privacy.

## Securable Objects in Clean Rooms

When a securable object (such as a view or table) is shared via a clean room, specific restrictions are placed on that object to maintain the integrity of the collaboration. Databricks prevents deletion of securable objects that are currently in use by clean rooms. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

## Deletion Restriction

If an attempt is made to delete a securable object that is currently shared in clean rooms, Databricks returns the `DELTA_SHARING_SECURABLE_DELETE_BLOCKED` error with the subcondition `BY_CLEAN_ROOMS`. The error message lists the central clean room IDs where the object is shared, for example:

```
It is shared in clean rooms with central clean room ids: <cleanRoomIds>.
```

The object may also be shared through [OpenSharing](/concepts/opensharing.md) shares at the same time. If the object is both shared via OpenSharing and used in clean rooms, the error message includes both details. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

## Central Clean Room IDs

Each clean room is assigned a unique identifier known as a **central clean room ID**. These IDs appear in error messages when deletion of a shared securable object is blocked. Administrators can use these IDs to identify which clean rooms are using a particular object. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

## Resolution

To update a shared view that is blocked from deletion, use `ALTER VIEW` instead of attempting to drop the object. The preferred workflow is to modify the view definition rather than deleting and recreating it, because deletion is not permitted while the object is still shared in clean rooms. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) – The broader data sharing mechanism in Unity Catalog that can coexist with clean rooms
- [Unity Catalog](/concepts/unity-catalog.md) – The underlying governance layer for clean rooms
- Securable Objects – Objects such as views and tables that can be shared via clean rooms
- Central Clean Room IDs – Identifiers assigned to each clean room that appear in deletion-blocked errors
- [Delta Sharing](/concepts/delta-sharing.md) – The open protocol used for data sharing in clean rooms

## Sources

- delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md

# Citations

1. [delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md](/references/delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws-0eeb76c6.md)

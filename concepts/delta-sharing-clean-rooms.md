---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 966ab5beb7887feeff10c2f35d0dd99e6c6773a5e69e36865a9183803140868e
  pageDirectory: concepts
  sources:
    - delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-sharing-clean-rooms
    - DSCR
  citations:
    - file: delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md
title: Delta Sharing Clean Rooms
description: A mechanism within Delta Sharing where securable objects are shared via clean rooms, with central clean room IDs tracked as a dependency that blocks deletion.
tags:
  - databricks
  - delta-sharing
  - clean-rooms
timestamp: "2026-06-19T15:07:13.515Z"
---

# Delta Sharing Clean Rooms

**Delta Sharing Clean Rooms** is a private compute environment within the [Delta Sharing](/concepts/delta-sharing.md) framework that allows data recipients to query shared data without the data provider exposing the underlying securable objects. Clean rooms enforce that shared data can be consumed but not deleted or altered by the recipient, providing a controlled collaboration space.

## Overview

In [Delta Sharing](/concepts/delta-sharing.md), a clean room is a secure collaboration environment where data is shared under the **OpenSharing** protocol. When a securable (such as a table, view, or share) is shared through a clean room, the provider’s system prevents deletion of that securable because it is actively being served to the clean room. This is enforced through the `DELTA_SHARING_SECURABLE_DELETE_BLOCKED` error condition. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

## Error Condition Context

The only documented reference to clean rooms appears in the error handling for securable deletion. If a user attempts to drop a securable that is currently shared via a clean room, the system returns:

```
<securableType> <securableFullName> cannot be deleted because it is being shared via OpenSharing.
```

When the securable is specifically involved in a clean room, the error includes the sub‑condition `BY_CLEAN_ROOMS`, listing the central clean room IDs:

```
It is shared in clean rooms with central clean room ids: <cleanRoomIds>.
```

^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

The same error message may also mention traditional shares or a combination of shares and clean rooms. The recommendation provided in the error is to use `ALTER VIEW` instead of deleting the underlying object if the user merely needs to update a shared view. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

## Use Cases

Although the source material does not detail the full capabilities of clean rooms, the presence of this error condition indicates that clean rooms are used for:

- **Collaborative analytics** – multiple parties can query shared data without the provider losing control over the original securable.
- **Protected sharing** – providers can avoid accidental or intentional deletion of objects that are actively shared through clean rooms.

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) – The open protocol for secure data sharing across platforms.
- [Open Sharing](/concepts/opensharing.md) – The specific sharing mode (OpenSharing) that enables clean‑room access.
- Securable objects – Database objects (tables, views, shares) that can be shared.
- ALTER VIEW – The recommended alternative to dropping a shared view.

## Sources

- delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md

# Citations

1. [delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md](/references/delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws-0eeb76c6.md)

---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8b552433cb156b9cd3bc1adbb67e044350f88a3460ece6a5b6bc63d147e30e8b
  pageDirectory: concepts
  sources:
    - delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - by_clean_rooms-sub-error
  citations:
    - file: delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md
title: BY_CLEAN_ROOMS Sub-Error
description: A sub-condition of DELTA_SHARING_SECURABLE_DELETE_BLOCKED that appears when the securable is shared through Clean Rooms, listing the central clean room IDs.
tags:
  - databricks
  - clean-rooms
  - delta-sharing
timestamp: "2026-06-19T10:07:54.990Z"
---

---
title: BY_CLEAN_ROOMS Sub-Error
summary: A sub-error of DELTA_SHARING_SECURABLE_DELETE_BLOCKED that occurs when a securable object (e.g., view, table) cannot be deleted because it is shared via clean rooms.
sources:
  - delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T09:30:00.000Z"
updatedAt: "2026-06-19T09:30:00.000Z"
tags:
  - delta-sharing
  - error
  - clean-rooms
aliases:
  - by_clean_rooms-sub-error
  - BCRSE
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# BY_CLEAN_ROOMS Sub-Error

The **BY_CLEAN_ROOMS sub-error** is a specific variant of the DELTA_SHARING_SECURABLE_DELETE_BLOCKED Error|DELTA_SHARING_SECURABLE_DELETE_BLOCKED error condition. It indicates that a securable object (such as a view or table) cannot be deleted because it is currently being shared via [Databricks Clean Rooms](/concepts/databricks-clean-rooms.md) (OpenSharing). The error includes central clean room IDs that identify the clean rooms blocking the deletion. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

## Error Message

The full error message appears under the `DELTA_SHARING_SECURABLE_DELETE_BLOCKED` error class with SQLSTATE `55006` (object not in prerequisite state). The BY_CLEAN_ROOMS variant includes one of the following messages depending on whether the securable is also shared through other means: ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

> `<securableType> <securableFullName>` cannot be deleted because it is being shared via OpenSharing.
> It is shared in clean rooms with central clean room ids: `<cleanRoomIds>`.

If the securable is also shared through Delta Sharing shares, the message combines both reasons:

> It is shared through the following shares: `<shareNames>`. It is shared in clean rooms with central clean room ids: `<cleanRoomIds>`.

## Cause

A securable object (e.g., a view, table, or other object managed in Unity Catalog) is currently part of one or more clean rooms created via OpenSharing. Clean rooms enforce data isolation and require explicit removal of the securable from the clean room before the securable itself can be dropped. The error prevents accidental deletion of data still in use by active clean room collaborations. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

## Resolution

To delete the securable, first remove it from the clean rooms listed in the error message. You must modify or delete the clean room configurations that reference the securable. After the securable is no longer shared in any clean room, retry the drop operation.

If you only intend to update the shared view rather than delete it, use `ALTER VIEW` instead of `DROP VIEW`. Altering the view definition does not break the clean room sharing. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

### Steps to Resolve

1. Identify the clean room IDs from the error message.
2. Using the Databricks UI or API, remove the securable from each listed clean room (or delete the clean room if appropriate).
3. Verify that the securable is no longer part of any clean room.
4. Retry the `DROP` command.

## Related Concepts

- DELTA_SHARING_SECURABLE_DELETE_BLOCKED Error|DELTA_SHARING_SECURABLE_DELETE_BLOCKED error condition – The parent error class with other sub-errors (NO_HINT, BY_SHARES).
- [Databricks Clean Rooms](/concepts/databricks-clean-rooms.md) – The OpenSharing feature that causes this block.
- [Delta Sharing](/concepts/delta-sharing.md) – The underlying protocol for sharing data.
- [SQLSTATE 55006](/concepts/sqlstate-55006.md) – Object not in prerequisite state.

## Sources

- delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md

# Citations

1. [delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md](/references/delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws-0eeb76c6.md)

---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d1a47f91703f4735bc6c5131b59627c41eb2a3d17b9666af26ff4782e767fda6
  pageDirectory: concepts
  sources:
    - delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta_sharing_securable_delete_blocked-error-class
    - DEC
  citations:
    - file: delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md
title: DELTA_SHARING_SECURABLE_DELETE_BLOCKED Error Class
description: A Databricks error that prevents deletion of a securable object (e.g., table, view) that is currently being shared via Delta Sharing's OpenSharing protocol.
tags:
  - databricks
  - error-handling
  - delta-sharing
timestamp: "2026-06-19T10:07:39.111Z"
---

# DELTA_SHARING_SECURABLE_DELETE_BLOCKED Error Class

The **DELTA_SHARING_SECURABLE_DELETE_BLOCKED** error class occurs when a user attempts to delete a securable object (such as a view) that is currently being shared via [OpenSharing](/concepts/opensharing.md). Databricks returns this error to prevent accidental deletion of objects that are in active use through sharing or clean rooms. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

## Error Message

The error message follows this pattern:

```
<securableType> <securableFullName> cannot be deleted because it is being shared via OpenSharing.
```

The full SQLSTATE is [55006](https://docs.databricks.com/aws/en/error-messages/sqlstates#class-55-object-not-in-prerequisite-state) (Class 55: Object not in prerequisite state). ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

## Sub-Conditions

The error includes a sub‑condition identifier that provides context about how the securable is being shared. The possible sub‑conditions are:

### BY_CLEAN_ROOMS[​](#by_clean_rooms)

Indicates the securable is shared in [clean rooms](/concepts/databricks-clean-rooms.md) with central clean room IDs. The message includes the list of clean room IDs. A hint advises using `ALTER VIEW` instead of deleting the object if the goal is only to update the shared view. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

### BY_SHARES[​](#by_shares)

Indicates the securable is shared through shares (the share names are listed). Again, `ALTER VIEW` is suggested as an alternative. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

### Combined BY_CLEAN_ROOMS and BY_SHARES[​](#by_clean_rooms_and_by_shares)

When the securable is shared both through shares and in clean rooms, the message includes both the share names and the central clean room IDs. The hint to use `ALTER VIEW` is still given. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

### NO_HINT[​](#no_hint)

A generic sub‑condition that simply repeats the hint that if the goal is to update a shared view, `ALTER VIEW` should be used instead. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md)
- [Securable objects in Unity Catalog](/concepts/securable-objects-in-unity-catalog.md)
- ALTER VIEW – The recommended alternative to deletion for shared views.
- [Clean Rooms](/concepts/databricks-clean-rooms.md)
- [SQLSTATE 55006](/concepts/sqlstate-55006.md)

## Sources

- delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md

# Citations

1. [delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md](/references/delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws-0eeb76c6.md)

---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b8ad622fe0f561938a5df492799c816c5d751e8e5eb183b84fd3a3bf3346feba
  pageDirectory: concepts
  sources:
    - delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - securable-object-lifecycle-in-delta-sharing
    - SOLIDS
  citations:
    - file: delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md
title: Securable Object Lifecycle in Delta Sharing
description: The constraint that a securable object (e.g., view, table) cannot be dropped while it is actively shared via OpenSharing, shares, or clean rooms, with ALTER VIEW recommended as an alternative.
tags:
  - databricks
  - delta-sharing
  - object-lifecycle
timestamp: "2026-06-19T15:07:14.668Z"
---

# Securable Object Lifecycle in Delta Sharing

**Securable Object Lifecycle in Delta Sharing** describes the operations—create, alter, share, and delete—that can be performed on securable objects (such as views, tables, or schemas) that are exposed through [Delta Sharing](/concepts/delta-sharing.md). The lifecycle is constrained by sharing relationships: once a securable object is included in a share or a [clean room](/concepts/databricks-clean-rooms.md), certain management operations are blocked until the object is removed from those sharing configurations. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

## Deletion Constraint

A securable object **cannot be deleted** while it is being shared via OpenSharing. Attempting to delete such an object raises the `DELTA_SHARING_SECURABLE_DELETE_BLOCKED` error (SQLSTATE `55006` – Object not in prerequisite state). The error message indicates the securable type and full name and specifies why the deletion is blocked. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

### Sub‑Conditions

The error class distinguishes three scenarios based on how the object is shared:

**BY\_CLEAN\_ROOMS**  
The object is shared in clean rooms. The error lists the central clean room IDs. The user is informed that if they only need to update a shared view, they should use `ALTER VIEW` instead. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

**PROVIDER\_ONLY\_SHARES**  
The object is shared directly through shares. The error lists the names of the shares. The same recommendation to use `ALTER VIEW` for view updates is given. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

**BOTH**  
The object is shared both in clean rooms and through shares. The error lists both the central clean room IDs and the share names. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

### NO\_HINT

When no additional hint can be provided, the error simply states: “If you just want to update a shared view, please use `ALTER VIEW` instead.” ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

## Workaround

To delete a securable object that is currently shared, you must first remove it from all shares and clean rooms. Alternatively, if the goal is to modify an object rather than delete it (for example, updating a view definition), use `ALTER VIEW` or the appropriate `ALTER` DDL command. The error message explicitly recommends this path. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) – The open protocol for sharing data across platforms.
- Clean rooms – Secure environments for collaborative analytics on shared data.
- [Shared views](/concepts/opensharing-views.md) – Views that are shared via Delta Sharing; their definitions can be updated without dropping and recreating.
- [SQLSTATE 55006](/concepts/sqlstate-55006.md) – The standard SQL error class for “object not in prerequisite state”.
- ALTER VIEW – The DDL command to modify a view definition without affecting its sharing metadata.

## Sources

- delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md

# Citations

1. [delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md](/references/delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws-0eeb76c6.md)

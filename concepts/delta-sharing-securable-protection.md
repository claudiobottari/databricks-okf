---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: df27d506c3ffe3d7934a2b44b5f303041f34b7a707e9487bd64d7e166507aefb
  pageDirectory: concepts
  sources:
    - delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - delta-sharing-securable-protection
    - DSSP
  citations:
    - file: delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md
title: Delta Sharing Securable Protection
description: The security principle that securable objects (tables, views) actively shared via OpenSharing or used in clean rooms cannot be deleted until sharing is revoked.
tags:
  - delta-sharing
  - security
  - governance
timestamp: "2026-06-18T15:21:50.207Z"
---

Here is the wiki page for "Delta Sharing Securable Protection".

---

## Delta Sharing Securable Protection

**Delta Sharing Securable Protection** is a safeguard in [Unity Catalog](/concepts/unity-catalog.md) that prevents the deletion of securable objects (such as tables, views, or schemas) when they are actively being shared via [Delta Sharing](/concepts/delta-sharing.md) or used in [clean rooms](/concepts/databricks-clean-rooms.md). This protection ensures that data consumers do not lose access to shared data due to accidental or unauthorized deletion of the underlying securable.

### Error Condition

When a user attempts to delete a securable that is currently shared, the system raises a `DELTA_SHARING_SECURABLE_DELETE_BLOCKED` error. The error message includes the type and full name of the securable and indicates that it cannot be deleted because it is being shared via OpenSharing. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

The error has two sub-categories that provide additional context:

- **BY_CLEAN_ROOMS**: The securable is shared in clean rooms. The error lists the central clean room IDs and the share names through which the securable is shared. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]
- **NO_HINT**: The securable is shared, but no additional context about clean rooms is provided. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

### Resolution

To resolve the error, the user must first remove the securable from all shares and clean rooms before attempting to delete it. Alternatively, if the intent is to update a shared view rather than delete it, the error message recommends using `ALTER VIEW` instead. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

### Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol for sharing data across platforms.
- [Clean Rooms](/concepts/databricks-clean-rooms.md) — Secure environments for collaborative data analysis.
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that enforces securable protection.
- Securable Objects — The objects (tables, views, schemas) protected by this mechanism.

## Sources

- delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md

# Citations

1. [delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md](/references/delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws-0eeb76c6.md)

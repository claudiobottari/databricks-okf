---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 68711a6234db72c603ddab1d4bc6c6949ce782f1a1faa3cf6c6ebc4389a7e563
  pageDirectory: concepts
  sources:
    - delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sqlstate-55006
  citations:
    - file: delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md
title: SQLSTATE 55006
description: ANSI/ISO SQL standard state 'object not in prerequisite state', which this Databricks error maps to, indicating the object is in a state that prevents the requested operation.
tags:
  - databricks
  - sqlstate
  - error-standards
timestamp: "2026-06-19T18:26:59.442Z"
---

---
title: SQLSTATE 55006
summary: An error that occurs when attempting to delete a securable object (such as a table or view) that is currently being shared via Open Sharing in Delta Sharing or used in clean rooms. The securable cannot be deleted until it is removed from all shares and clean rooms.
sources:
  - delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:00:00.000Z"
updatedAt: "2026-06-18T12:00:00.000Z"
tags:
  - error
  - delta-sharing
  - sqlstate
  - databricks
aliases:
  - sqlstate-55006
  - object-not-in-prerequisite-state
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# SQLSTATE 55006

**SQLSTATE 55006** is an error condition that belongs to the SQLSTATE class **55 – Object not in prerequisite state**. On Databricks it is raised when a user attempts to delete a securable object (for example, a table, view, or schema) that is currently being shared through [Delta Sharing](/concepts/delta-sharing.md)'s Open Sharing protocol or used in a [Clean rooms|clean room](/concepts/databricks-clean-rooms.md). The deletion is blocked because the object is in a state that does not allow the operation. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

## Error Details

The full error message follows the pattern:

```
<securableType> <securableFullName> cannot be deleted because it is being shared via OpenSharing.
```

The error includes one of several sub-condition identifiers that provide additional context:

- **BY_CLEAN_ROOMS**: The securable is used in clean rooms. The message includes the central clean room IDs and the share names.
- **NO_HINT**: The securable is shared through Open Sharing, but no additional context is provided beyond the basic message.
- **Combined**: A combination of `BY_CLEAN_ROOMS` and share names may appear if both apply.

All sub-conditions include the same resolution guidance: "If you just want to update a shared view, please use `ALTER VIEW` instead." ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

## Cause

The securable object cannot be deleted because it is actively referenced in one or more active [Delta Sharing](/concepts/delta-sharing.md) shares (Open Sharing) or is part of a clean room. Deleting the object would break the sharing contracts or the clean room definitions, so the system prevents the operation. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

## Solutions

### For a shared securable (not in a clean room)

1. Remove the object from all Delta Sharing shares that reference it.
2. After removal, retry the `DROP` operation.

Alternatively, if the goal is to modify the object rather than remove it entirely, use `ALTER` statements instead of `DROP`. The error message explicitly advises using `ALTER VIEW` to update a shared view. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

### For a securable in a clean room

1. Remove the object from the clean room(s) that reference it (by central clean room ID).
2. Then retry the deletion.

### General approach

- Use `ALTER` (e.g., `ALTER VIEW ... AS ...`) to update the definition of a shared view without deleting and recreating it.
- If deletion is necessary, first revoke the object from all shares and clean rooms that depend on it. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol for sharing data across platforms.
- [Open Sharing](/concepts/opensharing.md) — A sharing mode that uses Delta Sharing protocol without requiring a recipient account.
- Clean rooms — Secure environments for collaborative analysis without exposing raw data.
- SQLSTATE class 55 — The parent error class for "object not in prerequisite state".
- ALTER VIEW — Statement used to modify a view without dropping it.
- DROP TABLE / DROP VIEW — The operations that can trigger SQLSTATE 55006.

## Sources

- delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md

# Citations

1. [delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md](/references/delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws-0eeb76c6.md)

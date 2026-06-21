---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 488e42cc1a6a2870c539a15ce84dc7e36317ccd1a8d89ce96a338c38dd1d7e3c
  pageDirectory: concepts
  sources:
    - delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta_sharing_securable_delete_blocked-error
    - DELTA_SHARING_SECURABLE_DELETE_BLOCKED
    - DELTA_SHARING_SECURABLE_DELETE_BLOCKED error condition
    - delta_sharing_securable_delete_blocked-error-class
    - DEC
  citations:
    - file: delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md
title: DELTA_SHARING_SECURABLE_DELETE_BLOCKED Error
description: A Databricks error (SQLSTATE 55006) raised when a securable object cannot be deleted because it is actively shared via Delta Sharing (OpenSharing).
tags:
  - databricks
  - error-message
  - delta-sharing
timestamp: "2026-06-19T18:26:47.614Z"
---

---
title: DELTA_SHARING_SECURABLE_DELETE_BLOCKED Error
summary: A Databricks error (SQLSTATE 55006) raised when attempting to delete a securable object that is currently shared via Delta Sharing's OpenSharing protocol.
sources:
  - delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:55:16.485Z"
updatedAt: "2026-06-19T15:07:02.263Z"
tags:
  - databricks
  - delta-sharing
  - error-messages
aliases:
  - delta_sharing_securable_delete_blocked-error
confidence: 1
provenanceState: extracted
inferredParagraphs: 2
---

# DELTA_SHARING_SECURABLE_DELETE_BLOCKED Error

The **DELTA_SHARING_SECURABLE_DELETE_BLOCKED** error occurs when a user attempts to drop or delete a securable object (such as a table, view, or model) that is currently being shared through [Delta Sharing](/concepts/delta-sharing.md). The error prevents deletion to protect ongoing sharing agreements. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

## SQLSTATE

The error is classified under SQLSTATE **55006**, which indicates that the object is not in a prerequisite state for the requested operation. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

## Error Message Structure

The error message follows the pattern:

```
<securableType> <securableFullName> cannot be deleted because it is being shared via OpenSharing.
```

Depending on the specific sharing configuration, the message includes one of the following sub‑conditions: ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

| Sub‑condition | Additional details |
|---------------|-------------------|
| `BY_CLEAN_ROOMS` | Lists the central clean room IDs where the securable is used. |
| `BY_SHARES` | Lists the share names through which the securable is shared. |
| `BY_CLEAN_ROOMS` + `BY_SHARES` | Combines both clean room IDs and share names. |
| `NO_HINT` | No further information; the object is simply blocked from deletion. |

All variants include the suggestion: “If you just want to update a shared view, please use `ALTER VIEW` instead.” ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

## Common Causes

- The securable is included in one or more active Delta Shares.
- The securable is referenced in a [Clean Room](/concepts/databricks-clean-rooms.md) job.
- The object is under an [OpenSharing](/concepts/opensharing.md) provider relationship.

These causes follow directly from the error condition: any securable that is part of an active share or clean room cannot be deleted until the sharing relationship is removed.

## How to Resolve

To delete the securable, you must first remove it from all Delta Shares and/or Clean Rooms that reference it.

1. **For shares**: Remove the object from the share using `ALTER SHARE … REMOVE` or the Catalog Explorer.
2. **For clean rooms**: Remove the object from the clean room definition.
3. **For views**: If you only need to modify the view definition, use `ALTER VIEW` instead of dropping and recreating it.

After the object is no longer shared, you can safely drop it using `DROP TABLE`, `DROP VIEW`, or `DROP MODEL`.

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol for sharing data across platforms.
- [OpenSharing](/concepts/opensharing.md) — Databricks' implementation of Delta Sharing.
- [Clean Rooms](/concepts/databricks-clean-rooms.md) — Secure environments for collaborative data analysis.
- ALTER VIEW — SQL command to modify a view without dropping it.
- [SQLSTATE 55006](/concepts/sqlstate-55006.md) — Object not in prerequisite state.

## Sources

- delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md

# Citations

1. [delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md](/references/delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws-0eeb76c6.md)

---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e4b8d7cb6af43da2f8ca9f3f566b3cee8299b63cfbe97dbc79876dc38557b15e
  pageDirectory: concepts
  sources:
    - delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sqlstate-55006-object-not-in-prerequisite-state
    - S5—ONIPS
  citations:
    - file: delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md
title: SQLSTATE 55006 — Object Not in Prerequisite State
description: A SQL standard error class (class 55) indicating the target object cannot be modified because it is not in the required prerequisite state, used here when a shared securable is blocked from deletion.
tags:
  - sql
  - error-handling
  - databricks
timestamp: "2026-06-19T10:07:48.321Z"
---

```markdown
---
title: SQLSTATE 55006 — Object Not in Prerequisite State
summary: A SQL standard error class indicating that an object operation (e.g., delete) cannot proceed because the object is not in the required prerequisite state (e.g., it is currently shared).
sources:
  - delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T15:22:00.644Z"
updatedAt: "2026-06-18T15:22:00.644Z"
tags:
  - sqlstate
  - error-class
  - database-errors
aliases:
  - sqlstate-55006-object-not-in-prerequisite-state
  - S5—ONIPS
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 1
---

# SQLSTATE 55006 — Object Not in Prerequisite State

**SQLSTATE 55006** is a class-55 error condition indicating that an operation cannot be completed because the target object is not in the prerequisite state required by the command. In Databricks, this error often appears as the `DELTA_SHARING_SECURABLE_DELETE_BLOCKED` error when a user attempts to delete a securable (such as a table or view) that is actively being shared via [[OpenSharing]]. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

## Error Message

The general form of the error is:

```
<securableType> <securableFullName> cannot be deleted because it is being shared via OpenSharing.
```

The message includes the type and full name of the securable that could not be deleted. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

## Sub‑Error Categories

The error provides one or more sub‑error messages that describe the specific sharing context. Each sub‑error also suggests using `ALTER VIEW` instead if the intent is only to update a shared view. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

### BY_CLEAN_ROOMS

The securable is shared in [[Databricks Clean Rooms|clean rooms]]. The message includes the central clean room IDs:

```
It is shared in clean rooms with central clean room ids: <cleanRoomIds>.
```

### BY_SHARES

The securable is shared through one or more shares. The message lists the share names:

```
It is shared through the following shares: <shareNames>.
```

### Combined

When the securable is shared through both shares and clean rooms, the error lists all relevant identifiers:

```
It is shared through the following shares: <shareNames>.
It is shared in clean rooms with central clean room ids: <cleanRoomIds>.
```

### NO_HINT

No additional hints are provided beyond the basic suggestion to use `ALTER VIEW`. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

## Resolution

Because the securable is part of an active [[Delta Sharing]] relationship, it cannot be deleted directly. If the goal is to modify the definition of a shared view, use ALTER VIEW instead of attempting to drop the object. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

## Related Concepts

- SQLSTATE
- [[Delta Sharing]]
- [[OpenSharing]]
- [[Databricks Clean Rooms|Clean Rooms]]
- ALTER VIEW
- Securable

## Sources

- delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md
```

# Citations

1. [delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md](/references/delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws-0eeb76c6.md)

---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a9bad2fd3f0a30a1825ae7aee9e93379f2d78839587fe8573d38ee08387c0ab9
  pageDirectory: concepts
  sources:
    - delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - no_hint-sub-error
    - IN subquery
  citations:
    - file: delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md
title: NO_HINT Sub-Error
description: A sub-condition of DELTA_SHARING_SECURABLE_DELETE_BLOCKED with no additional context, simply advising the user to use ALTER VIEW instead of deleting.
tags:
  - databricks
  - delta-sharing
  - error-messages
timestamp: "2026-06-19T10:08:11.412Z"
---

## NO_HINT Sub-Error

**NO_HINT** is a sub-error that appears within the DELTA_SHARING_SECURABLE_DELETE_BLOCKED error condition. It provides a fallback message when no specific reason is available for why a securable object (such as a view) cannot be deleted. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

### Error Message

When the `DELTA_SHARING_SECURABLE_DELETE_BLOCKED` error occurs with the `NO_HINT` sub-error, the system returns the following message: ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

> If you just want to update a shared view, please use `ALTER VIEW` instead.

### Context

This sub-error is part of the [SQLSTATE 55006](/concepts/sqlstate-55006.md) class, which indicates an "Object not in prerequisite state" condition. It is raised when a securable object is being shared via OpenSharing ([Delta Sharing](/concepts/delta-sharing.md)) and cannot be deleted due to sharing constraints. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

### Related Sub-Errors

The `DELTA_SHARING_SECURABLE_DELETE_BLOCKED` error condition includes several possible sub-errors that provide more specific context: ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

| Sub-Error | Meaning |
|-----------|---------|
| `BY_CLEAN_ROOMS` | Object is shared in [Clean Rooms](/concepts/databricks-clean-rooms.md) |
| `BY_SHARES` | Object is shared through specific shares |
| `BY_SHARES_AND_CLEAN_ROOMS` | Object is shared through both shares and clean rooms |
| `NO_HINT` | No specific reason available; generic fallback message |

### Usage

When you encounter the `NO_HINT` sub-error, it means the system cannot determine the specific sharing mechanism that is blocking the deletion. The recommended action is to use `ALTER VIEW` instead of attempting to delete the view. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

This is a catch-all sub-error that appears when none of the more specific sub-errors (like `BY_CLEAN_ROOMS` or `BY_SHARES`) apply to the situation. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

### Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) - Open sharing protocol for data collaboration
- [Clean Rooms](/concepts/databricks-clean-rooms.md) - Secure collaboration environments for shared data
- [SQLSTATE 55006](/concepts/sqlstate-55006.md) - Error class for object not in prerequisite state

## Sources

- delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md

# Citations

1. [delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md](/references/delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws-0eeb76c6.md)

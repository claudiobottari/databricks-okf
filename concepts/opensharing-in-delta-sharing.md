---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 73246b6597eca7e245ddc6a93ad46d6d729df6116d16cf33bf1d63ea12fcfc33
  pageDirectory: concepts
  sources:
    - delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md
  confidence: 0.8
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - opensharing-in-delta-sharing
    - OIDS
  citations:
    - file: delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md
title: OpenSharing in Delta Sharing
description: The sharing protocol underlying Databricks Delta Sharing that, when active on a securable object, blocks its deletion to prevent breaking active sharing recipients.
tags:
  - databricks
  - delta-sharing
  - sharing-protocol
timestamp: "2026-06-19T15:07:10.456Z"
---

# OpenSharing in Delta Sharing

**OpenSharing** is a feature in [Delta Sharing](/concepts/delta-sharing.md) that allows securable objects (such as tables, views, and other data assets) to be shared with recipients. When a securable is shared through OpenSharing, it becomes protected from deletion until the sharing relationship is removed. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

## DELTA_SHARING_SECURABLE_DELETE_BLOCKED Error

Attempting to delete a securable that is currently shared via OpenSharing raises the error class `DELTA_SHARING_SECURABLE_DELETE_BLOCKED` with SQLSTATE `55006`. The error message identifies the securable type and full name and explains why deletion is blocked. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

The error presents one of three sub‑conditions depending on how the securable is shared:

- **BY_CLEAN_ROOMS** – The securable is shared in [Clean Rooms](/concepts/databricks-clean-rooms.md), referenced by central clean room IDs. The error lists the share names and clean room IDs. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]
- **NO_HINT** – The securable is shared through shares (without clean rooms). The error lists the share names. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]
- A combination of both – The securable is shared through both shares and clean rooms. The error message includes both the share names and the clean room IDs. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

## Resolving the Blocked Deletion

If the intent is only to update a shared view, the recommended action is to use `ALTER VIEW` instead of attempting to delete the securable. If the deletion must proceed, the sharing must first be revoked from the affected shares and/or clean rooms before dropping the securable. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md)
- [Clean Rooms](/concepts/databricks-clean-rooms.md)
- [Shared Views](/concepts/opensharing-views.md)
- ALTER VIEW
- Error Conditions – Overview of error handling in Databricks.
- [SQLSTATE 55006](/concepts/sqlstate-55006.md) – Object Not in Prerequisite State.

## Sources

- delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md

# Citations

1. [delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md](/references/delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws-0eeb76c6.md)

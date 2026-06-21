---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4db164195acbeff8b244cba724c00c523ce9f8909716d609cfbcfb22588bc69b
  pageDirectory: concepts
  sources:
    - delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - clean-rooms-in-databricks
    - CRID
  citations:
    - file: delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md
title: Clean Rooms in Databricks
description: A data collaboration environment where shared objects are protected from deletion; the error message distinguishes clean room sharing from standard share-based sharing.
tags:
  - databricks
  - clean-rooms
  - data-collaboration
timestamp: "2026-06-19T18:26:40.375Z"
---

#Clean Rooms in Databricks

**Clean Rooms in Databricks** is a secure collaboration feature that enables multiple parties to share and analyze data without exposing the underlying raw data to each other. Clean Rooms leverage [OpenSharing](/concepts/opensharing.md) to share securables (such as tables, views, or other data objects) across organizational boundaries while enforcing access and usage controls.

## Overview

A Clean Room is defined in the context of the **`DELTA_SHARING_SECURABLE_DELETE_BLOCKED`** error condition, which occurs when a user attempts to delete a securable that is currently being shared via an OpenSharing share that is associated with one or more Clean Rooms. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

## Key Characteristics

- Clean Rooms require **central clean room IDs** that identify the room across the sharing network. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]
- Securables shared in a Clean Room cannot be deleted while the sharing relationship exists. This is enforced by the **`DELTA_SHARING_SECURABLE_DELETE_BLOCKED`** error (SQLSTATE 55006 – object not in prerequisite state). ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

## Error Sub‑Categories

When a deletion is blocked because the securable is shared through Clean Rooms, the error message includes one of the following hints:

| Hint | Meaning |
|------|---------|
| `BY_CLEAN_ROOMS` | The securable is shared in Clean Rooms with central clean room IDs listed. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md] |
| `NO_HINT` | The securable is shared but the blocking reason is not further detailed (generic). ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md] |
| Combined | The securable is shared through both named shares and Clean Rooms simultaneously. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md] |

### Workaround

If you need to modify a shared view without disrupting the Clean Room, use `ALTER VIEW` instead of `DROP VIEW` or `DROP TABLE`. The error message explicitly advises:

> "If you just want to update a shared view, please use `ALTER VIEW` instead." ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) – The underlying sharing mechanism used by Clean Rooms.
- DELTA_SHARING_SECURABLE_DELETE_BLOCKED Error|DELTA_SHARING_SECURABLE_DELETE_BLOCKED error condition – The full error class that reports Clean Room sharing conflicts.
- [Securables in Databricks](/concepts/securable-types-in-databricks.md) – Objects such as tables, views, and functions that can be shared.
- Data Collaboration – The broader practice of secure multi‑party data analysis.

## Sources

- delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md

# Citations

1. [delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md](/references/delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws-0eeb76c6.md)

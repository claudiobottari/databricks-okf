---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b8105e00afd4e305df5fe6b849eba9c3ad55a2f21bf1e7a5cf9b6880c920a33b
  pageDirectory: concepts
  sources:
    - delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md
  confidence: 0.75
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - securable-types-in-databricks
    - STID
    - Secrets in Databricks
    - Securables in Databricks
  citations:
    - file: delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md
title: Securable Types in Databricks
description: Objects such as tables, views, or schemas that can be shared via Delta Sharing and are protected from deletion while actively shared; the error message uses placeholders for securable type and full name.
tags:
  - databricks
  - securable
  - access-control
timestamp: "2026-06-19T18:27:18.536Z"
---

# Securable Types in Databricks

**Securable Types** are the categories of objects in Databricks that can have permissions managed through the [Unity Catalog](/concepts/unity-catalog.md) access control system. Each securable type represents a distinct class of object that can be secured, shared, and governed within the Databricks environment.

## Overview

In Databricks, securable types define what kinds of objects can be protected by access control policies. These objects range from high-level organizational units like catalogs down to individual columns within tables. The system enforces permissions at each securable level, allowing fine-grained control over who can access, modify, or manage data assets. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

When a securable object is actively being shared through [Delta Sharing](/concepts/delta-sharing.md), certain management operations may be restricted. For example, attempting to delete a securable that is currently shared via OpenSharing will trigger a `DELTA_SHARING_SECURABLE_DELETE_BLOCKED` error, preventing accidental removal of shared assets. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

## Common Securable Types

### Catalogs

Catalogs represent the top-level container for data organization in Unity Catalog. They contain schemas, tables, views, models, and other data assets. Catalog-level permissions control who can access and create objects within the entire catalog. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

### Schemas

Schemas (also known as databases) are logical groupings within a catalog that contain tables, views, and other objects. Schema-level permissions provide granular control over access to groups of related data objects. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

### Tables and Views

Tables store actual data in structured format, while views provide virtual representations based on queries. Both are securable types that can have their own access control policies. Views are particularly relevant when considering the `DELTA_SHARING_SECURABLE_DELETE_BLOCKED` error, as the error message specifically suggests using `ALTER VIEW` instead of deletion when a view is shared. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

### Shares

Shares are a securable type specific to [Delta Sharing](/concepts/delta-sharing.md) that define how data is shared with recipients. When a securable object is shared through one or more shares, deleting that object is blocked to maintain data availability for recipients. The error condition reports the specific share names that are preventing deletion. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

### Clean Rooms

[Clean Rooms](/concepts/databricks-clean-rooms.md) are secure environments for collaborative data analysis where participants can query data without exposing raw data to each other. Clean rooms are represented as securable types with their own central clean room IDs. When a securable is shared in clean rooms, the deletion is blocked, and the error message includes the specific clean room IDs involved. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

## Deletion Restrictions for Shared Securables

A critical behavior of securable types is that objects actively being shared through OpenSharing cannot be deleted. This protection applies to various sharing contexts: ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

- **Shares only**: When the securable is shared through shares but not clean rooms, the deletion is blocked with share names reported.
- **Clean rooms only**: When the securable is shared in clean rooms but not through shares, the deletion is blocked with clean room IDs reported.
- **Both shares and clean rooms**: When the securable is shared through both mechanisms, both share names and clean room IDs are reported in the error.
- **No hint**: When neither shares nor clean rooms are involved but the deletion is still blocked, the error provides a general message suggesting `ALTER VIEW` as an alternative.

The recommended approach for updating a shared view is to use `ALTER VIEW` instead of deleting and recreating the object, which would break the existing sharing relationships. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that manages securable types
- [Delta Sharing](/concepts/delta-sharing.md) — Open protocol for sharing securable objects across platforms
- [Clean Rooms](/concepts/databricks-clean-rooms.md) — Secure collaborative environments for securable data
- Access Control Lists (ACLs) — Permissions management for securable objects
- [SQLSTATE 55006](/concepts/sqlstate-55006.md) — The SQL state associated with object deletion blocks

## Sources

- delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md

# Citations

1. [delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md](/references/delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws-0eeb76c6.md)

---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b245c95487efca20a8fdedaf00b775c1902c6e390d9d1a1b691aefdb4b782d40
  pageDirectory: concepts
  sources:
    - manage-privileges-in-unity-catalog-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - collaborative-editing-via-group-ownership
    - CEVGO
  citations:
    - file: manage-privileges-in-unity-catalog-databricks-on-aws.md
title: Collaborative Editing via Group Ownership
description: Transferring ownership of a view or metric view to a group enables collaborative editing, where all group members can edit the definition while data access is limited to what the group has permission to see.
tags:
  - unity-catalog
  - collaboration
  - views
  - ownership
timestamp: "2026-06-19T19:27:51.028Z"
---

# Collaborative Editing via Group Ownership

**Collaborative Editing via Group Ownership** is a pattern in [Unity Catalog](/concepts/unity-catalog.md) that enables multiple users to edit the definition of a view or metric view while preserving data access controls. By transferring ownership of the view to a group, all members of that group become co-owners and can modify the view’s definition without needing individual owner roles. ^[manage-privileges-in-unity-catalog-databricks-on-aws.md]

## How It Works

When a group owns a view or metric view, each member of the group inherits the owner’s full privileges on that object, including the ability to alter its definition. Data access remains limited to what the group itself has permission to see—group membership does not grant broader data access than what the owning group already possesses. ^[manage-privileges-in-unity-catalog-databricks-on-aws.md]

## Setting Up Collaborative Editing

To enable collaborative editing, an authorized principal transfers ownership of the view or metric view to a group. The following principals can transfer ownership:

- The current owner of the view
- A [metastore admin](/concepts/metastore-admin-role.md)
- The owner of the containing catalog or schema
- A user with the [MANAGE Privilege](/concepts/manage-privilege.md) on the view

When transferring ownership of a view or function to a group, a [Metastore](/concepts/metastore.md) admin may transfer to any user, service principal, or group. Non-admin owners and users with the `MANAGE` privilege are restricted to transferring ownership to their own username or to a group they are a member of. ^[manage-privileges-in-unity-catalog-databricks-on-aws.md]

*For step-by-step instructions, see the Transfer ownership section under Manage object ownership.*

## Related Concepts

- Ownership — The principal that has all privileges on a securable object.
- View — A saved query that can be shared and edited collaboratively.
- Metric View — A type of view used for business metrics and KPIs.
- Group — A collection of users or service principals that can own securable objects.
- [Metastore admin](/concepts/metastore-admin-role.md) — An admin role that can transfer ownership without restrictions.
- [MANAGE Privilege](/concepts/manage-privilege.md) — A privilege that allows a principal to manage grants and ownership on an object.

## Sources

- manage-privileges-in-unity-catalog-databricks-on-aws.md

# Citations

1. [manage-privileges-in-unity-catalog-databricks-on-aws.md](/references/manage-privileges-in-unity-catalog-databricks-on-aws-f0868c6d.md)

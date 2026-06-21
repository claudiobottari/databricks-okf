---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d8edaf7a11a29f3700af414f903720079e748c51a711503ddd35e723b1cd1c8f
  pageDirectory: concepts
  sources:
    - flag-data-as-certified-or-deprecated-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - governed-tag-permissions-in-unity-catalog
    - GTPIUC
  citations:
    - file: flag-data-as-certified-or-deprecated-databricks-on-aws.md
title: Governed Tag Permissions in Unity Catalog
description: The ASSIGN permission on system-governed tags and APPLY TAG privilege required to apply certification status tags to Unity Catalog objects.
tags:
  - permissions
  - access-control
  - unity-catalog
timestamp: "2026-06-19T10:36:33.091Z"
---

# Governed Tag Permissions in Unity Catalog

**Governed Tag Permissions in Unity Catalog** control who can apply, modify, and remove [Governed Tags](/concepts/governed-tags.md) on Unity Catalog securable objects. These permissions are separate from the standard object-level privileges (e.g., `SELECT`, `MODIFY`) and are managed through a dedicated `ASSIGN` permission on the tag itself.

## Overview

A governed tag, whether system-defined (like `system.certification_status`) or user-defined, can be applied to objects such as catalogs, schemas, tables, views, volumes, functions, registered models, dashboards, Genie Spaces, Databricks apps, and notebooks. To assign a tag to an object, the user must have:

- The **`ASSIGN` permission** on the governed tag.
- The necessary object-level privileges on the target object.

These two layers ensure that only authorized principals can use governed tags, while also respecting existing access controls on the data assets. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

## The `ASSIGN` Permission

Each governed tag has its own `ASSIGN` permission. A user or group with `ASSIGN` on a specific tag can apply that tag to any supported object, provided they also meet the object-level requirements. Without `ASSIGN`, the user cannot assign the tag regardless of their object privileges.

The `ASSIGN` permission is managed through the [Manage permissions on governed tags](/concepts/permissions-for-governed-tags.md) interface (see the source document for the external link). ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

## Object-Level Privileges Required

In addition to `ASSIGN` on the tag, applying a tag to a Unity Catalog securable object requires that the user **own** the object or have **all of the following** privileges:

| Privilege | Description |
|-----------|-------------|
| `APPLY TAG` | On the target object itself |
| `USE SCHEMA` | On the object's parent schema |
| `USE CATALOG` | On the object's parent catalog |

These privileges follow the standard Unity Catalog hierarchy. For example, tagging a table requires `USE CATALOG` on the catalog containing the table, `USE SCHEMA` on the schema, and `APPLY TAG` on the table. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

## System-Governed Tag Example: Certification Status

The `system.certification_status` governed tag is a system-defined tag with two values: `certified` and `deprecated`. Applying it requires `ASSIGN` on that tag plus the object-level privileges above. This tag is used to indicate data quality or lifecycle status and appears as a visual icon in the workspace. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

## Managing Permissions

Permissions on governed tags (who has `ASSIGN`) are configured separately from object ACLs. For details on how to grant, revoke, and view `ASSIGN` permissions, see the documentation on [Manage permissions on governed tags](/concepts/permissions-for-governed-tags.md). ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

## Related Concepts

- [Governed Tags](/concepts/governed-tags.md) – The metadata attributes subject to these permissions.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer that enforces tag permissions.
- [System Tags](/concepts/system-tags.md) – Predefined governed tags like `system.certification_status`.
- APPLY TAG Privilege – The object-level privilege for tag assignment.
- [Object Ownership in Unity Catalog](/concepts/object-ownership-in-unity-catalog.md) – Ownership as an alternative to individual privileges.
- [Flag data as certified or deprecated](/concepts/certified-and-deprecated-data-flags.md) – Practical example of using governed tag permissions.

## Sources

- flag-data-as-certified-or-deprecated-databricks-on-aws.md

# Citations

1. [flag-data-as-certified-or-deprecated-databricks-on-aws.md](/references/flag-data-as-certified-or-deprecated-databricks-on-aws-ee1b377b.md)

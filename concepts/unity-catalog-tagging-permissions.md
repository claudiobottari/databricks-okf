---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8c7df9de9f0d1bb0e297ef5328c121c55c66cebbc27abbbf53c49bfa2da905a5
  pageDirectory: concepts
  sources:
    - flag-data-as-certified-or-deprecated-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-tagging-permissions
    - UCTP
  citations:
    - file: flag-data-as-certified-or-deprecated-databricks-on-aws.md
    - file: create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
    - file: best-practices-for-abac-policies-databricks-on-aws.md
title: Unity Catalog Tagging Permissions
description: The permission model required to assign governed tags in Unity Catalog, including the ASSIGN permission on the system tag and object-level privileges like APPLY TAG, USE SCHEMA, and USE CATALOG.
tags:
  - permissions
  - unity-catalog
  - data-governance
timestamp: "2026-06-18T12:24:09.819Z"
---

# Unity Catalog Tagging Permissions

**Unity Catalog Tagging Permissions** define the privileges required to apply, manage, and control access to [Governed Tags](/concepts/governed-tags.md) on securable objects within Unity Catalog. These permissions govern who can assign tags to objects, manage tag metadata, and use tags as the basis for [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies.

## Tag Permission Model

Tagging permissions in Unity Catalog operate at two levels: permissions on the tag itself and permissions on the target object. Both must be satisfied for a user to successfully apply a tag. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

### Permissions on the Tag

To apply a governed tag to any object, you must have the `ASSIGN` permission on that specific tag. This is separate from object-level permissions and controls who can use a particular tag across the catalog. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

For example, to apply the `system.certification_status` tag (which marks objects as certified or deprecated), a user must have the `ASSIGN` permission on that governed tag. See [Manage permissions on governed tags](/concepts/permissions-for-governed-tags.md) for details on configuring tag-level permissions. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

### Permissions on the Target Object

In addition to tag-level permissions, adding tags to Unity Catalog securable objects requires all of the following privileges on the target object: ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

| Privilege | Scope |
|-----------|-------|
| `APPLY TAG` | On the target object itself |
| `USE SCHEMA` | On the object's parent schema |
| `USE CATALOG` | On the object's parent catalog |

A user must hold all three privileges simultaneously to tag an object. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

### Ownership as an Alternative

Users who own the target object can also apply tags without needing the specific `APPLY TAG` privilege, as ownership grants implicit privileges on the owned object. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

## Permissions for Specific Tag Types

### System Tags

System tags are predefined tags managed by Databricks. The most commonly used system tag is `system.certification_status`, which accepts the values `certified` and `deprecated`. To use this tag, users must have the `ASSIGN` permission on `system.certification_status` in addition to the standard object-level tagging permissions. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

### User-Defined Governed Tags

For tags created by administrators or data stewards, the same permission model applies: users need `ASSIGN` on the tag itself plus `APPLY TAG`, `USE SCHEMA`, and `USE CATALOG` on the target object. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

## Supported Object Types for Tagging

Tags can be applied to the following Unity Catalog securable objects: ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

- Catalogs
- Schemas
- Tables
- Views
- Volumes
- Functions
- Registered models
- Dashboards
- Genie Spaces
- Databricks Apps
- Notebooks

## Auditing Tagging Operations

All tag assignment and deletion operations are logged in the `system.access.audit` system table. The relevant action names are: ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

| Action Name | Description |
|-------------|-------------|
| `createEntityTagAssignment` | A tag is assigned to a securable object |
| `deleteEntityTagAssignment` | A tag is removed from a securable object |

Administrators can query these logs to monitor who is applying or removing tags, which is critical because tags serve as a security boundary in ABAC. If a user can change tags on a data asset, they can change which ABAC policies apply to it — potentially gaining or blocking unintended access. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md, best-practices-for-abac-policies-databricks-on-aws.md]

## Tag Permissions as a Security Boundary

Because ABAC policies (including [ABAC GRANT Policy](/concepts/abac-grant-policy.md), [Row Filter Policies](/concepts/row-filter-policies.md), and [Column Mask Policies](/concepts/column-mask-policies.md)) evaluate conditions against tags on securable objects, controlling who can assign and modify tags is essential for maintaining security. Databricks recommends: ^[best-practices-for-abac-policies-databricks-on-aws.md]

- Restricting `ASSIGN` permission on governed tags to authorized data stewards or governance administrators.
- Auditing tag changes regularly to detect unauthorized modifications.
- Documenting the tagging taxonomy and governance model so teams can identify anomalous changes in the audit log.
- Auditing tag changes together with direct grants and ABAC policy changes to get a complete picture of effective permissions. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Related Concepts

- [Governed Tags](/concepts/governed-tags.md) — The tag system that drives ABAC policy evaluation
- [System Tags](/concepts/system-tags.md) — Predefined tags such as `system.certification_status`
- [ABAC GRANT Policy](/concepts/abac-grant-policy.md) — Policies that grant privileges based on tag conditions
- [Column Mask Policies](/concepts/column-mask-policies.md) — Policies that mask columns based on tag conditions
- [Row Filter Policies](/concepts/row-filter-policies.md) — Policies that filter rows based on tag conditions
- [Data Classification](/concepts/data-classification.md) — Automatic detection of sensitive columns with classification tags
- [ABAC Policy Audit Logging](/concepts/abac-policy-audit-logging.md) — Audit events for tag and policy operations
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer providing ABAC capabilities

## Sources

- flag-data-as-certified-or-deprecated-databricks-on-aws.md
- create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
- best-practices-for-abac-policies-databricks-on-aws.md

# Citations

1. [flag-data-as-certified-or-deprecated-databricks-on-aws.md](/references/flag-data-as-certified-or-deprecated-databricks-on-aws-ee1b377b.md)
2. [create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md](/references/create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws-d315307d.md)
3. [best-practices-for-abac-policies-databricks-on-aws.md](/references/best-practices-for-abac-policies-databricks-on-aws-716fb4af.md)

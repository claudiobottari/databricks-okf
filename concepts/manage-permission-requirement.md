---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 60726ba8febb000b5010041217d0bf65aedaf0c31efb24300bfa7575a0f9bd23
  pageDirectory: concepts
  sources:
    - create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - manage-permission-requirement
    - MPR
  citations:
    - file: create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
title: MANAGE Permission Requirement
description: All ABAC policy operations (create, edit, delete, show, describe) require MANAGE permission on the securable object or object ownership, ensuring only authorized users can modify data access rules.
tags:
  - data-governance
  - unity-catalog
  - permissions
timestamp: "2026-06-19T09:34:36.999Z"
---

# MANAGE Permission Requirement

The **MANAGE Permission Requirement** is a privilege level in [Unity Catalog](/concepts/unity-catalog.md) that governs who can create, edit, delete, and view [ABAC Row Filter Policies](/concepts/abac-row-filter-policies.md) and [ABAC Column Mask Policies](/concepts/abac-column-mask-policies.md). It is a higher-level permission than standard object access privileges and is required for administrative operations on security policies.

## Permission Scope

All policy operations — including creating, editing, deleting, viewing, and describing policies — require the `MANAGE` permission on the target securable object (catalog, schema, or table) or ownership of that object. This applies to both row filter policies and column mask policies. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Operations Requiring MANAGE

The following operations require `MANAGE` on the relevant securable object:

- **Creating a policy**: The user must have `MANAGE` on the object where the policy is attached (catalog, schema, or table) and `EXECUTE` on the user-defined function (UDF) that implements the filtering or masking logic. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]
- **Editing a policy**: Users can modify the description, principals, policy type, conditions, and function input mappings. The policy name and the securable object where the policy is applied cannot be edited. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]
- **Deleting a policy**: Requires `MANAGE` on the target securable object or object ownership. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]
- **Describing a policy**: Using the `DESCRIBE POLICY` statement requires `MANAGE` on the target securable object or object ownership. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]
- **Viewing effective policies**: `SHOW EFFECTIVE POLICIES` for a table does not require permissions on the parent catalog or schema, allowing a table admin to see applicable rules without read access to sibling tables' policies. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Relationship to Other Permissions

- **`MANAGE` permission** is distinct from privileges like `SELECT`, `EXECUTE`, or `MODIFY`. A user may have `SELECT` on a table (allowing them to query data) without having `MANAGE` (allowing them to create or modify policies on that table).
- For [ABAC Column Mask Policies](/concepts/abac-column-mask-policies.md), users querying masked data need `SELECT` (or appropriate) privileges on the table. The policy does not grant access; it only controls how data appears to users who already have access.
- Creating a policy also requires `EXECUTE` privilege on the UDF referenced by the policy.

## Related Concepts

- [ABAC Row Filter Policies](/concepts/abac-row-filter-policies.md)
- [ABAC Column Mask Policies](/concepts/abac-column-mask-policies.md)
- [Unity Catalog Permissions](/concepts/unity-catalog-permissions-model.md)
- User-Defined Functions (UDFs)

## Sources

- create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md

# Citations

1. [create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md](/references/create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws-d315307d.md)

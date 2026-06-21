---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 93b384424f8ddace4ff68047ecce54b20cb9748d48a47e61ac7bf03cd4bcfd8d
  pageDirectory: concepts
  sources:
    - create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - manage-permission-in-unity-catalog
    - MPIUC
    - Permissions in Unity Catalog
    - Table Permissions in Unity Catalog
  citations:
    - file: create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
title: MANAGE Permission in Unity Catalog
description: A privilege required for all policy operations (create, edit, delete, describe) on securable objects in Unity Catalog, distinct from ownership but an alternative requirement.
tags:
  - unity-catalog
  - permissions
  - access-control
timestamp: "2026-06-19T17:59:28.707Z"
---

# MANAGE Permission in Unity Catalog

**MANAGE Permission in Unity Catalog** is a powerful privilege that governs the ability to create, edit, delete, show, and describe [ABAC](/concepts/abac-attribute-based-access-control.md) row filter and column mask policies. It can be granted on a securable object such as a catalog, schema, or table, and its presence (or object ownership) is required for all policy lifecycle operations. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Overview

Unity Catalog’s attribute‑based access control (ABAC) uses row filter and column mask policies to enforce fine‑grained data protection. The `MANAGE` permission is the top‑level authorization for administering these policies. It is separate from the `EXECUTE` permission needed on the user‑defined function (UDF) that implements the filtering or masking logic. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## What MANAGE Permission Allows

All of the following policy operations require `MANAGE` on the securable object (or ownership of that object): ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

- **Create policy** — Requires `MANAGE` on the catalog, schema, or table where the policy will be attached, together with `EXECUTE` on the UDF used in the policy. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]
- **Edit policy** — Update an existing policy’s description, principals, type, conditions, or function input mappings. The policy name and its attached securable object cannot be changed. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]
- **Delete policy** — Permanently remove a policy from a securable object. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]
- **Show policies** — List all policies defined on a securable object using `SHOW POLICIES`. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]
- **Describe policy** — View the properties of a specific policy (name, securable type, securable name, principals, conditions, function name, timestamps) using `DESCRIBE POLICY`. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

The `SHOW EFFECTIVE POLICIES` command, which also includes policies inherited from parent scopes, does **not** require `MANAGE` on the parent catalog or schema. This allows a table admin to see all applicable rules without needing read access to sibling tables’ policies. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Requirements

- To perform any policy operation, you must either have the `MANAGE` privilege on the target securable object or be the owner of that object. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]
- For policy creation, you additionally need `EXECUTE` on the Unity Catalog UDF that implements the row filter or column mask logic. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]
- The compute must be Databricks Runtime 16.4 or above, or serverless compute. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]
- Governed tags must be applied to the target objects. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Related Concepts

- [ABAC (Attribute-Based Access Control)](/concepts/abac-attribute-based-access-control.md) — The overarching access control model that uses policies.
- [Row Filter Policies](/concepts/row-filter-policies.md) — Policies that exclude rows from query results based on a boolean UDF.
- [Column Mask Policies](/concepts/column-mask-policies.md) — Policies that mask column values using a UDF.
- [Catalog Explorer](/concepts/catalog-explorer.md) — The UI for managing policies when the `MANAGE` permission is held.
- [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md) — The full set of privileges available in Unity Catalog, including `MANAGE`, `EXECUTE`, and ownership.

## Sources

- create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md

# Citations

1. [create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md](/references/create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws-d315307d.md)

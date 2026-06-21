---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: abe07b00e4e537d14b43fba1aa78685fac55573915a2c653df12286025ff3a10
  pageDirectory: concepts
  sources:
    - access-control-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - privilege-grant-and-revocation
    - Revocation and Privilege Grant
    - PGAR
  citations:
    - file: access-control-in-unity-catalog-databricks-on-aws.md
title: Privilege Grant and Revocation
description: Granting, revoking, and inspecting privileges on Unity Catalog objects using Catalog Explorer and SQL
tags:
  - unity-catalog
  - access-control
  - sql
  - administration
timestamp: "2026-06-19T08:48:31.851Z"
---

# Privilege Grant and Revocation

**Privilege Grant and Revocation** refers to the process of assigning (granting) or removing (revoking) permissions on securable objects within [Unity Catalog](/concepts/unity-catalog.md). This mechanism controls *who* can access *what* by using grants on securable objects such as catalogs, schemas, tables, and views. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## Overview

Privilege grant and revocation is one of the foundational access control models in Unity Catalog. It works alongside other mechanisms — [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md), [Row Filters and Column Masks](/concepts/row-filters-and-column-masks.md), and workspace-level restrictions — to enforce secure, fine-grained access across your data environment. ^[access-control-in-unity-catalog-databricks-on-aws.md]

The privilege model focuses on:
- **Who** can access securable objects
- **What** operations they can perform (e.g., SELECT, MODIFY, CREATE, MANAGE)
- **Which** objects they can access

## When to Use Privilege Grants vs. Other Mechanisms

Privilege grants, ABAC policies, and workspace bindings evaluate access at different levels and are designed to be used together. While privilege grants provide direct access control on specific objects, ABAC offers a centralized, tag-driven approach that scales more effectively for large estates. ^[access-control-in-unity-catalog-databricks-on-aws.md]

Databricks recommends using attribute-based access control (ABAC) to centralize and scale access control based on governed tags. Use row filters and column masks only when you need per-table logic or haven't adopted ABAC yet. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- Permissions Concepts — Understand the [Unity Catalog Object Hierarchy](/concepts/unity-catalog-object-hierarchy.md), privilege inheritance, and how access flows from parent to child objects.
- Privileges Reference — Detailed descriptions of every privilege in Unity Catalog.
- Admin Roles — Account admin, workspace admin, and [Metastore](/concepts/metastore.md) admin roles and their scopes.
- [Manage Privileges](/concepts/manage-privilege.md) — Grant, revoke, and inspect privileges using Catalog Explorer and SQL.
- Access Requests — Configure destinations for access requests on Unity Catalog securable objects.
- [Workspace-Catalog Binding](/concepts/workspace-catalog-binding.md) — Restrict which workspaces can access specific catalogs, external locations, and storage credentials.
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — Define centralized, tag-driven policies that dynamically filter and mask data across your catalog.

## Sources

- access-control-in-unity-catalog-databricks-on-aws.md

# Citations

1. [access-control-in-unity-catalog-databricks-on-aws.md](/references/access-control-in-unity-catalog-databricks-on-aws-817d7ad8.md)

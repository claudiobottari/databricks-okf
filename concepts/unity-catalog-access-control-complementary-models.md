---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8eb8df5c9e644b61b9e9182772dc67aece68c073090319cb4b77b4d35d784403
  pageDirectory: concepts
  sources:
    - access-control-in-unity-catalog-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-access-control-complementary-models
    - UCACCM
  citations:
    - file: access-control-in-unity-catalog-databricks-on-aws.md
title: Unity Catalog Access Control Complementary Models
description: The four complementary access control models (privileges, ABAC, table-level filtering, workspace bindings) that work together for fine-grained security.
tags:
  - access-control
  - unity-catalog
  - architecture
timestamp: "2026-06-18T14:16:22.716Z"
---

# Unity Catalog Access Control Complementary Models

**Unity Catalog Access Control Complementary Models** describes the set of four access control mechanisms in [Unity Catalog](/concepts/unity-catalog.md) that work together to enforce secure, fine-grained access across your data environment. These models are designed to be used in combination, each addressing a different aspect of access control. ^[access-control-in-unity-catalog-databricks-on-aws.md]

---

## Overview

Access control in Unity Catalog is built on the following complementary models: ^[access-control-in-unity-catalog-databricks-on-aws.md]

- **Privileges and ownership** — control *who* can access *what*, using grants on securable objects.
- **Attribute-based policies (ABAC)** — control *what* data users can access, using governed tags and centralized policies.
- **Table-level filtering and masking** — control *what* data users can see within tables using table-specific filters and views.
- **Workspace-level restrictions** — control *where* users can access data, by limiting objects to specific workspaces.

These models evaluate access at different levels and are intended to be combined for comprehensive governance. ^[access-control-in-unity-catalog-databricks-on-aws.md]

---

## When to Use Each Access Control Mechanism

Workspace bindings, privileges, and ABAC policies all evaluate access at different levels. The source documentation provides a comparison table; the summary below captures the key distinctions:

| Mechanism | What it controls | Primary use case |
|-----------|------------------|------------------|
| **Privileges & ownership** | Ability to read, write, manage, or own securable objects | Granting or revoking explicit permissions on catalogs, schemas, tables, views, models, etc. |
| **ABAC (governed tag policies)** | Dynamic filtering and masking of data based on tags | Centralizing and scaling access control across many objects without per-object grants |
| **Row filters & column masks** | Per-table row and column visibility | Applying table-specific logic when ABAC is not yet adopted or per-table rules are needed |
| **Workspace-catalog binding** | Which workspaces can access a catalog | Restricting sensitive data to approved workspaces |

Databricks recommends using [ABAC](/concepts/abac-attribute-based-access-control.md) to centralize and scale access control based on governed tags. Use [row filters](/concepts/row-filter-policies.md) and [column masks](/concepts/delta-lake-column-masks.md) only when you need per-table logic or have not yet adopted ABAC. ^[access-control-in-unity-catalog-databricks-on-aws.md]

---

## How the Models Work Together

The models are complementary, not mutually exclusive. For example: ^[access-control-in-unity-catalog-databricks-on-aws.md]

- A principal must first have the `USE CATALOG` and `USE SCHEMA` privileges (via grants) to even reach the data.
- Workspace-level restrictions may further limit which workspaces can access the catalog, regardless of privileges.
- Once the user is allowed to query a table, ABAC policies or row filters / column masks can dynamically restrict which rows and columns they see.

This layered approach allows administrators to implement the principle of least privilege at multiple enforcement points. ^[access-control-in-unity-catalog-databricks-on-aws.md]

---

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The data governance platform that provides these access control models
- [ABAC GRANT Policies](/concepts/abac-grant-policy.md) — Attribute-based grant policies for models (Beta)
- [Row Filter Policies](/concepts/row-filter-policies.md) — ABAC-style row filters using governed tags
- [Column Mask Policies](/concepts/column-mask-policies.md) — ABAC-style column masking using governed tags
- [Workspace-Catalog Binding](/concepts/workspace-catalog-binding.md) — Restricting catalog access to specific workspaces
- [Manage Privileges](/concepts/manage-privilege.md) — Grant, revoke, and inspect privileges on Unity Catalog objects
- Privileges Reference — Detailed descriptions of every privilege in Unity Catalog

## Sources

- access-control-in-unity-catalog-databricks-on-aws.md

# Citations

1. [access-control-in-unity-catalog-databricks-on-aws.md](/references/access-control-in-unity-catalog-databricks-on-aws-817d7ad8.md)

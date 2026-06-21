---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 90ff70db75ae3890304e664d529ed6de355d1afb21e771b321c2abcf060cad7e
  pageDirectory: concepts
  sources:
    - access-control-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-permissions-model
    - UCPM
    - Unity Catalog Permission Model
    - Unity Catalog Permissions
    - Unity Catalog Permissions Model Concepts
    - Unity Catalog permissions
    - Unity Catalog Model Permissions
    - Unity Catalog model permissions
  citations:
    - file: access-control-in-unity-catalog-databricks-on-aws.md
title: Unity Catalog Permissions Model
description: The object hierarchy, privilege inheritance, and access flow from parent to child objects in Unity Catalog
tags:
  - unity-catalog
  - access-control
  - authorization
timestamp: "2026-06-19T08:48:31.340Z"
---

# Unity Catalog Permissions Model

The **Unity Catalog Permissions Model** is a multi-layered access control system that governs who can access what data and how data is presented to users. The model combines four complementary mechanisms: privileges and ownership, attribute-based policies, table-level filtering and masking, and workspace-level restrictions. These layers work together to enforce secure, fine-grained access across your data environment.^[access-control-in-unity-catalog-databricks-on-aws.md]

## Overview

Unity Catalog's permissions model is built on the following complementary approaches:^[access-control-in-unity-catalog-databricks-on-aws.md]

| Mechanism | Purpose |
|-----------|---------|
| **Privileges and ownership** | Control *who* can access *what*, using grants on [securable objects](/concepts/unity-catalog-securable-objects.md) |
| **Attribute-based policies (ABAC)** | Control *what* data users can access, using [Governed Tags](/concepts/governed-tags.md) and centralized policies |
| **Table-level filtering and masking** | Control *what* data users can see within tables using table-specific filters and views |
| **Workspace-level restrictions** | Control *where* users can access data, by limiting objects to specific workspaces |

## When to Use Each Access Control Mechanism

Workspace bindings, privileges, and ABAC policies all evaluate access at different levels and are designed to be used together. Databricks recommends using [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) to centralize and scale access control based on governed tags. Use [Row Filters and Column Masks](/concepts/row-filters-and-column-masks.md) only when you need per-table logic or have not yet adopted ABAC.^[access-control-in-unity-catalog-databricks-on-aws.md]

## Permissions Concepts

Understanding the Unity Catalog permissions model requires familiarity with several foundational concepts:^[access-control-in-unity-catalog-databricks-on-aws.md]

- **Object hierarchy** — How securable objects are organized ([Metastore](/concepts/metastore.md) → catalog → schema → table/view)
- **Privilege inheritance** — How privileges flow from parent to child objects
- **Access flow** — How permissions are evaluated when queries are executed

## Manage Access

Administrators can manage access through several interfaces:^[access-control-in-unity-catalog-databricks-on-aws.md]

- **Manage privileges** — Grant, revoke, and inspect privileges on Unity Catalog objects using Catalog Explorer and SQL
- **Access requests** — Configure destinations for access requests on Unity Catalog securable objects, including email, Slack, Teams, and webhooks
- **Workspace-catalog binding** — Restrict which workspaces can access specific catalogs, external locations, and storage credentials

## Fine-Grained Data Access

For more granular control over data visibility:^[access-control-in-unity-catalog-databricks-on-aws.md]

- **Attribute-based access control (ABAC)** — Define centralized, tag-driven policies that dynamically filter and mask data across your catalog
- **Row filters and column masks** — Apply per-table row and column filters using UDFs to control what data users see at query time

## Model Layers

### Privileges and Ownership

The privileges model uses a system of grants on securable objects. The privileges reference provides detailed descriptions of every privilege available. The admin roles documentation explains the scope and authority of account admins, workspace admins, and [Metastore](/concepts/metastore.md) admins.^[access-control-in-unity-catalog-databricks-on-aws.md]

### Attribute-Based Access Control (ABAC)

ABAC policies use governed tags to dynamically control data access. Policies are defined centrally and can apply across many tables without per-table configuration. Related concepts include:

- [ABAC Column Mask Policies](/concepts/abac-column-mask-policies.md) — Dynamically mask column values
- [ABAC Row Filter Policies](/concepts/abac-row-filter-policies.md) — Restrict which rows users can see
- [ABAC GRANT Policies](/concepts/abac-grant-policies.md) — Dynamically grant privileges (currently for models)

### Table-Level Filtering and Masking

Row filters and column masks are per-object UDFs that transform query results at query time. They are best suited for:^[access-control-in-unity-catalog-databricks-on-aws.md]

- Scenarios requiring per-table logic
- Environments that have not yet adopted ABAC

### Workspace-Level Restrictions

Workspace-catalog binding restricts which workspaces can access specific catalogs, external locations, and storage credentials.

## Related Concepts

- Securable objects
- [Privilege inheritance](/concepts/privilege-inheritance-hierarchy.md)
- [Governed Tags](/concepts/governed-tags.md)
- Policy evaluation order
- [Row Filters and Column Masks (table-level)](/concepts/row-filters-and-column-masks.md)

## Sources

- access-control-in-unity-catalog-databricks-on-aws.md

# Citations

1. [access-control-in-unity-catalog-databricks-on-aws.md](/references/access-control-in-unity-catalog-databricks-on-aws-817d7ad8.md)

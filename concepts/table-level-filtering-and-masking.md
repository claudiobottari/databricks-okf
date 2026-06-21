---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bdf7563d628540805e780c52cec3d2d3d8449761ea9d0de9f6e696e389e5418c
  pageDirectory: concepts
  sources:
    - access-control-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - table-level-filtering-and-masking
    - Masking and Table-Level Filtering
    - TFAM
  citations:
    - file: access-control-in-unity-catalog-databricks-on-aws.md
title: Table-Level Filtering and Masking
description: Fine-grained data access controls using row filters and column masks applied via UDFs to control what data users see within tables at query time.
tags:
  - unity-catalog
  - access-control
  - data-masking
  - row-filters
timestamp: "2026-06-18T10:36:36.007Z"
---

# Table-Level Filtering and Masking

**Table-level filtering and masking** are fine-grained access control mechanisms in [Unity Catalog](/concepts/unity-catalog.md) that restrict what data users can see within tables at query time. These controls are applied per-table using user-defined functions (UDFs) to implement row filters and column masks, complementing other access control models like [ABAC GRANT Policy](/concepts/abac-grant-policy.md) and direct privileges. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## Overview

Table-level filtering and masking provide granular control over data visibility within individual tables. Unlike attribute-based access control (ABAC) which uses centralized tag-driven policies across the catalog, row filters and column masks operate at the table level and implement logic using custom UDFs. ^[access-control-in-unity-catalog-databricks-on-aws.md]

These controls are part of Unity Catalog's fine-grained data access layer, which also includes [ABAC|attribute-based access control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies. Databricks recommends using ABAC with governed tags to centralize and scale access control, reserving row filters and column masks for cases where you need per-table logic or have not yet adopted ABAC. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## How They Work

### Row Filters

Row filters restrict which rows a user can see when querying a table. A row filter is implemented as a user-defined function (UDF) that evaluates to a boolean condition. When a user queries the table, Unity Catalog applies the filter automatically, returning only the rows that satisfy the filter condition for that user. ^[access-control-in-unity-catalog-databricks-on-aws.md]

### Column Masks

Column masks control what data is visible in specific columns of a table. A column mask is also implemented as a UDF. When a user queries the table, the mask UDF transforms or hides the column's values for unauthorized users — for example, replacing a Social Security number with a masked version like `***-**-1234`. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## Comparison with ABAC Policies

| Aspect | Row Filters & Column Masks | ABAC Policies (GRANT Policies) |
|---|---|---|
| **Scope** | Per-table logic | Cross-catalog, tag-driven |
| **Implementation** | User-defined functions (UDFs) | Inline conditions in policy definitions |
| **Effect** | Restricts data content within accessible tables | Determines whether a user can access the object |
| **Management** | Applied individually to tables | Centralized policy attached to catalog or schema |
| **Recommendation** | Use when per-table logic is needed or ABAC is not adopted | Preferred method for scaling and centralizing access control |

^[access-control-in-unity-catalog-databricks-on-aws.md]

## When to Use Table-Level Filtering and Masking

Databricks recommends using [ABAC|attribute-based access control (ABAC)](/concepts/attribute-based-access-control-abac.md) to centralize and scale access control based on governed tags. Use row filters and column masks only when: ^[access-control-in-unity-catalog-databricks-on-aws.md]

- You need per-table logic that cannot be expressed through tag-based ABAC policies.
- You have not yet adopted ABAC and need a simpler, table-specific approach.
- You need to transform or mask column values differently depending on the user or context.

## Relationship to Other Access Controls

Table-level filtering and masking work alongside other access control mechanisms in Unity Catalog: ^[access-control-in-unity-catalog-databricks-on-aws.md]

- **Privileges and ownership** control *who* can access *what*, using grants on securable objects.
- **Attribute-based policies (ABAC)** control *what* data users can access, using governed tags and centralized policies.
- **Table-level filtering and masking** control *what* data users can see *within* tables.
- **Workspace-level restrictions** control *where* users can access data, by limiting objects to specific workspaces.

These models work together to enforce secure, fine-grained access across your data environment. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## Key Differences from GRANT Policies

An important distinction exists between table-level filtering/masking and [GRANT policies|ABAC GRANT policies](/concepts/grant-policies-abac-beta.md): ^[access-control-in-unity-catalog-databricks-on-aws.md]

- **Row filter and column mask policies restrict the content of data a user can already access.** They operate within a table that the user has permission to query.
- **GRANT policies determine whether the user can access the object at all.** They grant or deny the privilege to query the object itself.
- **Row filters and column masks require a UDF** to implement the filter or mask logic.
- **GRANT policies do not use UDFs** — the condition is expressed inline in the policy definition.

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The data governance platform that provides these controls
- [ABAC|Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — Centralized, tag-driven access control
- [ABAC GRANT Policy](/concepts/abac-grant-policy.md) — Policy mechanism for dynamically granting privileges based on tags
- [Row Filter Policies](/concepts/row-filter-policies.md) — ABAC policies that filter rows based on conditions
- [Column Mask Policies](/concepts/column-mask-policies.md) — ABAC policies that mask sensitive column values
- [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md) — The full set of available privileges for granting access

## Sources

- access-control-in-unity-catalog-databricks-on-aws.md

# Citations

1. [access-control-in-unity-catalog-databricks-on-aws.md](/references/access-control-in-unity-catalog-databricks-on-aws-817d7ad8.md)

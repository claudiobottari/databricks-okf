---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2098199a639c27b504c32b23f07d801ceed95a2596a59c93e5db7a170299d788
  pageDirectory: concepts
  sources:
    - row-filters-and-column-masks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - abac-policies-vs-table-level-row-filters-and-column-masks
    - column masks and ABAC policies vs table-level row filters
    - APVTRFACM
    - ABAC vs Table-Level Row Filters and Column Masks
    - When to use ABAC vs table-level row filters and column masks
  citations:
    - file: row-filters-and-column-masks-databricks-on-aws.md
title: ABAC policies vs table-level row filters and column masks
description: Comparison of attribute-based access control (schema/catalog-level, tag-driven) versus per-table manual row filters and column masks in Unity Catalog.
tags:
  - data-governance
  - unity-catalog
  - architecture
  - security
timestamp: "2026-06-19T20:17:45.216Z"
---

# ABAC Policies vs Table-Level Row Filters and Column Masks

**ABAC policies vs table-level row filters and column masks** describes the trade-offs between two approaches to row-level and column-level access control in [Unity Catalog](/concepts/unity-catalog.md): centralized attribute-based access control (ABAC) policies and per-table SQL-based row filters and column masks. Both mechanisms restrict the rows and column values a user can see at query time, but they differ in scope, management, scalability, and administration. ^[row-filters-and-column-masks-databricks-on-aws.md]

## Overview

Row filters restrict which rows a user can see in a table by evaluating a SQL user-defined function (UDF) at query time; rows where the function returns `FALSE` are excluded. Column masks control what values a user sees for specific columns by applying a SQL UDF that returns either the original value or a masked version. Both mechanisms exist in two forms: table-level (configured directly on individual tables) and ABAC-based (configured centrally via policies). ^[row-filters-and-column-masks-databricks-on-aws.md]

## Table-Level Row Filters and Column Masks

Table-level row filters and column masks are bound to a single table using SQL commands such as `ALTER TABLE ... SET ROW FILTER` and `ALTER TABLE ... ALTER COLUMN ... SET MASK`. They are managed by the table owner. ^[row-filters-and-column-masks-databricks-on-aws.md]

### Characteristics

- **Scope:** Per-table. Each filter or mask applies only to the specific table or column it is configured on. ^[row-filters-and-column-masks-databricks-on-aws.md]
- **Management:** Manual, per-table configuration by the table owner. ^[row-filters-and-column-masks-databricks-on-aws.md]
- **Scale:** Harder to scale and maintain across many tables. ^[row-filters-and-column-masks-databricks-on-aws.md]
- **Override:** Table owners can modify or remove filters and masks they own. ^[row-filters-and-column-masks-databricks-on-aws.md]

## ABAC Policies

ABAC policies attach at the catalog or schema level and apply automatically to tables and columns based on governed tags. They are the recommended approach when consistent row filtering and column masking is needed across many tables. ^[row-filters-and-column-masks-databricks-on-aws.md]

### Characteristics

- **Scope:** Catalog- or schema-level. Policies apply automatically to all tagged tables and columns within the scope. ^[row-filters-and-column-masks-databricks-on-aws.md]
- **Management:** Centralized. Higher-level admins define policies, providing separation of duties between policy authors and data stewards. ^[row-filters-and-column-masks-databricks-on-aws.md]
- **Scale:** Scales across catalogs and schemas. New tables are automatically covered as they are tagged. ^[row-filters-and-column-masks-databricks-on-aws.md]
- **Override:** Table owners cannot override or remove centrally-defined policies. ^[row-filters-and-column-masks-databricks-on-aws.md]
- **Performance:** Policy logic is evaluated more efficiently than table-specific UDFs. ^[row-filters-and-column-masks-databricks-on-aws.md]

## Comparison Summary

| Aspect | ABAC Policies | Table-Level Row Filters & Column Masks |
|--------|---------------|----------------------------------------|
| Attachment point | Catalog or schema | Individual table or column |
| Configuration | Centrally defined; tag-based | Per-table SQL commands |
| Administrator | Higher-level admin | Table owner |
| Override by table owner | No | Yes |
| Automatic coverage of new tables | Yes (when tagged) | No (manual configuration required) |
| Scalability | High (single policy, many tables) | Low (one config per table) |
| Separation of duties | Yes | No |
| Policy evaluation efficiency | Better | Standard UDF evaluation |

^[row-filters-and-column-masks-databricks-on-aws.md]

## When to Use ABAC Policies

Use ABAC policies when you need: ^[row-filters-and-column-masks-databricks-on-aws.md]

- Consistent rules across many tables
- Separation of duties between policy authors and data stewards
- Automatic coverage of new tables as they are tagged
- Central management by higher-level admins

## When to Use Table-Level Controls

Use table-level row filters and column masks when: ^[row-filters-and-column-masks-databricks-on-aws.md]

- Fine-grained, table-specific control is required
- Only a small number of tables need restrictions
- The table owner needs direct management authority without dependency on central policy

## Alternative: Dynamic Views

Dynamic views provide another approach to row-level and column-level access control. They wrap one or more base tables in a SQL view that filters rows, masks columns, or reshapes data, typically gated by group-membership functions like `is_account_group_member()`. Use dynamic views when you want to expose a curated, transformed, or joined version of your data to users who do not have access to the underlying tables. ^[row-filters-and-column-masks-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that hosts both ABAC policies and table-level controls
- Data governance — Overview of access control strategies
- [Row filters](/concepts/row-filter-policies.md) — Detailed documentation on table-level row filtering
- [Column masks](/concepts/column-mask-policies.md) — Detailed documentation on table-level column masking
- Dynamic views — View-based approach to row and column security
- tag-based governance — Foundational mechanism for ABAC policy application

## Sources

- row-filters-and-column-masks-databricks-on-aws.md

# Citations

1. [row-filters-and-column-masks-databricks-on-aws.md](/references/row-filters-and-column-masks-databricks-on-aws-f091f827.md)

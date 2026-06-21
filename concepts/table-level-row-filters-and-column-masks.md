---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5a03b7c7ac4277452e32097c99c7c2ffb18011cc271e0caeda37411004a565be
  pageDirectory: concepts
  sources:
    - access-control-in-unity-catalog-databricks-on-aws.md
    - when-to-use-abac-vs-table-level-row-filters-and-column-masks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - table-level-row-filters-and-column-masks
    - Column Masks and Table-Level Row Filters
    - TRFACM
    - ABAC vs Table-Level Row Filters and Column Masks
  citations:
    - file: when-to-use-abac-vs-table-level-row-filters-and-column-masks-databricks-on-aws.md
    - file: access-control-in-unity-catalog-databricks-on-aws.md
title: Table-Level Row Filters and Column Masks
description: Per-table UDF-based filters and masks that control what data users see at query time within tables.
tags:
  - unity-catalog
  - data-filtering
  - data-masking
timestamp: "2026-06-19T21:55:01.345Z"
---

# Table-Level Row Filters and Column Masks

**Table-Level Row Filters and Column Masks** are per‑table security mechanisms in [Unity Catalog](/concepts/unity-catalog.md) that restrict which rows and columns users can see at query time. They are applied directly to individual tables using `ALTER TABLE` statements and are managed by the table owner. ^[when-to-use-abac-vs-table-level-row-filters-and-column-masks-databricks-on-aws.md] ^[access-control-in-unity-catalog-databricks-on-aws.md]

## Overview

Row filters and column masks implement fine‑grained access control **within** a table. A row filter is a [User‑Defined Function (UDF)](/concepts/abac-user-defined-functions-udfs.md) that returns a boolean expression; only rows for which the expression evaluates to `TRUE` are visible to the querying user. A column mask is a UDF that transforms the column value (e.g., replacing an email with a hashed value) for users who do not meet the mask’s condition. ^[when-to-use-abac-vs-table-level-row-filters-and-column-masks-databricks-on-aws.md]

These controls do **not** grant access to the underlying table on their own. Base table access must be granted separately through object‑level privileges (`GRANT`). Row filters and column masks only add restrictions on top of those privileges. ^[when-to-use-abac-vs-table-level-row-filters-and-column-masks-databricks-on-aws.md]

Table owners manage their own filters and masks directly. They can create, modify, or remove them without requiring a centralized tag system or administrator involvement. This makes them suitable for small, stable sets of tables where each table has specific, non‑generalizable logic. ^[when-to-use-abac-vs-table-level-row-filters-and-column-masks-databricks-on-aws.md]

## When to Use Table‑Level Filters and Masks

Use table‑level row filters and column masks when: ^[when-to-use-abac-vs-table-level-row-filters-and-column-masks-databricks-on-aws.md]

- Each table has strict, per‑table logic that does not apply to other tables.
- Table owners should manage their own data protection directly, without a centralized tag system.
- The set of protected tables is small and changes infrequently.

Databricks recommends [ABAC (Attribute‑Based Access Control)](/concepts/abac-attribute-based-access-control.md) for centralised, tag‑driven policies that scale across many tables. Row filters and column masks should be used only when per‑table logic is required or when ABAC has not yet been adopted. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## Comparison with ABAC Policies

| Aspect | Table‑Level Row Filters / Column Masks | ABAC Policies |
|---|---|---|
| **Scope** | Per‑table; applied via `ALTER TABLE`. | Attached at catalog, schema, or table level; apply dynamically based on governed tags. |
| **Management** | Table owner manages directly. | Higher‑level administrator enforces centrally; table owner cannot remove or bypass. |
| **Tagging required** | No. | Relies on governed tags for dynamic matching. |
| **Scalability** | Each table must be configured individually. | A single policy can cover many tables automatically when they are tagged. |
| **Conflict resolution** | When combined with ABAC, only one distinct row filter and one distinct column mask per column can resolve; if functions differ, access is blocked. | Same as left. |

^[when-to-use-abac-vs-table-level-row-filters-and-column-masks-databricks-on-aws.md]

## Combining ABAC and Table‑Level Filters and Masks

Both mechanisms can coexist on the same table. At query time, Unity Catalog evaluates them independently for the querying user. The following rules apply: ^[when-to-use-abac-vs-table-level-row-filters-and-column-masks-databricks-on-aws.md]

- Only **one** distinct row filter can apply.
- Only **one** distinct column mask can be resolved per column.

Databricks evaluates conflict by comparing the functions applied, not the data output. If both an ABAC policy and a table‑level filter or mask apply the **same** function for the same user, execution proceeds. If they apply **different** functions, Databricks blocks access and returns an error — even if the two functions produce identical data. ^[when-to-use-abac-vs-table-level-row-filters-and-column-masks-databricks-on-aws.md]

## Comparison with Dynamic Views

Dynamic views can also implement row‑ and column‑level security by embedding identity functions like `current_user()` and `is_account_group_member()` in the view definition. Dynamic views, row filters, and column masks all apply filtering or transformation logic at query time, but they differ in management and auditing: ^[when-to-use-abac-vs-table-level-row-filters-and-column-masks-databricks-on-aws.md]

| Aspect | Row Filters / Column Masks | Dynamic Views |
|---|---|---|
| **Management** | Applied directly on a table. | Separate view object that may span multiple tables. |
| **Auditing** | Semantic metadata (tags, policy definitions) is stored in system tables, aiding auditability. | Lack semantic metadata; harder to audit at scale. |
| **Performance** | May have optimisation limitations compared to views. | Fully support query optimisation and predicate pushdown. |
| **Security** | No special vulnerability. | Vulnerable to probing attacks unless wrapped in a secure barrier. |

Use dynamic views when you need access control across multiple source tables or want to reshape data for sharing. Use row filters and column masks when you want to control access on individual tables without introducing new objects. ^[when-to-use-abac-vs-table-level-row-filters-and-column-masks-databricks-on-aws.md]

## Related Concepts

- [ABAC](/concepts/abac-attribute-based-access-control.md) – Centralised, tag‑driven access control that works alongside table‑level filters.
- [Unity Catalog](/concepts/unity-catalog.md) – The data governance layer that hosts securable objects and fine‑grained controls.
- Dynamic Views – Another mechanism for row‑ and column‑level security.
- GRANT – Object‑level privilege statements that must be issued before filters/masks can take effect.
- [Row Filters](/concepts/row-filter-policies.md) – The specific UDF‑based row‑restriction mechanism.
- Column Masks – The specific UDF‑based column‑transformation mechanism.

## Sources

- access-control-in-unity-catalog-databricks-on-aws.md
- when-to-use-abac-vs-table-level-row-filters-and-column-masks-databricks-on-aws.md

# Citations

1. [when-to-use-abac-vs-table-level-row-filters-and-column-masks-databricks-on-aws.md](/references/when-to-use-abac-vs-table-level-row-filters-and-column-masks-databricks-on-aws-d92860b7.md)
2. [access-control-in-unity-catalog-databricks-on-aws.md](/references/access-control-in-unity-catalog-databricks-on-aws-817d7ad8.md)

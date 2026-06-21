---
title: When to use ABAC vs table-level row filters and column masks | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/abac-vs-rls-cm
ingestedAt: "2026-06-18T08:03:15.681Z"
---

Unity Catalog supports two approaches for row-level and column-level security: [ABAC policies](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/) and [table-level row filters and column masks](https://docs.databricks.com/aws/en/data-governance/unity-catalog/filters-and-masks/). Neither approach grants access to data on its own — both add restrictions on top of existing object-level privileges. You must grant base table access separately through object-level permissions (`GRANT`).

The core difference is where the restrictions are defined. **Table-level row filters and column masks** apply sensitivity controls directly on individual tables using `ALTER TABLE`. Table owners manage their own data protection without needing a governed tag system. This is straightforward for a small number of tables, but each table must be configured individually, and table owners can modify or remove their own filters and masks.

**ABAC policies** attach at the catalog, schema, or table level and match tables and columns dynamically based on governed tags. A policy defined at the catalog level applies to all tables in that catalog, and individual table owners can't remove, modify, or bypass it. The policy lives on the catalog and is evaluated by Unity Catalog before the query reaches the runtime. This lets higher-level administrators enforce organization-wide rules and ensure that lower-level administrators and owners can't circumvent them.

## Detailed comparison summary[​](#detailed-comparison-summary "Direct link to detailed-comparison-summary")

This table summarizes the differences between ABAC policies and table-level row filters and column masks.

In general, use **ABAC policies** when:

*   You need consistent access rules across many tables, schemas, or catalogs.
*   Your organization separates duties. For example, policy authors define rules, and data stewards classify data with tags.
*   Your data estate is growing and you want new tables covered automatically when they are tagged.
*   You need the `EXCEPT` clause to allow operations like time travel, OpenSharing, or full query optimization for specific principals.

In general, use **table-level row filters and column masks** when:

*   Each table has strict, specific logic that doesn't generalize to other tables.
*   Table owners should manage their own filters and masks directly, without a centralized tag system.
*   You have a small, stable set of tables that change infrequently.

## Combining ABAC and table-level row filters and column masks[​](#combining-abac-and-table-level-row-filters-and-column-masks "Direct link to combining-abac-and-table-level-row-filters-and-column-masks")

ABAC and table-level row filters and column masks can co-exist on the same table. At query time, the policies are evaluated independently for the querying user with the following rules:

*   Only one distinct row filter can apply.
*   Only one distinct column mask can be resolved per column.

Databricks evaluates conflict by comparing the functions applied, not the data output. If both an ABAC policy and a table-level filter or mask apply the same row filter or column mask function for the same user, Databricks allows execution. If they apply different functions, Databricks blocks access and returns an error, even if those functions produce identical data output.

For details on conflict resolution and troubleshooting, see [Rules for multiple filters and masks](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/policy-evaluation#multiple-filters).

## Row-level and column-level security with dynamic views[​](#row-level-and-column-level-security-with-dynamic-views "Direct link to row-level-and-column-level-security-with-dynamic-views")

[Dynamic views](https://docs.databricks.com/aws/en/views/dynamic) can also implement row-level and column-level security by embedding identity functions like `current_user()` and `is_account_group_member()` directly in the view definition. Dynamic views, row filters, and column masks all apply filtering or transformation logic at query time, but they differ in how they are managed, scoped, and exposed to users.

Use dynamic views when you need fine-grained access control that spans multiple source tables or reshapes data for sharing. Use row filters and column masks when you want to control access on individual tables without introducing new objects.

For example, a dynamic view can mask an email column for non-auditors:

SQL

    CREATE VIEW sales_redacted ASSELECT  user_id,  CASE    WHEN is_account_group_member('auditors') THEN email    ELSE regexp_extract(email, '^.*@(.*)$', 1)  END AS email,  country,  product,  totalFROM sales_raw

Dynamic views fully support query optimization and predicate pushdown, so they can offer better query performance than row filters and column masks. They also prevent users from modifying the underlying tables.

However, dynamic views have two drawbacks for data governance:

*   **Limited auditing**: Dynamic views lack semantic metadata such as tags or policy definitions in system tables, which makes them harder to audit at scale.
*   **Vulnerability to probing**: Because they lack a `SecureView` barrier, they don't protect against probing attacks, where a user crafts a predicate with side effects to infer information about filtered rows. See [Understand predicate pushdown on protected tables](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/performance#predicate-pushdown).

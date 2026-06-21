---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 74535ab5162710f78de5fdb250acbd0a9879c635e75f0f938101a845ad726c5b
  pageDirectory: concepts
  sources:
    - hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dynamic-views-for-fine-grained-access-control
    - DVFFAC
    - Dynamic Views for Access Control
    - Fine-grained access control (FGAC)
    - Fine-grained access controls
    - Fine‑grained access control on dedicated compute
    - fine-grained access control (FGAC) filtering
    - fine-grained access control filtering
  citations:
    - file: hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md
    - file: when-to-use-abac-vs-table-level-row-filters-and-column-masks-databricks-on-aws.md
    - file: hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md
      start: 17
      end: 22
title: Dynamic Views for Fine-Grained Access Control
description: Using dynamic views with is_member() and current_user() functions in view definitions to enforce column-level, row-level, and data-masking permissions in the Hive metastore.
tags:
  - hive-metastore
  - access-control
  - dynamic-views
  - data-masking
timestamp: "2026-06-19T19:04:30.892Z"
---

# Dynamic Views for Fine-Grained Access Control

**Dynamic views** are read-only SQL views that embed identity-based logic directly in their definition to implement row-level security, column-level permissions, and data masking without requiring separate access control policies. By using built-in functions like `current_user()`, `is_member()`, and `is_account_group_member()`, you can dynamically restrict what data a user sees based on their identity or group membership at query time.^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Overview

Dynamic views implement fine-grained access control by embedding filtering or transformation logic in the view body. They differ from [Row Filter Policies](/concepts/row-filter-policies.md) and [Column Mask Policies](/concepts/column-mask-policies.md), which apply restrictions at the table level, and from ABAC Policies, which use governed tags and are managed centrally. Dynamic views are defined in SQL and evaluated at query time, supporting full query optimization and predicate pushdown.^[when-to-use-abac-vs-table-level-row-filters-and-column-masks-databricks-on-aws.md]

## Identity Functions for Dynamic Views

### `current_user()`

The `current_user()` function returns the name of the current user. It is available in both Unity Catalog and the legacy Hive [Metastore](/concepts/metastore.md) and can be used to tailor view results to individual users.^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

### `is_member()`

The `is_member()` function determines if the current user is a member of a specific Databricks group at the workspace level. This function is available in the legacy Hive [Metastore](/concepts/metastore.md) and allows you to check group membership dynamically in view definitions.^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md:17-22]

### `is_account_group_member()`

The `is_account_group_member()` function checks membership in an account-level group. This is the recommended identity function for dynamic views in [Unity Catalog](/concepts/unity-catalog.md), providing consistent group membership across workspaces.^[when-to-use-abac-vs-table-level-row-filters-and-column-masks-databricks-on-aws.md]

## Usage Patterns

### Column-Level Permissions

You can limit which columns a specific group or user can see using a `CASE` statement in the view definition. The following example shows only users in the `auditors` group the full email address; all other users see the literal `'REDACTED'`. This approach allows for all the usual performance optimizations provided by Spark because the `CASE` statement is evaluated at analysis time.^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

```sql
CREATE VIEW sales_redacted AS
SELECT
  user_id,
  CASE WHEN is_group_member('auditors') THEN email ELSE 'REDACTED' END AS email,
  country,
  product,
  total
FROM sales_raw;
```

### Row-Level Permissions

You can restrict which rows a user sees using a `WHERE` clause with identity functions. The following example lets users in the `managers` group see all transaction amounts, while other users only see transactions with a total <= $1,000,000.^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

```sql
CREATE VIEW sales_redacted AS
SELECT user_id, country, product, total
FROM sales_raw
WHERE
  CASE
    WHEN is_group_member('managers') THEN TRUE
    ELSE total <= 1000000
  END;
```

### Data Masking

Dynamic views support complex masking expressions beyond simple redaction. The following example lets all users perform analysis on email domains, but only the `auditors` group sees full email addresses:^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

```sql
CREATE VIEW sales_redacted AS
SELECT
  user_id,
  region,
  CASE
    WHEN is_group_member('auditors') THEN email
    ELSE regexp_extract(email, '^.*@(.*), 1)
  END AS email
FROM sales_raw;
```

## Comparison with Other Access Control Approaches

Dynamic views differ from [Row Filter Policies](/concepts/row-filter-policies.md) and [Column Mask Policies](/concepts/column-mask-policies.md) in several key ways:^[when-to-use-abac-vs-table-level-row-filters-and-column-masks-databricks-on-aws.md]

| Aspect | Dynamic Views | Row Filters / Column Masks |
|--------|---------------|---------------------------|
| Definition | SQL view with identity functions | Policy function attached to table |
| Scope | Can span multiple source tables | Single table |
| Management | Created and owned by view creator | Attached by table owner |
| Query optimization | Full predicate pushdown | May block predicate pushdown |
| User modification | Users cannot modify underlying tables | Table owners can modify/remove filters |

Dynamic views fully support query optimization and predicate pushdown, so they can offer better query performance than row filters and column masks. They also prevent users from modifying the underlying tables, since views are read-only.^[when-to-use-abac-vs-table-level-row-filters-and-column-masks-databricks-on-aws.md]

However, dynamic views have two limitations for data governance:^[when-to-use-abac-vs-table-level-row-filters-and-column-masks-databricks-on-aws.md]

- **Limited auditing**: Dynamic views lack semantic metadata such as tags or policy definitions in system tables, making them harder to audit at scale.
- **Security considerations**: Dynamic views may reveal the filtering logic in their definitions, which could be visible through `EXPLAIN` plans or direct view inspection.

## Best Practices

- **Use dynamic views when restrictions span multiple tables.** If the access logic joins or reshapes data from several source tables, a dynamic view is more natural than separate filters on each table.^[when-to-use-abac-vs-table-level-row-filters-and-column-masks-databricks-on-aws.md]
- **Use account-level groups for Unity Catalog.** In Unity Catalog, prefer `is_account_group_member()` over workspace-level group functions for consistent group membership across workspaces.^[when-to-use-abac-vs-table-level-row-filters-and-column-masks-databricks-on-aws.md]
- **Consider row filters and column masks for single-table access control.** For restrictions on a single table, row filters and column masks provide better auditability and centralized management.^[when-to-use-abac-vs-table-level-row-filters-and-column-masks-databricks-on-aws.md]

## Related Concepts

- [Row Filter Policies](/concepts/row-filter-policies.md) — Table-level row security
- [Column Mask Policies](/concepts/column-mask-policies.md) — Table-level column security
- [ABAC Policy Requirements and Prerequisites](/concepts/abac-policy-requirements-and-prerequisites.md) — Centralized attribute-based access control
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer supporting dynamic views
- [Hive Metastore](/concepts/built-in-hive-metastore.md) — Legacy [Metastore](/concepts/metastore.md) with dynamic view support
- [Data Masking](/concepts/conditional-column-masking.md) — Techniques for obscuring sensitive data

## Sources

- hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md
- when-to-use-abac-vs-table-level-row-filters-and-column-masks-databricks-on-aws.md

# Citations

1. [hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md](/references/hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws-f9aea977.md)
2. [when-to-use-abac-vs-table-level-row-filters-and-column-masks-databricks-on-aws.md](/references/when-to-use-abac-vs-table-level-row-filters-and-column-masks-databricks-on-aws-d92860b7.md)
3. [hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md:17-22](/references/hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws-f9aea977.md)

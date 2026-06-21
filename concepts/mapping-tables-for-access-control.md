---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1c19e004369cc82f1920ebfe681adb45122c65d5f219d404a23c833170a19469
  pageDirectory: concepts
  sources:
    - manually-apply-row-filters-and-column-masks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mapping-tables-for-access-control
    - MTFAC
    - Mapping Tables for Dynamic Access Control
    - Mapping Tables
    - Mapping tables
  citations:
    - file: manually-apply-row-filters-and-column-masks-databricks-on-aws.md
title: Mapping Tables for Access Control
description: A pattern using dedicated mapping tables (access-control lists) to encode which users or groups can access specific rows, integrated via row filters that join against the mapping table.
tags:
  - data-governance
  - unity-catalog
  - access-control-lists
timestamp: "2026-06-19T19:30:43.749Z"
---

# Mapping Tables for Access Control

**Mapping Tables for Access Control** is a pattern for implementing row-level and column-level security in Unity Catalog by using dedicated lookup tables that encode which users or groups can access specific data rows. This approach enables flexible, scalable access control lists (ACLs) without requiring hard‑coded rules in individual filter or mask functions. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

## Overview

Mapping tables (also called access-control lists) are ordinary Unity Catalog tables that store user-to-permission mappings. They are used inside [Row Filter](/concepts/row-filter-policies.md) or Column Mask SQL UDFs to determine whether the current user has access to a given row or column value. The UDF joins the mapping table against the current session user or group membership to produce a boolean result. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

This methodology addresses many use cases, including: ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

- Imposing restrictions based on the logged-in user while accommodating different rules for specific user groups.
- Creating intricate hierarchies, such as organizational structures, that require diverse sets of rules.
- Replicating complex security models from external source systems.

## How It Works

1. **Create a mapping table** that lists the permitted users or groups. For example, a table of valid usernames: ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

   ```sql
   CREATE TABLE valid_users(username string);
   INSERT INTO valid_users VALUES
     ('fred@databricks.com'),
     ('barney@databricks.com');
   ```

2. **Create a row filter UDF** that checks whether the current user appears in the mapping table. The UDF uses the `SESSION_USER()` function to get the current user and `EXISTS` to test membership: ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

   ```sql
   CREATE FUNCTION row_filter()
     RETURN EXISTS(
       SELECT 1 FROM valid_users v
       WHERE v.username = SESSION_USER());
   ```

3. **Apply the filter to a table**, either at creation time or with `ALTER TABLE`. The filter passes no column parameters (empty parentheses) because the decision depends only on the user identity, not on column values: ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

   ```sql
   CREATE TABLE data_table (x INT, y INT, z INT)
     WITH ROW FILTER row_filter ON ();
   ```

   Only users listed in `valid_users` will see any rows in the table.

## Combining Mapping Tables with Group Membership

Mapping tables can also store account group names. A UDF can combine column-value conditions with group membership checks: ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

```sql
CREATE TABLE valid_accounts(account string);
INSERT INTO valid_accounts VALUES ('admin'), ('cstaff');

CREATE FUNCTION row_filter_small_values (x INT, y INT, z INT)
  RETURN (x < 5 AND y < 5 AND z < 5)
    OR EXISTS(
      SELECT 1 FROM valid_accounts v
      WHERE IS_ACCOUNT_GROUP_MEMBER(v.account));

ALTER TABLE data_table SET ROW FILTER row_filter_small_values ON (x, y, z);
```

In this example, rows are visible if *all* column values are less than 5, or if the invoking user is a member of any group listed in the `valid_accounts` mapping table. Members of the `admin` or `cstaff` groups see all rows regardless of values. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

## Definer vs. Invoker Rights

All row filter and column mask UDFs run with definer's rights, **except** for functions that check user context — such as `SESSION_USER()` and `IS_ACCOUNT_GROUP_MEMBER()` — which always run as the invoker. This means that mapping table lookups inside a UDF see the data as the function owner, while user-identity checks see the actual calling user. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

## Comparison with Attribute-Based Access Control

If you are looking for a centralized, tag-based approach to filtering and masking across many tables, consider [Attribute-Based Access Control (ABAC) in Unity Catalog](/concepts/attribute-based-access-control-abac-in-unity-catalog.md). ABAC enables you to manage policies using governed tags and apply them consistently, whereas mapping tables require you to write and maintain individual UDFs for each table. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

## Best Practices

- Store mapping tables in a dedicated schema to simplify permission management.
- Keep mapping tables small and indexed for performance, because the UDF runs the `EXISTS` query on every row evaluation.
- Use `IS_ACCOUNT_GROUP_MEMBER()` for group-based access rather than enumerating individual users, to reduce maintenance overhead.
- When using mapping tables with column masks, pass additional columns via the `USING COLUMNS` clause to control behavior based on other column values.

## Related Concepts

- [Row Filter](/concepts/row-filter-policies.md) — Applies a UDF to restrict which rows are visible.
- Column Mask — Applies a UDF to transform column values at query time.
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — Tag-based alternative for centralized policy management.
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that enforces row filters and column masks.
- Session User Function — SQL function used within UDFs to identify the current user.
- Account Group Membership — SQL function to check if the user belongs to a specific group.

## Sources

- manually-apply-row-filters-and-column-masks-databricks-on-aws.md

# Citations

1. [manually-apply-row-filters-and-column-masks-databricks-on-aws.md](/references/manually-apply-row-filters-and-column-masks-databricks-on-aws-b311d10e.md)

---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5b013adbe4abb7ba0b3c2c97cde815eb799a376d7fdbac197a293e733a039ecd
  pageDirectory: concepts
  sources:
    - core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - abac-policy-types
    - APT
    - ABAC policy|ABAC policies
  citations:
    - file: core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
title: ABAC Policy Types
description: "Three policy types in Unity Catalog ABAC: row filter policies, column mask policies, and GRANT policies (Beta), each enforcing different access controls based on tag conditions."
tags:
  - abac
  - policies
  - access-control
timestamp: "2026-06-19T17:53:46.614Z"
---

# ABAC Policy Types

**ABAC Policy Types** are the three categories of attribute-based access control (ABAC) policies supported in Unity Catalog: row filter policies, column mask policies, and GRANT policies (Beta). Each type defines a different action that Unity Catalog applies when a policy's tag-based conditions match a securable object. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Overview

ABAC policies are attached to [Unity Catalog](/concepts/unity-catalog.md) securable objects to define access control rules based on tag conditions. Each policy specifies a scope (catalog, schema, or table), the principals it applies to, the action to perform, and the tag-based conditions that determine which objects or columns are targeted. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

Row filter and column mask policies require a User-Defined Function (UDF) to implement the filtering or masking logic. GRANT policies do not use UDFs and instead grant privileges directly when conditions are met. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Row Filter Policies

Row filter policies restrict which rows a user can see in a table based on values in columns identified by tags. The policy references a UDF that evaluates each row; rows where the function returns `FALSE` are excluded from query results. Arguments are passed to the UDF through the `USING COLUMNS` clause. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

**Example use case:** For a sales catalog, ensure the EMEA team sees only EMEA sale records across all tables that have a column tagged `region`. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

```sql
CREATE FUNCTION filter_by_region(region STRING, allowed STRING) RETURNS BOOLEAN
    RETURN region = allowed;

CREATE POLICY regional_access_emea
ON CATALOG sales
ROW FILTER filter_by_region
TO `emea team`
FOR TABLES
MATCH COLUMNS has_tag('region') AS rgn
USING COLUMNS (rgn, 'EMEA');
```

^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Column Mask Policies

Column mask policies control what values a user sees for specific columns identified by tags. The policy references a UDF that takes the column value as input and returns the original value or a masked version. The masked column value is bound automatically as the first argument from the `ON COLUMN` clause, and additional arguments can be passed through `USING COLUMNS`. The return type must match or be castable to the column's data type. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

**Example use case:** Mask SSN columns tagged with `pii : ssn` so that users see `***-**-XXXX` (last four digits only) unless they are in a compliance group exempt from the policy. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

```sql
CREATE FUNCTION mask_ssn(ssn STRING, show_last INT) RETURNS STRING
    RETURN CONCAT('***-**-', RIGHT(ssn, show_last));

CREATE POLICY mask_ssn_columns
ON CATALOG hr_catalog
COLUMN MASK mask_ssn
TO `account users` EXCEPT `compliance team`
FOR TABLES
MATCH COLUMNS has_tag_value('pii', 'ssn') AS ssn_col
ON COLUMN ssn_col
USING COLUMNS (4);
```

^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

The `USING COLUMNS` clause passes arguments to the UDF. It accepts aliases for columns that match a tag-based expression, or constant values (quoted strings, numeric literals, boolean values (`TRUE`/`FALSE`), or `NULL`), supplied in the order the function expects them. For column mask policies, these are additional arguments beyond the masked column (which is bound automatically from `ON COLUMN`). This allows a single UDF to be reused across policies with different parameters. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

SQL UDFs are recommended for better performance. Python UDFs registered in Unity Catalog are also supported, though the query optimizer cannot inline or optimize them the way it can SQL UDFs. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## GRANT Policies (Beta)

GRANT policies dynamically grant a Unity Catalog privilege when their tag-based condition matches a securable object's tags. Each time a user attempts to access a securable object, Unity Catalog identifies all GRANT policies whose scope covers the object, checks whether the user is in the `TO` list and not in the `EXCEPT` list, and evaluates the policy's `WHEN` condition against the tags on the securable, including inherited tags. If the policy applies, Unity Catalog grants the privilege. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

GRANT policies use the same evaluation model as row filter and column mask policies, except they do not use UDFs. The condition is expressed inline in the policy definition. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

The effective privileges on an object are the union of direct grants and any applicable GRANT policies. A principal has the privilege if a GRANT policy in scope applies to that principal or a direct `GRANT` of the same privilege applies. GRANT policies only add access; they cannot revoke access that was granted directly. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

GRANT policies are currently scoped to `EXECUTE` on models. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Policy Scope

Each policy specifies a scope using the `ON` clause:

- **Row filter and column mask policies** support scopes of `CATALOG`, `SCHEMA`, or `TABLE`. Tables, including streaming tables and materialized views, are the only supported securable object type, specified using the `FOR TABLES` clause. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- **GRANT policies (Beta)** support scopes of `CATALOG` and `SCHEMA`, and support models only, specified using `GRANT EXECUTE FOR MODELS`. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

A policy attached at a catalog evaluates against all tables in that catalog. A policy attached at a schema evaluates against all tables in that schema. A policy attached at a table evaluates only against that table. Databricks recommends attaching policies at the highest applicable level, usually the catalog, to maximize governance efficiency. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Conditions and Built-in Functions

Both table conditions (`WHEN` clause) and column conditions (`MATCH COLUMNS` clause) use built-in functions evaluated by Unity Catalog against securable metadata:

- `has_tag(tag_key)` — checks whether a given tag key is present on the target data object, either directly or through tag inheritance. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- `has_tag_value(tag_key, tag_value)` — checks whether a given tag key-value pair is present. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

Tags do not propagate from tables to columns. Using `has_tag()` in a `MATCH COLUMNS` clause only matches column-level tags, not tags on the parent table or its ancestors. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Related Concepts

- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md)
- [Governed Tags](/concepts/governed-tags.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Row Filters and Column Masks](/concepts/row-filters-and-column-masks.md)
- User-Defined Functions (UDFs)
- Policy Evaluation Model
- [Separation of Duties in ABAC](/concepts/separation-of-duties-in-abac.md)

## Sources

- core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md

# Citations

1. [core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md](/references/core-concepts-for-attribute-based-access-control-abac-databricks-on-aws-ca4d8af7.md)

---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2c1fcffd4be36757ce6bbfb8c9bb56ee7150cbf7fdd4bf4c6735fd19d6cb11d5
  pageDirectory: concepts
  sources:
    - core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - abac-attribute-based-access-control
    - A(AC
    - ABAC (Attribute‑Based Access Control)
    - ABAC
  citations:
    - file: core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
title: ABAC (Attribute-Based Access Control)
description: An access-control model in Unity Catalog that uses governed tags and policies to grant permissions based on object attributes rather than per-object grants.
tags:
  - access-control
  - data-governance
  - unity-catalog
timestamp: "2026-06-19T14:27:28.918Z"
---

# ABAC (Attribute-Based Access Control)

**Attribute-based access control (ABAC)** is a dynamic access control model where access decisions are based on policies evaluated against attributes associated with securable objects. In [Unity Catalog](/concepts/unity-catalog.md), these attributes are represented through governed tags, which are used in policy conditions to match data objects within a given scope, such as a catalog or a schema. This allows a single policy to apply automatically across multiple data objects that meet its conditions.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

ABAC supports row- and column-level security through **row filter policies** and **column mask policies** on tables, materialized views, and streaming tables. It also supports dynamic privilege grants through **GRANT policies** (Beta), currently scoped to `EXECUTE` on models.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Governed Tags

In Unity Catalog, attributes are implemented as governed tags—key-value pairs defined at the account level and applied to Unity Catalog securable objects such as catalogs, schemas, tables, columns, models, and volumes. They represent characteristics such as sensitivity, classification, or business domain. By default, securables inherit tags from their parent catalog or schema, except column tags, which must be applied directly on the column.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

Governed tags can be referenced in policy conditions using built-in functions like `has_tag()` and `has_tag_value()`, which check whether a given tag is present on the target data object, either directly or through inheritance. Tags are defined at the account level, allowing the same tag taxonomy across the entire data estate in an account, including across multiple metastores.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Policies

Policies are attached to securable objects in Unity Catalog to define access control rules based on tag conditions. Each policy specifies:

- **Scope**: The securable object where the policy is attached (e.g., `CATALOG`, `SCHEMA`, or `TABLE` for row/column masks; `CATALOG` or `SCHEMA` for GRANT policies).
- **Principals**: Users, groups, or service principals subject to the policy (the `TO` clause), with optional exceptions (`EXCEPT`).
- **Actions**: The operation applied—row filter, column mask, or privilege grant.
- **Conditions**: Tag-based expressions that determine which tables or columns the policy targets.

Databricks recommends attaching policies at the highest applicable level (usually the catalog) to maximize governance efficiency.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

Policies are managed via SQL statements (`CREATE POLICY`, `DROP POLICY`, etc.), REST APIs, Databricks SDKs, or Terraform.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Policy Types

### Row Filter Policies

Row filter policies restrict which rows a user can see in a table based on values in columns identified by tags. The policy references a user-defined function (UDF) that evaluates each row. Rows where the UDF returns `FALSE` are excluded from query results. Arguments are passed to the UDF through the `USING COLUMNS` clause.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

Example: A policy that limits the EMEA team to see only EMEA sales records across all tables that have a column tagged with `region`.

### Column Mask Policies

Column mask policies control what values a user sees for specific columns identified by tags. The policy references a UDF that takes the column value as input and returns the original value or a masked version. The masked column value is bound automatically as the first argument from the `ON COLUMN` clause. Additional arguments can be passed via `USING COLUMNS`. The return type must match or be castable to the column's data type.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

Example: A policy that masks SSN columns tagged with `pii : ssn` so that non‑exempt users see only the last four digits.

### GRANT Policies (Beta)

GRANT policies dynamically grant a Unity Catalog privilege when their tag-based condition matches a securable object’s tags. They use an inline condition (no UDF) and only add access—they cannot revoke a direct grant. Effective privileges are the union of direct grants and applicable GRANT policies.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Conditions and Built-in Functions

- **Table conditions** (`WHEN` clause): Boolean expressions that match tables based on their tags. If omitted, defaults to `TRUE`.
- **Column conditions** (`MATCH COLUMNS` clause): One or more comma‑separated boolean expressions using `has_tag()`, `has_tag_value()`, or logical combinations. Each expression can be assigned an alias (via `AS`) for use in `ON COLUMN` and `USING COLUMNS` clauses. A policy can include up to three column expressions, and all must match for the policy to apply.

Tags do not propagate from tables to columns; `has_tag()` in `MATCH COLUMNS` only matches column‑level tags. The functions use snake_case naming; the older camelCase forms still work but are not recommended for new policies.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## User-Defined Functions (UDFs)

Row filter and column mask policies use UDFs to implement filtering or masking logic. SQL UDFs are recommended for better performance; Python UDFs registered in Unity Catalog are also supported but cannot be optimized as efficiently by the query optimizer.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Separation of Duties and Permissions

Setting up ABAC involves several steps, each with specific permission requirements, enabling distribution of tasks across specialized teams:

1. **Create the tag taxonomy** – Account admin or user with `CREATE` permission for tags at the account level.
2. **Tag data assets** – Requires `ASSIGN` on the tag and `APPLY TAG` on the object. Correct tagging is essential for ABAC policies.
3. **Create a policy** – Requires `MANAGE` permission (or ownership) on the securable object where the policy is attached, and for row/column masks, `EXECUTE` on the UDF.
4. **Create data objects** – Data creators need relevant creation privileges (e.g., `CREATE TABLE`). New objects inherit tags from parents; creators can also apply additional tags.
5. **Access governed objects** – Users must have direct table grants (e.g., `SELECT`) for row/column mask policies to apply; GRANT policies grant privileges themselves and union with direct grants.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

Tagging is a security boundary; organizations should control who can apply tags and audit tag changes.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Benefits of ABAC

- **Reusable policies based on attributes** – A single policy can apply to multiple data objects that match the same attribute conditions, rather than being tied to one specific object.
- **Automatic application to new objects** – When new data objects are created within scope and tagged appropriately, existing ABAC policies apply without additional configuration.
- **Consistent enforcement within a scope** – Policies attached at the catalog or schema level are evaluated dynamically against matching objects, removing differences in how similar data is filtered or masked.
- **Lower ongoing maintenance** – Changes can be made by updating policy logic or governed tags, rather than revisiting each individual object as required with table-level row filters and column masks.
- **Centralized governance** – Policies can be defined once and applied across many matching data objects, allowing governance teams to manage controls across larger parts of the data estate with fewer definitions.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [Row Filters and Column Masks](/concepts/row-filters-and-column-masks.md)
- [Governed Tags](/concepts/governed-tags.md)
- Access Control in Databricks
- User-Defined Functions (UDFs)
- [GRANT Policies for Models (Beta)](/concepts/grant-policies-beta.md)
- [Policy Evaluation in Unity Catalog](/concepts/effective-policy-evaluation-in-unity-catalog.md)
- ABAC Best Practices

## Sources

- core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md

# Citations

1. [core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md](/references/core-concepts-for-attribute-based-access-control-abac-databricks-on-aws-ca4d8af7.md)

---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e9bc40efd08e403831e106d72518f38f02b53ba7019b482b8a842124d1f940b8
  pageDirectory: concepts
  sources:
    - create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - abac-row-filter-policies
    - ARFP
  citations:
    - file: create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
title: ABAC Row Filter Policies
description: A Unity Catalog policy type that filters rows from query results based on a user-defined function (UDF), where rows returning FALSE are excluded.
tags:
  - data-governance
  - unity-catalog
  - access-control
  - abac
timestamp: "2026-06-19T17:59:54.844Z"
---

Here is the updated wiki page based on the provided source material.

# ABAC Row Filter Policies

**ABAC Row Filter Policies** are a type of [ABAC](/concepts/abac-attribute-based-access-control.md) policy in Unity Catalog that restrict which rows a user can see in a table based on attribute conditions evaluated against [Governed Tags](/concepts/governed-tags.md) on columns. They provide a dynamic, tag-driven approach to row-level security that can be applied across multiple tables within a catalog or schema scope without per-object configuration. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## How Row Filter Policies Work

A row filter policy references a User-Defined Functions (UDFs) that implements the filtering logic. The UDF evaluates each row and returns a boolean. Rows where the function returns `FALSE` are excluded from query results. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

Arguments are passed to the UDF through the `USING COLUMNS` clause. These inputs can be a column matched by tags, a column matched by a custom expression, or a constant value. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

### Policy Structure

Each row filter policy specifies:

- **Scope**: The catalog, schema, or table where the policy is attached. The policy evaluates against all tables in that scope (specified via `FOR TABLES`). ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

- **Principals**: The users, groups, or service principals who are subject to the policy and those who are exempted. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

- **Table condition** (`WHEN` clause): A Boolean expression using built-in functions like `has_tag()` to match tables based on their tags. If omitted, defaults to `TRUE`, meaning the policy applies to all tables in scope. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

- **Column conditions** (`MATCH COLUMNS` clause): One or more comma-separated Boolean expressions that identify which columns the policy targets, using functions like `has_tag()` and `has_tag_value()`. Each expression can be assigned an alias (after `AS`) that can be referenced in `USING COLUMNS`. A policy can include up to 3 column expressions; all must match for the policy to apply. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

- **Filter function** (`ROW FILTER` clause): The name of the UDF that implements the row-level filtering logic. You can specify an existing UDF or define a SQL function inline. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

### Built-in Functions for Conditions

The `WHEN` and `MATCH COLUMNS` clauses use the following built-in functions evaluated against securable metadata:

- `has_tag('tag_key')` – Returns true if the object has the specified tag key.
- `has_tag_value('tag_key', 'tag_value')` – Returns true if the object has the specified tag key with the specified value.

These functions use snake_case naming. The older camelCase forms (`hasTag`, `hasTagValue`) continue to work but are not recommended for new policies. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

Importantly, tags do not propagate from tables to columns. Using `has_tag()` in a `MATCH COLUMNS` clause only matches column-level tags, not tags on the parent table or its ancestors. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Permissions and Separation of Duties

Creating a policy requires `MANAGE` on the securable object or object ownership. You must also have `EXECUTE` on the UDF that implements the filtering logic. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Benefits

Row filter policies offer:
- **Reusable policies** based on attributes rather than specific objects.
- **Automatic application** to new tables created within scope and properly tagged.
- **Consistent enforcement** across all matching tables in a catalog or schema.
- **Lower maintenance** – policy logic or tag changes propagate without per-object updates. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Related Concepts

- [ABAC Column Mask Policies](/concepts/abac-column-mask-policies.md) – The column-level counterpart that controls how values are presented.
- [ABAC GRANT Policies](/concepts/abac-grant-policies.md) – Dynamic privilege grants based on tags (Beta).
- Table-Level Row Filters – Per-object row filters that do not use tags.
- [Policy Evaluation](/concepts/dynamic-abac-policy-evaluation.md) – How policies are evaluated at query time.
- [Governed Tags](/concepts/governed-tags.md) – The tag system used to identify columns and tables.

## Sources

- create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md

# Citations

1. [create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md](/references/create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws-d315307d.md)

---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0ece58b12642022d41788e03ea635428a9e013293c2aed3a7da281f176295fe6
  pageDirectory: concepts
  sources:
    - access-control-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-attribute-based-access-control-abac
    - UCAAC(
    - unity-catalog-abac-attribute-based-access-control
    - UCA(AC
  citations:
    - file: core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
title: Unity Catalog Attribute-Based Access Control (ABAC)
description: Centralized, tag-driven policies that dynamically filter and mask data across the catalog, recommended over per-table row/column filters.
tags:
  - access-control
  - abac
  - unity-catalog
timestamp: "2026-06-18T14:16:09.888Z"
---

# Unity Catalog Attribute-Based Access Control (ABAC)

**Attribute-Based Access Control (ABAC)** is a fine-grained access control model in [Unity Catalog](/concepts/unity-catalog.md) that dynamically grants or restricts access to data and AI assets based on attributes—specifically, governed tags attached to securable objects. Instead of issuing explicit `GRANT` statements for each individual object, ABAC uses centralized policies that evaluate tag conditions at access time, enabling scalable, attribute-driven governance. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Overview

ABAC in Unity Catalog is built on two complementary policy types:

- **GRANT policies** — Dynamically grant privileges (currently `EXECUTE` on models) to securable objects whose tags match a condition. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Row filter and column mask policies** — Restrict the content of data a user can already access, using user-defined functions (UDFs) to filter rows or mask columns at query time. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

Both policy types rely on [Governed Tags](/concepts/governed-tags.md)—key-value pairs that you or Databricks apply to securable objects—to make access decisions. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

ABAC works alongside the traditional privilege model. A principal must first have the necessary base privileges (e.g., `USE CATALOG`, `USE SCHEMA`, `SELECT` on a table) before ABAC policies further refine what they can see or execute. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## How ABAC Works

1. **Tagging** — Tag securable objects (catalogs, schemas, tables, models) with governed tags. Tags can be applied manually or through tag inheritance from parent objects. System tags (prefixed `system.`) are automatically assigned by Databricks. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
2. **Policy creation** — Define an ABAC policy that specifies a `WHEN` condition referencing governed tags, the principals it applies to (via `TO` and optionally `EXCEPT`), and the privilege to grant (for GRANT policies) or the UDF to apply (for row/column policies). ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
3. **Access evaluation** — Every time a user attempts to access a securable object, Unity Catalog evaluates all applicable ABAC policies. For GRANT policies, if a principal is in `TO` and the policy’s `WHEN` condition matches the object’s tags, the privilege is effectively granted. For row/column policies, the filter or mask instruction is applied to the query result. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## ABAC Policy Types

### GRANT Policies

GRANT policies dynamically grant a privilege (currently limited to `EXECUTE` on models) to all securable objects in a catalog or schema that carry specific governed tags. They do not require a UDF; the condition is expressed inline. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

**Example** — Grant `EXECUTE` on all models tagged `lifecycle = 'production'` in schema `production.ml_models` to the `analysts` group:

```sql
CREATE POLICY grant_production_model_access
ON SCHEMA production.ml_models
COMMENT 'Grant EXECUTE on production MLflow models'
TO `analysts`
GRANT EXECUTE FOR MODELS
WHEN has_tag_value('lifecycle', 'production');
```

GRANT policies support referencing both user-defined governed tags and Databricks-defined system tags (e.g., `ai.model_creator`). ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

### Row Filter Policies

Row filter policies use a UDF to decide which rows a principal can see in a table. The policy is attached to a table and is evaluated per query. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

### Column Mask Policies

Column mask policies use a UDF to transform or hide column values for certain principals at query time. They are commonly used to mask personally identifiable information (PII). ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Key Concepts

- **Governed Tags** — User-defined key-value pairs applied to securable objects. Used in ABAC policy conditions. Tags can be inherited from parent objects. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- **System Tags** — Predefined tags set by Databricks, such as `ai.model_creator`. They can be used in GRANT policies without manual tagging. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **`has_tag_value(tag_key, tag_value)`** — A system function used in GRANT policy `WHEN` conditions to test for the existence of a tag with a specific value. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **`TO` / `EXCEPT`** — Clauses that specify which principals the policy applies to or excludes. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **`SHOW EFFECTIVE POLICIES`** — A command to list all ABAC policies that affect a given catalog or schema, including inherited catalog-level policies. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Creating and Managing ABAC Policies

### GRANT Policies

- **SQL** — Use `CREATE POLICY` with the `GRANT` syntax. Requires `MANAGE` privilege on the target catalog or schema. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Catalog Explorer** — Navigate to a catalog or schema, click the **Policies** tab, then **New policy**. Fill in the details. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Compute requirement** — Creating, altering, or dropping policies with SQL requires a classic compute cluster running Databricks Runtime 18.3 or above. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

### Row Filter and Column Mask Policies

These are created using SQL with a UDF or via Catalog Explorer. They are scoped to individual tables. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Best Practices

- **Use tag inheritance for safe defaults.** Apply default tag values at the catalog or schema level so children inherit them unless overridden. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Use groups in `TO` and `EXCEPT`** instead of individual users to simplify maintenance. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Attach policies at the smallest scope** that covers the intended objects to avoid unintended access. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Do not mix GRANT policies and direct grants for the same privilege.** Choose one approach per privilege to avoid confusion. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Grant base privileges directly.** ABAC policies do not grant `USE CATALOG` or `USE SCHEMA`; those must be granted explicitly. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Limitations (Beta)

- GRANT policies currently support only `EXECUTE` on models. Other privileges and securable types are not yet supported. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- Policies can be attached only to catalogs or schemas, not directly to models. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- `SHOW GRANTS` does not reflect privileges granted via GRANT policies. Use `SHOW EFFECTIVE POLICIES` instead. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- [Delta Sharing](/concepts/delta-sharing.md) cannot share models that have GRANT policies defined on them. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- `INFORMATION_SCHEMA` does not include ABAC policy information. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Audit Logging

Operations on ABAC policies (create, alter, drop) are logged with the same event types as row filter and column mask policies: `createPolicy`, `deletePolicy`, `getPolicy`, `listPolicies`. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [Governed Tags](/concepts/governed-tags.md)
- [System Tags](/concepts/system-tags.md)
- [ABAC GRANT Policies](/concepts/abac-grant-policy.md)
- [Row Filter Policies](/concepts/row-filter-policies.md)
- [Column Mask Policies](/concepts/column-mask-policies.md)
- Access Control in Unity Catalog
- MLflow Models

## Sources

- core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
- abac-grant-policies-for-models-beta-databricks-on-aws.md
- access-control-in-unity-catalog-databricks-on-aws.md

# Citations

1. [core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md](/references/core-concepts-for-attribute-based-access-control-abac-databricks-on-aws-ca4d8af7.md)
2. [abac-grant-policies-for-models-beta-databricks-on-aws.md](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)

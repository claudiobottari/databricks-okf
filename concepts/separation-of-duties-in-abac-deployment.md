---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 84ce753144f93c6243c2153a90b1323fabc0d698d3681dd6255f6ca946083bc6
  pageDirectory: concepts
  sources:
    - core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - separation-of-duties-in-abac-deployment
    - SODIAD
  citations:
    - file: core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
title: Separation of Duties in ABAC Deployment
description: "A five-step workflow distributing ABAC responsibilities across specialized roles: tag taxonomy creation, data asset tagging, policy creation, data object creation, and governed data access — each with distinct permission requirements."
tags:
  - governance
  - roles
  - permissions
  - workflow
timestamp: "2026-06-19T09:25:57.287Z"
---

# Separation of Duties in ABAC Deployment

**Separation of duties in ABAC deployment** refers to the distribution of tasks across specialized roles when setting up [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) in Databricks Unity Catalog. By dividing responsibilities such as tag creation, data classification, policy writing, object creation, and data access, organizations can enforce least-privilege principles and reduce the risk that any single user can both classify data and define the policies that govern it. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## The Five Steps and Corresponding Roles

Setting up ABAC involves five steps, each with its own permission requirements. Organizations can assign these steps to different groups based on their desired separation of duties. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

### 1. Create the Tag Taxonomy

An account admin or a user with `CREATE` permission for tags at the account level defines the governed tag keys and their allowed values before anyone applies them or writes policies. For example, a `sensitivity` tag with controlled values (`public`, `internal`, `confidential`, `restricted`) or a `pii` tag with values like `ssn`, `email`, and `phone_number`. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

- **Role:** Account admin or tag creator.
- **Permission required:** `CREATE` permission for tags at the account level.

### 2. Tag Data Assets

A data steward, data creator, or AI classification system applies governed tags to Unity Catalog securable objects such as catalogs, schemas, tables, columns, models, and volumes. For example, tagging columns containing personally identifiable information with `pii : ssn`. Correct tagging is essential for ABAC policies to apply. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

- **Role:** Data steward, data creator, or automated classifier.
- **Permission required:** `ASSIGN` on the tag plus `APPLY TAG` on the object.
- **Security boundary warning:** If a user can change tags on a data asset, they can change which policies apply to it. Organizations should control who can apply tags and audit tag changes. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

### 3. Create a Policy

A governance admin creates an ABAC policy at a scope (catalog, schema, or table). The policy specifies the principals, conditions (using tag-based functions like `has_tag()` and `has_tag_value()`), and the action — a row filter, a column mask, or a privilege grant. Row filter and column mask policies also require a user-defined function (UDF) and the user must have `EXECUTE` privilege on that UDF. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

- **Role:** Governance admin.
- **Permission required:** `MANAGE` permission or ownership on the securable object where the policy is attached; for row filter and column mask policies, also `EXECUTE` on the referenced UDF.

### 4. Create Data Objects

Data creators create securable objects (tables, models, volumes) within the scopes to which they have been granted access. New objects inherit tags from parent catalogs and schemas. Data creators automatically get `APPLY TAG` on objects they create, so they can apply additional tags. They do not need to configure any access controls if policies are set at higher levels, which is the recommended practice. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

- **Role:** Data creator.
- **Permission required:** `CREATE TABLE` or other relevant creation privileges on the parent object.

### 5. Access Governed Objects

When a user attempts to access a securable object within a policy’s scope, Unity Catalog evaluates applicable policies automatically. For row filter and column mask policies, the user sees filtered or masked data if the table or columns match the policy’s conditions and the user is not exempt. For GRANT policies (Beta), the user gains the granted privilege if the conditions match. Users must already have `SELECT` (or appropriate) privileges on the table through a direct object grant; policies do not grant access on their own (except GRANT policies, which union with direct grants). ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

- **Role:** Data consumer.
- **Permission required:** Direct object privileges such as `SELECT` on the table (for row filter and column mask policies). GRANT policies grant the privilege themselves.

## Required Permissions Summary

| Step | Role | Minimum Permission |
|------|------|-------------------|
| 1. Create tag taxonomy | Account admin / tag creator | `CREATE` (tag at account level) |
| 2. Tag data assets | Data steward / creator | `ASSIGN` on tag + `APPLY TAG` on object |
| 3. Create a policy | Governance admin | `MANAGE` or ownership on scope + `EXECUTE` on UDF (for RLS/CM) |
| 4. Create data objects | Data creator | `CREATE TABLE` or equivalent on parent |
| 5. Access governed data | Data consumer | Direct privilege (e.g., `SELECT`) or GRANT policy grants |

^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Benefits of Separation of Duties

- **Centralized governance:** Policies can be defined once by a governance team and applied across many matching data objects, reducing per-object configuration. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- **Lower maintenance:** Changes can be made by updating policies or tags rather than revisiting each individual object. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- **Consistent enforcement:** Policies attached at catalog or schema level apply dynamically to all matching objects in scope, removing inconsistencies. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- **Automatic application to new objects:** New data objects created within scope and tagged appropriately automatically gain the protections of existing policies without additional configuration. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Related Concepts

- [ABAC Column Mask Policies](/concepts/abac-column-mask-policy.md)
- [ABAC Row Filter Policies](/concepts/abac-row-filter-policy.md)
- [ABAC GRANT Policies](/concepts/abac-grant-policy.md) (Beta)
- [Governed Tags](/concepts/governed-tags.md)
- [Unity Catalog Permissions](/concepts/unity-catalog-permissions-model.md)
- [Row Filters and Column Masks (table-level)](/concepts/row-filters-and-column-masks.md)
- Policy Evaluation Order

## Sources

- core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md

# Citations

1. [core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md](/references/core-concepts-for-attribute-based-access-control-abac-databricks-on-aws-ca4d8af7.md)

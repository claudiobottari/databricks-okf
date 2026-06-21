---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ddbd1997931acc8b1450a8058ae3de0381611e633beb0211b7f8607580dcd9fd
  pageDirectory: concepts
  sources:
    - core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - separation-of-duties-in-abac
    - SODIA
  citations:
    - file: core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
title: Separation of Duties in ABAC
description: "ABAC enables distributing governance tasks across specialized teams: taxonomy creators, data stewards (tagging), governance admins (policy creation), data creators, and data consumers."
tags:
  - abac
  - governance
  - roles
timestamp: "2026-06-19T17:54:14.840Z"
---

# Separation of Duties in ABAC

**Separation of duties in [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md)** refers to the practice of distributing the tasks required to set up and maintain ABAC across specialized groups, so that no single person has end-to-end control over both tagging and policy creation. This reduces the risk of errors or misuse and aligns with governance best practices. Unity Catalog's ABAC model naturally supports this division by requiring distinct permissions for each step.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## How separation of duties works

Setting up ABAC involves several sequential steps, each with its own permission requirements. An organization can assign these steps to different roles — for example, a governance team defines the tag taxonomy, data stewards classify assets, governance admins write policies, data creators build objects within governed scopes, and data consumers access the governed objects.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

![Diagram showing the five roles and their interactions: tag taxonomy creator, data steward/tagger, governance admin, data creator, and data consumer.](https://docs.databricks.com/aws/en/assets/images/abac-separation-of-duties-b1d6e07523bce2aadaf83ee6b61243b4.png)^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

### Step 1 – Create the tag taxonomy

Define the governed tag keys and their allowed values before anyone applies them or writes policies. For example, create a `sensitivity` tag with controlled values (`public`, `internal`, `confidential`, `restricted`) or a `pii` tag with values like `ssn`, `email`, and `phone_number`.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

- **Required permissions:** Account admin, or a user with `CREATE` permission for tags at the account level.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

### Step 2 – Tag data assets

A data steward, data creator, or AI classification system applies [Governed Tags](/concepts/governed-tags.md) to Unity Catalog securable objects such as catalogs, schemas, tables, columns, models, and volumes. For example, tag columns that contain personally identifiable information with `pii : ssn`, or tag a model with `lifecycle : production`. Correct tagging is the essential first step for ABAC policies to apply.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

- **Required permissions:** `ASSIGN` on the tag, and `APPLY TAG` on the object.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

> **Warning:** Tagging is a security boundary. If a user can change tags on a data asset, they can change which policies apply to it. Organizations should control who can apply tags and audit tag changes.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

### Step 3 – Create a policy

A governance admin creates a policy at a scope, such as a catalog or schema. The policy specifies who it applies to, what conditions it evaluates, and the action to apply — a [row filter](/concepts/row-filter-policies.md), a [column mask](/concepts/column-mask-policies.md), or a [privilege grant](/concepts/abac-grant-policy.md).^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

- **Required permissions:** `MANAGE` permission or object ownership on the securable object where the policy is attached. For row filter and column mask policies, also `EXECUTE` privilege on the user-defined function (UDF).^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

### Step 4 – Create data objects

Data creators create securable objects such as tables, models, or volumes within the scopes to which they have access. New objects inherit tags from parent catalogs and schemas. Data creators also have `APPLY TAG` automatically on objects they create, so they can apply additional tags. Alternatively, they can rely on automatic data classification to handle tagging. If an organization relies on data creators to tag their own objects, it should establish clear tagging practices. Data creators do not need to configure any access controls if policies are set at higher levels, which Databricks recommends.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

- **Required permissions:** `CREATE TABLE` or other relevant creation privileges on the parent object.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

### Step 5 – Access governed objects

When a user attempts to access a securable object within a policy's scope, Unity Catalog evaluates applicable policies automatically. For row filter and column mask policies, the user sees filtered or masked data if the table or columns match the policy's conditions and the user is not exempt. For GRANT policies (Beta), the user gains the granted privilege if the conditions match and the user is in `TO` and not in `EXCEPT`.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

- **Required permissions:** For row filter and column mask policies, users must have a direct grant on the table (e.g., `SELECT`). These policies do not grant permissions on their own. GRANT policies (Beta) grant the privilege themselves and union with any direct grants on the same securable.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Benefits of separation of duties

- **Reduced risk of privilege escalation:** No single person can both tag an asset and write a policy that grants themselves access.
- **Clear accountability:** Each role has a defined scope and permission boundary.
- **Scalable governance:** Teams can specialize (e.g., security team defines tags, data stewards apply them, compliance team writes policies) without overlapping responsibilities.^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Related concepts

- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — The access control model that enables this separation.
- [Governed Tags](/concepts/governed-tags.md) — The key-value attributes used in ABAC policies.
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that enforces ABAC permissions.
- [Row Filter Policies](/concepts/row-filter-policies.md) — ABAC policies that restrict data rows.
- [Column Mask Policies](/concepts/column-mask-policies.md) — ABAC policies that mask sensitive columns.
- [ABAC GRANT Policy](/concepts/abac-grant-policy.md) — Dynamic privilege grants based on tag conditions (Beta).
- [ABAC Tagging Taxonomy and Governance](/concepts/abac-tagging-taxonomy-and-governance.md) — Best practices for standardizing tags.
- [ABAC Policy Scoping and Sprawl Prevention](/concepts/abac-policy-scoping-and-sprawl-prevention.md) — Guidance on policy placement and management.

## Sources

- core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md

# Citations

1. [core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md](/references/core-concepts-for-attribute-based-access-control-abac-databricks-on-aws-ca4d8af7.md)

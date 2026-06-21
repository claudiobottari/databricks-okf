---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 067f86fe9295e462c46526f57bd77255187b3397af66b36df5d34f64084e9f8d
  pageDirectory: concepts
  sources:
    - core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
  confidence: 0.96
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - abac-separation-of-duties
    - ASOD
  citations:
    - file: core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
title: ABAC Separation of Duties
description: The role-based permission model for ABAC that distributes responsibilities across specialized teams (tag taxonomy creators, data stewards, governance admins, data creators, data consumers) with distinct permission requirements per role.
tags:
  - governance
  - roles
  - unity-catalog
timestamp: "2026-06-18T14:46:03.583Z"
---

# ABAC Separation of Duties

**ABAC Separation of Duties** is the practice of distributing the tasks required to set up and maintain attribute-based access control (ABAC) across specialized teams or roles. By dividing responsibilities—such as defining tag taxonomies, classifying data, writing policies, creating data objects, and consuming data—organizations can enforce checks and balances, reduce the risk of privilege abuse, and keep governance processes auditable. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## The Five-Step Separation Model

Unity Catalog’s ABAC implementation supports a natural division of labor. Each step has distinct permission requirements and is typically owned by a different persona.

### 1. Create the tag taxonomy

Governed tag keys and their allowed values are defined centrally at the account level. This ensures a consistent vocabulary before any tags are applied or policies written.

*Required permissions:* Account admin, or a user with `CREATE` permission for tags at the account level.
*Example persona:* Central governance team. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

This step establishes the attribute vocabulary that all later steps depend on.

### 2. Tag data assets

Data stewards, data creators, or automated classification systems apply governed tags to Unity Catalog securable objects (catalogs, schemas, tables, columns, models, volumes). Correct tagging is essential; if tags are missing or wrong, ABAC policies will not apply as intended.

*Required permissions:* `ASSIGN` on the tag, and `APPLY TAG` on the object.
*Example persona:* Data steward.
*Warning:* Because tag changes can alter which policies apply, organizations should audit tag modifications and tightly control who can apply tags. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

### 3. Create a policy

A governance admin writes ABAC policies—row filter, column mask, or GRANT (Beta)—and attaches them at a scope (catalog or schema). The policy defines the principals, conditions (tag-based), and the action (filter, mask, or grant).

*Required permissions:* `MANAGE` permission or object ownership on the securable object where the policy is attached. For row filter and column mask policies, also `EXECUTE` privilege on the referenced UDF.
*Example persona:* Governance admin.
*Policy types:*
- Row filter policies – restrict which rows a user can see.
- Column mask policies – control how column values are displayed.
- [ABAC GRANT Policies](/concepts/abac-grant-policies.md) (Beta) – dynamically grant privileges (currently `EXECUTE` on models) when tag conditions match. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

### 4. Create data objects

Data creators build tables, models, volumes, and other objects within the scopes governed by ABAC policies. New objects inherit tags from parent catalogs and schemas. Data creators may also apply additional tags directly, or rely on automatic classification. They do not need to configure access controls if policies are set at higher levels.

*Required permissions:* `CREATE TABLE` or other creation privileges on the parent object.
*Example persona:* Data engineer or analyst.
*Best practice:* Establish clear tagging guidelines so that creators tag objects consistently. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

### 5. Access governed objects

When a user queries a governed object, Unity Catalog evaluates applicable policies automatically. For row filter or column mask policies, the user sees filtered or masked data (if the user is not exempt in the policy). For GRANT policies, the user gains the granted privilege if the conditions match and the principal is in `TO` and not in `EXCEPT`.

*Required permissions:* Row filter and column mask policies do **not** grant access themselves; users must already hold `SELECT` (or another relevant privilege) through a direct grant. GRANT policies (Beta) grant the privilege directly and union with any existing direct grants.
*Example persona:* Data consumer (analyst, scientist, application). ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Benefits of a Separated Duties Model

- **Reduced risk of privilege escalation:** No single person can both define the tag taxonomy, assign tags, and write policies that affect their own access.
- **Clear accountability:** Each action (tag creation, tagging, policy creation, data creation, access) is associated with a specific role and permission, making audits straightforward.
- **Scalability:** Centralized governance teams can define policies once at a catalog or schema level, while data creators and stewards continue to work independently.
- **Policy reuse and consistency:** Policies are written against governed tags, not individual objects, so they automatically cover new objects that carry the right tags.

## Related Concepts

- [Governed Tags](/concepts/governed-tags.md) – The attribute vocabulary used in ABAC policy conditions.
- [Row Filter Policies](/concepts/row-filter-policies.md) – ABAC policies that limit row-level visibility.
- [Column Mask Policies](/concepts/column-mask-policies.md) – ABAC policies that transform column values.
- [ABAC GRANT Policies and Direct Grants Auditing](/concepts/abac-grant-policies-and-direct-grants-auditing.md) – How to audit both policy-based and direct privilege sources.
- [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md) – The full set of securable actions that can be granted or used in ABAC policies.
- [ABAC Policy Evaluation](/concepts/dynamic-abac-policy-evaluation.md) – How policies are evaluated dynamically at query time.

## Sources

- core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md

# Citations

1. [core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md](/references/core-concepts-for-attribute-based-access-control-abac-databricks-on-aws-ca4d8af7.md)

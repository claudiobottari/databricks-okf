---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 946ce7e99dad58dfd53b7d2be8daae3eae6af67f042f29f8fafd7469ed8c7449
  pageDirectory: concepts
  sources:
    - create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-policy-lifecycle-management
    - UCPLM
  citations:
    - file: best-practices-for-abac-policies-databricks-on-aws.md
    - file: create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
title: Unity Catalog Policy Lifecycle Management
description: Create, edit, delete, show, and describe operations for ABAC policies using Catalog Explorer UI, SQL statements (CREATE POLICY, SHOW POLICIES, DESCRIBE POLICY), Python SDK, REST APIs, and Terraform.
tags:
  - data-governance
  - unity-catalog
  - policy-management
timestamp: "2026-06-18T11:20:17.320Z"
---

# Unity Catalog Policy Lifecycle Management

**Unity Catalog Policy Lifecycle Management** refers to the complete set of processes for creating, deploying, monitoring, updating, and retiring [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies within [Unity Catalog](/concepts/unity-catalog.md). This encompasses [Row Filter Policies](/concepts/row-filter-policies.md), [Column Mask Policies](/concepts/column-mask-policies.md), and [ABAC GRANT Policies](/concepts/abac-grant-policy.md) for models.

## Policy Lifecycle Stages

### 1. Planning and Design

Before creating any policy, establish a consistent tagging taxonomy and define governance requirements. Determine which securable objects (catalogs, schemas, or tables) need protection and what access rules should apply.^[best-practices-for-abac-policies-databricks-on-aws.md]

Key planning considerations:
- Define tag key names, allowed values, and naming conventions across teams
- Start with a small number of broad policies rather than creating separate policies for every edge case
- Identify which [Governed Tags](/concepts/governed-tags.md) will drive policy conditions

### 2. Creation

Policies are created at the catalog, schema, or table level depending on the desired scope. Creation requires `MANAGE` on the securable object or object ownership.^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

**Requirements for creation:**
- Databricks Runtime 16.4 or above (or serverless compute)
- For row filters and column masks: a user-defined function (UDF) in Unity Catalog with `EXECUTE` permission, or a SQL function defined inline
- For GRANT policies: only `WHEN` conditions using governed tags (no UDF required)
- Governed tags applied to target objects

**Creation methods:**
- **Catalog Explorer UI**: Navigate to Catalog, select the target object, click the Policies tab, and use the New policy form
- **SQL**: Use `CREATE POLICY` statements
- **Python SDK**: Use Databricks REST APIs and SDKs

### 3. Policy Types

| Policy Type | Purpose | Mechanism |
|-------------|---------|-----------|
| Row filter | Restricts which rows users can see | UDF returns boolean; `FALSE` rows excluded |
| Column mask | Obscures sensitive column values | UDF transforms values; masks sensitive data |
| GRANT (Beta) | Dynamically grants `EXECUTE` on models | Evaluates tag conditions at access time; no UDF |

### 4. Deployment and Evaluation

ABAC policies are dynamic—they evaluate at query time based on user identity, group memberships, and tags on the data object in the policy scope. Unlike static table-level permissions, policies are not visible on the table definition itself.^[best-practices-for-abac-policies-databricks-on-aws.md]

**Evaluation behavior:**
- Catalog-scoped policies evaluate against all tables in the catalog
- Schema-scoped policies evaluate against all tables in the schema
- When new tables or models are added, existing policies apply as long as their tags match the policy's conditions

### 5. Monitoring and Audit

Continuous monitoring ensures policies remain effective and do not create unintended access gaps.

**Audit tools:**
- `SHOW POLICIES` lists all policies defined on a securable object
- `SHOW EFFECTIVE POLICIES` includes inherited policies from parent scopes
- `DESCRIBE POLICY` displays detailed policy properties
- Audit log system tables track policy CRUD operations and tag assignments

**Example audit queries:**
```sql
-- Track all ABAC policy operations
SELECT event_time, action_name, user_identity.email AS actor,
       request_params.name AS policy_name,
       request_params.on_securable_type
FROM system.access.audit
WHERE service_name = 'unityCatalog'
  AND action_name IN ('createPolicy', 'deletePolicy', 'getPolicy', 'listPolicies')
ORDER BY event_time DESC;
```

### 6. Maintenance and Updates

Policies require periodic review to prevent sprawl and accommodate changing data landscapes.

**Update mechanisms:**
- **Catalog Explorer**: Select the policy, update fields (description, principals, conditions), click Update policy
- **SQL**: Use `ALTER POLICY` statements
- **Python SDK**: Use REST API endpoints

**Best practices for maintenance:**
- Review policies periodically and consolidate overlapping ones
- Use tag inheritance for safe defaults at parent catalog/schema levels
- Audit both direct grants and ABAC GRANT policies together (effective privileges are the union of both)
- Avoid mixing GRANT policies and direct grants for the same privilege on a securable

### 7. Retirement and Deletion

Policies should be removed when no longer needed to maintain a clean governance model.

**Deletion methods:**
- **Catalog Explorer**: Select the policy and click Delete policy
- **SQL**: Use `DROP POLICY` statements
- **Python SDK**: Use REST API endpoints

**When to retire policies:**
- When tagging taxonomies change and existing tags no longer apply
- When data classifications change (e.g., data is no longer sensitive)
- When organizational restructuring changes team access requirements

## Performance Considerations

Large numbers of policies and complex conditions can slow authorization checks. Follow these guidelines to maintain performance:^[best-practices-for-abac-policies-databricks-on-aws.md]

- Attach policies at the highest applicable scope (catalog or schema level)
- Avoid creating a separate policy for every edge case
- Use a small, well-defined set of tags rather than ad-hoc proliferation
- Consolidate overlapping policies

## Security Boundaries

Tagging is a security boundary in ABAC. If a user can change tags on a data asset, they can change which policies apply to it. Wrong or missing tags can leave data unprotected or inaccessible.^[best-practices-for-abac-policies-databricks-on-aws.md]

**Security best practices:**
- Restrict tag creation and modification to authorized data stewards or governance admins
- Audit tag changes regularly using the audit log system table
- Apply default restrictive tags (like `classification: unverified`) to new objects until review

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The data governance platform providing ABAC capabilities
- [Row Filter Policies](/concepts/row-filter-policies.md) — Mechanisms for restricting data rows by user attributes
- [Column Mask Policies](/concepts/column-mask-policies.md) — Mechanisms for obscuring sensitive data columns
- [ABAC GRANT Policy](/concepts/abac-grant-policy.md) — Dynamic privilege grants based on tag conditions
- [Governed Tags](/concepts/governed-tags.md) — Tags that drive ABAC policy evaluation
- [System Tags](/concepts/system-tags.md) — Predefined tags provided by Databricks
- [ABAC Policy Scoping and Sprawl Prevention](/concepts/abac-policy-scoping-and-sprawl-prevention.md) — Best practices for managing policy proliferation
- [ABAC Tagging Taxonomy and Governance](/concepts/abac-tagging-taxonomy-and-governance.md) — Standards for tag classification and management
- [Audit Log System Table](/concepts/audit-log-system-table-requirements.md) — System table for tracking governance operations

## Sources

- best-practices-for-abac-policies-databricks-on-aws.md
- create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md

# Citations

1. [best-practices-for-abac-policies-databricks-on-aws.md](/references/best-practices-for-abac-policies-databricks-on-aws-716fb4af.md)
2. [create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md](/references/create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws-d315307d.md)

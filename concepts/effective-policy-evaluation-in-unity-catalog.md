---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c1fe4a68be34aab66ec0de524719f956241a0b208d9e4c87d81e0cf5839a0235
  pageDirectory: concepts
  sources:
    - create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - effective-policy-evaluation-in-unity-catalog
    - EPEIUC
    - Policy Evaluation in Unity Catalog
  citations:
    - file: create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
title: Effective Policy Evaluation in Unity Catalog
description: Policies applied at a catalog or schema scope are inherited by child objects (tables); SHOW EFFECTIVE POLICIES reveals all applicable policies including those from parent scopes, enabling table admins to see rules without requiring parent-level read access.
tags:
  - data-governance
  - unity-catalog
  - policy-evaluation
  - abac
timestamp: "2026-06-18T11:20:08.607Z"
---

# Effective Policy Evaluation in Unity Catalog

**Effective policy evaluation** in [Unity Catalog](/concepts/unity-catalog.md) refers to the process of inspecting which [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) row filter and column mask policies apply to a given securable object, understanding their details, and auditing changes over time. Proper evaluation ensures that governance rules are correctly enforced and accessible to administrators without unnecessary permissions.

## Viewing Policies with `SHOW POLICIES` and `SHOW EFFECTIVE POLICIES`

Use the `SHOW POLICIES` command to list all policies directly defined on a catalog, schema, or table. To also see policies inherited from parent scopes (for example, a catalog-level policy that affects a table), use `SHOW EFFECTIVE POLICIES`. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

```sql
SHOW [EFFECTIVE] POLICIES ON { CATALOG | SCHEMA | TABLE } securable_name
```

The result includes the policy name, policy type, and the object where each policy is defined. Notably, viewing effective policies for a table does **not** require the caller to have `MANAGE` permissions on the parent catalog or schema. This allows a table admin to see all applicable rules without needing read access to sibling tables’ policies. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Describing a Policy with `DESCRIBE POLICY`

To obtain the full details of a specific policy — including its condition expression, function name, principals, and timestamps — use the `DESCRIBE POLICY` statement. This command requires `MANAGE` on the target securable object or object ownership. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

```sql
DESC | DESCRIBE POLICY policy_name ON { CATALOG | SCHEMA | TABLE } securable_name
```

The output is a set of key-value pairs covering name, securable object type and full name, principals (applied to and except lists), the UDF or inline function used, and the condition expression. This is the primary tool for a detailed inspection of a policy’s behavior. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Audit Logging for Policy Operations

Databricks logs all governed tag and ABAC policy changes in the audit log system table. Common action names include `createPolicy`, `deletePolicy`, `getPolicy`, and `listPolicies`. For tag assignments, actions such as `createEntityTagAssignment` and `deleteEntityTagAssignment` are recorded. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

Example queries can be run against `system.access.audit` to review policy creation, deletion, and tag modifications, allowing administrators to trace who changed a policy and when. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

```sql
-- All ABAC policy CRUD operations
SELECT event_time, action_name, user_identity.email AS actor,
       request_params.name AS policy_name,
       request_params.on_securable_type,
       request_params.on_securable_fullname,
       request_params.policy_info,
       response.status_code
FROM system.access.audit
WHERE service_name = 'unityCatalog'
  AND action_name IN ('createPolicy', 'deletePolicy', 'getPolicy', 'listPolicies')
ORDER BY event_time DESC;
```

## Key Considerations for Evaluation

*   **Effective vs. direct policies:** A table may be subject to policies defined at the catalog, schema, or table level. `SHOW EFFECTIVE POLICIES` is the authoritative way to see the full set of policies that will be applied at query time. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]
*   **Minimal permissions for inspection:** Table owners can inspect effective policies without needing elevated rights on parent objects, simplifying governance audits. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]
*   **Audit trail completeness:** Combine `DESCRIBE POLICY` with audit log queries to understand both the current configuration and its history. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Sources

- create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md

---

**Related concepts:** [Row Filter Policies](/concepts/row-filter-policies.md), [Column Mask Policies](/concepts/column-mask-policies.md), [ABAC GRANT Policy](/concepts/abac-grant-policy.md), [Unity Catalog](/concepts/unity-catalog.md), [Governed Tags](/concepts/governed-tags.md), [Audit Log System Table](/concepts/audit-log-system-table-requirements.md)

# Citations

1. [create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md](/references/create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws-d315307d.md)

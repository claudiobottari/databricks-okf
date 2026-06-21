---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dfff0a94802ceaa26d2cdac8aa56e342534d8c29f8d914e6886cad59a0c6037d
  pageDirectory: concepts
  sources:
    - best-practices-for-abac-policies-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - principal-targeting-with-to-and-except-clauses
    - EXCEPT Clauses and Principal Targeting with TO
    - PTWTAEC
  citations:
    - file: best-practices-for-abac-policies-databricks-on-aws.md
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
title: Principal Targeting with TO and EXCEPT Clauses
description: Using policy TO and EXCEPT clauses to define which users/groups a row filter or column mask applies to, keeping UDF logic simple and avoiding complex conditional logic inside functions.
tags:
  - abac
  - row-filter
  - column-mask
timestamp: "2026-06-19T09:09:26.554Z"
---

Here is the wiki page for "Principal Targeting with TO and EXCEPT Clauses", written based solely on the provided source material.

---

# Principal Targeting with `TO` and `EXCEPT` Clauses

**Principal targeting with `TO` and `EXCEPT` clauses** is a mechanism in [Unity Catalog](/concepts/unity-catalog.md) ABAC policies that defines which principals (users, service principals, or groups) a policy applies to or excludes from. These clauses are used in both [ABAC GRANT Policy](/concepts/abac-grant-policy.md) (for attribute-based grants) and [Row Filter Policies](/concepts/row-filter-policies.md) / [Column Mask Policies](/concepts/column-mask-policies.md) (for data filtering and masking). ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Usage in ABAC GRANT Policies

In ABAC GRANT policies (currently Beta, supporting `EXECUTE` on models), the `TO` and `EXCEPT` clauses are the **only** mechanism for targeting principals because GRANT policies do not use user-defined functions (UDFs). ^[best-practices-for-abac-policies-databricks-on-aws.md]

The `TO` clause lists one or more principals to whom the grant is applied. The optional `EXCEPT` clause excludes specified principals from the grant, even if they are members of a group listed in `TO`. The effective set of principals is the `TO` set minus the `EXCEPT` set. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Usage in Row Filter and Column Mask Policies

For row filter and column mask policies, `TO` and `EXCEPT` are the **preferred** way to define which users and groups the policy applies to. This keeps the UDF logic simple and avoids complex conditional logic inside the UDF. The `EXCEPT` clause excludes specific principals from the policy entirely, so they are not subject to any filtering or masking. ^[best-practices-for-abac-policies-databricks-on-aws.md]

When complex conditional logic is required, identity functions such as `is_account_group_member()` inside UDFs remain a valid alternative. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Syntax

### GRANT Policy Syntax

```sql
CREATE POLICY policy_name
ON { CATALOG | SCHEMA } securable_name
TO `principal1` [, `principal2` ...]
[EXCEPT `principal1` [, `principal2` ...]]
GRANT EXECUTE FOR MODELS
WHEN condition_expression;
```

The `EXCEPT` clause is optional. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

### Row Filter / Column Mask Policy Syntax

The exact syntax varies by policy type, but all support `TO` and optional `EXCEPT`. A representative structure is:

```sql
CREATE ... POLICY ... (UDF)
TO `principal1` [, `principal2` ...]
[EXCEPT `principal1` [, `principal2` ...]];
```

^[best-practices-for-abac-policies-databricks-on-aws.md]

## Best Practices

- **Use groups in `TO` and `EXCEPT`, not individual users.** Adding or removing users from a group named in a policy changes who the policy applies to without editing the policy itself. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Use `TO` and `EXCEPT` instead of complex UDF logic** where possible, to keep policies simple and auditable. ^[best-practices-for-abac-policies-databricks-on-aws.md]
- **For GRANT policies**, because they do not support UDFs, `TO` and `EXCEPT` are the only way to target principals. Plan your group structure accordingly. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Example

The following GRANT policy grants `EXECUTE` on foundation models in `system.ai` to `data_scientists`, except `contractors`:

```sql
CREATE POLICY grant_anthropic_foundation_models
ON SCHEMA system.ai
TO `data_scientists`
EXCEPT `contractors`
GRANT EXECUTE FOR MODELS
WHEN has_tag_value('ai.model_creator', 'anthropic');
```

^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Related Concepts

- [ABAC GRANT Policy](/concepts/abac-grant-policy.md) – Attribute-based grants using `TO`/`EXCEPT` for principal targeting
- [Row Filter Policies](/concepts/row-filter-policies.md) – ABAC policies that filter rows, typically using `TO`/`EXCEPT`
- [Column Mask Policies](/concepts/column-mask-policies.md) – ABAC policies that mask columns, typically using `TO`/`EXCEPT`
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) – The overarching access control model
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer that supports ABAC policies

## Sources

- best-practices-for-abac-policies-databricks-on-aws.md
- abac-grant-policies-for-models-beta-databricks-on-aws.md

# Citations

1. [best-practices-for-abac-policies-databricks-on-aws.md](/references/best-practices-for-abac-policies-databricks-on-aws-716fb4af.md)
2. [abac-grant-policies-for-models-beta-databricks-on-aws.md](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)

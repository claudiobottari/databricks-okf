---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d7bf7c0618185f7cbd46ca8beb50a29cb30e54f88b78e201647c514662dabde7
  pageDirectory: concepts
  sources:
    - best-practices-for-abac-policies-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - to-and-except-clauses-for-principal-targeting
    - EXCEPT Clauses for Principal Targeting and TO
    - TAECFPT
  citations:
    - file: best-practices-for-abac-policies-databricks-on-aws.md
title: TO and EXCEPT Clauses for Principal Targeting
description: Using TO and EXCEPT clauses in row filter and column mask policies to define which principals the policy applies to
tags:
  - data-governance
  - abac
  - policy-design
  - unity-catalog
timestamp: "2026-06-19T22:13:37.587Z"
---

# TO and EXCEPT Clauses for Principal Targeting

The **TO and EXCEPT clauses** are mechanisms used in [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies on Databricks to define which users and groups a policy applies to. These clauses simplify policy logic by keeping the underlying user-defined function (UDF) code clean and focused on data filtering, rather than identity management. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Purpose

For [row filter](/concepts/row-filter-policies.md) and column mask policies, the `TO` and `EXCEPT` clauses control principal targeting directly on the policy definition. This approach isolates identity-based logic from data transformation logic, making policies easier to maintain and audit. The `EXCEPT` clause is particularly useful for excluding specific users from a policy entirely, so they are not subject to any filtering or masking. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Relationship to UDF Logic

Using `TO` and `EXCEPT` is the recommended approach for principal targeting because it keeps the UDF logic simple. When complex conditional logic is required, identity functions like `is_account_group_member()` inside UDFs remain a valid alternative, but the simpler clause-based approach should be preferred. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Usage in GRANT Policies (Beta)

For [ABAC GRANT Policies](/concepts/abac-grant-policy.md) (currently in Beta), `TO` and `EXCEPT` are the **only** mechanisms available for targeting principals. Unlike row filter and column mask policies, GRANT policies do not use UDFs at all, so these clauses serve as the exclusive way to define which users and groups receive the granted privileges. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Best Practices

- Prefer `TO` and `EXCEPT` over identity functions in UDFs whenever possible to maintain simpler, more auditable policies. ^[best-practices-for-abac-policies-databricks-on-aws.md]
- Use the `EXCEPT` clause to exempt specific users (such as data stewards or auditors) from filtering or masking rules. ^[best-practices-for-abac-policies-databricks-on-aws.md]
- When auditing access, check both direct grants and ABAC GRANT policies together, as a user's effective privileges on a data object are the union of both. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Related Concepts

- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md)
- [ABAC GRANT Policies](/concepts/abac-grant-policy.md)
- [Row Filter Policies](/concepts/row-filter-policies.md)
- [Column Mask Policies](/concepts/column-mask-policies.md)
- [Principal targeting approaches](/concepts/toexcept-principal-targeting-in-abac.md)
- Best practices for ABAC policies

## Sources

- best-practices-for-abac-policies-databricks-on-aws.md

# Citations

1. [best-practices-for-abac-policies-databricks-on-aws.md](/references/best-practices-for-abac-policies-databricks-on-aws-716fb4af.md)

---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ccb9fc5fb8743ec538329367276ff137f0f0c1c9fc83f7de750e79dd92c9e9e3
  pageDirectory: concepts
  sources:
    - performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - principal-targeting-in-abac-policies-toexcept-vs-identity-functions
    - PTIAPTVIF
  citations:
    - file: performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md
title: "Principal targeting in ABAC policies: TO/EXCEPT vs identity functions"
description: "Two approaches for specifying which principals a policy applies to: using TO/EXCEPT clauses (simpler, eliminates UDF execution for exempt users) or identity functions like current_user() and is_account_group_member() inside the UDF (flexible, resolved once per query, not per row)."
tags:
  - abac-policies
  - principal-targeting
  - unity-catalog
timestamp: "2026-06-19T19:54:27.427Z"
---

# Principal targeting in ABAC policies: TO/EXCEPT vs identity functions

**Principal targeting in ABAC policies** refers to the decision point when writing an ABAC policy on Databricks where you choose between using the policy's built-in `TO`/`EXCEPT` clauses or embedding identity functions like `current_user()` and `is_account_group_member()` inside the policy's User-Defined Function (UDF). The choice affects both policy performance and maintainability. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Recommended approach: TO/EXCEPT clauses

In general, use the policy's `TO`/`EXCEPT` clauses to define which principals a policy applies to. This keeps the policy definition simpler and the UDF focused on data transformation, filtering, or masking. The `EXCEPT` clause eliminates the policy entirely for exempt users, which means no UDF execution for those users. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

Using `EXCEPT` has a performance advantage beyond simplicity: when a user is exempted, the `SecureView` barrier that [Row Filter and Column Mask Policies](/concepts/row-filter-policies.md) introduce is removed entirely for that user. This restores full [predicate pushdown](/concepts/selective-caching-with-predicate-pushdown.md) and partition pruning, which are otherwise blocked by the barrier. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Alternative approach: identity functions in UDFs

When the conditional logic is too complex for the policy's principal clauses, identity functions inside the UDF are a possible alternative. These functions are resolved once during query analysis, not per row. Multiple calls to identity functions like `is_account_group_member()` with different group arguments result in a single Unity Catalog API call, so the performance impact is typically minimal. ^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

The following UDF is efficient because it relies only on identity functions, which are resolved once during query analysis:

```sql
CREATE OR REPLACE FUNCTION rowfilter() RETURNS BOOLEAN
RETURN
  CASE
    WHEN is_account_group_member('auditors') OR is_account_group_member('external-auditors') THEN true
    WHEN is_account_group_member('low-privileged') THEN false
    WHEN session_user() = 'admin@organization.com' THEN true
    ELSE false
  END;
```

^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

In contrast, the following UDF is slower because it encodes privileges in a secondary table, which requires an additional table lookup:

```sql
CREATE OR REPLACE FUNCTION rowfilter() RETURNS BOOLEAN
RETURN
  CASE WHEN EXISTS(SELECT 1 FROM access_lease WHERE user = session_user()) THEN true
  ELSE false
  END;
```

^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Decision guide

| Scenario | Recommendation |
|---|---|
| Simple group membership checks | Use `TO`/`EXCEPT` clauses — simpler and faster |
| Exempting certain users from the policy entirely | Use `EXCEPT` — removes UDF execution and restores predicate pushdown |
| Complex logic combining multiple groups, roles, or user-specific rules | Use identity functions in the UDF — they resolve once per query, not per row |
| Privileges stored in a lookup table | Use identity functions if necessary, but keep the lookup table small enough for broadcast hash join |

^[performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Related concepts

- ABAC policies — Attribute-based access control for Unity Catalog
- [Row Filter and Column Mask Policies](/concepts/row-filter-policies.md) — The policy types that execute UDFs at query time
- [GRANT Policies (Beta)](/concepts/grant-policies-beta.md) — An alternative that does not execute UDFs
- Predicate pushdown — Performance optimization affected by the SecureView barrier
- SecureView barrier — The protection mechanism that can block query optimizations
- User-Defined Function (UDF) — The function executed per row or per column value

## Sources

- performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md

# Citations

1. [performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws.md](/references/performance-considerations-for-row-filter-and-column-mask-policies-databricks-on-aws-b415eba9.md)

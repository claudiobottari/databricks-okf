---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4a2cbb9440c3fa73cf3c7ef3a0bcfbf8566d95793276d5d122f502a0a01c3c58
  pageDirectory: concepts
  sources:
    - best-practices-for-abac-policies-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - toexcept-principal-targeting-in-abac
    - TPTIA
    - Principal targeting approaches
  citations:
    - file: best-practices-for-abac-policies-databricks-on-aws.md
title: TO/EXCEPT Principal Targeting in ABAC
description: Using TO and EXCEPT clauses in row filter, column mask, and GRANT policies to define which users and groups a policy applies to
tags:
  - abac
  - principal-targeting
  - unity-catalog
  - access-control
timestamp: "2026-06-19T14:09:22.854Z"
---

# TO/EXCEPT Principal Targeting in ABAC

**TO/EXCEPT Principal Targeting** refers to the mechanism in [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies within [Unity Catalog](/concepts/unity-catalog.md) that defines which users and groups a policy applies to (or excludes from) using the `TO` and `EXCEPT` clauses. This approach keeps policy logic simple by separating principal targeting from condition logic.

## Overview

In ABAC policies, the `TO` clause specifies which principals the policy applies to, while the `EXCEPT` clause excludes specific principals from the policy entirely. This is the preferred method for targeting principals in row filter, column mask, and GRANT policies. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## How TO/EXCEPT Works

The `TO` clause defines the set of users, service principals, or groups that are subject to the policy. The `EXCEPT` clause removes specific principals from that set, so they are not subject to any filtering, masking, or access restrictions imposed by the policy. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Benefits of TO/EXCEPT

### Simplified UDF Logic

For [row filter](/concepts/row-filter-policies.md) and column mask policies, using `TO` and `EXCEPT` keeps UDF logic simple by separating principal targeting from the filter or mask conditions. This avoids embedding complex identity checks inside user-defined functions. ^[best-practices-for-abac-policies-databricks-on-aws.md]

### Exclusive Mechanism for GRANT Policies

For [ABAC GRANT Policies](/concepts/abac-grant-policy.md), `TO` and `EXCEPT` are the only mechanisms for targeting principals, because GRANT policies do not use UDFs. ^[best-practices-for-abac-policies-databricks-on-aws.md]

### Alternatives

When more complex conditional logic is required beyond simple inclusion/exclusion, identity functions like `is_account_group_member()` inside UDFs remain a valid option for row filter and column mask policies. However, `TO` and `EXCEPT` should be preferred whenever possible. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Best Practices

- **Prefer TO/EXCEPT over UDF-based identity checks.** This keeps UDF logic simple and makes policies easier to audit and maintain. ^[best-practices-for-abac-policies-databricks-on-aws.md]
- **Audit both direct grants and ABAC GRANT policies together.** A user's effective privileges are the union of both direct grants and GRANT policies, so reviewing only one surface can hide unintended permissions. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Related Concepts

- [ABAC GRANT Policies](/concepts/abac-grant-policy.md) — GRANT policies that use TO/EXCEPT for principal targeting
- [Row Filter Policies](/concepts/row-filter-policies.md) — Policies that restrict data content, often using TO/EXCEPT
- [Column Mask Policies](/concepts/column-mask-policies.md) — Policies that mask sensitive columns, using TO/EXCEPT
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance platform that implements ABAC
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — The broader access control model

## Sources

- best-practices-for-abac-policies-databricks-on-aws.md

# Citations

1. [best-practices-for-abac-policies-databricks-on-aws.md](/references/best-practices-for-abac-policies-databricks-on-aws-716fb4af.md)
